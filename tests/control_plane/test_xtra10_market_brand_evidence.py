"""XTRA-10 evidence-only market research and public-claims denial checks."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "governance/application-planning/xtra-pre-pcv-readiness"
REGISTRY = DIR / "XTRA-10_MARKET_BRAND_EVIDENCE_MATRIX_v1.0.0.json"
MCB_BACKLOG = ROOT / "governance/application-planning/market-capture-brand-backbone/MCB_PROGRAM_BACKLOG.json"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def claim_can_go_public(claim, verified_real_product=False, owner_signed=False, rights_approved=False):
    """Reference rejection only; does not approve any real external publication."""
    if not all((verified_real_product, owner_signed, rights_approved)):
        return False
    if claim.get("status", "").startswith(("REJECT_", "HOLD_", "HYPOTHESIS_")):
        return False
    return claim.get("approved_public") is True

class Xtra10MarketSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load(REGISTRY)

    def test_registry_coverage_and_authority(self):
        data = self.data
        self.assertEqual(data["registry_id"], "XTRA10-MARKET-VOICE-CLAIMS-REFERENCE-001")
        self.assertEqual(data["work_item"], "XTRA-10")
        self.assertEqual(data["retrieved_at"], "2026-11-02")
        self.assertEqual(data["mcb_alignment"], [f"MCB-{i:02d}" for i in range(1, 9)])
        self.assertTrue((DIR / "XTRA-10_MARKET_CATEGORY_PERSONA_BRAND_CLAIMS_HANDOFF.md").is_file())
        self.assertTrue(all(data[k] is True for k in (
            "no_live_customer_interviews", "no_user_cohort_metrics", "no_validated_market_size",
            "no_mcb_implementation", "no_spend_or_recruitment", "no_public_release"
        )))
        self.assertEqual(len(data["competitors"]), 7)
        self.assertEqual(len(data["personas"]), 4)
        self.assertEqual(len(data["customer_research_proposals"]), 8)
        self.assertEqual(len(data["claims"]), 16)
        self.assertEqual(len(data["audience_message_drafts"]), 8)

    def test_source_traceability_and_vendor_caution(self):
        data = self.data
        sources = data["sources"]
        source_ids = [s["id"] for s in sources]
        self.assertEqual(len(source_ids), len(set(source_ids)))
        self.assertGreaterEqual(len(sources), 16)
        for s in sources:
            with self.subTest(source=s["id"]):
                if s["kind"] == "internal_source":
                    self.assertTrue((ROOT / s["path"]).is_file(), s["path"])
                else:
                    parsed = urlparse(s["url"])
                    self.assertEqual(parsed.scheme, "https")
                    self.assertTrue(parsed.hostname)
                    self.assertEqual(s["retrieved"], "2026-11-02")
        official_ids = {s["id"] for s in sources if s["kind"] == "vendor_primary"}
        self.assertEqual(len(official_ids), 7)
        self.assertEqual({c["primary"] for c in data["competitors"]}, official_ids)
        self.assertTrue(all(c["unknowns"] for c in data["competitors"]))
        self.assertEqual(len({c["id"] for c in data["competitors"]}), 7)
        for p in data["personas"]:
            self.assertEqual(p["evidence_grade"], "HYPOTHESIS_ONLY_NO_INTERVIEWS")
            self.assertTrue(p["validation"])
            self.assertTrue(set(p["supporting_qualitative_sources"]).issubset(source_ids))

    def test_all_unverified_market_and_customer_data_rejected(self):
        data = self.data
        self.assertFalse(data["research_backlog"]["live_observation_performed"])
        self.assertEqual(data["research_backlog"]["collected_real_responses"], 0)
        for item in data["customer_research_proposals"]:
            self.assertEqual(item["response_count"], 0)
        self.assertEqual(len({x["id"] for x in data["customer_research_proposals"]}), 8)
        market = data["market_caution"]
        self.assertEqual(market["source"], "I-ICV2")
        self.assertIn("not", market["strict_boundary"].lower())
        self.assertFalse(data["brand"]["approved_visual_identity"])

    def test_every_product_claim_stays_nonpublic(self):
        data = self.data
        claims = data["claims"]
        self.assertEqual(len({x["id"] for x in claims}), 16)
        sources = {s["id"] for s in data["sources"]}
        claim_ids = {x["id"] for x in claims}
        for c in claims:
            with self.subTest(claim=c["id"]):
                self.assertFalse(c["approved_public"])
                self.assertTrue(c["guardrail"])
                self.assertTrue(c["source_ids"])
                self.assertTrue(set(c["source_ids"]).issubset(sources))
                self.assertFalse(claim_can_go_public(c))
                self.assertFalse(claim_can_go_public(c, True, True, True))
        for msg in data["audience_message_drafts"]:
            self.assertFalse(msg["public_ready"])
            self.assertTrue(set(msg["proof_claims"]).issubset(claim_ids))
        self.assertEqual({m["persona"] for m in data["audience_message_drafts"]},
                         {p["id"] for p in data["personas"]})

    def test_no_mcb_activation_or_product_gate_bypass(self):
        mcb = load(MCB_BACKLOG)
        self.assertIsNone(mcb["current_item"])
        self.assertIsNone(mcb["current_attempt"])
        self.assertEqual(len(mcb["tranches"]), 25)
        self.assertTrue(all(x["status"] == "planned" for x in mcb["tranches"]))
        current = load(ROOT / "operations/CURRENT.json")
        selected = current["lanes"]["xtra"]["selected_work_item"]
        self.assertIn(selected, ("XTRA-10", "XTRA-11", "XTRA-12"))
        xtra10 = load(ROOT / "operations/work-items/XTRA-10.json")
        if selected == "XTRA-10":
            self.assertEqual(xtra10["status"], "in_progress")
        else:
            self.assertEqual(xtra10["status"], "completed_verified")
            self.assertTrue(xtra10["completed"])
        self.assertFalse(current["lanes"]["xtra"]["implementation_authority"])
        previous = load(ROOT / "operations/work-items/XTRA-09.json")
        self.assertEqual(previous["status"], "completed_verified")
        external = load(ROOT / "operations/work-items/XTRA-02.json")
        self.assertEqual(external["status"], "blocked_external")

if __name__ == "__main__":
    unittest.main()
