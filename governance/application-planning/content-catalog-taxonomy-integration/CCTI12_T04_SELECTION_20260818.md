# CCTI-12-T04 Selection — Local Review Worksets & Proposal Disposition

**Work item:** CCTI-12-T04  
**State:** `selected_not_started`  
**Selected:** 2026-08-18  
**Owner authority:** existing owner-approved bounded CCTI-12 GM/owner review/authoring integration scope  
**Predecessor:** CCTI-12-T03 `completed_verified` through Multiversal-app PR #190 / merge `59fd30d3ad38d688c18b1abe0adfb7c9a8eaffa5`

## Selection decision

The next bounded CCTI-12 integration tranche is:

**CCTI-12-T04 — Local Review Worksets & Proposal Disposition.**

T01 established candidate discovery/inspection and local review notes. T02 added a local review queue and read-only candidate comparison. T03 added structured local proposed amendments. The next useful bounded step is to let an authorized GM/owner organize those existing review objects into explicit local review worksets, record noncanonical review dispositions, and export the result for later governed processing without applying any proposal or enabling any candidate data.

This tranche is selected but is deliberately **not activated by this record**. No app branch, attempt checkpoint, implementation commit, or runtime path is created here.

## Why this is the next bounded step

The current CCTI roadmap retains two large unresolved adoption dependencies:

- Item: 91 structural-review rows and 85 additive correction proposals, with canonical adoption not ready;
- Platform: 4,326 review-required rows, with canonical adoption not ready.

The app now has enough primitives to inspect, compare, queue, and draft a correction, but it does not yet provide a coherent review-session/workset layer for turning those primitives into organized review evidence. T04 fills that gap while remaining entirely on the noncanonical side of every retained gate.

## Authorized T04 outcomes

A future T04 implementation may provide the authorized GM/owner with:

1. **Local review worksets**
   - create a named local workset from explicit candidate IDs and/or existing local queue entries;
   - preserve projection identity and stable candidate identity;
   - show workset counts by domain, review state, proposal presence, and local disposition;
   - never infer identity from display names.

2. **Local packet ingestion for review continuity**
   - load previously exported CCTI review-queue/amendment packets from the owner's device;
   - validate packet schema, projection binding, stable identities, and hard-false mutation boundaries before accepting them into local review state;
   - no upload, server persistence, publication, or canonical import path.

3. **Noncanonical review dispositions**
   - dispositions such as `unresolved`, `needs-evidence`, `retain-for-later-governed-review`, and `reject-proposal`;
   - dispositions describe review intent only and cannot mean canonical approval/adoption;
   - no bulk canonical action is permitted.

4. **Workset review navigation**
   - move from a workset entry to existing candidate inspection, comparison, review reasons, and amendment draft surfaces;
   - preserve reference-only identities without inventing Definition IDs.

5. **Local governed-review export**
   - export workset membership, proposal references, review notes/dispositions, projection identity, stable subject identity, optional current Definition identity, and provenance references;
   - every export must keep proposal application, taxonomy enablement, canonical mutation, relationship promotion, compatibility finalization, runtime Asset mutation, mechanics mutation, release, and deployment requests false.

## Explicit non-goals / retained gates

T04 does **not** authorize:

- applying a T03 amendment to the loaded candidate projection;
- Item or Platform taxonomy enablement/adoption;
- accepting a local disposition as canonical approval;
- promotion of the 260 relationship candidates;
- compatibility finalization;
- source/master CSV mutation;
- identity or supersession rewrite;
- A8 runtime Asset creation/activation/mutation;
- mechanics reauthoring;
- Player-facing canonical exposure;
- release, deployment, tester-distribution replacement, paid-provider, credential, or public authority;
- supersession or merge of Multiversal-app PR #185;
- activation of DS-008 or ordinary Stage A.

## Expected acceptance boundary when T04 is later activated

A T04 implementation should not be mergeable as `completed_verified` unless its exact final head proves:

- GM/owner authorization and Player/default-route isolation;
- deterministic validation of imported local packets and projection binding;
- workset membership keyed by explicit candidate IDs;
- reference-only identity preservation;
- local disposition semantics that cannot be mistaken for canonical approval;
- no mutation of the loaded candidate projection;
- hard-false mutation/enablement/promotion/compatibility/runtime/mechanics/release boundaries in exported review evidence;
- full client regression, typecheck, accessibility, build, DT-008 design-system compliance, and bounded Player/runtime separation;
- final validation routed under `MV-AI-VALIDATION-003` on the applicable self-hosted exact-head gate(s), with deterministic cross-platform comparison if T04 creates a cross-platform artifact expected to be identical.

## Exact next action

**Stop here until T04 is intentionally activated.**

When execution is authorized/resumed, create a new `CCTI-12-attempt-004` start checkpoint and a dedicated Multiversal-app branch from the then-current canonical `main`, then construct the complete T04 tranche before running its finished-step validation gate.
