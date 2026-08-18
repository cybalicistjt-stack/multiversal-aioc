# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.17.0  
**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; STAGE-A-A9 COMPLETED_VERIFIED; A10 REVALIDATION COMPLETED / ACTIVATION NEXT; PPIA/CAPP COMPLETED_VERIFIED; APW/CSW PARALLEL PLANNING TRACKS ADDED  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-18

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
- **STAGE-A-A6 — First Playable Action and Approval Loop is `COMPLETED_VERIFIED`.** Application PR #141 final head `dd6ccfe8638110648806c11c3937c842eb568ebe` passed final exact-head A1/A2/A3/A4/A5/A6/DT-008 validation and squash-merged as GitHub-verified commit `79425943f25cce347abcfd2c0abb721005d7a772`. Frozen product/browser-tested candidate `d320d1cd770d9b650a48de523ead5c561740d7ed` passed the full package matrix and 5/5 headed-Chromium scenarios; closure is recorded in `Multiversal-app/receipts/STAGE-A-A6-CLOSURE.json`. Release/deployment remained false.
- **STAGE-A-A7 — Full Combat Interface is `COMPLETED_VERIFIED`.** Application PR #143 final head `ee2d23857644ef451b8cfca17a2b4c3dc5f412c5` passed product-candidate and evidence-head A1/A2/A3/A4/A5/A6/A7/DT-008 matrices and squash-merged as GitHub-verified commit `2821fd41c06a61983c0cfb96d374c298dcb3fc48`. Repaired frozen product/browser-tested candidate `f3e8d2d1e74b7bdeeb93a1d92ec36dfc83ae277e` passed the full A7 package and 6/6 headed-Chromium scenarios; closure is recorded in `Multiversal-app/receipts/STAGE-A-A7-CLOSURE.json`. Release/deployment remained false.
- **STAGE-A-A8 — Inventory, Equipment, Crafting, and Vehicles is `COMPLETED_VERIFIED`.** A8-R0 supplemental authority at `governance/application-planning/stage-a-a8/supplemental-authority/STAGE_A_A8_SUPPLEMENTAL_AUTHORITY_RECONCILIATION.md` completed through AIOC PR #320 / verified merge `08e0ec54808b901a62bfcc537b3dac395ca46490`, with receipt `governance/application-planning/stage-a-a8/supplemental-authority/STAGE_A_A8_R0_COMPLETION_RECEIPT.json`; current-repository revalidation passed through AIOC PR #322 / verified merge `a82810d3d0ba462f890324bb15918ea27dadf7ec`; all 16 AST/VEH construction slices were completed before checks per owner direction; final A1–A8 + DT-008 validation passed; headed Chromium passed 8/8 scenarios; application PR #144 squash-merged as GitHub-verified commit `e9aaa858b345e6a29e27369c01468551752a2483`; closure is recorded in `Multiversal-app/receipts/STAGE-A-A8-CLOSURE.json`. Release/deployment/provider/vendor/paid-service authority remained false.
- **STAGE-A-A9 — Investigation and Social Workspaces is `COMPLETED_VERIFIED`.** All 48 source slices were constructed before checks; 144 source fixtures and 168 published blocking acceptance IDs were preserved; the final A1–A9 + DT-008 + P9 wrapper matrix passed; headed Chromium passed 8/8; application PR #145 squash-merged as GitHub-verified `c2030febf860a4fc9bcac9c65fa44a6b22418dd4`; closure is recorded in `Multiversal-app/receipts/STAGE-A-A9-CLOSURE.json`. Release/deployment remained false.
- **STAGE-A-A10 — World Content Authoring has completed current-repository revalidation and is the current next application target for bounded activation.** AIOC PR #327 squash-merged as GitHub-verified `9124860691ea208bded3800008a2d92b4b2c2139` with verdict `PASS — READY FOR BOUNDED A10 ACTIVATION`. The revalidation preserves the 32 WSM/AM/CC/AI source slices, 120 deterministic fixtures, 140 published blocking criteria, split D06/D07/D18/D28/D29/D05/D13 ownership, owner-only canonical promotion, privacy-before-derived-output, declarative creator sandboxing and additive migration `0008_a10_world_content_authoring.json`. A10 implementation is not activated by the governance merge itself.
- **Internal Alpha feature design is complete through IA-D09.** Prepared tester/reference/support assets do not activate tester access or release.
- **APW — Asynchronous Play & Persistent Workspace is an owner-approved parallel planning track, planned but not implementation-active.** Its governing plan and backlog define universal-user/contextual-role authority, asynchronous Campaign Actions, between-session activity, Personal workspaces, creator/sandbox capability, hybrid recovery/acceptance, and an additive implementation handoff. APW does not change the selected runtime pointer or reopen completed Stage A closure evidence.
- **CSW — Creator Storycraft Workspace is an owner-approved parallel planning track, planned but not implementation-active.** Its plan and backlog define creative fragments, Story Bible/project memory, inspiration, guided creation, plot/adventure design, continuity/open-thread analysis, writing/revision, reuse/remix, and an additive A10/APW implementation handoff. CSW does not change the selected runtime pointer or replace A10 World/Adventure/authoring authority.
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
- **APW:** owner-approved parallel planning subproject for asynchronous play, Personal workspaces, campaign-independent creation, and hybrid Campaign continuity; implementation remains separately gated.
- **CSW:** owner-approved parallel planning subproject for creator storycraft, project memory, creative development, writing, continuity, and reuse; implementation remains separately gated.

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
- **STAGE-A-A10:** current next application target; current-repository revalidation completed_verified, implementation authorized/not activated;
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

