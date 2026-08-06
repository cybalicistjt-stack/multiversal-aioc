# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.24.0  
**Status:** ACTIVE DESIGN BACKLOG  
**Owner:** John Brandon Turner

## Backlog rule

This backlog governs design packets, fixture specifications, and integration reviews. Implementation remains dependency-gated by P9-06. A design item is complete only when artifacts exist, limitations and boundaries are explicit, deterministic validation passes, and repository merge evidence is recorded.

## IA-D01 — Program foundation — COMPLETE

Scope, registry, dependency map, journeys, shared systems, acceptance matrix, deferred-feature reconciliation, initial fixture baseline, decisions, packet template, backlog, validation, and CI are complete.

## IA-D02 — Shared foundations — COMPLETE

- IA-D02-001 — MV-IA-F002 Universal Object Experience — complete.
- IA-D02-002 — MV-IA-F020 Permissions and Hidden Information — complete.
- IA-D02-003 — MV-IA-F003 Identity, Dashboard, and Workspace Selection — complete.
- IA-D02-004 — MV-IA-F021 Autosave, Reconnect, Recovery, and Bounded Offline Use — complete.
- IA-D02-005 — MV-IA-F025 Onboarding, Help, Diagnostics, and Issue Reporting — complete.
- IA-D02-006 — Shared-foundations integration review — complete.

## IA-D03 — Character and Campaign preparation — COMPLETE

1. **IA-D03-001 — MV-IA-F004 Character Creation and Advancement packet — complete.**
2. **IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder packet — complete.**
3. **IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab packet — complete.**
4. **IA-D03-004 — alpha content and fixture specification — complete.**
5. **IA-D03-005 — Character/Campaign integration review — complete.**

## IA-D04 — First playable loop — COMPLETE

1. **IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — complete.**
2. **IA-D04-002 — proposal and approval shared-component contract — complete.**
3. **IA-D04-003 — two-device interruption and reconnect matrix — complete.**
4. **IA-D04-004 — authoritative result and history presentation — complete.**
5. **IA-D04-005 — first-playable-loop implementation handoff — complete.**

## IA-D05 — Relationship, social, and investigation systems — COMPLETE

1. **IA-D05-001 — MV-IA-F009 Relationship Tracker — complete.**
2. **IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations — complete.**
3. **IA-D05-003 — MV-IA-F010 Social Interaction Mode — complete.**
4. **IA-D05-004 — MV-IA-F011 Investigation and Clue Board — complete.**
5. **IA-D05-005 — graph/list accessibility matrix — complete.**
6. **IA-D05-006 — noncombat integration review — complete.**

## IA-D06 — Combat and Assets

1. **IA-D06-001 — MV-IA-F007 Full Combat Interface — complete.**
2. **IA-D06-002 — MV-IA-F008 Inventory, Ownership, and Shared Assets — complete.**
3. **IA-D06-003 — bounded MV-IA-F013 Maps, Zones, and Tactical Positioning — complete.**
4. **IA-D06-004 — basic MV-IA-F014 Vehicle, Mecha, and Starship Operations — complete.**
5. **IA-D06-005 — combat/Asset integrity matrix — complete.**
6. **IA-D06-006 — combat and Assets integration review — next.**

## IA-D07 — World, adventure, and Project depth

F015, F017, bounded F018, creator proposal/Campaign-local content, and authoring integration review.

## IA-D08 — Optional AI and experimental systems

F023, AI permission/provenance/cost/fallback, advanced map and vehicle deferrals, broad offline deferral, and isolation review.

## IA-D09 — Internal-alpha release-design package

Traceability, fixture catalog, permission matrix, accessibility matrix, recovery matrix, budgets, onboarding, implementation queue, owner decisions, and completion review.

## Completion records

### IA-D03-005

The completed Character/Campaign preparation integration defines one coherent permission-safe, versioned, recoverable preparation path, preserves 155 provenance-labeled fixture identities, and advances to the first playable loop with zero blocking findings.

