# Roadmap

## Done

**Phase 1 — Foundation**
Provider registry with adapter dispatch. Adapters for Statuspage (22
providers), GCP, Azure RSS, AWS RSS. Normalized schema with an ordinal
severity scale. Corpus dedup, daily deltas, derived metrics.

**Phase 2 — Correctness**
31 tests over recorded fixtures, no network. Ruff lint. CI on push and PR,
skipping `data/` and `docs/` so ingest commits do not re-run tests against
unchanged code. Statuspage `/history.json` backfill: corpus 1074 → 22,284
records spanning 2019–2026.

Five real bugs found and fixed along the way, each now covered by a
regression test:

| Bug | Effect |
| --- | --- |
| Same-day delta overwritten | Second run erased the first run's audit trail |
| `date.today()` local time | IST box and UTC runners disagreed on the date before 05:30 IST |
| Incident filed under end month | Records dated 2027-01-01 in a corpus built 2026-07-31 |
| `strptime` `%Z` with PDT/PST | All 36 AWS records had a null `created_at` |
| `status.zoom.us` ignores `?page` | 128 records multiplied to 1536 |

**Phase 3 — Published site**
MkDocs Material on GitHub Pages. Provider comparison table, methodology page
documenting collection, thresholds and known limitations.

## Next

**Phase 4 — Query surface**
SQLite export published as a release artifact. Parquet export. Datasette
instance for ad-hoc SQL.

**Phase 5 — AWS MTTR**
Pair issue and resolution items per service and region so AWS contributes
durations, not just counts. The largest remaining data gap.

**Phase 6 — Analysis**
Day-of-week and time-of-day distribution. Correlated-incident detection —
whether one provider's incidents co-occur with another's. Written up with the
method and its failure modes stated, not just the result.

**Phase 7 — Incident classification**
Rule-based classifier over titles: networking, capacity, deploy, dependency,
auth, storage. Hand-label a sample as ground truth and publish precision and
recall including where it fails.

**Phase 8 — Alerting**
Configurable watch rules, webhook notifier, Terraform module so others can
deploy an instance.

**Phase 9 — Hardening**
CONTRIBUTING, issue templates, Dependabot, CodeQL. Architecture write-up.

## Operating notes

The ingest commits only when a provider published something. There is
deliberately no fallback that commits on a quiet day — the history reflects
real upstream activity, and the gaps are accurate.

Backdated commits are out of scope. Rewriting author dates to fabricate
history is falsification rather than automation, and the GitHub API exposes
authored and pushed dates separately, so it does not survive inspection.
