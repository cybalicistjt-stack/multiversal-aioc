# Internal Alpha Feature Dependency Map

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** DESIGN BASELINE

## 1. Purpose

This map establishes design and implementation dependency order. It prevents work from beginning with attractive isolated screens that later require incompatible identity, object, permission, persistence, or recovery models.

## 2. Dependency layers

### Layer 0 — Governed content and release foundations

- **MV-IA-F024 — Pack Lifecycle and Canonical Content Registry**
- active Phase 9 service ports and future concrete adapters
- backup, restore, and provider-exit foundations

Every feature using real content depends on governed stable IDs, pack versions, installation state, provenance, and migration behavior.

### Layer 1 — Cross-cutting product foundations

- **MV-IA-F001 — Application Shell and Workspace Navigation**
- **MV-IA-F022 — Accessibility and Adaptive Interface**
- **MV-IA-F019 — Content Library and Entitlements**

Accessibility begins here rather than after feature implementation.

### Layer 2 — Universal retrieval and identity boundaries

- **MV-IA-F002 — Universal Object Experience**
- **MV-IA-F003 — Identity, Dashboard, and Workspace Selection**
- **MV-IA-F020 — Permissions and Hidden Information**

No domain picker, dashboard, search, or live projection should bypass these shared boundaries.

### Layer 3 — Durable user and Campaign state

- **MV-IA-F004 — Character Creation and Advancement**
- **MV-IA-F005 — Campaign, Scene, and Session Builder**
- **MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use**
- **MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting**

### Layer 4 — First playable vertical slice

- **MV-IA-F006 — First Playable Action and GM Approval Loop**

This is the first complete internal-alpha product proof.

### Layer 5 — Social and GM preparation systems

These may be designed early because they define reusable data and UI components:

- **MV-IA-F009 — Relationship Tracker**
- **MV-IA-F012 — Encounter Builder and Balance Lab**
- **MV-IA-F016 — Factions, Reputation, and Organizations**

### Layer 6 — Tabletop breadth

- **MV-IA-F007 — Full Combat Interface**
- **MV-IA-F008 — Inventory, Ownership, and Shared Assets**
- **MV-IA-F010 — Social Interaction Mode**
- **MV-IA-F011 — Investigation and Clue Board**

### Layer 7 — Content and Campaign depth

- **MV-IA-F013 — Maps, Zones, and Tactical Positioning**
- **MV-IA-F015 — World and Setting Builder**
- **MV-IA-F014 — Vehicle, Mecha, and Starship Operations**
- **MV-IA-F017 — Adventure and Story Flow Runtime**
- **MV-IA-F018 — Downtime, Crafting, and Projects**

### Layer 8 — Optional assistance

- **MV-IA-F023 — Governed AI Assistance**

AI is intentionally last because it must reuse completed identity, permission, entitlement, retrieval, provenance, proposal, and approval boundaries.

## 3. Critical dependency chain

```text
Pack lifecycle and content registry
    ↓
Shell + accessibility + content entitlements
    ↓
Universal object experience + identity + permissions
    ↓
Character + Campaign/Scene + persistence/recovery
    ↓
Action proposal and GM approval loop
    ↓
Combat / inventory / relationships / investigation / social
    ↓
World, adventure, vehicles, downtime, maps
    ↓
Governed AI assistance
```

## 4. Highest-leverage design order

The first feature packets should be designed in this order:

1. MV-IA-F002 — Universal Object Experience
2. MV-IA-F020 — Permissions and Hidden Information
3. MV-IA-F003 — Identity, Dashboard, and Workspace Selection
4. MV-IA-F021 — Autosave, Reconnect, Recovery, and Bounded Offline Use
5. MV-IA-F004 — Character Creation and Advancement
6. MV-IA-F005 — Campaign, Scene, and Session Builder
7. MV-IA-F006 — First Playable Action and GM Approval Loop
8. MV-IA-F009 — Relationship Tracker
9. MV-IA-F012 — Encounter Builder and Balance Lab
10. MV-IA-F025 — Onboarding, Help, Diagnostics, and Issue Reporting

This order maximizes reuse across later features.

## 5. Shared-component dependency clusters

### Object cluster

Used by:

- Character creation;
- Campaign and Scene Builder;
- inventory;
- encounter building;
- investigation;
- relationships;
- World Builder;
- AI retrieval.

Required shared components:

- object browser;
- object inspector;
- object picker;
- provenance panel;
- relationship viewer;
- version and variant comparison;
- visibility and entitlement badges.

### Proposal and approval cluster

Used by:

- Player Actions;
- GM NPC Actions;
- social outcomes;
- content submissions;
- AI suggestions;
- canonical promotion requests;
- destructive actions.

Required shared components:

- proposal summary;
- source and rules details;
- warnings;
- approve, deny, modify controls;
- decision receipt;
- history.

### Relationship and graph cluster

Used by:

- Relationship Tracker;
- factions;
- investigation;
- World Builder;
- adventure flow;
- dependency traversal.

Required shared components:

- typed edge editor;
- graph and list views;
- visibility filter;
- history timeline;
- thresholds and states;
- accessible nonvisual representation.

### Asset and ownership cluster

Used by:

- inventory;
- crafting;
- vehicles;
- Campaign Assets;
- shops;
- Scene objects.

Required shared components:

- owner/custodian display;
- transfer flow;
- permission check;
- equipment and container slots;
- audit history;
- duplication/loss safeguards.

## 6. Parallel design that is safe before P9-06-008

The following design work may proceed without implementing around the paused backend dependency:

- feature packet requirements;
- user journeys;
- object and relationship data needs;
- permission matrices;
- error and recovery-state design;
- accessibility behavior;
- acceptance tests;
- fixture definitions;
- content-corpus selection;
- telemetry event definitions without provider activation;
- UI information architecture and interaction contracts.

## 7. Implementation hold points

A feature packet may be implementation-ready but should not enter application implementation when it requires an incomplete blocking dependency.

Examples:

- trusted alpha data must not be promised durable before backup and restore pass;
- a live Action loop must not bypass authoritative Session contracts;
- universal search must not expose objects before permission and entitlement filtering exist;
- AI retrieval must not begin before the same visibility rules used by the product are available.

## 8. Dependency-change rule

A feature packet that changes a shared dependency must identify every affected downstream feature and invalidate or revise their design packets where necessary.