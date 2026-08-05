# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.6.0  
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

## Feature classes

- **entry-critical** — required before internal alpha may begin;
- **alpha-required** — must be completed and tested during internal alpha before it may close;
- **experimental** — may be enabled for selected tests but cannot block the entire alpha unless promoted;
- **deferred** — deliberately excluded from the current internal-alpha scope.

A feature may contain a narrow alpha slice while its full long-term form remains deferred.

## Design method

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

Complete at design level with object browse, search, exact stable-ID lookup, inspection, source and provenance, relationships, comparison, constrained picker, role safety, recovery, accessibility, fixtures, implementation handoff, and fifteen blocking acceptance criteria.

### IA-D02-002 — Permissions and Hidden Information

Complete at design level with deny-by-default authorization, field-safe projections, ten visibility classes, protected product surfaces, denied cases, support-access boundaries, revocation, zero-AI authorization, provider-neutral decomposition, and twenty blocking acceptance criteria.

### IA-D02-003 — Identity, Dashboard, and Workspace Selection

Complete at design level with provider-neutral identity, invitation lifecycle, role-aware dashboards, safe workspace discovery, selected-context receipts, switching, revocation, recovery, accessibility, and twenty blocking acceptance criteria.

### IA-D02-004 — Autosave, Reconnect, Recovery, and Bounded Offline Use

Complete at design level with local versus authoritative state, idempotency, command-status lookup, Event-gap recovery, pending-GM continuity, conflict preservation, checkpoints, history-preserving restore, bounded offline reading and drafts, accessibility, and twenty blocking acceptance criteria.

### IA-D02-005 — Onboarding, Help, Diagnostics, and Issue Reporting

Complete at design level with:

- role-specific tester onboarding;
- exact release, build, environment, schema, and pack-set identity;
- supported-journey checklists;
- contextual help and glossary;
- known limitations and experimental labels;
- structured issue drafts and reports;
- permission-safe diagnostic manifests;
- explicit attachment selection, preview, removal, quarantine, consent, and checksums;
- idempotent submission and ambiguous-failure lookup;
- export-only operation with zero paid services;
- receipts, status, follow-up, revocation, and provider-exit behavior;
- keyboard, touch, screen-reader, responsive, offline-draft, reconnect, and recovery requirements;
- twenty blocking acceptance criteria and a machine-readable support matrix.

The packet does not grant support access to underlying Campaign content.

## File map

- `INTERNAL_ALPHA_SCOPE.md`
- `INTERNAL_ALPHA_FEATURE_REGISTRY.json`
- `INTERNAL_ALPHA_DEPENDENCY_MAP.md`
- `INTERNAL_ALPHA_USER_JOURNEYS.md`
- `INTERNAL_ALPHA_SHARED_SYSTEMS.md`
- `INTERNAL_ALPHA_ACCEPTANCE_MATRIX.md`
- `INTERNAL_ALPHA_DEFERRED_FEATURES.md`
- `INTERNAL_ALPHA_CONTENT_AND_FIXTURES.md`
- `INTERNAL_ALPHA_OWNER_DECISIONS.md`
- `INTERNAL_ALPHA_DESIGN_BACKLOG.md`
- `feature-packets/README.md`
- `feature-packets/FEATURE_PACKET_TEMPLATE.md`
- implementation-ready F002, F020, F003, F021, and F025 packets and companion artifacts
- `validate_internal_alpha_design.py`
- `validate_feature_packets.py`
- `.github/workflows/internal-alpha-design-validation.yml`

## Execution boundary

MV-IA-001 may produce approved design packets while P9-06-008 is paused. Implementation work orders are created only when service dependencies and repository gates are ready.

No document in this directory authorizes paid service enrollment, production credentials, production deployment, collection of real tester diagnostics, internal-alpha release, public release, irreversible provider coupling, or canonical promotion of AI or contributor proposals.

## Current next design action

**IA-D02-006 — Complete the shared-foundations integration review.**

The review must prove that the object, permission, identity, selected-context, recovery, onboarding, help, diagnostics, and issue-reporting contracts agree and can be consumed without contradictory authority, persistence, visibility, accessibility, or evidence behavior.
