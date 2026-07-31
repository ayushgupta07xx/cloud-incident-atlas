# Roadmap

Nine phases, roughly one per month, Aug 2026 → Apr 2027. Each phase is a
weekend's worth of real work plus small weekday commits. The dataset compounds:
by month six you hold cross-vendor incident history that isn't publicly
available anywhere else, which is what makes the later analysis phases possible.

---

## Phase 1 — Aug 2026 · Foundation
*Status: scaffolded, needs deployment*

- [x] Provider registry + adapter dispatch
- [x] Statuspage / GCP / Azure / AWS adapters
- [x] Normalized incident schema, severity mapping
- [x] Corpus dedup, daily deltas, metrics module
- [ ] Deploy workflow, verify first green run
- [ ] Backfill: Statuspage v2 exposes ~90 days of history on first run
- [ ] Unit tests for each adapter against recorded fixtures

**Human commits:** ~12 · **Machine commits:** ~24

## Phase 2 — Sep 2026 · Correctness
- [ ] Fixture-based test suite (record real payloads, assert normalization)
- [ ] Schema validation with `pydantic`; reject malformed records instead of storing them
- [ ] Handle Statuspage pagination for providers with >100 incidents
- [ ] CI: run tests on PR, lint with `ruff`, type-check with `mypy`
- [ ] Alert on adapter drift — if a provider returns 0 incidents for 7 consecutive
      days, open an issue automatically (this also puts real issues on your graph)

**Human commits:** ~20 · **Machine commits:** ~24

## Phase 3 — Oct 2026 · Published site
- [ ] GitHub Pages site from `docs/`, built with MkDocs Material
- [ ] Provider comparison table, sortable, with sparklines
- [ ] Per-provider detail pages generated from the corpus
- [ ] Deploy workflow on push to main

**Human commits:** ~25 · **Machine commits:** ~26

## Phase 4 — Nov 2026 · Query surface
- [ ] Export corpus to SQLite; publish the `.db` as a release artifact
- [ ] Datasette instance on Fly.io free tier for ad-hoc SQL
- [ ] Parquet export for the data-engineering crowd
- [ ] Document the schema properly

**Human commits:** ~22 · **Machine commits:** ~25

## Phase 5 — Dec 2026 · Analysis
- [ ] First written analysis: "Which cloud category has the worst MTTR?" — now
      backed by four months of your own data
- [ ] Day-of-week and time-of-day incident distribution
- [ ] Correlated-incident detection: do Cloudflare incidents co-occur with others?
- [ ] Publish as a post; link from your portfolio

**Human commits:** ~18 · **Machine commits:** ~26

## Phase 6 — Jan 2027 · Incident classification
- [ ] Rule-based classifier over incident titles: networking / capacity / deploy /
      dependency / auth / storage
- [ ] Hand-label ~300 incidents as ground truth
- [ ] Measure the rules; publish precision/recall honestly, including where it fails

**Human commits:** ~24 · **Machine commits:** ~24

## Phase 7 — Feb 2027 · Alerting
- [ ] Configurable watch rules (`providers I care about` + severity threshold)
- [ ] Webhook + email notifier
- [ ] Terraform module so others can deploy their own instance
- [ ] Ties directly into your SentinelOps narrative

**Human commits:** ~26 · **Machine commits:** ~24

## Phase 8 — Mar 2027 · API
- [ ] Read-only FastAPI over the corpus
- [ ] Deploy on free tier, add OpenAPI docs
- [ ] Rate limiting, caching headers
- [ ] Client examples in the README

**Human commits:** ~22 · **Machine commits:** ~26

## Phase 9 — Apr 2027 · Hardening and handoff
- [ ] CONTRIBUTING.md, issue templates, good-first-issue labels
- [ ] Dependabot, CodeQL, SBOM
- [ ] Write-up: architecture decisions and what you'd do differently
- [ ] Submit to Hacker News / r/devops — real stars beat green squares

**Human commits:** ~20 · **Machine commits:** ~25

---

## Cadence design

The target was roughly 7 green days in 10. Here's how that arises without
faking anything:

**Machine layer.** The cron runs Mon–Sat, six days a week. It commits only when
a provider actually published something new. Across 13 providers, at least one
publishes on most days — but not all days, and the quiet stretches are real.
Expect 70–85% coverage from this layer alone, with genuine gaps.

**Human layer.** One substantial session per week (the phase checklist above)
plus small weekday commits — a test, a docs fix, an adapter tweak. This is what
fills Sundays and the quiet stretches.

**Do not** add a fallback that commits when there's no news. The no-op behaviour
is the single thing that makes the history honest, and it's also what makes the
gaps look natural. A graph with no gaps at all is the tell.

## What I won't build into this

Backdated commits. Rewriting `GIT_AUTHOR_DATE` to fill in history that didn't
happen is falsification, not automation, and it's detectable — the GitHub API
exposes both the authored date and the pushed date, and a year of history that
was all pushed in one week is obvious to anyone who looks. It would also put
every honest thing in this repo under suspicion.

The line this project stays on: the commits are real artifacts of a real system,
committed under your name because you built and maintain the system, and the
README says so plainly.

## Expected outcome

By April 2027: ~190 hand-written commits, ~220 machine commits, a dataset nobody
else publishes, a live site, an API, and one genuinely novel piece of analysis.

The graph fills in as a side effect. That ordering matters — it's why this
survives someone clicking into it.
