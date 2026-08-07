# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.1.0  
**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-07

## Purpose

This roadmap governs the transition from completed source recovery, canonicalization, architecture, and AI-team preparation into verified application construction.

Repository evidence is mandatory. Nothing is complete merely because it was discussed, planned, drafted, generated outside the repository, or claimed. Completion requires the evidence declared by the governing work item.

The authoritative ordered Phase 9 backlog is `governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json`. If a derived roadmap description conflicts with that backlog, the canonical backlog controls and the roadmap must be corrected before implementation.

## Project phase history

- **Phase 0 — Legacy source creation:** John Brandon Turner and his brother created the legacy PDF game content.
- **Phase 0.5 — Definition document:** established Multiversal as a broad, system-flexible tabletop RPG platform.
- **Phases 1–7:** product conception, functional design, data and pack architecture, mechanics architecture, content-domain architecture, interface/workflow design, and governed repository preparation.
- **Phase 8:** standards, normalization, canonical domain architecture, source conversion, final validation, golden regression corpus, balance harness, and AI Development Team Operating Package.
- **Phase 9:** canonical product architecture and bounded implementation readiness.

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

## Owner authorization

John Brandon Turner authorized bounded implementation of **P9-06-001 through P9-06-023**.

This authorization permits repository implementation, tests, CI, and local/provider-neutral adapters. It does **not** authorize paid services or paid-plan enrollment, production deployment, public release, irreversible vendor coupling, credentials or production secrets, or spending beyond a separately approved owner gate.

## P9-06 implementation progress

Completed and merged in `cybalicistjt-stack/Multiversal-app`:

1. **P9-06-001 — Implementation authorization and repository baseline** — COMPLETE, PR #71.
2. **P9-06-002 — Local-only development environment contract** — COMPLETE, PR #72.
3. **P9-06-003 — Secrets and environment isolation policy** — COMPLETE, PR #73. **Acceptance Gate AG-01 complete.**
4. **P9-06-004 — Provider-neutral identity service port** — COMPLETE, PR #74.
5. **P9-06-005 — Provider-neutral entitlement service port** — COMPLETE, PR #75.
6. **P9-06-006 — Provider-neutral persistence and migration ports** — COMPLETE, PR #76.
7. **P9-06-007 — Realtime and authoritative-session service ports** — COMPLETE, PR #77, squash commit `149b866f530f3a8896170bfe3ba6af0c01fb2f72`.

### Corrected preparatory work

Application PR #78 created a valid provider-neutral backup, restore, and provider-exit contract package after an older derived roadmap description mislabeled that scope as P9-06-008. The authoritative backlog defines P9-06-008 differently.

Application PR #79 reclassified the package as **P9-06-011A — Recovery Contract Foundation**. It is preparatory groundwork only and does not complete P9-06-008, P9-06-009, P9-06-010, or P9-06-011.

### Current application-implementation state

**P9-06-008 — Create initial 17-table logical schema migration** remains unfinished in `P9-06-008-attempt-002` and is a paused parallel track while the owner-selected Internal Alpha design track continues. It must resume from its recorded checksum-validation failure rather than being inferred complete or restarted from scratch.

The exact required tables remain governed by `governance/phase9/P9-04_IMPLEMENTATION_READINESS_REGISTRY.json`: `subjects`, `identities`, `subscriptions`, `entitlement_grants`, `sponsored_months`, `campaigns`, `campaign_members`, `content_packs`, `canonical_objects`, `game_sessions`, `session_commands`, `session_events`, `session_projections`, `checkpoints`, `audit_events`, `outbox_events`, and `schema_migrations`.

After P9-06-008 is `completed_verified`, continue in authoritative dependency order through **P9-06-023**. P9-06-009 remains the next dependent item.

## Internal Alpha feature-design track — owner-selected active design program

The canonical backlog is `governance/application-planning/internal-alpha/INTERNAL_ALPHA_DESIGN_BACKLOG.md`.

