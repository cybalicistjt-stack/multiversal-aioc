#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SPEC = BASE / "PPIA-03_ITEMS_EQUIPMENT_INVENTORY_EXPERIENCE_SPEC_v1.0.0.md"
ACCEPTANCE = BASE / "PPIA-03_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json"
CANDIDATE = BASE / "PPIA-03_COMPLETION_CANDIDATE.md"
TAXONOMY = BASE / "PPIA-03_ITEM_EXPERIENCE_TAXONOMY_v0.1.0.json"
INSPECTOR = BASE / "PPIA-03_ITEM_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-03_REFERENCE_CASES_v0.1.0.json"
WORKFLOWS = BASE / "PPIA-03_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
R1_ROUTING = BASE / "PPIA-03_R1_DEFERRED_ITEM_ROUTING_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-03 COMPLETION CONTRACT: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (SPEC, CANDIDATE):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    spec = SPEC.read_text(encoding="utf-8")
    candidate = CANDIDATE.read_text(encoding="utf-8")
    acceptance = load(ACCEPTANCE)
    taxonomy = load(TAXONOMY)
    inspector = load(INSPECTOR)
    cases_doc = load(CASES)
    workflows_doc = load(WORKFLOWS)
    r1 = load(R1_ROUTING)

    required_spec_phrases = [
        "13 dedicated PDFs / 218 pages",
        "nine Item-domain CSV datasets / 5,389 governed rows",
        "53 Item-classified structural candidates",
        "Unknown is not zero",
        "Laser Assault Rifle",
        "Seven energy-weapon records",
        "Energy Sniper Rifle, Plasma Carbine, and Cryo Blaster",
        "Taser conflict handling",
        "PPIA-04",
        "PPIA-05",
        "PPIA-07",
        "PPIA-08",
        "PPIA-10",
        "PPIA-11",
        "PPIA-12",
        "18 reference cases",
        "No broad offline authoritative Item mutation",
    ]
    for phrase in required_spec_phrases:
        require(phrase in spec, f"integrated spec missing {phrase!r}")

    require(len(taxonomy.get("identity_layers", [])) == 10, "taxonomy must preserve 10 identity/state layers")
    require(len(inspector.get("field_groups", [])) == 14, "Inspector must preserve 14 field groups")
    require(len(inspector.get("action_contracts", [])) == 12, "Inspector must preserve 12 action contracts")
    require(len(cases_doc.get("cases", [])) == 18, "reference corpus must contain 18 cases")
    require(len(workflows_doc.get("workflows", [])) == 12, "workflow matrix must contain 12 workflows")
    require(len(workflows_doc.get("handoff_contracts", [])) == 10, "workflow matrix must contain 10 handoffs")
    require(r1.get("source_candidate_count") == 53, "R1 routing must preserve all 53 candidates")
    require(all(group.get("canonical_item_definition") is False for group in r1.get("groups", [])), "R1 candidates must not be promoted automatically")

    require(acceptance.get("format") == "multiversal-ppia03-item-inventory-acceptance-traceability-matrix", "wrong acceptance matrix format")
    requirements = acceptance.get("requirements", [])
    require(len(requirements) == 40, f"expected 40 acceptance requirements, got {len(requirements)}")
    expected_ids = [f"PPIA03-AC-{n:03d}" for n in range(1, 41)]
    require([item.get("requirement_id") for item in requirements] == expected_ids, "acceptance IDs must be continuous 001-040")
    require(all(item.get("traces") for item in requirements), "every acceptance requirement must have upstream/file traceability")

    categories = {item.get("category") for item in requirements}
    require(len(categories) == 15, f"expected 15 acceptance categories, got {len(categories)}")
    summary = acceptance.get("summary", {})
    require(summary.get("requirements") == 40, "acceptance summary requirement count mismatch")
    require(summary.get("categories") == 15, "acceptance summary category count mismatch")
    require(summary.get("reference_cases_available") == 18, "acceptance summary reference-case count mismatch")
    for flag in ("a2_activation_authorized", "application_runtime_mutation_authorized", "release_authorized", "deployment_authorized"):
        require(summary.get(flag) is False, f"{flag} must remain false")

    valid_case_ids = {case.get("case_id") for case in cases_doc.get("cases", [])}
    referenced_case_ids: set[str] = set()
    for requirement in requirements:
        for case_id in requirement.get("reference_cases", []):
            require(case_id in valid_case_ids, f"unknown reference case {case_id} in {requirement['requirement_id']}")
            referenced_case_ids.add(case_id)
    require(referenced_case_ids == valid_case_ids, "all 18 reference cases must be covered by the acceptance matrix")

    for merge_sha in (
        "2aa3ae590dab59710e0bfaab398db19d376b6490",
        "b00aeab9f3ad4cb66869968c3584e969e132a700",
        "c2cb92857e1beb79208790b13f92d46bad769df3",
    ):
        require(merge_sha in candidate, f"completion candidate missing verified milestone merge {merge_sha}")

    required_candidate_phrases = [
        "COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES",
        "40 requirements across 15 acceptance categories",
        "PPIA-03 may become `completed_verified` only after",
        "post-merge continuity checkpoint",
        "does **not**",
    ]
    for phrase in required_candidate_phrases:
        require(phrase in candidate, f"completion candidate missing guardrail {phrase!r}")

    full = json.dumps({"acceptance": acceptance, "workflows": workflows_doc, "inspector": inspector}, ensure_ascii=False).lower()
    for phrase in (
        "source-unspecified",
        "reference-only",
        "taser",
        "hidden",
        "ownership",
        "custody",
        "idempotent",
        "expected-version",
        "lineage",
        "accessibility",
    ):
        require(phrase in full, f"completion packet missing invariant {phrase!r}")

    print("PPIA-03 COMPLETION CONTRACT: PASS")
    print("taxonomy_layers=10")
    print("inspector_field_groups=14")
    print("action_contracts=12")
    print("reference_cases=18")
    print("workflows=12")
    print("handoffs=10")
    print("acceptance_requirements=40")
    print("acceptance_categories=15")
    print("r1_candidates_accounted=53")
    print("completion_state=candidate_pending_exact_head_merge_and_post_merge_checkpoint")


if __name__ == "__main__":
    main()
