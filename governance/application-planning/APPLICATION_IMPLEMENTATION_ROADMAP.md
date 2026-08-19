# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.7.0  
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

Delivered first-class zero-Campaign Personal Home, Personal-owned versus Personal-accessible resource classification, fresh protected workspace entry, Campaign/Character/Session → Personal protected-state destruction, stale/revoked reference omission, feature-disable fallback and distinct nonvisual route-area naming without creating a Personal truth super-domain.

### APW-I03 — COMPLETED_VERIFIED

Application PR #209; exact validated head `9b6da9236e9f01003ef4dddccd5edced8359fda1`; repository-health `32258970144`; product validation `32258970575` with self-hosted Windows PASS, self-hosted Linux PASS after unchanged retry of the unrelated A2 p95 fluctuation and deterministic comparison PASS; squash merge `06c0d4ff5f0742cbf5f7f65ff4c2adfd167bf81b`; no migration, so head remained `0010_apm_automated_run_foundation.json`.

Delivered asynchronous A6 Action orchestration with durable pending proposal submission, permission-filtered GM inbox, advisory review claims, fresh delayed-decision authorization, stale failure, one accepted atomic `ActionResultCommitted` outcome, denial without gameplay-result Event, idempotent submission/decision retry and Player → later GM → Player recovery without a second Action engine or AI dependency.

Its failed→repaired history remains preserved: validator semantics, a test timestamp typing defect, decision retry identity including observation time and GM outcome messages overwritten by inbox refresh were repaired. Final Linux A2 timing fluctuation passed on unchanged rerun; no threshold/assertion/scope was weakened.

### APW-I04 — COMPLETED_VERIFIED

**APW-I04 — Bounded Campaign Activity and downtime integration** is complete.

Evidence:
- Application PR #210;
- exact validated head `6702968394192d074d3945ce54f76e77ac5090bc`;
- application repository-health run `32261809233`: PASS;
- product validation run `32261809426`: self-hosted Linux PASS, self-hosted Windows PASS after an unchanged retry of the unrelated A2 p95 fluctuation, deterministic cross-platform comparison PASS;
- squash merge `a907fec750fafe812530d0350eaf3ef3a0875204`;
- migration head advances to `database/migrations/0011_apw_campaign_activity_foundation.json`.

Live inspection before implementation established a genuine D26 persistence gap: `domains/downtime-projects` and its public contract/schema roots contained only ownership placeholders, while immutable Stage A migration `0006_a8_asset_foundations.json` explicitly recorded that long-running D26 Project timing/research was not implemented. APW-I04 therefore legitimately claimed the next unused additive migration `0011` rather than forcing Campaign Activity into another domain's storage.

Delivered foundation:
- provider-neutral D26 Campaign Activity, task, operation and external-reference records only;
- all seven APW-03 resolution classes: informational, immediate-domain-command, proposal-required, timed-project-progress, human-choice-required, GM-adjudication-required and prohibited;
- explicit Campaign-time evidence with wall-clock elapsed time denied Campaign-time authority;
- explicit owner-domain completion evidence rather than D26 gameplay mutation;
- A8 reservation acquisition/release through the existing `AssetReservationPort`, with D26 storing references only;
- A6 Action, A8 Asset/economy, A9 investigation/social, Character/progression, Campaign, World and Adventure authority left with their existing owners;
- human choice, irreversible advancement and GM-only adjudication/reveal as hard stops;
- privacy filtering before Campaign Activity list cardinality;
- stable operation identity excluding retry observation time, stale expected-version failure and recovery without duplicate work;
- deterministic local-alpha/CI orchestration harness and bounded Activity UI, explicitly not production client authority;
- ten focused acceptance tests covering D26-only orchestration, private nonleakage, A9 research evidence, A8 reservation/retry/cancel, training without auto-advance, current GM adjudication, wall-clock nonauthority, stale/idempotent recovery and safe UI guidance;
- complete manual/no-AI path.

APW-I04 preserves its validation history: Linux passed the exact-head profile on the first product attempt. Windows invariant checks, TypeScript and all ten focused APW-I04 tests also passed, while the pre-existing A2 p95 timing check measured `251.76089999999976ms` against `250ms`. The failed jobs were rerun unchanged and Windows passed; no APW-I04 source, threshold, assertion or validation scope was weakened.

## Current work — CSW-I02

**CSW-I02 — Creative Library, Story Bible and Project Memory** is the selected next application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `CSW-I02-attempt-001`  
State: `selected_not_started`

CSW-I02 implements CSW-02 over the completed CSW-I01 D29 CreativeFragment foundation and current authorized governed references. Its persistence boundary is D29 project/library/reference metadata; governed payloads remain references only.

