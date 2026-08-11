#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SPEC = BASE / "PPIA-05_SPECIES_FORMS_CHARACTER_BIOLOGY_EXPERIENCE_SPEC_v1.0.0.md"
ACCEPTANCE = BASE / "PPIA-05_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json"
CANDIDATE = BASE / "PPIA-05_COMPLETION_CANDIDATE.md"
INVENTORY = BASE / "PPIA-05_SOURCE_AND_DESIGN_INVENTORY.md"
TAXONOMY = BASE / "PPIA-05_SPECIES_FORMS_BIOLOGY_TAXONOMY_v0.1.0.json"
ROUTING = BASE / "PPIA-05_ABILITY_BIOLOGY_ROUTING_v0.1.0.json"
INSPECTOR = BASE / "PPIA-05_SPECIES_FORM_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-05_REFERENCE_CASES_v0.1.0.json"
WORKFLOWS = BASE / "PPIA-05_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-05 COMPLETION CONTRACT: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (SPEC, CANDIDATE, INVENTORY):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    spec = SPEC.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    inventory = INVENTORY.read_text(encoding="utf-8")
    acceptance = load(ACCEPTANCE)
    taxonomy = load(TAXONOMY)
    routing = load(ROUTING)
    inspector = load(INSPECTOR)
    cases_doc = load(CASES)
    workflows_doc = load(WORKFLOWS)

    required_spec_phrases = [
        "29 direct Species/Form/Biology PDFs / 654 pages",
        "6 supporting environment/Adaptation PDFs / 233 pages",
        "2,203 rows",
        "260 Species Perks",
        "539 Innate Abilities",
        "1,404 Elementalist rows",
        "1,018 rows",
        "296 Environment-Based Ability Collection rows",
        "60 detailed Ability rows and 57 pricing-only rows",
        "Zero automatic merges are authorized",
        "Unknown is not a human default",
        "15 integrated workflows",
        "10 cross-domain handoff contracts",
        "20 reference cases",
        "42 acceptance requirements across 14 categories",
        "No broad offline authoritative Species/Form or biology mutation",
        "STAGE-A-A2 activation authorized by this document:** No",
    ]
    for phrase in required_spec_phrases:
        require(phrase in spec, f"integrated spec missing {phrase!r}")

    authority = taxonomy.get("authority", {})
    expected_authority = {
        "species_innate_dataset_rows": 2203,
        "species_perk_rows": 260,
        "innate_ability_rows": 539,
        "elementalist_rows_in_mixed_dataset": 1404,
        "supporting_environment_dataset_rows": 1018,
        "environment_based_collection_rows": 296,
        "retained_direct_pdfs": 29,
        "retained_direct_pdf_pages": 654,
        "retained_supporting_environment_pdfs": 6,
        "retained_supporting_environment_pdf_pages": 233,
        "shapeshifter_detailed_ability_rows": 60,
        "shapeshifter_pricing_only_rows": 57,
        "shapeshifter_automatic_merges_authorized": 0,
    }
    for key, value in expected_authority.items():
        require(authority.get(key) == value, f"taxonomy authority {key} changed")
    require(authority.get("dataset_membership_implies_biology_ownership") is False, "dataset membership cannot imply biology ownership")
    require(authority.get("obsolete_semantic_database_is_content_authority") is False, "obsolete semantic database cannot regain authority")
    require(len(taxonomy.get("identity_state_layers", [])) == 13, "taxonomy must preserve 13 identity/state layers")
    require(len(taxonomy.get("presentation_profiles", [])) == 12, "taxonomy must preserve 12 presentation profiles")

    for phrase in (
        "29 PDFs / 654 pages",
        "6 supporting PDFs / 233 pages",
        "2,203 ability-domain rows",
        "1,018 rows",
        "60 detailed Shapeshifter Ability rows",
        "57 pricing-only rows",
        "0 automatic merges authorized",
    ):
        require(phrase in inventory, f"source inventory changed/missing {phrase!r}")

    require(routing.get("work_item") == "PPIA-05", "Ability/biology routing work item changed")
    routing_text = json.dumps(routing, ensure_ascii=False).lower()
    for phrase in ("2203", "species perk", "innate", "elementalist", "environment", "shapeshifter"):
        require(phrase in routing_text, f"Ability/biology routing missing {phrase!r}")

    field_groups = inspector.get("field_groups", [])
    actions = inspector.get("action_contracts", [])
    cases = cases_doc.get("cases", [])
    workflows = workflows_doc.get("workflows", [])
    handoffs = workflows_doc.get("handoff_contracts", [])
    require(len(field_groups) == 13, "Inspector must preserve 13 field groups")
    require(len(actions) == 14, "Inspector must preserve 14 action contracts")
    require(len(cases) == 20, "reference corpus must preserve 20 cases")
    require(len(workflows) == 15, "workflow matrix must preserve 15 workflows")
    require(len(handoffs) == 10, "workflow matrix must preserve 10 handoffs")
    require(len([w for w in workflows if w.get("authoritative_mutation_performed") is True]) == 10, "workflow matrix must preserve 10 authoritative mutation workflows")

    expected_case_ids = [f"PPIA05-RC-{n:03d}" for n in range(1, 21)]
    require([item.get("case_id") for item in cases] == expected_case_ids, "reference case IDs must remain continuous 001-020")
    case_summary = cases_doc.get("summary", {})
    require(case_summary.get("cases") == 20, "reference summary cases changed")
    require(case_summary.get("contract_grounded_cases") == 12, "reference summary contract-grounded count changed")
    require(case_summary.get("synthetic_qa_cases") == 5, "reference summary synthetic QA count changed")
    require(case_summary.get("guardrail_cases") == 3, "reference summary guardrail count changed")
    require(case_summary.get("canonical_synthetic_records") == 0, "synthetic reference cases cannot become canonical records")

    require(acceptance.get("format") == "multiversal-ppia05-species-forms-character-biology-acceptance-traceability-matrix", "wrong acceptance matrix format")
    requirements = acceptance.get("requirements", [])
    require(len(requirements) == 42, f"expected 42 acceptance requirements, got {len(requirements)}")
    expected_ids = [f"PPIA05-AC-{n:03d}" for n in range(1, 43)]
    require([item.get("requirement_id") for item in requirements] == expected_ids, "acceptance IDs must be continuous 001-042")
    require(all(item.get("traces") for item in requirements), "every acceptance requirement must have traceability")
    categories = {item.get("category") for item in requirements}
    require(len(categories) == 14, f"expected 14 acceptance categories, got {len(categories)}")

    actual_projection_ids = [item.get("id") for item in field_groups]
    actual_action_ids = [item.get("id") for item in actions]
    actual_workflow_ids = [item.get("workflow_id") for item in workflows]
    actual_handoff_ids = [item.get("handoff_id") for item in handoffs]
    actual_case_ids = [item.get("case_id") for item in cases]
    coverage = acceptance.get("coverage", {})
    require(coverage.get("projection_groups") == actual_projection_ids, "acceptance projection-group coverage must exactly match Inspector")
    require(coverage.get("action_contracts") == actual_action_ids, "acceptance action-contract coverage must exactly match Inspector")
    require(coverage.get("workflows") == actual_workflow_ids, "acceptance workflow coverage must exactly match workflow matrix")
    require(coverage.get("handoffs") == actual_handoff_ids, "acceptance handoff coverage must exactly match workflow matrix")
    require(coverage.get("reference_cases") == actual_case_ids, "acceptance reference-case coverage must exactly match corpus")

    valid_case_ids = set(actual_case_ids)
    referenced_case_ids: set[str] = set()
    trace_tokens: set[str] = set()
    for requirement in requirements:
        trace_tokens.update(requirement.get("traces", []))
        for case_id in requirement.get("reference_cases", []):
            require(case_id in valid_case_ids, f"unknown reference case {case_id} in {requirement['requirement_id']}")
            referenced_case_ids.add(case_id)
    require(referenced_case_ids == valid_case_ids, "all 20 reference cases must be exercised by acceptance requirements")
    for token in actual_projection_ids + actual_action_ids + actual_workflow_ids + actual_handoff_ids:
        require(
            token in trace_tokens
            or token in coverage.get("projection_groups", [])
            or token in coverage.get("action_contracts", [])
            or token in coverage.get("workflows", [])
            or token in coverage.get("handoffs", []),
            f"missing trace token {token}",
        )

    summary = acceptance.get("summary", {})
    expected_summary = {
        "requirements": 42,
        "categories": 14,
        "projection_groups_traced": 13,
        "action_contracts_traced": 14,
        "workflows_traced": 15,
        "handoffs_traced": 10,
        "reference_cases_available": 20,
        "reference_cases_covered": 20,
        "direct_pdfs_accounted": 29,
        "direct_pdf_pages_accounted": 654,
        "supporting_environment_pdfs_accounted": 6,
        "supporting_environment_pdf_pages_accounted": 233,
        "mixed_ability_rows_accounted": 2203,
        "supporting_environment_ability_rows_accounted": 1018,
        "shapeshifter_detailed_rows_accounted": 60,
        "shapeshifter_pricing_only_rows_accounted": 57,
        "shapeshifter_automatic_merges_authorized": 0,
    }
    for key, value in expected_summary.items():
        require(summary.get(key) == value, f"acceptance summary {key} mismatch")
    for flag in (
        "a2_activation_authorized",
        "application_runtime_mutation_authorized",
        "release_authorized",
        "deployment_authorized",
        "unsupported_canonical_promotion_authorized",
    ):
        require(summary.get(flag) is False, f"{flag} must remain false")

    for merge_sha in (
        "74e2a5540ddee5560407f7bf1bc8f48e6eb0443c",
        "91a84ed83ed51c33e7c6a2a045fcdb7fa08aaf24",
        "9aa72c8738070c0d94074abd3643b9145baaf163",
    ):
        require(merge_sha in candidate, f"completion candidate missing verified milestone merge {merge_sha}")

    required_candidate_phrases = [
        "COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES",
        "42 requirements across 14 acceptance categories",
        "PPIA-05 may become `completed_verified` only after",
        "post-merge continuity checkpoint",
        "does **not**",
    ]
    for phrase in required_candidate_phrases:
        require(phrase in candidate, f"completion candidate missing guardrail {phrase!r}")

    full = json.dumps(
        {"acceptance": acceptance, "workflows": workflows_doc, "inspector": inspector, "taxonomy": taxonomy},
        ensure_ascii=False,
    ).lower()
    for phrase in (
        "culture",
        "species eligibility",
        "dataset membership",
        "shapeshifter",
        "source-unspecified",
        "human default",
        "compatibility",
        "hidden",
        "expected-version",
        "operation id",
        "idempot",
        "accessibility",
        "ppia-06",
        "ppia-08",
        "ppia-11",
        "ppia-12",
    ):
        require(phrase in full, f"completion packet missing invariant {phrase!r}")

    print("PPIA-05 COMPLETION CONTRACT: PASS")
    print("taxonomy_layers=13")
    print("presentation_profiles=12")
    print("inspector_field_groups=13")
    print("action_contracts=14")
    print("reference_cases=20")
    print("workflows=15")
    print("authoritative_mutation_workflows=10")
    print("handoffs=10")
    print("acceptance_requirements=42")
    print("acceptance_categories=14")
    print("mixed_ability_rows_accounted=2203")
    print("shapeshifter_automatic_merges=0")
    print("completion_state=candidate_pending_exact_head_merge_and_post_merge_checkpoint")


if __name__ == "__main__":
    main()
