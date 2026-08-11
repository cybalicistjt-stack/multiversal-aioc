#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
INVENTORY = BASE / "PPIA-05_SOURCE_AND_DESIGN_INVENTORY.md"
TAXONOMY = BASE / "PPIA-05_SPECIES_FORMS_BIOLOGY_TAXONOMY_v0.1.0.json"
ROUTING = BASE / "PPIA-05_ABILITY_BIOLOGY_ROUTING_v0.1.0.json"
SHAPESHIFTER_ANALYZER = ROOT / "scripts/analyze-ppia01-shapeshifter-pricing.py"
SOURCE_MAP = BASE / "PPIA-01_CSV_SOURCE_NAME_MAP.json"
SOURCE_REGISTRY = ROOT / "governance/object-system/csv-intake/CSV_SOURCE_REGISTRY.json"
ROUTING_REGISTRY = ROOT / "governance/object-system/csv-intake/CSV_DOMAIN_ROUTING_CONTRACT_REGISTRY.json"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-05 FOUNDATION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (INVENTORY, TAXONOMY, ROUTING, SHAPESHIFTER_ANALYZER, SOURCE_MAP, SOURCE_REGISTRY, ROUTING_REGISTRY):
        require(path.exists(), f"missing {path.relative_to(ROOT)}")

    inventory = INVENTORY.read_text(encoding="utf-8")
    required_inventory = [
        "29 PDFs / 654 pages",
        "6 supporting PDFs / 233 pages",
        "2,203 ability-domain rows",
        "260 Species Perks",
        "539 Innate Abilities",
        "1,404 Elementalist Abilities",
        "1,018 rows",
        "296 rows",
        "60 detailed Shapeshifter Ability rows",
        "57 pricing-only rows",
        "0 automatic merges authorized",
        "culture-versus-biology",
        "MV-IA-F004",
        "MV-IA-F002",
        "PPIA-02",
        "PPIA-03",
        "PPIA-06",
        "PPIA-08",
        "PPIA-11",
        "PPIA-12",
    ]
    for phrase in required_inventory:
        require(phrase in inventory, f"inventory missing {phrase!r}")

    direct_section = inventory.split("## 2. Retained direct Species/Form/Biology source library", 1)[1].split("## 3. Supporting environment and Adaptation source library", 1)[0]
    supporting_section = inventory.split("## 3. Supporting environment and Adaptation source library", 1)[1].split("## 4. Governed structured ability surface", 1)[0]
    direct_pdf_rows = [line for line in direct_section.splitlines() if line.startswith("| `") and ".PDF` |" in line]
    supporting_pdf_rows = [line for line in supporting_section.splitlines() if line.startswith("| `") and ".PDF` |" in line]
    require(len(direct_pdf_rows) == 29, f"expected 29 direct PDF inventory rows, got {len(direct_pdf_rows)}")
    require(len(supporting_pdf_rows) == 6, f"expected 6 supporting PDF rows, got {len(supporting_pdf_rows)}")

    taxonomy = load(TAXONOMY)
    require(taxonomy.get("format") == "multiversal-ppia05-species-forms-character-biology-experience-taxonomy", "wrong taxonomy format")
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
    for key, expected in expected_authority.items():
        require(authority.get(key) == expected, f"authority {key} expected {expected!r}, got {authority.get(key)!r}")
    require(authority.get("obsolete_semantic_database_is_content_authority") is False, "obsolete semantic DB cannot be PPIA-05 content authority")
    require(authority.get("dataset_membership_implies_biology_ownership") is False, "dataset membership cannot imply biology ownership")

    expected_layers = [
        "species-definition",
        "lineage-subspecies-variant",
        "form-definition",
        "biological-trait-ability-definition",
        "morphology-body-plan-anatomy",
        "character-biological-selection",
        "current-body-form-state",
        "transformation-adaptation-state",
        "senses-movement-physiology",
        "biology-compatibility-limits",
        "bioengineering-symbiosis-modification",
        "knowledge-visibility-projection",
        "provenance-history-recovery",
    ]
    layers = taxonomy.get("identity_state_layers", [])
    require([layer.get("id") for layer in layers] == expected_layers, "13-layer Species/Form/Biology taxonomy changed")
    require(len(taxonomy.get("presentation_profiles", [])) == 12, "expected 12 presentation profiles")

    guards = " ".join(taxonomy.get("source_guardrails", [])).lower()
    for phrase in ("culture", "species perk", "environment-based", "2,203-row", "57 shapeshifter", "same-name"):
        require(phrase in guards, f"source guardrail missing {phrase!r}")

    mutation = " ".join(taxonomy.get("mutation_invariants", [])).lower()
    for phrase in ("never rewrites the reusable definition", "temporary effects", "server-authoritative", "offline authoritative"):
        require(phrase in mutation, f"mutation invariant missing {phrase!r}")

    permissions = " ".join(taxonomy.get("permission_invariants", [])).lower()
    require("authorize before" in permissions and "hidden or unrevealed forms" in permissions, "permission-before-projection guard missing")
    accessibility = " ".join(taxonomy.get("accessibility_invariants", [])).lower()
    for phrase in ("keyboard", "screen readers", "textual equivalents", "high zoom"):
        require(phrase in accessibility, f"accessibility invariant missing {phrase!r}")

    separation = taxonomy.get("culture_biology_separation", {})
    require("culture" in separation.get("non_biology_facets", []), "culture must remain non-biology facet")
    require("temporary Effects" in separation.get("non_biology_facets", []), "temporary Effects must remain non-biology facet")

    routes = taxonomy.get("cross_domain_routes", {})
    require(routes.get("character_creation_advancement_selection_grants_calculation") == "MV-IA-F004", "F004 route missing")
    require(routes.get("creature_forms_stages_ecology_playable_conversion") == "PPIA-02", "PPIA-02 route missing")
    require(routes.get("equipment_symbiotes_cybernetics_generic_assets") == "PPIA-03", "PPIA-03 route missing")
    require(routes.get("full_visual_character_appearance_creator") == "PPIA-06", "PPIA-06 route missing")
    require(routes.get("campaign_scene_environment_authoring") == "PPIA-08", "PPIA-08 route missing")
    require(routes.get("encounter_and_balance_calibration") == "PPIA-11", "PPIA-11 route missing")
    require(routes.get("world_specific_culture_history_environment_extensions") == "PPIA-12", "PPIA-12 route missing")

    routing = load(ROUTING)
    require(routing.get("format") == "multiversal-ppia05-ability-biology-routing", "wrong routing format")
    sources = routing.get("sources", [])
    require(len(sources) == 2, "expected two governed routing source surfaces")
    species_source = next((item for item in sources if item.get("governed_dataset") == "species_elementalist_and_innate_abilities_catalog.csv"), None)
    env_source = next((item for item in sources if item.get("governed_dataset") == "prestige_environment_and_special_ability_trees_catalog.csv"), None)
    require(species_source is not None and species_source.get("rows") == 2203, "species/innate governed source missing")
    require(env_source is not None and env_source.get("rows") == 1018 and env_source.get("environment_based_collection_rows") == 296, "environment governed source missing")
    categories = {item["name"]: item for item in species_source.get("categories", [])}
    require(categories.get("Species Perks", {}).get("rows") == 260, "Species Perks count mismatch")
    require(categories.get("Innate Abilities", {}).get("rows") == 539, "Innate Abilities count mismatch")
    require(categories.get("Elementalist Abilities", {}).get("rows") == 1404, "Elementalist count mismatch")
    require(all(item.get("automatic_biology_ownership") is False for item in categories.values()), "no mixed category may auto-own biology")

    shapeshifter = routing.get("shapeshifter_reconciliation", {})
    require(shapeshifter.get("detailed_ability_rows") == 60, "Shapeshifter detailed count mismatch")
    require(shapeshifter.get("pricing_only_rows") == 57, "Shapeshifter pricing count mismatch")
    require(shapeshifter.get("automatic_merges_authorized") == 0, "Shapeshifter auto-merge must remain zero")
    branch_counts = {item["branch"]: (item["detailed"], item["pricing_only"]) for item in shapeshifter.get("branches", [])}
    require(branch_counts == {"Combat Forms": (20, 20), "Environmental Adaptations": (20, 19), "Utility Transformations": (20, 18)}, "Shapeshifter branch counts changed")

    source_map = load(SOURCE_MAP)
    require(source_map.get("datasets", {}).get("Species_Innate_Abilities.csv") == "species_elementalist_and_innate_abilities_catalog.csv", "Species retained/governed name mapping missing")
    require(source_map.get("datasets", {}).get("Prestige_Env_Abilities.csv") == "prestige_environment_and_special_ability_trees_catalog.csv", "Environment retained/governed name mapping missing")

    source_registry = load(SOURCE_REGISTRY)
    reg = {item["file"]: item for item in source_registry.get("datasets", [])}
    require(reg.get("species_elementalist_and_innate_abilities_catalog.csv", {}).get("rows") == 2203, "governed registry species row count mismatch")
    require(reg.get("prestige_environment_and_special_ability_trees_catalog.csv", {}).get("rows") == 1018, "governed registry environment row count mismatch")

    routing_registry = load(ROUTING_REGISTRY)
    contracts = {item["dataset"]: item for item in routing_registry.get("contracts", [])}
    require("species/innate ownership classification" in contracts.get("species_elementalist_and_innate_abilities_catalog.csv", {}).get("nextAction", ""), "governed species/innate ownership-classification boundary missing")
    require("environment adaptations" in contracts.get("prestige_environment_and_special_ability_trees_catalog.csv", {}).get("nextAction", ""), "governed environment-adaptation routing boundary missing")

    analyzer_text = SHAPESHIFTER_ANALYZER.read_text(encoding="utf-8")
    for phrase in ('"detailed": 20, "pricing": 20', '"detailed": 20, "pricing": 19', '"detailed": 20, "pricing": 18', 'automaticMergeAuthorized'):
        require(phrase in analyzer_text, f"existing Shapeshifter analyzer missing {phrase!r}")

    print("PPIA-05 FOUNDATION: PASS")
    print("retained_direct_pdfs=29")
    print("retained_direct_pdf_pages=654")
    print("supporting_environment_pdfs=6")
    print("supporting_environment_pdf_pages=233")
    print("species_innate_dataset_rows=2203")
    print("species_perk_rows=260")
    print("innate_ability_rows=539")
    print("elementalist_rows=1404")
    print("environment_dataset_rows=1018")
    print("environment_collection_rows=296")
    print("shapeshifter_detailed=60")
    print("shapeshifter_pricing_only=57")
    print("identity_state_layers=13")
    print("presentation_profiles=12")


if __name__ == "__main__":
    main()
