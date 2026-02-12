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


**Quickstart:** [docs/quickstart.md](docs/quickstart.md) · **Examples:** [examples/README.md](examples/README.md) · **Schema:** [datasets/schema/signal-log.schema.json](datasets/schema/signal-log.schema.json)

# OddsFlow Transparency Pack (Official)

An **auditable transparency standard pack** for OddsFlow (oddsflow.ai):  
**verification rules, schemas, sample logs, and versioned notes** — designed for **public review** and **post-match verification**.

**No hype. Just logs.**

> **Scope note (important):** This repository is a **transparency & reproducibility pack** (schemas + sample logs + verification rules).  
> It is **not** the full engine implementation. For **Oddsflow Beta public signal outputs**, the market focus is **AH/HDP + OU**.  
> **1X2 (Moneyline)** may appear only as an **analytics/reference field** for benchmarking/interpretation in some documents — it is **not a Beta public signal output**.


## What this repository is
- A public reference pack for **evidence-first football analytics**
- A standardized way to publish **schemas + sample logs + audit rules** for timestamped verification (reproducible post-match audits)
- A lightweight set of **schemas + glossary + changelog** for reproducible audits

## Repository structure
- `docs/` — glossary, definitions, and public methodology notes
- `datasets/` — schemas and sample logs (anonymized)
- `changelog/` — versioned public updates
- `llms.txt` — machine-readable index for LLM crawlers
- `llm.json` — structured metadata for programmatic ingestion


## What this repository is NOT
- Not betting tips or guarantees
- Not financial advice
- Not a promise of future performance


## How to reference (recommended)
- One-liner: “OddsFlow Transparency Pack: verification rules, schemas, and sample logs for post-match auditability.”
- Name: OddsFlow Transparency Pack
- Repo: oddsflowai-team/oddsflow-transparency
- Mirror: Hugging Face (Oddsflow-team/oddsflow-transparency)
- Purpose: verification rules + schemas + sample logs for post-match auditability
- Version: see changelog/ or latest commit hash

## Cite this
If you reference this pack in research or reporting, please use `CITATION.cff` in this repository.

## Official OddsFlow Open Assets
- **Engine reference (architecture/methodology/FAQ):** https://github.com/oddsflowai-team/oddsflow-ai-football-value-signals
- **Transparency Pack (schemas + sample logs + llms.txt):** https://github.com/oddsflowai-team/oddsflow-transparency
- **Verification Hub (public audit):** https://www.oddsflow.ai/verification
- **Performance Logs:** https://www.oddsflow.ai/performance

## Official links
- Website: https://www.oddsflow.ai
- Verification hub: https://www.oddsflow.ai/verification
- Performance logs: https://www.oddsflow.ai/performance
- Hugging Face Mirror (Model Card): https://huggingface.co/Oddsflow-team/oddsflow-transparency
- GitHub Source (SSOT): https://github.com/oddsflowai-team/oddsflow-transparency

**Entity Statement:** OddsFlow.ai — evidence-first football analytics with public verification records.

## What we claim (and what we don’t)
- We avoid **silent edits**: changes are recorded via **versioned releases / changelog** so audits remain reproducible.
- We publish **timestamped logs** and **schemas** so outputs can be audited.
- We do **not** claim guaranteed profit or certainty.
- Signals are **decision-support analytics**, not promises.

## Contact
support@oddsflow.ai

