# Current code and authority review — SA-BILL-01
**Date:** 2026-11-01 · Static code review against Multiversal-app `main` at start of study. This is NOT a demonstrated production exploit or independent installed security test.

## Exact source paths
- `cybalicistjt-stack/Multiversal-app/packages/contracts/src/identity-device/entitlement-evaluator.ts`
- `cybalicistjt-stack/Multiversal-app/packages/entitlements/src/entitlement-service-port.ts`
- `cybalicistjt-stack/Multiversal-app/packages/contracts/src/authorization/campaign-authorization-policy.ts`
- `cybalicistjt-stack/Multiversal-app/packages/contracts/src/a3/context-authority.ts`
- `cybalicistjt-stack/Multiversal-app/packages/contracts/src/optional-ai/ai-budget-policy-port.ts`
- `cybalicistjt-stack/multiversal-aioc/governance/application-planning/internal-alpha/INTERNAL_ALPHA_SHARED_SYSTEMS.md`
- `cybalicistjt-stack/multiversal-aioc/governance/application-planning/internal-alpha/IA-D08-004_OFFLINE_DEFERRAL_READINESS.md`
- `cybalicistjt-stack/multiversal-aioc/governance/application-planning/internal-alpha/feature-packets/MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md`

## Findings in the actual current evaluator (not speculative source code)

**CR-01 — Billing cancellation conflates renew intent with effective access (HIGH).** The subscription record has only `status: active | cancelled | expired`; `evaluateEntitlements` grants subscription only for `status === "active"`. A paid-up user marked `cancelled` at cancellation request loses subscriber capabilities immediately even if `endsAt` lies in the future. It may be possible for ingestion to preserve `active` until expiry, but that convention is neither explicit nor enforced. Required: separate `autoRenew` from effective paid entitlement interval and provider cancellation status.

**CR-02 — String-based time comparisons rather than parsed instants (HIGH).** `activeWindow` uses `startsAt <= at` and `at < endsAt` on strings; sponsored grants and next-change sorting also use string ordering. It is correct for consistently canonical UTC timestamps, but fails safely only if every source has already enforced identical normalized timestamp formats. Mixed offset strings or invalid dates can yield wrong authorization or expiry order. Required: validate and normalize instants to server epoch milliseconds before evaluation; reject invalid times, zero/negative windows and client clocks.

**CR-03 — Campaign-less sponsored-month evaluation may widen scope (HIGH conditional).** A sponsored-month record is included when `input.campaignId === undefined || record.campaignId === input.campaignId`; if a caller omits Campaign context, sponsored access from *any* campaign counts toward `tier: subscriber`, `subscriber-ability-tiers` and `campaign-premium-content`. May be intentional for a standalone sponsored-month model, but it conflicts with the campaign-only owner allowance unless explicitly segregated. Required: define global sponsored-month vs Campaign allowance as different grant types with incompatible scopes and enforce campaign-bound queries for the latter. Do not change sponsored-month semantics without owner policy.

**CR-04 — No one-slot allowance record or content root/dependency structure (CRITICAL design gap).** `CampaignPremiumGrantRecord` contains grantId, campaignId, subjectId, startsAt, endsAt and revokedAt only. No issuer GM ID, current GM subscription reference, selected root kind/release/version, recursive dependency closure, slot ID, per-Campaign uniqueness or transfer policy. This model cannot by itself enforce the 2026-10-27 one-allowance owner directive. Required: distinct `CampaignAllowanceSlot` owner ledger and DB unique constraint/CAS.

**CR-05 — Grant records are input data, not payment proof (HIGH boundary).** `EntitlementEvaluationInput` receives arrays of records; `EntitlementServicePort` accepts a list of grants and exposes record/revoke. Neither code shape verifies store signatures, canonical purchase ownership or immutable GM authority. This is normal for a pure evaluator/port; security depends on a genuine backend owner path, **not a proven vulnerability in a production endpoint**. Required: verify exact producing service and test direct spoofed grant requests fail.

**CR-06 — Capabilities cannot express selected granted resource (HIGH).** Evaluator exposes only `official-content`, `subscriber-ability-tiers`, and `campaign-premium-content`. Any active Campaign grant yields generic premium-content capability. It cannot distinguish the Setting+dependencies from Species/item set/tree or enforce a local Character-only allowed projection. Required: resource-scoped entitlement decision with registered roots, closure and usage action checks.

**CR-07 — Role policy is separate from subscription (EXPECTED).** `authorizeCampaignRequest` checks owner/GM/player membership and `CampaignAction` but no paid entitlement or allowance; owner bypasses membership check for ownerSubjectId. This is a legitimate domain boundary, but a caller must combine the canonical role decision with billing and grant issuer eligibility rather than treating GM role or Campaign ownership as paid authority.

**CR-08 — Cache and offline grant implementation not established by these contracts (HIGH proof gap).** A3 context partitioning preserves per-subject/per-context scopes, but does not cryptographically bind premium offline leases, device decryption keys or remote revocation epochs. IA-D08-004 explicitly defers unrestricted offline entitlement mutation. Required physical encrypted offline tests and bounded read-only leases; no fake instantaneous disconnected revocation claim.

**CR-09 — Duplicates and source revisions not enforced by pure evaluator (MEDIUM).** Multiple duplicate subscription IDs or grant IDs can appear in `activeRecordIds`. There is no purchaser receipt uniqueness, provider event version or monotonic revocation; call site/backing ledger must enforce. Required unique source keys and idempotent transactional tests.

**CR-10 — AI budget preview port is not billing implementation (MEDIUM).** `AiBudgetPolicyPort` supports estimated cost, confirmation and hard-limit decisions but explicitly does not authorize billing. Include adversarial opt-in/cost tests and avoid any subscription claim that generative model usage is automatically free/unlimited.

## Suggested verification hooks
1. Introduce an isolated pure evaluator for `BillingAgreement -> verified EntitlementDecision`, with normalized UTC time, cross-platform provider test vectors, provider-revision ordering and no payment credentials in client projections.
2. Add CampaignAllowanceSlot DB uniqueness and idempotent create/replace/revoke in authoritative service; try 100 concurrent sends to same `(campaign,subject)`.
3. Query every protected destination by `(subject,campaign,registered_release,scope,source_digest,decision_revision)`. Inspect nested Character/Setting/Species/item provenance instead of only top-level pickers.
4. Add browser/network negative tests for search/autocomplete/count/AI/export/subscription before and after GM downgrade, membership loss and grant retargeting.
5. Test real Android/Windows installs for two-device identity, stale encrypted cache and restoration; admit unresolved physical/remote limitations honestly.

## Required sequencing / no product mutation
This study is advisory and no current GPR/PCV-03F, MTLC-14 or AXI selectors or code were changed. Implement only under an explicitly authorized future scope and exact-head protected PR. Do not treat a static finding as a confirmed exploit or source fixture as live commerce.