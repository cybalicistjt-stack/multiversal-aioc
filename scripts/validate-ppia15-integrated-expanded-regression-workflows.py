#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
P = lambda name: BASE / name

FILES = {
    "workflow": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json"),
    "trace": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_TRACEABILITY_MATRIX_v0.1.0.json"),
    "cases": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_REFERENCE_CASES_v0.1.0.json"),
    "index": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_PACKAGE_INDEX_v0.1.0.json"),
    "candidate": P("PPIA-15_INTEGRATED_EXPANDED_REGRESSION_WORKFLOW_CANDIDATE.md"),
    "scenario": P("PPIA-15_EXPANDED_REGRESSION_SCENARIO_LIBRARY_v0.1.0.json"),
    "iar_trace": P("PPIA-15_IAR_TRACEABILITY_MATRIX_v0.1.0.json"),
    "projection": P("PPIA-15_INSPECTOR_PROJECTION_CONTRACTS_v0.1.0.json"),
    "action": P("PPIA-15_ACTION_AND_REFERENCE_CONTRACTS_v0.1.0.json"),
    "foundation_cases": P("PPIA-15_FOUNDATION_REFERENCE_CASES_v0.1.0.json"),
    "iar_cases": P("PPIA-15_IAR_REFERENCE_CASES_v0.1.0.json"),
    "backlog": P("PPIA_PROGRAM_BACKLOG.json"),
}
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-15-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

EXPECTED_COUNTS = {
    "workflows":18,
    "awkward_families":18,
    "stable_scenario_contracts":24,
    "projection_groups":12,
    "action_contracts":20,
    "handoffs":12,
    "foundation_cases":32,
    "iar_cases":40,
    "integrated_cases":18,
    "effective_cases":90,
    "upstream_command_presentation_workflows":7,
    "ordinary_gm_modification_clones":0,
    "open_f024_source_gaps":1,
}


def fail(message: str) -> None:
    raise SystemExit("PPIA-15 INTEGRATED EXPANDED REGRESSION WORKFLOWS: FAIL — " + message)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def exact_once(actual: list[str], expected: list[str], label: str) -> None:
    counts = Counter(actual)
    req(set(counts) == set(expected), f"{label} coverage set mismatch")
    req(all(v == 1 for v in counts.values()), f"{label} must be assigned exactly once")


