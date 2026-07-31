# Methodology

## Collection

Twenty-five providers, six days a week. Twenty-two run Atlassian Statuspage and
share a uniform v2 JSON API; GCP, Azure and AWS have bespoke adapters. A
provider that fails is skipped, not fatal — one dead feed cannot take down a
run. If every provider fails the run aborts without writing, so a network
partition cannot truncate the corpus.

## Backfill

The v2 API returns at most 50 incidents. `/history.json` pages by month and
uses the same id space, so historical records merge on the existing key without
duplicating anything the daily run holds. That endpoint has a poorer schema: no
ISO timestamps, no components, no status vocabulary. Dates are parsed from
display strings; seven format variants covered 3144 of 3144 sampled records.
Unparseable input produces no record rather than a guessed date.

## Normalization

Vendor severity vocabularies map onto one ordinal scale (none/maintenance 0,
minor 1, major 2, critical 3). Timestamps are converted to UTC. Duration is
computed only where both a start and a resolution exist.

## Statistical thresholds

Medians require n≥5, percentiles n≥10. A p90 over four samples is the maximum
wearing a suit; publishing it beside a p90 over fifty implies a comparability
that is not there.

## Known limitations

- **AWS** contributes incident counts but no MTTR. Its RSS emits one item per
  update rather than per incident, so durations require pairing issue and
  resolution items per service and region.
- **Azure** publishes only currently-active incidents. An empty feed means
  nothing is broken, not that collection failed. There is no public Azure
  historical feed.
- **Fastly** is excluded: its status page returns 403 to automated clients.
- Scheduled maintenance appears alongside unplanned incidents where a vendor
  files it as an incident. Severity `maintenance` and `none` both rank 0.

## Reproducing

```bash
pip install -r requirements.txt -r requirements-dev.txt
python -m src.ingest --dry-run
pytest tests -q
```
