# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.2.0  
**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-11

## Purpose

This roadmap governs the transition from completed source recovery, canonicalization, architecture, and AI-team preparation into verified application construction.

Repository evidence is mandatory. Nothing is complete merely because it was discussed, planned, drafted, generated outside the repository, or claimed. Completion requires the evidence declared by the governing work item.

The authoritative ordered Phase 9 backlog is `governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json`. If a derived roadmap description conflicts with that backlog, the canonical backlog controls and the roadmap must be corrected before implementation.

The permanent recovery protocol is `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`. Runtime pointers and compact status projections may lag legitimate attempt-branch evidence; when they do, the newest internally consistent repository evidence controls recovery and the stale projection must be corrected through a bounded verified change.

## Current verified execution position — 2026-08-11

Repository evidence establishes the following current boundary:

- **Phase 9 bounded implementation through P9-06-023 is complete.** The final P9-06-023 / AG-07 two-physical-device acceptance was completed in `Multiversal-app` PR #102 and squash-merged as `fb22295948745347913bcbfebf56ecca26bf39fb`. The evidence records a Windows laptop GM and Android Player, ordered authoritative events, hidden-information protection, reconnect, and passing focused physical-evidence validation. `releaseAuthorized` remains `false`.
- **P9-06-024 owner decision is recorded.** `Multiversal-app` PR #103, merge `8b7f53da1f72c280226f64be67c9aa1c280fefdf`, closed P9-06-023 continuity and set `STAGE-A-A2 — Universal Object Experience` as the authorized current application work item. This did not authorize release or deployment.
- **STAGE-A-A2 is authorized and prepared, but implementation has not started.** `Multiversal-app` PR #104, merge `dced7f92163050690c807c1fda937146bb8dce85`, added the governed ready work order. At the 2026-08-11 recovery check, the prescribed branch `stage-a/a2-universal-object-experience` did not yet exist.
- **Internal Alpha feature design is complete through IA-D09.** IA-D09 remains the release-design anchor. Subsequent tester/reference, tester-package, demo-campaign, future-workspace-verification, and pack-lifecycle acceptance assets are prepared support packages; they do not activate tester access, later Stage A programs, release, deployment, or canonical game-content promotion.
- **Design Standards preparation is complete; exact-byte repository ingestion is not.** The audit/canonicalization tranche merged through PR #208. The active `DS-008-working-series-attempt-002` branch subsequently completed pre-ingestion preparation at `f0d9295215a057e0f42603a0777c276a7437aad4`, but T1–T4 exact-byte transfer, checksum receipts, validators, exact-head CI, PR/merge, and completion evidence remain unfinished.
- **Parallel-track rule:** the AIOC conversational primary may remain the unfinished Design Standards attempt while `Multiversal-app` independently records A2 as its authorized current implementation work order. Neither track silently supersedes or completes the other.

This section is a recovery summary, not an autosave ledger. More recent verified repository evidence controls if the project advances beyond it.

## Project phase history

- **Phase 0 — Legacy source creation:** John Brandon Turner and his brother created the legacy PDF game content.
- **Phase 0.5 — Definition document:** established Multiversal as a broad, system-flexible tabletop RPG platform.
- **Phases 1–7:** product conception, functional design, data and pack architecture, mechanics architecture, content-domain architecture, interface/workflow design, and governed repository preparation.
- **Phase 8:** standards, normalization, canonical domain architecture, source conversion, final validation, golden regression corpus, balance harness, and AI Development Team Operating Package.
- **Phase 9:** canonical product architecture, provider-neutral implementation foundations, acceptance gates, and bounded implementation readiness.
- **Phase 10 / Stage A:** current core application implementation program.

## Completed Phase 8 milestones

- **8D-007 — Golden Test Corpus and Balance Harness:** COMPLETE.
- **8D-008 — AI Development Team Operating Package:** COMPLETE.
- **8E-009 — Canonical Object Template and CSV-First Program:** COMPLETE.
- 20 governed datasets, 19,199 source rows, 19,199 promoted records, zero unprocessed rows, and passing provenance/runtime/install/uninstall validation.

