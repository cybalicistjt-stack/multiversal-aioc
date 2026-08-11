#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
MATRIX = BASE / "PPIA-05_SPECIES_FORM_INSPECTOR_PROJECTION_MATRIX_v0.1.0.json"
CASES = BASE / "PPIA-05_REFERENCE_CASES_v0.1.0.json"
TAXONOMY = BASE / "PPIA-05_SPECIES_FORMS_BIOLOGY_TAXONOMY_v0.1.0.json"
ROUTING = BASE / "PPIA-05_ABILITY_BIOLOGY_ROUTING_v0.1.0.json"
INVENTORY = BASE / "PPIA-05_SOURCE_AND_DESIGN_INVENTORY.md"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-05 INSPECTOR/REFERENCE: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (MATRIX, CASES, TAXONOMY, ROUTING, INVENTORY):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    matrix = load(MATRIX)
    cases_doc = load(CASES)
    taxonomy = load(TAXONOMY)
    routing = load(ROUTING)
    inventory = INVENTORY.read_text(encoding="utf-8")

    require(matrix.get("format") == "multiversal-ppia05-species-form-inspector-projection-matrix", "wrong matrix format")
    require(matrix.get("inherits") == TAXONOMY.name, "matrix must inherit PPIA-05 taxonomy")

    expected_groups = [
        "identity_species_definition",
        "lineage_variant",
        "form_definition",
        "biological_trait_ability",
        "morphology_body_plan",
        "character_selection",
        "current_body_form",
        "transformation_adaptation",
        "senses_movement_physiology",
        "compatibility_limits",
        "bioengineering_symbiosis",
        "knowledge_visibility",
        "provenance_recovery",
    ]
    groups = matrix.get("field_groups", [])
    require([group.get("id") for group in groups] == expected_groups, "13 field-group set/order changed")

    actions = matrix.get("action_contracts", [])
    require(len(actions) == 14, f"expected 14 action contracts, got {len(actions)}")
    action_ids = {action.get("id") for action in actions}
    expected_actions = {
        "inspect_compare",
        "select_species_form",
        "choose_lineage_variant",
        "playable_conversion_handoff",
        "activate_end_form",
        "invoke_transformation",
        "acquire_swap_adaptation",
        "use_innate_ability",
        "validate_biology_compatibility",
        "apply_bioengineering_modification",
        "correction_respec_proposal",
        "reveal_hide_biology",
        "source_conflict_resolution_candidate",
        "history_export_recovery",
    }
    require(action_ids == expected_actions, "action contract set changed")

    roles = matrix.get("role_projection", {})
    require(set(roles) == {"player", "gm", "assistant_gm", "creator_owner_admin", "service_ai"}, "role projection set changed")

    principles = " ".join(matrix.get("principles", [])).lower()
    for phrase in (
        "culture",
        "species eligibility",
        "unknown or source-unspecified",
        "2,203-row",
        "60 detailed and 57 pricing-only",
        "zero automatic merges",
        "form definition",
        "nonvisual",
    ):
        require(phrase in principles, f"matrix principle missing {phrase!r}")

    all_matrix = json.dumps(matrix, ensure_ascii=False)
    for phrase in (
        "Kola-Ha",
        "operation-ID/status lookup",
        "normal-human anatomy",
        "universal compatibility",
        "hidden forms",
        "MV-IA-F004",
        "MV-IA-F006/F007",
        "MV-IA-F020/F021",
        "MV-IA-F022",
    ):
        require(phrase in all_matrix, f"matrix invariant/source anchor missing {phrase!r}")

    accessibility = matrix.get("responsive_accessibility_matrix", {})
    require(set(accessibility) == {"expanded_large", "medium", "compact", "keyboard", "screen_reader", "high_zoom_reflow", "reduced_motion", "nonvisual_morphology"}, "responsive/accessibility contract set changed")

    require(cases_doc.get("format") == "multiversal-ppia05-species-form-reference-cases", "wrong reference case format")
    require(cases_doc.get("inherits") == TAXONOMY.name, "cases must inherit PPIA-05 taxonomy")
    policy = cases_doc.get("policy", {})
    for key in (
        "culture_is_automatic_biology",
        "species_eligibility_proves_physiology",
        "dataset_membership_proves_biology_ownership",
        "automatic_identity_or_lineage_merge",
        "shapeshifter_automatic_merge",
        "unknown_source_value_uses_human_default",
        "absence_of_incompatibility_means_universal_compatibility",
        "synthetic_qa_records_are_canonical",
    ):
        require(policy.get(key) is False, f"policy must remain false: {key}")

    cases = cases_doc.get("cases", [])
    require(len(cases) == 20, f"expected 20 reference cases, got {len(cases)}")
    require([case.get("case_id") for case in cases] == [f"PPIA05-RC-{n:03d}" for n in range(1, 21)], "case IDs must be continuous 001-020")

    kinds = Counter(case.get("kind") for case in cases)
    require(kinds == Counter({"contract_grounded": 12, "synthetic_qa": 5, "guardrail": 3}), f"reference case kind counts changed: {dict(kinds)}")

    titles = " | ".join(case.get("title", "") for case in cases).lower()
    for phrase in (
        "definition versus character",
        "culture and biology",
        "species perk",
        "mixed species elementalist innate",
        "lineage or subspecies",
        "form definition",
        "shapeshifter pricing",
        "suula adaptation",
        "environment-based learned ability",
        "kola-ha bioengineering",
        "transformation action",
        "human default",
        "universal biological compatibility",
        "hidden forms and vulnerabilities",
        "playable creature conversion",
        "temporary effects conditions equipment",
        "ambiguous network transformation",
        "accessible nonvisual",
        "source conflict and recommendation",
    ):
        require(phrase in titles, f"missing required reference case {phrase!r}")

    all_cases = json.dumps(cases_doc, ensure_ascii=False)
    for phrase in (
        "Humans vAlpha.PDF",
        "Oaran Species.PDF",
        "Species Perks(1).PDF",
        "Mythragara vAlpha2.PDF",
        "Innate Trees(3).PDF",
        "Suula.PDF",
        "Environment-Based Abilities.PDF",
        "Kola-Ha Bioengineering.PDF",
        "PPIA-02",
        "MV-IA-F004",
        "MV-IA-F020/F021",
        "MV-IA-F022",
        "operation ID/status",
    ):
        require(phrase in all_cases, f"missing case source/contract anchor {phrase!r}")

    authority = taxonomy.get("authority", {})
    require(len(taxonomy.get("identity_state_layers", [])) == 13, "taxonomy must retain 13 identity/state layers")
    require(authority.get("species_innate_dataset_rows") == 2203, "taxonomy mixed Species/Innate row count changed")
    require(authority.get("species_perk_rows") == 260, "taxonomy Species Perk count changed")
    require(authority.get("innate_ability_rows") == 539, "taxonomy Innate Ability count changed")
    require(authority.get("elementalist_rows_in_mixed_dataset") == 1404, "taxonomy Elementalist count changed")
    require(authority.get("supporting_environment_dataset_rows") == 1018, "taxonomy environment dataset count changed")
    require(authority.get("environment_based_collection_rows") == 296, "taxonomy Environment-Based collection count changed")
    require(authority.get("shapeshifter_detailed_ability_rows") == 60, "taxonomy Shapeshifter detailed count changed")
    require(authority.get("shapeshifter_pricing_only_rows") == 57, "taxonomy Shapeshifter pricing count changed")
    require(authority.get("shapeshifter_automatic_merges_authorized") == 0, "taxonomy Shapeshifter auto-merge boundary changed")

    require("29 PDFs / 654 pages" in inventory, "foundation direct PDF inventory count changed")
    require("6 supporting PDFs / 233 pages" in inventory, "foundation supporting PDF inventory count changed")
    require("2,203 ability-domain rows" in inventory, "foundation mixed Ability row count changed")
    require("0 automatic merges authorized" in inventory, "foundation Shapeshifter no-auto-merge text missing")

    sources = routing.get("sources", [])
    species_source = next((item for item in sources if item.get("governed_dataset") == "species_elementalist_and_innate_abilities_catalog.csv"), None)
    env_source = next((item for item in sources if item.get("governed_dataset") == "prestige_environment_and_special_ability_trees_catalog.csv"), None)
    require(species_source is not None and species_source.get("rows") == 2203, "routing mixed Species/Innate source changed")
    require(env_source is not None and env_source.get("rows") == 1018 and env_source.get("environment_based_collection_rows") == 296, "routing environment source changed")
    require(routing.get("shapeshifter_reconciliation", {}).get("automatic_merges_authorized") == 0, "routing Shapeshifter auto-merge boundary changed")

    summary = cases_doc.get("summary", {})
    require(summary.get("cases") == 20, "summary case count must be 20")
    require(summary.get("contract_grounded_cases") == 12, "summary contract-grounded count must be 12")
    require(summary.get("synthetic_qa_cases") == 5, "summary synthetic QA count must be 5")
    require(summary.get("guardrail_cases") == 3, "summary guardrail count must be 3")
    require(summary.get("canonical_synthetic_records") == 0, "synthetic QA cases must create zero canonical records")
    require(len(summary.get("required_coverage", [])) == 20, "required coverage must trace all 20 bounded concerns")

    print("PPIA-05 INSPECTOR/REFERENCE: PASS")
    print("field_groups=13")
    print("action_contracts=14")
    print("reference_cases=20")
    print("contract_grounded_cases=12")
    print("synthetic_qa_cases=5")
    print("guardrail_cases=3")
    print("shapeshifter_automatic_merges=0")


if __name__ == "__main__":
    main()
