#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
REPORT = BASE / "PPIA-07_COMPLETION_REPORT.md"
MAP_CONTRACT = BASE / "PPIA-08_MAP_GRID_DUNGEON_AUTHORING_CONTRACT_v0.1.0.json"
P7 = ROOT / "governance/ai/work-state/PPIA-07-attempt-001.json"
P8 = ROOT / "governance/ai/work-state/PPIA-08-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

P7_FINAL_HEAD = "c8e9d1ab677ca4bb37a772b1883099d23abb8187"
P7_COMPLETION_MERGE = "ac1628227d34df7fc1585b21c21988fb2fd7080a"
P8_BRANCH = "governance/ppia-08-campaign-scene-session-authoring"
MAP_TERMS = ("map-image upload", "grid", "calibration", "cell-addressable", "dungeon-map construction kit")


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-07→PPIA-08 TRANSITION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def validate_map_contract() -> str:
    require(MAP_CONTRACT.exists(), "durable PPIA-08 map contract is required after foundation")
    contract = load(MAP_CONTRACT)
    require(contract.get("work_item_id") == "PPIA-08", "map contract work-item identity mismatch")
    require(contract.get("owner_requirement_blocking") is True, "owner map requirement must remain blocking")
    require(contract.get("coordinate_modes") == ["square", "gridless"], "map coordinate modes changed")
    require(contract.get("map_asset_contract", {}).get("destructive_rewrite_for_grid_alignment") is False, "grid alignment may not rewrite image bytes")
    calibration = contract.get("square_grid_calibration", {})
    required = set(calibration.get("required_fields", []))
    require({"cellSizePx", "originOffsetXPx", "originOffsetYPx"}.issubset(required), "square-grid calibration fields incomplete")
    require(calibration.get("camera_view_state_is_not_calibration_state") is True, "camera pan/zoom may not become calibration state")
    placement = contract.get("placement_record", {})
    require(placement.get("copies_source_definition") is False, "PPIA-08 placements may not copy source Definitions")
    require({"ownerDomain", "objectId", "objectVersion"}.issubset(set(placement.get("owning_object_ref_fields", []))), "placement identity fields incomplete")
    require({"item", "hazard", "encounter", "creature-npc", "vehicle"}.issubset(set(placement.get("placement_kinds", []))), "required placement kinds missing")
    require(set(placement.get("location_ref_types", [])) >= {"cell", "cell-area", "named-zone", "gridless-location"}, "location references incomplete")
    require(len(contract.get("dungeon_construction_kit", {}).get("primitive_families", [])) == 7, "seven dungeon primitive families required")
    require(contract.get("accessibility", {}).get("map_is_only_authoritative_representation") is False, "nonvisual map equivalence lost")
    return "durable_map_contract"


