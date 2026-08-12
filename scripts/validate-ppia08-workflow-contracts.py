#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = BASE / "PPIA-08_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
TRACE = BASE / "PPIA-08_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"
TAXONOMY = BASE / "PPIA-08_CAMPAIGN_SCENE_SESSION_TAXONOMY_v0.1.0.json"
MAP_CONTRACT = BASE / "PPIA-08_MAP_GRID_DUNGEON_AUTHORING_CONTRACT_v0.1.0.json"
AUTHORITY = BASE / "PPIA-08_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
INSPECTOR = BASE / "PPIA-08_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-08_REFERENCE_CASES_v0.1.0.json"
NOTE = BASE / "PPIA-08_WORKFLOW_AUTHORING_CANDIDATE.md"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-08 WORKFLOW CONTRACTS: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    doc = load(WORKFLOWS)
    trace = load(TRACE)
    taxonomy = load(TAXONOMY)
    map_contract = load(MAP_CONTRACT)
    authority = load(AUTHORITY)
    inspector = load(INSPECTOR)
    cases_doc = load(CASES)
    note = NOTE.read_text(encoding="utf-8")

    require(doc.get("format") == "multiversal-ppia08-workflow-authoring-contract-matrix", "wrong workflow format")
    expected_inherits = [TAXONOMY.name, MAP_CONTRACT.name, AUTHORITY.name, INSPECTOR.name, CASES.name]
    require(doc.get("inherits") == expected_inherits, "workflow inheritance changed")

    workflows = doc.get("workflows", [])
    expected_workflow_ids = [f"P8-WF-{n:03d}" for n in range(1,18)]
    require(len(workflows) == 17, f"expected 17 workflows, got {len(workflows)}")
    require([w.get("workflow_id") for w in workflows] == expected_workflow_ids, "workflow IDs must be continuous P8-WF-001..017")

    required = (
        "name","primary_personas","entry_points","preconditions","steps","outputs","projection_groups",
        "presentation_profiles","actions","reference_cases","handoffs","mutation_owner","privacy_requirements",
        "recovery_requirements","accessibility_requirements","forbidden_mutations"
    )
    for w in workflows:
        for key in required:
            require(w.get(key), f"{w['workflow_id']} missing {key}")

    mutation_workflows = [w for w in workflows if w.get("authoritative_mutation_performed") is True]
    require(len(mutation_workflows) == 14, f"expected 14 authoritative mutation workflows, got {len(mutation_workflows)}")
    for w in mutation_workflows:
        text = json.dumps(w, ensure_ascii=False).lower()
        require("expected_version" in text or "expected-version" in text or "version" in text, f"{w['workflow_id']} missing version boundary")
        require("operation_id" in text or "operation id" in text or "idempot" in text, f"{w['workflow_id']} missing operation/idempotency boundary")

    expected_pgs = [f"P8-PG-{n:03d}" for n in range(1,17)]
    expected_profiles = taxonomy.get("presentation_profiles", [])
    expected_actions = [f"P8-ACT-{n:03d}" for n in range(1,27)]
    expected_cases = [f"PPIA08-RC-{n:03d}" for n in range(1,27)]
    expected_handoffs = [f"P8-HO-{n:03d}" for n in range(1,11)]

    require(len(taxonomy.get("identity_state_layers", [])) == 16, "taxonomy must retain 16 semantic layers")
    require(len(expected_profiles) == 12, "taxonomy must retain 12 presentation profiles")
    require([x.get("projection_group_id") for x in inspector.get("projection_groups", [])] == expected_pgs, "verified projection set changed")
    require([x.get("action_id") for x in inspector.get("action_contracts", [])] == expected_actions, "verified action set changed")
    require([x.get("case_id") for x in cases_doc.get("cases", [])] == expected_cases, "verified reference-case set changed")
    require([x.get("id") for x in authority.get("domain_handoffs", [])] == expected_handoffs, "verified handoff set changed")

    routed_pgs = {x for w in workflows for x in w["projection_groups"]}
    routed_profiles = {x for w in workflows for x in w["presentation_profiles"]}
    routed_actions = {x for w in workflows for x in w["actions"]}
    routed_cases = {x for w in workflows for x in w["reference_cases"]}
    routed_handoffs = {x for w in workflows for x in w["handoffs"]}
    require(routed_pgs == set(expected_pgs), "workflow layer must route all and only 16 projection groups")
    require(routed_profiles == set(expected_profiles), "workflow layer must route all and only 12 presentation profiles")
    require(routed_actions == set(expected_actions), "workflow layer must route all and only 26 governed actions")
    require(routed_cases == set(expected_cases), "workflow layer must cover all and only 26 reference cases")
    require(routed_handoffs == set(expected_handoffs), "workflow layer must exercise all and only 10 handoffs")

    policy = doc.get("workflow_policy", {})
    require(policy.get("workflow_count") == 17, "workflow policy count changed")
    require(policy.get("authoritative_mutation_workflow_count") == 14, "mutation workflow policy count changed")
    for key in ("all_16_projection_groups_required","all_12_presentation_profiles_required","all_26_actions_required",
                "all_26_reference_cases_required","all_10_domain_handoffs_required","permission_filter_before_aggregation",
                "expected_version_operation_id_for_authoritative_mutations"):
        require(policy.get(key) is True, f"workflow policy lost {key}")
    for key in ("visual_map_only_authoritative_representation","source_definition_ownership_transferred",
                "launch_snapshot_silent_rewrite_allowed","encounter_balance_owned_by_ppia08","runtime_activation"):
        require(policy.get(key) is False, f"workflow policy boundary changed: {key}")

    require(trace.get("workflow_count") == 17 and trace.get("authoritative_mutation_workflow_count") == 14, "trace workflow counts changed")
    coverage_specs = (
        ("projection_group_coverage", expected_pgs),
        ("presentation_profile_coverage", expected_profiles),
        ("action_coverage", expected_actions),
        ("reference_case_coverage", expected_cases),
        ("handoff_coverage", expected_handoffs),
    )
    for field, expected_ids in coverage_specs:
        coverage = trace.get(field, {})
        require(list(coverage) == expected_ids, f"{field} keys changed")
        require(all(coverage[x] for x in expected_ids), f"{field} contains a coverage gap")
        for refs in coverage.values():
            require(set(refs).issubset(set(expected_workflow_ids)), f"{field} references unknown workflow")
    require(trace.get("coverage_gap_counts") == {
        "projection_groups":0,"presentation_profiles":0,"actions":0,"reference_cases":0,"handoffs":0
    }, "traceability gaps must be zero")
    require(len(trace.get("end_to_end_assertions", [])) == 11, "expected 11 end-to-end trace assertions")

    full = (json.dumps(doc, ensure_ascii=False) + "\n" + json.dumps(trace, ensure_ascii=False) + "\n" + note).lower()
    for phrase in (
        "17 end-to-end authoring workflows","14 workflows perform authoritative mutation",
        "cellsizepx","originoffsetxpx","originoffsetypx","camera pan/zoom","square-grid","gridless",
        "multi-cell","named-zone","seven verified primitive families","room/floor","corridor/path","wall",
        "door/opening","terrain/feature","stairs/portal/transition","reusable tile/stamp",
        "ownerdomain","objectid","objectversion","permission filtering","counts","ai context",
        "immutable launch snapshot","live-session amendment","expected_version","operation_id",
        "status/current-version lookup","screen-reader","semantic nonvisual","ppia-11","final balance","stage-a-a2"
    ):
        require(phrase in full, f"missing required workflow boundary {phrase!r}")

    for phrase in ("collision","line of sight","cover","movement legality","damage","lighting","fog","balance"):
        require(phrase in full, f"tactical boundary missing {phrase!r}")

    calibration = map_contract.get("grid_calibration", {})
    require(calibration.get("cell_size_field") == "cellSizePx", "map contract cellSizePx changed")
    require(calibration.get("origin_offset_fields") == ["originOffsetXPx","originOffsetYPx"], "map contract origin offsets changed")
    require(map_contract.get("camera_vs_calibration", {}).get("camera_pan_zoom_changes_calibration") is False, "camera/calibration separation changed")
    require(set(map_contract.get("location_addressing", {}).get("location_types", [])) >= {"cell","cell-area","named-zone","gridless-location"}, "location addressing lost required type")
    require(len(map_contract.get("dungeon_primitive_families", [])) == 7, "seven dungeon primitive families changed")

    print("PPIA-08 WORKFLOW CONTRACTS: PASS")
    print("workflows=17")
    print("authoritative_mutation_workflows=14")
    print("projection_groups=16")
    print("presentation_profiles=12")
    print("actions=26")
    print("reference_cases=26")
    print("handoffs=10")
    print("traceability_gaps=0")
    print("end_to_end_assertions=11")


if __name__ == "__main__":
    main()
