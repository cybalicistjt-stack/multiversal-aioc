# Multiversal Content Catalog Taxonomy Integration Program

**Program ID:** CCTI  
**Status:** OWNER-APPROVED PARALLEL PROGRAM — READ-ONLY AUDIT COMPLETED_VERIFIED / ADDITIVE CANDIDATE PHASE ACTIVE  
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

Prepared-source identities are now recovered and checksum-verified from the owner-supplied `Adding.zip`:
- Item v0.12.0: `d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca`
- Platform v0.11.0: `621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6`
- Reality v0.14.0 shared seams only: `928aaacbd84082d88ea9e64fc6c3506a321f26633bce718cfb46199b5364f4d6`

Exact-source receipt: `CCTI02_EXACT_SOURCE_RECOVERY_RECEIPT_20260817.json`.

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

- Preserve original/master CSV rows; current write work is additive sidecar/projection work, not in-place rewriting.
- Existing stable IDs, identity decisions, aliases, supersession, provenance, normalization, relationships, and unresolved queues are authoritative inputs.
- Same-name does not imply same identity.
- Item Definition != live A8 Asset Instance.
- Platform Model != individual runtime asset.
- A8 retains ownership/custody/quantity/equipment/condition/damage/repair/runtime-state authority.
- Economy retains dynamic price authority.
- Legacy/source mechanics remain provenance unless rebuilt through current governed rules.
- Unknown remains unknown/review-required; do not invent completeness.
- Candidate taxonomy sidecars are not automatically enabled canonical content.
- No release, deployment, spend, production credential, public exposure, APK, shared-live expansion, or A13 authority is created.

## Program sequence

1. **CCTI-01 — Reconstruct existing corpus.** COMPLETED_VERIFIED.
2. **CCTI-02 — Recover exact taxonomy authority.** COMPLETED_VERIFIED; exact Item/Platform/Reality source packages checksum-match canonical identities.
3. **CCTI-03 — Establish shared integration model.** COMPLETED_VERIFIED for read-only audit.
4. **CCTI-04 — Build deterministic crosswalks.** COMPLETED_VERIFIED for read-only audit.
5. **CCTI-05 — Item taxonomy projection.** ACTIVE ADDITIVE CANDIDATE WORK. IAX-01 `record_scope` tranche produced 5,353 current candidate assignments, 36 reference-only holds and zero active unassigned rows; IAX-02 through IAX-10 remain unfinished.
6. **CCTI-06 — Platform projection.** Read-only exact Platform v0.11.0 alignment complete; prepared crosswalk review/adoption work remains additive candidate work.
7. **CCTI-07 — Reconcile cross-domain relationships.** Read-only signal inventory complete; governed candidate-edge resolution/adoption remains unfinished.
8. **CCTI-08 — Shared context/compatibility audit.** Read-only audit completed; reviewed candidate adoption remains unfinished.
9. **CCTI-09 — Resolve review queues/taxonomy gaps.** ACTIVE inside the additive candidate phase, beginning with Item IAX axis review states and Platform prepared crosswalk review queues.
10. **CCTI-10 — Produce governed derived catalogs.** ACTIVE only as additive candidate sidecars/projections; no source/master CSV rewrite or automatic enablement.
11. **CCTI-11 — Full corpus validation.** PLANNED; prove 11,017/11,017 accounting and all identity/provenance/boundary invariants on the finished candidate package.
12. **CCTI-12 — App-facing content integration.** OWNER-GATED / NOT STARTED; taxonomy-aware discovery/inspection/authoring through existing application authorities.

## Read-only audit closure

`CCTI-READONLY-01-attempt-001` is completed_verified. Its exact completion receipt is `CCTI_READ_ONLY_COMPLETION_RECEIPT_20260817.json`. The private audit artifact is `CCTI_ReadOnly_Integration_Audit_20260817.zip`, SHA-256 `54685f8aff2a81541dc0201285ecab5a9ae5f1bd794432e80159fd664eeee55f`.

## Active additive tranche

`CCTI-WRITE-01-attempt-001` is the active recovery state.

The first write-sidecar tranche produced:
- exact-source recovery receipt;
- Item IAX-01 candidate projection: 5,353 current rows, 36 reference-only rows, zero active unassigned;
- Object Game-Readiness program/schema and a private 11,017-row readiness ledger;
- no source/master CSV mutation, no mechanics rewrite, no runtime asset creation and no `GAME_READY` certification.

Private tranche artifact: `CCTI_Game_Readiness_Tranche1_20260817.zip`, SHA-256 `c586a01d3d542c0230d09de600995df42408532a5f604dfa02d112a724112a9f`.

## Object Game-Readiness dependency

Downstream game-readiness is governed by `OBJECT_GAME_READINESS_PROGRAM.md`. Taxonomy completeness is a prerequisite, not a substitute, for descriptive-content, mechanics, relationship, runtime, validation and playtest readiness. Before OGR-05 mechanics mutation begins, present the failing mechanics cohorts and repair policy to the owner. Runtime/app enablement retains existing Stage A gates.

## Current execution authorization

Permitted now: exact-registry-derived additive candidate taxonomy/catalog sidecars, confidence/review queues, readiness measurement artifacts, bounded governance/recovery updates, and deterministic candidate validation.

Not permitted now: source/master CSV mutation, automatic canonical enablement of candidate assignments, destructive identity/supersession changes, mechanics reauthoring, runtime asset creation/activation, release/deployment, or public publication.

## Exact next action

Continue the Item taxonomy with **IAX-02 — object_nature** as a bounded candidate sidecar using exact v0.12.0 controlled values and existing source/provenance evidence. Preserve confidence/review state and the 36 legacy-reference holds. Do not begin mechanics reauthoring in the taxonomy tranche.

## Parallel-track preservation

App PR #185 remains unfinished and held for its declared final confirmation. The currently approved tester distribution remains unchanged. DS-008 remains separately blocked. Ordinary roadmap work remains preserved while CCTI is owner-selected.
