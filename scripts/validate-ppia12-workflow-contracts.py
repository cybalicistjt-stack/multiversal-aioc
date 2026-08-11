#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = BASE / "PPIA-12_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
MATRIX = BASE / "PPIA-12_WORLD_SETTING_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-12_REFERENCE_CASES_v0.1.0.json"
TAXONOMY = BASE / "PPIA-12_WORLD_SETTING_TAXONOMY_v0.1.0.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-12 WORKFLOW CONTRACTS: FAIL — {message}")


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

    require(doc.get("format") == "multiversal-ppia12-world-setting-workflow-authoring-contract-matrix", "wrong workflow format")
    require(doc.get("inherits") == [TAXONOMY.name, MATRIX.name, CASES.name], "workflow inheritance changed")

    workflows = doc.get("workflows", [])
    expected_workflow_ids = [f"WS-WF-{n:03d}" for n in range(1, 17)]
    require(len(workflows) == 16, f"expected 16 workflows, got {len(workflows)}")
    require([w.get("workflow_id") for w in workflows] == expected_workflow_ids, "workflow IDs must be continuous WS-WF-001..016")

    required_keys = (
        "primary_personas", "entry_points", "preconditions", "steps", "outputs", "mutation_owner",
        "privacy_requirements", "recovery_requirements", "accessibility_requirements", "reference_cases",
        "forbidden_mutations", "actions", "handoffs",
    )
    for workflow in workflows:
        for key in required_keys:
            require(workflow.get(key), f"{workflow['workflow_id']} missing {key}")

    mutation_workflows = [w for w in workflows if w.get("authoritative_mutation_performed") is True]
    require(len(mutation_workflows) == 12, f"expected 12 authoritative mutation workflows, got {len(mutation_workflows)}")
    for workflow in mutation_workflows:
        joined = json.dumps(workflow, ensure_ascii=False).lower()
        require(workflow.get("revalidation_points"), f"{workflow['workflow_id']} missing revalidation points")
        require("version" in joined or "revalid" in joined, f"{workflow['workflow_id']} missing version/revalidation boundary")
        require("operation id" in joined or "idempot" in joined, f"{workflow['workflow_id']} missing operation/idempotency recovery boundary")

    handoffs = doc.get("handoff_contracts", [])
    expected_handoff_ids = [f"WS-HO-{n:03d}" for n in range(1, 11)]
    require(len(handoffs) == 10, f"expected 10 handoffs, got {len(handoffs)}")
    require([h.get("handoff_id") for h in handoffs] == expected_handoff_ids, "handoff IDs must be continuous WS-HO-001..010")
    for handoff in handoffs:
        require(handoff.get("receiving_owner"), f"{handoff['handoff_id']} missing receiving owner")
        require(handoff.get("payload"), f"{handoff['handoff_id']} missing payload")
        require(handoff.get("rule"), f"{handoff['handoff_id']} missing rule")

    expected_cases = [f"PPIA12-RC-{n:03d}" for n in range(1, 21)]
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
        "inspect_compare", "author_setting_definition", "author_hierarchy_relation", "attach_environment_profile",
        "author_infrastructure_landmark", "author_faction_governance", "author_culture_society_economy",
        "author_history_timeline", "scope_content_extension", "scope_local_rule_extension",
        "author_route_connectivity", "campaign_scene_handoff", "reveal_hide_setting_fact",
        "generate_authoring_proposal", "source_conflict_resolution_candidate", "history_export_recovery",
    }
    matrix_actions = {item.get("id") for item in matrix.get("action_contracts", [])}
    require(matrix_actions == expected_actions, "Inspector action contract set changed")
    workflow_actions = {action for workflow in workflows for action in workflow.get("actions", [])}
    require(workflow_actions == expected_actions, "workflow layer must route every verified Inspector action without additions")

    summary = taxonomy.get("source_summary", {})
    require(len(taxonomy.get("identity_state_layers", [])) == 14, "taxonomy must retain 14 identity/state layers")
    require(summary.get("primary_setting_cosmology_location_pdfs") == 22 and summary.get("primary_pages") == 693, "primary setting source count/pages changed")
    require(summary.get("environment_template_pdfs") == 8 and summary.get("environment_template_pages") == 238, "environment template count/pages changed")
    require(summary.get("authoring_guidance_pdfs") == 2 and summary.get("authoring_guidance_pages") == 30, "authoring source count/pages changed")
    require(summary.get("total_pdfs") == 32 and summary.get("total_pages") == 961, "total source count/pages changed")
    require(summary.get("dedicated_world_setting_csv_catalog_present") is False, "dedicated World/Setting CSV catalog boundary changed")

    full = json.dumps(doc, ensure_ascii=False).lower()
    required_phrases = (
        "co-occurrence", "environment template", "world-local", "musical reality", "branch-specific",
        "stratebrait", "unknown", "operation id", "idempotency", "screen-reader", "pathfinding",
        "ppia-08", "ppia-02", "ppia-03", "ppia-04", "ppia-05", "ppia-11",
        "mv-ia-f002", "mv-ia-f006/f007", "mv-ia-f020/f021", "mv-ia-f022",
        "32 retained pdfs / 961 pages", "stage-a-a2",
    )
    for phrase in required_phrases:
        require(phrase in full, f"missing required workflow boundary {phrase!r}")

    boundaries = " ".join(doc.get("authoring_boundaries", {}).get("not_allowed_here", [])).lower()
    for phrase in (
        "raw pdf/csv", "hierarchy", "environment template", "universalize", "ppia-02", "ppia-03",
        "ppia-04", "ppia-05", "mv-ia-f006/f007", "ppia-08", "ppia-11",
        "worldbuilding.pdf", "world creation tables.pdf", "stratebrait", "pathfind", "f020/f021",
        "f022", "stage-a-a2",
    ):
        require(phrase in boundaries, f"authoring boundary missing {phrase!r}")

    invariants = doc.get("completion_invariants", [])
    require(len(invariants) == 9, "expected nine completion invariants")
    invariant_text = " ".join(invariants).lower()
    for phrase in (
        "16 ppia-12 workflows", "12 authoritative mutation workflows", "10 cross-domain handoffs",
        "20 ppia-12 reference cases", "16 verified inspector action contracts", "14-layer",
        "32 retained pdfs / 961 pages", "permission-before-aggregation/pathfinding", "accessible nonvisual",
    ):
        require(phrase in invariant_text, f"completion invariant missing {phrase!r}")

    print("PPIA-12 WORKFLOW CONTRACTS: PASS")
    print("workflows=16")
    print("authoritative_mutation_workflows=12")
    print("handoffs=10")
    print("reference_cases_covered=20")
    print("inspector_actions_routed=16")
    print("identity_state_layers=14")
    print("source_pdfs=32")
    print("source_pages=961")
    print("completion_invariants=9")


if __name__ == "__main__":
    main()
