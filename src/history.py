"""Statuspage /history.json backfill.

The history endpoint uses a different, poorer schema than the v2 API:
no ISO timestamps, no components, no status. Dates arrive as display
strings wrapped in HTML <var> tags, and the year lives on the parent
month object rather than the record.

Sampled 3088 records across three providers; seven format variants
cover 100%. See tests/test_history.py.
"""

from __future__ import annotations

import datetime as dt
import re

TIMEOUT_S = 25
USER_AGENT = "cloud-incident-atlas/1.0 (+https://github.com/ayushgupta07xx)"
SEVERITY_RANKS = {"none": 0, "maintenance": 0, "minor": 1, "major": 2, "critical": 3}

VAR_TAG = re.compile(r"<var[^>]*>(.*?)</var>")
MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}

# Statuspage renders a fixed abbreviation, so a static offset is correct here.
# Do not swap in a tz database lookup: the string already tells us which of
# EST/EDT applied on that date.
TZ_OFFSETS = {"UTC": 0, "GMT": 0, "EDT": -4, "EST": -5,
              "PDT": -7, "PST": -8, "CDT": -5, "CST": -6}

_HALF = re.compile(r"(?:([A-Z][a-z]{2})\s+(\d{1,2}),\s*)?(\d{1,2}):(\d{2})")


def strip_tags(raw: str) -> str:
    return VAR_TAG.sub(r"\1", raw or "").strip()


MONTH_NAMES = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11,
    "December": 12,
}


def parse_timestamp(
    raw: str, year: int, filed_month: int | None = None
) -> tuple[dt.datetime | None, dt.datetime | None]:
    """Parse a history timestamp into (start, end) UTC datetimes.

    `year` and `filed_month` come from the enclosing month object. Statuspage
    files an incident under the month it *ended*, so one that starts Dec 31
    and ends Jan 1 appears under January of the following year. Without
    `filed_month` the start silently gains a year - observed as records dated
    2026-12-31 and 2027-01-01 in a corpus built on 2026-07-31.

    Returns (None, None) on anything unrecognized rather than guessing: a
    wrong duration silently corrupts MTTR, which is worse than a missing one.
    """
    text = strip_tags(raw)
    if not text:
        return None, None

    tz_match = re.search(r"\b([A-Z]{3})\s*$", text)
    tz_name = tz_match.group(1) if tz_match else "UTC"
    if tz_name not in TZ_OFFSETS:
        return None, None
    tz = dt.timezone(dt.timedelta(hours=TZ_OFFSETS[tz_name]))
    body = text[: tz_match.start()].strip() if tz_match else text

    halves = [h.strip() for h in body.split(" - ")]
    parsed: list[dt.datetime] = []
    cur_month = None

    # An incident filed under month M that starts in a later month began in
    # the previous calendar year.
    base_year = year
    first = _HALF.search(halves[0])
    if not first:
        return None, None
    if filed_month and first.group(1) and MONTHS.get(first.group(1), 0) > filed_month:
        base_year = year - 1

    for half in halves:
        m = _HALF.search(half)
        if not m:
            return None, None
        mon_txt, day_txt, hh, mm = m.groups()
        if mon_txt:
            if mon_txt not in MONTHS:
                return None, None
            cur_month, day = MONTHS[mon_txt], int(day_txt)
        elif cur_month is not None and parsed:
            day = parsed[-1].day  # "09:07 - 10:12" means same day
        else:
            return None, None

        yr = base_year
        # December -> January rollover within one incident
        if parsed and cur_month < parsed[-1].month:
            yr = base_year + 1
        try:
            parsed.append(dt.datetime(yr, cur_month, day, int(hh), int(mm), tzinfo=tz))
        except ValueError:
            return None, None

    start = parsed[0].astimezone(dt.timezone.utc)
    end = parsed[1].astimezone(dt.timezone.utc) if len(parsed) > 1 else None
    if end and end < start:
        return start, None
    return start, end


def fetch_history(cfg: dict, max_pages: int = 12) -> list[dict]:
    """Backfill from /history.json.

    IDs match the v2 API (`code` == `id`), verified across the 50-record
    overlap window, so records merge into the corpus by the existing key
    and never duplicate what the daily ingest already holds.

    Fields absent from this endpoint are left empty rather than invented:
    no components, no status vocabulary, no update count. `source` marks
    the provenance so a later schema change can tell the two apart.
    """
    import requests

    out: list[dict] = []
    seen_months: set[tuple] = set()

    for page in range(1, max_pages + 1):
        try:
            resp = requests.get(
                f"{cfg['url'].rstrip('/')}/history.json",
                params={"page": page}, timeout=TIMEOUT_S,
                headers={"User-Agent": USER_AGENT},
            )
            resp.raise_for_status()
            months = resp.json().get("months", [])
        except Exception:
            break

        if not months:
            break

        # Some providers ignore ?page and return the same months every time
        # (observed: status.zoom.us returned 128 records 12x). Stop when a
        # page contributes no month we have not already read.
        ids = {(m.get("name"), m.get("year")) for m in months}
        if ids <= seen_months:
            break
        seen_months |= ids

        page_count = 0
        for month in months:
            try:
                year = int(month.get("year") or 0)
            except (TypeError, ValueError):
                continue
            if not year:
                continue

            filed_month = MONTH_NAMES.get(month.get("name", ""))

            for raw in month.get("incidents", []):
                start, end = parse_timestamp(
                    raw.get("timestamp", ""), year, filed_month)
                if start is None:
                    continue

                severity = (raw.get("impact") or "none").lower()
                duration = None
                if end:
                    duration = round((end - start).total_seconds() / 60, 1)

                out.append({
                    "provider_id": cfg["id"],
                    "provider_name": cfg["name"],
                    "category": cfg["category"],
                    "incident_id": str(raw.get("code")),
                    "title": (raw.get("name") or "").strip(),
                    "status": "resolved" if end else "unknown",
                    "severity": severity,
                    "severity_rank": SEVERITY_RANKS.get(severity, 1),
                    "created_at": start.isoformat(),
                    "updated_at": (end or start).isoformat(),
                    "resolved_at": end.isoformat() if end else None,
                    "duration_minutes": duration,
                    "shortlink": None,
                    "components": [],
                    "update_count": 0,
                    "source": "history",
                })
                page_count += 1

        del page_count

    return out
