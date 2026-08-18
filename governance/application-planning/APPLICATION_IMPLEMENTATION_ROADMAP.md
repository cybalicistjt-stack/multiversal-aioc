# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.18.0  
**Status:** ACTIVE — STAGE-A-A0-A12 COMPLETED_VERIFIED; INTERNAL-ALPHA TESTER/GATX PROOF COMPLETED_VERIFIED; CCTI-12-T04 VALIDATION QUARANTINED / NOT COMPLETE; VCH OWNER-APPROVED; APW/CSW PLANNED; CROSS-CUTTING PRODUCT TODOs INTEGRATED  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-18

## Purpose

This roadmap governs the transition from completed source recovery, canonicalization, architecture, AI-team preparation, Phase 9 implementation foundations, completed Stage A construction, Internal Alpha evidence work, and current parallel integration/design programs into subsequent verified application construction.

Repository evidence is mandatory. Nothing is complete merely because it was discussed, planned, drafted, generated outside the repository, or claimed. Completion requires the evidence declared by the governing work item.

The authoritative ordered Phase 9 backlog remains `governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json`. Runtime recovery is governed by `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`, `governance/ai/runtime/CURRENT_WORK_POINTER.json`, and the newest internally consistent repository checkpoint/amendment. When a newer checkpoint or repository record is more recent than a compact runtime projection, the newer evidence controls recovery until merged or explicitly superseded.

## Current verified execution position — 2026-08-18

