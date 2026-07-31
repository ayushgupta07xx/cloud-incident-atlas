"""Provider adapters.

Every adapter takes a provider config dict and returns a list of
normalized Incident records. The point of this module is that the
rest of the pipeline never knows or cares which vendor a record
came from.
"""

from __future__ import annotations

import datetime as dt
import logging
import re
import xml.etree.ElementTree as ET
from collections.abc import Callable
from dataclasses import asdict, dataclass, field
from typing import Any

import requests

log = logging.getLogger(__name__)

TIMEOUT = 25
UA = "cloud-incident-atlas/1.0 (+https://github.com/ayushgupta07xx/cloud-incident-atlas)"

# Vendor-specific severity vocabularies mapped onto one ordinal scale.
# strptime cannot resolve these; see _parse_ts.
NAMED_OFFSETS = {"UTC": 0, "GMT": 0, "EDT": -4, "EST": -5,
                 "PDT": -7, "PST": -8, "CDT": -5, "CST": -6,
                 "MDT": -6, "MST": -7}

SEVERITY_MAP = {
    "none": 0,
    "maintenance": 0,
    "minor": 1,
    "major": 2,
    "critical": 3,
}


@dataclass
class Incident:
    """One normalized incident, regardless of source vendor."""

    provider_id: str
    provider_name: str
    category: str
    incident_id: str
    title: str
    status: str
    severity: str
    severity_rank: int
    created_at: str | None
    updated_at: str | None
    resolved_at: str | None
    duration_minutes: float | None
    shortlink: str | None
    components: list[str] = field(default_factory=list)
    update_count: int = 0

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def _get(url: str) -> requests.Response:
    r = requests.get(url, timeout=TIMEOUT, headers={"User-Agent": UA})
    r.raise_for_status()
    return r


