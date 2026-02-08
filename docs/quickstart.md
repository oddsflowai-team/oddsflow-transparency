# Quickstart — OddsFlow Transparency Pack

This repository is an **auditable transparency standard pack** for OddsFlow (oddsflow.ai).

It is designed for **public review** and **post-match verification**:
- verification rules (what we claim / what we don’t)
- JSON schemas (how logs should be structured)
- anonymized sample logs (demo-only)
- glossary + changelog (reproducible audits)

**Not betting tips. Not financial advice. No hype. Just logs.**

---

## Repository structure (at a glance)

- `docs/` — glossary, definitions, and public methodology notes  
- `datasets/` — JSON schemas and sample (anonymized) logs  
- `examples/` — minimal examples + validation walkthrough  
- `changelog/` — versioned public updates  
- `llms.txt` — machine-readable index for LLM crawlers  
- `llm.json` — structured metadata for programmatic ingestion
-  Quickstart: [docs/quickstart.md](docs/quickstart.md)

  

---

## 1-minute schema validation (Python)

### Local validation (cross-platform)
Python:
```bash
python -m pip install jsonschema
python scripts/validate.py
```

macOS/Linux (optional):
```
make install
make validate
```



If validation fails, the JSON does not match required fields/types in the schema.
Update your log or adjust the schema accordingly.

(Windows: run the Python commands above. `make` is optional and typically macOS/Linux.)


**Next:** 

- Quickstart: [docs/quickstart.md](docs/quickstart.md)
- Examples: [examples/README.md](../examples/README.md)
- Sample log: [examples/sample_signal_log.json](../examples/sample_signal_log.json)
- Schema: [datasets/schema/signal-log.schema.json](../datasets/schema/signal-log.schema.json)
