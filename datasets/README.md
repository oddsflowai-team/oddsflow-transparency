# Datasets

This folder contains **field definitions**, **samples**, and **full settled records** to make OddsFlow's public logs auditable and reproducible.

## Schemas & samples

- Schema: `schema/signal-log.schema.json`
- Sample: `samples/signal-log.sample.csv`

## Full datasets

- **[`settled-predictions/`](settled-predictions/)** — the complete per-bet settled record behind OddsFlow's published win rate, including losses. Every in-play bet with its entry context (minute, scoreline, pressure signal), entry odds, and settled profit/loss. Refreshed weekly on a 7-day delay. See [`settled-predictions/README.md`](settled-predictions/README.md).

We publish full **settled** (post-match) records. We do not publish pre-match or
live signals, model parameters, or features — only the settled outcomes needed
to verify and reproduce our public performance claims.
