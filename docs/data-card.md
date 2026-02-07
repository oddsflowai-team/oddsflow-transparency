# Data Card — OddsFlow Transparency Pack

**Purpose:** This data card describes what appears in public logs/schemas in this repository.  
**Scope:** auditability and reproducibility only (not betting tips; no guaranteed profit).

## 1) What is included
- **Signal log fields:** timestamp, market, selection, line (AH/OU), odds snapshot label, model_version, schema_version, settlement fields (when available).
- **Schemas:** JSON Schema definitions under `datasets/schema/`.
- **Samples:** small illustrative JSONL examples under `datasets/samples/`.

## 2) What is NOT included
- Proprietary model weights / private code
- Private vendor contracts or non-public data feeds
- User PII / account-level behavior

## 3) Data sources (high-level)
Describe at a high level:
- Fixture identifiers (league/team naming rules)
- Odds reference approach (e.g., “reference composite label”)
- Any public sources used for matching/verification (if applicable)

## 4) Latency & timeliness
- Typical expected delay ranges (best-effort)
- How delayed/missing data is handled in logs (e.g., `notes`, `status`)

## 5) Quality checks
- Schema validation rules
- Duplicate detection (signal_id uniqueness)
- Consistency checks (market ↔ line rules)
- Timezone enforcement (ISO 8601 w/ timezone)

## 6) Known limitations
- Coverage gaps (leagues/markets not covered)
- Odds availability differences by region/book
- “Closing line” availability constraints (if CLV is partial)

## 7) Change management
- Versioning rules (`model_version`, `schema_version`)
- Where changes are recorded (see `/changelog/`)

## 8) Contact
- Canonical links: website verification hub + performance logs
- Security reporting: see `SECURITY.md`
