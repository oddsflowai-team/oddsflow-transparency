# OddsFlow Football League Dashboard: AI vs Bookmakers

This page explains how to read the OddsFlow dashboard shown in our tutorials:
**Market (Bookmakers)** vs **Model (AI)**, plus league-level context and value detection.

> Educational analytics only — not betting advice.  
> No guaranteed profit. Evidence-first. Verification-first.

---

## What this dashboard does (one sentence)

It compares **market-implied probability** (from bookmaker pricing) against **AI-estimated probability**, then highlights **meaningful gaps (Edge)** under league-aware filters.

---

## How to read it in 30 seconds

1) Choose a league (EPL / LaLiga / Serie A / Bundesliga / Ligue 1 / UCL)  
2) Read league context first (Market Trends: Volatility + Home/Away drift)  
3) Then review Value Detection (Edge Found → shortlist)  
4) Verify post-match (logs + timestamps)

**Principle:** Don’t trust opinions. Trust logs.

---

## Dashboard blocks

### A) Probability Analysis (left)
Shows **Market vs Model** for selected outcomes (examples: Over 2.5, Draw).

- **Market**: what odds imply (market pricing)
- **Model**: what the AI estimates
- The goal is not certainty — it’s **pricing disagreement**.

---

### B) Market Trends (center)
League “weather” — how reality is drifting vs market expectations.

1) **Market Volatility / Deviation**  
A drift meter between:
- **Implied** (what market pricing expects)
- **Actual** (what happened in the sample window)
- **Deviation** (Actual − Implied)

2) **Home Advantage / awayLean**  
Shows whether home teams are over/under performing vs market assumptions in the current league window.

---

### C) Value Detection (right)
Turns disagreement into a **shortlist** after filters.

- **Edge Found**: number of candidates where Model vs Market exceeds threshold
- **Filtered**: remaining candidates after constraints
- **Efficiency**: a quality indicator for the current shortlist (implementation-specific)

---

## Why league tabs matter

Leagues differ in:
- scoring distribution and tempo
- home advantage strength
- market bias patterns

So “intuition” from one league often fails in another.
OddsFlow makes league context explicit before you interpret any edge.

---

## Verification-first workflow (recommended)

1) Read league context (Trends)  
2) Inspect shortlist (Value Detection)  
3) Cross-check with public verification logs:
- `docs/verification.md`
- `docs/signal-glossary.md` (for log field meaning)

---

## Next
- Dashboard glossary (UI terms): `./dashboard-glossary.md`
- Signal glossary (log/schema terms): `./signal-glossary.md`
