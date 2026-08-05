# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.9.0  
**Status:** ACTIVE DESIGN BACKLOG  
**Owner:** John Brandon Turner

## Backlog rule

This backlog governs feature design packets and integration reviews, not application implementation. Completed design work may remain implementation-blocked by unfinished P9-06 dependencies.

Design work maximizes reuse: shared systems and high-fan-out features are specified and integrated before downstream domain features.

## Tranche IA-D01 — Program foundation — COMPLETE

1. IA-D01-001 — Establish program and terminology correction — complete.
2. IA-D01-002 — Define internal-alpha scope — complete.
3. IA-D01-003 — Create feature registry and classifications — complete.
4. IA-D01-004 — Create dependency map — complete.
5. IA-D01-005 — Define core Player and GM user journeys — complete.
6. IA-D01-006 — Inventory shared systems — complete.
7. IA-D01-007 — Define acceptance matrix — complete.
8. IA-D01-008 — Reconcile historically deferred modules — complete.
9. IA-D01-009 — Create standard feature-packet template — complete.
10. IA-D01-010 — Add machine validation and CI — complete.

## Tranche IA-D02 — Shared foundations — COMPLETE

1. **IA-D02-001 — MV-IA-F002 Universal Object Experience — complete**
   - packet: `feature-packets/MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md`
   - status: implementation-ready design; implementation not started and dependency-gated
2. **IA-D02-002 — MV-IA-F020 Permissions and Hidden Information — complete**
   - packet: `feature-packets/MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md`
   - matrix: `feature-packets/MV-IA-F020_PERMISSION_SURFACE_MATRIX.json`
   - validation: twenty acceptance criteria, protected surfaces, visibility classes, and denied cases
3. **IA-D02-003 — MV-IA-F003 Identity, Dashboard, and Workspace Selection — complete**
   - packet: `feature-packets/MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md`
   - matrix: `feature-packets/MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json`
   - validation: twenty acceptance criteria, identity, invitation, role, workspace, discovery, and denied-case contracts
4. **IA-D02-004 — MV-IA-F021 Autosave, Reconnect, Recovery, and Bounded Offline Use — complete**
   - packet: `feature-packets/MV-IA-F021_AUTOSAVE_RECONNECT_RECOVERY_AND_BOUNDED_OFFLINE_USE.md`
   - matrix: `feature-packets/MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json`
   - validation: twenty acceptance criteria, state vocabulary, interruption points, denied cases, and bounded-offline rules
5. **IA-D02-005 — MV-IA-F025 Onboarding, Help, Diagnostics, and Issue Reporting — complete**
   - packet: `feature-packets/MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md`
   - matrix: `feature-packets/MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json`
   - validation: twenty acceptance criteria, role-specific onboarding, exact release identity, diagnostic allowlisting, attachment consent, export-only operation, and zero-service operation
6. **IA-D02-006 — Shared-foundations integration review — complete**
   - review: `feature-packets/IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md`
   - matrix: `feature-packets/IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json`
   - receipt: `feature-packets/IA-D02-006_REVIEW_RECEIPT.md`
   - completion: `feature-packets/IA-D02-006_COMPLETION_RECORD.json`
   - validation: twenty-four shared contracts, five integrated journeys, eight resolved findings, zero blocking findings, and twenty acceptance criteria

Rationale: F002, F020, F003, F021, and F025 establish the object, authority, identity, recovery, onboarding, help, diagnostics, and issue-evidence patterns consumed by later work. IA-D02-006 normalizes their roles, fields, workspace types, authority, persistence, recovery, support, accessibility, provider, and cost boundaries.

## Tranche IA-D03 — Character and Campaign preparation

