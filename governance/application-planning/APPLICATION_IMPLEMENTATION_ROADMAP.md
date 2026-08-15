# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.10.0  
**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; STAGE-A-A5 COMPLETED_VERIFIED; A6 REVALIDATION NEXT; PPIA/CAPP COMPLETED_VERIFIED  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-15

## Purpose

This roadmap governs the transition from completed source recovery, canonicalization, architecture, AI-team preparation, and Phase 9 implementation foundations into verified application construction and related parallel work.

Repository evidence is mandatory. Nothing is complete merely because it was discussed, planned, drafted, generated outside the repository, or claimed. Completion requires the evidence declared by the governing work item.

The authoritative ordered Phase 9 backlog remains `governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json`. Runtime recovery is governed by `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`. When a newer internally consistent attempt-branch checkpoint or repository record is more recent than a compact runtime projection, the newer evidence controls recovery until merged or explicitly superseded.

## Current verified execution position — 2026-08-15

- **Phase 9 bounded implementation through P9-06-023 is complete.** Final P9-06-023 / AG-07 physical-device acceptance merged in `Multiversal-app` PR #102 at `fb22295948745347913bcbfebf56ecca26bf39fb`; `releaseAuthorized=false`.
- **DT-001 through DT-010 Developer Toolbelt is complete.** Application PRs #105–#114 produced `mv-dev` v0.10.0, ending at `354e24007d2c453d090a2a6cdb31d3e3333c84c1`.
- **STAGE-A-A2 — Universal Object Experience is `COMPLETED_VERIFIED`.** PR #134 squash-merged as `cdd0713864edc6b6fc3ad78c66b3d2edb5491b2d`; exact closure evidence is retained in `Multiversal-app/receipts/STAGE-A-A2-CLOSURE.json`. Release/deployment remained false.
- **STAGE-A-A3 — Identity, Dashboard, and Workspace Selection is `COMPLETED_VERIFIED`.** PR #136 final head `e4977daf328606a20f1f334d26b22fe6cd40a91a` passed exact-head A3/A1/A2/DT-008 validation and squash-merged as verified commit `7c1392977962a54b91af4519ed258a2a86823665`. The frozen product/browser-tested head `fd4e6d3ac2c23de80707669dc67411b3ee7bb60a` passed focused A3 validation and headed-Chromium evidence; closure is recorded in `Multiversal-app/receipts/STAGE-A-A3-CLOSURE.json`. No production identity provider, new runtime dependency, release or deployment was authorized.
- **STAGE-A-A4 — Character Workspace is `COMPLETED_VERIFIED`.** PR #138 final head `9b690328e9f76abd6941b9e4a23f47189b805b47` passed exact-head A4/A1/A2/A3/DT-008 validation and squash-merged as `38f47a8aa7a5a921fb72a7365dfa6c3f0ea94c31`. Frozen product/browser-tested candidate `6668448c63eba93c7441f5a7ff1f5f9d65cf0cdc` passed the focused Character package and 4/4 headed-Chromium scenarios; closure is recorded in `Multiversal-app/receipts/STAGE-A-A4-CLOSURE.json`. Release/deployment remained false.
- **STAGE-A-A5 — Campaign and Scene Workspace is `COMPLETED_VERIFIED`.** Application PR #139 final head `ddcb98e9e09075fc703b193db9e9e87ca2405717` passed exact-head A5/A1/A2/A3/A4/DT-008 validation and squash-merged as verified commit `89c045b3cf1e04cc906dafac0be2c28c003ae892`. Frozen product/browser-tested candidate `e030089b32634056e212c011022f18d74d4e363f` passed focused A5 validation and 4/4 headed-Chromium scenarios; closure is recorded in `Multiversal-app/receipts/STAGE-A-A5-CLOSURE.json`. Release/deployment remained false.
- **STAGE-A-A6 — First Playable Action and Approval Loop is the current next application target for revalidation and is not activated.** Recovered AIOC preparation remains provenance/input only until reconciled against current post-A5 `main` and implemented A2–A5 authority.
- **Internal Alpha feature design is complete through IA-D09.** Prepared tester/reference/support assets do not activate tester access or release.
- **Design Standards exact-byte ingestion remains unfinished.** `DS-008-working-series-attempt-002` remains blocked on a capable exact-byte transfer/validation surface. Verified preparation remains PR #207 / merge `bd3071f6f855b66b740ba4bf1f1ba0208636548c`, PR #208 / merge `0cfd8128786e4cdd055e3e3be26bdd1854efdfa7`, PR #209 / merge `708e0ea72a6dce6f5d46ddacd042c1ddb80eee0a`, and prepared handoff commit `f0d9295215a057e0f42603a0777c276a7437aad4`.
- **PPIA is `COMPLETED_VERIFIED`.** All sixteen tranches are complete/completed_verified. Final substantive PPIA-16 exact head `eede4bfb530056963a4a595faac54515ff151c3b` passed 70/70 applicable hosted workflows; final-state recovery merged through PR #295 as `8357cc812436e8bbe40c214ac0ca6e44363cc1a5`.
- **CAPP — Character Appearance Production Preparation is `COMPLETED_VERIFIED`.** `CAPP_PROGRAM_BACKLOG.json` records CAPP-01 through CAPP-12 completed_verified. CAPP is direct implementation input for Character appearance/presentation and related diagnostics, while PPIA-05 remains Species/Form biology authority and PPIA-03 remains Asset/equipment authority.
- **Historical 8E-008G-R1 source-accountability closure remains PASS.** PR #218 / merge `d271d1e7ec453cd153a7bf5768b3df837ba677a9` records 101/101 acceptance checks PASS, 7,144/7,144 structural candidates accounted, 0 unbound source sections, and 1,671 formal deferrals preserved.

