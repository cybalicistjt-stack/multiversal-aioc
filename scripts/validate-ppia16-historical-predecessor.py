#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
COMPLETION = BASE / "PPIA-16_COMPLETION_PACKAGE_INDEX_v0.1.0.json"

STAGES = {
    "transition": {
        "script": ROOT / "scripts/validate-ppia15-to-ppia16-transition.py",
        "milestone": "ppia15_to_ppia16_transition",
        "head": "21054af7b372d2216097e91bd32efe9298ec8a9d",
        "merge": "87ee7795de362059d92a76e3923e2a7f8d182124",
        "run": "31682807809",
        "pr": 290,
        "workflows": 66,
        "immutable_paths": [],
    },
    "foundation": {
        "script": ROOT / "scripts/validate-ppia16-foundation.py",
        "milestone": "foundation_existing_toolbelt_and_control_surface_authority_inventory",
        "head": "8e0650fb9ab237ec3f1b1fe9152de42ee6f7c889",
        "merge": "015f200595fd6e8ba5da85a2956ee1c9dc8fb15b",
        "run": "31685859485",
        "pr": 291,
        "workflows": 67,
        "immutable_paths": [
            "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_EXISTING_TOOLBELT_AND_CONTROL_SURFACE_AUTHORITY_INVENTORY.md",
            "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_PACKAGE_INDEX_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_AUTHORITY_AND_STATUS_MODEL_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_TOOLBELT_AND_AUTHORITY_INVENTORY_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_SCREEN_WORKFLOW_COVERAGE_MAP_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_FOUNDATION_INFORMATION_ARCHITECTURE_v0.1.0.json",
            "scripts/validate-ppia16-foundation.py",
        ],
    },
    "screen": {
        "script": ROOT / "scripts/validate-ppia16-screen-action-reference.py",
        "milestone": "screen_states_action_contracts_reference_cases",
        "head": "45e7e34b6bf7de0ca2ebff4b2818bdb1007f04c5",
        "merge": "be811bd4508954700a83032b285107a8bd0d019a",
        "run": "31689903909",
        "pr": 292,
        "workflows": 68,
        "immutable_paths": [
            "governance/application-planning/parallel-preimplementation/PPIA-16_SCREEN_ACTION_REFERENCE_CONTRACT.md",
            "governance/application-planning/parallel-preimplementation/PPIA-16_SCREEN_ACTION_REFERENCE_PACKAGE_INDEX_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_SCREEN_STATE_CONTRACTS_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_ACTION_CONTRACTS_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_COMPONENT_INTERACTION_CONTRACTS_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_SCREEN_ACTION_REFERENCE_CASES_v0.1.0.json",
            "scripts/validate-ppia16-screen-action-reference.py",
        ],
    },
    "integrated": {
        "script": ROOT / "scripts/validate-ppia16-integrated-screen-workflow-traceability.py",
        "milestone": "integrated_screen_workflow_traceability",
        "head": "d9b46fb71bcb71504308429ebf96c6ac5afd1811",
        "merge": "e5253e6cd08c3a053a6b9e8d99592faa652d7798",
        "run": "31692631899",
        "pr": 293,
        "workflows": 69,
        "immutable_paths": [
            "governance/application-planning/parallel-preimplementation/PPIA-16_INTEGRATED_SCREEN_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_INTEGRATED_SCREEN_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_INTEGRATED_SCREEN_WORKFLOW_REFERENCE_CASES_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_INTEGRATED_SCREEN_WORKFLOW_PACKAGE_INDEX_v0.1.0.json",
            "governance/application-planning/parallel-preimplementation/PPIA-16_INTEGRATED_SCREEN_WORKFLOW_CANDIDATE.md",
            "scripts/validate-ppia16-integrated-screen-workflow-traceability.py",
        ],
    },
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_immutable_since_merge(merge: str, paths: list[str]) -> None:
    if not paths:
        return
    subprocess.run(["git", "cat-file", "-e", f"{merge}^{{commit}}"], cwd=ROOT, check=True)
    result = subprocess.run(["git", "diff", "--exit-code", "--quiet", merge, "--", *paths], cwd=ROOT)
    assert result.returncode == 0, f"verified predecessor artifacts changed after {merge}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("stage", choices=sorted(STAGES))
    args = parser.parse_args()
    expected = STAGES[args.stage]
    backlog = load(BACKLOG)
    p16 = next(row for row in backlog["tranches"] if row["work_item_id"] == "PPIA-16")

    if p16["status"] != "completed_verified":
        subprocess.run([sys.executable, str(expected["script"])], cwd=ROOT, check=True)
        return 0

    checkpoint = load(CHECKPOINT)
    completion = load(COMPLETION)
    assert checkpoint["status"] == "completed_verified"
    assert checkpoint["latest_pushed_commit"] == "eede4bfb530056963a4a595faac54515ff151c3b"
    assert checkpoint["merge_commit"] == "5b87d57d9b06fbb7427b6fae7ca022509f92a5fe"
    rows = {row["milestone"]: row for row in completion["verified_milestones"]}
    row = rows[expected["milestone"]]
    assert row["validated_head"] == expected["head"]
    assert row["merge"] == expected["merge"]
    assert row["dedicated_run"] == expected["run"]
    assert row["pull_request"] == expected["pr"]
    assert row["hosted_workflows"] == expected["workflows"]
    evidence_text = json.dumps({"completed":checkpoint["completed_substeps"],"validation":checkpoint["validation"],"evidence":checkpoint["evidence"]})
    for token in (expected["head"], expected["merge"], expected["run"], f"#{expected['pr']}"):
        assert token in evidence_text
    assert_immutable_since_merge(expected["merge"], expected["immutable_paths"])
    print(f"PPIA-16 historical predecessor validation: PASS ({args.stage})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
