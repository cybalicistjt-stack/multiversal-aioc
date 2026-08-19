# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.6.0  
**Status:** ACTIVE — COMBINED WORKSPACE IMPLEMENTATION  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. Historical detail remains in Git history and completed checkpoints rather than being recopied into every roadmap revision.

Implementation transitions use one bounded state synchronization after a verified application merge, one AIOC repository-health gate, and one final selector verification. Ordinary implementation operations do not trigger repeated roadmap/pointer rewrites.

## Completed verified foundations

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06 and POST-GATX-SUCCESSOR are **COMPLETED_VERIFIED**.

The APW/APM/CSW design series is **COMPLETED_VERIFIED** through APW-08, APM-06 and CSW-10.

## Combined implementation progress

| Slice | State | Application evidence | Migration |
|---|---|---|---|
| APW-I01 | completed_verified | PR #205 / merge `e1f074bb…` | none |
| CSW-I01 | completed_verified | PR #206 / merge `bebf833d…` | `0009_csw_creative_fragment_foundation.json` |
| APM-I01 | completed_verified | PR #207 / merge `3941a066…` | `0010_apm_automated_run_foundation.json` |
| APW-I02 | completed_verified | PR #208 / merge `c5c4e896…` | none |
| APW-I03 | completed_verified | PR #209 / merge `06c0d4ff…` | none |
| APW-I04 | completed_verified | PR #210 / merge `a907fec7…` | `0011_apw_campaign_activity_foundation.json` |
| CSW-I02 | completed_verified | PR #211 / merge `72eb9a6b…` | `0012_csw_creator_library_memory.json` |
| APM-I02 | completed_verified | PR #212 / merge `8d3684ed…` | none |
| APM-I03 | completed_verified | PR #213 / merge `ffe354ca…` | `0013_apm_autogm_encounter_foundation.json` |
| APW-I05 | completed_verified | PR #214 / merge `c043c6b9…` | `0014_apw_creator_workshop_sandbox.json` |
| CSW-I03 | completed_verified | PR #215 / merge `0c49376a…` | none |
| CSW-I04 | completed_verified | PR #216 / merge `de028a41…` | `0015_csw_guided_creation_workflow.json` |
| CSW-I05 | completed_verified | PR #217 / merge `dc9c0f75…` | `0016_csw_narrative_lab_continuity.json` |
| CSW-I06 | completed_verified | PR #218 / merge `c7aac6ff…` | `0017_csw_writing_studio_revision_workspace.json` |
| CSW-I07 | completed_verified | PR #219 / `245b90df…` / merge `5d349777…` | `0018_csw_reuse_remix_transformation.json` |
| APW-I06 | **selected_not_started** | `APW-I06-attempt-001` | inspect live head first |

### CSW-I07 completion evidence

Application PR #219 completed from exact validated head `245b90dfc6b9728df5a9d1954bf7c1176c5b0d2e`. Repository-health run `32285069748` passed. Product run `32285069972` ended with self-hosted Windows PASS, self-hosted Linux PASS and deterministic comparison PASS before squash merge `5d34977710ae1229e32de06e7e7b28610b90ae84`.

CSW-I07 added migration `0018_csw_reuse_remix_transformation.json` only after live inspection proved a genuine D29 gap. It stores independent derivative identity, exact one-or-many source snapshots, deterministic recipe provenance, inherited-reference dispositions, idempotent operation evidence and advisory source-drift reviews without copying source/result payload truth or source authority. Source changes never silently propagate; explicit rebase candidates remain creator-controlled and source mutation is prohibited.

Validation history is preserved in `CSW-I07-attempt-001`: candidate `7a0d96f…` exposed an over-specific validator formatting check; candidate `39d5bde…` exposed a focused fixture TS2783 typing defect. On final head `245b90df…`, the first Linux regression execution failed only the pre-existing A2 performance budget at p95 `455.828575 ms` versus `250 ms`; all 11 CSW-I07 focused tests passed and Windows passed the full profile. The exact unchanged Linux job retry passed and deterministic comparison then passed. No source, test, threshold, privacy or authority rule was changed for the retry.

## Current work — APW-I06