## Phase 9 — Product Architecture and Implementation Readiness

The uploaded Phase 9 package remains canonical. The generic AI roadmap was renamed **Phase 9R** to prevent duplication.

Completed first-level packages:

1. **P9-01 — Entitlements and freemium architecture:** subscriptions, sponsored months, campaign grants, restrictions, cancellation, and portability.
2. **P9-02 — Authoritative session architecture:** two-device multiplayer, reconnect, checkpoints, hidden information, and transport abstraction.
3. **P9-03 — Technology and service decision package:** selected a Postgres-centered managed-backend architecture class while preserving provider neutrality.
4. **P9-04 — Postgres-centered architecture contract:** database, identity, authorization, entitlements, sessions, realtime, security, migration, backup, observability, and provider-exit contracts.
5. **P9-05 — Bounded technical spike and cost envelope:** deterministic two-device validation and a target operating envelope of $0–$25/month, with owner review above $35/month.
6. **P9-06 — Implementation backlog and acceptance gates:** 7 workstreams, 24 ordered backlog items, and 8 acceptance gates.

## Owner authorization and release boundary

John Brandon Turner authorized bounded implementation of **P9-06-001 through P9-06-023**. That bounded implementation program has now reached verified completion through P9-06-023.

The subsequent owner decision recorded by P9-06-024 authorizes `STAGE-A-A2 — Universal Object Experience` as the current application work item.

These authorizations permit repository implementation, tests, CI, local/provider-neutral adapters, and the governed A2 work defined by its work order. They do **not** authorize paid services or paid-plan enrollment, production deployment, public release, irreversible vendor coupling, credentials or production secrets, tester access, or spending beyond a separately approved owner gate.

## P9-06 implementation progress — completed through P9-06-023

Completed and merged in `cybalicistjt-stack/Multiversal-app`:

1. **P9-06-001 — Implementation authorization and repository baseline** — COMPLETE, PR #71.
2. **P9-06-002 — Local-only development environment contract** — COMPLETE, PR #72.
3. **P9-06-003 — Secrets and environment isolation policy** — COMPLETE, PR #73. **Acceptance Gate AG-01 complete.**
4. **P9-06-004 — Provider-neutral identity service port** — COMPLETE, PR #74.
5. **P9-06-005 — Provider-neutral entitlement service port** — COMPLETE, PR #75.
6. **P9-06-006 — Provider-neutral persistence and migration ports** — COMPLETE, PR #76.
7. **P9-06-007 — Realtime and authoritative-session service ports** — COMPLETE, PR #77, squash commit `149b866f530f3a8896170bfe3ba6af0c01fb2f72`.
8. **P9-06-008 — Initial 17-table logical schema migration** — COMPLETE.
9. **P9-06-009 — Deterministic seed and reset fixtures** — COMPLETE.
10. **P9-06-010 — Expand-migrate-contract migration checks** — COMPLETE.
11. **P9-06-011 — Backup restore and export rehearsal scripts** — COMPLETE, building on the preserved P9-06-011A recovery-contract foundation.
12. **P9-06-012 — Provider-independent user identity mapping** — COMPLETE.
13. **P9-06-013 — Row and campaign authorization policies** — COMPLETE.
14. **P9-06-014 — Subscription and sponsored-month entitlement evaluator** — COMPLETE.
15. **P9-06-015 — Entitlement transition and cancellation tests** — COMPLETE.
16. **P9-06-016 — Authoritative session command handler** — COMPLETE.
17. **P9-06-017 — Ordered realtime event delivery** — COMPLETE.
18. **P9-06-018 — Hidden-information response filtering** — COMPLETE, PR #90.
19. **P9-06-019 — Checkpoint reconnect and deterministic restoration** — COMPLETE, PR #91.
20. **P9-06-020 — Structured audit and operational telemetry** — COMPLETE, PR #92.
21. **P9-06-021 — Cost budget and resource threshold alarms** — COMPLETE, PR #93.
22. **P9-06-022 — Provider-exit export/import rehearsal** — COMPLETE, PR #94.
23. **P9-06-023 — Two-device online internal-alpha acceptance suite / AG-07** — COMPLETE. Deterministic simulated acceptance and the physical-device operator/evidence tooling were built through PRs #95–#101; the final real laptop + Android evidence and insecure-LAN browser correction were merged in PR #102 at `fb22295948745347913bcbfebf56ecca26bf39fb`.

