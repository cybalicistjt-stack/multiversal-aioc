"""XTRA-07 tester/onboarding guide verification; never asserts installed usability."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
BASE = "governance/application-planning"
MATRIX = ROOT / BASE / "xtra-pre-pcv-readiness/XTRA-07_ROLE_TESTER_ONBOARDING_MATRIX_v1.0.0.json"
PLAYBOOK = ROOT / BASE / "xtra-pre-pcv-readiness/XTRA-07_ONBOARDING_SUPPORT_HUMAN_TESTER_PLAYBOOK.md"
F025 = ROOT / BASE / "internal-alpha/feature-packets/MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json"
FIXTURE = ROOT / BASE / "xtra-pre-pcv-readiness/XTRA-04_BEACON_DEBT_GOLDEN_CAMPAIGN_FIXTURE_v1.0.0.json"

def load(file):
    return json.loads(file.read_text(encoding="utf-8"))

class Xtra07RoleTesterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=load(MATRIX)
        cls.f=load(F025)
        cls.g=load(FIXTURE)
        cls.md=PLAYBOOK.read_text(encoding="utf-8")

    def test_source_bounded_three_roles_and_21_ordered_tasks(self):
        self.assertEqual(self.m["status"], "DOCUMENTATION_ONLY_PREPARED_NOT_HUMAN_TESTED")
        self.assertEqual([g["id"] for g in self.m["role_guides"]], ["PLAYER","GM","CREATOR"])
        self.assertEqual([g["role"] for g in self.m["role_guides"]], ["player","game-master","content-creator"])
        self.assertEqual(len(self.m["source_pins"]), 6)
        for group in self.m["role_guides"]:
            self.assertEqual(len(group["steps"]), 7)
            self.assertEqual([s["sequence"] for s in group["steps"]], list(range(1,8)))
            self.assertTrue(all(not s["verified_in_installed_product"] for s in group["steps"]))
            self.assertTrue(all(s["step_id"] in self.md for s in group["steps"]))
        self.assertEqual(sum(len(g["steps"]) for g in self.m["role_guides"]),21)

    def test_f025_issue_and_diagnostics_preserve_canonical_fields(self):
        mapping={"release_identity_required":"releaseIdentityRequiredFields",
                 "support_categories":"issueCategories",
                 "onboarding_stages":"onboardingStages",
                 "issue_report_required":"issueReportRequiredFields",
                 "diagnostic_manifest_required":"diagnosticManifestRequiredFields",
                 "issue_receipt_required":"issueReceiptRequiredFields",
                 "help_contexts":"helpContexts"}
        for key,field in mapping.items():
            self.assertEqual(self.m[key],self.f[field],msg=key)
        self.assertEqual(self.m["protected_diagnostics"],self.f["protectedDiagnosticSurfaces"])
        self.assertEqual(self.m["support_severity_levels"],[s["id"] for s in self.f["severityValues"]])
        p=self.m["privacy_and_consent"]
        self.assertEqual(p["default_diagnostics"],"EXCLUDED")
        self.assertTrue(p["consent_before_diagnostics"])
        self.assertTrue(p["redaction_preview_before_attachment"])
        self.assertTrue(p["client_redaction_plus_server_revalidation"])
        self.assertIn("raw database or filesystem dumps",p["secrets_excluded"])

    def test_negative_and_recovery_handoffs_are_unrun(self):
        cases=self.m["negative_cases"]
        self.assertEqual(len(cases),12)
        self.assertEqual(len({x["id"] for x in cases}),12)
        self.assertTrue(all(x["execution_status"]=="NOT_RUN" for x in cases))
        self.assertTrue(all(x["id"] in self.md for x in cases))
        self.assertEqual(len(self.m["recovery_cards"]),6)
        self.assertTrue(all(x["status"]=="SCRIPT_ONLY_NOT_TESTED" for x in self.m["recovery_cards"]))
        self.assertEqual(self.m["tester_session_template"]["first_success"],"NOT_OBSERVED")
        self.assertEqual(self.m["tester_session_template"]["negative_case_result"],"NOT_RUN")
        self.assertEqual(self.m["limits"]["cross_device_two_human"],"NOT_RUN")
        self.assertEqual(self.m["limits"]["installed_window_android"],"NOT_RUN")
        self.assertFalse(self.m["limits"]["public_release"])

    def test_source_first_party_accessibility_without_new_media(self):
        sc=self.m["accessibility_preparation"]
        self.assertEqual(sc["mobile_touch_target_min_px"],44)
        self.assertEqual([x["scene_id"] for x in sc["nonvisual_maps"]],
                         [x["scene_id"] for x in self.g["scenes"]])
        self.assertEqual([x["description"] for x in sc["nonvisual_maps"]],
                         [x["map_binding"]["semantic_alternative"] for x in self.g["scenes"]])
        self.assertEqual(sc["real_assistive_technology_human_proof"],"NOT_RUN")
        self.assertIn("NOT_RUN",self.md)
        self.assertIn("XTRA-02",self.md)
        self.assertIn("XTRA-06",self.md)

if __name__=="__main__":
    unittest.main()
