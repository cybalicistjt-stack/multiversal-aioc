"""XTRA-06: verify PCV-04..10 acceptance matrix fidelity. Not real-app proof."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "governance/application-planning"
MATRIX = ROOT / BASE / "xtra-pre-pcv-readiness/XTRA-06_PCV_ACCEPTANCE_PREFLIGHT_v1.0.0.json"
PROGRAM = ROOT / BASE / "product-convergence/PCV_PRODUCT_CONVERGENCE_REAL_APP_VALIDATION_PROGRAM.md"
BACKLOG = ROOT / BASE / "product-convergence/PCV_PROGRAM_BACKLOG.json"
ASSETS = ROOT / BASE / "xtra-pre-pcv-readiness/XTRA-05_BEACON_ASSET_RIGHTS_COVERAGE_v1.0.0.json"
FIXTURE = ROOT / BASE / "xtra-pre-pcv-readiness/XTRA-04_BEACON_DEBT_GOLDEN_CAMPAIGN_FIXTURE_v1.0.0.json"

def read_json(file):
    return json.loads(file.read_text(encoding="utf-8"))

class Xtra06PCVAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = read_json(MATRIX)
        cls.program = PROGRAM.read_text(encoding="utf-8")
        cls.pcv = read_json(BACKLOG)
        cls.assets = read_json(ASSETS)
        cls.fixture = read_json(FIXTURE)

    def test_every_source_acceptance_requirement_preserved_in_order(self):
        expected_ids = [f"PCV-{i:02d}" for i in range(4, 11)]
        self.assertEqual([x["id"] for x in self.m["cases"]], expected_ids)
        self.assertEqual(self.m["acceptance_case_total"], 45)
        self.assertEqual(sum(len(x["criteria"]) for x in self.m["cases"]), 45)
        registry = {x["id"]: x for x in self.pcv["tranches"]}
        all_ids = []
        for row in self.m["cases"]:
            item = row["id"]
            self.assertEqual(row["name"], registry[item]["name"])
            self.assertEqual(row["status"], "blocked_by_predecessor")
            self.assertEqual(registry[item]["status"], "blocked_by_predecessor")
            m = re.search(r"^### \d+\. " + re.escape(item) + r" — [^\n]+\n(.*?)(?=^### |^## |\Z)", self.program, re.M | re.S)
            self.assertIsNotNone(m, msg=item)
            section = m.group(1)
            self.assertIn("Acceptance:\n", section)
            acceptance_section = section.split("Acceptance:\n", 1)[1].split("\n\n", 1)[0]
            source_requirements = [line[2:] for line in acceptance_section.splitlines() if line.startswith("- ")]
            self.assertEqual([c["source_requirement"] for c in row["criteria"]],
                             source_requirements, msg=item)
            self.assertEqual(len(source_requirements), len(row["criteria"]))
            for idx, criterion in enumerate(row["criteria"], 1):
                self.assertEqual(criterion["test_id"], f"{item}-AC{idx:02d}")
                self.assertTrue(criterion["test_procedure"].strip())
                self.assertTrue(criterion["required_observation"].strip())
                self.assertEqual(criterion["result"], "NOT_RUN")
                all_ids.append(criterion["test_id"])
        self.assertEqual(len(all_ids), len(set(all_ids)))

    def test_negative_preflights_are_not_fake_results(self):
        all_ids = []
        self.assertEqual(self.m["negative_preflight_total"], 24)
        for row in self.m["cases"]:
            self.assertFalse(row["implementation_authorized"])
            self.assertFalse(row["real_device_verified"])
            for entry in row["negative_preflights"]:
                self.assertTrue(entry["id"].startswith(row["id"] + "-N"))
                self.assertTrue(entry["scenario"].strip())
                self.assertTrue(entry["expected"].strip())
                self.assertEqual(entry["result"], "NOT_RUN")
                all_ids.append(entry["id"])
        self.assertEqual(len(all_ids), 24)
        self.assertEqual(len(set(all_ids)), 24)
        self.assertEqual(self.m["global_result"], "NOT_RUN")
        self.assertEqual(self.m["status"], "SOURCE_LINKED_PREIMPLEMENTATION_TEST_PLAN_NOT_RUN")

    def test_asset_and_campaign_gates_remain_unclaimed(self):
        expected = [a["need_id"] for a in self.assets["additional_product_demands"]]
        self.assertEqual(expected, [f"PCV10-A{i:02d}" for i in range(1, 10)])
        self.assertEqual(self.m["asset_needs"], expected)
        self.assertFalse(self.m["source_campaign"]["real_combat"])
        self.assertFalse(self.m["source_campaign"]["real_player"])
        self.assertEqual(self.m["source_campaign"]["id"], self.fixture["campaign"]["id"])
        self.assertFalse(self.fixture["proof_limits"]["actual_two_human_play"])
        self.assertEqual(self.assets["coverage"]["source_media_bindings"], 0)
        self.assertEqual(len(self.m["source_pins"]), 4)

    def test_receipt_and_safety_fields_are_actionable(self):
        receipt = self.m["receipt_fields"]
        for field in ("pcv_item", "case_id", "candidate_sha", "role", "platform",
                      "device_id", "actual_result", "independent_evidence",
                      "artifact_digest", "authoritative_source_owner"):
            self.assertIn(field, receipt)
        capture = self.m["evidence_capture_instructions"]
        self.assertIn("two distinct human", capture["device_roles"].lower())
        self.assertIn("No secrets", capture["privacy"])
        self.assertIn("PCV-03F", capture["sequential_owner_gate"])
        self.assertGreaterEqual(len(capture["failure_taxonomy"]), 8)

if __name__ == "__main__":
    unittest.main()
