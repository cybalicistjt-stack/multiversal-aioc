# GATE — Governed Access, Transactions & Entitlements

**Owner approval:** 2026-11-02 · **OPS5 on-demand program** · **Current:** GATE-03 provider-neutral contracts work in progress; GATE-01 registered PR1952 and GATE-02 source-policy published PR1953.

GATE builds Multiversal's provider-independent subscription, billing, entitlement and campaign-grant architecture. **Stripe is the working payment-adapter assumption, not a selected/activated provider.** Payments, access rights, account identity, Campaign authority, content provenance and durable authored ownership remain independent.

## Governance and authority

- Canonical bootstrap: `operations/BOOTSTRAP.md`; selector: `operations/CURRENT.json`; lane routing: `operations/LANES.json`. GATE does **not** add a fourth persistent implementation lane; `gpr,cwks,mtlc` remain the only three persistent slots.
- GPR PCV-03F owns service-first authenticated account/transport and PostgreSQL proof; MTLC-14 and AXI retain their separate work. GATE reads dependencies without mutating their code or selectors.
- GATE-01..08 are architecture/research/synthetic preparation. GATE-09..13 require separate owner-selected implementation scopes and verified prerequisites. GATE-14 requires explicit owner commercial go/no-go.
- MCB owns public pricing/claims and launch messaging. $4.99/month is a historical target, not binding; informal $9.99 is unadopted. Optional AI and creator marketplace are not automatically included in the base offer.
- No active payment, provider account creation, secrets, money movement, storefront publication, or live release is authorized by registration.

## Roadmap (14 tranches)

| ID | Work | Dependencies | Boundary |
| --- | --- | --- | --- |
| GATE-01 | OPS5 scope, evidence audit & architecture | Owner selected | source_only |
| GATE-02 | Membership, capability and ownership policies | GATE-01 | source_only |
| GATE-03 | Provider-neutral account/checkout interfaces | GATE-01, GATE-02 | source_only |
| GATE-04 | Billing lifecycle and event reconciliation | GATE-03 | source_only |
| GATE-05 | PostgreSQL ledger, invariants and atomicity | GATE-03, GATE-04 | source_only |
| GATE-06 | Campaign allowances and sponsored access | GATE-02, GATE-05 | source_only |
| GATE-07 | Offline license/device security design | GATE-05, GATE-06 | source_only |
| GATE-08 | Storefront, taxes, consumer disclosure and economics | GATE-02, GATE-04 | source_only |
| GATE-09 | Authoritative backend and database staging | GATE-05, GATE-06, GATE-07 | future_product |
| GATE-10 | Stripe signed test-mode integration | GATE-03, GATE-04, GATE-09 | future_provider |
| GATE-11 | Installed Windows/Android subscription journeys | GATE-07, GATE-09, GATE-10 | future_product |
| GATE-12 | Independent adversarial security acceptance | GATE-09, GATE-10, GATE-11 | future_product |
| GATE-13 | Support, reconciliation and incident operations | GATE-04, GATE-08, GATE-10 | future_provider |
| GATE-14 | Commercial release decision and owner approval | GATE-08, GATE-11, GATE-12, GATE-13 | owner_only |

**Stage A (01–08):** independently design/test policies, contracts, security/rights, privacy/storefront conditions and ledgers without assuming PCV completion.

**Stage B (09–10):** actual server/payment sandbox implementation only after PCV-03F and credential/merchant approvals; all proof is real service/provider test-mode, not redirect or simulated webhook.

**Stage C (11–13):** real installed Windows/Android, adversarial proof and operational/settlement validation.

**Stage D (14):** explicit pricing, contractual, legal, store, tax, refund, support, financial and security signoff. No automatic activation.

## Foundational invariants

1. Permanent subject ID differs from device/username/email/provider customer/store receipt.
2. Verified payment grants no GM role, Campaign membership, content ownership or transfer license by itself.
3. A Stripe Checkout redirect never activates access; verified signed evidence and current-provider reconcile must bind the canonical account.
4. Distinguish `autoRenew`, `billingStatus`, `paidThrough`, `revokedAt` and `effectiveEntitlement`; normalize trusted instants; preserve already-paid time on ordinary cancellation.
5. Free, personal subscriber, Sponsored Month and Campaign Allowance are distinct causes and resource scopes.
6. Database-unique `(campaign_id,player_subject_id)` allowance slot; one selected root plus source-verified dependency closure, not all premium features.
7. Preserve restriction/provenance through derived characters, exports, imports, AI, search, event projections and offline cache. Retained character inspection is not an unrestricted library license.
8. Signed, finite account/device-bound offline rights stay within verified paid-through time; known revocations cannot be resurrected by cache, but offline devices cannot learn immediate remote refunds.
9. Preserve user-owned independent data on lapse and make denials visible; no unrestricted platform-dependent runtime.
10. Publish only with OPS5 exact-head validated protected PR and observed independent evidence for the claimed boundary.

## Source material

- [SBEC research](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/sbec/README.md) — architecture and synthetic engineering, not billing implementation.
- [BESF study](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/besf/README.md) — cost/unit economics, no verified Multiversal invoices.
- [UADS approved baseline](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/uads/README.md) and [allowances](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/uads/CAMPAIGN_ALLOWANCES.md) — approved account/offline requirements, product tests outstanding.
- [SA-BILL study](https://github.com/cybalicistjt-stack/multiversal-aioc/pull/1918) and [current source issues](https://github.com/cybalicistjt-stack/multiversal-aioc/blob/main/governance/research-evaluations/subscription-allowance-threats-2026-11-01/CURRENT_CODE_REVIEW.md) — synthetic/static, not production security.
- [SCEV draft PR #145](https://github.com/cybalicistjt-stack/NCG/pull/145) — unmerged source comparison, no market adoption.
- [XTRA commercial preparation](https://github.com/cybalicistjt-stack/multiversal-aioc/blob/main/governance/application-planning/xtra-pre-pcv-readiness/XTRA-11_NONPUBLIC_SITE_COMMERCIAL_CONSENT_HANDOFF.md) — templates, not approval.

Related: [backlog](GATE_PROGRAM_BACKLOG.json), [GATE-01 baseline](GATE_01_BASELINE_AND_ARCHITECTURE.md), [decision register](GATE_DECISION_REGISTER.json), [acceptance cases](GATE_ACCEPTANCE_MATRIX.md), [selected work record](../../../operations/work-items/GATE-01.json).

**Source acceptance:** GATE-01 PR1952 (run41501440843, merge e51e653c, queue410); GATE-02 PR1953 (run41505626093, merge 51e8c524, queue412, 50 design-only cases). GATE-03 is CURRENT-selected source-only, with [provider-neutral contracts](GATE_03_PROVIDER_CONTRACTS.md) and [42 test fixtures](GATE_03_PROVIDER_CONTRACT_FIXTURES.json) pending separate publication. No later tranche auto-selected.
