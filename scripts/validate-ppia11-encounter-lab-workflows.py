#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "governance/application-planning/parallel-preimplementation"


def load(name):
    return json.loads((P / name).read_text(encoding="utf-8"))


def req(value, message):
    if not value:
        raise AssertionError(message)


def union(rows, key):
    out = set()
    for row in rows:
        out.update(row.get(key, []))
    return out


def main():
    wf = load("PPIA-11_ENCOUNTER_LAB_WORKFLOW_CONTRACT_MATRIX_v0.1.0.json")
    tr = load("PPIA-11_ENCOUNTER_LAB_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json")
    inspector = load("PPIA-11_ENCOUNTER_LAB_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json")
    refs = load("PPIA-11_ENCOUNTER_LAB_REFERENCE_CASES_v0.1.0.json")
    method = load("PPIA-11_ENCOUNTER_METHODOLOGY_CONTRACT_v0.1.0.json")
    taxonomy = load("PPIA-11_ENCOUNTER_BALANCE_TAXONOMY_v0.1.0.json")
    authority = load("PPIA-11_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json")
    candidate = (P / "PPIA-11_ENCOUNTER_LAB_WORKFLOW_TRACEABILITY_CANDIDATE.md").read_text(encoding="utf-8").lower()

    req(wf["work_item"] == "PPIA-11" and tr["work_item"] == "PPIA-11", "wrong work item")
    workflows = wf["workflows"]
    req(len(workflows) == 14, "expected 14 workflows")
    req(len({x["id"] for x in workflows}) == 14, "workflow IDs must be unique")
    req(sum(1 for x in workflows if x["mutation"]) == 5, "expected five mutation workflows")
    req(sum(1 for x in workflows if not x["mutation"]) == 9, "expected nine read/analysis workflows")

    expected_groups = {f"P11-PG-{i:03d}" for i in range(1, 17)}
    expected_actions = {f"P11-ACT-{i:03d}" for i in range(1, 25)}
    expected_cases = {f"PPIA11-IR-{i:03d}" for i in range(1, 43)}
    expected_factors = {f"P11-F-{i:03d}" for i in range(1, 21)}
    expected_methods = {f"P11-M-{i:03d}" for i in range(1, 14)}
    expected_handoffs = {f"P11-HO-{i:03d}" for i in range(1, 11)}
    expected_pressures = set(method["inherited_authority"]["pressure_dimensions"])
    expected_uncertainty = {x["id"] for x in taxonomy["uncertainty_bands"]}

    req({x["id"] for x in inspector["projection_groups"]} == expected_groups, "Inspector projection IDs changed")
    req({x["id"] for x in inspector["actions"]} == expected_actions, "Inspector action IDs changed")
    req({x["id"] for x in taxonomy["factor_families"]} == expected_factors, "factor IDs changed")
    req({x["id"] for x in method["assessment_steps"]} == expected_methods, "method step IDs changed")
    req({x["id"] for x in authority["domain_handoffs"]} == expected_handoffs, "handoff IDs changed")
    req(expected_uncertainty == {"low", "moderate", "high", "indeterminate"}, "uncertainty bands changed")

    req(union(workflows, "groups") == expected_groups, "workflow projection coverage incomplete")
    req(union(workflows, "actions") == expected_actions, "workflow action coverage incomplete")
    req(union(workflows, "factor_ids") == expected_factors, "workflow factor coverage incomplete")
    req(union(workflows, "pressure_dimensions") == expected_pressures, "workflow pressure coverage incomplete")
    req(union(workflows, "uncertainty_bands") == expected_uncertainty, "workflow uncertainty coverage incomplete")
    req(union(workflows, "method_steps") == expected_methods, "workflow methodology-step coverage incomplete")
    req(union(workflows, "handoffs") == expected_handoffs, "workflow handoff coverage incomplete")

    all_cases = [case for row in workflows for case in row["case_ids"]]
    req(len(all_cases) == 42, "expected 42 workflow case assignments")
    req(set(all_cases) == expected_cases, "workflow reference-case coverage incomplete")
    req(len(set(all_cases)) == 42, "reference cases must be assigned exactly once")
    req(refs["resolved_case_count"] == 42 and refs["imported_case_count"] == 18 and refs["local_case_count"] == 24, "reference corpus counts changed")

    trace_rows = tr["rows"]
    req(len(trace_rows) == 14, "traceability row count mismatch")
    req({x["id"] for x in trace_rows} == {x["id"] for x in workflows}, "traceability workflow IDs mismatch")
    trace_cases = [case for row in trace_rows for case in row["cases"]]
    req(len(trace_cases) == 42 and set(trace_cases) == expected_cases and len(set(trace_cases)) == 42, "traceability must assign all 42 cases exactly once")
    by_id = {x["id"]: x for x in workflows}
    for row in trace_rows:
        req(row["cases"] == by_id[row["id"]]["case_ids"], f"traceability case mapping differs for {row['id']}")
        req(row["mutation"] == by_id[row["id"]]["mutation"], f"traceability mutation flag differs for {row['id']}")

    for row in workflows:
        if row["mutation"]:
            req(row.get("protocol") == "P11-MUT-001", f"{row['id']} missing P11-MUT-001")
    mut = inspector["mutation_protocols"]["P11-MUT-001"]
    req(set(mut["required"]) == {"authorization", "expected_version", "operation_id"}, "P11-MUT-001 requirements changed")
    req(mut["ambiguous_result"] == ["query_operation_status", "query_current_version", "retry_only_if_safe"], "ambiguous-result recovery changed")
    req(mut["offline_authoritative_mutation"] is False and mut["source_truth_mutation"] is False, "mutation authority boundary weakened")

    policy = wf["workflow_policy"]
    for key in ["universal_scalar", "weighted_pressure_collapse", "source_defaulting", "automatic_balance_rewrite", "automatic_benchmark_canonical_promotion", "ai_irreversible_authority", "guaranteed_balance_claim", "runtime_activation"]:
        req(policy[key] is False, f"workflow policy weakened: {key}")
    for key in ["permission_filter_before_reference_resolution", "permission_filter_before_derivatives", "mutation_requires_P11_MUT_001", "expected_version_required_for_write", "operation_id_required_for_write", "ambiguous_result_recovery_before_retry", "semantic_nonvisual_parity_required", "benchmark_and_simulation_are_evidence_not_source_truth", "historical_receipts_immutable"]:
        req(policy[key] is True, f"required workflow policy missing: {key}")

    for phrase in [
        "14 end-to-end workflows",
        "42 / 42",
        "20 / 20",
        "12 / 12",
        "4 / 4",
        "13 / 13",
        "10 / 10",
        "no universal cr",
        "p11-mut-001",
        "indeterminate_blocked",
        "ai cannot approve",
        "ppia-11 remains `started`",
        "no application runtime"
    ]:
        req(phrase in candidate, f"candidate narrative missing {phrase}")

    checkpoint = json.loads((ROOT / "governance/ai/work-state/PPIA-11-attempt-001.json").read_text(encoding="utf-8"))
    pointer = json.loads((ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json").read_text(encoding="utf-8"))
    compact = json.loads((ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json").read_text(encoding="utf-8"))
    req(checkpoint["work_item_id"] == "PPIA-11" and checkpoint["status"] in {"started", "completed_verified"}, "PPIA-11 checkpoint state invalid")
    req(pointer["primary_attempt_id"] == "PPIA-11-attempt-001", "pointer no longer selects PPIA-11")
    req(compact["primary"]["work_item_id"] == "PPIA-11", "compact status no longer selects PPIA-11")
    active = (checkpoint.get("active_substep") or "").lower()
    evidence_text = " ".join(str(x.get("value", "")) for x in checkpoint.get("evidence", [])).lower()
    candidate_mode = "workflow" in active and "traceability" in active
    historical_mode = "workflow / traceability squash merge" in evidence_text or "workflow/traceability squash merge" in evidence_text
    req(candidate_mode or historical_mode or checkpoint["status"] == "completed_verified", "checkpoint lacks active or historical workflow milestone evidence")

    req(checkpoint["owner_decision_required"] is False, "unexpected owner decision gate")
    req(checkpoint["unresolved_failures"] == [], "checkpoint has unresolved failures")

    print("PPIA-11 Encounter Lab workflow/traceability validation: PASS")
    print("workflows=14 mutation=5 read_analysis=9")
    print("coverage=16 projections / 24 actions / 42 cases exactly once / 20 factors / 12 pressures / 4 uncertainty bands / 13 method steps / 10 handoffs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
