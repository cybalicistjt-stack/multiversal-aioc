# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.14.0  
**Status:** ACTIVE — DESIGN PROGRAM  
**Owner and final authority:** John Brandon Turner

## Purpose

MV-IA-001 converts the approved Project Bible, Stage A program, Phase 9 architecture, and historical feature roadmap into implementation-ready internal-alpha design contracts. It does not bypass P9-06 or authorize release.

## Completed foundations

IA-D01 and IA-D02 are complete. Shared contracts cover governed objects, identity, authority, projections, persistence, recovery, diagnostics, accessibility, provider neutrality, and zero-service operation.

## Completed Character and Campaign preparation

- IA-D03-001 — Character Creation and Advancement.
- IA-D03-002 — Campaign, Scene, and Session Builder.
- IA-D03-003 — Encounter Builder and Balance Lab.
- IA-D03-004 — Internal Alpha Content and Deterministic Fixtures.
- IA-D03-005 — Character/Campaign Integration Review.

## IA-D03-002 — Campaign, Scene, and Session Builder

Completed at design level with Campaign rules and packs, invitation and membership lifecycles, role, delegation, observer and Character-control separation, Scene drafts and stable-ID placements, safe previews, validation, immutable launch snapshots, exactly-once Session launch, Event recovery, exports, accessibility, and twenty blocking acceptance criteria.

## IA-D03-003 — Encounter Builder and Balance Lab

Completed at design level with governed Encounter composition, stable-ID provenance, dependency and compatibility validation, twelve independent pressure dimensions, explicit uncertainty and omitted-variable tracking, source-grounded warnings, deterministic bounded simulation, scenario comparison, permission-safe projections, Scene attachment, recovery, accessibility, and twenty blocking acceptance criteria. The design prohibits guaranteed-balance, fairness, safety, victory, survival, optimality, and actual-play prediction claims.

## IA-D03-004 — Internal Alpha Content and Deterministic Fixtures

Completed at design level with 36 exact inherited source-backed fixtures, 119 explicitly synthetic noncanonical fixtures, five exact-version fixture packs, fifteen coverage families, migration and cleanup rules, deterministic checksum derivation, twenty blocking acceptance criteria, and zero blocking findings. The corpus is bounded test data, not the complete game and not a canonical release.

## IA-D03-005 — Character/Campaign Integration Review

Complete at design level with 28 normalized integration contracts, eight end-to-end preparation journeys, twelve resolved findings, ten dependency-ordered implementation slices, twenty-four blocking acceptance criteria, zero blocking findings, Campaign-scoped Character control, advisory Encounter analysis, immutable launch snapshots, conflict-safe recovery, and 155 provenance-labeled deterministic fixture identities.

## IA-D04-001 — First Playable Action and GM Approval Loop

Completed at design level with a 24-section packet, twenty blocking acceptance criteria, explicit Player proposal and GM approve/deny/modify contracts, GM-controlled NPC and enemy Action parity, 18 states, 28 proposal fields, 20 decision-receipt fields, 28 validation classes, 28 operations, 28 Events, 40 denied cases, fourteen deterministic fixtures, ten implementation slices, zero blocking findings, bounded offline drafts, accessible responsive parity, privacy-safe diagnostics, and zero-AI/zero-service core operation.

Primary artifacts:

- `feature-packets/MV-IA-F006_FIRST_PLAYABLE_ACTION_AND_GM_APPROVAL_LOOP.md`
- `feature-packets/MV-IA-F006_ACTION_APPROVAL_MATRIX.json`
- `feature-packets/MV-IA-F006_IMPLEMENTATION_TRACEABILITY.json`
- `feature-packets/MV-IA-F006_REVIEW_RECEIPT.md`
- `feature-packets/MV-IA-F006_READINESS_RECORD.md`
- `feature-packets/MV-IA-F006_COMPLETION_RECORD.json`
- `validate_first_playable_action_approval_loop.py`

## IA-D04-002 — Proposal and Approval Shared-Component Contract

Completed at design level with:

- SS-06 normalized as a reusable orchestration contract rather than a new domain authority;
- a versioned consumer-adapter boundary;
- eight mapped consumer types;
- twenty lifecycle states;
- thirty proposal fields and twenty-four decision-receipt fields;
- four explicit approval policies;
- twenty-four validation classes, twenty-four operations, twenty-four orchestration Events, and thirty-six denied cases;
- approve, deny, modify-and-approve, and bounded request-changes behavior;
- field-addressed allowlisted patches, revalidation, recalculation where required, and final confirmation;
- exactly-once domain commit-adapter invocation with proposal/domain Event separation;
- permission-safe queues, notifications, inspection, history, exports, diagnostics, support, and optional-AI projections;
- idempotency, conflict preservation, status lookup, reconnect, revocation, offline boundaries, expiry, withdrawal, and supersession;
- sixteen deterministic fixtures, ten implementation slices, twenty blocking acceptance criteria, and zero blocking findings;
- zero-AI and zero-paid-service core operation.

Primary artifacts:

- `feature-packets/IA-D04-002_PROPOSAL_APPROVAL_SHARED_COMPONENT_CONTRACT.md`
- `feature-packets/IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json`
- `feature-packets/IA-D04-002_CONSUMER_MAPPING.json`
- `feature-packets/IA-D04-002_IMPLEMENTATION_TRACEABILITY.json`
- `feature-packets/IA-D04-002_REVIEW_RECEIPT.md`
- `feature-packets/IA-D04-002_READINESS_RECORD.md`
- `feature-packets/IA-D04-002_COMPLETION_RECORD.json`
- `validate_proposal_approval_shared_component.py`

## Preparation boundary

The fixture corpus is bounded test data, not the complete game and not a canonical content release. Synthetic fixtures remain noncanonical. Encounter analysis remains advisory and cannot guarantee balance, fairness, safety, victory, survival, or optimality.

The proposal-and-approval shared component does not grant domain authority, reviewer authority, owner approval, or commit validity merely because a generic proposal is marked approved.

## Execution boundary

Design work may proceed while implementation dependencies remain incomplete. No document here authorizes canonical promotion, paid services, production credentials, real-user data, internal-alpha release, production deployment, or public release.

## Current next design action

**IA-D04-003 — Two-Device Interruption and Reconnect Matrix.**

## Historical IA-D03-004 handoff anchor

This archival block preserves the exact program wording validated when IA-D03-004 completed. It is historical evidence, not the current route or document version.

**Version:** 0.11.0

## IA-D03-004 — Internal Alpha Content and Deterministic Fixtures

**IA-D03-005 — Character/Campaign integration review.**

Historical IA-D03-005 route: **IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop**.

Historical IA-D04-001 route: **IA-D04-002 — Proposal and Approval Shared-Component Contract**.