Repository evidence through merged PR #180 establishes the true current state:

- **IA-D01 — Program foundation:** COMPLETE.
- **IA-D02 — Shared foundations:** COMPLETE.
- **IA-D03 — Character and Campaign preparation:** COMPLETE.
- **IA-D04 — First playable loop:** COMPLETE.
- **IA-D05 — Relationship, social, and investigation systems:** COMPLETE.
- **IA-D06 — Combat and Assets:** COMPLETE.
- **IA-D07 — World, adventure, and Project depth:** COMPLETE.
- **IA-D08-001 — Optional AI Assistant boundaries and interaction contract:** COMPLETE.
- **IA-D08-002 — AI permission, provenance, cost, and fallback matrix:** COMPLETE.
- **IA-D08-003 — Advanced map and vehicle deferral package:** COMPLETE, merged PR #180.
- **IA-D08-004 — Broad offline deferral package:** NEXT.
- **IA-D08-005 — Optional and experimental isolation review:** planned after IA-D08-004.
- **IA-D09 — Internal-alpha release-design package:** planned after IA-D08; includes traceability, fixture catalog, permission matrix, accessibility matrix, recovery matrix, budgets, onboarding, implementation queue, owner decisions, and completion review.

The older runtime work pointer that still names IA-D04-003 is stale and must be corrected from repository evidence before new IA mutation. IA-D04-003, IA-D04-004, IA-D04-005, IA-D05, IA-D06, IA-D07, and IA-D08-001 through IA-D08-003 must not be redone merely because that pointer lagged the merged repository state.

## Design Standards Completion subproject — paused and resumable

This is a **parallel documentation/design-system subproject**, not the currently selected IA execution track. It exists to finish the engineering-facing design standards before or alongside Phase 10 UI implementation, and it may be paused and resumed without changing the status of IA or P9 work.

### Current evidence status

During the owner/assistant design-standard session, a rebuilt **DS-006 Pattern Library** and a **DS-007 Responsive Standards** series were generated as downloadable working packages. These chat-generated files are useful source artifacts but are **not yet canonical repository deliverables** because they have not been ingested, audited, committed, validated, reviewed, and merged into `multiversal-aioc`.

Therefore:

- do not mark the design-standard subproject `completed_verified` from chat generation alone;
- preserve the generated packages for later governed ingestion;
- when this subproject resumes, begin with an inventory/audit that distinguishes valid final packages from invalid abbreviated predecessors;
- do not recreate already-good packages unless the audit finds a defect;
- resolve any numbering/name collision with existing canonical design-system documents before promotion.

### Intended design-standard path

1. **DS-006 — Pattern Library:** generated/rebuilt working set; later repository ingestion and canonical audit required.
2. **DS-007 — Responsive Standards:** working series generated through DS-007J (Responsive QA & Acceptance); later repository ingestion and canonical audit required.
3. **DS-008 — Accessibility Standards:** keyboard, mouse, controller, touch, voice, screen reader, reduced motion, color blindness, large fonts, contrast, and equivalent operation.
4. **DS-009 — Token Standards:** colors, spacing, elevation, typography, radius, icons, motion, opacity, and token governance.
5. **DS-010 — Flutter Implementation Standards:** architecture, widgets, composition, state, Riverpod, rendering, performance, testing integration, and AI coding rules.
6. **DS-011 — Testing Standards:** acceptance, golden tests, accessibility, performance, interaction, responsive behavior, and AI regression.
7. **DS-012 — Visual Language Standards:** narrative-first interface philosophy, hierarchy, density/whitespace, glass/translucency/layering, lighting/glow, color usage, iconography, artwork integration, typography personality, motion personality, gameplay-mode emotional tone, and explicit anti-drift / “never do” rules.
8. **Design-standard integration audit:** reconcile the DS working series with existing canonical design documents and Phase 10 implementation requirements; resolve duplicate identifiers before canonical promotion.
9. **Repository ingestion and validation:** commit the accepted design-standard packages in bounded governed changes, with the smallest relevant validation and one final hosted gate per bounded package or tranche.
10. **Phase 10 handoff:** expose the final canonical standards to the application implementation queue and AI/Codex coding guidance.

