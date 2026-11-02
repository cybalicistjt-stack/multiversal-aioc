"""SA-BILL-06 disposable research: synthetic HMAC and fake provider lookup.

NOT a Google Play RTDN verifier, Stripe adapter, deployed backend, A3
authentication implementation or real billing. No payments can be made.
"""
from datetime import datetime, timezone
import hashlib
import hmac
import json
import time
from urllib.parse import urlparse
import psycopg
from psycopg import errors

STATES = {"verified_active", "cancel_scheduled", "grace_entitled", "account_hold",
          "expired", "revoked_refunded", "pending_purchase", "trial_verified"}

def instant(value):
    if not isinstance(value, str) or "T" not in value:
        raise ValueError("explicit ISO instant required")
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("timezone required")
    return dt.astimezone(timezone.utc)

def sign_synthetic(secret, sent_at, raw):
    # Synthetic provider HMAC ONLY, not actual Play Pub/Sub authentication.
    return hmac.new(secret, str(sent_at).encode()+b"."+raw, hashlib.sha256).hexdigest()

def decode(raw, signature, sent_at, now, secret):
    if type(sent_at) is not int or abs(now-sent_at)>300:
        raise ValueError("expired webhook")
    if not isinstance(raw, bytes) or len(raw)>16384:
        raise ValueError("malformed webhook bytes")
    expected=sign_synthetic(secret,sent_at,raw)
    if not isinstance(signature,str) or not hmac.compare_digest(signature,expected):
        raise ValueError("invalid synthetic signature")
    try:
        event=json.loads(raw.decode("utf-8"))
    except (ValueError,UnicodeError) as exc:
        raise ValueError("bad notification document") from exc
    if not isinstance(event,dict):
        raise ValueError("event must be object")
    for field in ("eventId","originId"):
        if not isinstance(event.get(field),str) or not 1<=len(event[field])<=120:
            raise ValueError("missing event identity")
    return event

def normalize(snapshot, origin, *, provider, app, products, environment, bindings):
    # Only a *trusted server* may construct bindings from A3 account proofs;
    # this study passes synthetic bindings in memory, not from API callers.
    if not isinstance(snapshot,dict) or origin not in bindings:
        raise ValueError("unowned purchase")
    subject,provider_ref=bindings[origin]
    values={"provider":provider,"originId":origin,"appId":app,
            "environment":environment,"providerAccountRef":provider_ref}
    if any(snapshot.get(k)!=v for k,v in values.items()):
        raise ValueError("mismatched source or provider account")
    if snapshot.get("productId") not in products or snapshot.get("state") not in STATES:
        raise ValueError("unapproved SKU/state")
    if type(snapshot.get("revision")) is not int or snapshot["revision"]<1:
        raise ValueError("non-monotonic source revision")
    start,end=instant(snapshot.get("entitledFrom")),instant(snapshot.get("entitledUntil"))
    if end<=start:
        raise ValueError("invalid interval")
    return dict(subject=subject,ref=provider_ref,provider=provider,origin=origin,
                product=snapshot["productId"],revision=snapshot["revision"],
                state=snapshot["state"],start=start,end=end)

def entitled(row, at):
    now=instant(at)
    return row["state"] in ("verified_active","cancel_scheduled","grace_entitled") and (
        row["entitled_from"]<=now<row["entitled_until"]
    )