- **Phase 9 bounded implementation through P9-06-023 is complete.** Final P9-06-023 / AG-07 physical-device acceptance merged in `Multiversal-app` PR #102 at `fb22295948745347913bcbfebf56ecca26bf39fb`; `releaseAuthorized=false`.
- **DT-001 through DT-010 Developer Toolbelt is complete.** Application PRs #105–#114 produced `mv-dev` v0.10.0, ending at `354e24007d2c453d090a2a6cdb31d3e3333c84c1`.
- **STAGE-A-A2 — Universal Object Experience is `COMPLETED_VERIFIED`.** PR #134 squash-merged as `cdd0713864edc6b6fc3ad78c66b3d2edb5491b2d`; exact closure evidence is retained in `Multiversal-app/receipts/STAGE-A-A2-CLOSURE.json`. Release/deployment remained false.
- **STAGE-A-A3 — Identity, Dashboard, and Workspace Selection is `COMPLETED_VERIFIED`.** PR #136 final head `e4977daf328606a20f1f334d26b22fe6cd40a91a` passed exact-head A3/A1/A2/DT-008 validation and squash-merged as verified commit `7c1392977962a54b91af4519ed258a2a86823665`. The frozen product/browser-tested head `fd4e6d3ac2c23de80707669dc67411b3ee7bb60a` passed focused A3 validation and headed-Chromium evidence. Release/deployment remained false.
- **STAGE-A-A4 — Character Workspace is `COMPLETED_VERIFIED`.** PR #138 final head `9b690328e9f76abd6941b9e4a23f47189b805b47` passed exact-head A4/A1/A2/A3/DT-008 validation and squash-merged as `38f47a8aa7a5a921fb72a7365dfa6c3f0ea94c31`; frozen product/browser-tested candidate `6668448c63eba93c7441f5a7ff1f5f9d65cf0cdc` passed the focused Character package and 4/4 headed-Chromium scenarios. Release/deployment remained false.
- **STAGE-A-A5 — Campaign and Scene Workspace is `COMPLETED_VERIFIED`.** Application PR #139 final head `ddcb98e9e09075fc703b193db9e9e87ca2405717` passed exact-head A5/A1/A2/A3/A4/DT-008 validation and squash-merged as verified commit `89c045b3cf1e04cc906dafac0be2c28c003ae892`. Release/deployment remained false.
- **STAGE-A-A6 — First Playable Action and Approval Loop is `COMPLETED_VERIFIED`.** Application PR #141 final head `dd6ccfe8638110648806c11c3937c842eb568ebe` passed final exact-head A1/A2/A3/A4/A5/A6/DT-008 validation and squash-merged as GitHub-verified commit `79425943f25cce347abcfd2c0abb721005d7a772`; frozen product candidate `d320d1cd770d9b650a48de523ead5c561740d7ed` passed 5/5 headed-Chromium scenarios. Release/deployment remained false.
- **STAGE-A-A7 — Full Combat Interface is `COMPLETED_VERIFIED`.** Application PR #143 final head `ee2d23857644ef451b8cfca17a2b4c3dc5f412c5` passed product-candidate and evidence-head A1/A2/A3/A4/A5/A6/A7/DT-008 matrices and squash-merged as GitHub-verified commit `2821fd41c06a61983c0cfb96d374c298dcb3fc48`; repaired frozen product candidate `f3e8d2d1e74b7bdeeb93a1d92ec36dfc83ae277e` passed 6/6 headed-Chromium scenarios. Release/deployment remained false.
- **STAGE-A-A8 — Inventory, Equipment, Crafting, and Vehicles is `COMPLETED_VERIFIED`.** A8-R0 supplemental authority completed through AIOC PR #320 / verified merge `08e0ec54808b901a62bfcc537b3dac395ca46490`, current-repository revalidation passed through AIOC PR #322 / verified merge `a82810d3d0ba462f890324bb15918ea27dadf7ec`, all 16 AST/VEH construction slices were completed before checks, final A1–A8 + DT-008 validation passed, headed Chromium passed 8/8 scenarios, and application PR #144 squash-merged as GitHub-verified commit `e9aaa858b345e6a29e27369c01468551752a2483`. Release/deployment/provider/vendor/paid-service authority remained false.
- **STAGE-A-A9 — Investigation and Social Workspaces is `COMPLETED_VERIFIED`.** All 48 source slices were constructed before checks; 144 source fixtures and 168 published blocking acceptance IDs were preserved; final A1–A9 + DT-008 + P9 wrapper validation passed; headed Chromium passed 8/8; application PR #145 squash-merged as GitHub-verified `c2030febf860a4fc9bcac9c65fa44a6b22418dd4`. Release/deployment remained false.
- **STAGE-A-A10 — World Content Authoring is `COMPLETED_VERIFIED`.** AIOC current-repository revalidation completed through PR #327 / verified squash `9124860691ea208bded3800008a2d92b4b2c2139`; application implementation completed through PR #146 / GitHub-verified squash `9744c5223eb41f9cac765f3807a7860ffe0d1143`; closure projection is `f023c7feab49910b02abccf3ae87fd4b581c64c8`; closure receipt is `Multiversal-app/receipts/STAGE-A-A10-CLOSURE.json`. Construction completed 32/32 WSM/AM/CC/AI slices with 120 deterministic fixtures and 140 blocking source acceptance IDs; exact-head A1–A10 + DT-008 and required P9 runner checks passed; headed Chromium passed 8/8. Release/deployment/provider/paid-service/production-credential/public-marketplace/autonomous-publication/canonical-promotion authority remained false.
- **STAGE-A-A11 — Contextual AI Interfaces is `COMPLETED_VERIFIED`.** Application PR #149 merged as `bf54f36737fe02041f02ab44a69f45c3b0b294ac`. The completion receipt records 24 slices, 72 source fixtures, 76 blocking acceptance keys, provider-neutral/nonautonomous boundaries, exact-head A1–A11 + DT-008 success, and headed-Chromium evidence. Provider selection, credentials, paid execution, autonomous mutation/approval/publication, release, deployment and canonical promotion remain unauthorized.
- **STAGE-A-A12 — Internal Alpha Hardening is `COMPLETED_VERIFIED`.** Application PR #151 merged as `4a488f366058c4b63af9f897744388cc77688763`; closure PR #152 merged as `47a060c70f23bf5b60226f1aaa433bf301fa24db`; validated evidence head is `56b127f1fc01eebe5c73ba0472a5b6496fe92b5e`. The completion receipt records 12 construction slices, 26 acceptance contracts, 22 blocking release gates, 8 owner-only gates, 17 evidence classes, 30 security threat families, 90 security scenarios, 24 IA-D09 release fixtures, and 24 tester/reference journeys. Stage A completion does not itself authorize public release or deployment.
- **Internal Alpha tester access/release owner-decision work and physical account testing are complete.** The governed tester-distribution line reached 20 accounts (10 GM / 10 Player), all 20 physically exercised, with zero role-routing errors. The retained HOTFIX2 package is `Multiversal-Internal-Alpha-Windows-HOTFIX2-a4e262167aa9.zip`, SHA-256 `5c9f31c96a3373f927f8d3a7ee6ee821aafeda8d0ae26a0c6cecf94ca129e0de`.
- **GATX guided-alpha testing through T08 is `COMPLETED_VERIFIED`.** T07-REMOTE live remote evidence and T08 geographic evidence are complete; the current GATX backlog records no active GATX item.
- **The post-GATX successor distribution remains unfinished.** `Multiversal-app` PR #185 / branch `internal-alpha/post-gatx-successor-distribution` is preserved. Its previous generic GitHub-hosted-runner requirement must be re-evaluated under `MV-AI-VALIDATION-003`; no automatic completion or merge follows from the policy change.
- **CCTI-01 through CCTI-11 are complete; CCTI-12 T01–T03 are `COMPLETED_VERIFIED`.** T01 merged through application PR #188 (`2d2eb4c3cf9f10fe4a32029045d688b3301362e3`), T02 through PR #189 (`96acc3b34114cad7c6b75abab11e8a862a04509c`), and T03 through PR #190 (`59fd30d3ad38d688c18b1abe0adfb7c9a8eaffa5`).
- **CCTI-12-T04 — Local Review Worksets & Proposal Disposition is construction-complete but `VALIDATION_QUARANTINED`, not complete.** Application PR #191 remains open at head `3d32ee9317bc924a6a8206121402c68bdf8a061b`. Self-hosted Windows/Linux validation reached focused test execution after the persistent-Windows Python bootstrap repair. The remaining known failure class concerns a brittle repeated-boundary UI test contract around `Canonical taxonomy: OFF`. Exact failing-line retrieval through the conversational GitHub evidence surface proved unreliable. T04 may not merge or be called complete until exact-final-head Windows + Linux + deterministic receipt comparison pass. Its validation quarantine no longer blocks unrelated production work.
- **VCH — Validation Core Hardening is owner-approved and may proceed as an independent support tranche while T04 remains validation-quarantined.** VCH must not be used to retroactively claim T04 complete. It exists to establish runner-contract verification, shared execution, deterministic self-exporting evidence, failure-layer attribution, cross-platform comparison, and harness fault-injection proof so validation-interface failures do not repeatedly stall production.
- **APW — Asynchronous Play & Persistent Workspace is an owner-approved parallel planning track, planned but not implementation-active.** It defines universal-user/contextual-role authority, asynchronous Campaign Actions, between-session activity, Personal workspaces, creator/sandbox capability, hybrid recovery/acceptance, and an additive implementation handoff.
- **CSW — Creator Storycraft Workspace is an owner-approved parallel planning track, planned but not implementation-active.** It defines creative fragments, Story Bible/project memory, inspiration, guided creation, plot/adventure design, continuity/open-thread analysis, writing/revision, reuse/remix, and an additive implementation handoff.
- **Design Standards exact-byte ingestion remains unfinished.** `DS-008-working-series-attempt-002` remains blocked on a capable exact-byte transfer/validation surface. Verified preparation remains PR #207 / merge `bd3071f6f855b66b740ba4bf1f1ba0208636548c`, PR #208 / merge `0cfd8128786e4cdd055e3e3be26bdd1854efdfa7`, PR #209 / merge `708e0ea72a6dce6f5d46ddacd042c1ddb80eee0a`, and prepared handoff commit `f0d9295215a057e0f42603a0777c276a7437aad4`.
- **PPIA is `COMPLETED_VERIFIED`.** All sixteen tranches are complete/completed_verified. Final substantive PPIA-16 exact head `eede4bfb530056963a4a595faac54515ff151c3b` passed its declared final matrix; final-state recovery merged through PR #295 as `8357cc812436e8bbe40c214ac0ca6e44363cc1a5`.
- **CAPP — Character Appearance Production Preparation is `COMPLETED_VERIFIED`.** `CAPP_PROGRAM_BACKLOG.json` records CAPP-01 through CAPP-12 completed_verified.
- **Historical 8E-008G-R1 source-accountability closure remains PASS.** PR #218 / merge `d271d1e7ec453cd153a7bf5768b3df837ba677a9` records 101/101 acceptance checks PASS, 7,144/7,144 structural candidates accounted, 0 unbound source sections, and 1,671 formal deferrals preserved.