def _parse_ts(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    txt = value.strip().replace("Z", "+00:00")

    # strptime's %Z only accepts the *local* machine's abbreviations, so
    # "PDT"/"PST" parse on a US box and fail everywhere else. AWS emits
    # Pacific abbreviations; resolve them explicitly instead.
    tz_match = re.search(r"\b([A-Z]{3,4})\s*$", txt)
    if tz_match and tz_match.group(1) in NAMED_OFFSETS:
        offset = NAMED_OFFSETS[tz_match.group(1)]
        body = txt[: tz_match.start()].strip()
        for fmt in ("%a, %d %b %Y %H:%M:%S", "%d %b %Y %H:%M:%S"):
            try:
                # DTZ007 false positive: tzinfo is attached on the next line
                naive = dt.datetime.strptime(body, fmt)  # noqa: DTZ007
            except ValueError:
                continue
            aware = naive.replace(tzinfo=dt.timezone(dt.timedelta(hours=offset)))
            return aware.astimezone(dt.timezone.utc)

    for parser in (
        lambda s: dt.datetime.fromisoformat(s),
        lambda s: dt.datetime.strptime(s, "%a, %d %b %Y %H:%M:%S %z"),
        # %Z cannot recover an offset; _parse_ts assumes UTC for naive results
        lambda s: dt.datetime.strptime(s, "%a, %d %b %Y %H:%M:%S %Z"),  # noqa: DTZ007
    ):
        try:
            parsed = parser(txt)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except (ValueError, TypeError):
            continue
    log.debug("unparseable timestamp: %r", value)
    return None


def _iso(value: dt.datetime | None) -> str | None:
    return value.isoformat() if value else None


def _duration(start: dt.datetime | None, end: dt.datetime | None) -> float | None:
    if not start or not end:
        return None
    minutes = (end - start).total_seconds() / 60
    return round(minutes, 1) if minutes >= 0 else None


# --------------------------------------------------------------------------
# adapters
# --------------------------------------------------------------------------


def statuspage_adapter(cfg: dict[str, Any]) -> list[Incident]:
    """Atlassian Statuspage v2 API. Covers the large majority of vendors.

    /incidents.json returns at most 50 records. That caps *backfill*, not
    ongoing collection: anything new since the previous run falls inside the
    window. Deeper history needs /history.json, which pages by month.
    See ROADMAP Phase 2.
    """
    payload = _get(f"{cfg['url'].rstrip('/')}/api/v2/incidents.json").json()
    out: list[Incident] = []

    for raw in payload.get("incidents", []):
        created = _parse_ts(raw.get("created_at"))
        resolved = _parse_ts(raw.get("resolved_at"))
        severity = (raw.get("impact") or "none").lower()

        out.append(
            Incident(
                provider_id=cfg["id"],
                provider_name=cfg["name"],
                category=cfg["category"],
                incident_id=str(raw.get("id")),
                title=(raw.get("name") or "").strip(),
                status=raw.get("status") or "unknown",
                severity=severity,
                severity_rank=SEVERITY_MAP.get(severity, 1),
                created_at=_iso(created),
                updated_at=_iso(_parse_ts(raw.get("updated_at"))),
                resolved_at=_iso(resolved),
                duration_minutes=_duration(created, resolved),
                shortlink=raw.get("shortlink"),
                components=[
                    c.get("name", "") for c in (raw.get("components") or []) if c.get("name")
                ],
                update_count=len(raw.get("incident_updates") or []),
            )
        )
    return out


def gcp_adapter(cfg: dict[str, Any]) -> list[Incident]:
    """GCP publishes its own incident JSON with a different shape.

    Low record counts are expected and correct. GCP only publishes incidents
    it considers significant - 4 records spanning Feb-Jul 2026 at time of
    writing - but each record is large (~28KB) because it embeds its full
    update history.
    """
    payload = _get(f"{cfg['url'].rstrip('/')}/incidents.json").json()
    out: list[Incident] = []

    for raw in payload:
        created = _parse_ts(raw.get("begin"))
        resolved = _parse_ts(raw.get("end")) if raw.get("end") else None
        severity = (raw.get("severity") or "medium").lower()
        rank = {"low": 1, "medium": 2, "high": 3}.get(severity, 1)

        out.append(
            Incident(
                provider_id=cfg["id"],
                provider_name=cfg["name"],
                category=cfg["category"],
                incident_id=str(raw.get("id") or raw.get("number")),
                title=(raw.get("external_desc") or "").strip(),
                status="resolved" if raw.get("end") else "investigating",
                severity=severity,
                severity_rank=rank,
                created_at=_iso(created),
                updated_at=_iso(_parse_ts(raw.get("modified"))),
                resolved_at=_iso(resolved),
                duration_minutes=_duration(created, resolved),
                shortlink=raw.get("uri"),
                components=sorted(
                    {p.get("title", "") for p in (raw.get("affected_products") or [])} - {""}
                ),
                update_count=len(raw.get("updates") or []),
            )
        )
    return out


def azure_rss_adapter(cfg: dict[str, Any]) -> list[Incident]:
    """Azure publishes RSS only, and only for *currently active* incidents.

    An empty <channel> is the normal, correct response when Azure has nothing
    broken. It is not a parse failure. Verified 2026-07-31: well-formed RSS,
    zero <item> elements, during clear status.

    Do not "fix" this by hunting for another endpoint - Azure publishes no
    public historical incident feed. Consequence: Azure contributes little to
    the corpus outside active outages.
    """
    root = ET.fromstring(_get(cfg["url"]).content)
    out: list[Incident] = []

    for item in root.iterfind(".//item"):
        title = (item.findtext("title") or "").strip()
        published = _parse_ts(item.findtext("pubDate"))
        guid = (item.findtext("guid") or title).strip()

        out.append(
            Incident(
                provider_id=cfg["id"],
                provider_name=cfg["name"],
                category=cfg["category"],
                incident_id=guid,
                title=title,
                status="reported",
                severity="minor",
                severity_rank=1,
                created_at=_iso(published),
                updated_at=_iso(published),
                resolved_at=None,
                duration_minutes=None,
                shortlink=item.findtext("link"),
                components=[c.text for c in item.iterfind("category") if c.text],
            )
        )
    return out


def aws_adapter(cfg: dict[str, Any]) -> list[Incident]:
    """AWS RSS. Best-effort; AWS keeps changing this surface.

    KNOWN GAP: duration_minutes is always None for AWS. The RSS feed emits
    each incident update as a separate <item> rather than one item per
    incident, so computing MTTR requires pairing "issue" items with their
    matching "resolved" item per service and region. Not yet implemented -
    see ROADMAP Phase 2. AWS therefore contributes incident counts but no
    MTTR to the comparison table.
    """
    root = ET.fromstring(_get(f"{cfg['url'].rstrip('/')}/rss/all.rss").content)
    out: list[Incident] = []

    for item in root.iterfind(".//item"):
        title = (item.findtext("title") or "").strip()
        published = _parse_ts(item.findtext("pubDate"))
        resolved = "resolved" in title.lower() or "operating normally" in title.lower()

        out.append(
            Incident(
                provider_id=cfg["id"],
                provider_name=cfg["name"],
                category=cfg["category"],
                incident_id=(item.findtext("guid") or title).strip(),
                title=title,
                status="resolved" if resolved else "reported",
                severity="minor",
                severity_rank=1,
                created_at=_iso(published),
                updated_at=_iso(published),
                resolved_at=_iso(published) if resolved else None,
                duration_minutes=None,
                shortlink=item.findtext("link"),
            )
        )
    return out


ADAPTERS: dict[str, Callable[[dict[str, Any]], list[Incident]]] = {
    "statuspage": statuspage_adapter,
    "gcp": gcp_adapter,
    "azure_rss": azure_rss_adapter,
    "aws": aws_adapter,
}


def fetch(cfg: dict[str, Any]) -> list[Incident]:
    """Dispatch to the right adapter. Never raises: a dead vendor feed
    must not take down the whole run."""
    adapter = ADAPTERS.get(cfg["adapter"])
    if adapter is None:
        log.warning("no adapter registered for %s", cfg["adapter"])
        return []
    try:
        incidents = adapter(cfg)
        log.info("%-14s %3d incidents", cfg["id"], len(incidents))
        return incidents
    except Exception as exc:
        log.warning("%-14s FAILED: %s", cfg["id"], exc)
        return []
