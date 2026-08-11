#!/usr/bin/env python3
"""Validate the integrated PPIA-02 workflow/spec/acceptance packet."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "governance/application-planning/parallel-preimplementation"
WORKFLOWS = PROGRAM / "PPIA-02_WORKFLOW_AUTHORING_CONTRACT_MATRIX_v0.1.0.json"
ACCEPTANCE = PROGRAM / "PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.0.json"
ACCEPTANCE_FIX = PROGRAM / "PPIA-02_ACCEPTANCE_TRACEABILITY_MATRIX_v0.1.1.json"
SPEC = PROGRAM / "PPIA-02_CREATURE_NPC_EXPERIENCE_SPEC_v1.0.0.md"
CASES = PROGRAM / "PPIA-02_REFERENCE_CASES_v0.1.0.json"
R1_ADDENDUM = PROGRAM / "PPIA-02_R1_PROVENANCE_AND_DEFERRED_CREATURE_ADDENDUM_v0.1.0.json"
R1_CANDIDATES = PROGRAM / "PPIA-02_R1_DEFERRED_CREATURE_CANDIDATES.csv"
R1_RECOVERY = PROGRAM / "PPIA-01_8E-008G-R1_RECOVERY_CLOSURE.md"
COMPLETION_CANDIDATE = PROGRAM / "PPIA-02_COMPLETION_CANDIDATE.md"


def main() -> int:
    workflows = json.loads(WORKFLOWS.read_text(encoding="utf-8"))
    acceptance = json.loads(ACCEPTANCE.read_text(encoding="utf-8"))
    correction = json.loads(ACCEPTANCE_FIX.read_text(encoding="utf-8"))
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    spec = SPEC.read_text(encoding="utf-8")
    r1_addendum = json.loads(R1_ADDENDUM.read_text(encoding="utf-8"))
    r1_recovery = R1_RECOVERY.read_text(encoding="utf-8")
    completion_candidate = COMPLETION_CANDIDATE.read_text(encoding="utf-8")

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

    if r1_addendum.get("format") != "multiversal-ppia02-r1-provenance-deferred-creature-addendum" or r1_addendum.get("version") != "0.1.0":
        raise SystemExit("unexpected PPIA-02 R1 addendum identity/version")
    if r1_addendum.get("work_item") != "PPIA-02" or r1_addendum.get("status") != "required_completion_addendum":
        raise SystemExit("PPIA-02 R1 addendum is not completion-governed")
    r1 = r1_addendum.get("canonical_r1_recovery") or {}
    expected_r1 = {
        "merge": "d271d1e7ec453cd153a7bf5768b3df837ba677a9",
        "owner_supplied_wrapper": "This.zip",
        "owner_supplied_wrapper_sha256": "daa8d2eed1d23400812c8a003fbee5c6680041227d42dc90555ebc2031715a18",
        "historical_baseline": "mv.freeze.8e008a.0.1.3",
        "result": "PASS",
        "acceptance_checks": 101,
        "acceptance_checks_passed": 101,
        "structural_candidates_accounted": 7144,
        "formerly_unbound_candidates_closed": 2766,
        "unbound_source_sections_remaining": 0,
        "authoritative_records_provenance_accounted": 158189,
        "authoritative_records_unaccounted": 0,
        "formally_deferred_candidates": 1671,
        "formal_deferral_is_public_canon_completion": False,
    }
    if r1 != expected_r1:
        raise SystemExit(f"PPIA-02 R1 recovered authority changed: {r1}")

    candidate_bytes = R1_CANDIDATES.read_bytes()
    candidate_hash = hashlib.sha256(candidate_bytes).hexdigest()
    reference = r1_addendum.get("creature_deferral_reference_set") or {}
    if candidate_hash != "dda92f7b4294e4162b633616b82256037855742bfe08fa07cc5376f5d5eb4ec0":
        raise SystemExit(f"R1 creature candidate subset hash changed: {candidate_hash}")
    if reference.get("derived_sha256") != candidate_hash or reference.get("source_register_sha256") != "39488657e712c1d834d83c1bb6e3400100252c5f2ce5a29170e6a7e63ee8d67b":
        raise SystemExit("R1 creature candidate derivation evidence changed")
    with R1_CANDIDATES.open(encoding="utf-8", newline="") as handle:
        deferred_rows = list(csv.DictReader(handle))
    if len(deferred_rows) != 93 or reference.get("rows") != 93:
        raise SystemExit("R1 creature deferral count changed")
    ids = [row["structural_candidate_id"] for row in deferred_rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("R1 creature candidate subset contains duplicate IDs")
    distribution: dict[str, int] = {}
    for row in deferred_rows:
        distribution[row["logical_source_id"]] = distribution.get(row["logical_source_id"], 0) + 1
    expected_distribution = {
        "src.logical.legacy-corpus-a-2251": 79,
        "src.logical.world-faction-compilation": 13,
        "src.logical.legacy-corpus-b-2271": 1,
    }
    if distribution != expected_distribution or reference.get("source_distribution") != expected_distribution:
        raise SystemExit(f"R1 creature source distribution changed: {distribution}")

    contract = r1_addendum.get("experience_contract") or {}
    if contract.get("content_state") != "formally_deferred_source_candidate":
        raise SystemExit("R1 formal deferral content state changed")
    for key in ("library_default", "inspector_behavior", "authoring_behavior", "scene_encounter_behavior", "privacy_behavior", "public_canon_behavior"):
        if not contract.get(key):
            raise SystemExit(f"R1 formal-deferral experience contract missing {key}")
    mapped = {item.get("requirement_id") for item in r1_addendum.get("acceptance_mapping") or []}
    if mapped != {"PPIA02-REQ-003", "PPIA02-REQ-007", "PPIA02-REQ-034", "PPIA02-REQ-035"}:
        raise SystemExit(f"R1 acceptance mapping changed: {sorted(mapped)}")
    for key, value in (r1_addendum.get("boundaries") or {}).items():
        if key.endswith("authorized") or key in {"raw_csv_modified", "r1_formal_deferral_promotes_canonical_content", "deferred_candidate_is_usable_definition"}:
            if value is not False:
                raise SystemExit(f"R1 addendum violates boundary {key}")

    for phrase in ("101 acceptance checks", "7,144 / 7,144", "1,671 candidates", "93 creature candidates"):
        if phrase not in r1_recovery:
            raise SystemExit(f"canonical R1 recovery note missing {phrase!r}")
    if "formal deferral is neither canonical promotion nor exclusion" not in json.dumps(r1_addendum).lower():
        raise SystemExit("R1 formal-deferral public-canon boundary is missing")
    if "This historical recovery request is now resolved" not in completion_candidate:
        raise SystemExit("PPIA-02 completion candidate still presents R1 recovery as owner action")
    if "f6568e77de2790e9012a95942435c8d88b2e1dd5" not in completion_candidate:
        raise SystemExit("PPIA-02 completion candidate lost original completion merge receipt")

    print(json.dumps({
        "workflows": len(rows),
        "crossWorkflowHandoffs": len(workflows.get('cross_workflow_handoffs') or []),
        "requirements": len(reqs),
        "categories": len(categories),
        "referenceCases": len(case_ids),
        "r1DeferredCreatureCandidates": len(deferred_rows),
        "r1AcceptanceChecksPassed": 101,
        "effectiveAcceptanceVersion": "0.1.1+r1-addendum-0.1.0",
        "a2Activated": False,
        "runtimeImplementationAuthorized": False,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
