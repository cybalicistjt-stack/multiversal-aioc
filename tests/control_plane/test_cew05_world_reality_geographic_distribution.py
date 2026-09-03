import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-05_WORLD_REALITY_GEOGRAPHIC_DISTRIBUTION_v1.0.0.json"
EVIDENCE = CEW / "CEW-05_DISTRIBUTION_SOURCE_EVIDENCE_v1.0.0.json"
CONTRACT = CEW / "CEW-05_WORLD_REALITY_GEOGRAPHIC_DISTRIBUTION_CONTRACT.md"
REPORT = CEW / "CEW-05_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew05WorldRealityGeographicDistributionTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_distribution_model_preserves_scope_and_open_world_semantics(self):
        model = self.load(MODEL)
        self.assertEqual(model["contract_id"], "CEW-DIST-1.0")
        self.assertEqual(model["work_item"], "CEW-05")
        self.assertEqual(model["identity_authority"], "CEW-ID-1.0")
        self.assertEqual(model["classification_authority"], "CEW-CLASS-1.0")
        self.assertEqual(model["habitat_authority"], "CEW-HAB-1.0")
        self.assertEqual(model["world_setting_authority"], "PPIA-12")
        self.assertFalse(model["application_implementation_authority"])
        self.assertTrue(model["unknown_is_first_class"])
        self.assertFalse(model["source_silence_means_absent"])
        self.assertFalse(model["habitat_fit_implies_presence"])
        self.assertFalse(model["habitat_fit_implies_native"])
        self.assertFalse(model["setting_membership_implies_native"])
        self.assertFalse(model["migration_implies_range_endpoints"])
        self.assertEqual(
            model["scope_levels"],
            ["reality_or_cosmology", "world", "setting", "region", "location_or_site"],
        )
        self.assertEqual(
            model["range_relations"],
            ["present", "native", "introduced", "domesticated", "invasive", "explicitly_absent", "unknown", "unresolved_conflict"],
        )

    def test_distribution_facts_require_typed_scope_and_provenance(self):
        model = self.load(MODEL)
        fact = model["distribution_fact_contract"]
        self.assertEqual(
            fact["required_fields"],
            ["scope_level", "scope_ref", "relation", "state", "provenance"],
        )
        self.assertEqual(
            fact["state_values"],
            ["asserted", "explicitly_absent", "unknown", "unresolved_conflict", "not_applicable"],
        )
        self.assertTrue(fact["explicit_absence_requires_source_authority"])
        self.assertTrue(fact["native_requires_explicit_or_governed_authority"])
        self.assertTrue(fact["scope_type_must_survive_projection"])
        self.assertEqual(fact["source_silence_default"], "unknown")

    def test_evidence_distinguishes_setting_membership_from_native_range(self):
        evidence = self.load(EVIDENCE)
        self.assertEqual(evidence["evidence_id"], "CEW-DIST-EVIDENCE-1.0")
        canonical = {row["subject_ref"]: row for row in evidence["canonical_setting_membership_records"]}
        expected = {
            "mv.setting.havalaea.creature.rootstalker",
            "mv.setting.havalaea.creature.hisscap-frog",
            "mv.setting.havalaea.creature.mossling-glider",
            "mv.setting.havalaea.creature.sapcrawl-varnet",
            "mv.setting.havalaea.creature.jungle-slip-beetle",
        }
        self.assertEqual(set(canonical), expected)
        for row in canonical.values():
            self.assertEqual(row["scope_level"], "setting")
            self.assertEqual(row["scope_ref"], "Havalaea")
            self.assertEqual(row["relation"], "present")
            self.assertEqual(row["state"], "asserted")
            self.assertEqual(row["native_status"], "unknown")
            self.assertFalse(row["namespace_membership_promotes_native"])
            self.assertIn("content-db/objects/mv-object-creature-definition/", row["provenance"])

    def test_setting_collection_sources_are_association_evidence_not_range_autopromotion(self):
        evidence = self.load(EVIDENCE)
        rows = {row["collection_id"]: row for row in evidence["source_collection_associations"]}
        self.assertEqual(set(rows), {"havalaea-creatures", "skoaltarran-creatures"})
        self.assertEqual(rows["havalaea-creatures"]["scope_ref"], "Havalaea")
        self.assertEqual(rows["skoaltarran-creatures"]["scope_ref"], "Skoaltarran")
        for row in rows.values():
            self.assertEqual(row["evidence_class"], "setting_collection_association")
            self.assertFalse(row["canonical_identity_binding_created"])
            self.assertFalse(row["native_range_asserted"])
            self.assertEqual(row["range_status"], "unknown")

    def test_occurrence_qualifiers_do_not_manufacture_geography(self):
        evidence = self.load(EVIDENCE)
        rows = {row["subject_label"]: row for row in evidence["temporal_occurrence_carryforward"]}
        self.assertIn("Hurricane Manta", rows)
        self.assertIn("Cave-Tusk Mammoth", rows)
        self.assertIn("Flicker Stag", rows)
        manta = rows["Hurricane Manta"]
        self.assertEqual(manta["occurrence_kind"], "migration")
        self.assertEqual(manta["range_endpoints"], "unknown")
        self.assertFalse(manta["creates_distribution"])
        stag = rows["Flicker Stag"]
        self.assertEqual(stag["occurrence_kind"], "seasonal_occurrence")
        self.assertFalse(stag["creates_distribution"])

    def test_non_inference_rules_block_common_false_range_promotions(self):
        model = self.load(MODEL)
        rules = model["non_inference_rules"]
        for key in [
            "environment_compatibility_does_not_create_presence",
            "environment_compatibility_does_not_create_native_status",
            "source_collection_membership_does_not_create_native_status",
            "canonical_setting_namespace_does_not_create_native_status",
            "migration_without_locations_does_not_create_range",
            "taxonomy_or_affinity_does_not_create_geography",
            "creature_name_does_not_create_geography",
            "mundane_or_earthlike_similarity_does_not_create_earth_range",
            "world_or_reality_hierarchy_is_not_inferred_from_name_similarity",
            "explicit_absence_overrides_ecological_fit_for_presence",
            "source_conflicts_remain_visible",
        ]:
            self.assertTrue(rules[key])

    def test_contract_states_world_local_and_distribution_boundaries(self):
        text = CONTRACT.read_text(encoding="utf-8")
        for phrase in [
            "Habitat suitability is not canonical distribution.",
            "World-local content membership is not native-range proof.",
            "A setting-scoped creature Definition may establish setting membership while native, introduced, domesticated and invasive status remain unknown.",
            "Migration or seasonality without named geographic endpoints does not create a range map.",
            "Generic creature sources remain geographically unknown unless the source or governed authority establishes scope.",
            "Explicit source-backed absence blocks environment-derived presence.",
            "CEW-05 does not infer Earth distribution from mundane or Earthlike resemblance.",
            "CEW-06 owns ecological role and encounter-use classification.",
            "no application implementation authority",
        ]:
            self.assertIn(phrase, text)

    def test_closeout_is_monotonic_and_selects_cew06(self):
        backlog = self.load(BACKLOG)
        status = {row["id"]: row["status"] for row in backlog["tranches"]}
        strict_order = backlog["strict_order"]
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-05"))
        self.assertEqual(status["CEW-05"], "completed_verified")
        if backlog["completed_through"] == "CEW-05":
            self.assertEqual(backlog["current_item"], "CEW-06")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(status["CEW-06"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-05"))
        decisions = backlog["cew05_decisions"]
        self.assertEqual(decisions["contract_id"], "CEW-DIST-1.0")
        self.assertEqual(decisions["canonical_setting_membership_record_count"], 5)
        self.assertEqual(decisions["source_collection_association_count"], 2)
        self.assertFalse(decisions["habitat_fit_implies_presence"])
        self.assertFalse(decisions["setting_membership_implies_native"])
        self.assertFalse(decisions["application_runtime_mutation_authorized"])
        self.assertIn("CEW-06", REPORT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