## APW — Asynchronous Play & Persistent Workspace — parallel planning subproject

Governing documents:
- `governance/application-planning/asynchronous-persistent-workspace/APW_ASYNCHRONOUS_PLAY_AND_PERSISTENT_WORKSPACE_PROGRAM.md`
- `governance/application-planning/asynchronous-persistent-workspace/APW_PROGRAM_BACKLOG.json`

**Status:** OWNER-APPROVED PARALLEL PLANNING TRACK — PLANNED / NOT IMPLEMENTATION-ACTIVE.

APW makes live, asynchronous and hybrid use cadences of the same governed Campaign while establishing useful Personal workspaces and campaign-independent creation. It preserves universal subscribed-user capability outside Campaign context and scopes GM authority to governed Campaign/resources rather than a global account caste. Campaign-private truth remains permission-protected; optional spoiler shielding is not a security boundary.

### Approved planning tranches

1. **APW-01 — Authority, Account, Context and Terminology Canonicalization**
2. **APW-02 — Asynchronous Action, Proposal and GM Inbox Contract**
3. **APW-03 — Between-Session Campaign Activity and Bounded Downtime**
4. **APW-04 — Personal Workspace and No-Campaign Home**
5. **APW-05 — Creator Workshop, Reusable Assets and Sandbox/Lab**
6. **APW-06 — Shell, Navigation, Notifications, Visibility and Spoiler UX**
7. **APW-07 — Persistence, Recovery, Security and Hybrid Acceptance Architecture**
8. **APW-08 — Implementation Handoff and Stage/Alpha Integration**

Execution order:
`APW-01 → APW-02 → APW-03 → APW-04 → APW-05 → APW-06 → APW-07 → APW-08`.

Each tranche completes its bounded substantive package before its final tranche gate. APW-08 must produce additive application implementation slices rather than reopening completed A3/A5/A6/A8/A9/A10 closure evidence.

Provisional downstream implementation handles are APW-I01 through APW-I07 for contextual account/role extensions, Personal Home/workspace switching, asynchronous Action + GM inbox, bounded Campaign Activity/downtime, Creator Workshop/Sandbox, hybrid notification/recovery integration, and end-to-end live → async → live acceptance. These handles remain nonactive until APW-08 finalizes the implementation handoff and the governing application roadmap explicitly activates them.

APW planning does not change the selected runtime pointer and does not interrupt or supersede CCTI-12, ordinary Stage A work, DS-008, WP-011/Apple, or other preserved tracks. It does not authorize implementation, migration execution, release, deployment, tester access, paid services, production credentials, autonomous AI mutation, a public creator marketplace, or unrestricted offline multi-writer synchronization.

## CSW — Creator Storycraft Workspace — parallel planning subproject

Governing documents:
- `governance/application-planning/creator-storycraft-workspace/CSW_CREATOR_STORYCRAFT_WORKSPACE_PROGRAM.md`
- `governance/application-planning/creator-storycraft-workspace/CSW_PROGRAM_BACKLOG.json`

**Status:** OWNER-APPROVED PARALLEL PLANNING TRACK — PLANNED / NOT IMPLEMENTATION-ACTIVE.

