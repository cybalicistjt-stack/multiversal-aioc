import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class RoadmapGraphTests(unittest.TestCase):
 @classmethod
 def setUpClass(c):
  c.g=json.loads((ROOT/"governance/application-planning/ROADMAP_DEPENDENCY_GRAPH.json").read_text())
  c.projection=json.loads((ROOT/"governance/ai/runtime/ROADMAP_COMPILED_PROJECTION.json").read_text())
 def test_live_graph_and_retired_projection_authority(self):
  self.assertEqual(self.g["status"],"CURRENT_PLANNING_AUTHORITY")
  self.assertEqual(self.projection["status"],"HISTORICAL_INERT")
  self.assertFalse(self.projection["operational_authority"])
  self.assertEqual(self.projection["canonical_current_state"],"operations/CURRENT.json")
 def test_edge_vocabulary_and_authority(self):self.assertEqual(set(self.g["edge_types"]),{"hard_requires","start_requires","late_bind_requires","golden_proof_requires","parallel_safe_with"})
 def test_four_initial_lanes_are_not_serialized_by_each_other(self):
  e=self.g["program_edges"];initial={"MCS","MCCS","MRCS","MSAS"}
  for n in initial:self.assertFalse(initial&set(e[n]["hard_requires"]));self.assertFalse(initial&set(e[n]["start_requires"]))
  self.assertEqual(self.g["parallel_safe_sets"],[["MCS","MCCS","MRCS","MSAS"]])
 def test_real_mera_mbes_causality_is_preserved(self):self.assertIn("MERA",self.g["program_edges"]["MBES"]["hard_requires"]);self.assertIn("MERA-04",self.g["program_edges"]["MBES"]["start_requires"])
 def test_foundation_overlap_and_rotation(self):
  g=self.g["milestone_gates"]
  self.assertEqual(g["PCA"]["PCA-01"],["CNI-02"])
  self.assertEqual(g["rotation"]["GPR-01"],["MRCS-05"])
  self.assertEqual(g["rotation"]["MNCS-01"],["MCCS-01"])
  self.assertIn("MCCS-01",self.g["program_edges"]["MNCS"]["start_requires"])
  self.assertNotIn("MCCS-02",self.g["program_edges"]["MNCS"]["start_requires"])
if __name__=="__main__":unittest.main()
