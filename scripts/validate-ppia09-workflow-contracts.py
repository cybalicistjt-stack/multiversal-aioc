#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = BASE / "PPIA-09_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
TRACE = BASE / "PPIA-09_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"
NOTE = BASE / "PPIA-09_WORKFLOW_AUTHORING_CANDIDATE.md"
TAXONOMY = BASE / "PPIA-09_INVESTIGATION_MYSTERY_TAXONOMY_v0.1.0.json"
AUTHORITY = BASE / "PPIA-09_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
INSPECTOR = BASE / "PPIA-09_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json"
SOLVABILITY = BASE / "PPIA-09_SOLVABILITY_UNCERTAINTY_AUTHORING_CONTRACT_v0.1.0.json"
CASES = BASE / "PPIA-09_REFERENCE_CASES_v0.1.0.json"
CHECKPOINT = ROOT / "governance/ai/work-state/PPIA-09-attempt-001.json"
POINTER = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

INSPECTOR_FINAL_HEAD = "844b9e100ea3fe9bbf009ef29764967173a331f5"
INSPECTOR_PR = 254
INSPECTOR_MERGE = "5768ce7864cac4e03e12a610c22d126797583599"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-09 WORKFLOW CONTRACTS: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (WORKFLOWS, TRACE, NOTE, TAXONOMY, AUTHORITY, INSPECTOR, SOLVABILITY, CASES, CHECKPOINT, POINTER, STATUS):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    doc = load(WORKFLOWS)
    trace = load(TRACE)
    taxonomy = load(TAXONOMY)
    authority = load(AUTHORITY)
    inspector = load(INSPECTOR)
    solv = load(SOLVABILITY)
    cases_doc = load(CASES)
    checkpoint = load(CHECKPOINT)
    pointer = load(POINTER)
    status = load(STATUS)
    note = NOTE.read_text(encoding="utf-8")

    require(doc.get("format") == "multiversal-ppia09-workflow-authoring-contract-matrix", "wrong workflow format")
    require(doc.get("version") == "0.1.0" and doc.get("work_item") == "PPIA-09", "wrong workflow identity/version")
    expected_inherits = [TAXONOMY.name, AUTHORITY.name, INSPECTOR.name, SOLVABILITY.name, CASES.name]
    require(doc.get("inherits") == expected_inherits, "workflow inheritance changed")

    workflows = doc.get("workflows", [])
    expected_workflow_ids = [f"P9-WF-{n:03d}" for n in range(1, 19)]
    require(len(workflows) == 18, f"expected 18 workflows, got {len(workflows)}")
    require([w.get("workflow_id") for w in workflows] == expected_workflow_ids, "workflow IDs must be continuous P9-WF-001..018")

    required_fields = (
        "name", "primary_personas", "entry_points", "preconditions", "steps", "outputs", "projection_groups",
        "presentation_profiles", "actions", "reference_cases", "handoffs", "mutation_owner", "privacy_requirements",
        "recovery_requirements", "accessibility_requirements", "forbidden_mutations",
    )
    for workflow in workflows:
        for key in required_fields:
            require(workflow.get(key), f"{workflow['workflow_id']} missing {key}")

    expected_pgs = [f"P9-PG-{n:03d}" for n in range(1, 17)]
    expected_profiles = taxonomy.get("presentation_profiles", [])
    expected_actions = [f"P9-ACT-{n:03d}" for n in range(1, 31)]
    expected_cases = [f"PPIA09-RC-{n:03d}" for n in range(1, 37)]
    expected_handoffs = [f"P9-HO-{n:03d}" for n in range(1, 13)]

    require(len(taxonomy.get("identity_state_layers", [])) == 16, "taxonomy must retain 16 semantic layers")
    require(len(expected_profiles) == 12, "taxonomy must retain 12 presentation profiles")
    require([x.get("projection_group_id") for x in inspector.get("projection_groups", [])] == expected_pgs, "verified projection set changed")
    actions = inspector.get("action_contracts", [])
    require([x.get("action_id") for x in actions] == expected_actions, "verified action set changed")
    require([x.get("case_id") for x in cases_doc.get("cases", [])] == expected_cases, "verified reference-case set changed")
    require([x.get("id") for x in authority.get("domain_handoffs", [])] == expected_handoffs, "verified handoff set changed")

    action_by_id = {x["action_id"]: x for x in actions}
    writes = [x for x in actions if x.get("mutation") == "write"]
    reads = [x for x in actions if x.get("mutation") == "read"]
    require(len(writes) == 22 and len(reads) == 8, "verified 22-write / 8-read action split changed")
    mutation_workflows = [w for w in workflows if w.get("authoritative_mutation_performed") is True]
    read_only_workflows = [w for w in workflows if w.get("authoritative_mutation_performed") is False]
    require(len(mutation_workflows) == 15, f"expected 15 mutation workflows, got {len(mutation_workflows)}")
    require(len(read_only_workflows) == 3, f"expected 3 read-only workflows, got {len(read_only_workflows)}")
    for workflow in mutation_workflows:
        workflow_writes = [action_by_id[a] for a in workflow["actions"] if action_by_id[a].get("mutation") == "write"]
        require(workflow_writes, f"{workflow['workflow_id']} claims mutation but invokes no write")
        for action in workflow_writes:
            inputs = set(action.get("inputs", []))
            require("expected_version" in inputs, f"{action['action_id']} missing expected_version")
            require("operation_id" in inputs, f"{action['action_id']} missing operation_id")
    for workflow in read_only_workflows:
        require(all(action_by_id[a].get("mutation") == "read" for a in workflow["actions"]), f"{workflow['workflow_id']} read-only path invokes a write")

    routed_pgs = {x for w in workflows for x in w["projection_groups"]}
    routed_profiles = {x for w in workflows for x in w["presentation_profiles"]}
    routed_actions = {x for w in workflows for x in w["actions"]}
    routed_cases = [x for w in workflows for x in w["reference_cases"]]
    routed_handoffs = {x for w in workflows for x in w["handoffs"]}
    require(routed_pgs == set(expected_pgs), "workflow layer must route all and only 16 projection groups")
    require(routed_profiles == set(expected_profiles), "workflow layer must route all and only 12 presentation profiles")
    require(routed_actions == set(expected_actions), "workflow layer must route all and only 30 actions")
    require(set(routed_cases) == set(expected_cases), "workflow layer must route all and only 36 reference cases")
    require(all(v == 1 for v in Counter(routed_cases).values()), "each reference case must be assigned exactly once")
    require(routed_handoffs == set(expected_handoffs), "workflow layer must exercise all and only 12 handoffs")

    policy = doc.get("workflow_policy", {})
    require(policy.get("workflow_count") == 18, "workflow policy count changed")
    require(policy.get("authoritative_mutation_workflow_count") == 15, "mutation workflow policy count changed")
    require(policy.get("read_only_workflow_count") == 3, "read-only workflow policy count changed")
    for key in (
        "all_16_projection_groups_required", "all_12_presentation_profiles_required", "all_30_actions_required",
        "all_36_reference_cases_required", "all_12_domain_handoffs_required", "permission_filter_before_aggregation",
        "expected_version_operation_id_for_authoritative_mutations",
    ):
        require(policy.get(key) is True, f"workflow policy lost {key}")
    for key in (
        "truth_auto_promotion_allowed", "diagnostic_mutates_truth_or_reveal_state", "hidden_content_in_unauthorized_derivatives",
        "graph_layout_authoritative", "universal_clue_count_required", "contradiction_auto_adjudicates_truth",
        "evidence_reference_transfers_ownership", "ai_proposal_authoritative_without_acceptance", "runtime_activation",
    ):
        require(policy.get(key) is False, f"workflow policy boundary changed: {key}")

    require(trace.get("format") == "multiversal-ppia09-workflow-traceability-matrix", "wrong traceability format")
    require(trace.get("workflow_count") == 18 and trace.get("authoritative_mutation_workflow_count") == 15 and trace.get("read_only_workflow_count") == 3, "trace workflow counts changed")
    require(trace.get("expected_projection_groups") == expected_pgs, "trace projection set changed")
    require(trace.get("expected_presentation_profiles") == expected_profiles, "trace presentation-profile set changed")
    require(trace.get("expected_actions") == expected_actions, "trace action set changed")
    require(trace.get("expected_reference_cases") == expected_cases, "trace reference-case set changed")
    require(trace.get("expected_handoffs") == expected_handoffs, "trace handoff set changed")
    trace_rows = trace.get("workflow_trace_rows", [])
    require([x.get("workflow_id") for x in trace_rows] == expected_workflow_ids, "trace workflow rows changed")
    require(all(x.get("journey") and x.get("boundary_focus") for x in trace_rows), "trace row missing journey/boundary focus")
    expected_summary = {
        "projection_groups":{"expected":16,"covered":16,"gaps":0},
        "presentation_profiles":{"expected":12,"covered":12,"gaps":0},
        "actions":{"expected":30,"covered":30,"gaps":0},
        "reference_cases":{"expected":36,"covered":36,"gaps":0},
        "handoffs":{"expected":12,"covered":12,"gaps":0},
    }
    require(trace.get("coverage_summary") == expected_summary, "traceability gaps/counts changed")
    require(len(trace.get("end_to_end_assertions", [])) == 12, "expected 12 end-to-end trace assertions")

    # Read-only diagnostic boundaries remain inherited rather than redefined by workflow convenience.
    require(solv["solvability_diagnostic"]["status"] == "governed_ppia09_design_not_recovered_source_canon", "solvability authority label changed")
    require(any("at least two places" in x.lower() for x in solv["source_boundary"]["source_backed"]), "source-grounded redundancy guidance missing")
    require(any("universal required clue count" in x.lower() for x in solv["source_boundary"]["not_source_defined"]), "universal clue-count source gap missing")
    require(inspector["projection_policy"]["server_side_filter_before_resolution_and_aggregation"] is True, "permission-before-derivatives changed")
    require(inspector["projection_policy"]["contradiction_auto_adjudicates_truth"] is False, "contradiction truth boundary changed")
    require(inspector["action_policy"]["diagnostic_mutates_truth_or_reveal_state"] is False, "diagnostic mutation boundary changed")

    full = (json.dumps(doc, ensure_ascii=False) + "\n" + json.dumps(trace, ensure_ascii=False) + "\n" + note).lower()
    for phrase in (
        "18 end-to-end investigation/mystery workflows", "15 workflows perform authoritative mutation", "30 actions",
        "22 authoritative mutations", "36 deterministic reference cases", "24 f011 deterministic fixtures",
        "the vanishing of dr. wen", "at least two places", "no mandatory universal numeric probability scale",
        "permission filtering", "objective truth", "player knowledge", "contradiction", "false-lead",
        "solvability", "read-only", "universal clue-count", "ownerdomain", "objectid", "objectversion",
        "ppia-12", "expected_version", "operation_id", "status/current-version", "semantic nonvisual",
        "proposal-only", "not ppia-09 complete", "no application runtime", "stage-a-a2",
    ):
        require(phrase in full, f"missing required workflow boundary {phrase!r}")

    # Milestone continuity supports active-candidate mode and immutable historical mode after merge.
    require(checkpoint.get("work_item_id") == "PPIA-09" and checkpoint.get("status") == "started", "PPIA-09 checkpoint identity/state mismatch")
    require(checkpoint.get("branch") == "governance/ppia-09-investigation-mystery-authoring", "PPIA-09 branch mismatch")
    require(checkpoint.get("owner_decision_required") is False and checkpoint.get("unresolved_failures") == [], "PPIA-09 checkpoint unresolved state")
    history = json.dumps({
        "last_verified_action": checkpoint.get("last_verified_action"),
        "completed_substeps": checkpoint.get("completed_substeps", []),
        "validation": checkpoint.get("validation", []),
        "evidence": checkpoint.get("evidence", []),
    }, ensure_ascii=False).lower()
    for value in (INSPECTOR_FINAL_HEAD.lower(), f"pr #{INSPECTOR_PR}", INSPECTOR_MERGE.lower()):
        require(value in history, f"immutable inspector/reference evidence missing {value}")
    workflow_historical = "ppia-09 workflow" in history and "squash merge" in history
    if not workflow_historical:
        active = ((checkpoint.get("active_substep") or "") + " " + (checkpoint.get("next_action") or "")).lower()
        require("workflow" in active and "investigation/mystery" in active, "checkpoint must remain on workflow milestone before merge")
    require(pointer.get("primary_attempt_id") == "PPIA-09-attempt-001", "pointer must select PPIA-09")
    require(status.get("primary", {}).get("work_item_id") == "PPIA-09" and status.get("primary", {}).get("status") == "started", "compact status must select started PPIA-09")

    print("PPIA-09 INVESTIGATION / MYSTERY WORKFLOWS: PASS")
    print("workflows=18 authoritative_mutation_workflows=15 read_only_workflows=3")
    print("projection_groups=16 presentation_profiles=12 actions=30 writes=22 reads=8")
    print("reference_cases=36 cases_assigned_exactly_once=true handoffs=12 traceability_gaps=0")
    print("solvability_read_only=true contradiction_truth_adjudication=false universal_clue_count=false")
    print("permission_before_derivatives=true semantic_nonvisual=true proposal_only_ai=true")
    print("runtime_activation=false")


if __name__ == "__main__":
    main()
