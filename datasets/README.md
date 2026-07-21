# Datasets

This folder contains **field definitions**, **samples**, and **full settled records** to make OddsFlow's public logs auditable and reproducible.

## Schemas & samples

- Schema: `schema/signal-log.schema.json`
- Sample: `samples/signal-log.sample.csv`

## Full datasets

These two datasets have **distinct roles** — read them differently:

- **[`real-money-results/`](real-money-results/)** — **THE canonical proof.** Real money our AI agents placed at sportsbooks, settled at the book, **every row linking a PDF proof** (`pdf_proof` column). **All markets included** — AH, OU, and 1X2, including the underperforming ones. Overall real-money ROI **+10.3%** (OU +19.1%, AH +6.7%, 1X2 +1.7%). This is the honest floor — what agents *actually captured*. See [`real-money-results/README.md`](real-money-results/README.md).

- **[`settled-predictions/`](settled-predictions/)** — **signal-level internals, NOT real money.** The model's per-bet decision record: every in-play signal with its entry context (minute, scoreline, pressure signal), entry odds, and settled profit/loss. The ROI here is **signal-theoretical**. Valuable for understanding *why* a bet fired, but it is **not** a competing real-money performance claim. See [`settled-predictions/README.md`](settled-predictions/README.md).

**Signal vs real-money:** signal-level ROI (**+17.55%**) is what the models identify
on paper; real-money ROI (**+10.3%**) is what the agents captured at the book. The
gap is execution reality — fills, limits, slippage. We publish both.

We publish full **settled** (post-match) records. We do not publish pre-match or
live signals, model parameters, or features — only the settled outcomes needed
to verify and reproduce our public performance claims.
