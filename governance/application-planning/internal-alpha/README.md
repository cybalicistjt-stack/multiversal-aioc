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

IA-D03-001 through IA-D03-005 are complete, including Character, Campaign/Scene/Session, Encounter preparation, bounded deterministic fixtures, and the Character/Campaign integration review.

## IA-D04-001 — First Playable Action and GM Approval Loop

Completed at design level with:

- 24 numbered sections and twenty blocking acceptance criteria;
- explicit Player proposal, GM review, approve/deny/modify, atomic result, projection, history, and recovery contracts;
- GM-controlled NPC and enemy Action parity;
- 18 states, 28 proposal fields, 20 decision-receipt fields, 28 validation classes, 28 operations, 28 Events, and 40 denied cases;
- fourteen deterministic fixtures, ten dependency-ordered implementation slices, and zero blocking findings;
- secondary Player logs and proposals;
- bounded offline drafts, accessible responsive parity, privacy-safe diagnostics, and zero-AI/zero-service core operation.

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

- seven versioned consumer profiles;
- twelve reusable component surfaces;
- fifteen canonical states;
- twenty-four proposal fields and twenty decision-receipt fields;
- twenty-four validation classes, twenty-two operations, twenty-two Events, and thirty-two denied cases;
- immutable original proposals and standard evidence slots;
- permission-safe queues, notifications, and advisory review claims;
- approve, deny, and field-addressed modify-and-approve controls;
- semantic modification diffs, final confirmation, and attributable durable receipts;
- consumer-specific validation and atomic Event-backed commit adapters;
- server-side projections, history, exports, diagnostics, optional-AI boundaries, idempotency, reconnect, recovery, and revocation;
- sixteen deterministic fixtures, eight implementation slices, twenty blocking acceptance criteria, and zero blocking findings.

Primary artifacts:

- `feature-packets/IA-D04-002_PROPOSAL_APPROVAL_SHARED_COMPONENT_CONTRACT.md`
- `feature-packets/IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json`
- `feature-packets/IA-D04-002_IMPLEMENTATION_TRACEABILITY.json`
- `feature-packets/IA-D04-002_REVIEW_RECEIPT.md`
- `feature-packets/IA-D04-002_READINESS_RECORD.md`
- `feature-packets/IA-D04-002_COMPLETION_RECORD.json`
- `validate_proposal_approval_shared_component.py`

## Governing decisions

Silence is not approval. Review claims are advisory. Original proposals remain immutable. Modifications are explicit and attributable. Consumer profiles may narrow but cannot widen authority. AI has no decision, commit, or canonical-promotion authority.

## Preparation boundary

The fixture corpus is bounded test data, not the complete game and not a canonical content release. Synthetic fixtures remain noncanonical. Encounter analysis remains advisory and cannot guarantee balance, fairness, safety, victory, survival, or optimality.

## Execution boundary

Design work may proceed while implementation dependencies remain incomplete. No document here authorizes canonical promotion, paid services, production credentials, real-user data, internal-alpha release, production deployment, or public release.

## Current next design action

**IA-D04-003 — Two-Device Interruption and Reconnect Matrix.**

## Historical validation anchors

The following sections preserve exact prior result and handoff labels. They are historical evidence, not the current route.

**Version:** 0.11.0

## IA-D03-002 — Campaign, Scene, and Session Builder

Completed at design level; original handoff preserved to IA-D03-003 Encounter Builder and Balance Lab.

## IA-D03-003 — Encounter Builder and Balance Lab

Completed at design level; original handoff preserved to IA-D03-004 internal-alpha content and fixtures.

## IA-D03-004 — Internal Alpha Content and Deterministic Fixtures

Completed at design level; original handoff preserved to IA-D03-005 Character/Campaign integration review.

## IA-D03-005 — Character/Campaign Integration Review

Completed at design level; original handoff preserved to IA-D04-001 First Playable Action and GM Approval Loop.

**IA-D03-005 — Character/Campaign integration review.**

Historical IA-D03-005 route: **IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop**.

Historical IA-D04-001 route: **IA-D04-002 — Proposal and Approval Shared-Component Contract**.