This section is a recovery summary, not an autosave ledger. More recent verified repository evidence controls if the project advances beyond it.

## Project phase history

- **Phase 0 — Legacy source creation:** original Multiversal source material.
- **Phase 0.5 — Definition document:** broad tabletop RPG platform definition.
- **Phases 1–7:** product conception, functional design, data/pack architecture, mechanics architecture, content-domain architecture, interface/workflow design, and governed repository preparation.
- **Phase 8:** standards, normalization, canonical domain architecture, source conversion, final validation, golden regression corpus, balance harness, and AI Development Team Operating Package.
- **Phase 9:** canonical product architecture, provider-neutral implementation foundations, acceptance gates, and bounded implementation readiness.
- **Phase 10 / Stage A:** core application implementation through A12; completed_verified.
- **PPIA:** completed parallel pre-implementation advancement program retained as implementation input and historical evidence.
- **CAPP:** completed Character Appearance production-preparation program retained as direct implementation input for appearance/presentation domains.
- **CCTI:** content-catalog/taxonomy integration program; CCTI-12-T04 remains unmerged and validation-quarantined.
- **VCH:** bounded shared validation-core hardening support program.
- **APW:** owner-approved parallel planning subproject for asynchronous play, Personal workspaces, campaign-independent creation, and hybrid Campaign continuity.
- **CSW:** owner-approved parallel planning subproject for creator storycraft, project memory, creative development, writing, continuity, and reuse.

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