class Reconciler:
    def __init__(self,dsn, *, provider, app, products, environment, secret, fetch, bindings):
        u=urlparse(dsn)
        if u.scheme not in ("postgresql","postgres") or u.hostname not in ("localhost","127.0.0.1"):
            raise ValueError("only disposable loopback database permitted")
        self.dsn=dsn
        self.provider=provider
        self.app=app
        self.products=frozenset(products)
        self.environment=environment
        self.secret=secret
        self.fetch=fetch
        self.bindings=bindings

    def process(self,raw,signature,sent_at,now):
        try:
            event=decode(raw,signature,sent_at,now,self.secret)
        except ValueError:
            return "REJECTED_UNAUTHENTICATED"
        # Event contains NO authoritative price, state, payer or entitlement.
        try:
            snapshot=self.fetch(event["originId"])
        except (LookupError,ConnectionError,TimeoutError):
            return "SOURCE_UNAVAILABLE"
        try:
            normalized=normalize(snapshot,event["originId"],provider=self.provider,
                app=self.app,products=self.products,environment=self.environment,
                bindings=self.bindings)
        except (ValueError,TypeError,OverflowError):
            return "SOURCE_MISMATCH"
        digest=hashlib.sha256(raw).hexdigest()
        for attempt in range(20):
            try:
                with psycopg.connect(self.dsn,connect_timeout=8) as conn:
                    conn.execute("SET TRANSACTION ISOLATION LEVEL SERIALIZABLE")
                    old=conn.execute("""
                        SELECT body_sha256 FROM sa_bill06_fixture.notification_receipt
                        WHERE provider=%s AND notification_id=%s
                    """,(self.provider,event["eventId"])).fetchone()
                    if old:
                        return "DUPLICATE" if old[0]==digest else "EVENT_ID_CONFLICT"
                    conn.execute("""
                        INSERT INTO sa_bill06_fixture.purchase_binding
                        (provider,origin_id,subject_id,provider_account_ref)
                        VALUES (%s,%s,%s,%s)
                        ON CONFLICT(provider,origin_id) DO NOTHING
                    """,(self.provider,normalized["origin"],normalized["subject"],normalized["ref"]))
                    binding=conn.execute("""
                        SELECT subject_id,provider_account_ref
                        FROM sa_bill06_fixture.purchase_binding
                        WHERE provider=%s AND origin_id=%s FOR UPDATE
                    """,(self.provider,normalized["origin"])).fetchone()
                    if binding!=(normalized["subject"],normalized["ref"]):
                        return "BINDING_CONFLICT"
                    prev=conn.execute("""
                        SELECT revision,source_epoch FROM sa_bill06_fixture.billing_current
                        WHERE provider=%s AND origin_id=%s FOR UPDATE
                    """,(self.provider,normalized["origin"])).fetchone()
                    if prev is None or normalized["revision"]>prev[0]:
                        epoch=prev[1]+1 if prev else 1
                        conn.execute("""
                            INSERT INTO sa_bill06_fixture.billing_current
                            (provider,origin_id,subject_id,provider_account_ref,
                            app_id,product_id,environment,revision,state,
                            entitled_from,entitled_until,source_epoch,updated_at)
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())
                            ON CONFLICT(provider,origin_id) DO UPDATE SET
                            revision=EXCLUDED.revision,state=EXCLUDED.state,
                            entitled_from=EXCLUDED.entitled_from,
                            entitled_until=EXCLUDED.entitled_until,
                            source_epoch=EXCLUDED.source_epoch,updated_at=EXCLUDED.updated_at
                            WHERE sa_bill06_fixture.billing_current.revision<EXCLUDED.revision
                        """,(self.provider,normalized["origin"],normalized["subject"],
                             normalized["ref"],self.app,normalized["product"],
                             self.environment,normalized["revision"],normalized["state"],
                             normalized["start"],normalized["end"],epoch))
                        outcome="APPLIED"
                    else:
                        outcome="STALE_SOURCE"
                    conn.execute("""
                        INSERT INTO sa_bill06_fixture.notification_receipt
                        (provider,notification_id,origin_id,body_sha256,
                         projection_revision,apply_result)
                        VALUES (%s,%s,%s,%s,%s,%s)
                    """,(self.provider,event["eventId"],normalized["origin"],digest,
                         normalized["revision"],outcome))
                    return outcome
            except (errors.SerializationFailure,errors.DeadlockDetected,errors.UniqueViolation):
                if attempt==19:
                    raise
                time.sleep(min(0.002*(attempt+1),0.04))
        raise AssertionError("unreachable")
