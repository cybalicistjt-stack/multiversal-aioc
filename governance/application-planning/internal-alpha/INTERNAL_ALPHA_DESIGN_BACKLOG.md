# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.18.0  
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
   - result: six device roles, fifteen interruption boundaries, twenty recovery states, twenty-four deterministic fixtures, eight implementation slices, twenty blocking criteria, zero blocking findings
   - boundary: device-local state, review claims, notifications, caches, and realtime delivery remain advisory; durable Events and current server projections control
4. **IA-D04-004 — authoritative result and history presentation — complete.**
   - result: eight presentation surfaces, eighteen result states, twenty-eight history fields, twenty deterministic fixtures, eight implementation slices, twenty blocking criteria, zero blocking findings
   - boundary: only durable decisions, consumer commits, ordered Events, and current server projections may be presented as authoritative
5. **IA-D04-005 — first-playable-loop implementation handoff — complete.**

## IA-D05 — Relationship, social, and investigation systems

1. **IA-D05-001 — MV-IA-F009 Relationship Tracker — complete.**
2. **IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations — complete.**
3. **IA-D05-003 — MV-IA-F010 Social Interaction Mode — complete.**
4. **IA-D05-004 — MV-IA-F011 Investigation and Clue Board — complete.**
5. **IA-D05-005 — graph/list accessibility matrix — complete.**
6. **IA-D05-006 — noncombat integration review — next.**

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

The reusable Proposal and Approval Shared-Component Contract defines versioned consumer profiles, immutable original proposals, permission-safe queues, advisory review claims, attributable approve/deny/modify decisions, atomic consumer adapters, role-safe projections, sixteen deterministic fixtures, eight slices, twenty blocking criteria, and zero blocking findings.

## IA-D04-003 completion record

The Two-Device Interruption and Reconnect Matrix provides:

- deterministic Player, GM, Assistant-GM, and observer device behavior;
- status lookup before retry for ambiguous submit, decision, and consumer-commit outcomes;
- advisory review claims with safe expiry and revocation;
- exactly one final decision and at most one consumer commit;
- ordered Event-gap recovery and current role-safe projection convergence;
- explicit stale-version, permission, entitlement, and offline-draft conflicts;
- cross-device protected-cache invalidation after revocation;
- responsive and assistive recovery parity;
- twenty-four deterministic fixtures, eight implementation slices, twenty blocking acceptance criteria, and zero blocking findings.

Implementation remains dependency-gated by P9-06. Silent last-write-wins is prohibited.

## IA-D04-004 completion record

The Authoritative Result and History Presentation provides role-safe Player, GM, Assistant-GM, and observer outcomes; immutable original and final modification evidence; denial without accepted effects; committed cost, Effect, Condition, Resource, and target summaries; exact source versions; ordered duplicate-safe history; Event-gap recovery; revocation; exports; accessibility; twenty deterministic fixtures; twenty blocking criteria; and zero blocking findings.

## IA-D04-005 completion record

The First-Playable-Loop Implementation Handoff consolidates IA-D04-001 through IA-D04-004 into twelve dependency-ordered implementation packages and twenty-four normalized acceptance scenarios while preserving unfinished parallel work `P9-06-008-attempt-002`.

## IA-D05-001 through IA-D05-003 completion record

The Relationship Tracker, Factions/Reputation/Organizations, and Social Interaction Mode establish directional relationship history, faction membership/standing/influence separation, and roleplay-first social resolution with permission-safe persistent consequences.

## IA-D05-004 completion record

The Investigation and Clue Board defines ten core record types, fifteen typed connection forms, server-authoritative discovery and reveal, strict separation of truth, claims, hypotheses, and conclusions, accessible graph/list parity, twenty-four deterministic fixtures, eight implementation slices, twenty-eight blocking criteria, seven resolved findings, and zero blocking findings. `P9-06-008-attempt-002` remains unfinished and unmodified.

## IA-D05-005 completion record

The Graph/List Accessibility Matrix defines one semantic node/edge projection and six equivalent views for Relationship, Faction, Social, and Investigation surfaces. It requires complete keyboard, screen-reader, touch, text-scaling, high-contrast, reduced-motion, responsive, virtualization, hidden-topology, reconnect, export, diagnostic, and optional-AI parity through twenty-four deterministic fixtures, eight implementation slices, twenty-eight blocking criteria, seven resolved findings, and zero blocking findings. `P9-06-008-attempt-002` remains unfinished and unmodified.

## Current next design item

**IA-D05-006 — noncombat integration review — next.**

## Historical validation anchors

These archival lines preserve prior validated routes and are not the current next item:

**Version:** 0.11.0

- IA-D03-004 — alpha content and fixture specification — complete.
- IA-D03-005 — Character/Campaign integration review — next.

**IA-D03-005 — Character/Campaign integration review.**

**IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next.**

**IA-D04-002 — proposal and approval shared-component contract — next.**

**IA-D04-003 — two-device interruption and reconnect matrix — next.**

**IA-D04-004 — authoritative result and history presentation — next.**
