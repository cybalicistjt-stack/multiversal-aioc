#!/usr/bin/env python3
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "governance/application-planning/parallel-preimplementation"

def load(name):
    return json.loads((P / name).read_text(encoding="utf-8"))

contract = load("PPIA-13_INTEGRATED_TEACHING_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json")
trace = load("PPIA-13_INTEGRATED_TEACHING_TRACEABILITY_MATRIX_v0.1.0.json")
refs = load("PPIA-13_INTEGRATED_TEACHING_REFERENCE_CASES_v0.1.0.json")
actions = load("PPIA-13_TEACHING_LIBRARY_ACTION_CONTRACT_MATRIX_v0.1.0.json")
taxonomy = load("PPIA-13_TEACHING_CONTENT_TAXONOMY_v0.1.0.json")
foundation = load("PPIA-13_FOUNDATION_REFERENCE_CASES_v0.1.0.json")
academy = load("PPIA-13_GM_ACADEMY_REFERENCE_CASES_v0.1.0.json")
iar = load("PPIA-13_TEACHING_LIBRARY_REFERENCE_CASES_v0.1.0.json")
academy_map = load("PPIA-13_GM_ACADEMY_CURRICULUM_AND_MULTIVERSAL_MAP_v0.1.0.json")
boundary = load("PPIA-13_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json")

assert contract["work_item_id"] == "PPIA-13"
assert contract["counts"] == trace["counts"]
assert contract["counts"]["workflows"] == 18
assert contract["counts"]["teaching_surfaces"] == 18
assert contract["counts"]["roles"] == 9
assert contract["counts"]["projection_groups"] == 18
assert contract["counts"]["actions"] == 30
assert contract["counts"]["handoffs"] == 13
assert contract["counts"]["foundation_cases"] == 30
assert contract["counts"]["academy_cases"] == 20
assert contract["counts"]["iar_cases"] == 40
assert contract["counts"]["integrated_cases"] == 36
assert contract["counts"]["effective_cases"] == 126
assert refs["counts"]["effective_cases"] == 126

workflow_ids = [w["id"] for w in contract["workflows"]]
assert workflow_ids == [f"P13-WF-{i:03d}" for i in range(1,19)]
assert trace["workflow_ids"] == workflow_ids

known_actions = {a["id"]: a for a in actions["actions"]}
assert set(known_actions) == {f"P13-ACT-{i:03d}" for i in range(1,31)}
known_surfaces = {x["id"] for x in taxonomy["teaching_surfaces"]}
known_roles = set(taxonomy["audience_roles"])
known_handoffs = {h["id"] for h in contract["handoffs"]}

seen_actions=set(); seen_surfaces=set(); seen_roles=set(); seen_handoffs=set(); seen_groups=set()
for w in contract["workflows"]:
    for a in w["actions"]:
        assert a in known_actions
        seen_actions.add(a)
        seen_groups.update(known_actions[a]["groups"])
    assert set(w["surface_ids"]) <= known_surfaces
    assert set(w["roles"]) <= known_roles
    assert set(w["handoffs"]) <= known_handoffs
    seen_surfaces.update(w["surface_ids"]); seen_roles.update(w["roles"]); seen_handoffs.update(w["handoffs"])
    writes=[a for a in w["actions"] if known_actions[a]["kind"]=="write"]
    if writes:
        assert w["mutation"] is True
        assert w["protocol"]=="P13-MUT-001"
        for a in writes:
            assert known_actions[a]["protocol"]=="P13-MUT-001"
    else:
        assert w["mutation"] is False

assert seen_actions == set(known_actions)
assert seen_surfaces == known_surfaces
assert seen_roles == known_roles
assert seen_handoffs == known_handoffs
assert seen_groups == {f"P13-PG-{i:03d}" for i in range(1,19)}

foundation_ids={c["id"] for c in foundation["cases"]}
academy_ids={c["case_id"] for c in academy["cases"]}
iar_ids={c["id"] for c in iar["cases"]}
integrated_ids={c["id"] for c in refs["cases"]}
assert foundation_ids == {f"PPIA13-FC-{i:03d}" for i in range(1,31)}
assert academy_ids == {f"P13-GMA-RC-{i:03d}" for i in range(1,21)}
assert iar_ids == {f"P13-IAR-{i:03d}" for i in range(1,41)}
assert integrated_ids == {f"P13-IW-{i:03d}" for i in range(1,37)}

for field, expected in [("foundation_case_ids", foundation_ids),("academy_case_ids", academy_ids),("iar_case_ids", iar_ids),("integrated_case_ids", integrated_ids)]:
    flattened=[x for w in contract["workflows"] for x in w[field]]
    assert set(flattened)==expected
    assert all(v==1 for v in Counter(flattened).values())

policy=contract["workflow_policy"]
for k in ["permission_filter_before_discovery_search_counts_ranking_autocomplete_examples_tutorial_diagnostics_export_ai","teaching_write_requires_P13_MUT_001","expected_version_required_for_write","operation_id_required_for_write","ambiguous_result_status_lookup_before_retry","academy_optional_non_gating","multiversal_specific_claim_requires_canonical_grounding","mobile_keyboard_touch_screen_reader_high_zoom_reduced_motion_noncolor_parity","zero_ai_parity"]:
    assert policy[k] is True
for k in ["hidden_derivative_leak","outline_gap_fabrication","tutorial_campaign_canonical","world_creation_output_canonical","pack_lifecycle_invention","p14_final_microcopy_claim","offline_authoritative_mutation","gameplay_mutation","permission_mutation","runtime_activation"]:
    assert policy[k] is False

assert actions["mutation_protocol"]["id"]=="P13-MUT-001"
assert {"expected_version","operation_id"} <= set(actions["mutation_protocol"]["required_inputs"])
assert "status" in actions["mutation_protocol"]["ambiguous_network_outcome"].lower()
assert academy_map["multiversal_outline_policy"]["status"]=="approved_outline_scaffold_not_developed_lesson_source"
assert academy_map["world_creation_tables_policy"]["canonical_promotion"] is False
assert "F024" in " ".join(boundary["blocking_invariants"])
assert "PPIA-14" in " ".join(boundary["blocking_invariants"])
assert all(c["permission_filter_required"] and c["nonvisual_equivalent_required"] and not c["runtime_activation"] for c in refs["cases"])

candidate=(P/"PPIA-13_INTEGRATED_TEACHING_WORKFLOW_CANDIDATE.md").read_text(encoding="utf-8")
for needle in ["126 effective deterministic cases","P13-MUT-001","GM Academy","Multiversal","P13-GAP-001","PPIA-14","zero-AI","Final Completion Gate"]:
    assert needle in candidate

print("PPIA-13 Integrated Teaching Workflows / Traceability: PASS")
