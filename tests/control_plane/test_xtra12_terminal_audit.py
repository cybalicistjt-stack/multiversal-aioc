"""XTRA-12 terminal *source* audit. No real provider/installed/commercial certification."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
DIR = ROOT / "governance/application-planning/xtra-pre-pcv-readiness"
REPORT = DIR / "XTRA-12_TERMINAL_EVIDENCE_REGISTRY_v1.0.0.json"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def git_blob_sha(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

class Xtra12TerminalSourceAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = load(REPORT)

    def test_source_scope_and_counts(self):
        r = self.r
        self.assertEqual(r["report_id"], "XTRA12-TERMINAL-EVIDENCE-AUDIT-20261102")
        self.assertEqual(r["observed_date"], "2026-11-02")
        self.assertEqual(r["total_tranches"], 12)
        self.assertEqual(r["completed_source_only"], 10)
        self.assertEqual(r["externally_blocked"], 1)
        self.assertEqual(r["terminal_audit_active"], 1)
        self.assertEqual(len(r["records"]), 11)
        self.assertEqual([x["id"] for x in r["records"]], [f"XTRA-{i:02d}" for i in range(1,12)])
        self.assertTrue((DIR / "XTRA-12_TERMINAL_READINESS_AND_OWNER_HANDOFF.md").is_file())
        self.assertIn("SOURCE", r["evidence_grade"])
        self.assertEqual(r["current_revision"], 653)
        self.assertFalse(r["real_environment_operations_performed"])
        self.assertIn("NOT_CERTIFIED",r["terminal_summary"])

    def test_every_artifact_source_git_sha_matches(self):
        for record in self.r["records"]:
            with self.subTest(work=record["id"]):
                path = ROOT / record["source_path"]
                self.assertTrue(path.is_file(), str(path))
                self.assertEqual(git_blob_sha(path), record["source_git_blob_sha"])
                cp = load(ROOT / "operations/work-items" / (record["id"]+".json"))
                self.assertEqual(cp["status"], record["status"])
                self.assertEqual(cp["completed"], record["completed"])
                self.assertTrue(record["proof_grade"])

    def test_exact_head_pr_and_ci_receipt_invariants(self):
        r = self.r
        receipts = [p for row in r["records"] for p in row["publication_receipts"]]
        self.assertEqual(len(receipts), 11)
        self.assertEqual(r["source_prs_verified"], 11)
        self.assertEqual(r["source_ci_runs_verified"], 11)
        self.assertEqual(len({p["pr"] for p in receipts}), 11)
        generations = [x["ready_reconciled_generation"] for x in r["records"] if x["id"]!="XTRA-02"]
        self.assertEqual(generations, sorted(generations))
        for p in receipts:
            self.assertTrue(p["ci_completed_success"])
            self.assertTrue(p["merged"])
            self.assertGreater(p["pr"], 1900)
            self.assertGreater(p["ci_run"], 41400000000)
            for key in ("head","merge_commit"):
                self.assertRegex(p[key], r"^[0-9a-f]{40}$")
        self.assertFalse(next(x for x in r["records"] if x["id"]=="XTRA-02")["publication_receipts"])

    def test_external_blocker_and_product_gates_remain_unresolved(self):
        r = self.r
        xtra02 = load(ROOT / "operations/work-items/XTRA-02.json")
        self.assertEqual(xtra02["status"], "blocked_external")
        self.assertFalse(xtra02["external_blocker"]["backup_verified"])
        self.assertFalse(xtra02["external_blocker"]["restore_verified"])
        self.assertEqual(len(r["unresolved_gates"]), 9)
        self.assertTrue(all(not x["resolved"] and x["status"]=="OPEN_OR_EXTERNAL_BLOCKED"
                            for x in r["unresolved_gates"]))
        first = next(x for x in r["unresolved_gates"] if x["source"]=="XTRA-02")
        self.assertEqual(first["priority"],"P0")
        self.assertEqual(first["deadline_utc"],"2026-11-08T11:53:54.383435Z")
        self.assertTrue(all(not value for value in r["non_authorizations"].values()))
        self.assertFalse(r["real_environment_operations_performed"])
        self.assertFalse(r["terminal_audit_completed"])
        self.assertFalse(r["audit_published"])
        app = r["app_snapshot"]
        self.assertTrue(app["pcv_03f"]["draft"])
        self.assertFalse(app["pcv_03f"]["actual_installed_pass"])
        self.assertFalse(app["mtlc_14"]["human_pass"])
        self.assertFalse(app["axi_pr_876"]["terminal_axi_program_proof"])

    def test_no_next_program_selected(self):
        current = load(ROOT / "operations/CURRENT.json")
        self.assertEqual(current["lanes"]["xtra"]["selected_work_item"], "XTRA-12")
        self.assertFalse(current["lanes"]["xtra"]["implementation_authority"])
        self.assertEqual(load(ROOT/"operations/work-items/XTRA-12.json")["status"],"in_progress")
        mcb = load(ROOT / "governance/application-planning/market-capture-brand-backbone/MCB_PROGRAM_BACKLOG.json")
        self.assertIsNone(mcb["current_item"])
        self.assertTrue(all(x["status"]=="planned" for x in mcb["tranches"]))
        pcv = load(ROOT / "governance/application-planning/product-convergence/PCV_PROGRAM_BACKLOG.json")
        blocked = [x for x in pcv["tranches"] if x["id"] in {f"PCV-{i:02d}" for i in range(4,11)}]
        self.assertEqual(len(blocked),7)
        self.assertTrue(all(x["status"]=="blocked_by_predecessor" for x in blocked))

if __name__=="__main__":
    unittest.main()