def main() -> None:
    d = {k: load(v) for k, v in FILES.items() if k != "candidate"}
    workflow = d["workflow"]
    trace = d["trace"]
    cases = d["cases"]
    index = d["index"]
    scenario = d["scenario"]
    iar_trace = d["iar_trace"]
    projections = d["projection"]
    actions = d["action"]
    foundation_cases = d["foundation_cases"]
    iar_cases = d["iar_cases"]
    backlog = d["backlog"]
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    candidate = FILES["candidate"].read_text(encoding="utf-8").lower()

    req(workflow.get("counts") == EXPECTED_COUNTS, "workflow counts changed")
    req(trace.get("counts") == EXPECTED_COUNTS, "traceability counts changed")
    locked = index.get("locked_counts", {})
    req(locked == {
        "workflows":18,"required_awkward_families":18,"stable_scenario_contracts":24,"projection_groups":12,
        "action_contracts":20,"handoffs":12,"foundation_cases":32,"iar_cases":40,"new_integrated_cases":18,
        "effective_cases":90,"upstream_command_presentation_workflows":7,"ordinary_gm_modification_clones":0,
        "open_f024_source_gaps":1,
    }, "package locked counts changed")

    wfs = workflow.get("workflows", [])
    req([x.get("id") for x in wfs] == [f"P15-WF-{i:03d}" for i in range(1, 19)], "workflow IDs changed")
    req([x.get("awkward_family_id") for x in wfs] == [f"P15-AWK-{i:03d}" for i in range(1, 19)], "one-primary-workflow-per-family mapping changed")

    scenarios = scenario.get("scenario_contracts", [])
    req([x.get("id") for x in scenarios] == [f"P15-SCN-{i:03d}" for i in range(1, 25)], "stable scenario IDs changed")
    scenario_by_id = {x["id"]: x for x in scenarios}
    scenario_ids = set(scenario_by_id)
    pg_rows = projections.get("projection_groups", [])
    projection_ids = {x.get("id") for x in pg_rows}
    req(projection_ids == {f"P15-PG-{i:03d}" for i in range(1, 13)}, "projection group IDs changed")
    req(all(x.get("semantic_nonvisual_parity") is True for x in pg_rows), "projection semantic parity changed")
    action_rows = actions.get("actions", [])
    action_ids = {x.get("id") for x in action_rows}
    req(action_ids == {f"P15-ACT-{i:03d}" for i in range(1, 21)}, "action IDs changed")
    req(all(x.get("ppia15_mutates_authoritative_state") is False for x in action_rows), "PPIA-15 action gained mutation authority")
    upstream_actions = {x.get("id") for x in action_rows if x.get("upstream_mutation_possible") is True}
    req(upstream_actions == {"P15-ACT-016","P15-ACT-017","P15-ACT-018","P15-ACT-019"}, "upstream command-presentation action set changed")

    family_source = {x.get("awkward_id"): x for x in iar_trace.get("family_rows", [])}
    req(set(family_source) == {f"P15-AWK-{i:03d}" for i in range(1, 19)}, "IAR family source changed")
    used_scenarios, used_pgs, used_actions, used_handoffs = set(), set(), set(), set()
    mutation_presenting = []
    for w in wfs:
        family = w["awkward_family_id"]
        source = family_source[family]
        req(w.get("scenario_ids") == source.get("scenario_ids"), f"{w['id']} scenario trace differs from verified IAR family row")
        req(w.get("projection_group_ids") == source.get("projection_groups"), f"{w['id']} projection trace differs from verified IAR family row")
        expected_actions = source.get("actions")[:]
        if family == "P15-AWK-018":
            expected_actions = expected_actions + ["P15-ACT-020"]
        req(w.get("action_ids") == expected_actions, f"{w['id']} action trace differs from verified IAR family row")
        req(w.get("scenario_ids") and set(w["scenario_ids"]) <= scenario_ids, f"{w['id']} references unknown scenario")
        for sid in w["scenario_ids"]:
            req(family in scenario_by_id[sid].get("awkward_family_ids", []), f"{w['id']} uses {sid} outside its declared awkward family")
        req(set(w.get("projection_group_ids", [])) <= projection_ids, f"{w['id']} unknown projection")
        req(set(w.get("action_ids", [])) <= action_ids, f"{w['id']} unknown action")
        req(w.get("handoff_ids") and w.get("foundation_case_ids") and w.get("iar_case_ids") and w.get("integrated_case_ids"), f"{w['id']} incomplete trace assignment")
        req(w.get("composition_differential"), f"{w['id']} missing composition differential")
        has_upstream = bool(set(w["action_ids"]) & upstream_actions)
        req(has_upstream == w.get("may_present_upstream_mutation"), f"{w['id']} upstream-command presentation flag mismatch")
        if has_upstream:
            mutation_presenting.append(w["id"])
        used_scenarios |= set(w["scenario_ids"])
        used_pgs |= set(w["projection_group_ids"])
        used_actions |= set(w["action_ids"])
        used_handoffs |= set(w["handoff_ids"])

    req(used_scenarios == scenario_ids, "not all 24 stable scenarios are covered")
    req(used_pgs == projection_ids, "not all 12 projection groups are covered")
    req(used_actions == action_ids, "not all 20 actions are covered")
    req(len(mutation_presenting) == 7, "upstream command-presentation workflow count changed")

    handoffs = workflow.get("handoffs", [])
    handoff_ids = {x.get("id") for x in handoffs}
    req(handoff_ids == {f"P15-HO-{i:03d}" for i in range(1, 13)}, "handoff IDs changed")
    req(used_handoffs == handoff_ids, "not all 12 handoffs are exercised")
    req(all(x.get("owner") and x.get("boundary") for x in handoffs), "handoff owner/boundary missing")

    fc_expected = [x.get("id") for x in foundation_cases.get("cases", [])]
    iar_expected = [x.get("id") for x in iar_cases.get("cases", [])]
    iw_expected = [x.get("id") for x in cases.get("cases", [])]
    req(fc_expected == [f"PPIA15-FC-{i:03d}" for i in range(1, 33)], "Foundation case IDs changed")
    req(iar_expected == [f"P15-IAR-{i:03d}" for i in range(1, 41)], "IAR case IDs changed")
    req(iw_expected == [f"P15-IW-{i:03d}" for i in range(1, 19)], "integrated case IDs changed")
    exact_once([cid for w in wfs for cid in w["foundation_case_ids"]], fc_expected, "Foundation cases")
    exact_once([cid for w in wfs for cid in w["iar_case_ids"]], iar_expected, "IAR cases")
    exact_once([cid for w in wfs for cid in w["integrated_case_ids"]], iw_expected, "Integrated cases")
    req(cases.get("counts") == {"new_integrated_cases":18,"inherited_foundation_cases":32,"inherited_iar_cases":40,"effective_cases":90}, "integrated case counts changed")

    wf_by_id = {x["id"]: x for x in wfs}
    for c in cases.get("cases", []):
        req(c.get("workflow_id") in wf_by_id, f"{c['id']} references unknown workflow")
        req(wf_by_id[c["workflow_id"]]["integrated_case_ids"] == [c["id"]], f"{c['id']} workflow assignment mismatch")
        for field in ("title","composition_differential","authoritative_oracle","projection_oracle","recovery_oracle","forbidden"):
            req(c.get(field), f"{c['id']} missing {field}")

    common = workflow.get("common_sequence", [])
    req(common == [
        "establish_case_local_fixture_and_authority_inputs",
        "resolve_current_actor_permission_entitlement_and_visibility",
        "bind_stable_identity_and_owning_domain_before_derivatives",
        "obtain_or_confirm_owning_domain_authoritative_state",
        "apply_hidden_information_and_minimum_disclosure_reduction",
        "derive_ppia15_inspector_projection",
        "expose_only_governed_read_or_upstream_presented_actions",
        "execute_or_observe_scenario_specific_external_event_only_when_upstream_authorized",
        "handle_conflict_status_projection_or_offline_transition_without_invented_authority",
        "reauthorize_and_reproject_after_any_authority_change",
        "compare_visual_nonvisual_and_device_semantics_at_same_disclosure_ceiling",
        "assert_deterministic_oracle_for_authoritative_state_projection_actions_and_forbidden_outcomes",
        "record_case_local_provenance_trace_and_no_activation_assertions",
    ], "common deterministic workflow order changed")

    policy = workflow.get("workflow_policy", {})
    for key in ("permission_entitlement_filter_before_derivatives","stable_identity_before_display_name_reasoning","hidden_missing_external_equivalence","status_unknown_not_failure","accepted_event_distinct_from_projection","visual_nonvisual_disclosure_ceiling_equal","synthetic_noncanonical_only"):
        req(policy.get(key) is True, f"workflow invariant changed: {key}")
    for key in ("blind_ambiguous_mutation_retry","offline_local_state_is_authoritative_mutation","case_local_scale_is_capacity_promise","ppia11_balance_guarantee_allowed","ordinary_gm_modification_standalone_clone_allowed","f024_pack_lifecycle_invention","ppia15_creates_mutation_authority"):
        req(policy.get(key) is False, f"workflow boundary changed: {key}")

    gm = workflow.get("protected_nonclone_guard", {})
    req(gm.get("awkward_family_id") == "P15-AWK-004" and gm.get("ordinary_gm_modification_clone_count") == 0 and "stale-version" in gm.get("allowed_additive_composition", ""), "GM modification no-clone guard changed")
    sg = workflow.get("source_gap_guard", {})
    req(sg.get("gap_id") == "P15-GAP-001" and sg.get("foundation_case_id") == "PPIA15-FC-032" and sg.get("iar_case_id") == "P15-IAR-040" and sg.get("status") == "open-not-invented" and "unsupported" in sg.get("oracle", ""), "F024 source-gap guard changed")
    req(wf_by_id["P15-WF-018"].get("source_gap_guard") is True and "P15-ACT-020" in wf_by_id["P15-WF-018"]["action_ids"], "F024 workflow guard missing")

    gr = cases.get("global_requirements", {})
    for key in ("permission_filter_before_derivatives","stable_identity_before_display_name_reasoning","hidden_missing_equivalence_when_existence_protected","status_unknown_not_failure","accepted_event_distinct_from_projection","offline_local_not_authoritative","semantic_nonvisual_parity","fixture_isolation","synthetic_noncanonical","p15_gap_001_f024_open"):
        req(gr.get(key) is True, f"integrated case requirement changed: {key}")
    req(gr.get("ordinary_gm_modification_clone_count") == 0, "integrated GM clone count changed")
    for key in ("ppia11_balance_guarantee_allowed","runtime_activation","stage_a_a2_activation","tester_access","release","deployment","paid_service","production_credentials","canonical_promotion"):
        req(gr.get(key) is False, f"integrated case boundary changed: {key}")

    predecessor = index.get("immutable_predecessor_evidence", {})
    req(predecessor.get("foundation") == {"exact_validated_head":"d876093989e656d3cf8366c19755295ef0f785e8","hosted_workflows":"62/62","dedicated_run":"31652241636","pull_request":286,"merge":"a1f6b7380a07e65469ba8072e8aa4135d7b1e42f","merge_signature":"verified valid"}, "Foundation predecessor evidence changed")
    req(predecessor.get("expanded_iar") == {"exact_validated_head":"94029c704fa097f99440a58a64c4293d52b4ad36","hosted_workflows":"63/63","dedicated_run":"31653764114","successor_safe_transition_run":"31653764056","pull_request":287,"merge":"740683e33ff6e3a0b1a8672c06fbbf9d87fa3bf5","merge_signature":"verified valid"}, "Expanded IAR predecessor evidence changed")
    req(index.get("completion_effect") == "Intermediate PPIA-15 milestone only. This package does not by itself complete PPIA-15.", "package completion boundary changed")
    req(index.get("next_milestone") == "PPIA-15 Completion Contract / Evidence Closure", "next milestone changed")

    for phrase in ("18 integrated workflows","24 stable scenario contracts","32 foundation cases","40 iar cases","90 cases","zero standalone ppia-15 clones","p15-gap-001","mv-ia-f024","not ppia-15 completion","completion/evidence-closure"):
        req(phrase in candidate, f"candidate narrative missing {phrase!r}")

    tranches = {x.get("work_item_id"): x for x in backlog.get("tranches", [])}
    for dep in ("PPIA-09","PPIA-10","PPIA-11","PPIA-14"):
        req(tranches.get(dep, {}).get("status") == "completed_verified", f"{dep} dependency changed")
    req(backlog.get("current_work_item_id") == "PPIA-15" and tranches.get("PPIA-15", {}).get("status") in {"started","ready_for_review"}, "PPIA-15 backlog state changed")
    req(checkpoint.get("attempt_id") == "PPIA-15-attempt-001" and checkpoint.get("branch") == "governance/ppia-15-internal-alpha-test-content-expansion", "checkpoint identity changed")
    req(checkpoint.get("status") in {"started","ready_for_review"} and checkpoint.get("completed_at") is None, "integrated milestone cannot complete whole PPIA-15")
    req(checkpoint.get("unresolved_failures") == [] and checkpoint.get("owner_decision_required") is False, "PPIA-15 unresolved state")
    req(pointer.get("primary_attempt_id") == "PPIA-15-attempt-001", "pointer does not select PPIA-15")
    req(status.get("primary", {}).get("work_item_id") == "PPIA-15" and status.get("primary", {}).get("status") in {"started","ready_for_review"}, "compact status does not select PPIA-15")

    active = checkpoint.get("active_substep") or ""
    if "Integrated Expanded Regression Workflows / Traceability" in active:
        milestone_mode = "active_integrated_workflows"
    else:
        blob = json.dumps({"completed_substeps":checkpoint.get("completed_substeps", []),"validation":checkpoint.get("validation", []),"evidence":checkpoint.get("evidence", []),"last_verified_action":checkpoint.get("last_verified_action", "")}, ensure_ascii=False)
        req("PPIA-15 Integrated Expanded Regression Workflows / Traceability" in blob, "successor checkpoint lost integrated milestone evidence")
        req(any(x.get("command") == "Validate PPIA-15 Integrated Expanded Regression Workflows" and x.get("status") == "passed" for x in checkpoint.get("validation", [])), "successor checkpoint lacks passed integrated validation evidence")
        milestone_mode = "successor_after_verified_integrated_workflows"

    bounds = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized","a2_activation_authorized","release_authorized","deployment_authorized","tester_access_authorized","canonical_promotion_without_source_evidence_authorized"):
        req(bounds.get(key) is False, f"program boundary changed: {key}")
    req(all(v is False for v in workflow.get("nonactivation", {}).values()), "workflow nonactivation boundary changed")
    req(all(v is False for v in index.get("nonactivation", {}).values()), "package nonactivation boundary changed")

    print("PPIA-15 INTEGRATED EXPANDED REGRESSION WORKFLOWS: PASS")
    print("workflows=18 awkward_families=18 scenarios=24 projections=12 actions=20 handoffs=12")
    print("foundation_cases=32_exact_once iar_cases=40_exact_once integrated_cases=18_exact_once effective_cases=90")
    print("upstream_command_presentation_workflows=7 ppia15_mutation_authority=false")
    print("gm_baseline_clones=0 f024_gap=open-not-invented ppia11_balance_guarantee=false")
    print(f"milestone_mode={milestone_mode} runtime_activation=false a2_activation=false tester_access=false release=false deployment=false")


if __name__ == "__main__":
    main()
