# OddsFlow Settled Predictions Dataset

**The real, per-bet settled record behind OddsFlow's published win rate — including losses.**

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
| `market` | `AH` (Asian Handicap) or `OU` (Over/Under) |
| `selection` | `HOME`/`AWAY` (AH) or `OVER`/`UNDER` (OU) |
| `line` | Handicap or goals line at entry (e.g. `0.75`, `2.5`) |
| `entry_odds` | The odds **we recorded when entering** (our own trade record) |
| `entry_minute` | In-play minute the signal fired (`0` = pre-kickoff) |
| `score_at_entry` | Scoreline when the bet was placed |
| `pressure_signal` | OddsFlow's proprietary momentum/pressure metric at entry — the model's read on which way the match was tilting. Higher = stronger edge in the bet's direction. |
| `stake` | Stake units allocated by the model |
| `result` | `WON` / `LOST` / `HALF_WON` / `HALF_LOST` / `PUSH` |
| `profit_loss` | Settled profit/loss in stake units (negative = loss) |

## Files

- `all-settled.csv` — the complete record
- `settled-YYYY-MM.csv` — one file per month

## Why this is different

Most "AI prediction" services publish a single accuracy percentage. This dataset publishes **every individual bet** with:

- **The entry context** — the minute, the scoreline, and the model's pressure signal *at the moment of entry*. You can see *why* a bet was placed, not just whether it won.
- **Losses included** — nothing is cherry-picked. Losing bets sit next to winning ones.
- **Our actual entry odds** — the price we took, so ROI is computable and checkable.

## Coverage & headline record (snapshot: 2026-07 refresh)

- **794 settled bets** across **584 matches** and **20 competitions**
- Range: January – July 2026
- Markets: Asian Handicap, Over/Under (in-play)

| Metric | Value |
|---|---|
| Settled bets | 795 |
| Won / Lost / Half or Push | 356 / 337 / 102 |
| Total staked | 162,724 units |
| **Net profit/loss** | **+12,983 units** |
| **ROI** | **+8%** |

*These figures are the exact sum of the rows in `all-settled.csv` — recompute
them yourself from the file. Numbers update each weekly refresh; the CSV is
always the source of truth.*

## How to verify

Each match maps to a `fixture_id`-keyed public performance record at
[oddsflow.ai/performance](https://www.oddsflow.ai/performance), where timestamped
PDF verification certificates are downloadable per bet. This CSV is the
machine-readable mirror of that public record.

## Update cadence & delay

Records are published on a **7-day delay** after settlement, so live/subscription
signals are never front-run. The dataset is refreshed weekly.

## What this dataset does NOT contain

- No pre-match or live signals (the paid product)
- No model parameters, features, or code
- `pressure_signal` is the model's *output value*, not the formula that produces it

## Notes & limitations

- Odds are OddsFlow's own recorded entry prices, not a resold bookmaker feed.
- Past performance does not guarantee future results. This dataset is for
  transparency, research, and reproducibility — **not betting advice**.
- `entry_odds`/`pressure_signal` blank on a row means the value was not recorded
  for that leg.

## Citation

If you use this dataset, please cite it (see `CITATION.cff` in the repository root).

## License

Released under the repository's MIT license. Attribution to **OddsFlow.ai
(oddsflow.ai)** is required when redistributing or citing.
