# SA-BILL-06 — Provider Truth, Replay and Cross-Account Binding

**Classification:** advisory security research and disposable synthetic provider / PostgreSQL integration tests. **Date:** 2026-11-01. **No activation of subscriptions, merchant account, price, live store, user payment, production grants or app endpoint changes.**

## Exact source context and scope

This stage builds on SA-BILL-01 threat inventory (60 proposed hostile scenarios), SA-BILL-03 actual-app evaluator characterization, SA-BILL-04 bounded entitlement model, and SA-BILL-05's tested disposable PostgreSQL issuance transaction.

In published app source `packages/contracts/src/identity-device/entitlement-evaluator.ts`, an `EntitlementEvaluationInput` carries records supplied by its caller; it does not itself prove payment or grant source authenticity. In the proposed design, **subscription, A3 role, Campaign membership and content license are separate authority checks**. The SA-BILL-06 laboratory models only the billing-source reconciliation boundary. Its synthetic in-process provider supplies data; it cannot prove store/API or A3 account authenticity.

Current [Google Play subscription lifecycle](https://developer.android.com/google/play/billing/lifecycle/subscriptions) documentation says backend purchase verification must fetch the latest state from `purchases.subscriptionsv2.get`; real-time developer notifications are a prompt to perform that lookup, not complete entitlement authority. Google Play Pub/Sub notifications and authentication are **not HMAC event payloads**. This laboratory deliberately uses an invented HMAC-signed fake provider as a **transport rejection exercise**, not an implementation or emulation of Play RTDN authentication. The provider-specific production adapter must authenticate Cloud Pub/Sub push identity or authorized delivery, use the real Developer API and correct purchase-token lifecycle, and verify linked account/product/app/environment. No Play credentials or provider sandbox are accessed here.

## Assets and trust seams

1. **External provider truth:** real provider answers about source purchase, original purchase identity, lifecycle state, verified entitlement period, revocation and account ownership. Here represented by isolated, mutable `FakeProvider.fetch()` **only**.
2. **Notification transport authenticity:** invented HMAC `sent_at + raw bytes` tests signature mismatch and bounded replay window. This neither models Cloud Pub/Sub OIDC authenticity nor proves a real vendor verifier.
3. **Canonical subject binding:** `(provider,original_purchase_id)` belongs to one A3 subject. The test maps fake external account references to synthetic subject IDs; production must use authenticated A3 possession and source-side purchase linkage, not a player-supplied recipient or shared device ID.
4. **Monotonic durable projection:** PostgreSQL `sa_bill06_fixture.billing_current` retains the highest verified source revision and increments its local entitlement source epoch for every newer projection. Neither a duplicated notification nor a lower revision may move status backwards.
5. **Two separate audit identities:** one durable `(provider,notification_id)` receipt and body hash per accepted notification, plus an immutable `(provider,origin_id,source_revision)` audit entry for **every changed provider projection**, including refresh triggered by a duplicate event. The body under one event ID cannot change. Receipt, purchase binding, projection and revision audit commit together.
6. **GM allowance issuance boundary:** only after verified provider state and fresh GM/Player role can the campaign allowance *separately* be issued, subject to SA-BILL-05's one-slot transaction. The tests here **do not** mint or spend an allowance, change Campaign assets, or authorize money.

## Test sources and exact claims

- `tests/control_plane/sa_bill06_provider_reconcile.py`: reference-only validation adapter, bounded HMAC webhook, fake provider `GET`, normalized offset-aware periods, provider/product/app/env/subject checks, source-revision monotonic PG update, receipt deduplication.
- `tests/control_plane/test_sa_bill06_provider_reconcile.py`: 18 tests with a genuinely running **disposable PostgreSQL 16** service, not SQLite or an in-memory DB. Includes up to 30 simultaneous notifications, wrong/duplicate IDs, competing account binding, invalid product/app/environments, malicious client state hints, provider timeout, cancelled paid access, provider grace/hold, refund replay, malformed dates, and audit-write rollback.
- `governance/research-evaluations/subscription-allowance-threats-2026-11-01/SA_BILL_06_DISPOSABLE_PROVIDER_SCHEMA.sql`: fixture-only three-table owner projection, unique provider purchase binding, monotonic subscription record, immutable per-event receipt.
- `.github/workflows/validate-sa-bill05-postgres.yml`: extends the existing disposable database CI with the SA-BILL-06 tests, so there is no extra production service or payment provider connection. Both the existing SA05 PostgreSQL and SA06 fake-provider tests need to pass at exact candidate head.

### Expected adversarial observables

| Vector | Proof oracle |
|---|---|
| Forged notification signature and stale delivery timestamp | Rejected **before provider fetch or DB mutation** |
| Validly signed notification with false `statusHint=active` | Authoritative fake provider `GET` returns refunded: persisted refunded, not hinted status |
| Wrong app, wrong store environment, unallowlisted SKU or provider | No subscription projection, binding or receipt |
| Retry same event ID/body, provider state unchanged | `DUPLICATE`; no extra source epoch or ledger record |
| Retry same event ID/body, provider state now revoked at a higher revision | `SOURCE_REFRESHED`; one existing event receipt, new immutable source-revision audit, updated denied entitlement |
| Same event ID, changed body | `EVENT_ID_CONFLICT` even if adversarial tester knows synthetic signing secret |
| Old event after newer source revision | `STALE_SOURCE`, no resurrection, historical receipt safe |
| Cancel scheduled, paid time still valid | Paid access valid through verified period end; no promise of renewal |
| Provider-confirmed grace then account hold | Entitlement only during confirmed grace; denied in hold |
| Provider API outage | No new entitlement/binding/receipt, status recoverable by later reconciliation |
| Purchase rebound to another A3 subject | Durable purchase binding rejects subject mismatch |
| Two distinct purchase identities | Distinct canonical subjects allowed after owner binding |
| Concurrent notifications for same latest revision | Single source epoch increment, one projection, one receipt per event |
| Receipt insert fails after projection update | PostgreSQL transaction rolls back *all* new records |
| Invalid dates / status / revision | No grant or permanent entitlement |

**No scenario should be promoted to an actual vendor penetration test.** These tests only demonstrate the fixture algorithms against fake provider data and the real temporary SQL engine.

## Important unproved boundary

A signed webhook does **not** establish a paid subscription. A notification may be replayed or arrive out of order, and a verified account binding must exist independently from caller intent. The owner billing adapter must query the current vendor API, verify the application ID, source product, original purchase token, linked payer, provider effective time and revision, and translate provider-specific lifecycle. Stripe-like signature design is not interchangeable with Google Play Pub/Sub OIDC delivery.

Even `SERIALIZABLE` in PostgreSQL does not atomically fence a remote provider that is revoked before its latest revision has reached local storage; live enforcement requires bounded provider freshness and A3/GM revision epochs, invalidation of derived permissions and fail-closed mutations on uncertain source. Subscription-only status can never authorize Campaign ownership, transfers or unrestricted content search/AI.

**Future gates:** real provider sandbox credentials (only with owner authorization); provider-specific push signature/OIDC and token ownership test; live A3 subject/GM-role revocation; end-to-end Campaign allowance transaction; source-rights/provenance through Characters, dependencies, exports and caches; installed Windows/Android offline key tests; independent consumer billing/price/terms review.

**No silent owner policy choices:** price and SKU; trial GM ability to grant; new grants during grace; GM replacement/succession; allowance replacement, durable offline lease and refunds remain unresolved. `operations/CURRENT.json`, PCV-03F, MTLC-14 and AXI-01 are unchanged; research branch has no product implementation authority.

## SA-BILL-06 RED → GREEN evidence and remaining source-version problem

A focused test was added for duplicate transport delivery after the fake provider changed its current result to `revoked_refunded`. On exact head `ceaad9b60408d1a4684a5afacdf8198c694031e6`, PostgreSQL run `41388132577` failed with **one expected functional assertion**: received `DUPLICATE` instead of expected `SOURCE_REFRESHED`. This was a real caught defect in the new **research reconciler**, not a discovered exploit of the shipping application. The correction separates immutable notification deduplication from verified source-state refreshing; a new source revision is persisted and independently audited even when the notification ID already exists. Confirm the subsequent exact-head green workflow before calling the fix validated.

**Monotone revision abstraction is a test fixture, not a Play API field guarantee.** Google Play SubscriptionsV2 does not supply a general developer-facing integer `provider_revision` as used in this synthetic adapter. Real provider adapters need a separately justified, monotonic, provenance-preserving normalization based on trusted vendor truth, linked purchase lineage, state digests and event/poll sequence. They must not invent an ordering from arbitrary client timestamps or allow stale provider responses to resurrect an entitlement. The test does not measure real-world provider consistency or delivery latency.

**Duplicate event is not a complete reconciliation schedule.** Production also needs authenticated purchase-status refresh on relevant protected actions, app resume, disputes and bounded periodic reconciliation. No backend can promise immediate cross-device revocation while offline caches remain disconnected.
