#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
SPEC = BASE / "PPIA-12_WORLD_SETTING_AUTHORING_EXPERIENCE_SPEC_v1.0.0.md"
ACCEPTANCE = BASE / "PPIA-12_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json"
CANDIDATE = BASE / "PPIA-12_COMPLETION_CANDIDATE.md"
INVENTORY = BASE / "PPIA-12_SOURCE_AND_DESIGN_INVENTORY.md"
TAXONOMY = BASE / "PPIA-12_WORLD_SETTING_TAXONOMY_v0.1.0.json"
ROUTING = BASE / "PPIA-12_SETTING_EXTENSION_ROUTING_v0.1.0.json"
INSPECTOR = BASE / "PPIA-12_WORLD_SETTING_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-12_REFERENCE_CASES_v0.1.0.json"
WORKFLOWS = BASE / "PPIA-12_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-12 COMPLETION CONTRACT: FAIL — {message}")


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
        "22 primary setting/cosmology/location PDFs / 693 pages",
        "8 reusable environment-template PDFs / 238 pages",
        "2 authoring-guidance PDFs / 30 pages",
        "32 retained PDFs / 961 pages total",
        "No dedicated World/Setting CSV catalog is present",
        "Unknown stays unknown",
        "World-local stays world-local",
        "14 Inspector projection groups",
        "16 governed action contracts",
        "12 action contracts are authoritative mutation paths",
        "16 integrated World/Setting workflows",
        "12 authoritative mutation workflows",
        "10 cross-domain handoff contracts",
        "20 reference cases",
        "13 contract-grounded, 4 synthetic QA and 3 guardrails",
        "48 acceptance requirements across 16 categories",
        "No broad offline authoritative World/Setting mutation is permitted",
        "STAGE-A-A2 activation authorized by this document:** No",
    ]
    for phrase in required_spec_phrases:
        require(phrase in spec, f"integrated spec missing {phrase!r}")

    summary = taxonomy.get("source_summary", {})
    expected_source = {
        "primary_setting_cosmology_location_pdfs": 22,
        "primary_pages": 693,
        "environment_template_pdfs": 8,
        "environment_template_pages": 238,
        "authoring_guidance_pdfs": 2,
        "authoring_guidance_pages": 30,
        "total_pdfs": 32,
        "total_pages": 961,
        "dedicated_world_setting_csv_catalog_present": False,
    }
    for key, value in expected_source.items():
        require(summary.get(key) == value, f"taxonomy source summary {key} changed")
    require(len(taxonomy.get("identity_state_layers", [])) == 14, "taxonomy must preserve 14 identity/state layers")
    require(len(taxonomy.get("presentation_profiles", [])) == 12, "taxonomy must preserve 12 presentation profiles")

    for phrase in (
        "22 primary setting/cosmology/location sources / 693 pages",
        "8 reusable environment-template sources / 238 pages",
        "2 supporting worldbuilding-authoring sources / 30 pages",
        "32 retained PDFs / 961 pages total",
        "No dedicated World/Setting CSV catalog is present",
        "Havalaea.PDF",
        "Vertigon.PDF",
        "Black Vegas.PDF",
        "The Antiquaria.PDF",
        "The Rakuuta Road.PDF",
        "Musical Reality Gameplay.PDF",
        "Stratebrait.PDF",
        "Worldbuilding.PDF",
        "World Creation tables.PDF",
    ):
        require(phrase in inventory, f"source inventory changed/missing {phrase!r}")

    require(routing.get("work_item_id") == "PPIA-12", "setting-extension routing work item changed")
    routing_text = json.dumps(routing, ensure_ascii=False).lower()
    for phrase in ("ppia-02", "ppia-03", "ppia-04", "ppia-05", "ppia-08", "ppia-11"):
        require(phrase in routing_text, f"setting-extension routing missing {phrase!r}")

    field_groups = inspector.get("field_groups", [])
    actions = inspector.get("action_contracts", [])
    cases = cases_doc.get("cases", [])
    workflows = workflows_doc.get("workflows", [])
    handoffs = workflows_doc.get("handoff_contracts", [])

    require(len(field_groups) == 14, "Inspector must preserve 14 field groups")
    require(len(actions) == 16, "Inspector must preserve 16 action contracts")
    require(len([a for a in actions if a.get("mutates") is True]) == 12, "Inspector must preserve 12 mutating action contracts")
    require(len(cases) == 20, "reference corpus must preserve 20 cases")
    require(len(workflows) == 16, "workflow matrix must preserve 16 workflows")
    require(len(handoffs) == 10, "workflow matrix must preserve 10 handoffs")
    require(len([w for w in workflows if w.get("authoritative_mutation_performed") is True]) == 12, "workflow matrix must preserve 12 authoritative mutation workflows")

    expected_case_ids = [f"PPIA12-RC-{n:03d}" for n in range(1, 21)]
    require([item.get("case_id") for item in cases] == expected_case_ids, "reference case IDs must remain continuous 001-020")
    kinds = {k: sum(1 for item in cases if item.get("kind") == k) for k in ("contract_grounded", "synthetic_qa", "guardrail")}
    require(kinds == {"contract_grounded": 13, "synthetic_qa": 4, "guardrail": 3}, f"reference kind counts changed: {kinds}")

    require(acceptance.get("format") == "multiversal-ppia12-world-setting-authoring-acceptance-traceability-matrix", "wrong acceptance matrix format")
    requirements = acceptance.get("requirements", [])
    require(len(requirements) == 48, f"expected 48 acceptance requirements, got {len(requirements)}")
    expected_ids = [f"PPIA12-AC-{n:03d}" for n in range(1, 49)]
    require([item.get("requirement_id") for item in requirements] == expected_ids, "acceptance IDs must be continuous 001-048")
    require(all(item.get("traces") for item in requirements), "every acceptance requirement must have traceability")
    categories = {item.get("category") for item in requirements}
    require(len(categories) == 16, f"expected 16 acceptance categories, got {len(categories)}")

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

    acc_summary = acceptance.get("summary", {})
    expected_acceptance_summary = {
        "requirements": 48,
        "categories": 16,
        "identity_state_layers_traced": 14,
        "projection_groups_traced": 14,
        "action_contracts_traced": 16,
        "workflows_traced": 16,
        "authoritative_mutation_workflows_traced": 12,
        "handoffs_traced": 10,
        "reference_cases_available": 20,
        "reference_cases_covered": 20,
        "primary_pdfs_accounted": 22,
        "primary_pdf_pages_accounted": 693,
        "environment_template_pdfs_accounted": 8,
        "environment_template_pages_accounted": 238,
        "authoring_guidance_pdfs_accounted": 2,
        "authoring_guidance_pages_accounted": 30,
        "total_pdfs_accounted": 32,
        "total_pdf_pages_accounted": 961,
        "dedicated_world_setting_csv_catalog_present": False,
    }
    for key, value in expected_acceptance_summary.items():
        require(acc_summary.get(key) == value, f"acceptance summary {key} mismatch")
    for flag in (
        "a2_activation_authorized",
        "application_runtime_mutation_authorized",
        "release_authorized",
        "deployment_authorized",
        "unsupported_canonical_promotion_authorized",
    ):
        require(acc_summary.get(flag) is False, f"{flag} must remain false")

    for merge_sha in (
        "f5feda7d8250cd20fbe59176dff9af397ac61932",
        "fc95b079dbeaeec5dbcaf468423687f0b0760499",
        "9d85d019ac6eb701846f4f8edb0eddd6adfd31ac",
    ):
        require(merge_sha in candidate, f"completion candidate missing verified milestone merge {merge_sha}")

    for phrase in (
        "COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES",
        "48 requirements across 16 acceptance categories",
        "PPIA-12 may become `completed_verified` only after",
        "post-merge continuity checkpoint",
        "does **not**",
    ):
        require(phrase in candidate, f"completion candidate missing guardrail {phrase!r}")

    full = json.dumps(
        {"acceptance": acceptance, "workflows": workflows_doc, "inspector": inspector, "taxonomy": taxonomy, "routing": routing},
        ensure_ascii=False,
    ).lower()
    for phrase in (
        "typed hierarchy",
        "co-occurrence",
        "environment template",
        "world-local",
        "campaign",
        "hidden",
        "pathfinding",
        "proposal",
        "conflict",
        "expected-version",
        "operation id",
        "idempot",
        "screen-reader",
        "ppia-08",
        "ppia-02",
        "ppia-03",
        "ppia-04",
        "ppia-05",
        "ppia-11",
    ):
        require(phrase in full, f"completion packet missing invariant {phrase!r}")

    print("PPIA-12 COMPLETION CONTRACT: PASS")
    print("taxonomy_layers=14")
    print("presentation_profiles=12")
    print("inspector_field_groups=14")
    print("action_contracts=16")
    print("mutating_action_contracts=12")
    print("reference_cases=20")
    print("contract_grounded=13")
    print("synthetic_qa=4")
    print("guardrail=3")
    print("workflows=16")
    print("authoritative_mutation_workflows=12")
    print("handoffs=10")
    print("acceptance_requirements=48")
    print("acceptance_categories=16")
    print("source_pdfs_accounted=32")
    print("source_pages_accounted=961")
    print("completion_state=candidate_pending_exact_head_merge_and_post_merge_checkpoint")


if __name__ == "__main__":
    main()
