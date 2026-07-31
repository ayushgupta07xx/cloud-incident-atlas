"""Derived reliability metrics over the accumulated incident corpus.

This is where the dataset stops being a scrape and starts being a
product: MTTR, incident frequency, severity mix, and category rollups
that nobody publishes across vendors in one place.
"""

from __future__ import annotations

import datetime as dt
import statistics
from collections import Counter, defaultdict
from typing import Any

# Statistical reporting thresholds. A p90 over four samples is just the
# maximum with extra steps; publishing it next to a p90 over fifty implies a
# comparability that isn't there. Below these counts we report None and the
# digest renders an em dash.
MIN_N_MEDIAN = 5
MIN_N_PERCENTILE = 10


def _percentile(values: list[float], pct: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    k = (len(ordered) - 1) * pct
    lo, hi = int(k), min(int(k) + 1, len(ordered) - 1)
    return round(ordered[lo] + (ordered[hi] - ordered[lo]) * (k - lo), 1)


def provider_stats(incidents: list[dict[str, Any]]) -> dict[str, Any]:
    """Per-provider reliability summary."""
    by_provider: dict[str, list[dict]] = defaultdict(list)
    for inc in incidents:
        by_provider[inc["provider_id"]].append(inc)

    out = {}
    for pid, records in by_provider.items():
        durations = [
            r["duration_minutes"]
            for r in records
            if r.get("duration_minutes") is not None
        ]
        severities = Counter(r["severity"] for r in records)

        out[pid] = {
            "provider_name": records[0]["provider_name"],
            "category": records[0]["category"],
            "incident_count": len(records),
            "resolved_count": sum(1 for r in records if r["status"] == "resolved"),
            "open_count": sum(1 for r in records if r["status"] != "resolved"),
            "resolved_with_duration": len(durations),
            "mttr_minutes_mean": (
                round(statistics.fmean(durations), 1)
                if len(durations) >= MIN_N_MEDIAN else None
            ),
            "mttr_minutes_median": (
                round(statistics.median(durations), 1)
                if len(durations) >= MIN_N_MEDIAN else None
            ),
            "mttr_minutes_p90": (
                _percentile(durations, 0.90)
                if len(durations) >= MIN_N_PERCENTILE else None
            ),
            "longest_incident_minutes": round(max(durations), 1) if durations else None,
            "stats_note": (
                None if len(durations) >= MIN_N_PERCENTILE
                else f"insufficient sample (n={len(durations)}) for percentile reporting"
            ),
            "severity_mix": dict(severities),
            "mean_severity_rank": round(
                statistics.fmean([r["severity_rank"] for r in records]), 2
            ),
        }
    return dict(sorted(out.items()))


def category_stats(incidents: list[dict[str, Any]]) -> dict[str, Any]:
    """Rollup by vendor category (cloud / cdn / data / devtools / observability)."""
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for inc in incidents:
        by_cat[inc["category"]].append(inc)

    return {
        cat: {
            "incident_count": len(records),
            "providers": len({r["provider_id"] for r in records}),
            "major_or_worse": sum(1 for r in records if r["severity_rank"] >= 2),
        }
        for cat, records in sorted(by_cat.items())
    }


def recent_window(incidents: list[dict[str, Any]], days: int = 30) -> dict[str, Any]:
    """Trailing-window view — the part that actually changes day to day."""
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)
    recent = []
    for inc in incidents:
        created = inc.get("created_at")
        if not created:
            continue
        try:
            if dt.datetime.fromisoformat(created) >= cutoff:
                recent.append(inc)
        except ValueError:
            continue

    return {
        "window_days": days,
        "incident_count": len(recent),
        "by_provider": dict(
            Counter(r["provider_id"] for r in recent).most_common()
        ),
        "major_or_worse": sum(1 for r in recent if r["severity_rank"] >= 2),
    }


def build_summary(incidents: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "total_incidents": len(incidents),
        "providers_tracked": len({i["provider_id"] for i in incidents}),
        "last_30_days": recent_window(incidents, 30),
        "last_90_days": recent_window(incidents, 90),
        "by_category": category_stats(incidents),
        "by_provider": provider_stats(incidents),
    }
