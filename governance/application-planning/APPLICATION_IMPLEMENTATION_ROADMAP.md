# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.4.0  
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

Delivered one stable subject across Personal/Campaign/Session contexts, contextual role rather than permanent Player/GM caste, zero-Campaign Personal authority, fresh context authorization and protected partitions, cadence-independent Campaign identity, and sanitized client context projection without reopening Stage A migrations `0001`–`0008`.

### CSW-I01 — COMPLETED_VERIFIED

Application PR #206; exact validated head `2836c17042bb11d52755d2589814e6b1e542867c`; repository-health `32250405319`; product validation `32250405607` with self-hosted Linux, self-hosted Windows and deterministic comparison PASS; squash merge `bebf833d59923fbfc78ba593219c727a635fc7b7`; migration head `0009_csw_creative_fragment_foundation.json`.

Delivered D29 pre-authoritative CreativeFragment identity/version/lifecycle/ownership/provenance, Personal/Campaign creative context binding, source/relationship references, exact-version incorporation receipts, recovery/tombstones/idempotency and no governed target-domain authority transfer.

### APM-I01 — COMPLETED_VERIFIED

**APM-I01 — Automated-run authority and lifecycle foundation** is complete.

Evidence:
- Application PR #207;
- exact validated head `cdf80bd30bc38a85b847b86a521dc862b654c8af`;
- application repository-health run `32252196140`: PASS;
- product validation run `32252196432`: self-hosted Linux PASS, self-hosted Windows PASS, deterministic cross-platform comparison PASS;
- squash merge `3941a06600dc1c3477d67ef2aa6ef74b0447ff28`;
- resulting migration head `database/migrations/0010_apm_automated_run_foundation.json`.

Delivered foundation:
- D04 nonhuman `automationControllerId` identity rather than Player/GM/account role;
- explicit versioned `AutomationDelegationGrant` with Personal/Campaign/Session context, capability, object, duration, step, Event, resource, visibility, feature and policy bounds;
- D04 `AutomationRun` lifecycle with deterministic pause/stop/revoke/expiry/stale/recovery/review/completion/failure barriers;
- owning-domain operation classification as `automatic_permitted`, `automatic_with_bounds`, `proposal_required`, `human_required` or `prohibited`;
- fresh owning-domain authorization for every state-affecting automated operation, so delegation is necessary but never sufficient;
- D12 lifecycle, operation-status, idempotency, payload-fingerprint, Event-reference and recovery evidence;
- recovery/status behavior that never replays already accepted ordinary domain Events;
- feature-disable/manual fallback preserving ordinary play and inspectable evidence;
- additive provider-neutral migration `0010` with automation authority/bookkeeping only, never Character/Campaign/Adventure/combat/inventory/world truth.

The initial Linux client-regression lane encountered only the existing A2 p95 performance timing fluctuation (`315.5ms` versus `250ms`) while all ten APM-I01 tests, TypeScript and Windows passed. An unchanged Linux rerun passed. No performance threshold, product assertion or validation scope was weakened.

## Current work — APW-I02

**APW-I02 — Personal Home and workspace switching** is the selected next application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I02-attempt-001`  
State: `selected_not_started`

APW-I02 implements APW-04 through the APW-08 handoff:
- a useful first-class Personal Home for a valid subject with zero Campaign memberships;
- Personal Home as an orchestrating projection over owning domains, never a Personal truth super-domain;
- safe Personal-owned versus Personal-accessible resource presentation;
- Personal/Campaign/Session context switching built on APW-I01 rather than a second context model;
- fresh authorization on every authority-partition transition;
- protected cache, realtime subscription, search, recent-work/deep-link, notification/waiting and optional-assistance context replacement when switching;
- Campaign-private data never copied into Personal authority merely for convenience or later access;
- safe stale/revoked recent-work behavior and feature-disable fallback to owning screens;
- desktop/mobile/keyboard/nonvisual context clarity.

The first APW-I02 operation is to re-fetch current application main and migration head, inspect the existing client shell/A3 APW-I01 context projection, dashboard/recent-work/Character/creator-reference surfaces and current feature/fallback patterns, then create a bounded application branch from exact current main.

Current canonical application main is `3941a06600dc1c3477d67ef2aa6ef74b0447ff28`; current migration head is `database/migrations/0010_apm_automated_run_foundation.json`. APW-I02 must independently re-fetch both before deciding whether conditional Personal workspace metadata requires another additive migration.

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

`APW-I01`, `CSW-I01` and `APM-I01` are completed_verified. `APW-I02` is selected_not_started. Every later item remains inactive until its own canonical selector transition.

## Migration and ownership policy

- migrations `0001` through `0010` are immutable predecessors once merged;
- each implementation tranche rechecks current migration head before mutation;
- no migration is required when a slice has no schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- Personal Home is projection/orchestration over established owners and cannot become a Personal truth store;
- D29 owns CSW creative-support durable records/provenance while governed payloads remain in owning domains;
- D04 owns APM controller/delegation/run authority and D12 owns automation recovery/evidence; neither replaces ordinary owning-domain state/Event history;
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

Current selection authorizes only the bounded APW-I02 application implementation tranche. It does not authorize APW-I03 or later slices, APM-I02, CSW-I02, a Personal truth super-domain, implicit Character/Campaign binding, Campaign-private data copied into Personal scope, T04 before September, tester distribution, public release/deployment, paid-provider activation, canonical publication or broad Stage A redesign.

## Mandatory execution behavior

“Continue” means execute the next verified unfinished operation. Preserve provenance, hidden-information boundaries, permissions, reversibility and owner gates.