This section is a recovery summary, not an autosave ledger. More recent verified repository evidence controls if the project advances beyond it.

## Project phase history

- **Phase 0 — Legacy source creation:** original Multiversal source material.
- **Phase 0.5 — Definition document:** broad tabletop RPG platform definition.
- **Phases 1–7:** product conception, functional design, data/pack architecture, mechanics architecture, content-domain architecture, interface/workflow design, and governed repository preparation.
- **Phase 8:** standards, normalization, canonical domain architecture, source conversion, final validation, golden regression corpus, balance harness, and AI Development Team Operating Package.
- **Phase 9:** canonical product architecture, provider-neutral implementation foundations, acceptance gates, and bounded implementation readiness.
- **Phase 10 / Stage A:** current core application implementation program.
- **PPIA:** completed parallel pre-implementation advancement program retained as implementation input and historical evidence.
- **CAPP:** completed Character Appearance production-preparation program retained as direct implementation input for appearance/presentation domains.

## Completed Phase 8 milestones

- **8D-007 — Golden Test Corpus and Balance Harness:** COMPLETE.
- **8D-008 — AI Development Team Operating Package:** COMPLETE.
- **8E-009 — Canonical Object Template and CSV-First Program:** COMPLETE.
- Canonical conversion/normalization established 20 governed datasets, 19,199 source rows, 19,199 promoted records, zero unprocessed rows, and passing provenance/runtime/install/uninstall validation at that milestone.

## Phase 9 — Product Architecture and Implementation Readiness

Completed first-level packages:
1. P9-01 — Entitlements and freemium architecture.
2. P9-02 — Authoritative session architecture.
3. P9-03 — Technology and service decision package.
4. P9-04 — Postgres-centered architecture contract.
5. P9-05 — Bounded technical spike and cost envelope.
6. P9-06 — Implementation backlog and acceptance gates.

P9-06-001 through P9-06-023 are complete and merged in `cybalicistjt-stack/Multiversal-app`. `P9-06-024-OWNER-DECISION-001` established the bounded Stage A implementation-readiness boundary without authorizing release or deployment.

## Developer Toolbelt — DT-001 through DT-010

The owner-approved Developer Toolbelt support series is complete in `Multiversal-app`:
1. DT-001 — Developer Toolbelt Foundation / `mv-dev doctor`.
2. DT-002 — A2 Preflight / Compatibility Mapper.
3. DT-003 — Codex Task Capsule Builder.
4. DT-004 — Governed Fixture Gateway.
5. DT-005 — Scenario/E2E Runner.
6. DT-006 — Permission Leak Scanner.
7. DT-007 — UI Evidence Harvester.
8. DT-008 — Design-System Compliance Linter.
9. DT-009 — Traceability Compiler.
10. DT-010 — Recovery / Performance Harness.

Final state: application PRs #105–#114 merged, `mv-dev` v0.10.0, final merge `354e24007d2c453d090a2a6cdb31d3e3333c84c1`. The toolbelt remains support infrastructure; it does not itself authorize release/deployment/paid services.

## Internal Alpha feature-design track — completed design anchor

The canonical backlog is `governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md`. IA-D01 through IA-D09 are complete, with IA-D09 retained as the release-design anchor. Prepared tester/reference, demo, future-workspace-verification, and pack-lifecycle assets remain non-activating support material.

## PPIA — Parallel Pre-Implementation Advancement Program

