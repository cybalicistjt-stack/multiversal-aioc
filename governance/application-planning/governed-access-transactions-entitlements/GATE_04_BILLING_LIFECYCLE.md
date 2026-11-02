# GATE-04 — Billing lifecycle, temporal access and event reconciliation

**Authority:** GATE-04 design only, on-demand OPS5. No live billing, Stripe account, provider signature, database schema mutation, native test or product code. **Status:** source design pending protected publication.

## Evidence hierarchy

1. Owner-approved UADS account/offline and Campaign allowance policy controls account identity, data retention and finite verified rights.
2. GATE-02 published resource-scoped policy controls effective capability and provenance.
3. GATE-03 published provider-neutral checkout/customer binding contracts control payment evidence entry.
4. NCG SBEC source model, explanatory research only (not adopted product): payment, subscription period, grants, ownership, taxes and in-game economy differ.
5. Stripe official documentation is used to identify adapter events and failure semantics; it does not define the cross-provider canonical schema or prove a functioning integration.

## Separate independent facts — do not collapse into “active/cancelled”

- `provider_billing_status`: raw provider enum plus source/version, can be `active`, `trialing`, `past_due`, `unpaid`, `paused`, `canceled`, `incomplete`, or provider-specific.
- `auto_renew` and `cancel_at_period_end`: intent about a *future renewal*, separate from access to an already paid period. Cancel-at-end preserves valid paid coverage until the verified end, absent a distinct revocation event.
- `paid_through`: finite trusted entitlement ceiling from reconciled, paid invoice/verified period (not the time an email/webhook arrived). A paid-through change must be traceable to an invoice, refund or correction.
- `invoice_payment`: paid/unpaid/failed/action-required/processing/voided, with trusted provider reference. A checkout redirect or subscription-created event alone is not proof of collection.
- `refund`, `dispute` and `revocation`: distinct attributed evidence and owner policy, not automatically the same as canceling auto-renew.
- `authorization`: resource scope, visibility, role, ownership, account security, subject and signed offline lease (GATE-02, 06, 07), not derived from commercial status alone.

## Normalized lifecycle

```text
checkout intent → provider session created → pending verification
              ↘ abandoned/expired (NO paid capability)
provider evidence ingested → raw signature verified → persisted inbox + dedupe
 → customer/subject/environment/offer mapping → provider-current lookup
 → immutable commercial fact + invoice/paid period attribution
 → derived subscription-state projection + version comparison
 → resource-scoped entitlement recomputation (NOT direct webhook grant)
 → cache invalidation or finite offline lease issuance (future GATE-07)
```

**Period status** is a derived projection, never a single mutable Boolean. The event inbox is append-only; duplicates are acknowledged safely; all destructive/regression corrections are compensating events under GATE-05.

## Access decision reference matrix

| Condition | Proposed access behavior | Important limit |
| --- | --- | --- |
| Provider current and paid verified, paid-through in future, active | Authorize within independent resource permissions | Exactly paid scope, finite end |
| Auto-renew turned off, already paid period current | Preserve rights until paid-through | Cancellation is not expiry |
| Payment failed for **next** period, previous period still paid | Preserve previously paid period; show retry needed | No automatic extra grace after paid-through |
| Payment fails and no verified paid interval | Do not create new paid rights | “past_due” alone is not payment |
| Cancel-at-period-end confirmed | Preserve verified current paid coverage only | Known early termination/revocation remains controlling |
| Paid-through reached/exceeded | Expire paid-period rights; retain owned data | Do not infer recurring renewal |
| Trialing or trial ends | **Pending policy**: no automatic subscriber grant in source model | Trial eligibility/length must be approved |
| Unpaid, paused collection or paused subscription | Hold new rights pending source-specific policy | Stripe collection pause ≠ subscription paused |
| Full/partial refund or dispute | Place affected access decision in policy-review/hold; track prior facts | Owner must decide precise retroactive effect; no blanket data deletion |
| Repeated, late, older or unordered event | Deduplicate and fetch current provider state | Never replay stale event into fresh rights |
| Signature missing/bad or wrong provider environment/customer | Reject/quarantine; no grant | Payment proof from another account is invalid |
| Provider outage while finite previously verified grant exists | Preserve already-valid rights until its trusted end, absent known revocation | Do not extend paid-through, mint new rights or override known denial |
| Offline account/device valid signed lease | Usable only inside last verified finite scope; remote revocation detection delayed | GATE-07 actual crypto/native acceptance later |

**Conservative source-model defaults** (e.g. refund/dispute hold and no implicit trial/grace) are design proposals, not already approved consumer policy. They do not imply taking a paying user's granted access without owner review. Clarify policy before backend release.

## Ordered event and idempotent reconciliation contract