1. **IA-D03-001 — MV-IA-F004 Character Creation and Advancement packet — complete**
   - packet: `feature-packets/MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md`
   - matrix: `feature-packets/MV-IA-F004_CHARACTER_CREATION_MATRIX.json`
   - traceability: `feature-packets/MV-IA-F004_IMPLEMENTATION_TRACEABILITY.json`
   - completion: `feature-packets/MV-IA-F004_COMPLETION_RECORD.json`
   - status: implementation-ready design; implementation not started and dependency-gated
   - validation: twenty blocking acceptance criteria, twelve lifecycle states, eighteen validation classes, sixteen operation types, twenty-six denied cases, and zero blocking findings
2. **IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet — complete**
   - packet: `feature-packets/MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md`
   - matrix: `feature-packets/MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json`
   - traceability: `feature-packets/MV-IA-F005_IMPLEMENTATION_TRACEABILITY.json`
   - completion: `feature-packets/MV-IA-F005_COMPLETION_RECORD.json`
   - status: implementation-ready design; implementation not started and dependency-gated
   - validation: twenty blocking acceptance criteria, twenty-four shared contracts, at least twenty-four validation classes, thirty-one operation types, thirty-one Event types, forty-two denied cases, and zero blocking findings
3. **IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet — next**
4. IA-D03-004 — alpha content and fixture specification
5. IA-D03-005 — Character/Campaign integration review

## Tranche IA-D04 — First playable loop

1. IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop packet
2. IA-D04-002 — proposal and approval shared-component contract
3. IA-D04-003 — two-device interruption and reconnect scenario matrix
4. IA-D04-004 — authoritative result and history presentation contract
5. IA-D04-005 — first-playable-loop implementation handoff package

## Tranche IA-D05 — Relationship, social, and investigation systems

1. IA-D05-001 — MV-IA-F009 Relationship Tracker packet
2. IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations packet
3. IA-D05-003 — MV-IA-F010 Social Interaction Mode packet
4. IA-D05-004 — MV-IA-F011 Investigation and Clue Board packet
5. IA-D05-005 — graph/list accessibility and visibility contract
6. IA-D05-006 — noncombat integration review

## Tranche IA-D06 — Combat and Assets

1. IA-D06-001 — MV-IA-F007 Full Combat Interface packet
2. IA-D06-002 — MV-IA-F008 Inventory, Ownership, and Shared Assets packet
3. IA-D06-003 — MV-IA-F013 bounded Maps, Zones, and Tactical Positioning packet
4. IA-D06-004 — MV-IA-F014 basic Vehicle alpha-slice packet
5. IA-D06-005 — combat and Asset integrity scenario matrix
6. IA-D06-006 — combat/Asset integration review

## Tranche IA-D07 — World, adventure, and Project depth

1. IA-D07-001 — MV-IA-F015 World and Setting Builder packet
2. IA-D07-002 — MV-IA-F017 Adventure and Story Flow Runtime packet
3. IA-D07-003 — MV-IA-F018 bounded Downtime, Crafting, and Projects packet
4. IA-D07-004 — creator proposal and Campaign-local content contract
5. IA-D07-005 — content-authoring integration review

## Tranche IA-D08 — Optional AI and experimental systems

1. IA-D08-001 — MV-IA-F023 Governed AI Assistance packet
2. IA-D08-002 — AI permission, provenance, cost, and fallback matrix
3. IA-D08-003 — advanced map and vehicle deferral packets
4. IA-D08-004 — broad offline synchronization deferral packet
5. IA-D08-005 — experimental-feature isolation review

## Tranche IA-D09 — Internal-alpha release-design package

1. IA-D09-001 — complete feature-to-journey traceability.
2. IA-D09-002 — complete alpha content and fixture catalog.
3. IA-D09-003 — complete permission and hidden-information matrix.
4. IA-D09-004 — complete accessibility and responsive test matrix.
5. IA-D09-005 — complete recovery and failure-injection matrix.
6. IA-D09-006 — complete performance and cost budgets.
7. IA-D09-007 — complete tester onboarding and issue workflow.
8. IA-D09-008 — compile implementation work-order queue.
9. IA-D09-009 — compile owner decision packet.
10. IA-D09-010 — internal-alpha feature-design completion review.

## Status rules

Each backlog item uses one state:

- not-started;
- in-progress;
- blocked-by-dependency;
- review-required;
- complete;
- deferred;
- superseded.

A design item is complete only when its artifact exists, passes validation, records limitations and authorization boundaries, and identifies the next executable item.

## IA-D02 completion result

Tranche IA-D02 is complete at design level.

The shared-foundation baseline now requires:

- stable provider-neutral subject identity;
- deny-by-default authorization and field-safe projection;
- nonauthoritative selected-context receipts;
- stable-ID object selection with caller validation;
- explicit separation of local draft, submitted operation, accepted Event, and current projection;
- idempotency and status lookup after ambiguous failure;
- revocation-aware cache, subscription, workspace, and issue behavior;
- manifest-bound offline reading and local drafts with no offline authoritative mutation;
- diagnostic exclusion by default, redaction, preview, consent, quarantine, and checksums;
- separate governed support access;
- equivalent desktop, tablet, mobile, keyboard, touch, screen-reader, high-zoom, reduced-motion, and noncolor behavior;
- provider-neutral adapters and a zero-paid-service, zero-AI core path.

All IA-D02 application implementation remains dependency-gated by the active P9-06 sequence.

## IA-D03-001 completion record

MV-IA-F004 now defines:

- Campaign-, rules-profile-, creation-policy-, advancement-policy-, and pack-lock-bound Character drafts;
- stable-ID species, form, origin, attribute, skill, proficiency, Ability, Action, Effect, Condition, Resource, and initial-equipment selections;
- authoritative prerequisite, exclusivity, budget, grant, entitlement, pack, lifecycle, and compatibility validation;
- source-linked deterministic calculation traces;
- explicit Character-control grants separate from identity, membership, role, ownership, and entitlement;
- role-safe Character, history, export, diagnostic, and AI projections;
- local draft, authoritative save, submission, activation, award, advancement, correction, migration, retirement, archival, and recovery states;
- idempotency, expected versions, status lookup, conflict preservation, Event-gap recovery, and no offline authoritative mutation;
- history-preserving advancement, correction, migration, and historical entitlement behavior;
- responsive and accessible creation and advancement flows;
- twenty blocking acceptance criteria and deterministic fixture requirements.

The packet is implementation-ready as a design artifact. Application implementation remains dependency-gated by the active P9-06 sequence and does not authorize paid services, production credentials, real-user data collection, internal-alpha release, production, or public release.

## IA-D03-002 completion record

MV-IA-F005 now defines:

- Campaign identity, rules-profile binding, schema identity, entitlement policy, and immutable pack-lock state;
- invitation, membership, active-role, Character-control, observer, and Assistant-GM delegation boundaries;
- Scene drafts, Campaign-local placements, explicit field visibility, accessible map alternatives, and server-generated Player previews;
- authoritative validation of stable-ID references, permissions, entitlements, dependencies, Character eligibility, and launch readiness;
- immutable launch snapshots that separate mutable preparation from active Session state;
- Session launch, entry, pause, resume, close, Event history, current projection, and reconnect behavior;
- idempotency, expected versions, ambiguous-failure lookup, conflict preservation, revocation, and no offline authoritative mutation;
- realtime as advisory and durable ordered Events plus server projections as authoritative;
- role-safe export, diagnostics, optional AI proposals, accessibility, responsive behavior, and zero-paid-service operation;
- twenty blocking acceptance criteria and deterministic Campaign, Scene, invitation, launch, visibility, and recovery fixtures.

The packet is implementation-ready as a design artifact. Application implementation remains dependency-gated by the active P9-06 sequence and does not authorize paid services, production credentials, real-user data collection, internal-alpha release, production, or public release.

## Current next design item

**IA-D03-003 — Design MV-IA-F012, Encounter Builder and Balance Lab.**

F012 is next because it consumes the completed Campaign, Scene, Session, Character, object, permission, recovery, and pack contracts to define bounded encounter composition, dependency validation, pressure estimates, uncertainty, and source-grounded warnings without guaranteed-balance claims.
