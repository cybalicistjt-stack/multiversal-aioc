# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.10.0  
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

Complete: scope, registry, dependency map, journeys, shared-system inventory, acceptance matrix, deferred-feature reconciliation, content and fixture baseline, owner-decision register, packet template, ordered backlog, validation, and CI.

### Tranche IA-D02 — Shared foundations

Complete at design level:

- MV-IA-F002 Universal Object Experience;
- MV-IA-F020 Permissions and Hidden Information;
- MV-IA-F003 Identity, Dashboard, and Workspace Selection;
- MV-IA-F021 Autosave, Reconnect, Recovery, and Bounded Offline Use;
- MV-IA-F025 Onboarding, Help, Diagnostics, and Issue Reporting;
- IA-D02-006 Shared-Foundations Integration Review.

The integration review establishes the downstream baseline for canonical roles and workspaces, stable identity, authorization, field-safe projection, object selection, local versus authoritative state, idempotency, Event recovery, revocation, bounded offline use, diagnostics, issue reporting, support access, accessibility, provider-neutral adapters, and zero-service operation.

## IA-D03-001 — Character Creation and Advancement

Complete at design level with governed Character drafts, stable-ID selections, authoritative validation, deterministic calculations, Character control, role-safe projections, lifecycle history, persistence, reconnect, recovery, accessibility, twenty blocking acceptance criteria, and deterministic fixtures.

Application implementation remains dependency-gated.

## IA-D03-002 — Campaign, Scene, and Session Builder

Complete at design level with Campaign policy and pack binding, invitations, membership, roles, Character control, Scene drafts, stable-ID placements, local overrides, notes, accessible maps, safe previews, launch validation, immutable launch snapshots, Session lifecycle, Event recovery, exports, diagnostics, accessibility, twenty blocking criteria, and deterministic fixtures.

Application implementation remains dependency-gated.

## IA-D03-003 — Encounter Builder and Balance Lab

Complete at design level with:

- governed Encounter drafts bound to Campaign, Scene, Character roster, rules, schemas, packs, and analysis policy;
- stable-ID composition and source-versus-placement provenance;
- dependency, scale, compatibility, permission, entitlement, version, and integrity validation;
- twelve transparent pressure dimensions;
- evidence quality, uncertainty classes, omitted-variable disclosure, and sensitivity;
- source-grounded warnings without guaranteed-balance claims;
- deterministic bounded simulation and regression replay;
- scenario comparisons and immutable analysis receipts;
- permission-safe GM, Assistant-GM, Player, observer, export, diagnostic, and optional-AI projections;
- Scene attachment without mutation of launch snapshots or live Sessions;
- persistence, idempotency, concurrency, reconnect, revocation, bounded offline, export, migration, backup, restore, accessibility, and zero-service contracts;
- twenty blocking acceptance criteria, forty-eight denied cases, and ten deterministic fixtures.

Application implementation remains dependency-gated. No balance certification, paid simulation, production credential, real-user data collection, internal-alpha release, production deployment, or public release is authorized.

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
- implementation-ready F002, F020, F003, F021, F025, F004, F005, and F012 packets and companion artifacts
- `feature-packets/IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md`
- `feature-packets/IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json`
- `feature-packets/IA-D02-006_REVIEW_RECEIPT.md`
- `feature-packets/IA-D02-006_COMPLETION_RECORD.json`

Validation:

- `validate_internal_alpha_design.py`
- `validate_feature_packets.py`
- `validate_shared_foundations_integration.py`
- `validate_character_creation_design.py`
- `validate_campaign_scene_session_design.py`
- `validate_encounter_builder_balance_lab_design.py`
- `.github/workflows/internal-alpha-design-validation.yml`
- `.github/workflows/campaign-scene-session-design-validation.yml`
- `.github/workflows/encounter-builder-balance-lab-design-validation.yml`

## Execution boundary

MV-IA-001 may produce approved design packets while implementation dependencies remain incomplete. Implementation work orders are created only when service dependencies and repository gates are ready.

No document in this directory authorizes paid service enrollment, production credentials, production deployment, collection of real tester diagnostics, internal-alpha release, public release, irreversible provider coupling, guaranteed-balance claims, or canonical promotion of AI or contributor proposals.

Silence is not approval.

## Current next design action

**IA-D03-004 — Define the internal-alpha content and deterministic fixture specification.**

This specification must consume the completed Character, Campaign, Scene, Session, Encounter, object, permission, recovery, pack, and accessibility contracts and provide a bounded reproducible corpus for the first playable loop.