def main() -> None:
    backlog = load(BACKLOG)
    p7 = load(P7)
    p8 = load(P8)
    pointer = load(POINTER)
    status = load(STATUS)
    report = REPORT.read_text(encoding="utf-8")
    tranches = {item["work_item_id"]: item for item in backlog["tranches"]}

    for work_item in ("PPIA-01", "PPIA-02", "PPIA-03", "PPIA-04", "PPIA-05", "PPIA-12", "PPIA-07"):
        require(tranches[work_item]["status"] in {"complete", "completed", "completed_verified"}, f"{work_item} must be complete before PPIA-08")
    require(tranches["PPIA-07"]["status"] == "completed_verified", "PPIA-07 backlog state must be completed_verified")
    gate = tranches["PPIA-08"]["completion_gate"].lower()
    for term in MAP_TERMS:
        require(term in gate, f"PPIA-08 completion gate missing owner map requirement: {term}")

    require(p7["status"] == "completed_verified" and p7["active_substep"] is None, "PPIA-07 checkpoint must be completed_verified")
    require(p7["latest_pushed_commit"] == P7_FINAL_HEAD, "PPIA-07 exact final head mismatch")
    require(p7["pull_request"] == 246 and p7["merge_commit"] == P7_COMPLETION_MERGE, "PPIA-07 final PR/merge mismatch")
    require(not p7["unresolved_failures"] and p7["owner_decision_required"] is False, "PPIA-07 completion has unresolved state")
    require(any("31545759090" in item.get("command", "") and item.get("status") == "passed" for item in p7["validation"]), "PPIA-07 completion-gate evidence missing")

    require(p8["work_item_id"] == "PPIA-08" and p8["attempt_id"] == "PPIA-08-attempt-001", "PPIA-08 checkpoint identity mismatch")
    require(p8["branch"] == P8_BRANCH, "PPIA-08 governed branch mismatch")
    require(p8["status"] in {"started", "in_progress", "completed_verified"}, "unexpected PPIA-08 checkpoint state")
    require(any(P7_COMPLETION_MERGE in item.get("value", "") for item in p8.get("evidence", [])), "PPIA-08 must preserve PPIA-07 completion merge evidence")
    require(p8["roadmap_projection_pending"] is True, "PPIA-08 roadmap projection must remain batched/pending")

    p8_scope = " ".join([
        p8.get("objective", ""), p8.get("active_substep", "") or "", p8.get("next_action", "") or "",
        " ".join(p8.get("completed_substeps", [])), " ".join(p8.get("notes", [])),
        " ".join(item.get("value", "") for item in p8.get("evidence", [])),
    ]).lower()
    for term in ("map", "grid", "calibration", "cell", "dungeon"):
        require(term in p8_scope, f"PPIA-08 checkpoint missing map-authoring scope term: {term}")
    require("uploaded" in p8_scope and "offset" in p8_scope, "PPIA-08 checkpoint must preserve upload and grid-offset behavior")
    require("gridless" in p8_scope and "nonvisual" in p8_scope, "PPIA-08 scope must preserve gridless and nonvisual operation")
    placement_identity_mode = validate_map_contract()

    if p8["status"] in {"started", "in_progress"}:
        require(backlog["current_work_item_id"] == "PPIA-08", "active PPIA-08 must remain current backlog item")
        require(tranches["PPIA-08"]["status"] in {"started", "in_progress"}, "active PPIA-08 backlog state mismatch")
        require(p8.get("active_substep"), "active PPIA-08 must have active work")
        selected = [item for item in pointer["active_attempts"] if item.get("owner_selected")]
        require(len(selected) == 1, "exactly one owner-selected active attempt required")
        current = selected[0]
        require(pointer["primary_attempt_id"] == "PPIA-08-attempt-001", "primary attempt must be PPIA-08 while active")
        require(current["work_item_id"] == "PPIA-08" and current["checkpoint_path"] == "governance/ai/work-state/PPIA-08-attempt-001.json", "pointer must select PPIA-08 checkpoint")
        for field in ("branch", "status", "updated_at", "roadmap_projection_pending"):
            require(current[field] == p8[field], f"pointer/PPIA-08 checkpoint mismatch: {field}")
        primary = status["primary"]
        for field in ("work_item_id", "attempt_id", "branch", "status", "active_substep", "next_action", "owner_decision_required", "unresolved_failures", "roadmap_projection_pending"):
            require(primary[field] == p8[field], f"compact status/PPIA-08 checkpoint mismatch: {field}")
        require(primary["latest_pushed_commit"] == p8["latest_pushed_commit"] and primary["pull_request"] == p8["pull_request"], "compact PPIA-08 commit/PR mismatch")
        continuity_mode = "active"
    else:
        require(tranches["PPIA-08"]["status"] == "completed_verified", "completed PPIA-08 checkpoint requires completed backlog tranche")
        require(p8.get("completed_at") and p8.get("active_substep") is None, "completed PPIA-08 requires completion timestamp and no active substep")
        require(isinstance(p8.get("pull_request"), int) and p8["pull_request"] > 250, "completed PPIA-08 requires final completion PR")
        require(isinstance(p8.get("merge_commit"), str) and len(p8["merge_commit"]) == 40, "completed PPIA-08 requires final merge SHA")
        continuity_mode = "historical_completed"

    for value in ("34 core runes", "16 blind rune-play reference cases", "48 blocking final acceptance requirements", P7_FINAL_HEAD, P7_COMPLETION_MERGE, "PPIA-08"):
        require(value.lower() in report.lower(), f"PPIA-07 completion report missing {value!r}")
    require("roadmap" in pointer["selection_reason"].lower() and "pending" in pointer["selection_reason"].lower(), "pointer must explain batched roadmap projection")

    print("PPIA-07→PPIA-08 TRANSITION: PASS")
    print("ppia07_status=completed_verified")
    print(f"ppia07_final_head={P7_FINAL_HEAD}")
    print(f"ppia07_final_merge={P7_COMPLETION_MERGE}")
    print(f"ppia08_status={p8['status']}")
    print(f"ppia08_branch={P8_BRANCH}")
    print(f"placement_identity_validation={placement_identity_mode}")
    print("map_image_upload_grid_calibration_cell_assignment_dungeon_kit=required")
    print(f"continuity_mode={continuity_mode}")
    print("roadmap_projection_pending=true")


if __name__ == "__main__":
    main()