Governing documents:
- `governance/application-planning/parallel-preimplementation/PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md`
- `governance/application-planning/parallel-preimplementation/PPIA_PROGRAM_BACKLOG.json`

**Status:** COMPLETED_VERIFIED — OWNER-APPROVED PARALLEL PROGRAM CLOSED.

PPIA was additive parallel source/content/design/authoring/acceptance work. Its completion does not by itself complete a later Stage A implementation item, Design Standards exact-byte ingestion, WP-011 / Apple work, Internal Alpha release, deployment, or public release.

### Approved sixteen tranches

1. **PPIA-01 — Content Quality & Missing-Information Closure** — COMPLETE
2. **PPIA-02 — Creature & NPC Experience** — COMPLETED_VERIFIED
3. **PPIA-03 — Items, Equipment & Inventory Experience** — COMPLETED_VERIFIED
4. **PPIA-04 — Vehicle, Mecha & Starship Experience** — COMPLETED_VERIFIED
5. **PPIA-05 — Species, Forms & Character Biology** — COMPLETED_VERIFIED
6. **PPIA-06 — Character Appearance Creator** — COMPLETED_VERIFIED
7. **PPIA-07 — Rune Construction RPG System** — COMPLETED_VERIFIED
8. **PPIA-08 — Campaign / Scene / Session Authoring Depth** — COMPLETED_VERIFIED
9. **PPIA-09 — Investigation & Mystery Authoring Kit** — COMPLETED_VERIFIED
10. **PPIA-10 — Relationship, Social & Faction Content Framework** — COMPLETED_VERIFIED
11. **PPIA-11 — Encounter & Balance Design Laboratory** — COMPLETED_VERIFIED
12. **PPIA-12 — World & Setting Authoring System** — COMPLETED_VERIFIED
13. **PPIA-13 — Onboarding, Help & In-App Teaching Content** — COMPLETED_VERIFIED
14. **PPIA-14 — Error, Recovery & Permission Microcopy** — COMPLETED_VERIFIED
15. **PPIA-15 — Internal Alpha Test Content Expansion** — COMPLETED_VERIFIED
16. **PPIA-16 — Developer Console / AI-Team Control Surface** — COMPLETED_VERIFIED

Dependency-optimized execution order:
`PPIA-01 → 02 → 03 → 04 → 05 → 12 → 07 → 08 → 09 → 10 → 11 → 06 → 13 → 14 → 15 → 16`.

### Verified completion evidence

Final substantive PPIA-16 closure: exact validated head `eede4bfb530056963a4a595faac54515ff151c3b`; 70/70 workflows; dedicated run `31694048323`; PR #294; signed/verified merge `5b87d57d9b06fbb7427b6fae7ca022509f92a5fe`.

Final machine-readable recovery: exact head `031d4c7af10245069a5cf8bd5b2819965e338cee`; 70/70 hosted workflows; PR #295; signed/verified merge `8357cc812436e8bbe40c214ac0ca6e44363cc1a5`; backlog status `completed_verified_owner_approved_parallel_work`; all sixteen tranches complete/completed_verified.

PPIA-16 preserves the Development Console design over DT-001 through DT-010: 10 DT tools, 10 AIOC control surfaces, 16 program concerns, 5 authority layers, 10 screens, 8 shared states, 8 action classes, 8 components, 12 workflows, 12 handoffs, 48 predecessor cases exact-once, and 12 integrated synthetic/noncanonical cases for 60 effective QA cases with zero intended orphaned coverage.

### Post-PPIA selection boundary

PPIA completion does not select work by itself. Current independent boundaries are:
- **STAGE-A-A6:** current next application target for revalidation, not activated;
- **Design Standards / DS-008 attempt-002:** unfinished/blocked on exact-byte transfer and validation capability;
- **WP-011 / Apple track:** separate bounded Mac-dependent work under its own latest repository evidence when selected.

PPIA completion does not authorize release, deployment, tester access, paid services, production credentials, or unsupported canonical-content promotion.

## CAPP — Character Appearance Production Preparation — completed parallel track

Governing documents:
- `governance/application-planning/character-appearance-production/CAPP_CHARACTER_APPEARANCE_PRODUCTION_PREPARATION_PROGRAM.md`
- `governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json`

**Status:** COMPLETED_VERIFIED — OWNER-APPROVED PARALLEL PROGRAM CLOSED.

CAPP inherited and extended completed PPIA-06 Character Appearance Creator architecture into production preparation without reopening PPIA-06. PPIA-05 remains Species/Form biology authority and PPIA-03 remains actual Asset/equipment authority.

