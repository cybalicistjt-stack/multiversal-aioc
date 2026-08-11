#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SPEC = BASE / "PPIA-04_VEHICLE_MECHA_STARSHIP_EXPERIENCE_SPEC_v1.0.0.md"
ACCEPTANCE = BASE / "PPIA-04_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json"
CANDIDATE = BASE / "PPIA-04_COMPLETION_CANDIDATE.md"
TAXONOMY = BASE / "PPIA-04_VEHICLE_EXPERIENCE_TAXONOMY_v0.1.0.json"
INSPECTOR = BASE / "PPIA-04_VEHICLE_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-04_REFERENCE_CASES_v0.1.0.json"
WORKFLOWS = BASE / "PPIA-04_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
R1 = BASE / "PPIA-04_R1_DEFERRED_VEHICLE_SYSTEM_CANDIDATES.csv"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-04 COMPLETION CONTRACT: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (SPEC, CANDIDATE, R1):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    spec = SPEC.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    acceptance = load(ACCEPTANCE)
    taxonomy = load(TAXONOMY)
    inspector = load(INSPECTOR)
    cases_doc = load(CASES)
    workflows_doc = load(WORKFLOWS)

    required_spec_phrases = [
        "24 retained Vehicle/Mecha/Spacecraft/Operations PDFs / 608 pages",
        "three governed Vehicle-domain CSV datasets / 5,628 rows",
        "10 recovered R1 vehicle/system structural candidates",
        "Unknown is not zero",
        "name similarity cannot create",
        "15 integrated workflows",
        "10 cross-domain handoff contracts",
        "20 reference cases",
        "No broad offline authoritative vehicle mutation",
        "continuous Newtonian flight",
        "full orbital mechanics",
        "autonomous drones",
        "programmable vehicle AI",
        "full synchronized interior/exterior geometry",
        "STAGE-A-A2 activation authorized by this document:** No",
    ]
    for phrase in required_spec_phrases:
        require(phrase in spec, f"integrated spec missing {phrase!r}")

    require(taxonomy.get("authority", {}).get("vehicle_csv_datasets") == 3, "taxonomy Vehicle CSV dataset count changed")
    require(taxonomy.get("authority", {}).get("vehicle_csv_rows") == 5628, "taxonomy Vehicle CSV row count changed")
    require(taxonomy.get("authority", {}).get("retained_direct_pdfs") == 24, "taxonomy retained PDF count changed")
    require(taxonomy.get("authority", {}).get("retained_direct_pdf_pages") == 608, "taxonomy retained PDF page count changed")
    require(taxonomy.get("authority", {}).get("recovered_r1_vehicle_system_candidates") == 10, "taxonomy R1 candidate count changed")
    require(taxonomy.get("authority", {}).get("r1_structural_candidates_are_canonical_vehicle_or_system_definitions") is False, "R1 candidates cannot become canonical automatically")
    require(len(taxonomy.get("identity_state_layers", [])) == 14, "taxonomy must preserve 14 identity/state layers")

    field_groups = inspector.get("field_groups", [])
    actions = inspector.get("action_contracts", [])
    cases = cases_doc.get("cases", [])
    workflows = workflows_doc.get("workflows", [])
    handoffs = workflows_doc.get("handoff_contracts", [])
    require(len(field_groups) == 14, "Inspector must preserve 14 field groups")
    require(len(actions) == 14, "Inspector must preserve 14 action contracts")
    require(len(cases) == 20, "reference corpus must preserve 20 cases")
    require(len(workflows) == 15, "workflow matrix must preserve 15 workflows")
    require(len(handoffs) == 10, "workflow matrix must preserve 10 handoffs")

    with R1.open("r", encoding="utf-8-sig", newline="") as handle:
        r1_rows = list(csv.DictReader(handle))
    require(len(r1_rows) == 10, f"expected 10 recovered R1 candidate rows, got {len(r1_rows)}")

    require(acceptance.get("format") == "multiversal-ppia04-vehicle-mecha-starship-acceptance-traceability-matrix", "wrong acceptance matrix format")
    requirements = acceptance.get("requirements", [])
    require(len(requirements) == 42, f"expected 42 acceptance requirements, got {len(requirements)}")
    expected_ids = [f"PPIA04-AC-{n:03d}" for n in range(1, 43)]
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
        require(token in trace_tokens or token in coverage.get("projection_groups", []) or token in coverage.get("action_contracts", []) or token in coverage.get("workflows", []) or token in coverage.get("handoffs", []), f"missing trace token {token}")

    summary = acceptance.get("summary", {})
    expected_summary = {
        "requirements": 42,
        "categories": 14,
        "projection_groups_traced": 14,
        "action_contracts_traced": 14,
        "workflows_traced": 15,
        "handoffs_traced": 10,
        "reference_cases_available": 20,
        "reference_cases_covered": 20,
        "r1_candidates_accounted": 10,
    }
    for key, value in expected_summary.items():
        require(summary.get(key) == value, f"acceptance summary {key} mismatch")
    for flag in ("a2_activation_authorized", "application_runtime_mutation_authorized", "release_authorized", "deployment_authorized", "deferred_simulation_activation_authorized"):
        require(summary.get(flag) is False, f"{flag} must remain false")

    for merge_sha in (
        "8afc51555dbb46d68536fb95adcb6b2cc0a9c4e8",
        "67017018b8a50694dd041230bc1b6f66395903d8",
        "4768a5ac6854f9b5f82a2bc81ae807f99d23f576",
    ):
        require(merge_sha in candidate, f"completion candidate missing verified milestone merge {merge_sha}")

    required_candidate_phrases = [
        "COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES",
        "42 requirements across 14 acceptance categories",
        "PPIA-04 may become `completed_verified` only after",
        "post-merge continuity checkpoint",
        "does **not**",
    ]
    for phrase in required_candidate_phrases:
        require(phrase in candidate, f"completion candidate missing guardrail {phrase!r}")

    full = json.dumps({"acceptance": acceptance, "workflows": workflows_doc, "inspector": inspector}, ensure_ascii=False).lower()
    for phrase in (
        "source-unspecified",
        "hidden",
        "ownership",
        "custody",
        "station",
        "semantic",
        "idempot",
        "expected-version",
        "operation id",
        "accessibility",
        "deferred",
    ):
        require(phrase in full, f"completion packet missing invariant {phrase!r}")

    print("PPIA-04 COMPLETION CONTRACT: PASS")
    print("taxonomy_layers=14")
    print("inspector_field_groups=14")
    print("action_contracts=14")
    print("reference_cases=20")
    print("workflows=15")
    print("handoffs=10")
    print("acceptance_requirements=42")
    print("acceptance_categories=14")
    print("r1_candidates_accounted=10")
    print("completion_state=candidate_pending_exact_head_merge_and_post_merge_checkpoint")


if __name__ == "__main__":
    main()
