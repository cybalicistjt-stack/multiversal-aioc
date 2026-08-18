# Multiversal Content Catalog Taxonomy Integration Program

**Program ID:** CCTI  
**Status:** OWNER-APPROVED PARALLEL PROGRAM — CANDIDATE PACKAGE VALIDATED / CCTI-12 OWNER GATE  
**Owner:** John Brandon Turner  
**Started:** 2026-08-17  
**Updated:** 2026-08-18

## Purpose

Integrate the governed Content V2 corpus for Items, Vehicles, Mecha, and Spacecraft with the later Item Taxonomy v0.12.0 and Platform/Vehicle Catalog v0.11.0 systems without discarding completed identity, provenance, normalization, relationship, supersession, or unresolved-review work.

CCTI is a parallel content mission. It does not supersede post-GATX PR #185, ordinary Internal Alpha work, DS-008, or any retained track.

## Source authority

1. Current canonical repositories and A8 domain/runtime boundaries.
2. Governed Content V2 consolidation artifacts and sidecars.
3. Item Taxonomy Preparation v0.12.0 and Platform/Vehicle Catalog Preparation v0.11.0, checksum-bound through completed A8-R0.
4. Shared Reality content-context/compatibility seams adopted by A8-R0.
5. Conversation/export evidence only for provenance/recovery.

The owner-supplied `Content Consolidation.zip` was inspected at SHA-256 `cf82636489b6a5616766e0631646591bf2e558c90ef8d4529ff04aaa153969b8`.

Prepared-source identities are checksum-verified from owner-supplied `Adding.zip` SHA-256 `a550ed965e4433dc9a3d800ef7aebda4f699c363db8ef8037d104a4a844d6277`:

- Item v0.12.0: `d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca`
- Platform v0.11.0: `621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6`
- Reality v0.14.0 shared seams: `928aaacbd84082d88ea9e64fc6c3506a321f26633bce718cfb46199b5364f4d6`

Exact-source receipt: `CCTI02_EXACT_SOURCE_RECOVERY_RECEIPT_20260817.json`.

## Corpus scope

Twelve catalogs / **11,017 records**:

- Items.csv — 761
- EVA_Suits.csv — 430
- Ranged_Weapons.csv — 230
- Computers.csv — 1,000
- Magitech_Items.csv — 532
- Symbiotes_Cybernetics.csv — 572
- Weapons_Ammo.csv — 36 reference-only rows
- Melee_Weapons.csv — 327
- Living_Spellbooks.csv — 1,501
- Vehicles.csv — 1,200
- Mecha.csv — 2,117
- Spacecraft.csv — 2,311

Item total: **5,389**. Platform-domain total: **5,628**.

The Platform catalogs contain exactly **2,984 platform/model/named-asset/archetype rows** and **2,644 component/module/rules/support/service/non-model rows**. Spacecraft remains first-class Platform content rather than being flattened into a generic Vehicle bucket.

## Permanent boundaries

- Preserve original/master CSV rows; CCTI candidate work is additive sidecar/projection work, not in-place rewriting.
- Existing stable IDs, identity decisions, aliases, supersession, provenance, normalization, relationships, and unresolved queues are authoritative inputs.
- Same-name does not imply same identity.
- Item Definition != live A8 Asset Instance.
- Platform Model != individual runtime Asset.
- A8 retains ownership/custody/quantity/equipment/condition/damage/repair/runtime-state authority.
- Economy retains dynamic price authority.
- Legacy/source mechanics remain provenance unless rebuilt through current governed rules.
- Unknown remains unknown/review-required; do not invent completeness.
- Candidate taxonomy sidecars are not automatically enabled canonical content.
- Compatibility does not imply current installation, equipment, carriage, ownership, attachment, availability, legality, commonness, price, or narrative importance.
- No release, deployment, spend, production credential, public exposure, APK, shared-live expansion, or A13 authority is created.

## Program sequence and verified state

