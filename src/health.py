"""Provider drift detection.

The ingest deliberately isolates provider failures so one dead feed cannot
abort a run. The cost is that a provider which changes its schema degrades
silently: it returns zero records, the run succeeds, and the corpus quietly
stops growing for that vendor.

This compares each run against a rolling baseline and reports providers that
have gone quiet in a way their history does not explain.
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
BASELINE = DATA / "baseline.json"

# A provider that historically returns records but now returns none for this
# many consecutive runs is treated as broken rather than quiet.
ZERO_RUN_THRESHOLD = 3

# Providers that legitimately return zero. Azure publishes only active
# incidents; an empty feed is the correct response to a healthy cloud.
EXPECTED_ZERO = {"azure"}


def load_baseline() -> dict:
    if not BASELINE.exists():
        return {"providers": {}, "updated_at": None}
    return json.loads(BASELINE.read_text())


def update(counts: dict[str, int]) -> tuple[dict, list[str]]:
    """Fold this run's counts into the baseline; return (baseline, alerts)."""
    base = load_baseline()
    providers = base.get("providers", {})
    alerts: list[str] = []

    for pid, count in counts.items():
        entry = providers.setdefault(
            pid, {"max_seen": 0, "consecutive_zero": 0, "last_nonzero": None}
        )

        if count > 0:
            entry["max_seen"] = max(entry["max_seen"], count)
            entry["consecutive_zero"] = 0
            entry["last_nonzero"] = dt.datetime.now(dt.timezone.utc).isoformat()
        else:
            entry["consecutive_zero"] += 1

        if pid in EXPECTED_ZERO:
            continue

        if (
            entry["consecutive_zero"] >= ZERO_RUN_THRESHOLD
            and entry["max_seen"] > 0
        ):
            alerts.append(
                f"{pid}: returned 0 records for {entry['consecutive_zero']} "
                f"consecutive runs (previously returned up to "
                f"{entry['max_seen']}); last non-empty "
                f"{entry['last_nonzero'] or 'never'}"
            )

    base["providers"] = providers
    base["updated_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    return base, alerts


def write(base: dict) -> None:
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    BASELINE.write_text(json.dumps(base, indent=2, sort_keys=True) + "\n")