### Preserved preparatory history

Application PR #78 created a valid provider-neutral backup, restore, and provider-exit contract package after an older derived roadmap description mislabeled that scope as P9-06-008.

Application PR #79 reclassified the package as **P9-06-011A — Recovery Contract Foundation**. That package remains preparatory provenance for the completed P9-06-011 work and must not be rewritten as a separate later migration.

### P9-06-024 transition

`P9-06-024-OWNER-DECISION-001` is recorded in `Multiversal-app` PR #103. It closes the old P9 queue as the current implementation focus and authorizes **STAGE-A-A2 — Universal Object Experience** as the exact current application work item.

P9-06-024 does not set `releaseAuthorized=true`, does not authorize deployment, and does not activate a later Stage A item.

## Internal Alpha feature-design track — completed design anchor

The canonical backlog is `governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md`.

Repository evidence now establishes:

- **IA-D01 — Program foundation:** COMPLETE.
- **IA-D02 — Shared foundations:** COMPLETE.
- **IA-D03 — Character and Campaign preparation:** COMPLETE.
- **IA-D04 — First playable loop:** COMPLETE.
- **IA-D05 — Relationship, social, and investigation systems:** COMPLETE.
- **IA-D06 — Combat and Assets:** COMPLETE.
- **IA-D07 — World, adventure, and Project depth:** COMPLETE.
- **IA-D08 — Optional/experimental boundaries and deferrals:** COMPLETE, including optional AI boundaries, AI permission/provenance/cost/fallback, advanced map/vehicle deferral, broad-offline deferral, and optional/experimental isolation review.
- **IA-D09 — Internal-alpha release-design package:** COMPLETE and retained as the release-design anchor.

IA-D09 does not itself authorize an Internal Alpha release. Its release/tester gates remain owner-controlled.

### Prepared post-IA-D09 support assets

The following later preparation packages are durable support evidence and must retain their nonauthorization boundaries:

- **Stage A Tester / Reference Campaign Kit v0.1.0** — prepared complete synthetic/noncanonical test fixture package; 27 portable synthetic records, 24 IA-D09 mapped journeys, six role profiles, deterministic reset. Handoff commit `156e5559a82406bdc884568b3f1046cb96c8fbf9`.
- **Internal Alpha Tester Package v1.0.0** — prepared complete but not activated; tester access remains unauthorized until candidate-specific parameters and owner gate are satisfied. Handoff commit `07a7628e319f03d49d9ff0ad0e69c496a91ffa1f`.
- **Canonical Demo Campaigns + E2E Portfolio v1.0.0** — four canonical demo/QA Campaign fixtures, 57 portable synthetic records, 48 E2E steps, 52 checkpoints; canonical for demo/test behavior, not canonical game lore. Handoff commit `2a7bd4671175d503efcf6e3471fe2e200aa57e67`.
- **Future Workspace UI Verification Package v1.0.0** — prepared complete, not executed; eight major future workspaces and 96 blocking screenshot requirements. Handoff commit `37d9847789affe37b5b7a6d0922207f1ebdd8dfc`.
- **Pack Lifecycle Acceptance Library v1.0.0** — prepared complete, not app-integrated; 33 real fixture pack archives, 50 deterministic lifecycle scenarios, 25 threat cases, 24 blocking acceptance gates, and a 12,000-object bounded large-pack fixture. Handoff commit `7b52b803a086614285c9663fa1d6a03b571546dd`.

These assets are intended to reduce reinterpretation during A2–A12 implementation and hardening. They do not move the current application pointer by themselves.

## Design Standards Completion subproject — active unfinished ingestion track

