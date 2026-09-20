from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"governance/application-planning/player-species"
STANDARD=BASE/"CORE_26_GAME_READY_STANDARD_v1.0.0.json"
M22=BASE/"MVPS-22_CORE26_CERTIFICATION_MATRIX_v1.0.0.json"
GOLDEN=BASE/"MVPS-23_CORE26_GAME_READY_GOLDEN_PROOF_v1.0.0.json"
ROSTER=["Human","Elf","Dwarf","Goblin","Orc","Giantkin","Stygian","Sharr","Gray","The Free","Ratman","Furashin","Rog","Rohai","Moravi","Vespin","Rakuuta","Traiga","Kola-Ha","Toba-Madra","Arborae","Mythragara","Suula","Morganthyr","ManyToms","Akwi"]

class MVPS23GoldenProof(unittest.TestCase):
    def j(self,p): return json.loads(p.read_text(encoding="utf-8"))

    def test_golden_proof_exists(self):
        self.assertTrue(GOLDEN.is_file(),GOLDEN)

    def test_all_26_replay_same_19_dimension_standard(self):
        g=self.j(GOLDEN); s=self.j(STANDARD); m=self.j(M22)
        self.assertEqual(g["proof_id"],"MVPS23.CORE26.GAME_READY.GOLDEN.v1")
        self.assertEqual(g["standard_ref"],"CORE26.GAME_READY.v1")
        self.assertEqual(g["species_count"],26)
        self.assertEqual(g["dimension_count"],19)
        self.assertEqual([x["species"] for x in g["species"]],ROSTER)
        self.assertEqual([x["species"] for x in m["species"]],ROSTER)
        dims=[d["id"] for d in s["dimensions"]]
        for row in g["species"]:
            with self.subTest(species=row["species"]):
                self.assertEqual(row["result"],"game_ready_certified")
                self.assertEqual(row["definition_version"],"1.2.0")
                self.assertEqual(row["register_version"],"1.2.0")
                self.assertTrue(row["source_traceable"])
                self.assertFalse(row["unresolved_mandatory_gaps"])
                self.assertEqual(list(row["dimension_replay"]),dims)
                self.assertTrue(all(v["result"]=="pass" for v in row["dimension_replay"].values()))
                self.assertTrue(all(v["evidence_refs"] for v in row["dimension_replay"].values()))

    def test_zero_roster_drift_and_zero_species_name_application_branches(self):
        g=self.j(GOLDEN)
        self.assertEqual(g["roster_drift"]["added"],[])
        self.assertEqual(g["roster_drift"]["removed"],[])
        self.assertEqual(g["roster_drift"]["renamed"],[])
        a=g["application_branch_audit"]
        self.assertEqual(a["repository"],"cybalicistjt-stack/Multiversal-app")
        self.assertEqual(a["audited_main_sha"],"e3bdef17ce2ce497d172479b81c35166af2226bb")
        self.assertEqual(a["species_name_application_branch_findings"],[])
        self.assertEqual(a["species_name_application_branch_count"],0)
        self.assertTrue(a["typed_dispatch_only"])

    def test_terminal_summary_has_no_waivers_or_follow_on_gap_filling(self):
        g=self.j(GOLDEN)
        self.assertEqual(g["game_ready_certified_count"],26)
        self.assertEqual(g["unresolved_mandatory_gap_count"],0)
        self.assertEqual(g["waived_mandatory_dimension_count"],0)
        self.assertTrue(g["production_extension_terminal"])
        self.assertIsNone(g["strict_successor"])
        self.assertFalse(g["future_tranche_required_to_fill_current_game_ready_gap"])

if __name__=="__main__":
    unittest.main()
