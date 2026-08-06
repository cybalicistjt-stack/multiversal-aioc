# Internal Alpha Shared Systems

**Program:** MV-IA-001  
**Version:** 0.2.0  
**Status:** DESIGN BASELINE

## 1. Purpose

Shared systems are designed before domain-specific duplication. Every feature packet must declare which shared systems it consumes, extends, or changes.

## 2. Shared system SS-01 — Application shell

Responsibilities:

- top navigation;
- desktop sidebar;
- mobile navigation;
- workspace selector;
- Campaign selector;
- Character selector;
- notifications;
- global search;
- user menu;
- responsive layout;
- loading, empty, error, offline, forbidden, stale, and recovery states.

Primary consumers: all features.

## 3. Shared system SS-02 — Identity and role context

Responsibilities:

- stable internal subject;
- active identity;
- Campaign membership;
- role resolution;
- active Character or actor context;
- service actor context;
- invitation and revocation state;
- account recovery status.

Primary consumers: dashboards, Campaigns, Sessions, content creation, AI, exports.

## 4. Shared system SS-03 — Authorization and visibility

Responsibilities:

- default deny;
- Campaign isolation;
- object and field visibility;
- Player-safe versus GM-only projections;
- search and count safety;
- realtime subscription safety;
- export and AI retrieval safety;
- revocation and cache invalidation.

Primary consumers: every feature handling Campaign or user data.

## 5. Shared system SS-04 — Entitlement evaluation

Responsibilities:

- free access;
- first two Ability-tree tiers;
- Campaign grants;
- sponsored access;
- restrictions;
- expiry;
- reasoned decisions;
- offline snapshots;
- historical-state preservation.

Primary consumers: content library, Character creation, object pickers, Sessions, AI.

## 6. Shared system SS-05 — Universal object experience

Responsibilities:

- browse;
- search;
- filter;
- exact stable-ID lookup;
- inspect;
- provenance;
- relationships;
- version and variant comparison;
- conflict display;
- picker constraints;
- preview;
- permission and entitlement badges.

Primary consumers: Character, Campaign, Scene, inventory, encounter, investigation, World Builder, AI.

## 7. Shared system SS-06 — Proposal and approval framework

Responsibilities:

- proposal author;
- actor;
- action or change type;
- source and rules summary;
- target scope;
- costs;
- calculated result;
- proposed Effects;
- warnings;
- approve;
- deny;
- modify;
- decision receipt;
- history;
- notification.

Primary consumers: live Actions, GM NPC Actions, social play, content submission, AI proposals, destructive changes.

Canonical contract: `feature-packets/IA-D04-002_PROPOSAL_APPROVAL_SHARED_COMPONENT_CONTRACT.md` version 0.1.0.

Companion artifacts:

- `feature-packets/IA-D04-002_PROPOSAL_APPROVAL_COMPONENT_MATRIX.json`;
- `feature-packets/IA-D04-002_CONSUMER_MAPPING.json`;
- `feature-packets/IA-D04-002_IMPLEMENTATION_TRACEABILITY.json`;
- `feature-packets/IA-D04-002_REVIEW_RECEIPT.md`;
- `feature-packets/IA-D04-002_READINESS_RECORD.md`;
- `feature-packets/IA-D04-002_COMPLETION_RECORD.json`.

The contract maps eight consumer types: live Player Actions, GM NPC/enemy Actions, social-play proposals, content submission, optional-AI proposals, destructive changes, canonical promotion, and Asset-transfer acceptance.

SS-06 owns common proposal envelopes, lifecycle, queue and notification projections, reviewer inspection, approve/deny/modify-and-approve decisions, immutable receipts, history, idempotency, reconnect, accessibility, and diagnostics. Each consumer retains proposer eligibility, reviewer authority, domain validation, calculation, modifiable-field policy, commit adapter, domain Events, visibility, retention, and owner gates.

The exact next design item is **IA-D04-003 — Two-Device Interruption and Reconnect Matrix**.

## 8. Shared system SS-07 — Persistence, drafts, and state versions

Responsibilities:

- local drafts;
- authoritative saves;
- optimistic versioning;
- idempotency;
- autosave;
- save status;
- conflict detection;
- snapshot metadata;
- event history;
- recovery receipts.

Primary consumers: all editable and live-state features.

## 9. Shared system SS-08 — Realtime and reconnect

Responsibilities:

- connection state;
- role-filtered subscription;
- ordered events;
- last acknowledged sequence;
- missed-event recovery;
- stale-client handling;
- duplicate command handling;
- reconnect;
- Session checkpoint recovery.

Primary consumers: live Sessions, notifications, approvals, combat, social, investigation.

## 10. Shared system SS-09 — Relationship and graph model

Responsibilities:

- typed nodes and edges;
- direction;
- visibility;
- source;
- Campaign placement;
- current state;
- history;
- thresholds;
- accessible list and table views;
- graph filtering.

Primary consumers: Relationship Tracker, factions, investigation, World Builder, adventures, dependency traversal.

## 11. Shared system SS-10 — Ownership and Asset transfer

Responsibilities:

- ownership;
- custody;
- controller;
- location;
- access;
- equipment slot;
- container nesting;
- transfer;
- acceptance;
- audit history;
- anti-duplication controls.

Primary consumers: inventory, crafting, vehicles, Campaign Assets, Scene objects.

## 12. Shared system SS-11 — Rules inspection and calculation presentation

Responsibilities:

- source-linked rule summary;
- prerequisites;
- cost;
- targets;
- roll or seed;
- modifiers and ordering;
- computed result;
- proposed and accepted Effects;
- Conditions;
- Resources;
- warnings;
- replay details.

Primary consumers: live Actions, combat, social, encounter building, help.

## 13. Shared system SS-12 — Activity, history, and timeline

Responsibilities:

- Campaign events;
- Character advancement;
- relationship history;
- Asset transfer;
- adventure progress;
- approvals;
- recovery;
- filters;
- role-safe projections.

Primary consumers: Campaign, Character, relationship, investigation, adventure, diagnostics.

## 14. Shared system SS-13 — Notifications and work queues

Responsibilities:

- approval requests;
- invitations;
- validation problems;
- failed operations;
- owner decisions;
- content review;
- reconnect status;
- read/unread and resolution state.

Primary consumers: dashboards, Sessions, content creation, owner workspace.

## 15. Shared system SS-14 — Validation and issue presentation

Responsibilities:

- errors;
- warnings;
- informational findings;
- source links;
- affected object and field;
- permitted fixes;
- owner-only decisions;
- retained failure evidence.

Primary consumers: Character creation, Scene Builder, content creation, packs, migration, AI validation.

## 16. Shared system SS-15 — Accessibility behavior

Responsibilities:

- semantic structure;
- keyboard navigation;
- visible focus;
- screen-reader names and states;
- live-region priority;
- text scaling;
- contrast;
- noncolor status;
- reduced motion;
- touch targets;
- nondrag alternatives;
- map and graph alternatives.

Primary consumers: all features.

## 17. Shared system SS-16 — Responsive information hierarchy

Responsibilities:

- desktop multi-panel layout;
- tablet adaptive layout;
- mobile single-focus flow;
- drawer and inspector behavior;
- preserved context;
- action priority;
- touch and keyboard equivalence.

Primary consumers: all interfaces.

## 18. Shared system SS-17 — Content pack lifecycle

Responsibilities:

- registry;
- installation;
- validation;
- dependency resolution;
- activation;
- update;
- migration;
- blocked removal;
- safe removal;
- reinstall;
- export;
- provenance.

Primary consumers: content library, Character, Campaign, Scene, World Builder.

## 19. Shared system SS-18 — Telemetry and diagnostics

Responsibilities:

- release identity;
- correlation IDs;
- operation state;
- errors;
- performance;
- reconnect;
- backup and restore status;
- cost signals;
- privacy-safe issue attachments.

Primary consumers: alpha administration, support, recovery, performance review.

## 20. Shared system SS-19 — Help and source-grounded explanation

Responsibilities:

- glossary;
- contextual help;
- rules browser;
- source display;
- examples;
- error recovery guidance;
- optional AI explanation using the same permission boundary.

Primary consumers: all Player and GM workflows.

## 21. Shared system SS-20 — Feature flags and experimental isolation

Responsibilities:

- environment-scoped enablement;
- tester cohort;
- dependency checks;
- safe disablement;
- fallback behavior;
- diagnostics;
- state compatibility;
- owner or release gate.

Primary consumers: AI, advanced maps, full vehicle stations, broad offline sync, experimental creator flows.

## 22. Change rule

A feature packet that modifies a shared system must include:

- affected consumers;
- compatibility impact;
- migration impact;
- retest list;
- fallback;
- documentation update.

A domain feature may not privately implement a conflicting version of a shared system.