This remains a **parallel documentation/design-system subproject**. It can be the AIOC conversational primary while A2 remains the authorized current application work item.

### Completed Design Standards recovery/canonicalization work

The owner-supplied Design Standards series has now passed the initial recovery/audit tranche that the previous roadmap described as future work.

Verified repository evidence includes:

- PR #207 / merge `bd3071f6f855b66b740ba4bf1f1ba0208636548c` — governed Design Standards working-series inventory/canonicalization audit;
- PR #208 / merge `0cfd8128786e4cdd055e3e3be26bdd1854efdfa7` — records the audit tranche as `completed_verified`;
- PR #209 / merge `708e0ea72a6dce6f5d46ddacd042c1ddb80eee0a` — records the exact-publication ingestion boundary without falsely claiming the publication bytes were already canonical;
- active attempt branch `governance/design-standards-publication-ingestion` — newer pre-ingestion preparation and checkpoint evidence beyond the merged `main` projection;
- commit `f0d9295215a057e0f42603a0777c276a7437aad4` — prepared Design Standards exact-byte ingestion completion package/handoff.

The prepared Design Standards state now freezes:

- 56 candidate artifacts / 55 unique active or working IDs;
- 27 DS-001–DS-005 foundation artifacts preserved as working references;
- 14 selected DS-006 Pattern Library packages;
- 10 selected DS-007 Responsive Standards packages;
- five FINAL_VALIDATED DS-008–DS-012 publications;
- duplicate/legacy/numbering dispositions;
- an acyclic dependency graph;
- a 12-program Phase-10 usage map;
- a 25-gate ingestion acceptance matrix;
- source/target checksum receipt requirements;
- exact-byte transfer manifests and full-ingestion validation tooling.

### Canonical status boundary

Preparation is complete. Repository ingestion is not.

The current attempt remains unfinished until the exact source bytes are transferred and every declared completion gate exists. The four transfer classes are:

1. **T1 — DS-008–DS-012:** exact FINAL_VALIDATED publication/evidence bytes.
2. **T2 — DS-006 A–N:** selected recovered Pattern Library packages.
3. **T3 — DS-007 A–J:** selected recovered Responsive Standards packages.
4. **T4 — DS-001–DS-005:** exact preservation as working references only, including deterministic DS-004A collision comparison/quarantine.

Required final evidence includes exact source/target checksums, `DS_EXACT_BYTE_TRANSFER_RECEIPTS.json`, `python tools/validate_design_standards_publications.py`, `python tools/validate_design_standards_full_ingestion.py`, focused exact-head hosted CI, PR, merge, and governed completion evidence.

If the required owner/source archive or prepared exact-byte packages are not available on the active execution surface, record **source bytes unavailable**. If the bytes are available but a repository tool cannot transfer them byte-for-byte, record an **execution-surface transfer blocker**. Do not reconstruct checksum-bound artifacts from truncated text, generated prose, screenshots, OCR, or memory.

No owner decision is currently required for the mechanical ingestion work itself.

### Collision, precedence, and stack rules

- Current DS-006 is the Pattern Library A–N; legacy DS-006 Iconography is evidence only.
- Current DS-007 is Responsive Standards A–J; legacy DS-007 Motion is evidence only.
- DS-007A v0.2 is superseded by v1.0 FINAL.
- `67.zip` is a duplicate transport/recovery container and is not an additional standard source.
- Older DS-008 drafts and earlier Audio/Haptic → Accessibility → Layout → Navigation numbering files remain evidence only.
- DS-001–DS-005 remain working references and must not be upgraded to `FINAL — VALIDATED` by ingestion mechanics.
- DS-009 governs token architecture/naming/governance after ingestion while earlier color/typography/spacing/elevation standards remain preserved semantic/value references.
- DS-012 remains visual-language authority; later Stage A functional specifications are additive where nonconflicting.
- DS-010 remains a valid Flutter-specific standard, but the current Stage A application is React/Vite/TypeScript. DS-010 must not introduce Flutter, Riverpod, or a stack migration into the current client. Stack-neutral principles may be consulted where applicable.

