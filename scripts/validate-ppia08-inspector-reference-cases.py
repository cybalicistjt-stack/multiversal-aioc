#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
MATRIX = BASE / "PPIA-08_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-08_REFERENCE_CASES_v0.1.0.json"
CANDIDATE = BASE / "PPIA-08_INSPECTOR_ACTION_REFERENCE_CANDIDATE.md"
TAXONOMY = BASE / "PPIA-08_CAMPAIGN_SCENE_SESSION_TAXONOMY_v0.1.0.json"
MAP_CONTRACT = BASE / "PPIA-08_MAP_GRID_DUNGEON_AUTHORING_CONTRACT_v0.1.0.json"
AUTHORITY = BASE / "PPIA-08_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-08-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

INSPECTOR_FINAL_HEAD = "e460f747aa9d909a88fd7e08654c74e0dc013f47"
INSPECTOR_MERGE = "91cc220c846f132ca539531574b42f56425e9a57"
INSPECTOR_PR = 249


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    for path in (MATRIX, CASES, CANDIDATE, TAXONOMY, MAP_CONTRACT, AUTHORITY, CHECKPOINT, POINTER, STATUS):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    matrix = load(MATRIX)
    cases = load(CASES)
    taxonomy = load(TAXONOMY)
    map_contract = load(MAP_CONTRACT)
    authority = load(AUTHORITY)
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    note = CANDIDATE.read_text(encoding="utf-8")

    require(matrix["work_item"] == "PPIA-08", "wrong matrix work item")
    require(matrix["version"] == "0.1.0", "wrong matrix version")
    require(matrix["foundation_merge"] == "327ae916f61cf3e9bba16397ada4c5abe7950d92", "foundation merge drifted")

    layers = [item["id"] for item in taxonomy["identity_state_layers"]]
    groups = matrix["projection_groups"]
    require(len(layers) == 16, "foundation taxonomy must contain 16 layers")
    require(len(groups) == 16, "inspector must contain 16 projection groups")
    require([g["projection_group_id"] for g in groups] == [f"P8-PG-{i:03d}" for i in range(1, 17)], "projection group IDs must be contiguous")
    require([g["layer_id"] for g in groups] == layers, "projection groups must map one-to-one and in order to the 16 foundation layers")
    require(all(g["fields"] for g in groups), "every projection group needs fields")

    pp = matrix["projection_policy"]
    require(pp["server_side_filter_before_resolution_and_aggregation"] is True, "permission filtering must precede projection/aggregation")
    require(pp["hidden_content_in_unauthorized_counts_or_search"] is False, "hidden content may not affect unauthorized counts/search")
    require(pp["visual_map_only_authoritative_representation"] is False, "visual map cannot be the only authoritative representation")
    require(pp["camera_pan_zoom_is_calibration"] is False, "camera pan/zoom may not become calibration state")
    require(pp["placement_copies_source_definition"] is False, "placement may not copy source Definition")
    require(pp["dungeon_geometry_implies_tactical_rules"] is False, "dungeon geometry may not imply tactical rules")

    actions = matrix["action_contracts"]
    require(len(actions) == 26, "expected 26 governed actions")
    require([a["action_id"] for a in actions] == [f"P8-ACT-{i:03d}" for i in range(1, 27)], "action IDs must be contiguous")
    require(len({a["name"] for a in actions}) == 26, "action names must be unique")
    mutating = [a for a in actions if a["mutation"] == "write"]
    reads = [a for a in actions if a["mutation"] == "read"]
    require(len(mutating) == matrix["action_policy"]["authoritative_mutation_count"] == 22, "expected 22 authoritative mutation actions")
    require(len(reads) == matrix["action_policy"]["read_action_count"] == 4, "expected four read actions")
    for action in mutating:
        require("expected_version" in action["inputs"], f"{action['action_id']} missing expected_version")
        require("operation_id" in action["inputs"], f"{action['action_id']} missing operation_id")

    required_actions = {
        "upload_map_asset","replace_map_asset","create_grid_calibration","revise_or_lock_grid_calibration",
        "define_location_address","place_scene_content","edit_placement_layer_location","hide_or_reveal_scene_content",
        "create_dungeon_primitive","edit_dungeon_primitive","duplicate_or_remove_dungeon_primitive",
        "validate_launch_readiness","create_launch_snapshot","propose_live_session_amendment","accept_or_reject_live_amendment",
        "inspect_history_recover_accessible_projection"
    }
    require(required_actions <= {a["name"] for a in actions}, "owner-required map/dungeon/session actions incomplete")
    ap = matrix["action_policy"]
    require(ap["placement_owns_source_definition"] is False, "placement ownership boundary drifted")
    require(ap["live_amendment_silently_rewrites_launch_snapshot"] is False, "launch snapshot must remain immutable")
    require(ap["encounter_balance_owned_by_ppia08"] is False, "Encounter balance boundary drifted")
    require(ap["offline_authoritative_map_or_session_mutation_allowed"] is False, "offline authoritative mutation must remain prohibited")

    require(map_contract["owner_requirement_blocking"] is True, "owner map requirement must remain blocking")
    require(map_contract["coordinate_modes"] == ["square", "gridless"], "required initial coordinate modes drifted")
    require(map_contract["map_asset_contract"]["destructive_rewrite_for_grid_alignment"] is False, "grid alignment may not rewrite image")
    require(map_contract["square_grid_calibration"]["camera_view_state_is_not_calibration_state"] is True, "camera/calibration separation drifted")
    require(map_contract["placement_record"]["copies_source_definition"] is False, "placement source copy guardrail drifted")
    require(len(map_contract["dungeon_construction_kit"]["primitive_families"]) == 7, "expected seven dungeon primitive families")
    require(map_contract["launch_snapshot"]["post_launch_recalibration_silently_moves_active_session"] is False, "post-launch recalibration isolation drifted")
    require(map_contract["accessibility"]["map_is_only_authoritative_representation"] is False, "nonvisual map contract drifted")

    require(len(authority["domain_handoffs"]) == 10, "foundation must retain ten ownership handoffs")

    corpus = cases["cases"]
    require(cases["case_count"] == len(corpus) == 26, "reference corpus must contain 26 cases")
    require([c["case_id"] for c in corpus] == [f"PPIA08-RC-{i:03d}" for i in range(1, 27)], "reference case IDs must be contiguous")
    action_ids = {a["action_id"] for a in actions}
    group_ids = {g["projection_group_id"] for g in groups}
    covered_actions = set()
    covered_groups = set()
    for case in corpus:
        require(case["scenario"] and case["expected"], f"{case['case_id']} missing scenario/expected")
        require(set(case["actions"]) <= action_ids, f"{case['case_id']} references unknown action")
        require(set(case["projection_groups"]) <= group_ids, f"{case['case_id']} references unknown projection group")
        covered_actions.update(case["actions"])
        covered_groups.update(case["projection_groups"])
    require(covered_actions == action_ids, f"action coverage gap: {sorted(action_ids-covered_actions)}")
    require(covered_groups == group_ids, f"projection coverage gap: {sorted(group_ids-covered_groups)}")

    case_titles = {c["title"] for c in corpus}
    for title in [
        "Upload map image","Square-grid calibration end to end","Camera pan versus grid translation",
        "Multi-cell large vehicle placement","Gridless Scene locations","Dungeon room corridor wall and door construction",
        "Hidden GM-only placement does not leak","Launch readiness and immutable snapshot",
        "Post-launch recalibration isolation","Governed live-session amendment",
        "Stale calibration expected-version conflict","Duplicate retry does not duplicate placement",
        "Accessible nonvisual map and revoked access"
    ]:
        require(title in case_titles, f"missing required reference case: {title}")

    policy = cases["policy"]
    require(all(value is False for value in policy.values()), "reference-case guardrail policy drifted")

    # Historical milestone validation is dual-mode. A mutable checkpoint may compact old
    # run IDs; the immutable validated head + PR + merge anchors are the durable proof.
    require(checkpoint["work_item_id"] == "PPIA-08", "PPIA-08 checkpoint identity changed")
    require(checkpoint["status"] in {"started","in_progress","completed_verified"}, "invalid PPIA-08 checkpoint status")
    evidence_text = json.dumps({
        "last_verified_action": checkpoint.get("last_verified_action"),
        "completed_substeps": checkpoint.get("completed_substeps", []),
        "validation": checkpoint.get("validation", []),
        "evidence": checkpoint.get("evidence", []),
    }, ensure_ascii=False)
    for value in (INSPECTOR_FINAL_HEAD, INSPECTOR_MERGE, f"PR #{INSPECTOR_PR}"):
        require(value in evidence_text, f"immutable inspector milestone evidence missing {value}")
    require(checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"] == [], "checkpoint has unresolved inspector state")

    if checkpoint["status"] != "completed_verified":
        require(pointer["primary_attempt_id"] == "PPIA-08-attempt-001", "active PPIA-08 must remain selected while unfinished")
        require(status["primary"]["work_item_id"] == "PPIA-08" and status["primary"]["status"] in {"started","in_progress"}, "compact status must remain on active PPIA-08")
    else:
        require(checkpoint.get("completed_at"), "completed_verified PPIA-08 must have completed_at")

    low = note.lower()
    for phrase in ["16 inspector projection groups","26 actions","22 are authoritative mutations","26 contiguous reference cases","cellsizepx","originoffsetxpx","originoffsetypx","gridless","seven verified primitive families","expected_version","operation_id","not ppia-08 complete"]:
        require(phrase.lower() in low, f"candidate note missing phrase: {phrase}")

    print("PPIA-08 INSPECTOR / ACTION / REFERENCE CASES: PASS")
    print("projection_groups=16 actions=26 authoritative_mutations=22 reference_cases=26")
    print("map_workflow=upload+calibrate+address+place+reveal+snapshot+amendment+recovery")
    print("dungeon_primitive_families=7 coordinate_modes=square,gridless")
    print("source_definition_copy=false hidden_aggregate_leak=false visual_only=false")
    print(f"historical_inspector_merge={INSPECTOR_MERGE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
