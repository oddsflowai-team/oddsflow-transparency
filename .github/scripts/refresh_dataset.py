#!/usr/bin/env python3
"""Pull the latest settled-predictions CSVs from OddsFlow's public export
endpoint and write them into datasets/settled-predictions/. Injects the
endpoint's pre-rendered README snapshot between the <!--SNAPSHOT--> markers
(single generated block — no fragile regex, no stale-number drift). Read-only
fetch; no secrets. Aborts loudly on empty/degraded data."""
import json, os, sys, time, urllib.error, urllib.request, pathlib, re

URL = os.environ.get("EXPORT_URL", "https://www.oddsflow.ai/api/v1/settled-export")
DEST = pathlib.Path("datasets/settled-predictions")
MIN_BETS = 600  # floor guard: refuse to overwrite good data with a degraded pull

# The export is served from a 6h edge cache, but that cache is per-POP and a
# deploy purges it, so this runner can and does land on a cold one. Measured
# 2026-09-05: cold >120s, warm 24.5s. The route's own ceiling is maxDuration=300.
#
# A single 90s attempt was the whole failure: on 2026-09-03 the export moved from
# the retired V8 table (2,473 rows) to the live V9 record (~24k rows), the cold
# rebuild crossed 90s, and the daily refresh failed silently for two days while
# the published dataset sat still. The floor guard below protects against BAD
# data; nothing protected against NO data.
FETCH_TIMEOUT = 240
FETCH_ATTEMPTS = 3

def fetch():
    """Fetch the export, retrying a timeout. A timed-out attempt still leaves the
    origin computing, so the retry usually lands on a warm cache rather than
    repeating the full cold rebuild."""
    req = urllib.request.Request(URL, headers={"User-Agent": "oddsflow-dataset-refresh"})
    for attempt in range(1, FETCH_ATTEMPTS + 1):
        started = time.monotonic()
        try:
            with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as r:
                payload = json.load(r)
            print(f"fetched export in {time.monotonic() - started:.0f}s (attempt {attempt})")
            return payload
        except (TimeoutError, urllib.error.URLError, json.JSONDecodeError) as e:
            waited = time.monotonic() - started
            print(f"attempt {attempt}/{FETCH_ATTEMPTS} failed after {waited:.0f}s: "
                  f"{type(e).__name__}: {e}", file=sys.stderr)
            if attempt == FETCH_ATTEMPTS:
                raise
            time.sleep(15)

def main():
    payload = fetch()

    files = payload.get("files", {})
    summary = payload.get("summary", {})
    snapshot = payload.get("readme_snapshot", "")

    # Floor guard — a header-only/empty CSV or a collapsed row count means the
    # source query is degraded; do NOT overwrite the published dataset.
    bets = int(summary.get("bets", 0))
    all_csv = files.get("all-settled.csv", "")
    if "all-settled.csv" not in files or bets < MIN_BETS or all_csv.count("\n") < MIN_BETS:
        print(f"ABORT: degraded export (bets={bets}, floor={MIN_BETS}). Not overwriting.", file=sys.stderr)
        sys.exit(1)

    DEST.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (DEST / name).write_text(content, encoding="utf-8")
        print(f"wrote {name} ({len(content)} bytes)")

    # Inject the pre-rendered snapshot block (generated from the same summary the
    # CSV is built from — cannot drift).
    readme = DEST / "README.md"
    if readme.exists() and snapshot:
        txt = readme.read_text(encoding="utf-8")
        new = re.sub(r"<!--SNAPSHOT:START-->.*?<!--SNAPSHOT:END-->",
                     f"<!--SNAPSHOT:START-->\n{snapshot}\n<!--SNAPSHOT:END-->",
                     txt, flags=re.DOTALL)
        if new != txt:
            readme.write_text(new, encoding="utf-8")
            print(f"README snapshot injected: {bets} bets, ROI {summary.get('roiPct')}%")
        else:
            print("WARNING: SNAPSHOT markers not found in README — snapshot NOT updated", file=sys.stderr)

if __name__ == "__main__":
    main()
