# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.5.0  
**Status:** ACTIVE — COMBINED WORKSPACE IMPLEMENTATION  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and purpose

This is the concise current application roadmap. Historical revisions remain in Git history and receipts; they are not current-work selectors. Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence.

## Completed verified foundations

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06 and POST-GATX-SUCCESSOR are **COMPLETED_VERIFIED**.

The APW/APM/CSW design series is **COMPLETED_VERIFIED** through APW-08, APM-06 and CSW-10.

## Combined implementation progress

### APW-I01 — COMPLETED_VERIFIED

Application PR #205; exact validated head `2814de3c08e62f8fc6b857f5f43800f3106615dd`; repository-health `32248201457`; product validation `32248201728` with self-hosted Linux, self-hosted Windows and deterministic comparison PASS; squash merge `e1f074bb44b89ade0ab27da205043e2681d2a1be`.

Delivered stable Personal/Campaign/Session contextual authority without permanent Player/GM account caste, zero-Campaign Personal authority, fresh context authorization and sanitized client context projection.

### CSW-I01 — COMPLETED_VERIFIED

Application PR #206; exact validated head `2836c17042bb11d52755d2589814e6b1e542867c`; repository-health `32250405319`; product validation `32250405607` with self-hosted Linux, self-hosted Windows and deterministic comparison PASS; squash merge `bebf833d59923fbfc78ba593219c727a635fc7b7`; migration `0009_csw_creative_fragment_foundation.json`.

Delivered D29 pre-authoritative CreativeFragment identity/version/lifecycle/ownership/provenance, Personal/Campaign creative context binding, exact-version incorporation receipts and recovery/idempotency without moving governed target-domain authority into CSW.

### APM-I01 — COMPLETED_VERIFIED

Application PR #207; exact validated head `cdf80bd30bc38a85b847b86a521dc862b654c8af`; repository-health `32252196140`; product validation `32252196432` with self-hosted Linux, self-hosted Windows and deterministic comparison PASS; squash merge `3941a06600dc1c3477d67ef2aa6ef74b0447ff28`; migration `0010_apm_automated_run_foundation.json`.

Delivered D04 nonhuman automation controller/delegation/run authority, D12 recovery/evidence, owning-domain operation classification, fresh execution-time authorization, deterministic lifecycle barriers, idempotent recovery and manual/no-AI fallback without a second state engine.

### APW-I02 — COMPLETED_VERIFIED

**APW-I02 — Personal Home and workspace switching** is complete.

Evidence:
- Application PR #208;
- exact validated head `d5463609176916f146e6f8de2eea2e3d17dadffb`;
- application repository-health run `32255424927`: PASS;
- product validation run `32255425519`: self-hosted Windows PASS, self-hosted Linux PASS after an unchanged retry of an unrelated A2 timing fluctuation, deterministic cross-platform comparison PASS;
- squash merge `c5c4e8962c388c462b5da00b7a8ec788d0932d08`;
- migration head remains `database/migrations/0010_apm_automated_run_foundation.json`; APW-I02 added no migration.

Delivered foundation:
- first-class useful Personal Home for a valid zero-Campaign subject;
- ten baseline Home areas covering Continue, Characters, Creative Library, Practice/Sandbox, Reference, Invitations, Waiting, Campaigns, portability and account/entitlement entry;
- Personal Home as a projection over already-authorized A3/APW-I01 data, never a Personal truth super-domain;
- explicit Personal-owned versus Personal-accessible resource classification retaining owner-domain identity;
- Campaign-bound Character, Campaign and Session references never become Personal-owned by appearing on Home;
- client Personal Home state omits stable subject/session IDs and permission/entitlement evidence identifiers;
- Campaign/Character/Session → Personal return remounts the current alpha shell, destroying protected in-memory state and requiring fresh Personal authorization;
- protected workspace entry still uses the existing A3 fresh authorization path;
- stale/revoked Campaign references disappear from a newly authorized Personal Home without leaking labels, counts or protected-existence errors;
- feature-disable fallback restores the predecessor A3 dashboard without deleting or moving owner-domain data;
- route-colliding Home headings use distinct nonvisual accessible names while retaining familiar visible labels.

APW-I02 preserved its failed→repaired validation history: duplicate Home/dashboard composition, a changed stable `Open` control and Home/destination heading ambiguity were repaired before final validation. The final Linux run initially encountered the existing A2 performance timing fluctuation (`330.24ms` versus `250ms`) while APW-I02 behavior and Windows passed; an unchanged rerun passed. No performance threshold, assertion or validation scope was weakened.

## Current work — APW-I03