Completed execution order:
1. **CAPP-01 — 25-Species Appearance Choice Registry + Constraint Model** — COMPLETED_VERIFIED
2. **CAPP-02 — Preset, Randomization and Lock Libraries** — COMPLETED_VERIFIED
3. **CAPP-03 — Pixel-Art Asset Production Standard** — COMPLETED_VERIFIED
4. **CAPP-04 — Asset Manifest and Coverage Analyzer Contract** — COMPLETED_VERIFIED
5. **CAPP-05 — Deterministic Appearance Compiler / Reference Engine** — COMPLETED_VERIFIED
6. **CAPP-06 — Wardrobe and Equipment-Fit Compatibility Catalog** — COMPLETED_VERIFIED
7. **CAPP-07 — Full Appearance Studio Screen and State Specification** — COMPLETED_VERIFIED
8. **CAPP-08 — Portrait, Token and Export Production Contract** — COMPLETED_VERIFIED
9. **CAPP-09 — Appearance Versioning and Migration Engine Contract** — COMPLETED_VERIFIED
10. **CAPP-10 — Accessibility Description Grammar** — COMPLETED_VERIFIED
11. **CAPP-11 — Expanded Generated QA and Coverage Corpus** — COMPLETED_VERIFIED
12. **CAPP-12 — Integrated Production Handoff and Completion Gate** — COMPLETED_VERIFIED

CAPP is direct implementation input to Character appearance/presentation and related diagnostics. It does not become Character mechanical truth, Species/Form biology truth, or Asset/equipment ownership/mechanics truth. CAPP completion does not independently activate a Stage A item or authorize release/deployment/tester access/paid services/production credentials.

## Design Standards Completion subproject — unfinished parallel track

The audited/canonicalization tranche is complete, but exact repository ingestion is not. The unfinished gate still requires T1–T4 exact-byte transfer, source/target checksum receipts, publication/full-ingestion validators, focused exact-head CI, PR/merge, and completion evidence. Do not reconstruct checksum-bound publications from excerpts, OCR, screenshots, regenerated prose, or memory.

## Phase 10 / Stage A — Core Application Implementation

Primary programs remain application shell/design system; universal objects; identity/workspaces/permissions; character workspace; campaign/scene builder; live session; combat; inventory/equipment/crafting/vehicles; investigation/social; world builder; contextual AI; and internal-alpha hardening.

### Completed Stage A implementation — A0 through A5

- **STAGE-A-A0 — UI Baseline Audit:** COMPLETE.
- **STAGE-A-A1 — Application Shell and Design System:** COMPLETE.
- **STAGE-A-A2 — Universal Object Experience:** COMPLETED_VERIFIED through application PR #134 / merge `cdd0713864edc6b6fc3ad78c66b3d2edb5491b2d`.
- **STAGE-A-A3 — Identity, Dashboard, and Workspace Selection:** COMPLETED_VERIFIED through application PR #136 / verified squash merge `7c1392977962a54b91af4519ed258a2a86823665`.
- **STAGE-A-A4 — Character Workspace:** COMPLETED_VERIFIED through application PR #138 / squash merge `38f47a8aa7a5a921fb72a7365dfa6c3f0ea94c31`.
- **STAGE-A-A5 — Campaign and Scene Workspace:** COMPLETED_VERIFIED through application PR #139 / verified squash merge `89c045b3cf1e04cc906dafac0be2c28c003ae892`; closure receipt `Multiversal-app/receipts/STAGE-A-A5-CLOSURE.json`.

A3 established a provider-neutral local-alpha identity/session path, authorization-first dashboard projection, separate workspace discovery and entry, nonauthoritative selected-context receipts, role/delegation/support boundaries, inference-safe invitation/recent-work/notification behavior, context revocation isolation, recovery states, accessibility/responsive/offline gates, and a real local-alpha vertical flow into a protected workspace. Its final exact-head A3/A1/A2/DT-008 checks passed, and headed-Chromium evidence passed for keyboard entry/dashboard, fresh workspace entry, axe audits, desktop/mobile reflow, touch targets and offline denial. Release/deployment remain false.

A4 added provider-neutral Character persistence, governed A2 Picker-based creation selections, authoritative calculation and exact 18-class validation, separate Character control, seven-class role-safe projection, Character workspace, append-only advancement/correction and migration history, permission-filtered export, offline/recovery/accessibility boundaries, and a bounded Character-to-Scene reference. Its final exact-head A4/A1/A2/A3/DT-008 checks and focused headed-Chromium Character-entry/workspace evidence passed. Release/deployment remain false.

### Current next application item — STAGE-A-A6 First Playable Action and Approval Loop

