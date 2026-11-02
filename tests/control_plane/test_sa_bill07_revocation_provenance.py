#!/usr/bin/env python3
"""SA-BILL-07: disposable PostgreSQL campaign/right/revocation policy tests.

Tests a local SQL FUNCTION against seeded role, subscription and release facts.
It does NOT authenticate A3 sessions, implement production A5/GM owners, test
real REST/WSS/search/AI endpoints, or enforce DB role isolation/RLS. A backend
must not expose raw tables to untrusted clients. No live subscription charged.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import unittest
from urllib.parse import urlparse

import psycopg

REPO=Path(__file__).resolve().parents[2]
DDL=REPO/"governance/research-evaluations/subscription-allowance-threats-2026-11-01/SA_BILL_07_DISPOSABLE_SCOPE_SCHEMA.sql"
DSN=os.environ.get("SA_BILL05_TEST_DATABASE_URL","")
URL=urlparse(DSN)
if URL.scheme not in ("postgresql","postgres") or URL.hostname not in ("localhost","127.0.0.1"):
    raise RuntimeError("Only explicit disposable loopback PostgreSQL is allowed")


def conn(*,autocommit=False):
    return psycopg.connect(DSN,connect_timeout=10,autocommit=autocommit)


def reset():
    with conn(autocommit=True) as db:
        db.execute(DDL.read_text())
        db.execute("""
            TRUNCATE sa_bill07_fixture.resource_dependency,
              sa_bill07_fixture.resource,sa_bill07_fixture.allowance_slot,
              sa_bill07_fixture.registered_closure,sa_bill07_fixture.registered_release,
              sa_bill07_fixture.membership,sa_bill07_fixture.issuer_entitlement CASCADE
        """)
    with conn() as db:
        db.executemany("""
          INSERT INTO sa_bill07_fixture.membership
          (campaign_id,subject_id,role,active,revision) VALUES(%s,%s,%s,true,1)
        """,[
          ("X","gm","gm"),("X","p1","player"),("X","p2","player"),
          ("Y","gm","gm"),("Y","p1","player"),
        ])
        db.execute("""
          INSERT INTO sa_bill07_fixture.issuer_entitlement
          (issuer_subject_id,state,source_verified,source_revision,checked_at,
            entitled_from,entitled_until)
          VALUES ('gm','verified_active',true,1,now(),now()-interval '1 day',
            now()+interval '1 day')
        """)
        db.executemany("""
          INSERT INTO sa_bill07_fixture.registered_release
          (id,version,owner_revision,active,rights_valid,closure_digest)
          VALUES(%s,'v1',1,true,true,'digest-setting-v1')
        """,[("setting",),("relic",),("tree",),("foreign",)])
        db.executemany("""
          INSERT INTO sa_bill07_fixture.registered_closure
          (root_release_id,permitted_release_id,owner_revision,closure_digest)
          VALUES ('setting',%s,1,'digest-setting-v1')
        """,[("setting",),("relic",),("tree",)])
        db.execute("""
          INSERT INTO sa_bill07_fixture.allowance_slot
          (campaign_id,player_subject_id,issuer_gm_subject_id,root_release_id,
           root_owner_revision,closure_digest,grant_epoch,issuer_membership_revision,
           player_membership_revision,issuer_entitlement_revision,state)
          VALUES ('X','p1','gm','setting',1,'digest-setting-v1',4,1,1,1,'active')
        """)
        db.executemany("""
          INSERT INTO sa_bill07_fixture.resource
          (id,campaign_id,owner_subject_id,source_release_id,
           safe_label,protected_payload,self_authored_raw_note)
          VALUES(%s,%s,%s,%s,%s,%s,%s)
        """,[
          ("char","X","p1",None,"Personal Hero","restricted character body","I wrote this biography"),
          ("sword","X","gm","relic","Sponsored Sword","secret licensed item bytes",""),
          ("tree-choice","X","gm","tree","Ability choice","secret ability bytes",""),
          ("foreign-item","X","gm","foreign","Unrelated premium","secret unrelated source",""),
          ("y-item","Y","gm","relic","Y-only item","campaign Y secret",""),
          ("other-char","X","p2",None,"Other Player Hero","private PC notes","p2 own original text"),
        ])
        db.executemany("""
          INSERT INTO sa_bill07_fixture.resource_dependency(parent_id,child_id)
          VALUES (%s,%s)
        """,[("char","sword"),("sword","tree-choice")])


def authorized(resource="char",*,campaign="X",subject="p1",action="campaign-read",epoch=4):
    with conn() as db:
        return db.execute(
          "SELECT sa_bill07_fixture.protected_use_authorized(%s,%s,%s,%s,%s)",
          (campaign,subject,resource,action,epoch)).fetchone()[0]


def project(resource="char",*,campaign="X",subject="p1",action="campaign-read",epoch=4):
    with conn() as db:
        return db.execute("""
          SELECT * FROM sa_bill07_fixture.safe_protected_projection(%s,%s,%s,%s,%s)
        """,(campaign,subject,resource,action,epoch)).fetchall()


def change(sql,*args):
    with conn() as db:
        db.execute(sql,args)


class RevocationAndLineage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with conn(autocommit=True) as db:
            version=db.execute("SHOW server_version_num").fetchone()[0]
        assert int(version)>=160000,version
        print("SA-BILL-07 PostgreSQL fixture engine",version)

    def setUp(self):
        reset()

    def test_01_baseline_one_campaign_root_and_nested_dependencies(self):
        self.assertTrue(authorized())
        self.assertEqual(project()[0][2],"restricted character body")
        self.assertTrue(authorized(action="campaign-use"))

    def test_02_gm_membership_revoked_denies_new_projections(self):
        change("UPDATE sa_bill07_fixture.membership SET active=false,revision=revision+1 WHERE campaign_id='X' AND subject_id='gm'")
        self.assertFalse(authorized())
        self.assertEqual(project(),[])

    def test_03_gm_demoted_but_still_member_does_not_issue_permission(self):
        change("UPDATE sa_bill07_fixture.membership SET role='player',revision=revision+1 WHERE campaign_id='X' AND subject_id='gm'")
        self.assertFalse(authorized())

    def test_04_billing_refund_after_allowance_denies_without_deleting_slot(self):
        change("UPDATE sa_bill07_fixture.issuer_entitlement SET state='revoked_refunded',source_revision=2 WHERE issuer_subject_id='gm'")
        self.assertFalse(authorized())
        with conn() as db:
            self.assertEqual(db.execute("SELECT count(*) FROM sa_bill07_fixture.allowance_slot").fetchone()[0],1)

    def test_05_newer_billing_epoch_requires_grant_revalidation(self):
        change("UPDATE sa_bill07_fixture.issuer_entitlement SET source_revision=2 WHERE issuer_subject_id='gm'")
        self.assertFalse(authorized())

    def test_06_player_membership_removed_denies_reuse(self):
        change("UPDATE sa_bill07_fixture.membership SET active=false,revision=2 WHERE campaign_id='X' AND subject_id='p1'")
        self.assertFalse(authorized())

    def test_07_player_identity_and_other_person_owned_character_not_shared(self):
        self.assertFalse(authorized(subject="p2"))
        self.assertFalse(authorized(resource="other-char"))

    def test_08_campaign_scope_does_not_bleed_to_other_campaign(self):
        self.assertFalse(authorized(campaign="Y"))
        self.assertFalse(authorized(resource="y-item",campaign="Y"))

    def test_09_suspended_grant_is_inert_but_record_retained(self):
        change("UPDATE sa_bill07_fixture.allowance_slot SET state='suspended' WHERE campaign_id='X' AND player_subject_id='p1'")
        self.assertFalse(authorized())
        with conn() as db:
            self.assertEqual(db.execute("SELECT state FROM sa_bill07_fixture.allowance_slot").fetchone()[0],"suspended")

    def test_10_old_epoch_token_denied_even_after_valid_grant_epoch_rotation(self):
        change("UPDATE sa_bill07_fixture.allowance_slot SET grant_epoch=5 WHERE campaign_id='X' AND player_subject_id='p1'")
        self.assertFalse(authorized(epoch=4))
        self.assertTrue(authorized(epoch=5))

    def test_11_revoked_nested_release_rights_denies_whole_character(self):
        change("UPDATE sa_bill07_fixture.registered_release SET rights_valid=false WHERE id='tree'")
        self.assertFalse(authorized())
        self.assertEqual(project(),[])

    def test_12_revision_changed_without_closure_reapproval_denies(self):
        change("UPDATE sa_bill07_fixture.registered_release SET owner_revision=2 WHERE id='relic'")
        self.assertFalse(authorized())

    def test_13_smuggling_unrelated_premium_dependency_denies(self):
        change("INSERT INTO sa_bill07_fixture.resource_dependency(parent_id,child_id) VALUES('sword','foreign-item')")
        self.assertFalse(authorized())

    def test_14_mixed_campaign_dependency_denies(self):
        change("INSERT INTO sa_bill07_fixture.resource_dependency(parent_id,child_id) VALUES('char','y-item')")
        self.assertFalse(authorized())

    def test_15_provenance_cycle_denies_instead_of_recursing_forever(self):
        change("INSERT INTO sa_bill07_fixture.resource_dependency(parent_id,child_id) VALUES('tree-choice','char')")
        self.assertFalse(authorized())

    def test_16_exports_transfers_and_publication_not_implicit_rights(self):
        for action in ("export-outside-campaign","transfer-character",
                       "copy-to-private-library","mint-entitlement","publish"):
            self.assertFalse(authorized(action=action),action)
            self.assertEqual(project(action=action),[])

    def test_17_search_counts_ai_and_wss_scope_follow_revocation(self):
        for action in ("search","ai","wss"):
            self.assertEqual(len(project(action=action)),1,action)
        change("UPDATE sa_bill07_fixture.allowance_slot SET state='revoked' WHERE campaign_id='X' AND player_subject_id='p1'")
        for action in ("search","ai","wss"):
            self.assertEqual(project(action=action),[],action)
        with conn() as db:
            count=db.execute("""SELECT count(*) FROM sa_bill07_fixture.resource r
              WHERE sa_bill07_fixture.protected_use_authorized('X','p1',r.id,'search',4)""").fetchone()[0]
            self.assertEqual(count,0)

    def test_18_separate_self_authored_note_is_recoverable_after_lapse(self):
        change("UPDATE sa_bill07_fixture.issuer_entitlement SET state='expired' WHERE issuer_subject_id='gm'")
        self.assertEqual(project(),[])
        with conn() as db:
            self.assertEqual(db.execute(
              "SELECT sa_bill07_fixture.recover_raw_note('p1','char')").fetchone()[0],
              "I wrote this biography")
            self.assertIsNone(db.execute(
              "SELECT sa_bill07_fixture.recover_raw_note('p2','char')").fetchone()[0])

    def test_19_old_source_timestamp_is_not_permanent_authority(self):
        change("UPDATE sa_bill07_fixture.issuer_entitlement SET checked_at=now()-interval '2 hours' WHERE issuer_subject_id='gm'")
        self.assertFalse(authorized())

    def test_20_missing_content_owner_or_dependency_digest_denies(self):
        change("UPDATE sa_bill07_fixture.registered_release SET closure_digest='changed' WHERE id='setting'")
        self.assertFalse(authorized())

    def test_21_unverified_billing_projection_denies_even_if_active(self):
        change("UPDATE sa_bill07_fixture.issuer_entitlement SET source_verified=false WHERE issuer_subject_id='gm'")
        self.assertFalse(authorized())

    def test_22_grace_issuance_policy_is_unselected_and_not_implicit_in_sql(self):
        change("UPDATE sa_bill07_fixture.issuer_entitlement SET state='grace_entitled' WHERE issuer_subject_id='gm'")
        self.assertFalse(authorized())

    def test_23_forbidden_api_action_does_not_appear_through_safe_projection(self):
        self.assertEqual(project(action="download-file-outside-campaign"),[])
        self.assertEqual(project(resource="missing"),[])

    def test_24_post_commit_revocation_fences_forty_fresh_transactions(self):
        # This proves only post-commit visibility, not interruption of a
        # preexisting read, disconnected cache, or an external A3 race.
        change("UPDATE sa_bill07_fixture.membership SET active=false,revision=2 WHERE campaign_id='X' AND subject_id='gm'")
        with ThreadPoolExecutor(max_workers=12) as pool:
            out=list(pool.map(lambda _: authorized(),range(40)))
        self.assertEqual(out,[False]*40)

if __name__=="__main__":
    unittest.main(verbosity=2)
