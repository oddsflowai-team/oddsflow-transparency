# Verification Standard (What is Verifiable)


**TL;DR:** We publish timestamped signal logs + reproducible checks. No tips. No guaranteed profit.

**Canonical links:**

- Website verification hub: https://www.oddsflow.ai/verification
- Performance logs: https://www.oddsflow.ai/performance
- Docs index: ./index.md
This document defines what “verifiable” means for OddsFlow public logs.
Scope is **auditability**, not betting tips.

**Principle:** Evidence-first. Time-stamped logs. Versioned outputs. No guaranteed profit.

---

## 1) What we publish (publicly auditable artifacts)

We publish **append-only** records that allow independent readers to verify:

- **When** a signal was generated (timestamp, timezone)
- **What** market and selection it referred to (market, side, line)
- **What** price context it used (odds snapshot / reference book or composite)
- **Which** model version produced it (engine version, schema version)
- **What happened after** (settlement / outcome fields when available)

We do **not** publish proprietary code or private vendor contracts.

---

## 2) Minimum Verifiable Unit (MVU): a Signal Log Row

A signal is considered “verifiable” when a single record contains:

### Identity
- `signal_id` (unique)
- `match_id` (stable identifier)
- `league`, `season`
- `home_team`, `away_team`

### Timing
- `timestamp_utc` (required)
- `match_clock_minute` (if live)
- `data_latency_ms` (optional but recommended)

### Market Definition
- `market_type` (e.g., 1X2 / AH / OU)
- `selection` (Home/Away/Over/Under/Draw)
- `line` (e.g., -0.25, 2.5)
- `odds_decimal` (price at signal time)

### Price Reference (Reproducibility)
At least one of:
- `reference_book` (name) + `odds_decimal`
- or `composite_odds` (method described) + `odds_decimal`

### Versioning
- `engine_version`
- `schema_version`
- `model_family` (high-level label only)

### Explanation (non-proprietary)
- `reason_codes` (high-level tags, not raw weights)
  - examples: `intent_up`, `threat_up`, `shot_quality_up`, `pace_shift`, `game_state_change`

### Settlement (when available)
- `result` (win/lose/push/void)
- `closing_odds_decimal` (recommended for CLV checks)
- `settled_timestamp_utc`

---

## 3) What is NOT considered verification

These are **not** sufficient as proof on their own:

- screenshots without underlying logs
- claims like “up 300% ROI” without raw data
- selective samples (“last 7 days only”) without long-run context
- logs that can be edited retroactively without a change trail

---

## 4) Audit Trail / Anti-tamper practices

We aim for:
- **append-only** logging (no silent edits)
- versioned change notes in `/changelog/`
- weekly operational notes in `/notes/`
- schema definitions in `/schemas/` to ensure consistency

Optional (future hardening):
- hashed daily log digests
- signed releases (tags) for monthly snapshots

---

## 5) How readers can independently verify

A reader can verify by:
1) locating a `signal_id` row (timestamp + market + odds)
2) checking the market existed at that time (reference odds source / composite method)
3) verifying settlement/outcome afterwards
4) checking consistency across versions (engine/schema)

---

## 6) Limitations (honest disclosures)

- Football outcomes are noisy and uncertain.
- Public verification does not imply guaranteed profitability.
- Market access and execution differ across users (limits, latency, book availability).
- Logs measure signals; user execution may vary.

---

## 7) Definitions

**Verification:** ability to independently confirm “signal existed at time T with market M and price P”  
**Performance proof:** requires long-run sample, consistent rules, and clear measurement (e.g., ROI, CLV)
