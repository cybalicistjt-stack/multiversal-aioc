# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.14.0  
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
   - result: 36 source-backed fixtures, 119 synthetic fixtures, 155 total identities, five packs, fifteen coverage families, twenty blocking criteria, zero blocking findings
   - boundary: bounded test corpus, not complete game, not canonical release
5. **IA-D03-005 — Character/Campaign integration review — complete.**
   - result: 28 normalized contracts, eight journeys, twelve resolved findings, ten implementation slices, twenty-four blocking criteria, zero blocking findings

## IA-D04 — First playable loop

1. **IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — complete.**
2. **IA-D04-002 — proposal and approval shared-component contract — complete.**
   - result: seven consumer profiles, twelve component surfaces, fifteen states, sixteen deterministic fixtures, eight implementation slices, twenty blocking criteria, zero blocking findings
   - boundary: the component coordinates evidence and decisions but does not replace consumer-specific authority, validation, or atomic commit rules
3. **IA-D04-003 — two-device interruption and reconnect matrix — next.**
4. IA-D04-004 — authoritative result and history presentation.
5. IA-D04-005 — first-playable-loop implementation handoff.

## IA-D05 — Relationship, social, and investigation systems

F009, F016, F010, F011, graph/list accessibility, and noncombat integration review.

## IA-D06 — Combat and Assets

F007, F008, bounded F013, basic F014, combat/Asset integrity matrix, and integration review.

## IA-D07 — World, adventure, and Project depth

F015, F017, bounded F018, creator proposal/Campaign-local content, and authoring integration review.

## IA-D08 — Optional AI and experimental systems

F023, AI permission/provenance/cost/fallback, advanced map and vehicle deferrals, broad offline deferral, and isolation review.

## IA-D09 — Internal-alpha release-design package

Traceability, fixture catalog, permission matrix, accessibility matrix, recovery matrix, budgets, onboarding, implementation queue, owner decisions, and completion review.

## IA-D03-005 completion record

The completed Character/Campaign preparation integration defines one coherent permission-safe, versioned, recoverable preparation path, preserves 155 provenance-labeled fixture identities, and advances to the first playable loop with zero blocking findings.

## IA-D04-001 completion record

The implementation-ready First Playable Action and GM Approval Loop defines Player and GM Action proposals, approve/deny/modify decisions, NPC/enemy parity, atomic `ActionResultCommitted` authority, role-filtered projections, idempotency, reconnect recovery, fourteen fixtures, ten slices, twenty blocking criteria, and zero blocking findings.

## IA-D04-002 completion record

The reusable Proposal and Approval Shared-Component Contract provides:

- versioned consumer profiles for live Actions, GM NPC/enemy Actions, social outcomes, content submissions, optional AI suggestions, destructive changes, and canonical-promotion requests;
- immutable original proposals and standard evidence slots;
- permission-safe queues, notifications, and advisory review claims;
- approve, deny, and field-addressed modify-and-approve decisions;
- semantic modification diffs, final confirmation, and attributable durable receipts;
- consumer-specific validators and atomic Event-backed commit adapters;
- server-side proposer, decision-maker, observer, history, export, diagnostic, and AI projections;
- idempotency, status lookup, reconnect, Event-gap recovery, and revocation;
- responsive accessible parity, sixteen deterministic fixtures, eight implementation slices, twenty blocking acceptance criteria, and zero blocking findings;
- zero paid-service and zero-AI core operation.

Implementation remains dependency-gated by P9-06. Silence is not approval. Canonical promotion remains owner-gated.

## Current next design item

**IA-D04-003 — Two-Device Interruption and Reconnect Matrix — next.**

## Historical validation anchors

These archival lines preserve prior validated routes and are not the current next item:

**Version:** 0.11.0

- IA-D03-004 — alpha content and fixture specification — complete.
- IA-D03-005 — Character/Campaign integration review — next.

**IA-D03-005 — Character/Campaign integration review.**

**IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next.**

**IA-D04-002 — proposal and approval shared-component contract — next.**
