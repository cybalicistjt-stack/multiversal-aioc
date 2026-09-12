import json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class ReferenceProductProofTests(unittest.TestCase):
 @classmethod
 def setUpClass(c):c.m=json.loads((ROOT/"governance/application-planning/reference-product-proof/REFERENCE_PRODUCT_PROOF_MANIFEST.json").read_text())
 def test_base_is_immutable_nonauthoritative(self):b=self.m["base_fixture"];self.assertTrue(b["immutable"]);self.assertFalse(b["canonical_product_truth"]);self.assertFalse(b["authoritative_mutation_allowed"])
 def test_crassus_is_source_backed_exterior_constraint(self):c=self.m["exterior_creature"];self.assertEqual(c["name"],"Crassus");self.assertEqual(c["pages"],[25,26]);self.assertIn("Beast Creatures 1.PDF",c["project_source"]);self.assertIn("World/MCS",c["placement_boundary"])
 def test_reference_proof_does_not_replace_content_milestones(self):t=(ROOT/"governance/application-planning/reference-product-proof/REFERENCE_PRODUCT_PROOF_CONTRACT.md").read_text();self.assertIn("SMB-08",t);self.assertIn("SMB-09",t);self.assertIn("not a substitute",t)
if __name__=="__main__":unittest.main()
