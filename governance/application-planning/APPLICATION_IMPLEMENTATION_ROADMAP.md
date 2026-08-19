# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.6.0  
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

Application PR #208; exact validated head `d5463609176916f146e6f8de2eea2e3d17dadffb`; repository-health `32255424927`; product validation `32255425519` with self-hosted Windows PASS, self-hosted Linux PASS after an unchanged retry of an unrelated A2 timing fluctuation and deterministic comparison PASS; squash merge `c5c4e8962c388c462b5da00b7a8ec788d0932d08`; no new migration.

Delivered first-class zero-Campaign Personal Home, ten baseline Home areas, Personal-owned versus Personal-accessible resource classification, fresh protected workspace entry, Campaign/Character/Session → Personal protected-state destruction, stale/revoked reference omission, feature-disable dashboard fallback and distinct nonvisual route-area naming without creating a Personal truth super-domain.

Its failed→repaired history remains preserved: duplicate Home/dashboard composition, changed stable `Open` control and Home/destination heading ambiguity were repaired before final validation. The final Linux run initially encountered the existing A2 performance fluctuation and passed on an unchanged rerun; no threshold, assertion or validation scope was weakened.

### APW-I03 — COMPLETED_VERIFIED

**APW-I03 — Asynchronous Action submission, durable GM inbox and delayed resolution** is complete.

Evidence:
- Application PR #209;
- exact validated head `9b6da9236e9f01003ef4dddccd5edced8359fda1`;
- application repository-health run `32258970144`: PASS;
- product validation run `32258970575`: self-hosted Windows PASS, self-hosted Linux PASS after an unchanged retry of the unrelated A2 p95 fluctuation, deterministic cross-platform comparison PASS;
- squash merge `06c0d4ff5f0742cbf5f7f65ff4c2adfd167bf81b`;
- migration head remains `database/migrations/0010_apm_automated_run_foundation.json`; APW-I03 added no migration.

Live A6 inspection before implementation proved migration `0004_a6_action_approval.json` already owns `action_proposals`, `action_review_claims`, `action_decisions`, `action_results`, `action_history`, `action_notifications` and `a6_operations`, including proposal-operation uniqueness and one-final-decision-per-proposal. APW-I03 therefore did not claim migration `0011` or create a parallel asynchronous truth store.

Delivered foundation:
- an APW-I03 orchestration port over the existing A6 proposal/decision/Event model rather than a second asynchronous rules engine;
- a deterministic local-alpha/CI transactional harness reusing A6 validation, decision projection, notification projection and atomic accepted-result commit boundaries, explicitly not production client authority;
- durable pending proposal submission with one stable operation identity across timeout/retry/status recovery;
- same operation plus same payload returns prior submission status while conflicting reuse is rejected;
- permission/visibility filtering before GM inbox rows, count and topology projection;
- advisory review claims that coordinate work without granting decision authority;
- fresh GM authority and exact proposal/Session version checks at delayed decision time;
- stale delayed intent fails closed instead of being silently recalculated or applied;
- approved delayed resolution passes the existing A6 atomic commit boundary and produces one `ActionResultCommitted` Event while advancing Session version once;
- denial produces no gameplay result Event and does not advance Session version;
- decision retry identity is bound to decision intent, not retry observation time, so a lost response can be recovered later without changing the command identity;
- Player submit/status recovery and GM durable-inbox UI proving Player submit → later GM review → Player recovery without AI or a second Action engine;
- nine focused APW-I03 acceptance tests plus the full client regression suite on the final exact head.

APW-I03 preserves its complete failed→repaired validation history:
1. the initial deterministic checker searched for prose `review claim`; it was corrected to assert the actual `ActionReviewClaim` + `advisoryOnly` contract rather than adding meaningless production prose;
2. the first compile reached a test-helper timestamp literal-type defect; the helper was widened to `string` with no product behavior change;
3. the first full client gate found two real defects: decision retry fingerprinting included retry timestamp, and GM inbox refresh overwrote the user-visible review/final outcome; both were repaired at the source;
4. on final exact head, all nine APW-I03 tests and TypeScript passed on Linux while the known A2 p95 check measured `323.772308ms` against `250ms`; an unchanged Linux rerun passed. No APW-I03 code, assertion, performance threshold or validation scope was weakened.

