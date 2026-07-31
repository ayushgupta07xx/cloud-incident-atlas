"""Same-day delta merge. Regression guard for the bug in 07724fc."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from src import ingest


def _inc(pid, iid):
    return {"provider_id": pid, "incident_id": iid, "title": f"t-{iid}",
            "provider_name": pid, "category": "test", "status": "resolved",
            "severity": "minor", "severity_rank": 1}


def test_second_run_preserves_first(tmp_path, monkeypatch):
    monkeypatch.setattr(ingest, "DATA", tmp_path)
    (tmp_path / "daily").mkdir()
    day = "2026-01-01"

    first = ingest.merge_daily(day, [_inc("a", "1"), _inc("a", "2")], [])
    (tmp_path / "daily" / f"{day}.json").write_text(json.dumps(first))
    assert first["runs"] == 1 and len(first["new"]) == 2

    second = ingest.merge_daily(day, [_inc("a", "3")], [])
    assert second["runs"] == 2
    assert len(second["new"]) == 3


def test_same_day_change_not_double_counted(tmp_path, monkeypatch):
    monkeypatch.setattr(ingest, "DATA", tmp_path)
    (tmp_path / "daily").mkdir()
    day = "2026-01-01"

    first = ingest.merge_daily(day, [_inc("a", "1")], [])
    (tmp_path / "daily" / f"{day}.json").write_text(json.dumps(first))

    second = ingest.merge_daily(day, [], [_inc("a", "1")])
    assert len(second["new"]) == 1
    assert len(second["changed"]) == 0