1. **CCTI-01 — Reconstruct existing corpus.** `COMPLETED_VERIFIED`.
2. **CCTI-02 — Recover exact taxonomy authority.** `COMPLETED_VERIFIED`.
3. **CCTI-03 — Establish shared integration model.** `COMPLETED_VERIFIED`.
4. **CCTI-04 — Build deterministic crosswalks.** `COMPLETED_VERIFIED`.
5. **CCTI-05 — Item taxonomy projection.** `COMPLETED_VERIFIED` at candidate-disposition level: IAX-01 through IAX-10 complete across 5,389 rows; taxonomy disabled/noncanonical.
6. **CCTI-06 — Platform projection.** `COMPLETED_VERIFIED` at candidate-disposition level: all seven universal Platform facets complete across 5,628 rows; exact 2,984/2,644 routing preserved; taxonomy disabled/noncanonical.
7. **CCTI-07 — Reconcile cross-domain relationships.** Candidate graph tranche complete: 216 canonical resolved relationships preserved, 260 new review-only candidate edges, 96 withheld ambiguous/common-term signals; no runtime-instance state claims.
8. **CCTI-08 — Shared context/compatibility audit and candidate layer.** Candidate tranche complete using the exact 9-facet / 241-value shared authority across 11,017 rows; all compatibility outcomes remain `NOT_EVALUATED`; nothing enabled.
9. **CCTI-09 — Resolve review queues/taxonomy gaps.** Candidate review stage complete: Item cross-axis review has 91 structural-review rows and 85 additive correction proposals; Platform cross-facet review retains 4,326 review-required rows. Item and Platform adoption remain not ready.
10. **CCTI-10 — Produce governed derived catalogs.** Completed at additive candidate-sidecar/projection level; no source/master rewrite or automatic enablement.
11. **CCTI-11 — Full corpus validation.** `COMPLETED_VERIFIED` through AIOC PR #379 / merge `0ab03915b88e1c297e974855388728eaf9ed98ff`. Candidate-package accounting, identity/provenance, controlled-registry integrity, Platform routing, candidate-relationship endpoints, shared-context integrity, and Definition/Model-versus-runtime-Asset boundaries validated across 11,017 rows.
12. **CCTI-12 — App-facing content integration.** **OWNER-GATED / NOT STARTED**. Taxonomy-aware discovery/inspection/authoring through existing application authorities must not begin without explicit owner approval and a bounded activation scope.

## Item taxonomy adoption dependency

The Item candidate pass is complete, but canonical adoption is **NOT READY**.

Before enablement:

1. preserve all ten sealed historical candidate tranches;
2. apply the 85 cross-axis corrections as a new adoption overlay;
3. recover original IAX-06/IAX-07/IAX-08 row-level evidence at the sealed hashes or produce explicitly versioned superseding reprojections;
4. rebuild one complete 5,389-row ten-axis adoption ledger;
5. rerun deterministic adoption validation and present unresolved/review cohorts;
6. obtain explicit owner approval.

## Platform taxonomy adoption dependency

The Platform candidate pass is complete, but canonical adoption is **NOT READY**.

Before enablement:

- preserve all seven facet candidate/disposition records;
- preserve the 4,326-row cross-facet review queue and all explicit unresolved/host-dependent/preparation-gap states;
- resolve or explicitly accept the retained review cohorts through a governed adoption package;
- retain shared Genre/Technology and other systemic deferrals unless separately resolved;
- obtain explicit owner approval.

## Relationship candidate dependency

The 260 new cross-domain edges remain **candidate review evidence only**. They do not alter the canonical relationship registry and do not establish runtime Asset-instance state. Promotion requires separate governed review/approval.

## Shared context / compatibility dependency

The exact 241-value shared authority is integrated only as a candidate evidence layer. Source Genre/Technology/Environment strings remain provenance. Intrinsic identity, affinity, and compatibility remain separate. All final compatibility outcomes remain `NOT_EVALUATED`.

## CCTI-11 validation evidence

Canonical report:
`CCTI11_FULL_CANDIDATE_VALIDATION_REPORT_20260818.md`

Completion receipt:
`CCTI11_COMPLETION_RECEIPT_20260818.json`

Private deterministic validation artifact:
`CCTI11_Full_Candidate_Validation_20260818.zip`  
SHA-256 `f30ca0e3b0927c6909dbb0da82c66186dadbfc5de6df5128b279719459b70595`.

## Object Game-Readiness dependency

Downstream game-readiness remains governed by `OBJECT_GAME_READINESS_PROGRAM.md`. Taxonomy completeness is a prerequisite, not a substitute, for descriptive-content, mechanics, relationship, runtime, validation and playtest readiness. The current 11,017-row baseline certifies **zero** rows `GAME_READY`.

Before OGR-05 mechanics mutation begins, present the failing mechanics cohorts and repair policy to the owner. Runtime/app enablement retains existing Stage A gates.

## Current execution authorization

Completed authorization covered exact-registry-derived additive candidate taxonomy/catalog sidecars, confidence/review queues, readiness measurement artifacts, governed candidate relationship/context layers, bounded governance/recovery updates, and deterministic candidate validation.

Still **not permitted without a new owner gate**:

- CCTI-12 app-facing integration;
- source/master CSV mutation;
- automatic canonical enablement of Item or Platform candidate assignments;
- promotion of relationship candidates;
- final compatibility determination;
- destructive identity/supersession changes;
- mechanics reauthoring;
- runtime Asset creation/activation;
- release/deployment/public publication.

## Exact next action

**STOP at CCTI-12 owner gate.** Do not activate app-facing integration until John explicitly approves the bounded CCTI-12 scope.

## Parallel-track preservation

- Multiversal-app PR #185 remains unfinished/validation-failed and held at its declared successor-distribution boundary.
- The currently approved tester distribution remains unchanged.
- DS-008 remains separately `blocked_non_owner`.
- Ordinary Stage A roadmap work remains preserved while CCTI is selected.
