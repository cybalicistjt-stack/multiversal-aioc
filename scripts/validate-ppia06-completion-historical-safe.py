#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P06_CP = ROOT / "governance/ai/work-state/PPIA-06-attempt-001.json"
P16_CP = ROOT / "governance/ai/work-state/PPIA-16-attempt-001.json"
ORIGINAL = ROOT / "scripts/validate-ppia06-completion-contracts.py"
P06_HEAD = "6d2da6fb5a7c2d62492de895c6a9c7a1fe970a06"
P06_MERGE = "ffce4859a8912813021776c4f5825c3d219bb0f2"
P06_RUN = "31622184027"
P06_PR = 273

IMMUTABLE_PATHS = [
    "governance/application-planning/parallel-preimplementation/PPIA-06_COMPLETION_SCOPE_LOCK_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_COMPLETION_PACKAGE_INDEX_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_COMPLETION_REPORT.md",
    "governance/application-planning/parallel-preimplementation/PPIA-06_COMPLETION_README.md",
    "governance/application-planning/parallel-preimplementation/PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_APPEARANCE_STUDIO_CONTROL_SURFACE_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_OWNER_VISUAL_CANON_DECISIONS_v0.1.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_SPECIES_VISUAL_COVERAGE_MATRIX_v0.2.0.json",
    "governance/application-planning/parallel-preimplementation/PPIA-06_PIXEL_ART_RENDERER_CONTRACT_v0.2.0.json",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    backlog = load(BACKLOG)
    p16 = next((row for row in backlog.get("tranches", []) if row.get("work_item_id") == "PPIA-16"), None)
    if p16 is None or p16.get("status") != "completed_verified":
        subprocess.run([sys.executable, str(ORIGINAL)], cwd=ROOT, check=True)
        return 0

    p06 = next(row for row in backlog["tranches"] if row["work_item_id"] == "PPIA-06")
    cp06 = load(P06_CP)
    cp16 = load(P16_CP)
    assert p06["status"] == "completed_verified"
    assert cp06["status"] == "completed_verified"
    assert cp06["latest_pushed_commit"] == P06_HEAD
    assert cp06["merge_commit"] == P06_MERGE
    assert cp06["pull_request"] == P06_PR
    assert cp06.get("unresolved_failures", []) == []
    evidence = json.dumps({
        "validation": cp06.get("validation", []),
        "evidence": cp06.get("evidence", []),
        "completed": cp06.get("completed_substeps", []),
        "last_verified_action": cp06.get("last_verified_action", ""),
    })
    for token in (P06_HEAD, P06_MERGE, P06_RUN, f"#{P06_PR}"):
        assert token in evidence, f"PPIA-06 completion evidence missing {token}"
    assert "signed/verified valid" in cp06.get("last_verified_action", "")
    assert cp16["status"] == "completed_verified"
    subprocess.run(["git", "cat-file", "-e", f"{P06_MERGE}^{{commit}}"], cwd=ROOT, check=True)
    unchanged = subprocess.run(["git", "diff", "--exit-code", "--quiet", P06_MERGE, "--", *IMMUTABLE_PATHS], cwd=ROOT)
    assert unchanged.returncode == 0, "verified PPIA-06 completion/data artifacts changed after signed completion merge"
    print("PPIA-06 completion historical validation: PASS")
    print(f"verified_head: {P06_HEAD}")
    print(f"verified_run: {P06_RUN}")
    print(f"verified_pr: #{P06_PR}")
    print(f"verified_merge: {P06_MERGE}")
    print("final_program_anchor: PPIA-16 completed_verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
