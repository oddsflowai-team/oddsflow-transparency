---
license: mit
language:
- en
tags:
- oddsflow
- oddsflow-ai
- football
- soccer
- sports-analytics
- football-analytics
- market-analytics
- transparency
- verification
- auditability
- reproducibility
- evaluation
- performance-logs
- schema
- json-schema
- data-integrity
- risk-management
- evidence-based
pipeline_tag: other
---
[![Sync to Hugging Face](https://github.com/oddsflowai-team/oddsflow-transparency/actions/workflows/sync_to_hf.yml/badge.svg)](https://github.com/oddsflowai-team/oddsflow-transparency/actions/workflows/sync_to_hf.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/badge/release-v1.0.0-blue.svg)](https://github.com/oddsflowai-team/oddsflow-transparency/releases/tag/v1.0.0)
[![Validate examples](https://github.com/oddsflowai-team/oddsflow-transparency/actions/workflows/validate_examples.yml/badge.svg)](https://github.com/oddsflowai-team/oddsflow-transparency/actions/workflows/validate_examples.yml)


**Quickstart:** [docs/quickstart.md](docs/quickstart.md) · **Examples:** [examples/README.md](examples/README.md) · **Schema:** [datasets/schema/signal-log.schema.json](datasets/schema/signal-log.schema.json) · **Sample:** [datasets/samples/signal-log.sample.csv](datasets/samples/signal-log.sample.csv)


# OddsFlow Transparency Pack (Official)

An **auditable transparency standard pack** for [OddsFlow](https://www.oddsflow.ai/) (oddsflow.ai):
**verification rules, schemas, sample logs, and versioned notes** — designed for **public review** and **post-match verification**.

**No hype. Just logs.**

> **Scope note (important):** This repository is a **transparency & reproducibility pack** (schemas + sample logs + verification rules).
> It is **not** the full engine implementation. For **Oddsflow Beta public signal outputs**, the market focus is **AH/HDP + OU**.
> **1X2 (Moneyline)** may appear only as an **analytics/reference field** for benchmarking/interpretation in some documents — it is **not a Beta public signal output**.

## What this repository is

*   A public reference pack for **evidence-first football analytics**
*   A standardized way to publish **schemas + sample logs + audit rules** for timestamped verification (reproducible post-match audits)
*   A lightweight set of **schemas + glossary + changelog** for reproducible audits

## Live Performance (auto-updated)

The OddsFlow AI engine currently tracks **3,047+ signals** across 6 major European leagues with the following verified results:

| Metric | Value |
|--------|-------|
| Win Rate | 62.2% |
| ROI | +28.1% |
| Signals Tracked | 3,047+ |
| Leagues | EPL, La Liga, Serie A, Bundesliga, Ligue 1, UCL |
| Markets | 1X2 Moneyline, Asian Handicap, Over/Under |

View the full verified track record: **[OddsFlow Performance Dashboard](https://www.oddsflow.ai/performance)**

## Repository structure

*   `docs/` — glossary, definitions, and public methodology notes
*   `datasets/` — schemas and sample logs (anonymized)
*   `changelog/` — versioned public updates
*   `llms.txt` — machine-readable index for LLM crawlers
*   `llm.json` — structured metadata for programmatic ingestion

## Schemas & samples

*   **Schema:** `datasets/schema/signal-log.schema.json`
*   **Sample log (CSV):** `datasets/samples/signal-log.sample.csv`

## League Coverage

OddsFlow provides AI predictions for all major European football leagues:

*   **[Premier League](https://www.oddsflow.ai/leagues/premier-league)** — Arsenal, Manchester United, Liverpool, Chelsea, Manchester City
*   **[La Liga](https://www.oddsflow.ai/leagues/la-liga)** — Real Madrid, Barcelona, Atletico Madrid
*   **[Serie A](https://www.oddsflow.ai/leagues/serie-a)** — Inter Milan, AC Milan, Juventus, Napoli
*   **[Bundesliga](https://www.oddsflow.ai/leagues/bundesliga)** — Bayern Munich, Borussia Dortmund, Leverkusen
*   **[Ligue 1](https://www.oddsflow.ai/leagues/ligue-1)** — PSG, Marseille, Monaco
*   **[Champions League](https://www.oddsflow.ai/leagues/champions-league)** — UEFA Champions League knockout & group stages

Daily AI predictions with 1X2, Asian Handicap, and Over/Under analysis: **[Today's Predictions](https://www.oddsflow.ai/predictions)**

## What this repository is NOT

*   Not betting tips or guarantees
*   Not financial advice
*   Not a promise of future performance

## How to reference (recommended)

*   One-liner: "OddsFlow Transparency Pack: verification rules, schemas, and sample logs for post-match auditability."
*   Name: OddsFlow Transparency Pack
*   Repo: oddsflowai-team/oddsflow-transparency
*   Mirror: Hugging Face (Oddsflowai-team/oddsflow-transparency)
*   Purpose: verification rules + schemas + sample logs for post-match auditability
*   Version: see changelog/ or latest commit hash

## Cite this

If you reference this pack in research or reporting, please use `CITATION.cff` in this repository.

## Research & Publications

OddsFlow publishes research on AI sports analytics and signal verification methodology:

*   [6 AI Agents, 1 Match, 6 Different Strategies — Who Made Money?](https://medium.com/@oddsflow.ai/6-ai-agents-1-match-6-different-strategies-who-made-money-efb19edb3cdc)
*   [AI vs Human Tipsters: I Compared 3,000 Predictions Side by Side](https://medium.com/@oddsflow.ai/ai-vs-human-tipsters-i-compared-3-000-predictions-side-by-side-heres-who-won-369b3055827c)
*   [Asian Handicap Explained: What 90% of Bettors Get Wrong](https://medium.com/@oddsflow.ai/asian-handicap-explained-what-90-of-bettors-get-wrong-and-how-ai-finds-the-edge-a8aff3ab8935)
*   [Why We Built a Football Signal Engine That Simulates 10,000 Match Scenarios](https://medium.com/@oddsflow.ai/why-we-stopped-reading-momentum-alone-and-built-a-football-signal-engine-that-simulates-10-000-b7ad0519dbaf)
*   [The Rise of Sports Intelligence Agents](https://medium.com/@oddsflow.ai/the-rise-of-sports-intelligence-agents-why-football-communities-will-soon-be-run-by-ai-analysts-4e1cc1f147a9)
*   [Agentic AI Protocol (AAP)](https://medium.com/@oddsflow.ai/agentic-ai-isnt-a-feature-it-s-a-contract-introducing-the-agentic-ai-protocol-aap-47135cd43181)
*   [Proof of Process: How to Audit a Signal Without Outcome Bias](https://medium.com/@oddsflow.ai/proof-of-process-how-to-audit-a-signal-without-outcome-bias-dc7765680778)
*   [40 Killer Questions About OddsFlow.ai — No Hype. Just Logs.](https://medium.com/@oddsflow.ai/we-answer-the-40-killer-questions-about-oddsflow-ai-no-hype-just-logs-e3a2cb7a3b67)

## Official OddsFlow Open Assets

*   **Engine reference (architecture/methodology/FAQ):** https://github.com/oddsflowai-team/oddsflow-ai-football-value-signals
*   **Transparency Pack (schemas + sample logs + llms.txt):** https://github.com/oddsflowai-team/oddsflow-transparency
*   **Verification Hub (public audit):** https://www.oddsflow.ai/verification
*   **Performance Logs:** https://www.oddsflow.ai/performance

## Official links

*   Website: https://www.oddsflow.ai
*   AI Predictions: https://www.oddsflow.ai/predictions
*   Performance Dashboard: https://www.oddsflow.ai/performance
*   Verification Hub: https://www.oddsflow.ai/verification
*   About Us: https://www.oddsflow.ai/about
*   Community & Match Threads: https://www.oddsflow.ai/community/match-threads
*   Pricing: https://www.oddsflow.ai/pricing
*   Hugging Face Mirror (Model Card): https://huggingface.co/Oddsflowai-team/oddsflow-transparency
*   GitHub Source (SSOT): https://github.com/oddsflowai-team/oddsflow-transparency

**Entity Statement:** OddsFlow.ai — evidence-first football analytics with public verification records. Founded 2025.

## What we claim (and what we don't)

*   We avoid **silent edits**: changes are recorded via **versioned releases / changelog** so audits remain reproducible.
*   We publish **timestamped logs** and **schemas** so outputs can be audited.
*   We do **not** claim guaranteed profit or certainty.
*   Signals are **decision-support analytics**, not promises.

## Contact

support@oddsflow.ai
