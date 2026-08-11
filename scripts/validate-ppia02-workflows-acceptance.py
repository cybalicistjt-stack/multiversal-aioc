#!/usr/bin/env python3
"""Validate PPIA-02 workflow, integrated specification, and acceptance traceability."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = PROGRAM / "PPIA-02_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
ACCEPTANCE = PROGRAM / "PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json"
SPEC = PROGRAM / "PPIA-02_CREATURE_NPC_EXPERIENCE_SPEC_v1.0.0.md"
CASES = PROGRAM / "PPIA-02_REFERENCE_CASES_v0.1.0.json"


def main() -> int:
    workflows = json.loads(WORKFLOWS.read_text(encoding="utf-8"))
    acceptance = json.loads(ACCEPTANCE.read_text(encoding="utf-8"))
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    spec = SPEC.read_text(encoding="utf-8")

    if workflows.get("format") != "multiversal-ppia02-creature-npc-workflow-authoring-contract-matrix":
        raise SystemExit("unexpected workflow matrix format")
    if workflows.get("version") != "0.1.0" or workflows.get("work_item") != "PPIA-02":
        raise SystemExit("workflow matrix identity mismatch")

    rows = workflows.get("workflows") or []
    expected_workflow_ids = [f"CN-WF-{n:03d}" for n in range(1, 11)]
    if [row.get("workflow_id") for row in rows] != expected_workflow_ids:
        raise SystemExit("workflow ID/order set changed")
    for row in rows:
        if not row.get("surface_refs") or not row.get("entry_points") or not row.get("preconditions"):
            raise SystemExit(f"workflow {row.get('workflow_id')} missing source/entry/precondition contract")
        if not row.get("steps") or not row.get("outputs") or not row.get("mutation_owner"):
            raise SystemExit(f"workflow {row.get('workflow_id')} missing execution/output/mutation contract")
        if not row.get("privacy_requirements") or not row.get("recovery_requirements") or not row.get("accessibility_requirements"):
            raise SystemExit(f"workflow {row.get('workflow_id')} missing privacy/recovery/accessibility contract")

    non_authoritative = {
        "CN-WF-001": False,
        "CN-WF-008": False,
    }
    for workflow_id, expected in non_authoritative.items():
        row = next(item for item in rows if item["workflow_id"] == workflow_id)
        if row.get("authoritative_mutation_performed") is not expected:
            raise SystemExit(f"workflow {workflow_id} changed non-authoritative boundary")

    placement = next(item for item in rows if item["workflow_id"] == "CN-WF-003")
    if "placementId != sourceStableId" not in placement.get("identity_invariants", []):
        raise SystemExit("Scene placement identity boundary disappeared")
    runtime = next(item for item in rows if item["workflow_id"] == "CN-WF-005")
    if "Definition HP" not in runtime.get("forbidden_mutations", []):
        raise SystemExit("runtime workflow can mutate Definition HP")
    summon = next(item for item in rows if item["workflow_id"] == "CN-WF-009")
    if not any("summoner != controller" in item for item in summon.get("identity_requirements", [])):
        raise SystemExit("summon role separation disappeared")
    conversion = next(item for item in rows if item["workflow_id"] == "CN-WF-010")
    if not any("source creature != playable species definition != Character instance" in item for item in conversion.get("identity_requirements", [])):
        raise SystemExit("playable conversion identity separation disappeared")

    handoffs = workflows.get("cross_workflow_handoffs") or []
    if len(handoffs) != 9:
        raise SystemExit(f"expected 9 governed cross-workflow handoffs; found {len(handoffs)}")
    if len(workflows.get("stop_conditions") or []) != 5:
        raise SystemExit("PPIA-02 stop-condition set changed")

    required_spec_sections = [
        "## 3. Core experience model",
        "## 4. Presentation profiles",
        "## 5. Universal Creature/NPC Inspector",
        "## 6. Permission-safe projection",
        "## 7. GM NPC & Creature Manager",
        "## 8. Scene placement and quick-add",
        "## 9. Encounter preparation",
        "## 10. Live runtime",
        "## 11. Named NPC versus generic creature",
        "## 12. Ecology, behavior and bestiary discovery",
        "## 13. Relationships, factions and investigation/social use",
        "## 14. Equipment, carried assets and loot",
        "## 15. Variants, templates, types, forms and transformations",
        "## 16. Summons, minions and spawned entities",
        "## 17. Playable creature conversion",
        "## 19. Responsive and accessibility contract",
        "## 20. Recovery and offline behavior",
        "## 21. Provenance and conflict behavior",
        "## 23. Implementation dependency map",
        "## 24. Completion boundary",
    ]
    for section in required_spec_sections:
        if section not in spec:
            raise SystemExit(f"integrated specification missing section {section}")

    required_spec_boundaries = [
        "does **not** authorize implementation, A2 activation",
        "Presentation Profile — information ordering/emphasis only; never a new canonical type",
        "A placement never overwrites the Definition.",
        "Balance output is advisory.",
        "No runtime HP/resource/Condition change writes back into the reusable Definition.",
        "Uncertainty can be shown without telling a Player whether hidden GM truth exists.",
        "A runtime transformation must be executed by the owning Ability/Action/Session workflow",
        "A stale reconnect cannot resurrect an expired/dismissed summon.",
        "Source creature, playable species definition, and Character instance remain separate identities.",
    ]
    for phrase in required_spec_boundaries:
        if phrase not in spec:
            raise SystemExit(f"integrated specification lost boundary: {phrase}")

    if acceptance.get("format") != "multiversal-ppia02-creature-npc-acceptance-traceability-matrix":
        raise SystemExit("unexpected acceptance matrix format")
    if acceptance.get("version") != "0.1.0" or acceptance.get("work_item") != "PPIA-02":
        raise SystemExit("acceptance matrix identity mismatch")
    reqs = acceptance.get("requirements") or []
    expected_req_ids = [f"PPIA02-REQ-{n:03d}" for n in range(1, 37)]
    if [req.get("id") for req in reqs] != expected_req_ids:
        raise SystemExit("acceptance requirement IDs/order changed")

    categories = {req.get("category") for req in reqs}
    expected_categories = {
        "identity", "presentation", "privacy", "authoring", "scene_placement", "encounter",
        "runtime", "social_investigation", "ecology_bestiary", "assets", "variants_forms",
        "summons", "playable_conversion", "accessibility", "provenance", "recovery",
    }
    if categories != expected_categories:
        raise SystemExit(f"acceptance category set changed: {sorted(categories)}")

    case_ids = {row.get("case_id") for row in cases.get("cases") or []}
    for req in reqs:
        if not req.get("requirement") or not req.get("contract_refs") or not req.get("upstream_refs"):
            raise SystemExit(f"requirement {req.get('id')} lacks traceability")
        if not req.get("case_refs") or not req.get("verification"):
            raise SystemExit(f"requirement {req.get('id')} lacks acceptance verification")
        unknown_cases = set(req["case_refs"]) - case_ids
        if unknown_cases:
            raise SystemExit(f"requirement {req['id']} references unknown cases {sorted(unknown_cases)}")

    summary = acceptance.get("summary") or {}
    if summary.get("requirements") != 36:
        raise SystemExit("acceptance summary requirement count changed")
    if summary.get("categories") != 16:
        raise SystemExit("acceptance summary category count changed")
    if summary.get("source_or_upstream_traceability_required") is not True:
        raise SystemExit("acceptance source/upstream traceability no longer required")
    if summary.get("reference_case_traceability_required") is not True:
        raise SystemExit("acceptance reference-case traceability no longer required")
    if summary.get("a2_activation_authorized") is not False or summary.get("application_runtime_mutation_authorized") is not False:
        raise SystemExit("acceptance matrix incorrectly authorizes A2/runtime mutation")

    transform_req = next(req for req in reqs if req["id"] == "PPIA02-REQ-025")
    if transform_req.get("case_refs") != ["PPIA02-RC-013"]:
        raise SystemExit("runtime transformation requirement lost dedicated case")
    privacy_req = next(req for req in reqs if req["id"] == "PPIA02-REQ-007")
    if "PPIA02-RC-009" not in privacy_req.get("case_refs", []):
        raise SystemExit("privacy-before-derived-data requirement lost hidden-placement case")

    print(json.dumps({
        "workflows": len(rows),
        "crossWorkflowHandoffs": len(handoffs),
        "requirements": len(reqs),
        "categories": len(categories),
        "referenceCases": len(case_ids),
        "a2Activated": False,
        "runtimeImplementationAuthorized": False,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