### Design Standards exact next action

When the required exact source packages/archive are accessible in a repository-capable checkout, resume `DS-008-working-series-attempt-002` from its newest branch checkpoint and perform T1–T4 byte transfer, checksum capture, prepared validators, focused exact-head CI, PR/merge, and completion projection. Do not redesign or regenerate the standards.

## Validation and CI efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md` is controlling policy.

Going forward:

- use the smallest deterministic validator declared by the active work item during construction;
- do not run every historical validator after every new package or implementation edit;
- do not regenerate historical scorecards because a work pointer changed;
- use one final relevant hosted validation gate on the completed bounded package unless the declared completion gate requires more;
- inspect and repair only checks that are actually relevant or genuinely blocking;
- keep workflow path filters scoped so one work item does not trigger unrelated historical suites;
- batch related validator/workflow fixes instead of creating a full CI cycle per assertion;
- treat recurring unrelated fan-out as an infrastructure defect rather than normalizing dozens of irrelevant checks;
- distinguish historical entries in `governance/ci-failures/INDEX.md` from a current blocking failure by binding blockers to the active attempt/head/gate.

## Phase 10 / Stage A — Core Application Implementation

Connect verified engines, registries, services, permissions, and canonical design standards to production-quality user interfaces through governed vertical slices.

Primary programs:

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

### Current authorized Stage A work item — STAGE-A-A2

`Multiversal-app/.ai/current-work-order.md` names **STAGE-A-A2 — Universal Object Experience** as `AUTHORIZED CURRENT NEXT`.

The governed work order merged in application PR #104 at `dced7f92163050690c807c1fda937146bb8dce85`. It explicitly records **READY FOR ACTIVATION — IMPLEMENTATION NOT YET STARTED**.

A2 implements:

- governed universal object Library/search and exact stable-ID lookup;
- authorization-safe suggestions, filters, facets, and sorting;
- list/card presentation;
- responsive universal Inspector and explicit presentation profiles;
- Generic fallback and bounded source-only diagnostic mode;
- relationships and accessible nonvisual relationship traversal;
- progressive provenance with safe redaction;
- read-only version/variant/conflict comparison;
- reusable constrained Picker with current-authority revalidation;
- one bounded Scene Add Object caller adapter creating a distinct Campaign-local placement without mutating the source Definition;
- deep-link/history/recovery semantics;
- privacy, keyboard, focus, responsive/mobile, reduced-motion, high-zoom/reflow, and accessibility acceptance;
- real-data validation in addition to synthetic fixtures.

The established implementation sequence is:

- **A2-01** — contracts, schemas, fixtures, explicit profile registry, deterministic local adapter;
- **A2-02** — Library and deterministic search/exact-ID/suggestions;
- **A2-03** — filters, authorized facets, sort, card/list views;
- **A2-04** — universal Inspector shell, record layers, anchor profiles;
- **A2-05** — remaining profiles, Generic fallback, source-only diagnostic mode;
- **A2-06** — relationships, provenance, related-object navigation;
- **A2-07** — Picker, provisional selection, final revalidation;
- **A2-08** — Scene Add Object reference caller adapter and local/test persistence;
- **A2-09** — version/variant/conflict compare plus deep-link/history recovery;
- **A2-10** — privacy, accessibility, responsive, large-corpus, and evidence closure.

The companion A2 automation/Sunday-master handoff v2.6.0 records:

- all ten slices A2-01 through A2-10;
- 49 evidence requirements;
- all 36 hostile blocking cases;
- 11,881 governed release objects in the master corpus;
- exact-head evidence controls that prevent an older PASS or mismatched PR/CI head from satisfying completion.

### Exact next application operation

Before A2 implementation mutation, perform the recorded compatibility audit against current `Multiversal-app` React/Vite/TypeScript/A1 structure and the final A2 v2.6.0 execution package. Produce the Codex-facing existing-module/path/script/workflow map and collision/dependency review. Then, if current repository evidence still authorizes A2 and no stop condition is triggered, create exactly one implementation branch:

