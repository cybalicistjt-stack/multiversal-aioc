# GATE-05 — PostgreSQL commerce ledger, atomicity and controlled projections

**Status:** source-only technical schema proposal; implementation *not* authorized.  
**Selected work:** GATE-05 under OPS5. **Database target/reference:** PostgreSQL 17 documentation for current Render instance family (do not infer service is healthy or migrations executed).

## Separating four domains of truth

1. **Account identity:** canonical immutable Multiversal `subject_id`, no provider ID, email, device or username as ownership key.
2. **Provider evidence/inbox:** verified authenticated delivery proof and immutable provider/environment/event ID; first seen and payload digest; independently fetched current provider snapshots remain separate from raw notifications.
3. **Commercial journal:** immutable attributed invoices, financial postings, paid periods, reversals and reconciliation receipts; this cannot itself authorize Campaign role, content license or grant.
4. **Effective access:** entitlement cause, scoped capability, resource provenance, version/expiry/revocation and account/device offline lease. Derive from journal + approved policies; preserve authorship separately.

**Explicit invariant:** a row in `billing_inbox` or a successful provider redirect is NEVER evidence of an authorized active subscription. Exactly-one inbox event and exactly-one financial posting are different constraints. An idempotency key cannot be reused across subject, operation, provider environment or amount silently.

## Proposed relational tables

| Table | Identity/key | Required facts | Rejects |
| --- | --- | --- | --- |
| `billing_provider_customer` | PK binding_id; unique provider/environment/customer_ref | subject_id, bind version, actor/audit proof | A customer ID belonging to two subjects |
| `billing_checkout_intent` | PK intent_id; unique subject/operation/idempotency_hash | offer version, consent, currency, storefront, expiry, immutable subject | Redirect minted member, double-session unintended |
| `billing_provider_inbox` | PK inbox_id; unique provider/environment/event_ref | verified raw source digest, processing status, first seen, snapshot ref | Duplicate signed delivery double application |
| `billing_subscription` | unique provider/environment/subscription_ref | canonical subject, provider customer, status, autoRenew, last snapshot version | Cross-account claim, out-of-order reversal |
| `billing_paid_period` | unique provider/environment/invoice_ref + period ref | verified paid interval, currency, approved revision, ended/corrected facts | More than one grant from same invoice |
| `billing_journal_entry` / `billing_journal_line` | immutable grouped balanced postings | integer minor units, one currency per group, external evidence ref | Double money posting, unexplained refund |
| `billing_entitlement_projection` | subject/scope/source unique key | paidThrough, cause, source revision, grant policy epoch | Payment status scalar controlling all rights |
| `billing_allowance_slot` | UNIQUE(campaign_id, beneficiary_subject_id) | GM issuer, selected root, closure hash, version, state, tombstone | Two concurrent GM allowances for player/campaign |
| `billing_outbox` | unique aggregate/version/event kind | event payload digest and delivery metadata | Lost or doubled side effect after commit |

The associated **readable SQL artifact** [GATE_05_POSTGRES_SCHEMA_PROPOSAL.sql](GATE_05_POSTGRES_SCHEMA_PROPOSAL.sql) is a non-executable-production design skeleton. It is not a migration, and may not be applied to Render/production/any user data under this tranche. The actual implementation must integrate with existing account/PCV schema instead of creating a second authoritative subject store.

## Transaction boundary design

### A. Provider notification ingestion

1. Verify raw event authenticity and environment at the HTTP ingress. Reject invalid signatures before persistence as accepted provider evidence.
2. In one PostgreSQL transaction, write verified event key `(provider,env,event_id)` using a **unique constraint** and `ON CONFLICT DO NOTHING`; record dedupe outcome, never overwrite a distinct digest for an existing ID (flag security anomaly).
3. Out-of-order, re-delivered and old messages schedule a **current provider fetch**; never reapply a dated webhook state as current source truth.
4. If provider fetch fails, commit pending lookup to outbox with bounded backoff; **no new entitlement**. If a former paid-through grant exists, allow it only within its finite validated scope and without contradicting a known denial.

### B. Verified state reconciliation (single transaction)

1. Fetch a provider-current snapshot outside the DB transaction and authenticate its customer/environment/subscription/offer, money and invoice references. In DB, lock the canonical customer/subscription mapping **FOR UPDATE** and recheck ownership and current revision.
2. Only an actually fresher, authenticated snapshot can advance the saved provider projection. Normalize trusted instants, `autoRenew`, raw billing status and verified paid-through separately; if missing, hold instead of inventing infinite valid time.
3. Append exactly-once commercial journal fact referencing immutable provider event/invoice. Monetary postings are **balanced** and reversals are new compensating entries; older history is never rewritten. Capture refund/dispute and pending policy separately.
4. Change the `billing_entitlement_projection` and append outbox invalidation/delta in **the same commit**. The service reads only committed projections. A committed fact without an emitted notification can be recovered from the outbox; an uncommitted event is never externally visible.
5. Use per-object version compare and read locks; apply PostgreSQL `SERIALIZABLE` only where cross-row decisions require it, and retry the *whole transaction* on SQLSTATE 40001 within a bounded policy. Unique violations are not all serialization failures; classify them. Never retry external charges inside the DB retry callback.
6. Publish committed outbox records using stable event IDs and consumer-side dedupe. `FOR UPDATE SKIP LOCKED` may distribute **queue tasks only**; it is not a substitute for full consistency when making entitlement or ownership decisions.

### C. Allowance slot creation (later GATE-06)