`Multiversal-app/.ai/current-work-order.md` names **STAGE-A-A6 — First Playable Action and Approval Loop** as `CURRENT NEXT FOR REVALIDATION / NOT ACTIVATED`.

Recovered preparation authority:

- AIOC branch `governance/stage-a-a6-preimplementation`;
- historical branch tip `5f245cd930f82c799c342fce9ccf5d979298c24f`;
- recovered compatibility artifact record `STAGE_A_A6_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`;
- recorded artifact SHA-256 `ca80319e0282821f19b7fa4f43e439107bc845f0ececfa2937c8bc5418152d00`;
- historical preparation describes 20 repository/predecessor anchors, 16 blocking gaps/risks, 18 provider-neutral A6 contracts, 42 exact future path actions, 15 reuse/composition decisions and 18 blocking validation/CI lanes.

The recovered A6 package is provenance/input only. Retain authoritative Action proposal validation, immutable original proposal plus approve/deny/modify-and-approve semantics, fresh authorization and Character control, exact Session/snapshot/Action Definition bindings, inference-safe queue/projection behavior, stable operation identity/status lookup, reconnect/event-gap recovery and all-or-none accepted-result commit. A6 must consume implemented A2 lookup, A3 subject/delegation/context, A4 Character lifecycle/control and A5 Campaign/Scene/launch-snapshot/Session-shell contracts rather than recreate them. Revalidate the historical protected-cardinality warning so generic hidden-event counts cannot become Player/observer/queue/notification/analytics leaks; IA-D04-002 proposal/approval semantics remain a design dependency where compatible with current repository reality.

### Exact next A6 operation

1. reverify current `Multiversal-app` post-A5 product baseline `89c045b3cf1e04cc906dafac0be2c28c003ae892` and A5 closure evidence;
2. inspect recovered `governance/stage-a-a6-preimplementation` without wholesale-merging it;
3. compare its historical predecessor assumptions and exact 42 path actions to current A2–A5 implementation;
4. preserve A2 governed lookup, A3 subject/delegation/context, A4 Character lifecycle/control and A5 immutable launch snapshot/Session shell;
5. revalidate proposal/approval, protected-cardinality/inference safety, Session revision/idempotency, reconnect/status and atomic accepted-result boundaries;
6. refresh exact A6 path authority, validators, CI lanes and bounded activation contracts against current `main`;
7. produce a bounded current-repository A6 revalidation/activation record;
8. only if that gate passes, create/activate the A6 implementation branch/work order and begin construction;
9. keep release/deployment/provider/vendor/paid-service authority false.

Do not activate A7–A12 merely because their historical design/support packages are prepared.

## Validation and CI efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md` remains controlling: build meaningful bounded slices first, use the smallest deterministic/focused validator during construction, batch related repairs, run broad relevant hosted validation at the bounded package/final gate rather than after every small mutation, keep workflow path filters scoped, bind failures to the active head/gate, and update checkpoints only at material recovery/ready/completion boundaries.

## Phase 11 — GM and Player Experience

Complete day-to-day campaign creation, character creation, scene building, combat/non-combat play, persistence, disconnect/reconnect, and safe resumption.

## Phase 12 — AI Team and Automation

Integrate specialized GM, Rules, Narrative, World, Character, Encounter, and Developer/Content assistants with canonical retrieval, provenance, permissions, visible proposals, reversible actions, and approval gates. AI remains optional/non-authoritative unless later explicitly changed.

## Phase 13 — Internal Alpha Completion

Complete major workflows, authorized service integration, approved content population, gameplay testing, multiplayer/recovery, accessibility, performance, pack lifecycle, onboarding, telemetry, tester documentation, and candidate-specific Internal Alpha gates. Prepared tester/demo/reference assets do not authorize tester access or release by themselves.

## Parallel Apple track

`WP-011 — Tauri iOS/iPadOS Spike` remains a bounded Mac-dependent track. Use its latest repository checkpoint/branch/evidence when selected; do not infer completion or rerun authority from roadmap prose.

## Mandatory execution behavior

- “Continue” means perform the next verified unfinished operation.
- Read the authoritative backlog/work order before starting each item.
- Preserve parallel tracks; completing PPIA/CAPP or one Stage A item does not complete or supersede Design Standards, Apple work, or unrelated retained tracks.
- Distinguish missing source bytes, transfer-tool limits, unavailable checkout, validation failure, and owner-only gates.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, deployments, or exact-byte ingestion without matching evidence.
- Preserve source truth, provenance, variants, conflicts, stable IDs, exact-byte requirements, permissions, hidden-information boundaries, and reversibility.
- John Brandon Turner retains final authority.
