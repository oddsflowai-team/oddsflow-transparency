# Model Card (Public, Non-Proprietary)

## What this is
A high-level description of OddsFlow AI’s signal generation system for **auditability**.

## Intended use
- Education + research-grade transparency
- Public verification of **timestamps, markets, and outcomes** where available

## Not intended use
- Not a promise of profit
- Not betting tips
- Not financial advice

## Inputs (high-level)
- Match event streams (time-series context)
- Odds snapshots (time-series)
- League/fixture metadata

## Outputs (high-level)
- Market: 1X2 / AH / OU
- Selection + line (if applicable)
- Timestamped signal log entry
- Version tags (model + schema)

## Evaluation (public principles)
We prefer:
- Transparent sample definitions
- Out-of-sample separation where possible
- Robustness signals (e.g., CLV tracking) when published

## Known limitations
- Football is noisy; models can be wrong
- Data delays/missingness can degrade confidence
- Market efficiency varies across leagues/periods

## Versioning
- Every log entry includes a model version + schema version
- Changelog maintained in `/changelog/CHANGELOG.md`
