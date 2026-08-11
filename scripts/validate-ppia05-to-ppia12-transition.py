#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
P5 = ROOT / "governance/ai/work-state/PPIA-05-attempt-001.json"
P12 = ROOT / "governance/ai/work-state/PPIA-12-attempt-001.json"
P5_REPORT = BASE / "PPIA-05_COMPLETION_REPORT.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"

P5_FINAL_HEAD = "e6e2bcfd0f22f537a73721dfd8069531bd1af24c"
P5_COMPLETION_MERGE = "0ffaa34ef15f9a7e4b77776688c6be3fc3047446"
P5_TO_P12_TRANSITION_MERGE = "17dc6be36960b65bbcef5c4382b67de75c05218c"
P12_FINAL_HEAD = "ae3d538e85e09e52681df5a05bd8ee343aa5e908"
P12_COMPLETION_MERGE = "0ed9f9a0c53b2a132d8f38c0d3cae22cc7ae14a0"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    p5 = load(P5)
    p12 = load(P12)
    backlog = load(BACKLOG)
    report = P5_REPORT.read_text(encoding="utf-8")
    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}

    assert p5["status"] == "completed_verified"
    assert p5["latest_pushed_commit"] == P5_FINAL_HEAD
    assert p5["pull_request"] == 234 and p5["merge_commit"] == P5_COMPLETION_MERGE
    assert P5_TO_P12_TRANSITION_MERGE in json.dumps(p12)
    assert p12["status"] == "completed_verified"
    assert p12["latest_pushed_commit"] == P12_FINAL_HEAD
    assert p12["pull_request"] == 239 and p12["merge_commit"] == P12_COMPLETION_MERGE
    assert tranches["PPIA-05"]["status"] == "completed_verified"
    assert tranches["PPIA-12"]["status"] == "completed_verified"
    assert "29 direct Species/Form/Biology PDFs / 654 pages" in report
    assert "42 acceptance requirements across 14 categories" in report
    assert P5_FINAL_HEAD in report and P5_COMPLETION_MERGE in report

    print("PPIA-05→PPIA-12 HISTORICAL TRANSITION: PASS")
    print(f"ppia05_final_merge={P5_COMPLETION_MERGE}")
    print(f"ppia12_transition_merge={P5_TO_P12_TRANSITION_MERGE}")
    print(f"ppia12_final_merge={P12_COMPLETION_MERGE}")


if __name__ == "__main__":
    main()
