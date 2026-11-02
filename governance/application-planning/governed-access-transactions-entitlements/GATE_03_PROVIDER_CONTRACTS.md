# GATE-03 — Provider-neutral billing and account-binding contracts

**Scope:** source-only interface and adversarial design. Stripe is the first *hypothetical adapter*, not a merchant account, activated payment rail, signed event test or approved commercial offer.  
**Inputs:** verified OPS5 GATE-01/02 published artifacts, UADS approved canonical account model, SBEC documentary research, current application entitlements port, and dated official Stripe docs.

## Architectural distinction

1. **Multiversal account** is a stable opaque `subjectId` with verified email and unique username. Authentication comes from our session authority, not the payment provider or mailbox alone.
2. **Commercial customer** belongs to one provider environment and one canonical `subjectId`; a Stripe Customer ID, Play purchase token, email string or client reference is never the user account primary key.
3. **Checkout intent** is a server-issued expiring authorization to request a specific priced offer in one storefront, bound to `subjectId`, published offer-version, product/category, currency, region, terms/consent version and idempotency key. This is not a paid entitlement.
4. **Provider receipt** is untrusted at ingress until independently validated by that provider's signed/authenticated mechanism and server-side lookup of current subscription/invoice status; signed webhooks represent event evidence, not an unordered source of truth.
5. **Effective entitlement** is a separately authorized, dated resource/capability grant produced by our backend only after authoritative reconciliation. Payment facts do not grant Campaign membership, GM role, content transfer license or universal catalog entitlement.
6. **Owned work** remains owned and historically reconstructable independently of paid access. Cancellation of auto-renew is not immediate expiry; failed payments, refunds, disputes and grace choices belong to GATE-04.

## Proposed TypeScript interfaces — no product changes

```ts
type ProviderKind = "stripe-direct" | "google-play" | "apple-app-store" | "mock-contract";
type Storefront = "direct-web" | "windows-direct" | "android-play" | "ios-app-store";
type IdempotencyToken = string; // opaque, server checked and bounded
type CanonicalSubjectId = string;
interface CheckoutIntentRequest {
  offerId: string; offerVersion: string; storefront: Storefront;
  consentVersion: string; idempotencyToken: IdempotencyToken;
  // subjectId is intentionally NOT accepted here: trusted auth context only
  // amount, currency and provider price IDs must NOT be client-supplied
}
interface AuthContext {
  subjectId: CanonicalSubjectId; verifiedEmail: boolean;
  authSessionId: string; securityVersion: number;
}
interface OfferedPrice {
  offerId: string; offerVersion: string; capabilitySku: string;
  currency: string; amountMinor: number; taxPolicyVersion: string;
  merchantRegion: string; allowedStorefronts: Storefront[];
  providerMapping: { provider: ProviderKind; environment: "test"|"live"; catalogRef: string };
  approvalStatus: "unapproved"|"approved_inactive"|"activated";
}
interface CheckoutIntent {
  intentId: string; subjectId: CanonicalSubjectId; offerSnapshot: OfferedPrice;
  storefront: Storefront; requestedAtTrusted: number; expiresAtTrusted: number;
  consentVersion: string; nonceHash: string; idempotencyKeyHash: string;
  status: "created"|"provider_session_open"|"expired"|"reconciled"|"invalidated";
}
interface ProviderCheckoutSession {
  provider: ProviderKind; environment: "test"|"live"; providerSessionRef: string;
  checkoutUrl?: string; nativePurchaseAction?: string;
  expiresAtTrusted: number; linkedIntentId: string;
}
interface ProviderCustomerBinding {
  provider: ProviderKind; environment: "test"|"live";
  providerCustomerRef: string; subjectId: CanonicalSubjectId;
  verifiedAt: number; bindingVersion: number;
}
interface ProviderEvidenceEnvelope {
  provider: ProviderKind; environment: "test"|"live";
  eventRef: string; deliveryId?: string; eventType: string;
  receivedAtTrusted: number; // sealed raw payload/signature handled server-side
}
interface VerifiedBillingSnapshot {
  provider: ProviderKind; environment: "test"|"live";
  providerSubscriptionRef: string; providerCustomerRef: string;
  providerInvoiceRef?: string; canonicalSubjectId: CanonicalSubjectId;
  offerId: string; offerVersion: string; currency: string;
  providerStatus: string; paymentConfirmed: boolean;
  autoRenew: boolean; paidThroughTrusted?: number;
  providerVersionOrFetchedAt: string;
}
interface ProviderAdapter {
  createCheckoutSession(intent: CheckoutIntent): Promise<ProviderCheckoutSession>;
  verifyEventAuthenticity(rawBody: Uint8Array, signatureHeaders: Record<string,string>): Promise<ProviderEvidenceEnvelope>;
  lookupCurrentBilling(verifiedProviderRef: string): Promise<VerifiedBillingSnapshot>;
  createCustomerManagementSession(subject: CanonicalSubjectId, verifiedBinding: ProviderCustomerBinding): Promise<{url:string;expiresAtTrusted:number}>;
}
```

