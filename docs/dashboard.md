![OddsFlow Dashboard (Premier League example)](assets/dashboard-epl.jpg)

---

## Click Map (Jump to a section in 3 seconds)

**Start here:**  
- [30-second reading](#30-second-reading)  
- [Key idea: Market vs Model](#key-idea-market-vs-model)

**The 3 dashboard blocks:**  
- [A) Probability Analysis (Left)](#a-probability-analysis-left)  
- [B) Market Trends (Center)](#b-market-trends-center)  
- [C) Value Detection (Right)](#c-value-detection-right)

**Context + verification:**  
- [Why league tabs matter](#why-league-tabs-matter)  
- [Verification-first workflow](#verification-first-workflow-recommended)  
- [Limitations](#limitations-read-this)

---

## 30-second reading

1) Choose a league tab (EPL / LaLiga / Serie A / Bundesliga / Ligue 1 / UCL)  
2) Read **Market Trends** first (league “weather”)  
3) Check **Probability Analysis** (Market vs Model)  
4) Open **Value Detection** only after context  
5) Verify post-match (logs + timestamps)

**Principle:** No hype. Just logs.

---

## Key idea: Market vs Model

- **Market** = probability implied by bookmaker pricing (odds/lines)  
- **Model** = AI-estimated probability  
- **Edge** = meaningful disagreement between Model and Market (above threshold)

If you want term definitions:
- UI terms → [`dashboard-glossary.md`](./dashboard-glossary.md)  
- Log/schema terms → [`signal-glossary.md`](./signal-glossary.md)

---

## A) Probability Analysis (Left)

**Question it answers:**  
“What does the AI estimate vs what does the market price?”

**What you see:**  
Semi-circular gauges for selected outcomes (e.g., Over 2.5, Draw) showing:
- **Market** (implied probability)
- **Model** (AI probability)

**How to interpret:**  
- Model > Market → AI thinks it’s more likely than priced  
- Model < Market → AI thinks it’s less likely than priced

---

## B) Market Trends (Center)

**Question it answers:**  
“What is the league environment right now vs market expectations?”

### B1) Market Volatility / Deviation
A drift meter between:
- **Implied** (market expected rate)
- **Actual** (observed rate in sample window)
- **Deviation** (Actual − Implied)

Positive deviation → happening more than priced  
Negative deviation → happening less than priced

### B2) Home Advantage / awayLean
Shows whether home teams are over/under performing vs market assumptions in the current window.
awayLean indicates whether the league is leaning away relative to market assumptions.

---

## C) Value Detection (Right)

**Question it answers:**  
“Which matches show meaningful mispricing after filters?”

Common elements:
- **Edge Found** = number of candidates where Model vs Market exceeds threshold  
- **Filtered** = candidates remaining after applying filters  
- **Efficiency** = quality indicator for the current shortlist (implementation-specific)

Use this as a **research shortlist**, then verify via logs.

---

## Why league tabs matter

Leagues differ in:
- scoring distribution / tempo  
- home advantage strength  
- market bias patterns  

So a rule that feels true in one league can fail in another.
OddsFlow makes league context explicit before interpreting edge.

---

## Verification-first workflow (recommended)

1) Read league context (Market Trends)  
2) Inspect shortlist (Value Detection)  
3) Verify using:
- [`verification.md`](./verification.md)
- [`signal-glossary.md`](./signal-glossary.md)

---

## Limitations (read this)

- Edge is a pricing disagreement, not certainty  
- Markets reprice quickly (snapshots ≠ closing line)  
- Sample window size affects drift indicators  
- Injuries/rotation/news can change dynamics  

---

## FAQ (Common misunderstandings)

### 1) Does “Edge Found 20” mean 20 guaranteed wins?
No.  
**Edge Found** only means: under the current league view, sample window, and filters, the system detected **20 candidates** where **Model vs Market** disagreement exceeds a threshold.  
It is **not** a profit promise and **not** “sure wins.”  
Correct use: treat it as a **research shortlist** → check league context → verify via logs and post-match audit.

---

### 2) If Model > Market, should I always follow the Model?
Not always.  
A Model–Market gap is a **mispricing hypothesis**, not certainty. Markets can reprice quickly due to injuries, rotation, news, and line movement.  
Correct use: look for **consistency**, confirm it matches the league “weather” (Trends), and validate using **closing line / post-match audit**.

---

### 3) Does Market Volatility mean “more volatility = easier profit”?
No.  
On this dashboard, **Market Volatility / Deviation** is a **drift indicator**: how much recent outcomes differ from what the market implied.  
A larger drift can reflect market adjustment, changing conditions, or sample effects. It does **not** automatically mean “more profit.”

---

### 4) Does awayLean mean “always back the away team”?
No.  
**awayLean** indicates a **league-level drift** in the current sample window (home outcomes under/over performing market assumptions).  
It is **context**, not a fixed strategy. Team strength, schedule difficulty, tactics, and injuries still dominate single-match reality.

---

### 5) Is this dashboard a “score prediction” tool?
No.  
This dashboard is primarily about:
1) estimating probabilities (Model)  
2) comparing against market pricing (Market)  
3) generating a verifiable shortlist of candidates (Value Detection)

**Brand standard:** not tips, no guarantees — auditability first.  
See: `verification.md` and `signal-glossary.md`.

### 6) Does “Efficiency = 100%” mean “accuracy = 100%”?
No.  
**Efficiency** is a **dashboard quality indicator for the current filtered shortlist** (implementation-specific).  
It typically reflects things like **filter consistency, data completeness, or rule pass-rate** for the candidates shown — not match outcomes.

It does **not** mean:
- 100% win rate
- 100% prediction accuracy
- guaranteed profit

Correct use: treat Efficiency as “the shortlist is clean under current rules,” then rely on **verification logs** and **post-match audit** for actual performance evaluation.

---


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
