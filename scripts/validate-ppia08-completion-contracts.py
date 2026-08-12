#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SPEC = BASE / "PPIA-08_CAMPAIGN_SCENE_SESSION_AUTHORING_EXPERIENCE_SPEC_v1.0.0.md"
ACCEPTANCE = BASE / "PPIA-08_ACCEPTANCE_TRACEABILITY_MATRIX_v1.0.0.json"
REPORT = BASE / "PPIA-08_COMPLETION_REPORT.md"
SOURCE = BASE / "PPIA-08_SOURCE_MANIFEST_v0.1.0.json"
TAXONOMY = BASE / "PPIA-08_CAMPAIGN_SCENE_SESSION_TAXONOMY_v0.1.0.json"
MAP = BASE / "PPIA-08_MAP_GRID_DUNGEON_AUTHORING_CONTRACT_v0.1.0.json"
AUTHORITY = BASE / "PPIA-08_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
INSPECTOR = BASE / "PPIA-08_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-08_REFERENCE_CASES_v0.1.0.json"
WORKFLOWS = BASE / "PPIA-08_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
TRACE = BASE / "PPIA-08_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-08-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-08 COMPLETION CONTRACT: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (SPEC, REPORT):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")
    spec = SPEC.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")
    acceptance = load(ACCEPTANCE)
    source = load(SOURCE)
    taxonomy = load(TAXONOMY)
    mapc = load(MAP)
    authority = load(AUTHORITY)
    inspector = load(INSPECTOR)
    cases_doc = load(CASES)
    workflows_doc = load(WORKFLOWS)
    trace = load(TRACE)
    backlog = load(BACKLOG)
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)

    # Bounded source and owner-directed authority.
    require(source.get("work_item_id") == "PPIA-08", "source manifest work item changed")
    require(len(source.get("canonical_repository_sources", [])) == 9, "expected nine canonical repository sources")
    require(len(source.get("retained_supporting_design_sources", [])) == 3, "expected three retained supporting design-source groups")
    require(source.get("owner_directed_extension", {}).get("blocking") is True, "owner map/grid/dungeon extension must remain blocking")
    findings = " ".join(source.get("source_boundary_findings", [])).lower()
    for phrase in ("calibration transform", "cell addressing schema", "dungeon primitive schema", "governed ppia-08 design"):
        require(phrase in findings, f"source boundary missing {phrase!r}")

    # Semantic model and presentation set.
    layers = taxonomy.get("identity_state_layers", [])
    profiles = taxonomy.get("presentation_profiles", [])
    require(len(layers) == 16 and len({x.get('id') for x in layers}) == 16, "expected sixteen unique semantic layers")
    require(len(profiles) == 12 and len(set(profiles)) == 12, "expected twelve presentation profiles")
    require(taxonomy.get("foundation_non_assumptions", {}).get("fixed_distance_per_square_invented") is False, "universal distance-per-square may not be invented")
    require(taxonomy.get("foundation_non_assumptions", {}).get("encounter_balance_owned_by_ppia08") is False, "Encounter balance boundary changed")

    # Map/calibration/location/dungeon contract.
    require(mapc.get("coordinate_modes") == ["square", "gridless"], "coordinate modes must remain square + gridless")
    require(mapc.get("map_asset_contract", {}).get("destructive_rewrite_for_grid_alignment") is False, "calibration may not rewrite image bytes")
    cal = mapc.get("square_grid_calibration", {})
    required_cal = set(cal.get("required_fields", []))
    for field in ("cellSizePx", "originOffsetXPx", "originOffsetYPx", "expected_version"):
        require(field in required_cal, f"calibration missing {field}")
    require(cal.get("camera_view_state_is_not_calibration_state") is True, "camera/calibration separation changed")
    location_types = set(mapc.get("placement_record", {}).get("location_ref_types", []))
    require(location_types == {"cell", "cell-area", "named-zone", "gridless-location"}, "semantic location types changed")
    require(mapc.get("placement_record", {}).get("copies_source_definition") is False, "placement may not copy source Definition")
    require(len(mapc.get("dungeon_construction_kit", {}).get("primitive_families", [])) == 7, "expected seven dungeon primitive families")
    require(mapc.get("dungeon_construction_kit", {}).get("automatic_collision_cover_los_rules") is False, "dungeon geometry may not infer tactical rules")
    require(mapc.get("launch_snapshot", {}).get("post_launch_recalibration_silently_moves_active_session") is False, "post-launch recalibration isolation changed")
    require(mapc.get("accessibility", {}).get("map_is_only_authoritative_representation") is False, "visual map may not be sole authority")

    # Ownership handoffs.
    handoffs = authority.get("domain_handoffs", [])
    require(len(handoffs) == 10, "expected ten domain handoffs")
    require([x.get("id") for x in handoffs] == [f"P8-HO-{n:03d}" for n in range(1, 11)], "handoff IDs changed")
    require("PPIA-11" in json.dumps(authority, ensure_ascii=False), "PPIA-11 boundary missing")

    # Inspector/action contract.
    groups = inspector.get("projection_groups", [])
    actions = inspector.get("action_contracts", [])
    require([x.get("projection_group_id") for x in groups] == [f"P8-PG-{n:03d}" for n in range(1, 17)], "projection groups must remain P8-PG-001..016")
    require([x.get("action_id") for x in actions] == [f"P8-ACT-{n:03d}" for n in range(1, 27)], "actions must remain P8-ACT-001..026")
    writes = [a for a in actions if a.get("mutation") == "write"]
    reads = [a for a in actions if a.get("mutation") == "read"]
    require(len(writes) == 22 and len(reads) == 4, "expected 22 authoritative mutations and four read actions")
    for action in writes:
        require("expected_version" in action.get("inputs", []), f"{action['action_id']} missing expected_version")
        require("operation_id" in action.get("inputs", []), f"{action['action_id']} missing operation_id")
    policy = inspector.get("projection_policy", {})
    require(policy.get("server_side_filter_before_resolution_and_aggregation") is True, "permission filtering must precede aggregation")
    require(policy.get("hidden_content_in_unauthorized_counts_or_search") is False, "hidden content may not affect unauthorized counts/search")

    # Reference corpus.
    cases = cases_doc.get("cases", [])
    expected_cases = [f"PPIA08-RC-{n:03d}" for n in range(1, 27)]
    require(len(cases) == 26 and [x.get("case_id") for x in cases] == expected_cases, "reference cases must remain contiguous 001..026")
    require(all(c.get("scenario") and c.get("expected") for c in cases), "reference cases require scenario and expected result")

    # Integrated workflows and traceability.
    workflows = workflows_doc.get("workflows", [])
    expected_workflows = [f"P8-WF-{n:03d}" for n in range(1, 18)]
    require(len(workflows) == 17 and [x.get("workflow_id") for x in workflows] == expected_workflows, "workflows must remain contiguous P8-WF-001..017")
    require(len([w for w in workflows if w.get("authoritative_mutation_performed") is True]) == 15, "expected fifteen mutation workflows")
    require(trace.get("workflow_count") == 17, "trace workflow count changed")
    require(trace.get("authoritative_mutation_workflow_count") == 15, "trace mutation-workflow count changed")
    require(trace.get("coverage_gap_counts") == {"projection_groups":0,"presentation_profiles":0,"actions":0,"reference_cases":0,"handoffs":0}, "workflow traceability gaps must be zero")

    # Final 48/16 acceptance matrix.
    require(acceptance.get("format") == "multiversal-ppia08-campaign-scene-session-authoring-acceptance-traceability-matrix", "wrong acceptance format")
    reqs = acceptance.get("requirements", [])
    require(len(reqs) == 48, "final acceptance matrix must contain 48 requirements")
    require([r.get("requirement_id") for r in reqs] == [f"PPIA08-AC-{n:03d}" for n in range(1, 49)], "acceptance IDs must remain contiguous 001..048")
    categories = Counter(r.get("category") for r in reqs)
    require(len(categories) == 16 and all(v == 3 for v in categories.values()), "expected 16 acceptance categories with three requirements each")
    require(all(r.get("blocking") is True and r.get("traces") and r.get("reference_cases") for r in reqs), "every acceptance requirement must be blocking and traced")
    referenced_cases = {case for r in reqs for case in r.get("reference_cases", [])}
    require(referenced_cases == set(expected_cases), "acceptance requirements must collectively exercise all 26 reference cases")
    coverage = acceptance.get("coverage", {})
    require(coverage.get("traceability_gap_count") == 0, "final acceptance traceability gap count must be zero")
    sets = coverage.get("sets", {})
    expected_counts = {"semantic_layers":16,"presentation_profiles":12,"projection_groups":16,"actions":26,"reference_cases":26,"workflows":17,"handoffs":10}
    for key, count in expected_counts.items():
        require(sets.get(key, {}).get("count") == count, f"acceptance coverage {key} count changed")
    require(sets.get("actions", {}).get("authoritative_mutations") == 22, "acceptance action mutation count changed")
    require(sets.get("workflows", {}).get("authoritative_mutations") == 15, "acceptance workflow mutation count changed")
    require(coverage.get("source_manifest") == {"canonical_repository_sources":9,"retained_supporting_design_source_groups":3,"owner_directed_extension_blocking":True}, "acceptance source summary changed")
    require(coverage.get("map_contract", {}).get("coordinate_modes") == ["square","gridless"], "acceptance coordinate modes changed")
    require(coverage.get("map_contract", {}).get("calibration_fields") == ["cellSizePx","originOffsetXPx","originOffsetYPx"], "acceptance calibration fields changed")
    require(coverage.get("map_contract", {}).get("dungeon_primitive_families") == 7, "acceptance dungeon primitive count changed")

    blocking = acceptance.get("blocking_policy", {})
    for true_key in ("permission_filter_before_resolution_and_aggregation",):
        require(blocking.get(true_key) is True, f"blocking policy lost {true_key}")
    for false_key in (
        "hidden_content_in_unauthorized_aggregates_allowed","visual_map_only_authoritative_representation_allowed",
        "grid_calibration_may_rewrite_image_bytes","camera_pan_zoom_may_mutate_calibration","placement_may_copy_source_definition",
        "launch_snapshot_silent_rewrite_allowed","blind_last_write_wins_allowed","duplicate_authoritative_retry_allowed",
        "offline_authoritative_map_or_session_mutation_allowed","dungeon_geometry_may_infer_tactical_rules",
        "universal_distance_per_square_invented","application_runtime_mutation_authorized","a2_activation_authorized",
        "release_authorized","deployment_authorized","tester_access_authorized","paid_service_activation_authorized",
        "production_credentials_authorized"
    ):
        require(blocking.get(false_key) is False, f"blocking policy must keep {false_key}=false")
    require(blocking.get("final_balance_owner") == "PPIA-11", "final balance owner must remain PPIA-11")

    # Human-readable final specification and report.
    for phrase in (
        "16 semantic identity/state layers","12 profiles","26 governed actions","22 are authoritative mutations",
        "26 contiguous reference cases","17 end-to-end authoring workflows","15 perform authoritative mutation",
        "cellSizePx","originOffsetXPx","originOffsetYPx","square","gridless","seven dungeon primitive families",
        "expected_version","operation_id","permission filtering","immutable","semantic nonvisual","PPIA-11",
        "48 requirements across 16 categories","STAGE-A-A2 activation authorized:** No"
    ):
        require(phrase.lower() in spec.lower(), f"final spec missing {phrase!r}")
    for phrase in (
        "COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES",
        "327ae916f61cf3e9bba16397ada4c5abe7950d92",
        "91cc220c846f132ca539531574b42f56425e9a57",
        "c85941c8c255eed7be098798bb9cb8d36ee2c3ea",
        "48 blocking acceptance requirements across 16 categories",
        "post-merge continuity",
        "PPIA-09"
    ):
        require(phrase in report, f"completion report missing {phrase!r}")

    # Dual-mode continuity: strict candidate while active; immutable evidence after completion.
    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    require("PPIA-08" in tranches, "PPIA-08 missing from backlog")
    cp_status = checkpoint.get("status")
    require(cp_status in {"started", "completed_verified"}, f"unexpected PPIA-08 checkpoint status {cp_status!r}")
    if cp_status == "started":
        require(backlog.get("current_work_item_id") == "PPIA-08", "active completion candidate must keep PPIA-08 selected")
        require(tranches["PPIA-08"].get("status") == "started", "active backlog PPIA-08 must remain started")
        require(pointer.get("primary_attempt_id") == "PPIA-08-attempt-001", "active pointer must select PPIA-08")
        require(status.get("primary", {}).get("work_item_id") == "PPIA-08", "compact status must select PPIA-08")
        combined = ((checkpoint.get("active_substep") or "") + " " + (checkpoint.get("next_action") or "")).lower()
        require("completion" in combined and "v1.0.0" in combined, "active checkpoint must identify final completion package")
    else:
        require(tranches["PPIA-08"].get("status") == "completed_verified", "completed checkpoint requires completed_verified backlog tranche")
        require(checkpoint.get("completed_at"), "completed checkpoint requires completed_at")
        require(isinstance(checkpoint.get("pull_request"), int) and checkpoint.get("pull_request") > 0, "completed checkpoint requires completion PR")
        require(isinstance(checkpoint.get("merge_commit"), str) and len(checkpoint.get("merge_commit")) == 40, "completed checkpoint requires completion merge SHA")
        require(isinstance(checkpoint.get("latest_pushed_commit"), str) and len(checkpoint.get("latest_pushed_commit")) == 40, "completed checkpoint requires validated exact head")
        require(any(v.get("command", "").startswith("Validate PPIA-08 Completion Contract") and v.get("status") == "passed" for v in checkpoint.get("validation", [])), "completed checkpoint requires passed completion-gate evidence")

    require(checkpoint.get("owner_decision_required") is False, "PPIA-08 completion must not require unresolved owner decision")
    require(checkpoint.get("unresolved_failures") == [], "PPIA-08 completion must have no unresolved failures")

    print("PPIA-08 COMPLETION CONTRACT: PASS")
    print("sources=9 canonical + 3 supporting design groups")
    print("semantic_layers=16 presentation_profiles=12 projection_groups=16")
    print("actions=26 authoritative_mutations=22 reads=4")
    print("reference_cases=26")
    print("workflows=17 authoritative_mutation_workflows=15 handoffs=10")
    print("acceptance=48 requirements / 16 categories / gaps=0")
    print("coordinate_modes=square,gridless dungeon_primitive_families=7")
    print("permission_before_aggregation=true snapshot_immutable=true recovery_idempotent=true")
    print("final_balance_owner=PPIA-11 runtime_activation=false")
    print(f"continuity_mode={cp_status}")


if __name__ == "__main__":
    main()
