# GATE-08 — Storefront, subscription disclosures, tax/merchant roles and economics

**Scope:** source-only 2026-11-02 research and decision-support. No vendor contract, price/SKU publication, live merchant onboarding, store entitlement enrollment, legal sign-off, billable subscription or product implementation is authorized. The historical **$4.99/month is a target, not an approved offer**; any numeric example is illustrative only.

## Channel and region decision matrix (current evidence, not legal approval)

| Surface | Payment routes to evaluate | Required proof / caveat |
| --- | --- | --- |
| Self-distributed Windows / direct web | Hosted Stripe Checkout/Billing as *assumed first adapter*, or later provider-neutral substitute | Verified owner-approved offer, merchant/tax/account lifecycle, server-side receipt; provider fees and terms independently quoted |
| Google Play Android, United States | Play Billing; or qualified US alternative billing after program enrollment | As of Google's 2026 US policy: alternative billing is opt-in, eligibility/region/reporting/service fees apply. Reporting and payment fee requirements started Oct 1, 2026 under applicable program; cannot silently treat an external Stripe link as globally authorized |
| Google Play Android, other countries | Play Billing or region-approved programs only | Recheck country-specific current rules, SDK and billing programs; US permission does not extend globally |
| iOS via App Store, United States (future) | Apple IAP; links to other purchase methods as currently allowed in US storefront subject to exact guidelines | Apple's Oct 16 2026 guideline updates clarify link rules; do not infer all other regions permit external direct checkout |
| iOS via App Store, other storefronts (future) | Apple IAP and eligibility-specific entitlements/approved links | Validate App Review sections 3.1.1, 3.1.1(a), 3.1.2 and 3.1.3 for app category, region/platform and current storefront state; no blanket direct billing |
| Independent or third-party Android distribution | Conditional direct provider and store terms | Distinguish installation/distribution channel and merchant obligations; do not assume Google Play program applies to non-Play build |

**Cross-platform access:** even when payment rail differs, canonical Multiversal `subjectId` owns entitlement after authenticated server provider verification. One receipt may not activate two distinct accounts, and it does not transfer Campaign membership or full library ownership. Storefront-specific purchase tokens, transaction receipts and customer support routes remain source-linked.

## Evidence and transaction lifecycle

User chooses a published, owner-approved offer → sees exact price/currency, recurrence, taxes if applicable, benefits/limitations and cancellation/trial/refund terms → affirmatively consents → provider-specific checkout on approved channel → server verifies exact-subject purchase/receipt/current status → ledger period and resource-scoped entitlement are reconciled → platform-specific acknowledgement/reporting handled by appropriate provider → user receives clear paid-through and account/cancel-management path.

A client success redirect, unverified Stripe Checkout Session, Play `PENDING` transaction, shared recovery email or copied Apple signed purchase is **never** membership proof. Android Play purchases must be verified with the Play Developer API and acknowledged under its current requirements after accepted grant. Apple's server-side verification must bind transaction history to our account subject; trial and family/restore policies need separate decisions.

Store-specific subscription management must route users to the rail that actually charged them. A Google Play-billed purchase belongs in Play management, whereas alternative billing may require a developer-operated management URL, refunds and customer support. Windows direct billing management similarly uses verified account-owned provider binding. A generic “cancel in Play” button is wrong for direct Stripe purchases.

## Subscription disclosures and consumer protection (legal-review required)

Before any charge, present: responsible merchant; plan/price and currency; whether taxes are included/added; renewal interval and price-change rules; what paid subscription actually unlocks versus free/GM allowance/Sponsored Month; trial length and conversion price if used; cancel method and effective paid-through; refund/dispute policy; data retention and restricted-character read after lapse; access loss on expiration; supported device/offline limitations; customer support and receipt/records.

Capture versioned disclosure/consent tied to the canonical account and provider checkout intent. Show a clear user route to cancel and view next billing/paid-through; never treat uninstalling the app as canceling a subscription. Customer retention UX must not obstruct lawful cancellation.

**Important US rule timing:** the FTC's 2024 amended “Click-to-Cancel” Negative Option Rule was vacated in 2025; the FTC in Feb 2026 recodified the prior Negative Option Rule and initiated a new 2026 rulemaking process. **Do not claim the vacated amendment is currently enforceable as written**. ROSCA and other applicable federal/state consumer laws still require analysis; jurisdiction, exact statutory requirements, state automatic renewal rules and responsible merchant/terms require qualified legal review before launch. Store policy compliance does not replace legal compliance.

## Tax and merchant roles

