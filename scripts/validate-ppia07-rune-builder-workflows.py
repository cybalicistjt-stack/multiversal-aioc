#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
MATRIX = BASE / "PPIA-07_RUNE_BUILDER_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
TRACE = BASE / "PPIA-07_RUNE_BUILDER_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json"
NOTE = BASE / "PPIA-07_RUNE_BUILDER_WORKFLOW_CANDIDATE.md"
TAXONOMY = BASE / "PPIA-07_RUNE_COMPOSITION_TAXONOMY_v0.1.0.json"
GRAMMAR = BASE / "PPIA-07_DETERMINISTIC_GRAMMAR_CANDIDATE_v0.1.0.json"
RC = BASE / "PPIA-07_RUNE_REFERENCE_CORPUS_v0.1.0.json"
COST = BASE / "PPIA-07_COST_COMPLEXITY_STABILITY_PROGRESSION_CONTRACT_v0.1.0.json"
CSP = BASE / "PPIA-07_COST_STABILITY_PROGRESSION_BENCHMARKS_v0.1.0.json"
CP = ROOT / "governance/ai/work-state/PPIA-07-attempt-001.json"
PTR = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"

EXPECTED_INPUTS = {
    "foundation_merge": "183d199d69f5cce121d4b971f33fe6c0145a6c45",
    "grammar_reference_merge": "15202626a0ba96d7675ee4ab4cbec4923158cd63",
    "cost_stability_progression_merge": "210ca8f13eaba7c1ea295c280368c68a13a300f3",
}
EXPECTED_LAYERS = [
    "rune-atom-definition","effect-domain-and-payload","connection-topology",
    "shaping-and-geometry-modifier","target-range-area-and-scope",
    "trigger-condition-and-timing","sequence-branch-and-composition",
    "execution-and-casting-context","resource-cost-capacity-and-budget",
    "stability-resonance-risk-and-failure","counterplay-resistance-and-disruption",
    "progression-knowledge-and-unlock","crafting-inscription-container-and-item-link",
    "visibility-permission-and-accessibility","provenance-conflict-version-and-recovery",
]

def fail(msg: str) -> None:
    raise SystemExit(f"PPIA-07 RUNE BUILDER WORKFLOWS: FAIL — {msg}")

def req(cond: bool, msg: str) -> None:
    if not cond:
        fail(msg)

