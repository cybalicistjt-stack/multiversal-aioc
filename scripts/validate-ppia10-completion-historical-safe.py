#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P10_CP = ROOT / "governance/ai/work-state/PPIA-10-attempt-001.json"
P16_CP = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
ORIGINAL = ROOT / "scripts/validate-ppia10-completion-contracts.py"

P10_HEAD = "507c9da21dd74d771f910861323693e2d7193bfa"
P10_RUN = "31585946135"
P10_PR = 261
P10_MERGE = "b4ac8c080af7055e2d150ab6d37de41e9cc2a68f"

IMMUTABLE_PATHS = [
    "governance/application-planning/parallel-preimplementation/PPIA-10_SOURCE_MANIFEST_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-10_RELATIONSHIP_SOCIAL_FACTION_TAXONOMY_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-10_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-10_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-10_REFERENCE_CASES_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-10_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-10_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-10_COMPLETION_REPORT.md",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    backlog = load(BACKLOG)
    tranches = backlog.get("tranches", [])
    p16 = next((row for row in tranches if row.get("work_item_id") == "PPIA-16"), None)

    # While the PPIA sequence is still live, retain the original continuity-sensitive validator.
    if p16 is None or p16.get("status") != "completed_verified":
        subprocess.run([sys.executable, str(ORIGINAL)], cwd=ROOT, check=True)
        return 0

    p10 = next(row for row in tranches if row["work_item_id"] == "PPIA-10")
    cp10 = load(P10_CP)
    cp16 = load(P16_CP)

    assert p10["status"] == "completed_verified"
    assert cp10["status"] == "completed_verified"
    assert cp10["latest_pushed_commit"] == P10_HEAD
    assert cp10["pull_request"] == P10_PR
    assert cp10["merge_commit"] == P10_MERGE
    assert cp10["expected_remote_head"] == P10_MERGE
    assert cp10.get("unresolved_failures", []) == []
    assert cp10.get("owner_decision_required") is False

    evidence = json.dumps({
        "last_verified_action": cp10.get("last_verified_action", ""),
        "completed_substeps": cp10.get("completed_substeps", []),
        "validation": cp10.get("validation", []),
        "evidence": cp10.get("evidence", []),
    })
    for token in (P10_HEAD, P10_RUN, f"#{P10_PR}", P10_MERGE, "37 applicable"):
        assert token in evidence, f"PPIA-10 completion evidence missing {token}"

    assert cp16["status"] == "completed_verified"
    subprocess.run(["git", "cat-file", "-e", f"{P10_MERGE}^{{commit}}"], cwd=ROOT, check=True)
    commit_text = subprocess.check_output(["git", "cat-file", "-p", P10_MERGE], cwd=ROOT, text=True)
    assert "gpgsig -----BEGIN PGP SIGNATURE-----" in commit_text, "PPIA-10 merge commit lacks GitHub signature payload"

    unchanged = subprocess.run(
        ["git", "diff", "--exit-code", "--quiet", P10_MERGE, "--", *IMMUTABLE_PATHS],
        cwd=ROOT,
    )
    assert unchanged.returncode == 0, "verified PPIA-10 substantive artifacts changed after signed completion merge"

    print("PPIA-10 completion historical validation: PASS")
    print(f"verified_head: {P10_HEAD}")
    print(f"verified_run: {P10_RUN}")
    print(f"verified_pr: #{P10_PR}")
    print(f"verified_merge: {P10_MERGE}")
    print("merge_signature_payload: present")
    print("final_program_anchor: PPIA-16 completed_verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
