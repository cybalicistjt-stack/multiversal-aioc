"""XTRA-06 source acceptance traceability, not installed/client execution proof."""
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
BASE = "governance/application-planning/xtra-pre-pcv-readiness/"
MATRIX = BASE + "XTRA-06_PCV_ACCEPTANCE_PREFLIGHT_v1.0.0.json"
PROGRAM = "governance/application-planning/product-convergence/PCV_PRODUCT_CONVERGENCE_REAL_APP_VALIDATION_PROGRAM.md"
BACKLOG = "governance/application-planning/product-convergence/PCV_PROGRAM_BACKLOG.json"
GOLDEN = BASE + "XTRA-04_BEACON_DEBT_GOLDEN_CAMPAIGN_FIXTURE_v1.0.0.json"
ASSETS = BASE + "XTRA-05_BEACON_ASSET_RIGHTS_COVERAGE_v1.0.0.json"

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def parse_json(path):
    return json.loads(read(path))

class Xtra06PcvAcceptancePrework(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = parse_json(MATRIX)
        cls.program = read(PROGRAM)
        cls.backlog = parse_json(BACKLOG)
        cls.golden = parse_json(GOLDEN)
        cls.assets = parse_json(ASSETS)

    def test_every_blocked_pcv_successor_and_source_requirement_traced_exactly(self):
        matrix = self.matrix
        ids = [f"PCV-{i:02d}" for i in range(4, 11)]
        self.assertEqual([x["id"] for x in matrix["cases"]], ids)
        self.assertEqual(len(matrix["cases"]), 7)
        sources = re.split(r"(?=### (?:[4-9]\. PCV-0[4-9]|10\. PCV-10))", self.program)
        indexed = {}
        for section in sources:
            if not re.match(r"### (?:[4-9]\. PCV-0[4-9]|10\. PCV-10)", section):
                continue
            id_match = re.search(r"PCV-(?:0[4-9]|10)", section)
            indexed[id_match.group(0)] = [line[2:] for line in section.splitlines() if line.startswith("- ")]
        for entry in matrix["cases"]:
            id = entry["id"]
            source_item = next(item for item in self.backlog["tranches"] if item["id"] == id)
            self.assertEqual(entry["status"], "blocked_by_predecessor")
            self.assertEqual(source_item["status"], entry["status"])
            self.assertEqual(entry["name"], source_item["name"])
            self.assertEqual([c["source_requirement"] for c in entry["criteria"]], indexed[id])
            self.assertEqual([c["test_id"] for c in entry["criteria"]],
                             [id + "-AC" + f"{n:02d}" for n in range(1, len(indexed[id]) + 1)])
            self.assertTrue(all(c["result"] == "NOT_RUN" for c in entry["criteria"]))
            self.assertFalse(entry["implementation_authorized"])
            self.assertFalse(entry["real_device_verified"])
        self.assertEqual(sum(len(x["criteria"]) for x in matrix["cases"]), 45)

    def test_targeted_negative_scenarios_are_not_fabricated_passes(self):
        self.assertEqual(self.matrix["negative_preflight_total"], 24)
        self.assertEqual(self.matrix["acceptance_case_total"], 45)
        for entry in self.matrix["cases"]:
            self.assertGreaterEqual(len(entry["negative_preflights"]), 2)
            for case in entry["negative_preflights"]:
                self.assertEqual(case["result"], "NOT_RUN")
                self.assertTrue(case["scenario"] and case["expected"])
                self.assertIn(case["id"], [entry["id"] + "-N" + f"{n:02d}"
                                         for n in range(1, len(entry["negative_preflights"]) + 1)])
        self.assertEqual(self.matrix["global_result"], "NOT_RUN")

    def test_existing_first_party_and_asset_fixtures_preserved(self):
        self.assertEqual(self.matrix["source_campaign"]["id"], self.golden["campaign"]["id"])
        self.assertEqual(self.matrix["source_campaign"]["scene_count"], len(self.golden["scenes"]))
        self.assertEqual(self.matrix["source_campaign"]["scene_count"], 5)
        self.assertFalse(self.matrix["source_campaign"]["real_combat"])
        self.assertFalse(self.matrix["source_campaign"]["real_player"])
        self.assertEqual(self.matrix["asset_needs"],
                         [d["need_id"] for d in self.assets["additional_product_demands"]])
        self.assertEqual(len(self.matrix["asset_needs"]), 9)
        self.assertIn("NOT_RUN", self.matrix["status"])

    def test_provenance_and_real_world_receipt_fields(self):
        self.assertEqual([x["path"] for x in self.matrix["source_pins"]],
                         [PROGRAM, BACKLOG, ASSETS, GOLDEN])
        fields = self.matrix["receipt_fields"]
        self.assertTrue({"pcv_item", "case_id", "candidate_sha", "platform",
                         "actual_result", "independent_evidence"} <= set(fields))
        self.assertIn("cannot start or certify", self.matrix["authority"])

if __name__ == "__main__":
    unittest.main()