## Internal Alpha feature-design and testing track

The canonical design backlog is `governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md`. IA-D01 through IA-D09 are complete. Subsequent owner-decision, tester-distribution, guided testing and geographic/remote evidence are governed by their later checkpoints and GATX records.

GATX-T01 through GATX-T08 are complete/completed_verified. A future successor distribution is a separate bounded release-candidate operation and remains unfinished at application PR #185.

## PPIA — Parallel Pre-Implementation Advancement Program

Governing documents:
- `governance/application-planning/parallel-preimplementation/PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md`
- `governance/application-planning/parallel-preimplementation/PPIA_PROGRAM_BACKLOG.json`

**Status:** COMPLETED_VERIFIED — OWNER-APPROVED PARALLEL PROGRAM CLOSED.

Approved sixteen tranches:
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

Dependency-optimized execution order was `PPIA-01 → 02 → 03 → 04 → 05 → 12 → 07 → 08 → 09 → 10 → 11 → 06 → 13 → 14 → 15 → 16`.

PPIA completion does not authorize release, deployment, tester access, paid services, production credentials, or unsupported canonical-content promotion.

## CAPP — Character Appearance Production Preparation — completed parallel track

Governing documents:
- `governance/application-planning/character-appearance-production/CAPP_CHARACTER_APPEARANCE_PRODUCTION_PREPARATION_PROGRAM.md`
- `governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json`

**Status:** COMPLETED_VERIFIED — OWNER-APPROVED PARALLEL PROGRAM CLOSED.

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

CAPP completion does not independently authorize release/deployment/tester access/paid services/production credentials.

## CCTI — Content Catalog Taxonomy Integration

CCTI preserves Content V2 identity/provenance/normalization/supersession work while reconciling Item, Platform, relationship, context and future adoption concerns. Source/master mutation, automatic canonical taxonomy adoption, relationship promotion, compatibility finalization, mechanics reauthoring, runtime Asset mutation and Player canonical exposure remain separately governed.

CCTI-01 through CCTI-11 are complete. CCTI-12 app-facing work is bounded into local noncanonical review tooling:
- **T01 — Candidate Content Workspace:** COMPLETED_VERIFIED, app PR #188.
- **T02 — Local Review Queue / Candidate Compare:** COMPLETED_VERIFIED, app PR #189.
- **T03 — Amendment Drafting / Export:** COMPLETED_VERIFIED, app PR #190.
- **T04 — Local Review Worksets & Proposal Disposition:** construction complete, validation quarantined, app PR #191 open; not merge-authorized and not complete.

Validation quarantine is an execution-state distinction, not a waiver. T04 resumes only when exact failure evidence can safely drive the patch and the declared exact-final-head Windows/Linux/comparator gate can be satisfied.

## VCH — Validation Core Hardening

Governing program: `Multiversal-app/governance/application-planning/validation-core/VALIDATION_CORE_HARDENING_PROGRAM.md`.

**Status:** OWNER-APPROVED / CONSTRUCTION PENDING; permitted to proceed while T04 is validation-quarantined.

