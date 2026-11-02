"""XTRA owner-scoped, pre-PCV readiness control-plane invariants."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
def load(relative):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))

class XtraRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.current = load("operations/CURRENT.json")
        self.lanes = load("operations/LANES.json")
        self.work = load("operations/work-items/" + self.current["lanes"]["xtra"]["selected_work_item"] + ".json")
        self.backlog = load("governance/application-planning/xtra-pre-pcv-readiness/XTRA_PROGRAM_BACKLOG.json")

    def test_xtra_is_selected_without_a_fourth_persistent_slot(self):
        self.assertEqual(self.lanes["persistent_implementation_lanes"], ["gpr", "cwks", "mtlc"])
        self.assertEqual(sum(row["id"] == "xtra" for row in self.lanes["lanes"]), 1)
        selected = self.current["lanes"]["xtra"]
        self.assertEqual(selected["selected_work_item"], self.work["work_item_id"])
        self.assertEqual(selected["attempt_id"], self.work["attempt_id"])
        self.assertEqual(selected["checkpoint_path"], "operations/work-items/" + selected["selected_work_item"] + ".json")
        self.assertEqual(selected["state"], self.work["status"])
        self.assertFalse(selected["implementation_authority"])
        self.assertFalse(self.work["implementation_authority"])
        for lane, expected in (("gpr", "PCV-03F"), ("mtlc", "MTLC-14"), ("axi", "AXI-01")):
            self.assertEqual(self.current["lanes"][lane]["selected_work_item"], expected)

    def test_all_twelve_tranches_are_bounded(self):
        entries = self.backlog["tranches"]
        self.assertEqual(len(entries), 12)
        self.assertEqual([row["id"] for row in entries],
                         [f"XTRA-{n:02d}" for n in range(1, 13)])
        self.assertEqual(self.backlog["selected_work_item"], self.work["work_item_id"])
        self.assertEqual(entries[0]["status"], "completed_verified")
        self.assertEqual(entries[1]["status"], "blocked_external")
        self.assertEqual(entries[2]["status"], "completed_verified")
        self.assertEqual(entries[3]["status"], "completed_verified")
        self.assertEqual(entries[4]["status"], "completed_verified")
        self.assertEqual(entries[5]["status"], "completed_verified")
        self.assertEqual(entries[6]["status"], "in_progress")
        self.assertTrue(all(row["status"] == "planned" for row in entries[7:]))
        self.assertTrue(all(row["code_implementation_allowed"] is False for row in entries))
        self.assertTrue(all(row["scope"] and row["acceptance"] and row["classification"] for row in entries))
        self.assertTrue(all(row["id"] not in row["depends_on"] for row in entries))

    def test_pcv_and_commercial_gates_remain_closed(self):
        gates = self.backlog["release_gates"]
        self.assertIn("blocked_by_pcv03f", gates["pcv04_to_10"])
        self.assertIn("human", gates["mtlc14"])
        self.assertIn("owner_approval_required", gates["commercial"])
        self.assertIn("verified_real_restore", gates["backup"])
        self.assertFalse(self.current["product_start_freeze"]["active"])
        self.assertIn("acceptance", self.current["lanes"]["xtra"]["execution_authority"])

if __name__ == "__main__":
    unittest.main()
