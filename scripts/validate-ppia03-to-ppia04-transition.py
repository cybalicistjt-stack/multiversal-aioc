#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
REPORT = BASE / "PPIA-03_COMPLETION_REPORT.md"
P3 = ROOT / "governance/ai/work-state/PPIA-03-attempt-001.json"
P4 = ROOT / "governance/ai/work-state/PPIA-04-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"
PROGRAM = BASE / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-03→PPIA-04 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p3 = load(P3)
    p4 = load(P4)
    pointer = load(POINTER)
    status = load(STATUS)
    report = REPORT.read_text(encoding="utf-8")
    roadmap = ROADMAP.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")

    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}
    require(backlog["current_work_item_id"] == "PPIA-04", "backlog current item must be PPIA-04")
    require(tranches["PPIA-03"]["status"] == "completed_verified", "PPIA-03 backlog state must be completed_verified")
    require(tranches["PPIA-04"]["status"] == "started", "PPIA-04 backlog state must be started")

    require(p3["status"] == "completed_verified", "PPIA-03 checkpoint must be completed_verified")
    require(p3["completed_at"] == "2026-08-11T17:38:18+00:00", "PPIA-03 completion time mismatch")
    require(p3["active_substep"] is None, "completed PPIA-03 cannot have active substep")
    require(p3["latest_pushed_commit"] == "c1e00ebf67fe4c78af2ce6e1dd483bb699706047", "PPIA-03 exact final validated head mismatch")
    require(p3["pull_request"] == 224, "PPIA-03 final PR must be #224")
    require(p3["merge_commit"] == "ea08234b9d6bcd4cb942c2de964639b330d9511e", "PPIA-03 final merge mismatch")
    require(p3["roadmap_projection_pending"] is True, "PPIA-03 roadmap projection should be batched/pending")
    require(not p3["unresolved_failures"] and p3["owner_decision_required"] is False, "PPIA-03 completion has unresolved state")
    for run_id in ("31518534709", "31518534704", "31518534758", "31518534698"):
        require(any(run_id in item.get("command", "") and item.get("status") == "passed" for item in p3["validation"]), f"PPIA-03 missing passed run {run_id}")

    require(p4["status"] == "started", "PPIA-04 checkpoint must be started")
    require(p4["work_item_id"] == "PPIA-04" and p4["attempt_id"] == "PPIA-04-attempt-001", "PPIA-04 checkpoint identity mismatch")
    require(p4["branch"] == "governance/ppia-04-vehicle-mecha-starship", "PPIA-04 branch mismatch")
    require(p4["base_commit"] == "ea08234b9d6bcd4cb942c2de964639b330d9511e", "PPIA-04 must start from PPIA-03 completion merge")
    require(p4["expected_remote_head"] == "ea08234b9d6bcd4cb942c2de964639b330d9511e", "PPIA-04 provisional expected head mismatch")
    require(p4["active_substep"], "PPIA-04 needs active substep")
    require(p4["roadmap_projection_pending"] is True, "PPIA-04 roadmap projection must be pending until batched projection")

    selected = [item for item in pointer["active_attempts"] if item.get("owner_selected")]
    require(len(selected) == 1, "exactly one owner-selected active attempt required")
    current = selected[0]
    require(pointer["primary_attempt_id"] == "PPIA-04-attempt-001", "primary attempt must be PPIA-04")
    require(current["work_item_id"] == "PPIA-04", "selected work item must be PPIA-04")
    require(current["checkpoint_path"] == "governance/ai/work-state/PPIA-04-attempt-001.json", "selected checkpoint path mismatch")
    for field in ("branch", "status", "updated_at", "roadmap_projection_pending"):
        require(current[field] == p4[field], f"pointer/PPIA-04 checkpoint mismatch: {field}")

    primary = status["primary"]
    for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
        require(primary[field] == p4[field], f"compact status/PPIA-04 checkpoint mismatch: {field}")
    require(primary["latest_pushed_commit"] == p4["latest_pushed_commit"], "compact latest commit mismatch")
    require(primary["pull_request"] == p4["pull_request"], "compact PR mismatch")

    for value in (
        "2aa3ae590dab59710e0bfaab398db19d376b6490",
        "b00aeab9f3ad4cb66869968c3584e969e132a700",
        "c2cb92857e1beb79208790b13f92d46bad769df3",
        "c1e00ebf67fe4c78af2ce6e1dd483bb699706047",
        "ea08234b9d6bcd4cb942c2de964639b330d9511e",
        "31518534709",
        "40 acceptance requirements across 15 categories",
        "PPIA-04 — Vehicle, Mecha & Starship Experience",
    ):
        require(value in report, f"completion report missing {value!r}")

    require("PPIA-03 — Items, Equipment & Inventory Experience" in roadmap, "roadmap must retain PPIA-03 milestone")
    require("PPIA-04 — Vehicle, Mecha & Starship Experience" in roadmap, "roadmap must retain PPIA-04 tranche")
    require("PPIA-03 — Items, Equipment & Inventory Experience" in program, "program must retain PPIA-03 tranche")
    require("PPIA-04 — Vehicle, Mecha & Starship Experience" in program, "program must retain PPIA-04 tranche")
    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")

    print("PPIA-03→PPIA-04 TRANSITION: PASS")
    print("ppia03_status=completed_verified")
    print("ppia03_final_pr=224")
    print("ppia03_final_merge=ea08234b9d6bcd4cb942c2de964639b330d9511e")
    print("ppia04_status=started")
    print("ppia04_branch=governance/ppia-04-vehicle-mecha-starship")
    print("roadmap_projection_pending=true")


if __name__ == "__main__":
    main()
