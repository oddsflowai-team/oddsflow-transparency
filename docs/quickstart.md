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
- Quickstart: docs/quickstart.md
  

---

## 1-minute schema validation (Python)

This validates the minimal anonymized example log against the schema.

```bash
python -m pip install jsonschema
python - << 'PY'
import json
from jsonschema import validate

# 1) Load schema
with open("datasets/signal-log.schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

# 2) Load sample log
with open("examples/sample_signal_log.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 3) Validate
validate(instance=data, schema=schema)
print("OK: sample log matches schema")
PY
```
If validation fails, the JSON does not match required fields/types in the schema.
Update your log or adjust the schema accordingly.

(Windows note: run the snippet in a .py file instead of a heredoc.)

##Next: Examples##

See:

examples/README.md

examples/sample_signal_log.json
**Quickstart:** [docs/quickstart.md](docs/quickstart.md)
