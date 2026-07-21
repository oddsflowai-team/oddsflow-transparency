# OddsFlow Real-Money Results Dataset

**The canonical proof dataset — real money our AI agents placed at sportsbooks, with a PDF proof for every row.**

This is part of the [OddsFlow Transparency Pack](https://github.com/oddsflowai-team/oddsflow-transparency). Unlike signal-level records (theoretical entry logic), **this dataset is actual money staked at real sportsbooks and settled at the book**. Every row links to a downloadable PDF proof from the sportsbook via the `pdf_proof` column. **All markets are included — AH, OU, and 1X2 — including the ones that underperform.**

**No hype. Just real bets, with receipts.**

## What's in here

Each row aggregates the real-money bets our AI agents placed on one match/market, settled at the sportsbook. Nothing is theoretical: these are fills we actually got, at prices we actually took, settled at the book's own numbers.

| Column | Description |
|---|---|
| `settled_date` | Date the bet(s) settled (UTC) |
| `league` | Competition name |
| `home_team` / `away_team` | Teams |
| `market` | `AH` (Asian Handicap), `OU` (Over/Under), or `1X2` (Moneyline) |
| `bets` | Number of individual real-money bets in this row |
| `staked` | Total amount staked (real money) |
| `profit_loss` | Net settled profit/loss (negative = loss) |
| `roi_pct` | Row ROI = `profit_loss / staked × 100` |
| `pdf_proof` | Direct URL to the sportsbook PDF proof for this bet/match |

## Files

- `all-results.csv` — the complete real-money record, all markets
- `by-market/ou.csv` — Over/Under only
- `by-market/ah.csv` — Asian Handicap only
- `by-market/1x2.csv` — Moneyline only

<!--SNAPSHOT:START-->
**Real-money results (snapshot):**

| Metric | Value |
|--------|-------|
| Settled bets | 3,482 |
| Matches / Competitions | 633 / 18 |
| Total wagered | 720,456 |
| **Net profit/loss** | **+73,954** |
| **ROI (profit / turnover)** | **+10.3%** |

**By market — the honest breakdown (nothing hidden):**

| Market | Bets | Wagered | Net | ROI |
|--------|------|---------|-----|-----|
| OU | 428 | 275,040 | +52,522 | **+19.1%** |
| AH | 2,474 | 279,526 | +18,627 | **+6.7%** |
| 1X2 | 580 | 165,890 | +2,805 | **+1.7%** |

*Every number is the exact sum of the rows in `all-results.csv`, each row linking to a PDF proof from the sportsbook. Recompute it yourself. ROI = profit / total wagered — the same definition OddsFlow uses everywhere.*
<!--SNAPSHOT:END-->

## Signal vs real-money

We publish **two** ROI numbers, and they are not the same — on purpose:

- **Signal-level ROI: +17.55%** — what the models *identify*. This is the theoretical return of our signal logic (`ai_performance_summary`): the edges the models flag, priced at the odds we recorded when the signal fired. It is what the strategy is *worth on paper*.
- **Real-money ROI: +10.3%** — what our agents *actually captured* at sportsbooks. This is the honest floor: real fills, real limits, real slippage, real settlement.

**The gap between 17.55% and 10.3% is execution reality.** Paper edges don't survive contact with the market intact — you don't always get the price, size gets limited, lines move before you're on. We could publish only the flattering signal number. Instead we publish both, and this dataset is the *lower, real one* — the money that actually changed hands. For the signal-level internals (per-bet minute, scoreline, pressure signal), see [`../settled-predictions/`](../settled-predictions/), which is signal-theoretical, not real money.

## Per-market honesty

Radical transparency means publishing the weak markets, not just the strong one:

- **OU (Over/Under) is our strength — +19.1%.** This is where the models earn their keep.
- **AH (Asian Handicap) is modest — +6.7%.** Positive, useful, not spectacular.
- **1X2 (Moneyline) is near break-even — +1.7%.** Barely above the line. We used to keep 1X2 out of the public framing because it was the weakest. That was the wrong instinct. We trade it, so we publish it — including the fact that it barely beats the vig.

Every market OddsFlow trades is in this file. We do not hide the ones that make us look worse, because a proof dataset that only shows the wins isn't proof of anything.

## How to verify

Every row's `pdf_proof` is a live URL to the sportsbook PDF certificate for that bet/match. Open any of them. Recompute the totals directly from `all-results.csv` — they will match the snapshot above to the unit. The per-market files (`by-market/*.csv`) are exact subsets of `all-results.csv` split by the `market` column.

## What this dataset does NOT contain

- No pre-match or live signals (the paid product)
- No model parameters, features, or code
- Not betting advice. Past performance does not guarantee future results.

## Citation

If you use this dataset, please cite it (see `CITATION.cff` in the repository root).

## License

Released under the repository's MIT license. Attribution to **OddsFlow.ai (oddsflow.ai)** is required when redistributing or citing.
