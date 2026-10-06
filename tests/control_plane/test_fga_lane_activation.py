from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]

def read_json(path:str)->dict:
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

class FgaTerminalHistoryTests(unittest.TestCase):
    def test_fga_and_fde_are_terminal_history_after_mtlc_slot_replacement(self)->None:
        lanes=read_json("operations/LANES.json")
        current=read_json("operations/CURRENT.json")
        rows={row["id"]:row for row in lanes["lanes"]}
        self.assertIn("fga",rows)
        self.assertNotIn("fga",lanes["persistent_implementation_lanes"])
        self.assertEqual(current["lanes"]["fga"]["state"],"completed_verified")
        self.assertFalse(current["lanes"]["fga"]["implementation_authority"])
        self.assertEqual(current["completed_programs"]["FGA"]["state"],"completed_verified")
        self.assertEqual(current["completed_programs"]["FDE"]["state"],"completed_verified")
        self.assertEqual(current["completed_programs"]["FDE"]["selected_work_item"],"FDE-07")

if __name__=="__main__":
    unittest.main()
