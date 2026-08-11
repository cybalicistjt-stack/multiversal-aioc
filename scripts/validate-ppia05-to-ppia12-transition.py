#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
REPORT = BASE / "PPIA-05_COMPLETION_REPORT.md"
P5 = ROOT / "governance/ai/work-state/PPIA-05-attempt-001.json"
P12 = ROOT / "governance/ai/work-state/PPIA-12-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
ROADMAP = ROOT / "governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md"
PROGRAM = BASE / "PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md"

P5_FINAL_HEAD = "e6e2bcfd0f22f537a73721dfd8069531bd1af24c"
P5_COMPLETION_MERGE = "0ffaa34ef15f9a7e4b77776688c6be3fc3047446"
P5_TO_P12_TRANSITION_MERGE = "17dc6be36960b65bbcef5c4382b67de75c05218c"
P12_BRANCH = "governance/ppia-12-world-setting-authoring"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-05→PPIA-12 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p5 = load(P5)
    p12 = load(P12)
    pointer = load(POINTER)
    status = load(STATUS)
    report = REPORT.read_text(encoding="utf-8")
    roadmap = ROADMAP.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")
    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}

    require(backlog["current_work_item_id"] == "PPIA-12", "backlog current item must be PPIA-12")
    for work_item in ("PPIA-01", "PPIA-02", "PPIA-03", "PPIA-04", "PPIA-05"):
        require(tranches[work_item]["status"] in {"complete", "completed", "completed_verified"}, f"{work_item} dependency must be complete")
    require(tranches["PPIA-05"]["status"] == "completed_verified", "PPIA-05 backlog state must be completed_verified")
    require(tranches["PPIA-12"]["status"] in {"started", "in_progress"}, "PPIA-12 backlog state must be active")

    require(p5["status"] == "completed_verified" and p5["active_substep"] is None, "PPIA-05 checkpoint must be completed_verified")
    require(p5["latest_pushed_commit"] == P5_FINAL_HEAD, "PPIA-05 exact final head mismatch")
    require(p5["pull_request"] == 234 and p5.get("merge_commit") == P5_COMPLETION_MERGE, "PPIA-05 final PR/merge mismatch")
    require(not p5["unresolved_failures"] and p5["owner_decision_required"] is False, "PPIA-05 completion has unresolved state")
    require(any("31529821441" in item.get("command", "") and item.get("status") == "passed" for item in p5["validation"]), "PPIA-05 completion gate evidence missing")

    require(p12["work_item_id"] == "PPIA-12" and p12["attempt_id"] == "PPIA-12-attempt-001", "PPIA-12 checkpoint identity mismatch")
    require(p12["branch"] == P12_BRANCH, "PPIA-12 governed branch mismatch")
    require(p12["status"] in {"started", "in_progress"}, "PPIA-12 checkpoint must be active")
    require(p12["base_commit"] == P5_TO_P12_TRANSITION_MERGE, "PPIA-12 governed branch must anchor to the canonical PPIA-05→PPIA-12 transition merge")
    require(any(P5_COMPLETION_MERGE in item.get("value", "") for item in p12.get("evidence", [])), "PPIA-12 must preserve PPIA-05 completion merge evidence")
    require(any(P5_TO_P12_TRANSITION_MERGE in item.get("value", "") for item in p12.get("evidence", [])), "PPIA-12 must preserve transition merge evidence")
    require(p12["active_substep"] and p12["roadmap_projection_pending"] is True, "PPIA-12 must have active source/design substep and pending roadmap projection")

    selected = [item for item in pointer["active_attempts"] if item.get("owner_selected")]
    require(len(selected) == 1, "exactly one owner-selected active attempt required")
    current = selected[0]
    require(pointer["primary_attempt_id"] == "PPIA-12-attempt-001", "primary attempt must be PPIA-12")
    require(current["work_item_id"] == "PPIA-12" and current["checkpoint_path"] == "governance/ai/work-state/PPIA-12-attempt-001.json", "pointer must select PPIA-12 checkpoint")
    for field in ("branch", "status", "updated_at", "roadmap_projection_pending"):
        require(current[field] == p12[field], f"pointer/PPIA-12 checkpoint mismatch: {field}")

    primary = status["primary"]
    for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
        require(primary[field] == p12[field], f"compact status/PPIA-12 checkpoint mismatch: {field}")
    require(primary["latest_pushed_commit"] == p12["latest_pushed_commit"] and primary["pull_request"] == p12["pull_request"], "compact PPIA-12 commit/PR mismatch")

    for value in ("29 direct Species/Form/Biology PDFs / 654 pages", "42 acceptance requirements across 14 categories", P5_FINAL_HEAD, P5_COMPLETION_MERGE, "PPIA-12 — World & Setting Authoring System"):
        require(value in report, f"PPIA-05 completion report missing {value!r}")
    for value in ("PPIA-05 — Species, Forms & Character Biology", "PPIA-12 — World & Setting Authoring System"):
        require(value in roadmap and value in program, f"roadmap/program lost {value}")
    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")

    print("PPIA-05→PPIA-12 TRANSITION: PASS")
    print("ppia05_status=completed_verified")
    print(f"ppia05_final_head={P5_FINAL_HEAD}")
    print(f"ppia05_final_merge={P5_COMPLETION_MERGE}")
    print("ppia12_status=started")
    print(f"ppia12_transition_merge={P5_TO_P12_TRANSITION_MERGE}")
    print(f"ppia12_branch={P12_BRANCH}")
    print("roadmap_projection_pending=true")


if __name__ == "__main__":
    main()
