import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ParallelLaneTests(unittest.TestCase):
 @classmethod
 def setUpClass(c):c.r=json.loads((ROOT/"governance/ai/runtime/PRODUCT_EXECUTION_LANES.json").read_text());c.p=json.loads((ROOT/"governance/ai/runtime/CURRENT_WORK_POINTER.json").read_text());c.by={x["lane_id"]:x for x in c.r["lane_definitions"]}
 def test_initial_cap_and_zero_active_after_maintenance(self):self.assertEqual(self.r["initial_active_cap"],4);self.assertEqual(self.r["active_product_attempts"],[]);self.assertFalse(self.r["legacy_primary_selection"]["implementation_authority"])
 def test_lane_maintenance_projection_matches_live_pointer(self):
  maintenance=self.r["maintenance_mode"]
  self.assertNotIn("exclusive_control_plane_maintenance",self.p)
  self.assertFalse(maintenance["active"])
  self.assertIsNone(maintenance["work_item"])
  self.assertFalse(maintenance["feature_starts_blocked"])
 def test_four_guaranteed_lanes_exist_and_are_disjoint(self):
  ids=["L1_SPATIAL","L2_CHARACTER_PRESENTATION","L3_RULES_CONTENT","L4_AUDIO"];self.assertTrue(all(x in self.by for x in ids));owners=[];paths=[]
  for i in ids:owners.extend(self.by[i]["mutation_claims"]);paths.extend(self.by[i]["path_claims"])
  self.assertEqual(len(owners),len(set(owners)));self.assertEqual(len(paths),len(set(paths)))
 def test_shared_integration_is_single_lease(self):q=self.r["shared_integration_queue"];self.assertFalse(q["ordinary_lane_direct_write"]);self.assertIn("CURRENT_WORK_POINTER/authority selectors",q["surfaces"])
 def test_waiting_for_integration_frees_slot_without_mutation(self):s=self.r["waiting_for_integration"];self.assertTrue(s["releases_active_slot"]);self.assertTrue(s["mutation_authority_retired"])
 def test_rotation_lanes_exist(self):
  for i in ["L5_NPC_CREATURE","L6_ADVENTURE","L7_GAMEPLAY_RUNTIME","L8_ENGINEERING","L9_BUILT_ENVIRONMENT"]:self.assertIn(i,self.by)
if __name__=="__main__":unittest.main()
