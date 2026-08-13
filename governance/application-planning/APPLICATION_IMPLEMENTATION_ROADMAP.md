# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.7.0  
**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED; PPIA COMPLETED_VERIFIED; CAPP AUTHORIZED PARALLEL WORK  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-13

## Purpose

This roadmap governs the transition from completed source recovery, canonicalization, architecture, AI-team preparation, and Phase 9 implementation foundations into verified application construction and related parallel work.

Repository evidence is mandatory. Nothing is complete merely because it was discussed, planned, drafted, generated outside the repository, or claimed. Completion requires the evidence declared by the governing work item.

The authoritative ordered Phase 9 backlog remains `governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json`. Runtime recovery is governed by `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`. When a newer internally consistent attempt-branch checkpoint or repository record is more recent than a compact runtime projection, the newer evidence controls recovery until merged or explicitly superseded.

## Current verified execution position — 2026-08-13

- **Phase 9 bounded implementation through P9-06-023 is complete.** Final P9-06-023 / AG-07 physical-device acceptance merged in `Multiversal-app` PR #102 at `fb22295948745347913bcbfebf56ecca26bf39fb`; `releaseAuthorized=false`.
- **STAGE-A-A2 — Universal Object Experience is the authorized current application item.** Application PR #103 / merge `8b7f53da1f72c280226f64be67c9aa1c280fefdf` recorded the owner decision; PR #104 / merge `dced7f92163050690c807c1fda937146bb8dce85` added the ready work order. A2 is not activated.
- **DT-001 through DT-010 Developer Toolbelt is complete.** Application PRs #105–#114 produced `mv-dev` v0.10.0 on `main`, ending at `354e24007d2c453d090a2a6cdb31d3e3333c84c1`.
- **Exact A2 source authority is recovered.** The superseding Sunday master v2.7.1, preimplementation package v1.0.0, repository compatibility audit v2.7.0, and exact `A2_CHANGED_PATH_SCOPE_v1.0.0.csv` are verified; CSV SHA-256 `945b3619b25bd24e54267c8259fc17e667063a3056214e080cbe8034836d5aa6`.
- **The governed A2 branch exists but remains unactivated.** `stage-a/a2-universal-object-experience` starts from application `main` `354e24007d2c453d090a2a6cdb31d3e3333c84c1`; the mandatory evidence/checkpoint/recovery runner still requires a repository-capable private checkout before A2-01 implementation.
- **Internal Alpha feature design is complete through IA-D09.** Prepared tester/reference/support assets do not activate tester access or release.
- **Design Standards exact-byte ingestion remains unfinished.** `DS-008-working-series-attempt-002` remains blocked on a capable exact-byte transfer/validation surface. Verified preparation remains PR #207 / merge `bd3071f6f855b66b740ba4bf1f1ba0208636548c`, PR #208 / merge `0cfd8128786e4cdd055e3e3be26bdd1854efdfa7`, PR #209 / merge `708e0ea72a6dce6f5d46ddacd042c1ddb80eee0a`, and prepared handoff commit `f0d9295215a057e0f42603a0777c276a7437aad4`.
- **PPIA is completed_verified.** All sixteen tranches are complete/completed_verified. Final substantive PPIA-16 exact head `eede4bfb530056963a4a595faac54515ff151c3b` passed **70/70** applicable hosted workflows; dedicated run `31694048323` passed; PR #294 squash-merged as signed/verified `5b87d57d9b06fbb7427b6fae7ca022509f92a5fe`.
- **PPIA final-state recovery is merged.** Exact recovery head `031d4c7af10245069a5cf8bd5b2819965e338cee` passed **70/70** hosted workflows; PR #295 squash-merged as signed/verified `8357cc812436e8bbe40c214ac0ca6e44363cc1a5`. PPIA-16 remains the completed evidence anchor; no successor is selected by PPIA completion.
- **CAPP — Character Appearance Production Preparation is owner-approved parallel work.** CAPP inherits the completed PPIA-06 appearance architecture without reopening it. `CAPP-01 — 25-Species Appearance Choice Registry + Constraint Model` is the authorized first work item and is not yet started. CAPP does not activate A2/runtime/release/deployment/tester/paid-service/production-credential authority.
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
- **CAPP:** owner-approved parallel Character Appearance production-preparation program that converts completed PPIA-06 architecture into production-ready data, tooling, renderer specifications, UX states and QA without activating application runtime.

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