```ts
interface BillingInboxEvent {
  provider: ProviderKind;
  environment: 'test'|'live';
  deliveryId?: string;
  providerEventId: string; // unique within provider/environment
  objectRef: string; eventKind: string;
  signatureProofRef: string; // verification performed before accepting
  payloadIntegrityDigest: string; receivedAtTrusted: number;
  processingState: 'verified_unprocessed'|'pending_lookup'|'applied'|'duplicate'|'quarantined'|'permanently_rejected';
}
interface PaidPeriodEvidence {
  canonicalSubjectId: string; provider: ProviderKind; environment: string;
  customerRef: string; subscriptionRef: string; invoiceRef?: string;
  paidThroughTrusted: number; periodStartsTrusted: number;
  invoicePaymentVerified: boolean; providerSnapshotRef: string;
  reconciledAtTrusted: number; revision: number; policyVersion: string;
}
interface ReconcileOutcome {
  kind: 'no_change'|'applied'|'quarantined'|'requires_owner_policy'|'retry_later';
  subjectId?: string; subscriptionRef?: string;
  previousVersion?: number; nextVersion?: number;
  changedPaidThrough?: number; selectedEvidenceRefs: string[];
  idempotentReceipt: string;
}
```

**Mandatory durability/ordering:**

1. Authenticate provider event with raw payload/signature and environment before any processing; webhook secret never reaches clients. For scheduled provider poll, authenticate the job and still verify customer/offer mapping.
2. Unique inbound key `(provider, environment, provider_event_id)`, plus separate command idempotency and provider-object revision keys; duplicate messages must not duplicate grants or payments. HTTP retries can arrive out of order.
3. Resolve `(provider, environment, provider_customer_ref)` to exactly one subject; never trust event metadata/email or user-provided subject. Unknown/cross-owner events are quarantined with review provenance.
4. Fetch provider **current** subscription, invoices and payment state when events arrive or the periodic reconciliation job runs. Record `fetchedAtTrusted`, verified source reference and status; older events only trigger refresh/reconciliation, not rollback.
5. Within one GATE-05 transaction: apply normalized commercial fact once, compare current version, compute changed paid-period projection, record reason/provenance, enqueue entitlement recalculation, and publish outbox after commit. A crash must not yield payment recorded but unowned permissions silently granted.
6. Periodic sweep accounts for missed webhooks, ambiguous network timeouts, retry backoff, invoice reversal and manual support changes; never assume “no webhook” means paid/not paid.
7. Rebuild from journal and verified snapshots, compare computed projection with persisted one, flag mismatches; corrective writes use typed compensating entries, no untracked edits.
8. Consumer API reports `billingStatus`, `autoRenew`, `paidThrough`, `effectiveEntitlement`, `nextRecheck`, `sourceProof` independently. UI billing messaging does not expose provider secrets, nor infer “no access” from every timeout.

## Temporal and failure test plan

The [GATE-04 synthetic fixtures](GATE_04_TEMPORAL_FIXTURES.json) and `scripts/gate04_reference_oracle.mjs` exercise **70** fixed fixtures (50 subscription/temporal, 20 ingress) including paid-at-boundary, cancellation, paid-but-no-invoice, source mismatches, late events, duplicates, refund/dispute, time bounds and owner mismatch.

This reference checks deterministic design choices only. It intentionally does not implement a provider SDK, signature verification, concurrent transactions or actual permissions and cannot certify GATE-05/09/10. Future adversarial proof includes two out-of-order invoices, network retry with server crash, provider backfill, two account/device duplicate checkout, concurrent refund and renewal, GM subscription expired with allowance, offline stale-but-previously-verified lease, source downgrade and local cache known denial. Each has independent real-boundary proof debt.

## Policy decisions still pending (not silently approved)

- Failed-payment dunning, optional grace window, trial availability/duration, customer support exception and source-specific paid-through semantics.
- Whether a refunded/disputed period is revoked immediately, prorated, retained until reconciliation or handled by customer support; separately preserve user-authored data.
- Pause collection vs pause subscription, chargeback review process, repeated failures, and policy on multi-provider overlapping subscriptions.
- Sponsorship source issuance and the ongoing GM eligibility for previously issued Campaign allowances.
- Which provider receipt events are sufficient for specific payment methods and storefronts, given asynchronous settlement.
- Notifications/disclosures/consent, renewal cadence and price/tax changes are GATE-08/owner subjects.

## Dated evidence pointers (2026-11-02)

- [Stripe subscription webhook lifecycle](https://docs.stripe.com/billing/subscriptions/webhooks) — events include `customer.subscription.updated`, `invoice.paid`, `invoice.payment_failed`; implementation must not assume delivery order.
- [Stripe event type API](https://docs.stripe.com/api/events/retrieve) — the provider defines different invoice/subscription events; `invoice.paid` can include marking paid out of band so verify actual paid circumstances.
- [Stripe subscription update API](https://docs.stripe.com/api/subscriptions/update) — payment behavior, prorations and `pause_collection` are not equivalent to `paused`.
- [Stripe webhooks](https://docs.stripe.com/webhooks) — signature validation, retries, duplicate/out-of-order deliveries.
- [NCG SBEC boundary](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/sbec/COMMERCE_BOUNDARY_MODEL.md) — research model only, no commercial authority.
- [GATE-03 contract](GATE_03_PROVIDER_CONTRACTS.md) and [GATE-02 policy](GATE_02_MEMBERSHIP_CAPABILITY_POLICY.md) — already-published OPS5 source dependencies.
