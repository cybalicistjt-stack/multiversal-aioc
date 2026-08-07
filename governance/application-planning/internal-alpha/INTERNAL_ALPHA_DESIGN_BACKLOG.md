# Internal Alpha Feature Design Backlog

**Program:** MV-IA-001  
**Version:** 0.34.0  
**Status:** ACTIVE DESIGN BACKLOG  
**Owner:** John Brandon Turner

## Backlog rule

This backlog governs design packets, fixture specifications, and integration reviews. Implementation remains dependency-gated by P9-06. A design item is complete only when artifacts exist, limitations and boundaries are explicit, deterministic validation passes, and repository merge evidence is recorded.

## IA-D01 — Program foundation — COMPLETE
## IA-D02 — Shared foundations — COMPLETE
## IA-D03 — Character and Campaign preparation — COMPLETE
## IA-D04 — First playable loop — COMPLETE
## IA-D05 — Relationship, social, and investigation systems — COMPLETE
## IA-D06 — Combat and Assets — COMPLETE
## IA-D07 — World, adventure, and Project depth — COMPLETE

## IA-D08 — Optional AI and experimental systems

1. **IA-D08-001 — MV-IA-F023 Optional AI Assistant boundaries and interaction contract — complete.**
2. **IA-D08-002 — AI permission, provenance, cost, and fallback matrix — complete.**
3. **IA-D08-003 — advanced map and vehicle deferral package — complete.**
4. **IA-D08-004 — broad offline deferral package — package complete; merge verification pending.**
5. **IA-D08-005 — optional and experimental isolation review — next after IA-D08-004 merge.**

## IA-D09 — Internal-alpha release-design package

Traceability, fixture catalog, permission matrix, accessibility matrix, recovery matrix, budgets, onboarding, implementation queue, owner decisions, and completion review.

## Completion records

### IA-D07

World, adventure, creator, Campaign-local content, authority, and authoring integration design are complete. `P9-06-008-attempt-002` remains unfinished and unmodified.

### IA-D08-001

The Optional AI Assistant is opt-in, advisory-only, permission-filtered, provenance- and cost-visible, provider-abstracted, accessible, recoverable, and unable to block core non-AI workflows or cross owner gates.

### IA-D08-002

The AI governance matrix defines distinct permissions, provenance, hard budgets, provider routing, privacy, retention, deterministic fallback, accessibility, and duplicate-charge prevention.

### IA-D08-003

The advanced map and vehicle deferral package enumerates deferred and retained capabilities, prevents silent approximation, preserves unsupported data as opaque versioned extensions, produces compatibility reports, defines upgrade seams and migration receipts, and preserves provenance, accessibility, hidden-information filtering, and historical interpretation. It includes twenty-four fixtures, eight implementation slices, twenty-eight blocking criteria, seven resolved findings, and zero blocking findings.

### IA-D08-004

The broad offline deferral package preserves authorized cache, recoverable drafts, bounded replay-safe intent, authoritative status lookup, Event-gap recovery, reconnect reauthorization, permission-safe cache invalidation, opaque future-extension preservation, accessibility, and provenance while explicitly deferring broad offline campaign authority, peer authority transfer, unrestricted offline mutation, CRDT/OT canonical collaboration, offline publication/ownership/entitlement changes, and silent automatic merge. It prohibits local fabrication of canonical Events and silent last-write-wins, defines O0 through O4 offline command classes, includes twenty-four deterministic fixtures and eight implementation slices, and advances to IA-D08-005 after merge verification.

## Current next design item

**IA-D08-005 — optional and experimental isolation review — next after IA-D08-004 merge verification.**

## Parallel paused tracks

- `P9-06-008-attempt-002` remains unfinished and paused in the application-implementation track.
- The Design Standards Completion subproject is paused/resumable as recorded in `APPLICATION_IMPLEMENTATION_ROADMAP.md` v2.1.0; its chat-generated DS-006/DS-007 working packages are not repository-canonical until later governed ingestion.

## Validation-efficiency rule

`governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md` controls. Each IA item uses its targeted deterministic validator during construction and one final relevant hosted gate. Unrelated historical IA or Development Brain workflows must not be treated as required validation for every new packet. Recurring unrelated fan-out is a workflow-scoping defect.

## Historical validation anchors

These archival statements preserve earlier validated routes and versions. They are not the current next item.

**Version:** 0.11.0
**Version:** 0.24.0
**Version:** 0.25.0

IA-D03-004 — alpha content and fixture specification — complete.
IA-D03-005 — Character/Campaign integration review — complete.
IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop — complete.
IA-D04-002 — proposal and approval shared-component contract — complete.
IA-D04-003 — two-device interruption and reconnect matrix — complete.
IA-D04-004 — authoritative result and history presentation — complete.
IA-D04-005 — first-playable-loop implementation handoff — complete.
IA-D05-001 — MV-IA-F009 Relationship Tracker — complete.
IA-D05-002 — MV-IA-F016 Factions, Reputation, and Organizations — complete.
IA-D05-003 — MV-IA-F010 Social Interaction Mode — complete.
IA-D05-004 — MV-IA-F011 Investigation and Clue Board — complete.
IA-D05-005 — graph/list accessibility matrix — complete.
IA-D05-006 — noncombat integration review — complete.
IA-D06-001 — MV-IA-F007 Full Combat Interface — complete.
IA-D06-002 — MV-IA-F008 Inventory, Ownership, and Shared Assets — complete.
IA-D06-003 — bounded MV-IA-F013 Maps, Zones, and Tactical Positioning — complete.
IA-D06-004 — basic MV-IA-F014 Vehicle, Mecha, and Starship Operations — complete.
IA-D06-005 — combat/Asset integrity matrix — complete.
IA-D06-006 — combat and Assets integration review — complete.
IA-D07-001 — MV-IA-F015 World and Setting Management — complete.
IA-D07-002 — MV-IA-F017 Adventure and Module Management — complete.
IA-D07-003 — bounded MV-IA-F018 Creator and Campaign-local Content — complete.
IA-D07-004 — world/adventure content authority matrix — complete.
IA-D07-005 — authoring integration review — complete.
IA-D08-001 — MV-IA-F023 Optional AI Assistant boundaries and interaction contract — complete.
IA-D08-002 — AI permission, provenance, cost, and fallback matrix — complete.
IA-D08-003 — advanced map and vehicle deferral package — complete.
IA-D08-004 — broad offline deferral package — package complete; merge verification pending.