P9-06-001 through P9-06-023 are complete and merged in `cybalicistjt-stack/Multiversal-app`. `P9-06-024-OWNER-DECISION-001` transitions current application focus to STAGE-A-A2 without authorizing release or deployment.

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

Final state: application PRs #105–#114 merged, `mv-dev` v0.10.0, final merge `354e24007d2c453d090a2a6cdb31d3e3333c84c1`; no A2 product implementation or release/deployment/paid-service authority was added by this support series.

## Internal Alpha feature-design track — completed design anchor

The canonical backlog is `governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md`. IA-D01 through IA-D09 are complete, with IA-D09 retained as the release-design anchor. Prepared tester/reference, demo, future-workspace-verification, and pack-lifecycle assets remain non-activating support material.

## PPIA — Parallel Pre-Implementation Advancement Program

Governing documents:
- `governance/application-planning/parallel-preimplementation/PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md`
- `governance/application-planning/parallel-preimplementation/PPIA_PROGRAM_BACKLOG.json`

**Status:** COMPLETED_VERIFIED — OWNER-APPROVED PARALLEL PROGRAM CLOSED.

PPIA was additive parallel source/content/design/authoring/acceptance work. Its completion does not supersede or complete STAGE-A-A2, Design Standards exact-byte ingestion, WP-011 / Apple work, later Stage A items, Internal Alpha release, deployment, or public release.

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

Final substantive PPIA-16 closure: exact validated head `eede4bfb530056963a4a595faac54515ff151c3b`; **70/70** workflows; dedicated run `31694048323`; PR #294; signed/verified merge `5b87d57d9b06fbb7427b6fae7ca022509f92a5fe`.

Final machine-readable recovery: exact head `031d4c7af10245069a5cf8bd5b2819965e338cee`; **70/70** workflows; PR #295; signed/verified merge `8357cc812436e8bbe40c214ac0ca6e44363cc1a5`; backlog status `completed_verified_owner_approved_parallel_work`; all sixteen tranches complete/completed_verified.

PPIA-16 preserves the Development Console design over DT-001 through DT-010: 10 DT tools, 10 AIOC control surfaces, 16 program concerns, 5 authority layers, 10 screens, 8 shared states, 8 action classes, 8 components, 12 workflows, 12 handoffs, 48 predecessor cases exact-once, and 12 integrated synthetic/noncanonical cases for 60 effective QA cases with zero intended orphaned coverage.

### Post-PPIA selection boundary

No automatic successor is selected by PPIA completion. Independent unfinished/blocked boundaries remain:
- **STAGE-A-A2:** authorized current application item, not activated; mandatory runner still needs a repository-capable checkout.
- **Design Standards / DS-008 attempt-002:** unfinished/blocked on exact-byte transfer and validation capability.
- **WP-011 / Apple track:** separate bounded Mac-dependent work under its own latest repository evidence when selected.

PPIA completion does not authorize runtime mutation, release, deployment, tester access, paid services, production credentials, or unsupported canonical-content promotion.

## CAPP — Character Appearance Production Preparation — authorized parallel track

Governing documents:
- `governance/application-planning/character-appearance-production/CAPP_CHARACTER_APPEARANCE_PRODUCTION_PREPARATION_PROGRAM.md`
- `governance/application-planning/character-appearance-production/CAPP_PROGRAM_BACKLOG.json`

**Status:** OWNER-APPROVED — AUTHORIZED PARALLEL WORK; NOT YET STARTED.

CAPP inherits and extends the completed PPIA-06 Character Appearance Creator architecture into production preparation. It does not reopen PPIA-06. PPIA-05 remains Species/Form biology authority and PPIA-03 remains actual Asset/equipment authority.

Approved execution order:
1. **CAPP-01 — 25-Species Appearance Choice Registry + Constraint Model** — AUTHORIZED NEXT / NOT STARTED
2. **CAPP-02 — Preset, Randomization and Lock Libraries** — PLANNED
3. **CAPP-03 — Pixel-Art Asset Production Standard** — PLANNED
4. **CAPP-04 — Asset Manifest and Coverage Analyzer Contract** — PLANNED
5. **CAPP-05 — Deterministic Appearance Compiler / Reference Engine** — PLANNED
6. **CAPP-06 — Wardrobe and Equipment-Fit Compatibility Catalog** — PLANNED
7. **CAPP-07 — Full Appearance Studio Screen and State Specification** — PLANNED
8. **CAPP-08 — Portrait, Token and Export Production Contract** — PLANNED
9. **CAPP-09 — Appearance Versioning and Migration Engine Contract** — PLANNED
10. **CAPP-10 — Accessibility Description Grammar** — PLANNED
11. **CAPP-11 — Expanded Generated QA and Coverage Corpus** — PLANNED
12. **CAPP-12 — Integrated Production Handoff and Completion Gate** — PLANNED

