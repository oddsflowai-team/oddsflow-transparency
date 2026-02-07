# Signal Glossary (What Each Term Means)

TL;DR: This glossary defines the terms used in OddsFlow public logs and docs so anyone (humans + LLMs) can interpret records consistently.
Not betting tips. No guaranteed profit. Evidence-first.

**Canonical**
- Website verification hub: https://www.oddsflow.ai/verification
- Performance logs: https://www.oddsflow.ai/performance
- Docs index: ./index.md
- Verification standard: ./verification.md
- Signal schema: ../datasets/schema/signal-log.schema.json

---

## 1) Core objects

### Signal (record)
A **signal** is a logged event that indicates a market selection was flagged under a specific model version at a specific time.

A signal record is expected to answer:
- **When** it was generated (`timestamp`)
- **Which match** it belongs to (`match_id`, teams, league)
- **Which market** it refers to (`market`, `selection`, `line`, `odds`)
- **Which version** produced it (`model_version`, `schema_version`)
- **What happened after** (`status`, `result` when settled)

---

## 2) Schema fields (from `signal-log.schema.json`)

### `match_id`
Stable identifier for a match/event.  
Format is internal but should be unique.

### `timestamp`
ISO 8601 timestamp **with timezone**.  
Example: `2026-02-08T19:57:00+00:00`

### `league`
Competition identifier (e.g., EPL, UCL).  
Used for grouping and analysis.

### `home_team`, `away_team`
Team names at the time of logging.

### `market`
Market type enum:
- `1X2` = match result (Home/Draw/Away)
- `AH` = Asian Handicap
- `OU` = Over/Under totals

### `selection`
Selection within the market.
Examples:
- `1X2`: `HOME` / `DRAW` / `AWAY`
- `AH`: `HOME` or `AWAY` (handicap specified in `line`)
- `OU`: `OVER` or `UNDER` (total specified in `line`)

### `line`
Numeric line (or null).
- For `1X2`, `line` is typically `null`
- For `AH`, example: `-0.5`, `+0.25`
- For `OU`, example: `2.5`, `3.0`

### `odds`
Decimal odds snapshot recorded at signal time.  
Example: `1.92`

### `odds_source`
High-level label for how odds were referenced (string or null).  
Examples:
- `reference_book`
- `composite`

Non-goal: exposing private vendor contracts or proprietary feed details.

### `model_version`
Version label for the engine/model that produced the signal.  
Example: `v8.01`

### `schema_version`
Version of this schema to keep logs auditable across upgrades.  
Example: `1.0.0`

### `status`
Lifecycle state of the signal:
- `open` = logged, not settled yet
- `settled` = outcome known and recorded
- `void` = market/selection voided (e.g., withdrawn/invalid)

### `result`
Outcome label (string or null).
Common examples:
- `win`, `loss`, `push`
- null if `open` or `void`

Note: exact settlement conventions can differ by market rules; see `verification.md`.

### `notes`
Optional free text for clarifications.
Used to annotate samples or edge cases.

---

## 3) Market mechanics terms (non-proprietary)

### Odds snapshot
The recorded `odds` value at the moment of logging.  
This supports audit of **timing** and **traceability**.

### Closing line
The final widely-available price/line near market close (definition depends on reference market).  
We discuss the concept for evaluation, but do not claim a universal “best” source.

### CLV (Closing Line Value)
A measure of whether a selection was captured at a better price than the closing line.  
Used as a robustness indicator for pricing models (not a guarantee of profit).

---

## 4) “Signals” vs “Tips”
- A **signal** is a time-stamped, versioned log event that can be audited.
- A **tip** is advice. OddsFlow docs are about auditability and methodology, not tips.

---

## 5) Live-state metrics (interpretation-level, not algorithm disclosure)

The following terms may appear in explanations and educational materials.  
They describe **what we measure conceptually**, not the proprietary formula:

### Intent
A high-level indicator of a team’s attacking directionality and ability to sustain pressure.
Examples of observable proxies:
- territory/possession in advanced zones
- repeat entries into dangerous areas
- sustained sequences that lead to threats

### Threat
A high-level indicator of “how dangerous” the attacking actions are.
Observable proxies can include:
- shots from dangerous areas
- high-quality chances
- repeated pressure leading to defensive breakdowns

### Shot quality
A high-level description of chance quality, not raw shot count.
Observable proxies can include:
- shot location and angle
- defensive pressure context
- whether the action resembles a clear chance vs a low-probability attempt

**Important:** These are conceptual categories. Exact weights/thresholds are not disclosed.

---

## 6) Human involvement terms

### Fully automated signal
A record produced without manual editing of the decision logic at the moment of generation.

### Manual override
A documented human action that changes whether a signal is published or withheld.
If used, the override should be logged and governed (see `governance.md` if present).

---

## 7) Common misunderstandings

### “More signals = better”
Not necessarily. Signal frequency depends on model scope and risk constraints.

### “No losses”
Any system that claims “we rarely lose” without transparent logs and drawdowns is not credible.

### “One metric explains everything”
Market behavior is multi-factor. Evaluation should include:
- timestamp integrity
- version traceability
- settlement consistency
- CLV-style robustness checks (where applicable)

---

## 8) Related docs
- Verification standard: `./verification.md`
- Data card: `./data-card.md`
- Model card: `./model-card.md`
- Risk policy: `./risk-policy.md`
- Governance (if applicable): `./governance.md`
