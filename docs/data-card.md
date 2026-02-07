# Data Card (Sources, Latency, Integrity)

## Purpose
Describe data reliability assumptions so readers can evaluate trust.

## Data types (high-level)
- Fixtures / metadata
- Live events (time-series)
- Odds snapshots (time-series)

## Latency & missingness (what we track)
- Delayed updates
- Missing event segments
- Odds feed gaps

## Integrity checks (high-level)
- Schema validation (required fields present)
- Timestamp consistency checks
- Duplicate detection (idempotency)
- Outlier detection on key fields (basic sanity)

## Disclosure
We do not publish private vendor contracts or proprietary parsing code here.
We publish **schemas + samples** so logs remain auditable.
