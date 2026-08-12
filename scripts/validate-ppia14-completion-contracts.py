#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-14-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"

MILESTONES = [
    ("foundation_source_and_message_state_inventory", "ea21b8d4d3e2ffe816fa53a8591e28892b8140f1", "f693accd98edbc3932ce2a4d80c920a48731924c", 57, 281),
    ("microcopy_library_inspector_action_reference", "08d250cd882989cae9d35e9035166e71fb9ea1ff", "bcd2e5317fc477fd679b96303deed4f79dc161d8", 58, 282),
    ("integrated_error_recovery_permission_workflows_traceability", "22d19e7681fed0e3193976d5f4dd181225ef1a3d", "73c534f8baa2fa96050557d002a71db7e789aca7", 59, 283),
]

SURFACE_COUNTS = {
    "acceptance_categories": 18,
    "message_states": 18,
    "message_objects": 18,
    "authority_domains": 8,
    "hidden_information_boundaries": 11,
    "roles": 9,
    "contexts": 20,
    "channels": 7,
    "safe_affordance_classes": 13,
    "foundation_cases": 32,
    "projection_groups": 12,
    "actions": 20,
    "iar_cases": 40,
    "workflows": 18,
    "handoffs": 11,
    "integrated_cases": 36,
    "effective_cases": 108,
}

