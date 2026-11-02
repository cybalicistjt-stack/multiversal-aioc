#!/usr/bin/env python3
"""SA-BILL-01 proposed reference contract and corpus regression.

NOT a payment, server, database, encrypted-device or hostile-API test.
In particular, the locked in-memory slot below does NOT establish real
PostgreSQL serializable isolation, A3 authorization or deployed GM ownership.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
import json
import unittest

ROOT = Path(__file__).resolve().parents[2]
STUDY = ROOT / "governance/research-evaluations/subscription-allowance-threats-2026-11-01"
ALLOWED_ROOTS = frozenset({
    "custom-setting", "registered-species", "registered-item-set",
    "registered-ability-tree", "future-allowlisted-owner-type",
})
DENIED_PROVIDER_STATES = frozenset({
    "pending_purchase", "account_hold", "expired", "revoked_refunded",
    "disputed", "provider_unreachable",
})


def moment(value: str) -> datetime:
    """Only aware, real instants; normalize offsets before comparing."""
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("naive datetime cannot grant access")
    return dt.astimezone(timezone.utc)


def paid_entitled(snapshot: dict, now: str) -> bool:
    """Conservative model for *verified* provider entitlement, not issuance."""
    if snapshot.get("verified_by_provider") is not True:
        return False
    if not snapshot.get("payer_subject_id") or (
        snapshot.get("payer_subject_id") != snapshot.get("bound_subject_id")
    ):
        return False
    state = snapshot.get("status")
    if state in DENIED_PROVIDER_STATES or state in ("paused", "trial_verified"):
        return False  # explicitly unselected owner policy for trial/paused
    if state not in ("verified_active", "cancel_scheduled", "grace_entitled"):
        return False
    try:
        t = moment(now)
        if t < moment(snapshot["entitlement_from"]):
            return False
        if state == "grace_entitled":
            return snapshot.get("provider_confirms_grace") is True and (
                t < moment(snapshot["provider_grace_until"])
            )
        return t < moment(snapshot["entitled_until"])
    except (ValueError, TypeError, KeyError, OverflowError):
        return False


def gm_issue_eligibility(snapshot: dict, now: str) -> bool | None:
    """None means owner policy is not selected, never silently allow."""
    if snapshot.get("status") in ("trial_verified", "grace_entitled"):
        return None
    return paid_entitled(snapshot, now)


def trusted_closure(root: str, edges: dict[str, list[str]]) -> frozenset[str]:
    """One root's registered dependency graph; cycles/unknowns fail closed."""
    if root not in edges:
        raise ValueError("unregistered root")
    visited: set[str] = set()
    visiting: set[str] = set()

    def walk(node: str) -> None:
        if node not in edges:
            raise ValueError("unregistered dependency")
        if node in visiting:
            raise ValueError("dependency cycle")
        if node in visited:
            return
        visiting.add(node)
        for child in edges[node]:
            walk(child)
        visiting.remove(node)
        visited.add(node)

    walk(root)
    return frozenset(visited)


class ReferenceAllowanceSlots:
    """A test oracle, not the required production DB uniqueness fence."""
    def __init__(self) -> None:
        self._lock = Lock()
        self._slots: dict[tuple[str, str, str], tuple[str, str]] = {}

    def issue(
        self, *, campaign: str, player: str, issuer: str,
        registered_root: str, root_kind: str, request_id: str,
        issuer_eligible: bool, current_gm: bool, current_player: bool,
        trusted_dependencies: frozenset[str],
        claimed_dependencies: frozenset[str],
    ) -> str:
        if not all((campaign, player, issuer, registered_root, request_id)):
            return "DENY"
        if not all((issuer_eligible, current_gm, current_player)):
            return "DENY"
        if root_kind not in ALLOWED_ROOTS or trusted_dependencies != claimed_dependencies:
            return "DENY"
        if registered_root not in trusted_dependencies:
            return "DENY"
        key = (campaign, player, "gm-sponsored-premium")
        with self._lock:
            prior = self._slots.get(key)
            if prior is not None:
                return "IDEMPOTENT" if prior == (request_id, registered_root) else "CONFLICT"
            self._slots[key] = (request_id, registered_root)
            return "ISSUED"

    def total(self) -> int:
        return len(self._slots)


