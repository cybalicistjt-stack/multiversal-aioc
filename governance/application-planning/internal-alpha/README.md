# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.3.0  
**Status:** ACTIVE — DESIGN PROGRAM  
**Owner and final authority:** John Brandon Turner  
**Established:** 2026-08-05

## Purpose

MV-IA-001 converts the approved Multiversal Project Bible, Stage A UI Implementation Program, Phase 9 architecture, and earlier Feature Module Roadmap into implementation-ready internal-alpha feature packets.

This is a design and governance program. It does not bypass the active P9-06 implementation sequence, authorize production, or place unapproved code into `Multiversal-app`.

## Terminology correction

There is **no prophecy content or prophecy feature domain** in this program. A prior reference to prophecy was an autocorrect mistake for **project**. The mistaken term must not be promoted into requirements, content architecture, taxonomy, roadmap, or feature design.

## Mission

Define exactly what internal alpha contains, why each feature is present, how features depend on shared systems, how Player and GM journeys connect, and what evidence will make each feature implementation-ready and alpha-ready.

The program must prevent two opposite failures:

1. treating internal alpha as the entire final application;
2. reducing internal alpha to disconnected mock screens or a narrow technical demo.

## Governing sources

1. `MULTIVERSAL_PROJECT_BIBLE_v2.0.md`
2. `governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md`
3. `governance/application-planning/STAGE_A_UI_IMPLEMENTATION_PROGRAM.md`
4. Phase 9 architecture and P9-06 acceptance-gate records
5. `feature-modules.html` as historical feature-planning evidence
6. current verified repository evidence
7. direct owner decisions

When sources conflict, direct owner decisions and newer verified repository evidence control.

## Feature classes

Every feature is assigned one internal-alpha class:

- **entry-critical** — required before internal alpha may begin;
- **alpha-required** — must be completed and tested during internal alpha before it may close;
- **experimental** — may be enabled for selected tests but cannot block the entire alpha unless promoted;
- **deferred** — deliberately excluded from the current internal-alpha scope.

A feature may contain a narrow alpha slice while its full long-term form remains deferred.

## Design method

Features are designed as vertical slices:

> navigation → real governed data → actions → permissions → persistence → recovery → responsive behavior → accessibility → tests

A screen description alone is not a completed feature design.

## Completed design work

### Tranche IA-D01 — Program foundation

Complete:

- internal-alpha scope and success definition;
- complete feature registry;
- dependency map;
- Player and GM user journeys;
- shared-system inventory;
- acceptance matrix;
- historical deferred-feature reconciliation;
- bounded content and fixture baseline;
- owner-decision register;
- standard feature-packet template;
- ordered feature-design backlog;
- machine validation and CI.

### IA-D02-001 — Universal Object Experience

Complete at design level:

- object browser and result contract;
- search, filter, exact stable-ID lookup, and safe count behavior;
- object inspector and original-source view;
- provenance and source-coverage presentation;
- bounded relationship traversal with accessible list alternative;
- version, variant, supersession, conflict, and incomplete-data comparison;
- constrained object picker and stable selection receipt;
- Character and Scene caller requirements;
- role, permission, entitlement, pack, persistence, recovery, responsive, accessibility, telemetry, test, fixture, and implementation-handoff requirements;
- fifteen blocking acceptance criteria;
- dedicated implementation-ready packet validation.

The packet is implementation-ready as a design artifact. Application implementation remains dependency-gated.

### IA-D02-002 — Permissions and Hidden Information

Complete at design level:

- deny-by-default server authorization and field-safe projection contract;
- Player, GM, Assistant GM, creator, observer, Owner/Admin, service, and AI authority boundaries;
- ten visibility classes and stable internal/user-safe decision reason codes;
- safe object results, counts, facets, aliases, exact IDs, provenance, relationships, comparison, selection, realtime, notification, history, export, object-storage, diagnostics, cache, offline, and AI surfaces;
- explicit Player-private note and Owner/Admin support-access boundaries;
- service/database agreement, mutation reauthorization, server-generated Player preview, fail-closed behavior, revocation, and cache invalidation;
- twenty-eight protected-surface records and twenty required denied cases in a machine-readable companion matrix;
- twenty blocking acceptance criteria;
- zero-AI and zero-paid-service core authorization requirement;
- provider-neutral implementation decomposition and dependency holds;
- expanded CI validation for packets and companion files.

The packet is implementation-ready as a design artifact. Application implementation remains dependency-gated.

## File map

- `INTERNAL_ALPHA_SCOPE.md` — release boundary and success definition
- `INTERNAL_ALPHA_FEATURE_REGISTRY.json` — machine-readable feature inventory and design status
- `INTERNAL_ALPHA_DEPENDENCY_MAP.md` — dependency order and shared foundations
- `INTERNAL_ALPHA_USER_JOURNEYS.md` — end-to-end Player and GM journeys
- `INTERNAL_ALPHA_SHARED_SYSTEMS.md` — systems reused by multiple features
- `INTERNAL_ALPHA_ACCEPTANCE_MATRIX.md` — feature and release evidence
- `INTERNAL_ALPHA_DEFERRED_FEATURES.md` — historical list and current scope decisions
- `INTERNAL_ALPHA_CONTENT_AND_FIXTURES.md` — bounded test corpus and fixture requirements
- `INTERNAL_ALPHA_OWNER_DECISIONS.md` — owner-only decisions and future gates
- `INTERNAL_ALPHA_DESIGN_BACKLOG.md` — dependency-ordered packet backlog
- `feature-packets/README.md` — packet index and maturity status
- `feature-packets/FEATURE_PACKET_TEMPLATE.md` — required design packet format
- `feature-packets/MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md` — Universal Object Experience design packet
- `feature-packets/MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md` — Permissions and Hidden Information design packet
- `feature-packets/MV-IA-F020_PERMISSION_SURFACE_MATRIX.json` — protected surfaces, classifications, reason codes, and denied cases
- `validate_internal_alpha_design.py` — program and registry validator
- `validate_feature_packets.py` — implementation-ready packet and companion-file validator
- `.github/workflows/internal-alpha-design-validation.yml` — automated validation

## Execution boundary

MV-IA-001 may produce approved design packets while P9-06-008 is paused. Implementation work orders are created only when their service dependencies and repository gates are ready.

No document in this directory authorizes:

- paid service enrollment;
- production credentials;
- production deployment;
- internal-alpha release;
- public release;
- irreversible provider coupling;
- canonical promotion of AI or contributor proposals.

## Current next design action

**IA-D02-003 — Design MV-IA-F003, Identity, Dashboard, and Workspace Selection.**

This packet is next because the object and permission contracts now define what the entry experience must resolve and present: stable subject identity, invitations, Campaign memberships, scoped roles, active Character context, recent work, drafts, approvals, notifications, support states, and only the workspaces and actions the current subject may use.
