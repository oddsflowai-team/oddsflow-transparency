# Examples — How to use this Transparency Pack

These examples are **anonymized** and intended for **validation + audit workflow demos**.

This repository is a transparency standard pack:
- verification rules
- JSON schemas
- sample logs (demo)
- glossary + changelog

**Not betting tips. Not financial advice. No hype. Just logs.**

---

## Example files
- `sample_signal_log.json` — a minimal anonymized signal log example

---

## Validate a sample log against the schema

1) Locate the schema in this repo  
Typical path (example): `datasets/signal-log.schema.json`

Run from repo root (so the relative paths resolve).

2) Install a JSON schema validator (pick one)

 Python (jsonschema)
```bash
python -m pip install jsonschema
python - << 'PY'
import json
from jsonschema import validate

with open("datasets/signal-log.schema.json","r",encoding="utf-8") as f:
    schema = json.load(f)

with open("examples/sample_signal_log.json","r",encoding="utf-8") as f:
    data = json.load(f)

validate(instance=data, schema=schema)
print("OK: sample log matches schema")
PY
```
If validation fails, your JSON does not match the required fields/types in the schema.
Check the `required` fields in the schema and update `sample_signal_log.json` accordingly.

(Windows users: run the Python snippet in a `.py` file instead of heredoc.)
