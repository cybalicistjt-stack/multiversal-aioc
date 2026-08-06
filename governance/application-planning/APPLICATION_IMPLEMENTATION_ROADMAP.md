# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 2.0.1  
**Status:** ACTIVE — BOUNDED IMPLEMENTATION AUTHORIZED  
**Owner and final authority:** John Brandon Turner  
**Originally approved:** 2026-08-03  
**Last updated:** 2026-08-06

## Purpose

This roadmap governs the transition from completed source recovery, canonicalization, architecture, and AI-team preparation into verified application construction.

Repository evidence is mandatory. Nothing is complete merely because it was discussed, planned, drafted, or claimed. Completion requires actual files, commits, pull requests, CI results, and merges where applicable.

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

This authorization permits repository implementation, tests, CI, and local/provider-neutral adapters. It does **not** authorize:

- paid services or paid-plan enrollment;
- production deployment;
- public release;
- irreversible vendor coupling;
- credentials or production secrets;
- spending beyond a separately approved owner gate.

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

### Current next executable action

**P9-06-008 — Create initial 17-table logical schema migration.**

The exact required tables are governed by `governance/phase9/P9-04_IMPLEMENTATION_READINESS_REGISTRY.json`:

`subjects`, `identities`, `subscriptions`, `entitlement_grants`, `sponsored_months`, `campaigns`, `campaign_members`, `content_packs`, `canonical_objects`, `game_sessions`, `session_commands`, `session_events`, `session_projections`, `checkpoints`, `audit_events`, `outbox_events`, and `schema_migrations`.

The migration must remain provider-neutral, represent all 17 logical tables, define reversible up/down operations, preserve explicit constraints and indexes, include deterministic validation and dedicated CI, and must not apply a live schema or create a hosted-provider commitment.

### Remaining authorized backlog

After P9-06-008 is `completed_verified`, continue in authoritative dependency order through **P9-06-023**, automatically resolving ordinary implementation and CI failures. P9-06-009 remains the next dependent item. Stop only at a genuine owner-only decision, spending gate, deployment gate, production credential requirement, or public/internal-alpha release gate.

## Phase 10 — Core Application Implementation

Connect verified engines, registries, services, and permissions to production user interfaces.

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
- each slice includes navigation, real data, actions, permissions, save/load, loading/error states, desktop/mobile behavior, tests, and owner review;
- reuse universal object and relationship components rather than creating domain-specific duplicates;
- significant UI changes require deployed or reproducible interaction verification.

## Phase 11 — GM and Player Experience

Complete the day-to-day product experience for campaign creation, character creation, scene building, combat and non-combat play, persistence, disconnect/reconnect, and safe resumption.

## Phase 12 — AI Team and Automation

Integrate specialized GM, Rules, Narrative, World, Character, Encounter, and Developer/Content assistants with canonical retrieval, provenance, permissions, visible proposals, reversible actions, and approval gates.

## Phase 13 — Internal Alpha Completion

Complete major workflows, real-service integration, approved content population, gameplay testing, multiplayer/recovery, accessibility, performance, pack lifecycle, onboarding, telemetry, and internal tester documentation.

## Public-live path after Phase 13

A formal release program must govern:

1. closed alpha;
2. beta stabilization and load testing;
3. commercial, legal, privacy, moderation, backup, and support readiness;
4. staged production deployment and platform certification;
5. public launch with monitoring and rollback.

## Parallel Apple track

`WP-011 — Tauri iOS/iPadOS Spike` remains a bounded Mac-dependent track. The borrowed Mac is for one-time Apple-only build, signing, simulator/device, provisioning, packaging, and certification work. Most development must proceed without waiting for it, and project material must be removable afterward.

## Mandatory execution behavior

- “Continue” means perform the next verified unfinished repository operation.
- Do not substitute explanations or plans for work.
- Use John’s approved recommendation process to resolve ambiguity unless a decision truly requires him personally.
- Group compatible validation, conversion, and repair work into efficient tranches.
- Inspect CI failures, repair them, rerun, and continue automatically.
- Read the authoritative P9-06 backlog item before starting each implementation item; derived roadmap prose cannot override it.
- Never claim completion, files, commits, PRs, merges, tests, artifacts, or deployments without tool verification.
- Report the next step after every completed step.
- Preserve source truth, provenance, variants, conflicts, and reversibility.
- John Brandon Turner retains final authority.