### IA-D04

The first playable loop defines Player and GM Action proposals, approve/deny/modify decisions, NPC/enemy parity, atomic authoritative results, role-filtered projections, reconnect recovery, reusable proposal/approval, two-device interruption handling, authoritative history presentation, and a twelve-package implementation handoff. `P9-06-008-attempt-002` remains unfinished parallel work.

### IA-D05

The Relationship Tracker, Factions/Reputation/Organizations, Social Interaction Mode, Investigation and Clue Board, Graph/List Accessibility Matrix, and Noncombat Integration Review establish one permission-safe noncombat runtime with distinct authority, hidden-information protection, atomic cross-domain outcomes, recovery, provenance, and accessible semantic parity.

### IA-D06-001

The Full Combat Interface defines authoritative encounter lifecycle, participants, timing, Actions, targets, semantic movement, Resources, Conditions, reactions, hazards, defeat/withdrawal, completion, accessibility, and recovery.

### IA-D06-002

Inventory, Ownership, and Shared Assets defines stable Asset identity and lineage; distinct ownership, custody, possession, control, access, usage, equipment, and location; containers, stacks, transfers, reservations, combat usage, repair, crafting/salvage boundaries, hidden-Asset protection, accessible parity, and recovery.

### IA-D06-003

Bounded Maps, Zones, and Tactical Positioning defines four map modes, semantic zones/anchors, typed adjacency, distance, elevation, cover, movement, range, visibility, deterministic area snapshots, hazards, annotations, Asset/vehicle adapters, accessible nonvisual parity, bounded large-map behavior, recovery, and explicit advanced-map deferrals.

### IA-D06-004

Vehicle, Mecha, and Starship Operations defines ten operational classes, twelve stations, thirteen operational states, explicit command authority, semantic movement, systems and Resource models, atomic combat outcomes, damage/failure, boarding/docking, hidden-information protection, recovery, pack lifecycle, provenance, and accessible nonvisual operation.

### IA-D06-005

The Combat/Asset Integrity Matrix proves atomic integration across combat, Assets, tactical positioning, and Vehicle operations. It defines reservation and contention behavior, proposal-versus-commit cost timing, exact quantity and lineage handling, authority separation, hidden-information filtering, nested-Asset semantics, idempotency, version conflicts, status lookup, Event-gap recovery, compensating undo, pack lifecycle, provenance, and accessible parity. It includes twenty-four deterministic fixtures, eight implementation slices, twenty-eight blocking acceptance criteria, seven resolved findings, and zero blocking findings. `P9-06-008-attempt-002` remains unfinished and unmodified.

## Current next design item

**IA-D06-006 — combat and Assets integration review — next.**

## Historical validation anchors

These archival statements preserve earlier validated routes and are not the current next item.

**Version:** 0.11.0

- IA-D03-004 — alpha content and fixture specification — complete.
- IA-D03-005 — Character/Campaign integration review — next.

**IA-D03-005 — Character/Campaign integration review.**

**IA-D03-005 — Character/Campaign integration review — next.**

**IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next.**

**IA-D04-002 — proposal and approval shared-component contract — next.**

**IA-D04-003 — two-device interruption and reconnect matrix — next.**

**IA-D04-004 — authoritative result and history presentation — next.**

**IA-D04-005 — first-playable-loop implementation handoff — next.**

**IA-D05-005 — graph/list accessibility matrix — next.**

**IA-D05-006 — noncombat integration review — next.**

**IA-D06-001 — MV-IA-F007 Full Combat Interface — next.**

**IA-D06-002 — MV-IA-F008 Inventory, Ownership, and Shared Assets — next.**

**IA-D06-003 — bounded MV-IA-F013 Maps, Zones, and Tactical Positioning — next.**

**IA-D06-004 — basic MV-IA-F014 Vehicle, Mecha, and Starship Operations — next.**

**IA-D06-005 — combat/Asset integrity matrix — next.**