CSW is the creative-thinking, project-memory, story-development, writing, continuity, and reuse layer above existing governed World, Adventure and creator-content systems. It targets `Capture → Develop → Connect → Structure → Write → Check → Use → Reuse`. Scratch ideas and speculative structures remain distinct from Campaign truth or published/canonical content until an explicit owning-domain transition occurs.

### Approved planning tranches

1. **CSW-01 — Storycraft Vocabulary, Creative Object Model and Authority**
2. **CSW-02 — Creative Library, Story Bible and Project Memory**
3. **CSW-03 — Idea Inbox and Inspiration Engine**
4. **CSW-04 — Guided Creation Workflows**
5. **CSW-05 — Plot, Adventure and Narrative Design Lab**
6. **CSW-06 — Continuity, Consistency and Open-Thread Tracker**
7. **CSW-07 — Writing Studio and Revision Workspace**
8. **CSW-08 — Reuse, Remix and Transformation**
9. **CSW-09 — Creator Command Center and Assistance Integration**
10. **CSW-10 — Integration, Acceptance and Implementation Handoff**

Execution order:
`CSW-01 → CSW-02 → CSW-03 → CSW-04 → CSW-05 → CSW-06 → CSW-07 → CSW-08 → CSW-09 → CSW-10`.

CSW must reuse A10's D18 World, D28 Adventure, D29 authoring-provenance, D05 visibility and D07 reusable-definition boundaries rather than create a competing content store. APW remains the broader Personal Workspace/Creator Workshop track; CSW supplies the deeper storycraft vocabulary, memory, inspiration, writing, continuity and reuse workflows. Neither track completes the other.

Provisional downstream implementation handles are CSW-I01 through CSW-I08 for creative-fragment identity/provenance, Creative Library/Story Bible memory, Idea Inbox/inspiration, guided workflows, Plot/Adventure plus continuity tools, Writing Studio, reuse/remix, and Creator Command Center/APW integration. These handles remain nonactive until CSW-10 finalizes the implementation handoff and the governing application roadmap explicitly activates them.

Core CSW capability must remain useful without an external AI provider. Optional AI may suggest, expand, transform, critique or draft from creator-authorized context, but cannot silently overwrite creator work, publish, canonize, reveal hidden material, or mutate live Campaign state.

CSW planning does not change the selected runtime pointer and does not interrupt or supersede APW, CCTI-12, ordinary Stage A work, DS-008, WP-011/Apple, or other preserved tracks. It does not authorize implementation, migration execution, release, deployment, tester access, paid services, production credentials, autonomous publication, canonical promotion, or a public creator marketplace.

## Design Standards Completion subproject — unfinished parallel track

The audited/canonicalization tranche is complete, but exact repository ingestion is not. The unfinished gate still requires T1–T4 exact-byte transfer, source/target checksum receipts, publication/full-ingestion validators, focused exact-head CI, PR/merge, and completion evidence. Do not reconstruct checksum-bound publications from excerpts, OCR, screenshots, regenerated prose, or memory.

## Phase 10 / Stage A — Core Application Implementation

Primary programs remain application shell/design system; universal objects; identity/workspaces/permissions; character workspace; campaign/scene builder; live session; combat; inventory/equipment/crafting/vehicles; investigation/social; world builder; contextual AI; and internal-alpha hardening.

### Completed Stage A implementation — A0 through A9