**APW-I03 — Asynchronous Action submission, durable GM inbox and delayed resolution** is the selected next application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I03-attempt-001`  
State: `selected_not_started`

APW-I03 implements APW-02/APW-07 by extending the existing Stage A A6 proposal/decision/Event architecture:

- submitted Action proposals remain durably pending across disconnect, time and device boundaries;
- one stable `proposalId` is one intent thread and may produce at most one final authoritative outcome;
- proposal revisions remain versioned/provenance-preserving and use fresh state-changing operation identities;
- withdrawal, revocation, server-governed expiry, clarification and stale/review-required states are explicit barriers rather than silent rewrites;
- GM inbox rows, counts and ordering are permission/visibility-filtered before aggregation;
- inbox position or an optional review lease never grants decision authority;
- final decision reauthorizes current reviewer, exact proposal version, Session/Character/target versions, rules/pack/schema, entitlement, resource and hidden-information state;
- authoritative persistence, not disabled UI controls, enforces at-most-one final decision and at-most-one resulting gameplay Event;
- submission/decision ambiguity uses operation/proposal/decision status lookup before retry;
- reconnect recovers current proposal/final status plus missed Events without blindly resending state-changing commands;
- notifications/deep links are safe attention signals only and require fresh authorization before protected detail;
- normal manual submit/review/decision behavior remains usable without AI.

The first APW-I03 operation is to re-fetch current application main and migration head, inspect live A6 proposal/decision persistence, operation/status/idempotency, reconnect/Event-cursor, D05 filtering and safe-notification seams, then decide whether the verified `0010` baseline actually requires an additive `0011` migration.

Current canonical application main is `c5c4e8962c388c462b5da00b7a8ec788d0932d08`; current migration head is `database/migrations/0010_apm_automated_run_foundation.json`.

## Design handoff evidence

Final design handoff evidence remains:
- CSW-10: PR #449 / repo-health `32237196497` / merge `d27a6774470261450f41e1591580c7feba174cee`;
- APW-07: PR #451 / repo-health `32237975517` / merge `e9592399eaca07d0cdf28b79320fc6bf59bde5ef`;
- APM-06: PR #453 / repo-health `32244745957` / merge `9396ce2ec6094982d292eb4a630036c641094904`;
- APW-08: PR #455 / exact head `f6263185682ec04c948ef865d8f5f3b674b6e825` / repo-health `32245783537` / merge `608e3ddde4b634a1d545856cfd6cb3b2c273fbc7`.

The design series produced a 21-slice additive implementation program, migration/touch-point inventory, six incremental Internal Alpha milestones, cross-program blocking acceptance cases, feature/fallback/no-AI requirements and explicit Stage A non-reopening rules.

## Combined implementation handles

### APW
APW-I01 through APW-I07.

### CSW
CSW-I01 through CSW-I08, with D29 `authoring-provenance` as the initial creative-support persistence owner and explicit receipt-bound governed incorporation.

### APM
APM-I01 through APM-I06, with bounded automation over ordinary owning-domain/Event authority and complete no-AI recovery paths.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

`APW-I01`, `CSW-I01`, `APM-I01` and `APW-I02` are completed_verified. `APW-I03` is selected_not_started. Every later item remains inactive until its own canonical selector transition.

## Migration and ownership policy

- migrations `0001` through `0010` are immutable predecessors once merged;
- each implementation tranche rechecks current migration head before mutation;
- `0011` is not reserved and may be used by APW-I03 only if live A6 persistence inspection proves an additive schema delta is required;
- no migration is required when a slice has no schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- Personal Home remains projection/orchestration over established owners;
- D29 owns CSW creative-support durable records/provenance while governed payloads remain in owning domains;
- D04 owns APM controller/delegation/run authority and D12 owns automation recovery/evidence; neither replaces ordinary owning-domain state/Event history;
- APW-I03 must extend the existing A6/D21 proposal/decision/Event persistence rather than create a parallel asynchronous truth store;
- authorization/visibility filtering precedes count/search/topology/notification/export/diagnostic/AI aggregation.

## Internal Alpha implementation milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06.
6. Whole-system hybrid proof — APW-I07.

Tester distribution remains separately owner-gated.

## Deferred work — CCTI-12-T04

CCTI-12-T04 remains unfinished and owner-deferred until September 2026 under `governance/ai/runtime/OWNER_DECISION_2026-08-18_DEFER_CCTI12_T04_TO_SEPTEMBER.md`. Preserve App PR #191 and its clean reconstruction branch as provenance only. On/after 2026-09-01 first establish the owner-approved GitHub-hosted validation route or explicit bounded exception before reevaluation.

## Other preserved unfinished work

- **WP-011:** special Mac-environment work; may temporarily preempt when the required borrowed Mac is available.
- **DS-008:** blocked non-owner exact-byte transfer/validation; checksum-bound content must never be reconstructed from excerpts/OCR/memory.

## Permanent completion and validation rules

- Only evidence-backed `completed_verified` is complete.
- Artifact existence or partial tests never establishes completion.
- A failed required validation leaves the slice unfinished.
- Normal application/package final acceptance uses owner-controlled self-hosted Windows + Linux plus deterministic comparison where outputs should agree, unless a bounded owner-approved exception explicitly applies.
- Exact-head AIOC repository health is governance evidence, not a substitute for product/platform gates.
- One stable operation ID represents one authoritative intent across retries; accepted effects are at-most-once.
- Successor work does not reopen completed Stage A evidence unless fresh independent evidence proves a predecessor regression.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear, confident and restrained; never obsequious.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work.

## Nonauthorization

Current selection authorizes only the bounded APW-I03 application implementation tranche. It does not authorize APW-I04 or later slices, APM-I02, CSW-I02, an alternate asynchronous rules/state engine, queue-position or review-lease authority, AI/automation GM authority, unrestricted offline multi-writer mutation, broad notification-provider implementation, T04 before September, tester distribution, public release/deployment, paid-provider activation, canonical publication or broad Stage A redesign.

## Mandatory execution behavior

“Continue” means execute the next verified unfinished operation. Preserve provenance, hidden-information boundaries, permissions, reversibility and owner gates.