def access_decision(
    *, grant_campaign: str, requested_campaign: str,
    granted_player: str, current_player: str, membership: bool,
    issuer_current_gm: bool, issuer_subscribed: bool,
    grant_active: bool, release_active: bool, rights_allow: bool,
    resource_in_trusted_closure: bool, current_epoch: bool,
    requested_action: str,
) -> bool:
    """Separate access from ownership/export/transfer of dependent content."""
    if requested_action in (
        "export-outside-campaign", "transfer-restricted-character",
        "copy-protected-source", "mint-entitlement", "publish-content",
    ):
        return False
    return all((
        grant_campaign == requested_campaign,
        granted_player == current_player, membership, issuer_current_gm,
        issuer_subscribed, grant_active, release_active, rights_allow,
        resource_in_trusted_closure, current_epoch,
        requested_action in ("campaign-read", "campaign-use"),
    ))


class StudyIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.corpus = json.loads((STUDY / "ADVERSARIAL_SCENARIOS.json").read_text())
        cls.model = json.loads((STUDY / "BILLING_REFERENCE_MODEL.json").read_text())

    def test_sixty_unique_scenarios_and_truthful_evidence(self):
        cases = self.corpus["scenarios"]
        self.assertEqual(len(cases), 60)
        self.assertEqual(self.corpus["scenarioCount"], len(cases))
        self.assertEqual(len({c["id"] for c in cases}), len(cases))
        self.assertEqual(
            {x: sum(c["domain"] == x for c in cases) for x in
             ("billing", "allowance", "offline", "privacy")},
            {"billing": 20, "allowance": 24, "offline": 8, "privacy": 8})
        for case in cases:
            self.assertEqual(case["verificationStatus"], "not_executed")
            self.assertIn(case["expectedDecision"], self.corpus["interpretation"])
            for key in ("given", "when", "expectedEffect", "evidenceRequired"):
                self.assertTrue(case[key], (case["id"], key))

    def test_model_does_not_claim_payment_or_launch_approval(self):
        self.assertEqual(self.model["billingProduct"]["pricing"], "NOT_SELECTED")
        self.assertEqual(self.model["authority"], "PROPOSED_NOT_OWNER_RATIFIED")
        self.assertEqual(self.model["allowanceRules"]["maxActiveGrantsPerSlot"], 1)
        self.assertEqual(
            self.model["allowanceRules"]["uniqueIndex"],
            ["campaignId", "playerSubjectId", "slotKind"])
        self.assertEqual(len(self.model["billingStates"]), 11)
        self.assertEqual(
            len({s["id"] for s in self.model["billingStates"]}), 11)

    def test_consent_vs_paid_access_and_offset_instants(self):
        snap = {
            "verified_by_provider": True, "payer_subject_id": "gm1",
            "bound_subject_id": "gm1", "status": "cancel_scheduled",
            "entitlement_from": "2026-11-01T00:00:00Z",
            "entitled_until": "2026-12-01T00:00:00Z",
        }
        self.assertTrue(paid_entitled(snap, "2026-11-30T18:00:00-06:00".replace(
            "18:00:00", "17:59:59")))  # 23:59:59 UTC
        self.assertFalse(paid_entitled(snap, "2026-11-30T18:00:00-06:00"))
        self.assertTrue(gm_issue_eligibility(snap, "2026-11-30T17:59:59-06:00"))
        self.assertFalse(paid_entitled({**snap, "bound_subject_id": "gm2"},
                                       "2026-11-20T00:00:00Z"))
        self.assertFalse(paid_entitled({**snap, "verified_by_provider": False},
                                       "2026-11-20T00:00:00Z"))

    def test_invalid_dates_cannot_extend_entitlement(self):
        snap = {"verified_by_provider": True, "payer_subject_id": "gm",
                "bound_subject_id": "gm", "status": "verified_active",
                "entitlement_from": "2026-11-01T00:00:00Z",
                "entitled_until": "bad"}
        for now in ("2026-11-03T00:00:00Z", "invalid", "2026-11-03T00:00:00"):
            self.assertFalse(paid_entitled(snap, now))

    def test_grace_provenance_required_and_trial_policy_open(self):
        snap = {"verified_by_provider": True, "payer_subject_id": "gm",
                "bound_subject_id": "gm", "status": "grace_entitled",
                "entitlement_from": "2026-11-01T00:00:00Z",
                "entitled_until": "2026-11-01T00:00:01Z",
                "provider_grace_until": "2026-11-04T00:00:00Z"}
        t = "2026-11-03T00:00:00Z"
        self.assertFalse(paid_entitled(snap, t))
        self.assertTrue(paid_entitled({**snap, "provider_confirms_grace": True}, t))
        self.assertIsNone(gm_issue_eligibility(snap, t))
        self.assertIsNone(gm_issue_eligibility({**snap, "status": "trial_verified"}, t))
        self.assertFalse(paid_entitled({**snap, "status": "account_hold"}, t))

    def test_atomic_single_slot_under_hundred_competing_commands(self):
        slots = ReferenceAllowanceSlots()
        kwargs = dict(campaign="cx", player="p1", issuer="gm1",
                      root_kind="custom-setting", issuer_eligible=True,
                      current_gm=True, current_player=True,
                      trusted_dependencies=frozenset(("setting", "tree")),
                      claimed_dependencies=frozenset(("setting", "tree")))
        def run(i):
            return slots.issue(**kwargs, registered_root="setting", request_id=f"req{i}")
        with ThreadPoolExecutor(max_workers=16) as pool:
            results = list(pool.map(run, range(100)))
        self.assertEqual(results.count("ISSUED"), 1)
        self.assertEqual(results.count("CONFLICT"), 99)
        self.assertEqual(slots.total(), 1)
        self.assertEqual(slots.issue(**kwargs, registered_root="setting",
                                    request_id=f"req{results.index('ISSUED')}"),
                         "IDEMPOTENT")

    def test_per_campaign_per_player_not_one_global_slot(self):
        slots = ReferenceAllowanceSlots()
        args = dict(issuer="gm", registered_root="species", root_kind="registered-species",
                    issuer_eligible=True, current_gm=True, current_player=True,
                    trusted_dependencies=frozenset(("species",)),
                    claimed_dependencies=frozenset(("species",)))
        for campaign, player in (("cx", "p1"), ("cx", "p2"), ("cy", "p1")):
            self.assertEqual(slots.issue(campaign=campaign, player=player,
                                         request_id=f"{campaign}:{player}", **args), "ISSUED")
        self.assertEqual(slots.total(), 3)

    def test_require_registered_single_root_and_exact_closure(self):
        graph = {"setting": ["species", "item"], "species": ["tree"],
                 "item": [], "tree": [], "unrelated": []}
        close = trusted_closure("setting", graph)
        self.assertEqual(close, frozenset(("setting", "species", "item", "tree")))
        with self.assertRaises(ValueError):
            trusted_closure("setting", {"setting": ["setting"]})
        with self.assertRaises(ValueError):
            trusted_closure("missing", graph)
        slots = ReferenceAllowanceSlots()
        args = dict(campaign="cx", player="p1", issuer="gm",
                    root_kind="custom-setting", registered_root="setting",
                    request_id="first", issuer_eligible=True,
                    current_gm=True, current_player=True,
                    trusted_dependencies=close)
        self.assertEqual(slots.issue(**args,
                                    claimed_dependencies=close | {"unrelated"}), "DENY")
        self.assertEqual(slots.issue(**args, claimed_dependencies=close), "ISSUED")
        self.assertEqual(slots.total(), 1)

    def test_revocation_transfer_and_cross_campaign_veto(self):
        baseline = dict(grant_campaign="cx", requested_campaign="cx",
                        granted_player="p1", current_player="p1",
                        membership=True, issuer_current_gm=True,
                        issuer_subscribed=True, grant_active=True,
                        release_active=True, rights_allow=True,
                        resource_in_trusted_closure=True, current_epoch=True,
                        requested_action="campaign-use")
        self.assertTrue(access_decision(**baseline))
        for field in ("membership", "issuer_current_gm", "issuer_subscribed",
                      "grant_active", "release_active", "rights_allow",
                      "resource_in_trusted_closure", "current_epoch"):
            self.assertFalse(access_decision(**{**baseline, field: False}), field)
        self.assertFalse(access_decision(**{**baseline, "current_player": "p2"}))
        self.assertFalse(access_decision(**{**baseline, "requested_campaign": "cy"}))
        for forbidden in ("export-outside-campaign", "transfer-restricted-character",
                          "copy-protected-source", "mint-entitlement", "publish-content"):
            self.assertFalse(access_decision(**{**baseline, "requested_action": forbidden}))


if __name__ == "__main__":
    unittest.main(verbosity=2)
