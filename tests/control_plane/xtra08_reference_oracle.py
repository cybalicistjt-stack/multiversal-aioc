"""XTRA-08 only: synthetic model for a fail-closed threat preflight.
DO NOT import this from product code or treat green tests as deployed security.
"""
from __future__ import annotations
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MATRIX=ROOT/"governance/application-planning/xtra-pre-pcv-readiness/XTRA-08_ALLOWANCE_SECURITY_THREAT_MATRIX_v1.0.0.json"
ALL_SOURCE=ROOT/"governance/research-evaluations/subscription-allowance-threats-2026-11-01"
SOURCE_NAME="XTRA08-SA-BILL-PROTECTED-CAMPAIGN-REFERENCE-v1"

def reference_decision(domain, values):
    """Conservative synthetic-only oracle, NOT a source of entitlement authority."""
    checks={
        "issuance":("verified_subject","gm_role","player_member",
            "gm_subscription_active","current_revision","provider_signed",
            "rights_current","allowed_root","slot_open"),
        "use":("member","same_campaign","grant_current","rights_current","dependency_valid"),
        "replay":("current_membership","actor_match","command_match",
            "receipt_from_store","safe_external_projection"),
        "offline":("valid_signature","device_match","not_expired","epoch_current",
            "encrypted_vault","read_only"),
    }
    if domain=="policy":
        return "OWNER_DECISION_REQUIRED"
    if domain not in checks:
        return "DENY"
    if any(values.get(key) is not True for key in checks[domain]):
        return "DENY"
    if domain=="use" and values.get("operation")!="campaign-read":
        return "DENY"  # no broad export/search rights granted by this restricted oracle
    return "ALLOW_SYNTHETIC_ONLY"

class Xtra08ReferenceThreatTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=json.loads(MATRIX.read_text(encoding="utf-8"))

    def test_source_context_and_scope_safety(self):
        self.assertEqual(self.m["id"],SOURCE_NAME)
        self.assertEqual(self.m["status"],"REFERENCE_ONLY_NOT_DEPLOYED_NOT_BILLED")
        self.assertEqual(len(self.m["source_pins"]),5)
        for path in self.m["source_pins"]:
            self.assertTrue((ROOT/path).is_file(),path)
        self.assertTrue(self.m["no_real_payment"])
        self.assertTrue(self.m["no_production_patch"])
        self.assertEqual(self.m["runtime_result"],"NOT_RUN")
        self.assertEqual(self.m["reference_result"],"NOT_RUN")
        self.assertIn("one allowance per campaign per player-user",self.m["owner_policy_baseline"].lower())
        self.assertTrue(any("SA-BILL-09" in s for s in self.m["source_known_risks"]))
        self.assertTrue(any("SA-BILL-09" in s for s in self.m["source_known_risks"]))

    def test_all_synthetic_vectors_against_conservative_oracle(self):
        cases=self.m["scenarios"]
        self.assertEqual(len(cases),39)
        self.assertEqual(len(set(x["id"] for x in cases)),39)
        counts={}
        for case in cases:
            counts[case["domain"]]=counts.get(case["domain"],0)+1
            actual=reference_decision(case["domain"],case["input"])
            self.assertEqual(actual,case["expected_reference_decision"],case["id"])
            self.assertEqual(case["execution"],"REFERENCE_PENDING")
            self.assertEqual(case["real_product_status"],"NOT_TESTED")
            self.assertTrue(case["threat"])
            self.assertIn(case["evidence_source"],
                ["SA-BILL-05","SA-BILL-08","SA-BILL-09","SA-BILL-10",
                 "THREAT_MODEL_AND_BILLING_RULES"])
        self.assertEqual(counts,{"issuance":10,"use":12,"replay":6,"offline":7,"policy":4})
        self.assertEqual(sum(x["expected_reference_decision"]=="ALLOW_SYNTHETIC_ONLY" for x in cases),4)
        self.assertEqual(sum(x["expected_reference_decision"]=="OWNER_DECISION_REQUIRED" for x in cases),4)

    def test_negative_controls_fail_closed(self):
        allow={x["domain"]:x["input"] for x in self.m["scenarios"]
            if x["expected_reference_decision"]=="ALLOW_SYNTHETIC_ONLY"}
        self.assertEqual(set(allow),{"issuance","use","replay","offline"})
        for domain,valid in allow.items():
            self.assertEqual(reference_decision(domain,valid),"ALLOW_SYNTHETIC_ONLY")
            key={"issuance":"provider_signed","use":"grant_current",
                 "replay":"receipt_from_store","offline":"valid_signature"}[domain]
            tampered={**valid,key:False}
            self.assertEqual(reference_decision(domain,tampered),"DENY")
        self.assertEqual(reference_decision("unregistered",{}),"DENY")

    def test_owner_choices_cannot_activate_live_billing(self):
        self.assertGreaterEqual(len(self.m["owner_decisions_unapproved"]),5)
        self.assertEqual(reference_decision("policy",{"policy_approved":False}),
                         "OWNER_DECISION_REQUIRED")
        self.assertIn("SA-BILL-09 direct generic patch", " ".join(self.m["source_known_risks"]))
        self.assertGreaterEqual(len(self.m["production_blockers"]),6)

if __name__=="__main__":
    unittest.main()
