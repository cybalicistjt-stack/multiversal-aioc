import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEW = ROOT / "governance/application-planning/creature-ecology-wildlife"
MODEL = CEW / "CEW-02_CREATURE_TYPE_RECOVERY_v1.0.0.json"
AUDIT = CEW / "CEW-02_TAXONOMY_AUDIT.md"
REPORT = CEW / "CEW-02_COMPLETION_REPORT.md"
BACKLOG = CEW / "CEW_PROGRAM_BACKLOG.json"


class Cew02CreatureTypeTaxonomyAuditTests(unittest.TestCase):
    def load(self, path):
        return json.loads(path.read_text(encoding="utf-8"))

    def test_contract_identity_scope_and_boundary(self):
        model = self.load(MODEL)
        self.assertEqual(model["audit_id"], "CEW-TAX-1.0")
        self.assertEqual(model["work_item"], "CEW-02")
        self.assertEqual(model["audit_scope"]["dedicated_creature_pdf_count"], 23)
        self.assertEqual(model["audit_scope"]["creation_conversion_sources"], ["Player Creatures.PDF"])
        self.assertFalse(model["audit_scope"]["source_only_identity_binding_performed"])
        self.assertFalse(model["application_runtime_mutation_authorized"])
        self.assertFalse(model["authority"]["canonical_promotion_authorized"])

    def test_all_23_creature_sources_have_taxonomy_roles(self):
        model = self.load(MODEL)
        rows = model["source_family_audit"]
        self.assertEqual(len(rows), 23)
        names = {r["source_document"] for r in rows}
        self.assertEqual(len(names), 23)
        self.assertIn("Creature types.PDF", names)
        self.assertIn("Plant Creatures.PDF", names)
        self.assertIn("Incorporeal Creatures.PDF", names)
        self.assertIn("Vampirism&Lycanthropy.PDF", names)

    def test_recovered_base_types_do_not_flatten_cross_axes(self):
        model = self.load(MODEL)
        findings = {r["term"]: r["status"] for r in model["base_type_findings"]}
        required = {"Aberration","Chaos","Construct","Demonic","Digital","Divine","Dragon","Elemental","Fell","Fey","Toon","Undead","Beast"}
        self.assertTrue(required.issubset(findings))
        self.assertEqual(findings["Illusion"], "orphan_type_usage_unresolved")
        forbidden = {"Plant","Incorporeal","Fire","Cold","Shadow","Mechanical","Zombie","Ghost","Vampire","Lycanthrope"}
        self.assertTrue(forbidden.isdisjoint(findings))

    def test_creature_types_pdf_is_modifier_source_with_only_explicit_type_changes(self):
        source = self.load(MODEL)["cross_axis_recovery"]["Creature types.PDF"]
        rows = {r["term"]: r for r in source["terms"]}
        self.assertEqual(len(rows), 6)
        self.assertIsNone(rows["Fire-Type Animal"]["base_type_change"])
        self.assertIsNone(rows["Cold-Type Animal"]["base_type_change"])
        self.assertIsNone(rows["Shadow-Type Animal"]["base_type_change"])
        self.assertEqual(rows["Undead-Type Animal"]["base_type_change"], "Undead")
        self.assertIsNone(rows["Chaos-Type Animal"]["base_type_change"])
        self.assertEqual(rows["Mechanical-Type Animal"]["base_type_change"], "Construct")
        self.assertIn("Follow The White Rabbit scenario", source["non_taxonomy_material"])

    def test_body_manifestation_and_template_systems_remain_separate(self):
        cross = self.load(MODEL)["cross_axis_recovery"]
        self.assertEqual(cross["Incorporeal Creatures.PDF"]["role"], "body_plan_or_manifestation")
        self.assertIn("not a single category", cross["Incorporeal Creatures.PDF"]["explicit_rule"])
        self.assertEqual(cross["Plant Creatures.PDF"]["movement_axis"], ["Immobile","Creeping","Spreading","Mobile"])
        self.assertEqual(cross["Zombies 11-16-24.PDF"]["system"], "Zombie Conversion Template System")
        self.assertEqual(cross["Ghosts 11-16-24.PDF"]["system"], "Ghost & Spirit Template System")
        self.assertEqual(cross["Vampirism&Lycanthropy.PDF"]["role"], "template_or_modifier")

    def test_source_disagreements_are_preserved_not_resolved_by_flattening(self):
        model = self.load(MODEL)
        conflicts = {r["id"]: r for r in model["overloaded_and_conflicting_usage"]}
        self.assertEqual(len(conflicts), 10)
        self.assertEqual(conflicts["CEW02-CONFLICT-005"]["resolution"], "owner_resolution_required_no_flattening")
        self.assertEqual(conflicts["CEW02-CONFLICT-006"]["resolution"], "preserve_nested_demonic_subtype_and_cross_type_name_overlap")
        self.assertEqual(conflicts["CEW02-CONFLICT-007"]["resolution"], "preserve_cross_tag_overlap")
        self.assertEqual(len(model["owner_resolution_queue"]), 5)

    def test_havalaea_animal_personhood_and_pathways_do_not_collapse_into_type(self):
        model = self.load(MODEL)
        labels = model["cross_axis_recovery"]["Player Creatures.PDF"]["havalaean_sapient_animal_template"]["source_labels"]
        self.assertEqual(labels, ["Beast","Monstrous Beast","Beast (Sapient)","Beastfolk"])
        decisions = self.load(BACKLOG)["cew02_decisions"]
        self.assertFalse(decisions["animal_equals_beast"])
        self.assertFalse(decisions["havalaea_sapient_animal_conversion_erases_ecological_animal_identity"])
        text = AUDIT.read_text(encoding="utf-8")
        self.assertIn("native-born Havalaean animals may remain biologically/ecologically animals", text)
        self.assertIn("mount/pet/familiar status is never inferred from type", text)

    def test_nested_systems_preserve_body_affinity_subtype_and_stage_roles(self):
        nested = self.load(MODEL)["nested_systems"]
        self.assertEqual(nested["Chaos"]["role"], "body_plan_or_manifestation")
        self.assertEqual(nested["Fey"]["role"], "body_plan_or_manifestation")
        self.assertEqual(nested["Elemental"]["role"], "origin_or_affinity")
        self.assertEqual(nested["Dragon"]["secondary_axis"]["role"], "stage_or_variant")
        self.assertEqual(nested["Toon"]["secondary_axis"]["role"], "behavioral_tag")
        self.assertIn("Mechanical", nested["Construct"]["terms"])
        self.assertIn("Chaos Demons (Chaos & Foam)", nested["Demonic"]["terms"])

    def test_closeout_advances_once_to_cew03(self):
        backlog = self.load(BACKLOG)
        states = {r["id"]: r["status"] for r in backlog["tranches"]}
        strict_order = backlog["strict_order"]
        self.assertGreaterEqual(strict_order.index(backlog["completed_through"]), strict_order.index("CEW-02"))
        self.assertEqual(states["CEW-01"], "completed_verified")
        self.assertEqual(states["CEW-02"], "completed_verified")
        if backlog["completed_through"] == "CEW-02":
            self.assertEqual(backlog["current_item"], "CEW-03")
            self.assertEqual(backlog["current_item_state"], "selected_not_started")
            self.assertEqual(states["CEW-03"], "selected_not_started")
        else:
            self.assertGreater(strict_order.index(backlog["current_item"]), strict_order.index("CEW-02"))
        self.assertEqual(backlog["cew02_decisions"]["contract_id"], "CEW-TAX-1.0")
        self.assertFalse(backlog["application_implementation_authority"])

    def test_report_names_exact_successor(self):
        text = REPORT.read_text(encoding="utf-8")
        self.assertIn("CEW-03 — Creature Classification Model", text)
        self.assertIn("performed no creature definition identity promotion", text.lower())


if __name__ == "__main__":
    unittest.main()
