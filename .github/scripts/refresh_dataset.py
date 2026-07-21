#!/usr/bin/env python3
"""Pull the latest settled-predictions CSVs from OddsFlow's public export
endpoint and write them into datasets/settled-predictions/. Also refreshes the
snapshot numbers in the dataset README. Read-only fetch; no secrets."""
import json, os, sys, urllib.request, re, pathlib

URL = os.environ.get("EXPORT_URL", "https://www.oddsflow.ai/api/v1/settled-export")
DEST = pathlib.Path("datasets/settled-predictions")

def main():
    req = urllib.request.Request(URL, headers={"User-Agent": "oddsflow-dataset-refresh"})
    with urllib.request.urlopen(req, timeout=90) as r:
        payload = json.load(r)

    files = payload.get("files", {})
    if not files or "all-settled.csv" not in files:
        print("No files in export payload; aborting.", file=sys.stderr)
        sys.exit(1)

    DEST.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (DEST / name).write_text(content, encoding="utf-8")
        print(f"wrote {name} ({len(content)} bytes)")

    # Refresh the README snapshot table from the summary
    s = payload.get("summary", {})
    readme = DEST / "README.md"
    if readme.exists() and s:
        txt = readme.read_text(encoding="utf-8")
        repl = {
            r"\| Settled bets \| [\d,]+ \|": f"| Settled bets | {s['bets']:,} |",
            r"\| Won / Lost / Half or Push \| [\d/ ]+\|": f"| Won / Lost / Half or Push | {s['won']} / {s['lost']} / {s['bets']-s['won']-s['lost']} |",
            r"\| \*\*Net profit/loss\*\* \| \*\*[+\-][\d,]+ units\*\* \|": f"| **Net profit/loss** | **{'+' if s['netPl']>=0 else ''}{round(s['netPl']):,} units** |",
            r"\| \*\*ROI\*\* \| \*\*[+\-][\d.]+%\*\* \|": f"| **ROI** | **{'+' if s['roiPct']>=0 else ''}{s['roiPct']}%** |",
            r"\| Matches / Competitions \| [\d/ ]+\|": f"| Matches / Competitions | {s['matches']} / 20 |",
        }
        for pat, sub in repl.items():
            txt = re.sub(pat, sub, txt)
        readme.write_text(txt, encoding="utf-8")
        print(f"README snapshot refreshed: {s['bets']} bets, ROI {s['roiPct']}%")

if __name__ == "__main__":
    main()