Dependency-optimized order: `CAPP-01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12`.

CAPP-01 is first because later presets, randomization, asset production, coverage analysis, renderer tooling, UI controls and QA must derive from one stable machine-readable choice/constraint authority.

CAPP may be selected as the conversational primary while STAGE-A-A2 remains the authorized current application item. CAPP selection does not activate A2 or alter the application work order. CAPP also does not complete/supersede DS-008 or WP-011 / Apple work.

No CAPP item authorizes application runtime mutation, release, deployment, tester access, paid services, production credentials, or unsupported canonical-content promotion.

## Design Standards Completion subproject — unfinished parallel track

The audited/canonicalization tranche is complete, but exact repository ingestion is not. The unfinished gate still requires T1–T4 exact-byte transfer, source/target checksum receipts, publication/full-ingestion validators, focused exact-head CI, PR/merge, and completion evidence. Do not reconstruct checksum-bound publications from excerpts, OCR, screenshots, regenerated prose, or memory.

## Phase 10 / Stage A — Core Application Implementation

Primary programs remain application shell/design system; universal objects; identity/workspaces/permissions; character workspace; campaign/scene builder; live session; combat; inventory/equipment/crafting/vehicles; investigation/social; world builder; contextual AI; and internal-alpha hardening.

### Current authorized application work item — STAGE-A-A2

`Multiversal-app/.ai/current-work-order.md` names **STAGE-A-A2 — Universal Object Experience** as `AUTHORIZED CURRENT NEXT`.

A2 covers governed Library/search and stable-ID lookup; authorization-safe filters/facets/sorting; list/card presentation; responsive Inspector and presentation profiles; Generic fallback/source-only diagnostics; relationships; progressive provenance/redaction; read-only version/variant/conflict comparison; constrained Picker; bounded Scene Add Object placement; deep-link/history/recovery; privacy; keyboard/focus; responsive/mobile; reduced motion; high zoom/reflow; accessibility; and real-data acceptance. Established slices remain A2-01 through A2-10.

### A2 exact-source and activation state

The previous changed-path authority blocker is resolved. The v2.7.1 master, v1.0.0 preimplementation package, v2.7.0 compatibility audit, and exact `A2_CHANGED_PATH_SCOPE_v1.0.0.csv` are verified. The governed branch exists from application `main` `354e24007d2c453d090a2a6cdb31d3e3333c84c1`.

**A2 is not activated.**

### Exact next A2 operation

On a repository-capable private checkout:
1. checkout/reverify the existing governed A2 branch;
2. initialize the mandatory v2.6 evidence/checkpoint/recovery runner as the v2.7.1 master directs;
3. require `verify-state` PASS and zero substantive dirty paths;
4. continue `MASTER_EXECUTION_ORDER_v2.7.1.csv` from the applicable activation step;
5. use exact `A2_CHANGED_PATH_SCOPE_v1.0.0.csv` at the governed point;
6. run `python -m tools.mv_dev preflight a2 --json`;
7. run `python -m tools.mv_dev task A2-01 --json`;
8. require exact scope authority `READY` before A2-01 implementation;
9. keep release/deployment false.

Do not activate A3–A12 merely because their designs/support packages are prepared.

## Validation and CI efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md` remains controlling: use the smallest deterministic validator during construction, batch repairs, run final relevant hosted validation at the bounded package gate, keep workflow path filters scoped, bind failures to the active head/gate, and update checkpoints only at material recovery/ready/completion boundaries.

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
- Preserve parallel tracks; completing PPIA or working CAPP does not complete or supersede A2, Design Standards, Apple work, or other retained tracks.
- Distinguish missing source bytes, transfer-tool limits, unavailable checkout, validation failure, and owner-only gates.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, deployments, or exact-byte ingestion without matching evidence.
- Preserve source truth, provenance, variants, conflicts, stable IDs, exact-byte requirements, permissions, hidden-information boundaries, and reversibility.
- John Brandon Turner retains final authority.
