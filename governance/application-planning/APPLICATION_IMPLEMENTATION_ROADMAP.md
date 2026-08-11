# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.3.0  
**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED + PARALLEL PRE-IMPLEMENTATION WORK ACTIVE  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-11

## Purpose

This roadmap governs the transition from completed source recovery, canonicalization, architecture, AI-team preparation, and Phase 9 implementation foundations into verified application construction and related parallel preparation work.

Repository evidence is mandatory. Nothing is complete merely because it was discussed, planned, drafted, generated outside the repository, or claimed. Completion requires the evidence declared by the governing work item.

The authoritative ordered Phase 9 backlog remains `governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json`. Runtime recovery is governed by `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`. When a newer internally consistent attempt-branch checkpoint or repository record is more recent than a compact runtime projection, the newer evidence controls recovery until merged or explicitly superseded.

## Current verified execution position — 2026-08-11

Repository and source evidence establishes the following boundary:

- **Phase 9 bounded implementation through P9-06-023 is complete.** Final P9-06-023 / AG-07 physical-device acceptance was merged in `Multiversal-app` PR #102 at `fb22295948745347913bcbfebf56ecca26bf39fb`. The evidence includes Windows GM + Android Player, ordered authoritative events, hidden-information protection, reconnect, and focused physical-evidence validation. `releaseAuthorized=false`.
- **P9-06-024 owner decision is recorded.** `Multiversal-app` PR #103 / merge `8b7f53da1f72c280226f64be67c9aa1c280fefdf` authorized **STAGE-A-A2 — Universal Object Experience** as the exact current application work item. It did not authorize deployment or release.
- **The A2 ready work order is merged.** Application PR #104 / merge `dced7f92163050690c807c1fda937146bb8dce85` added `.ai/ready-work-orders/STAGE-A-A2-universal-object-experience.md`.
- **DT-001 through DT-010 Developer Toolbelt is complete.** Application PRs #105 through #114 produced `mv-dev` v0.10.0 on `main`, ending at squash merge `354e24007d2c453d090a2a6cdb31d3e3333c84c1`. The series includes doctor/preflight, task capsules, fixture gateway, scenario runner, permission leak scanner, UI evidence harvester, design-system linter, traceability compiler, and recovery/performance harness.
- **The previously missing exact A2 source authority has been recovered.** Owner-supplied `Pre-A2.zip` contained and verified the superseding Sunday master v2.7.1, the v1.0.0 preimplementation package, the v2.7.0 repository compatibility audit, and exact `A2_CHANGED_PATH_SCOPE_v1.0.0.csv`. The CSV SHA-256 is `945b3619b25bd24e54267c8259fc17e667063a3056214e080cbe8034836d5aa6`.
- **The governed A2 branch now exists but A2 is not activated.** `stage-a/a2-universal-object-experience` was created from application `main` `354e24007d2c453d090a2a6cdb31d3e3333c84c1`. No A2 implementation commit has been made. The mandatory v2.6 evidence/checkpoint/recovery runner still requires a repository-capable private checkout before activation, preflight/task-capsule `READY`, and A2-01 work.
- **Internal Alpha feature design is complete through IA-D09.** IA-D09 remains the completed release-design anchor. Prepared tester/reference, tester-package, demo-campaign, future-workspace-verification, and pack-lifecycle assets do not activate tester access or release.
- **Design Standards preparation is complete; exact-byte ingestion is still unfinished.** `DS-008-working-series-attempt-002` remains blocked on a repository-capable exact-byte transfer/validation surface and is not completed by preparation artifacts alone.
- **A new owner-approved parallel work track is active:** **PPIA — Parallel Pre-Implementation Advancement Program**. It contains sixteen non-Codex tranches designed to advance content quality, UX/content authoring, gameplay systems, acceptance material, onboarding, and developer-control design while A2/Design Standards wait for their required execution surfaces. PPIA does not replace or activate A2.

This section is a recovery summary, not an autosave ledger. More recent verified repository evidence controls if the project advances beyond it.

## Project phase history

