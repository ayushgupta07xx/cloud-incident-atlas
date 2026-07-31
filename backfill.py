"""One-time historical backfill. Not part of the daily run."""
import json
import logging
import pathlib
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from src import metrics
from src.history import fetch_history

logging.basicConfig(level=logging.INFO, format="%(levelname)-7s %(message)s")
log = logging.getLogger("backfill")

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "data"

cfgs = [p for p in yaml.safe_load(open(ROOT / "providers.yaml"))["providers"]
        if p["adapter"] == "statuspage"]

from src.ingest import load_corpus, write_corpus  # noqa: E402

corpus = load_corpus()
log.info("corpus before: %d", len(corpus))

added = 0
for cfg in cfgs:
    try:
        recs = fetch_history(cfg)
    except Exception as exc:
        log.warning("%-14s FAILED: %s", cfg["id"], exc)
        continue
    new = 0
    for r in recs:
        key = f"{r['provider_id']}:{r['incident_id']}"
        if key not in corpus:
            corpus[key] = r
            new += 1
    added += new
    log.info("%-14s %4d fetched, %4d new", cfg["id"], len(recs), new)

records = sorted(corpus.values(), key=lambda i: (i["created_at"] or "", i["provider_id"]))
write_corpus(records)
json.dump(metrics.build_summary(records), open(DATA / "summary.json", "w"),
          indent=2, sort_keys=True)

log.info("added %d; corpus now %d", added, len(records))
