#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = BASE / "PPIA-05_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
MATRIX = BASE / "PPIA-05_SPECIES_FORM_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-05_REFERENCE_CASES_v0.1.0.json"
TAXONOMY = BASE / "PPIA-05_SPECIES_FORMS_BIOLOGY_TAXONOMY_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-05 WORKFLOW CONTRACTS: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    doc = load(WORKFLOWS)
    matrix = load(MATRIX)
    cases_doc = load(CASES)
    taxonomy = load(TAXONOMY)

    require(doc.get("format") == "multiversal-ppia05-species-form-workflow-authoring-contract-matrix", "wrong workflow format")
    require(doc.get("inherits") == [TAXONOMY.name, MATRIX.name, CASES.name], "workflow inheritance changed")

    workflows = doc.get("workflows", [])
    expected_workflow_ids = [f"SF-WF-{n:03d}" for n in range(1, 16)]
    require(len(workflows) == 15, f"expected 15 workflows, got {len(workflows)}")
    require([w.get("workflow_id") for w in workflows] == expected_workflow_ids, "workflow IDs must be continuous SF-WF-001..015")

    required_keys = (
        "primary_personas", "entry_points", "preconditions", "steps", "outputs", "mutation_owner",
        "privacy_requirements", "recovery_requirements", "accessibility_requirements", "reference_cases",
        "forbidden_mutations", "actions", "handoffs",
    )
    for workflow in workflows:
        for key in required_keys:
            require(workflow.get(key), f"{workflow['workflow_id']} missing {key}")

    mutation_workflows = [w for w in workflows if w.get("authoritative_mutation_performed") is True]
    require(len(mutation_workflows) == 10, f"expected 10 authoritative mutation workflows, got {len(mutation_workflows)}")
    for workflow in mutation_workflows:
        joined = json.dumps(workflow, ensure_ascii=False).lower()
        require(workflow.get("revalidation_points"), f"{workflow['workflow_id']} missing revalidation points")
        require("version" in joined or "revalid" in joined, f"{workflow['workflow_id']} missing version/revalidation boundary")
        require("operation id" in joined or "idempot" in joined or "event" in joined, f"{workflow['workflow_id']} missing idempotency/event recovery boundary")

    handoffs = doc.get("handoff_contracts", [])
    expected_handoff_ids = [f"SF-HO-{n:03d}" for n in range(1, 11)]
    require(len(handoffs) == 10, f"expected 10 handoffs, got {len(handoffs)}")
    require([h.get("handoff_id") for h in handoffs] == expected_handoff_ids, "handoff IDs must be continuous SF-HO-001..010")
    for handoff in handoffs:
        require(handoff.get("receiving_owner"), f"{handoff['handoff_id']} missing receiving owner")
        require(handoff.get("payload"), f"{handoff['handoff_id']} missing payload")
        require(handoff.get("rule"), f"{handoff['handoff_id']} missing rule")

    expected_cases = [f"PPIA05-RC-{n:03d}" for n in range(1, 21)]
    require([case.get("case_id") for case in cases_doc.get("cases", [])] == expected_cases, "reference case source set changed")
    coverage = doc.get("reference_case_coverage", {})
    require(list(coverage) == expected_cases, "reference-case coverage keys changed")
    require(all(coverage[case_id] for case_id in expected_cases), "one or more reference cases lack workflow coverage")
    for workflow in workflows:
        require(set(workflow["reference_cases"]).issubset(set(expected_cases)), f"{workflow['workflow_id']} references unknown case")
        require(set(workflow["handoffs"]).issubset(set(expected_handoff_ids)), f"{workflow['workflow_id']} references unknown handoff")
    for case_id, workflow_ids in coverage.items():
        require(set(workflow_ids).issubset(set(expected_workflow_ids)), f"{case_id} coverage references unknown workflow")

    expected_actions = {
        "inspect_compare", "select_species_form", "choose_lineage_variant", "playable_conversion_handoff",
        "activate_end_form", "invoke_transformation", "acquire_swap_adaptation", "use_innate_ability",
        "validate_biology_compatibility", "apply_bioengineering_modification", "correction_respec_proposal",
        "reveal_hide_biology", "source_conflict_resolution_candidate", "history_export_recovery",
    }
    matrix_actions = {item.get("id") for item in matrix.get("action_contracts", [])}
    require(matrix_actions == expected_actions, "Inspector action contract set changed")
    workflow_actions = {action for workflow in workflows for action in workflow.get("actions", [])}
    require(workflow_actions == expected_actions, "workflow layer must route every Inspector action exactly through the known action set")

    authority = taxonomy.get("authority", {})
    require(len(taxonomy.get("identity_state_layers", [])) == 13, "taxonomy must retain 13 identity/state layers")
    require(authority.get("species_innate_dataset_rows") == 2203, "mixed Species/Innate dataset row count changed")
    require(authority.get("species_perk_rows") == 260 and authority.get("innate_ability_rows") == 539 and authority.get("elementalist_rows_in_mixed_dataset") == 1404, "mixed Ability category counts changed")
    require(authority.get("shapeshifter_detailed_ability_rows") == 60 and authority.get("shapeshifter_pricing_only_rows") == 57, "Shapeshifter counts changed")
    require(authority.get("shapeshifter_automatic_merges_authorized") == 0, "Shapeshifter automatic merge boundary changed")

    full = json.dumps(doc, ensure_ascii=False).lower()
    required_phrases = (
        "culture", "2,203-row", "260 species perks", "539 innate abilities", "1,404 elementalist",
        "60 detailed", "57 pricing-only", "zero automatic merges", "source-unspecified", "human default",
        "universal compatibility", "hidden forms", "operation id", "screen-reader", "ppia-02", "ppia-03",
        "ppia-06", "ppia-08", "ppia-11", "ppia-12", "mv-ia-f002", "mv-ia-f004",
        "mv-ia-f006/f007", "mv-ia-f020/f021", "mv-ia-f022", "stage-a-a2",
    )
    for phrase in required_phrases:
        require(phrase in full, f"missing required workflow boundary {phrase!r}")

    boundaries = " ".join(doc.get("authoring_boundaries", {}).get("not_allowed_here", [])).lower()
    for phrase in (
        "raw pdf/csv", "2,203-row", "60 detailed", "57 pricing-only", "culture", "source-unspecified",
        "ppia-03", "mv-ia-f002", "mv-ia-f004", "mv-ia-f006/f007", "mv-ia-f020/f021",
        "ppia-06", "ppia-08", "ppia-11", "ppia-12", "stage-a-a2",
    ):
        require(phrase in boundaries, f"authoring boundary missing {phrase!r}")

    invariants = doc.get("completion_invariants", [])
    require(len(invariants) == 9, "expected nine completion invariants")
    invariant_text = " ".join(invariants).lower()
    for phrase in (
        "15 ppia-05 workflows", "10 authoritative mutation workflows", "10 cross-domain handoffs",
        "20 ppia-05 reference cases", "accessible nonvisual", "2,203-row", "60 detailed", "57 pricing-only",
    ):
        require(phrase in invariant_text, f"completion invariant missing {phrase!r}")

    print("PPIA-05 WORKFLOW CONTRACTS: PASS")
    print("workflows=15")
    print("authoritative_mutation_workflows=10")
    print("handoffs=10")
    print("reference_cases_covered=20")
    print("inspector_actions_routed=14")
    print("completion_invariants=9")


if __name__ == "__main__":
    main()
