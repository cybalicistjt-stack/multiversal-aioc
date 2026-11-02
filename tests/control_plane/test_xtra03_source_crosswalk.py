"""XTRA-03: source-ledger structure checks, not application acceptance proof."""
import json
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "governance/application-planning/internal-alpha/INTERNAL_ALPHA_FEATURE_REGISTRY.json"
LEDGER = ROOT / "governance/application-planning/internal-alpha/INTERNAL_ALPHA_FEATURE_SOURCE_PR_RECONCILIATION_2026-11-02.md"
PACKETS = ROOT / "governance/application-planning/internal-alpha/feature-packets/README.md"

class Xtra03FeatureSourceLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
        cls.ledger = LEDGER.read_text(encoding="utf-8")
        cls.packet_index = PACKETS.read_text(encoding="utf-8")
        cls.rows = [line for line in cls.ledger.splitlines()
                    if re.match(r"^\| MV-IA-F\d{3} \|", line)]

    def test_25_feature_ids_and_design_status_match_current_registry(self):
        expected = {item["featureId"]: item["designStatus"] for item in self.registry["features"]}
        self.assertEqual(len(expected), 25)
        self.assertEqual(len(self.rows), 25)
        actual = {}
        for row in self.rows:
            fields = row.split("|")
            feature_id, status = fields[1].strip(), fields[2].strip().strip("`")
            self.assertNotIn(feature_id, actual)
            self.assertEqual(status, expected[feature_id])
            actual[feature_id] = status
        self.assertEqual(actual, expected)
        self.assertEqual(sum(v == "implementation-ready" for v in actual.values()), 9)
        self.assertEqual(sum(v == "registered" for v in actual.values()), 16)

    def test_all_rows_have_pinned_source_link_and_specific_limit(self):
        paths = set()
        for row in self.rows:
            fields = row.split("|")
            links = re.findall(
                r"https://github\.com/cybalicistjt-stack/Multiversal-app/blob/"
                r"db8e2d9b9d6cbc72f4386f6af2a5b98d01936e7f/([^\)]+)", row
            )
            self.assertTrue(links, msg=fields[1].strip() + " missing pinned app source")
            paths.update(links)
            self.assertIn("Multiversal-app/pull/", row)
            self.assertTrue(fields[4].strip(), msg="missing source assessment")
            self.assertTrue(fields[5].strip(), msg="missing limitation/gate")
        self.assertEqual(len(paths), 23)

    def test_open_candidate_and_unproved_feature_gates_are_explicit(self):
        self.assertIn("b77c9660c93d8480070a2c4403b30055059ced89", self.ledger)
        self.assertIn("70d83e43c1ed45990dcc7866552a679581f03171", self.ledger)
        self.assertIn("OPEN, unmerged", self.ledger)
        for feature_id in ("MV-IA-F012", "MV-IA-F017", "MV-IA-F024"):
            row = next(line for line in self.rows if feature_id in line)
            self.assertRegex(row, r"not independently|not separately|not establish|not prove|does not establish|not independently established|not independently certified|not proved")
        self.assertIn("historical design-handoff snapshot", self.packet_index)
        self.assertIn("INTERNAL_ALPHA_FEATURE_SOURCE_PR_RECONCILIATION_2026-11-02.md", self.packet_index)

if __name__ == "__main__":
    unittest.main()