### Resume rule

When the owner says to return to this subproject, recover from this roadmap section and the then-current design-standard inventory. Treat the last accepted generated package as the working boundary, but repository evidence remains the authority for what is canonical.

## Validation and CI efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md` is controlling policy.

The repository has already begun correcting excessive GitHub Actions fan-out: governance PR #181 reduced Internal Alpha workflow fan-out and PR #182 continued Development Brain workflow scoping. Those changes are infrastructure optimization, not IA feature completion.

Going forward:

- use the single deterministic validator declared by the active IA work item during construction;
- do not run every historical IA validator after every new packet;
- do not regenerate historical scorecards because a work pointer changed;
- use one final relevant hosted validation gate on the completed bounded package;
- inspect and repair only checks that are actually relevant or genuinely blocking;
- keep workflow path filters scoped so an IA packet does not trigger unrelated historical feature or Development Brain suites;
- batch related validator/workflow fixes instead of creating a full CI cycle per assertion;
- treat any recurring unrelated fan-out as an infrastructure defect and repair the workflow scope rather than normalizing dozens of irrelevant checks.

## Phase 10 — Core Application Implementation

Connect verified engines, registries, services, permissions, and canonical design standards to production user interfaces.

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

Implementation method:

- build vertical slices, not disconnected mock screens;
- each slice includes navigation, real data, actions, permissions, save/load, loading/error states, responsive behavior, tests, and owner review;
- reuse universal object and relationship components rather than creating domain-specific duplicates;
- significant UI changes require deployed or reproducible interaction verification;
- use the canonical design-standard subproject outputs after governed ingestion rather than relying on stale or conflicting chat artifacts.

## Phase 11 — GM and Player Experience

Complete the day-to-day product experience for campaign creation, character creation, scene building, combat and non-combat play, persistence, disconnect/reconnect, and safe resumption.

## Phase 12 — AI Team and Automation

Integrate specialized GM, Rules, Narrative, World, Character, Encounter, and Developer/Content assistants with canonical retrieval, provenance, permissions, visible proposals, reversible actions, and approval gates.

## Phase 13 — Internal Alpha Completion

Complete major workflows, real-service integration, approved content population, gameplay testing, multiplayer/recovery, accessibility, performance, pack lifecycle, onboarding, telemetry, and internal tester documentation.

## Public-live path after Phase 13

A formal release program must govern closed alpha, beta stabilization and load testing, commercial/legal/privacy/moderation/backup/support readiness, staged production deployment and platform certification, and public launch with monitoring and rollback.

## Parallel Apple track

`WP-011 — Tauri iOS/iPadOS Spike` remains a bounded Mac-dependent track. The borrowed Mac is for one-time Apple-only build, signing, simulator/device, provisioning, packaging, and certification work. Most development must proceed without waiting for it, and project material must be removable afterward.

## Mandatory execution behavior

- “Continue” means perform the next verified unfinished repository operation.
- Do not substitute explanations or plans for work.
- Use the owner-approved recommendation process to resolve reversible ambiguity unless a decision truly requires the owner personally.
- Group compatible validation, conversion, and repair work into efficient tranches.
- Inspect CI failures, repair relevant failures, rerun the smallest applicable set, and continue automatically.
- Read the authoritative backlog item before starting each implementation or IA design item; derived roadmap prose cannot override it.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, or deployments without tool verification.
- Report the next step after every completed bounded step.
- Preserve source truth, provenance, variants, conflicts, and reversibility.
- John Brandon Turner retains final authority.
