import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENV_DIR = ROOT / "governance/application-planning/environment-preset-overlay"
MODEL = ENV_DIR / "ENV-04_OVERLAY_MODEL_v1.0.0.json"
LIBRARY = ENV_DIR / "ENV-13_SUPERNATURAL_MULTIVERSAL_OVERLAY_LIBRARY_v1.0.0.json"
MATRIX = ENV_DIR / "ENV-13_SUPERNATURAL_OVERLAY_INTERACTION_MATRIX_v1.0.0.csv"
GUIDE = ENV_DIR / "ENV-13_SUPERNATURAL_MULTIVERSAL_OVERLAY_GUIDE.md"
SOURCE_NOTES = ENV_DIR / "ENV-13_SUPERNATURAL_SOURCE_NOTES.md"
BACKLOG = ENV_DIR / "ENV_PROGRAM_BACKLOG.json"


class Env13SupernaturalMultiversalOverlayTests(unittest.TestCase):
    def load_json(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def load_csv(self, path):
        with path.open(encoding="utf-8", newline="") as fh:
            return list(csv.DictReader(fh))

    def test_exact_10_unique_overlay_identities(self):
        library = self.load_json(LIBRARY)
        overlays = library["overlays"]
        self.assertEqual(library["overlay_count"], 10)
        self.assertEqual(len(overlays), 10)
        ids = [o["overlay_id"] for o in overlays]
        names = [o["name"] for o in overlays]
        self.assertEqual(len(set(ids)), 10)
        self.assertEqual(len(set(names)), 10)
        self.assertEqual(set(ids), {
            "OVL-SUP-MAGICAL-SATURATION",
            "OVL-SUP-MAGICAL-DEAD-ZONE",
            "OVL-SUP-REALITY-INSTABILITY",
            "OVL-SUP-DIMENSIONAL-BLEED",
            "OVL-SUP-PORTAL-ACTIVITY",
            "OVL-SUP-PSYCHIC-INFLUENCE",
            "OVL-SUP-CORRUPTION",
            "OVL-SUP-TEMPORAL-INSTABILITY",
            "OVL-SUP-CHAOS-FOAM",
            "OVL-SUP-DREAM-INFLUENCE",
        })

    def test_every_definition_satisfies_env04_contract(self):
        model = self.load_json(MODEL)
        library = self.load_json(LIBRARY)
        contract = model["overlay_definition_contract"]
        families = {f["id"] for f in model["overlay_families"]}
        operations = set(contract["allowed_delta_operations"])
        stack_modes = set(contract["stack_modes"])
        relation_types = set(model["relation_types"])
        required = set(contract["required_fields"])
        delta_required = set(contract["delta_requirements"])
        ids = {o["overlay_id"] for o in library["overlays"]}
        for overlay in library["overlays"]:
            self.assertTrue(required.issubset(overlay), overlay["overlay_id"])
            self.assertEqual(overlay["family_id"], "OVF-SUPERNATURAL")
            self.assertIn(overlay["family_id"], families)
            self.assertTrue(overlay["target_domains"])
            self.assertTrue(overlay["applicability"])
            self.assertTrue(overlay["deltas"])
            self.assertEqual(overlay["provenance"]["classification"], "owner_authored")
            self.assertFalse(overlay["provenance"]["source_text_claimed"])
            for delta in overlay["deltas"]:
                self.assertTrue(delta_required.issubset(delta), overlay["overlay_id"])
                self.assertIn(delta["operation"], operations)
                self.assertIn(delta["stack_mode"], stack_modes)
                self.assertTrue(delta["effect_key"])
            for relation in overlay.get("relations", []):
                self.assertIn(relation["type"], relation_types)
                self.assertIn(relation["target"], ids)

    def test_interaction_matrix_never_auto_activates_another_condition(self):
        rows = self.load_csv(MATRIX)
        ids = {o["overlay_id"] for o in self.load_json(LIBRARY)["overlays"]}
        self.assertGreaterEqual(len(rows), 10)
        self.assertTrue(all(r["Automatic_Activation"] == "NO" for r in rows))
        self.assertTrue(all(r["Source_Overlay_ID"] in ids and r["Target_Overlay_ID"] in ids for r in rows))
        actual = {(r["Source_Overlay_ID"], r["Relation"], r["Target_Overlay_ID"]) for r in rows}
        for edge in {
            ("OVL-SUP-MAGICAL-SATURATION", "excludes", "OVL-SUP-MAGICAL-DEAD-ZONE"),
            ("OVL-SUP-REALITY-INSTABILITY", "amplifies", "OVL-SUP-DIMENSIONAL-BLEED"),
            ("OVL-SUP-REALITY-INSTABILITY", "amplifies", "OVL-SUP-TEMPORAL-INSTABILITY"),
            ("OVL-SUP-DIMENSIONAL-BLEED", "amplifies", "OVL-SUP-PORTAL-ACTIVITY"),
            ("OVL-SUP-DREAM-INFLUENCE", "amplifies", "OVL-SUP-PSYCHIC-INFLUENCE"),
        }:
            self.assertIn(edge, actual)

    def test_magic_regimes_are_environment_context_not_spell_rules(self):
        overlays = {o["overlay_id"]: o for o in self.load_json(LIBRARY)["overlays"]}
        sat = overlays["OVL-SUP-MAGICAL-SATURATION"]
        dead = overlays["OVL-SUP-MAGICAL-DEAD-ZONE"]
        self.assertIn("ambient_magic_regime", sat["exclusive_groups"])
        self.assertIn("ambient_magic_regime", dead["exclusive_groups"])
        self.assertIn("ambient_magic", sat["target_domains"])
        self.assertIn("ambient_magic", dead["target_domains"])
        guide = GUIDE.read_text(encoding="utf-8")
        self.assertIn("does not grant spell bonuses", guide)
        self.assertIn("does not universally disable magic", guide)

    def test_chaos_foam_is_source_backed_context_but_not_a_bundle_of_automatic_effects(self):
        overlays = {o["overlay_id"]: o for o in self.load_json(LIBRARY)["overlays"]}
        chaos = overlays["OVL-SUP-CHAOS-FOAM"]
        self.assertEqual(chaos["source_support"]["status"], "source_backed_environment_context")
        self.assertGreaterEqual(len(chaos["source_support"]["references"]), 2)
        self.assertIn("multiversal_context", chaos["target_domains"])
        notes = SOURCE_NOTES.read_text(encoding="utf-8")
        self.assertIn("Environment-Based Abilities.PDF", notes)
        self.assertIn("pages 35–36", notes)
        self.assertIn("The Chaos v2.PDF", notes)
        self.assertIn("does not promote the source-specific XP costs, die sizes, DCs, exposure thresholds, time-conversion ratio, mutation table, or perk mechanics", notes)
        guide = GUIDE.read_text(encoding="utf-8")
        for phrase in [
            "Chaos/Foam Influence does not automatically activate Reality Instability",
            "does not automatically activate Temporal Instability",
            "does not automatically activate Psychic Influence",
            "does not automatically activate Corruption",
        ]:
            self.assertIn(phrase, guide)

    def test_supernatural_conditions_do_not_invent_participant_outcomes(self):
        library = self.load_json(LIBRARY)
        rules = " ".join(library["library_rules"])
        for phrase in [
            "No universal damage", "saving throw", "mutation", "alignment", "spell bonus",
            "participant-owning systems", "ability systems", "technology systems",
        ]:
            self.assertIn(phrase, rules)
        guide = GUIDE.read_text(encoding="utf-8")
        for phrase in [
            "Reality Instability does not automatically create Dimensional Bleed",
            "Dimensional Bleed does not automatically create Portal Activity",
            "Psychic Influence does not automatically impose a mental condition",
            "Corruption does not automatically mutate, possess, align, or morally redefine a participant",
            "Dream Influence does not automatically force sleep or make imagined content real",
            "Temporal Instability does not adopt a universal time-conversion ratio",
        ]:
            self.assertIn(phrase, guide)

    def test_gehenna_branch_identity_is_not_fabricated_into_an_overlay(self):
        library = self.load_json(LIBRARY)
        names = [o["name"].lower() for o in library["overlays"]]
        ids = [o["overlay_id"].lower() for o in library["overlays"]]
        self.assertFalse(any("gehenna" in x for x in names + ids))
        notes = SOURCE_NOTES.read_text(encoding="utf-8")
        self.assertIn("No Gehenna-specific environment overlay is promoted in ENV-13", notes)
        self.assertIn("branch/access authority", notes)

    def test_env14_env15_and_cew_boundaries_remain_intact(self):
        boundary = self.load_json(LIBRARY)["authority_boundary"]
        self.assertFalse(boundary["application_implementation_authority"])
        self.assertFalse(boundary["runtime_schema_mutation_authorized"])
        self.assertFalse(boundary["automatic_event_causation_authorized"])
        self.assertEqual(boundary["ability_adaptation_reconciliation_deferred_to"], "ENV-14")
        self.assertEqual(boundary["habitat_signature_vocabulary_deferred_to"], "ENV-15")
        self.assertEqual(boundary["creature_distribution_owned_by"], "CEW")
        self.assertEqual(boundary["world_reality_branch_identity_owned_externally"], True)

    def test_candidate_preserves_library_counts_and_env13_pointer(self):
        backlog = self.load_json(BACKLOG)
        self.assertEqual(backlog["env10_decisions"]["current_preset_count"], 76)
        self.assertEqual(backlog["env10_decisions"]["current_composed_archetype_count"], 19)
        self.assertEqual(backlog["env11_decisions"]["weather_climate_disaster_overlays_added"], 22)
        self.assertEqual(backlog["env12_decisions"]["planetary_physical_overlays_added"], 15)
        self.assertEqual(backlog["env12_decisions"]["current_total_concrete_overlay_count"], 37)
        self.assertEqual(backlog["completed_through"], "ENV-12")
        self.assertEqual(backlog["current_item"], "ENV-13")
        statuses = {item["id"]: item["status"] for item in backlog["tranches"]}
        self.assertEqual(statuses["ENV-13"], "selected_not_started")
        self.assertFalse(backlog["application_implementation_authority"])


if __name__ == "__main__":
    unittest.main()
