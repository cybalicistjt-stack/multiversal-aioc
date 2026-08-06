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
   - boundary: design integration only; implementation and release remain dependency-gated

## IA-D04 — First playable loop

1. **IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — complete.**
2. **IA-D04-002 — proposal and approval shared-component contract — complete.**
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

The completed Character/Campaign preparation integration provides Campaign policy authority, Character lifecycle and control boundaries, Definition/placement/instance separation, advisory Encounter analysis, immutable launch snapshots, durable Event authority, conflict-safe recovery, bounded offline use, transparent fixture provenance, accessibility parity, zero-service operation, ten implementation slices, and zero blocking findings.

Implementation remains dependency-gated by P9-06.

## IA-D04-001 completion record

The implementation-ready First Playable Action and GM Approval Loop provides Player Action proposals, source-linked rule inspection, target/cost/roll/Effect evidence, GM approve/deny/modify-and-approve decisions, NPC/enemy parity, atomic `ActionResultCommitted` authority, role-safe projections, idempotency, reconnect recovery, fourteen deterministic fixtures, ten implementation slices, twenty blocking acceptance criteria, and zero blocking findings.

Implementation remains dependency-gated by P9-06.

## IA-D04-002 completion record

The completed Proposal and Approval Shared-Component Contract provides:

- a versioned consumer-adapter boundary that preserves each domain's authority;
- twenty common proposal lifecycle states;
- thirty proposal-envelope fields and twenty-four immutable decision-receipt fields;
- approve, deny, modify-and-approve, and bounded request-changes behavior;
- field-addressed allowlisted modification, revalidation, recalculation when required, before/after evidence, and final confirmation;
- single-authorized-reviewer, sequential-required-reviewers, owner-only, and explicit no-approval policies;
- exactly-once domain commit-adapter invocation with proposal/domain Event separation and no partial success;
- permission-safe queues, notifications, inspection, history, export, diagnostics, support, and optional-AI projections;
- idempotency, optimistic concurrency, ambiguous-failure status lookup, reconnect, revocation, expiry, withdrawal, supersession, conflict preservation, and bounded offline drafts;
- eight mapped consumers, sixteen deterministic fixtures, ten implementation slices, twenty blocking acceptance criteria, and zero blocking findings;
- zero-AI and zero-paid-service core operation.

The shared component never grants domain authority merely because a generic proposal is approved. Implementation remains dependency-gated by P9-06.

## Current next design item

**IA-D04-003 — Two-Device Interruption and Reconnect Matrix — next.**

## Historical IA-D03-004 validation anchor

This archival block preserves the exact handoff language validated when IA-D03-004 completed. It is historical evidence, not the current route or document version.

**Version:** 0.11.0

- IA-D03-004 — alpha content and fixture specification — complete.
- IA-D03-005 — Character/Campaign integration review — next.

**IA-D03-005 — Character/Campaign integration review.**

## Historical IA-D03-005 to IA-D04-001 handoff anchor

This archival line preserves the exact prior validated route and is not the current next item:

**IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — next.**

## Historical IA-D04-001 to IA-D04-002 handoff anchor

This archival block preserves the exact F006 completion route and is not the current next item.

**Version:** 0.13.0

**IA-D04-002 — proposal and approval shared-component contract — next.**

**IA-D04-002 — Proposal and Approval Shared-Component Contract — next.**