**APW-I06 — Notification, Visibility, Recovery and Hybrid Cross-Device Integration** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I06-attempt-001`  
State: `selected_not_started`

The governing shell rule is:

`authorize candidate set → visibility project → aggregate/count/rank → render`

Never:

`aggregate all → redact individual rows`.

Required boundaries:
- Personal, Campaign and Session context remain explicit; role/capability presentation is contextual rather than an account caste;
- navigation, badges, attention counts, search, notifications, recents and deep-link previews are authorization-filtered before aggregation or presentation;
- the shell is orchestration/projection only and cannot become a second Campaign, Action, creator or notification workflow authority;
- attention center may compose decision-required, result-ready, waiting, recovery-required, informational and creator-advisory projections while owning domains retain state/disposition authority;
- notifications are durable or reconstructable projections of owning-domain outcomes; quieting reduces pressure and never grants automation/consent;
- deep links carry context/target hints, not permission; open always reauthorizes and re-resolves current target/version;
- Spoiler Shield applies only to already-authorized content and never substitutes for D05 authorization, parental controls or child-safety security;
- context switching must invalidate/re-evaluate prior-context protected search, counts, previews, recents, assistance scope and cached Campaign-private cards;
- offline/cached state is explicitly labeled and cannot invent write authority; reconnect revalidates authorization/version before protected data is rendered;
- ambiguous prior mutations recover through owning-domain status/idempotency rather than blind duplicate retry;
- mobile, keyboard, screen-reader/nonvisual and reduced-motion paths carry equivalent context, visibility and recovery meaning;
- shell language remains warm, calm, concise and non-obsequious;
- deterministic no-AI operation remains first-class and no external push/email provider is required for acceptance.

First operation: re-fetch App main and migration head **once**, inspect current shell/context switching, D05 visibility projections, APW-I03/I04 attention sources, notification/recovery/deep-link/cache seams and cross-device reconnect behavior, determine whether the smallest durable APW-I06 model genuinely requires migration `0019`, then implement the first deterministic context-switch + authorization-safe attention/recovery path.

Canonical App baseline after CSW-I07: `5d34977710ae1229e32de06e7e7b28610b90ae84`. Migration head: `0018_csw_reuse_remix_transformation.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through CSW-I07 is completed_verified. APW-I06 is selected_not_started. CSW-I08 and all later slices remain inactive.

A later slice may move earlier only when its declared dependencies remain satisfied **and the owner approves the reorder**. No such reorder is active.

## Migration and ownership policy

- migrations `0001` through `0018` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- APW-I06 composes visibility-projection, audit/export/recovery, diagnostics/support and shell surfaces; notification/attention/recovery metadata, if durable storage is genuinely needed, remains bounded to the correct owning domain rather than one generic APW truth store;
- D05 authorization precedes counts, badges, search, notifications, deep-link previews, recents, context caches, exports and optional assistance;
- Spoiler Shield is presentation preference for authorized content only;
- broad offline authoritative mutation remains out of scope;
- D18/D28/A9/Character/Campaign/Action transitions remain explicit owning-domain operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **complete**.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06 — **APW-I06 current**.
6. Whole-system hybrid proof — APW-I07.

Tester distribution remains separately owner-gated.

## Preserved/deferred work

- **CCTI-12-T04:** owner-deferred until September 2026; preserve App PR #191 and its branches. On/after 2026-09-01 establish the owner-approved validation route before reevaluation.
- **WP-011:** dormant until the required special Mac environment is available.
- **DS-008:** blocked non-owner exact-byte transfer/validation; never reconstruct checksum-bound bytes from excerpts/OCR/memory.

## Permanent validation rules

Only evidence-backed `completed_verified` is complete. A failed required gate leaves work unfinished. Normal App/package acceptance is self-hosted Windows + self-hosted Linux + deterministic comparison where outputs should agree, plus exact-head repository health. AIOC repository health validates governance state; it does not substitute for product validation.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear, confident and restrained; never obsequious.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work.

## Nonauthorization

Current selection authorizes only APW-I06. It does not authorize CSW-I08+, APM-I04+, APW-I07, migration `0019` without a proven durable delta, a new shell authority/workflow engine, hidden count/search/notification leakage, permission-bearing deep links, Spoiler Shield as security/parental control, broad offline authoritative mutation, external notification-provider activation, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
