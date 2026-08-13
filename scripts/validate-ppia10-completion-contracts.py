#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKLOG = ROOT / "governance/application-planning/parallel-preimplementation/PPIA_PROGRAM_BACKLOG.json"
LIVE = ROOT / "scripts/validate-ppia10-completion-live.py"
HISTORICAL = ROOT / "scripts/validate-ppia10-completion-historical-safe.py"


def main() -> int:
    backlog = json.loads(BACKLOG.read_text(encoding="utf-8"))
    p16 = next((row for row in backlog.get("tranches", []) if row.get("work_item_id") == "PPIA-16"), None)
    target = HISTORICAL if p16 and p16.get("status") == "completed_verified" else LIVE
    return subprocess.call([sys.executable, str(target)], cwd=ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