The bounded implementation must preserve these rules:
- **Creative Library** is an authorization-safe organizational/search projection over Creative Fragments, projects, collections, tags, references, incorporation/derivation relationships and history; it is not a truth store;
- **Creator Project** is an organizational/context object, not a World, Adventure or Campaign and does not transfer ownership merely by containing a reference;
- **Story Bible** is a curated project-memory projection and must distinguish `creative-possibility`, `creator-note`, `governed-current-reference`, `governed-pinned-reference`, `campaign-private-reference` and `historical-unavailable-reference` rather than flattening them into undifferentiated facts;
- governed current references remain current authorized owner-domain projections; pinned references retain exact version/provenance evidence without becoming copied CSW truth;
- **Project Memory** is a stable-ID graph over explicit relationships, receipts, history and references; backlinks come from stored relations/provenance, not text-similarity guesses;
- similarity may produce candidate relationships only and cannot create authoritative backlinks until explicitly accepted/recorded;
- D05 authorization/visibility filtering occurs before search counts, facets, rankings, snippets, similarity, graph expansion, degree calculations, topology and pagination;
- hidden/revoked material must not leak labels, counts, facets, snippets, relationships or existence through graph shape;
- saved views store query/filter/sort/layout preferences, not a bypassable result set or authorization grant, and re-evaluate current authority whenever opened;
- tombstoned/unavailable references may preserve authorized history/provenance while inaccessible content remains undiscoverable;
- list/table/outline/graph presentations share stable semantics and nonvisual topology parity;
- feature disable must preserve durable D29 organization and direct owning-screen access;
- the complete core experience remains usable without AI or paid providers.

The first CSW-I02 operation is to re-fetch current application main and migration head, inspect live CSW-I01 D29 CreativeFragment/project/reference persistence, D05 visibility/search projection seams and current creator UI surfaces, then decide whether the `0011` baseline genuinely requires a new additive migration before creating the bounded application branch.

Current canonical application main is `a907fec750fafe812530d0350eaf3ef3a0875204`; current migration head is `database/migrations/0011_apw_campaign_activity_foundation.json`.

## Design handoff evidence

Final design handoff evidence remains:
- CSW-10: PR #449 / repo-health `32237196497` / merge `d27a6774470261450f41e1591580c7feba174cee`;
- APW-07: PR #451 / repo-health `32237975517` / merge `e9592399eaca07d0cdf28b79320fc6bf59bde5ef`;
- APM-06: PR #453 / repo-health `32244745957` / merge `9396ce2ec6094982d292eb4a630036c641094904`;
- APW-08: PR #455 / exact head `f6263185682ec04c948ef865d8f5f3b674b6e825` / repo-health `32245783537` / merge `608e3ddde4b634a1d545856cfd6cb3b2c273fbc7`.

## Combined implementation handles

### APW
APW-I01 through APW-I07.

### CSW
CSW-I01 through CSW-I08, with D29 `authoring-provenance` as the initial creative-support persistence owner and explicit receipt-bound governed incorporation.

### APM
APM-I01 through APM-I06, with bounded automation over ordinary owning-domain/Event authority and complete no-AI recovery paths.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

`APW-I01`, `CSW-I01`, `APM-I01`, `APW-I02`, `APW-I03` and `APW-I04` are `completed_verified`. `CSW-I02` is `selected_not_started`. Every later item remains inactive until its own canonical selector transition.

## Migration and ownership policy

- migrations `0001` through `0011` are immutable predecessors once merged;
- each implementation tranche rechecks current migration head before mutation;
- `0012` is not reserved; CSW-I02 may use the actual next unused migration only if live D29/D05 inspection proves an additive project/library/reference schema delta is required;
- no migration is required when a slice has no schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- D29 owns CSW creative-support durable records/provenance while governed payloads remain references to owning domains;
- D05 filtering precedes count/search/topology/notification/export/diagnostic/AI aggregation;
- Story Bible/project memory organization cannot become governed World/Adventure/Character/Campaign/A9/Asset truth;
- Personal Home remains projection/orchestration over established owners;
- D04 owns APM controller/delegation/run authority and D12 owns automation recovery/evidence;
- APW-I03 extends existing A6 proposal/decision/Event persistence without a parallel async truth store;
- APW-I04 D26 Campaign Activity is orchestration only; owner-domain gameplay effects remain external.

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

Current selection authorizes only the bounded CSW-I02 application implementation tranche. It does not authorize CSW-I03 or later slices, APM-I02 or later slices, APW-I05 or later slices, a new top-level creative truth domain, copying governed payloads into Story Bible authority, similarity/AI relations as authoritative backlinks, saved result sets as authorization grants, hidden-count/facet/topology leakage, silent governed-reference incorporation/propagation, T04 before September, tester distribution, public release/deployment, paid-provider activation, canonical publication or broad Stage A redesign.

## Mandatory execution behavior

“Continue” means execute the next verified unfinished operation. Preserve provenance, hidden-information boundaries, permissions, reversibility and owner gates.
