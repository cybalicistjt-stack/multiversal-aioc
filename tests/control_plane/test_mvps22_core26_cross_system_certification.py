from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"governance/application-planning/player-species"
STANDARD=BASE/"CORE_26_GAME_READY_STANDARD_v1.0.0.json"
MATRIX=BASE/"MVPS-22_CORE26_CERTIFICATION_MATRIX_v1.0.0.json"
CROSS=BASE/"MVPS-22_REAL_SPECIES_CROSS_SYSTEM_FIXTURES_v1.0.0.json"
BALANCE=BASE/"MVPS-22_BALANCE_ADJUDICATION_REGISTER_v1.0.0.json"
RECEIPT=BASE/"MVPS-22_CERTIFICATION_RECEIPT_v1.0.0.json"

ROSTER=["Human","Elf","Dwarf","Goblin","Orc","Giantkin","Stygian","Sharr","Gray","The Free","Ratman","Furashin","Rog","Rohai","Moravi","Vespin","Rakuuta","Traiga","Kola-Ha","Toba-Madra","Arborae","Mythragara","Suula","Morganthyr","ManyToms","Akwi"]
OPTIONAL={"lineage_subspecies","forms_transformation","progression_maturation"}
ADAPTER_DOMAINS={"campaign","combat","social","exploration","crafting"}

class MVPS22Core26CertificationTests(unittest.TestCase):
    def j(self,p): return json.loads(p.read_text(encoding="utf-8"))

    def test_required_mvps22_artifacts_exist(self):
        for p in (MATRIX,CROSS,BALANCE,RECEIPT):
            with self.subTest(path=p):
                self.assertTrue(p.is_file(),p)

    def test_all_26_satisfy_the_same_19_dimension_standard(self):
        std=self.j(STANDARD); matrix=self.j(MATRIX)
        dims=[d["id"] for d in std["dimensions"]]
        self.assertEqual(len(dims),19)
        self.assertEqual(matrix["matrix_id"],"MVPS22.CORE26.CERTIFICATION.v1")
        self.assertEqual(matrix["standard_ref"],"CORE26.GAME_READY.v1")
        self.assertEqual([r["species"] for r in matrix["species"]],ROSTER)
        self.assertEqual(len(matrix["species"]),26)
        for row in matrix["species"]:
            with self.subTest(species=row["species"]):
                self.assertEqual(set(row["dimensions"]),set(dims))
                self.assertEqual(row["dispatch_rule"],"typed_data_not_species_name")
                self.assertEqual(row["overall_state"],"certified_for_mvps23_golden_proof")
                self.assertFalse(row["unresolved_mandatory_gaps"])
                for dim in std["dimensions"]:
                    d=row["dimensions"][dim["id"]]
                    self.assertTrue(d["evidence_refs"])
                    if dim["id"] in OPTIONAL:
                        self.assertIn(d["state"],{"certified","explicit_not_applicable"})
                    else:
                        self.assertEqual(d["state"],"certified")

    def test_cross_system_real_species_fixtures_cover_all_26_and_shared_owner_domains(self):
        x=self.j(CROSS)
        self.assertEqual(x["fixture_set_id"],"MVPS22.CORE26.REAL_SPECIES_CROSS_SYSTEM.v1")
        self.assertEqual(x["species_count"],26)
        self.assertEqual(x["adapter_domains"],sorted(ADAPTER_DOMAINS))
        self.assertEqual(len(x["species"]),26)
        for row in x["species"]:
            with self.subTest(species=row["species"]):
                self.assertEqual(set(row["adapters"]),ADAPTER_DOMAINS)
                self.assertTrue(all(v["state"]=="resolved" for v in row["adapters"].values()))
                self.assertTrue(all(v["canonical_owner_mutation_performed"] is False for v in row["adapters"].values()))
                self.assertEqual(row["npc_creature_reuse"]["species_canon_reused"],True)
                self.assertEqual(row["npc_creature_reuse"]["duplicate_species_canon_created"],False)
                self.assertEqual(row["runtime_projection"]["dispatch_rule"],"typed_data_not_species_name")
                self.assertEqual(row["serialization_migration"]["round_trip_state"],"verified")
                self.assertEqual(row["creation_validation"]["state"],"playable")

    def test_balance_and_adjudication_are_explicit_for_every_species(self):
        b=self.j(BALANCE)
        self.assertEqual(b["register_id"],"MVPS22.CORE26.BALANCE_ADJUDICATION.v1")
        self.assertEqual([r["species"] for r in b["species"]],ROSTER)
        for row in b["species"]:
            with self.subTest(species=row["species"]):
                self.assertEqual(row["balance_state"],"certified_at_current_contract_scope")
                self.assertEqual(row["adjudication_state"],"explicit_shared_owner_rules")
                self.assertFalse(row["unresolved_mandatory_gap"])
                self.assertFalse(row["species_name_runtime_branch_required"])
                self.assertTrue(row["evidence_refs"])

    def test_receipt_reports_zero_unresolved_mandatory_gaps_and_defers_only_final_replay(self):
        r=self.j(RECEIPT)
        self.assertEqual(r["receipt_id"],"MVPS22.CORE26.CERTIFICATION.RECEIPT.v1")
        self.assertEqual(r["species_count"],26)
        self.assertEqual(r["dimension_count"],19)
        self.assertEqual(r["unresolved_mandatory_gap_count"],0)
        self.assertEqual(r["cross_system_fixture_species_count"],26)
        self.assertEqual(r["balance_register_species_count"],26)
        self.assertEqual(r["next_required_tranche"],"MVPS-23")
        self.assertTrue(r["mvps23_final_golden_replay_required"])
        self.assertFalse(r["mvps23_expected_to_fill_mandatory_content_gaps"])

if __name__=="__main__":
    unittest.main()
