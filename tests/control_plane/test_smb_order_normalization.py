import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class SmbOrderingTests(unittest.TestCase):
 def setUp(self):self.e=json.loads((ROOT/"governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json").read_text())["program_edges"]
 def test_saa_sits_between_core_and_final_creator_integration(self):self.assertIn("SMB10A",self.e["SAA"]["start_requires"]);self.assertIn("SAA-20",self.e["SMB10B"]["start_requires"])
 def test_optional_ai_does_not_gate_internal_alpha(self):self.assertNotIn("SMB12",self.e["SMB13"]["hard_requires"]);self.assertNotIn("SMB12",self.e["SMB13"]["start_requires"]);self.assertIn("SMB12 optional live AI",self.e["SMB13"]["late_bind_requires"])
 def test_minimum_safety_precedes_remote_testers_and_full_hardening_remains(self):self.assertIn("PRE_ALPHA_SAFETY",self.e["SMB13"]["start_requires"]);self.assertIn("SMB13",self.e["SMB14"]["hard_requires"])
 def test_brp_gate_is_preserved(self):self.assertIn("SMB16",self.e["BRP"]["hard_requires"]);self.assertIn("BRP",self.e["SMB17"]["hard_requires"])
if __name__=="__main__":unittest.main()
