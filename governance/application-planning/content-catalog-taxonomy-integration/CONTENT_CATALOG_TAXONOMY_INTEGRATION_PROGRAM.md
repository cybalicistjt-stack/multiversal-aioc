# Multiversal Content Catalog Taxonomy Integration Program

**Program ID:** CCTI  
**Status:** OWNER-APPROVED PARALLEL PROGRAM — READ-ONLY TRANCHE ACTIVE  
**Owner:** John Brandon Turner  
**Started:** 2026-08-17

## Purpose

Integrate the governed Content V2 corpus for Items, Vehicles, Mecha, and Spacecraft with the later Item Taxonomy v0.12.0 and Platform/Vehicle Catalog v0.11.0 systems without discarding completed identity, provenance, normalization, relationship, supersession, or unresolved-review work.

CCTI is a parallel content mission. It does not supersede post-GATX PR #185, ordinary Internal Alpha work, DS-008, or any retained track.

## Source authority

1. Current canonical repositories and A8 domain/runtime boundaries.
2. Governed Content V2 consolidation artifacts and sidecars.
3. Item Taxonomy Preparation v0.12.0 and Platform/Vehicle Catalog Preparation v0.11.0, checksum-bound through completed A8-R0.
4. Shared Reality content-context/compatibility seams adopted by A8-R0.
5. Conversation/export evidence only for provenance/recovery.

The owner-supplied `Content Consolidation.zip` was inspected read-only at session SHA-256 `cf82636489b6a5616766e0631646591bf2e558c90ef8d4529ff04aaa153969b8`; it contains fifteen nested consolidation packages.

Prepared-source identities:
- Item v0.12.0: `d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca`
- Platform v0.11.0: `621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6`
- Reality v0.14.0 shared seams only: `928aaacbd84082d88ea9e64fc6c3506a321f26633bce718cfb46199b5364f4d6`

## Corpus scope

Twelve catalogs / **11,017 records**:

- Items.csv 761
- EVA_Suits.csv 430
- Ranged_Weapons.csv 230
- Computers.csv 1,000
- Magitech_Items.csv 532
- Symbiotes_Cybernetics.csv 572
- Weapons_Ammo.csv 36 reference-only rows
- Melee_Weapons.csv 327
- Living_Spellbooks.csv 1,501
- Vehicles.csv 1,200
- Mecha.csv 2,117
- Spacecraft.csv 2,311

Item total: **5,389**. Platform-catalog total: **5,628**.

The platform catalogs contain exactly **2,984 platform/model rows**: 953 Vehicles, 930 Mecha, and 1,101 Spacecraft. The remaining **2,644 rows** are components, modules, rules/frameworks, support equipment, supplies, services, or other non-model content and must not be forced into model taxonomy assignments. Spacecraft remain first-class platform content rather than being flattened into a generic Vehicle bucket.

## Boundaries

- Preserve original/master CSV rows; no in-place rewriting during the read-only tranche.
- Existing stable IDs, identity decisions, aliases, supersession, provenance, normalization, relationships, and unresolved queues are authoritative inputs.
- Same-name does not imply same identity.
- Item Definition != live A8 Asset Instance.
- Platform Model != individual runtime asset.
- A8 retains ownership/custody/quantity/equipment/condition/damage/repair/runtime-state authority.
- Economy retains dynamic price authority.
- Legacy/source mechanics remain provenance unless rebuilt through current governed rules.
- Unknown remains unknown/review-required; do not invent completeness.
- No release, deployment, spend, production credential, public exposure, APK, shared-live expansion, or A13 authority is created.

## Program sequence

1. **CCTI-01 — Reconstruct existing corpus.** Read master rows plus identity/provenance/normalization/relationship/supersession/completeness/review sidecars.
2. **CCTI-02 — Recover exact taxonomy authority.** Recover and checksum-verify complete Item v0.12.0 and Platform v0.11.0 artifacts plus applicable shared context vocabulary; never reconstruct checksum-bound registries from memory.
3. **CCTI-03 — Establish shared integration model.** Define Items/Platforms/components/rules/creator/product-lineage/compatibility/A8/Economy boundaries.
4. **CCTI-04 — Build deterministic crosswalks.** Source row -> stable/canonical identity -> consolidation evidence -> intended taxonomy/lineage projection -> provenance/review state.
5. **CCTI-05 — Shadow-project 5,389 Items.** Use exact Item registries read-only; preserve mechanics/source fields and explicit unresolved values.
6. **CCTI-06 — Shadow-project 5,628 platform-catalog rows.** Apply Platform taxonomy to valid model rows and route 2,644 non-model rows to component/module/rules/support structures.
7. **CCTI-07 — Reconcile cross-domain relationships.** Modules, weapons, ammunition/charges, power, cargo/support, EVA, repair, upgrades, configurations, creators/manufacturers, and lineage; never create runtime installation state.
8. **CCTI-08 — Shared context/compatibility audit.** Evaluate intrinsic requirements, affinity, compatibility, and governed exceptions; produce owner decision packet.

**OWNER DECISION GATE:** CCTI-01 through CCTI-08 are approved as read-only discovery/reconciliation. No persistent corpus/taxonomy/catalog adoption begins until the owner reviews the audit and explicitly approves the proposed write package.

9. **CCTI-09 — Resolve review queues/taxonomy gaps.** Owner-gated.
10. **CCTI-10 — Produce governed derived catalogs.** Owner-gated; additive sidecars/projections only unless separately approved.
11. **CCTI-11 — Full corpus validation.** Owner-gated; prove 11,017/11,017 accounting and all identity/provenance/boundary invariants.
12. **CCTI-12 — App-facing content integration.** Owner-gated; taxonomy-aware discovery/inspection/authoring through existing application authorities.

## Current execution authorization

Permitted now: read-only inspection/comparison, hashing, aggregate metrics, crosswalk-envelope construction, non-destructive governance/audit artifacts, and roadmap/bootstrap recovery updates.

Not permitted yet: source/master CSV mutation, canonical row-level taxonomy adoption, identity/supersession changes, runtime asset creation, or CCTI-09 through CCTI-12.

## Exact-registry prerequisite

The repository currently preserves checksum identities and implementation-relevant extracts for Item v0.12.0 and Platform v0.11.0, but their complete exact archives were not found on the active session source surface during the initial audit. Deterministic row-level assignment against the complete controlled registries therefore waits for exact-byte recovery and checksum verification. CCTI-01, cross-corpus accounting, platform/model routing, sidecar reconstruction, and crosswalk-envelope work can continue meanwhile.

## Parallel-track preservation

App PR #185 remains unfinished and held for its declared final confirmation. The currently approved tester distribution remains unchanged. DS-008 remains separately blocked. Ordinary roadmap work remains preserved while CCTI is owner-selected.
