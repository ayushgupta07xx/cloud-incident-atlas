# Cloud Incident Atlas

A normalized, continuously-updated dataset of public cloud and SaaS incidents,
with derived reliability metrics across vendors.

Every major provider publishes a status page. Almost none publish machine-readable
history in a comparable shape, and nobody publishes them side by side. This repo
ingests 13 providers daily, normalizes them into one schema, and computes MTTR,
incident frequency, and severity distributions you can actually compare.

## Why this exists

If you run on three clouds and six SaaS dependencies, "is this vendor reliable?"
is answerable only by scrolling nine separate status pages. This turns that into
a table.

## Architecture

```
providers.yaml ──> adapter dispatch ──> normalized Incident ──> corpus (dedup by key)
                   ├─ statuspage (10)                              │
                   ├─ gcp                                          ├─> summary.json  (metrics)
                   ├─ azure_rss                                    ├─> daily/*.json  (deltas)
                   └─ aws                                          └─> docs/index.md (digest)
```

Ten of thirteen providers run Atlassian Statuspage, which exposes a uniform v2
JSON API — so one adapter covers most of the surface, and bespoke feeds (GCP,
Azure RSS, AWS RSS) get their own. Adding a provider is a one-line change to
`providers.yaml`.

Provider fetches are isolated: a vendor that changes its feed shape or goes down
degrades that provider only, it does not fail the run. If *every* provider fails,
the run aborts without writing, so a network partition can't truncate the corpus.

## Data

| File | Contents |
| --- | --- |
| `data/incidents.json` | Canonical deduplicated corpus |
| `data/summary.json` | Derived metrics: MTTR mean/median/p90, severity mix, category rollups |
| `data/daily/YYYY-MM-DD.json` | That day's new and changed incidents |
| `docs/index.md` | Human-readable digest |

Schema per incident: provider, category, id, title, status, severity (normalized
to a 0–3 ordinal across vendor vocabularies), created/updated/resolved timestamps,
duration, affected components, update count.

## Automation disclosure

**This repository commits automatically.** A scheduled GitHub Actions workflow
(`.github/workflows/daily-ingest.yml`) runs six days a week, fetches the provider
feeds, and commits under my account identity when upstream data has changed.

- Commits titled `data: ingest N new, M updated incidents` are machine-generated.
  Each carries a link to the Actions run that produced it and a
  `Co-authored-by: github-actions[bot]` trailer.
- Every other commit is hand-written work: adapters, metrics, analysis, docs.
- If no provider published anything new, the workflow commits nothing. The history
  reflects real upstream activity, not a heartbeat.

I'd rather you know this up front than discover it and wonder. The pipeline is the
interesting part of the project; hiding that it runs would be both dishonest and
counterproductive.

## Running locally

```bash
pip install -r requirements.txt
python -m src.ingest --dry-run    # fetch and report, write nothing
python -m src.ingest              # full run
```

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## License

MIT for the code. The incident data is aggregated from public vendor status pages
and belongs to the respective vendors.