- **Phase 0 — Legacy source creation:** original Multiversal game/source material.
- **Phase 0.5 — Definition document:** broad, system-flexible tabletop RPG platform definition.
- **Phases 1–7:** product conception, functional design, data/pack architecture, mechanics architecture, content-domain architecture, interface/workflow design, and governed repository preparation.
- **Phase 8:** standards, normalization, canonical domain architecture, source conversion, final validation, golden regression corpus, balance harness, and AI Development Team Operating Package.
- **Phase 9:** canonical product architecture, provider-neutral implementation foundations, acceptance gates, and bounded implementation readiness.
- **Phase 10 / Stage A:** current core application implementation program.
- **PPIA:** parallel pre-implementation advancement track that may run while checkout-dependent implementation is blocked.

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

### P9-06 implementation progress

P9-06-001 through P9-06-023 are complete and merged in `cybalicistjt-stack/Multiversal-app`. This includes repository/environment/secrets foundations; provider-neutral identity, entitlement, persistence, migration, realtime/session ports; 17-table logical schema, deterministic seed/reset, migration checks, recovery rehearsal, identity mapping, row/campaign authorization, entitlement transitions, authoritative command handling, ordered realtime events, hidden-information filtering, reconnect/restoration, telemetry, cost thresholds, provider-exit rehearsal, and final two-device acceptance.

`P9-06-024-OWNER-DECISION-001`, recorded in application PR #103, transitions the current application focus to STAGE-A-A2. It does not authorize release or deployment.

## Developer Toolbelt — DT-001 through DT-010

The owner-approved Developer Toolbelt support series is complete in `Multiversal-app`.

1. **DT-001 — Developer Toolbelt Foundation** — `mv-dev doctor`.
2. **DT-002 — A2 Preflight / Compatibility Mapper**.
3. **DT-003 — Codex Task Capsule Builder**.
4. **DT-004 — Governed Fixture Gateway**.
5. **DT-005 — Scenario/E2E Runner**.
6. **DT-006 — Permission Leak Scanner**.
7. **DT-007 — UI Evidence Harvester**.
8. **DT-008 — Design-System Compliance Linter**.
9. **DT-009 — Traceability Compiler**.
10. **DT-010 — Recovery / Performance Harness**.

Final support-series state:
- application PRs #105–#114 merged;
- `mv-dev` version `0.10.0`;
- final merge `354e24007d2c453d090a2a6cdb31d3e3333c84c1`;
- no A2 product implementation was performed by the toolbelt series;
- no release/deployment/paid-service authority was added.

These tools are intended to reduce manual repository exploration, enforce bounded scope, generate exact task packets, standardize fixtures/scenarios/evidence, detect privacy/design regressions, compile traceability, and support recovery/performance verification during later implementation.

## Internal Alpha feature-design track — completed design anchor

The canonical backlog is `governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md`.

Repository evidence establishes:
- IA-D01 through IA-D08: COMPLETE.
- **IA-D09 — Internal-alpha release-design package:** COMPLETE and retained as the release-design anchor.

Prepared post-IA-D09 support assets include:
- Stage A Tester / Reference Campaign Kit v0.1.0;
- Internal Alpha Tester Package v1.0.0, prepared but not activated;
- Canonical Demo Campaigns + E2E Portfolio v1.0.0;
- Future Workspace UI Verification Package v1.0.0, prepared not executed;
- Pack Lifecycle Acceptance Library v1.0.0, prepared not app-integrated.

These support assets reduce future implementation/hardening work but do not authorize tester access, release, deployment, or canonical game-lore promotion.

## PPIA — Parallel Pre-Implementation Advancement Program

Governing documents:
- `governance/application-planning/parallel-preimplementation/PPIA_PARALLEL_PREIMPLEMENTATION_ADVANCEMENT_PROGRAM.md`
- `governance/application-planning/parallel-preimplementation/PPIA_PROGRAM_BACKLOG.json`

**Status:** ACTIVE — OWNER APPROVED PARALLEL WORK.

Purpose: perform substantial source/content/design/authoring/acceptance work that does not require a repository-capable Codex checkout, especially while A2 and Design Standards remain blocked on execution surfaces.

PPIA is additive. It does not supersede or complete:
- STAGE-A-A2;
- Design Standards exact-byte ingestion;
- WP-011 / Apple-only work;
- later Stage A items;
- Internal Alpha release;
- deployment/public release.

### Approved sixteen tranches

