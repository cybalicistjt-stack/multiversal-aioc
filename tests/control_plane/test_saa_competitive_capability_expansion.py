import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

class SaaCompetitiveExpansionTests(unittest.TestCase):
    def setUp(self):
        self.backlog=json.loads((ROOT/"governance/application-planning/sequential-art-authoring/SAA_PROGRAM_BACKLOG.json").read_text())
        self.dag=json.loads((ROOT/"governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json").read_text())
        self.saa02=json.loads((ROOT/"governance/ai/work-state/SAA-02-attempt-001.json").read_text())
        self.amendment=(ROOT/"governance/application-planning/sequential-art-authoring/SAA_COMPETITIVE_CAPABILITY_EXPANSION_2026-09-21.md").read_text()
    def test_expansion_is_durable_and_does_not_start_saa02(self):
        self.assertEqual(len(self.backlog["strict_order"]),30)
        self.assertEqual(self.backlog["strict_order"][-1],"SAA-30")
        self.assertEqual(self.saa02["status"],"selected_not_started")
        self.assertFalse(self.saa02["implementation_authority"])
    def test_professional_capability_tranches_are_present(self):
        names={x["id"]:x["name"] for x in self.backlog["tranches"]}
        expected={
            "SAA-21":"Real-Time Collaboration, Review & Multi-Device Sync",
            "SAA-22":"Advanced Lettering, Balloon Styling & Story Text Editor",
            "SAA-23":"Pro Raster/Vector Drawing, Masks & Layer Interop",
            "SAA-24":"Comic Finishing Materials, Tones, Effect Lines, Rulers & Perspective",
            "SAA-25":"3D Reference, Pose/Scene Staging & Line Extraction",
            "SAA-26":"Webtoon & Responsive Scroll Authoring Preview",
            "SAA-27":"Print Prepress, CMYK & Bound-Book Preview",
            "SAA-28":"Multimedia/Interactive Comic, Localization & Accessible Read-Aloud",
            "SAA-29":"Industry Interchange & Layer-Aware Roundtrip",
            "SAA-30":"Expanded Professional/Collaborative Golden Comic Proof",
        }
        for key,value in expected.items(): self.assertEqual(names[key],value)
    def test_terminal_dependency_moves_to_saa30(self):
        self.assertEqual(self.dag["program_edges"]["SAA"]["golden_proof_requires"],["SAA-30"])
        self.assertIn("SAA-30",self.dag["program_edges"]["SMB10B"]["start_requires"])
        self.assertNotIn("SAA-20",self.dag["program_edges"]["SMB10B"]["start_requires"])
    def test_clean_room_feature_level_boundary_is_explicit(self):
        for phrase in ("clean-room","proprietary code","private file formats","SAA-30"):
            self.assertIn(phrase,self.amendment)

if __name__=="__main__":
    unittest.main()
