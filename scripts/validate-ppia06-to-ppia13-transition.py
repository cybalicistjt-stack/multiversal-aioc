#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P6 = ROOT / "governance/ai/work-state/PPIA-06-attempt-001.json"
P13 = ROOT / "governance/ai/work-state/PPIA-13-attempt-001.json"
P8 = ROOT / "governance/ai/work-state/PPIA-08-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

P6_FINAL_HEAD = "6d2da6fb5a7c2d62492de895c6a9c7a1fe970a06"
P6_COMPLETION_PR = 273
P6_COMPLETION_RUN = "31622184027"
P6_COMPLETION_MERGE = "ffce4859a8912813021776c4f5825c3d219bb0f2"
P13_BRANCH = "governance/ppia-13-onboarding-help-teaching-content"
EXPECTED_ORDER = ["PPIA-01","PPIA-02","PPIA-03","PPIA-04","PPIA-05","PPIA-12","PPIA-07","PPIA-08","PPIA-09","PPIA-10","PPIA-11","PPIA-06","PPIA-13","PPIA-14","PPIA-15","PPIA-16"]
COMPLETE = {"complete","completed","completed_verified"}


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-06→PPIA-13 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p6 = load(P6)
    p13 = load(P13)
    p8 = load(P8)
    pointer = load(POINTER)
    status = load(STATUS)
    tranches = {x["work_item_id"]: x for x in backlog["tranches"]}

    require(backlog["execution_order"] == EXPECTED_ORDER, "dependency-optimized PPIA order changed")
    require(backlog["current_work_item_id"] == "PPIA-13", "current PPIA item must be PPIA-13")
    require(EXPECTED_ORDER.index("PPIA-06") + 1 == EXPECTED_ORDER.index("PPIA-13"), "PPIA-13 must directly follow PPIA-06")
    require(tranches["PPIA-06"]["status"] == "completed_verified", "PPIA-06 backlog must be completed_verified")
    require(tranches["PPIA-13"]["status"] == "started", "PPIA-13 backlog must be started")
    require(tranches["PPIA-13"].get("dependencies") == ["PPIA-08"], "PPIA-13 dependency declaration changed")
    require(tranches["PPIA-08"]["status"] in COMPLETE and p8["status"] == "completed_verified", "PPIA-08 dependency must remain completed_verified")
    for work_item in EXPECTED_ORDER[:EXPECTED_ORDER.index("PPIA-13")]:
        require(tranches[work_item]["status"] in COMPLETE, f"{work_item} must be complete before PPIA-13")
    for work_item in EXPECTED_ORDER[EXPECTED_ORDER.index("PPIA-13") + 1:]:
        require(tranches[work_item]["status"] == "planned", f"{work_item} must remain planned during PPIA-13 activation")

    require(p6["work_item_id"] == "PPIA-06" and p6["attempt_id"] == "PPIA-06-attempt-001", "PPIA-06 checkpoint identity mismatch")
    require(p6["status"] == "completed_verified" and p6["active_substep"] is None and p6.get("completed_at"), "PPIA-06 checkpoint must be finalized")
    require(p6["latest_pushed_commit"] == P6_FINAL_HEAD, "PPIA-06 exact validated completion head mismatch")
    require(p6["pull_request"] == P6_COMPLETION_PR and p6["merge_commit"] == P6_COMPLETION_MERGE, "PPIA-06 completion PR/merge mismatch")
    require(p6["owner_decision_required"] is False and p6["unresolved_failures"] == [], "PPIA-06 completion has unresolved state")
    require(any(P6_COMPLETION_RUN in item.get("command", "") and item.get("status") == "passed" for item in p6.get("validation", [])), "PPIA-06 completion run evidence missing")
    p6_evidence = json.dumps(p6.get("evidence", []), ensure_ascii=False)
    for value in (P6_FINAL_HEAD, P6_COMPLETION_MERGE, "PR #273", P6_COMPLETION_RUN):
        require(value in p6_evidence or value in p6.get("last_verified_action", ""), f"PPIA-06 immutable evidence missing {value}")

    require(p13["work_item_id"] == "PPIA-13" and p13["attempt_id"] == "PPIA-13-attempt-001", "PPIA-13 checkpoint identity mismatch")
    require(p13["branch"] == P13_BRANCH and p13["base_commit"] == P6_COMPLETION_MERGE, "PPIA-13 branch/base mismatch")
    require(p13["status"] in {"started", "ready_for_review"} and p13["active_substep"] and p13["next_action"], "PPIA-13 must remain on an active bounded in-tranche step")
    require(p13["owner_decision_required"] is False and p13["unresolved_failures"] == [] and p13["roadmap_projection_pending"] is True, "PPIA-13 transition state must be unblocked with pending roadmap projection")
    scope = json.dumps({
        "objective": p13.get("objective"),
        "active_substep": p13.get("active_substep"),
        "next_action": p13.get("next_action"),
        "completed_substeps": p13.get("completed_substeps", []),
        "notes": p13.get("notes", []),
    }, ensure_ascii=False).lower()
    for phrase in (
        "player", "gm", "creator", "first launch", "campaign join", "character creation", "first action", "approval",
        "library", "inspector", "permission", "hidden-information", "offline", "reconnect", "packs", "troubleshooting",
        "contextual", "empty state", "glossary", "tutorial-campaign", "accessibility", "mobile", "nonvisual", "ppia-14"
    ):
        require(phrase in scope, f"PPIA-13 governed scope missing {phrase!r}")
    for prohibited in ("runtime_activation=true", "release_authorized=true", "tester_access_authorized=true", "canonical_promotion_without_source_evidence_authorized=true"):
        require(prohibited not in scope, f"PPIA-13 scope contains prohibited positive authorization {prohibited!r}")

    selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
    require(len(selected) == 1, "exactly one owner-selected active attempt required")
    current = selected[0]
    require(pointer["primary_attempt_id"] == "PPIA-13-attempt-001", "pointer primary attempt must be PPIA-13")
    require(current["work_item_id"] == "PPIA-13" and current["checkpoint_path"] == "governance/ai/work-state/PPIA-13-attempt-001.json", "pointer must select PPIA-13 checkpoint")
    for field in ("attempt_id","branch","status","updated_at","roadmap_projection_pending"):
        require(current[field] == p13[field], f"pointer/PPIA-13 checkpoint mismatch: {field}")

    primary = status["primary"]
    for field in ("work_item_id","attempt_id","branch","status","active_substep","next_action","latest_pushed_commit","pull_request","owner_decision_required","unresolved_failures","roadmap_projection_pending"):
        require(primary[field] == p13.get(field), f"compact status/PPIA-13 checkpoint mismatch: {field}")
    require(status["active_attempt_count"] == len(pointer["active_attempts"]), "compact active attempt count mismatch")
    require(status["deferred_track_count"] == len(pointer["deferred_tracks"]), "compact deferred track count mismatch")
    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")
    require(P6_COMPLETION_MERGE in pointer["selection_reason"] and P6_COMPLETION_RUN in pointer["selection_reason"], "pointer must preserve PPIA-06 completion evidence")

    boundaries = backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        require(boundaries[key] is False, f"transition may not enable {key}")
    require(boundaries["requires_codex"] is False, "PPIA transition must not require Codex")

    print("PPIA-06→PPIA-13 TRANSITION: PASS")
    print(f"ppia06_final_head={P6_FINAL_HEAD}")
    print(f"ppia06_final_merge={P6_COMPLETION_MERGE}")
    print(f"ppia06_completion_run={P6_COMPLETION_RUN}")
    print("ppia06_status=completed_verified")
    print(f"ppia13_status={p13['status']}")
    print(f"ppia13_branch={P13_BRANCH}")
    print("ppia13_dependency=PPIA-08 completed_verified")
    print("ppia13_foundation=role-aware onboarding/help/teaching source inventory")
    print("roadmap_projection_pending=true runtime_activation=false")


if __name__ == "__main__":
    main()