## Current work — APW-I04

**APW-I04 — Bounded Campaign Activity and downtime integration** is the selected next application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I04-attempt-001`  
State: `selected_not_started`

APW-I04 implements APW-03/APW-07 as a governed Campaign-scoped orchestration layer over existing owning domains. It does not create a generic game-state mutation engine, second Campaign ledger or universal downtime simulator.

The bounded initial implementation must preserve these design rules:
- Campaign Activity may coordinate participants, prerequisites, time profile, resources, proposals, progress, waiting states, notifications and provenance, but authoritative effects remain in Character/progression, A6 Action/result, A8 Asset/economy/inventory, A9 investigation/social, World/Adventure, Campaign/Session or another registered owner;
- activity/task resolution is explicit: informational, immediate-domain-command, proposal-required, timed-project-progress, human-choice-required, GM-adjudication-required or prohibited;
- initial alpha-useful families may include bounded preparation/logistics, training preparation, research/investigation, journal/reflection, social maintenance, crafting/repair and recovery/upkeep without attempting universal business, estate, travel, training, crafting or economy simulation;
- Campaign time and wall-clock time remain distinct; elapsed real time does not advance an Activity unless a separately governed profile explicitly authorizes that mapping;
- long-running crafting/repair and other resource work may reference reservations, but A8/owning domains must validate exact resource/facility versions, custody/access, quantity, consumption and release; APW cannot double-reserve or create economy truth;
- Activity lifecycle/progress never silently applies irreversible Character advancement, reveals hidden clues, changes social state, supplies another participant’s consent or invents an NPC/GM response;
- stable activity/task operation IDs, expected versions, status lookup and Event/result references govern recovery so retry cannot duplicate progress, cost or result;
- stale rules/profile/entitlement/permission/resource/participant state blocks or pauses resume until current state is revalidated;
- private journals, hidden investigation/social information and participant-private content are filtered before list/count/progress/notification/diagnostic projection;
- no-AI/manual owning-domain behavior remains available if Campaign Activity orchestration is disabled or unavailable.

The first APW-I04 operation is to re-fetch current application main and migration head, inspect live `downtime-projects`/Project, Campaign/Scene, A8 reservation/resource, A9 investigation/social and APW-I03/A6 proposal seams, then decide whether the verified `0010` baseline actually requires an additive next migration before implementing the smallest useful Campaign Activity path.

Current canonical application main is `06c0d4ff5f0742cbf5f7f65ff4c2adfd167bf81b`; current migration head is `database/migrations/0010_apm_automated_run_foundation.json`.

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

`APW-I01`, `CSW-I01`, `APM-I01`, `APW-I02` and `APW-I03` are completed_verified. `APW-I04` is selected_not_started. Every later item remains inactive until its own canonical selector transition.

## Migration and ownership policy

- migrations `0001` through `0010` are immutable predecessors once merged;
- each implementation tranche rechecks current migration head before mutation;
- `0011` is not reserved; APW-I04 may use the actual next unused migration only if live inspection proves an additive Campaign Activity or owner-domain reservation schema delta is required;
- no migration is required when a slice has no schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- Personal Home remains projection/orchestration over established owners;
- D29 owns CSW creative-support durable records/provenance while governed payloads remain in owning domains;
- D04 owns APM controller/delegation/run authority and D12 owns automation recovery/evidence; neither replaces ordinary owning-domain state/Event history;
- APW-I03 extends existing A6 proposal/decision/Event persistence and does not create parallel asynchronous truth;
- APW-I04 Campaign Activity is orchestration only; Character, Action, Asset/economy, investigation/social, World/Adventure and Campaign effects remain with their registered owners;
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

Current selection authorizes only the bounded APW-I04 application implementation tranche. It does not authorize APW-I05 or later slices, CSW-I02, APM-I02, a generic game-state mutation engine or second Campaign ledger, universal calendar/travel/training/crafting/economy simulation, automatic irreversible advancement, automatic human consent, unrestricted offline/background authoritative mutation, Cozy/APM automation activation, T04 before September, tester distribution, public release/deployment, paid-provider activation, canonical publication or broad Stage A redesign.

## Mandatory execution behavior

“Continue” means execute the next verified unfinished operation. Preserve provenance, hidden-information boundaries, permissions, reversibility and owner gates.