WORKFLOW_COUNTS = {
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


def load(path: Path) -> dict:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def j(name: str) -> dict:
    return load(BASE / name)


def fail(message: str) -> None:
    raise SystemExit("PPIA-14 COMPLETION CONTRACT: FAIL — " + message)


def req(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def ids(rows: list[dict], key: str = "id") -> list[str]:
    return [row[key] for row in rows]


def main() -> None:
    taxonomy = j("PPIA-14_MESSAGE_STATE_TAXONOMY_v0.1.0.json")
    authority = j("PPIA-14_AUTHORITY_AND_HIDDEN_INFORMATION_BOUNDARY_MATRIX_v0.1.0.json")
    actor = j("PPIA-14_ACTOR_CONTEXT_AND_DELIVERY_MATRIX_v0.1.0.json")
    affordances = j("PPIA-14_SAFE_AFFORDANCE_CLASSES_v0.1.0.json")
    foundation_cases = j("PPIA-14_FOUNDATION_REFERENCE_CASES_v0.1.0.json")
    gaps = j("PPIA-14_SOURCE_GAPS_v0.1.0.json")
    library = j("PPIA-14_MICROCOPY_LIBRARY_v0.1.0.json")
    inspector = j("PPIA-14_MICROCOPY_INSPECTOR_CONTRACT_v0.1.0.json")
    actions = j("PPIA-14_MICROCOPY_ACTION_CONTRACT_MATRIX_v0.1.0.json")
    iar_cases = j("PPIA-14_MICROCOPY_REFERENCE_CASES_v0.1.0.json")
    microcopy_package = j("PPIA-14_MICROCOPY_LIBRARY_PACKAGE_INDEX_v0.1.0.json")
    integrated_package = j("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_PACKAGE_INDEX_v0.1.0.json")
    workflows = j("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json")
    trace = j("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_TRACEABILITY_MATRIX_v0.1.0.json")
    integrated_cases = j("PPIA-14_INTEGRATED_ERROR_RECOVERY_PERMISSION_REFERENCE_CASES_v0.1.0.json")
    acceptance = j("PPIA-14_COMPLETION_ACCEPTANCE_MATRIX_v0.1.0.json")
    scope = j("PPIA-14_COMPLETION_SCOPE_LOCK_v0.1.0.json")
    package = j("PPIA-14_COMPLETION_PACKAGE_INDEX_v0.1.0.json")
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    backlog = load(BACKLOG)
    report = (BASE / "PPIA-14_COMPLETION_REPORT.md").read_text(encoding="utf-8").lower()
    readme = (BASE / "PPIA-14_COMPLETION_README.md").read_text(encoding="utf-8").lower()

    # Immutable predecessor milestone evidence.
    verified = package.get("verified_milestones", [])
    req(len(verified) == 3, "three verified predecessor milestone records required")
    for rec, exp in zip(verified, MILESTONES):
        expected = {"milestone": exp[0], "validated_head": exp[1], "merge": exp[2], "hosted_workflows": exp[3], "pull_request": exp[4]}
        for key, value in expected.items():
            req(rec.get(key) == value, f"milestone evidence changed {exp[0]} field {key}")
    req(verified[2].get("dedicated_run") == "31646016233", "integrated dedicated run evidence changed")
    req(package.get("milestone") == "final_completion_gate", "completion package milestone changed")
    req(package.get("state") == "completion_candidate_only_until_exact_head_all_green_and_merge", "completion package state changed")
    req(package.get("transition_after_completion") == "PPIA-14 -> PPIA-15 separate governed operation", "successor transition boundary changed")
    req(package.get("completion_surface") == SURFACE_COUNTS, "completion surface counts changed")

    # Foundation identities and global nonleak/recovery rules.
    state_rows = taxonomy.get("message_states", [])
    req(ids(state_rows) == [f"P14-MS-{i:03d}" for i in range(1, 19)], "message-state IDs changed")
    req(len(authority.get("authority_domains", [])) == 8, "authority-domain count changed")
    req(len(authority.get("hidden_information_boundaries", [])) == 11, "hidden-information boundary count changed")
    req("missing" in authority.get("equivalence_rule", "").lower() and "hidden" in authority.get("equivalence_rule", "").lower(), "hidden/missing equivalence rule lost")
    global_rules = taxonomy.get("global_rules", {})
    for key in (
        "permission_filter_before_copy_selection",
        "permission_filter_before_counts_search_diagnostics_support_exports_notifications_ai",
        "status_unknown_is_not_failure",
        "accepted_event_is_distinct_from_projection",
        "offline_local_state_is_not_authoritative_mutation",
        "hidden_and_missing_must_not_be_distinguished_when_existence_is_protected",
    ):
        req(global_rules.get(key) is True, f"Foundation invariant disabled {key}")
    req(global_rules.get("copy_can_change_authoritative_state") is False, "copy authority boundary weakened")

    role_names = [row.get("role") for row in actor.get("role_profiles", [])]
    req(role_names == ["invited-tester", "player", "game-master", "assistant-gm", "content-creator", "observer", "owner-admin", "service-actor", "ai"], "governed role set changed")
    req(len(actor.get("help_contexts", [])) == 20, "help-context count changed")
    req(len(actor.get("delivery_channels", [])) == 7, "delivery-channel count changed")
    req(ids(affordances.get("affordance_classes", [])) == [f"P14-AF-{i:03d}" for i in range(1, 14)], "safe affordance IDs changed")
    mutating_affordances = {row["id"] for row in affordances["affordance_classes"] if row.get("may_mutate")}
    req(mutating_affordances == {"P14-AF-006", "P14-AF-012"}, "mutation-labelled affordance boundary changed")
    forbidden = " ".join(affordances.get("forbidden_affordances", [])).lower()
    for phrase in ("blind retry", "hidden resource", "permission escalation", "forced conflict overwrite", "raw diagnostics", "automatic screenshot", "f024", "ai action"):
        req(phrase in forbidden, f"forbidden affordance lost {phrase!r}")
    req(foundation_cases.get("case_count") == 32 and len(foundation_cases.get("cases", [])) == 32, "Foundation deterministic-case count changed")

    # Gaps: wording gap resolved; F024 remains open.
    gap_by_id = {row["id"]: row for row in gaps.get("gaps", [])}
    req(gap_by_id["P14-GAP-001"].get("status") == "open", "P14-GAP-001/F024 must remain open")
    req(gap_by_id["P14-GAP-001"].get("inherited_id") == "P13-GAP-001", "P14-GAP-001 provenance changed")
    req(gap_by_id["P14-GAP-002"].get("status") == "resolved_by_candidate", "P14-GAP-002 wording-library resolution lost")

    # Complete message library and safe Inspector/action projection.
    message_rows = library.get("message_objects", [])
    req(ids(message_rows) == [f"P14-MSG-{i:03d}" for i in range(1, 19)], "message-object IDs changed")
    req([row.get("message_state_id") for row in message_rows] == [f"P14-MS-{i:03d}" for i in range(1, 19)], "state/message one-to-one mapping changed")
    for row in message_rows:
        for key in ("semantic_intent_key", "title_key", "body_key", "default_en", "severity_semantic", "disclosure_class", "allowed_interpolation_keys", "nonvisual_status_key", "default_en_nonvisual", "support_reference_policy"):
            req(key in row, f"message {row.get('id')} missing {key}")
    msg2, msg3 = message_rows[1], message_rows[2]
    req(msg2.get("default_en") == msg3.get("default_en"), "hidden/safe-unavailable visual wording must remain equivalent")
    req(msg2.get("default_en_nonvisual") == msg3.get("default_en_nonvisual"), "hidden/safe-unavailable nonvisual wording must remain equivalent")
    req("status" in message_rows[8]["default_en"]["body"].lower(), "status-unknown wording lost status lookup guidance")
    req("recorded" in message_rows[9]["default_en"]["body"].lower(), "accepted Event/projection wording lost durable-state distinction")
    req(len(inspector.get("projection_groups", [])) == 12 and ids(inspector["projection_groups"]) == [f"P14-PG-{i:03d}" for i in range(1, 13)], "Inspector projection groups changed")
    req(actions.get("counts") == {"actions": 20, "mutating_presentations": 2, "nonmutating_presentations": 18}, "microcopy action counts changed")
    req(ids(actions.get("actions", [])) == [f"P14-ACT-{i:03d}" for i in range(1, 21)], "microcopy action IDs changed")
    mutating_actions = {row["id"] for row in actions["actions"] if row.get("may_mutate_upstream")}
    req(mutating_actions == {"P14-ACT-015", "P14-ACT-018"}, "upstream mutation-presentation boundary changed")
    req(microcopy_package.get("counts") == {"message_objects": 18, "projection_groups": 12, "actions": 20, "new_reference_cases": 40, "effective_reference_cases": 72}, "Microcopy package counts changed")
    req(iar_cases.get("counts") == {"new_cases": 40, "inherited_foundation_cases": 32, "effective_cases": 72}, "Microcopy IAR case counts changed")

    # Integrated workflow traceability.
    req(workflows.get("counts") == WORKFLOW_COUNTS, "integrated workflow counts changed")
    req(integrated_package.get("counts") == {"workflows":18,"message_states":18,"message_objects":18,"roles":9,"contexts":20,"channels":7,"projection_groups":12,"actions":20,"handoffs":11,"new_reference_cases":36,"effective_reference_cases":108}, "integrated package counts changed")
    req(trace.get("counts", {}).get("workflows") == 18 and trace.get("counts", {}).get("effective_cases") == 108 and trace.get("counts", {}).get("handoffs") == 11, "traceability counts changed")
    req(integrated_cases.get("counts", {}).get("new_cases") == 36 and integrated_cases.get("counts", {}).get("effective_cases") == 108, "integrated reference-case counts changed")

    workflow_rows = workflows.get("workflows", [])
    req(ids(workflow_rows) == [f"P14-WF-{i:03d}" for i in range(1, 19)], "workflow IDs changed")
    req([row.get("nominal_message_state_id") for row in workflow_rows] == [f"P14-MS-{i:03d}" for i in range(1, 19)], "workflow/state one-to-one coverage changed")
    req([row.get("nominal_message_object_id") for row in workflow_rows] == [f"P14-MSG-{i:03d}" for i in range(1, 19)], "workflow/message one-to-one coverage changed")
    req(sum(bool(row.get("may_present_upstream_mutation")) for row in workflow_rows) == 2, "integrated mutation-presenting workflow count changed")

    foundation_ids = ids(foundation_cases.get("cases", []))
    iar_ids = ids(iar_cases.get("cases", []))
    integrated_ids = ids(integrated_cases.get("cases", []))
    assigned_foundation = [case_id for row in workflow_rows for case_id in row.get("foundation_case_ids", [])]
    assigned_iar = [case_id for row in workflow_rows for case_id in row.get("iar_case_ids", [])]
    assigned_integrated = [case_id for row in workflow_rows for case_id in row.get("integrated_case_ids", [])]
    req(len(assigned_foundation) == 32 and sorted(assigned_foundation) == sorted(foundation_ids), "Foundation cases must be assigned exactly once")
    req(len(assigned_iar) == 40 and sorted(assigned_iar) == sorted(iar_ids), "IAR cases must be assigned exactly once")
    req(len(assigned_integrated) == 36 and sorted(assigned_integrated) == sorted(integrated_ids), "integrated cases must be assigned exactly once")

    req({r for row in workflow_rows for r in row.get("roles", [])} == set(role_names), "workflow role coverage incomplete")
    req({c for row in workflow_rows for c in row.get("contexts", [])} == set(actor.get("help_contexts", [])), "workflow context coverage incomplete")
    req({c for row in workflow_rows for c in row.get("channels", [])} == {row["channel"] for row in actor.get("delivery_channels", [])}, "workflow channel coverage incomplete")
    req({a for row in workflow_rows for a in row.get("actions", [])} == {f"P14-ACT-{i:03d}" for i in range(1, 21)}, "workflow action coverage incomplete")
    req({h for row in workflow_rows for h in row.get("handoffs", [])} == {f"P14-HO-{i:03d}" for i in range(1, 12)}, "workflow handoff coverage incomplete")
    req({p for row in workflow_rows for p in row.get("projection_group_ids", [])} == {f"P14-PG-{i:03d}" for i in range(1, 13)}, "workflow projection-group coverage incomplete")

    policy = workflows.get("workflow_policy", {})
    true_policy = (
        "permission_entitlement_filter_before_message_discovery",
        "hidden_missing_external_equivalence",
        "filter_before_counts_timing_interpolation_actions_diagnostics_support_exports_notifications_ai",
        "visual_nonvisual_disclosure_ceiling_equal",
        "idempotent_retry_requires_upstream_proof",
        "accepted_event_distinct_from_projection",
        "p13_teaching_ownership_preserved",
        "support_diagnostics_follow_f025",
    )
    false_policy = (
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
    )
    for key in true_policy:
        req(policy.get(key) is True, f"workflow policy disabled {key}")
    for key in false_policy:
        req(policy.get(key) is False, f"workflow prohibition weakened {key}")

    # Completion acceptance artifacts.
    req(acceptance.get("counts") == SURFACE_COUNTS, "completion acceptance counts changed")
    req(ids(acceptance.get("categories", [])) == [f"P14-CG-{i:02d}" for i in range(1, 19)], "completion acceptance category IDs changed")
    req(scope.get("scope_locked") is True and len(scope.get("required_categories", [])) == 18, "completion scope lock changed")
    req("transition_to_PPIA_15_before_verified_completion" in scope.get("prohibited_shortcuts", []), "premature successor transition prohibition lost")
    req("P14-GAP-001" in scope.get("retained_gap", "") and "F024" in scope.get("retained_gap", ""), "retained F024 gap lost from scope lock")
    req("P14-GAP-002" in scope.get("resolved_gap", ""), "resolved wording gap lost from scope lock")

    report_phrases = (
        "complete permission-safe error/recovery microcopy library",
        "eighteen stable message objects",
        "hidden-vs-missing equivalence",
        "permission and entitlement first",
        "status unknown and retry safety",
        "operation receipt/status evidence remains upstream-owned",
        "accepted event vs projection",
        "p14-gap-001",
        "p14-gap-002",
        "ppia-13 ownership boundary",
        "108 effective deterministic cases",
        "no application runtime",
        "ppia-14 → ppia-15 transition",
    )
    for phrase in report_phrases:
        req(phrase in report, f"completion report missing {phrase!r}")
    for phrase in ("p14-gap-001", "p14-gap-002", "exact pull-request head", "ppia-14 → ppia-15", "does not authorize or activate"):
        req(phrase in readme, f"completion readme missing {phrase!r}")

    # Current completion-review mode vs future historical mode.
    tranches = {row["work_item_id"]: row for row in backlog.get("tranches", [])}
    req(tranches["PPIA-08"]["status"] == "completed_verified", "PPIA-08 dependency changed")
    req(tranches["PPIA-13"]["status"] == "completed_verified", "PPIA-13 dependency changed")
    current = backlog.get("current_work_item_id")
    if current == "PPIA-14":
        req(tranches["PPIA-14"]["status"] == "started" and tranches["PPIA-15"]["status"] == "planned", "completion review backlog state invalid")
        req(checkpoint.get("status") in {"started", "ready_for_review"}, "PPIA-14 checkpoint must be active during completion review")
        req("completion contract" in checkpoint.get("active_substep", "").lower(), "PPIA-14 checkpoint must select final completion gate")
        selected = [row for row in pointer.get("active_attempts", []) if row.get("owner_selected")]
        req(len(selected) == 1 and selected[0].get("work_item_id") == "PPIA-14", "runtime pointer must select PPIA-14 during completion review")
        req(status.get("primary", {}).get("work_item_id") == "PPIA-14", "compact runtime status must select PPIA-14 during completion review")
        mode = "current"
    else:
        req(tranches["PPIA-14"]["status"] == "completed_verified", "historical PPIA-14 must be completed_verified")
        req(checkpoint.get("status") == "completed_verified" and checkpoint.get("active_substep") is None, "historical PPIA-14 checkpoint must be finalized")
        req(checkpoint.get("pull_request") and checkpoint.get("merge_commit") and checkpoint.get("latest_pushed_commit"), "historical PPIA-14 immutable completion evidence incomplete")
        req(any(row.get("command") == "Validate PPIA-14 Completion Contract" and row.get("status") == "passed" for row in checkpoint.get("validation", [])), "historical PPIA-14 completion validation missing")
        ev = json.dumps(checkpoint.get("evidence", []), ensure_ascii=False).lower()
        for phrase in ("pull_request", "merge", "ci_run"):
            req(phrase in ev, f"historical PPIA-14 evidence missing {phrase}")
        mode = "historical"

    req(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], "PPIA-14 unresolved state")
    req(checkpoint.get("roadmap_projection_pending") is True, "roadmap projection should remain batched through completion review/transition")
    boundaries = backlog.get("boundaries", {})
    for key in ("application_runtime_mutation_authorized", "a2_activation_authorized", "release_authorized", "deployment_authorized", "tester_access_authorized", "canonical_promotion_without_source_evidence_authorized"):
        req(boundaries.get(key) is False, f"completion gate may not enable {key}")
    req(boundaries.get("requires_codex") is False, "PPIA completion gate must not require Codex")

    print("PPIA-14 COMPLETION CONTRACT: PASS")
    print("surface=18 states / 18 messages / 9 roles / 20 contexts / 7 channels / 12 projections / 20 actions / 18 workflows / 11 handoffs / 108 cases")
    print("gaps=P14-GAP-002 resolved; P14-GAP-001/F024 retained open")
    print("continuity_mode=" + mode + " runtime_activation=false")


if __name__ == "__main__":
    main()
