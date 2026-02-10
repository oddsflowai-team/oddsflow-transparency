# Dashboard Glossary (AI vs Bookmakers)

This glossary defines **UI terms** used on the OddsFlow dashboard.
For log/schema field definitions (timestamp, match_id, market enums), see:
`docs/signal-glossary.md`.

> Educational analytics only — not betting advice.

---

## Market
**Meaning:** Market-implied probability derived from bookmaker pricing (odds/lines).  
**Intuition:** “What the market is pricing.”

## Model
**Meaning:** AI-estimated probability based on data/modeling.  
**Intuition:** “What the model believes.”

## Implied
**Meaning (in Trend cards):** the market’s expected rate for an outcome category.  
**Intuition:** “The market forecast.”

## Actual
**Meaning (in Trend cards):** the observed rate in a recent sample window.  
**Intuition:** “What really happened.”

## Deviation
**Meaning:** the difference between Actual and Implied.  
- Positive → happening more often than priced  
- Negative → happening less often than priced  
**Intuition:** “Forecast error.”

## Market Volatility (as displayed)
**Meaning:** a measured drift indicator between market expectations and outcomes (via deviation).  
**Intuition:** “How far reality is drifting from the priced script.”

## Home Advantage
**Meaning:** whether home teams are performing stronger/weaker than typical assumptions.  
**Intuition:** “Is home actually home right now?”

## awayLean
**Meaning:** drift indicator suggesting away outcomes are outperforming or underperforming market assumptions in the sample window.  
**Intuition:** “Is the league leaning away right now?”

## Edge
**Meaning:** meaningful disagreement between Model and Market, beyond a threshold.  
**Intuition:** “The gap worth reviewing.”

## Threshold (Edge Threshold)
**Meaning:** minimum edge size required before an item becomes a shortlist candidate.  
**Intuition:** “Ignore tiny gaps.”

## Value Detection
**Meaning:** module that scans matches and returns a filtered shortlist of edge candidates.  
**Intuition:** “Shortlist builder.”

## Edge Found
**Meaning:** number of shortlist candidates discovered for the selected league/window.  
**Intuition:** “How many disagreements passed the bar.”

## Filtered
**Meaning:** candidates remaining after applying filters/constraints.  
**Intuition:** “How many survived filtering.”

## Efficiency
**Meaning:** quality indicator for the current filtered set (implementation-specific).  
**Intuition:** “How clean the shortlist is.”

## Sample Window
**Meaning:** the match sample used to compute Actual/Deviation metrics.  
**Intuition:** “The timeframe behind league weather.”
