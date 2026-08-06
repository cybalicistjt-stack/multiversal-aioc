# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.18.0  
**Status:** ACTIVE DESIGN BACKLOG  
**Owner:** John Brandon Turner

## Backlog rule

This backlog governs design packets, fixture specifications, integration reviews, and implementation handoffs. Implementation remains dependency-gated by P9-06. A design item is complete only when artifacts exist, limitations and boundaries are explicit, deterministic final-step validation passes, and repository merge evidence is recorded. Intra-step validation and administrative updates are prohibited by MV-AI-EFFICIENCY-002.

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

1. IA-D03-001 — MV-IA-F004 Character Creation and Advancement — complete.
2. IA-D03-002 — MV-IA-F005 Campaign, Scene, and Session Builder — complete.
3. IA-D03-003 — MV-IA-F012 Encounter Builder and Balance Lab — complete.
4. IA-D03-004 — alpha content and fixture specification — complete.
5. IA-D03-005 — Character/Campaign integration review — complete.

## IA-D04 — First playable loop — COMPLETE

1. IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — complete.
2. IA-D04-002 — Proposal and Approval Shared-Component Contract — complete.
3. IA-D04-003 — Two-Device Interruption and Reconnect Matrix — complete.
4. IA-D04-004 — Authoritative Result and History Presentation — complete.
5. IA-D04-005 — First-Playable-Loop Implementation Handoff — complete.
   - result: twelve dependency-ordered implementation packages, twenty-four normalized acceptance scenarios, twenty-eight blocking criteria, zero blocking findings
   - boundary: implementation and release remain P9- and owner-gated

## IA-D05 — Relationship, social, and investigation systems

1. **IA-D05-001 — MV-IA-F009 Relationship Tracker — complete.**
   - result: fourteen registry-capable dimensions, seven reveal layers, twelve domain commands, eleven source-defined Events, twenty-four deterministic fixtures, eight implementation slices, twenty-eight blocking criteria, five resolved findings, zero blocking findings
   - source boundary: the 154-row relationship register contains four explicit relationship facts and 150 rows with no provided relationship; absence remains absence
   - product boundary: relationship remains separate from reputation/standing, public status, mood, intent, and stance
2. **IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations — next.**
3. IA-D05-003 — MV-IA-F010 Social Interaction Mode.
4. IA-D05-004 — MV-IA-F011 Investigation and Clue Board.
5. IA-D05-005 — graph/list accessibility and role-safe projection integration.
6. IA-D05-006 — noncombat systems integration review.

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

## IA-D04 completion record

The completed IA-D04 tranche defines Campaign → Character/actor → Scene/Session → Action proposal → GM decision → atomic result → ordered Event → role-safe result/history → two-device recovery and a dependency-ordered implementation handoff. It preserves NPC/enemy parity, source versions, hidden-information protection, accessibility, deterministic replay, and zero blocking findings.

## IA-D05-001 completion record

The Relationship Tracker defines first-class directional edges, explicit mutual pairing, profile-scaled multidimensional state, append-only Event history, seven audience reveal layers, graph/list/mobile/nonvisual parity, social Bond consent gates, leverage and obligation records, safe legacy-strength migration, pack lifecycle protection, and two-device recovery. It does not convert missing source data into relationships or merge personal relationships with faction reputation or temporary social state.

## Current next design item

**IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations.**

## Historical validation anchors

The following are archival route evidence, not the current item:

- IA-D03-005 → IA-D04-001.
- IA-D04-001 → IA-D04-002.
- IA-D04-002 → IA-D04-003.
- IA-D04-003 → IA-D04-004.
- IA-D04-004 → IA-D04-005.
- IA-D04-005 → IA-D05-001.