- **STAGE-A-A0 — UI Baseline Audit:** COMPLETE.
- **STAGE-A-A1 — Application Shell and Design System:** COMPLETE.
- **STAGE-A-A2 — Universal Object Experience:** COMPLETED_VERIFIED through application PR #134 / merge `cdd0713864edc6b6fc3ad78c66b3d2edb5491b2d`.
- **STAGE-A-A3 — Identity, Dashboard, and Workspace Selection:** COMPLETED_VERIFIED through application PR #136 / verified squash merge `7c1392977962a54b91af4519ed258a2a86823665`.
- **STAGE-A-A4 — Character Workspace:** COMPLETED_VERIFIED through application PR #138 / squash merge `38f47a8aa7a5a921fb72a7365dfa6c3f0ea94c31`.
- **STAGE-A-A5 — Campaign and Scene Workspace:** COMPLETED_VERIFIED through application PR #139 / verified squash merge `89c045b3cf1e04cc906dafac0be2c28c003ae892`; closure receipt `Multiversal-app/receipts/STAGE-A-A5-CLOSURE.json`.
- **STAGE-A-A6 — First Playable Action and Approval Loop:** COMPLETED_VERIFIED through application PR #141 / verified squash merge `79425943f25cce347abcfd2c0abb721005d7a772`; frozen product candidate `d320d1cd770d9b650a48de523ead5c561740d7ed`; closure receipt `Multiversal-app/receipts/STAGE-A-A6-CLOSURE.json`.
- **STAGE-A-A7 — Full Combat Interface:** COMPLETED_VERIFIED through application PR #143 / verified squash merge `2821fd41c06a61983c0cfb96d374c298dcb3fc48`; repaired frozen product candidate `f3e8d2d1e74b7bdeeb93a1d92ec36dfc83ae277e`; closure receipt `Multiversal-app/receipts/STAGE-A-A7-CLOSURE.json`.
- **STAGE-A-A8 — Inventory, Equipment, Crafting, and Vehicles:** COMPLETED_VERIFIED through application PR #144 / verified squash merge `e9aaa858b345e6a29e27369c01468551752a2483`; frozen product candidate `cb5abdfb7515943c59995991410ca7f705e03f0b`; headed Chromium 8/8 PASS; closure receipt `Multiversal-app/receipts/STAGE-A-A8-CLOSURE.json`.
- **STAGE-A-A9 — Investigation and Social Workspaces:** COMPLETED_VERIFIED through application PR #145 / verified squash merge `c2030febf860a4fc9bcac9c65fa44a6b22418dd4`; closure receipt `Multiversal-app/receipts/STAGE-A-A9-CLOSURE.json`.

A3 established a provider-neutral local-alpha identity/session path, authorization-first dashboard projection, separate workspace discovery and entry, nonauthoritative selected-context receipts, role/delegation/support boundaries, inference-safe invitation/recent-work/notification behavior, context revocation isolation, recovery states, accessibility/responsive/offline gates, and a real local-alpha vertical flow into a protected workspace. Its final exact-head A3/A1/A2/DT-008 checks passed, and headed-Chromium evidence passed for keyboard entry/dashboard, fresh workspace entry, axe audits, desktop/mobile reflow, touch targets and offline denial. Release/deployment remain false.

A4 added provider-neutral Character persistence, governed A2 Picker-based creation selections, authoritative calculation and exact 18-class validation, separate Character control, seven-class role-safe projection, Character workspace, append-only advancement/correction and migration history, permission-filtered export, offline/recovery/accessibility boundaries, and a bounded Character-to-Scene reference. Its final exact-head A4/A1/A2/A3/DT-008 checks and focused headed-Chromium Character-entry/workspace evidence passed. Release/deployment remain false.

### Current next ordinary Stage A application item — STAGE-A-A10 World Content Authoring

STAGE-A-A10 current-repository revalidation is `COMPLETED_VERIFIED` through AIOC PR #327 / verified squash `9124860691ea208bded3800008a2d92b4b2c2139`. Its verdict is `PASS — READY FOR BOUNDED A10 ACTIVATION`; implementation is authorized but not activated by that governance merge.

Before A10 construction, read `governance/application-planning/stage-a-a10/current-revalidation/STAGE_A_A10_CURRENT_REPOSITORY_REVALIDATION.md` and preserve its D06/D07/D18/D28/D29/D05/D13 ownership, privacy, sandbox, migration `0008_a10_world_content_authoring.json`, owner-only canonical-promotion boundary, and A9-runtime separation.

The exact ordinary Stage A action is to activate bounded A10 implementation from the verified current repository baseline under the revalidation contract, without treating APW/CSW planning, CCTI-12 selection, Design Standards, Apple work, or prepared later-stage packages as automatic completion or supersession of A10.

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
- Preserve parallel tracks; completing PPIA/CAPP or one Stage A item does not complete or supersede APW, CSW, Design Standards, Apple work, or unrelated retained tracks.
- Distinguish missing source bytes, transfer-tool limits, unavailable checkout, validation failure, and owner-only gates.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, deployments, or exact-byte ingestion without matching evidence.
- Preserve source truth, provenance, variants, conflicts, stable IDs, exact-byte requirements, permissions, hidden-information boundaries, and reversibility.
- John Brandon Turner retains final authority.