An assumed PSP or Stripe Tax product does not make Multiversal tax-exempt or make Stripe merchant-of-record by default. Record **actual merchant-of-record/contracting party, tax-registration nexus/jurisdiction, tax-inclusive/exclusive offer, collection/remittance responsibility, storefront provider tax treatment, refund accounting, currency and evidence of invoices/receipts** before opening a sale territory. Do not invent Alabama/national digital goods tax applicability or apply tax rates from memory. A marketplace creator sale would require a distinct merchant/agency and creator settlement analysis and is outside the initial subscriber model.

For each sale/period, distinguish gross sale, sales tax collected and remitted, payment-processing charges, subscription Billing fees, platform/store alternative billing service charges, currency-conversion and dispute/chargeback losses, hosted service costs, variable AI usage, support, refunds and reserve. Do not double count fees already included in quoted provider plans and do not treat tax collected as earned margin.

## Cost scenario model (integer minor units)

```text
Customer collection (including any tax) = gross_minor
Net contribution = gross_minor
  – processor_fee – subscription_billing_fee – store_or_alt_billing_fee
  – other_provider_fee – variable_service_cost – support_cost
  – expected_refund_loss – risk_reserve
  – sales_tax_collected_and_remitted_by_responsible_merchant_or_platform
```

Use **per-channel and per-region contractual quotes**, not one global percentage, to populate the variables. When gross collection includes sales tax, subtract that tax **once** regardless of whether the merchant remits it or the platform withholds/remits it; a tax-positive sale with no identified remitter is an unresolved liability, not margin. The sample [fixtures](GATE_08_STOREFRONT_FIXTURES.json) use **499 minor units solely as historical-target arithmetic examples**, with fictional cost inputs for deterministic correctness. They are not proposals, forecasts or active prices. Avoid assuming vendor's domestic card headline rate is the all-in recurring bill: recurring Billing, store obligations, non-domestic payments, tax and support may change it.

Reevaluate unit economics at various paying subscriber counts, transaction mix, refunds, free-user consumption, AI usage, support labor, monthly infrastructure bills, discounts/promotions, taxable jurisdictions and payout delays. A $4.99 target can result in much less than $4.99 of contribution, and gross recurring price is not margin.

## Explicit owner and implementation gates

- **MCB/owner:** final offer price, capabilities/trials/grace/refunds/GM sponsorship, customer-facing claims, commercially effective terms and geographic scope.
- **Merchant/legal/accounting:** legal entity/tax/merchant registration, published policies, applicable ROSCA and state requirements, data privacy and regional storefront terms.
- **Engineering:** real account verification, PCV-03F backend prerequisites, GATE-09/10 signed provider staging, GATE-11 real Windows/Android purchase/restore/cancel, GATE-12 security and GATE-13 operations/incident reconciliation.
- **Store/provider:** actual contracts, fees, merchant accounts, Play enrollment/acknowledgment/reporting, Apple IAP or entitlements, published management routes and receipt verification. No auto-approval from documentary research.

The [storefront reference fixtures](GATE_08_STOREFRONT_FIXTURES.json) and `scripts/gate08_reference_oracle.mjs` cover 50 assumed-channel/region policy gates and 14 fictional integer-minor-unit cost cases. **Neither validates legal applicability nor provider quote, real tax, installed app or merchant eligibility.**

## Dated primary sources (reviewed 2026-11-02)

- [Google Play US alternative billing](https://support.google.com/googleplay/android-developer/answer/16497028?hl=en): program enrollment, eligibility, service fee/reporting obligations, region and currently applicable US conditions.
- [Google Play purchase fraud/verification](https://developer.android.com/google/play/billing/security): verify `purchaseToken` server-side before entitlement; distinguish PENDING, acknowledge eligible purchases.
- [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/): sections 3.1.1, 3.1.1(a), 3.1.2 and 3.1.3; [Oct 16, 2026 Apple guideline update](https://developer.apple.com/news/?id=92th7e5i).
- [FTC Feb 2026 recodification](https://www.ftc.gov/policy/public-comments/revision-negative-option-rule-withdrawal-cars-rule-removal-non-compete-rule-conform-these-rules-0); [ROSCA law](https://www.ftc.gov/legal-library/browse/statutes/restore-online-shoppers-confidence-act). No legal opinion.
- [Stripe Checkout pricing example](https://stripe.com/payments/checkout) and [Stripe local payment method pricing](https://stripe.com/pricing/local-payment-methods) — published conditional fee examples, not accepted Multiversal terms.
- NCG SBEC commerce boundary and BESF economic owner decision packet (research only); GATE-02/03/04 provider/account/period source acceptance.
