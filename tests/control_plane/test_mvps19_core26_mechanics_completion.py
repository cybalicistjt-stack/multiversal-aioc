from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECISIONS = ROOT / "governance/application-planning/player-species/MVPS-19_OWNER_DECISIONS_v1.0.0.json"
MATRIX = ROOT / "governance/application-planning/player-species/MVPS-19_CORE26_MECHANICS_MATRIX_v1.0.0.json"
PROFILES = ROOT / "governance/application-planning/player-species/MVPS-19_COMMON_MECHANICS_PROFILES_v1.0.0.json"
MANYTOMS = ROOT / "governance/application-planning/player-species/MVPS-19_MANYTOMS_DISTRIBUTED_CONTROLLER_CONTRACT_v1.0.0.json"

EXPECTED = {
    "Human": ("human", "mv.core.species.human"),
    "Elf": ("elf", "mv.core.species.elf"),
    "Dwarf": ("dwarf", "mv.core.species.dwarf"),
    "Goblin": ("goblin", "mv.core.species.goblin"),
    "Orc": ("orc", "mv.core.species.orc"),
    "Giantkin": ("giantkin", "mv.core.species.giantkin"),
    "Stygian": ("stygian", "mv.core.species.stygian"),
    "Sharr": ("sharr", "mv.core.species.sharr"),
    "Gray": ("gray", "mv.core.species.gray"),
    "The Free": ("the-free", "mv.core.species.free"),
    "Ratman": ("ratman", "mv.core.species.ratmen"),
    "Furashin": ("furashin", "mv.core.species.furashin"),
    "Rog": ("rog", "mv.core.species.rog"),
    "Rohai": ("rohai", "mv.core.species.rohai"),
    "Moravi": ("moravi", "mv.core.species.moravi"),
    "Vespin": ("vespin", "mv.core.species.vespin"),
    "Rakuuta": ("rakuuta", "mv.core.species.rakuuta"),
    "Traiga": ("traiga", "mv.core.species.traiga"),
    "Kola-Ha": ("kola-ha", "mv.core.species.kola-ha"),
    "Toba-Madra": ("toba-madra", "mv.core.species.toba-madra"),
    "Arborae": ("arborae", "mv.core.species.arborae"),
    "Mythragara": ("mythragara", "mv.core.species.mythragara"),
    "Suula": ("suula", "mv.core.species.suula"),
    "Morganthyr": ("morganthyr", "mv.core.species.morganthyr"),
    "ManyToms": ("manytoms", "mv.core.species.manytoms"),
    "Akwi": ("akwi", "species.akwi"),
}

SEMVER = re.compile(r"^1\.1\.0$")

