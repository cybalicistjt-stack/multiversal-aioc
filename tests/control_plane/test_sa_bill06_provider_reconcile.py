#!/usr/bin/env python3
"""Adversarial integration tests: fake signed provider + real disposable PG16.

A green result validates test fixture behavior, NOT Google Play/Stripe,
authentic purchase receipts, real A3 sessions or installed Multiversal.
"""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import threading
import unittest
import psycopg
from psycopg import errors
from sa_bill06_provider_reconcile import (
    Reconciler, entitled, sign_synthetic, instant
)

ROOT=Path(__file__).resolve().parents[2]
SCHEMA=ROOT/"governance/research-evaluations/subscription-allowance-threats-2026-11-01/SA_BILL_06_DISPOSABLE_PROVIDER_SCHEMA.sql"
DSN=os.environ["SA_BILL05_TEST_DATABASE_URL"]
SECRET=b"synthetic-only-ci-secret-not-a-live-merchant-key"
T=1800000000
START="2026-10-01T00:00:00Z"
END="2026-12-01T00:00:00Z"

def snap(**fields):
    result=dict(provider="synthetic-provider",originId="orig-1",
       appId="fake-multiversal-app",environment="sandbox",
       providerAccountRef="mock-account-gm",productId="fake-sub-plan",
       revision=1,state="verified_active",entitledFrom=START,entitledUntil=END)
    result.update(fields)
    return result

class FakeProvider:
    def __init__(self):
        self.snapshots={"orig-1":snap()}
        self.calls=0
        self.error=None
        self.lock=threading.Lock()

    def fetch(self,origin):
        with self.lock:
            self.calls+=1
            error=self.error
            snapshot=self.snapshots.get(origin)
        if error:
            raise error
        if snapshot is None:
            raise LookupError("no such purchase")
        return deepcopy(snapshot)

