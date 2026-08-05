# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.3.0  
**Status:** ACTIVE DESIGN BACKLOG  
**Owner:** John Brandon Turner

## Backlog rule

This backlog governs feature **design packets**, not application implementation. A completed design packet may remain implementation-blocked by unfinished P9-06 dependencies.

Design work should maximize reuse: shared systems and high-fan-out features are specified before downstream domain features.

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

## Tranche IA-D02 — Shared foundations

1. **IA-D02-001 — MV-IA-F002 Universal Object Experience packet — complete**
   - packet: `feature-packets/MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md`
   - registry status: implementation-ready
   - implementation status: not started; dependency-gated
   - validation: dedicated feature-packet validation added
2. **IA-D02-002 — MV-IA-F020 Permissions and Hidden Information packet — complete**
   - packet: `feature-packets/MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md`
   - matrix: `feature-packets/MV-IA-F020_PERMISSION_SURFACE_MATRIX.json`
   - registry status: implementation-ready
   - implementation status: not started; dependency-gated
   - validation: twenty acceptance criteria, twenty-eight protected surfaces, ten visibility classes, and denied-case validation
3. **IA-D02-003 — MV-IA-F003 Identity, Dashboard, and Workspace Selection packet — next**
4. IA-D02-004 — MV-IA-F021 Autosave, Reconnect, Recovery, and Bounded Offline Use packet
5. IA-D02-005 — MV-IA-F025 Onboarding, Help, Diagnostics, and Issue Reporting packet
6. IA-D02-006 — shared-foundations integration review

Rationale: these features establish the object, authority, recovery, and support patterns consumed by most later work.

## Tranche IA-D03 — Character and Campaign preparation

1. IA-D03-001 — MV-IA-F004 Character Creation and Advancement packet
2. IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet
3. IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet
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

A design item is complete only when its artifact exists, passes validation, records limitations, and identifies the next executable item.

## IA-D02-001 completion record

MV-IA-F002 defines:

- browse, search, filtering, exact stable-ID lookup, inspection, provenance, relationships, comparison, conflicts, and constrained selection;
- Definition, placement, instance, projection, event, index, stable-ID, and source boundaries;
- Player, GM, Owner/Admin, creator, Assistant GM, service, and optional AI permissions;
- entitlement, pack, version, migration, persistence, interruption, reconnect, and recovery behavior;
- desktop, tablet, mobile, keyboard, touch, screen-reader, high-zoom, reduced-motion, and graph-alternative requirements;
- fifteen blocking acceptance criteria;
- deterministic fixtures, denied cases, performance checks, zero-service operation, implementation decomposition, and dependency hold points.

The packet is implementation-ready as a design artifact. It does not authorize application implementation around unfinished P9-06 dependencies.

## IA-D02-002 completion record

MV-IA-F020 defines:

- deny-by-default server authorization for reads, writes, searches, counts, relationships, subscriptions, exports, object storage, diagnostics, and AI retrieval;
- ten semantic visibility classes covering public, Campaign, participant, Character-controller, Player-private, GM-only, creator, operational, security, and secret material;
- stable authorization request, decision, reason-code, projection, delegation, support-access, audit, and permission-snapshot contracts;
- twenty-eight protected product surfaces, including Universal Object results, facets, aliases, exact IDs, source views, relationships, comparison, private notes, GM truth, realtime, notifications, exports, backups, diagnostics, AI, caches, and role mutations;
- explicit boundaries for Players, GMs, Assistant GMs, creators, observers, Owner/Admin, service actors, and AI;
- service/database agreement, pre-pagination filtering, safe counts, field-safe serialization, server-generated Player preview, mutation reauthorization, revocation, and fail-closed behavior;
- twenty blocking acceptance criteria and a deterministic denied-case suite;
- privacy-safe audit, accessible permission and recovery states, zero-AI core policy evaluation, and provider-neutral implementation decomposition.

The packet is implementation-ready as a design artifact. Implementation remains dependency-gated by the active P9-06 sequence and does not authorize production, spending, provider commitment, internal-alpha release, or public release.

## Current next design item

**IA-D02-003 — Design MV-IA-F003, Identity, Dashboard, and Workspace Selection.**

This packet is next because the object and permission contracts now define what the entry experience must resolve and present: stable subject identity, invitations, Campaign memberships, scoped roles, active Character context, recent work, drafts, approvals, notifications, support states, and only the workspaces and actions the current subject may use.
