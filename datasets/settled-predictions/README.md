# OddsFlow Settled Predictions Dataset

> ⚠️ **This is SIGNAL-LEVEL data** (the model's entry logic with pressure/timing
> detail), **NOT real-money results.** The ROI here is **signal-theoretical** — the
> return of the signal logic on paper, not money placed at a book. For the
> **actual bets placed at sportsbooks with PDF proof** (all markets, the canonical
> real-money record), see **[`../real-money-results/`](../real-money-results/)**.

**The per-bet settled signal record behind OddsFlow's model — including losses.**

> **Rows dated up to 2026-08-24 also exist, unchanged, in
> [`../settled-predictions-v8-archive/`](../settled-predictions-v8-archive/).**
> That was the V8 engine, which stopped writing on that date; this dataset is
> generated from the V9 per-bet log. The archive is the only place the
> `pressure_signal` column is published — V9 does not record it. Nothing that was
> published there has been rewritten.

This dataset is part of the [OddsFlow Transparency Pack](https://github.com/oddsflowai-team/oddsflow-transparency). Where the Transparency Pack defines the *rules and schemas* for auditable prediction logs, this dataset provides the **actual settled outcomes**: every in-play bet our AI models placed, with the entry context that triggered it and the profit/loss after settlement.

**No hype. Just settled logs.**

## What's in here

Each row is one **settled bet** on a finished match — the output of OddsFlow's live AI models (Dixon-Coles + Shin de-vigging + isotonic calibration), recorded before the outcome was known and settled at full time.

| Column | Description |
|---|---|
| `match_date` | Match date (UTC) |
| `league` | Competition name |
| `home_team` / `away_team` | Teams |
| `final_score` | Full-time score (home-away) |
| `market` | `AH` (Asian Handicap), `OU` (Over/Under) or `1X2` (match result) |
| `selection` | `HOME`/`AWAY` (AH, 1X2), `DRAW` (1X2) or `OVER`/`UNDER` (OU) |
| `line` | Handicap or goals line at entry (e.g. `0.75`, `2.5`) |
| `entry_odds` | The odds **we recorded when entering** (our own trade record) |
| `entry_minute` | In-play minute the signal fired (`0` = pre-kickoff) |
| `score_at_entry` | Scoreline when the bet was placed |
| `model_key` | Which engine produced the entry (e.g. `oddsflow_handicap_sniper`) |
| `source` | Where the bet was recorded (`APIFOOTBALL`, `HGA`, `NOVA88`) |
| `stake` | Stake units allocated by the model |
| `result` | `WON` / `LOST` / `HALF_WON` / `HALF_LOST` / `PUSH` / `VOID` |
| `profit_loss` | Settled profit/loss in stake units (negative = loss) |

## Files

- `all-settled.csv` — the complete record
- `settled-YYYY-MM.csv` — one file per month

## Why this is different

Most "AI prediction" services publish a single accuracy percentage. This dataset publishes **every individual bet** with:

- **The entry context** — the minute, the scoreline and the price *at the moment of entry*. You can see when and into what a bet was placed, not just whether it won.
- **Losses included** — nothing is cherry-picked. Losing bets sit next to winning ones.
- **Our actual entry odds** — the price we took, so ROI is computable and checkable.

## Coverage & headline record

- Range: from 2026-01, refreshed daily on a 7-day delay
- Markets: Asian Handicap, Over/Under, 1X2 (settled)

**One row per model × source.** The same decision taken by two engines, or placed
at two brokers, is more than one row — `model_key` and `source` are published so
you can collapse or split it however you need. This is the same basis as the bet
count published on [oddsflow.ai/accuracy](https://www.oddsflow.ai/accuracy), which
is why the two reconcile; expect this file to sit slightly below it, because of
the 7-day publication delay.

<!--SNAPSHOT:START-->
**Settled-predictions dataset (latest settled match: 2026-08-30):**

| Metric | Value |
|--------|-------|
| Settled bets | 24,018 |
| Won / Lost | 11799 / 9570 |
| Half-won / Half-lost | 398 / 166 |
| Push / Void | 0 / 2085 |
| Total staked | 6,496,380.07 units |
| **Net profit/loss** | **+756,981 units** |
| **ROI** | **+11.7%** |
| Matches / Competitions | 3274 / 118 |

*One row per model × source: the same decision taken by two engines, or placed
at two brokers, is more than one row — `model_key` and `source` are published so
you can collapse or split it however you need. Every number above is the exact
sum of the rows in `all-settled.csv`; recompute it yourself. Refreshed daily on a
7-day delay.*
<!--SNAPSHOT:END-->

## How to verify

Each match maps to a `fixture_id`-keyed public performance record at
[oddsflow.ai/performance](https://www.oddsflow.ai/performance), where timestamped
PDF verification certificates are downloadable per bet. This CSV is the
machine-readable mirror of that public record.

## Update cadence & delay

Records are published on a **7-day delay** after settlement, so live/subscription
signals are never front-run. The dataset is refreshed **daily**.

## What this dataset does NOT contain

- No pre-match or live signals (the paid product)
- No model parameters, features, or code

## Notes & limitations

- Odds are OddsFlow's own recorded entry prices, not a resold bookmaker feed.
- Past performance does not guarantee future results. This dataset is for
  transparency, research, and reproducibility — **not betting advice**.
- A blank `entry_odds` on a row means the value was not recorded for that leg.

## Citation

If you use this dataset, please cite it (see `CITATION.cff` in the repository root).

## License

Released under the repository's MIT license. Attribution to **OddsFlow.ai
(oddsflow.ai)** is required when redistributing or citing.
