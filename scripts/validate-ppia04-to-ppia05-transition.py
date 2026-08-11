#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
REPORT = BASE / "PPIA-04_COMPLETION_REPORT.md"
P4 = ROOT / "governance/ai/work-state/PPIA-04-attempt-001.json"
P5 = ROOT / "governance/ai/work-state/PPIA-05-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"
PROGRAM = BASE / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"

P4_FINAL_HEAD = "a821f53794d675e73ae71d6c02d577141981ba22"
P4_COMPLETION_MERGE = "e8ec662534820e53fcb8a7d958c0946f494faefd"
P4_TO_P5_TRANSITION_MERGE = "6e9e82252d389f1360e7f1b1191afe5e8c336aa0"
P5_BRANCH = "governance/ppia-05-species-forms-biology"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-04→PPIA-05 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p4 = load(P4)
    p5 = load(P5)
    pointer = load(POINTER)
    status = load(STATUS)
    report = REPORT.read_text(encoding="utf-8")
    roadmap = ROADMAP.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}

    require(backlog["current_work_item_id"] == "PPIA-05", "backlog current item must be PPIA-05")
    require(tranches["PPIA-04"]["status"] == "completed_verified", "PPIA-04 backlog state must be completed_verified")
    require(tranches["PPIA-05"]["status"] in {"started", "in_progress"}, "PPIA-05 backlog state must be active")

    require(p4["status"] == "completed_verified", "PPIA-04 checkpoint must be completed_verified")
    require(p4["active_substep"] is None, "completed PPIA-04 cannot have active substep")
    require(p4["latest_pushed_commit"] == P4_FINAL_HEAD, "PPIA-04 exact final head mismatch")
    require(p4["pull_request"] == 229, "PPIA-04 final PR must be #229")
    require(p4.get("merge_commit") == P4_COMPLETION_MERGE, "PPIA-04 final merge mismatch")
    require(not p4["unresolved_failures"] and p4["owner_decision_required"] is False, "PPIA-04 completion has unresolved state")
    require(any("31524517244" in item.get("command", "") and item.get("status") == "passed" for item in p4["validation"]), "PPIA-04 completion gate evidence missing")

    require(p5["work_item_id"] == "PPIA-05" and p5["attempt_id"] == "PPIA-05-attempt-001", "PPIA-05 checkpoint identity mismatch")
    require(p5["branch"] == P5_BRANCH, "PPIA-05 governed branch mismatch")
    require(p5["status"] in {"started", "in_progress"}, "PPIA-05 checkpoint must be active")
    require(p5["base_commit"] == P4_TO_P5_TRANSITION_MERGE, "PPIA-05 governed branch must start from the canonical PPIA-04→PPIA-05 transition merge")
    require(any(P4_COMPLETION_MERGE in item.get("value", "") for item in p5.get("evidence", [])), "PPIA-05 must preserve PPIA-04 completion merge as dependency evidence")
    require(any(P4_TO_P5_TRANSITION_MERGE in item.get("value", "") for item in p5.get("evidence", [])), "PPIA-05 must preserve the transition merge as branch-start evidence")
    require(p5["active_substep"] and p5["roadmap_projection_pending"] is True, "PPIA-05 must have active source/design substep and pending roadmap projection")

    selected = [item for item in pointer["active_attempts"] if item.get("owner_selected")]
    require(len(selected) == 1, "exactly one owner-selected active attempt required")
    current = selected[0]
    require(pointer["primary_attempt_id"] == "PPIA-05-attempt-001", "primary attempt must be PPIA-05")
    require(current["work_item_id"] == "PPIA-05" and current["checkpoint_path"] == "governance/ai/work-state/PPIA-05-attempt-001.json", "pointer must select PPIA-05 checkpoint")
    for field in ("branch", "status", "updated_at", "roadmap_projection_pending"):
        require(current[field] == p5[field], f"pointer/PPIA-05 checkpoint mismatch: {field}")

    primary = status["primary"]
    for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
        require(primary[field] == p5[field], f"compact status/PPIA-05 checkpoint mismatch: {field}")
    require(primary["latest_pushed_commit"] == p5["latest_pushed_commit"] and primary["pull_request"] == p5["pull_request"], "compact PPIA-05 commit/PR mismatch")

    for value in ("24 retained Vehicle/Mecha/Spacecraft/Operations PDFs / 608 pages", "42 acceptance requirements across 14 categories", P4_FINAL_HEAD, P4_COMPLETION_MERGE, "PPIA-05 — Species, Forms & Character Biology"):
        require(value in report, f"PPIA-04 completion report missing {value!r}")
    for value in ("PPIA-04 — Vehicle, Mecha & Starship Experience", "PPIA-05 — Species, Forms & Character Biology"):
        require(value in roadmap and value in program, f"roadmap/program lost {value}")
    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")

    print("PPIA-04→PPIA-05 TRANSITION: PASS")
    print("ppia04_status=completed_verified")
    print(f"ppia04_final_head={P4_FINAL_HEAD}")
    print(f"ppia04_final_merge={P4_COMPLETION_MERGE}")
    print("ppia05_status=started")
    print(f"ppia05_transition_merge={P4_TO_P5_TRANSITION_MERGE}")
    print(f"ppia05_branch={P5_BRANCH}")
    print("roadmap_projection_pending=true")


if __name__ == "__main__":
    main()
