#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
P = lambda name: BASE / name

FILES = {
    "workflow": P("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json"),
    "trace": P("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_TRACEABILITY_MATRIX_v0.1.0.json"),
    "cases": P("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_REFERENCE_CASES_v0.1.0.json"),
    "index": P("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_PACKAGE_INDEX_v0.1.0.json"),
    "candidate": P("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_WORKFLOW_CANDIDATE.md"),
    "taxonomy": P("PPIA-14_MESSAGE_STATE_TAXONOMY_v0.1.0.json"),
    "actors": P("PPIA-14_ACTOR_CONTEXT_AND_DELIVERY_MATRIX_v0.1.0.json"),
    "inspector": P("PPIA-14_MICROCOPY_INSPECTOR_CONTRACT_v0.1.0.json"),
    "actions": P("PPIA-14_MICROCOPY_ACTION_CONTRACT_MATRIX_v0.1.0.json"),
    "library": P("PPIA-14_MICROCOPY_LIBRARY_v0.1.0.json"),
    "foundation_cases": P("PPIA-14_FOUNDATION_REFERENCE_CASES_v0.1.0.json"),
    "iar_cases": P("PPIA-14_MICROCOPY_REFERENCE_CASES_v0.1.0.json"),
    "gaps": P("PPIA-14_SOURCE_GAPS_v0.1.0.json"),
}
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-14-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG = P("PPIA_PROGRAM_BACKLOG.json")


def fail(message: str) -> None:
    raise SystemExit("PPIA-14 INTEGRATED WORKFLOWS: FAIL — " + message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path):
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def exact_once(actual, expected, label):
    counts = Counter(actual)
    require(set(counts) == set(expected), f"{label} coverage set mismatch")
    require(all(v == 1 for v in counts.values()), f"{label} must be assigned exactly once")