VCH exists because persistent self-hosted validation must be deterministic and diagnosable without making the entire project dependent on fragile log scraping or hosted-runner credit. It preserves `MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md` and the normal exact-final-head Windows + Linux + deterministic comparison gate.

Approved tranches:
1. **VCH-01 — Failure Taxonomy and Diagnostic Contract**
2. **VCH-02 — Runner Contract and Preflight**
3. **VCH-03 — Shared Execution Core and Thin Profiles**
4. **VCH-04 — Deterministic Evidence and Cross-Platform Comparator**
5. **VCH-05 — Harness Self-Tests and Fault Injection**
6. **VCH-06 — Migration and Adoption Gate**

VCH must add self-exporting compact failure evidence and retain raw evidence. A validation/evidence-interface failure may quarantine a feature merge; after bounded diagnosis attempts it must not automatically freeze unrelated roadmap work. Quarantine never converts an unfinished feature into complete.

## APW — Asynchronous Play & Persistent Workspace — parallel planning subproject

Governing documents:
- `governance/application-planning/asynchronous-persistent-workspace/APW_ASYNCHRONOUS_PLAY_AND_PERSISTENT_WORKSPACE_PROGRAM.md`
- `governance/application-planning/asynchronous-persistent-workspace/APW_PROGRAM_BACKLOG.json`

**Status:** OWNER-APPROVED PARALLEL PLANNING TRACK — PLANNED / NOT IMPLEMENTATION-ACTIVE.

APW makes live, asynchronous and hybrid use cadences of the same governed Campaign while establishing useful Personal workspaces and campaign-independent creation. It preserves universal subscribed-user capability outside Campaign context and scopes GM authority to governed Campaign/resources rather than a global account caste.

Approved tranches:
1. **APW-01 — Authority, Account, Context and Terminology Canonicalization**
2. **APW-02 — Asynchronous Action, Proposal and GM Inbox Contract**
3. **APW-03 — Between-Session Campaign Activity and Bounded Downtime**
4. **APW-04 — Personal Workspace and No-Campaign Home**
5. **APW-05 — Creator Workshop, Reusable Assets and Sandbox/Lab**
6. **APW-06 — Shell, Navigation, Notifications, Visibility and Spoiler UX**
7. **APW-07 — Persistence, Recovery, Security and Hybrid Acceptance Architecture**
8. **APW-08 — Implementation Handoff and Stage/Alpha Integration**

APW planning does not authorize implementation, migration execution, release, deployment, paid services, autonomous AI mutation, a public creator marketplace, or unrestricted offline multi-writer synchronization.

## CSW — Creator Storycraft Workspace — parallel planning subproject

Governing documents:
- `governance/application-planning/creator-storycraft-workspace/CSW_CREATOR_STORYCRAFT_WORKSPACE_PROGRAM.md`
- `governance/application-planning/creator-storycraft-workspace/CSW_PROGRAM_BACKLOG.json`

**Status:** OWNER-APPROVED PARALLEL PLANNING TRACK — PLANNED / NOT IMPLEMENTATION-ACTIVE.

CSW targets `Capture → Develop → Connect → Structure → Write → Check → Use → Reuse`. Scratch ideas and speculative structures remain distinct from Campaign truth or published/canonical content until an explicit owning-domain transition occurs.

Approved tranches:
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

Core CSW capability must remain useful without an external AI provider. Optional AI may suggest, expand, transform, critique or draft from creator-authorized context, but cannot silently overwrite creator work, publish, canonize, reveal hidden material, or mutate live Campaign state.

## Approved APW/CSW interleaved design order

The dependency-optimized owner-approved design sequence is:

`APW-01 → CSW-01 → CSW-02 → APW-02 → APW-03 → APW-04 → CSW-03 → CSW-04 → CSW-05 → CSW-06 → CSW-07 → CSW-08 → APW-05 → CSW-09 → APW-06 → CSW-10 → APW-07 → APW-08`.

This sequence remains downstream of the currently selected bounded support/reconciliation work and does not imply implementation activation.

## Cross-cutting product TODO — TODO-UX-VOICE

**Status:** OWNER-APPROVED TODO — product-wide design standard required before product-language/UI-assistance freeze.

Canonical direction:

> **Multiversal is a knowledgeable, creative companion: warm enough to invite experimentation, confident enough to give clear guidance, and restrained enough to respect the user.**

