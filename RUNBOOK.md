# Runbook

You are probably here because an issue was opened automatically. Everything
below assumes you have forgotten how this works, which is the expected state.

## Setup after a break

```bash
cd cloud-incident-atlas
git pull
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m src.ingest --dry-run   # fetch everything, write nothing
```

The dry run prints one line per provider. That output identifies the problem
in almost every case.

## Diagnosing by symptom

### "Ingest needs attention" issue, drift detail names a provider

That provider returned zero records for three consecutive runs after
previously returning data. Its feed changed shape.

```bash
python -m src.ingest --dry-run 2>&1 | grep -i -E "failed|  <provider> "
```

- **`FAILED: 404`** — the URL moved. Find the new status page, update the
  `url` in `providers.yaml`.
- **`FAILED: 403`** — a WAF is blocking automated clients. Do not work around
  it. Remove the provider from `providers.yaml` and record why, as was done
  for Fastly.
- **`0 incidents` with no error** — the JSON parsed but the shape changed.
  Inspect the raw payload:

```bash
python -c "
import requests, json
r = requests.get('<status-url>/api/v2/incidents.json', timeout=20,
                 headers={'User-Agent': 'cloud-incident-atlas/1.0'})
print(json.dumps(r.json(), indent=2)[:1500])"
```

Then adjust the adapter in `src/providers.py` and add a fixture test.

### Job failed outright

Every provider is wrapped in try/except, so a crash means something outside
the adapters. Usually a dependency. Check the run log for the traceback.

```bash
gh run view --log-failed --repo ayushgupta07xx/cloud-incident-atlas
```

### Commits stopped but no issue was opened

Check the workflow is still enabled:

```bash
gh workflow list --all --repo ayushgupta07xx/cloud-incident-atlas
gh workflow enable "Daily incident ingest" --repo ayushgupta07xx/cloud-incident-atlas
```

Public repos disable scheduled workflows after 60 days without repository
activity. The monthly Keepalive workflow should prevent this; if it has also
stopped, enable both.

### Commits happening every day with no real change

Something is writing a file that varies per run — a timestamp, a counter, a
dict iteration order. This happened once with `baseline.json`. Find it:

```bash
python -m src.ingest && cp data/baseline.json /tmp/a
python -m src.ingest && diff /tmp/a data/baseline.json
git diff --stat
```

The commit gate stages `data/incidents`, `data/daily` and `docs`, then tests
those for changes. Anything else must not be staged before that test.

## Adding a provider

One line in `providers.yaml` if it runs Atlassian Statuspage. Check first:

```bash
curl -s https://<status-domain>/api/v2/incidents.json | head -c 300
```

If that returns JSON with an `incidents` key, use `adapter: statuspage`.
Otherwise it needs a new adapter function and a fixture test.

## Before pushing anything

```bash
ruff check src tests && pytest tests -q
```

CI runs both and will reject a push that fails either.

## Things that are working as intended, not bugs

- **Azure returns 0 incidents.** It publishes only currently-active
  incidents. Empty means nothing is broken. It is exempt from drift alerts.
- **AWS has no MTTR.** Its RSS emits one item per update rather than per
  incident, so durations require pairing issue and resolution items. Known
  gap, documented in the methodology page.
- **Some providers show an em dash for p90.** Percentiles are suppressed
  below n=10 and medians below n=5.
- **A day with no commit.** The ingest commits only when a provider actually
  published something. Quiet days are real and the gaps are accurate.

## Design decisions that should not be reversed

- No fallback commit on quiet days. The history reflects real upstream
  activity; a heartbeat commit would make it fiction.
- No backdated commits. The API exposes authored and pushed dates separately,
  so fabricated history does not survive inspection.
- No WAF evasion. A provider that blocks automated clients gets removed.
- The automation stays documented in the README. Anyone reading the commit
  history should be able to tell which commits are machine-generated.
