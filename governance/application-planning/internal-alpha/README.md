# MV-IA-001 — Internal Alpha Feature Design Program

**Document ID:** MV-IA-001  
**Version:** 0.15.0  
**Status:** ACTIVE — DESIGN PROGRAM  
**Owner and final authority:** John Brandon Turner

## Purpose

MV-IA-001 converts the approved Project Bible, Stage A program, Phase 9 architecture, and historical feature roadmap into implementation-ready internal-alpha design contracts. It does not bypass P9-06 or authorize release.

## Completed foundations

IA-D01 and IA-D02 are complete. Shared contracts cover governed objects, identity, authority, projections, persistence, recovery, diagnostics, accessibility, provider neutrality, and zero-service operation.

## Completed Character and Campaign preparation

IA-D03-001 through IA-D03-005 are complete, including Character, Campaign/Scene/Session, Encounter preparation, bounded deterministic fixtures, and the Character/Campaign integration review.

## IA-D04-001 — First Playable Action and GM Approval Loop

Complete at design level with Player proposal, GM approve/deny/modify, NPC/enemy parity, atomic durable result, role-safe projections, recovery, fourteen fixtures, twenty blocking criteria, and zero blocking findings.

## IA-D04-002 — Proposal and Approval Shared-Component Contract

Complete at design level with seven consumer profiles, twelve surfaces, immutable proposals, advisory review claims, attributable decisions, atomic adapters, role-safe projections, sixteen fixtures, twenty blocking criteria, and zero blocking findings.

## IA-D04-003 — Two-Device Interruption and Reconnect Matrix

Completed at design level with:

- six device-role projections;
- fifteen interruption boundaries;
- twenty recovery states and twenty state-vector fields;
- twelve recovery actions and twenty-four denied cases;
- stable status lookup before retry;
- advisory review-claim expiry and revocation;
- exactly one final decision and at most one consumer commit;
- ordered durable Event-gap recovery;
- current role-safe projection convergence;
- explicit stale-version and offline-draft conflicts;
- protected-cache invalidation across devices;
- twenty-four deterministic fixtures, eight implementation slices, twenty blocking criteria, and zero blocking findings.

Primary artifacts:

- `feature-packets/IA-D04-003_TWO_DEVICE_INTERRUPTION_AND_RECONNECT_MATRIX.md`
- `feature-packets/IA-D04-003_TWO_DEVICE_RECONNECT_MATRIX.json`
- `feature-packets/IA-D04-003_IMPLEMENTATION_TRACEABILITY.json`
- `feature-packets/IA-D04-003_REVIEW_RECEIPT.md`
- `feature-packets/IA-D04-003_READINESS_RECORD.md`
- `feature-packets/IA-D04-003_COMPLETION_RECORD.json`
- `validate_two_device_interruption_reconnect.py`

## Governing decisions

Silence is not approval. Review claims, local drafts, caches, notifications, and realtime messages are advisory. Stable operation identities and status lookup control retries. Silent last-write-wins is prohibited. AI has no decision or commit authority.

## Preparation boundary

The fixture corpus is bounded test data, not the complete game and not a canonical content release. Synthetic fixtures remain noncanonical. Encounter analysis remains advisory and cannot guarantee balance, fairness, safety, victory, survival, or optimality.

## Execution boundary

Design work may proceed while implementation dependencies remain incomplete. No document here authorizes canonical promotion, paid services, production credentials, real-user data, internal-alpha release, production deployment, or public release.

## Current next design action

**IA-D04-004 — Authoritative Result and History Presentation.**

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

Historical IA-D04-002 route: **IA-D04-003 — Two-Device Interruption and Reconnect Matrix**.
