"""XTRA-11 synthetic nonpublic commercial-readiness guardrails. Never a live policy engine."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "governance/application-planning/xtra-pre-pcv-readiness"
MATRIX = DIR / "XTRA-11_NONPUBLIC_COMMERCIAL_PREP_MATRIX_v1.0.0.json"
MCB = ROOT / "governance/application-planning/market-capture-brand-backbone/MCB_PROGRAM_BACKLOG.json"
X10 = DIR / "XTRA-10_MARKET_BRAND_EVIDENCE_MATRIX_v1.0.0.json"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def reference_only(gates, operation, signals):
    """No user-controlled mock approvals authorize a real operation."""
    if operation not in gates:
        return "DENY"
    if operation != "synthetic_launch_rehearsal":
        return "DENY"
    return ("SIMULATION_ONLY" if all(signals.get(key) is True for key in gates[operation])
            else "DENY")

class Xtra11NonpublicCommercialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = load(MATRIX)

    def test_source_and_authority_boundaries(self):
        m = self.m
        self.assertEqual(m["registry_id"], "XTRA11-NONPUBLIC-COMMERCIAL-PREPARATION-001")
        self.assertEqual(m["work_item"], "XTRA-11")
        self.assertEqual(m["evidence_date"], "2026-11-02")
        self.assertEqual(m["runtime_proof"], "NOT_RUN")
        self.assertEqual(m["public_readiness"], "NOT_APPROVED")
        for field in ("no_live_users","no_public_deploy","no_billing","no_paid_services",
                      "no_analytics_collection","no_recruitment","no_actual_interviews"):
            self.assertTrue(m[field], field)
        self.assertFalse(m["implementation_authorized"])
        self.assertFalse(m["MCB_implementation_authorized"])
        for path in m["source_pins"]:
            self.assertTrue((ROOT / path).is_file(), path)
        for src in m["external_source_guidance"]:
            parsed = urlparse(src["url"])
            self.assertEqual(parsed.scheme, "https")
            self.assertTrue(parsed.hostname)
            self.assertFalse(src["publication_cleared"])
        self.assertTrue((DIR / "XTRA-11_NONPUBLIC_SITE_COMMERCIAL_CONSENT_HANDOFF.md").is_file())

    def test_all_mcb09_25_planned_and_prepared_only(self):
        m = self.m
        modules = m["modules"]
        self.assertEqual([x["id"] for x in modules], [f"MCB-{n:02d}" for n in range(9,26)])
        for item in modules:
            self.assertEqual(item["implementation_status"], "PLANNED_UNSELECTED")
            self.assertEqual(item["preflight_status"], "PREPARATION_ONLY")
            self.assertEqual(item["actual_public_execution"], "NOT_RUN")
        backlog = load(MCB)
        self.assertEqual(len(backlog["tranches"]), 25)
        self.assertIsNone(backlog["current_item"])
        self.assertTrue(all(row["status"] == "planned" for row in backlog["tranches"]))

    def test_no_live_pages_media_contacts_or_prices(self):
        m = self.m
        self.assertEqual(len(m["pages"]), 10)
        self.assertEqual(len({x["path"] for x in m["pages"]}), 10)
        self.assertTrue(all(x["public_ready"] is False and x["personal_data_capture"] is False
                            and x["actual_deployment"] == "NOT_RUN" for x in m["pages"]))
        claim_ids = {row["id"] for row in load(X10)["claims"]}
        self.assertTrue(all(not row["approved_public"] for row in load(X10)["claims"]))
        for page in m["pages"]:
            self.assertTrue(set(page["claim_ids"]).issubset(claim_ids))
        self.assertEqual(len(m["storyboard"]), 5)
        self.assertTrue(all(x["fixture_only"] and not x["filmed"] for x in m["storyboard"]))
        self.assertEqual(len(m["seo_topics"]), 8)
        self.assertTrue(all(x["ranking_or_traffic_data"] == "NONE" and
                            x["publication_status"] == "INTERNAL_DRAFT" for x in m["seo_topics"]))
        self.assertEqual(len(m["package_hypotheses"]), 5)
        for pkg in m["package_hypotheses"]:
            self.assertIsNone(pkg["proposed_price"])
            self.assertIsNone(pkg["billing_plan_id"])
            self.assertFalse(pkg["approved_price"] or pkg["merchant_live"] or pkg["safe_to_show_publicly"])
            self.assertEqual(pkg["transaction_count"], 0)
            self.assertTrue(set(pkg["claim_ids"]).issubset(claim_ids))
        self.assertEqual(m["unit_economics_template"]["observed_users"], 0)
        for key in ("cac_usd","conversion_rate","churn_rate","arpu_usd","lifetime_value_usd"):
            self.assertIsNone(m["unit_economics_template"][key])

    def test_no_recruitment_tracking_or_privacy_bypass(self):
        m = self.m
        p = m["privacy_form_spec"]
        self.assertEqual(p["status"], "NO_FORM_DEPLOYED")
        self.assertFalse(p["default_checked"])
        self.assertFalse(p["send_button_enabled"])
        self.assertEqual(p["contact_records"], 0)
        self.assertFalse(p["legal_language_approved"])
        self.assertTrue(p["age_and_parental_review_required"])
        self.assertEqual(len(m["lifecycle"]), 9)
        self.assertEqual(len(m["event_taxonomy"]), 8)
        self.assertTrue(all(x["status"] == "MODEL_ONLY" and x["actual_people"] == 0 for x in m["lifecycle"]))
        self.assertTrue(all(not x["enabled"] and x["observed_count"] == 0 and
                            x["synthetic_only"] and not x["private_payload_allowed"] for x in m["event_taxonomy"]))
        self.assertTrue(m["claim_policy"]["all_public_claims_held"])

    def test_every_denial_and_simulation_excludes_live_execution(self):
        m = self.m
        cases = m["denial_scenarios"]
        self.assertGreaterEqual(len(cases), 55)
        self.assertEqual(len({x["id"] for x in cases}), len(cases))
        gates = m["gates"]
        self.assertEqual(len(gates), 10)
        self.assertEqual(len(m["real_operation_gates"]), 9)
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertEqual(case["expected"], "DENY")
                self.assertEqual(case["live_outcome"], "NOT_RUN")
                self.assertEqual(case["signals"][case["missing"]], False)
                self.assertEqual(reference_only(gates,case["gate"],case["signals"]), "DENY")
        for gate, fields in gates.items():
            full = dict.fromkeys(fields, True)
            self.assertEqual(reference_only(gates,gate,full),
                             "SIMULATION_ONLY" if gate == "synthetic_launch_rehearsal" else "DENY")
            for field in fields:
                self.assertEqual(reference_only(gates,gate,{**full,field:"approved"}),"DENY")
        s = m["simulated_positive"]
        self.assertEqual(reference_only(gates,s["gate"],s["signals"]),"SIMULATION_ONLY")
        self.assertEqual(s["live_outcome"],"NOT_RUN")
        self.assertEqual(reference_only(gates,"unknown_operation",{}),"DENY")

    def test_selected_xtra_boundary_and_external_risk(self):
        current = load(ROOT / "operations/CURRENT.json")
        selected = current["lanes"]["xtra"]["selected_work_item"]
        self.assertIn(selected, ("XTRA-11", "XTRA-12"))
        self.assertFalse(current["lanes"]["xtra"]["implementation_authority"])
        x11 = load(ROOT / "operations/work-items/XTRA-11.json")
        self.assertEqual(x11["status"], "in_progress" if selected == "XTRA-11" else "completed_verified")
        self.assertEqual(load(ROOT / "operations/work-items/XTRA-02.json")["status"], "blocked_external")

if __name__ == "__main__":
    unittest.main()
