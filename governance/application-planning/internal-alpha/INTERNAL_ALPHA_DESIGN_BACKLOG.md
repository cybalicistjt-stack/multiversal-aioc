# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.12.0  
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
   - review: `feature-packets/IA-D03-005_CHARACTER_CAMPAIGN_INTEGRATION_REVIEW.md`
   - contract matrix: `feature-packets/IA-D03-005_CHARACTER_CAMPAIGN_CONTRACT_MATRIX.json`
   - findings: `feature-packets/IA-D03-005_INTEGRATION_FINDINGS_REGISTER.json`
   - traceability: `feature-packets/IA-D03-005_IMPLEMENTATION_TRACEABILITY.json`
   - result: 28 normalized contracts, eight journeys, twelve resolved findings, ten implementation slices, twenty-four blocking criteria, zero blocking findings
   - boundary: design integration only; implementation and release remain dependency-gated

## IA-D04 — First playable loop

1. **IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next.**
2. IA-D04-002 — proposal and approval shared-component contract.
3. IA-D04-003 — two-device interruption and reconnect matrix.
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

The completed Character/Campaign preparation integration provides:

- one explicit precedence order across F004, F005, F012, IA-D03-004, and the IA-D02-006 shared foundations;
- Campaign authority for policy, membership, roles, delegation, Character control, Scene validation, launch snapshots, and Session launch;
- Character lifecycle and advancement under exact Campaign policy and version bindings;
- source Definition, placement, instance, analysis snapshot, launch snapshot, Event, and projection separation;
- permission-safe roster binding, preview, warnings, exports, diagnostics, and optional-AI projections;
- advisory Encounter analysis with no guaranteed-balance, fairness, safety, victory, survival, or optimality claim;
- conflict-safe commands, Events, reconnect, revocation, recovery, migration, and export;
- 155 provenance-labeled deterministic fixture identities without canonical promotion or complete-game claims;
- ten dependency-ordered implementation slices and an exact IA-D04-001 handoff;
- zero blocking integration findings.

Implementation remains dependency-gated by P9-06.

## Current next design item

**IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next.**
