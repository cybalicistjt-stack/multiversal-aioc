# GATE-01 — Current-source baseline and initial architecture

**Evidence:** documented source/code review and proposed contracts as of 2026-11-02. **Not:** a working Stripe sandbox, actual payment, new app code, installed/device acceptance or completed GATE-01 publication.

## Existing evidence and proof gap

| Source | Demonstrates | Missing |
| --- | --- | --- |
| App `packages/entitlements/src/entitlement-service-port.ts` and `packages/contracts/src/identity-device/entitlement-evaluator.ts` | typed Free, subscription, sponsored and generic Campaign grant access | Verified payment/service ledger, distinct one-slot allowance, resource provenance, signed offline lease |
| NCG UADS account/allowance | owner-approved verified email, username, multi-device, offline continuity and 1 allowance per Campaign/Player | Auth vendor selection, actual Windows/Android tests, cryptography/service authority |
| NCG SBEC/BESF | provider-independent purchase/right/ownership model and hypothetical $4.99 viability | Actual invoices, renewal/fees, merchant contract, customer behavior |
| AIOC SA-BILL-01..10/PR1918 | Static code audit, planned source fixes, synthetic PostgreSQL and negative cases | Production deployment, provider-signed receipt, independent connected security test |
| XTRA-08/11 | negative-case preparation and nonpublic commercial templates | legal tax clearance, priced offer, public website or live merchant setup |
| NCG SCEV PR145 | further 32-tranche documentary method in **draft unmerged PR** | research adoption, live market/merchant proof |

## Recommended logical boundaries

```text
[Windows / Android / optional Web]
               |
[verified Multiversal account / installation binding]
               |
[server authorization entry point] <--------- [Campaign role/content/ownership policy]
               |
[resource-scoped entitlement evaluator] ----- [one allowance slot + dependency graph]
     |                     |
[canonical billing ledger]  [signed finite account/device offline lease]
     |
[verified provider adapter] -------- [Stripe direct assumed] / [Play conditional]
     |
[webhook verification + current provider reconcile + idempotent event log]
```

Payment processing identifies payer/transactions, **not** a Multiversal account or game content owner. Canonical subject ownership remains our backend. Preserve provider-specific IDs only in billing mappings. Offline lease signing keys never exist in client builds.

## Proposed records (no migration applied)

| Record | Core keys and invariant |
| --- | --- |
| `BillingCustomerBinding` | unique provider/customer -> canonical subject; verified account linkage |
| `BillingAgreement` | provider subscription/product/price version, subject, trusted period start/end, auto-renew distinct from access, provider revision |
| `PaymentEvent` | unique provider+event ID, authentic signature receipt, dedupe, ordered canonical agreement reconcile |
| `EntitlementGrant` | subject/source/capability/resource scope, start/end, policy+revocation epochs, trust provenance |
| `CampaignAllowanceSlot` | unique campaign+Player subject, subscribed issuer, one root+closure hash, history/tombstone |
| `OfflineDeviceAuthorization` | signed subject+device binding, scope/version/paid-through cap, expiration and antirollback anchor |
| `AccessDecisionAudit` | who/what/resource/action/why, minimal privacy footprint and immutable revision reference |

## Specific current source hazards to resolve

1. Cancellation of renewal may incorrectly be interpreted as immediate revocation of already-paid access; `autoRenew` and `entitledUntil` must be separate.
2. Arbitrary ISO string comparisons can give wrong results across offsets; validate canonical server instants and reject invalid windows.
3. Generic Campaign grant can create global access unless the selected root and exact Campaign context are enforced. Sponsored Month must be distinct from limited Campaign Allowance.
4. Existing grant port takes input records without proving origin. Server ingress must verify payment receipts, issuer GM role and canonical identity; clients cannot mint rights.
5. No one-slot root/dependency graph/provenance model exists in the pure evaluator. DB uniqueness and source-scoped authorization are required.
6. Cached signed rights require account/device binding, protected key storage, known-revocation precedence and finite checked paid-through limits, with disclosed disconnected-refund exposure.
7. All output boundaries—search counts, content indexes, snapshots, WSS, export/import and AI—must enforce same authorization, not only UI button visibility.

## Owner decisions that remain pending

Price ($4.99 historical target vs $9.99 informal), grace/retry, refunded charge behavior, paid GM lapse and existing allowances, region-specific store route, tax/merchant, identity/email provider, optional AI metering, exact cryptographic lease timing and real test credential/spend decisions. Defaults in GATE_DECISION_REGISTER are recommendations, not silently adopted policy.

## GATE-01 source-only acceptance

- Current OPS5 selector/registry/work-item agree; `gpr,cwks,mtlc` persistent IDs unchanged and PCV-03F/MTLC-14/AXI untouched.
- GATE-01..14 unique ordered acyclic tranches; later product stages gated without automatic activation.
- Reconciled source citations and major evaluator gap inventory; explicit proof-grade labels for unmerged SCEV and synthetic SA-BILL work.
- Exact-head PR checks, fresh-main integration, merge and publication evidence required before marking completed_verified.