The visible product personality should be warm, welcoming, curious, creatively supportive, clear and confident about complexity/errors/limits, and respectful of the user's intelligence, autonomy, taste and authorship. It must not become obsequious, saccharine, infantilizing, excessively congratulatory, mascot-like, relentlessly cheerful, or evasive about problems.

This concern applies across onboarding, navigation, empty states, contextual help, tutorials, warnings, validation/recovery/errors, Player/GM assistance, creator/storycraft/world/adventure surfaces, notifications, optional AI assistance, accessibility/support language, and future community/social surfaces. Detailed execution must reconcile with the existing UI Design Bible, Screen Design Bible, PPIA onboarding/help work, APW, CSW and contextual-assistance design rather than creating competing authority.

## Cross-cutting product TODO — TODO-FSF / Family Safety Framework

**Status:** OWNER-APPROVED TODO — bounded architecture/design track required before broad minor-facing community, stranger-discovery, public-publishing, marketplace or matchmaking exposure.

Canonical boundary:

> **Parental controls govern Multiversal-controlled capabilities and exposure; they do not claim to control or guarantee the conduct, speech, or fictional content introduced by other human participants.**

Family safety is an account-policy/capability axis, not a permanent gameplay role. Guardian authority must remain separate from contextual GM/Campaign authority and must not imply automatic access to a child's private creative work.

Future bounded design must cover family-linked account relationships, age-appropriate presets/granular controls, privacy-by-default/reduced discoverability, public profile/discovery/invitation/community controls, communication/block/report safety, Campaign-joining approval, content descriptors/maturity controls, optional-AI limits, purchase/marketplace authorization, public-publishing controls while preserving private creation, safety-center visibility, data minimization, and explicit acceptance tests for enforceable vs human-participant boundaries.

Architecture that is expensive to retrofit—account/family relationships, capability permissions, privacy classifications, content descriptors, reporting/blocking primitives, guardian-vs-Campaign authority separation and purchase authorization—must be established before dependent public/community systems are frozen. APW-01 must preserve the account/authority seams needed for this future framework.

## Design Standards Completion subproject — unfinished parallel track

The audited/canonicalization tranche is complete, but exact repository ingestion is not. The unfinished gate still requires T1–T4 exact-byte transfer, source/target checksum receipts, publication/full-ingestion validators, focused exact-head CI, PR/merge, and completion evidence. Do not reconstruct checksum-bound publications from excerpts, OCR, screenshots, regenerated prose, or memory.

## Phase 10 / Stage A — Core Application Implementation

Primary Stage A programs were application shell/design system; universal objects; identity/workspaces/permissions; character workspace; campaign/scene builder; first playable action/approval; combat; inventory/equipment/crafting/vehicles; investigation/social; world content authoring; contextual AI; and internal-alpha hardening.

### Completed Stage A implementation — A0 through A12

- **STAGE-A-A0 — UI Baseline Audit:** COMPLETE.
- **STAGE-A-A1 — Application Shell and Design System:** COMPLETE.
- **STAGE-A-A2 — Universal Object Experience:** COMPLETED_VERIFIED.
- **STAGE-A-A3 — Identity, Dashboard, and Workspace Selection:** COMPLETED_VERIFIED.
- **STAGE-A-A4 — Character Workspace:** COMPLETED_VERIFIED.
- **STAGE-A-A5 — Campaign and Scene Workspace:** COMPLETED_VERIFIED.
- **STAGE-A-A6 — First Playable Action and Approval Loop:** COMPLETED_VERIFIED.
- **STAGE-A-A7 — Full Combat Interface:** COMPLETED_VERIFIED.
- **STAGE-A-A8 — Inventory, Equipment, Crafting, and Vehicles:** COMPLETED_VERIFIED.
- **STAGE-A-A9 — Investigation and Social Workspaces:** COMPLETED_VERIFIED.
- **STAGE-A-A10 — World Content Authoring:** COMPLETED_VERIFIED through application PR #146 / merge `9744c5223eb41f9cac765f3807a7860ffe0d1143` and closure projection `f023c7feab49910b02abccf3ae87fd4b581c64c8`.
- **STAGE-A-A11 — Contextual AI Interfaces:** COMPLETED_VERIFIED through application PR #149 / merge `bf54f36737fe02041f02ab44a69f45c3b0b294ac`.
- **STAGE-A-A12 — Internal Alpha Hardening:** COMPLETED_VERIFIED through application PR #151 / merge `4a488f366058c4b63af9f897744388cc77688763` and closure PR #152 / merge `47a060c70f23bf5b60226f1aaa433bf301fa24db`.