`stage-a/a2-universal-object-experience`

and begin **A2-01**.

At the 2026-08-11 verification boundary, that branch had not yet been created. Recheck before acting; do not recreate or overwrite it if newer evidence exists.

### Stage A implementation method

- build vertical slices, not disconnected mock screens;
- each slice includes navigation, real data, actions, permissions, save/load, loading/error states, responsive behavior, tests, and evidence appropriate to the slice;
- reuse universal object and relationship components rather than creating domain-specific duplicates;
- significant UI changes require reproducible interaction/visual verification against the governing standards and A2 evidence contract;
- apply canonical Design Standards once ingested; while exact ingestion remains incomplete, use already-approved repository authority and the audited DS reconciliation boundary without pretending uncommitted bytes are canonical;
- keep source identity, version, provenance, Definition/Variant/Placement/Live Instance/Snapshot/Projection distinctions intact;
- do not activate A3–A12 merely because their designs or support packages are prepared.

### A2 completion boundary

A2 requires all declared contract/behavior/real-data/privacy/accessibility/evidence gates, final exact-head CI, merge evidence, and closure receipt. A2 is not complete if only synthetic/mock records pass while the governed real-data flow fails.

No later Stage A item is activated by A2 completion alone. After verified A2 merge, update canonical state and follow the next explicit roadmap/owner authority.

## Phase 11 — GM and Player Experience

Complete the day-to-day product experience for campaign creation, character creation, scene building, combat and non-combat play, persistence, disconnect/reconnect, and safe resumption.

## Phase 12 — AI Team and Automation

Integrate specialized GM, Rules, Narrative, World, Character, Encounter, and Developer/Content assistants with canonical retrieval, provenance, permissions, visible proposals, reversible actions, and approval gates.

AI remains optional/non-authoritative unless a later explicitly approved contract changes that boundary. Core application completion must not depend on an AI provider.

## Phase 13 — Internal Alpha Completion

Complete major workflows, real-service integration where separately authorized, approved content population, gameplay testing, multiplayer/recovery, accessibility, performance, pack lifecycle, onboarding, telemetry, tester documentation, and candidate-specific Internal Alpha gates.

The prepared Internal Alpha tester package and demo/reference fixtures reduce future preparation work but do not authorize tester access or an Internal Alpha release by themselves.

## Public-live path after Phase 13

A formal release program must govern closed alpha, beta stabilization and load testing, commercial/legal/privacy/moderation/backup/support readiness, staged production deployment and platform certification, and public launch with monitoring and rollback.

No current Phase 9, Design Standards, IA-design, Stage A preparation, or A2 authorization grants public-live authority.

## Parallel Apple track

`WP-011 — Tauri iOS/iPadOS Spike` remains a bounded Mac-dependent track. The borrowed Mac is for one-time Apple-only build, signing, simulator/device, provisioning, packaging, and certification work. Most development must proceed without waiting for it, and project material must be removable afterward.

The Apple track must not be inferred complete or rerun from roadmap prose alone; use its latest repository checkpoint/branch/evidence when it is selected.

## Mandatory execution behavior

- “Continue” means perform the next verified unfinished repository operation.
- Do not substitute explanations or plans for work.
- Use the owner-approved recommendation process to resolve reversible ambiguity unless a decision truly requires the owner personally.
- Group compatible validation, conversion, and repair work into efficient tranches.
- Inspect CI failures, repair relevant failures, rerun the smallest applicable set, and continue automatically.
- Read the authoritative backlog/work order before starting each implementation item; derived roadmap prose cannot override it.
- Compare `main` recovery state with the exact attempt branch before restarting unfinished work; preserve newer branch checkpoints and substantive commits.
- Distinguish missing source bytes from unavailable transfer tooling, unavailable checkout, failed validation, and owner-only gates.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, deployments, or exact-byte ingestion without matching tool/repository evidence.
- Report the next step after every completed bounded step.
- Preserve source truth, provenance, variants, conflicts, stable IDs, exact-byte requirements, and reversibility.
- John Brandon Turner retains final authority.
