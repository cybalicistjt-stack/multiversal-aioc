#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P11_CP = ROOT / "governance/ai/work-state/PPIA-11-attempt-001.json"
P16_CP = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
ORIGINAL = ROOT / "scripts/validate-ppia11-completion-contracts.py"
P11_HEAD = "9bf4627f9e8e4a4c21dcc2614dcb74d54d62d724"
P11_MERGE = "f2274707b1337425f0bc9ac8d1dd5ebb08d9f883"
P11_RUN = "31595927902"
P11_PR = 267
P16_HEAD = "eede4bfb530056963a4a595faac54515ff151c3b"
P16_MERGE = "5b87d57d9b06fbb7427b6fae7ca022509f92a5fe"

IMMUTABLE_PATHS = [
    "governance/application-planning/parallel-preimplementation/PPIA-11_SOURCE_MANIFEST_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_ENCOUNTER_BALANCE_TAXONOMY_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_ENCOUNTER_METHODOLOGY_CONTRACT_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_BENCHMARK_ENCOUNTER_SCHEMA_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_BENCHMARK_REFERENCE_CASES_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_ENCOUNTER_LAB_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_ENCOUNTER_LAB_REFERENCE_CASES_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_ENCOUNTER_LAB_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_ENCOUNTER_LAB_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-11_COMPLETION_REPORT.md",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    backlog = load(BACKLOG)
    p16 = next(row for row in backlog["tranches"] if row["work_item_id"] == "PPIA-16")
    if p16["status"] != "completed_verified":
        subprocess.run([sys.executable, str(ORIGINAL)], cwd=ROOT, check=True)
        return 0

    p11 = next(row for row in backlog["tranches"] if row["work_item_id"] == "PPIA-11")
    cp11 = load(P11_CP)
    cp16 = load(P16_CP)
    assert p11["status"] == "completed_verified"
    assert cp11["status"] == "completed_verified"
    assert cp11["latest_pushed_commit"] == P11_HEAD
    assert cp11["merge_commit"] == P11_MERGE
    assert cp11["pull_request"] == P11_PR
    evidence11 = json.dumps({"validation":cp11.get("validation", []),"evidence":cp11.get("evidence", []),"completed":cp11.get("completed_substeps", [])})
    for token in (P11_HEAD, P11_MERGE, P11_RUN, f"#{P11_PR}"):
        assert token in evidence11, f"PPIA-11 completion evidence missing {token}"

    assert cp16["status"] == "completed_verified"
    assert cp16["latest_pushed_commit"] == P16_HEAD
    assert cp16["merge_commit"] == P16_MERGE
    subprocess.run(["git", "cat-file", "-e", f"{P11_MERGE}^{{commit}}"], cwd=ROOT, check=True)
    unchanged = subprocess.run(["git", "diff", "--exit-code", "--quiet", P11_MERGE, "--", *IMMUTABLE_PATHS], cwd=ROOT)
    assert unchanged.returncode == 0, "verified PPIA-11 completion artifacts changed after signed completion merge"
    print("PPIA-11 completion historical validation: PASS")
    print(f"verified_head: {P11_HEAD}")
    print(f"verified_merge: {P11_MERGE}")
    print("final_program_anchor: PPIA-16 completed_verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
