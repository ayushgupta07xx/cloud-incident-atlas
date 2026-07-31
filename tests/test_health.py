"""Provider drift detection."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from src import health


def _fresh(tmp_path, monkeypatch):
    monkeypatch.setattr(health, "BASELINE", tmp_path / "baseline.json")


def test_healthy_provider_raises_nothing(tmp_path, monkeypatch):
    _fresh(tmp_path, monkeypatch)
    base, alerts = health.update({"github": 50})
    health.write(base)
    assert alerts == []
    assert base["providers"]["github"]["max_seen"] == 50


def test_alerts_only_after_threshold(tmp_path, monkeypatch):
    _fresh(tmp_path, monkeypatch)
    base, _ = health.update({"github": 50})
    health.write(base)

    for run in range(1, health.ZERO_RUN_THRESHOLD):
        base, alerts = health.update({"github": 0})
        health.write(base)
        assert alerts == [], f"alerted early on run {run}"

    base, alerts = health.update({"github": 0})
    assert len(alerts) == 1 and "github" in alerts[0]


def test_recovery_resets_counter(tmp_path, monkeypatch):
    _fresh(tmp_path, monkeypatch)
    base, _ = health.update({"github": 50})
    health.write(base)
    base, _ = health.update({"github": 0})
    health.write(base)
    base, _ = health.update({"github": 50})
    health.write(base)
    assert base["providers"]["github"]["consecutive_zero"] == 0


def test_azure_zero_is_not_drift(tmp_path, monkeypatch):
    """Azure publishes only active incidents; empty is correct."""
    _fresh(tmp_path, monkeypatch)
    base, _ = health.update({"azure": 3})
    health.write(base)
    for _ in range(health.ZERO_RUN_THRESHOLD + 2):
        base, alerts = health.update({"azure": 0})
        health.write(base)
    assert alerts == []


def test_never_seen_provider_does_not_alert(tmp_path, monkeypatch):
    """A provider that has never returned data is not 'broken'."""
    _fresh(tmp_path, monkeypatch)
    for _ in range(health.ZERO_RUN_THRESHOLD + 2):
        base, alerts = health.update({"newthing": 0})
        health.write(base)
    assert alerts == []
