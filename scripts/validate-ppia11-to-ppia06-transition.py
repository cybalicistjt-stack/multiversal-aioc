#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P11_REPORT = BASE / "PPIA-11_COMPLETION_REPORT.md"
P11 = ROOT / "governance/ai/work-state/PPIA-11-attempt-001.json"
P6 = ROOT / "governance/ai/work-state/PPIA-06-attempt-001.json"
P5 = ROOT / "governance/ai/work-state/PPIA-05-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

P11_FINAL_HEAD = "9bf4627f9e8e4a4c21dcc2614dcb74d54d62d724"
P11_COMPLETION_PR = 267
P11_COMPLETION_MERGE = "f2274707b1337425f0bc9ac8d1dd5ebb08d9f883"
P11_COMPLETION_RUN = "31595927902"
P6_BRANCH = "governance/ppia-06-character-appearance-creator"
P6_FINAL_HEAD = "6d2da6fb5a7c2d62492de895c6a9c7a1fe970a06"
P6_COMPLETION_PR = 273
P6_COMPLETION_MERGE = "ffce4859a8912813021776c4f5825c3d219bb0f2"
P6_COMPLETION_RUN = "31622184027"
COMPLETE = {"complete", "completed", "completed_verified"}
ACTIVE = {"started", "in_progress"}
PPIA_CLOSED = "completed_verified_owner_approved_parallel_work"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-11→PPIA-06 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    backlog = load(BACKLOG)
    p11 = load(P11)
    p6 = load(P6)
    p5 = load(P5)
    pointer = load(POINTER)
    status = load(STATUS)
    require(P11_REPORT.exists(), "missing PPIA-11 completion report")
    report = P11_REPORT.read_text(encoding="utf-8").lower()

    tranches = {x["work_item_id"]: x for x in backlog["tranches"]}
    require(tranches["PPIA-11"]["status"] == "completed_verified", "PPIA-11 backlog must be completed_verified")
    require(tranches["PPIA-06"]["status"] in ACTIVE | COMPLETE, "PPIA-06 backlog state invalid")
    require(tranches["PPIA-06"].get("dependencies") == ["PPIA-05"], "PPIA-06 dependency declaration changed")
    require(tranches["PPIA-05"]["status"] in COMPLETE, "PPIA-05 dependency is not complete")
    order = backlog["execution_order"]
    require(order.index("PPIA-11") + 1 == order.index("PPIA-06"), "dependency-optimized order must place PPIA-06 after PPIA-11")

    require(p11["status"] == "completed_verified", "PPIA-11 checkpoint must be completed_verified")
    require(p11["active_substep"] is None and p11.get("completed_at"), "PPIA-11 completion timestamp/substep invalid")
    require(p11["latest_pushed_commit"] == P11_FINAL_HEAD, "PPIA-11 exact validated completion head mismatch")
    require(p11["pull_request"] == P11_COMPLETION_PR, "PPIA-11 completion PR mismatch")
    require(p11["merge_commit"] == P11_COMPLETION_MERGE, "PPIA-11 completion merge mismatch")
    require(not p11["unresolved_failures"] and p11["owner_decision_required"] is False, "PPIA-11 completion has unresolved state")
    require(any(P11_COMPLETION_RUN in v.get("command", "") and v.get("status") == "passed" for v in p11["validation"]), "PPIA-11 completion-gate evidence missing")
    evidence_text = json.dumps(p11.get("evidence", []), ensure_ascii=False)
    for value in (P11_FINAL_HEAD, "PR #267", P11_COMPLETION_MERGE, P11_COMPLETION_RUN):
        require(value in evidence_text, f"PPIA-11 immutable completion evidence missing {value}")
    for phrase in ("encounter design handbook", "benchmark corpus", "20 encounter-factor families", "12 independently inspectable pressure dimensions", "4 uncertainty bands", "14 integrated workflows", "no universal cr", "ppia-11 → ppia-06 transition"):
        require(phrase in report, f"PPIA-11 completion report missing {phrase!r}")

    require(p5["status"] == "completed_verified", "PPIA-05 checkpoint must remain completed_verified")
    require(p5.get("merge_commit") == "0ffaa34ef15f9a7e4b77776688c6be3fc3047446", "PPIA-05 completion merge changed")

    require(p6["work_item_id"] == "PPIA-06" and p6["attempt_id"] == "PPIA-06-attempt-001", "PPIA-06 checkpoint identity mismatch")
    require(p6["branch"] == P6_BRANCH, "PPIA-06 governed branch mismatch")
    require(p6["base_commit"] == P11_COMPLETION_MERGE, "PPIA-06 base must be PPIA-11 completion merge")
    require(p6["status"] in ACTIVE | {"completed_verified"}, "PPIA-06 checkpoint state invalid")
    require(p6["owner_decision_required"] is False and p6["unresolved_failures"] == [], "PPIA-06 transition must be unblocked")
    scope = json.dumps({
        "objective": p6.get("objective"),
        "active_substep": p6.get("active_substep"),
        "next_action": p6.get("next_action"),
        "completed_substeps": p6.get("completed_substeps", []),
        "evidence": p6.get("evidence", []),
        "notes": p6.get("notes", []),
    }, ensure_ascii=False).lower()
    for phrase in (
        "appearance", "species", "form", "morphology", "body", "face", "hair", "fur", "scales", "feathers",
        "color", "markings", "equipment preview", "preset", "randomization", "nonhumanoid", "mobile", "accessibility",
        "portrait", "renderer-independent", "pixel-art-v1", "future-3d", "stable asset", "anchors", "occlusion", "palette",
        "unsupported", "unknown", "permission", "keyboard", "nonvisual"
    ):
        require(phrase in scope, f"PPIA-06 governed scope missing {phrase!r}")
    for prohibited in ("appearance may grant equipment", "unknown anatomy becomes human", "renderer template is species taxonomy"):
        require(prohibited not in scope, f"PPIA-06 scope contains prohibited implication {prohibited!r}")

    current_id = backlog["current_work_item_id"]
    if current_id == "PPIA-06":
        require(p6["status"] in ACTIVE, "active PPIA-06 transition requires active checkpoint")
        require(pointer["primary_attempt_id"] == "PPIA-06-attempt-001", "pointer must select PPIA-06")
        selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-06", "exactly one owner-selected PPIA-06 attempt required")
        current = selected[0]
        for field in ("attempt_id", "branch", "status", "updated_at", "roadmap_projection_pending"):
            require(current[field] == p6[field], f"pointer/PPIA-06 checkpoint mismatch: {field}")
        require(current["checkpoint_path"] == "governance/ai/work-state/PPIA-06-attempt-001.json", "PPIA-06 checkpoint path mismatch")
        primary = status["primary"]
        for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "latest_pushed_commit", "pull_request", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
            require(primary[field] == p6[field], f"compact status/PPIA-06 checkpoint mismatch: {field}")
        require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "active PPIA-06 pointer must explain batched roadmap projection")
        transition_mode = "active_ppia06"
    else:
        require(order.index(current_id) > order.index("PPIA-06"), "historical transition may only validate after PPIA-06")
        require(tranches["PPIA-06"]["status"] == "completed_verified", "historical PPIA-06 backlog must be completed_verified")
        require(p6["status"] == "completed_verified" and p6["active_substep"] is None, "historical PPIA-06 checkpoint must be completed_verified")
        require(p6["latest_pushed_commit"] == P6_FINAL_HEAD and p6["pull_request"] == P6_COMPLETION_PR and p6["merge_commit"] == P6_COMPLETION_MERGE, "historical PPIA-06 immutable completion evidence mismatch")
        require(any(P6_COMPLETION_RUN in v.get("command", "") and v.get("status") == "passed" for v in p6.get("validation", [])), "historical PPIA-06 completion gate evidence missing")
        if backlog.get("status") == PPIA_CLOSED:
            require(current_id == "PPIA-16", "closed PPIA historical transition must retain PPIA-16 final anchor")
            require(tranches["PPIA-16"]["status"] == "completed_verified", "closed PPIA final tranche must remain completed_verified")
            transition_mode = "historical_after_ppia06_program_closed"
        else:
            require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "in-flight historical pointer must explain batched roadmap projection")
            transition_mode = "historical_after_ppia06"

    boundaries = backlog["boundaries"]
    for key in ("application_runtime_mutation_authorized", "a2_activation_authorized", "release_authorized", "deployment_authorized", "tester_access_authorized", "canonical_promotion_without_source_evidence_authorized"):
        require(boundaries[key] is False, f"transition may not enable {key}")

    print("PPIA-11→PPIA-06 TRANSITION: PASS")
    print(f"ppia11_final_head={P11_FINAL_HEAD}")
    print(f"ppia11_final_merge={P11_COMPLETION_MERGE}")
    print("ppia11_status=completed_verified")
    print(f"ppia06_status={p6['status']}")
    print(f"ppia06_branch={P6_BRANCH}")
    print(f"transition_mode={transition_mode}")
    print("appearance_model=renderer-independent pixel-art-v1 first renderer future-3d boundary")
    print("biology_and_equipment_authority_preserved=true nonhumanoid_accessibility_required=true")
    print("runtime_activation=false")


if __name__ == "__main__":
    main()