The typed specification is intentionally *not* a usable payment implementation. A catalog mapping is not an owner-approved live price.

## Required server authorization flow

```text
POST /billing/checkout-intents (authenticated verified-email account)
 → verify requested offer is approved/active in relevant region and storefront
 → normalize `offerId+version` and server-controlled price/currency/consent
 → create idempotent subject-owned expiring CheckoutIntent
 → provider adapter creates hosted/native session under verified subject binding
 → return ONLY checkout session URL/native action, no capability grant

POST /billing/provider-event (internet-facing)
 → verify provider signature/raw bytes and environment, dedupe event reference
 → resolve or quarantine subject-bound stored purchase intent
 → map provider Customer/Subscription/offer/version/currency under server policy
 → fetch provider CURRENT billing status; reconcile revision and paid-through
 → transactional billing event/ledger (GATE-04/05)
 → derive resource-scoped entitlement via GATE-02/06 policy
 → issue new signed offline grant only via GATE-07, never a webhook-supplied Boolean
```

**Never:** accept a user-supplied subject ID, email or order ID as proof of ownership; let a client choose an amount/price ID; trust success redirect or `checkout.session.completed` by itself for asynchronous payment; bind a shared-mailbox payment to all subjects; accept a sandbox receipt in production.

## Security and cross-platform seams

- **Idempotency:** scoped to subject+offer+operation+intent version; retrying one intent returns its existing session or a well-defined expired/conflicted outcome. Multiple different user devices must not accidentally create two recurring subscriptions. Reconcile provider objects before recreating a session.
- **Wrong-account claim:** provider customer IDs/tokens are unique within provider/environment and bound to exactly one canonical subject; a later claim by another subject quarantines transfer for owner-reviewed recovery rather than silently moving entitlements.
- **Cancellation and customer portal:** only a verified same-subject owner opens direct-provider management; Google Play/Apple subscriptions route to that storefront's legitimate management path. Client-supplied email never authorizes a portal session.
- **Client role:** Windows/Android can initiate an authorized purchase path and read *our* effective entitlement, but cannot mint grants, prove subscriber status with screen pixels, or use another account's cached receipt.
- **Play and Apple distribution:** compliant storefront specifics are future GATE-08/11 and legal/provider gates. Do not assume Stripe checkout is permitted for all native Android contexts or territories.
- **Data minimization:** never log unredacted payment method, PAN, credentials, raw signed provider event secrets or unnecessary PII in app or CI. Durable event ID/trace, source hashes and appropriate receipt references are sufficient for testing.

## Evidence states and blockers

| Evidence | Status |
| --- | --- |
| Canonical account and allowance rules | Owner-approved UADS design, implementation not verified |
| Stripe Checkout hosted session association and webhook-first fulfillment | Official documentation, conditional first adapter design |
| Stripe Customer identity and return/referrer state | Official docs explain reusable Customer objects and Checkout Session IDs, **not proof of account ownership** |
| Provider adapter interfaces, 42 scenario rules | Synthetic source-only, no live provider requests |
| Current entitlement service integration | Proposed, not written |
| Merchant account/test-mode/production credentials | Not created, not requested, not authorized |
| Owner-approved offer price/tax/refunds/region/storefront | Pending GATE-08, MCB and owner approval |
| Provider/current-state validation, signed webhook and anti-replay | GATE-09/10 real acceptance, NOT_RUN |

## Dated sources

- [Stripe existing customers and Checkout sessions](https://docs.stripe.com/payments/existing-customers?platform=web&ui=stripe-hosted) — Checkout can associate an existing Customer; downstream webhook fulfillment is recommended over redirect.
- [Stripe subscription pricing table](https://docs.stripe.com/payments/checkout/pricing-table?locale=en-GB) — client reference is nonsecret metadata, cannot substitute for authenticated account binding.
- [Stripe event catalogue](https://docs.stripe.com/api/events/retrieve) — distinguishes Checkout, invoice and subscription events.
- [Stripe subscription modification API](https://docs.stripe.com/api/subscriptions/update) — incomplete payments, billing state and cancellation are separate concepts.
- [NCG SBEC overview](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/sbec/README.md) — payment / entitlement / owned data separation, documentary.
- [UADS account design](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/uads/ACCOUNT_DEVICE_ENTITLEMENT_DESIGN.md) — approved subject/verified email, recovery, device/offline and sharing rules.
- [Current app service port](https://github.com/cybalicistjt-stack/Multiversal-app/blob/main/packages/entitlements/src/entitlement-service-port.ts) — typed grant interface, not provider implementation.

## Self-contained reference fixtures

[GATE-03 provider contract fixtures](GATE_03_PROVIDER_CONTRACT_FIXTURES.json) and `scripts/gate03_reference_oracle.mjs` give 42 source-only positive/negative assertions across checkout creation, customer portal ownership, provider evidence validation, idempotency, wrong owner, wrong region and redirect spoofing. These are **not** a real Stripe signature, PostgreSQL atomicity, installed platform test or paid receipt.
