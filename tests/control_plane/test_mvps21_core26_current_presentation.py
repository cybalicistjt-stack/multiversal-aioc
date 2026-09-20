from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
P06=ROOT/"governance/application-planning/parallel-preimplementation/PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json"
CAPP=ROOT/"governance/application-planning/character-appearance-production/CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json"
BASE=ROOT/"governance/application-planning/player-species"
OVERLAY=BASE/"MVPS-21_CURRENT_APPEARANCE_PROFILE_OVERLAY_v1.0.0.json"
PICKER=BASE/"MVPS-21_CURRENT_CORE26_PRESENTATION_CATALOG_v1.0.0.json"
INDEX=BASE/"MVPS-21_AUTHORING_SEARCH_INSPECTION_INDEX_v1.0.0.json"
RECEIPT=BASE/"MVPS-21_PRESENTATION_REGENERATION_RECEIPT_v1.0.0.json"

ROSTER=["Human","Elf","Dwarf","Goblin","Orc","Giantkin","Stygian","Sharr","Gray","The Free","Ratman","Furashin","Rog","Rohai","Moravi","Vespin","Rakuuta","Traiga","Kola-Ha","Toba-Madra","Arborae","Mythragara","Suula","Morganthyr","ManyToms","Akwi"]

class MVPS21CurrentPresentationTests(unittest.TestCase):
    def j(self,p): return json.loads(p.read_text(encoding="utf-8"))

    def test_current_outputs_exist_without_rewriting_historical_25_profile_authorities(self):
        for p in (OVERLAY,PICKER,INDEX,RECEIPT):
            self.assertTrue(p.is_file(),p)
        p06=self.j(P06); capp=self.j(CAPP)
        self.assertEqual(p06["profile_count"],25)
        self.assertEqual(capp["profile_count"],25)
        self.assertIn("Nekron",[x["species"] for x in p06["profiles"]])
        self.assertNotIn("Morganthyr",[x["species"] for x in p06["profiles"]])
        self.assertNotIn("Akwi",[x["species"] for x in p06["profiles"]])

    def test_overlay_is_exact_current_core26_and_mechanically_non_authoritative(self):
        o=self.j(OVERLAY)
        self.assertEqual(o["overlay_id"],"MVPS21.CORE26.APPEARANCE.v1")
        self.assertEqual(o["authority_ref"],"CORE26-CURRENT-01")
        self.assertEqual(o["profile_count"],26)
        self.assertEqual([x["species"] for x in o["profiles"]],ROSTER)
        for p in o["profiles"]:
            with self.subTest(species=p["species"]):
                self.assertEqual(p["authority_class"],"current_authority_presentation_projection")
                self.assertFalse(p["mechanics_authority"])
                self.assertTrue(p["source_refs"])
                self.assertIn(p["profile_state"],{"historical_profile_projected_current","identity_migrated_historical_profile","current_source_backed_profile"})
                self.assertNotIn("grants",p)
                self.assertNotIn("mechanics",p)
        by={x["species"]:x for x in o["profiles"]}
        self.assertEqual(by["Morganthyr"]["source_species_identity"],"Nekron")
        self.assertEqual(by["Morganthyr"]["source_profile_id"],"species.nekron")
        self.assertEqual(by["Morganthyr"]["historical_aliases"],["Nekron","Nekrons"])
        self.assertEqual(by["Akwi"]["source_species_identity"],"Akwi")
        self.assertEqual(by["Akwi"]["source_profile_id"],"species.akwi")
        self.assertIn("Rabbit-like skull",by["Akwi"]["visual_summary"])
        self.assertIn("no tail",by["Akwi"]["visual_summary"])
        self.assertIn("long expressive ears",by["Akwi"]["visual_summary"])

    def test_picker_and_authoring_search_inspection_surfaces_use_current_roster(self):
        p=self.j(PICKER); i=self.j(INDEX)
        self.assertEqual(p["catalog_id"],"MVPS21.CORE26.PRESENTATION_CATALOG.v1")
        self.assertEqual(p["roster_count"],26)
        self.assertEqual([x["display_name"] for x in p["entries"]],ROSTER)
        self.assertNotIn("Nekron",[x["display_name"] for x in p["entries"]])
        self.assertTrue(all(x["appearance_profile_ref"].startswith("mvps21.appearance.") for x in p["entries"]))
        self.assertTrue(all(x["mechanics_authority"] is False for x in p["entries"]))
        self.assertEqual(i["entry_count"],26)
        self.assertEqual([x["display_name"] for x in i["entries"]],ROSTER)
        iby={x["display_name"]:x for x in i["entries"]}
        self.assertEqual(iby["Morganthyr"]["aliases"],["Nekron","Nekrons"])
        self.assertEqual(iby["Akwi"]["stable_id"],"species.akwi")
        self.assertEqual(iby["Ratman"]["peer_species_count"],1)
        self.assertEqual(iby["Ratman"]["subordinate_lineage_count"],9)

    def test_regeneration_receipt_binds_sealed_inputs_and_reports_no_current_25_hardcode(self):
        r=self.j(RECEIPT)
        self.assertEqual(r["receipt_id"],"MVPS21.CORE26.PRESENTATION.REGEN.v1")
        self.assertEqual(r["current_roster_count"],26)
        self.assertEqual(r["historical_inputs"]["ppia06"]["git_blob_sha"],"889e9f60513db718603a3295bd7e0867575909a6")
        self.assertEqual(r["historical_inputs"]["capp01"]["git_blob_sha"],"e2152e0ebe29dc70d5c503d36457092153adac5c")
        self.assertTrue(r["historical_inputs"]["sealed_unchanged"])
        self.assertEqual(r["current_surface_audit"]["hard_coded_25_current_surfaces"],[])
        self.assertEqual(r["current_surface_audit"]["canonical_identity_migrations"],{"Nekron":"Morganthyr","Nekrons":"Morganthyr"})
        self.assertTrue(r["boundaries"]["presentation_never_grants_mechanics"])
        self.assertTrue(r["boundaries"]["assets_never_define_species_taxonomy"])

if __name__=="__main__":
    unittest.main()
