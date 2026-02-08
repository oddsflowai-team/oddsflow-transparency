#!/usr/bin/env python3
"""
Validate examples/sample_signal_log.json against datasets/schema/signal-log.schema.json

Usage:
  python scripts/validate.py
"""

import json
import sys
from pathlib import Path

from jsonschema import validate


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]

    schema_path = repo_root / "datasets" / "schema" / "signal-log.schema.json"
    sample_path = repo_root / "examples" / "sample_signal_log.json"

    if not schema_path.exists():
        print(f"[ERROR] Schema not found: {schema_path}", file=sys.stderr)
        return 2

    if not sample_path.exists():
        print(f"[ERROR] Sample log not found: {sample_path}", file=sys.stderr)
        return 2

    with schema_path.open("r", encoding="utf-8") as f:
        schema = json.load(f)

    with sample_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    validate(instance=data, schema=schema)
    print("OK: sample log matches schema")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print(f"[ERROR] Validation failed: {e}", file=sys.stderr)
        raise