class MVPS19Core26MechanicsCompletionTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_mvps19_artifacts_exist(self):
        for p in (DECISIONS, MATRIX, PROFILES, MANYTOMS):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(), p)

    def test_owner_decision_packet_is_exactly_bound_and_complete(self):
        d = self._j(DECISIONS)
        self.assertEqual(d["decision_set_id"], "MVPS19.CORE26.OWNER_DECISIONS.v1")
        self.assertEqual(d["owner_decision_date"], "2026-09-20")
        self.assertEqual(d["source_document"]["filename"], "Core_26_MVPS19_Gap_Resolution_Decision_Packet_v0.1.docx")
        self.assertEqual(d["source_document"]["sha256"], "370d0e38a9c10438f8720f3bf4e167c80dde2f1865ff6a028a2c9ca34af0d19b")
        self.assertEqual([x["species"] for x in d["decisions"]], list(EXPECTED))
        self.assertEqual(len(d["decisions"]), 26)
        by = {x["species"]: x for x in d["decisions"]}
        self.assertEqual(by["Dwarf"]["edits"]["sense_grants"], ["low_light_vision"])
        self.assertEqual(by["Orc"]["edits"]["size_class"], "Medium")
        self.assertEqual(set(by["The Free"]["edits"]["immunities"]), {"poison", "disease"})
        self.assertEqual(by["Furashin"]["edits"]["size_class"], "Medium")
        self.assertEqual(by["Furashin"]["edits"]["stature"], "short")
        self.assertEqual(by["Vespin"]["edits"]["stinger_system"], "preserve_full_existing_species_system")
        self.assertEqual(by["Rakuuta"]["edits"]["facial_feature"], "raven_shaped_black_feather_scales")
        self.assertEqual(by["ManyToms"]["edits"]["controller"], "split_toms_with_automatic_attention_penalties")

    def test_matrix_has_same_five_mechanics_domains_for_all_26(self):
        m = self._j(MATRIX)
        domains = m["domains"]
        self.assertEqual(domains, [
            "morphology_body_plan",
            "scale_movement_senses",
            "physiology_lifecycle_environment",
            "capabilities_natural_equipment",
            "equipment_interface_compatibility",
        ])
        self.assertEqual([x["species"] for x in m["species"]], list(EXPECTED))
        self.assertEqual(len(m["species"]), 26)
        for row in m["species"]:
            with self.subTest(species=row["species"]):
                self.assertEqual(set(row["domains"]), set(domains))
                self.assertNotIn("unresolved", {x["state"] for x in row["domains"].values()})
                self.assertEqual(row["dispatch_rule"], "typed_data_not_species_name")

    def test_every_species_has_v1_1_register_and_definition_source(self):
        for name, (slug, stable_id) in EXPECTED.items():
            with self.subTest(species=name):
                regp = ROOT / f"content-source/core26-species/{slug}/register-v1.1.0.json"
                defp = ROOT / f"content-source/core26-species/{slug}/definition-v1.1.0.json"
                self.assertTrue(regp.is_file(), regp)
                self.assertTrue(defp.is_file(), defp)
                reg = self._j(regp)["records"][0]["gameObject"]
                raw = self._j(defp)["records"][0]
                obj = raw["gameObject"]
                self.assertEqual(reg["contentVersion"], "1.1.0")
                self.assertEqual(raw["contentVersion"], "1.1.0")
                self.assertEqual(obj["contentVersion"], "1.1.0")
                self.assertEqual(obj["id"], stable_id)
                self.assertEqual(raw["replacementOf"]["expectedContentVersion"], "1.0.0")
                self.assertEqual(reg["register"]["mechanicsCompletion"]["mvps19DecisionSet"], "MVPS19.CORE26.OWNER_DECISIONS.v1")
                self.assertEqual(obj["extensions"]["app.multiversal.aioc"]["mvps19Mechanics"]["decisionSet"], "MVPS19.CORE26.OWNER_DECISIONS.v1")

    def test_generated_current_species_are_v1_1_and_bound_to_mechanics_matrix(self):
        for name, (slug, stable_id) in EXPECTED.items():
            path = ROOT / "content-db/objects/mv-object-species-definition" / (stable_id.replace(".", "-").replace("_", "-").lower() + ".json")
            with self.subTest(species=name):
                obj = self._j(path)
                self.assertEqual(obj["contentVersion"], "1.1.0")
                mech = obj["gameObject"]["extensions"]["app.multiversal.aioc"]["mvps19Mechanics"]
                self.assertEqual(mech["matrixRef"], "MVPS19.CORE26.MECHANICS.v1")
                self.assertEqual(mech["dispatchRule"], "typed_data_not_species_name")

    def test_owner_edits_survive_generation(self):
        def species_obj(stable_id: str) -> dict:
            p = ROOT / "content-db/objects/mv-object-species-definition" / (stable_id.replace(".", "-").replace("_", "-").lower() + ".json")
            return self._j(p)["gameObject"]["extensions"]["app.multiversal.aioc"]["mvps19Mechanics"]

        dwarf = species_obj("mv.core.species.dwarf")
        self.assertIn("low_light_vision", dwarf["senses"])
        self.assertEqual(species_obj("mv.core.species.orc")["sizeClass"], "Medium")
        free = species_obj("mv.core.species.free")
        self.assertEqual(set(free["immunities"]), {"poison", "disease"})
        fur = species_obj("mv.core.species.furashin")
        self.assertEqual(fur["sizeClass"], "Medium")
        self.assertEqual(fur["stature"], "short")
        vespin = species_obj("mv.core.species.vespin")
        self.assertEqual(vespin["naturalEquipment"]["stinger"]["systemRef"], "mv.core.trait.vespin.stinger")
        self.assertEqual(vespin["naturalEquipment"]["stinger"]["progressionHandling"], "preserve_existing_system_mvps20_progression_binding")
        rakuuta = species_obj("mv.core.species.rakuuta")
        self.assertIn("raven_shaped_black_feather_scales", rakuuta["morphologyMarkers"])
        many = species_obj("mv.core.species.manytoms")
        self.assertEqual(many["distributedBodyController"]["contractRef"], "MVPS19.ManyTomsDistributedController")
        self.assertTrue(many["distributedBodyController"]["automaticAttentionPenalties"])

    def test_manytoms_controller_preserves_one_person_one_action_economy(self):
        c = self._j(MANYTOMS)
        self.assertEqual(c["contract_id"], "MVPS19.ManyTomsDistributedController")
        self.assertEqual(c["personhood"], "one_character_one_civic_identity")
        self.assertEqual(c["action_economy"], "one_character_action_economy")
        self.assertTrue(c["split_controls"]["allow_split_toms"])
        self.assertEqual(c["split_controls"]["attention_penalty_mode"], "automatic_from_active_focus_groups")
        self.assertEqual(c["split_controls"]["numeric_penalty_authority"], "shared_attention_rules_profile")
        self.assertFalse(c["split_controls"]["body_count_grants_extra_turns"])
        self.assertFalse(c["inventory"]["body_count_multiplies_free_inventory"])

if __name__ == "__main__":
    unittest.main()
