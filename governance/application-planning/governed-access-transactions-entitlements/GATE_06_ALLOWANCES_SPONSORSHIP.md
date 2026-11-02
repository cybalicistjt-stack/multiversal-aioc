# GATE-06 — Campaign Allowances, Sponsored Month and restricted lineage
**Status:** source-only design; no product, provider, database, security or native implementation certification. **Owner authority:** UADS Oct 27 approved account/offline baseline and Campaign Allowances requirements. GATE-02 resource policy, GATE-05 PostgreSQL schema are published source-only designs.

## Four distinct rights
- **Personal subscriber:** finite, account-scoped paid entitlement. Campaign role, source license, GM privacy and character ownership remain independent.
- **Account-scoped Sponsored Month:** legitimately verified account-subject sponsored subscription for its authorized finite period. Not automatically a campaign/content root allowance, not transferable to a shared-mailbox account, and not proof of GM role. The old app record may include a campaign origin; this does not make the sponsored entitlement equivalent to an allowance. Purchase, issuance, sponsor-GM eligibility and billing policy remain pending.
- **Campaign Allowance:** subscribed, authorized GM issues one slot to a single permanent player subject in a single Campaign for one selected resource root plus its exact required transitive dependencies. It permits only Campaign-scoped authorized actions and never creates `tier:subscriber`, unrestricted catalog access or a transferable license.
- **Retained character projection:** owner-approved separate, narrowly scoped inspection of a player's lawful Campaign character and possessions outside an active Session, including after runtime allowance loss. It excludes GM-secret data, unrestricted source packages, new item spawning, protected runtime execution and library exports. Account security remains binding.

## Issuance and database invariants
The server obtains the GM principal from authenticated authority, verifies Campaign GM role and *subscribed issuer* eligibility, verifies beneficiary membership, content sharing license, typed root, trustworthy manifest source and required dependency closure, then issues a versioned grant and outbox atomically. The unique slot is `(campaign_id, beneficiary_subject_id)` in GATE-05's **proposed** PostgreSQL schema; device, username, character and issuing GM never form additional quota keys. Competing issuances must resolve by DB uniqueness, not client or preflight-only checks. Tombstones remain; no root swapping, grant stacking or deleting/recreating a revoked slot. Valid required dependencies consume the same single slot.

Required closure verifies rooted manifest version, signed source/license provenance, stable resource IDs, cycles, missing/untrusted/unauthorized required edges, and records a canonical digest. Optional/recommended edges, human prose links and arbitrary URLs are not automatically included. Root updates require an explicit versioned authorized replacement policy, not silent scope expansion; a missing dependency fails rather than pretending a setting is usable.

## Authorization and resource provenance
At *every* API/service/native decision verify subject+session/device, Campaign ID and membership, GM/player role, resource license and visibility, entitlement cause/time/action, grant/manifest version, and provenance. Subject-paid subscriber access never overrides a source restriction. For a Campaign Allowance only the verified root closure is usable in the eligible Campaign; unrelated trees, third-party definitions and general source browsing remain denied.

Carry authoritative `campaign_id`, `beneficiary_subject_id`, `allowance_id+grant_version`, `root_id+version`, `closure_digest`, source pack/lineage identifiers and `transfer_scope=campaign-character-only` through Definition → Variant → Placement → Instance → Snapshot, nested inventory, ability/item sets, search/AI outputs, synced records and backup/import/export paths. Reauthorize **both source and destination** at each materialization. Missing, stripped or unknown lineage fails closed. Renaming, new IDs, wrapping in authored text, new device, personal subscription or cross-Campaign copy cannot launder restricted content.

A restricted item may be removed from a character in ordinary Campaign gameplay while keeping restrictions, but this allowance creates **no right to transfer it even to another character in the same Campaign**. An explicitly later-defined GM reassignment would need independent authorized source/destination controls.

Preserve independently owned text/media for lawful access or export after subscription lapse, but separate it from protected run-dependent packages and mixed-content restricted exports; no protected-runtime-free substitute.

## Grant lifecycle and unresolved owner policy
Initial subscribed-GM **issuance** and one-slot scope are owner-approved. Ongoing GM-subscription qualification for already-issued allowances is **recommended, not yet owner-ratified**. If adopted later, a known issuer lapse could suspend future allowance-runtime while preserving character view and history; a different subscribed GM taking over/reissuing under the *same* slot would require a separate audited procedure. No self-service replacement, automatic root swap or unbounded gift program is approved.

Sponsored Month purchase/price/renewal and whether sponsorship qualifies GM issuance are pending. Refund, expired-paid period, notice and grace choices also remain GATE-04/08/owner decisions. Do not infer them from an existing `sponsored-month` type.

## Offline seam for GATE-07
Approved behavior: after initial online verification, the unchanged signed-in account/device can use its previously authorized scoped encrypted cache offline within the finite verified authorization. Campaign lease additionally binds exact Campaign, beneficiary, GM issue evidence, allowance version, action/root/manifest digest and installation. Separate retained-character read keys from runtime/content-definition keys. Known revocation or account switch locks supported offline continuity; a timeout alone does not cancel a still-valid lease. Early remote revocation cannot be learned on a disconnected device; compromised client/plaintext remain residual risks. **No cryptographic test or device implementation is claimed.**

## Acceptance cases and evidence debt
[GATE-06 reference fixtures](GATE_06_POLICY_FIXTURES.json) and `scripts/gate06_reference_oracle.mjs` define 78 synthetic decisions across subscribed GM issuance, exact Campaign/root usage, sponsor subject binding, restricted transfer, retained projection and offline scope, and 12 graph closure cases (cycles, missing, untrusted/unlicensed, shared required dependency, optional excluded). Every fixture uses assumed verified booleans and is **not** a signature, PostgreSQL concurrency, device or real service test.

Real UADS CA01–CA12 remain NOT_RUN: 100 simultaneous GM/DB slot requests, Raven1/Raven2 identity isolation, nested pack closure updates, expiry/GM lapse, restricted object transfer/import/export, AI/search derived-content laundering, real Windows/Android offline key/grant binding and signed revocation. GATE-09/11/12 require separately selected product/security authority.

## Source hierarchy
1. Owner-approved [UADS Campaign Allowances](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/uads/CAMPAIGN_ALLOWANCES.md) and [Account/Device/Entitlement design](https://github.com/cybalicistjt-stack/NCG/blob/main/docs/uads/ACCOUNT_DEVICE_ENTITLEMENT_DESIGN.md), dated 2026-10-27.
2. Published GATE-02 membership policy, GATE-05 ledger design, GATE-04 period policy, GATE-03 provider binding in this repo.
3. Existing app `packages/contracts/src/identity-device/entitlement-evaluator.ts` and `packages/entitlements/src/entitlement-service-port.ts` are limited typed source interfaces, **not** complete allowance scope enforcement.
4. NCG SBEC is research and not independent product/commercial authority.
