"""Timestamp parsing for the Statuspage history endpoint."""
import datetime as dt
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from src.history import parse_timestamp, strip_tags


def test_strips_var_tags():
    raw = "Jul <var data-var='date'>30</var>, <var data-var='time'>09:07</var> UTC"
    assert strip_tags(raw) == "Jul 30, 09:07 UTC"


@pytest.mark.parametrize("text,year,start,end", [
    ("Jul 30, 09:07 - 10:12 UTC", 2026, (2026, 7, 30, 9, 7), (2026, 7, 30, 10, 12)),
    ("Jul 19, 23:34 - Jul 20, 04:44 UTC", 2026, (2026, 7, 19, 23, 34), (2026, 7, 20, 4, 44)),
    ("Jul 31, 00:00 UTC", 2026, (2026, 7, 31, 0, 0), None),
])
def test_utc_variants(text, year, start, end):
    s, e = parse_timestamp(text, year)
    assert (s.year, s.month, s.day, s.hour, s.minute) == start
    assert (e is None) if end is None else (e.year, e.month, e.day, e.hour, e.minute) == end


def test_edt_converts_to_utc():
    s, e = parse_timestamp("Jul 30, 03:44 - 04:27 EDT", 2026)
    assert (s.hour, s.minute) == (7, 44)   # EDT = UTC-4
    assert (e.hour, e.minute) == (8, 27)
    assert s.tzinfo == dt.timezone.utc


def test_est_converts_to_utc():
    s, _ = parse_timestamp("Feb 18, 14:30 - 15:37 EST", 2026)
    assert (s.hour, s.minute) == (19, 30)  # EST = UTC-5


def test_year_rollover():
    s, e = parse_timestamp("Dec 31, 23:00 - Jan 1, 02:00 UTC", 2025)
    assert s.year == 2025 and e.year == 2026
    assert (e - s).total_seconds() == 3 * 3600


def test_duration_is_positive():
    s, e = parse_timestamp("Jul 19, 23:34 - Jul 20, 04:44 UTC", 2026)
    assert (e - s).total_seconds() == 5 * 3600 + 10 * 60


@pytest.mark.parametrize("bad", ["", "not a timestamp", "Foo 99, 09:07 UTC",
                                 "Jul 30, 09:07 - 10:12 XYZ", "Feb 30, 01:00 UTC"])
def test_unparseable_returns_none(bad):
    assert parse_timestamp(bad, 2026) == (None, None)


def test_fetch_history_shape(monkeypatch):
    """Records must match the corpus schema so they merge cleanly."""
    from src import history

    payload = {"months": [{"year": "2026", "name": "July", "incidents": [
        {"code": "abc123", "name": "Test incident", "impact": "major",
         "timestamp": "Jul 30, 09:07 - 10:12 UTC"}]}]}

    class R:
        def raise_for_status(self): pass
        def json(self): return payload

    import requests
    monkeypatch.setattr(requests, "get", lambda *a, **k: R())
    out = history.fetch_history(
        {"id": "t", "name": "T", "category": "c", "url": "https://x"}, max_pages=1)

    assert len(out) == 1
    r = out[0]
    assert r["incident_id"] == "abc123"
    assert r["duration_minutes"] == 65.0
    assert r["severity_rank"] == 2
    assert r["source"] == "history"
    assert set(r) >= {"provider_id", "created_at", "resolved_at", "severity_rank"}


def test_cross_year_incident_uses_previous_year_for_start():
    """Filed under January 2026 but starts Dec 31 -> start is 2025."""
    s, e = parse_timestamp("Dec 31, 18:15 - Jan 1, 06:17 UTC", 2026, filed_month=1)
    assert s.year == 2025 and (s.month, s.day) == (12, 31)
    assert e.year == 2026 and (e.month, e.day) == (1, 1)


def test_same_month_unaffected_by_filed_month():
    s, e = parse_timestamp("Jul 30, 09:07 - 10:12 UTC", 2026, filed_month=7)
    assert s.year == 2026 and e.year == 2026


def test_pagination_stops_when_months_repeat(monkeypatch):
    """A provider ignoring ?page must not multiply its records."""
    from src import history

    payload = {"months": [{"year": "2026", "name": "July", "incidents": [
        {"code": "x1", "name": "n", "impact": "minor",
         "timestamp": "Jul 30, 09:07 - 10:12 UTC"}]}]}

    class R:
        def raise_for_status(self): pass
        def json(self): return payload

    import requests
    monkeypatch.setattr(requests, "get", lambda *a, **k: R())
    out = history.fetch_history(
        {"id": "t", "name": "T", "category": "c", "url": "https://x"}, max_pages=12)
    assert len(out) == 1
