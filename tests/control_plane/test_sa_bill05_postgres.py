#!/usr/bin/env python3
"""SA-BILL-05: disposable PostgreSQL 16 transactional research.

Requires a genuinely running isolated PostgreSQL service and psycopg 3.
The fixture contains fake account/receipt/content records only. This is NOT
the shipping Multiversal service, store purchase verification, external A3
identity proof, licensed asset test, or installed native security acceptance.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import hashlib
import os
from pathlib import Path
import random
import time
import unittest

import psycopg
from psycopg import errors

ROOT = Path(__file__).resolve().parents[2]
DDL = ROOT / "governance/research-evaluations/subscription-allowance-threats-2026-11-01/SA_BILL_03_POSTGRESQL_REFERENCE.sql"
DSN = os.environ.get("SA_BILL05_TEST_DATABASE_URL")
SCHEMA = "sa_bill03_reference"


class Aborted(Exception):
    def __init__(self, reason: str):
        self.reason = reason


def connect(*, autocommit=False):
    if not DSN or ("localhost" not in DSN and "127.0.0.1" not in DSN):
        raise RuntimeError("Explicit loopback disposable SA_BILL05_TEST_DATABASE_URL is required")
    return psycopg.connect(DSN, autocommit=autocommit, connect_timeout=10)


def count(table, where="TRUE", values=()):
    # table and where are static strings from the test source, never user input.
    with connect() as conn:
        return conn.execute(
            "SELECT count(*) FROM " + SCHEMA + "." + table + " WHERE " + where, values
        ).fetchone()[0]


def prepare():
    with connect(autocommit=True) as conn:
        conn.execute(DDL.read_text(encoding="utf-8"))
        conn.execute(
            "TRUNCATE " + ", ".join(SCHEMA + "." + t for t in (
                "allowance_immutable_event", "allowance_command_receipt",
                "campaign_allowance_slot", "billing_event_dedupe",
                "purchase_subject_binding", "registered_content_root",
                "campaign_membership", "verified_subscription",
            )) + " RESTART IDENTITY CASCADE"
        )
        conn.execute("""
            INSERT INTO sa_bill03_reference.verified_subscription
            (subscription_source_id,canonical_payer_subject_id,provider,
             provider_product_id,provider_revision,state,entitled_from,
             entitled_until,provider_checked_at,source_epoch)
            VALUES ('sub-gm','gm','synthetic-store','fictitious-plan',4,
            'verified_active',now()-interval '1 day',now()+interval '1 day',now(),1)
        """)
        conn.execute("""
            INSERT INTO sa_bill03_reference.registered_content_root
            (content_release_id,immutable_source_digest,root_kind,
             content_owner_revision,active,owner_authorized_as_grant_root,
             dependency_closure_digest)
            VALUES ('setting','synthetic-source','custom-setting',1,true,true,'closure-v1')
        """)


def seed_campaign(campaign, player):
    with connect() as conn:
        for subject, role in (("gm", "gm"), (player, "player")):
            conn.execute("""
                INSERT INTO sa_bill03_reference.campaign_membership
                (campaign_id,subject_id,role,active,owner_revision)
                VALUES (%s,%s,%s,true,1)
            """, (campaign, subject, role))


def issue(*, campaign, player, command_id, payload="setting",
          expected_source_revision=4, audit_type="issued", max_attempts=24):
    """Research-only owner-DB command; data is seeded synthetic local truth.

    The producer must provide a valid A3/session subject and verified
    billing/rights revisions in production, unlike this fixture.
    """
    digest = hashlib.sha256(
        f"{campaign}|{player}|gm|{payload}".encode("utf-8")
    ).hexdigest()
    for attempt in range(max_attempts):
        try:
            with connect() as conn:
                conn.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")
                cur = conn.cursor()
                # Rows are locked in deterministic subscription -> membership ->
                # release order; no client boolean can authorize this SQL path.
                bill = cur.execute("""
                    SELECT canonical_payer_subject_id,provider_revision,state,
                           entitled_from,entitled_until,provider_checked_at,revoked_at
                    FROM sa_bill03_reference.verified_subscription
                    WHERE subscription_source_id='sub-gm' FOR SHARE
                """).fetchone()
                if not bill or bill[0] != "gm" or bill[1] != expected_source_revision or (
                    bill[2] not in ("verified_active", "cancel_scheduled")
                ) or bill[6] is not None:
                    return "DENIED_BILLING"
                if not (bill[3] <= datetime.now(bill[3].tzinfo) < bill[4]):
                    return "DENIED_BILLING"
                if datetime.now(bill[5].tzinfo) - bill[5] > __import__("datetime").timedelta(hours=1):
                    return "DENIED_SOURCE_STALE"

                roles = cur.execute("""
                    SELECT subject_id,role,active FROM sa_bill03_reference.campaign_membership
                    WHERE campaign_id=%s AND subject_id=ANY(%s)
                    ORDER BY subject_id FOR SHARE
                """, (campaign, ["gm", player])).fetchall()
                mapped = {subject: (role, active) for subject, role, active in roles}
                if (mapped.get("gm") != ("gm", True) or
                    mapped.get(player) != ("player", True)):
                    return "DENIED_MEMBERSHIP"

                # Command IDs are bound to a durable digest, before a caller
                # can change the target to hide a replay attempt.
                existing = cur.execute("""
                    SELECT payload_sha256 FROM sa_bill03_reference.allowance_command_receipt
                    WHERE command_id=%s
                """, (command_id,)).fetchone()
                if existing:
                    return "IDEMPOTENT" if existing[0] == digest else "COMMAND_ID_CONFLICT"

                root = cur.execute("""
                    SELECT root_kind,active,owner_authorized_as_grant_root,
                           dependency_closure_digest
                    FROM sa_bill03_reference.registered_content_root
                    WHERE content_release_id=%s FOR SHARE
                """, (payload,)).fetchone()
                if root != ("custom-setting", True, True, "closure-v1"):
                    return "DENIED_REGISTERED_RIGHTS"

                row = cur.execute("""
                    INSERT INTO sa_bill03_reference.campaign_allowance_slot
                    (campaign_id,player_subject_id,issuer_gm_subject_id,
                     root_release_id,pinned_closure_digest,status,grant_epoch,
                     issuer_subscription_source_id,created_at,updated_at)
                    VALUES (%s,%s,'gm','setting','closure-v1','active',1,
                            'sub-gm',now(),now())
                    ON CONFLICT (campaign_id,player_subject_id,slot_kind)
                    DO NOTHING RETURNING grant_epoch
                """, (campaign,player)).fetchone()
                if row is None:
                    # No money or command record minted by this failed claim.
                    return "SLOT_CONFLICT"

                cur.execute("""
                    INSERT INTO sa_bill03_reference.allowance_command_receipt
                    (command_id,canonical_actor_subject_id,payload_sha256,
                     campaign_id,player_subject_id,accepted_epoch,result_code,occurred_at)
                    VALUES (%s,'gm',%s,%s,%s,1,'ISSUED',now())
                """, (command_id,digest,campaign,player))
                cur.execute("""
                    INSERT INTO sa_bill03_reference.allowance_immutable_event
                    (event_id,command_id,campaign_id,player_subject_id,event_type,
                     new_epoch,trusted_owner_revision_digest,event_at)
                    VALUES (%s,%s,%s,%s,%s,1,'synthetic-owner-rev-1',now())
                """, ("event:"+command_id,command_id,campaign,player,audit_type))
                return "ISSUED"
        except (errors.SerializationFailure, errors.DeadlockDetected):
            # Bounded retry of a genuine PostgreSQL conflict; NEVER replay
            # an ambiguous provider charge or blindly retry nonidempotent I/O.
            if attempt + 1 == max_attempts:
                raise
            time.sleep(min(0.004 * (attempt + 1) + random.uniform(0, 0.008), 0.08))
    raise AssertionError("unexpected retry loop completion")


class PostgresTransactionalProof(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        prepare()
        with connect() as conn:
            version = conn.execute("SHOW server_version_num").fetchone()[0]
        assert int(version) >= 150000, version
        print("SA-BILL-05 real PostgreSQL engine version", version)

    def test_01_forty_cross_connection_competing_requests_one_winner(self):
        seed_campaign("race", "player-race")
        def attempt(i):
            return issue(campaign="race", player="player-race",
                         command_id=f"race-{i}")
        with ThreadPoolExecutor(max_workers=12) as pool:
            outcomes = list(pool.map(attempt, range(40)))
        self.assertEqual(outcomes.count("ISSUED"), 1, outcomes)
        self.assertEqual(outcomes.count("SLOT_CONFLICT"), 39, outcomes)
        self.assertEqual(count("campaign_allowance_slot",
                               "campaign_id='race' AND player_subject_id='player-race'"), 1)
        self.assertEqual(count("allowance_command_receipt", "campaign_id='race'"), 1)
        self.assertEqual(count("allowance_immutable_event", "campaign_id='race'"), 1)

    def test_02_same_command_is_idempotent_changed_payload_conflicts(self):
        seed_campaign("idem", "p-idem")
        args = dict(campaign="idem",player="p-idem",command_id="idem-command")
        self.assertEqual(issue(**args), "ISSUED")
        self.assertEqual(issue(**args), "IDEMPOTENT")
        self.assertEqual(issue(**args,payload="different-root"), "COMMAND_ID_CONFLICT")
        self.assertEqual(count("allowance_immutable_event", "campaign_id='idem'"), 1)

    def test_03_audit_failure_rolls_back_slot_and_command(self):
        seed_campaign("audit", "p-audit")
        with self.assertRaises(errors.CheckViolation):
            issue(campaign="audit",player="p-audit",command_id="audit-invalid",
                  audit_type="unsupported-type")
        self.assertEqual(count("campaign_allowance_slot", "campaign_id='audit'"), 0)
        self.assertEqual(count("allowance_command_receipt", "campaign_id='audit'"), 0)
        self.assertEqual(count("allowance_immutable_event", "campaign_id='audit'"), 0)

    def test_04_recipient_and_issuer_membership_is_checked_on_commit(self):
        seed_campaign("membership", "p-member")
        with connect() as conn:
            conn.execute("""UPDATE sa_bill03_reference.campaign_membership
                            SET active=false, owner_revision=owner_revision+1
                            WHERE campaign_id='membership' AND subject_id='p-member'""")
        self.assertEqual(issue(campaign="membership",player="p-member",
                               command_id="invalid-member"), "DENIED_MEMBERSHIP")
        self.assertEqual(count("campaign_allowance_slot",
                               "campaign_id='membership'"), 0)

    def test_11_gm_entitlement_source_revocation_fences_issuance(self):
        seed_campaign("gm-off", "p-gm")
        with connect() as conn:
            conn.execute("""UPDATE sa_bill03_reference.verified_subscription
                            SET state='expired',source_epoch=source_epoch+1,
                            provider_revision=5,provider_checked_at=now()
                            WHERE subscription_source_id='sub-gm'""")
        self.assertEqual(issue(campaign="gm-off",player="p-gm",
                               command_id="gm-expired"), "DENIED_BILLING")
        self.assertEqual(count("campaign_allowance_slot","campaign_id='gm-off'"),0)
        # Never rewind a provider revision: this test runs last and retains
        # a monotonically incremented, expired synthetic source row.

    def test_06_same_player_two_campaigns_and_two_players_same_campaign(self):
        for campaign,player in (("A","p1"),("B","p1"),("A","p2")):
            if (campaign,player)==("A","p2"):
                with connect() as conn:
                    conn.execute("""INSERT INTO sa_bill03_reference.campaign_membership
                        (campaign_id,subject_id,role,active,owner_revision)
                        VALUES ('A','p2','player',true,1)""")
            else:
                seed_campaign(campaign,player)
            self.assertEqual(issue(campaign=campaign,player=player,
                                   command_id=f"{campaign}:{player}"), "ISSUED")
        self.assertEqual(count("campaign_allowance_slot",
                               "campaign_id IN ('A','B')"),3)

    def test_07_purchase_identity_cannot_bind_to_two_accounts(self):
        with connect() as conn:
            conn.execute("""INSERT INTO sa_bill03_reference.purchase_subject_binding
                 (provider,purchase_origin_id,canonical_payer_subject_id,bound_at)
                 VALUES ('fake-store','original-purchase','gm',now())""")
        with self.assertRaises(errors.UniqueViolation):
            with connect() as conn:
                conn.execute("""INSERT INTO sa_bill03_reference.purchase_subject_binding
                    (provider,purchase_origin_id,canonical_payer_subject_id,bound_at)
                    VALUES ('fake-store','original-purchase','other',now())""")
        self.assertEqual(count("purchase_subject_binding",
                               "purchase_origin_id='original-purchase'"),1)

    def test_08_duplicate_provider_event_not_replayed(self):
        with connect() as conn:
            conn.execute("""INSERT INTO sa_bill03_reference.billing_event_dedupe
                (provider,provider_event_id,purchase_origin_id,
                 canonical_payer_subject_id,raw_event_sha256,source_revision,
                 first_observed_at)
                VALUES ('fake-store','event-1','original-purchase','gm','hash-1',1,now())""")
        with self.assertRaises(errors.UniqueViolation):
            with connect() as conn:
                conn.execute("""INSERT INTO sa_bill03_reference.billing_event_dedupe
                  (provider,provider_event_id,purchase_origin_id,
                   canonical_payer_subject_id,raw_event_sha256,source_revision,
                   first_observed_at)
                  VALUES ('fake-store','event-1','original-purchase','gm','hash-2',2,now())""")
        self.assertEqual(count("billing_event_dedupe","provider_event_id='event-1'"),1)

    def test_09_direct_unique_slot_insert_is_blocked_at_database(self):
        with self.assertRaises(errors.UniqueViolation):
            with connect() as conn:
                conn.execute("""INSERT INTO sa_bill03_reference.campaign_allowance_slot
                    (campaign_id,player_subject_id,issuer_gm_subject_id,root_release_id,
                    pinned_closure_digest,status,issuer_subscription_source_id,
                    created_at,updated_at)
                    VALUES ('A','p1','gm','setting','closure-v1','active',
                            'sub-gm',now(),now())""")
        self.assertEqual(count("campaign_allowance_slot",
                               "campaign_id='A' AND player_subject_id='p1'"),1)

    def test_10_expired_rights_rejects_new_grants(self):
        seed_campaign("rights", "p-rights")
        with connect() as conn:
            conn.execute("""UPDATE sa_bill03_reference.registered_content_root
                            SET active=false,content_owner_revision=2
                            WHERE content_release_id='setting'""")
        self.assertEqual(issue(campaign="rights",player="p-rights",
                               command_id="bad-rights"), "DENIED_REGISTERED_RIGHTS")
        self.assertEqual(count("campaign_allowance_slot","campaign_id='rights'"),0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