1. **PPIA-01 — Content Quality & Missing-Information Closure**
2. **PPIA-02 — Creature & NPC Experience**
3. **PPIA-03 — Items, Equipment & Inventory Experience**
4. **PPIA-04 — Vehicle, Mecha & Starship Experience**
5. **PPIA-05 — Species, Forms & Character Biology**
6. **PPIA-06 — Character Appearance Creator**
7. **PPIA-07 — Rune Construction RPG System**
8. **PPIA-08 — Campaign / Scene / Session Authoring Depth**
9. **PPIA-09 — Investigation & Mystery Authoring Kit**
10. **PPIA-10 — Relationship, Social & Faction Content Framework**
11. **PPIA-11 — Encounter & Balance Design Laboratory**
12. **PPIA-12 — World & Setting Authoring System**
13. **PPIA-13 — Onboarding, Help & In-App Teaching Content**
14. **PPIA-14 — Error, Recovery & Permission Microcopy**
15. **PPIA-15 — Internal Alpha Test Content Expansion**
16. **PPIA-16 — Developer Console / AI-Team Control Surface**

Dependency-optimized execution order:
`PPIA-01 → 02 → 03 → 04 → 05 → 12 → 07 → 08 → 09 → 10 → 11 → 06 → 13 → 14 → 15 → 16`.

### Current PPIA work item

**PPIA-01 — Content Quality & Missing-Information Closure** is the owner-selected current conversational work item.

PPIA-01 must:
- inventory canonical content domains and source/provenance surfaces;
- classify incomplete/thin/inconsistent/orphaned/duplicated/ambiguous/presentation-deficient records;
- distinguish recoverable source-backed omissions from genuine source absence and authored proposals;
- create a prioritized repair backlog;
- perform only source-supported repairs;
- preserve unresolved source gaps explicitly;
- trace repairs/gaps to affected future feature surfaces.

No canonical fact may be invented merely to achieve completeness.

## Design Standards Completion subproject — unfinished parallel track

The audited/canonicalization tranche is complete, but exact repository ingestion is not.

Verified preparation includes:
- PR #207 / merge `bd3071f6f855b66b740ba4bf1f1ba0208636548c`;
- PR #208 / merge `0cfd8128786e4cdd055e3e3be26bdd1854efdfa7`;
- PR #209 / merge `708e0ea72a6dce6f5d46ddacd042c1ddb80eee0a`;
- attempt branch `governance/design-standards-publication-ingestion`;
- prepared ingestion handoff commit `f0d9295215a057e0f42603a0777c276a7437aad4`.

The unfinished completion gate still requires T1–T4 exact-byte transfer, source/target checksum receipts, publication/full-ingestion validators, focused exact-head CI, PR/merge, and completion evidence.

Do not reconstruct checksum-bound publications from excerpts, OCR, screenshots, regenerated prose, or memory.

## Phase 10 / Stage A — Core Application Implementation

Primary programs remain:

1. application shell and design system;
2. universal object browser, inspector, picker, relationships, variants, and provenance;
3. identity, dashboards, workspaces, and permissions;
4. character workspace and character creation;
5. campaign and scene builder;
6. live session and action-proposal/GM-approval loop;
7. combat interface;
8. inventory, equipment, crafting, and vehicles;
9. investigation and social workspaces;
10. world builder and content creation tools;
11. contextual AI interfaces;
12. internal-alpha hardening.

### Current authorized application work item — STAGE-A-A2

`Multiversal-app/.ai/current-work-order.md` names **STAGE-A-A2 — Universal Object Experience** as `AUTHORIZED CURRENT NEXT`.

A2 implements:
- governed universal object Library/search and exact stable-ID lookup;
- authorization-safe suggestions, filters, facets, and sorting;
- list/card presentation;
- responsive universal Inspector and explicit presentation profiles;
- Generic fallback and bounded source-only diagnostics;
- relationships and accessible nonvisual traversal;
- progressive provenance with safe redaction;
- read-only version/variant/conflict comparison;
- constrained Picker with current-authority revalidation;
- bounded Scene Add Object caller creating a distinct Campaign-local placement without mutating the Definition;
- deep-link/history/recovery semantics;
- privacy, keyboard/focus, responsive/mobile, reduced-motion, high-zoom/reflow, accessibility, and real-data acceptance.