No roadmap recovery process may again name A10, A11 or A12 as an unfinished ordinary Stage A activation target unless newer repository evidence explicitly reopens one under owner authority.

## Validation and CI efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md`, `governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md`, and `governance/ai/MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md` remain controlling.

Normal final validation for applicable work is exact-final-head owner-controlled self-hosted Windows + Linux plus deterministic cross-platform comparison where outputs should agree. GitHub-hosted runners are independent-audit capacity, not the routine final gate. Hosted-runner billing/minute unavailability must not be misclassified as a feature failure.

A validation/evidence-interface problem may block the affected merge. After bounded diagnostic attempts it may be quarantined so independent productive work can continue, provided the checkpoint remains explicit that the affected tranche is unfinished and all original completion gates remain intact.

## Current productive execution sequence

Unless newer owner direction or repository evidence changes dependencies, proceed as follows:

1. **Complete this roadmap/recovery reconciliation** and merge it without changing CCTI-12-T04 to complete.
2. **Activate VCH-01** and execute the bounded Validation Core Hardening series sufficiently to make persistent-runner failures self-diagnosing and self-exporting; do not let VCH expand into a general infrastructure rewrite.
3. **Re-evaluate/finalize the preserved post-GATX successor distribution** (application PR #185 or its clean successor) under the current self-hosted final-validation policy.
4. **Begin the approved APW/CSW interleaved design sequence**, starting APW-01, while preserving CCTI, DS-008 and WP-011 boundaries.
5. **Return to CCTI-12-T04** through the hardened/self-exporting evidence path when it can be safely diagnosed; require its original exact-final-head dual-platform/comparator gate before merge.
6. **Give WP-011 temporary priority whenever the borrowed Mac becomes available**, because that execution opportunity is externally time-constrained.
7. **Close DS-008 before UI-heavy APW-06 / CSW-09 if practical**, using an exact-byte-capable checkout surface.

## Phase 11 — GM and Player Experience

Complete day-to-day campaign creation, character creation, scene building, combat/non-combat play, persistence, disconnect/reconnect, safe resumption, asynchronous/hybrid workflows, and creator storycraft integration according to the later approved implementation handoffs.

## Phase 12 — AI Team and Automation

Integrate specialized GM, Rules, Narrative, World, Character, Encounter, and Developer/Content assistants with canonical retrieval, provenance, permissions, visible proposals, reversible actions, and approval gates. AI remains optional/non-authoritative unless later explicitly changed.

## Phase 13 — Internal Alpha Completion / Successor Testing

Continue candidate-specific Internal Alpha testing, authorized service integration, approved content population, gameplay testing, multiplayer/recovery, accessibility, performance, pack lifecycle, onboarding, telemetry, tester documentation, and successor distribution gates. Prior GATX completion is retained evidence; it does not pre-approve future release candidates.

## Parallel Apple track

`WP-011 — Tauri iOS/iPadOS Spike` remains a bounded Mac-dependent track. Use its latest repository checkpoint/branch/evidence when selected; do not infer completion or rerun authority from roadmap prose. Because the borrowed Mac is available only opportunistically, WP-011 may temporarily preempt normal sequencing when that hardware becomes available.

## Mandatory execution behavior

- “Continue” means perform the next verified unfinished operation.
- Read the authoritative backlog/work order before starting each item.
- Preserve parallel tracks; completing one Stage/program item does not complete or supersede CCTI, VCH, APW, CSW, Design Standards, Apple work, tester-successor work, or unrelated retained tracks.
- Distinguish missing source bytes, transfer-tool limits, hosted-runner billing/minute limits, unavailable self-hosted runners, evidence-transport failures, genuine validation failures, and owner-only gates.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, deployments, or exact-byte ingestion without matching evidence.
- Preserve source truth, provenance, variants, conflicts, stable IDs, exact-byte requirements, permissions, hidden-information boundaries, family/guardian-vs-Campaign authority boundaries, and reversibility.
- John Brandon Turner retains final authority.