Atomic issuance proposed:
```text
BEGIN;
  authenticate/lock Campaign GM membership and current eligible GM subscription;
  verify player subject membership, pack license, exact root and closure digest;
  INSERT billing_allowance_slot(campaign_id, beneficiary_subject_id, ...)
  -- the single composite UNIQUE constraint is final arbiter; NEVER precheck alone
  record versioned grant + provenance and required outbox event;
COMMIT;
```
Under 100 simultaneous issuers targeting the same `(campaign, player)`, **only one insert may commit successfully**. Competing calls return the occupied slot (or retry safely), never create 100 grants, reset a tombstone or issue for a different character to bypass one-slot. The future DB test must run real isolated transactions and verify exactly one durable row; this document's 100-attempt Set simulation proves **nothing** about actual PostgreSQL locking.

### D. Known denial / revocation precedence

A verified source cancellation-at-end does not prematurely delete a paid period, but an authorized known revocation/account suspension must not be reversed by older source projections or fallback caches. Persist a monotonic policy/security epoch and irrevocable tombstone/audit record for denied grant versions. A customer reinstall, refund race, stale provider event, network timeout or repeated outbox delivery cannot decrement it. Offline devices may remain unaware until a finite signed lease ends or rechecks online; this is a disclosed bound, not immediate global revocation.

## Financial journal invariants

- Record currency and integer minor units, not floating-point dollars. Decimal/exponent/currency precision requirements must be verified against provider-specific money semantics and approved offer catalog.
- A **postings group balances for its one currency** when all lines are present; enforce at transactional journal-finalization boundary (a simple per-row CHECK cannot sum other rows).
- Each provider object/fact/line has idempotent unique business reference; a duplicate does not create another invoice, revenue, grant or payout.
- Refund, adjustment and chargeback add attribution-linked compensating postings. Never edit the initial invoice/payment record in place.
- Real-money commerce does **not** mix with RPG currency or inventory market journals merely because both use prices or ledgers.
- Marketplace creator payouts, multi-currency FX, sales tax and chargebacks need further tranche/owner decisions; schema here is a minimal membership billing foundation, not approved general accounting.

## Concurrency, failure and recovery matrix

| Failure / race | Expected durable result | Required real proof at implementation |
| --- | --- | --- |
| Two verified event deliveries share ID | One inbox row; optionally log conflicting digest anomaly | Concurrent unique-key insertion |
| Two checkout retries with same idempotency token | One subject-owned intent; other subjects denied | Two devices, identity binding and unique key |
| Two customers claim same provider ref | One account binding, other quarantined | Unique composite key and race |
| Old refund webhook after newer renewal snapshot | Fetch current provider, no stale projection rollback | Different delivery ordering |
| Commit then worker dies before publish | Outbox persists and is later delivered once logically | Kill/restart DB worker |
| Publish then worker dies before ACK | Same stable event ID retried, consumer dedupes | Inject publish-ack failure |
| DB deadlock/serialization failure | Full atomic retry or typed conflict; no double billing call | Real `40001` and `40P01` fault injection |
| Provider lookup timeout | Pending work retained; no new grant | Provider unavailable simulation at service edge |
| Known revocation vs cached old grant | Denial remains authoritative online; offline finite leakage disclosed | Epoch/version and device recheck |
| 100 simultaneous GM allowance requests | 1 durable slot, 99 conflict/occupied | 100 real concurrent PostgreSQL sessions |
| Malicious restricted-character export | Rejected before any destination commit, provenance preserved | Real source+destination transaction |
| Backup/restore replay | Unique keys, tombstone epoch, journal audit and queued outbox survive | Isolated backup/restore (not existing Render data) |

## Acceptance and proof grade

Synthetic [60-case contract fixtures](GATE_05_LEDGER_FIXTURES.json) and `scripts/gate05_reference_oracle.mjs` are a **source-only sanity check**, not database execution. The 100-attempt Set model is a toy for unique-slot intent only.

**Future independent acceptance must use** a disposable PostgreSQL 17 instance, isolated schema, real parallel transactions, duplicate provider events, rollback/serialization/deadlock injection, actual service-to-DB access checks, committed outbox recovery, and backup/restore with preserved provenance. GATE-09 owns product implementation, subject to existing PCV-03F boundaries and external Render backup risk. Do not call GATE-05 *database verified* unless those artifacts exist.

## Source register

- PostgreSQL 17 [Transaction Isolation](https://www.postgresql.org/docs/17/transaction-iso.html): `SERIALIZABLE` blocks serialization anomalies; applications must retry conflicts.
- PostgreSQL 17 [INSERT / ON CONFLICT](https://www.postgresql.org/docs/17/sql-insert.html): unique-index-backed conflict processing; do not treat as generic replay authorization.
- PostgreSQL 17 [DDL Constraints](https://www.postgresql.org/docs/17/ddl-constraints.html): PK, unique, FK and CHECK behavior.
- PostgreSQL 17 [SELECT row locking](https://www.postgresql.org/docs/17/sql-select.html): `FOR UPDATE`; `SKIP LOCKED` for worker queues, not decisions requiring a consistent full view.
- [NCG SBEC commerce boundary](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/sbec/COMMERCE_BOUNDARY_MODEL.md): research-only separation of money, subscription, entitlement, rights and offline.
- [NCG UADS Campaign Allowances](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/uads/CAMPAIGN_ALLOWANCES.md): owner-approved one campaign/player allowance, provenance + closure rules.
- Published [GATE-03 provider contract](GATE_03_PROVIDER_CONTRACTS.md) and [GATE-04 lifecycle](GATE_04_BILLING_LIFECYCLE.md): internal source dependencies.
