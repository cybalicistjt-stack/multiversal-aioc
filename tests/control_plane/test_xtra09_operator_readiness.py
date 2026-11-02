"""XTRA-09 synthetic policy oracle. Never use for live authorization or restore attestations."""
from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / "governance/application-planning/xtra-pre-pcv-readiness"
M = D / "XTRA-09_OPERATIONAL_PRIVACY_INCIDENT_MATRIX_v1.0.0.json"

def oracle(profiles, gate, signals):
    """A checked synthetic prerequisite is not independent proof of its truth."""
    if gate not in profiles:
        return "DENY"
    reqs = profiles[gate]["requirements"]
    if any(signals.get(field) is not True for field in reqs):
        return "DENY"
    return "SYNTHETIC_REFERENCE_ONLY"

class Xtra09OperationalPreflight(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = json.loads(M.read_text(encoding="utf-8"))

    def test_reference_scope_and_source_pins(self):
        m = self.m
        self.assertEqual(m["matrix_id"], "XTRA09-OPERATIONS-PRIVACY-INCIDENT-REFERENCE-001")
        self.assertIn("REFERENCE_ONLY", m["proof_grade"])
        self.assertEqual(m["runtime_result"], "NOT_RUN")
        self.assertEqual(m["reference_result"], "NOT_RUN")
        for field in ("no_real_backups", "no_live_provider_changes", "no_real_user_data", "no_public_claims"):
            self.assertTrue(m[field])
        for path in m["source_pins"]:
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertTrue((D / "XTRA-09_OPERATOR_READINESS_AND_INCIDENT_RUNBOOK.md").is_file())

    def test_every_synthetic_scenario(self):
        m = self.m
        scenarios = m["scenarios"]
        self.assertGreaterEqual(len(scenarios), 45)
        self.assertEqual(len({s["id"] for s in scenarios}), len(scenarios))
        profiles = m["gate_profiles"]
        for s in scenarios:
            with self.subTest(id=s["id"]):
                self.assertEqual(s["reference_execution"], "NOT_RUN")
                self.assertEqual(s["actual_runtime_evidence"], "NOT_TESTED")
                self.assertEqual(oracle(profiles, s["gate"], s["signals"]), s["expected_reference_decision"])

    def test_every_gate_rejects_missing_and_nonboolean_proof(self):
        profiles = self.m["gate_profiles"]
        for gate, meta in profiles.items():
            valid = dict.fromkeys(meta["requirements"], True)
            self.assertEqual(oracle(profiles, gate, valid), "SYNTHETIC_REFERENCE_ONLY")
            for field in meta["requirements"]:
                for unproven in (False, None, "", "signed", 1):
                    with self.subTest(gate=gate, field=field, value=unproven):
                        self.assertEqual(oracle(profiles, gate, {**valid, field: unproven}), "DENY")
        self.assertEqual(oracle(profiles, "unlisted_operation", {}), "DENY")

    def test_actual_restore_and_privacy_remain_blocked(self):
        m = self.m
        restore = next(x for x in m["external_blockers"] if x["id"] == "XTRA-02")
        self.assertEqual(restore["status"], "BLOCKED_EXTERNAL")
        self.assertFalse(restore["verified_backup"])
        self.assertFalse(restore["verified_restore"])
        self.assertIsNone(m["targets"]["rpo_minutes"]["value"])
        self.assertIsNone(m["targets"]["rto_minutes"]["value"])
        self.assertIsNone(m["targets"]["retention_days"]["value"])
        current = json.loads((ROOT / "operations/CURRENT.json").read_text(encoding="utf-8"))
        self.assertEqual(current["lanes"]["xtra"]["selected_work_item"], "XTRA-09")
        self.assertFalse(current["lanes"]["xtra"]["implementation_authority"])
        xtra02 = json.loads((ROOT / "operations/work-items/XTRA-02.json").read_text(encoding="utf-8"))
        self.assertEqual(xtra02["status"], "blocked_external")

if __name__ == "__main__":
    unittest.main()
