"""Adapter tests against recorded payloads. No network."""
import json
import pathlib
import sys
from unittest.mock import Mock, patch

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from src import providers

FIX = pathlib.Path(__file__).parent / "fixtures"


def _cfg(pid, adapter, url="https://example.com"):
    return {"id": pid, "name": pid.title(), "category": "test",
            "adapter": adapter, "url": url}


def test_statuspage_normalizes():
    payload = json.loads((FIX / "statuspage.json").read_text())
    with patch.object(providers, "_get", return_value=Mock(json=lambda: payload)):
        out = providers.statuspage_adapter(_cfg("github", "statuspage"))
    assert out
    for i in out:
        assert i.incident_id and i.title
        assert i.severity_rank in (0, 1, 2, 3)
        if i.resolved_at:
            assert i.duration_minutes is not None and i.duration_minutes >= 0


def test_gcp_normalizes():
    payload = json.loads((FIX / "gcp.json").read_text())
    with patch.object(providers, "_get", return_value=Mock(json=lambda: payload)):
        out = providers.gcp_adapter(_cfg("gcp", "gcp"))
    assert out
    assert all(i.provider_id == "gcp" for i in out)


def test_azure_empty_channel_is_not_an_error():
    """Azure returns a well-formed empty feed when nothing is broken."""
    raw = (FIX / "azure.xml").read_bytes()
    with patch.object(providers, "_get", return_value=Mock(content=raw)):
        out = providers.azure_rss_adapter(_cfg("azure", "azure_rss"))
    assert isinstance(out, list)


def test_provider_failure_is_isolated():
    """One dead vendor must not abort the run."""
    with patch.object(providers, "_get", side_effect=RuntimeError("feed down")):
        assert providers.fetch(_cfg("x", "statuspage")) == []


def test_unknown_adapter_returns_empty():
    assert providers.fetch(_cfg("x", "nonexistent")) == []


@pytest.mark.parametrize("sev,rank", [("none",0),("minor",1),("major",2),("critical",3)])
def test_severity_scale(sev, rank):
    assert providers.SEVERITY_MAP[sev] == rank


@pytest.mark.parametrize("raw,expect_utc_hour", [
    ("Thu, 30 Apr 2026 00:25:54 PDT", 7),   # PDT = UTC-7
    ("Tue, 03 Mar 2026 08:40:00 PST", 16),  # PST = UTC-8
    ("Mon, 01 Jun 2026 12:00:00 UTC", 12),
])
def test_named_timezone_abbreviations(raw, expect_utc_hour):
    """strptime %Z only handles the local machine's names; AWS sends Pacific."""
    parsed = providers._parse_ts(raw)
    assert parsed is not None, f"failed to parse {raw!r}"
    assert parsed.hour == expect_utc_hour
