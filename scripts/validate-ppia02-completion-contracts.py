#!/usr/bin/env python3
"""Validate the integrated PPIA-02 workflow/spec/acceptance packet."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = PROGRAM / "PPIA-02_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
ACCEPTANCE = PROGRAM / "PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json"
ACCEPTANCE_FIX = PROGRAM / "PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.1.json"
SPEC = PROGRAM / "PPIA-02_CREATURE_NPC_EXPERIENCE_SPEC_v1.0.0.md"
CASES = PROGRAM / "PPIA-02_REFERENCE_CASES_v0.1.0.json"


def main() -> int:
    workflows = json.loads(WORKFLOWS.read_text(encoding="utf-8"))
    acceptance = json.loads(ACCEPTANCE.read_text(encoding="utf-8"))
    correction = json.loads(ACCEPTANCE_FIX.read_text(encoding="utf-8"))
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
        required_keys = ("surface_refs", "entry_points", "preconditions", "steps", "outputs", "mutation_owner", "privacy_requirements", "recovery_requirements", "accessibility_requirements")
        for key in required_keys:
            if not row.get(key):
                raise SystemExit(f"workflow {row.get('workflow_id')} missing {key}")

    library = next(item for item in rows if item["workflow_id"] == "CN-WF-001")
    compare = next(item for item in rows if item["workflow_id"] == "CN-WF-008")
    if library.get("authoritative_mutation_performed") is not False or compare.get("authoritative_mutation_performed") is not False:
        raise SystemExit("reference/compare workflow became authoritative")

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

    if len(workflows.get("cross_workflow_handoffs") or []) != 9:
        raise SystemExit("governed cross-workflow handoff count changed")
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
        "Presentation Profile** — information ordering/emphasis only; never a new canonical type",
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

    if correction.get("format") != "multiversal-ppia02-creature-npc-acceptance-traceability-correction" or correction.get("version") != "0.1.1":
        raise SystemExit("acceptance correction identity mismatch")
    if correction.get("requirements_source") != ACCEPTANCE.name:
        raise SystemExit("acceptance correction no longer points to v0.1.0 requirements")
    corrections = correction.get("corrections") or []
    if corrections != [{
        "path": "summary.categories",
        "from": 15,
        "to": 16,
        "reason": "The 36 requirements span sixteen unique categories: identity, presentation, privacy, authoring, scene_placement, encounter, runtime, social_investigation, ecology_bestiary, assets, variants_forms, summons, playable_conversion, accessibility, provenance, and recovery."
    }]:
        raise SystemExit("acceptance correction changed unexpectedly")
    effective_summary = correction.get("effective_summary") or {}
    if effective_summary != {
        "requirements": 36,
        "categories": 16,
        "source_or_upstream_traceability_required": True,
        "reference_case_traceability_required": True,
        "a2_activation_authorized": False,
        "application_runtime_mutation_authorized": False,
    }:
        raise SystemExit(f"effective acceptance summary changed: {effective_summary}")

    case_ids = {row.get("case_id") for row in cases.get("cases") or []}
    if len(case_ids) != 13:
        raise SystemExit("integrated packet must contain 13 reference cases")
    for req in reqs:
        if not req.get("requirement") or not req.get("contract_refs") or not req.get("upstream_refs") or not req.get("case_refs") or not req.get("verification"):
            raise SystemExit(f"requirement {req.get('id')} lacks traceability/verification")
        unknown_cases = set(req["case_refs"]) - case_ids
        if unknown_cases:
            raise SystemExit(f"requirement {req['id']} references unknown cases {sorted(unknown_cases)}")

    transform_req = next(req for req in reqs if req["id"] == "PPIA02-REQ-025")
    if transform_req.get("case_refs") != ["PPIA02-RC-013"]:
        raise SystemExit("runtime transformation requirement lost dedicated case")
    privacy_req = next(req for req in reqs if req["id"] == "PPIA02-REQ-007")
    if "PPIA02-RC-009" not in privacy_req.get("case_refs", []):
        raise SystemExit("privacy-before-derived-data requirement lost hidden-placement case")

    print(json.dumps({
        "workflows": len(rows),
        "crossWorkflowHandoffs": len(workflows.get('cross_workflow_handoffs') or []),
        "requirements": len(reqs),
        "categories": len(categories),
        "referenceCases": len(case_ids),
        "effectiveAcceptanceVersion": "0.1.1",
        "a2Activated": False,
        "runtimeImplementationAuthorized": False,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