def main() -> None:
    workflow = load(FILES["workflow"])
    trace = load(FILES["trace"])
    cases = load(FILES["cases"])
    index = load(FILES["index"])
    taxonomy = load(FILES["taxonomy"])
    actors = load(FILES["actors"])
    inspector = load(FILES["inspector"])
    actions = load(FILES["actions"])
    library = load(FILES["library"])
    foundation_cases = load(FILES["foundation_cases"])
    iar_cases = load(FILES["iar_cases"])
    gaps = load(FILES["gaps"])
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    backlog = load(BACKLOG)
    candidate = FILES["candidate"].read_text(encoding="utf-8")

    expected_counts = {
        "workflows": 18,
        "upstream_mutation_presenting_workflows": 2,
        "nonmutating_workflows": 16,
        "message_states": 18,
        "message_objects": 18,
        "roles": 9,
        "contexts": 20,
        "channels": 7,
        "projection_groups": 12,
        "actions": 20,
        "foundation_cases": 32,
        "iar_cases": 40,
        "integrated_cases": 36,
        "effective_cases": 108,
        "handoffs": 11,
    }
    require(workflow["counts"] == expected_counts, "workflow counts changed")
    require(trace["counts"] == expected_counts, "traceability counts changed")

    wfs = workflow["workflows"]
    require(len(wfs) == 18, "workflow count mismatch")
    require([x["id"] for x in wfs] == [f"P14-WF-{i:03d}" for i in range(1, 19)], "workflow IDs unstable")
    require([x["nominal_message_state_id"] for x in wfs] == [f"P14-MS-{i:03d}" for i in range(1, 19)], "nominal state mapping must be one-to-one")
    require([x["nominal_message_object_id"] for x in wfs] == [f"P14-MSG-{i:03d}" for i in range(1, 19)], "nominal message mapping must be one-to-one")

    taxonomy_ids = [x["id"] for x in taxonomy["message_states"]]
    library_ids = [x["id"] for x in library["message_objects"]]
    require(taxonomy_ids == [f"P14-MS-{i:03d}" for i in range(1, 19)], "Foundation state IDs changed")
    require(library_ids == [f"P14-MSG-{i:03d}" for i in range(1, 19)], "Microcopy message IDs changed")

    expected_roles = {x["role"] for x in actors["role_profiles"]}
    expected_contexts = set(actors["help_contexts"])
    expected_channels = {x["channel"] for x in actors["delivery_channels"]}
    expected_pgs = {x["id"] for x in inspector["projection_groups"]}
    expected_action_ids = {x["id"] for x in actions["actions"]}
    expected_handoffs = {f"P14-HO-{i:03d}" for i in range(1, 12)}

    require(set(v for w in wfs for v in w["roles"]) == expected_roles, "role coverage incomplete")
    require(set(v for w in wfs for v in w["contexts"]) == expected_contexts, "context coverage incomplete")
    require(set(v for w in wfs for v in w["channels"]) == expected_channels, "channel coverage incomplete")
    require(set(v for w in wfs for v in w["projection_group_ids"]) == expected_pgs, "projection-group coverage incomplete")
    require(set(v for w in wfs for v in w["actions"]) == expected_action_ids, "action coverage incomplete")
    require({x["id"] for x in workflow["handoffs"]} == expected_handoffs, "handoff IDs unstable")
    require(set(v for w in wfs for v in w["handoffs"]) == expected_handoffs, "handoff coverage incomplete")

    mutation_actions = {x["id"] for x in actions["actions"] if x["may_mutate_upstream"]}
    require(mutation_actions == {"P14-ACT-015", "P14-ACT-018"}, "upstream mutation presentation set changed")
    mutation_wfs = [w for w in wfs if w["may_present_upstream_mutation"]]
    require([w["id"] for w in mutation_wfs] == ["P14-WF-012", "P14-WF-015"], "only retry/report workflows may present upstream mutation")
    for w in wfs:
        contains_mutation_action = bool(set(w["actions"]) & mutation_actions)
        require(contains_mutation_action == w["may_present_upstream_mutation"], f"{w['id']} mutation presentation flag mismatch")
        require(w["sequence"][1] == "resolve_actor_role_context_permission_and_entitlement", f"{w['id']} must filter actor/authority before message selection")
        require(w["sequence"][2] == "apply_hidden_information_and_minimum_field_disclosure_reduction", f"{w['id']} must reduce disclosure before message selection")
        require(w["sequence"][-1] == "record_safe_audit_and_provenance_trace", f"{w['id']} missing audit/provenance trace")

    assigned_fc = [cid for w in wfs for cid in w["foundation_case_ids"]]
    assigned_iar = [cid for w in wfs for cid in w["iar_case_ids"]]
    assigned_iw = [cid for w in wfs for cid in w["integrated_case_ids"]]
    expected_fc = [x["id"] for x in foundation_cases["cases"]]
    expected_iar = [x["id"] for x in iar_cases["cases"]]
    expected_iw = [x["id"] for x in cases["cases"]]
    exact_once(assigned_fc, expected_fc, "Foundation cases")
    exact_once(assigned_iar, expected_iar, "Microcopy IAR cases")
    exact_once(assigned_iw, expected_iw, "Integrated cases")
    require(expected_iw == [f"P14-IW-{i:03d}" for i in range(1, 37)], "integrated case IDs unstable")

    action_key_to_id = {x["key"]: x["id"] for x in actions["actions"]}
    wf_by_id = {w["id"]: w for w in wfs}
    for c in cases["cases"]:
        require(c["permission_filter_required"] and c["nonvisual_equivalent_required"] and c["audit_trace_required"], f"{c['id']} missing required integrated assertions")
        require(c["runtime_activation"] is False, f"{c['id']} must not activate runtime")
        w = wf_by_id[c["workflow_id"]]
        selected_state = c["selected_message_state_id"]
        selected_message = c["selected_message_object_id"]
        if selected_state != w["nominal_message_state_id"]:
            require(selected_state in w["fallback_message_state_ids"], f"{c['id']} uses undeclared fallback state")
        require(selected_message == "P14-MSG-" + selected_state.split("-")[-1], f"{c['id']} state/message mismatch")
        for key in c["allowed_action_keys"]:
            require(key in action_key_to_id, f"{c['id']} unknown action key {key}")
            require(action_key_to_id[key] in w["actions"], f"{c['id']} action {key} absent from workflow")

    by_id = {w["id"]: w for w in wfs}
    require("P14-MS-002" in by_id["P14-WF-003"]["fallback_message_state_ids"], "hidden state must collapse to safe-unavailable")
    require("P14-ACT-010" in by_id["P14-WF-009"]["actions"] and "P14-ACT-015" not in by_id["P14-WF-009"]["actions"], "status-unknown must lookup status and forbid retry")
    require({"P14-ACT-010", "P14-ACT-015"}.issubset(by_id["P14-WF-012"]["actions"]), "safe idempotent retry workflow missing status/retry actions")
    require("P14-ACT-011" in by_id["P14-WF-010"]["actions"], "accepted Event/projection workflow missing refresh")
    require("P14-ACT-018" in by_id["P14-WF-015"]["actions"] and "P14-HO-007" in by_id["P14-WF-015"]["handoffs"], "issue reporting must remain F025-governed")
    require("P14-ACT-007" in by_id["P14-WF-016"]["actions"], "diagnostics workflow missing redacted preview")
    require("P14-MS-002" in by_id["P14-WF-017"]["fallback_message_state_ids"], "protected entitlement facts must collapse safely")
    require("P14-MS-002" in by_id["P14-WF-018"]["fallback_message_state_ids"] and "P14-HO-009" in by_id["P14-WF-018"]["handoffs"] and "P14-ACT-020" in by_id["P14-WF-018"]["actions"], "source-gap workflow boundary incomplete")

    policy = workflow["workflow_policy"]
    for key in (
        "permission_entitlement_filter_before_message_discovery",
        "hidden_missing_external_equivalence",
        "filter_before_counts_timing_interpolation_actions_diagnostics_support_exports_notifications_ai",
        "visual_nonvisual_disclosure_ceiling_equal",
        "idempotent_retry_requires_upstream_proof",
        "accepted_event_distinct_from_projection",
        "p13_teaching_ownership_preserved",
        "support_diagnostics_follow_f025",
    ):
        require(policy[key] is True, f"workflow invariant {key} changed")
    for key in (
        "status_unknown_is_failure",
        "blind_ambiguous_mutation_retry",
        "offline_local_state_is_authoritative_mutation",
        "copy_grants_permission_or_entitlement",
        "copy_resolves_conflict_or_approval",
        "copy_changes_gameplay_or_canonical_truth",
        "f024_pack_lifecycle_invention",
        "ai_decision_authority",
        "runtime_activation",
        "a2_activation",
        "release_activation",
        "deployment_activation",
        "tester_access_activation",
        "paid_service_activation",
        "production_activation",
    ):
        require(policy[key] is False, f"workflow boundary {key} changed")

    require(cases["counts"] == {"new_cases": 36, "inherited_foundation_cases": 32, "inherited_iar_cases": 40, "effective_cases": 108}, "integrated case counts changed")
    require(index["counts"] == {"workflows":18,"message_states":18,"message_objects":18,"roles":9,"contexts":20,"channels":7,"projection_groups":12,"actions":20,"handoffs":11,"new_reference_cases":36,"effective_reference_cases":108}, "package index counts changed")
    require(trace["coverage"]["effective_cases"] == "108", "traceability effective coverage changed")

    gap_by_id = {x["id"]: x for x in gaps["gaps"]}
    require(gap_by_id["P14-GAP-001"].get("status") == "open" and "f024" in json.dumps(gap_by_id["P14-GAP-001"]).lower(), "P14-GAP-001/F024 must remain explicit and open")
    require(gap_by_id["P14-GAP-002"].get("status") == "resolved_by_candidate", "Microcopy wording gap resolution regressed")

    require(checkpoint["work_item_id"] == "PPIA-14", "PPIA-14 checkpoint identity changed")
    require(checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"] == [], "PPIA-14 unresolved state changed")
    current_id = backlog["current_work_item_id"]
    if current_id == "PPIA-14":
        require(checkpoint["status"] in {"started", "ready_for_review"}, "active PPIA-14 checkpoint must remain active")
        require(checkpoint.get("active_substep") and "Integrated Error Recovery Permission Workflows / Traceability" in checkpoint["active_substep"], "checkpoint is not on integrated workflow substep")
        selected = [x for x in pointer["active_attempts"] if x.get("owner_selected")]
        require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-14", "runtime pointer must select PPIA-14")
        require(status["primary"]["work_item_id"] == "PPIA-14", "compact status must select PPIA-14")
        continuity_mode = "active_ppia14"
    else:
        order = backlog["execution_order"]
        require(current_id in order and order.index(current_id) > order.index("PPIA-14"), "historical integrated-workflow validation may only occur after PPIA-14")
        tranches = {x["work_item_id"]: x for x in backlog["tranches"]}
        require(tranches["PPIA-14"]["status"] == "completed_verified", "historical PPIA-14 backlog must be completed_verified")
        require(checkpoint["status"] == "completed_verified" and checkpoint.get("active_substep") is None and checkpoint.get("completed_at"), "historical PPIA-14 checkpoint must be completed_verified")
        continuity_mode = "historical_after_ppia14"

    low = candidate.lower()
    for phrase in (
        "18 end-to-end workflows",
        "108 effective deterministic cases",
        "status-unknown",
        "blind ambiguous-mutation retry",
        "accepted durable event",
        "p14-gap-001",
        "mv-ia-f024 pack lifecycle",
        "ppia-13 remains `completed_verified`",
        "validate ppia-14 integrated error recovery permission workflows and traceability",
        "stage-a-a2",
    ):
        require(phrase in low, f"candidate narrative missing {phrase!r}")

    all_text = (json.dumps(workflow) + json.dumps(trace) + json.dumps(cases) + candidate).lower()
    for prohibited in (
        "runtime_activation=true",
        "a2_activation=true",
        "release_activation=true",
        "deployment_activation=true",
        "tester_access_activation=true",
        "paid_service_activation=true",
        "production_activation=true",
    ):
        require(prohibited not in all_text, f"prohibited authorization {prohibited!r}")

    print("PPIA-14 INTEGRATED WORKFLOWS: PASS")
    print("workflows=18 states=18 messages=18 roles=9 contexts=20 channels=7")
    print("coverage=12 projection groups / 20 actions / 11 handoffs")
    print("cases=36 integrated + 32 Foundation + 40 IAR = 108 effective")
    print("hidden_missing_equivalence=true status_unknown_not_failure=true f024_gap_preserved=true")
    print(f"continuity_mode={continuity_mode} runtime_activation=false")


if __name__ == "__main__":
    main()
