# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.7.0  
**Status:** ACTIVE — DESIGN PROGRAM  
**Owner and final authority:** John Brandon Turner  
**Established:** 2026-08-05

## Purpose

MV-IA-001 converts the approved Multiversal Project Bible, Stage A UI Implementation Program, Phase 9 architecture, and earlier Feature Module Roadmap into implementation-ready internal-alpha feature packets and integration reviews.

This is a design and governance program. It does not bypass the active P9-06 implementation sequence, authorize production, or place unapproved code into `Multiversal-app`.

## Terminology correction

There is no prophecy content or prophecy feature domain in this program. A prior reference to that term was an autocorrect mistake for **project**. The mistaken term must not be promoted into requirements, content architecture, taxonomy, roadmap, or feature design.

## Mission

Define exactly what internal alpha contains, why each feature is present, how features consume shared systems, how Player and GM journeys connect, and what evidence makes each feature implementation-ready and later alpha-ready.

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
- feature registry and classification;
- dependency map;
- Player and GM user journeys;
- shared-system inventory;
- acceptance matrix;
- deferred-feature reconciliation;
- bounded content and fixture baseline;
- owner-decision register;
- standard packet template;
- ordered backlog;
- machine validation and CI.

### Tranche IA-D02 — Shared foundations

Complete at design level:

- **MV-IA-F002 — Universal Object Experience:** permission-safe browse, search, exact stable-ID lookup, inspection, provenance, relationships, comparison, and constrained selection;
- **MV-IA-F020 — Permissions and Hidden Information:** deny-by-default authorization, field-safe projection, inference safety, revocation, exports, AI limits, diagnostics, and support-access boundaries;
- **MV-IA-F003 — Identity, Dashboard, and Workspace Selection:** stable provider-neutral subjects, invitations, role-aware dashboards, safe workspace discovery, selected-context receipts, switching, revocation, and recovery;
- **MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use:** local versus authoritative state, idempotency, status lookup, Event-gap recovery, conflicts, checkpoints, offline manifests, and restore boundaries;
- **MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting:** role-specific onboarding, exact release identity, contextual help, known limitations, structured issues, diagnostic allowlisting, consent, attachments, receipts, follow-up, and export-only operation;
- **IA-D02-006 — Shared-Foundations Integration Review:** twenty-four controlling contracts, five integrated journeys, eight resolved compatibility or safety findings, zero blocking findings, and twenty integrated acceptance criteria.

The integration review establishes one downstream baseline for:

- canonical role IDs and workspace types;
- stable identity and selected context;
- authorization and projection precedence;
- object selection and caller validation;
- local drafts, authoritative saves, commands, Events, and projections;
- idempotency and ambiguous-failure lookup;
- reconnect, revocation, conflict, and bounded offline behavior;
- release identity, diagnostics, issues, attachments, and separate support access;
- responsive and accessible state equivalence;
- provider-neutral adapters and zero-paid-service, zero-AI core operation.

## File map

Program baselines:

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

Packet and integration artifacts:

- `feature-packets/README.md`
- `feature-packets/FEATURE_PACKET_TEMPLATE.md`
- implementation-ready F002, F020, F003, F021, and F025 packets and companion artifacts
- `feature-packets/IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md`
- `feature-packets/IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json`
- `feature-packets/IA-D02-006_REVIEW_RECEIPT.md`
- `feature-packets/IA-D02-006_COMPLETION_RECORD.json`

Validation:

- `validate_internal_alpha_design.py`
- `validate_feature_packets.py`
- `validate_shared_foundations_integration.py`
- `.github/workflows/internal-alpha-design-validation.yml`

## Execution boundary

MV-IA-001 may produce approved design packets while implementation dependencies remain incomplete. Implementation work orders are created only when service dependencies and repository gates are ready.

No document in this directory authorizes paid service enrollment, production credentials, production deployment, collection of real tester diagnostics, internal-alpha release, public release, irreversible provider coupling, or canonical promotion of AI or contributor proposals.

Silence is not approval.

## Current next design action

**IA-D03-001 — Design MV-IA-F004, Character Creation and Advancement.**

The Character packet must consume the IA-D02-006 shared-foundation contract matrix rather than creating private identity, permission, picker, save, recovery, diagnostic, or support behavior.
