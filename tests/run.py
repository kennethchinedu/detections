import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
ZIRCOLITE = Path(sys.argv[1]) / "zircolite.py"
CONFIG = ROOT / "tests" / "zircolite.yaml"


def rule_id(rule_file):
    docs = [d for d in yaml.safe_load_all(rule_file.read_text()) if d]
    return docs[-1]["id"]


def fired(rule_file, fixture, tmp):
    events = json.loads(fixture.read_text())
    if isinstance(events, dict):
        events = [events]
    jsonl = tmp / "events.json"
    jsonl.write_text("\n".join(json.dumps(e) for e in events) + "\n")
    out = tmp / "out.json"
    out.unlink(missing_ok=True)
    subprocess.run(
        [sys.executable, str(ZIRCOLITE),
         "--events", str(jsonl), "--json-input",
         "--ruleset", str(rule_file),
         "--config", str(CONFIG),
         "--timefield", "eventTime",
         "--no-event-filter",
         "--outfile", str(out)],
        check=True, cwd=ZIRCOLITE.parent,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    detections = json.loads(out.read_text()) if out.exists() else []
    return any(d.get("id") == rule_id(rule_file) for d in detections)


def main():
    failures = 0
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        for case in sorted((ROOT / "tests" / "fixtures").iterdir()):
            rule = ROOT / "rules" / "aws" / f"{case.name}.yml"
            pos = fired(rule, case / "positive.json", tmp)
            neg = fired(rule, case / "negative.json", tmp)
            status = "ok" if pos and not neg else "FAIL"
            if not pos:
                status += "  missed the attack"
            if neg:
                status += "  fired on benign event"
            print(f"{status:<40} {case.name}")
            failures += status != "ok"
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
