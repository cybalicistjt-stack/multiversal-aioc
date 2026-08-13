#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P14_CP = ROOT / "governance/ai/work-state/PPIA-14-attempt-001.json"
P15_CP = ROOT / "governance/ai/work-state/PPIA-15-attempt-001.json"
P16_CP = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
ORIGINAL = ROOT / "scripts/validate-ppia14-to-ppia15-transition.py"

P14_HEAD = "34c4575ad4ec7dad705b5e292b11c94699a648ac"
P14_RUN = "31646879101"
P14_PR = 284
P14_MERGE = "2bebbfcfeac78081ab942be1a15eab1745d35c3a"
TRANSITION_HEAD = "da5857e217425fbc637ecdc2447b0a309e3c771e"
TRANSITION_RUN = "31648209814"
TRANSITION_PR = 285
TRANSITION_MERGE = "f08d90a1dca686da9c86913f0635f206758b5da7"
P15_FOUNDATION_HEAD = "d876093989e656d3cf8366c19755295ef0f785e8"
P15_FOUNDATION_RUN = "31652241636"
P15_FOUNDATION_PR = 286
P15_FOUNDATION_MERGE = "a1f6b7380a07e65469ba8072e8aa4135d7b1e42f"
P15_HEAD = "6480e22d142e018fb1722570411baa8cd29a41ea"
P15_RUN = "31679948031"
P15_PR = 289
P15_MERGE = "1ec15976e662de466ec301caa20462640138bc13"
P16_HEAD = "eede4bfb530056963a4a595faac54515ff151c3b"
P16_MERGE = "5b87d57d9b06fbb7427b6fae7ca022509f92a5fe"

IMMUTABLE_PATHS = [
    "governance/application-planning/parallel-preimplementation/PPIA-14_COMPLETION_REPORT.md",
    "governance/application-planning/parallel-preimplementation/PPIA-14_COMPLETION_PACKAGE_INDEX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-15_FOUNDATION_EXISTING_TEST_CORPUS_AND_COVERAGE_GAP_INVENTORY.md",
    "governance/application-planning/parallel-preimplementation/PPIA-15_FOUNDATION_PACKAGE_INDEX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-15_COMPLETION_REPORT.md",
    "governance/application-planning/parallel-preimplementation/PPIA-15_COMPLETION_PACKAGE_INDEX_v0.1.0.json",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require_token(payload: str, token: str, label: str) -> None:
    assert token in payload, f"missing {label}: {token}"


def main() -> int:
    backlog = load(BACKLOG)
    p16_row = next(row for row in backlog["tranches"] if row["work_item_id"] == "PPIA-16")
    if p16_row["status"] != "completed_verified":
        subprocess.run([sys.executable, str(ORIGINAL)], cwd=ROOT, check=True)
        return 0

    p14 = load(P14_CP)
    p15 = load(P15_CP)
    p16 = load(P16_CP)
    rows = {row["work_item_id"]: row for row in backlog["tranches"]}
    assert rows["PPIA-14"]["status"] == "completed_verified"
    assert rows["PPIA-15"]["status"] == "completed_verified"
    assert rows["PPIA-16"]["status"] == "completed_verified"

    assert p14["status"] == "completed_verified"
    assert p14["latest_pushed_commit"] == P14_HEAD
    assert p14["pull_request"] == P14_PR
    assert p14["merge_commit"] == P14_MERGE
    p14_text = json.dumps(p14, ensure_ascii=False)
    for token, label in ((P14_HEAD,"PPIA-14 head"),(P14_RUN,"PPIA-14 run"),(P14_MERGE,"PPIA-14 merge"),(f"#{P14_PR}","PPIA-14 PR")):
        require_token(p14_text, token, label)

    assert p15["status"] == "completed_verified"
    assert p15["latest_pushed_commit"] == P15_HEAD
    assert p15["pull_request"] == P15_PR
    assert p15["merge_commit"] == P15_MERGE
    p15_text = json.dumps(p15, ensure_ascii=False)
    for token, label in (
        (TRANSITION_HEAD,"transition head"),(TRANSITION_RUN,"transition run"),(TRANSITION_MERGE,"transition merge"),(f"#{TRANSITION_PR}","transition PR"),
        (P15_FOUNDATION_HEAD,"PPIA-15 Foundation head"),(P15_FOUNDATION_RUN,"PPIA-15 Foundation run"),(P15_FOUNDATION_MERGE,"PPIA-15 Foundation merge"),(f"#{P15_FOUNDATION_PR}","PPIA-15 Foundation PR"),
        (P15_HEAD,"PPIA-15 completion head"),(P15_RUN,"PPIA-15 completion run"),(P15_MERGE,"PPIA-15 completion merge"),(f"#{P15_PR}","PPIA-15 completion PR"),
    ):
        require_token(p15_text, token, label)

    assert p16["status"] == "completed_verified"
    assert p16["latest_pushed_commit"] == P16_HEAD
    assert p16["merge_commit"] == P16_MERGE

    subprocess.run(["git", "cat-file", "-e", f"{P15_MERGE}^{{commit}}"], cwd=ROOT, check=True)
    unchanged = subprocess.run(["git", "diff", "--exit-code", "--quiet", P15_MERGE, "--", *IMMUTABLE_PATHS], cwd=ROOT)
    assert unchanged.returncode == 0, "verified PPIA-14/PPIA-15 completion artifacts changed after signed PPIA-15 completion merge"

    print("PPIA-14→PPIA-15 historical transition validation: PASS")
    print(f"transition_head: {TRANSITION_HEAD}")
    print(f"transition_merge: {TRANSITION_MERGE}")
    print(f"ppia15_final_merge: {P15_MERGE}")
    print("final_program_anchor: PPIA-16 completed_verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