def load(path: Path) -> dict:
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> None:
    matrix, trace = load(MATRIX), load(TRACE)
    taxonomy, grammar, rc, cost, csp = load(TAXONOMY), load(GRAMMAR), load(RC), load(COST), load(CSP)
    cp, ptr, status = load(CP), load(PTR), load(STATUS)
    note = NOTE.read_text(encoding="utf-8")

    req(matrix["format"] == "multiversal-ppia07-rune-builder-workflow-authoring-contract-matrix", "matrix format mismatch")
    req(matrix["work_item"] == "PPIA-07", "matrix work item mismatch")
    req(matrix["verified_inputs"]["foundation_merge"] == EXPECTED_INPUTS["foundation_merge"], "foundation merge mismatch")
    req(matrix["verified_inputs"]["grammar_reference_merge"] == EXPECTED_INPUTS["grammar_reference_merge"], "grammar/reference merge mismatch")
    req(matrix["verified_inputs"]["cost_stability_progression_merge"] == EXPECTED_INPUTS["cost_stability_progression_merge"], "cost/stability/progression merge mismatch")

    req(len(taxonomy["identity_state_layers"]) == 15, "taxonomy must retain 15 layers")
    req([x["id"] for x in taxonomy["identity_state_layers"]] == EXPECTED_LAYERS, "taxonomy layer IDs changed")
    req(len(grammar["atom_vocabulary"]) == 8, "grammar must retain 8 atoms")
    req(len(grammar["connection_types"]) == 4, "grammar must retain 4 connectors")
    req(len(grammar["validity_rules"]) == 12, "grammar must retain 12 validity rules")
    req(len(rc["cases"]) == 20, "reference corpus must retain 20 cases")
    req(len(csp["cases"]) == 16, "cost/stability benchmark corpus must retain 16 cases")
    req(cost["axis_separation"]["final_balance_owner"] == "PPIA-11", "PPIA-11 final balance ownership lost")
    req(cost["axis_separation"]["structural_complexity_is_power"] is False, "SCI cannot become power")
    req(cost["axis_separation"]["stability_load_is_failure_probability"] is False, "CSL cannot become failure probability")
    req(cost["resource_adapter_contract"]["source_specific_values_remain_scoped"] is True, "source-specific resource values must remain scoped")

    actions = matrix["action_contracts"]
    workflows = matrix["workflows"]
    handoffs = matrix["handoff_contracts"]
    req(len(actions) == 18, "expected 18 action contracts")
    req([x["action_id"] for x in actions] == [f"RB-ACT-{i:03d}" for i in range(1,19)], "action IDs must be contiguous RB-ACT-001..018")
    mut_actions = [x for x in actions if x["authoritative_mutation_performed"]]
    req(len(mut_actions) == 7, "expected 7 PPIA-07 mutation actions")
    for action in mut_actions:
        protocol = " ".join(action["mutation_protocol"])
        req("expected_version" in protocol and "operation_id" in protocol and "status/current-version" in protocol,
            f"mutation protocol incomplete for {action['action_id']}")

    req(len(workflows) == 16, "expected 16 workflows")
    req([x["workflow_id"] for x in workflows] == [f"RB-WF-{i:03d}" for i in range(1,17)], "workflow IDs must be contiguous RB-WF-001..016")
    wf_ids = {x["workflow_id"] for x in workflows}
    action_ids = {x["action_id"] for x in actions}
    req(len(handoffs) == 10, "expected 10 handoff contracts")
    req([x["id"] for x in handoffs] == [f"RB-HO-{i:03d}" for i in range(1,11)], "handoff IDs must be contiguous RB-HO-001..010")
    handoff_ids = {x["id"] for x in handoffs}

    for wf in workflows:
        req(set(wf["actions"]) <= action_ids, f"unknown action in {wf['workflow_id']}")
        req(set(wf["handoffs"]) <= handoff_ids, f"unknown handoff in {wf['workflow_id']}")
        req(set(wf["taxonomy_layers"]) <= set(EXPECTED_LAYERS), f"unknown taxonomy layer in {wf['workflow_id']}")
        req(all(x.startswith("PPIA07-RC-") for x in wf["reference_cases"]), f"bad RC ID in {wf['workflow_id']}")
        req(all(x.startswith("PPIA07-CSP-") for x in wf["cost_stability_benchmarks"]), f"bad CSP ID in {wf['workflow_id']}")
        req(wf["accessibility_requirements"], f"accessibility missing in {wf['workflow_id']}")
        req(wf["privacy_requirements"], f"privacy missing in {wf['workflow_id']}")
        if wf["authoritative_ppia07_mutation"]:
            text = " ".join(wf["recovery_requirements"])
            req("expected_version" in text and "operation_id" in text and "status lookup" in text, f"mutation recovery missing in {wf['workflow_id']}")

    req(trace["format"] == "multiversal-ppia07-rune-builder-workflow-traceability-matrix", "trace format mismatch")
    counts = trace["required_coverage_counts"]
    req(counts == {"taxonomy_layers":15,"reference_cases":20,"cost_stability_benchmarks":16,"action_contracts":18,"handoff_contracts":10,"workflows":16}, "trace count contract mismatch")
    expected_ids = {
        "taxonomy_layers": EXPECTED_LAYERS,
        "reference_cases": [f"PPIA07-RC-{i:03d}" for i in range(1,21)],
        "cost_stability_benchmarks": [f"PPIA07-CSP-{i:03d}" for i in range(1,17)],
        "action_contracts": [f"RB-ACT-{i:03d}" for i in range(1,19)],
        "handoff_contracts": [f"RB-HO-{i:03d}" for i in range(1,11)],
    }
    for group, ids in expected_ids.items():
        rows = trace["coverage"][group]
        req([x["id"] for x in rows] == ids, f"{group} IDs mismatch")
        for row in rows:
            req(row["workflows"], f"coverage gap for {row['id']}")
            req(set(row["workflows"]) <= wf_ids, f"unknown workflow in trace for {row['id']}")

    req(all(v is False for v in trace["policy"].values()), "trace policy guardrails must remain false")

    handoff_text = json.dumps(handoffs)
    for token in ("PPIA-03","PPIA-08","PPIA-11","PPIA-12","F020","F021","F022","SD-707"):
        req(token in handoff_text, f"missing handoff ownership token {token}")
    invariant_text = "\n".join(matrix["global_invariants"])
    for token in ("expected-version","operation-ID","PPIA-11","PPIA-03","PPIA-08","PPIA-12","canonical ordered linear","AI/generated constructions"):
        req(token in invariant_text, f"global invariant missing {token}")

    for phrase in ("16 workflows","18 governed actions","7","10 explicit handoffs","all 20","all 16","SCI is not power","CSL is not failure probability","PPIA-11","canonical ordered linear"):
        req(phrase.lower() in note.lower(), f"candidate note missing {phrase!r}")

    req(cp["work_item_id"] == "PPIA-07" and cp["attempt_id"] == "PPIA-07-attempt-001", "checkpoint identity mismatch")
    req(not cp["unresolved_failures"] and cp["owner_decision_required"] is False, "checkpoint unresolved state")
    if cp["status"] in {"started","in_progress"}:
        selected = [x for x in ptr["active_attempts"] if x.get("owner_selected")]
        req(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-07", "active PPIA-07 must remain owner-selected")
        req(ptr["primary_attempt_id"] == "PPIA-07-attempt-001", "primary attempt mismatch")
        req(status["primary"]["work_item_id"] == "PPIA-07", "compact status work item mismatch")
    else:
        req(cp["status"] == "completed_verified", "unexpected historical PPIA-07 status")

    print("PPIA-07 RUNE BUILDER WORKFLOWS: PASS")
    print("workflows=16")
    print("actions=18")
    print("mutation_actions=7")
    print("handoffs=10")
    print("taxonomy_layers=15")
    print("reference_cases=20")
    print("cost_stability_benchmarks=16")
    print("traceability_gaps=0")
    print("final_balance_owner=PPIA-11")

if __name__ == "__main__":
    main()