class ProviderLedgerAdversarial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with psycopg.connect(DSN,autocommit=True) as db:
            db.execute(SCHEMA.read_text(encoding="utf-8"))
            server=db.execute("SHOW server_version_num").fetchone()[0]
            assert int(server)>=160000,server
            print("SA-BILL-06 real disposable PostgreSQL server",server)

    def setUp(self):
        with psycopg.connect(DSN,autocommit=True) as db:
            db.execute("DROP TRIGGER IF EXISTS sa06_block_event ON sa_bill06_fixture.notification_receipt")
            db.execute("""TRUNCATE sa_bill06_fixture.notification_receipt,
                        sa_bill06_fixture.billing_current,
                        sa_bill06_fixture.purchase_binding CASCADE""")
        self.provider=FakeProvider()
        self.bindings={"orig-1":("gm-subject","mock-account-gm")}
        self.client=Reconciler(DSN,provider="synthetic-provider",
            app="fake-multiversal-app",products={"fake-sub-plan"},
            environment="sandbox",secret=SECRET,
            fetch=self.provider.fetch,bindings=self.bindings)

    def deliver(self,event="e1",origin="orig-1",*,hint=None,signature=None,
                sent_at=T,now=T):
        payload=dict(eventId=event,originId=origin)
        if hint is not None:
            payload["statusHint"]=hint
        raw=json.dumps(payload,sort_keys=True).encode("utf-8")
        signed=sign_synthetic(SECRET,sent_at,raw) if signature is None else signature
        return self.client.process(raw,signed,sent_at,now)

    def rows(self,table):
        with psycopg.connect(DSN) as db:
            cur=db.execute("SELECT * FROM sa_bill06_fixture."+table)
            cols=[c.name for c in cur.description]
            return [dict(zip(cols,x)) for x in cur.fetchall()]

    def current(self):
        rows=self.rows("billing_current")
        self.assertEqual(len(rows),1)
        return rows[0]

    def test_01_valid_notification_fetches_authoritative_snapshot(self):
        self.assertEqual(self.deliver(),"APPLIED")
        row=self.current()
        self.assertEqual(row["state"],"verified_active")
        self.assertEqual(row["subject_id"],"gm-subject")
        self.assertEqual(row["revision"],1)
        self.assertTrue(entitled(row,"2026-11-01T00:00:00Z"))
        self.assertEqual(self.provider.calls,1)

    def test_02_invalid_signature_never_fetches_or_writes(self):
        self.assertEqual(self.deliver(signature="00"*32),"REJECTED_UNAUTHENTICATED")
        self.assertEqual(self.provider.calls,0)
        self.assertEqual(self.rows("purchase_binding"),[])

    def test_03_old_or_future_notification_exceeds_freshness(self):
        self.assertEqual(self.deliver(sent_at=T-301),"REJECTED_UNAUTHENTICATED")
        self.assertEqual(self.deliver(sent_at=T+301),"REJECTED_UNAUTHENTICATED")
        self.assertEqual(self.provider.calls,0)

    def test_04_wrong_app_environment_or_product_never_mints_state(self):
        for field,value in (("appId","another-app"),("environment","production"),
                            ("productId","unapproved-plan"),("provider","imposter")):
            self.provider.snapshots["orig-1"]=snap(**{field:value})
            self.assertEqual(self.deliver(event=field),"SOURCE_MISMATCH")
        self.assertEqual(self.rows("purchase_binding"),[])

    def test_05_signed_event_status_is_only_a_hint(self):
        self.provider.snapshots["orig-1"]=snap(state="revoked_refunded",revision=2)
        self.assertEqual(self.deliver(hint="verified_active"),"APPLIED")
        self.assertEqual(self.current()["state"],"revoked_refunded")
        self.assertFalse(entitled(self.current(),"2026-11-01T00:00:00Z"))

    def test_06_duplicate_event_is_idempotent(self):
        self.assertEqual(self.deliver(),"APPLIED")
        self.assertEqual(self.deliver(),"DUPLICATE")
        self.assertEqual(len(self.rows("notification_receipt")),1)
        self.assertEqual(self.current()["source_epoch"],1)

    def test_06b_duplicate_delivery_still_applies_fresher_provider_revocation(self):
        self.assertEqual(self.deliver(event="same-hint"),"APPLIED")
        self.provider.snapshots["orig-1"]=snap(revision=2,state="revoked_refunded")
        self.assertEqual(self.deliver(event="same-hint"),"SOURCE_REFRESHED")
        self.assertEqual(self.current()["state"],"revoked_refunded")
        self.assertEqual(self.current()["source_epoch"],2)
        self.assertEqual(len(self.rows("notification_receipt")),1)
        self.assertEqual(sorted(r["revision"] for r in self.rows("source_revision_audit")),[1,2])

    def test_07_same_event_id_different_signed_payload_is_rejected(self):
        self.assertEqual(self.deliver(),"APPLIED")
        self.assertEqual(self.deliver(hint="bogus"),"EVENT_ID_CONFLICT")
        self.assertEqual(self.current()["source_epoch"],1)
        self.assertEqual(len(self.rows("notification_receipt")),1)

    def test_08_out_of_order_notifications_cannot_restore_older_entitlement(self):
        self.provider.snapshots["orig-1"]=snap(revision=7,state="revoked_refunded")
        self.assertEqual(self.deliver(event="newer"),"APPLIED")
        self.provider.snapshots["orig-1"]=snap(revision=3,state="verified_active")
        self.assertEqual(self.deliver(event="older"),"STALE_SOURCE")
        self.assertEqual(self.current()["revision"],7)
        self.assertEqual(self.current()["state"],"revoked_refunded")
        self.assertEqual(self.current()["source_epoch"],1)

    def test_09_cancelled_paid_term_then_grace_then_hold(self):
        self.provider.snapshots["orig-1"]=snap(revision=1,state="cancel_scheduled")
        self.assertEqual(self.deliver(event="cancel"),"APPLIED")
        self.assertTrue(entitled(self.current(),"2026-11-30T23:59:59Z"))
        self.assertFalse(entitled(self.current(),"2026-12-01T00:00:00Z"))
        self.provider.snapshots["orig-1"]=snap(revision=2,state="grace_entitled",
            entitledUntil="2026-12-03T00:00:00Z")
        self.assertEqual(self.deliver(event="grace"),"APPLIED")
        self.assertTrue(entitled(self.current(),"2026-12-02T00:00:00Z"))
        self.provider.snapshots["orig-1"]=snap(revision=3,state="account_hold",
            entitledUntil="2026-12-03T00:00:00Z")
        self.assertEqual(self.deliver(event="hold"),"APPLIED")
        self.assertFalse(entitled(self.current(),"2026-12-02T00:00:00Z"))
        self.assertEqual(self.current()["source_epoch"],3)

    def test_10_provider_outage_never_mints_entitlement(self):
        self.provider.error=ConnectionError("synthetic provider timeout")
        self.assertEqual(self.deliver(),"SOURCE_UNAVAILABLE")
        self.assertEqual(self.rows("purchase_binding"),[])
        self.provider.error=None
        self.assertEqual(self.deliver(),"APPLIED")

    def test_11_refuse_unknown_purchase_and_subject_swap(self):
        self.assertEqual(self.deliver(origin="missing"),"SOURCE_UNAVAILABLE")
        self.assertEqual(self.deliver(),"APPLIED")
        # A stolen client account ID must not overwrite existing purchase bond.
        self.bindings["orig-1"]=("attacker-subject","mock-account-gm")
        self.assertEqual(self.deliver(event="swap"),"BINDING_CONFLICT")
        self.assertEqual(self.current()["subject_id"],"gm-subject")

    def test_12_noncanonical_or_invalid_source_revision_does_not_write(self):
        for revision in (0,-1,"2",None,True):
            self.provider.snapshots["orig-1"]=snap(revision=revision)
            self.assertEqual(self.deliver(event="bad"+str(revision)),"SOURCE_MISMATCH")
        self.assertEqual(self.rows("purchase_binding"),[])

    def test_13_synthetic_source_dates_are_normalized_and_validated(self):
        self.provider.snapshots["orig-1"]=snap(entitledUntil="2026-11-01T00:00:00+02:00")
        self.assertEqual(self.deliver(),"APPLIED")
        self.assertFalse(entitled(self.current(),"2026-10-31T23:00:00Z"))
        self.assertEqual(instant("2026-11-01T00:00:00+02:00"),
                         instant("2026-10-31T22:00:00Z"))

    def test_14_invalid_or_reversed_interval_denies_instead_of_expires_forever(self):
        for end in ("nonsense",START,None):
            self.provider.snapshots["orig-1"]=snap(entitledUntil=end)
            self.assertEqual(self.deliver(event="bad"+str(end)),"SOURCE_MISMATCH")
        self.assertEqual(self.rows("billing_current"),[])

    def test_15_real_sql_failure_rolls_back_purchase_binding_and_projection(self):
        with psycopg.connect(DSN,autocommit=True) as db:
            db.execute("""CREATE OR REPLACE FUNCTION sa_bill06_fixture.raise_on_event()
              RETURNS trigger LANGUAGE plpgsql AS $$
              BEGIN IF NEW.notification_id='fail-commit' THEN
                  RAISE EXCEPTION 'injected audit-write failure';
                END IF;
                RETURN NEW;
              END $$""")
            db.execute("""CREATE TRIGGER sa06_block_event BEFORE INSERT
              ON sa_bill06_fixture.notification_receipt
              FOR EACH ROW EXECUTE FUNCTION sa_bill06_fixture.raise_on_event()""")
        with self.assertRaises(psycopg.errors.RaiseException):
            self.deliver(event="fail-commit")
        self.assertEqual(self.rows("purchase_binding"),[])
        self.assertEqual(self.rows("billing_current"),[])
        self.assertEqual(self.rows("notification_receipt"),[])
        self.assertEqual(self.rows("source_revision_audit"),[])

    def test_16_concurrent_distinct_events_same_latest_source_one_revision(self):
        def deliver_num(i):
            return self.deliver(event="thread-"+str(i))
        with ThreadPoolExecutor(max_workers=12) as pool:
            out=list(pool.map(deliver_num,range(30)))
        self.assertEqual(out.count("APPLIED"),1,out)
        self.assertEqual(out.count("STALE_SOURCE"),29,out)
        self.assertEqual(self.current()["source_epoch"],1)
        self.assertEqual(len(self.rows("notification_receipt")),30)
        self.assertEqual(len(self.rows("purchase_binding")),1)

    def test_17_distinct_purchases_have_distinct_owner_binding(self):
        self.provider.snapshots["orig-2"]=snap(originId="orig-2",
             providerAccountRef="mock-account-p2",revision=1)
        self.bindings["orig-2"]=("subject-p2","mock-account-p2")
        self.assertEqual(self.deliver(event="gm"),"APPLIED")
        self.assertEqual(self.deliver(event="p2",origin="orig-2"),"APPLIED")
        self.assertEqual(len(self.rows("purchase_binding")),2)
        self.assertEqual({r["subject_id"] for r in self.rows("billing_current")},
                         {"gm-subject","subject-p2"})

    def test_18_unapproved_pending_or_expired_purchase_not_premium(self):
        for state,rev in (("pending_purchase",1),("expired",2),("revoked_refunded",3)):
            self.provider.snapshots["orig-1"]=snap(state=state,revision=rev)
            self.assertEqual(self.deliver(event=state),"APPLIED")
            self.assertFalse(entitled(self.current(),"2026-11-01T00:00:00Z"))

if __name__=="__main__":
    unittest.main(verbosity=2)