Established slices remain A2-01 through A2-10.

### A2 exact-source and activation state

The previous changed-path authority blocker is resolved.

Verified supplied artifacts:
- `STAGE_A_A2_SUNDAY_CODEX_MASTER_EXECUTION_v2.7.1.zip` — SHA-256 matched its recorded authority;
- `STAGE_A_A2_PREIMPLEMENTATION_EXECUTION_PACKAGE_v1.0.0.zip` — SHA-256 matched;
- `STAGE_A_A2_APPLICATION_REPOSITORY_COMPATIBILITY_AUDIT_v2.7.0.zip` — SHA-256 matched;
- exact `A2_CHANGED_PATH_SCOPE_v1.0.0.csv` — SHA-256 `945b3619b25bd24e54267c8259fc17e667063a3056214e080cbe8034836d5aa6`.

The v2.7.1 master validation passed with 14 top-level packages, 20 recursive ZIP archives, 16 discovered validators, 337 checksum entries, 16 execution steps, and 28 blocking evidence-ledger entries. The compatibility audit passed with 50 planned path actions and zero required new runtime dependencies.

The branch `stage-a/a2-universal-object-experience` exists from app `main` `354e24007d2c453d090a2a6cdb31d3e3333c84c1`.

**A2 is not activated.**

### Exact next A2 operation

On a repository-capable private checkout:

1. checkout/reverify the existing governed A2 branch; do not create a second branch;
2. initialize the mandatory v2.6 evidence/checkpoint/recovery runner exactly as the v2.7.1 Sunday master directs;
3. require runner `verify-state` PASS and zero substantive dirty paths;
4. continue `MASTER_EXECUTION_ORDER_v2.7.1.csv` from the applicable activation step;
5. transfer/use the exact `A2_CHANGED_PATH_SCOPE_v1.0.0.csv` at the governed point in that sequence;
6. run `python -m tools.mv_dev preflight a2 --json`;
7. run `python -m tools.mv_dev task A2-01 --json`;
8. require exact scope authority `READY` before A2-01 implementation;
9. keep release/deployment false.

Do not activate A3–A12 merely because their designs/support packages are prepared.

## Validation and CI efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md` remains controlling.

- use the smallest deterministic validator during construction;
- batch related repairs;
- run final relevant hosted validation at the bounded package gate;
- keep workflow path filters scoped;
- do not treat historical CI failures as current blockers without binding them to the active head/gate;
- update checkpoints at material recovery/ready/completion boundaries, not every minor action.

## Phase 11 — GM and Player Experience

Complete the day-to-day product experience for campaign creation, character creation, scene building, combat/non-combat play, persistence, disconnect/reconnect, and safe resumption.

## Phase 12 — AI Team and Automation

Integrate specialized GM, Rules, Narrative, World, Character, Encounter, and Developer/Content assistants with canonical retrieval, provenance, permissions, visible proposals, reversible actions, and approval gates.

AI remains optional/non-authoritative unless a later explicitly approved contract changes that boundary.

## Phase 13 — Internal Alpha Completion

Complete major workflows, authorized service integration, approved content population, gameplay testing, multiplayer/recovery, accessibility, performance, pack lifecycle, onboarding, telemetry, tester documentation, and candidate-specific Internal Alpha gates.

Prepared tester/demo/reference assets do not authorize tester access or release by themselves.

## Parallel Apple track

`WP-011 — Tauri iOS/iPadOS Spike` remains a bounded Mac-dependent track. Use its latest repository checkpoint/branch/evidence when selected; do not infer completion or rerun authority from roadmap prose.

## Mandatory execution behavior

- “Continue” means perform the next verified unfinished operation.
- Read the authoritative backlog/work order before starting each item.
- Preserve parallel tracks; selecting PPIA does not complete or supersede A2, Design Standards, or Apple work.
- Distinguish missing source bytes, transfer-tool limits, unavailable checkout, validation failure, and owner-only gates.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, deployments, or exact-byte ingestion without matching evidence.
- Preserve source truth, provenance, variants, conflicts, stable IDs, exact-byte requirements, permissions, hidden-information boundaries, and reversibility.
- John Brandon Turner retains final authority.
