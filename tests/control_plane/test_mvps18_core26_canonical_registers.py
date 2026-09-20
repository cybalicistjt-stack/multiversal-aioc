from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER_ROOT = ROOT / "content-source" / "core26-species"
BY_TYPE = ROOT / "content-db" / "indexes" / "by-type.json"
BY_SOURCE = ROOT / "content-db" / "indexes" / "by-source.json"
SOURCE_REGISTRY = ROOT / "content-db" / "source-registry.json"
AUTHORITY = ROOT / "governance/application-planning/species-reconciliation/CORE_26_SPECIES_AUTHORITY_v1.0.0.json"

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

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


class MVPS18Core26CanonicalRegisterTests(unittest.TestCase):
    def _j(self, path: Path) -> dict:
        return json.loads(path.read_text(encoding="utf-8"))

    def test_every_current_species_has_a_permanent_versioned_canon_register_source(self):
        self.assertTrue(REGISTER_ROOT.is_dir(), REGISTER_ROOT)
        for name, (slug, definition_id) in EXPECTED.items():
            with self.subTest(species=name):
                register = REGISTER_ROOT / slug / "register-v1.0.0.json"
                self.assertTrue(register.is_file(), register)
                payload = self._j(register)
                self.assertEqual(payload["format"], "multiversal-canonical-content-source")
                self.assertEqual(payload["status"], "owner-approved-canonical-incorporation")
                self.assertEqual(len(payload["records"]), 1)
                obj = payload["records"][0]["gameObject"]
                self.assertEqual(obj["id"], f"mv.core.species-canon-register.{slug}")
                self.assertEqual(obj["name"], f"{name} Canon Register")
                self.assertEqual(obj["contentVersion"], "1.0.0")
                reg = obj["register"]
                self.assertEqual(reg["speciesName"], name)
                self.assertEqual(reg["speciesDefinitionStableId"], definition_id)
                self.assertEqual(reg["authorityId"], "CORE26-CURRENT-01")
                self.assertEqual(reg["gameReadyStandard"], "CORE26.GAME_READY.v1")
                self.assertTrue(reg["sourceLedger"])
                self.assertEqual(reg["updateContract"]["mode"], "append_versioned_source_never_mutate_history")
                self.assertTrue(reg["updateContract"]["requiresSourcePipelineRebuild"])
                self.assertTrue(reg["updateContract"]["requiresRegisterVersionBumpForCanonChange"])

    def test_every_current_species_has_a_versioned_definition_source_chain(self):
        for name, (slug, definition_id) in EXPECTED.items():
            with self.subTest(species=name):
                definition = REGISTER_ROOT / slug / "definition-v1.0.0.json"
                self.assertTrue(definition.is_file(), definition)
                payload = self._j(definition)
                self.assertIn(payload["status"], {
                    "owner-approved-canonical-incorporation",
                    "owner-approved-canonical-replacement",
                })
                self.assertEqual(len(payload["records"]), 1)
                raw = payload["records"][0]
                obj = raw["gameObject"]
                self.assertEqual(obj["id"], definition_id)
                self.assertEqual(obj["name"], name)
                self.assertEqual(obj["objectType"], "mv.object.species-definition")
                self.assertTrue(SEMVER.match(raw["contentVersion"]))
                if payload["status"] == "owner-approved-canonical-replacement":
                    self.assertEqual(raw["replacementOf"]["stableId"], definition_id)

    def test_generated_database_exposes_exactly_the_current_core26_and_26_registers(self):
        by_type = self._j(BY_TYPE)
        species_ids = set(by_type["mv.object.species-definition"])
        register_ids = set(by_type["mv.object.species-canon-register"])
        self.assertEqual(species_ids, {definition_id for _, definition_id in EXPECTED.values()})
        self.assertEqual(register_ids, {f"mv.core.species-canon-register.{slug}" for slug, _ in EXPECTED.values()})
        self.assertNotIn("mv.core.species.nekron", species_ids)

    def test_generated_species_definitions_are_exact_versioned_and_bound_to_current_authority(self):
        for name, (slug, definition_id) in EXPECTED.items():
            path = ROOT / "content-db" / "objects" / "mv-object-species-definition" / (
                definition_id.replace(".", "-").replace("_", "-").lower() + ".json"
            )
            with self.subTest(species=name):
                self.assertTrue(path.is_file(), path)
                obj = self._j(path)
                self.assertEqual(obj["name"], name)
                self.assertTrue(SEMVER.match(obj["contentVersion"]))
                reg = obj["gameObject"]["extensions"]["app.multiversal.aioc"]["speciesCanonRegister"]
                self.assertEqual(reg["authorityId"], "CORE26-CURRENT-01")
                self.assertEqual(reg["registerStableId"], f"mv.core.species-canon-register.{slug}")

    def test_manytoms_dossier_is_a_real_source_replacement_and_findable_by_source(self):
        many = self._j(ROOT / "content-db/objects/mv-object-species-definition/mv-core-species-manytoms.json")
        self.assertEqual(many["contentVersion"], "1.0.0")
        self.assertEqual(many["source"], "owner-approved-manytoms-canonical-species-dossier-v1.0.0")
        self.assertEqual(many["sourceLocator"], "ManyToms_Canonical_Species_Dossier_v1.0.0.docx")
        self.assertEqual(many["gameObject"]["canonicalLore"]["coreIdentity"]["normalHealthyComplement"], 12)
        self.assertEqual(many["provenance"]["sourceClass"], "replacement")
        self.assertIn("/manytoms/definition-v1.0.0.json", many["provenance"]["sourcePath"])

        by_source = self._j(BY_SOURCE)
        self.assertIn("mv.core.species.manytoms", by_source["owner-approved-manytoms-canonical-species-dossier-v1.0.0"])
        registry = self._j(SOURCE_REGISTRY)
        source_paths = {x["sourcePath"] for x in registry["sources"]}
        self.assertIn("content-source/core26-species/manytoms/definition-v1.0.0.json", source_paths)

    def test_manytoms_register_preserves_drive_provenance_and_development_precursor(self):
        payload = self._j(REGISTER_ROOT / "manytoms/register-v1.0.0.json")
        reg = payload["records"][0]["gameObject"]["register"]
        ledger = reg["sourceLedger"]
        canonical = [x for x in ledger if x["role"] == "canonical_dossier"]
        precursor = [x for x in ledger if x["role"] == "development_precursor"]
        self.assertEqual(len(canonical), 1)
        self.assertEqual(canonical[0]["title"], "ManyToms_Canonical_Species_Dossier_v1.0.0.docx")
        self.assertEqual(canonical[0]["driveFileId"], "1Pd9BQFYVDQBZIJBGM_Utnd_KLblHGGQ1")
        self.assertEqual(len(precursor), 1)
        self.assertEqual(precursor[0]["title"], "Manytomsinfo")
        self.assertEqual(precursor[0]["driveFileId"], "1cbrTQjYvpOBwAncFCGJqUjsCPeTzbxLTr2QwyM1Ra-s")
        self.assertEqual(precursor[0]["canonRole"], "development_history_not_blanket_canon")

    def test_legacy_nekron_is_retained_only_as_alias_to_morganthyr(self):
        by_type = self._j(BY_TYPE)
        self.assertIn("mv.core.species.nekron", by_type["mv.object.species-legacy-alias"])
        legacy = self._j(ROOT / "content-db/objects/mv-object-species-legacy-alias/mv-core-species-nekron.json")
        self.assertEqual(legacy["gameObject"]["currentTarget"]["objectId"], "mv.core.species.morganthyr")
        self.assertEqual(legacy["gameObject"]["aliasStatus"], "historical_alias_only")
        authority = self._j(AUTHORITY)
        self.assertEqual(authority["identity_migrations"]["Nekron"]["current"], "Morganthyr")


if __name__ == "__main__":
    unittest.main()
