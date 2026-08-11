#!/usr/bin/env python3
"""Validate the PPIA-02 Creature/NPC source inventory and experience taxonomy."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAM = ROOT / "governance/application-planning/parallel-preimplementation"
INVENTORY = PROGRAM / "PPIA-02_SOURCE_AND_DESIGN_INVENTORY.md"
TAXONOMY = PROGRAM / "PPIA-02_EXPERIENCE_TAXONOMY_v0.1.0.json"

SHA_RE = re.compile(r"`([0-9a-f]{64})`")


def main() -> int:
    inventory = INVENTORY.read_text(encoding="utf-8")
    taxonomy = json.loads(TAXONOMY.read_text(encoding="utf-8"))

    required_inventory = [
        "23 dedicated Creature PDFs",
        "Player Creatures.PDF",
        "Creature types.PDF",
        "Dragons(1).PDF",
        "Havalaea Creatures.PDF",
        "MV-IA-F002",
        "MV-IA-F005",
        "MV-IA-F012",
        "SD-405",
        "SD-503",
        "SD-1003",
        "SD-1004",
        "SD-1007",
        "SD-1107",
        "unsuccessful semantic-parse database",
        "does **not** contain a dedicated creature catalog",
    ]
    for phrase in required_inventory:
        if phrase not in inventory:
            raise SystemExit(f"inventory missing required boundary/surface: {phrase}")

    source_rows = [line for line in inventory.splitlines() if line.startswith("| `Creatures/") or line.startswith("| `Part 1/Creation/Player Creatures.PDF`")]
    if len(source_rows) != 24:
        raise SystemExit(f"expected 24 Creature-domain source rows; found {len(source_rows)}")
    hashes = SHA_RE.findall(inventory)
    if len(hashes) < 24 or len(set(hashes[:24])) != 24:
        raise SystemExit("Creature-domain source SHA-256 inventory is incomplete or duplicated")

    if taxonomy.get("format") != "multiversal-ppia02-creature-npc-experience-taxonomy":
        raise SystemExit("unexpected PPIA-02 taxonomy format")
    if taxonomy.get("version") != "0.1.0" or taxonomy.get("work_item") != "PPIA-02":
        raise SystemExit("PPIA-02 taxonomy identity mismatch")
    authority = taxonomy.get("authority") or {}
    if set(authority.get("repository_contracts") or []) != {"MV-IA-F002", "MV-IA-F005", "MV-IA-F012"}:
        raise SystemExit("PPIA-02 controlling feature-contract set changed")
    if authority.get("legacy_semantic_database_is_content_authority") is not False:
        raise SystemExit("obsolete semantic database was promoted into PPIA-02 content authority")

    boundaries = taxonomy.get("boundaries") or {}
    required_false = [
        "presentation_profile_creates_new_canonical_object_type",
        "definition_mutation_from_inspector",
        "campaign_placement_mutates_definition",
        "live_instance_mutates_definition",
        "automatic_variant_merge",
        "hidden_fields_delivered_then_visually_hidden",
        "unknown_source_fields_may_be_invented_as_source_fact",
        "a2_activation_authorized",
        "application_runtime_mutation_authorized",
        "release_authorized",
    ]
    for key in required_false:
        if boundaries.get(key) is not False:
            raise SystemExit(f"PPIA-02 boundary violated: {key}")

    layers = taxonomy.get("object_layers") or []
    expected_layers = {
        "definition", "presentation_profile", "variant_modifier_relationship",
        "campaign_placement", "live_instance", "playable_conversion", "source_provenance",
    }
    if {item.get("id") for item in layers} != expected_layers:
        raise SystemExit("PPIA-02 object-layer set changed")
    if any(item.get("mutable_from_ppia02") is not False for item in layers):
        raise SystemExit("PPIA-02 foundation incorrectly authorizes object-layer mutation")

    profiles = taxonomy.get("presentation_profiles") or []
    expected_profiles = {
        "creature_standard", "npc_persona", "sentient_hybrid", "swarm_group",
        "summon_minion_spawn", "stage_variant", "type_modifier", "playable_conversion",
    }
    if {item.get("id") for item in profiles} != expected_profiles:
        raise SystemExit("PPIA-02 presentation-profile set changed")

    contexts = taxonomy.get("experience_contexts") or []
    expected_contexts = {
        "library_reference", "gm_authoring", "scene_placement", "encounter_preparation",
        "live_runtime", "investigation_social", "exploration_bestiary", "comparison_variant",
        "summon_minion_spawn", "playable_conversion",
    }
    if {item.get("id") for item in contexts} != expected_contexts:
        raise SystemExit("PPIA-02 experience-context set changed")

    sections = taxonomy.get("inspector_sections") or []
    section_ids = {item.get("id") for item in sections}
    required_sections = {
        "identity_status", "encounter_summary", "traits_actions", "ecology_behavior",
        "persona_social", "assets_loot", "variants_forms", "summon_control",
        "campaign_context", "runtime_state", "source_provenance",
    }
    if not required_sections.issubset(section_ids):
        raise SystemExit(f"PPIA-02 inspector hierarchy missing sections: {sorted(required_sections-section_ids)}")

    player_denies = set(taxonomy.get("role_projection_rules", {}).get("player", {}).get("deny_before_serialization") or [])
    required_denies = {"hidden_existence", "hidden_exact_counts", "secret_motives", "gm_tactics", "unrevealed_loot", "reinforcement_timing", "private_notes"}
    if not required_denies.issubset(player_denies):
        raise SystemExit("PPIA-02 Player projection can leak hidden Creature/NPC information")

    reference_cases = taxonomy.get("reference_case_requirements") or []
    if len(reference_cases) != 10:
        raise SystemExit(f"expected 10 PPIA-02 reference-case families; found {len(reference_cases)}")

    print(json.dumps({
        "sourcePdfs": 24,
        "objectLayers": len(layers),
        "presentationProfiles": len(profiles),
        "experienceContexts": len(contexts),
        "inspectorSections": len(sections),
        "referenceCaseFamilies": len(reference_cases),
        "legacySemanticDatabaseAuthority": False,
        "a2Activated": False,
        "result": "PASS",
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
