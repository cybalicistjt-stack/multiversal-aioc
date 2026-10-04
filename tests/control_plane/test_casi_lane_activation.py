from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]

def read_json(path:str)->dict:
    return json.loads((ROOT/path).read_text(encoding="utf-8"))

class CasiTerminalHistoryTests(unittest.TestCase):
    def test_casi_is_terminal_history_after_fga_slot_replacement(self)->None:
        lanes=read_json("operations/LANES.json")
        current=read_json("operations/CURRENT.json")
        rows={row["id"]:row for row in lanes["lanes"]}
        self.assertIn("casi",rows)
        self.assertNotIn("casi",lanes["persistent_implementation_lanes"])
        self.assertEqual(current["lanes"]["casi"]["state"],"completed_verified")
        self.assertFalse(current["lanes"]["casi"]["implementation_authority"])
        self.assertEqual(current["completed_programs"]["CASI"]["state"],"completed_verified")
        self.assertEqual(current["completed_programs"]["CASI"]["selected_work_item"],"CASI-08")

if __name__=="__main__":
    unittest.main()
