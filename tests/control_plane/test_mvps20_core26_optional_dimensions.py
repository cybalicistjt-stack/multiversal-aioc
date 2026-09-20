from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "governance/application-planning/player-species/MVPS-20_CORE26_OPTIONAL_DIMENSION_MATRIX_v1.0.0.json"
BINDINGS = ROOT / "governance/application-planning/player-species/MVPS-20_SPECIAL_SYSTEM_BINDINGS_v1.0.0.json"

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

OPTIONAL = ("lineage_subspecies", "forms_transformation", "progression_maturation")

class MVPS20Core26OptionalDimensionTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_required_mvps20_artifacts_exist(self):
        for p in (MATRIX, BINDINGS):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(), p)

    def test_matrix_explicitly_resolves_all_four_dimensions_for_all_26(self):
        m = self._j(MATRIX)
        self.assertEqual(m["matrix_id"], "MVPS20.CORE26.OPTIONAL_DIMENSIONS.v1")
        self.assertEqual(m["dimensions"], [*OPTIONAL, "social_language_knowledge"])
        self.assertEqual([x["species"] for x in m["species"]], list(EXPECTED))
        self.assertEqual(len(m["species"]), 26)
        for row in m["species"]:
            with self.subTest(species=row["species"]):
                self.assertEqual(row["dispatch_rule"], "typed_data_not_species_name")
                self.assertEqual(set(row["dimension_status"]), set(m["dimensions"]))
                for dim in OPTIONAL:
                    d = row["dimension_status"][dim]
                    self.assertIn(d["applicability"], {"applicable", "not_applicable_current_canon"})
                    self.assertIn(d["state"], {"governed", "explicit_not_applicable"})
                    self.assertTrue(d["source_refs"])
                social = row["dimension_status"]["social_language_knowledge"]
                self.assertEqual(social["state"], "governed")
                self.assertFalse(social["culture_is_biology"])
                self.assertTrue(social["biological_communication_distinct_from_learned_language"])
                self.assertEqual(social["learned_language_policy"], "explicit_source_rule_required_no_inference")
                self.assertEqual(social["knowledge_visibility_contract"], "MVPS.SpeciesIdentityKnowledgeHook")

    def test_source_backed_special_systems_bind_to_shared_contracts(self):
        b = self._j(BINDINGS)
        self.assertEqual(b["binding_set_id"], "MVPS20.CORE26.SPECIAL_SYSTEMS.v1")
        by = b["bindings"]

        self.assertEqual(by["Giantkin"]["lineage_subspecies"]["values"], ["Grendelkin", "Surtrborn", "Daityr"])
        self.assertEqual(by["Giantkin"]["lineage_subspecies"]["contract_ref"], "MVPS.LineageComposition")

        rat = by["Ratman"]["lineage_subspecies"]
        self.assertEqual(rat["values"], ["Rattori", "Nybra", "Rattakar", "Ratborn", "Chitta", "Taipanua", "Ska", "Muridian", "Raughtt"])
        self.assertEqual(rat["taxonomy_rank"], "subordinate_lineage_or_subspecies_candidate")
        self.assertFalse(rat["peer_core_species"])
        self.assertEqual(rat["raughtt_established_facts"], ["proper", "aristocratic", "Dominix"])

        self.assertEqual(by["Stygian"]["forms_transformation"]["binding_kind"], "conditional_functional_or_vestigial_wing_state")
        self.assertFalse(by["Stygian"]["forms_transformation"]["appearance_grants_flight"])

        v = by["Vespin"]["progression_maturation"]
        self.assertEqual(v["base_trait_ref"], "mv.core.trait.vespin.stinger")
        self.assertEqual(v["progression_contract_ref"], "MVPS.SpeciesProgressionHook")
        self.assertEqual(v["canonical_mutation_owner"], "Character/Progression owning domain")
        self.assertTrue(v["preserve_existing_stinger_system"])

        self.assertEqual(by["Kola-Ha"]["forms_transformation"]["contract_ref"], "MVPS.FormDefinition")
        self.assertEqual(by["Mythragara"]["forms_transformation"]["contract_ref"], "MVPS.TransformationSemantics")
        self.assertTrue(by["Suula"]["progression_maturation"]["xp_purchased_adaptations"])
        self.assertEqual(by["Suula"]["progression_maturation"]["progression_contract_ref"], "MVPS.SpeciesProgressionHook")
        self.assertEqual(by["Morganthyr"]["forms_transformation"]["outcomes"], ["Revenant", "Sanguivore", "Fragmentarii"])
        self.assertEqual(by["Morganthyr"]["forms_transformation"]["transition_count_max"], 1)
        self.assertTrue(by["Traiga"]["progression_maturation"]["source_bounded_adaptations"])
        self.assertTrue(by["Moravi"]["lineage_subspecies"]["source_bounded_subspecies"])
        self.assertTrue(by["ManyToms"]["lineage_subspecies"]["source_bounded_variants"])

    def test_every_species_appends_v1_2_definition_and_register_without_rewriting_v1_1(self):
        for name, (slug, stable_id) in EXPECTED.items():
            with self.subTest(species=name):
                old_def = ROOT / f"content-source/core26-species/{slug}/definition-v1.1.0.json"
                old_reg = ROOT / f"content-source/core26-species/{slug}/register-v1.1.0.json"
                defp = ROOT / f"content-source/core26-species/{slug}/definition-v1.2.0.json"
                regp = ROOT / f"content-source/core26-species/{slug}/register-v1.2.0.json"
                self.assertTrue(old_def.is_file(), old_def)
                self.assertTrue(old_reg.is_file(), old_reg)
                self.assertTrue(defp.is_file(), defp)
                self.assertTrue(regp.is_file(), regp)
                raw = self._j(defp)["records"][0]
                obj = raw["gameObject"]
                reg = self._j(regp)["records"][0]["gameObject"]
                self.assertEqual(raw["contentVersion"], "1.2.0")
                self.assertEqual(obj["contentVersion"], "1.2.0")
                self.assertEqual(reg["contentVersion"], "1.2.0")
                self.assertEqual(raw["replacementOf"]["expectedContentVersion"], "1.1.0")
                self.assertEqual(obj["id"], stable_id)
                mv20 = obj["extensions"]["app.multiversal.aioc"]["mvps20OptionalDimensions"]
                self.assertEqual(mv20["matrixRef"], "MVPS20.CORE26.OPTIONAL_DIMENSIONS.v1")
                self.assertEqual(mv20["dispatchRule"], "typed_data_not_species_name")
                self.assertEqual(reg["register"]["optionalDimensionCompletion"]["matrixRef"], "MVPS20.CORE26.OPTIONAL_DIMENSIONS.v1")
                self.assertEqual(reg["register"]["optionalDimensionCompletion"]["definitionVersion"], "1.2.0")

    def test_generated_current_species_are_v1_2_and_preserve_mvps19_plus_mvps20_bindings(self):
        for name, (slug, stable_id) in EXPECTED.items():
            path = ROOT / "content-db/objects/mv-object-species-definition" / (stable_id.replace(".", "-").replace("_", "-").lower() + ".json")
            with self.subTest(species=name):
                obj = self._j(path)
                self.assertEqual(obj["contentVersion"], "1.2.0")
                ext = obj["gameObject"]["extensions"]["app.multiversal.aioc"]
                self.assertEqual(ext["mvps19Mechanics"]["matrixRef"], "MVPS19.CORE26.MECHANICS.v1")
                self.assertEqual(ext["mvps20OptionalDimensions"]["matrixRef"], "MVPS20.CORE26.OPTIONAL_DIMENSIONS.v1")
                self.assertEqual(ext["mvps20OptionalDimensions"]["dispatchRule"], "typed_data_not_species_name")

if __name__ == "__main__":
    unittest.main()
