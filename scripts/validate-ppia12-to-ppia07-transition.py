#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
REPORT = BASE / "PPIA-12_COMPLETION_REPORT.md"
P12 = ROOT / "governance/ai/work-state/PPIA-12-attempt-001.json"
P7 = ROOT / "governance/ai/work-state/PPIA-07-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

P12_FINAL_HEAD = "ae3d538e85e09e52681df5a05bd8ee343aa5e908"
P12_COMPLETION_MERGE = "0ed9f9a0c53b2a132d8f38c0d3cae22cc7ae14a0"
P7_BRANCH = "governance/ppia-07-rune-construction-rpg-system"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-12→PPIA-07 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p12 = load(P12)
    p7 = load(P7)
    pointer = load(POINTER)
    status = load(STATUS)
    report = REPORT.read_text(encoding="utf-8")
    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}

    require(backlog["current_work_item_id"] == "PPIA-07", "backlog current item must be PPIA-07")
    for work_item in ("PPIA-01", "PPIA-02", "PPIA-03", "PPIA-04", "PPIA-05", "PPIA-12"):
        require(tranches[work_item]["status"] in {"complete", "completed", "completed_verified"}, f"{work_item} must be complete before PPIA-07")
    require(tranches["PPIA-12"]["status"] == "completed_verified", "PPIA-12 backlog state must be completed_verified")
    require(tranches["PPIA-07"]["status"] in {"started", "in_progress"}, "PPIA-07 backlog state must be active")

    require(p12["status"] == "completed_verified" and p12["active_substep"] is None, "PPIA-12 checkpoint must be completed_verified")
    require(p12["latest_pushed_commit"] == P12_FINAL_HEAD, "PPIA-12 exact final head mismatch")
    require(p12["pull_request"] == 239 and p12["merge_commit"] == P12_COMPLETION_MERGE, "PPIA-12 final PR/merge mismatch")
    require(not p12["unresolved_failures"] and p12["owner_decision_required"] is False, "PPIA-12 completion has unresolved state")
    require(any("31536379370" in item.get("command", "") and item.get("status") == "passed" for item in p12["validation"]), "PPIA-12 completion gate evidence missing")

    require(p7["work_item_id"] == "PPIA-07" and p7["attempt_id"] == "PPIA-07-attempt-001", "PPIA-07 checkpoint identity mismatch")
    require(p7["branch"] == P7_BRANCH, "PPIA-07 governed branch mismatch")
    require(p7["status"] in {"started", "in_progress"}, "PPIA-07 checkpoint must be active")
    require(any(P12_COMPLETION_MERGE in item.get("value", "") for item in p7.get("evidence", [])), "PPIA-07 must preserve PPIA-12 completion merge evidence")
    require(p7["active_substep"] and p7["roadmap_projection_pending"] is True, "PPIA-07 must have active source/design substep and pending roadmap projection")

    selected = [item for item in pointer["active_attempts"] if item.get("owner_selected")]
    require(len(selected) == 1, "exactly one owner-selected active attempt required")
    current = selected[0]
    require(pointer["primary_attempt_id"] == "PPIA-07-attempt-001", "primary attempt must be PPIA-07")
    require(current["work_item_id"] == "PPIA-07" and current["checkpoint_path"] == "governance/ai/work-state/PPIA-07-attempt-001.json", "pointer must select PPIA-07 checkpoint")
    for field in ("branch", "status", "updated_at", "roadmap_projection_pending"):
        require(current[field] == p7[field], f"pointer/PPIA-07 checkpoint mismatch: {field}")

    primary = status["primary"]
    for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
        require(primary[field] == p7[field], f"compact status/PPIA-07 checkpoint mismatch: {field}")
    require(primary["latest_pushed_commit"] == p7["latest_pushed_commit"] and primary["pull_request"] == p7["pull_request"], "compact PPIA-07 commit/PR mismatch")

    for value in ("32 retained PDFs / 961 pages total", "48 acceptance requirements across 16 categories", P12_FINAL_HEAD, P12_COMPLETION_MERGE, "PPIA-07 — Rune Construction RPG System"):
        require(value in report, f"PPIA-12 completion report missing {value!r}")
    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")

    print("PPIA-12→PPIA-07 TRANSITION: PASS")
    print("ppia12_status=completed_verified")
    print(f"ppia12_final_head={P12_FINAL_HEAD}")
    print(f"ppia12_final_merge={P12_COMPLETION_MERGE}")
    print("ppia07_status=started")
    print(f"ppia07_branch={P7_BRANCH}")
    print("roadmap_projection_pending=true")


if __name__ == "__main__":
    main()
