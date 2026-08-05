# Multiversal Project Bible v2.0

> **Document status:** Audited release candidate — canonical repository integration pending  
> **Document role:** Primary human- and AI-readable project handbook  
> **Owner and final authority:** John Brandon Turner  
> **Canonical repositories:** `cybalicistjt-stack/Multiversal-app`; `cybalicistjt-stack/multiversal-aioc`  
> **Working-copy rule:** This file is rebuilt as one complete manuscript. A continuation must preserve and improve all accepted material already present.  
> **Current editorial milestone:** Final editorial audit PASS; canonical repository integration pending
> **Editorial audit date:** 2026-08-05  
> **Verified application repository head:** `149b866f530f3a8896170bfe3ba6af0c01fb2f72`  
> **Verified governance repository head:** `29278c8568114ffc77ba4176aa88b664875ca35a`  
> **Release checksum rule:** The exact audited-file checksum is maintained in the companion `.sha256` file and release manifest to avoid self-referential checksum changes.

---

# Document Control

## Purpose

The Multiversal Project Bible is the integrated handbook for the project. It connects product identity, game-system architecture, content architecture, application design, technical architecture, repository governance, AI-development operations, validation, and release planning.

It does not replace machine-enforced schemas, validators, source registries, test fixtures, CI definitions, or repository history. Instead, it explains how those authorities fit together and directs contributors to the controlling artifacts.

## Authority and conflict rules

When sources disagree, use the following order:

1. A direct, current decision by John Brandon Turner.
2. Newer verified repository evidence.
3. Active governance documents in `multiversal-aioc`.
4. Validated canonical schemas, registries, packs, fixtures, and tests.
5. Approved architecture and planning packages.
6. This Project Bible.
7. Historical Development Bible material.
8. Conversation history and informal notes.

The Bible must be corrected when it conflicts with a higher authority. It must never silently convert an unresolved conflict into canon.

## Normative vocabulary

- **Must / shall:** mandatory requirement.
- **Must not / shall not:** prohibited behavior.
- **Should:** preferred behavior that may be departed from with recorded rationale.
- **May:** permitted behavior.
- **Example:** explanatory only; not an additional rule.
- **Recommendation:** reversible implementation guidance; not owner-locked canon unless promoted.
- **Owner decision required:** work must stop at that boundary.

## Status vocabulary

| Status | Meaning |
|---|---|
| Vision | Desired direction without a complete approved specification |
| Designed | Approved at the architectural or workflow level |
| Canonical | Locked as the controlling specification |
| Implemented | Present in repository code or governed data |
| Validated | Verified by defined tests or governance checks |
| Operational | In active project use |
| Deferred | Intentionally postponed |
| Deprecated | Superseded but retained for migration or history |
| Archived | Historical only; not current authority |

## Section template

Substantive sections should state, as applicable:

1. Purpose
2. Scope
3. Canonical specification
4. Design rationale
5. Dependencies
6. Implementation status
7. Future considerations
8. Controlling references

---

# Master Table of Contents

## Volume I — Project Foundation

1. Project Identity
2. Vision, Mission, and Product Boundaries
3. Project History and Architectural Evolution
4. Canon, Governance, and Authority
5. Repository and Documentation Architecture
6. AI Contributor Operating Model

## Volume II — Multiversal Game System

7. Rules Philosophy and Runtime Contract
8. Core Resolution Model
9. Character Lifecycle
10. Character Composition and State
11. Progression and Advancement
12. Actions
13. Effects
14. Conditions and Statuses
15. Resources
16. Modifiers, Ordering, and Stacking
17. Abilities, Powers, and Capability Domains
18. Combat
19. Social Play
20. Investigation
21. Exploration and Environments
22. Downtime and Projects
23. Crafting and Economy
24. Items, Vehicles, Mecha, and Starships
25. Creatures, NPCs, Species, and Forms
26. Balance and Regression Philosophy

*Tranche 2 Integration Review*

## Volume III — World and Content Architecture

27. Multiversal Cosmology and Setting Boundaries
28. Content Domains
29. World and Setting Packs
30. Adventure, Campaign, Quest, and Scene Content
31. Organizations, Factions, Relationships, and Reputation
32. Content Production Standards
33. Art, Asset, and Localization Pipelines

*Tranche 3 Integration Review*

## Volume IV — Object and Data Architecture

34. Canonical Object Model
35. Stable Identifiers
36. Schemas and Validation
37. Pack Format and Lifecycle
38. Dependencies, Extensions, and Overrides
39. Provenance and Coverage
40. Installation, Update, Migration, and Removal
41. Runtime Representation and Indexing

*Tranche 4 Integration Review*

## Volume V — Application Design

42. Product Shell and Navigation
43. Player Experience
44. Game Master Experience
45. Character Builder and Character Workspace
46. Campaign, Session, and Scene Builder
47. Live Session and Approval Workflows
48. Combat Interface
49. Inventory, Shared Assets, Crafting, and Vehicles
50. Investigation and Social Workspaces
51. World Builder and Content Studio
52. Rules Browser, Search, and Contextual Help
53. Accessibility, Responsive Design, and Themes

*Tranche 5 Integration Review*

## Volume VI — Technical Architecture

54. System Context and Technology Direction
55. Provider-Neutral Service Architecture
56. Identity and Authorization
57. Entitlements and Freemium Policy
58. Persistence and Migration
59. Realtime and Authoritative Sessions
60. Backup, Restore, and Provider-Exit Export
61. Security, Privacy, and Secrets
62. Observability, Performance, and Cost Controls
63. Testing and CI Architecture
64. Deployment and Platform Boundaries

*Tranche 6 Integration Review*

## Volume VII — AI Development Operations

65. AI Team Structure
66. Authority, Approval, and Stop Conditions
67. Context Loading and Credit Optimization
68. Work Orders and Bounded Execution
69. Repository Workflow
70. Review and Quality Gates
71. Checkpoints, Handoffs, and Recovery
72. Documentation and Decision Preservation

*Tranche 7 Integration Review*

## Volume VIII — Roadmap, Verification, and Release

73. Completed Project Phases
74. Current Implementation Program
75. Acceptance Gates
76. Internal Alpha
77. Closed Alpha and Beta
78. Commercial and Public-Release Readiness
79. Parallel Apple Platform Track
80. Risks, Deferred Work, and Owner Decisions

*Tranche 8 Integration Review*

## Appendices

A. Glossary  
B. Abbreviations  
C. Naming and Stable-ID Reference  
D. Canonical Repository Map  
E. Decision Register  
F. Source and Provenance Index  
G. Developer Checklists  
H. Validation and Release Checklists  
I. AI Prompt and Work-Order Templates  
J. Change Log

---

# Volume I — Project Foundation

# 1. Project Identity

## 1.1 Official identity

**Project name:** Multiversal  
**Owner and final authority:** John Brandon Turner

Multiversal is privately owned intellectual property. Contributors, repositories, tools, AI systems, governance documents, and implementation teams support the owner’s vision; none supersede the owner.

## 1.2 Product definition

Multiversal is a broad tabletop role-playing platform, not merely a single game, campaign, setting, virtual tabletop, character sheet, rules compendium, or AI storyteller.

It combines:

- a universal and extensible tabletop rules framework;
- governed modular game content;
- player and Game Master workflows;
- campaign, world, character, scene, and asset management;
- local and online session support;
- provider-neutral technical architecture;
- contextual AI assistance;
- repository-governed development and content production.

## 1.3 Primary participants

### Owner

Controls project direction, canon, spending, production credentials, deployment, release, irreversible vendor commitments, and final approval.

### Game Master

Acts as the table-level narrative and adjudication authority within the permissions of a campaign. The application supports and records GM decisions; it does not erase the GM’s role.

### Player

Creates and controls characters, makes choices, proposes actions, manages accessible assets, and participates in campaigns under the active rules and visibility model.

### Creator or curator

Creates or maintains governed worlds, adventures, characters, creatures, items, abilities, and other content through approved schemas and validation.

### AI contributor

Performs bounded development, documentation, validation, analysis, or content-support tasks under explicit authority and repository evidence.

## 1.4 Permanent ownership principle

No automated system may convert delegated operational authority into project ownership. AI recommendations remain recommendations unless accepted through the project’s authority and governance process.

**Status:** Canonical

---

# 2. Vision, Mission, and Product Boundaries

## 2.1 Mission

Enable people to create, play, expand, and preserve tabletop role-playing experiences across virtually any genre through a consistent, extensible rules framework and an application that reduces bookkeeping without replacing human creativity.

## 2.2 Vision

Multiversal should support fantasy, science fiction, horror, mystery, superheroes, historical play, modern drama, comedy, survival, cosmic adventure, and hybrid genres without requiring unrelated game engines for each setting.

The long-term platform should allow thousands of worlds and content packs to coexist while retaining:

- reliable identity;
- traceable provenance;
- controlled compatibility;
- deterministic validation;
- understandable mechanics;
- portable user and campaign data;
- reversible provider choices.

## 2.3 Product pillars

### Human creativity first

The application and AI enhance human storytelling and decision-making. They do not become the sole author or table authority.

### Game Master authority

The GM may approve, deny, or explicitly alter outcomes where the campaign workflow grants adjudication. The system must distinguish calculated results from GM adjustments and final accepted outcomes.

### One framework, many domains

Combat, investigation, social interaction, exploration, travel, crafting, downtime, vehicles, and other play modes are first-class systems built from shared mechanics.

### Canon before convenience

Implementation shortcuts may not silently change rules, identities, provenance, permissions, or content meaning.

### Modularity

Content, systems, services, and UI capabilities should be replaceable or extensible without forcing a total redesign.

### Provider neutrality

Core contracts must not depend unnecessarily on a specific authentication, database, realtime, hosting, storage, AI, backup, or deployment provider.

### Explainability

A player, GM, maintainer, or validator should be able to determine why an outcome occurred and which source authorized it.

### Long-term preservation

Project knowledge must be stored in durable governed artifacts rather than conversation memory.

## 2.4 Product non-goals

Multiversal is not intended to become:

- a conventional video game with fixed authored paths;
- a fully autonomous replacement for a human GM;
- a vendor-locked content silo;
- an application in which UI prose becomes the rules authority;
- a system that silently fills missing canon with generated assumptions;
- a single-setting product disguised as a universal engine;
- a public or production service before formal release gates are satisfied.

## 2.5 Success criteria

Multiversal succeeds when it provides:

- enjoyable and understandable tabletop play;
- broad genre support without incompatible core engines;
- reduced GM bookkeeping;
- strong player agency;
- reusable and searchable canonical content;
- deterministic and auditable resolution;
- safe offline and online session continuity;
- pack portability and provider-exit capability;
- sustainable AI-assisted development;
- preserved owner control.

**Status:** Canonical at the product-principle level; implementation remains phased.

---

# 3. Project History and Architectural Evolution

## 3.1 Phase history

### Phase 0 — Legacy source creation

John Brandon Turner and his brother created the original body of game material in legacy PDFs and related source files.

### Phase 0.5 — Multiversal definition

The project was formally defined as a broad, system-flexible tabletop RPG platform rather than a narrow single-game application.

### Phases 1–7 — Design and preparation

These phases established:

- product conception and scope;
- functional design;
- data and pack architecture;
- mechanics architecture;
- content-domain architecture;
- UI and workflow design;
- governed repository preparation.

### Phase 8 — Canonicalization and validation

Phase 8 converted the accumulated design and source material into governed structures.

Verified outcomes include:

- standards and normalization;
- canonical domain architecture;
- source conversion;
- final domain validation;
- a golden regression corpus;
- a balance harness;
- the AI Development Team Operating Package;
- 20 governed datasets;
- 19,199 source rows and 19,199 promoted records;
- zero unprocessed rows;
- passing provenance, runtime, installation, and uninstallation validation.

### Phase 9 — Architecture and bounded implementation readiness

Phase 9 established:

- entitlement and freemium architecture;
- sponsored-month behavior;
- authoritative session architecture;
- a Postgres-centered but provider-neutral architecture class;
- a bounded technical spike and cost envelope;
- the P9-06 ordered implementation backlog and acceptance gates.

The owner authorized bounded implementation of P9-06-001 through P9-06-023.

### Current implementation state

Repository evidence records P9-06-001 through P9-06-007 as complete and merged. The next executable item is P9-06-008, backup, restore, and provider-exit export ports.

The Bible must not treat later planned phases as implemented.

## 3.2 Major architectural milestones

### Universal rules framework

Settings and genres share a core execution model instead of creating unrelated engines.

### Canonical object architecture

Game content is represented as governed objects rather than only as prose documents.

### Pack architecture

Content can be installed, updated, extended, migrated, and removed as modular packages.

### Stable identity

Canonical objects retain deterministic identifiers across imports, references, migrations, and runtime use.

### Provenance

Canonical records retain source origin and transformation history.

### Cross-domain consolidation

Shared actions, effects, conditions, resources, rules profiles, and progression patterns are represented once and reused.

### Repository separation

The application repository contains active implementation. The AIOC repository contains governance, planning, canonical intelligence, and institutional memory.

### Provider-neutral ports

Identity, entitlement, persistence, migration, realtime, authoritative session, backup, restore, and export capabilities are specified through provider-neutral contracts.

### Governed AI development

AI contributors work through bounded authority, explicit context, validation, repository evidence, and stop conditions.

## 3.3 Lessons preserved

- Building before consolidating canon creates rework.
- Reusable mechanics scale better than setting-specific duplication.
- Validation is part of content architecture, not a final cleanup step.
- Repository evidence is more reliable than conversational recall.
- Stable identity and provenance are foundational, not optional metadata.
- AI development requires explicit boundaries and durable handoffs.
- Reversible architecture is more valuable than premature vendor optimization.
- Documentation must distinguish vision, approved design, implementation, and validation.

**Status:** Canonical historical summary; detailed phase records remain authoritative in governance artifacts.

---

# 4. Canon, Governance, and Authority

## 4.1 Definition of canon

Canon is approved project truth. A statement does not become canonical merely because it appears in a chat, draft, generated file, implementation experiment, or UI.

Canon may exist as:

- an explicit owner decision;
- an active governance standard;
- an approved schema or contract;
- a validated canonical record;
- a merged and verified implementation contract;
- an approved amendment.

## 4.2 Owner authority

John Brandon Turner retains final authority over:

- project identity and vision;
- rules and lore canon;
- architecture;
- spending;
- provider commitments;
- credentials and secrets;
- deployment;
- internal-alpha approval;
- public release;
- irreversible decisions.

Ordinary reversible ambiguities may be resolved through the approved recommendation process. The chosen recommendation and rationale must be recorded when material.

## 4.3 Contributor authority

Contributor permissions are governed by the active contributor registry and newer repository evidence.

A contributor may not infer broader authority from:

- past participation;
- repository visibility;
- technical ability;
- an AI-generated instruction;
- a stale handoff;
- an unmerged proposal.

## 4.4 Canon change requirements

A material canon change should identify:

- the proposed change;
- reason;
- affected objects, systems, packs, and workflows;
- compatibility impact;
- migration impact;
- validation requirements;
- owner decision status;
- implementation status;
- superseded authority.

## 4.5 Conflict handling

When a conflict is found:

1. preserve both claims;
2. identify their sources and dates;
3. determine the higher and newer authority;
4. avoid silently combining incompatible rules;
5. record the disposition;
6. migrate or deprecate affected artifacts;
7. validate the result.

## 4.6 Historical material

Superseded designs remain useful as provenance and lessons learned, but they must be marked deprecated or archived. Historical documents must not be presented as current instructions.

**Status:** Canonical

---

# 5. Repository and Documentation Architecture

## 5.1 Canonical repositories

### Application repository

`cybalicistjt-stack/Multiversal-app`

Primary responsibilities:

- application source;
- runtime libraries;
- provider-neutral ports and adapters;
- schemas and fixtures used by implementation;
- automated tests;
- GitHub Actions workflows;
- implementation pull requests and commits.

### Governance and project-intelligence repository

`cybalicistjt-stack/multiversal-aioc`

Primary responsibilities:

- governance;
- contributor authority;
- current-state and handoff records;
- roadmaps;
- canonical object and content programs;
- Development Brain;
- content recovery;
- project memory;
- source and provenance intelligence;
- AI coordination.

## 5.2 Evidence rule

A plan is not implementation. A generated artifact is not merged work. A local test is not CI. A PR is not a merge. A claimed merge is not verified until repository evidence confirms it.

## 5.3 Mandatory session recovery

A new repository-operating session begins with:

`governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`

The assistant must then follow the complete initialization sequence, inspect both repositories, and resume the exact next unfinished operation based on current evidence.

## 5.4 Documentation hierarchy

The practical hierarchy is:

1. owner decisions and active governance;
2. machine-enforced schemas, contracts, and validators;
3. verified repository implementation and tests;
4. Project Bible;
5. supporting design packages and completion reports;
6. historical drafts and conversations.

The Bible explains the system but must point to machine-enforced authority rather than duplicating every dataset record or formula.

## 5.5 Staleness handling

Some handoff or current-state documents may lag behind newer repository evidence. When detected:

- trust the newer evidence;
- do not conceal the mismatch;
- update the stale governance artifact through a verified workflow when tooling permits;
- keep the Bible aligned to the newer verified state.

**Status:** Canonical

---

# 6. AI Contributor Operating Model

## 6.1 Purpose

The AI operating model enables substantial autonomous work while preserving owner authority, traceability, and quality.

## 6.2 Operating principles

- Execute approved work rather than repeatedly restating plans.
- Recover context from repositories and canonical artifacts.
- Use the smallest sufficient authoritative context.
- Prefer reversible recommendations for ordinary ambiguities.
- Stop only for owner-only gates or real tool limitations.
- Inspect failures, identify root causes, repair them, and continue.
- Never claim unverified work.
- Preserve source truth, variants, conflicts, provenance, and reversibility.

## 6.3 Functional roles

An AI contributor may act as one or more bounded roles:

- documentation architect;
- technical architect;
- repository operator;
- implementation engineer;
- content architect;
- rules validator;
- test and quality engineer;
- provenance auditor;
- release coordinator.

Role labels describe responsibilities, not independent authority.

## 6.4 Mandatory boundaries

Without separate authorization, AI contributors must not:

- spend money;
- enroll in paid plans;
- deploy production;
- publish publicly;
- create or expose production credentials;
- make irreversible vendor commitments;
- approve internal alpha or public release;
- invent missing canon.

## 6.5 Work continuity

A complete handoff identifies:

- current authority;
- completed verified work;
- active branch or PR when applicable;
- checks and evidence;
- unresolved failures;
- owner decisions required;
- exact next executable action.

**Status:** Canonical and operational at the governance level.

---

# Volume II — Multiversal Game System

# 7. Rules Philosophy and Runtime Contract

## 7.1 Purpose

Define the common game-system obligations that every play mode, content domain, rules extension, and runtime implementation must preserve.

## 7.2 Scope

This volume explains the shared architecture of the game. Individual formulas, ability descriptions, species traits, item records, encounter values, and other specific content remain authoritative in their governed datasets and packs.

## 7.3 Governing principles

### Data is authoritative

UI labels, summaries, tooltips, and AI explanations are projections of governed records. They may clarify but may not silently become executable canon.

### Shared mechanics are represented once

Combat, social play, investigation, exploration, crafting, downtime, creatures, items, vehicles, powers, and settings reuse canonical actions, effects, conditions, resources, modifiers, and rules profiles.

### All major play modes are first-class

Non-combat systems must not be implemented as decorative prose around a combat-only engine.

### Missing information remains visible

Unknown, incomplete, ambiguous, or conflicting records must be marked, quarantined, or routed for adjudication. The system must not fabricate completeness.

### Resolution is reproducible

Given the same authoritative state, declarations, permissions, roll results or seed, modifier ordering, and adjudications, the runtime must produce the same result.

### Every accepted change is explainable

The system must be able to identify:

- who initiated the operation;
- what rule authorized it;
- what was targeted;
- what costs were committed;
- what roll or deterministic test occurred;
- which modifiers applied;
- what result was calculated;
- whether a GM changed it;
- what final state changed.

## 7.4 Rules versus application

The game rules exist independently of the application. The application:

- validates and executes governed rules;
- records decisions and state;
- presents accessible workflows;
- automates bookkeeping;
- supports adjudication.

It does not redefine the game through implementation convenience.

## 7.5 Rules profiles

A rules profile binds reusable calculation, scaling, recovery, compatibility, or degree-of-success behavior to content.

A profile should identify:

- stable ID;
- compatible versions;
- input contract;
- calculation and ordering rules;
- output contract;
- error behavior;
- migration requirements.

Content references profiles rather than copying formulas into each record.

## 7.6 Authority during play

The runtime resolves deterministic rules. The GM adjudicates ambiguity where permitted.

The application must distinguish:

1. declared proposal;
2. validated inputs;
3. calculated result;
4. GM approval, denial, or alteration;
5. final accepted result;
6. applied state change.

An alteration is explicit, attributed, and auditable.

## 7.7 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/README.md`
- DB-004 `DevelopmentBible/02-game-framework/core-rules-model.md`
- Phase 8 cross-domain consolidation packages
- Golden rules corpus and balance harness
- Rules runtime architecture and implementation roadmap

**Status:** Canonical architecture; dataset-specific mechanics remain separate authorities.

---

# 8. Core Resolution Model

## 8.1 Resolution stages

Multiversal separates four stages:

1. **Declaration**
2. **Validation**
3. **Resolution**
4. **Application**

These stages must remain distinguishable in logs, tests, UI, and authoritative-session behavior.

## 8.2 Declaration

A declaration states the intended operation and enough context to validate it.

It may include:

- actor;
- selected action or rule;
- target or targets;
- chosen parameters;
- declared substitutions;
- intended resource use;
- optional reactions or contingencies;
- visibility requirements.

A proposal may be incomplete, but it may not proceed to resolution until mandatory inputs are present.

## 8.3 Validation

Validation evaluates:

- actor authority and ownership;
- campaign and session permissions;
- timing;
- action availability;
- prerequisites;
- target legality;
- range, location, and visibility;
- content and entitlement access;
- costs and resources;
- incompatibilities and exclusions;
- required GM approval.

Validation failure produces a typed result and no hidden partial mutation.

## 8.4 Resolution

Resolution applies:

- declared rules profile;
- recorded random result or reproducible seed;
- substitutions;
- reactions and interrupts;
- ordered modifiers;
- degree-of-success logic;
- conditional branches;
- effect generation.

The calculation result is preserved even when the GM later changes the accepted outcome.

## 8.5 Application

Application converts accepted effects into state changes.

Application must be:

- authorized;
- ordered;
- auditable;
- idempotent or protected against duplicate execution;
- capable of reporting complete, failed, or compensating outcomes.

Where an operation cannot be atomic, the contract must define compensation or recovery behavior.

## 8.6 Canonical execution vocabulary

### Actor

An entity initiating an operation.

### Target

An entity, location, zone, asset, collection, or other governed subject of an operation.

### Action

An executable declaration containing timing, permissions, requirements, costs, targeting, resolution, and outcomes.

### Check or roll

A governed random or deterministic test that uses a declared rules profile.

### Effect

A bounded state-change instruction produced by a rule or resolution.

### Condition

A named ongoing state with a defined lifecycle and mechanical hooks.

### Resource

A governed pool, quantity, charge, capacity, timer, or similar value used by rules.

### Modifier

An ordered adjustment with a source, scope, stacking behavior, and duration.

### Event

An immutable record of a validated occurrence.

### Projection

A current view derived from accepted events and persisted authoritative state.

## 8.7 Randomness

Randomness must be represented by either:

- explicit recorded roll results; or
- a reproducible seed, algorithm identity, and algorithm version.

The application must not reconstruct a supposedly authoritative result using a new random operation.

## 8.8 Cost timing

Preconditions are evaluated before costs are committed unless a governing rule explicitly defines a cost for an attempted or failed action.

## 8.9 Adjudication

When content is ambiguous or a table-level judgment is required, the runtime records the adjudication. It must not manufacture a hidden rule and present it as canon.

## 8.10 Failure taxonomy

At minimum, the resolution system should distinguish:

- malformed declaration;
- unauthorized actor;
- unavailable action;
- unmet prerequisite;
- invalid target;
- insufficient resource;
- incompatible rule or schema version;
- unresolved content ambiguity;
- deterministic calculation failure;
- approval denied;
- application conflict;
- duplicate or stale operation;
- recovery required.

**Status:** Canonical architecture; implementation maturity varies by P9 and later runtime work.

---

# 9. Character Lifecycle

## 9.1 Purpose

Define how characters are created, validated, played, advanced, migrated, retired, archived, and recovered without losing source or advancement history.

## 9.2 Lifecycle states

A character may move through states such as:

- draft;
- rules-incomplete;
- ready for validation;
- valid and playable;
- active in a campaign;
- temporarily unavailable;
- migration required;
- retired;
- archived;
- recovered from backup or import.

The exact enum is an implementation contract, but the distinctions must not be collapsed into a single active/inactive flag.

## 9.3 Creation as a staged transaction

Character creation is not a loose collection of form fields. It is a staged process that records:

- campaign context;
- source and entitlement availability;
- identity and ownership;
- species, form, or ancestry choices;
- attributes and derived values;
- abilities, skills, and proficiencies;
- progression selections;
- starting resources;
- inventory and equipment;
- relationships and campaign ties;
- appearance, biography, and presentation;
- unresolved or optional choices.

A draft may be saved while incomplete. It must not be represented as valid and playable until required gates pass.

## 9.4 Validation gates

Character validation may include:

- required identity fields;
- campaign membership and permissions;
- species or form compatibility;
- choice budgets;
- prerequisites;
- mutual exclusions;
- duplicate grants;
- resource bounds;
- inventory compatibility;
- required progression nodes;
- campaign restrictions;
- entitlement constraints;
- content and schema compatibility.

A validation result should explain each blocking or advisory issue and identify the rule source.

## 9.5 Campaign participation

Joining a campaign may add:

- campaign-specific rules;
- temporary content access;
- campaign grants;
- relationships;
- permissions;
- visibility scopes;
- starting assets;
- GM adjudications.

Campaign-specific changes must not mutate global canonical content.

## 9.6 Migration

A migrated character preserves:

- stable identity;
- ownership;
- source references;
- advancement history;
- superseded or unavailable choices;
- migration receipts;
- unresolved discrepancies.

Migration must not silently delete a historical selection merely because its source became unavailable.

## 9.7 Retirement and archive

Retirement ends active use without erasing history. Archive reduces active visibility while preserving provenance, campaign references, and recovery potential.

## 9.8 Recovery

A recovered character must be validated against:

- manifest integrity;
- schema compatibility;
- pack dependencies;
- campaign identity;
- ownership;
- advancement replay;
- current projection.

Recovery discrepancies are reported; they are not silently reconciled.

**Status:** Canonical domain model; full user-facing lifecycle is planned for later application phases.

---

# 10. Character Composition and State

## 10.1 Character aggregate

A character is an aggregate containing or referencing:

- stable identity;
- owner and authorized controllers;
- campaign memberships;
- species, subspecies, form, and adaptation selections;
- attributes and derived values;
- skills and proficiencies;
- abilities and capability grants;
- resources;
- active and historical conditions;
- inventory, equipment, and shared assets;
- relationships, affiliations, and reputation;
- progression history;
- notes, biography, appearance, and presentation data;
- visibility classification;
- rules and schema versions.

## 10.2 State distinctions

The character model must distinguish:

- authored choices from granted choices;
- base values from derived values;
- permanent advancement from temporary effects;
- mechanical state from presentation data;
- user-owned content from campaign-granted access;
- current projection from historical events;
- active grants from inactive historical grants;
- public, party-visible, GM-only, and private data.

## 10.3 Grant provenance

Every granted element records:

- grant source;
- grant reason;
- grant time or event;
- duration or permanence;
- activation state;
- replacement and stacking behavior;
- removal or expiration rule.

A displayed ability without grant provenance is insufficient for a canonical character state.

## 10.4 Derived values

Derived values are recalculated through registered rules profiles or canonical derivation rules. UI code must not maintain competing formulas.

## 10.5 Biography and appearance

Biography, portrait, visual customization, and descriptive appearance should be stored separately from mechanical projections so cosmetic edits do not trigger unnecessary rules migrations.

## 10.6 Visibility

Character information may be:

- public to the campaign;
- visible to the party;
- visible only to the owning player and GM;
- GM-only;
- private draft material.

Visibility must be enforced at service and authoritative-session boundaries, not only hidden in the UI.

**Status:** Canonical domain responsibility; complete UI and storage implementation remains phased.

---

# 11. Progression and Advancement

## 11.1 Event-based progression

Progression is recorded as advancement events rather than only as overwritten final values.

An advancement event should record:

- character identity;
- before-state fingerprint;
- selected option;
- cost;
- evaluated prerequisites;
- grants and removals;
- substitutions;
- exclusions;
- rules profile;
- source content;
- resulting state;
- adjudication;
- timestamp and actor;
- schema and engine version.

## 11.2 Rebuild requirement

Replaying valid advancement history under the appropriate compatible rules must recreate the expected projection or raise a migration discrepancy.

## 11.3 Progression graphs

Ability trees and other progression structures use:

- stable node IDs;
- tier, rank, or stage;
- explicit prerequisites;
- explicit grants;
- exclusions;
- replacement rules;
- scaling profiles;
- respec policy;
- source provenance.

## 11.4 Duplicate grants

Duplicate grants are rejected unless the governing rule defines:

- stacking;
- conversion;
- replacement;
- increased rank;
- alternate benefit.

The reason for the accepted duplicate behavior must be visible.

## 11.5 Respec and reversal

Progression is reversible only when allowed by:

- the progression’s governing rule;
- a campaign rule;
- a recorded GM adjudication;
- a migration operation.

Reversal preserves the original event and creates a compensating event or governed replacement history.

## 11.6 Entitlement boundary

Entitlement controls access to select or use content; it does not rewrite canonical ability identities.

The approved free-access policy limits ability trees to their first two tiers, including abilities received through grants. Campaign grants and sponsored access are entitlement policies, not duplicate ability definitions.

## 11.7 Unavailable historical content

If a pack is removed, access expires, or content is deprecated, historical selections remain preserved. Their current active behavior follows compatibility, entitlement, and campaign policy rather than deletion.

**Status:** Canonical; entitlement service port is implemented at the P9-06 contract level, while full character progression UI is later work.

---

# 12. Actions

## 12.1 Definition

An action is a versioned executable object representing an intentional operation.

## 12.2 Required contract

An action may define:

- stable identity and version;
- labels and presentation;
- actor constraints;
- target constraints;
- timing and phase;
- permissions;
- prerequisites;
- costs;
- roll or deterministic resolution;
- ordered modifiers;
- effect branches;
- reactions and interrupts;
- failure behavior;
- visibility;
- source provenance;
- compatibility.

## 12.3 Shared action model

Domain-specific actions extend the common action contract. Combat attacks, social maneuvers, investigation operations, crafting steps, vehicle actions, and environmental interactions must not become incompatible execution engines.

## 12.4 Consolidated identities

Where Phase 8 consolidated duplicate actions, implementations must use canonical records, aliases, parameterization, or validated extensions. Importers must not recreate superseded duplicate canon.

## 12.5 Proposal and approval

In authoritative sessions, an action may enter a proposal workflow. The GM-facing approval item should provide enough context to adjudicate efficiently, including:

- action;
- actor;
- target;
- relevant ability or rule;
- roll result;
- modifiers;
- calculated outcomes;
- hidden-information constraints;
- allowed approval, denial, or alteration behavior.

**Status:** Canonical shared model; runtime and UI completion are phased.

---

# 13. Effects

## 13.1 Definition

An effect is the smallest governed outcome instruction emitted by a rule, action, condition, event, or adjudication.

## 13.2 Common effect families

- value change;
- resource spend or restoration;
- damage, healing, stress, or repair;
- condition application, refresh, suspension, expiration, or removal;
- movement or repositioning;
- ownership or inventory transfer;
- reveal or concealment;
- entity creation or removal;
- timer or duration change;
- relationship or reputation change;
- narrative or adjudication prompt.

## 13.3 Effect contract

An effect identifies:

- source;
- target;
- parameters;
- duration;
- stacking or replacement behavior;
- visibility;
- application preconditions;
- removal or dispel rules;
- rollback or compensation behavior where applicable.

## 13.4 Atomicity and compensation

Effects should apply atomically when practical. Multi-effect operations define ordering and failure behavior. If partial application cannot be avoided, the result must identify completed, failed, and compensating changes.

## 13.5 Provenance

Every applied effect remains traceable to its originating action, rule, condition, item, ability, environment, or adjudication.

**Status:** Canonical shared mechanic family.

---

# 14. Conditions and Statuses

## 14.1 Definition

A condition is a named ongoing state with a lifecycle and mechanical hooks. A label alone is not an executable condition.

## 14.2 Lifecycle

A condition may support:

1. apply;
2. refresh or stack;
3. suspend;
4. trigger or tick;
5. expire;
6. remove.

## 14.3 Required contract

A condition defines:

- stable identity;
- source and target;
- duration units;
- timing hooks;
- stacking policy;
- refresh behavior;
- modifiers and effects;
- immunities or resistances;
- suppression or suspension behavior;
- visibility;
- removal and expiration rules;
- provenance.

## 14.4 Status presentation

The UI may group or summarize conditions for readability but must not merge mechanically distinct states into one undocumented behavior.

## 14.5 Hidden conditions

Hidden information may restrict who can see a condition, but authoritative state and permitted GM views must retain it.

**Status:** Canonical shared mechanic family.

---

# 15. Resources

## 15.1 Definition

A resource is a governed quantity, pool, charge, slot, capacity, timer, or operational value used by rules.

## 15.2 Examples

Resources may include:

- health or integrity;
- stress;
- action capacity;
- charges;
- ammunition;
- fuel;
- heat;
- energy;
- currency;
- project progress;
- recovery capacity;
- countdown timers;
- inventory capacity.

The example list is not exhaustive.

## 15.3 Required contract

A resource defines:

- owner;
- units;
- minimum and maximum;
- current value;
- spend and restore permissions;
- recovery rules;
- overflow and underflow behavior;
- visibility;
- event hooks;
- source and provenance;
- version compatibility.

## 15.4 Canonical state

A UI counter without a governed resource definition is not canonical state.

## 15.5 Transactions

Resource changes are emitted as traceable effects or events. Spending should not be hidden inside unrelated UI behavior.

**Status:** Canonical shared mechanic family.

---

# 16. Modifiers, Ordering, and Stacking

## 16.1 Purpose

Ensure that multiple rules produce deterministic results across domains.

## 16.2 Modifier contract

A modifier identifies:

- source;
- affected value or operation;
- scope;
- priority;
- stacking group;
- operation type;
- duration;
- prerequisites;
- visibility;
- provenance.

## 16.3 Operation types

A modifier may:

- add;
- multiply;
- replace;
- cap;
- floor;
- suppress;
- select highest;
- select lowest;
- substitute;
- redirect.

## 16.4 Ordering

The runtime applies explicit ordering. Simultaneous or tied effects use a declared tie-breaking rule or recorded GM adjudication.

## 16.5 No hidden UI math

Presentation layers may preview calculations but may not maintain a separate modifier engine.

**Status:** Canonical shared rule behavior.

---

# 17. Abilities, Powers, and Capability Domains

## 17.1 Ability model

An ability is a governed capability record. It may grant:

- actions or reactions;
- passive modifiers;
- effects;
- conditions;
- resources;
- proficiencies;
- senses;
- movement modes;
- transformations;
- crafting access;
- other typed capabilities.

## 17.2 Required ability fields

An ability may define:

- domain;
- source;
- prerequisites;
- tier or rank;
- costs;
- timing;
- targets;
- rules profile;
- grants;
- exclusions;
- scaling;
- presentation;
- provenance;
- compatibility.

## 17.3 Domains

A domain classifies capabilities and may add validated extensions. A domain is not permission to create a separate incompatible action or resolution engine.

## 17.4 Grants and wrappers

Species, forms, environments, items, conditions, creatures, vehicles, templates, and campaign rules may grant abilities.

A grant records:

- source;
- reason;
- duration;
- activation state;
- replacement or stacking behavior.

A wrapper may adapt presentation or parameters while preserving the underlying canonical identity unless it defines a genuinely distinct ability.

## 17.5 Coverage

Ability coverage must include capabilities embedded outside traditional ability sections, including:

- environmental adaptations;
- species traits;
- creature actions;
- item abilities;
- vehicle, mecha, and spacecraft systems;
- setting-specific capabilities.

## 17.6 Incomplete abilities

Incomplete records remain marked and may be quarantined or non-playable. AI must not silently complete them as canon.

## 17.7 AI boundary

AI may search, explain, compare, and propose builds using accessible records. It must preserve source references, disclose uncertainty, and may not create canonical abilities without approval.

**Status:** Canonical cross-domain model.

---


# 18. Combat

## 18.1 Purpose

Define combat as a structured scene that uses the same canonical actors, actions, effects, conditions, resources, permissions, provenance, and event history as the rest of the game.

Combat is not a separate application or incompatible rules engine. It is one high-pressure mode of the shared Multiversal runtime.

## 18.2 Combat scene state

A combat scene may include:

- participants and sides;
- encounter objectives;
- turn, phase, initiative, or other timing state where required;
- maps, zones, ranges, or theater-of-the-mind positioning;
- visibility and hidden information;
- movement and reach;
- defenses and protective states;
- resources and action capacity;
- ongoing effects and conditions;
- terrain, cover, atmosphere, gravity, hazards, traps, and environmental exposure;
- vehicles, mecha, starships, mounts, structures, and other operational assets;
- pause, checkpoint, reconnect, and recovery state.

A rules profile may select a specific timing or positioning method without redefining the common action and effect contracts.

## 18.3 Action lifecycle in combat

A combat operation follows the shared declaration, validation, resolution, adjudication, and application stages.

The minimum authoritative flow is:

1. The actor selects or proposes an action.
2. The proposal identifies the actor, action, target or targets, declared parameters, costs, and relevant rules.
3. Validation checks timing, permissions, availability, prerequisites, targeting, range or reach, visibility, environment, and resources.
4. The system records or resolves rolls and deterministic calculations.
5. Ordered modifiers, substitutions, reactions, interrupts, prevention, mitigation, and conditional branches are processed.
6. The GM receives the required approval or adjudication view.
7. The GM approves, denies, or explicitly alters the calculated result when the campaign workflow permits.
8. Accepted effects are applied and logged.
9. The authoritative projection is updated and synchronized to each participant according to visibility permissions.

## 18.4 GM approval view

The GM-facing approval item should make adjudication fast without hiding the calculation.

It should show, as permitted:

- acting entity and controller;
- selected action or ability;
- accessible rule summary with a direct path to the full rule;
- target or targets;
- declared costs and substitutions;
- roll result or deterministic inputs;
- applied modifiers and their sources;
- reactions or interruptions;
- calculated effects and affected values;
- hidden-information warnings;
- validation warnings;
- available approve, deny, and alter controls.

The same inspectability applies when the GM controls enemies and NPCs. GM-controlled actions still become attributable authoritative events.

## 18.5 Altered outcomes

An alteration must preserve:

- the original calculated result;
- fields changed by the GM;
- the final accepted result;
- the adjudicator;
- a reason or note when provided;
- the event and rules versions.

The application must not overwrite the calculation so completely that later review cannot distinguish the original result from the adjudicated one.

## 18.6 Player information

Players do not need the complete action log visible by default. They may access the history they are permitted to see.

A player-facing outcome should provide enough information to understand:

- what their character attempted;
- what result was accepted;
- which visible conditions, resources, positions, or assets changed;
- what choices or reactions remain available.

GM-only statistics, secrets, enemy knowledge, and unrevealed effects remain permission-scoped.

## 18.7 Positioning

Multiversal must support:

- maps and coordinates;
- zones or areas;
- range bands;
- theater of the mind;
- mixed positioning.

Coordinates are projections used by a scene or tool. They are not mandatory identity fields for characters, creatures, assets, or locations.

## 18.8 Participants

Combat participants may include:

- player characters;
- NPCs and creatures;
- groups or swarms;
- vehicles;
- mecha;
- starships;
- structures;
- traps;
- hazards;
- environmental processes.

All participants use shared entity references. Domain-specific extensions may add typed state without duplicating the core character, item, action, or effect models.

## 18.9 Damage, mitigation, and recovery

Damage and related harm are effect families governed by rules profiles and content. The Bible does not invent a single universal damage table.

The runtime must preserve the distinction between:

- incoming effect;
- prevention;
- resistance;
- mitigation;
- redirection;
- final applied harm;
- resulting conditions or thresholds;
- later healing, repair, recovery, or restoration.

## 18.10 Encounter objectives

Combat need not end only when one side is destroyed. Objectives may include:

- escape;
- rescue;
- capture;
- survival;
- delay;
- control of a location;
- protection of an asset;
- retrieval;
- negotiation;
- disabling a system;
- completing a ritual;
- transition to another scene mode.

Objectives and completion events should be explicit where authored.

## 18.11 Recovery and audit

Combat state must support:

- checkpointing;
- disconnect and reconnect;
- pause and resume;
- duplicate-operation protection;
- stale-client rejection or reconciliation;
- authoritative event review;
- backup and restore compatibility.

## 18.12 AI boundary

AI may:

- explain visible rules;
- summarize combat state;
- identify legal options;
- propose tactics;
- assist the GM with encounter management.

AI must not:

- expose hidden enemy information to players;
- invent unobserved statistics;
- silently select character actions;
- convert suggestions into accepted state changes without authority;
- replace GM adjudication.

## 18.13 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/combat.md`
- Cross-domain Actions, Effects, Conditions, and Resources consolidation
- Creature action and behavior packages
- Encounter integration packages
- Operational asset and environment packages
- Authoritative-session and UI workflow decisions

**Status:** Canonical game and workflow architecture; detailed formulas and content remain governed by their profiles and packs.

---

# 19. Social Play

## 19.1 Purpose

Treat social interaction as a first-class scene and rules domain rather than unstructured dialogue or a single persuasion statistic.

## 19.2 Social scene model

A social scene may include:

- participants and roles;
- relationships;
- organizations and factions;
- goals and opposing goals;
- leverage;
- attitudes;
- trust;
- reputation;
- obligations;
- promises, favors, and debts;
- secrets and hidden motives;
- stakes;
- time pressure;
- public and private knowledge;
- temporary scene state;
- consequences and follow-on scenes.

Narrative choices remain human decisions. Mechanical social operations use the shared action, effect, condition, resource, modifier, and adjudication contracts.

## 19.3 Layered social state

Social state must not be flattened into one universal score.

Relevant layers may include:

- personal identity, values, and motives;
- relationship edges between specific entities;
- role within an organization;
- faction standing;
- public reputation;
- private attitude;
- temporary emotional or situational state;
- promises, obligations, favors, and debts;
- knowledge and secrets;
- campaign-specific adjudications.

A faction reputation does not automatically equal every member’s personal attitude. A personal relationship does not automatically modify an entire culture or organization.

## 19.4 Influence actions

An influence action should identify:

- actor;
- target;
- approach;
- desired outcome;
- stakes;
- leverage or offered consideration;
- prerequisites;
- costs;
- target defenses or thresholds;
- possible outcomes;
- visibility;
- time horizon.

Content and rules profiles may define different social approaches, defenses, currencies, and degrees of success. The Bible does not replace them with a single universal formula.

## 19.5 Social outcomes

A social scene may end through:

- agreement;
- refusal;
- compromise;
- delay;
- obligation;
- exchange;
- revelation;
- deception;
- escalation;
- relationship change;
- reputation change;
- transition to investigation, exploration, downtime, or combat.

Mechanical consequences should be applied as attributable effects or events rather than buried only in notes.

## 19.6 Relationship edges

A relationship is a typed, attributable connection between entities.

A relationship edge may include:

- source entity;
- target entity;
- relationship type;
- directionality;
- strength or tier where governed;
- trust, hostility, obligation, or other typed dimensions;
- public and hidden facets;
- source events;
- duration;
- campaign scope;
- GM notes;
- visibility.

Relationship history should be preserved rather than represented only by an overwritten current number.

## 19.7 Promises, favors, and debts

Promises, favors, debts, obligations, and similar social assets should record:

- parties;
- terms;
- source event;
- due conditions;
- value or weight where governed;
- visibility;
- fulfillment, transfer, breach, forgiveness, or expiration.

They are not ordinary currencies unless a rules profile explicitly models them that way.

## 19.8 GM information

Motives, hidden thresholds, secrets, deceptions, and unrevealed relationship facts are permission-scoped. Search, exports, AI context, notifications, and synchronization must respect the same boundaries.

## 19.9 Dialogue and transcripts

Dialogue notes and transcripts are separate from mechanical consequences.

They may link to:

- scene events;
- relationship changes;
- promises;
- clues;
- adjudications.

A transcript does not become canonical lore merely because it was recorded. Campaign events become authoritative through the campaign’s accepted state and GM authority.

## 19.10 AI boundary

AI may:

- summarize visible relationship context;
- suggest questions or approaches;
- propose dialogue prompts;
- help the GM track obligations and consequences.

AI must not:

- reveal hidden motives or secrets;
- decide a canonical NPC response without authority;
- create permanent lore silently;
- convert generated dialogue into accepted mechanical consequences without approval.

## 19.11 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/social-play.md`
- NPC archetype, social-role, relationship, and faction packages
- Faction and culture packages
- Cross-domain mechanics consolidation
- Approved social-workspace and relationship-tracker direction

**Status:** Canonical architecture; individual social formulas remain content- and rules-profile-specific.

---

# 20. Investigation

## 20.1 Purpose

Define investigations so mysteries remain playable, permission-safe, auditable, and compatible with many adventure structures.

## 20.2 Investigation objects

An investigation may use:

- scenes;
- questions;
- leads;
- clues;
- evidence;
- sources;
- subjects;
- locations;
- timelines;
- hypotheses;
- relationships;
- revelations;
- conclusions;
- complications.

## 20.3 Information classification

Investigation data must preserve distinctions among:

- canonical fact;
- evidence;
- authored interpretation;
- rumor;
- deception;
- unreliable evidence;
- player note;
- player hypothesis;
- unresolved information;
- GM-only answer or explanation.

These categories must not be flattened into a generic fact record.

## 20.4 Clue contract

A clue may define:

- stable identity;
- source and provenance;
- acquisition conditions;
- discoverable portions;
- reliability or ambiguity where authored;
- visibility;
- links to entities, locations, scenes, or events;
- consequences;
- escalation or follow-up leads;
- false or deceptive characteristics;
- rules for automatic or GM-mediated revelation.

## 20.5 Discovery event

When information is discovered, the system should record:

- what was discovered;
- which portion became visible;
- discovering actor or party;
- method;
- source scene or action;
- time;
- validation or roll result;
- GM adjustment;
- recipients;
- related clues or leads.

The canonical clue remains distinct from the party’s current knowledge projection.

## 20.6 Investigation actions

Investigation operations may include:

- search;
- analyze;
- recall;
- interview;
- research;
- surveil;
- compare;
- decode;
- reconstruct;
- test;
- trace;
- observe;
- preserve evidence.

They use the shared action model but may produce:

- partial information;
- graded confidence;
- time or resource costs;
- complications;
- new questions;
- false confidence;
- a GM prompt;
- no immediate revelation.

## 20.7 Nonlinear structure

The application must allow clue networks and multiple successful approaches. It must not require every mystery to be a single linear chain.

A failed check should not automatically create a dead end unless the authored rules or adventure explicitly require that consequence.

## 20.8 Player workspace

Player-authored tools may include:

- notes;
- pins;
- theories;
- timelines;
- evidence boards;
- relationship diagrams;
- tags and collections.

These overlays may reference canonical entities but do not change canon. Private player notes must remain private unless shared.

## 20.9 GM workspace

The GM may:

- prepare clues and revelation conditions;
- connect scenes, subjects, and sources;
- release selected information;
- correct visibility;
- record adjudications;
- view hidden answer structures;
- track what each participant knows.

The application must prevent hidden answers, clues, and GM notes from leaking through search, synchronization, exports, AI context, notifications, or client caches.

## 20.10 AI boundary

AI may:

- organize already-visible evidence;
- summarize a visible timeline;
- identify contradictions in player-visible information;
- suggest questions or research directions.

AI must not:

- access GM-only data for a player;
- declare a player hypothesis true;
- add canonical clues without explicit acceptance;
- erase uncertainty authored into evidence.

## 20.11 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/investigation.md`
- NPC, relationship, setting, location, and lore packages
- Shared mechanics consolidation
- Approved investigation workspace planning

**Status:** Canonical architecture; detailed clue schemas and revelation rules remain governed by canonical content packages.

---

# 21. Exploration and Environments

## 21.1 Purpose

Connect travel, locations, discovery, environmental exposure, hazards, and adaptation across worlds, realities, regions, settlements, sites, and scenes.

## 21.2 Spatial and setting hierarchy

A setting pack may cover a world, city, region, realm, station, facility, or another bounded context.

Relationships may include:

- world to reality;
- reality to branch;
- region to parent region;
- settlement to region;
- site to settlement or region;
- scene to location;
- adjacency;
- route;
- portal;
- transit network;
- overlapping or alternate layers.

A pack need not contain an entire world. Its scope and parent references must be explicit.

## 21.3 Location identity

Locations use stable identity. Map coordinates are optional projections rather than mandatory identity.

A location may have:

- canonical parent relationships;
- multiple maps;
- alternate scales;
- historical states;
- discovered and undiscovered projections;
- portals or non-Euclidean connections;
- campaign-specific changes.

## 21.4 Environment record

An environment may define:

- terrain;
- climate;
- gravity;
- atmosphere;
- pressure;
- temperature;
- light;
- radiation;
- corruption;
- supernatural influence;
- hazards;
- movement constraints;
- visibility;
- resources;
- encounter profiles;
- adaptation requirements;
- recovery or shelter conditions.

Environmental abilities and adaptations are governed mechanical records, not descriptive prose alone.

## 21.5 Exploration state

Exploration may track:

- route;
- pace;
- time;
- watches or shifts;
- supplies;
- vehicle, mount, or asset state;
- exposure;
- party formation;
- navigation uncertainty;
- discovered locations;
- hazards;
- encounters;
- weather or environmental change;
- objectives.

Detailed travel and abstract transitions are both valid when controlled by explicit rules profiles.

## 21.6 Adaptation evaluation

Environmental evaluation should consider:

- species traits;
- body forms;
- environmental adaptations;
- equipment;
- vehicles or shelters;
- abilities;
- conditions;
- temporary protections;
- campaign rules.

The environment references required capabilities or effects. It does not duplicate each possible adaptation into the environment record.

## 21.7 Environmental effects

Environment effects use shared:

- conditions;
- resources;
- modifiers;
- actions;
- effects;
- timers.

Environmental changes must identify their source and timing.

## 21.8 Maps and discovery

GM-only layers, hidden locations, undiscovered routes, traps, and secret portals remain permission-scoped.

Discovery events may reveal:

- a location;
- a route;
- a name;
- a map region;
- a hazard;
- a resource;
- a historical fact;
- a portal;
- an encounter possibility.

## 21.9 Travel outcomes

Travel may produce:

- time passage;
- resource costs;
- exposure;
- encounters;
- discoveries;
- complications;
- damage or repair requirements;
- downtime transitions;
- scene creation;
- campaign events.

## 21.10 Caching and invalidation

Environment evaluations may be cached, but must be invalidated when relevant state changes, including:

- participant;
- species or form;
- equipment;
- vehicle;
- condition;
- ability;
- location;
- environment;
- campaign rule.

## 21.11 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/exploration-and-environments.md`
- Adaptation packages
- Setting, world, region, settlement, location, and environment packages
- Operational asset packages
- Cross-domain mechanics consolidation

**Status:** Canonical architecture.

---

# 22. Downtime and Projects

## 22.1 Purpose

Define long-running activities outside moment-to-moment scenes while preserving campaign time, asset commitments, provenance, and shared runtime behavior.

## 22.2 Project aggregate

A project is a durable governed activity with:

- stable identity;
- owner and participants;
- objective;
- phases, tasks, or milestones;
- prerequisites;
- inputs;
- assigned assets;
- required time;
- location or facility requirements;
- actions, checks, or decisions;
- progress;
- complications;
- outputs;
- pause, transfer, abandonment, cancellation, and completion rules;
- provenance;
- visibility.

## 22.3 Project examples

Projects may represent:

- training;
- research;
- recovery;
- construction;
- repair;
- crafting;
- business;
- travel preparation;
- relationship work;
- ritual preparation;
- campaign-specific long actions.

Examples do not create mandatory universal project types.

## 22.4 Proposal and commitment

A project proposal is distinct from a committed project.

Before commitment, validation should evaluate:

- participants;
- time availability;
- facilities;
- assets;
- resources;
- prerequisites;
- campaign permission;
- conflicting commitments.

Commitment reserves or consumes inputs according to the governing rule.

## 22.5 Time and availability

Downtime uses explicit campaign time.

The system must prevent double commitment of:

- a character;
- a unique tool;
- a facility;
- a vehicle;
- another exclusive asset;

unless the applicable rule permits concurrent use.

Rules profiles may support abstract time blocks or detailed schedules.

## 22.6 Project events

The project history should record:

- commitment;
- assigned participants;
- input reservations or expenditures;
- progress;
- rolls;
- decisions;
- complications;
- participant changes;
- pauses;
- transfers;
- cancellations;
- completions;
- GM adjustments;
- outputs.

A project must not be reduced to one countdown field when its rules require recoverable state and history.

## 22.7 Outputs

Project outputs are applied through normal canonical events, such as:

- character advancement;
- item creation;
- item repair;
- relationship change;
- resource change;
- setting change;
- clue discovery;
- new content instance;
- campaign event.

## 22.8 Partial completion and abandonment

The governing rule defines what happens to:

- consumed inputs;
- reserved inputs;
- partial progress;
- created by-products;
- complications;
- learned information;
- transferable work.

The runtime must not guess a universal refund policy.

## 22.9 AI boundary

AI may help:

- summarize project state;
- identify missing prerequisites;
- propose schedules;
- estimate visible risks;
- generate a reversible plan.

Automated real-time reminders, marketplace scheduling, and autonomous project management are not implicitly authorized merely because a project object exists.

## 22.10 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/downtime-and-projects.md`
- Crafting and economy packages
- Operational asset repair packages
- Shared resources, timers, and progression packages

**Status:** Canonical architecture; specialized project rules remain content-specific.

---

# 23. Crafting and Economy

## 23.1 Purpose

Connect materials, recipes, production, trade, ownership, custody, containers, stacking, and economic context without imposing a single currency or universal price table.

## 23.2 Material and item foundations

Relevant content may include:

- materials;
- components;
- food;
- trade goods;
- tools;
- consumables;
- medicine;
- weapons;
- armor;
- technology;
- magic items;
- software;
- facilities;
- vehicles and operational assets.

Where relevant, records define:

- units;
- quantity;
- quality;
- condition;
- provenance;
- legality;
- perishability;
- compatibility;
- ownership;
- custody;
- stack behavior.

## 23.3 Recipes and production rules

A recipe or production rule should identify:

- output;
- output quantity;
- permitted alternatives;
- required inputs;
- tools;
- facilities;
- knowledge;
- skills or abilities;
- time;
- actions or checks;
- quality rules;
- by-products;
- failure and complication behavior;
- provenance.

The engine must not infer a canonical recipe solely from item names or generated similarity.

## 23.4 Crafting duration

Crafting may execute as:

- an immediate or scene-scale action;
- a multi-step action sequence;
- a downtime project.

The governing recipe or rules profile determines the mode.

## 23.5 Quality and condition

Quality, condition, modification history, serial identity, provenance, or ownership may require a unique item instance.

Items should stack only when their stack keys and mutable properties are compatible.

## 23.6 Economic models

A setting may use:

- currency;
- barter;
- abstract wealth;
- favors;
- requisition;
- availability;
- legality;
- scarcity;
- reputation;
- setting-specific exchange systems.

Values are contextual offers, references, or governed calculations. They are not immutable universal truth unless a canonical rule explicitly defines them.

## 23.7 Transactions

A transaction should record:

- parties;
- offered assets;
- requested assets;
- quantities and units;
- valuation context;
- taxes or fees where authored;
- permissions;
- ownership and custody changes;
- final acceptance;
- failure or cancellation;
- provenance.

Transactions must be protected against replay, partial duplication, and stale-state acceptance.

## 23.8 Ownership, custody, and use

The system must distinguish:

- ownership;
- possession;
- storage location;
- custody;
- authorized use;
- control during a scene;
- entitlement to the content definition.

A shared vehicle or facility may have multiple owners, custodians, and authorized users.

Subscription or content entitlement is not the same as in-world ownership.

## 23.9 Containers

A container may define:

- capacity;
- allowed contents;
- nesting rules;
- access permissions;
- mass, volume, slot, or abstract capacity;
- overflow behavior;
- spill or loss behavior;
- location;
- ownership and custody.

## 23.10 Market adjudication

The GM may adjudicate availability, offers, scarcity, legality, and market response without rewriting the canonical base item record.

Campaign-specific prices and transactions become campaign events or overlays, not global changes to the item definition.

## 23.11 AI boundary

AI may:

- search known recipes;
- compare visible costs;
- identify missing components;
- propose production plans;
- summarize inventory implications.

AI must not:

- invent canonical recipes;
- create assets through text alone;
- bypass ownership or entitlement;
- silently establish a universal market value.

## 23.12 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/crafting-and-economy.md`
- Phase 8 item, material, component, recipe, trade, ownership, stacking, and container packages
- Operational asset packages
- Shared resources and mechanics consolidation

**Status:** Canonical architecture; world-specific currencies, recipes, markets, and prices remain content authority.



# 24. Items, Vehicles, Mecha, and Starships

## 24.1 Purpose

Define personal equipment and larger operational assets through shared identity, ownership, custody, component, inventory, action, effect, resource, condition, and project models while preserving specialized domain rules.

## 24.2 Common asset principles

Items and operational assets are canonical definitions or campaign instances with stable identity and provenance.

The model must distinguish:

- content definition from owned instance;
- ownership from custody;
- custody from authorized use;
- authorized use from current control;
- in-world ownership from content entitlement;
- base definition from modification history;
- destruction from deletion;
- temporary assignment from permanent transfer.

A record may participate in inventories, scenes, projects, transactions, encounters, and exports without changing identity.

## 24.3 Items

Items may include:

- weapons;
- armor;
- shields and protective equipment;
- tools;
- consumables;
- medicine;
- technology;
- magical items;
- software;
- materials;
- components;
- food;
- trade goods;
- containers;
- setting-specific objects.

An item definition or typed extension may provide:

- classification;
- physical properties;
- quantity and units;
- equip and use requirements;
- actions, reactions, effects, or grants;
- charges and resources;
- compatible components and modifications;
- stacking behavior;
- condition and durability;
- value references;
- legality and availability;
- images and presentation;
- source and provenance.

## 24.4 Definition and instance separation

A canonical item definition describes the type. An item instance describes a specific in-world object.

An instance may add:

- unique identity;
- owner;
- custodian;
- location or container;
- quantity;
- current condition;
- current charges;
- modifications;
- serial or maker information;
- acquired history;
- campaign-specific notes;
- visibility;
- loss, destruction, salvage, or recovery state.

Identical definitions do not require identical instances when mutable state differs.

## 24.5 Stacking

Items may stack only when the governing stack key and mutable state are compatible.

Relevant distinctions may include:

- definition and version;
- quality;
- condition;
- charges;
- modifications;
- ownership;
- legality;
- provenance;
- expiration;
- custom name;
- hidden information.

A transfer or split must preserve total quantity and may not duplicate contained or attached assets.

## 24.6 Equipment and loadouts

Equipping an item is an explicit state change governed by:

- compatible slot or body location;
- form and scale;
- prerequisites;
- ownership or use permission;
- current condition;
- conflicting equipment;
- campaign rules.

Loadouts are reusable selections or projections. They do not create duplicate item instances.

## 24.7 Components and modifications

A component or modification relationship should identify:

- host;
- component;
- attachment point or slot;
- compatibility rule;
- dependency;
- granted capabilities;
- resource or capacity impact;
- installation and removal requirements;
- modification history;
- provenance.

Compatibility graphs must be validated. Cycles or unresolved dependencies must produce explicit failures.

## 24.8 Containers and nested inventory

A container may contain items or other containers where permitted.

The inventory system must:

- enforce capacity and content restrictions;
- prevent unbounded or self-containing cycles;
- preserve owner and custodian relationships;
- avoid duplication during move, split, merge, import, restore, and synchronization;
- define behavior when a container is destroyed, inaccessible, transferred, or removed.

## 24.9 Operational assets

Vehicles, mecha, ships, starships, and bases are durable operational assets.

An operational asset may define:

- frame, chassis, hull, structure, or base;
- scale;
- components and subsystems;
- stations and roles;
- occupants and crew;
- movement and handling;
- cargo;
- power, fuel, heat, ammunition, atmosphere, or other resources;
- integrity and subsystem condition;
- sensors;
- communications;
- defenses;
- weapons and tools;
- repair requirements;
- ownership, custody, access, and operational state;
- source and provenance.

Operational assets participate in shared scenes and resolutions rather than living in a disconnected asset-only runtime.

## 24.10 Vehicles

Vehicle rules may cover:

- frame;
- movement modes;
- handling;
- acceleration or maneuver profiles;
- occupancy;
- cargo;
- collisions;
- mounted systems;
- exposure of occupants;
- terrain or environment compatibility.

A vehicle may be a personal possession, shared party asset, NPC asset, organizational asset, location-linked asset, or setting entity.

## 24.11 Mecha

Mecha may add:

- pilot link;
- frame and part architecture;
- heat;
- energy;
- localized or subsystem damage;
- repair and refit;
- ejection;
- pilot compatibility;
- transformation or mode state.

Pilot and machine state remain separate.

Every effect must identify whether it targets:

- pilot;
- occupant;
- frame;
- component;
- subsystem;
- cargo;
- shared system;
- external target.

## 24.12 Ships and starships

Ships may use:

- crew stations;
- scale;
- internal environments;
- navigation;
- sensors;
- cargo and hangars;
- power;
- propulsion;
- damage control;
- travel systems;
- life support;
- communications;
- boarding and occupant state.

The architecture must support sailing vessels, aircraft, spacecraft, dimensional craft, and setting-specific vessels through rules profiles and extensions without pretending that all vessels use identical mechanics.

## 24.13 Crew stations and command authority

An asset station or role should define:

- permitted controllers;
- available actions;
- associated systems;
- required proficiency;
- command priority;
- concurrency rules;
- visibility;
- substitution and vacancy behavior.

Concurrent or conflicting commands require a deterministic authority and conflict policy.

Ownership alone does not automatically grant authority to every station.

## 24.14 Asset actions

Asset actions use the shared action lifecycle.

An action should identify:

- asset;
- initiating actor or station;
- controller;
- targets;
- costs;
- relevant subsystem;
- environment;
- roll or deterministic profile;
- effects;
- GM approval or adjudication;
- resulting asset and occupant changes.

## 24.15 Damage and subsystem state

Damage may target:

- overall integrity;
- localized section;
- component;
- subsystem;
- occupant;
- cargo;
- environment;
- linked asset.

The model must preserve incoming effect, mitigation, final applied harm, resulting conditions, and disabled or degraded functions.

A disabled component remains identifiable and repairable. It is not deleted from the asset definition or instance.

## 24.16 Maintenance, repair, and refit

Repairs and modifications are actions or projects that may require:

- tools;
- components;
- materials;
- facilities;
- time;
- skills or abilities;
- checks;
- permissions.

The resulting event history records consumed inputs, restored state, replaced components, new capabilities, and remaining defects.

## 24.17 Destruction, abandonment, salvage, and recovery

These are explicit lifecycle transitions.

### Destruction

The asset ceases normal operation but may still leave wreckage, evidence, cargo, recoverable components, or campaign consequences.

### Abandonment

Control or custody is relinquished without erasing the asset.

### Salvage

Governed outputs are recovered from a damaged, abandoned, or destroyed asset.

### Recovery

The asset returns to controlled or operational state through a governed action, project, import, or restore.

Deleting a record is not a valid substitute for any of these transitions.

## 24.18 Shared ownership and use

Shared assets may have:

- multiple owners;
- a custodian;
- assigned operators;
- station-specific controllers;
- passengers;
- borrowers;
- maintenance responsibility;
- resource responsibility.

Transfer, loan, assignment, revocation, and inheritance must preserve event history and prevent duplication.

## 24.19 Scale

Personal, vehicle, mecha, ship, and larger encounters may use different rules profiles.

Scale affects resolution through explicit rules and modifiers. It does not require separate databases or incompatible action models.

## 24.20 Asset images and presentation

Images, portraits, diagrams, maps, and tokens are referenced through the governed asset pipeline.

Alternate art retains:

- asset identity;
- license;
- provenance;
- variant or theme;
- suitability for portrait, token, map, or reference use.

Large media must not be embedded repeatedly into each object record.

## 24.21 AI boundary

AI may:

- compare visible specifications;
- suggest compatible loadouts;
- identify missing parts or resources;
- summarize damage and repair options;
- propose a route, crew assignment, or refit plan.

AI must not:

- create ownership;
- transfer assets;
- consume resources;
- install components;
- resolve commands;
- expose hidden cargo or systems;
- invent canonical compatibility;

without the required authority and accepted state change.

## 24.22 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/items-vehicles-mecha-and-starships.md`
- Phase 8E-003A–G item and inventory packages
- Phase 8E-005A–G operational asset packages
- 8E-005B vehicle packages
- 8E-005C-R1 mecha packages
- Phase 8E-007 shared-mechanics consolidation
- Phase 8E-008 final validation

**Status:** Canonical domain architecture; individual equipment and operational-asset rules remain governed by their records and rules profiles.

---

# 25. Creatures, NPCs, Species, and Forms

## 25.1 Purpose

Define the related but distinct models for species, subspecies, forms, adaptations, creatures, archetypes, NPCs, templates, variants, and campaign instances.

## 25.2 Separation of concepts

The system must preserve the distinction among:

- species;
- subspecies or lineage;
- body form;
- adaptation;
- creature type;
- creature definition;
- NPC archetype;
- template;
- variant;
- individual character or creature instance;
- campaign-specific NPC.

These concepts may reference one another but must not be collapsed into one generic stat block.

## 25.3 Species

A species record may define:

- identity;
- taxonomy;
- physical and biological traits;
- senses;
- movement;
- environmental tolerances;
- scale;
- lifespan or development information where authored;
- forms or subspecies;
- adaptations;
- default grants;
- optional grants;
- compatibility constraints;
- setting and lore links;
- provenance.

Species mechanics are grants and references to shared records. They must not rely on duplicated free-form mechanics copied directly into every character.

## 25.4 Species choice layers

Character creation must distinguish:

- fixed species traits;
- selected traits;
- optional alternatives;
- subspecies or lineage choices;
- form choices;
- adaptations;
- campaign restrictions;
- setting restrictions;
- substitutions;
- grants from other sources.

The validation result should explain which source provided each choice and why it is legal or blocked.

## 25.5 Forms and transformations

A form is a governed body or state configuration.

A form may change:

- scale;
- anatomy;
- movement;
- senses;
- environmental compatibility;
- equipment compatibility;
- attributes or derived values;
- abilities;
- actions;
- resources;
- conditions;
- presentation.

A transformation is an attributable state change with:

- source;
- target;
- entry requirements;
- cost;
- duration;
- retained state;
- replaced state;
- equipment behavior;
- exit or reversal rule;
- visibility;
- provenance.

The system must not silently merge the form’s traits into the base identity so that the original state cannot be recovered.

## 25.6 Environmental adaptations

Adaptations include capabilities that permit survival, movement, perception, resistance, or function in particular environments.

Adaptations may come from:

- species;
- form;
- ability;
- equipment;
- vehicle;
- condition;
- temporary effect;
- campaign rule.

Environment evaluation references these capabilities rather than duplicating their mechanics.

## 25.7 Creatures

A creature definition may include:

- taxonomy;
- scale;
- biology;
- movement;
- senses;
- defenses;
- resources;
- actions;
- reactions;
- traits;
- behavior guidance;
- encounter role;
- habitat;
- variants;
- harvest or loot references where authored;
- images;
- source and provenance.

A rendered stat block is a projection of the canonical creature, selected rules profile, applied templates, and current state.

## 25.8 Creature actions and abilities

Creature actions, reactions, and traits reference canonical shared mechanics.

A creature record must not create duplicate action or ability definitions merely because a stat block presents them inline.

Inline display text may summarize the referenced mechanic but does not become a competing authority.

## 25.9 Behavior guidance

Behavior guidance may describe:

- instincts;
- priorities;
- tactics;
- threat response;
- retreat behavior;
- communication;
- social tendencies;
- habitat behavior.

Guidance is advisory to the GM unless a rule explicitly automates a behavior.

AI-generated tactics are not canon and may not override GM control.

## 25.10 Encounter role

Encounter role may help:

- select creatures;
- compose encounters;
- identify likely behavior;
- test peer groups;
- present GM summaries.

It is not an automatic guarantee of balance or difficulty.

## 25.11 Variants and templates

A variant or template must retain:

- base identity;
- applied layer identity;
- changed fields;
- grants;
- removals;
- replacements;
- compatibility;
- provenance;
- version.

The system must be able to distinguish the base record from the resulting projection.

## 25.12 NPC archetypes

An NPC archetype is reusable content describing a role or pattern.

It may contain:

- social role;
- typical capabilities;
- motivations;
- behavior guidance;
- faction or profession associations;
- equipment suggestions;
- knowledge profile;
- presentation guidance.

An archetype is not a unique campaign person.

## 25.13 NPC instances

A campaign NPC may use species, creature, and archetype foundations while adding:

- unique identity;
- name and presentation;
- campaign role;
- motives;
- relationships;
- faction membership;
- reputation;
- knowledge;
- secrets;
- loadout;
- schedule or location context;
- current state;
- event history;
- GM notes;
- visibility.

Campaign events may cause the instance to diverge from the source archetype without rewriting the archetype.

## 25.14 Knowledge and partial identification

The system must support partial identification.

Different participants may know different portions of:

- name;
- species;
- abilities;
- motives;
- faction;
- health or condition;
- equipment;
- history;
- secrets;
- true form.

Search, AI context, export, notifications, and synchronization must respect these knowledge boundaries.

## 25.15 Creature and NPC inventories

Inventory and loadout relationships use canonical item instances and definitions.

Loot and harvest references are only authoritative when present in source or approved content. The application must not generate canonical loot solely from category assumptions.

## 25.16 Images and assets

Creature, species, form, and NPC images are referenced through the content-addressed asset pipeline.

Alternate portraits, tokens, silhouettes, anatomical references, and form art retain license and provenance metadata.

Images must not redefine hidden mechanical or lore facts.

## 25.17 Incomplete and conflicting source records

Incomplete or contradictory source creatures and NPCs remain tracked through:

- provenance;
- coverage status;
- conflict registers;
- missing-information registers;
- validation status.

The Bible and application must not fabricate missing statistics, actions, lore, taxonomy, or balance values and present them as canon.

## 25.18 AI boundary

AI may:

- summarize visible records;
- suggest encounter selections;
- compare variants;
- propose advisory behavior;
- assist with noncanonical draft NPCs;
- identify missing or conflicting fields.

AI must not:

- expose hidden NPC facts;
- invent canonical statistics;
- promote a generated variant;
- create a permanent campaign event;
- replace GM control;

without the appropriate review and accepted operation.

## 25.19 Controlling references

- DB-004 `DevelopmentBible/02-game-framework/creatures-npcs-and-species.md`
- Phase 8E-002A–C species and character-foundation packages
- Phase 8E-004A–G creature, NPC, hazard, and encounter packages
- Phase 8E-006 setting packages
- Phase 8E-007 cross-domain mechanics consolidation
- Phase 8E-008 final validation
- Source conflict, missing-information, and coverage registers

**Status:** Canonical domain architecture; incomplete source content remains explicitly incomplete.

---

# 26. Balance and Regression Philosophy

## 26.1 Purpose

Define how Multiversal evaluates mechanical behavior, detects regressions, identifies possible balance problems, and governs changes without converting automated findings into unreviewed canon.

## 26.2 Balance is not sameness

Balance does not require every ability, item, creature, progression, asset, or strategy to produce identical numerical output.

Evaluation must consider:

- role;
- tier or progression stage;
- cost;
- risk;
- action economy;
- range;
- duration;
- reliability;
- flexibility;
- prerequisites;
- opportunity cost;
- rarity;
- setting;
- encounter context;
- nonnumeric utility;
- intended asymmetry.

A meaningful comparison requires a declared peer group and evaluation model.

## 26.3 Source truth and balance observations

Canonical source values and balance observations are separate.

A test result may state that a record appears to be an outlier. It must not silently edit:

- source values;
- formulas;
- rules profiles;
- classifications;
- tiers;
- encounter roles;
- canonical definitions.

Balance changes require an approved, versioned correction or design decision.

## 26.4 Evidence classes

The project distinguishes different kinds of evidence.

Relevant forms include:

- exact formula or schema conformance;
- deterministic fixture and replay results;
- seeded simulation evidence;
- comparative peer-group metrics;
- human table observation.

Simulation evidence must not be presented as human playtest evidence.

A release that has no human playtesting must say so directly.

## 26.5 Golden corpus

The golden corpus preserves representative, deterministic expectations across domains.

It verifies behavior such as:

- identity;
- schema;
- provenance;
- relationships;
- rules profiles;
- actions;
- effects;
- conditions;
- resources;
- progression;
- creatures and encounters;
- items and economy;
- operational assets;
- installation;
- migration;
- uninstallation;
- deterministic replay.

Golden results protect known behavior. They do not prove that every protected value is perfectly balanced.

## 26.6 Deterministic randomness

Stochastic testing requires:

- declared random algorithm;
- algorithm version;
- root seed;
- derived stream identity;
- sample count;
- input fingerprint;
- retained outlier seeds;
- replay bundle;
- uncertainty method.

A failure must be reproducible from recorded evidence.

## 26.7 Peer groups

A peer group uses declared mandatory and optional dimensions.

Mandatory dimensions must not be broadened merely to obtain enough comparison records.

The approved evaluation model requires at least five eligible comparators.

If a valid peer group or target band does not exist, the result is **insufficient evidence**, not a silent pass or failure.

## 26.8 Review thresholds

Default peer-relative thresholds are review triggers rather than automatic canon judgments:

| Classification | Robust-Z threshold | Practical relative difference |
|---|---:|---:|
| Watch | at least 2.5 | at least 10% |
| Review required | at least 3.5 | at least 20% |
| Urgent review | at least 5.0 | at least 35% |

Both the statistical and practical thresholds must be met.

Provider- or domain-specific absolute target bands require owner approval and versioning.

## 26.9 Uncertainty

Stochastic observations use a declared 95% interval method.

Approved methods include profiles such as:

- seeded bootstrap intervals;
- Wilson intervals for proportions;
- exact conformance for deterministic formulas.

The uncertainty profile, seeds, resampling inputs, and retained outliers are part of the evidence.

## 26.10 Simulation profiles

The permanent harness may use multiple batch profiles, including:

- fast deterministic or smoke profiles;
- adaptive review profiles;
- confirmation profiles;
- legacy parity profiles.

The Phase 8B foundation used 200,000 trials per metric. The 8D-007 harness retained a `legacy-balance-parity-200000` profile for direct comparison while also supporting adaptive review batches.

## 26.11 Finding workflow

Unexpected findings follow a controlled workflow:

1. Intake.
2. Source and control-status triage.
3. Reproduction with retained seeds or an approved independent batch.
4. Domain review.
5. Rules-owner review only when a canonical change is proposed.
6. Separate versioned errata, migration, or rejection.
7. New baseline approval when required.

The queue item never edits canon directly.

## 26.12 Finding dispositions

A finding may close or remain open as:

- closed intentional control;
- rejected with no change;
- approved migration;
- approved canonical correction;
- deprecated with history;
- deferred for human playtesting;
- insufficient evidence;
- open owner review.

The exact machine enums remain controlled by the harness schemas.

## 26.13 Baseline governance

A baseline is approved evidence for expected behavior.

Changing a baseline requires:

- identified reason;
- reviewed drift;
- compatibility or migration analysis;
- approval;
- versioned release;
- retained prior history.

A developer must not update expected outputs merely to make failing tests pass.

## 26.14 Regression versus balance

A regression means behavior changed relative to an approved baseline.

A balance concern means behavior may be undesirable relative to intended peers or goals.

A change may be:

- a regression without a balance issue;
- a balance issue without a regression;
- both;
- neither.

The review system must preserve this distinction.

## 26.15 Current verified harness baseline

The completed 8D-007J release candidate recorded:

- 9 verified component packs;
- 3,717 passing component-acceptance checks represented;
- 259 active canonical cases;
- 220 exact product-case baselines;
- 39 executed regression cases;
- 18 separate RNG-conformance cases;
- 339 approved baseline objects;
- 21 retained simulation runs;
- 3,080,000 retained candidate trials;
- 7 replay bundles;
- 7 closed intentional control findings;
- 0 unexpected canonical-content findings;
- 0 open owner-action review items;
- 957 final release-candidate acceptance checks;
- 0 final release-candidate failures.

These results complete the automated golden-corpus and balance-harness program. They do not approve final game balance, human playtest sufficiency, usability, accessibility, production performance, or release.

## 26.16 Human playtesting

Human playtesting remains necessary to evaluate:

- fun;
- clarity;
- pacing;
- cognitive load;
- perceived fairness;
- strategic variety;
- social dynamics;
- GM burden;
- emergent interactions;
- usability.

Automated evidence helps select, reproduce, and prioritize issues. It does not replace actual tables.

## 26.17 AI boundary

AI may:

- run approved analyses;
- summarize metrics;
- reproduce findings;
- compare peer groups;
- propose review hypotheses;
- draft noncanonical correction options.

AI must not:

- alter canonical values automatically;
- broaden peer groups improperly;
- hide insufficient evidence;
- treat generated target bands as approved;
- claim human validation;
- approve a new baseline without authority.

## 26.18 Controlling references

- 8D-007C Golden Rules Corpus
- 8D-007D Deterministic Randomness and Replay
- 8D-007E Domain Test Suites
- 8D-007F Cross-Domain Scenario Corpus
- 8D-007G Balance Metrics and Evaluation Model
- 8D-007H Simulation and Batch Harness
- 8D-007I Regression Baselines and Balance Review Queue
- 8D-007J Golden Corpus and Balance Harness Release Candidate
- Phase 9 runtime and test-roadmap integration maps

**Status:** Canonical and validated automated evaluation architecture; final balance and human-playtest sufficiency remain unapproved.

---

# Tranche 2 Integration Review

## T2.1 Coverage

Volume II now defines the shared game-system architecture from declaration through accepted state change and across the principal rules and content domains.

It covers:

- core resolution;
- characters;
- progression;
- actions;
- effects;
- conditions;
- resources;
- modifiers;
- abilities;
- combat;
- social play;
- investigation;
- exploration;
- environments;
- downtime;
- projects;
- crafting;
- economy;
- items;
- operational assets;
- species;
- forms;
- creatures;
- NPCs;
- balance;
- regression.

## T2.2 Shared runtime spine

All domains should reuse the following spine where applicable:

1. Stable identity.
2. Versioned content and rules profiles.
3. Actor and authority.
4. Declaration or proposal.
5. Validation.
6. Deterministic or recorded resolution.
7. Ordered modifiers.
8. Generated effects.
9. GM approval, denial, or alteration where required.
10. Accepted application.
11. Immutable event evidence.
12. Updated projection.
13. Permission-scoped synchronization.
14. Backup, restore, migration, and export compatibility.

## T2.3 Cross-domain invariants

The following requirements apply across Volume II:

- No UI-only rules engine.
- No silent completion of missing canon.
- No duplicate canonical mechanics where a shared record exists.
- No mutation without actor, authority, source, and result.
- No hidden partial state change after validation failure.
- No erased calculation after GM alteration.
- No entitlement state disguised as in-world ownership.
- No current projection without recoverable history where history is required.
- No secret leakage through search, AI, notification, cache, export, or synchronization.
- No balance finding that edits canon directly.
- No deletion used as a substitute for destruction, retirement, abandonment, expiration, or archive.
- No migration that silently discards historical selections or provenance.

## T2.4 Composition rules

The system composes complex entities from governed layers.

Examples include:

- a character composed from species, form, progression, abilities, items, conditions, campaign grants, and events;
- a creature projection composed from a base definition, rules profile, template, variant, encounter adjustment, and current state;
- a vehicle composed from a frame, components, resources, crew assignments, cargo, conditions, and modification history;
- an investigation projection composed from canonical clues, discovery events, participant knowledge, and player-created theories.

Composed projections must retain the identity and provenance of each layer.

## T2.5 Authority boundaries

### Canon authority

Defines reusable rules and content.

### Campaign authority

Defines campaign instances, events, restrictions, grants, relationships, and adjudications without rewriting global canon.

### Session authority

Controls ordering, validation, accepted actions, visibility, synchronization, reconnect, and recovery during active play.

### User-authored overlays

Notes, theories, labels, collections, preferred layouts, and similar overlays may reference canon without changing it.

## T2.6 Data quality boundary

An incomplete or contradictory record is a data-quality state.

It is not permission to:

- invent values;
- select an arbitrary variant;
- merge conflicts silently;
- treat prose inference as approved mechanics;
- declare the record balanced.

## T2.7 Implementation guidance

Later implementation should prioritize vertical slices that exercise the shared runtime across more than one domain.

A slice should include, where applicable:

- real canonical data;
- validation;
- permissions;
- save and load;
- event evidence;
- error and recovery behavior;
- desktop and mobile presentation;
- tests;
- owner-verifiable behavior.

This reduces the risk of building disconnected domain-specific mock interfaces.

## T2.8 Tranche boundary

Volume II is complete at the architectural level.

It does not replace:

- exact canonical records;
- schemas;
- formula definitions;
- pack manifests;
- validators;
- fixtures;
- golden baselines;
- campaign-specific rules;
- future human playtest findings.

Future revisions should reference those authorities rather than duplicating all of their machine-readable content into the Bible.

**Tranche 2 status:** Complete — canonical architectural consolidation.


# Volume III — World and Content Architecture

# 27. Multiversal Cosmology and Setting Boundaries

## 27.1 Purpose

Define the structural language used to represent cosmology, realities, worlds, settings, timelines, travel relationships, and bounded areas of play without forcing all source material into one physical-geography hierarchy.

This chapter defines architecture and boundaries. It does not replace the canonical cosmology pack or invent missing cosmological facts.

## 27.2 Core principle

Multiversal content may exist at many scales and in many kinds of relationship.

A setting can be:

- a complete world;
- a reality;
- a realm;
- a plane;
- a city;
- a region;
- a facility;
- a station;
- a mall;
- an alternate history;
- a pocket dimension;
- a repeating world pattern;
- an adventure-bounded location;
- another source-defined scope.

The application must not assume that every setting is a planet, that every world belongs to one conventional universe, or that every connection is geographic.

## 27.3 Canonical cosmology layers

The governed setting architecture supports typed definitions including:

- Branch;
- cosmological layer;
- Reality Cluster;
- Reality;
- Reality Archetype;
- World;
- world pattern;
- world variant;
- Setting Node;
- timeline concept;
- travel network;
- access profile;
- setting relationship;
- compatibility axis and rating;
- stability state;
- reveal state.

These record families describe different concepts. A world is not automatically a Reality, a Setting Node is not automatically a World, and a travel connection does not imply containment.

## 27.4 Branches

A Branch is a high-level cosmological definition sourced from the Multiversal cosmology material.

A Branch may define or reference:

- stable identity;
- name and source-grounded summary;
- order or placement where canonically established;
- cosmological characteristics;
- known relationships;
- compatible reality or world patterns;
- travel and access concepts;
- reveal state;
- provenance;
- unresolved boundaries.

The 8E-006B conversion preserved fourteen Branch Definitions from the detailed source catalog.

Legacy or example labels that remain unresolved must not be silently promoted into canonical Branches. Temporalis and Abundantia remain examples of such unresolved labels unless a later owner-approved source changes their status.

## 27.5 Cosmological layers

Cosmological layers are ordered or related conceptual strata.

The canonical conversion includes fourteen ordered layers, from Non-Duality through Oblivion. Their exact content, ordering, and definitions remain controlled by the cosmology pack.

An implementation may visualize layers but must not convert visualization coordinates into new cosmological facts.

## 27.6 Reality clusters and realities

A Reality Cluster groups Realities according to source-defined cosmological relationships.

A Reality definition may include:

- cluster;
- archetype;
- compatibility characteristics;
- stability state;
- access restrictions;
- timeline relationships;
- worlds or Setting Nodes associated with it;
- travel relationships;
- reveal state;
- source and provenance.

A dead Reality remains a Reality with a defined state or classification. It must not be deleted or represented only as a broken link.

## 27.7 Reality archetypes

A Reality Archetype is a reusable descriptive or classification pattern.

It may support:

- comparison;
- compatibility assessment;
- discovery;
- content filtering;
- travel or access evaluation;
- presentation.

An archetype is not a substitute for the identity or source-specific facts of an individual Reality.

## 27.8 Worlds

A World is a governed setting definition at a world scale.

A World may reference:

- Branch or Reality relationships;
- world pattern;
- parent or peer Setting Nodes;
- Regions;
- travel networks;
- timelines;
- factions and cultures;
- lore;
- environments;
- rules profiles;
- compatible content extensions;
- source and provenance.

A world record is not the same as:

- a world pack;
- a campaign placement;
- a current campaign instance;
- a map;
- a timeline snapshot.

The 8E-006B conversion added eight source-grounded World Definitions. The number is a conversion result, not a claim that the Multiversal canon contains only eight worlds.

## 27.9 World patterns and variants

A world pattern represents a source-grounded recurring or shared world structure.

A world variant represents a variation, placement, historical state, alternate expression, or other typed relationship to a base World or pattern.

A variant must preserve:

- base identity;
- variant identity;
- relationship type;
- changed or contextual fields;
- source and provenance;
- compatibility;
- reveal state.

A variant may not silently overwrite the base World.

## 27.10 Setting Nodes

A Setting Node is a flexible top-level or intermediate setting entity that cannot safely be reduced to a conventional World or Location.

A Setting Node may represent a source-defined cosmological, spatial, conceptual, or campaign-usable setting boundary.

It may connect to:

- Branches;
- Realities;
- Worlds;
- Regions;
- Locations;
- timelines;
- travel networks;
- other Setting Nodes.

The use of Setting Nodes allows the architecture to preserve unusual source structures rather than forcing them into an inaccurate hierarchy.

## 27.11 Setting scopes

The owner-approved setting classification baseline contains eight Scopes.

A scope describes the scale or boundedness of the setting material. It helps determine:

- expected content coverage;
- suitable pack structure;
- browsing and navigation;
- readiness evaluation;
- campaign use;
- dependency expectations.

Scope is classification metadata. It does not grant authority, alter canon status, or prove completeness.

## 27.12 Support levels

The setting classification baseline contains six Support Levels.

A support level communicates how much application and content support is available for a setting.

Support may reflect areas such as:

- source coverage;
- canonical conversion;
- rules support;
- characters;
- items;
- creatures;
- environments;
- adventures;
- maps or assets;
- validation.

The exact support-level definitions remain authoritative in the shared setting baseline.

A support level must not be inferred only from the amount of prose in a source document.

## 27.13 Capability badges

The classification baseline contains fifteen Capability Badges.

Badges communicate available or expected capabilities, such as whether the setting includes certain kinds of content or play support.

Badges are discoverability and readiness signals. They must be derived from governed evidence and must not become duplicate rules.

## 27.14 Readiness tracks

The classification baseline contains twelve Readiness Tracks and an internal zero-to-five readiness scale.

Readiness is multidimensional. A setting may have strong lore but weak encounter support, or strong creatures and items but incomplete adventure integration.

A single summary score must not conceal blocking track failures.

Public promotion or release readiness requires the applicable governance gate; an internal readiness score alone is not approval.

## 27.15 Setting layers

Optional setting layers may represent source-grounded dimensions such as:

- historical era;
- alternate timeline;
- supernatural overlay;
- political state;
- environmental state;
- campaign adaptation;
- reveal layer.

Layers should be additive or explicitly overriding. They must preserve the base setting and identify their source and compatibility.

## 27.16 Timelines

A timeline definition describes a source-grounded chronology, sequence, era framework, or branching-history structure.

The architecture distinguishes:

- timeline definition;
- historical event definition;
- campaign timeline state;
- timeline divergence;
- snapshot;
- player-visible knowledge.

A campaign event may create a divergence without rewriting the canonical history definition.

## 27.17 Travel networks

A Travel Network defines a set of possible routes or relationships.

A network may represent:

- roads;
- portals;
- dimensional paths;
- transit systems;
- sea lanes;
- star routes;
- ritual routes;
- conceptual connections;
- another governed travel structure.

A network may include nodes, edges, route types, access requirements, known directionality, and references to rules profiles.

The 8E-006B conversion produced four source-grounded Travel Networks.

## 27.18 Access profiles

An access profile defines source-grounded restrictions, prerequisites, or context for reaching or using a setting relationship.

An access profile may reference:

- ability or capability requirements;
- item or vehicle requirements;
- knowledge;
- authorization;
- time or era;
- route state;
- reality stability;
- campaign condition;
- GM reveal;
- rules profile.

The 8E-006B conversion created nine source-grounded access profiles.

Numeric difficulty classes, timers, Sync values, strain values, phase ratings, and similar Multiversal Dynamics procedures remain source rules profiles pending or subject to their controlling canon rules work. The setting graph must not hardcode unresolved values.

## 27.19 Setting relationships

A setting relationship is a typed edge between setting entities.

Relationship types may include:

- contains;
- located in;
- adjacent to;
- connected to;
- accessed through;
- variant of;
- historical successor or predecessor;
- timeline branch;
- overlaps;
- mirrors;
- depends on;
- source-defined relationship.

The exact relationship catalog is governed.

Each relationship should identify:

- stable edge identity;
- source and target;
- relationship type;
- directionality;
- access profile where applicable;
- travel network;
- visibility;
- source;
- provenance;
- unresolved issues.

The 8E-006B conversion created forty-one source-grounded relationship edges.

## 27.20 Compatibility

Reality or setting compatibility is an assessment, not an assumption.

Compatibility may evaluate declared axes and ratings for:

- travel;
- physics;
- environment;
- magic or supernatural rules;
- technology;
- time;
- identity;
- form;
- other source-defined concerns.

An assessment should identify:

- entities compared;
- axes;
- ratings;
- evidence;
- version;
- unresolved conditions.

Compatibility must not be simplified into a universal compatible/incompatible flag when the source architecture requires multiple axes.

## 27.21 Stability

A stability state describes source-grounded or campaign-state information about a Reality, route, timeline, or related entity.

Definition-level stability classifications remain separate from live campaign stability.

A campaign event may change live stability without rewriting the reusable definition.

## 27.22 Reveal and discovery

Cosmology contains information characters may not know.

The architecture distinguishes:

- GM truth;
- public setting information;
- campaign-discovered information;
- participant-specific knowledge;
- hidden routes;
- hidden relationships;
- unresolved source information.

A hidden edge must not leak through:

- map layout;
- search;
- autocomplete;
- dependency errors;
- AI context;
- export;
- cache;
- notification.

## 27.23 Definitions, placements, state, and snapshots

Every cosmological or setting system must preserve the separation among:

### Definition

Reusable canonical content.

### Placement or binding

The decision that a definition exists in a campaign, adventure, timeline, location graph, or other context.

### Live state

Current discoveries, route availability, stability, occupancy, environment, control, and other mutable campaign facts.

### Snapshot

A historical or recovery representation tied to versions and event position.

Updating a definition must not reset placements or live state.

## 27.24 Explicit unresolved boundaries

The source record may state a relationship without providing a complete roster or exact mechanics.

Examples preserved by 8E-006B include:

- the Thirty Winds connect thirty worlds, but the complete roster is not enumerated;
- The Mall has an unresolved relationship involving both Goblin tunnels and the Chaos;
- certain legacy Branch labels remain unresolved;
- some Multiversal Dynamics numbers remain source profiles rather than universal constants.

The correct behavior is to preserve the known statement and the unresolved boundary. Worlds, relationships, or numbers must not be invented to create apparent completeness.

## 27.25 Controlling references

- 8E-006A Setting Corpus Reconciliation and Shared World Baseline
- 8E-006B Branches, Realities, Worlds, and Setting Relationships
- canonical cosmology framework pack
- shared setting baseline pack
- setting classification schemas and catalogs
- world, Reality, Branch, Setting Node, relationship, access, compatibility, stability, reveal, timeline, and travel-network schemas

**Status:** Canonical architecture and validated source conversion. Unresolved cosmological facts remain unresolved.

---

# 28. Content Domains

## 28.1 Purpose

Define the major governed content domains and how they interact without duplicating identities, mechanics, or ownership.

## 28.2 Domain principle

A content domain groups records with similar responsibility. It does not create a separate runtime, identity system, provenance system, or pack lifecycle.

All domains share:

- stable IDs;
- record layers;
- schema versions;
- content versions;
- source references;
- provenance;
- canon and conversion status;
- dependencies;
- validation;
- pack ownership;
- compatibility;
- visibility where applicable.

## 28.3 Foundation domains

Foundation content provides shared structures used by many packs.

Examples include:

- canonical object contracts;
- Actions;
- Effects;
- Conditions;
- Resources;
- modifiers;
- rules profiles;
- movement modes;
- ownership and visibility models;
- setting classifications;
- adventure-framework definitions.

Foundation content should be owned by dedicated framework or core packs when it is truly shared.

## 28.4 Character domains

Character content includes:

- species;
- subspecies and lineages;
- forms;
- adaptations;
- attributes;
- skills;
- proficiencies;
- abilities;
- progression structures;
- character templates;
- character creation rules.

World packs reference this content through dependencies or extensions rather than copying it.

## 28.5 Item and economy domains

Item content includes:

- items;
- weapons;
- ammunition;
- armor;
- tools;
- technology;
- magic items;
- software;
- materials;
- food;
- trade goods;
- crafting inputs;
- recipes;
- containers;
- economy and transaction profiles.

Definitions remain separate from campaign item instances and ownership.

## 28.6 Creature and NPC domains

Creature and NPC content includes:

- creature definitions;
- creature actions and traits;
- behavior profiles;
- variants;
- templates;
- NPC archetypes;
- social roles;
- relationships;
- faction references;
- loadouts;
- mounts;
- companions;
- summons;
- hazards;
- traps;
- encounter templates.

A world or adventure pack references integrated creature and NPC content rather than duplicating stat blocks as new authority.

## 28.7 Operational asset domains

Operational assets include:

- vehicles;
- mecha;
- ships;
- starships;
- bases;
- facilities;
- components;
- subsystems;
- crew stations;
- asset actions;
- repair and refit structures.

Definitions remain separate from owned, placed, crewed, or damaged campaign instances.

## 28.8 Setting domains

Setting content includes:

- Branches;
- cosmological layers;
- Reality Clusters;
- Realities;
- Reality Archetypes;
- Worlds;
- world patterns and variants;
- Setting Nodes;
- Regions;
- Settlements;
- Locations;
- Environments;
- travel networks;
- access profiles;
- setting relationships;
- compatibility;
- stability;
- timelines.

## 28.9 Culture and lore domains

Culture and lore content includes:

- factions;
- governments;
- organizations;
- cultures;
- religions;
- lore;
- legends;
- histories;
- eras;
- historical events;
- conflicts;
- timeline definitions.

Live membership, office, reputation, control, cultural presence, religious practice, revealed knowledge, current conflict, and timeline state remain campaign-managed state.

## 28.10 Adventure domains

Adventure content includes:

- adventure definitions;
- campaign templates;
- acts;
- hooks;
- routes;
- quests;
- objectives;
- milestones;
- scenes;
- choice points;
- clues;
- revelations;
- GM truths;
- rewards;
- consequences;
- cast placements;
- encounter bindings;
- scaling profiles;
- adventure rules profiles.

## 28.11 Media and presentation domains

Media and presentation content may include:

- images;
- portraits;
- tokens;
- maps;
- diagrams;
- audio;
- handouts;
- icons;
- theme assets;
- localization strings.

Media is referenced by governed metadata and content identity. It must not be duplicated into every record or treated as mechanical authority.

## 28.12 Documentation and instructional domains

Some packs or repositories may include:

- GM guidance;
- player guidance;
- examples;
- tutorials;
- conversion notes;
- release notes;
- migration guides;
- validation reports.

Instructional material must identify whether it is normative, explanatory, procedural, or historical.

## 28.13 Record layers

The integrated architecture distinguishes at least:

### Definition

Reusable canonical content.

### Placement or binding

A contextual relationship establishing that a definition is used or located in another context.

### Live instance or state

Mutable campaign or session data.

### Event

Immutable accepted occurrence.

### Snapshot

Recovery, audit, or historical projection tied to versions.

### User-authored overlay

Notes, tags, theories, collections, display preferences, and other noncanonical additions.

A domain may use only the layers it needs, but it must not collapse layers in a way that causes definition updates to overwrite live state.

## 28.14 Record ownership

Each stable reusable record has one owner pack.

Other packs may:

- require it;
- optionally reference it;
- extend it through governed extension points;
- place or bind it;
- provide compatibility metadata.

Other packs must not create a second authoritative copy of the same stable record.

## 28.15 Shared versus world-specific content

Content belongs in a shared framework pack when:

- it is reusable across multiple settings;
- its identity and mechanics are not owned by one world;
- duplication would create incompatible authority;
- the source explicitly defines it as shared.

Content belongs in a world or setting pack when:

- it is owned by that setting;
- its lore or identity depends on that setting;
- its default placement is setting-specific;
- independent installation should include or exclude it.

A world pack may have optional extension packs for creatures, items, characters, assets, or adventures when separating them improves dependency control and installation choice.

## 28.16 External dependencies

A setting or adventure may depend on content owned by other domain packs.

External dependencies should identify:

- required pack and version range;
- referenced stable IDs;
- whether the dependency is required or optional;
- fallback or degraded behavior;
- compatibility status;
- source and rationale.

An absent required dependency is an install or validation failure. It is not permission to create a local duplicate.

## 28.17 Source boundaries

Source documents often combine lore, mechanics, examples, tables, art notes, and adventure placement.

Conversion must classify each source unit into the correct domain and layer while preserving source coordinates.

A source paragraph can support multiple linked records, but each promoted record must retain its provenance.

## 28.18 Cross-domain references

Cross-domain references must be explicit and typed.

Examples include:

- a World references Regions;
- a Location references an Environment;
- a Faction references a World or Region;
- an NPC references a Faction and loadout;
- an adventure Scene references a Location, participants, clues, and encounter bindings;
- an Environment references source rules profiles and hazard types;
- a world pack references character, item, creature, and asset extensions.

## 28.19 No mechanical duplication

A setting description may mention an ability, faction progression, environmental adaptation, weapon, creature action, or hazard procedure.

The mention should reference the canonical record owned by its domain.

It should not create a second mechanic embedded only in the setting record.

## 28.20 Content status

Records should retain distinct status dimensions where relevant:

- canon status;
- conversion status;
- validation status;
- release status;
- support level;
- visibility;
- deprecation or supersession.

One generic status field is insufficient when it would hide these distinctions.

## 28.21 Coverage

Coverage reports should distinguish:

- source units discovered;
- source units registered;
- candidates extracted;
- canonical records promoted;
- mechanics mapped;
- unresolved conflicts;
- missing information;
- deferred routes;
- validation state.

A high record count does not prove complete source coverage.

## 28.22 Content-domain extension rule

A new domain should be created only when existing canonical object types and extension mechanisms cannot accurately represent the content.

Before creating a new domain, contributors must check:

- existing schemas;
- canonical object templates;
- extension points;
- shared actions and effects;
- pack ownership;
- compatibility;
- migration cost.

## 28.23 Controlling references

- Phase 8 canonical object and domain programs
- 8E-001 master source inventory
- 8E-002 character foundations
- 8E-003 items and economy
- 8E-004 creatures, NPCs, hazards, traps, and encounters
- 8E-005 operational assets
- 8E-006 settings and adventures
- 8E-007 shared-mechanics consolidation
- 8E-008 final validation
- 8E-009 CSV-first reconciliation and promotion program
- canonical data contracts and object templates

**Status:** Canonical domain architecture.

---

# 29. World and Setting Packs

## 29.1 Purpose

Define how setting content is assembled into installable `.pack` releases with clear ownership, dependencies, compatibility, migration, and separation from live campaign state.

## 29.2 Approved extension

Multiversal pack files use the `.pack` extension.

Internal manifests and content determine the pack type. Separate public filename extensions for every domain are not required by the canonical pack standard.

## 29.3 Pack roles

The 8E-006F release architecture organizes setting and adventure content into:

- framework packs;
- world and setting packs;
- optional domain extensions;
- adventure extensions.

The release-candidate assembly validated twenty-five framework, world, and adventure packs.

The count describes that release candidate. It does not limit future settings or pack types.

## 29.4 Framework packs

Framework packs provide shared definitions that multiple world and adventure packs can reference.

The 8E-006F architecture uses four framework roles covering shared setting baseline, cosmology, environment, and adventure support.

Framework packs should contain only shared records with clear ownership. They must not become dumping grounds for unrelated world-specific content.

## 29.5 World and setting packs

A world or setting pack owns reusable setting-specific definitions.

It may include or reference:

- World or Setting Node definitions;
- Regions;
- Settlements;
- Locations;
- Environment definitions;
- factions;
- cultures;
- religions;
- lore;
- history;
- timelines;
- travel relationships;
- world-specific rules profiles;
- media and presentation;
- compatibility metadata;
- optional extension routes.

A setting pack may represent less than a complete World when its declared scope is narrower.

## 29.6 Adventure extensions

An adventure extension owns reusable adventure content and may bind it to a setting through explicit dependencies and placements.

It may include:

- adventure definitions;
- campaign templates;
- acts;
- hooks;
- routes;
- quests;
- objectives;
- milestones;
- scenes;
- choices;
- clues;
- revelations;
- rewards;
- consequences;
- cast placements;
- encounter bindings;
- scaling profiles.

An adventure pack should not duplicate the world, NPC, creature, item, or encounter definitions it references.

## 29.7 Optional domain extensions

World-specific species, items, creatures, NPCs, operational assets, abilities, or other domain content may be packaged as extensions when:

- they depend on the world pack;
- they should be installable separately;
- they have their own validation or release cadence;
- they are owned by another domain architecture;
- separating them avoids circular or oversized dependencies.

## 29.8 One owner per record

Every stable reusable record has exactly one owner pack.

The owner pack:

- publishes the record;
- controls its canonical version;
- carries its provenance;
- defines migration and supersession;
- provides its content hash.

Other packs reference the record by stable ID and dependency.

## 29.9 Required dependency order

The 8E-006F architecture defines this order:

1. Shared Setting Baseline.
2. Cosmology, Environment, and Adventure Frameworks.
3. World and Setting Packs.
4. Character, item, creature, ability, and operational-asset extensions.
5. Adventure Extensions.
6. Campaign placement and live state.

Installers must resolve dependencies before promoting dependent content.

## 29.10 Required and optional dependencies

A required dependency must be present and compatible.

An optional dependency may enable:

- additional creatures;
- items;
- characters;
- assets;
- encounters;
- maps;
- adventure routes;
- enhanced rules support.

Optional dependency absence should produce defined degraded behavior, not broken references.

## 29.11 Dependency graph requirements

A pack dependency graph must be:

- resolvable;
- version-aware;
- cycle-safe;
- deterministic;
- inspectable;
- validated before installation.

A circular dependency is rejected unless the pack architecture explicitly supports a governed cycle-breaking mechanism. No such mechanism should be assumed.

## 29.12 Record ownership map

A release should provide an ownership map linking stable records to owner packs.

The ownership map supports:

- duplicate detection;
- dependency validation;
- update planning;
- uninstall safety;
- provider-exit export;
- provenance;
- source and pack browsing.

## 29.13 Manifest

A world or setting pack manifest should identify, as applicable:

- pack ID;
- name;
- version;
- pack role or classification;
- schema or contract version;
- owner or authority;
- dependencies and version ranges;
- optional dependencies;
- record counts and content indexes;
- source registry;
- checksums;
- compatibility;
- migration;
- install order;
- release and canon status;
- support blockers;
- media and license references.

The machine schema controls exact required fields.

## 29.14 Index

The pack index enumerates owned records and their content paths or content streams.

The index must be deterministic and consistent with:

- manifest counts;
- content hashes;
- schemas;
- checksums;
- ownership map.

## 29.15 Sources and provenance

A pack must preserve source information sufficient to trace records to authoritative source units and conversion history.

Provenance-only older compilations may remain registered without becoming the active conversion source.

## 29.16 Checksums

Release files and indexed content should be protected by deterministic integrity checksums.

A checksum verifies bytes. It does not establish canon authority, source correctness, or semantic compatibility by itself.

## 29.17 Installation

Installation should:

1. verify package integrity;
2. validate manifest and index;
3. resolve required dependencies;
4. evaluate compatibility;
5. validate schemas and stable IDs;
6. reject ownership conflicts;
7. import definitions into the installed registry;
8. create no campaign placements unless explicitly requested;
9. emit an install receipt or event;
10. leave live campaign state unchanged.

## 29.18 Update

An update should:

- verify the current installed version;
- validate the new pack;
- apply migrations;
- preserve stable identities;
- retain history and snapshots;
- report superseded or deprecated records;
- preserve campaign placements and live state;
- produce an update receipt.

A definition update must not reset:

- discoveries;
- visited state;
- faction reputation;
- ownership;
- inventory;
- adventure progress;
- timeline divergence;
- live environment state.

## 29.19 Uninstallation

Uninstallation must distinguish among:

- removing reusable definitions;
- preserving live snapshots;
- blocking removal because active campaigns depend on the pack;
- archiving or exporting campaign state;
- removing optional unused content;
- removing an adventure extension while preserving completed history.

The uninstaller must report blocking references and required actions.

It must not silently delete campaign history or user-owned state.

## 29.20 Migration and supersession

A migration identifies:

- source version;
- target version;
- affected records;
- stable-ID continuity;
- replacements;
- deprecations;
- transformations;
- compatibility;
- rollback or recovery behavior;
- validation.

Supersession should preserve the old identity and its relationship to the replacement.

## 29.21 Pack compatibility

Compatibility may include:

- schema version;
- application contract;
- framework dependencies;
- world relationships;
- cross-domain extensions;
- rules profiles;
- required providers;
- migration availability;
- known conflicts.

A compatible archive is not automatically suitable for a particular campaign. Campaign placement and policy remain separate.

## 29.22 Support blockers

A pack may be valid but not ready for a target support level.

Blockers may include:

- missing required dependencies;
- unresolved source conflicts;
- incomplete mechanics;
- insufficient locations;
- absent adventure support;
- missing assets;
- unvalidated migration;
- owner-only canon decisions;
- release-policy requirements.

Blockers must be reported explicitly rather than hidden by a single readiness score.

## 29.23 Pack contents versus campaign state

A pack contains reusable definitions and release metadata.

It does not contain a campaign’s mutable truth unless it is a governed campaign export or snapshot with a different contract.

Installing a world pack must not automatically:

- create a campaign;
- place every setting entity;
- reveal hidden lore;
- grant abilities;
- assign faction membership;
- establish ownership;
- set beliefs;
- start an adventure;
- rewrite history.

## 29.24 Campaign placement

A campaign may bind selected pack definitions into its own setting graph.

Placement may specify:

- which World or Setting Node is used;
- selected Regions and Locations;
- timeline or era;
- active world variants or layers;
- factions and cultures present;
- allowed character and content extensions;
- active adventures;
- visibility;
- campaign-specific overrides or adjudications.

Placement does not change the reusable definitions.

## 29.25 Public and private content

Pack visibility and distribution are separate from canon status.

A pack may be:

- internal;
- test;
- playtest;
- closed-alpha;
- private campaign content;
- approved public content.

Public release requires the applicable owner and release gates.

## 29.26 Provider neutrality

Pack import, registry, storage, install, update, migration, uninstall, and export contracts remain provider-neutral.

No pack should require a specific hosted provider merely to represent its content.

## 29.27 Validation

A release candidate should validate:

- ZIP or archive integrity;
- manifest and index;
- checksums;
- schema conformance;
- stable-ID uniqueness;
- one-owner rule;
- dependency graph;
- cross-pack references;
- compatibility;
- migration and supersession;
- installation order;
- install and uninstall behavior;
- role-filtered visibility;
- export and recovery contracts where applicable.

## 29.28 Current release-candidate boundary

The completed 8E-006G architecture validated:

- cumulative setting and adventure `.pack` content;
- twenty-five assembled framework, world, and adventure packs;
- schemas;
- fixtures;
- references;
- migration contracts;
- integration and release handoff materials.

It did not validate:

- production database execution;
- production UI wiring;
- realtime transport;
- staging performance;
- owner approval of Canon 1.0;
- public release.

## 29.29 Controlling references

- 8E-006A Shared Setting Baseline
- 8E-006F World-Pack Assembly, Dependencies, and Release Preparation
- 8E-006G Setting and Adventure Integration Release Candidate
- world-pack release catalog
- dependency graph
- record ownership map
- install-order fixture
- migration and supersession map
- compatibility matrix
- release-gate matrix
- canonical pack schemas

**Status:** Canonical and validated release architecture; production integration and release remain unapproved.

---

# 30. Adventure, Campaign, Quest, and Scene Content

## 30.1 Purpose

Define reusable narrative structures and their relationship to campaign placement, live play, visibility, event history, and recovery.

## 30.2 Separation of reusable and live content

Adventure architecture distinguishes:

1. reusable Definitions;
2. Campaign Placements and Bindings;
3. live campaign state;
4. role-filtered projections;
5. immutable events and snapshots.

This separation is mandatory.

An adventure definition is not an active campaign. A scene definition is not a current scene instance. A clue definition is not automatically known to players.

## 30.3 Adventure definition

An Adventure Definition describes a reusable module or structured adventure.

It may reference:

- premise;
- intended scope or tier;
- World or setting;
- campaign template;
- acts;
- hooks;
- routes;
- quests;
- objectives;
- milestones;
- scenes;
- choice points;
- clues;
- GM truths;
- encounters;
- cast placements;
- rewards;
- consequences;
- scaling profiles;
- rules profiles;
- source and provenance.

The adventure definition must not duplicate referenced external creature, NPC, item, environment, or encounter mechanics.

## 30.4 Campaign template

A Campaign Template provides a reusable starting structure.

It may define:

- setting bindings;
- initial era or timeline;
- allowed content;
- default rules profiles;
- starting locations;
- adventure placement;
- cast placement;
- initial faction or world state;
- GM-only preparation;
- onboarding;
- optional routes.

Creating a campaign from a template creates new campaign identity and state. It does not mutate the template.

## 30.5 Campaign

A Campaign is a live governed aggregate with:

- stable identity;
- owner and GM authority;
- members and roles;
- installed and permitted content;
- setting placements;
- timeline and world state;
- characters;
- NPC and creature instances;
- factions and relationships;
- inventory and ownership;
- active and completed adventures;
- discoveries and knowledge;
- event history;
- snapshots;
- permissions;
- exports and recovery metadata.

A campaign may diverge from canonical history through accepted events without rewriting reusable world definitions.

## 30.6 Acts

An Act Definition groups an intentional portion of an adventure.

An act may define:

- purpose;
- entry conditions;
- scenes;
- objectives;
- milestones;
- routes;
- escalation;
- completion conditions;
- transitions.

Acts are organizational structures. The runtime should not assume a fixed three-act model unless the adventure defines it.

## 30.7 Hooks

A Hook Definition describes a way characters or a campaign may enter an adventure.

A hook may include:

- trigger;
- involved factions or NPCs;
- starting knowledge;
- starting location;
- required prerequisites;
- initial objectives;
- visibility;
- source and provenance.

Selecting a hook creates campaign placement or events. It does not alter the reusable hook definition.

## 30.8 Routes

A Route Definition describes a meaningful path through an adventure.

A route may include:

- entry conditions;
- required or optional objectives;
- scene transitions;
- choices;
- consequences;
- rewards;
- failure states;
- ending state.

Routes may branch, converge, be abandoned, or remain unresolved.

The system must not force a nonlinear adventure into one mandatory linear route.

## 30.9 Quests

A Quest Definition represents a trackable purpose or structured undertaking.

A quest may define:

- hook or premise;
- objectives;
- routes;
- rewards;
- consequences;
- failure outcomes;
- visibility;
- source and provenance.

A live Quest State should track:

- accepted or discovered state;
- current objectives;
- completed and failed objectives;
- selected routes;
- consequences;
- rewards;
- event history;
- visibility.

## 30.10 Objectives

An Objective Definition states a desired result.

An objective may include:

- success condition;
- failure condition;
- optionality;
- dependencies;
- timing;
- visibility;
- linked scenes;
- linked clues;
- linked encounters;
- reward or consequence references.

A live Objective State should distinguish:

- unavailable;
- hidden;
- available;
- active;
- completed;
- failed;
- abandoned;
- superseded.

The exact enum remains schema-controlled.

## 30.11 Milestones

A Milestone Definition marks a meaningful progress point.

A milestone may:

- unlock scenes;
- reveal information;
- activate routes;
- award progression;
- change faction or world state;
- trigger consequences;
- support campaign summaries.

Milestone completion is an accepted event, not an inference based only on a UI checkbox.

## 30.12 Scenes

A Scene Definition describes a reusable prepared scene.

It may reference:

- scene type;
- adventure;
- act;
- location;
- default environments;
- participants;
- cast placements;
- encounter bindings;
- clues;
- objectives;
- player brief;
- GM notes;
- entry conditions;
- exits or transitions;
- source and provenance.

A live Scene Instance adds:

- current participants;
- actual placement;
- time;
- active environment;
- reveal state;
- initiative or timing state if used;
- active objectives;
- discovered clues;
- current hazards;
- actions and events;
- notes;
- completion or pause state.

## 30.13 Scene types

Scene types may include:

- opening;
- investigation;
- social;
- exploration;
- travel;
- combat;
- puzzle;
- downtime;
- transition;
- climax;
- aftermath;
- another source-defined type.

Scene type supports preparation and UI. It does not create a separate incompatible rules engine.

## 30.14 Choice points

A Choice Point Definition identifies a consequential player or GM decision.

It may define:

- available options;
- conditions;
- visibility;
- consequences;
- route changes;
- world or faction effects;
- required adjudication;
- reversibility.

A live choice event records:

- options presented;
- participants with authority;
- selected result;
- time;
- consequences;
- GM alteration;
- resulting state.

## 30.15 Clues

A Clue Definition is reusable investigation content.

It may include:

- source;
- discoverable portions;
- reveal conditions;
- reliability;
- ambiguity;
- relationships;
- related objectives;
- related scenes;
- consequences;
- GM truth links;
- visibility;
- provenance.

A clue definition remains separate from participant knowledge.

## 30.16 Revelations and GM truths

A GM Truth represents authoritative hidden information for an adventure.

A Revelation defines the controlled disclosure of information.

The architecture must preserve:

- hidden truth;
- reveal conditions;
- information revealed;
- recipients;
- partial reveals;
- resulting knowledge state;
- event history.

GM truth must not leak through player-facing search, AI context, export, notifications, dependency errors, or client cache.

## 30.17 Cast placements

A Cast Placement binds a reusable NPC, creature, archetype, or role to an adventure, act, scene, location, or route.

A placement may specify:

- definition reference;
- adventure role;
- location;
- scene;
- timing;
- visibility;
- relationship;
- loadout or variant reference;
- substitution;
- source and provenance.

Placement does not duplicate the cast member’s mechanics.

A campaign may instantiate, replace, move, remove, or alter the placed cast member through live state and events.

## 30.18 Encounter bindings

An Encounter Binding links an encounter definition or template to an adventure context.

It may specify:

- scene or route;
- placement;
- trigger;
- scaling profile;
- participant substitutions;
- environment;
- reward or consequence;
- visibility.

The underlying encounter content remains owned by its encounter pack.

## 30.19 Scaling profiles

A Scaling Profile defines source-grounded or approved adjustment logic.

It may account for:

- party size;
- character progression;
- available abilities;
- campaign rules;
- optional content;
- difficulty intent.

Scaling must not silently change canonical base records. It creates an explicit encounter or adventure projection.

## 30.20 Rewards

A Reward Definition describes an authored possible result.

Rewards may include:

- progression;
- items;
- resources;
- relationships;
- faction reputation;
- knowledge;
- access;
- world-state change;
- another governed outcome.

A reward is applied only through an accepted campaign event.

## 30.21 Consequences and failure outcomes

A Consequence Definition describes an authored result of:

- choice;
- success;
- failure;
- delay;
- abandonment;
- partial completion.

Consequences may alter campaign state without rewriting reusable definitions.

Failure need not end the adventure. It may open a new route, add complications, remove opportunities, change world state, or create a later objective.

## 30.22 Adventure state

Live adventure state may track:

- selected hook;
- active act;
- active and completed scenes;
- routes;
- objectives;
- milestones;
- choices;
- discovered clues;
- revealed truths;
- cast state;
- encounter state;
- rewards;
- consequences;
- timeline and world changes;
- pause and resume;
- completion, failure, or abandonment.

The projection must be recoverable from event history and snapshots under compatible versions.

## 30.23 Visibility

Adventure content should declare a visibility default and may define more specific reveal behavior.

Typical categories include:

- player-visible;
- discovered;
- role-filtered;
- GM-only;
- participant-specific;
- unresolved.

The same reusable record may produce different role-filtered projections.

## 30.24 Branching

Branching should be represented through explicit routes, choices, conditions, objectives, scene transitions, and consequences.

The application must support:

- optional scenes;
- skipped scenes;
- repeated scenes;
- multiple paths;
- converging paths;
- divergent endings;
- unresolved branches;
- campaign-created branches.

A diagram is a projection of the graph. It is not the only authoritative form of the adventure.

## 30.25 Notes and authored changes

GM notes, player notes, and campaign-created content remain distinct from reusable adventure canon.

A GM may:

- add a scene;
- move a cast member;
- alter a reward;
- create a route;
- adjudicate an outcome;
- add campaign lore.

The change belongs to campaign state or a separately governed derived content pack. It does not silently modify the original adventure definition.

## 30.26 Event history

Accepted adventure operations should create immutable events or event groups, including:

- adventure placement;
- hook selection;
- quest activation;
- objective change;
- clue discovery;
- revelation;
- cast placement or movement;
- encounter activation;
- choice;
- milestone;
- reward;
- consequence;
- scene start, pause, resume, and completion;
- route change;
- adventure completion, failure, or abandonment;
- GM adjudication.

## 30.27 Snapshots and recovery

A snapshot should record:

- campaign;
- adventure placement;
- pack versions;
- definition snapshots or fingerprints where required;
- event position;
- live projection;
- visibility state;
- compatibility and recovery metadata.

Recovery must preserve choices, discoveries, hidden truth, objective state, cast state, and consequences.

## 30.28 The Lost Key to Nowhere acceptance fixture

The Lost Key to Nowhere is a governed playtest and acceptance adventure used to validate the architecture.

The accepted package preserves sixty-six records and includes structures such as:

- an adventure module;
- campaign template;
- acts;
- hooks;
- routes;
- quests;
- objectives;
- milestones;
- scenes;
- clues;
- GM truths;
- cast placements;
- encounter bindings;
- choice points;
- rewards;
- consequences;
- scaling profiles.

It demonstrates investigation, exploration, combat, social interaction, moral choice, and multiversal consequences.

Its playtest authority does not automatically promote all of its content to final Canon 1.0.

## 30.29 External content rule

Adventure content must reference external canonical definitions for:

- creatures;
- NPCs;
- encounters;
- items;
- abilities;
- environments;
- factions;
- locations;
- operational assets.

The reference must identify the required or optional owner pack.

Missing required content is a dependency failure. It is not permission to embed an ungoverned duplicate.

## 30.30 AI boundary

AI may:

- summarize player-visible objectives;
- organize GM-visible preparation;
- propose noncanonical scene variants;
- identify unresolved references;
- help create draft adventure content;
- suggest branching consequences;
- prepare session recaps from accepted events.

AI must not:

- expose GM truth;
- reveal undiscovered clues;
- make a player choice;
- apply a reward;
- change an objective;
- instantiate cast;
- promote generated adventure material to canon;

without the required authority and accepted operation.

## 30.31 Current validated integration boundary

The 8E-006G release candidate validates the architecture for:

- installed pack registry;
- reusable setting and adventure definitions;
- campaign placements and bindings;
- live campaign state;
- role-filtered projections;
- immutable history and snapshots;
- external provider routing;
- cumulative pack compatibility;
- migration and supersession;
- integration scenarios.

It does not validate production UI, database, realtime, staging, or public release.

## 30.32 Controlling references

- 8E-006A Settings and Adventures Subphase Plan
- 8E-006E Adventures, Campaigns, Scenes, Objectives, Clues, and Cast Placement
- 8E-006F World-Pack Assembly
- 8E-006G Integration Release Candidate
- canonical adventure, campaign, quest, objective, milestone, scene, route, hook, choice, clue, revelation, reward, consequence, cast-placement, encounter-binding, and scaling schemas
- The Lost Key to Nowhere governed acceptance pack
- external creature, NPC, encounter, item, ability, environment, faction, and setting packs

**Status:** Canonical and validated content architecture. Final adventure canon and production runtime remain separately governed.



# 31. Organizations, Factions, Relationships, and Reputation

## 31.1 Purpose

Define reusable organizations, factions, governments, cultures, religions, lore, history, and timelines while keeping them separate from mutable campaign membership, authority, control, reputation, belief, discovery, and divergence.

## 31.2 Architectural separation

The setting architecture distinguishes reusable Definitions from provider- or campaign-managed state.

Reusable Definitions include:

- factions;
- organizations;
- governments;
- cultures;
- religions;
- lore entries;
- eras;
- historical events;
- timelines;
- faction relationships;
- referenced faction and prestige profiles.

Mutable state includes:

- membership;
- rank;
- office;
- ownership;
- current control;
- permissions;
- reputation;
- cultural presence;
- religious practice;
- revealed knowledge;
- current conflict;
- current leadership;
- timeline state;
- campaign divergence.

Installing or referencing a definition does not create any of the mutable state above.

## 31.3 Organizations and factions

An Organization Definition describes a structured collective.

A Faction Definition describes a collective whose identity, goals, alignments, relationships, influence, or role matter within the setting or campaign.

The architecture may use a shared organization foundation with typed faction extensions, but must preserve source distinctions.

A reusable definition may include:

- stable identity;
- name;
- aliases;
- organization or faction type;
- purpose;
- goals;
- values;
- methods;
- structure;
- leadership model;
- headquarters or operating locations;
- territory or sphere of influence;
- known resources;
- symbols;
- allies, rivals, enemies, dependencies, or parent relationships;
- setting and timeline references;
- public and hidden information;
- source and provenance;
- conflict and missing-information status.

An incomplete headquarters, leader, membership count, or relationship remains explicitly incomplete.

## 31.4 Governments

A Government Definition describes a source-grounded governing structure.

It may include:

- jurisdiction;
- government type;
- offices;
- institutions;
- legal or political relationships;
- succession;
- recognized authority;
- setting and timeline context;
- public and hidden lore;
- source and provenance.

A Government Definition does not establish who currently holds an office in a live campaign.

Current office holders, contested claims, coups, elections, succession, territorial control, and active law enforcement are mutable campaign state or events.

## 31.5 Membership

Membership is a contextual relationship among an entity, organization, and campaign or setting placement.

A membership record may identify:

- member;
- organization or faction;
- membership type;
- rank;
- status;
- start and end events;
- sponsor;
- visibility;
- permissions;
- obligations;
- source;
- campaign scope.

Membership must not be inferred solely from species, culture, birthplace, religion, profession, or reputation.

## 31.6 Rank and office

Rank and office are separate concepts.

### Rank

Represents a governed position within a progression, hierarchy, or classification.

### Office

Represents a specific role, responsibility, title, or authority position.

A person may hold an office without following the same rank model as another organization. A rank may exist without a unique office.

Rank and office records should define:

- organization;
- title or tier;
- prerequisites;
- authority;
- permissions;
- responsibilities;
- duration;
- vacancy or succession behavior;
- source and provenance.

## 31.7 Authority and permissions

Organization authority is explicit and scoped.

Permissions may govern:

- access;
- requisition;
- command;
- voting;
- information;
- facilities;
- assets;
- membership management;
- diplomacy;
- finance;
- law;
- another organization-specific function.

A title displayed in prose must not silently grant application permissions. Permissions must be represented through governed policy or campaign state.

## 31.8 Ownership and control

Ownership, jurisdiction, influence, occupation, custody, and current control are distinct.

Examples:

- a faction may claim a region without controlling it;
- a government may legally own a facility while another faction occupies it;
- a character may command an asset without owning it;
- an organization may sponsor an item without possessing it.

The relationship type and current state must be explicit.

## 31.9 Faction relationships

A Faction Relationship Definition describes a source-grounded relationship between organizations or factions.

It may include:

- source faction;
- target faction;
- relationship type;
- directionality;
- public stance;
- hidden stance;
- historical basis;
- conditions;
- setting and timeline context;
- source and provenance.

A reusable relationship does not lock the live campaign into that state forever.

Campaign events may create a new relationship state while preserving the original definition and historical context.

The completed 8E-006D conversion produced twenty-eight stable Faction Relationship Definitions.

## 31.10 Relationship types

Relationship types may include:

- alliance;
- rivalry;
- hostility;
- vassalage;
- dependency;
- trade;
- patronage;
- competition;
- truce;
- covert cooperation;
- infiltration;
- historical succession;
- another source-defined relationship.

The type vocabulary remains governed. Contributors must not reduce all relationships to ally, neutral, or enemy when the source provides more meaningful distinctions.

## 31.11 Reputation

Reputation is a contextual perception or standing, not a property of the reusable faction definition.

A reputation record may be scoped to:

- character;
- group;
- campaign;
- organization;
- region;
- settlement;
- culture;
- public audience;
- hidden internal audience.

A reputation record should identify:

- subject;
- perceiving group or context;
- current value, tier, or state;
- source events;
- visibility;
- decay or persistence rules;
- relevant faction or prestige rules profile;
- campaign scope.

Reputation is not automatically membership, rank, office, trust, loyalty, or permission.

## 31.12 Approved faction and prestige mechanics

The Phase 8B Faction and Prestige release is the authoritative progression dependency for approved faction-facing mechanics.

World and setting packs reference the approved profiles rather than duplicating their formulas or progression rules.

The 8E-006D package preserved seven authoritative dependency links to the Phase 8B faction-profile system.

A faction may exist without using a particular progression profile. A progression profile may apply to more than one faction where canonically appropriate.

## 31.13 Cultures

A Setting Culture Definition describes a source-grounded cultural context.

It may include:

- identity;
- values;
- customs;
- institutions;
- language references;
- traditions;
- art;
- etiquette;
- social structures;
- relationships;
- geography;
- history;
- variation;
- source and provenance.

Setting cultures remain separate from:

- species;
- subspecies;
- biological traits;
- character-facing origin or culture components;
- individual belief or behavior.

A character’s culture selections may reference a Setting Culture Definition but must not imply that every member shares identical values, skills, abilities, or conduct.

The completed 8E-006D conversion produced forty-seven Setting Culture Definitions.

## 31.14 Religions

A Religion Definition may describe:

- institution;
- beliefs;
- cosmology;
- practices;
- offices;
- sacred places;
- texts;
- symbols;
- relationships;
- historical context;
- source and provenance.

A Religion Definition does not set a player character’s:

- faith;
- practice;
- devotion;
- alignment;
- behavior;
- membership;
- office.

Those are character choices, campaign relationships, or live state.

The completed 8E-006D conversion produced thirteen Religion Definitions.

## 31.15 Lore

Lore content must identify the kind of claim it represents.

Relevant claim classes may include:

- official history;
- scholarly account;
- public knowledge;
- local tradition;
- legend;
- myth;
- propaganda;
- rumor;
- secret history;
- source assertion;
- discovered campaign truth;
- unresolved or contradictory account.

These classes may coexist. The application must not merge them into one authoritative statement.

A Lore Entry may define:

- subject;
- claim class;
- source;
- period;
- setting scope;
- public and hidden portions;
- reliability or dispute status where authored;
- related records;
- reveal behavior;
- provenance.

The completed 8E-006D conversion produced twenty Lore Entries.

## 31.16 Eras and calendars

An Era Definition describes a source-grounded historical period.

It may include:

- name;
- start and end references;
- predecessor and successor;
- associated timelines;
- major events;
- relevant worlds or regions;
- source date system;
- source and provenance.

Source eras and dates must be preserved without inventing a universal calendar.

The application may provide comparison or conversion views only when a governed mapping exists.

The completed 8E-006D conversion produced eighteen Era Definitions.

## 31.17 Historical events

A Historical Event Definition describes reusable source history.

It may include:

- stable identity;
- title;
- event type;
- date or era references;
- participants;
- locations;
- causes;
- outcomes;
- interpretations;
- public and hidden information;
- timeline relationships;
- source and provenance.

A historical definition does not assert that the event occurred identically in every campaign timeline.

The completed 8E-006D conversion produced forty-three Historical Event Definitions.

## 31.18 Timelines

A Timeline Definition describes a source-grounded chronology or branching historical structure.

It may identify:

- parent timeline;
- branch point;
- era relationships;
- historical event relationships;
- worlds and settings;
- known divergences;
- compatibility;
- reveal state;
- source and provenance.

Live campaign timeline state is separate.

A campaign may:

- follow the canonical timeline;
- diverge;
- create alternate outcomes;
- discover hidden history;
- merge or cross timelines where supported.

These changes become campaign events and state, not edits to the reusable Timeline Definition.

The completed 8E-006D conversion produced eleven Timeline Definitions.

## 31.19 Historical conflict handling

When sources conflict, the conversion and runtime must preserve:

- each claim;
- source;
- authority;
- scope;
- date or era system;
- public or hidden status;
- conflict classification;
- adjudication status.

The system must not choose the most convenient account and erase the others.

## 31.20 Reveal and knowledge

Faction motives, secret memberships, covert relationships, disputed histories, hidden faiths, propaganda, and secret lore require role-filtered projection.

The system must prevent leakage through:

- search;
- relationship graphs;
- map overlays;
- membership lists;
- AI context;
- export;
- notifications;
- autocomplete;
- dependency diagnostics;
- cached projections.

## 31.21 Relationship tracker requirements

The application’s relationship tracker should be a projection over governed relationship records and events.

It should be capable of representing:

- person-to-person relationships;
- person-to-faction relationships;
- faction-to-faction relationships;
- organization membership;
- rank and office;
- reputation;
- promises, favors, and debts;
- public and hidden facets;
- historical changes;
- source and campaign events.

A graph view is not the canonical record. It is one visualization of typed relationships.

## 31.22 Source-completion boundary

The 8E-006D conversion preserved incomplete one-line factions, uncertain headquarters, incompatible date systems, and conflicting histories rather than silently completing them.

The correct workflow is:

1. preserve the source statement;
2. record the missing field or conflict;
3. route it for source recovery or owner review;
4. keep it out of required runtime fields unless a valid fallback exists;
5. promote a correction only through governance.

## 31.23 Validated conversion baseline

The completed 8E-006D package contains 1,204 cumulative setting records across fifty-nine content types.

It preserved the 875 records from 8E-006C and added 329 stable Definitions and profiles, including:

- 83 Faction Definitions;
- 47 Setting Culture Definitions;
- 13 Religion Definitions;
- 20 Lore Entries;
- 18 Era Definitions;
- 43 Historical Event Definitions;
- 11 Timeline Definitions;
- 28 Faction Relationship Definitions;
- 7 authoritative faction-profile dependency links;
- 16 runtime schemas and golden fixtures;
- 41 passing acceptance checks.

These totals describe the validated conversion release, not a permanent limit on Multiversal content.

## 31.24 AI boundary

AI may:

- summarize visible faction and relationship context;
- identify unresolved source fields;
- compare visible historical claims;
- suggest noncanonical organization drafts;
- help prepare relationship or reputation views.

AI must not:

- set membership;
- assign rank or office;
- change reputation;
- reveal secret relationships;
- select one conflicting history as canon;
- set a character’s culture or religion;
- promote generated lore;

without the appropriate authority and accepted operation.

## 31.25 Controlling references

- 8E-006D Factions, Cultures, Lore, History, and Timelines
- Phase 8B Faction and Prestige release
- faction, culture, religion, lore, era, historical-event, timeline, and faction-relationship schemas
- faction-profile dependency map
- faction relationship map
- source conflict and missing-information register
- provider-routing report
- runtime architecture summary
- 8E-006F and 8E-006G world-pack integration releases

**Status:** Canonical and validated content architecture. Live membership, reputation, control, belief, knowledge, and timeline state remain campaign-managed.

---

# 32. Content Production Standards

## 32.1 Purpose

Define the governed lifecycle for creating, recovering, converting, reviewing, validating, packaging, publishing, and maintaining Multiversal content.

## 32.2 Production principle

Content production is not complete when prose is written.

A production-ready content release requires:

- identified source or authoring authority;
- stable identity;
- correct domain and layer;
- schema conformance;
- provenance;
- dependencies;
- explicit mechanics;
- validation;
- deterministic packaging;
- migration and compatibility planning;
- release status.

## 32.3 Content creation paths

Multiversal supports three distinct creation paths.

### Source recovery

Transforms legacy source material into canonical governed records while preserving source coordinates, variants, conflicts, and omissions.

### Canonical original authoring

Creates new owner-approved content directly in current schemas and standards.

### Campaign-local authoring

Creates content for one campaign or private context without automatically promoting it to global canon.

The paths may share tools, but their authority and promotion requirements differ.

## 32.4 Source-first recovery workflow

A source recovery tranche should:

1. register source files;
2. establish source authority and aliases;
3. create structural or row-level inventory;
4. identify candidate records and embedded mechanics;
5. classify domains and record layers;
6. assign deterministic candidate identity;
7. preserve source coordinates;
8. map candidates to canonical schemas;
9. reconcile duplicates and variants;
10. record conflicts and missing information;
11. promote valid canonical records;
12. validate provenance and coverage;
13. package and test the release;
14. preserve deferred candidates.

No source section should disappear merely because it did not become a canonical record in the current pass.

## 32.5 Original canonical authoring workflow

New canonical content should begin with an approved brief that identifies:

- purpose;
- scope;
- owner;
- target domain;
- target audience;
- dependencies;
- intended support level;
- required mechanics;
- source or design authority;
- release target;
- owner-only decisions.

The author then works from canonical templates and validators rather than creating an incompatible free-form format.

## 32.6 Campaign-local authoring workflow

Campaign-local content may be created more freely but must still preserve:

- campaign identity;
- author;
- record type;
- source or note origin;
- visibility;
- stable campaign-local identity;
- dependencies;
- migration and export behavior.

Campaign-local content must be visibly distinguished from official or shared canon.

## 32.7 Brief requirements

A content-production brief should define:

- content family;
- number and range of records;
- required fields;
- allowed optional fields;
- source boundary;
- canon target;
- mechanics boundary;
- art and media needs;
- localization needs;
- acceptance fixtures;
- validation commands or checks;
- exclusions;
- delivery format.

A brief may use representative examples, but examples do not silently add requirements.

## 32.8 Templates

Templates should provide:

- correct stable-ID structure;
- required metadata;
- domain-specific fields;
- provenance slots;
- dependency references;
- visibility;
- canon and conversion status;
- validation annotations;
- extension points.

A template is a starting contract. It must not be filled with invented values merely to satisfy completeness scoring.

## 32.9 Stable naming

Content names should be:

- source-faithful;
- unambiguous within their display context;
- suitable for localization;
- distinct from stable identity;
- free from file-path dependence.

Aliases may support:

- source variations;
- abbreviations;
- alternate spellings;
- former names;
- translated names;
- search terms.

Aliases must retain source or editorial provenance.

## 32.10 Stable identity

Stable IDs must be assigned according to the canonical ID standard.

A stable ID must not change merely because:

- display name changes;
- spelling is corrected;
- localization is added;
- a record moves files;
- a pack is reorganized;
- an image changes;
- formatting changes.

A genuinely different canonical concept requires a different stable ID or an explicit variant or replacement relationship.

## 32.11 Definition versus presentation

Mechanics and canonical facts belong in structured fields and references.

Presentation may include:

- summary;
- descriptive prose;
- examples;
- GM guidance;
- player guidance;
- flavor;
- generated display blocks.

Presentation must not be the only location of executable mechanics.

## 32.12 Mechanics authoring

A mechanic should use existing canonical:

- Actions;
- Effects;
- Conditions;
- Resources;
- modifiers;
- rules profiles;
- progression;
- grants;
- compatibility rules.

A new mechanic type is justified only when existing structures cannot accurately represent the behavior.

Content authors must not copy a formula into many records when a shared rules profile should own it.

## 32.13 Domain completeness

Completeness is domain-specific.

A creature, item, location, adventure, faction, or ability has different required fields.

Completeness profiles may classify fields as:

- required;
- conditionally required;
- recommended;
- optional;
- source unavailable;
- not applicable.

A missing source value must not be replaced with a guessed value solely to improve a score.

## 32.14 Canon and conversion status

At minimum, content workflows should distinguish:

- draft;
- candidate;
- source-extracted;
- normalized;
- conflict-held;
- incomplete;
- promoted;
- canonical;
- deprecated;
- archived.

Exact machine enums remain schema-controlled.

Canon status and conversion status must not be collapsed into one ambiguous field.

## 32.15 Source provenance

Each source-derived record should retain enough information to answer:

- which source file;
- which logical source;
- which page, row, section, coordinate, or object;
- which extraction or conversion method;
- which transformation;
- which candidate;
- which canonical record;
- which release;
- which conflicts or missing fields;
- which validator result.

## 32.16 Original-author provenance

New original content should record:

- author or owner;
- creation date;
- approving authority;
- design brief;
- source inspirations where relevant and legally usable;
- change history;
- pack ownership;
- release status.

AI involvement should be recorded when material to authorship, review, or generation.

## 32.17 Variants and conflicts

A source variant is not automatically a duplicate.

A content review should decide whether records are:

- exact duplicates;
- aliases;
- variants;
- historical versions;
- local adaptations;
- conflicting claims;
- separate concepts.

The decision and evidence should be recorded.

## 32.18 Missing information

Missing information must be classified.

Examples include:

- source omission;
- unreadable source;
- contradictory source;
- undefined mechanic;
- required owner decision;
- deferred conversion;
- external dependency;
- future content need.

The content may remain valid for limited use if the missing information is nonblocking and clearly represented.

## 32.19 Writing standards

Canonical prose should:

- use clear direct language;
- separate fact, rule, example, and guidance;
- avoid unnecessary ambiguity;
- preserve source tone where appropriate without compromising structure;
- avoid embedding interface instructions into reusable lore or mechanics;
- identify pronouns and references clearly;
- avoid assumptions about a single genre or world unless the record is setting-specific;
- use canonical terms consistently.

Flavor text may be expressive. Rules text must be precise.

## 32.20 Rule-text structure

Rules text should make explicit:

- trigger;
- actor;
- target;
- timing;
- prerequisites;
- cost;
- resolution;
- outcome;
- duration;
- stacking;
- failure;
- removal or recovery;
- source.

Not every rule uses every element, but required behavior must not depend on hidden interpretation.

## 32.21 Examples

Examples should:

- use canonical identifiers or clearly fictional placeholders;
- state assumptions;
- avoid adding unapproved mechanics;
- demonstrate one primary behavior at a time;
- identify noncanonical illustrative values;
- remain valid when display names are localized.

An example is not a golden fixture unless it is registered and tested as one.

## 32.22 Cross-references

Cross-references use stable IDs or governed references rather than text-only names.

A display layer may render human-readable names, but the underlying link must remain deterministic.

## 32.23 Dependencies

Every external reference should identify its owner pack and compatibility requirements.

Content authors must avoid:

- hidden dependencies;
- circular dependencies;
- copying dependency records;
- referencing unpromoted candidates as canon;
- assuming optional content is installed.

## 32.24 Content review roles

A production tranche may require separate review lenses:

- source fidelity;
- game mechanics;
- lore and setting;
- schema;
- provenance;
- dependency;
- balance observation;
- accessibility;
- media rights;
- localization;
- release.

One reviewer or AI may perform several roles, but the acceptance evidence should identify which checks occurred.

## 32.25 Validation layers

Content validation should include, where applicable:

- syntax;
- schema;
- required fields;
- stable-ID uniqueness;
- reference resolution;
- pack ownership;
- dependency graph;
- provenance;
- source coverage;
- conflict handling;
- mechanics contracts;
- install and uninstall;
- migration;
- runtime fixture;
- regression;
- media and license metadata;
- localization structure;
- checksums.

## 32.26 Golden fixtures

Representative valid and invalid fixtures should test:

- simple records;
- complex records;
- optional fields;
- boundary values;
- missing dependencies;
- unresolved conflicts;
- hidden information;
- installation;
- migration;
- removal;
- role-filtered projections.

A fixture should be deterministic and versioned.

## 32.27 Balance boundary

Content production may collect balance observations, but source truth and proposed balance changes remain separate.

A creator must not silently alter source mechanics to fit a target metric.

## 32.28 Promotion

Promotion to a higher status should require evidence appropriate to that status.

Examples:

### Candidate to promoted

Requires valid mapping, identity, provenance, and schema.

### Promoted to canonical release

Requires owner or delegated canon authority, package validation, dependency resolution, and release evidence.

### Internal to public

Requires the formal release gate, including rights, privacy, safety, support, and production readiness.

## 32.29 Deprecation and replacement

Deprecating a record should preserve:

- old stable ID;
- reason;
- replacement;
- migration;
- compatibility;
- history;
- affected packs;
- affected live state;
- release notes.

Deletion is inappropriate when users or campaign history may still reference the record.

## 32.30 Content updates

An update should identify:

- changed fields;
- reason;
- source or decision;
- compatibility;
- migration;
- balance impact;
- dependent records;
- tests;
- release version.

Cosmetic and mechanical changes should be distinguishable.

## 32.31 Content Studio requirements

A future content-authoring tool should help creators:

- select the correct domain;
- start from canonical templates;
- search existing records before creating duplicates;
- create stable IDs;
- manage dependencies;
- attach provenance;
- validate in real time;
- preview role-filtered presentation;
- run fixtures;
- assemble packs;
- create migration notes;
- export deterministic releases.

The tool must not hide schema errors by silently discarding fields.

## 32.32 AI-assisted content production

AI may assist with:

- source classification;
- draft extraction;
- normalization proposals;
- duplicate detection;
- schema mapping;
- missing-field identification;
- noncanonical drafting;
- consistency review;
- test-fixture proposals;
- editorial revision.

AI-generated material remains a proposal unless accepted.

AI must preserve:

- source boundaries;
- uncertainty;
- provenance;
- conflicts;
- owner authority;
- rights and licensing constraints.

## 32.33 Batch efficiency

Large content programs should use governed tranches.

A tranche should combine compatible:

- source inventory;
- conversion;
- identity reconciliation;
- dependency mapping;
- schema validation;
- provenance audit;
- fixture generation;
- migration;
- packaging.

It should not be split into unnecessary conversational microsteps.

## 32.34 Completion report

A completed production tranche should report:

- source boundary;
- records preserved;
- records added;
- record types;
- unresolved conflicts;
- deferred candidates;
- schemas and fixtures;
- validation checks;
- package hashes;
- restrictions;
- next handoff.

## 32.35 Controlling references

- Canonical Object Template Program
- Canonical Object Specification and completeness profiles
- 8E-001 source inventory and conversion map
- 8E-002 through 8E-006 domain conversion releases
- 8E-007 consolidation releases
- 8E-008 final validation and provenance audit
- 8E-009 CSV-first conversion and reconciliation
- Development Brain content-system destinations
- pack schemas, validators, fixtures, manifests, and release reports

**Status:** Canonical production principles consolidated from validated project practice. Tool-specific Content Studio implementation remains planned.

---

# 33. Art, Asset, and Localization Pipelines

## 33.1 Purpose

Define how images, maps, tokens, diagrams, audio, handouts, icons, theme assets, and localized text attach to canonical content without duplicating large files, losing rights information, leaking hidden content, or changing mechanical authority.

## 33.2 Media Asset definition

A Media Asset is a governed presentation record for an image, audio file, video, map, handout, token, portrait, diagram, document, or related file.

The canonical object catalog identifies Media Asset as a presentation-layer object carrying file metadata, rights, and visibility.

A Media Asset should be separate from:

- the creature, character, item, location, or other subject definition;
- a campaign placement;
- a rendered thumbnail;
- a user’s annotation;
- a temporary upload;
- a generated preview.

## 33.3 Asset identity

A media record should have stable identity independent of its display filename or storage URL.

A media record may identify:

- asset ID;
- subject references;
- media type;
- purpose;
- variant;
- source file;
- content hash;
- dimensions or duration;
- file format;
- accessibility metadata;
- rights;
- creator or provider;
- source and provenance;
- visibility;
- release status;
- derivative relationships;
- storage references.

Storage paths and CDN URLs are replaceable locations, not canonical identity.

## 33.4 Content-addressed storage

Large media should be stored once and referenced by content identity or governed asset record.

Content addressing helps:

- deduplicate identical bytes;
- verify integrity;
- support provider exit;
- rebuild derivatives;
- detect corruption;
- preserve provenance;
- reduce pack size.

A new crop, resize, compression, color treatment, or format conversion may be a derivative asset linked to its source.

## 33.5 Asset purposes

A single subject may have multiple assets for different purposes, including:

- portrait;
- full-body reference;
- token;
- silhouette;
- inventory icon;
- map marker;
- scene illustration;
- handout;
- GM-only diagram;
- anatomical or technical diagram;
- card art;
- thumbnail;
- background;
- promotional image.

Purpose should be explicit so the application does not misuse a portrait as a token or expose a GM-only diagram to players.

## 33.6 Variants

Media variants may differ by:

- crop;
- aspect ratio;
- resolution;
- format;
- color palette;
- theme;
- pose;
- form;
- era;
- condition;
- reveal state;
- localization;
- accessibility treatment.

Variants must preserve their relationship to the base asset and subject.

## 33.7 Rights and licensing

Every media asset intended for governed distribution should identify, as applicable:

- creator;
- copyright owner;
- license;
- usage rights;
- attribution requirements;
- territory or platform restrictions;
- modification rights;
- commercial-use rights;
- source;
- evidence or receipt location;
- expiration or review requirement.

Unknown rights are a release blocker for public distribution.

Rights metadata must not be inferred from file presence, an online URL, or AI generation alone.

## 33.8 AI-generated art

AI-generated assets should record:

- generation provider or tool;
- model or service identifier where available;
- creation date;
- prompt or generation brief where policy permits;
- human editor;
- source references supplied;
- post-processing;
- rights and usage assessment;
- approval status;
- subject and purpose;
- derivative history.

AI-generated art is not automatically approved canon or approved for commercial release.

No production credential or paid generation service is authorized by this chapter.

## 33.9 Source art and scans

Legacy art, scans, diagrams, and maps should preserve:

- source file;
- source coordinate;
- crop boundary;
- extraction method;
- original resolution;
- cleanup history;
- rights status;
- relation to the source document;
- whether the asset is canonical, reference-only, or restricted.

A cleaned derivative must not replace the source evidence.

## 33.10 Asset intake workflow

A media intake workflow should:

1. receive the source file;
2. compute integrity hash;
3. scan or validate format;
4. record metadata;
5. identify subject and purpose;
6. record rights and provenance;
7. classify visibility;
8. create derivatives;
9. validate accessibility fields;
10. attach stable references;
11. package or register the asset;
12. produce an intake result.

A failed rights or visibility check must not be hidden by successful file conversion.

## 33.11 Derivative pipeline

The derivative pipeline may create:

- thumbnails;
- responsive sizes;
- web formats;
- print formats;
- tokens;
- crops;
- previews;
- low-bandwidth versions;
- accessibility alternatives.

Derivatives should be reproducible where practical.

A derivative record should identify:

- source asset;
- transformation profile;
- tool and version where material;
- output hash;
- dimensions;
- intended use.

## 33.12 Maps

A Map Definition is separate from the underlying image or vector asset.

A map definition may add:

- scale;
- coordinate system;
- layers;
- grid;
- zones;
- anchors;
- scene and location links;
- token support;
- reveal state;
- annotations;
- GM-only layers.

The image is a Media Asset. The coordinate and reveal model is governed map content. Live tokens and discoveries are campaign state.

## 33.13 Tokens

A token is a presentation or live scene projection of an entity, asset, hazard, area, or note.

A token may reference:

- subject;
- token art;
- scene;
- position;
- scale;
- orientation;
- visibility;
- state indicators.

A token is not the canonical creature, character, vehicle, or item record.

## 33.14 Handouts

A Handout may contain:

- media;
- localized text;
- annotations;
- version;
- reveal conditions;
- recipients;
- delivery history;
- source and provenance.

The handout definition is separate from the live reveal event.

A player export may contain delivered handouts but must not include unrevealed GM material.

## 33.15 Accessibility metadata

Media should include relevant accessibility fields, such as:

- concise alt text;
- extended description;
- captions;
- transcript;
- meaningful versus decorative classification;
- color-dependence warning;
- motion or flashing warning;
- readable-text alternative.

Alt text must not reveal information hidden from the current viewer.

Role-filtered assets may require role-filtered descriptions.

## 33.16 Visibility and secrets

Media visibility must be enforced in:

- search;
- previews;
- thumbnails;
- caches;
- offline bundles;
- exports;
- AI context;
- notifications;
- URLs;
- metadata;
- error messages.

A hidden asset must not leak its title, dimensions, filename, subject, or thumbnail when those details themselves reveal a secret.

## 33.17 Pack integration

A pack may reference media assets through an asset index or manifest.

The pack should identify:

- required assets;
- optional assets;
- rights and attribution files;
- content hashes;
- purpose;
- subject references;
- visibility;
- derivative availability;
- localization.

Large assets may be packaged separately if the dependency and offline behavior are explicit.

## 33.18 Missing assets

A missing image must not invalidate mechanical content unless the content contract declares the asset required.

The application should provide:

- deterministic placeholder behavior;
- accessible text;
- missing-asset diagnostic;
- optional retry or install path.

It must not substitute an unrelated image and imply canonical accuracy.

## 33.19 Themes and palettes

Theme assets and color palettes should be referenced through governed design tokens or theme records.

A theme may alter:

- surfaces;
- typography;
- accent;
- icons;
- decorative texture;
- presentation assets.

A theme must not alter:

- mechanics;
- permissions;
- hidden information;
- canonical identity;
- accessibility requirements.

## 33.20 Asset lifecycle

Media assets may be:

- draft;
- reference-only;
- approved internal;
- approved playtest;
- approved public;
- deprecated;
- withdrawn;
- archived.

Withdrawal should preserve history and identify replacement behavior.

A public asset may need to be removed while the associated mechanical content remains valid.

## 33.21 Provider neutrality and exit

Asset storage must support provider exit.

An export should preserve:

- asset identity;
- original and permitted derivatives;
- hashes;
- metadata;
- subject links;
- rights;
- visibility;
- pack ownership;
- storage-independent references;
- recovery information.

A canonical content record must not become unusable solely because one storage provider is unavailable.

## 33.22 Localization purpose

Localization allows approved content and application presentation to be shown in different languages and locales without changing stable identity, mechanics, permissions, or source provenance.

The Development Brain localization chapter was originally a scaffold. This section consolidates the durable baseline that follows from stable IDs, pack architecture, search, accessibility, and provider-neutral content design.

Specific translation vendors, libraries, machine-translation providers, and rollout languages remain unapproved unless separately governed.

## 33.23 Localizable content

Localizable fields may include:

- display name;
- short name;
- summary;
- descriptive prose;
- rules explanation;
- labels;
- instructions;
- examples;
- captions;
- alt text;
- handouts;
- UI strings;
- search aliases;
- release notes.

Stable IDs, formulas, enumerated machine values, hashes, source coordinates, and executable references must not be translated.

## 33.24 Localization keys

Localizable text should use stable keys or field-addressable records.

A localization key should remain stable when wording changes.

Keys should be based on stable content identity and semantic field, not on the English source text.

Example pattern:

`content.<stable-id>.display-name`

The exact key format remains an implementation standard to be validated before production localization.

## 33.25 Source locale

Each localizable record should identify its source locale.

The source locale is the authoritative authored language for that text field unless another owner-approved source-language policy applies.

A translated string does not become the source mechanical authority.

## 33.26 Locale fallback

Locale fallback must be deterministic.

A fallback chain may use:

1. requested locale;
2. approved regional parent;
3. source locale;
4. accessible placeholder or missing-translation diagnostic.

The exact application fallback configuration remains implementation-controlled.

Fallback must not expose hidden text that the requested role cannot access.

## 33.27 Translation status

A translation unit should track status such as:

- missing;
- draft;
- machine-assisted;
- human-reviewed;
- approved;
- outdated;
- blocked;
- deprecated.

Exact machine enums remain schema-controlled.

An unreviewed machine translation must not be represented as owner-approved.

## 33.28 Translation provenance

A translation should record:

- source unit;
- source text version or hash;
- target locale;
- translator or provider;
- review status;
- reviewer;
- creation and update time;
- terminology version;
- rights or restrictions;
- notes.

When the source text changes, affected translations should become outdated until reviewed.

## 33.29 Terminology

A governed terminology registry should preserve:

- canonical term;
- stable concept reference;
- approved translations;
- prohibited or deprecated translations;
- context;
- capitalization;
- grammatical notes;
- source and rationale.

Mechanically significant terms require especially careful consistency.

## 33.30 Variables and formatting

Localized text containing variables should use named placeholders tied to typed values.

Translation must not:

- remove required variables;
- change stable IDs;
- alter formulas;
- reorder values in a way the formatter cannot support;
- assume one plural form;
- concatenate fragments that cannot be translated naturally.

The application should use locale-aware formatting for:

- numbers;
- dates;
- time;
- currency;
- units;
- lists;
- pluralization.

## 33.31 Rules integrity

Localized rules text is a presentation of canonical mechanics.

The executable rule remains structured data and references.

If a translation conflicts with the canonical rule, the structured rule and source-language authority control until the translation is corrected.

## 33.32 Search and indexing

Search must support localized:

- titles;
- aliases;
- descriptions;
- terminology.

Every result must retain:

- stable ID;
- source pack;
- content version;
- locale;
- visibility;
- provenance.

Search must distinguish:

- no translation;
- content not installed;
- content not entitled;
- content hidden by role;

without leaking protected text.

## 33.33 Media localization

Some media may require localized variants, including:

- text-bearing maps;
- diagrams;
- handouts;
- captions;
- audio;
- video;
- screenshots;
- icon labels.

A localized derivative should retain:

- base asset;
- target locale;
- translator or editor;
- transformation history;
- rights;
- output hash;
- visibility.

Text embedded into an image should have a separate accessible text representation where practical.

## 33.34 Right-to-left and layout expansion

UI and asset pipelines should anticipate:

- right-to-left presentation;
- text expansion;
- longer labels;
- line breaking;
- different scripts;
- font fallback;
- vertical metrics;
- mirrored directional icons where appropriate.

Localization readiness must not be treated as translation alone.

## 33.35 User-generated text

User-generated campaign notes, dialogue, names, and custom content remain in the user’s authored language unless explicitly translated.

Automatic translation should not overwrite the original.

A translated view should identify that it is a derived presentation.

## 33.36 AI and localization

AI may:

- propose translations;
- identify terminology inconsistencies;
- flag missing placeholders;
- generate draft alt text;
- assist with captions;
- compare source and target coverage.

AI must not:

- mark its own output approved;
- erase source text;
- expose hidden content to a translation service;
- upload protected content to an unapproved provider;
- invent rights metadata;
- alter mechanics.

## 33.37 Validation

Media and localization validation should check, where applicable:

- asset hash;
- readable file;
- format;
- dimensions or duration;
- subject references;
- visibility;
- rights metadata;
- attribution;
- derivative relationship;
- accessibility fields;
- locale codes;
- stable localization keys;
- placeholder parity;
- source-text hash;
- fallback behavior;
- translation status;
- search-index behavior;
- role-filtered export.

## 33.38 Current boundary

The following are durable architectural requirements:

- Media Assets are governed presentation records.
- Stable identity is independent of storage URL.
- rights, provenance, and visibility must be preserved.
- mechanical content must remain usable without optional art.
- localization must not alter stable IDs or executable rules.
- search and export remain permission-aware.
- provider exit must include asset and localization metadata.

The following remain to be selected or completed later:

- production asset storage provider;
- image-processing library;
- CDN;
- supported launch locales;
- translation vendor;
- machine-translation provider;
- exact localization key schema;
- font licensing and fallback set;
- audio and video production standards;
- public asset-licensing policy.

## 33.39 Controlling references

- Master Game Object Catalog:
  - `mv.object.media-asset`
  - `mv.object.map-definition`
  - `mv.object.token`
  - `mv.object.handout`
- Canonical Object Specification and provenance model
- DB-004 content-system localization destination
- DB-003 search and indexing architecture
- pack manifests, checksums, asset indexes, visibility rules, and provider-exit requirements
- UI design system and accessibility planning
- source coverage and provenance audits
- owner-approved art direction and mockups

**Status:** Canonical baseline for identity, provenance, rights, visibility, permission safety, and provider exit. Production toolchain and localization rollout choices remain designed or pending.

---

# Tranche 3 Integration Review

## T3.1 Coverage

Volume III now consolidates the architecture for:

- cosmology;
- Branches;
- Realities;
- Worlds;
- Setting Nodes;
- timelines;
- travel;
- setting classifications;
- content domains;
- world and setting packs;
- adventures;
- campaigns;
- quests;
- scenes;
- clues;
- factions;
- organizations;
- governments;
- cultures;
- religions;
- lore;
- history;
- relationships;
- reputation;
- content production;
- media assets;
- localization.

## T3.2 Definition and state separation

The most important Volume III invariant is the separation of reusable content from live campaign truth.

Reusable definitions may describe:

- a faction;
- a culture;
- a historical event;
- a World;
- an adventure;
- a scene;
- a clue;
- a map;
- a media asset.

Live state determines:

- who belongs to the faction;
- current reputation;
- who controls a location;
- which timeline occurred;
- which adventure route was chosen;
- which clues were discovered;
- which scene is active;
- which handout was revealed;
- which asset variant a user may see.

Installing a pack must not create live state unless an explicit placement or import operation is accepted.

## T3.3 Pack ownership

Every stable reusable record has one owner pack.

Cross-domain or cross-setting use occurs through:

- required dependency;
- optional dependency;
- extension;
- placement;
- binding;
- compatibility relationship.

Copying a record to avoid a dependency is not permitted.

## T3.4 Knowledge and visibility

Volume III content often contains secrets.

Permission enforcement must cover:

- definitions;
- projections;
- relationships;
- maps;
- media;
- search;
- AI context;
- localization;
- exports;
- caches;
- notifications;
- errors.

A role-filtered projection is not optional presentation behavior. It is part of the data contract.

## T3.5 Source fidelity

Source recovery must preserve:

- source authority;
- coordinates;
- variants;
- contradictory claims;
- incomplete records;
- unresolved rosters;
- incompatible date systems;
- hidden information;
- provenance.

Apparent completeness must never be manufactured by AI inference.

## T3.6 Content production lifecycle

The common content lifecycle is:

1. Brief or source registration.
2. Source and authority boundary.
3. Candidate identification.
4. Domain and layer classification.
5. Stable identity.
6. Schema mapping.
7. Mechanics and dependency reconciliation.
8. Provenance.
9. Conflict and missing-information handling.
10. Validation.
11. Fixture and integration testing.
12. Pack assembly.
13. Release status and approval.
14. Migration and maintenance.
15. Export and preservation.

## T3.7 Media and localization

Art and localization are first-class content concerns, but they do not become mechanical authority.

Media and translations must preserve:

- subject identity;
- source;
- rights;
- visibility;
- accessibility;
- derivative history;
- locale;
- review status;
- provider exit.

Optional presentation assets must not make canonical mechanics inaccessible when they are unavailable.

## T3.8 Campaign divergence

A campaign may create:

- alternate history;
- changed faction relationships;
- new organizations;
- destroyed or rebuilt locations;
- discovered cosmology;
- new adventure routes;
- custom media;
- translated notes.

These changes belong to campaign state or a separately governed derived pack.

They do not silently rewrite global definitions.

## T3.9 Validation boundary

The completed Phase 8 packages validate content architecture, records, pack relationships, migrations, provenance, and representative runtime scenarios.

They do not by themselves validate:

- production UI;
- production storage;
- live realtime transport;
- public asset rights;
- commercial localization;
- staging performance;
- release approval.

## T3.10 Tranche status

Volume III is complete at the architectural level.

Future work may refine exact media, localization, authoring-tool, and public-publishing specifications as those owner-approved programs begin.

**Tranche 3 status:** Complete — canonical world and content architecture consolidated.


# Volume IV — Object and Data Architecture

# 34. Canonical Object Model

## 34.1 Purpose

Define the common architecture used to represent reusable Multiversal content, live campaign entities, relationships, events, snapshots, user-authored overlays, and provider-exit data without forcing every domain into an identical flat record.

## 34.2 Canonical object principle

Every governed Multiversal concept should be represented by the smallest accurate canonical object or linked set of canonical objects.

The object model exists to provide:

- stable identity;
- explicit type;
- source and provenance;
- versioning;
- dependency resolution;
- validation;
- deterministic relationships;
- pack ownership;
- runtime projection;
- migration;
- export and recovery.

The model must preserve source meaning rather than distort content merely to make every record look alike.

## 34.3 Common object envelope

Canonical reusable objects should expose a common envelope appropriate to their layer.

The envelope may include:

- stable object ID;
- object type;
- schema version;
- content version;
- display name and aliases;
- owning pack;
- canon status;
- conversion or authoring status;
- source references;
- provenance;
- dependencies;
- compatibility;
- visibility defaults;
- deprecation or supersession;
- validation metadata;
- extension data;
- content fingerprint.

The exact required fields remain controlled by the applicable schema.

## 34.4 Typed object families

The canonical object hierarchy groups related object types into families.

Representative families include:

- foundation mechanics;
- characters and progression;
- abilities and capability domains;
- items and economy;
- creatures and NPCs;
- operational assets;
- settings and cosmology;
- organizations and lore;
- adventures and scenes;
- media and presentation;
- rules profiles;
- provider or runtime contracts.

A family provides shared parameters and capability modules without erasing subtype-specific requirements.

## 34.5 Base object versus subtype

The base object contains fields required across governed objects.

A subtype adds fields needed for accurate domain representation.

Examples:

- an Item adds quantity, stacking, equip, ownership, and capability references;
- a Creature adds actions, behavior, habitat, resources, and encounter role;
- a Location adds setting relationships, environment, maps, and discovery information;
- an Adventure adds hooks, routes, scenes, objectives, clues, and consequences;
- a Media Asset adds file metadata, rights, visibility, and derivatives.

A subtype may not redefine the meaning of shared envelope fields.

## 34.6 Capability modules

Capability modules provide reusable, typed behavior blocks.

Modules may represent concerns such as:

- action granting;
- effect emission;
- condition lifecycle;
- resource ownership;
- inventory;
- equipment;
- movement;
- senses;
- environmental adaptation;
- relationships;
- ownership;
- progression;
- visibility;
- media attachment;
- runtime evaluation;
- installation and migration.

A module should be reused across object families where the behavior is genuinely the same.

## 34.7 Parameter sets

Parameter sets define reusable collections of typed values and constraints.

They may support:

- scale;
- movement;
- damage or recovery profiles;
- environmental tolerances;
- item dimensions;
- crew stations;
- ability costs;
- progression nodes;
- compatibility;
- visibility;
- content readiness.

Parameter sets must have clear units and validation rules. Similar-looking values with different meaning must not be merged merely to reduce field count.

## 34.8 Definition layer

A Definition is reusable governed content.

Examples include:

- Species Definition;
- Item Definition;
- Creature Definition;
- World Definition;
- Faction Definition;
- Ability Definition;
- Adventure Definition;
- Rules Profile;
- Media Asset Definition.

A Definition may be installed, referenced, extended, deprecated, migrated, and exported independently of any one campaign.

## 34.9 Placement and binding layer

A placement or binding establishes that a Definition participates in another governed context.

Examples include:

- an NPC archetype placed in an adventure;
- a creature placed in an encounter;
- a faction placed in a World;
- a location placed in a Region;
- an adventure placed in a Campaign;
- an item assigned to a loadout;
- a Media Asset attached to a subject.

Placements preserve both identities and define the relationship between them.

## 34.10 Instance and live-state layer

An instance represents a specific live entity or context.

Examples include:

- a player character;
- a campaign NPC;
- a specific item;
- a damaged vehicle;
- a live scene;
- a campaign faction state;
- a discovered clue;
- an active project.

An instance references reusable Definitions while adding mutable state, ownership, permissions, event position, and campaign context.

## 34.11 Event layer

An event is an immutable accepted occurrence.

Events should identify:

- event ID;
- aggregate or subject;
- actor;
- authority;
- event type;
- inputs;
- source rules;
- before-state fingerprint where required;
- result;
- applied changes;
- visibility;
- timestamp or sequence;
- schema and engine version;
- correlation and causation IDs.

Events are not arbitrary logs. They are evidence for accepted state changes.

## 34.12 Snapshot layer

A snapshot captures a recoverable projection at a known event position and version boundary.

A snapshot may include:

- aggregate identity;
- event cursor;
- current projection;
- installed pack versions;
- schema versions;
- compatibility information;
- checksums;
- recovery metadata.

Snapshots accelerate recovery but must not erase event history or provenance.

## 34.13 Overlay layer

A user-authored overlay adds information without changing canon.

Examples include:

- notes;
- tags;
- collections;
- theories;
- display preferences;
- private annotations;
- custom labels;
- campaign-local presentation.

Overlays must preserve their author, scope, visibility, and referenced canonical objects.

## 34.14 Relationship objects

A relationship should be explicit when it carries meaning beyond simple containment.

A relationship object or edge may identify:

- stable edge ID;
- source object;
- target object;
- relationship type;
- directionality;
- scope;
- conditions;
- visibility;
- validity interval;
- provenance;
- source events;
- extension fields.

Relationships must not depend solely on display-name matching.

## 34.15 References

References should use stable IDs and, where required, owner-pack or version context.

References may be:

- required;
- optional;
- weak or informational;
- deferred;
- external;
- role-filtered.

A missing required reference is a validation failure. A missing optional reference should produce defined degraded behavior.

## 34.16 Embedded content

A record may embed small value objects when they:

- have no independent identity;
- are owned exclusively by the parent;
- cannot be referenced independently;
- share the parent lifecycle;
- do not require separate provenance.

Content should be promoted to a separate canonical object when it requires independent:

- identity;
- ownership;
- versioning;
- references;
- migration;
- provenance;
- visibility;
- reuse.

## 34.17 Extensions

An extension adds governed fields or capabilities to an existing object type.

An extension must identify:

- target object type or capability;
- extension namespace;
- schema;
- compatibility;
- owner pack;
- migration;
- validation;
- collision behavior.

Extensions must not overwrite core fields silently.

## 34.18 Overrides and replacements

An override alters behavior in a declared context.

Overrides must be:

- explicit;
- scoped;
- attributable;
- versioned;
- reversible;
- ordered;
- validated.

A replacement should identify the superseded object and migration relationship.

A local campaign override must not rewrite the reusable global Definition.

## 34.19 Provenance

Provenance should answer:

- where the claim originated;
- how it was transformed;
- which candidate produced it;
- which record was promoted;
- which version changed it;
- who or what approved it;
- which conflicts or omissions remain.

Provenance is part of the object architecture, not an optional note.

## 34.20 Canon status and conversion status

Canon status and conversion status are separate.

A record may be:

- fully converted but not owner-approved canon;
- canonical but awaiting a newer schema migration;
- incomplete but still an authoritative source claim;
- deprecated but historically valid;
- campaign-local and never intended for global canon.

The exact status enums remain schema-controlled.

## 34.21 Completeness

Completeness is evaluated by object type and source availability.

A completeness result should identify:

- required fields present;
- conditionally required fields;
- missing source information;
- unresolved conflict;
- invalid mechanics;
- missing dependency;
- nonblocking recommendations;
- blocking failures.

A completeness score must not conceal a blocking missing field.

## 34.22 Deterministic fingerprints

A content fingerprint should be derived from canonicalized meaningful content and version context.

Fingerprints support:

- change detection;
- regression;
- backup integrity;
- migration;
- duplicate analysis;
- pack checksums;
- provenance.

Presentation-only changes should be distinguishable from mechanical or semantic changes where practical.

## 34.23 Serialization

Canonical serialized objects should be deterministic.

Deterministic serialization requires:

- stable field ordering or canonical encoding;
- normalized numbers and units;
- normalized null and omission behavior;
- deterministic collection ordering where order is not semantic;
- explicit schema version;
- no transient runtime fields in reusable content fingerprints.

## 34.24 Design Studio relationship

The canonical object program includes Design Studio form definitions.

A form definition should derive from the same schema and capability model used for validation.

The authoring UI must not maintain a second hidden object definition.

## 34.25 Runtime projection

The runtime may derive optimized projections, indexes, caches, summaries, or stat blocks.

Every projection must retain enough information to identify:

- source object;
- source version;
- applied extensions;
- applied templates;
- campaign overrides;
- current state;
- event position.

A projection is not a new canonical Definition unless promoted through governance.

## 34.26 Import boundary

Imported source data is not immediately canonical.

The import pipeline should distinguish:

- raw source;
- normalized claim;
- candidate;
- reconciled candidate;
- promoted canonical record;
- installed runtime projection.

Each transition should preserve identity and evidence.

## 34.27 Unknown fields

Unknown fields must not be silently discarded during import, migration, or provider exit.

The applicable policy may:

- reject the record;
- preserve an extension payload;
- quarantine it;
- require migration;
- record a warning.

The behavior must be deterministic and schema-governed.

## 34.28 AI boundary

AI may assist with:

- object classification;
- candidate extraction;
- field mapping;
- duplicate detection;
- provenance linking;
- completeness review;
- schema suggestions;
- fixture generation.

AI must not:

- merge variants silently;
- invent missing source facts;
- promote records without authority;
- alter stable IDs casually;
- discard unknown fields;
- treat a projection as canonical source.

## 34.29 Verified program baseline

The completed 8E-009 Canonical Object Template Program provides:

- canonical object-family hierarchy;
- parameter sets;
- capability modules;
- templates;
- validators;
- Design Studio form definitions;
- representative objects;
- governed conversion pipeline.

The final verified registry contains:

- 20 governed CSV datasets;
- 19,199 source rows;
- 19,199 promoted records;
- 19,199 deterministic canonical identities;
- zero unprocessed rows;
- zero partially processed datasets;
- passing cross-dataset identity and source-coordinate uniqueness;
- passing provenance preservation;
- passing runtime contract validation;
- passing install and uninstall validation;
- zero uninstall residue.

The final reconciliation artifact is protected by SHA-256 `112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40`.

## 34.30 Controlling references

- `governance/object-system/CANONICAL_OBJECT_TEMPLATE_PROGRAM.md`
- Canonical Object Specification
- Canonical Object Template Program artifacts
- Master Game Object Catalog
- capability and parameter registries
- completeness profiles
- Design Studio form definitions
- source registry and mapping contracts
- relationship and provenance validators
- 8E-009 completion governance and reconciliation artifacts

**Status:** Canonical and validated object-system foundation.

---

# 35. Stable Identifiers

## 35.1 Purpose

Define identity rules that allow objects, relationships, events, packs, sources, instances, and migrations to remain referentially stable across renaming, reorganization, localization, provider changes, and version upgrades.

## 35.2 Identity principle

A stable ID identifies a concept or governed record, not its current display name, file path, database row, provider key, or UI location.

Stable IDs must survive:

- spelling corrections;
- display-name changes;
- file moves;
- repository restructuring;
- storage-provider migration;
- localization;
- asset replacement;
- pack repackaging;
- nonidentity field changes.

## 35.3 ID domains

Distinct ID domains should exist for concepts with different lifecycles.

Examples include:

- canonical object IDs;
- pack IDs;
- source IDs;
- source-coordinate IDs;
- candidate IDs;
- relationship IDs;
- campaign IDs;
- instance IDs;
- event IDs;
- snapshot IDs;
- account or identity subject IDs;
- export IDs;
- backup IDs;
- migration IDs.

One identifier should not be reused across unrelated identity domains.

## 35.4 Canonical object IDs

Canonical object IDs identify reusable governed records.

They should be:

- globally unique within the Multiversal namespace;
- deterministic when derived from governed source coordinates or approved authoring rules;
- opaque enough not to require renaming when display labels change;
- readable enough for diagnostics where the canonical standard permits;
- validated against type and namespace rules.

## 35.5 Human-readable segments

Human-readable segments may improve diagnostics, but they must not become the sole identity source.

When a readable segment conflicts with identity continuity, continuity controls.

A renamed object should normally retain the same stable ID and add the former name as an alias or historical label.

## 35.6 Source-derived identities

Source-derived identities should use normalized, registered source coordinates.

A source coordinate may include:

- source registry ID;
- file or logical source;
- sheet, table, page, section, or row;
- local record key;
- source version;
- conversion fingerprint.

The derivation must avoid collisions across files, datasets, and versions.

## 35.7 Candidate identity

A candidate receives identity before final promotion so that review, conflict handling, provenance, and deferred processing remain traceable.

Candidate identity must not be confused with the eventual canonical stable ID when reconciliation determines the candidate is:

- an alias;
- a variant;
- a duplicate;
- a conflict;
- a replacement;
- a separate concept.

## 35.8 Promotion identity

Promotion should either:

- retain the approved deterministic identity; or
- create an explicit candidate-to-canonical mapping.

Promotion must not orphan the candidate provenance.

## 35.9 Duplicate names

Duplicate display names are permitted when they represent different concepts.

Disambiguation may use:

- object type;
- owner pack;
- setting;
- source;
- subtype;
- parent;
- variant;
- version.

The system must not merge records merely because their names match.

## 35.10 Aliases

Aliases support search and source fidelity.

An alias may identify:

- alternate spelling;
- former name;
- source label;
- abbreviation;
- transliteration;
- localization;
- nickname;
- legacy ID mapping.

Aliases do not become independent canonical identities unless the underlying concept is distinct.

## 35.11 Variants

A variant receives its own stable ID when it has independently referencable identity or lifecycle.

The relationship to the base object should be explicit.

A variant ID must not be generated by mutating the base ID in an ungoverned way.

## 35.12 Relationship IDs

Relationships that carry provenance, state, visibility, or independent references should have stable edge IDs.

An edge ID may be deterministic from:

- source;
- target;
- relationship type;
- scope;
- source coordinate;
- version context.

Two edges between the same entities may coexist when their type, direction, scope, source, or validity differs.

## 35.13 Instance IDs

Live instances receive unique identity separate from their Definitions.

Two item instances based on the same Item Definition must have different instance IDs when they can carry different:

- owners;
- condition;
- modifications;
- history;
- location;
- visibility.

## 35.14 Event IDs

Event IDs must support:

- uniqueness;
- idempotency;
- ordering or sequence association;
- correlation;
- causation;
- audit;
- replay.

An event retry must not accidentally create a second accepted event when the original was already committed.

## 35.15 Provider identifiers

Provider-specific IDs are mappings, not canonical identity.

An identity mapping should preserve:

- internal stable subject ID;
- provider;
- provider subject;
- tenancy or environment;
- created and revoked status;
- provenance.

Provider exit must retain internal identities even when provider mappings are removed.

## 35.16 Version identity

Object identity and object version are separate.

A content update normally retains stable ID and increments content or release version.

A new stable ID is required when the concept itself is intentionally distinct or when migration cannot preserve identity semantics.

## 35.17 Supersession

Supersession should record:

- old stable ID;
- replacement stable ID;
- reason;
- effective version;
- migration;
- compatibility;
- retained history.

Superseded IDs must remain resolvable for imports, history, and migration where policy permits.

## 35.18 Tombstones

A tombstone preserves the fact that an ID existed even when the record is withdrawn or unavailable.

A tombstone may identify:

- ID;
- former type;
- withdrawal reason;
- replacement;
- last known version;
- visibility or legal restrictions;
- migration guidance.

Tombstones prevent accidental ID reuse.

## 35.19 Namespace governance

Namespaces must be centrally governed.

A namespace should identify:

- owner;
- allowed object types;
- format;
- collision rules;
- reserved segments;
- extension policy;
- deprecation policy.

Third-party or campaign-local content should use assigned namespaces rather than imitating official IDs.

## 35.20 Campaign-local IDs

Campaign-local content may use a campaign-scoped namespace.

Export and promotion must preserve the original campaign-local identity and create an explicit mapping when promoted to shared canon.

## 35.21 Deterministic generation

A deterministic ID algorithm should declare:

- input fields;
- normalization;
- namespace;
- hash or encoding;
- algorithm version;
- collision policy;
- migration behavior.

Changing the algorithm requires a governed migration and retained legacy mappings.

## 35.22 Collision handling

A collision must never be resolved by silent overwrite.

The system should:

1. detect the collision;
2. compare source and semantic identity;
3. determine duplicate, alias, variant, or conflict;
4. preserve both claims;
5. create an explicit mapping or new identity;
6. record the decision;
7. rerun uniqueness validation.

## 35.23 Referential integrity

References should be validated for:

- existence;
- expected type;
- owner pack;
- version compatibility;
- visibility where relevant;
- lifecycle status;
- migration.

A reference to a deprecated object may remain valid when compatibility policy permits.

## 35.24 Identity reconciliation

Cross-file reconciliation should detect:

- exact duplicate coordinates;
- duplicate names;
- likely aliases;
- variants;
- conflicting records;
- split records;
- merged concepts;
- external references.

The 8E-009 program completed cross-dataset identity and source-coordinate uniqueness across all 20 governed datasets.

## 35.25 Export and backup identity

Backup, restore, and provider-exit export must preserve:

- stable IDs;
- provider mappings;
- ownership;
- relationships;
- event references;
- schema versions;
- source and provenance;
- tombstones and supersession mappings where required.

An import must not generate replacement IDs merely because the storage provider changed.

## 35.26 Search and display

Search may show human-readable names and context, but selection and internal references use stable IDs.

UI components must not persist only display text for object references.

## 35.27 AI boundary

AI may suggest:

- likely duplicate identities;
- alias mappings;
- variant relationships;
- namespace classification;
- collision review packets.

AI must not:

- reassign stable IDs casually;
- merge identities without evidence;
- reuse tombstoned IDs;
- generate official namespaces without authority;
- hide collisions.

## 35.28 Controlling references

- Canonical ID standard
- CSV Source Registry
- Mapping Contract Registry
- identity reconciliation reports
- source-coordinate uniqueness validators
- relationship schemas
- pack ownership maps
- migration and supersession maps
- provider-neutral identity service contracts

**Status:** Canonical and validated identity architecture.

---

# 36. Schemas and Validation

## 36.1 Purpose

Define how machine-readable contracts, validators, fixtures, reports, and CI enforce canonical structure and prevent invalid or ambiguous content from silently entering the project.

## 36.2 Schema principle

A schema is an executable contract for data shape and basic constraints.

A schema does not by itself prove:

- source truth;
- semantic correctness;
- canon approval;
- balance;
- permission safety;
- compatibility;
- release readiness.

Validation therefore occurs in layers.

## 36.3 Schema responsibilities

A schema may enforce:

- required fields;
- field types;
- enumerations;
- formats;
- numeric bounds;
- array cardinality;
- object structure;
- conditional requirements;
- additional-property policy;
- references by pattern;
- version fields.

Semantic and cross-record rules may require dedicated validators beyond the schema language.

## 36.4 Schema versioning

Every governed record or package should identify the schema version it follows.

Schema changes should be classified as:

- backward compatible;
- conditionally compatible;
- migration required;
- breaking;
- deprecated.

A breaking schema change requires migration and compatibility guidance.

## 36.5 Content versioning

Content version and schema version are separate.

A record may change content without changing schema. A schema may change without altering the semantic content.

Validators must not infer one from the other.

## 36.6 Strictness

Production canonical schemas should reject unknown fields unless an explicit extension mechanism exists.

Loose ingestion formats may preserve unknown source fields, but promotion must either:

- map them;
- preserve them in a governed extension;
- quarantine them;
- record them as unprocessed.

Silent field loss is prohibited.

## 36.7 Structural validation

Structural validation checks:

- parseability;
- required fields;
- types;
- formats;
- enums;
- bounds;
- conditional shape;
- duplicate keys;
- canonical serialization requirements.

## 36.8 Identity validation

Identity validation checks:

- stable-ID format;
- namespace ownership;
- uniqueness;
- tombstone reuse;
- candidate mapping;
- source-coordinate uniqueness;
- relationship-edge uniqueness where required.

## 36.9 Reference validation

Reference validation checks:

- target exists;
- expected object type;
- owner pack;
- dependency declared;
- version compatible;
- lifecycle status;
- optional-reference behavior;
- no forbidden circular relationship.

## 36.10 Provenance validation

Provenance validation checks:

- source registry entry;
- source coordinate;
- source hash or version;
- transformation history;
- candidate relationship;
- promotion mapping;
- conflict or missing-information status;
- release fingerprint.

## 36.11 Semantic validation

Semantic validation checks rules that are not expressible as simple schema constraints.

Examples include:

- resource minimum not greater than maximum;
- mutually exclusive progression nodes;
- valid action timing;
- condition lifecycle completeness;
- container cycle prevention;
- compatible component graph;
- valid setting hierarchy;
- adventure route reachability;
- role-filtered clue visibility;
- nonduplicated pack ownership;
- no unresolved required mechanic.

## 36.12 Runtime contract validation

Runtime validation confirms that records can participate in approved execution contracts.

It may test:

- action declaration;
- validation failure;
- deterministic resolution;
- effect application;
- condition lifecycle;
- resource mutation;
- progression;
- relationship projection;
- environment evaluation;
- installation;
- migration;
- removal;
- replay.

## 36.13 Permission validation

Permission validation checks that protected information cannot leak through:

- APIs;
- queries;
- search;
- projections;
- exports;
- AI context;
- notifications;
- caches;
- errors;
- fixtures.

Permission tests require both allowed and denied cases.

## 36.14 Pack validation

Pack validation checks:

- archive structure;
- manifest;
- index;
- checksums;
- owned-record counts;
- one-owner rule;
- dependencies;
- install order;
- schemas;
- compatibility;
- migration;
- uninstall behavior;
- zero residue where removal should be complete.

## 36.15 Migration validation

Migration validation checks:

- supported source version;
- target version;
- stable-ID continuity;
- transformed fields;
- preserved provenance;
- preserved unknown or extension data;
- live-state compatibility;
- rollback or recovery;
- deterministic receipts.

## 36.16 Completeness validation

Completeness validation uses object-type profiles.

It should report:

- blocking failures;
- missing source fields;
- conditional requirements;
- recommendations;
- nonapplicable fields;
- source-unavailable fields;
- score or summary where useful.

A record with a high score may still fail if one critical field is missing.

## 36.17 Coverage validation

Coverage validation compares registered source units with promoted or deferred results.

It should identify:

- total source units;
- processed units;
- promoted records;
- deferred units;
- conflicts;
- missing fields;
- unprocessed units;
- duplicate coordinates;
- unsupported domains.

The 8E-009 final state records zero unprocessed rows across 19,199 source rows.

## 36.18 Deterministic fixtures

A fixture should have:

- stable fixture ID;
- purpose;
- inputs;
- versions;
- expected result;
- expected warnings or failures;
- deterministic randomness when used;
- provenance;
- update policy.

Fixtures should include valid and invalid cases.

## 36.19 Representative fixtures

Representative fixtures should cover:

- simple records;
- complex records;
- modular records;
- magical records;
- technological records;
- living entities;
- vehicles;
- mecha;
- spacecraft;
- abilities;
- spells;
- hazards;
- traps;
- weapons;
- ammunition;
- facilities;
- materials;
- software.

This coverage reflects the governed golden-corpus program.

## 36.20 Golden baselines

A golden baseline protects approved expected behavior.

Updating a baseline requires:

- identified reason;
- reviewed change;
- compatibility assessment;
- approval;
- retained previous baseline;
- new fingerprint.

A failing test must not be resolved by automatically regenerating expected output.

## 36.21 Validator outputs

A validator should produce machine-readable and human-readable output.

A result should identify:

- validator name and version;
- subject;
- status;
- errors;
- warnings;
- evidence;
- affected paths or IDs;
- remediation guidance;
- timestamp;
- input fingerprint.

## 36.22 Severity

Validation findings may be classified as:

- error;
- warning;
- advisory;
- insufficient evidence;
- owner decision required.

Exact enums remain validator-controlled.

A warning must not silently become a pass when the release gate treats it as blocking.

## 36.23 Enforceability

A validator is enforceable when it is:

- version controlled;
- deterministic;
- invoked by documented commands;
- included in CI where required;
- tested against fixtures;
- capable of failing the workflow;
- not dependent on hidden manual state.

## 36.24 Dedicated CI

Major governed contracts should have dedicated CI.

Dedicated CI should:

- run on relevant changes;
- install pinned dependencies;
- validate fixtures;
- produce clear logs;
- fail on contract violations;
- avoid production credentials;
- preserve artifacts when useful;
- remain reproducible locally where practical.

## 36.25 Validator independence

Where risk warrants, validation should not rely only on the same code that generated the artifact.

Independent checks help detect generator and validator sharing the same mistake.

## 36.26 Validation ordering

An efficient validation order is:

1. parse and structural schema;
2. identity;
3. references and dependencies;
4. provenance;
5. semantic rules;
6. runtime contracts;
7. migration;
8. install and uninstall;
9. golden regression;
10. balance observations;
11. release gates.

Early failures should prevent misleading downstream results while still reporting enough context for repair.

## 36.27 Repair workflow

When validation fails:

1. inspect the exact failing check;
2. determine root cause;
3. correct the source, mapping, schema, fixture, validator, or migration;
4. rerun the smallest relevant checks;
5. rerun the full required suite;
6. preserve the correction evidence;
7. continue automatically unless an owner-only decision is reached.

## 36.28 CI truthfulness

A local validator pass is not a CI pass.

A workflow started is not a successful workflow.

A PR with green checks is not merged.

Reports must distinguish each evidence level.

## 36.29 Validation artifacts

Useful validation artifacts may include:

- JSON reports;
- coverage matrices;
- reconciliation ledgers;
- dependency graphs;
- ownership maps;
- migration receipts;
- replay bundles;
- failure fixtures;
- release summaries;
- checksums.

Artifacts should be deterministic and linked to the input commit or release.

## 36.30 Performance

Validation should remain bounded and efficient.

Large programs may use:

- changed-file targeting;
- cached schema compilation;
- deterministic batching;
- parallel independent checks;
- smoke and full profiles;
- retained golden results.

Optimization must not weaken required gates.

## 36.31 AI boundary

AI may:

- draft schemas;
- propose validators;
- triage failures;
- generate fixtures;
- explain reports;
- suggest repairs.

AI must not:

- suppress failures;
- regenerate baselines without review;
- convert warnings into passes;
- invent provenance;
- claim CI success without evidence;
- weaken schema strictness solely to accept bad input.

## 36.32 Verified validation baseline

The completed canonical-object program validates:

- templates;
- provenance;
- relationships;
- runtime contracts;
- installation;
- uninstallation;
- cross-dataset identity;
- source-coordinate uniqueness.

The Phase 8 final state records zero uninstall residue.

The golden-corpus and balance-harness program adds deterministic regression, replay, domain, cross-domain, simulation, and review validation.

## 36.33 Controlling references

- canonical schemas and validators
- Design Studio form definitions
- Mapping Contract Registry
- Template Coverage Matrix
- provenance and relationship validators
- 8E-008 final validation releases
- 8E-009 completion governance
- 8D-007 golden corpus and balance harness
- repository CI workflows and validation scripts

**Status:** Canonical and operational validation architecture.

---

# 37. Pack Format and Lifecycle

## 37.1 Purpose

Define the canonical `.pack` container, its required metadata, deterministic assembly, dependency behavior, installation, update, migration, uninstallation, export, and recovery lifecycle.

## 37.2 Pack principle

A pack is a governed installable unit of reusable content and supporting metadata.

A pack is not:

- a live campaign;
- a database backup;
- an arbitrary ZIP;
- a folder copied into the application;
- a license grant by itself;
- proof of canon approval;
- a provider-specific deployment artifact.

## 37.3 File extension

The approved public extension is:

`.pack`

The manifest declares the pack’s role and content. Separate extensions for creature, world, item, or adventure packs are not required.

## 37.4 Container

A `.pack` may use a deterministic archive format.

The archive should have:

- canonical path normalization;
- deterministic file ordering;
- normalized timestamps where applicable;
- defined compression behavior;
- no unexpected executable content;
- integrity checksums;
- manifest at a known path.

Exact binary packaging rules remain controlled by the pack specification.

## 37.5 Pack identity

A pack has stable pack identity separate from filename and download URL.

The pack identity should survive:

- storage migration;
- repository moves;
- renaming;
- mirrors;
- provider exit.

A fork or independently owned derivative requires distinct identity unless governed as a version or extension of the original pack.

## 37.6 Pack version

Pack version identifies a release of the pack.

Versioning should communicate:

- compatible content updates;
- schema changes;
- migration requirements;
- breaking changes;
- prerelease status.

The exact versioning convention remains controlled by the pack standard.

## 37.7 Manifest

The manifest should identify, as applicable:

- pack ID;
- display name;
- version;
- role or classification;
- owner and authority;
- license;
- schema and contract versions;
- minimum application compatibility;
- required dependencies;
- optional dependencies;
- conflicts;
- owned-record index;
- source registry;
- media index;
- localization index;
- migration routes;
- install and uninstall behavior;
- checksums;
- release and canon status;
- support blockers;
- creation and build metadata.

## 37.8 Indexes

A pack may include specialized indexes for:

- records;
- sources;
- media;
- localization;
- relationships;
- dependencies;
- migrations;
- search;
- fixtures.

Indexes must agree with the manifest and content hashes.

## 37.9 Owned records

The pack owns the reusable records it publishes.

Ownership should be deterministic and validated against the installed registry.

The installer must reject two active packs claiming the same canonical record unless a governed replacement or extension rule applies.

## 37.10 Dependencies

Dependencies should identify:

- target pack ID;
- compatible version range;
- required or optional status;
- reason;
- referenced records;
- fallback behavior.

A dependency must not be inferred solely from unresolved runtime references after installation.

## 37.11 Conflicts

A pack may declare known conflicts.

A conflict declaration should identify:

- conflicting pack;
- affected versions;
- reason;
- whether coexistence is impossible or degraded;
- remediation.

The installer should also detect undeclared ownership or compatibility conflicts.

## 37.12 Content

Pack content may include:

- canonical record streams;
- schemas or schema references;
- source and provenance metadata;
- relationships;
- rules profiles;
- media references or assets;
- localization;
- fixtures;
- migration scripts or declarative migrations;
- documentation;
- release notes.

Executable code should be prohibited or tightly governed according to the application security policy.

## 37.13 Deterministic assembly

Given the same source inputs, tool versions, configuration, and build profile, pack assembly should produce the same logical content and checksums.

Build metadata that necessarily varies must be excluded from semantic fingerprints or normalized.

## 37.14 Pack signing

A future release policy may require signatures or attestations.

A signature verifies the relationship between bytes and a signing identity. It does not by itself prove:

- canon approval;
- source fidelity;
- rights;
- safety;
- compatibility.

Production signing authority remains an owner-controlled release concern.

## 37.15 Preinstallation validation

Before installation, the application should verify:

1. archive safety;
2. manifest schema;
3. checksums;
4. pack identity and version;
5. dependencies;
6. conflicts;
7. record schemas;
8. stable IDs;
9. ownership;
10. provenance requirements;
11. compatibility;
12. migration availability.

## 37.16 Installation plan

Installation should first create a plan.

The plan should identify:

- new packs;
- required dependencies;
- optional features;
- upgrades;
- migrations;
- conflicts;
- disk or storage impact;
- records added;
- records replaced or deprecated;
- live-state risks;
- required approvals.

Planning must not mutate state.

## 37.17 Installation execution

Execution should:

- use the validated plan;
- verify the expected installed-state fingerprint;
- apply operations in dependency order;
- write definitions and indexes;
- register ownership;
- record installed versions;
- emit receipts;
- avoid creating campaign state;
- fail safely.

## 37.18 Installation receipt

A receipt should identify:

- operation ID;
- actor;
- time;
- plan fingerprint;
- installed pack IDs and versions;
- records added;
- migrations;
- warnings;
- final registry fingerprint;
- validator results.

## 37.19 Idempotency

Repeating an already completed installation request should not duplicate records or create inconsistent ownership.

The result should report that the requested state is already satisfied or return the original operation outcome where appropriate.

## 37.20 Update planning

An update plan should compare:

- installed version;
- target version;
- dependencies;
- schema changes;
- record changes;
- migrations;
- deprecations;
- removals;
- live references;
- compatibility;
- rollback or recovery path.

## 37.21 Definition update boundary

Updating a pack may change reusable Definitions.

It must not silently reset:

- campaign placements;
- live instances;
- ownership;
- reputation;
- discovered information;
- objective state;
- damage;
- project progress;
- timeline divergence.

A migration must explicitly handle affected live state.

## 37.22 Migration

A migration may be:

- declarative;
- executable under a restricted governed runtime;
- application-provided;
- manual owner-reviewed.

A migration should define:

- source and target versions;
- preconditions;
- transformations;
- stable-ID mappings;
- extension handling;
- validation;
- failure behavior;
- receipt;
- recovery.

## 37.23 Rollback and recovery

A failed install or update should:

- leave no partial unreported registry;
- roll back atomically where practical;
- otherwise apply compensation;
- preserve diagnostic evidence;
- produce a failure receipt;
- allow retry after repair.

## 37.24 Uninstallation planning

Uninstallation planning should identify:

- pack and dependents;
- owned records;
- active references;
- campaign placements;
- live instances;
- historical events;
- snapshots;
- exports required;
- removable caches or media;
- blockers.

## 37.25 Uninstallation execution

Uninstallation may:

- remove unused reusable definitions;
- unregister ownership;
- remove derived indexes;
- retain tombstones;
- preserve live snapshots;
- preserve history;
- block unsafe removal;
- archive dependent campaign material.

It must not silently destroy user-owned or campaign state.

## 37.26 Zero residue

Where complete removal is allowed, validation should confirm zero unintended residue.

Intended retained artifacts such as:

- receipts;
- tombstones;
- history;
- exported snapshots;

must be classified separately from residue.

The 8E-009 program verified zero uninstall residue for its governed test path.

## 37.27 Reinstallation

Reinstallation should preserve identity and correctly reconnect compatible retained state.

It must not create duplicate definitions or instances.

## 37.28 Pack registry

The installed pack registry should record:

- pack ID;
- version;
- state;
- install receipt;
- dependencies;
- content fingerprint;
- source or origin;
- update availability;
- compatibility;
- last validation;
- deprecation;
- removal state.

The registry must be exportable and provider-neutral.

## 37.29 Quarantine

A pack may be quarantined when:

- integrity fails;
- schema is unsupported;
- malware or unsafe content is suspected;
- ownership conflicts;
- migration fails;
- provenance is insufficient;
- rights or policy blocks release.

Quarantine prevents activation while preserving evidence.

## 37.30 Offline behavior

Pack installation and use should support local operation when dependencies are locally available and no provider-only operation is required.

Offline mode must not bypass:

- integrity;
- licensing;
- entitlement;
- permissions;
- compatibility;
- validation.

## 37.31 Entitlement boundary

Entitlement controls whether a user may access or activate content.

Entitlement does not:

- change pack identity;
- change canon status;
- create in-world ownership;
- delete historical campaign references.

Expired entitlement behavior must preserve recovery and export obligations.

## 37.32 Provider exit

Provider-exit export should preserve:

- pack registry;
- pack identities and versions;
- owned-record indexes;
- dependency graph;
- content or lawful retrieval references;
- checksums;
- source and provenance;
- migration history;
- install receipts;
- entitlement metadata;
- compatibility;
- recovery information.

Provider exit must not depend on the continuing operation of the original hosted provider.

## 37.33 Backup and restore

A backup should capture enough pack state to restore:

- installed registry;
- versions;
- dependencies;
- compatible content;
- migrations;
- campaign references;
- receipts;
- integrity evidence.

Restore must validate that required pack versions or lawful equivalent content are available.

## 37.34 Pack release states

A pack may move through states such as:

- draft;
- assembled;
- validation failed;
- validated;
- internal;
- playtest;
- release candidate;
- approved;
- deprecated;
- withdrawn;
- archived.

Exact enums remain schema-controlled.

A validated pack is not automatically approved for public release.

## 37.35 Release bundle

A release bundle may contain:

- `.pack` file;
- checksum;
- signature or attestation where required;
- release notes;
- migration notes;
- compatibility report;
- validation report;
- license and attribution;
- support blockers;
- source and provenance report.

## 37.36 CI

Pack CI should validate:

- deterministic assembly;
- schemas;
- references;
- dependency graph;
- ownership;
- checksums;
- fixtures;
- install;
- update;
- migration;
- uninstall;
- reinstallation;
- role-filtered visibility;
- export.

## 37.37 Security

Pack processing must defend against:

- path traversal;
- archive bombs;
- duplicate-path tricks;
- malformed encodings;
- unsafe executable content;
- malicious schemas or migrations;
- content spoofing;
- signature confusion;
- hidden network access.

## 37.38 AI boundary

AI may:

- draft manifests;
- analyze dependencies;
- prepare release notes;
- identify conflicts;
- generate fixtures;
- explain install plans.

AI must not:

- sign releases;
- weaken validation;
- bypass entitlement;
- install untrusted packs silently;
- discard blockers;
- approve public release.

## 37.39 Controlling references

- canonical `.pack` standard
- pack manifest and index schemas
- record ownership maps
- dependency graphs
- install-order fixtures
- migration and supersession maps
- compatibility matrices
- install and uninstall validators
- 8E-006F and 8E-006G release architecture
- 8E-008 final validation
- 8E-009 canonical-object lifecycle validation
- P9-06 persistence, migration, backup, restore, and export contracts

**Status:** Canonical pack lifecycle architecture; production signing, distribution, and public publishing remain gated.



# 38. Dependencies, Extensions, and Overrides

## 38.1 Purpose

Define how governed content depends on, extends, specializes, replaces, or contextually alters other content while preserving one owner per reusable record, deterministic compatibility, migration, and explainability.

## 38.2 Dependency principle

A dependency is an explicit requirement or optional relationship between governed units.

Dependencies must be declared before runtime failure reveals them.

A dependency should identify:

- requesting pack or record;
- required pack or record;
- version or compatibility range;
- required or optional status;
- reason;
- affected capabilities;
- fallback or degraded behavior;
- migration implications;
- provenance.

## 38.3 Dependency levels

Dependencies may exist at several levels:

### Pack dependency

A pack requires or optionally integrates another pack.

### Record dependency

A record references another canonical record.

### Capability dependency

A record requires a capability, extension, rules profile, or runtime service.

### Runtime dependency

A live operation requires installed content, an active provider-neutral port, a compatible schema, or an authoritative session state.

### Release dependency

A release gate depends on evidence, validation, migration, rights, or owner approval.

These levels should not be collapsed into a single untyped reference.

## 38.4 Required dependencies

A required dependency must be present and compatible before the dependent content is activated.

Failure behavior should identify:

- missing dependency;
- required version;
- requesting subject;
- blocked capability;
- remediation.

The system must not create a local copy of the missing dependency to make validation pass.

## 38.5 Optional dependencies

An optional dependency may enable enhanced behavior.

The dependent content must define what happens when the optional dependency is absent.

Valid degraded behavior may include:

- omitted optional content;
- reduced search results;
- unavailable optional scenes;
- fallback presentation;
- disabled optional integration.

Optional absence must not produce unresolved required references.

## 38.6 Weak and informational references

Some references are informational and do not block installation or use.

Examples may include:

- related lore;
- suggested content;
- external bibliography;
- optional media;
- nonmechanical cross-links.

Weak references must still preserve stable identity and visibility rules where available.

## 38.7 Dependency graph

The dependency graph must be:

- explicit;
- version-aware;
- deterministic;
- cycle-checked;
- inspectable;
- exportable;
- validated before activation.

A graph view is a projection. The canonical dependency records remain the authority.

## 38.8 Cycles

Circular dependencies are rejected unless a governed architecture explicitly permits and resolves them.

Permitted strategies may include:

- extracting shared content into a framework pack;
- replacing hard dependencies with optional integrations;
- defining a neutral interface contract;
- splitting record ownership;
- using deferred bindings.

A cycle must not be hidden by install-order tricks.

## 38.9 Version ranges

A version range should communicate tested compatibility.

It should not claim compatibility merely because a package installs.

Compatibility should consider:

- schema;
- content contracts;
- stable IDs;
- migrations;
- runtime behavior;
- extension points;
- validation evidence.

## 38.10 Dependency locking

A release, backup, snapshot, or replay may lock exact versions to preserve deterministic behavior.

A normal installation may use compatible ranges.

The system must distinguish:

- declared compatible range;
- currently resolved version;
- exact version required for replay or restore;
- replacement or migration path.

## 38.11 Extension principle

An extension adds governed capability or data without becoming a competing owner of the base record.

An extension should identify:

- extension ID;
- owner pack;
- target type, object, or capability;
- extension schema;
- compatibility;
- activation condition;
- priority or ordering if relevant;
- migration;
- provenance.

## 38.12 Extension namespaces

Extensions must use governed namespaces.

A namespace prevents two independent packs from using the same field name or extension identity with incompatible meanings.

The extension registry should identify:

- namespace owner;
- permitted targets;
- schema locations;
- compatibility policy;
- collision behavior;
- deprecation policy.

## 38.13 Type extensions

A type extension adds a reusable specialization to an object family.

Examples may include:

- setting-specific item properties;
- a new operational-asset subsystem;
- a domain-specific creature capability;
- an adventure-specific scene extension;
- a media or localization extension.

The extension must preserve the base object contract.

## 38.14 Instance extensions

A campaign or runtime extension may attach context-specific state to an instance.

Instance extensions must preserve:

- campaign scope;
- author or source;
- visibility;
- lifecycle;
- migration;
- export behavior.

An instance extension must not be mistaken for a global change to the Definition.

## 38.15 Capability extensions

A capability extension adds behavior through shared interfaces.

It may supply:

- Actions;
- Effects;
- Conditions;
- Resources;
- rules profiles;
- validators;
- presentation adapters.

Capability extensions must not bypass the common runtime lifecycle.

## 38.16 Overrides

An override intentionally changes a value or behavior within a declared scope.

An override should identify:

- target;
- field or rule;
- original value or behavior;
- new value or behavior;
- scope;
- source;
- priority;
- duration;
- compatibility;
- visibility;
- reason;
- migration or reversal.

## 38.17 Override scopes

Override scopes may include:

- pack;
- world;
- setting layer;
- adventure;
- campaign;
- scene;
- character;
- instance;
- temporary effect;
- GM adjudication.

A narrow override must not leak into broader scope.

## 38.18 Override ordering

When multiple overrides may apply, ordering must be deterministic.

Ordering may consider:

- scope specificity;
- explicit priority;
- dependency order;
- event time;
- rules profile;
- owner-approved precedence.

The system must detect unresolved equal-priority conflicts.

## 38.19 Replacement

A replacement declares that a new record supersedes another record.

Replacement should preserve:

- former stable ID;
- replacement ID;
- reason;
- effective version;
- compatibility;
- migration;
- retained history;
- dependency impact.

A replacement is not the same as an override.

## 38.20 Patch content

A patch pack may provide corrections or replacements when governed.

A patch pack should:

- declare its target packs and versions;
- identify each changed record;
- preserve source and approval;
- define migration;
- include validation;
- avoid claiming ownership of unrelated records;
- remain removable only when reversal is safe.

## 38.21 Local campaign alterations

Campaign-local alterations may change:

- NPC state;
- item state;
- faction relationships;
- world state;
- adventure structure;
- house rules;
- scene content.

They should be represented as:

- events;
- campaign-local Definitions;
- placements;
- extensions;
- overrides.

They must not modify the installed reusable source pack in place.

## 38.22 House rules

A house rule is a campaign-scoped or user-scoped rules override.

A house-rule record should identify:

- base rule;
- changed behavior;
- campaign;
- owner or GM authority;
- affected content;
- visibility;
- compatibility;
- test or preview result;
- activation and deactivation;
- migration and export.

House rules should be visible to affected participants.

## 38.23 Conflict detection

The system should detect:

- duplicate record ownership;
- incompatible extension namespaces;
- overlapping overrides;
- unresolvable version ranges;
- cycles;
- missing targets;
- replaced but still required records;
- incompatible migrations;
- hidden optional dependency becoming required.

## 38.24 Conflict resolution

A conflict may be resolved by:

- selecting compatible versions;
- disabling an optional extension;
- applying an approved patch;
- migrating;
- changing install plan;
- recording a campaign override;
- requiring owner review.

The resolver must not choose silently when more than one materially different result is possible.

## 38.25 Explainability

A resolved projection should be able to explain:

- base record;
- owner pack;
- extensions applied;
- overrides applied;
- ordering;
- replacement or migration;
- final value or capability;
- relevant versions;
- campaign-local changes.

## 38.26 Validation

Dependency and extension validation should test:

- graph resolution;
- version compatibility;
- namespace uniqueness;
- extension schema;
- target compatibility;
- ordering;
- collision behavior;
- optional-dependency absence;
- migration;
- uninstall;
- export;
- deterministic projection.

## 38.27 AI boundary

AI may:

- analyze dependency graphs;
- propose cycle breaks;
- identify likely extension points;
- prepare compatibility reports;
- explain applied overrides.

AI must not:

- choose an incompatible version silently;
- invent a dependency;
- hide a cycle;
- overwrite base ownership;
- activate a house rule without authority;
- resolve a material conflict without evidence or approval.

## 38.28 Controlling references

- pack dependency graphs
- record ownership maps
- extension registries
- compatibility matrices
- migration and supersession maps
- canonical object capability modules
- item template extension registry
- 8E-007 consolidation releases
- 8E-008 final validation
- provider-neutral service port contracts

**Status:** Canonical dependency, extension, and override architecture.

---

# 39. Provenance and Coverage

## 39.1 Purpose

Define the evidence chain that connects legacy source claims, normalized candidates, canonical records, packs, runtime projections, and releases while measuring what has and has not been recovered.

## 39.2 Provenance principle

Every canonical source-derived claim should be traceable to its origin and transformation history.

Provenance must survive:

- normalization;
- deduplication;
- variant handling;
- schema migration;
- pack assembly;
- provider migration;
- backup and restore;
- export;
- deprecation.

## 39.3 Source registry

A source registry entry should identify:

- stable source ID;
- logical source;
- physical file;
- version;
- hash;
- format;
- authority;
- provenance-only or active-source status;
- ingestion date;
- extraction method;
- known limitations;
- rights or restrictions;
- related sources.

## 39.4 Source coordinates

A source coordinate identifies the exact source location of a claim.

Coordinates may include:

- file;
- page;
- section;
- table;
- row;
- column;
- cell;
- object;
- paragraph;
- image region;
- PDF coordinate;
- archive member.

Coordinates should be stable enough to support reinspection.

## 39.5 Raw preservation

Raw source values should be retained when normalization could obscure:

- spelling;
- punctuation;
- units;
- formatting;
- ambiguity;
- contradictory values;
- embedded notes;
- source errors.

Normalized values should link back to raw values.

## 39.6 Candidate provenance

A candidate should identify:

- source coordinate;
- extraction tool or method;
- raw claim;
- normalized claim;
- proposed domain;
- proposed type;
- candidate ID;
- confidence or review status;
- related candidates;
- conflicts;
- missing fields.

## 39.7 Promotion provenance

A promoted record should identify:

- candidate or candidates used;
- mapping contract;
- transformation;
- canonical stable ID;
- reviewer or automated approval path;
- release;
- source fingerprints;
- unresolved issues;
- validation result.

## 39.8 Multi-source records

A record may be supported by multiple sources.

The provenance model should preserve:

- each source claim;
- authority;
- agreement or conflict;
- which fields each source supports;
- selected canonical interpretation;
- decision rationale.

The system must not collapse multiple source claims into one untraceable summary.

## 39.9 Conflicting sources

A conflict record should identify:

- affected subject;
- claims;
- sources;
- fields;
- authority;
- severity;
- whether runtime use is blocked;
- owner decision status;
- resolution;
- retained historical claims.

## 39.10 Provenance-only sources

Older compilations or derivative documents may remain registered for history and comparison while newer authoritative sources control conversion.

A provenance-only source must not silently override the active source.

## 39.11 Generated content provenance

AI-generated or procedurally generated content should record:

- generator;
- version;
- inputs;
- seed where applicable;
- prompt or brief where permitted;
- human review;
- source references;
- output fingerprint;
- approval status.

Generated provenance does not establish canon status.

## 39.12 Runtime provenance

A runtime projection should be explainable through:

- base Definitions;
- pack versions;
- extensions;
- overrides;
- migrations;
- campaign events;
- session adjudications;
- rules engine version.

## 39.13 Event provenance

An event should retain:

- actor;
- authority;
- originating operation;
- rules profile;
- source content;
- calculation result;
- adjudication;
- final effect;
- event version;
- correlation and causation.

## 39.14 Release provenance

A release should identify:

- source commit or source package;
- build process;
- tool versions;
- pack versions;
- validation reports;
- checksums;
- migration notes;
- approval;
- known blockers;
- retained artifacts.

## 39.15 Coverage principle

Coverage measures the relationship between known source material and governed outputs.

Coverage is not simply the number of records produced.

## 39.16 Coverage dimensions

Coverage may be measured across:

- sources;
- source units;
- rows;
- pages;
- sections;
- tables;
- domains;
- object types;
- mechanics;
- relationships;
- media;
- settings;
- variants;
- conflicts;
- missing fields;
- validation;
- pack ownership;
- runtime fixtures.

## 39.17 Source coverage states

A source unit may be classified as:

- registered;
- inventoried;
- candidate extracted;
- normalized;
- promoted;
- deferred;
- conflict-held;
- provenance-only;
- intentionally excluded;
- unprocessed.

Exact enums remain registry-controlled.

## 39.18 Record coverage

Record coverage should identify:

- object type;
- count;
- source support;
- required fields;
- missing fields;
- relationship completeness;
- mechanics mapping;
- validation;
- pack assignment;
- release state.

## 39.19 Mechanics coverage

Mechanics coverage checks whether source-described mechanics are represented through:

- Actions;
- Effects;
- Conditions;
- Resources;
- modifiers;
- rules profiles;
- progression;
- grants;
- compatibility;
- lifecycle.

A record with complete descriptive prose may still have incomplete mechanics coverage.

## 39.20 Relationship coverage

Relationship coverage checks:

- expected links identified;
- source and target exist;
- edge type;
- directionality;
- provenance;
- visibility;
- unresolved roster or boundary.

## 39.21 Media coverage

Media coverage checks:

- source image or media registered;
- subject identified;
- extraction state;
- rights;
- provenance;
- derivative availability;
- accessibility metadata;
- visibility.

## 39.22 Coverage gaps

A coverage gap should identify:

- source;
- affected domain;
- type;
- reason;
- impact;
- blocker status;
- recommended next action;
- owner decision requirement.

## 39.23 Coverage cannot invent completeness

When a source says that a group contains thirty worlds but names only some of them, coverage should record:

- the known group size claim;
- named members;
- unnamed or unresolved members;
- source coordinate;
- blocker status.

It must not generate missing members.

## 39.24 Coverage matrices

A coverage matrix may cross:

- source units;
- object types;
- templates;
- required fields;
- mechanics;
- pack destinations;
- validation;
- release status.

Matrices should be generated from registries where practical.

## 39.25 Reconciliation

Reconciliation compares registries and promoted outputs.

It should detect:

- unprocessed source rows;
- duplicate source coordinates;
- duplicate canonical identities;
- missing candidate mappings;
- orphaned records;
- unowned records;
- pack count mismatch;
- lost provenance;
- unresolved variants.

## 39.26 Verified CSV-first baseline

The completed CSV-first program records:

- 20 governed datasets;
- 19,199 source rows;
- 19,199 promoted records;
- 19,199 deterministic canonical identities;
- zero unprocessed rows;
- zero partially processed datasets;
- passing cross-dataset source-coordinate and registry-identity uniqueness;
- passing provenance;
- passing runtime, install, and uninstall validation.

The final reconciliation artifact SHA-256 is `112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40`.

## 39.27 Coverage limits

The verified CSV-first result proves full processing of the registered 20 datasets.

It does not automatically prove:

- every legacy PDF has no additional unique content;
- every image and table has been fully recovered;
- every source contradiction is resolved;
- every record is final game canon;
- every mechanic is balanced;
- every setting or adventure is public-release ready.

## 39.28 Audits

Useful audits include:

- source inventory audit;
- data-quality audit;
- provenance audit;
- identity audit;
- relationship audit;
- mechanics coverage audit;
- pack ownership audit;
- runtime contract audit;
- install and uninstall audit;
- provider-exit audit.

## 39.29 Audit independence

An audit should compare independent evidence where practical.

For example:

- source registry versus promoted registry;
- manifest versus archive;
- ownership map versus record index;
- event history versus snapshot;
- export manifest versus exported files.

## 39.30 Change impact

When a source, mapping, schema, or record changes, impact analysis should identify:

- affected canonical records;
- dependent records;
- packs;
- fixtures;
- baselines;
- migrations;
- live campaign references;
- exports;
- documentation.

## 39.31 AI boundary

AI may:

- classify source units;
- identify likely omissions;
- compare registries;
- generate audit packets;
- summarize gaps;
- suggest repair tranches.

AI must not:

- fabricate source coordinates;
- mark unresolved content complete;
- hide gaps;
- discard variants;
- declare a source authoritative without evidence;
- convert generated material into recovered source truth.

## 39.32 Controlling references

- source census
- neutral recovery ledger
- CSV Source Registry
- CSV Intake Audit
- Template Coverage Matrix
- Mapping Contract Registry
- Source Coverage and Provenance Audit
- identity and relationship reconciliation
- full CSV registry reconciliation
- completion governance validators
- source conflict and missing-information registers

**Status:** Canonical and validated provenance and coverage architecture.

---

# 40. Installation, Update, Migration, and Removal

## 40.1 Purpose

Define the lifecycle operations that safely move governed content and schemas into, through, and out of an installed environment while preserving identity, state, history, and recovery.

## 40.2 Lifecycle principle

Every lifecycle operation should be:

- planned before mutation;
- validated;
- deterministic;
- attributable;
- version-aware;
- idempotent where practical;
- recoverable;
- receipted;
- provider-neutral.

## 40.3 Installation states

A pack or content set may move through states such as:

- absent;
- available;
- planned;
- validating;
- installed;
- active;
- degraded;
- update available;
- migration required;
- quarantined;
- removal blocked;
- removed;
- archived.

Exact states remain implementation-controlled.

## 40.4 Install request

An install request should identify:

- actor;
- environment or workspace;
- target pack and version;
- source;
- requested optional dependencies;
- entitlement context;
- expected registry fingerprint;
- idempotency key.

## 40.5 Install planning

The planner should determine:

- current installed state;
- required dependencies;
- optional integrations;
- compatible versions;
- conflicts;
- migrations;
- storage impact;
- records added;
- schemas added;
- media and localization;
- live-state risks;
- required approvals.

The plan should have a deterministic fingerprint.

## 40.6 Install validation

Before execution, validate:

- archive integrity;
- manifest and index;
- checksums;
- signatures where required;
- schemas;
- stable IDs;
- pack ownership;
- dependencies;
- compatibility;
- entitlement;
- policy;
- storage;
- migration availability.

## 40.7 Install execution

Execution should:

1. revalidate the plan against current state;
2. acquire an operation lock or equivalent protection;
3. stage content;
4. run schemas and semantic validators;
5. apply in dependency order;
6. register ownership and versions;
7. build indexes;
8. activate permitted content;
9. produce receipt;
10. release lock.

## 40.8 Install failure

A failed installation should produce:

- operation ID;
- plan fingerprint;
- failure type;
- failed step;
- staged changes;
- rollback or compensation result;
- final registry fingerprint;
- retry guidance.

No partial activation should be hidden.

## 40.9 Update request

An update request identifies:

- installed pack;
- target version;
- expected current version;
- optional features;
- idempotency key;
- maintenance or downtime policy where relevant.

## 40.10 Update diff

The update planner should identify:

- added records;
- changed records;
- deprecated records;
- removed records;
- schema changes;
- migrations;
- dependency changes;
- compatibility;
- live references;
- baseline changes;
- media and localization changes.

## 40.11 Semantic change classification

Changes should be classified as:

- presentation-only;
- metadata;
- compatible content;
- mechanical;
- schema migration;
- breaking;
- legal or rights withdrawal;
- security correction.

The classification guides validation and release notes.

## 40.12 Live-state impact

An update must identify live state that references changed Definitions.

Affected state may include:

- character grants;
- item instances;
- NPCs;
- adventures;
- faction relationships;
- projects;
- scene state;
- event replay;
- snapshots.

The update must not mutate live state implicitly unless a migration defines the transformation.

## 40.13 Migration planning

A migration plan should identify:

- migration ID;
- source and target versions;
- subjects;
- preconditions;
- stable-ID mappings;
- field transforms;
- extension handling;
- unknown-field handling;
- event and snapshot impact;
- validation;
- rollback or recovery;
- expected result fingerprint.

## 40.14 Migration execution

Migration should:

- preserve source evidence;
- operate on a known snapshot or transaction boundary;
- transform deterministically;
- validate outputs;
- emit receipts;
- preserve supersession mappings;
- avoid re-running completed migration steps incorrectly.

## 40.15 Migration receipts

A migration receipt should include:

- operation ID;
- migration ID;
- input versions;
- output versions;
- affected IDs;
- mappings;
- warnings;
- validation;
- checksum or fingerprint;
- completion state.

## 40.16 Failed migration

A failed migration should leave:

- original state intact; or
- a clearly marked recoverable intermediate state with compensation instructions.

The system must not continue using an ambiguous half-migrated aggregate as valid.

## 40.17 Schema migration

Schema migration may affect:

- reusable records;
- instances;
- events;
- snapshots;
- indexes;
- exports.

Event migrations require special caution because historical evidence should not be rewritten casually.

A compatibility reader or upcaster may be preferable to destructive event rewriting.

## 40.18 Data backfill

A backfill populates newly required data from existing evidence.

A backfill must identify:

- source fields;
- derivation;
- confidence;
- unresolved records;
- default behavior;
- provenance;
- review requirements.

A guessed default must not be presented as source-derived truth.

## 40.19 Deprecation period

A deprecated record or field may remain available for:

- compatibility;
- migration;
- history;
- imports;
- replay.

The deprecation policy should state:

- replacement;
- warning period;
- removal version;
- migration;
- affected users and packs.

## 40.20 Removal request

A removal request should identify:

- pack or record set;
- actor;
- expected registry state;
- desired archive or export behavior;
- idempotency key.

## 40.21 Removal planning

The planner should identify:

- dependents;
- active campaign references;
- live instances;
- history;
- snapshots;
- user-owned state;
- entitlement consequences;
- media and cache;
- tombstones;
- export needs;
- blockers.

## 40.22 Removal blockers

Removal should be blocked when it would cause ungoverned loss of:

- active required dependencies;
- character history;
- campaign history;
- ownership;
- live assets;
- adventure state;
- recovery capability;
- legal or audit evidence.

## 40.23 Safe removal strategies

A safe strategy may include:

- disable rather than delete;
- archive;
- export;
- snapshot;
- replace with compatible pack;
- migrate references;
- retain tombstones;
- remove only optional unused content.

## 40.24 Removal execution

Removal should:

- revalidate plan;
- deactivate content;
- update dependency graph;
- remove owned definitions when safe;
- retain required tombstones and receipts;
- remove derived indexes and caches;
- preserve live history;
- validate final state.

## 40.25 Zero-residue validation

Zero-residue validation confirms no unintended data remains.

Intended retained evidence is not residue.

The validator should distinguish:

- receipts;
- tombstones;
- archived snapshots;
- retained history;
- exported content;
- accidental orphan data.

## 40.26 Reinstallation

Reinstallation should:

- recognize retained identities;
- reconnect compatible history;
- restore definitions;
- avoid duplicates;
- validate migrations;
- rebuild indexes.

## 40.27 Provider migration

A provider migration moves storage or services without changing canonical identity.

It should preserve:

- internal IDs;
- provider mappings;
- content;
- events;
- snapshots;
- schemas;
- indexes or rebuild instructions;
- checksums;
- receipts;
- access policy.

## 40.28 Backup interaction

Before risky lifecycle operations, the system may require a verified backup or checkpoint.

The backup should be compatible with:

- installed pack state;
- schema versions;
- migration plan;
- provider-exit requirements.

## 40.29 Concurrency

Lifecycle operations should prevent incompatible concurrent mutations.

Examples include:

- two updates to the same pack;
- removal during migration;
- restore during active install;
- two migrations on the same aggregate.

## 40.30 Maintenance and availability

The architecture should prefer online or bounded-maintenance operations where practical.

A maintenance requirement must be explicit and must not be treated as production authorization.

## 40.31 Audit

Every lifecycle operation should be auditable through:

- request;
- plan;
- actor;
- validations;
- execution steps;
- receipts;
- final fingerprint;
- failures and compensation.

## 40.32 Testing

Lifecycle tests should cover:

- fresh install;
- repeated install;
- optional dependency absent;
- dependency conflict;
- update;
- migration;
- failed migration;
- rollback;
- blocked removal;
- safe removal;
- reinstall;
- provider migration;
- backup restore;
- zero residue.

## 40.33 AI boundary

AI may:

- generate plans;
- analyze dependencies;
- prepare migrations;
- inspect failures;
- suggest recovery.

AI must not:

- execute destructive removal without authority;
- bypass blockers;
- fabricate a backup;
- mark a migration complete without validation;
- discard historical state;
- authorize production maintenance.

## 40.34 Controlling references

- pack lifecycle schemas
- install and uninstall validators
- migration and supersession maps
- provider-neutral persistence and migration ports
- backup, restore, and export architecture
- golden lifecycle fixtures
- 8E-008 and 8E-009 validation reports
- P9-06 implementation backlog

**Status:** Canonical lifecycle architecture; production execution remains gated.

---

# 41. Runtime Representation and Indexing

## 41.1 Purpose

Define how canonical content and live state are projected into runtime registries, indexes, caches, search results, APIs, and authoritative-session views without creating competing truth.

## 41.2 Runtime principle

The runtime uses optimized representations derived from canonical Definitions, installed-pack state, campaign state, events, snapshots, permissions, and active versions.

Derived runtime data is disposable and rebuildable unless a contract explicitly identifies it as authoritative state.

## 41.3 Installed content registry

The installed content registry should identify:

- stable object ID;
- object type;
- owner pack;
- pack version;
- content version;
- schema version;
- lifecycle status;
- compatibility;
- content fingerprint;
- provenance references;
- search/index status.

## 41.4 Definition store

The Definition store provides canonical installed reusable content.

It should support:

- lookup by stable ID;
- type filtering;
- version-aware access;
- owner-pack inspection;
- dependency inspection;
- provenance;
- extension resolution;
- deprecation and replacement.

## 41.5 Live state store

Live state is stored separately from Definitions.

Live state may include:

- campaign aggregates;
- characters;
- instances;
- memberships;
- reputation;
- scene state;
- project state;
- adventure state;
- knowledge and visibility;
- ownership;
- session projections.

## 41.6 Event store

The event store preserves accepted immutable events.

It should support:

- aggregate stream;
- sequence;
- correlation;
- causation;
- event type;
- actor;
- authority;
- visibility;
- schema version;
- replay;
- audit.

## 41.7 Snapshot store

Snapshots accelerate loading and recovery.

A snapshot should include:

- aggregate ID;
- event cursor;
- projection;
- versions;
- fingerprint;
- compatibility;
- creation reason;
- recovery metadata.

A snapshot should be rejected if its fingerprint or version context is incompatible.

## 41.8 Registry projection

A registry projection may merge:

- base Definition;
- active extensions;
- applicable overrides;
- replacement mappings;
- compatibility;
- installed version.

The projection should retain an explanation graph.

## 41.9 Runtime object handles

A runtime handle may include:

- stable ID;
- resolved version;
- object type;
- owner pack;
- projection fingerprint.

A handle is preferable to passing mutable full objects between components when identity and version consistency matter.

## 41.10 Index types

Indexes may support:

- ID lookup;
- object type;
- display name;
- aliases;
- pack;
- setting;
- domain;
- tags;
- relationships;
- dependency;
- provenance;
- capability;
- visibility;
- localization;
- full text;
- numeric or range filters;
- geospatial or graph projections where applicable.

## 41.11 Search index

The search index is a derived permission-aware projection.

Each result should retain:

- stable ID;
- type;
- display label;
- owner pack;
- content version;
- locale;
- visibility;
- entitlement status;
- provenance summary;
- search-match explanation where practical.

## 41.12 Permission filtering

Permission filtering must occur before protected content is returned.

The system must not fetch all secret content and rely only on UI hiding.

Permission-aware indexes may use:

- prefiltered documents;
- scoped queries;
- postfiltering in a trusted service;
- separate protected indexes.

The implementation must be tested against inference and metadata leakage.

## 41.13 Entitlement filtering

Entitlement determines access to installed or available content.

Search should distinguish, without leaking protected details:

- installed and accessible;
- installed but not permitted;
- available but not installed;
- unavailable;
- hidden by role.

## 41.14 Localization indexing

Localized indexes should preserve the same stable ID across locales.

They may index:

- translated name;
- aliases;
- translated summary;
- source-locale fallback;
- terminology.

The selected result remains the same canonical object.

## 41.15 Relationship index

A relationship index supports graph traversal.

It should preserve:

- edge ID;
- source;
- target;
- type;
- direction;
- scope;
- visibility;
- validity;
- provenance.

The index must not invent inverse relationships unless the relationship type defines them.

## 41.16 Dependency index

A dependency index supports:

- install planning;
- update planning;
- removal blocking;
- compatibility;
- provider-exit export;
- impact analysis.

## 41.17 Provenance index

A provenance index supports:

- source-to-record lookup;
- record-to-source lookup;
- candidate history;
- transformation;
- release;
- conflict;
- coverage audit.

## 41.18 Capability index

A capability index supports finding:

- actions;
- effects;
- conditions;
- resources;
- movement modes;
- adaptations;
- grants;
- rules profiles;
- item capabilities;
- creature capabilities;
- asset systems.

The index must reference canonical mechanics rather than extracting ungoverned keywords from prose alone.

## 41.19 Cache

A cache stores derived results for performance.

Cache keys should include all state that affects correctness, such as:

- object version;
- pack version;
- campaign override version;
- permissions;
- locale;
- entitlement;
- rules profile;
- environment;
- event cursor.

## 41.20 Cache invalidation

Caches should invalidate when relevant:

- content changes;
- pack changes;
- migration occurs;
- permissions change;
- entitlement changes;
- campaign events occur;
- visibility changes;
- locale changes;
- extension or override changes.

## 41.21 Materialized views

Materialized views may improve performance for:

- character summaries;
- encounter rosters;
- relationship graphs;
- campaign dashboards;
- content browsers;
- pack registries.

They must be rebuildable and tied to source fingerprints.

## 41.22 API projections

APIs should return purpose-specific projections rather than entire internal records by default.

A projection should include only:

- required fields;
- permitted fields;
- version and identity;
- pagination;
- errors;
- provenance references where appropriate.

## 41.23 Authoritative-session projections

An authoritative session may maintain different projections for:

- GM;
- acting player;
- party;
- observer;
- reconnecting client.

Each projection is derived from the same authoritative state and permission rules.

## 41.24 Hidden information

Hidden information must not leak through:

- result counts;
- sort order;
- pagination changes;
- IDs;
- names;
- aliases;
- thumbnails;
- relationships;
- validation errors;
- cache keys;
- AI retrieval.

## 41.25 Index rebuild

An index rebuild should:

1. select a consistent source snapshot;
2. validate source versions;
3. build deterministic index records;
4. verify counts and fingerprints;
5. atomically activate the new index;
6. retain rollback information;
7. emit a receipt.

## 41.26 Incremental indexing

Incremental indexing may process changed records and events.

It must detect:

- missed updates;
- duplicate updates;
- out-of-order events;
- stale versions;
- deleted or tombstoned records.

Periodic full reconciliation should verify incremental correctness.

## 41.27 Search ranking

Search ranking may consider:

- exact stable ID;
- exact name;
- alias;
- title;
- domain relevance;
- installed and permitted status;
- locale;
- usage context;
- semantic similarity.

Ranking must not change canon or visibility.

AI or semantic retrieval should not promote uninstalled or unauthorized content into hidden context.

## 41.28 No-result behavior

No-result behavior should distinguish permitted user-facing states without leaking secrets.

Internal diagnostics may identify:

- absent content;
- uninstalled pack;
- inaccessible entitlement;
- hidden role;
- indexing failure;
- stale index.

## 41.29 Offline indexes

Offline clients may maintain scoped indexes.

An offline bundle must include only content the user is authorized to retain and must support:

- expiry or revocation policy;
- migration;
- integrity;
- reconnect reconciliation;
- secure removal.

## 41.30 Provider neutrality

Runtime representation and indexing should be abstracted from a specific database or search provider.

Provider-specific adapters may optimize:

- SQL;
- graph queries;
- full-text search;
- vector search;
- caching.

The canonical query and projection contracts remain portable.

## 41.31 Vector and semantic search

Semantic indexes are derived aids.

They must preserve:

- stable ID;
- source record;
- visibility;
- entitlement;
- locale;
- model and embedding version;
- rebuild capability.

Embedding similarity is not canonical equivalence.

## 41.32 AI retrieval

AI retrieval should use governed indexes and return provenance-bearing references.

The retrieval layer must enforce:

- role permissions;
- entitlement;
- campaign scope;
- secret filtering;
- installed content;
- source citation;
- model-context minimization.

## 41.33 Observability

Runtime indexing should report:

- build duration;
- record counts;
- errors;
- stale records;
- permission-filter results;
- cache hit rate;
- rebuilds;
- provider adapter;
- version and fingerprint.

Observability must avoid logging protected content.

## 41.34 Validation

Index validation should compare:

- source registry versus index count;
- sample records;
- visibility;
- aliases;
- locale;
- relationships;
- tombstones;
- dependency graph;
- incremental versus full rebuild;
- provider-exit reconstruction.

## 41.35 Recovery

After restore or provider migration, indexes should be rebuilt from:

- Definitions;
- installed pack registry;
- live state;
- events;
- snapshots;
- permissions;
- localization.

Indexes should not be the only copy of authoritative data.

## 41.36 AI boundary

AI may:

- propose index strategies;
- analyze stale results;
- generate query tests;
- summarize provenance-bearing search results.

AI must not:

- bypass permission filters;
- treat embedding similarity as canon;
- expose hidden index metadata;
- make a derived cache authoritative;
- claim a provider-specific index is irreplaceable.

## 41.37 Controlling references

- DB-003 search and indexing architecture
- canonical object registry
- installed pack registry
- relationship and provenance registries
- provider-neutral persistence ports
- authoritative-session service ports
- identity and entitlement ports
- content-system search destination
- backup, restore, and provider-exit architecture

**Status:** Canonical runtime representation and indexing architecture; provider adapters remain implementation-specific.

---

# Tranche 4 Integration Review

## T4.1 Coverage

Volume IV now consolidates:

- canonical object families;
- object layers;
- stable IDs;
- schemas;
- validation;
- pack format;
- dependency graphs;
- extensions;
- overrides;
- provenance;
- source coverage;
- lifecycle operations;
- runtime registries;
- search and indexing;
- recovery and provider exit.

## T4.2 Core object layers

The integrated object architecture preserves:

1. raw source claim;
2. normalized claim;
3. candidate;
4. canonical Definition;
5. placement or binding;
6. live instance or state;
7. event;
8. snapshot;
9. user overlay;
10. runtime projection.

A system may omit layers it does not need, but must not collapse layers in ways that destroy identity, provenance, history, or campaign state.

## T4.3 Stable identity invariant

Stable identity is independent of:

- display name;
- filename;
- file path;
- database row;
- provider ID;
- localization;
- UI route;
- storage URL.

Identity migrations require explicit mappings.

## T4.4 One-owner invariant

Every reusable canonical record has one owner pack.

Other packs may:

- depend on;
- extend;
- bind;
- place;
- replace through governance;
- override in a declared scope.

They may not silently become co-owners.

## T4.5 Validation invariant

No single validation layer proves all forms of correctness.

Release evidence may require:

- schema;
- identity;
- references;
- provenance;
- semantics;
- runtime;
- permissions;
- pack lifecycle;
- migration;
- golden regression;
- coverage;
- release approval.

## T4.6 Lifecycle invariant

Install, update, migration, removal, restore, and provider exit require:

- planning;
- preconditions;
- deterministic execution;
- receipts;
- recovery;
- final validation.

## T4.7 Provenance invariant

A promoted record should remain traceable through:

- source;
- coordinate;
- candidate;
- mapping;
- canonical ID;
- owner pack;
- release;
- runtime projection.

## T4.8 Runtime invariant

Runtime indexes and caches are derived and rebuildable.

The authoritative sources remain:

- canonical installed Definitions;
- live state;
- events;
- snapshots;
- permissions;
- versions.

## T4.9 Permission invariant

Visibility and entitlement must be enforced throughout:

- storage;
- queries;
- indexes;
- APIs;
- AI retrieval;
- exports;
- caches;
- errors.

## T4.10 Verified baseline

The canonical object program has already validated:

- 20 datasets;
- 19,199 source rows;
- 19,199 promoted records;
- deterministic identity;
- provenance;
- runtime contracts;
- installation;
- uninstallation;
- zero residue.

Volume IV preserves those results as a baseline and connects them to future application runtime architecture.

## T4.11 Remaining boundaries

Volume IV does not select:

- production database provider;
- production search provider;
- vector database;
- CDN;
- hosted pack registry;
- production signing infrastructure;
- deployment topology.

Those decisions remain provider-neutral implementation concerns and release gates.

**Tranche 4 status:** Complete — canonical object and data architecture consolidated.


# Volume V — Application Design

# 42. Product Shell and Navigation

## 42.1 Purpose

Define the persistent application structure, navigation system, workspace model, design-system responsibilities, universal states, and cross-device behavior used by every Multiversal screen.

The shell must make a very large application understandable without flattening Player, Game Master, Content Creator, Owner/Admin, and live-session work into one undifferentiated menu.

## 42.2 Implementation principle

The visible application must be built through tested vertical slices:

> navigation → screen → real data → actions → permissions → persistence → tests

The project must not build hundreds of disconnected mock screens and postpone integration.

Every completed UI batch must include:

- real governed data;
- actions;
- permissions;
- persistence;
- desktop and mobile behavior;
- loading, empty, error, offline, forbidden, and recovery states;
- automated tests;
- reproducible preview;
- owner review.

## 42.3 Baseline audit requirement

Before a claim that a UI program is complete, the implementation team must inspect the actual application repository and record:

- frontend framework and project structure;
- routes and screens that truly exist;
- reusable components;
- implemented services and APIs;
- mock or temporary data;
- incomplete, dead, or duplicate interfaces;
- desktop, tablet, and mobile behavior;
- Content Library integration;
- authentication and permissions;
- build, test, deployment, and preview paths.

The audit produces:

- UI implementation inventory;
- screen status matrix;
- reusable-component inventory;
- technical blocker list;
- ordered implementation backlog.

A design document does not prove that the corresponding interface exists.

## 42.4 Shell responsibilities

The application shell should provide:

- global product identity;
- workspace selection;
- campaign selection;
- character selection;
- session context;
- top navigation;
- desktop sidebar;
- tablet navigation behavior;
- mobile navigation;
- global search;
- notifications;
- approvals;
- invitation access;
- recent work;
- connection and synchronization state;
- account and user menu;
- help and contextual documentation;
- safe exit and workspace switching.

The shell should remain stable while the central workspace changes.

## 42.5 Workspace model

The primary workspace modes are:

- Player;
- Game Master;
- Content Creator;
- Owner/Admin.

A user may hold more than one role, but the active workspace determines the default information architecture and available actions.

Workspace switching must:

- preserve unsaved work safely;
- update permission-scoped navigation;
- update campaign and character context;
- avoid leaking hidden information from the prior workspace;
- provide clear current-role indication;
- maintain accessible focus.

A workspace is not merely a visual theme. It is a permission- and task-oriented context.

## 42.6 Global context hierarchy

The shell should communicate the current context in a predictable hierarchy:

1. account or identity;
2. workspace;
3. campaign or content project;
4. character, world, pack, or other primary subject;
5. session, scene, or active task;
6. selected object or inspector context.

A user should be able to determine where an action will apply before committing it.

## 42.7 Desktop navigation

The desktop shell should normally support:

- persistent or collapsible sidebar;
- top context bar;
- central content workspace;
- optional contextual inspector;
- optional secondary panel or activity rail.

The sidebar should prioritize destinations rather than every possible object type.

Frequently reused domain content should be reached through:

- universal search;
- object browser;
- contextual pickers;
- recent items;
- favorites or collections;
- workspace-specific shortcuts.

## 42.8 Mobile navigation

Mobile navigation should preserve capabilities without shrinking the desktop layout.

Mobile behavior should use:

- a concise primary destination set;
- contextual drawers or sheets;
- full-screen inspectors where needed;
- touch-safe targets;
- explicit save and close behavior;
- preserved back-stack semantics;
- reduced simultaneous panels;
- clear active campaign and character context.

Critical actions must not be available only through hover.

## 42.9 Tablet behavior

Tablet behavior may combine:

- collapsible navigation;
- split views;
- slide-over inspectors;
- touch-first controls;
- adaptive density.

The design must be tested at realistic orientations and input modes.

## 42.10 Navigation levels

Navigation should distinguish:

### Global navigation

Moves among major workspaces and universal features.

### Workspace navigation

Moves among the active workspace’s major tools.

### Context navigation

Moves within the current campaign, character, world, pack, or session.

### Object navigation

Moves through relationships, dependencies, provenance, variants, and related records.

### History navigation

Supports browser back, application back, breadcrumbs, recent work, and return to prior selection.

These levels should not compete for the same visual hierarchy.

## 42.11 Route design

Routes should use stable identities rather than display names.

A route should be:

- shareable when permissions permit;
- restorable after reload;
- compatible with browser history;
- safe when the referenced content is absent or inaccessible;
- explicit about workspace and context where ambiguity is possible.

A route must not reveal protected object names in a way that bypasses permissions.

## 42.12 Breadcrumbs

Breadcrumbs are useful when the context has meaningful hierarchy.

They should show human-readable labels while retaining stable underlying references.

Breadcrumbs should not imply false containment. A relationship path may need a different visualization than a geographic or document hierarchy.

## 42.13 Campaign selector

The campaign selector should provide:

- campaigns the user may access;
- current role;
- current status;
- active or upcoming session information;
- unread or approval indicators;
- safe switching;
- search and sorting.

It must not expose campaigns, names, invitations, or participant information outside the user’s permissions.

## 42.14 Character selector

The character selector should distinguish:

- owned characters;
- controlled characters;
- campaign-bound characters;
- drafts;
- archived characters;
- unavailable or migration-required characters.

It should show enough state to choose correctly without attempting to become a complete character sheet.

## 42.15 Session context

When a session is active, the shell should make clear:

- campaign;
- scene;
- character or control role;
- connection state;
- synchronization state;
- pending proposal or approval count;
- whether the user is in live, paused, reconnecting, or recovered state.

The live-session context must not be hidden behind ordinary dashboard navigation.

## 42.16 Global search

Global search should support governed, permission-aware discovery across accessible content.

Search should preserve:

- stable ID;
- object type;
- owner pack;
- locale;
- campaign scope;
- visibility;
- entitlement;
- source and provenance summary.

Search should help users distinguish:

- canonical Definition;
- campaign instance;
- personal draft;
- historical item;
- unavailable or migration-required content.

## 42.17 Command and quick-action access

A command palette or quick-action system may provide efficient access to:

- create;
- open;
- search;
- switch workspace;
- switch campaign;
- switch character;
- run permitted actions;
- open contextual help.

Commands must still enforce service-level permissions and confirmations.

## 42.18 Notifications

Notifications should be categorized by actionability.

Relevant types may include:

- invitation;
- approval required;
- action result;
- session starting;
- disconnected or recovered state;
- migration required;
- validation failure;
- content review;
- ownership or permission change;
- export or backup result.

A notification is not the authoritative event. It links to the relevant governed state or operation.

## 42.19 Approval center

The shell may expose an approval center for:

- live action proposals;
- content submissions;
- ownership or transfer requests;
- campaign invitations;
- owner-gated decisions.

Approval entries should show:

- requester;
- subject;
- context;
- consequences;
- validation;
- age or urgency;
- permitted decisions.

Approval counts must respect role and campaign context.

## 42.20 Universal object experience

The shell and design system must support a universal object experience for:

- browsing;
- searching;
- filtering;
- selecting;
- inspecting;
- comparing;
- traversing relationships;
- viewing provenance;
- viewing source coverage;
- viewing variants and versions;
- permitted editing;
- validation.

The same object browser and picker foundation should serve:

- creatures;
- items;
- abilities;
- species;
- environments;
- vehicles;
- worlds;
- rules;
- scenes;
- other domains.

## 42.21 Object inspector

The object inspector should be a reusable component capable of showing:

- identity and type;
- summary;
- mechanics;
- relationships;
- dependencies;
- variants;
- version;
- pack ownership;
- provenance;
- source view;
- validation status;
- visibility and entitlement;
- permitted actions.

The inspector must not silently display GM-only or inaccessible fields.

## 42.22 Object picker

The universal object picker should support:

- contextual allowed types;
- search;
- filtering;
- recent and favored objects;
- relationship-aware suggestions;
- entitlement and installation state;
- selection validation;
- desktop and mobile use.

A picker returns stable object references, not copied display text.

## 42.23 Design tokens

The UI should use governed design tokens for:

- color;
- typography;
- spacing;
- radius;
- elevation;
- border;
- motion;
- focus;
- status;
- density;
- responsive breakpoints.

The owner-approved Multiversal visual direction should be expressed through tokens rather than hard-coded per-screen values.

The distinctive dark, luminous, multiversal presentation may use layered depth and controlled chromatic accents, but readability and accessibility control over decorative effects.

## 42.24 Color and contrast

Color may indicate:

- workspace;
- object domain;
- status;
- severity;
- selection;
- ownership;
- visibility;
- connection.

Color must not be the only indicator.

The palette must support sufficient contrast in:

- default;
- hover;
- focus;
- disabled;
- selected;
- error;
- warning;
- success;
- offline states.

## 42.25 Typography

Typography should distinguish:

- page title;
- workspace title;
- section;
- object name;
- data label;
- body text;
- rule text;
- helper text;
- code or stable ID;
- status.

Rules and long-form source text need comfortable reading widths and scalable text.

## 42.26 Core components

The approved reusable component set should include:

- buttons;
- links;
- icon buttons;
- forms;
- inputs;
- selects;
- autocomplete;
- menus;
- tabs;
- accordions;
- cards;
- panels;
- dialogs;
- drawers;
- tooltips;
- popovers;
- badges;
- alerts;
- tables;
- lists;
- trees;
- graphs;
- timelines;
- inspectors;
- relationship views;
- loading indicators;
- empty states;
- error boundaries;
- permission states.

Screens should be composed primarily from these components.

## 42.27 Form behavior

Forms should support:

- labels;
- descriptions;
- required and optional state;
- inline validation;
- server validation;
- unsaved-change protection;
- draft saving;
- keyboard use;
- touch use;
- error summary;
- recovery.

A form must not silently discard invalid or unknown data.

## 42.28 Loading state

Loading states should communicate:

- what is loading;
- whether prior data is stale or current;
- whether interaction remains safe;
- whether retry is possible.

Skeletons may preserve layout, but must not imitate real data so closely that users mistake them for actual state.

## 42.29 Empty state

An empty state should distinguish:

- no content exists;
- no content matches filters;
- no permission;
- content not installed;
- content unavailable offline;
- content hidden;
- failed load.

It should provide the next permitted action when one exists.

## 42.30 Error state

Errors should identify:

- operation;
- affected context;
- whether data was changed;
- retry behavior;
- recovery option;
- diagnostic reference.

Technical details should be available for support without overwhelming ordinary users or exposing secrets.

## 42.31 Offline state

Offline behavior should clearly communicate:

- current connection;
- last synchronized time;
- operations allowed offline;
- queued changes;
- conflicts;
- reconnect behavior;
- content unavailable offline.

Offline mode must not imply that unconfirmed queued operations are already authoritative.

## 42.32 Forbidden state

A forbidden state should avoid disclosing protected content.

It may state that access is unavailable without revealing:

- hidden name;
- object type;
- campaign;
- owner;
- reason that exposes confidential membership.

## 42.33 Recovery state

Recovery interfaces should support:

- restore draft;
- resume session;
- reconcile queued changes;
- retry failed save;
- inspect recovered snapshot;
- select safe version;
- contact GM or owner where required.

## 42.34 Destructive actions

Destructive or high-impact actions should:

- identify affected subject;
- state consequences;
- show recoverability;
- require appropriate confirmation;
- enforce authority;
- provide receipt.

Confirmation should be proportional. Routine reversible actions should not be burdened by excessive dialogs.

## 42.35 Autosave

Autosave may preserve drafts and low-risk edits.

The interface should indicate:

- saving;
- saved;
- offline queued;
- save failed;
- conflict;
- recovered state.

Autosave must not automatically commit GM approvals, canonical publication, irreversible transfers, or destructive operations.

## 42.36 Focus and keyboard navigation

Every interactive component must support:

- visible focus;
- logical focus order;
- keyboard activation;
- escape and close behavior;
- focus return;
- screen-reader naming.

Complex components such as trees, grids, relationship graphs, and object pickers require defined keyboard interaction.

## 42.37 Motion

Motion should clarify:

- navigation;
- hierarchy;
- panel changes;
- state transitions;
- drag and drop;
- synchronization.

Motion must respect reduced-motion preferences and avoid interfering with urgent live-session information.

## 42.38 Responsive density

Data-heavy views may support comfortable and compact density.

Density changes must not reduce:

- touch-target size on touch devices;
- focus visibility;
- semantic labels;
- information required for decisions.

## 42.39 Shell persistence

The shell should preserve appropriate preferences such as:

- sidebar state;
- density;
- theme;
- last workspace;
- recent context;
- panel arrangement.

It must not restore a hidden GM context into a player workspace without rechecking permissions.

## 42.40 Performance

The shell should load essential navigation and current context quickly.

Large object catalogs should use:

- pagination or virtualization;
- incremental search;
- cached permitted indexes;
- lazy-loaded inspectors;
- predictable loading states.

Performance optimization must not bypass permission checks.

## 42.41 Telemetry

UI telemetry may measure:

- route failures;
- load times;
- error rates;
- recovery use;
- interaction abandonment;
- accessibility issues;
- device classes.

Telemetry must avoid recording protected campaign content, rules secrets, private notes, or production credentials.

## 42.42 Acceptance criteria

The shell and design-system stage is ready when:

- a user can authenticate or enter the allowed identity flow;
- the correct workspace is selected;
- campaign and character context can be changed safely;
- desktop, tablet, and mobile navigation work;
- global search respects permissions;
- loading, empty, error, offline, forbidden, and recovery states exist;
- reusable components support keyboard, touch, focus, validation, and permission states;
- new screens can be built primarily from approved components.

## 42.43 Controlling references

- `governance/application-planning/STAGE_A_UI_IMPLEMENTATION_PROGRAM.md`
- Stage A A0–A3 requirements
- application implementation roadmap
- owner-approved Multiversal UI mockups and palette direction
- DB-003 search and indexing architecture
- identity, entitlement, session, and permission contracts
- accessibility and internal-alpha hardening requirements

**Status:** Owner-approved planned application architecture. Repository implementation must be verified through Stage A0 evidence.

---

# 43. Player Experience

## 43.1 Purpose

Define the player-facing experience from identity entry through campaigns, characters, invitations, preparation, live sessions, action proposals, results, recovery, and long-term character history.

The Player workspace should prioritize play, character understanding, and current choices rather than administrative systems or development terminology.

## 43.2 Player principles

The Player experience should:

- make the current campaign and character obvious;
- foreground what the player can do now;
- explain costs and consequences before commitment;
- keep logs and proposals available but secondary;
- preserve character agency;
- avoid exposing GM-only information;
- support desktop and mobile play;
- recover safely from interruption;
- make rules inspectable without overwhelming the main scene.

## 43.3 Player entry

After identity entry, the player should reach a dashboard containing, as permitted:

- active campaigns;
- upcoming or live sessions;
- characters;
- invitations;
- pending decisions;
- notifications;
- drafts;
- recent work;
- recovery notices.

The dashboard should not show GM or creator controls merely because hidden buttons are easy to implement. Service-level permissions define available actions.

## 43.4 Player dashboard priorities

The primary player dashboard should answer:

- What campaign am I in?
- When is the next or current session?
- Which character am I using?
- Is anything waiting for me?
- Did something change?
- Can I resume unfinished work?

Secondary information may include:

- recent journal entries;
- character progression availability;
- inventory or condition warnings;
- campaign announcements;
- newly revealed content.

## 43.5 Invitations

An invitation view should show:

- campaign name when permitted;
- inviting GM or owner;
- intended role;
- campaign summary;
- content or rules requirements;
- character requirements;
- expiration or status;
- accept or decline consequences.

Accepting an invitation creates the governed membership relationship. It must not be represented as complete until confirmed by the authoritative service.

## 43.6 Character selection

A player may see:

- active characters;
- campaign-bound characters;
- drafts;
- archived characters;
- characters controlled by delegation;
- migration-required characters.

The selector should show:

- character name and portrait;
- campaign;
- status;
- current condition summary;
- validation or migration warnings;
- last activity.

## 43.7 Campaign home

The Player campaign home may include:

- campaign overview;
- announcements;
- participants visible to the player;
- current character;
- next session;
- current objectives;
- discovered locations;
- visible relationships;
- visible timeline;
- shared assets;
- notes and journal;
- house rules;
- installed and accessible content summaries.

It must not expose hidden scenes, unrevealed cast, secret objectives, GM notes, or protected relationships.

## 43.8 Session preparation

Before a live session, a player should be able to:

- open the assigned character;
- review resources and conditions;
- check equipment and shared assets;
- review visible objectives and clues;
- read campaign announcements;
- resolve required character-validation issues;
- test connection and offline availability;
- enter the session.

## 43.9 Live player workspace

The live player workspace should foreground:

- scene title and visible description;
- map, image, or theater-of-the-mind context;
- character summary;
- current resources and conditions;
- available actions;
- valid targets;
- costs;
- reactions or time-sensitive decisions;
- current result;
- connection and synchronization state.

The layout should not default to an administrative action log.

## 43.10 Scene presentation

The player sees only the authorized projection of:

- scene;
- participants;
- map;
- objects;
- objectives;
- clues;
- environmental state;
- hazards;
- available interactions.

A hidden token or object must not affect layout or metadata in a way that reveals its presence.

## 43.11 Character summary during play

The live summary should include the information needed for decisions, such as:

- identity;
- active form;
- relevant attributes or derived values;
- resources;
- conditions;
- current equipment;
- action availability;
- movement or position;
- selected targets;
- pending effects.

A complete character sheet remains accessible without replacing the live-action focus.

## 43.12 Available actions

Available actions should be derived from:

- character grants;
- items;
- forms;
- conditions;
- resources;
- environment;
- campaign rules;
- session timing;
- target context;
- permissions.

The UI should distinguish:

- available;
- available with warning;
- unavailable with explanation;
- hidden because the character does not know it;
- inaccessible because content is not entitled or installed.

## 43.13 Rule inspection

A player should be able to inspect an action or ability quickly.

The rule inspector should show, as permitted:

- source;
- timing;
- prerequisites;
- cost;
- target;
- resolution;
- outcomes;
- duration;
- current modifiers;
- provenance or pack ownership.

The player should not need to leave the session permanently to understand a rule.

## 43.14 Target selection

Target selection should communicate:

- valid targets;
- invalid targets and reason;
- range or relationship;
- visibility;
- selected target count;
- friendly, hostile, neutral, object, area, or self context where relevant.

Target validation remains authoritative on the service, even when the UI previews legality.

## 43.15 Cost preview

Before confirmation, the player should see:

- resources spent;
- items or charges used;
- action capacity;
- conditions or risks;
- time;
- possible failure costs;
- irreversible consequences.

The preview should distinguish guaranteed costs from conditional outcomes.

## 43.16 Action proposal

The proposal confirmation should show:

- actor;
- selected action;
- target or targets;
- chosen options;
- costs;
- roll method;
- relevant warnings;
- whether GM approval is required.

Submitting creates a proposal or action request. It does not immediately assert that the result is accepted.

## 43.17 Pending proposal

While pending, the player should see:

- proposal status;
- submitted summary;
- whether edits or cancellation are permitted;
- expected next authority;
- connection state.

The interface should prevent accidental duplicate submissions.

## 43.18 Result

The result view should communicate:

- accepted outcome;
- visible roll or deterministic result;
- visible modifiers;
- applied effects;
- changed resources;
- changed conditions;
- movement or position changes;
- GM alteration indicator when permitted;
- next available choice.

Detailed event history remains available as a secondary view.

## 43.19 Denial or correction

When a proposal is denied or requires correction, the player should receive a useful explanation that does not reveal protected information.

The interface may allow:

- edit and resubmit;
- choose another target;
- choose another action;
- acknowledge;
- ask the GM through permitted communication.

## 43.20 Reactions and interrupts

Time-sensitive reactions should:

- appear prominently;
- identify the trigger;
- show available options;
- show cost and expiration;
- support pass or decline;
- prevent duplicate responses;
- remain accessible by keyboard and touch.

A timer should only be displayed when the governing rule or session policy actually enforces one.

## 43.21 Player logs

Logs are secondary but accessible.

A player log may include:

- their declarations;
- visible accepted actions;
- visible results;
- visible scene events;
- resource and condition changes;
- discoveries;
- rewards;
- GM adjustments visible to the player.

It must omit protected information.

## 43.22 My Proposals

A My Proposals view may help the player inspect:

- pending proposals;
- approved proposals;
- denied proposals;
- altered proposals;
- failed or stale submissions.

It should not occupy the default live-session focus.

## 43.23 Character sheet

The player character sheet should provide:

- overview;
- attributes;
- derived values;
- skills;
- traits;
- abilities;
- resources;
- conditions;
- inventory;
- equipment;
- progression;
- relationships;
- notes;
- journal;
- source and rules inspection.

The interface should separate current state, permanent character build, temporary effects, and history.

## 43.24 Inventory

The player inventory should distinguish:

- owned;
- carried;
- equipped;
- stored;
- shared;
- borrowed;
- assigned;
- unavailable;
- damaged;
- consumed;
- lost.

Transfers, trades, equipment changes, crafting, and use must preserve ownership and prevent duplication.

## 43.25 Shared assets

A shared asset view may include:

- owners;
- custodian;
- authorized users;
- current controller;
- location;
- crew or stations;
- resources;
- condition;
- activity.

The player should see only the controls permitted by ownership, role, and session state.

## 43.26 Progression

The progression view should show:

- available progression currency or opportunity;
- current path;
- prerequisites;
- legal choices;
- exclusions;
- grants;
- previewed result;
- source;
- campaign restrictions;
- validation.

Advancement should require explicit confirmation and produce an event or receipt.

## 43.27 Notes and journal

Player notes and journal entries may be:

- private;
- shared with party;
- shared with GM;
- linked to characters, scenes, clues, locations, or events.

Sharing state must be explicit.

A personal theory or note must not be displayed as canonical fact.

## 43.28 Investigation tools

A player investigation workspace may support:

- known clues;
- evidence;
- witnesses;
- documents;
- discoveries;
- hypotheses;
- false leads;
- timeline;
- relationship board;
- notes;
- unresolved questions.

GM-only truth and unrevealed clues remain absent from the player projection.

## 43.29 Social tools

A player social workspace may show visible:

- relationships;
- faction standing;
- reputation;
- promises;
- favors;
- debts;
- social conditions;
- known attitudes.

The UI should distinguish perceived attitude from hidden actual motive.

## 43.30 Offline and reconnect

A disconnected player should see:

- last confirmed state;
- pending local actions;
- whether new actions may be queued;
- reconnect progress;
- conflict or stale-state warning;
- recovered authoritative state.

The UI must not present local speculative results as accepted.

## 43.31 Multi-device use

When a player uses multiple devices:

- one device may be primary for action;
- another may show a permitted reference or character view;
- state must remain consistent;
- duplicate submissions must be prevented;
- control conflicts must be explicit.

The authoritative session controls which device or operation is accepted.

## 43.32 Accessibility

The Player experience must support:

- keyboard navigation;
- screen readers;
- touch;
- scalable text;
- reduced motion;
- sufficient contrast;
- noncolor status indicators;
- accessible dice and result announcements;
- accessible map alternatives;
- clear error recovery.

## 43.33 Notifications and interruption

Live-session notifications should be restrained.

Urgent items include:

- reaction available;
- action requires correction;
- disconnected;
- recovered;
- session paused;
- GM decision required from the player.

Nonurgent announcements should not obscure active choices.

## 43.34 Contextual AI

Player-facing AI may:

- explain accessible rules;
- summarize visible clues;
- compare permitted equipment;
- help organize notes;
- suggest legal options.

AI must not:

- reveal hidden information;
- choose an action automatically;
- submit a proposal without explicit authorization;
- alter character state;
- invent canonical rules.

## 43.35 Player acceptance slice

The first playable Player slice is complete when a player can:

1. enter the correct workspace;
2. open a campaign;
3. select or create a valid character;
4. enter a scene;
5. inspect available actions;
6. select a valid target;
7. review costs;
8. submit a proposal;
9. receive the GM decision;
10. see the accepted result;
11. observe persistent synchronized state;
12. reconnect and resume safely.

## 43.36 Controlling references

- Stage A A3 Identity, Dashboard, and Workspace Selection
- Stage A A4 Character Workspace
- Stage A A6 First Playable Action and Approval Loop
- Stage A A7 Full Combat Interface
- Stage A A8 Inventory, Equipment, Crafting, and Vehicles
- Stage A A9 Investigation and Social Workspaces
- authoritative-session architecture
- identity, entitlement, persistence, and realtime service ports
- owner feedback that logs and My Proposals remain secondary

**Status:** Owner-approved planned experience. Full repository implementation remains to be verified and completed.

---

# 44. Game Master Experience

## 44.1 Purpose

Define the Game Master workspace for campaign authority, preparation, scene building, participant management, live adjudication, hidden information, world state, recovery, and post-session continuity.

The Game Master experience must reduce bookkeeping while preserving human authority.

## 44.2 GM principles

The GM workspace should:

- foreground current decisions and scene state;
- make hidden information safe;
- make rules inspectable;
- support preparation and improvisation;
- allow approval, denial, and explicit alteration;
- preserve the original calculated result;
- minimize repetitive data entry;
- use universal object pickers;
- support recovery and audit;
- avoid forcing the GM through development-oriented interfaces.

## 44.3 GM dashboard

The GM dashboard may include:

- campaigns;
- live and upcoming sessions;
- pending invitations;
- pending approvals;
- draft scenes;
- recent edits;
- unresolved validation;
- participant issues;
- migration or pack warnings;
- backups or recovery notices;
- recent campaign activity.

The dashboard should prioritize items requiring action.

## 44.4 Campaign overview

The GM Campaign workspace should support:

- overview;
- players and roles;
- characters;
- invitations;
- permissions;
- sessions;
- scenes;
- timeline;
- notes;
- packs;
- house rules;
- relationships;
- factions;
- world links;
- active adventures;
- shared assets;
- recovery and export status.

## 44.5 Campaign creation

Campaign creation should establish:

- campaign identity;
- GM and owner roles;
- title and summary;
- rules profile;
- setting or World bindings;
- installed and permitted packs;
- visibility defaults;
- session policy;
- character rules;
- house-rule state;
- backup and recovery policy.

Creation may begin as a draft and become active only after required validation.

## 44.6 Player and role management

The GM should be able to:

- invite participants;
- assign permitted roles;
- view membership status;
- remove or suspend access with appropriate safeguards;
- delegate limited controls;
- manage character assignments;
- view permission warnings.

Role changes must be enforced at service level and produce audit evidence.

## 44.7 Character oversight

The GM may, according to campaign policy:

- review characters;
- approve creation;
- identify validation failures;
- grant campaign content;
- apply adjudications;
- approve advancement;
- manage NPC or temporary control;
- inspect character history.

GM authority must not become invisible mutation. Changes should identify source and reason.

## 44.8 Campaign timeline

The campaign timeline should combine accepted events and GM-authored campaign records without confusing them with canonical history.

The GM may inspect:

- session events;
- world-state changes;
- relationship changes;
- discoveries;
- objectives;
- character events;
- adventure milestones;
- created scenes.

## 44.9 Notes

GM notes may be:

- private;
- linked to campaign;
- linked to scene;
- linked to NPC;
- linked to clue;
- linked to location;
- linked to future trigger.

GM notes must not leak through player search, exports, AI context, or error messages.

## 44.10 Packs and content availability

The GM should be able to inspect:

- installed packs;
- campaign-enabled packs;
- dependencies;
- optional content;
- compatibility;
- migration requirements;
- entitlement grants;
- support blockers.

The GM should not be able to override owner-only production, licensing, or global canon gates.

## 44.11 House rules

The GM may create campaign-scoped house rules where permitted.

The house-rule interface should show:

- base rule;
- changed behavior;
- affected content;
- active scope;
- validation;
- player-visible explanation;
- activation history;
- deactivation or migration.

Affected players should be able to inspect active rules.

## 44.12 Relationship management

The GM relationship view should support:

- person-to-person;
- person-to-faction;
- faction-to-faction;
- membership;
- reputation;
- office;
- promise;
- debt;
- hidden and public facets;
- historical events.

The graph is a view over governed records and events.

## 44.13 Campaign and scene builder

The campaign and scene builder should allow the GM to organize:

- campaigns;
- adventures;
- acts;
- routes;
- quests;
- objectives;
- scenes;
- entry and exit links;
- consequences;
- rewards;
- timelines.

The builder should support both planned sequences and nonlinear graphs.

## 44.14 Scene definition editor

A scene editor should support:

- scene type;
- title;
- player-visible description;
- GM description;
- location;
- map or visual;
- environment;
- creatures;
- NPCs;
- hazards;
- traps;
- interactables;
- clues;
- objectives;
- hidden information;
- triggers;
- rewards;
- entry and exit links;
- notes;
- validation.

The GM should use the universal object picker instead of separate inconsistent selectors for every domain.

## 44.15 Scene composition

Objects added to a scene should be placements or bindings.

The scene does not copy the canonical Definition.

A placement may specify:

- scene role;
- position or zone;
- visibility;
- variant;
- current state;
- trigger;
- source;
- notes.

## 44.16 Map management

The GM should be able to:

- upload or select a map;
- connect it to a Location or Scene;
- define grid, zones, or theater-of-the-mind mode;
- place visible and hidden objects;
- manage layers;
- reveal areas;
- add notes and anchors;
- preview player view.

Uploading a map does not automatically establish canonical geography.

## 44.17 Environment selection

The GM should select governed Environment Definitions and add campaign or scene state.

The editor should preview:

- active environmental effects;
- adaptation requirements;
- hazards;
- visibility;
- movement implications;
- relevant rules;
- missing dependencies.

## 44.18 Creature and NPC placement

The GM should be able to:

- search governed creatures and NPC archetypes;
- inspect rules;
- select variants or templates;
- place instances;
- customize campaign state;
- assign hidden knowledge;
- link relationships;
- set scene role.

Campaign changes should not rewrite the source creature or NPC Definition.

## 44.19 Hazard and trap placement

Hazards and traps should support:

- hidden state;
- trigger;
- detection;
- disarm or interaction;
- effects;
- timing;
- reset;
- location;
- player-visible projections;
- source rules.

## 44.20 Clue preparation

The GM should prepare:

- clue definition;
- source;
- discoverable portions;
- reveal conditions;
- reliability;
- linked scenes;
- linked objectives;
- recipients;
- consequences.

The GM should be able to preview exactly what each player or party sees.

## 44.21 Objective preparation

The GM should define:

- objective;
- availability;
- visibility;
- success;
- failure;
- dependencies;
- rewards;
- consequences;
- scene and route links.

Objective completion must produce an accepted event.

## 44.22 Live GM workspace

The live GM workspace should foreground:

- active scene;
- participants;
- pending proposals;
- approvals;
- current objectives;
- hidden information;
- encounter or timing state;
- quick object and rule inspection;
- NPC, creature, hazard, and environment controls;
- session pause, checkpoint, and recovery.

## 44.23 Approval queue

The approval queue should show each proposal with:

- acting player or controller;
- actor;
- action;
- quick rule link;
- target;
- declared costs;
- roll or deterministic result;
- modifiers;
- computed result;
- proposed effects;
- warnings;
- hidden-information context;
- approve;
- deny;
- modify.

The queue should group and prioritize time-sensitive items.

## 44.24 GM-controlled actions

When the GM acts for enemies or NPCs, the system should provide the same clear calculation and approval information.

The GM may have a streamlined confirm step, but the operation still produces an attributable authoritative event.

## 44.25 Modification

The GM may alter permitted proposal results.

The modification interface should preserve:

- original result;
- changed values;
- final result;
- reason or note;
- affected effects;
- validation;
- visibility.

The GM should be able to correct:

- roll interpretation;
- target;
- damage or effect values;
- condition application;
- resource cost;
- narrative outcome;
- another governed field.

Not every modification must be exposed to players in full detail, but the audit record remains complete.

## 44.26 Denial

A denial should support:

- reason category;
- player-facing explanation;
- hidden GM note;
- whether resubmission is permitted;
- whether costs were committed;
- event or proposal status.

## 44.27 Quick rules inspection

The GM should open an action, ability, item, condition, creature, environment, or house rule without leaving the active scene.

The inspector should show source and applied overrides.

## 44.28 NPC and enemy controls

The GM should be able to:

- select NPC or creature;
- view current state;
- choose actions;
- select targets;
- spend resources;
- apply conditions;
- move;
- inspect behavior guidance;
- alter or confirm result.

AI behavior suggestions remain advisory.

## 44.29 Hidden information control

The live GM view may show:

- hidden tokens;
- unrevealed clues;
- secret objectives;
- actual motives;
- hidden conditions;
- private notes;
- trigger regions;
- unrevealed map layers.

The GM should have a reliable player-view preview.

## 44.30 Improvisation

The GM should be able to add during play:

- temporary NPC;
- creature placement;
- hazard;
- clue;
- note;
- objective;
- item;
- scene transition;
- campaign event.

Improvised material should be clearly scoped to the campaign and may later be promoted through a governed creator workflow.

## 44.31 Session controls

The GM should control:

- start;
- pause;
- resume;
- checkpoint;
- scene transition;
- reconnect policy;
- end session;
- recovery;
- post-session finalization.

These controls must not imply production deployment authority.

## 44.32 Checkpoint and recovery

The GM should be able to:

- create a safe checkpoint;
- see last confirmed event;
- inspect disconnected participants;
- resume from authoritative state;
- reject stale proposals;
- reconcile recoverable queued operations;
- restore from an approved snapshot.

## 44.33 Post-session workflow

After a session, the GM may:

- review events;
- finalize notes;
- mark objectives and milestones;
- review rewards and consequences;
- create recap;
- schedule or prepare next scene;
- inspect unresolved proposals;
- confirm backup or snapshot;
- share permitted summary.

## 44.34 GM content editing boundary

The GM can create campaign-local content and state.

Global canonical promotion remains a Content Creator or owner-governed workflow.

The GM interface must distinguish:

- campaign edit;
- derived local object;
- reusable draft;
- canonical submission.

## 44.35 Contextual AI

GM-facing AI may:

- summarize scene state;
- suggest encounter participants;
- check scene preparation for omissions;
- draft NPC dialogue;
- organize clues;
- suggest relationships;
- explain rules;
- prepare recap;
- identify unresolved state.

AI must not:

- reveal protected data to players;
- approve proposals;
- alter state;
- publish canon;
- act as the GM without explicit bounded authority.

## 44.36 GM acceptance slice

The first playable GM slice is complete when a GM can:

1. create or open a campaign;
2. invite a player;
3. inspect or approve a character;
4. build a scene with real governed objects;
5. save the scene;
6. open it as a live session;
7. receive a player proposal;
8. inspect actor, action, rule, target, costs, roll, result, effects, and warnings;
9. approve, deny, or modify;
10. observe synchronized persistent state;
11. perform an NPC or enemy action;
12. checkpoint, disconnect, reconnect, and resume.

## 44.37 Controlling references

- Stage A A3 Identity, Dashboard, and Workspace Selection
- Stage A A5 Campaign and Scene Workspace
- Stage A A6 First Playable Action and Approval Loop
- Stage A A7 Full Combat Interface
- Stage A A9 Investigation and Social Workspaces
- Stage A A10 World Builder and Content Creation
- authoritative-session architecture
- owner GM workflow feedback
- campaign, scene, object, permission, persistence, and recovery contracts

**Status:** Owner-approved planned experience. Full repository implementation remains to be verified and completed.

---

# 45. Character Builder and Character Workspace

## 45.1 Purpose

Define the complete user-facing lifecycle for discovering, creating, validating, saving, opening, using, advancing, migrating, retiring, archiving, and recovering a character.

The character builder and character sheet must use the same governed data and rules as live play.

## 45.2 Character workspace principle

The character workspace is one persistent character-centered environment.

It should not be split into unrelated creation, sheet, inventory, progression, and session implementations that calculate character state differently.

## 45.3 Character list

The character list should support:

- owned characters;
- controlled characters;
- campaign-bound characters;
- drafts;
- active characters;
- migration-required characters;
- retired characters;
- archived characters.

Filtering may include:

- campaign;
- status;
- species or form;
- progression;
- last activity;
- validation;
- ownership.

## 45.4 Character card

A character card should show enough information to select correctly:

- portrait;
- name;
- campaign;
- owner or controller;
- status;
- progression summary;
- current condition summary;
- validation warning;
- last activity.

The card should not reproduce the full character sheet.

## 45.5 New character entry

The new character flow should begin by choosing:

- create for a campaign;
- create without a campaign where allowed;
- use a campaign template;
- clone a permitted character as a new draft;
- import;
- recover.

Each path creates a new governed draft or import operation with separate identity.

## 45.6 Creation stages

A bounded character-creation flow should include:

1. campaign and rules context;
2. identity and ownership;
3. species, lineage, form, or equivalent foundation;
4. attributes and derived values;
5. skills and proficiencies;
6. starting traits and abilities;
7. progression choices;
8. equipment and resources;
9. relationships or campaign ties;
10. appearance and biography;
11. validation;
12. creation confirmation.

A campaign or rules profile may omit, rename, reorder, or add stages through governed configuration.

## 45.7 Campaign and rules context

The first stage should identify:

- campaign;
- rules profile;
- allowed packs;
- content entitlement;
- character creation constraints;
- starting progression;
- house rules;
- required approvals;
- visibility.

The builder must not allow a later choice to remain selected after the context changes if the choice is no longer valid.

## 45.8 Identity and ownership

The character identity stage may include:

- name;
- pronouns;
- player or owner;
- authorized controllers;
- campaign;
- portrait;
- private or shared draft state;
- campaign role.

Names are display values, not stable identity.

## 45.9 Species, lineage, and form

The builder should present legal source-grounded options.

Each option should show:

- summary;
- source;
- fixed grants;
- optional grants;
- forms;
- adaptations;
- prerequisites;
- restrictions;
- campaign compatibility;
- relevant rules.

The UI should distinguish biological species, cultural origin, form, and campaign background rather than merging them into one unclear ancestry field.

## 45.10 Choice dependencies

Selecting a species, form, progression node, or campaign option may:

- add choices;
- remove choices;
- satisfy prerequisites;
- create exclusions;
- alter costs;
- change equipment compatibility;
- change environment behavior.

The builder should explain these effects and preserve prior valid work when possible.

## 45.11 Attributes

The attribute stage should support the governing creation method.

It may include:

- allocated points;
- arrays;
- rolls;
- fixed values;
- source grants;
- campaign adjustments.

The builder should show:

- current value;
- base value;
- source adjustments;
- limits;
- remaining budget;
- derived impacts;
- validation.

UI code must not maintain a competing attribute formula.

## 45.12 Derived values

Derived values should update through canonical rules profiles.

A preview should identify:

- formula source;
- contributing values;
- current result;
- pending changes.

## 45.13 Skills and proficiencies

The builder should support:

- required choices;
- optional choices;
- grants;
- ranks;
- substitutions;
- exclusions;
- prerequisites;
- campaign restrictions.

Duplicate grants should be handled through canonical replacement, stacking, conversion, or rejection rules.

## 45.14 Traits and abilities

Ability selection should use the universal object browser and progression model.

The builder should show:

- ability tier;
- prerequisites;
- cost;
- grants;
- actions;
- effects;
- resources;
- exclusions;
- scaling;
- source;
- campaign availability;
- entitlement.

The approved free-access policy limits ability trees to the first two tiers, including abilities received through grants, unless campaign grants, sponsored access, or other approved entitlement policy provides access.

## 45.15 Starting equipment

Equipment selection should respect:

- ownership;
- creation budget;
- campaign grants;
- item prerequisites;
- form and scale;
- equipment slots;
- pack access;
- shared asset policy;
- quantity and stacking.

The builder should create governed item instances or starting grants, not copy item definitions.

## 45.16 Resources

Starting resources should show:

- base amount;
- source;
- maximum;
- current starting value;
- recovery rule;
- campaign adjustment.

## 45.17 Relationships and ties

Campaign-specific character creation may include:

- faction membership;
- relationships;
- patron;
- obligation;
- reputation;
- location;
- shared history;
- campaign hook.

These create campaign-scoped relationships, not global changes to the reusable faction or setting definitions.

## 45.18 Appearance and biography

Appearance and biography should be separated from mechanical state.

The character may include:

- portrait;
- body and appearance description;
- clothing or visual style;
- biography;
- personality notes;
- voice or presentation notes;
- private player notes;
- visible campaign summary.

Appearance tools may support detailed customization, but visual choices must not silently apply mechanics.

## 45.19 Draft saving

The builder should autosave or explicitly save a draft.

Draft state should indicate:

- last saved;
- unsaved;
- offline queued;
- save failed;
- conflict;
- recovered version.

A draft may remain incomplete.

## 45.20 Validation

Character validation should check:

- identity and ownership;
- campaign membership;
- required stages;
- species and form compatibility;
- choice budgets;
- attributes;
- skills;
- prerequisites;
- mutual exclusions;
- duplicate grants;
- progression;
- equipment;
- resources;
- entitlement;
- house rules;
- pack and schema compatibility.

## 45.21 Validation presentation

Validation results should be grouped as:

- blocking errors;
- warnings;
- recommendations;
- owner or GM approval required.

Each result should link to the affected stage and identify the rule source.

## 45.22 Creation confirmation

Before creating a playable character, the confirmation view should show:

- campaign;
- rules profile;
- identity;
- major choices;
- progression;
- abilities;
- equipment;
- resources;
- relationships;
- unresolved warnings;
- approval requirements.

Confirming should produce the character creation event or governed aggregate creation operation.

## 45.23 GM approval

A campaign may require GM approval.

The GM approval view should show:

- build summary;
- validation;
- source content;
- campaign exceptions;
- house rules;
- requested grants;
- warnings.

Approval should not erase the submitted draft history.

## 45.24 Character overview

The character overview should summarize:

- identity;
- portrait;
- campaign;
- progression;
- current state;
- key resources;
- conditions;
- equipment;
- current objectives;
- recent events;
- validation or migration warnings.

## 45.25 Character sheet sections

The complete sheet should support:

- overview;
- attributes;
- derived values;
- skills;
- traits;
- abilities;
- resources;
- conditions;
- inventory;
- equipment;
- progression;
- relationships;
- notes;
- journal;
- history;
- source and provenance where permitted.

## 45.26 Permanent and temporary state

The sheet must distinguish:

- base character choices;
- permanent progression;
- campaign grants;
- equipment grants;
- active form;
- temporary effects;
- conditions;
- environment modifiers;
- GM adjudications.

A total value should be inspectable as a breakdown.

## 45.27 Ability workspace

The ability view should support:

- known abilities;
- available actions;
- passive grants;
- resource costs;
- source;
- progression path;
- current availability;
- conditions affecting use;
- quick rules inspection.

## 45.28 Resource workspace

The resource view should show:

- current;
- maximum;
- source;
- recovery;
- recent changes;
- visibility;
- warnings.

Direct editing should be permission-controlled and attributable.

## 45.29 Conditions workspace

Conditions should show:

- name;
- source;
- duration;
- stacks;
- effects;
- removal;
- visibility;
- recent changes.

## 45.30 Inventory workspace

The inventory should support:

- carried;
- equipped;
- containers;
- shared;
- stored;
- borrowed;
- assigned;
- quantities;
- condition;
- charges;
- ownership;
- custody;
- transfers;
- trades;
- crafting;
- repair.

## 45.31 Equipment workspace

Equipment should show:

- slots or locations;
- active loadout;
- compatibility;
- granted abilities;
- resource use;
- conflicts;
- condition;
- quick swap where permitted.

## 45.32 Shared assets

A character may be linked to a shared vehicle, facility, container, or party asset.

The workspace should show:

- relationship;
- ownership;
- authorization;
- station or role;
- current location;
- condition;
- resources;
- permitted actions.

## 45.33 Progression workspace

The progression workspace should support:

- current progression graph;
- acquired nodes;
- available nodes;
- prerequisites;
- exclusions;
- costs;
- preview;
- advancement history;
- respec policy;
- campaign approval.

## 45.34 Advancement transaction

Advancement should:

1. capture before-state fingerprint;
2. validate prerequisites and currency;
3. preview grants and removals;
4. confirm;
5. apply event;
6. validate resulting projection;
7. produce receipt;
8. synchronize.

## 45.35 Respec

A respec should be available only when permitted.

It should show:

- affected selections;
- dependent selections;
- refunded or consumed resources;
- equipment or ability implications;
- campaign approval;
- resulting validation.

The original advancement history remains preserved.

## 45.36 Notes and journal

The character workspace should support:

- private notes;
- campaign-shared notes;
- GM-shared notes;
- journal entries;
- links to events;
- links to clues;
- links to relationships;
- links to locations.

## 45.37 Character history

History should show accepted events such as:

- creation;
- campaign binding;
- advancement;
- grants;
- condition changes;
- item acquisition;
- ownership changes;
- form changes;
- retirement;
- migration;
- recovery.

The view should be permission-aware and readable.

## 45.38 Character in live session

Opening a character during a session should preserve:

- live scene context;
- selected action;
- pending proposal;
- connection state;
- GM decision status.

The full sheet may open in a panel or secondary route without discarding the live task.

## 45.39 Multiple forms

A character with multiple forms should support:

- base form;
- available forms;
- active form;
- form-specific grants;
- retained state;
- equipment behavior;
- transformation cost;
- reversion;
- visibility.

The UI should preview what changes before transformation.

## 45.40 Migration

When migration is required, the character workspace should show:

- affected content;
- old and target versions;
- proposed mappings;
- lost or changed capabilities;
- unresolved selections;
- required decisions;
- backup state;
- validation.

Migration must not silently discard historical selections.

## 45.41 Import

Character import should:

- inspect format;
- identify source;
- map stable IDs;
- detect missing packs;
- preserve provenance;
- create preview;
- report unresolved fields;
- validate;
- require confirmation.

An import is not complete until the resulting character is stored and validated.

## 45.42 Export

Character export should preserve, as permitted:

- identity;
- Definition references;
- progression;
- inventory;
- relationships;
- history;
- source and provenance;
- pack versions;
- schema versions;
- migration information;
- attachments or lawful references.

Private campaign or GM-only data must not leak into a player export.

## 45.43 Retirement and archive

Retirement should:

- remove the character from ordinary active selection;
- preserve campaign and event history;
- preserve ownership;
- allow authorized viewing;
- support restoration where policy permits.

Archive may reduce visibility or active indexing without deleting the character.

## 45.44 Recovery

Recovery should support:

- failed autosave;
- local draft;
- snapshot;
- backup;
- provider-exit import;
- migration rollback.

The recovery interface should compare versions and identify conflicts.

## 45.45 Accessibility

Character creation and sheet use must support:

- keyboard;
- touch;
- screen readers;
- scalable text;
- accessible progression graphs;
- noncolor validation;
- clear focus movement;
- error summary;
- reduced motion.

## 45.46 Contextual AI

Character-facing AI may:

- explain abilities;
- identify legal choices;
- compare equipment;
- summarize progression;
- find missing prerequisites;
- help draft biography text.

AI must not:

- choose build options without explicit instruction;
- spend progression;
- equip or transfer items;
- alter state;
- bypass entitlement;
- invent canonical mechanics;
- submit GM approval automatically.

## 45.47 Character acceptance slice

The Character Workspace stage is complete when a player can:

1. create a draft;
2. select campaign and rules context;
3. choose species or form;
4. allocate attributes;
5. choose skills and abilities;
6. choose starting equipment;
7. resolve validation;
8. submit or confirm creation;
9. open the saved character;
10. use the character in a live scene;
11. advance the character;
12. save, reload, export, migrate, and recover without losing identity or history.

## 45.48 Controlling references

- Stage A A4 Character Workspace
- Stage A A6 First Playable Action and Approval Loop
- character lifecycle and progression architecture
- species, forms, abilities, inventory, and entitlement architecture
- provider-neutral identity, persistence, migration, and session ports
- character golden fixtures and pack contracts

**Status:** Owner-approved planned experience. Full repository implementation remains to be verified and completed.



# 46. Campaign, Session, and Scene Builder

## 46.1 Purpose

Define the Game Master tools used to create and operate campaigns, sessions, scenes, adventures, timelines, relationships, world links, and campaign-local content through governed reusable objects and live state.

The builder must support both careful preparation and rapid improvisation without turning campaign edits into silent changes to global canon.

## 46.2 Builder principle

The builder should use one consistent object and relationship architecture.

A GM should not need separate incompatible tools for:

- creatures;
- NPCs;
- items;
- locations;
- environments;
- traps;
- hazards;
- clues;
- objectives;
- vehicles;
- factions;
- maps.

The universal object picker, object inspector, placement model, relationship model, and validation system should serve all domains.

## 46.3 Campaign creation flow

Campaign creation should establish:

1. campaign identity;
2. owner and GM authority;
3. title and summary;
4. rules profile;
5. setting or world bindings;
6. installed and campaign-enabled packs;
7. allowed character content;
8. player invitation policy;
9. visibility defaults;
10. house rules;
11. session and approval policy;
12. backup and recovery settings;
13. initial validation.

A campaign may remain a draft until all required fields pass validation.

## 46.4 Campaign dashboard

The campaign dashboard should show:

- campaign status;
- active and upcoming sessions;
- current adventure or arc;
- participants and unresolved invitations;
- characters;
- draft and active scenes;
- objectives and milestones;
- relationship or faction changes;
- recent events;
- pack or migration warnings;
- pending approvals;
- backup and recovery state.

The dashboard should provide direct paths to the next likely GM task.

## 46.5 Campaign navigation

Campaign navigation should include, as appropriate:

- Overview;
- Players;
- Characters;
- Sessions;
- Scenes;
- Adventures;
- Timeline;
- Relationships;
- Factions;
- World;
- Notes;
- Packs;
- House Rules;
- Assets;
- Recovery and Export.

Navigation should be permission-scoped and responsive.

## 46.6 Players and invitations

The campaign player manager should support:

- invitation creation;
- invitation status;
- role assignment;
- character assignment;
- membership suspension or removal;
- controller delegation;
- visibility and permission review.

The interface must show the difference between:

- invited;
- accepted;
- active;
- suspended;
- removed;
- expired.

## 46.7 Character management

The GM should be able to:

- inspect campaign-bound characters;
- review validation;
- approve or reject submitted characters;
- assign campaign grants;
- review progression;
- transfer permitted control;
- mark unavailable or retired;
- open history.

Character edits must identify whether they are:

- player changes;
- GM grants;
- migration;
- adjudication;
- campaign-local override.

## 46.8 Campaign world binding

The builder should let the GM bind campaign context to:

- Worlds;
- Realities;
- Setting Nodes;
- Regions;
- Settlements;
- Locations;
- timelines;
- travel networks;
- factions;
- cultures;
- religions;
- lore;
- world variants or layers.

Bindings create campaign placement and state. They do not rewrite the reusable source pack.

## 46.9 Campaign timeline

The timeline tool should support:

- canonical historical references;
- campaign events;
- session events;
- adventure milestones;
- world-state changes;
- faction changes;
- character events;
- planned future entries;
- alternate or divergent timeline branches.

The view must distinguish:

- canonical history;
- campaign history;
- planned material;
- player-visible history;
- GM-only history.

## 46.10 Adventure placement

A GM may add an adventure by selecting:

- Adventure Definition;
- campaign;
- setting or location binding;
- timeline or era;
- selected hook;
- starting route;
- scaling profile;
- player visibility;
- cast and encounter substitutions.

Placing an adventure creates live adventure state without modifying the source Adventure Definition.

## 46.11 Campaign-local adventures

The GM may create a campaign-local adventure.

Campaign-local adventure content should use the same structures as reusable content:

- acts;
- hooks;
- routes;
- quests;
- objectives;
- milestones;
- scenes;
- clues;
- choices;
- rewards;
- consequences.

It must remain visibly campaign-local until submitted through a governed creator workflow.

## 46.12 Scene list

The scene list should distinguish:

- draft;
- validated;
- scheduled;
- active;
- paused;
- completed;
- archived;
- blocked.

Useful filters include:

- adventure;
- act;
- location;
- scene type;
- session;
- objective;
- cast member;
- readiness;
- validation.

## 46.13 Scene creation

A scene creation flow should establish:

- scene identity;
- campaign;
- adventure or campaign-local context;
- scene type;
- player-visible title and summary;
- GM-only preparation;
- location;
- environment;
- map or visual mode;
- entry conditions;
- exit links;
- visibility defaults.

## 46.14 Scene editor layout

A desktop scene editor may use:

- scene outline or scene list;
- central scene canvas or form;
- contextual object inspector;
- validation and readiness panel.

Mobile and tablet versions should transform these into sequential views, drawers, and full-screen inspectors rather than compressing all panels.

## 46.15 Scene content areas

The editor should support:

- visible description;
- GM notes;
- maps and layers;
- environments;
- creatures;
- NPCs;
- hazards;
- traps;
- interactables;
- items;
- vehicles and operational assets;
- clues;
- objectives;
- triggers;
- rewards;
- consequences;
- relationships;
- entry and exit links;
- scene rules;
- audio or handouts;
- validation.

## 46.16 Placements

Adding an object to a scene creates a placement or live instance plan.

The placement may define:

- source Definition;
- variant or template;
- position or zone;
- visibility;
- initial state;
- scene role;
- trigger;
- ownership or controller;
- notes;
- relationship links.

The source object remains owned by its canonical pack.

## 46.17 Map upload and selection

The GM should be able to:

- upload a campaign-local map;
- select an installed Map Definition;
- connect the map to a Location;
- define grid or zone behavior;
- create layers;
- place anchors;
- configure player reveal;
- preview player view.

Upload should preserve:

- source;
- rights or ownership declaration;
- file identity;
- visibility;
- campaign scope.

## 46.18 Theater-of-the-mind mode

A scene may operate without a map.

The editor should support:

- range bands;
- zones;
- relationships;
- descriptive positions;
- named areas;
- movement constraints.

The runtime should not force coordinates into scenes that do not need them.

## 46.19 Environment configuration

The environment editor should allow:

- governed Environment Definition selection;
- scene-specific state;
- weather;
- lighting;
- gravity;
- atmosphere;
- terrain;
- visibility;
- hazards;
- adaptation requirements;
- duration or change triggers.

The editor should preview mechanical consequences and missing dependencies.

## 46.20 Cast placement

The GM should be able to place:

- NPC instances;
- NPC archetypes;
- creature instances;
- groups;
- swarms;
- vehicles;
- organizations represented in the scene.

Placement should include:

- role;
- starting location;
- hidden or visible state;
- controller;
- initial attitude;
- relationship links;
- loadout;
- current condition;
- trigger.

## 46.21 Hazard and trap configuration

Hazard and trap placements should support:

- detection;
- hidden state;
- trigger;
- target;
- timing;
- effects;
- reset behavior;
- disarm or interaction options;
- source rules;
- player-visible presentation.

## 46.22 Interactables

An interactable may be:

- door;
- terminal;
- altar;
- container;
- mechanism;
- object;
- environmental feature;
- vehicle;
- another governed scene subject.

An interactable placement should define available actions and state rather than relying only on prose.

## 46.23 Clues

Clue preparation should support:

- canonical or campaign-local clue;
- source;
- discoverable portions;
- acquisition conditions;
- linked actions;
- linked scenes;
- linked objectives;
- reliability;
- hidden truth;
- recipients;
- consequences.

## 46.24 Objectives

The scene objective editor should support:

- objective Definition;
- scene-specific placement;
- visibility;
- availability;
- success condition;
- failure condition;
- optionality;
- reward;
- consequence;
- linked exit or route.

## 46.25 Triggers

Triggers may respond to:

- scene entry;
- time;
- location;
- action;
- condition;
- discovery;
- objective state;
- participant state;
- GM activation;
- another event.

A trigger should have:

- condition;
- action or effect;
- visibility;
- one-time or repeat behavior;
- priority;
- source;
- validation.

## 46.26 Entry and exit links

A scene may link to:

- previous or next scene;
- multiple routes;
- location;
- adventure act;
- campaign transition;
- downtime;
- another session.

Links should define conditions and consequences.

The editor must support nonlinear graphs.

## 46.27 Scene readiness

Scene readiness should evaluate tracks such as:

- required objects installed;
- participants configured;
- environment configured;
- objectives valid;
- clues linked;
- exits linked;
- hidden information safe;
- map or theater mode ready;
- permissions;
- rules and dependencies;
- save and persistence;
- live-session compatibility.

Readiness may be multidimensional rather than one percentage.

## 46.28 Validation panel

The validation panel should separate:

- blocking errors;
- warnings;
- recommendations;
- owner or GM decisions.

Selecting a finding should take the GM to the affected element.

## 46.29 Preview modes

The editor should provide preview as:

- GM;
- player;
- specific participant where required;
- desktop;
- tablet;
- mobile.

Preview must use actual permission projections rather than cosmetic hiding.

## 46.30 Scene templates

A scene template may provide reusable structure.

A template should remain separate from:

- scene Definition;
- campaign Scene Instance;
- saved scene copy.

Creating from a template produces a new scene identity.

## 46.31 Duplicate and clone

Cloning a scene should:

- create new identity;
- preserve source relationships;
- copy selected placements;
- allow remapping;
- avoid duplicating referenced canonical Definitions;
- preserve campaign-local provenance.

## 46.32 Session planning

A session plan may group:

- intended scenes;
- expected transitions;
- participants;
- objectives;
- backup scenes;
- reminders;
- expected duration;
- content dependencies;
- recovery checkpoint.

The plan is advisory. Live play may diverge.

## 46.33 Session creation

Creating a session should establish:

- campaign;
- GM;
- participants;
- assigned characters;
- planned scenes;
- authoritative-session policy;
- visibility;
- connection settings;
- initial checkpoint;
- start state.

## 46.34 Session status

A session may be:

- planned;
- open;
- live;
- paused;
- recovering;
- ended;
- finalized;
- archived.

Exact enums remain implementation-controlled.

## 46.35 Session entry

Before starting, the GM should see:

- participant connection;
- character validation;
- required packs;
- scene readiness;
- unresolved migrations;
- current checkpoint;
- permission warnings.

## 46.36 Scene activation

Activating a scene should:

- validate the scene;
- instantiate required placements;
- load current campaign state;
- create or select authoritative scene state;
- apply visibility;
- synchronize participants;
- emit activation event.

## 46.37 Scene transition

A transition should preserve:

- source scene result;
- selected route or exit;
- carried participants;
- carried conditions where applicable;
- time change;
- objectives;
- inventory and ownership;
- unresolved effects;
- event history.

## 46.38 Improvised scene creation

During play, the GM should be able to create a minimal scene quickly.

A rapid scene may begin with:

- title;
- type;
- description;
- environment;
- participant placement;
- map or no-map mode.

Additional structure can be added during or after play.

## 46.39 Save and version history

The builder should maintain:

- draft save;
- autosave;
- version history;
- validation state;
- last editor;
- change summary;
- recovery version.

Canonical source updates and campaign edits must remain distinguishable.

## 46.40 Collaboration

Future collaborative preparation may support multiple permitted editors.

Collaboration must handle:

- field conflicts;
- presence;
- comments;
- version history;
- permissions;
- save ownership;
- recovery.

No collaboration provider is selected by this requirement.

## 46.41 Export

Campaign or scene export should preserve:

- stable IDs;
- local content;
- placements;
- events;
- visibility;
- pack references;
- media references;
- schemas;
- versions;
- migration and recovery metadata.

Player exports must exclude GM-only content.

## 46.42 AI assistance

AI may help the GM:

- check a scene for omissions;
- suggest governed objects;
- propose links or objectives;
- draft descriptive text;
- summarize dependencies;
- generate a noncanonical backup scene;
- identify permission risks.

AI must not:

- start a session;
- reveal hidden information;
- publish campaign-local content;
- alter live state;
- approve its own content.

## 46.43 Acceptance criteria

The Campaign and Scene Builder stage is complete when a GM can:

1. create a campaign;
2. configure rules and packs;
3. invite a player;
4. bind or approve a character;
5. create an adventure or campaign-local structure;
6. create a scene;
7. add real governed creatures, NPCs, hazards, clues, objectives, environments, and assets;
8. upload or select a map;
9. preview player and GM views;
10. pass validation;
11. save and reopen;
12. create a session;
13. activate the scene;
14. transition and recover without data loss.

## 46.44 Controlling references

- Stage A A5 Campaign and Scene Workspace
- Stage A A6 First Playable Action and Approval Loop
- Stage A A10 World Builder and Content Creation
- campaign, adventure, scene, placement, objective, clue, environment, map, and relationship architectures
- provider-neutral persistence and authoritative-session contracts

**Status:** Owner-approved planned experience. Repository implementation remains to be verified and completed.

---

# 47. Live Session and Approval Workflows

## 47.1 Purpose

Define the authoritative live-session lifecycle connecting Player and GM devices through proposal, validation, calculation, adjudication, acceptance, persistence, synchronization, reconnect, and recovery.

## 47.2 Required vertical slice

The first playable vertical slice is:

> Campaign → Character → Scene → Action proposal → GM inspection, modification, or approval → Result → synchronized persistent state

This loop is the minimum proof that navigation, real data, rules, permissions, persistence, realtime, and recovery work together.

## 47.3 Authority principle

The authoritative service owns accepted session state.

Clients may:

- display;
- collect input;
- preview;
- submit proposals;
- cache permitted data;
- queue permitted offline actions.

Clients must not independently declare accepted canonical session outcomes.

## 47.4 Session participants

A session may include:

- GM;
- player;
- assistant GM;
- observer;
- owner or administrator;
- controlled NPC or entity clients;
- automation or AI service with bounded permissions.

Each participant receives a role-filtered projection.

## 47.5 Session connection

A session connection should identify:

- session ID;
- participant identity;
- role;
- device or client;
- character or controlled entities;
- connection state;
- protocol or contract version;
- last acknowledged event;
- permissions.

## 47.6 Connection states

A client may be:

- connecting;
- synchronized;
- degraded;
- reconnecting;
- stale;
- disconnected;
- rejected;
- recovered.

Exact enums remain implementation-controlled.

## 47.7 Authoritative sequence

Accepted events should have a deterministic sequence or equivalent ordering.

Clients should be able to determine:

- last applied event;
- current authoritative version;
- whether their projection is current;
- whether a proposal was accepted, rejected, or stale.

## 47.8 Proposal creation

A proposal should include:

- proposal ID;
- session;
- actor;
- submitting participant;
- action;
- targets;
- options;
- intended costs;
- client-known state version;
- idempotency key;
- local timestamp;
- required visibility context.

## 47.9 Client preview

The client may preview:

- eligibility;
- target legality;
- cost;
- likely modifiers;
- likely outcomes.

Preview is advisory.

The authoritative service revalidates against current state.

## 47.10 Submission

Submission should:

- preserve the proposal ID;
- prevent duplicate action;
- show pending state;
- allow cancellation only where policy permits;
- survive transient connection loss when safely queued.

## 47.11 Validation

The authoritative service checks:

- participant permission;
- actor control;
- session and scene state;
- action availability;
- timing;
- prerequisites;
- target validity;
- range or relationship;
- visibility;
- costs;
- resources;
- content entitlement;
- installed pack versions;
- stale state;
- approval requirement.

## 47.12 Validation failure

A failed proposal should return:

- typed reason;
- affected field;
- whether resubmission is possible;
- whether cost was committed;
- current authoritative version;
- safe player-facing explanation.

No hidden partial state change may occur.

## 47.13 Calculation

A valid proposal proceeds to calculation.

Calculation should preserve:

- rules profile;
- input state;
- roll or deterministic seed;
- modifiers;
- substitutions;
- reactions;
- conditional branches;
- computed effects;
- warnings;
- engine version.

## 47.14 Random results

Random results should be:

- generated by the authoritative service; or
- supplied through an approved verifiable process.

The result must be recorded.

A client must not reroll during reconnect or replay.

## 47.15 Approval requirement

The session policy determines which proposals require GM review.

Approval may be required for:

- all player actions;
- selected action types;
- hidden-information actions;
- ambiguous results;
- actions affecting protected state;
- campaign-specific cases.

## 47.16 GM approval item

The approval item should include:

- requester;
- acting player;
- actor;
- action;
- rule summary and full-rule link;
- target or targets;
- declared costs;
- roll;
- modifiers;
- computed result;
- proposed effects;
- warnings;
- hidden-information context;
- current state version.

## 47.17 Approval actions

The GM may:

- approve;
- deny;
- modify;
- return for correction;
- hold or defer where policy permits.

Each action creates an attributable decision record.

## 47.18 Approval

Approval accepts the computed result.

The service should:

- revalidate current state;
- apply effects atomically or through governed compensation;
- create accepted events;
- update projections;
- notify participants;
- persist state;
- acknowledge proposal.

## 47.19 Denial

Denial should record:

- proposal;
- GM;
- reason category;
- internal note;
- player-facing explanation;
- cost policy;
- resubmission policy.

## 47.20 Modification

Modification should preserve:

- original calculation;
- modified fields;
- final accepted effects;
- GM;
- reason;
- visibility;
- validation.

The service must validate the modified result before application.

## 47.21 Return for correction

The GM may identify a correctable issue, such as:

- wrong target;
- wrong option;
- missing cost;
- misunderstood action;
- invalid declaration.

The player should receive a new editable proposal state rather than a hidden silent rewrite.

## 47.22 Reactions and interrupts

Reactions may create nested or linked proposal windows.

The session must define:

- trigger;
- eligible participants;
- options;
- priority;
- timeout if governed;
- pass behavior;
- resulting continuation.

Nested workflows require correlation and causation IDs.

## 47.23 Simultaneous proposals

When multiple proposals occur, the service should resolve them through:

- timing rules;
- turn or initiative;
- priority;
- explicit GM ordering;
- conflict detection.

The order must be recorded.

## 47.24 GM-controlled actions

GM-controlled actions should use the same authoritative pipeline.

A streamlined GM action may:

- validate;
- calculate;
- present confirmation;
- accept;
- apply.

The result remains attributable.

## 47.25 Automatic actions

Automatic triggers may execute without manual proposal only when a governed rule and session policy authorize them.

They must still produce:

- source;
- trigger;
- calculation;
- effects;
- event;
- visibility.

## 47.26 Event broadcast

After acceptance, participants receive role-filtered events or projections.

The broadcast must not expose:

- hidden target data;
- GM notes;
- secret conditions;
- unrevealed rolls where rules hide them;
- protected object identities.

## 47.27 Result acknowledgement

Clients should acknowledge applied events.

The service should detect:

- missing acknowledgement;
- duplicate delivery;
- out-of-order delivery;
- stale projection.

## 47.28 Persistent state

Accepted state should persist independently of the realtime transport.

If the realtime connection fails after acceptance, reconnect should recover the accepted event rather than repeating the operation.

## 47.29 Idempotency

Every mutating request should use an idempotency mechanism.

Repeated submission of the same accepted proposal must not double-apply:

- damage;
- resource spending;
- movement;
- inventory transfer;
- conditions;
- rewards.

## 47.30 Stale proposals

A proposal is stale when the authoritative state changed in a way that invalidates the client’s assumptions.

The service may:

- reject;
- request refresh;
- revalidate and continue if safe;
- return for correction.

The behavior must be deterministic.

## 47.31 Disconnect

On disconnect, the client should preserve:

- last confirmed state;
- pending proposal IDs;
- unsent draft proposals;
- last acknowledged event.

It must distinguish:

- confirmed;
- pending;
- locally queued;
- failed.

## 47.32 Reconnect

Reconnect should:

1. authenticate;
2. reestablish role and permissions;
3. provide last acknowledged event;
4. receive missed events or snapshot;
5. reconcile pending proposals;
6. reject stale local state;
7. restore live context.

## 47.33 Checkpoints

A checkpoint may include:

- session;
- scene;
- event cursor;
- projections;
- pack and schema versions;
- pending proposals;
- visibility state;
- integrity fingerprint.

A checkpoint is not a substitute for durable event history.

## 47.34 Recovery

Recovery may be needed after:

- service restart;
- client crash;
- network partition;
- failed migration;
- corrupted projection;
- operator error.

The recovery path should use:

- event history;
- snapshot;
- backup;
- installed pack registry;
- version compatibility;
- integrity checks.

## 47.35 Conflict resolution

A conflict may involve:

- two devices controlling one character;
- two proposals spending the same resource;
- two GMs modifying the same action;
- stale offline queue;
- scene transition during pending action.

The service should reject or serialize conflicting operations and explain the result.

## 47.36 Multi-device policy

A user may use multiple devices for reference or control.

The session policy should define:

- active control device;
- secondary read-only views;
- handoff;
- duplicate prevention;
- loss of control;
- reconnect.

## 47.37 Hidden information

Permission safety applies to:

- proposal payloads;
- validation errors;
- approval queue;
- result events;
- logs;
- replay;
- snapshots;
- AI context;
- offline cache.

## 47.38 Action history

Action history should retain:

- proposal;
- validation;
- calculation;
- GM decision;
- final effects;
- events;
- visibility;
- versions;
- correlation.

The player-facing log may show only a filtered subset.

## 47.39 Replay

Replay should use recorded events and deterministic results.

Replay may support:

- audit;
- recovery;
- bug reproduction;
- session recap;
- test fixture.

Replay must not create new accepted events.

## 47.40 Session pause

Pausing should define:

- whether proposals may be submitted;
- whether timers pause;
- pending approvals;
- connection state;
- autosave and checkpoint.

## 47.41 Session end

Ending should:

- stop new ordinary proposals;
- resolve or cancel pending proposals;
- persist final state;
- create checkpoint;
- prepare recap;
- identify unresolved issues;
- emit end event.

## 47.42 Finalization

Finalization may include:

- rewards;
- milestones;
- notes;
- objective state;
- cleanup;
- backups;
- export.

Finalization should remain reversible until the campaign policy declares it closed.

## 47.43 Observability

The live service should observe:

- connection count;
- proposal latency;
- validation failures;
- approval latency;
- event persistence;
- delivery failures;
- reconnect success;
- stale-proposal rate;
- recovery events.

Logs must avoid protected content and secrets.

## 47.44 Testing

The vertical slice should test:

- one player and one GM;
- two player devices;
- GM action;
- approval;
- denial;
- modification;
- stale proposal;
- duplicate proposal;
- disconnect before result;
- disconnect after result;
- reconnect;
- service restart;
- hidden information;
- save and reload.

## 47.45 AI boundary

AI may:

- explain proposals;
- summarize approval context;
- identify warnings;
- suggest a modification;
- assist with recap.

AI must not:

- approve;
- deny;
- modify;
- submit;
- apply;
- reveal protected data;

unless a later owner-approved bounded automation explicitly grants that capability.

## 47.46 Acceptance criteria

The live-session stage is complete when:

- player and GM connect;
- role-filtered state synchronizes;
- the player proposes a real action;
- the service validates and calculates;
- the GM approves, denies, or modifies;
- accepted effects persist;
- both clients update;
- duplicate submissions are prevented;
- hidden information remains protected;
- disconnect and reconnect recover correctly;
- the session resumes after save and load.

## 47.47 Controlling references

- Stage A A6 First Playable Action and Approval Loop
- Stage A A7 Full Combat Interface
- P9-02 Authoritative Session Architecture
- P9-04 provider-neutral service contracts
- P9-06 identity, persistence, realtime, and session ports
- golden replay and deterministic randomness architecture
- owner approval-loop corrections

**Status:** Canonical planned product workflow with provider-neutral service foundations partially implemented through P9-06-007.

---

# 48. Combat Interface

## 48.1 Purpose

Define the full combat experience for Players and GMs using the shared live-session, proposal, approval, action, effect, condition, resource, map, environment, and event architecture.

The combat interface must support a complete encounter without development-only tools.

## 48.2 Combat workspace principle

Combat should emphasize:

- current scene;
- participants;
- whose decision matters now;
- available actions;
- targets;
- resources;
- conditions;
- movement;
- results;
- GM approvals.

The interface should not be dominated by raw event logs.

## 48.3 Combat modes

The interface should support:

- grid map;
- freeform map;
- zones;
- range bands;
- theater of the mind;
- mixed mode.

The selected mode comes from scene and rules configuration.

## 48.4 Player combat layout

A player combat layout may include:

- scene or map;
- participant and target context;
- character summary;
- action bar or action browser;
- resource and condition panel;
- proposal preview;
- result panel;
- reaction prompt;
- quick rules inspector.

On mobile, these should become focused sequential surfaces.

## 48.5 GM combat layout

The GM layout may include:

- map or scene;
- participant roster;
- turn or timing controls;
- pending approval queue;
- selected entity inspector;
- NPC and enemy action controls;
- objectives;
- environment and hazards;
- hidden information;
- encounter controls;
- event and recovery tools.

## 48.6 Participant roster

The roster should show, as permitted:

- name;
- controller;
- side or relationship;
- current turn or timing;
- visible resources;
- conditions;
- position;
- readiness;
- connection;
- hidden or defeated state.

The GM may see more than players.

## 48.7 Initiative and order

Where the rules profile uses initiative or ordered turns, the interface should support:

- current participant;
- next participant;
- delayed action;
- held action;
- interruption;
- grouped turns;
- custom GM ordering;
- round or phase.

Order changes must create or update authoritative state.

## 48.8 Non-initiative combat

The interface must also support scenes without traditional initiative.

Timing may be:

- simultaneous;
- phase-based;
- spotlight-based;
- action-clock;
- GM-directed;
- rules-profile-specific.

## 48.9 Map interaction

Map interaction should support:

- select participant;
- select target;
- move;
- measure;
- inspect;
- reveal;
- ping;
- place or remove authorized objects;
- change layer;
- open related rules.

The same action should not produce different authoritative meaning depending on mouse versus touch input.

## 48.10 Movement

Movement preview should show:

- path or destination;
- cost;
- range;
- terrain;
- hazards;
- opportunity or reaction risks;
- movement mode;
- invalid segments;
- final state.

The server revalidates movement.

## 48.11 Targeting

Targeting should support:

- single target;
- multiple targets;
- area;
- line;
- cone;
- zone;
- self;
- object;
- location;
- environment.

The interface should show legal targets and reasons for invalidity.

## 48.12 Action browser

The action browser should group actions by:

- current availability;
- category;
- source;
- cost;
- timing;
- item;
- ability;
- form;
- vehicle or station;
- reaction.

It should avoid overwhelming the user with every known action when many are irrelevant.

## 48.13 Action card

An action card should show:

- name;
- source;
- timing;
- cost;
- target type;
- range;
- key outcome;
- availability;
- warning;
- quick rule access.

## 48.14 Proposal preview

Before submission, the preview should show:

- actor;
- action;
- target;
- movement if included;
- costs;
- roll method;
- relevant modifiers;
- expected effect categories;
- warnings;
- approval requirement.

## 48.15 Dice and deterministic results

The interface may animate dice or result presentation, but the authoritative result is the recorded value.

Animation must not:

- reroll;
- delay critical state excessively;
- hide final number;
- prevent reduced-motion use;
- imply that the client generated the accepted result if it did not.

## 48.16 Modifier breakdown

A calculation inspector should show:

- base value;
- source;
- additions;
- multipliers;
- replacements;
- caps;
- floors;
- suppressions;
- final result;
- ordering.

The GM may see hidden modifiers that the player does not.

## 48.17 Damage and mitigation

Result presentation should distinguish:

- incoming effect;
- prevention;
- resistance;
- mitigation;
- redirection;
- applied harm;
- resulting conditions;
- resource changes.

## 48.18 Conditions

Conditions should be visible as compact indicators with quick inspection.

The interface should show:

- source;
- duration;
- stacks;
- mechanical effects;
- expiration;
- removal options.

## 48.19 Resources

Combat resources should be easy to read and hard to edit accidentally.

Direct GM edits should require:

- authority;
- explicit change;
- reason where required;
- event record.

## 48.20 Reactions

Reaction prompts should:

- identify trigger;
- show eligible options;
- show cost;
- show expiry;
- support pass;
- remain accessible on mobile;
- preserve session flow.

## 48.21 Hidden actors

A hidden actor should not leak through:

- map spacing;
- initiative gaps;
- target list;
- network events;
- counts;
- labels;
- accessibility tree.

## 48.22 GM NPC action flow

The GM selects:

1. NPC or creature;
2. action;
3. target;
4. options;
5. costs;
6. result;
7. confirmation or modification.

The operation uses the same authoritative event path as a player action.

## 48.23 Quick rule inspection

The GM and player should inspect:

- action;
- ability;
- item;
- condition;
- environment;
- creature;
- vehicle system;
- house rule.

Inspection should preserve combat context.

## 48.24 Encounter controls

The GM may need controls for:

- add participant;
- remove or archive participant;
- change controller;
- reveal;
- hide;
- set side;
- change position;
- apply condition;
- set objective;
- pause;
- end encounter.

High-impact changes require confirmation and audit.

## 48.25 Objectives

The combat interface should show encounter objectives, not only participant defeat.

Objectives may include:

- escape;
- rescue;
- survive;
- hold;
- capture;
- protect;
- disable;
- retrieve;
- negotiate;
- complete another task.

## 48.26 Environmental controls

The GM should be able to inspect and change:

- light;
- weather;
- terrain;
- atmosphere;
- gravity;
- hazard state;
- scene zones.

Changes produce events and updated projections.

## 48.27 Vehicles and large assets

Combat may include:

- vehicles;
- mecha;
- starships;
- structures;
- facilities.

The interface should support:

- station control;
- crew;
- subsystem state;
- power or fuel;
- scale;
- mounted actions;
- occupant effects.

## 48.28 Groups and swarms

A group or swarm may be represented as one governed participant or linked set according to the rules profile.

The interface should avoid forcing manual management of every member when the source model is aggregate.

## 48.29 Defeat and removal

Defeat, unconsciousness, destruction, escape, surrender, and removal are distinct.

The GM should select the correct state rather than deleting the entity.

## 48.30 Combat end

Ending combat should:

- resolve pending effects;
- preserve ongoing conditions;
- update objectives;
- record result;
- transition scene mode;
- preserve event history;
- create checkpoint.

## 48.31 Replay and audit

The GM should be able to inspect:

- action sequence;
- proposals;
- calculations;
- modifications;
- applied effects;
- state changes.

Replay is read-only.

## 48.32 Accessibility

Combat must support:

- keyboard target selection;
- screen-reader participant and map alternatives;
- noncolor side and status indicators;
- readable result announcements;
- reduced motion;
- scalable text;
- focus-safe reaction prompts;
- touch.

## 48.33 Performance

Large encounters should use:

- virtualized rosters;
- selective map rendering;
- incremental event updates;
- cached permitted object summaries;
- bounded animation.

Performance must not weaken permission checks or event integrity.

## 48.34 AI assistance

AI may:

- summarize combat;
- identify legal options;
- propose tactics;
- help the GM manage large rosters;
- explain modifiers;
- draft encounter recap.

AI must not:

- select or submit player actions;
- approve outcomes;
- expose hidden data;
- alter state;
- act as autonomous opposition without explicit future authorization.

## 48.35 Acceptance criteria

The combat interface is complete when a full encounter can be run with:

- participant order or configured timing;
- player action proposals;
- targeting;
- movement;
- costs;
- rolls;
- modifiers;
- GM approval, denial, and modification;
- NPC and enemy actions;
- conditions;
- resources;
- environment;
- objectives;
- persistence;
- reconnect;
- replay;
- no development-only interface.

## 48.36 Controlling references

- Stage A A7 Full Combat Interface
- Stage A A6 approval loop
- combat game-system architecture
- authoritative-session architecture
- maps, environments, creatures, vehicles, actions, effects, conditions, and resources
- golden replay and deterministic randomness packages

**Status:** Owner-approved planned experience. Full repository implementation remains to be verified and completed.

---

# 49. Inventory, Shared Assets, Crafting, and Vehicles

## 49.1 Purpose

Define the integrated application experience for personal inventory, containers, equipment, shared ownership, party assets, shops, trade, crafting, repair, salvage, vehicles, mecha, starships, and other operational assets.

## 49.2 Experience principle

Assets must move without duplication or loss, and ownership must remain correct.

The UI must distinguish:

- content Definition;
- specific instance;
- ownership;
- custody;
- storage;
- authorized use;
- current controller;
- entitlement.

## 49.3 Inventory scopes

The application should support:

- character inventory;
- equipped inventory;
- container inventory;
- party inventory;
- campaign storage;
- scene inventory;
- shop inventory;
- vehicle cargo;
- facility storage;
- shared asset inventory;
- temporary transfer view.

## 49.4 Inventory list

An inventory list may show:

- item name;
- quantity;
- container;
- owner;
- custodian;
- condition;
- charges;
- equipped state;
- weight, volume, slots, or capacity;
- value reference;
- visibility;
- source.

## 49.5 Inventory grouping

Useful grouping may include:

- equipped;
- carried;
- stored;
- shared;
- borrowed;
- consumable;
- ammunition;
- material;
- tool;
- quest item;
- damaged;
- unavailable.

Grouping is presentation and must not change ownership or container state.

## 49.6 Item inspector

The item inspector should show:

- Definition;
- instance identity;
- owner;
- custody;
- location;
- quantity;
- condition;
- charges;
- modifications;
- capabilities;
- compatible equipment or components;
- history;
- source;
- visibility.

## 49.7 Stack handling

Stack operations should support:

- split;
- merge;
- move;
- transfer;
- consume;
- discard where permitted.

The UI must show when items cannot merge because of different:

- owner;
- condition;
- charges;
- modifications;
- provenance;
- expiration;
- visibility.

## 49.8 Drag and drop

Drag and drop may support inventory movement, but every action must also be available through keyboard and touch-safe controls.

The UI should preview:

- destination;
- capacity;
- ownership consequence;
- permission;
- stack result;
- warnings.

## 49.9 Containers

Container views should show:

- contents;
- capacity;
- restrictions;
- nesting;
- owner;
- custodian;
- access;
- location.

The UI must prevent:

- self-containment;
- illegal cycles;
- silent overflow;
- duplication.

## 49.10 Equipment

The equipment workspace should support:

- slots or body locations;
- loadouts;
- compatibility;
- granted actions or abilities;
- current condition;
- conflicts;
- quick comparison;
- equip;
- unequip;
- swap.

## 49.11 Equipment preview

Before equipping, preview:

- slot changes;
- attribute or derived changes;
- granted abilities;
- removed abilities;
- resource changes;
- conflicts;
- prerequisites;
- resulting validation.

## 49.12 Ownership

Ownership changes require a governed transfer.

A transfer should identify:

- current owner;
- new owner;
- item or asset;
- quantity;
- terms;
- campaign;
- authorization;
- final result.

Custody can change without ownership.

## 49.13 Borrowing

A loan should record:

- owner;
- borrower or custodian;
- item;
- duration or return condition;
- permitted use;
- current location;
- return event;
- damage or loss policy where governed.

## 49.14 Shared ownership

A shared asset may have multiple owners.

The interface should show:

- ownership shares or roles where modeled;
- custodian;
- authorized users;
- current controller;
- transfer rules;
- maintenance responsibility;
- resource responsibility.

## 49.15 Party inventory

Party inventory should support:

- shared ownership;
- designated custodian;
- access policy;
- contribution history;
- withdrawals;
- transfers;
- session use;
- audit.

## 49.16 Shop and market interface

A shop or market view may show:

- seller;
- buyer;
- available inventory;
- offers;
- contextual price;
- currency or barter;
- legality;
- availability;
- reputation effects;
- transaction validation.

Displayed price is contextual, not universal canon.

## 49.17 Trade

A trade flow should show both sides:

- offered assets;
- requested assets;
- quantities;
- ownership;
- capacity;
- currency or barter;
- validation;
- acceptance state.

The transaction applies atomically or through governed compensation.

## 49.18 Crafting workspace

The crafting workspace should support:

- recipe search;
- output preview;
- required inputs;
- alternatives;
- tools;
- facilities;
- skills or abilities;
- time;
- checks;
- quality;
- by-products;
- failure risks.

## 49.19 Crafting availability

A recipe may be:

- known;
- available through equipment;
- available through facility;
- available through campaign content;
- hidden;
- unavailable;
- missing dependency.

## 49.20 Crafting transaction

Crafting should:

1. select recipe;
2. select inputs;
3. validate ownership and availability;
4. select tools and facility;
5. preview time and checks;
6. commit or start project;
7. resolve;
8. consume or reserve inputs;
9. create output instances;
10. record provenance and event.

## 49.21 Immediate and project crafting

The UI should distinguish:

- immediate action;
- scene-scale crafting;
- downtime project;
- long-term project.

The governing recipe determines the mode.

## 49.22 Repair

Repair should support:

- damaged item or asset;
- required parts;
- tools;
- facility;
- time;
- skill or ability;
- restored condition;
- remaining defects;
- cost;
- history.

## 49.23 Modification and upgrade

An upgrade flow should show:

- host asset;
- compatible component;
- slot;
- granted capability;
- resource or capacity impact;
- installation requirements;
- removal behavior;
- resulting validation.

## 49.24 Salvage

Salvage should show:

- source item or wreck;
- recoverable outputs;
- required tools;
- time;
- risks;
- ownership;
- resulting destruction or state change.

Salvage must not duplicate the source asset and outputs simultaneously.

## 49.25 Vehicle list

The vehicle and asset workspace should support:

- personal vehicles;
- party vehicles;
- organizational assets;
- borrowed assets;
- scene assets;
- damaged assets;
- unavailable assets.

## 49.26 Vehicle overview

A vehicle overview should show:

- name and image;
- owners;
- custodian;
- current location;
- operational status;
- crew;
- stations;
- cargo;
- equipment;
- resources;
- integrity;
- conditions;
- movement modes;
- recent events.

## 49.27 Crew and stations

The crew view should support:

- station;
- assigned operator;
- proficiency;
- permissions;
- available actions;
- vacancy;
- control conflict;
- handoff.

## 49.28 Vehicle cargo

Vehicle cargo uses the same container architecture as other inventories, with vehicle-specific capacity and access rules.

## 49.29 Vehicle equipment

Mounted systems and components should support:

- slot;
- subsystem;
- compatibility;
- power or capacity;
- operator;
- actions;
- condition;
- repair.

## 49.30 Travel use

A vehicle may be used as:

- travel asset;
- scene participant;
- mobile container;
- shelter;
- equipment platform;
- combat participant.

The application should not maintain separate unrelated vehicle identities for each mode.

## 49.31 Vehicle scene controls

During a scene, the interface may show:

- current operator;
- crew stations;
- movement;
- resources;
- mounted actions;
- subsystem conditions;
- occupants;
- cargo;
- environment compatibility.

## 49.32 Mecha

A mecha workspace may add:

- pilot link;
- frame;
- components;
- heat;
- energy;
- localized damage;
- transformation modes;
- repair;
- ejection.

Pilot and mecha state remain separate.

## 49.33 Starships

A starship workspace may add:

- bridge stations;
- navigation;
- sensors;
- propulsion;
- power;
- life support;
- cargo;
- hangars;
- damage control;
- travel state.

## 49.34 Facility assets

Facilities may share the same asset architecture for:

- ownership;
- rooms or zones;
- equipment;
- storage;
- power;
- staff;
- damage;
- projects;
- access.

## 49.35 Destruction and loss

The UI must distinguish:

- damaged;
- disabled;
- destroyed;
- lost;
- stolen;
- abandoned;
- impounded;
- inaccessible;
- archived.

Deleting the record is not a valid substitute.

## 49.36 Asset history

History should show:

- acquisition;
- transfer;
- loan;
- equip;
- modification;
- repair;
- use;
- damage;
- salvage;
- loss;
- recovery;
- destruction.

## 49.37 Permissions

Asset operations must enforce:

- ownership;
- custody;
- role;
- station;
- campaign policy;
- session state;
- entitlement.

Hiding a button is insufficient.

## 49.38 Offline and conflict behavior

Offline inventory edits should be limited and clearly queued.

Conflicts may include:

- two users moving the same item;
- spending the same ammunition;
- transferring an already transferred asset;
- editing the same loadout;
- assigning the same station.

The service must reject or reconcile deterministically.

## 49.39 Import and export

Asset export should preserve:

- Definition references;
- instance IDs;
- ownership;
- custody;
- location;
- condition;
- modifications;
- history;
- pack and schema versions;
- provenance.

## 49.40 Accessibility

Inventory and asset tools should support:

- keyboard movement;
- non-drag controls;
- screen-reader labels;
- accessible comparison;
- noncolor condition states;
- touch;
- scalable text;
- clear confirmations.

## 49.41 AI assistance

AI may:

- compare equipment;
- identify compatible components;
- summarize repair needs;
- propose crafting plans;
- optimize visible cargo;
- suggest crew assignments.

AI must not:

- transfer ownership;
- equip;
- consume;
- craft;
- repair;
- salvage;
- assign control;

without explicit user action and authoritative validation.

## 49.42 Acceptance criteria

The inventory and asset stage is complete when users can:

- move items without duplication;
- preserve ownership;
- equip and unequip;
- use containers;
- share and transfer assets;
- trade;
- craft;
- repair;
- salvage;
- manage a shared vehicle;
- assign crew;
- use the vehicle in travel and combat;
- disconnect and recover without loss.

## 49.43 Controlling references

- Stage A A8 Inventory, Equipment, Crafting, and Vehicles
- item, container, ownership, crafting, economy, vehicle, mecha, starship, and operational-asset architectures
- provider-neutral persistence and authoritative-session contracts
- golden installation, transfer, and lifecycle fixtures

**Status:** Owner-approved planned experience. Full repository implementation remains to be verified and completed.



# 50. Investigation and Social Workspaces

## 50.1 Purpose

Define the player- and GM-facing workspaces used to conduct investigations, organize evidence, manage hidden information, track relationships, resolve social scenes, and preserve persistent non-combat consequences.

Investigation and social play must be first-class experiences rather than informal notes attached to a combat-centered application.

## 50.2 Shared principles

Both workspaces should:

- use canonical objects and live campaign state;
- preserve player knowledge separately from GM truth;
- support persistent consequences;
- use the shared action, effect, condition, resource, and approval model;
- distinguish facts from theories, rumors, and deception;
- remain permission-aware in search, export, AI context, and synchronization;
- support desktop and mobile use;
- allow quick transition into scenes, objectives, relationships, or combat.

## 50.3 Investigation workspace structure

The Investigation workspace may include:

- active cases or investigations;
- questions;
- objectives;
- clues;
- evidence;
- witnesses;
- documents;
- locations;
- timelines;
- relationship graph;
- hypotheses;
- unresolved contradictions;
- discoveries;
- notes;
- GM truth;
- activity history.

The player and GM see different role-filtered projections of the same governed investigation state.

## 50.4 Investigation list

An investigation list should show:

- title;
- campaign;
- status;
- active question or objective;
- number of known clues;
- unresolved leads;
- last activity;
- assigned participants;
- visibility.

Useful states may include:

- undiscovered;
- active;
- stalled;
- resolved;
- failed;
- archived.

Exact states remain implementation-controlled.

## 50.5 Investigation overview

The overview should answer:

- What are we trying to learn?
- What is currently known?
- Which leads remain open?
- What evidence is disputed?
- What changed recently?
- What can the player or GM do next?

The GM version may also show hidden answer structure and unrevealed content.

## 50.6 Clue browser

The clue browser should support:

- known clues;
- partially revealed clues;
- linked source;
- discovery method;
- related people, places, and objects;
- reliability;
- visibility;
- linked objectives;
- follow-up leads;
- player notes;
- GM notes.

A clue Definition remains separate from the participant’s knowledge of it.

## 50.7 Evidence view

Evidence should preserve:

- evidence identity;
- source;
- chain of custody where relevant;
- condition;
- discovered portions;
- authenticity or uncertainty;
- linked clues;
- linked subjects;
- related actions;
- visibility;
- provenance.

A document, image, item, testimony, or observation may be evidence without becoming confirmed truth.

## 50.8 Hypotheses

Players should be able to create hypotheses that reference:

- clues;
- evidence;
- subjects;
- locations;
- events;
- relationships;
- unanswered questions.

A hypothesis should show:

- author;
- scope;
- confidence or status;
- supporting evidence;
- conflicting evidence;
- sharing state;
- history.

The application must never display a player hypothesis as canonical fact merely because many clues are linked to it.

## 50.9 Evidence board

An evidence board may provide a graph or canvas view.

It should allow:

- placing clue and evidence cards;
- linking relationships;
- adding notes;
- creating groups;
- filtering;
- arranging by time, location, person, or question;
- sharing selected views.

The board layout is a user-authored projection, not canonical structure.

## 50.10 Timeline view

The investigation timeline should support:

- known events;
- uncertain events;
- conflicting dates;
- inferred events;
- hidden GM events;
- source references.

Visual styling should distinguish certainty and visibility without relying only on color.

## 50.11 Witness and subject views

A witness or subject view may show, as permitted:

- identity;
- relationship to the case;
- statements;
- known whereabouts;
- associated clues;
- reputation;
- attitude;
- contradictions;
- notes;
- history.

GM-only motive, deception, and hidden relationships remain protected.

## 50.12 Investigation actions

The workspace should support governed actions such as:

- search;
- interview;
- analyze;
- compare;
- research;
- observe;
- trace;
- decode;
- test;
- reconstruct.

The action UI should show:

- actor;
- target;
- time;
- cost;
- relevant skill or ability;
- expected information category;
- risk;
- GM approval requirement.

## 50.13 Discovery result

A discovery result should show:

- what became visible;
- source;
- discovering actor or party;
- related clue or evidence;
- confidence or ambiguity;
- new leads;
- consequences;
- event history.

The interface should avoid implying that all discovered information is fully reliable.

## 50.14 Hidden information safety

Investigation content is especially vulnerable to accidental leakage.

Protection must cover:

- clue titles;
- clue counts;
- relationship edges;
- hidden answer nodes;
- map locations;
- thumbnails;
- search matches;
- AI summaries;
- exports;
- activity feeds;
- notifications;
- cache metadata.

## 50.15 GM investigation tools

The GM should be able to:

- create or import an investigation;
- define questions;
- place clues;
- define reveal conditions;
- link evidence;
- define hidden truth;
- preview player knowledge;
- reveal selected portions;
- correct mistaken visibility;
- add consequences;
- track who knows what;
- review action and discovery history.

## 50.16 Nonlinear investigation support

The workspace should support:

- multiple valid leads;
- optional clues;
- redundant clue paths;
- clues discovered in different orders;
- false or misleading evidence;
- partial resolution;
- new questions created during play.

The UI must not assume one linear sequence.

## 50.17 Investigation completion

Completing an investigation may produce:

- conclusion;
- unresolved questions;
- objective completion;
- new adventure route;
- faction or relationship change;
- reward;
- consequence;
- timeline event;
- archived case.

The conclusion should be an accepted campaign event, not merely a closed tab.

## 50.18 Social workspace structure

The Social workspace may include:

- current participants;
- attitudes;
- relationships;
- faction standing;
- reputation;
- leverage;
- promises;
- favors;
- debts;
- obligations;
- known motives;
- hidden motives;
- social conditions;
- objectives;
- dialogue notes;
- social action history.

## 50.19 Social scene overview

The overview should answer:

- Who is involved?
- What does each visible participant appear to want?
- What relationships and obligations matter?
- What is at stake?
- Which actions are available?
- What changed?

The GM may see hidden motives, thresholds, and deceptions.

## 50.20 Relationship inspector

The relationship inspector should show:

- source and target;
- relationship type;
- directionality;
- public facet;
- hidden facet where permitted;
- strength or tier;
- trust, hostility, obligation, or other typed dimensions;
- source events;
- promises, favors, and debts;
- current campaign scope.

## 50.21 Reputation view

A reputation view should distinguish:

- faction reputation;
- regional reputation;
- public reputation;
- private attitude;
- membership;
- rank;
- office;
- permission.

These concepts must not be flattened into one bar.

## 50.22 Influence action flow

A social action proposal should show:

- actor;
- target;
- approach;
- desired outcome;
- stakes;
- leverage;
- offered consideration;
- costs;
- relevant abilities or items;
- risk;
- approval requirement.

## 50.23 Dialogue support

The workspace may provide:

- scene notes;
- speaker indicators;
- visible relationship context;
- dialogue prompts;
- promises and concessions;
- transcript links.

Dialogue text remains separate from accepted mechanical consequences.

## 50.24 Promises, favors, and debts

The interface should support creating, viewing, fulfilling, transferring, breaching, forgiving, and expiring governed social obligations.

Each record should show:

- parties;
- terms;
- source event;
- due condition;
- visibility;
- current state;
- history.

## 50.25 Social conditions

Social conditions may represent:

- trust;
- fear;
- embarrassment;
- suspicion;
- obligation;
- hostility;
- another governed state.

The UI should show source, duration, mechanical effects, visibility, and removal.

## 50.26 Faction workspace connection

The Social workspace should connect to faction and organization views showing:

- membership;
- rank;
- office;
- reputation;
- relationships;
- promises;
- current conflicts;
- visible history.

## 50.27 GM social tools

The GM should be able to:

- inspect hidden motives;
- set or update private attitude;
- manage reputation;
- create or resolve obligations;
- apply social conditions;
- review influence calculations;
- approve, deny, or modify outcomes;
- create campaign events.

## 50.28 Social outcome presentation

The result should show, as permitted:

- accepted outcome;
- attitude change;
- relationship change;
- reputation change;
- promise or debt;
- resource or item exchange;
- new objective;
- escalation;
- transition to another scene mode.

## 50.29 Transition between modes

The workspace should support transition from:

- social to combat;
- social to investigation;
- investigation to social;
- investigation to exploration;
- either mode to downtime or a new scene.

State and event history must carry across the transition.

## 50.30 Notes and privacy

Player and GM notes should have explicit sharing controls.

Private notes must not be sent to AI or search indexes outside the authorized scope.

## 50.31 Accessibility

Graph and board views require accessible alternatives.

The workspace should provide:

- list and table views;
- keyboard traversal;
- screen-reader relationship summaries;
- noncolor certainty and visibility indicators;
- scalable text;
- touch-safe interactions;
- focus-preserving drawers and inspectors.

## 50.32 AI assistance

AI may:

- summarize visible clues;
- identify contradictions in visible evidence;
- organize a player evidence board;
- suggest interview questions;
- summarize visible relationships;
- draft NPC dialogue;
- propose noncanonical social approaches.

AI must not:

- reveal hidden truth;
- declare a theory correct;
- change reputation;
- create obligations;
- approve social outcomes;
- alter campaign state.

## 50.33 Acceptance criteria

The Investigation and Social stage is complete when:

- players can collect and organize visible clues;
- private hypotheses remain noncanonical;
- the GM can prepare and reveal hidden information safely;
- nonlinear progress persists;
- social relationships and faction standing are inspectable;
- promises, favors, and debts persist;
- actions use the approval loop;
- consequences change campaign state;
- hidden information does not leak;
- desktop and mobile workflows remain usable.

## 50.34 Controlling references

- Stage A A9 Investigation and Social Workspaces
- investigation and social game-system architecture
- clue, evidence, relationship, faction, reputation, objective, and event architectures
- authoritative-session and permission contracts
- owner-approved relationship-tracker direction

**Status:** Owner-approved planned experience. Full repository implementation remains to be verified and completed.

---

# 51. World Builder and Content Studio

## 51.1 Purpose

Define the governed authoring environment for creating, cloning, varying, relating, validating, previewing, submitting, packaging, and maintaining worlds, regions, locations, factions, cultures, items, creatures, adventures, and other canonical or campaign-local content.

## 51.2 One authoring architecture

The World Builder and Content Studio should use the same:

- canonical object schemas;
- stable IDs;
- capability modules;
- relationship contracts;
- provenance model;
- validators;
- pack ownership rules;
- runtime previews.

Creators must not author in a simplified format that later requires uncontrolled manual reinterpretation.

## 51.3 Creator workspace

The Content Creator workspace may include:

- drafts;
- assigned reviews;
- source intake;
- object browser;
- world projects;
- content projects;
- validation queue;
- conflict queue;
- submissions;
- pack assembly;
- release status;
- recent work.

## 51.4 Authority indication

Every content project should clearly show:

- author;
- owner;
- project scope;
- canon target;
- campaign-local or shared status;
- proposal-only status;
- required reviewers;
- release authority.

Proposal-only contributors may create drafts and submissions but may not promote canonical content.

## 51.5 New content flow

A new content flow should ask:

1. What domain is this?
2. Is it new, a variant, an extension, or campaign-local?
3. Does a similar canonical object already exist?
4. Which pack should own it?
5. Which schema applies?
6. What is the source or design authority?
7. Which dependencies are required?
8. Which validation and review gates apply?

## 51.6 Domain selection

The creator should select from governed object families and types.

The interface should explain:

- purpose;
- required fields;
- examples;
- extension options;
- related content;
- owner-pack expectations.

## 51.7 Duplicate prevention

Before creating a new object, the Studio should search:

- exact names;
- aliases;
- source coordinates;
- semantic similarity;
- same owner pack;
- variants;
- deprecated or superseded records.

Possible matches should be reviewed as:

- duplicate;
- alias;
- variant;
- extension;
- replacement;
- distinct object.

## 51.8 Templates and forms

Forms should derive from canonical schemas and Design Studio definitions.

They should support:

- required fields;
- conditional fields;
- repeatable groups;
- stable references;
- capability modules;
- inline help;
- source and provenance;
- validation;
- extension fields.

## 51.9 World Builder hierarchy

The World Builder should support:

- Branches;
- cosmological layers;
- Reality Clusters;
- Realities;
- Worlds;
- Setting Nodes;
- Regions;
- Settlements;
- Locations;
- Environments;
- travel networks;
- access profiles;
- timelines;
- relationships.

The UI must not force every setting into a planet-region-city hierarchy.

## 51.10 World project overview

A world project should show:

- scope;
- support level;
- capability badges;
- readiness tracks;
- packs;
- dependencies;
- locations;
- factions;
- cultures;
- religions;
- history;
- timelines;
- creatures;
- items;
- adventures;
- unresolved source gaps;
- validation.

## 51.11 Graph and hierarchy views

The World Builder may provide:

- hierarchy tree;
- relationship graph;
- map;
- timeline;
- list;
- matrix.

Each is a projection over governed records.

The creator should be able to switch views without losing unsaved work.

## 51.12 Region, settlement, and location editor

The editor should support:

- identity;
- parent and peer relationships;
- environment;
- maps;
- inhabitants;
- factions;
- resources;
- travel;
- lore;
- encounters;
- adventure links;
- source and provenance;
- visibility.

## 51.13 Faction and culture editor

The creator should define reusable:

- factions;
- organizations;
- governments;
- cultures;
- religions;
- relationships;
- offices;
- lore;
- history.

The editor must separate Definitions from live membership, rank, reputation, belief, and control.

## 51.14 Timeline editor

The timeline editor should support:

- eras;
- events;
- branches;
- uncertain dates;
- multiple date systems;
- conflicting accounts;
- public and hidden history;
- campaign divergence previews.

## 51.15 Adventure authoring

The Studio should support:

- adventure definition;
- campaign template;
- acts;
- hooks;
- routes;
- quests;
- objectives;
- milestones;
- scenes;
- choice points;
- clues;
- GM truths;
- cast placements;
- encounter bindings;
- scaling;
- rewards;
- consequences.

## 51.16 Scene authoring

Scene authoring in the Content Studio should use the same scene structures as the Campaign and Scene Builder.

The difference is authority and ownership:

- Studio content may become reusable pack content;
- Campaign Builder content remains campaign-local unless submitted and approved.

## 51.17 Object cloning

Cloning should create new identity and preserve source relationship.

The creator should choose whether the clone is:

- variant;
- extension;
- replacement candidate;
- independent object;
- campaign-local derivative.

## 51.18 Variant authoring

A variant editor should show:

- base object;
- inherited fields;
- changed fields;
- grants;
- removals;
- replacements;
- compatibility;
- provenance.

It should prevent accidental full duplication.

## 51.19 Extension authoring

An extension editor should show:

- namespace;
- target;
- schema;
- fields or capabilities;
- activation conditions;
- compatibility;
- owner pack;
- migration;
- validation.

## 51.20 Relationship authoring

A relationship editor should support:

- source;
- target;
- relationship type;
- directionality;
- scope;
- visibility;
- conditions;
- provenance;
- validity.

## 51.21 Mechanics editor

Mechanics authoring should use shared:

- Actions;
- Effects;
- Conditions;
- Resources;
- modifiers;
- rules profiles;
- grants;
- progression;
- compatibility.

The editor should warn when prose appears to contain unstructured executable mechanics.

## 51.22 Source intake

Source intake should support:

- file registration;
- hash;
- source authority;
- source coordinates;
- extraction;
- candidate creation;
- raw value preservation;
- conflict handling;
- missing-information tracking.

## 51.23 Provenance view

The provenance view should show:

- source file;
- coordinate;
- raw claim;
- normalized candidate;
- mapping;
- canonical record;
- transformations;
- reviewer;
- release;
- validation.

## 51.24 Conflict workspace

A conflict workspace should compare:

- claims;
- sources;
- authority;
- fields;
- candidate mappings;
- variants;
- proposed resolutions;
- owner decision status.

No source claim should disappear from the comparison.

## 51.25 Completeness workspace

Completeness should show:

- required fields;
- conditionally required fields;
- recommendations;
- missing source information;
- unresolved mechanics;
- missing dependencies;
- blocker status.

## 51.26 Validation

Validation should run:

- inline;
- on save;
- on submission;
- during pack assembly;
- in CI.

The Studio should distinguish local draft warnings from release-blocking failures.

## 51.27 Runtime preview

A creator should preview content as:

- object inspector;
- character option;
- creature stat block;
- item card;
- scene placement;
- player view;
- GM view;
- mobile view;
- pack installation.

Preview uses the actual schemas and projection rules.

## 51.28 Reference picker

All cross-object references should use the universal object picker.

The picker should restrict valid types and show:

- owner pack;
- version;
- compatibility;
- installation state;
- provenance;
- visibility.

## 51.29 Pack assignment

The creator should assign or confirm:

- owner pack;
- required dependencies;
- optional dependencies;
- extension relationships;
- localization;
- media;
- release status.

The Studio should reject duplicate ownership.

## 51.30 Pack assembly

Pack assembly should produce:

- manifest;
- indexes;
- records;
- source and provenance metadata;
- media and localization indexes;
- dependencies;
- migrations;
- checksums;
- validation report;
- release notes.

## 51.31 Submission

A submission should include:

- content;
- author;
- owner pack;
- design brief;
- source;
- validation;
- conflicts;
- migration;
- dependencies;
- review request;
- target status.

## 51.32 Review

Review may include:

- source fidelity;
- mechanics;
- lore;
- schema;
- provenance;
- dependencies;
- balance observations;
- accessibility;
- media rights;
- localization;
- release.

## 51.33 Approval and promotion

Only authorized reviewers or the owner may promote content.

Promotion should:

- preserve draft history;
- record approval;
- assign release;
- update pack indexes;
- run final validation;
- create receipt.

## 51.34 Rejection and revision

A rejected submission should preserve:

- content;
- reviewer findings;
- reason;
- requested revisions;
- resubmission path.

Rejection must not delete the draft.

## 51.35 Campaign-local promotion

Promoting campaign-local content should:

- preserve campaign-local identity;
- create explicit mapping;
- remove campaign-specific secrets or state;
- confirm pack ownership;
- resolve dependencies;
- validate reusable behavior;
- require approval.

## 51.36 Version comparison

The Studio should compare:

- fields;
- relationships;
- mechanics;
- source;
- provenance;
- dependencies;
- media;
- localization;
- validation;
- runtime projection.

## 51.37 Deprecation

A deprecation workflow should require:

- reason;
- replacement;
- migration;
- affected dependencies;
- release notes;
- owner or delegated authority.

## 51.38 Collaboration

Future collaboration may support:

- comments;
- assignments;
- presence;
- review threads;
- change proposals;
- branch-like drafts.

The authoritative accepted version remains explicit.

## 51.39 AI assistance

AI may:

- classify source;
- propose mappings;
- draft descriptions;
- identify duplicates;
- suggest relationships;
- validate omissions;
- generate noncanonical variants;
- prepare review packets;
- explain errors.

AI must not:

- approve its own work;
- promote canon;
- invent source facts;
- assign official stable IDs outside the governed process;
- select rights or licenses without evidence.

## 51.40 Acceptance criteria

The World Builder and Content Studio stage is complete when a permitted creator can:

- create or import a governed object;
- find and avoid duplicates;
- assign stable identity;
- attach source and provenance;
- create relationships;
- use shared mechanics;
- validate;
- preview;
- submit;
- receive review;
- assemble a `.pack`;
- preserve proposal-only authority;
- prevent unauthorized canonical promotion.

## 51.41 Controlling references

- Stage A A10 World Builder and Content Creation
- canonical object and Design Studio architecture
- content production standards
- world, setting, adventure, faction, media, localization, pack, provenance, and validation architecture
- contributor authority registry
- source recovery and CSV-first conversion programs

**Status:** Owner-approved planned experience. Full repository implementation remains to be verified and completed.

---

# 52. Rules Browser, Search, and Contextual Help

## 52.1 Purpose

Define the universal discovery and explanation experience for rules, objects, sources, relationships, provenance, variants, versions, and contextual assistance.

## 52.2 Discovery principle

Users should be able to find and understand governed content without knowing:

- file paths;
- schema names;
- stable-ID syntax;
- pack internals;
- repository structure.

The application should preserve those details for inspection without making them prerequisites for ordinary use.

## 52.3 Universal search entry

Search should be available from:

- global shell;
- object pickers;
- character builder;
- scene builder;
- live session;
- Content Studio;
- Rules Browser;
- contextual help.

Each entry may apply context filters but should use the same permission-aware search foundation.

## 52.4 Search scope

Search may cover:

- rules;
- actions;
- abilities;
- conditions;
- resources;
- species;
- items;
- creatures;
- NPCs;
- vehicles;
- worlds;
- locations;
- factions;
- lore;
- adventures;
- scenes;
- media;
- campaign instances;
- notes when authorized.

## 52.5 Search filters

Useful filters include:

- object type;
- domain;
- pack;
- setting;
- campaign;
- source;
- canon status;
- installed state;
- entitlement;
- version;
- locale;
- capability;
- relationship;
- validation;
- visibility;
- ownership.

## 52.6 Search result card

A result should show, as permitted:

- display name;
- object type;
- short summary;
- owner pack;
- source or provenance indicator;
- version;
- availability;
- validation or conflict warning;
- relationship context;
- match reason.

## 52.7 Match explanation

Search should be able to indicate whether the match came from:

- exact ID;
- exact name;
- alias;
- title;
- body text;
- relationship;
- capability;
- source;
- semantic similarity.

Semantic similarity must not be presented as canonical equivalence.

## 52.8 Permission safety

Search must not leak protected content through:

- result count;
- suggestion;
- autocomplete;
- snippets;
- thumbnails;
- sort order;
- filters;
- no-result text;
- stable IDs;
- relationship counts.

## 52.9 Entitlement behavior

Search should distinguish permitted user-facing states:

- accessible;
- accessible through campaign grant;
- installed but unavailable;
- available but not installed;
- unavailable.

Protected details may be withheld while still offering lawful acquisition or campaign-request paths.

## 52.10 Rules Browser structure

The Rules Browser should support:

- browse by domain;
- browse by object type;
- search;
- recently viewed;
- favorites or collections;
- relationship traversal;
- source and provenance;
- versions;
- examples;
- contextual application.

## 52.11 Rule article view

A rule article should show:

- name;
- stable identity;
- summary;
- rule text;
- timing;
- prerequisites;
- costs;
- targets;
- resolution;
- outcomes;
- duration;
- stacking;
- failure;
- source;
- owner pack;
- version;
- related rules;
- examples;
- active overrides.

Not every rule uses every section.

## 52.12 Applied rule view

In context, the user should see the applied form of a rule:

- base rule;
- character grants;
- item or ability source;
- campaign house rule;
- scene environment;
- active condition;
- current modifiers;
- final applicable behavior.

## 52.13 Source view

Authorized users may inspect:

- source file;
- source coordinate;
- raw claim;
- normalized record;
- transformation;
- release;
- conflicts.

Source view should not expose files or text outside the user’s rights and role.

## 52.14 Variant comparison

Comparison should show:

- base object;
- variants;
- differing fields;
- source;
- compatibility;
- pack ownership;
- status;
- current campaign selection.

## 52.15 Version comparison

Version comparison should distinguish:

- presentation change;
- rules change;
- source correction;
- migration;
- deprecation;
- replacement;
- current installed version;
- campaign-pinned version.

## 52.16 Relationship traversal

Users should navigate related:

- abilities;
- actions;
- effects;
- conditions;
- items;
- creatures;
- environments;
- factions;
- worlds;
- adventures;
- sources;
- dependencies.

The interface should distinguish relationship type and direction.

## 52.17 Contextual help

Contextual help should appear near the task without permanently occupying the workspace.

It may include:

- field explanation;
- current rule;
- example;
- validation guidance;
- keyboard shortcut;
- source link;
- role-specific help;
- recovery guidance.

## 52.18 Progressive disclosure

Help should use layers:

1. concise label or hint;
2. short explanation;
3. full rule or procedure;
4. source and provenance;
5. advanced implementation or schema detail.

This keeps ordinary workflows readable while preserving depth.

## 52.19 In-app glossary

The glossary should define canonical terms.

Glossary entries may link to:

- rules;
- object types;
- UI concepts;
- governance distinctions;
- examples.

Localized glossary terms should map to the same stable concept.

## 52.20 Error help

Validation and operation errors should link to:

- affected rule;
- likely cause;
- allowed repair;
- current state;
- recovery.

Help must not suggest bypassing authority or validation.

## 52.21 Onboarding

Onboarding should be role-specific.

Player onboarding may cover:

- campaign and character selection;
- live session;
- action proposal;
- inventory;
- notes.

GM onboarding may cover:

- campaign creation;
- scene building;
- approval;
- hidden information;
- recovery.

Creator onboarding may cover:

- object types;
- provenance;
- validation;
- submission;
- pack assembly.

## 52.22 Tutorials

Tutorials should use real or governed sample data and should clearly identify:

- sandbox or tutorial state;
- actions that do not affect live campaigns;
- sample objects;
- completion.

## 52.23 Help versioning

Help content should identify the application and rules versions it applies to.

Outdated help should be deprecated or updated when workflows change.

## 52.24 Localization

Search and help should support:

- localized names;
- aliases;
- translated summaries;
- source-locale fallback;
- locale-aware sorting;
- terminology registry.

Stable IDs and executable rules remain unchanged.

## 52.25 Accessibility

Search and help must support:

- keyboard;
- screen readers;
- focus management;
- scalable text;
- clear heading structure;
- accessible result count;
- noncolor status;
- touch.

## 52.26 Offline use

Permitted installed rules and help may be available offline.

Offline search should clearly identify:

- local index scope;
- last update;
- unavailable online-only content;
- stale content.

## 52.27 AI-assisted explanation

Contextual AI may:

- explain an accessible rule;
- compare accessible options;
- summarize source-grounded mechanics;
- cite the relevant object and source;
- answer within current campaign rules;
- disclose uncertainty.

AI responses should be visibly separate from canonical rule text.

## 52.28 AI retrieval requirements

AI retrieval must enforce:

- identity;
- role;
- campaign;
- entitlement;
- installed content;
- visibility;
- locale;
- provenance;
- context minimization.

## 52.29 AI proposal actions

An AI explanation may offer a permitted next action, such as:

- open rule;
- add accessible item to comparison;
- open character validation;
- create a draft note;
- add a noncanonical scene suggestion.

It must not silently mutate state.

## 52.30 Feedback

Users should be able to report:

- unclear rule;
- missing search result;
- incorrect relationship;
- outdated help;
- accessibility issue;
- suspected source conflict.

Feedback creates a review item, not an automatic canonical correction.

## 52.31 Acceptance criteria

The Rules Browser, Search, and Help stage is complete when users can:

- find a real governed object;
- inspect rules and provenance;
- compare variants and versions;
- traverse relationships;
- use the same picker across workflows;
- receive role-safe contextual help;
- search on desktop and mobile;
- use keyboard and screen reader;
- use AI explanation without hidden-data leakage or unapproved mutation.

## 52.32 Controlling references

- Stage A A2 Universal Object Experience
- Stage A A11 Contextual AI Interfaces
- DB-003 search and indexing architecture
- canonical object, relationship, provenance, localization, permission, and entitlement architecture
- internal-alpha onboarding and help requirements

**Status:** Owner-approved planned experience. Search and indexing foundations are designed; full UI implementation remains to be verified and completed.

---

# 53. Accessibility, Responsive Design, and Themes

## 53.1 Purpose

Define the application-wide requirements for accessible interaction, responsive layouts, touch, keyboard, assistive technology, readable visual design, themes, motion, and owner-approved Multiversal presentation.

## 53.2 Accessibility principle

Accessibility is a release requirement, not a later cosmetic pass.

Every feature should be usable through multiple input and perception modes where practical.

## 53.3 Conformance target

The project should target recognized contemporary web and platform accessibility standards appropriate to its release environments.

The exact formal conformance claim must be based on current audit evidence at release time.

No conformance claim should be made solely from component intent.

## 53.4 Semantic structure

Screens should use meaningful:

- headings;
- landmarks;
- labels;
- lists;
- tables;
- buttons;
- links;
- status regions;
- dialogs.

Interactive nonbutton elements must not imitate buttons without correct semantics and keyboard behavior.

## 53.5 Keyboard access

All functionality should be available by keyboard, including:

- navigation;
- menus;
- dialogs;
- forms;
- tabs;
- trees;
- object pickers;
- maps through alternatives;
- relationship views through alternatives;
- combat targeting;
- inventory movement;
- scene building.

## 53.6 Focus

Focus behavior should be:

- visible;
- predictable;
- trapped only when appropriate;
- restored after dialogs or drawers;
- moved to errors or new urgent content when necessary;
- not reset unexpectedly after realtime updates.

## 53.7 Screen readers

Screen-reader users should receive:

- meaningful names;
- current state;
- role;
- validation;
- result updates;
- proposal status;
- combat turn changes;
- resource changes;
- condition changes;
- connection state;
- error and recovery messages.

## 53.8 Live regions

Realtime announcements should be prioritized.

Urgent announcements may include:

- reaction available;
- action approved or denied;
- turn change;
- disconnected;
- session paused;
- critical validation failure.

Nonurgent updates should not flood assistive technology.

## 53.9 Maps and spatial interfaces

Maps should provide accessible alternatives such as:

- participant list;
- zone list;
- distance or relationship description;
- target list;
- movement destination list;
- objective list;
- hidden-safe scene summary.

A map-only workflow is insufficient.

## 53.10 Graphs and relationship boards

Relationship and evidence graphs should provide:

- list view;
- table view;
- keyboard traversal;
- node and edge summaries;
- filters;
- focus order;
- textual exports.

## 53.11 Color

Color must not be the only way to communicate:

- error;
- warning;
- success;
- side;
- ownership;
- visibility;
- condition;
- selection;
- relationship;
- certainty.

Use text, icon, shape, pattern, or position as additional indicators.

## 53.12 Contrast

Text, controls, focus indicators, charts, maps, and status badges should meet the project’s chosen accessibility contrast targets.

Decorative glow, transparency, texture, and gradients must not reduce legibility.

## 53.13 Typography

The application should support:

- scalable text;
- readable line height;
- comfortable line length;
- clear hierarchy;
- font fallback;
- script coverage;
- user zoom;
- no loss of function at enlarged sizes.

## 53.14 Touch targets

Touch targets should be large enough for reliable activation.

Dense desktop controls should adapt on touch devices rather than retaining small hit areas.

## 53.15 Pointer alternatives

Hover-dependent information must also be available through:

- focus;
- tap;
- explicit inspector;
- label.

Drag and drop must have non-drag alternatives.

## 53.16 Motion

Motion should:

- clarify change;
- avoid unnecessary distraction;
- respect reduced-motion preferences;
- avoid flashing;
- not delay action results excessively;
- preserve spatial understanding.

## 53.17 Timing

Timed interactions should exist only when rules or session policy require them.

Users should receive:

- warning;
- remaining time;
- extension or pause where policy permits;
- accessible announcement.

## 53.18 Forms

Accessible forms should include:

- persistent labels;
- descriptions;
- required indication;
- error summary;
- inline error;
- field association;
- keyboard order;
- touch-safe controls;
- preserved values after failure.

## 53.19 Error recovery

Errors should explain:

- what happened;
- what was affected;
- whether data changed;
- how to retry;
- how to recover.

## 53.20 Cognitive accessibility

The interface should reduce unnecessary cognitive load through:

- consistent navigation;
- plain labels;
- progressive disclosure;
- clear current context;
- confirmation of consequences;
- undo or recovery;
- limited simultaneous choices;
- saved drafts;
- predictable component behavior.

## 53.21 Content clarity

Rules and help should distinguish:

- required;
- optional;
- warning;
- example;
- GM-only;
- source text;
- AI proposal.

## 53.22 Responsive principle

Responsive design means adapting information architecture and interaction, not merely shrinking dimensions.

The project should support:

- desktop;
- tablet;
- mobile;
- portrait;
- landscape;
- touch;
- mouse;
- keyboard.

## 53.23 Breakpoint behavior

Breakpoints should be based on content and interaction needs.

A component should define:

- full layout;
- compressed layout;
- stacked layout;
- drawer or sheet behavior;
- hidden secondary information;
- preserved critical action.

## 53.24 Desktop layouts

Desktop may support:

- persistent navigation;
- multiple panels;
- inspectors;
- split views;
- denser data tables;
- drag and drop.

## 53.25 Mobile layouts

Mobile should prioritize:

- current task;
- current context;
- primary action;
- safe back navigation;
- full-screen inspector;
- drawers and sheets;
- touch targets;
- limited simultaneous panels.

## 53.26 Tablet layouts

Tablet may use:

- split view;
- collapsible navigation;
- slide-over inspector;
- touch-first controls;
- adaptive density.

## 53.27 Live-session responsiveness

On small screens, the live session should prioritize:

1. urgent prompt or reaction;
2. scene and target context;
3. character state;
4. available actions;
5. result;
6. logs and history.

## 53.28 Builder responsiveness

Complex builders should preserve:

- current selected object;
- unsaved work;
- validation;
- inspector access;
- relationship context.

On mobile, advanced authoring may use step-based workflows rather than simultaneous panels.

## 53.29 Theme architecture

Themes should use design tokens.

A theme may define:

- surfaces;
- text;
- accents;
- borders;
- shadows;
- glow;
- illustration treatment;
- domain colors;
- workspace identity;
- motion;
- density.

## 53.30 Owner-approved visual direction

The Multiversal visual direction uses a dark, layered, luminous, high-contrast science-fantasy presentation capable of expressing many genres within one product.

The design should evoke:

- depth;
- portals;
- cosmic layering;
- energy;
- mysterious worlds;
- domain variation.

It should avoid:

- unreadable neon-on-black combinations;
- uncontrolled visual noise;
- excessive glow;
- genre lock to only fantasy or science fiction;
- decorative complexity that obscures controls.

## 53.31 Workspace distinction

Player, GM, Creator, and Owner/Admin workspaces may use distinct accents or iconography.

Workspace themes must not change permission meaning.

## 53.32 Domain accents

Domains such as:

- characters;
- worlds;
- creatures;
- items;
- adventures;
- rules;
- AI;

may use controlled accents.

Domain color must not be the only identifier.

## 53.33 Light and dark modes

The product may support dark, light, and system appearance modes when implemented.

The owner-approved dark direction remains the primary art direction, but accessibility and platform expectations may require alternatives.

All themes must preserve:

- contrast;
- hierarchy;
- focus;
- status meaning;
- map and chart readability.

## 53.34 User customization

Permitted preferences may include:

- appearance mode;
- accent;
- density;
- font scaling;
- motion;
- map contrast;
- panel arrangement.

Customization must not create inaccessible or permission-confusing combinations.

## 53.35 High-contrast mode

A high-contrast mode should reduce decorative effects and strengthen:

- borders;
- focus;
- text contrast;
- status differences;
- selected states.

## 53.36 Reduced transparency

Users may need reduced transparency or blur.

Glass-like or translucent surfaces must have opaque fallbacks.

## 53.37 Localization and layout

Responsive and theme systems must support:

- text expansion;
- right-to-left layout;
- different scripts;
- font fallback;
- locale-specific number and date formats.

## 53.38 Accessibility testing

Testing should include:

- automated checks;
- keyboard-only use;
- screen reader;
- zoom;
- text scaling;
- reduced motion;
- high contrast;
- touch;
- orientation;
- color-vision simulations;
- real user testing where available.

Automated checks alone are insufficient.

## 53.39 Component acceptance

Each reusable component should document:

- semantics;
- keyboard behavior;
- focus behavior;
- touch behavior;
- responsive states;
- disabled state;
- validation;
- permission state;
- theme tokens;
- accessibility notes.

## 53.40 Screen acceptance

Each screen should be tested for:

- loading;
- empty;
- error;
- offline;
- forbidden;
- recovery;
- desktop;
- tablet;
- mobile;
- keyboard;
- screen reader;
- touch;
- permissions;
- localization expansion.

## 53.41 Performance and accessibility

Performance problems can become accessibility barriers.

The application should avoid:

- long blocked interactions;
- focus loss during loading;
- excessive animation;
- unannounced updates;
- huge unvirtualized lists;
- delayed error messages.

## 53.42 Telemetry and privacy

Accessibility and responsive telemetry may record:

- failed routes;
- component errors;
- viewport category;
- input mode;
- recovery usage.

It must not record sensitive content or infer disability status without explicit lawful policy.

## 53.43 AI interfaces

AI interfaces must be:

- clearly labeled;
- keyboard accessible;
- readable by screen readers;
- explicit about proposed versus canonical text;
- reversible;
- permission-aware.

Streaming text should not overwhelm assistive technology.

## 53.44 Acceptance criteria

The accessibility, responsive, and theme stage is complete when:

- all primary workflows function by keyboard and touch;
- screen readers can complete core tasks;
- maps and graphs have alternatives;
- desktop, tablet, and mobile layouts are tested;
- loading, error, offline, forbidden, and recovery states are accessible;
- themes preserve contrast and focus;
- reduced motion and high-contrast needs are supported;
- owner-approved art direction is implemented without sacrificing usability;
- an accessibility audit and defect-remediation cycle are complete.

## 53.45 Controlling references

- Stage A A1 Application Shell and Design System
- Stage A A12 Internal-Alpha Hardening
- owner-approved UI mockups and palette direction
- media and localization architecture
- application shell, Player, GM, builder, combat, inventory, search, and AI interface chapters
- platform accessibility requirements at release time

**Status:** Canonical product requirement and owner-approved visual direction. Formal conformance and production implementation require later audit evidence.

---

# Tranche 5 Integration Review

## T5.1 Coverage

Volume V now consolidates the application experience for:

- shell and navigation;
- Player workspace;
- GM workspace;
- character creation and character sheet;
- campaign, session, and scene building;
- live proposal and approval;
- combat;
- inventory and operational assets;
- investigation;
- social play;
- world building;
- content creation;
- rules browsing;
- search;
- contextual help;
- accessibility;
- responsive behavior;
- themes.

## T5.2 Vertical-slice invariant

Every application capability should be delivered as a vertical slice containing:

1. navigation;
2. screen;
3. real governed data;
4. actions;
5. permissions;
6. persistence;
7. loading, error, offline, forbidden, and recovery states;
8. desktop, tablet, and mobile behavior;
9. tests;
10. reproducible preview;
11. owner review.

## T5.3 Shared component invariant

Domain workflows should reuse:

- object browser;
- object inspector;
- object picker;
- relationship view;
- provenance view;
- validation panel;
- action proposal;
- approval item;
- result view;
- history;
- permission state;
- recovery state.

## T5.4 Definition and state invariant

The application must distinguish:

- reusable canonical Definition;
- placement;
- live instance;
- event;
- snapshot;
- user overlay;
- runtime projection.

UI convenience must not collapse these layers.

## T5.5 Permission invariant

Permission safety applies to:

- navigation;
- routes;
- search;
- object pickers;
- maps;
- graphs;
- approvals;
- notifications;
- AI context;
- exports;
- caches;
- error messages.

## T5.6 Player experience invariant

The Player view prioritizes:

- current scene;
- current character;
- available actions;
- targets;
- costs;
- results.

Logs and My Proposals remain accessible but secondary.

## T5.7 GM authority invariant

The GM may:

- inspect;
- approve;
- deny;
- modify;
- adjudicate;
- manage hidden information;
- create campaign-local content.

The system preserves the original calculation and records the final accepted result.

## T5.8 Creator authority invariant

Creators use the same governed structures as runtime.

Proposal-only contributors may draft and submit but may not promote canonical content.

## T5.9 Accessibility invariant

A feature is not complete when it works only:

- with a mouse;
- on desktop;
- through color;
- through a visual map or graph;
- with motion enabled;
- in one locale.

## T5.10 Recovery invariant

Every major workflow should preserve:

- draft state;
- last confirmed authoritative state;
- pending operations;
- event history;
- snapshots;
- reconnect or retry path;
- user-understandable recovery.

## T5.11 Current implementation boundary

The Stage A UI program is owner approved and planned.

The application repository must still be audited and each stage verified against:

- actual routes;
- actual components;
- real services;
- real data;
- tests;
- previews;
- merges.

This Bible does not claim that the full UI described in Volume V currently exists.

## T5.12 Delivery order

The approved implementation order remains:

1. A0 baseline audit.
2. A1 shell and design system.
3. A2 universal object experience.
4. A3 identity, dashboard, and permissions.
5. A4 character workspace.
6. A5 campaign and scene workspace.
7. A6 first playable action and approval loop.
8. A7 full combat.
9. A8 inventory, crafting, and vehicles.
10. A9 investigation and social.
11. A10 world and content tools.
12. A11 contextual AI.
13. A12 internal-alpha hardening.

## T5.13 Tranche status

Volume V is complete at the application-design level.

Implementation remains governed by Stage A, Phase 9 service readiness, repository evidence, acceptance tests, and owner review.

**Tranche 5 status:** Complete — canonical application design consolidated.


# Volume VI — Technical Architecture

# 54. System Context and Technology Direction

## 54.1 Purpose

Define the technical boundary of the Multiversal application, the major systems and actors that interact with it, the architecture principles that guide implementation, and the distinction between approved direction and verified repository implementation.

## 54.2 System purpose

The Multiversal application provides governed tools and services for:

- players;
- Game Masters;
- content creators;
- the owner and authorized administrators;
- AI contributors;
- local and online sessions;
- canonical content;
- campaign state;
- pack installation and migration;
- search and contextual assistance;
- backup, restore, and provider exit.

The application supports the tabletop experience. It does not become the independent owner of the rules, worlds, characters, or campaign decisions.

## 54.3 Primary actors

### Player

Uses characters, participates in campaigns and sessions, proposes actions, manages permitted assets, reviews visible rules, and creates private or shared notes.

### Game Master

Creates and manages campaigns, prepares scenes, controls hidden information, adjudicates actions, manages NPCs and environments, and preserves campaign continuity.

### Content Creator

Creates, validates, reviews, packages, and submits governed content.

### Owner or Administrator

Controls project authority, release gates, production credentials, provider commitments, canonical promotion, and high-impact administrative operations.

### AI contributor or assistant

Performs bounded assistance through explicit tools, permissions, provenance, and approval gates.

### External identity provider

May authenticate users through a provider-specific adapter while Multiversal retains internal stable subject identity.

### Storage, database, realtime, search, or media provider

May supply replaceable infrastructure behind provider-neutral ports.

### Repository and CI systems

Provide source control, governance evidence, validation, build, and release automation.

## 54.4 System boundary

Inside the Multiversal system boundary are:

- application shell and workspaces;
- domain services;
- provider-neutral service contracts;
- rules execution;
- authoritative-session coordination;
- content registry;
- pack lifecycle;
- campaign and character state;
- event and snapshot management;
- permissions and entitlement decisions;
- search and indexing contracts;
- backup, restore, and export orchestration;
- audit and observability contracts.

Outside the boundary are replaceable providers and external systems such as:

- hosted identity;
- relational database;
- realtime transport;
- object storage;
- search service;
- AI provider;
- email or notification delivery;
- deployment host;
- repository host.

Provider-specific implementations may exist inside adapter modules, but their APIs must not become the permanent domain contract.

## 54.5 Architecture principles

The technical architecture follows these permanent principles:

- provider neutrality;
- canonical data before UI convenience;
- stable identity;
- explicit permissions;
- authoritative accepted state;
- deterministic validation;
- event and receipt evidence;
- reversible migrations;
- exportability;
- secure-by-default behavior;
- bounded cost;
- local or offline capability where practical;
- observability without secret leakage;
- testable vertical slices.

## 54.6 Modular monolith direction

The preferred early architecture is a modular monolith with explicit internal boundaries rather than premature distributed microservices.

A modular monolith should provide:

- one deployable application or a small bounded set of deployables;
- domain modules;
- provider-neutral ports;
- clear data ownership;
- testable service contracts;
- internal event boundaries;
- ability to extract services later when justified.

This direction reduces operational complexity while preserving long-term modularity.

## 54.7 Reasons to avoid premature microservices

Premature service distribution would add:

- deployment complexity;
- network failure modes;
- distributed transaction problems;
- observability cost;
- credential management;
- version coordination;
- provider expense;
- development overhead.

A service should be extracted only when there is evidence of a meaningful need such as:

- independent scaling;
- security isolation;
- operational ownership;
- provider-specific deployment;
- failure isolation;
- release cadence;
- performance boundary.

## 54.8 Client architecture

The visible application may use a web-first client capable of desktop, tablet, and mobile responsive behavior.

The client should contain:

- presentation;
- local interaction state;
- permitted cache;
- optimistic or preview behavior where safe;
- offline queue where governed;
- provider-neutral API client;
- accessibility behavior.

The client must not contain authoritative hidden rules or permissions that the server does not enforce.

## 54.9 Server architecture

The server or trusted application layer should contain:

- authentication mapping;
- authorization;
- entitlement decisions;
- canonical registry access;
- campaign and character services;
- rules validation and resolution;
- authoritative-session state;
- persistence orchestration;
- pack lifecycle;
- audit;
- backup, restore, and export orchestration.

## 54.10 Domain modules

Representative domain modules include:

- identity;
- authorization;
- entitlement;
- content registry;
- pack lifecycle;
- character;
- campaign;
- scene;
- rules;
- action and effect runtime;
- inventory and ownership;
- relationships;
- investigation;
- social play;
- environment and travel;
- operational assets;
- search;
- media;
- localization;
- AI assistance;
- backup and recovery.

Modules should communicate through explicit contracts rather than reaching into each other’s internal storage arbitrarily.

## 54.11 Data architecture direction

The approved architecture class is Postgres-centered but provider-neutral.

A relational database is suitable because Multiversal requires:

- stable identity;
- referential integrity;
- transactions;
- structured content;
- campaign state;
- ownership;
- permissions;
- events;
- migrations;
- reporting.

This direction does not authorize a specific hosted provider or production deployment.

## 54.12 Event and state direction

Multiversal uses a hybrid state model:

- reusable canonical Definitions;
- durable current projections;
- immutable accepted events where history matters;
- snapshots for recovery and performance;
- derived indexes and caches.

The project does not require every database field to be reconstructed exclusively from events.

It does require important accepted changes to remain attributable and recoverable.

## 54.13 Realtime direction

Realtime transport is replaceable.

The authoritative session contract governs:

- connection;
- role-filtered projections;
- proposal flow;
- validation;
- approval;
- accepted events;
- acknowledgements;
- reconnect;
- recovery.

WebSocket, hosted realtime, polling, or another transport may implement the contract.

## 54.14 Search direction

Search is a derived provider-neutral capability.

A relational full-text index may be sufficient initially.

A dedicated search or semantic provider may be added only when justified by:

- corpus scale;
- latency;
- ranking requirements;
- multilingual needs;
- semantic retrieval;
- operational evidence.

## 54.15 Media direction

Media storage uses stable asset identity and replaceable storage references.

The application should support:

- local development storage;
- object-storage adapters;
- content hashes;
- derivatives;
- rights metadata;
- provider-exit export.

## 54.16 AI direction

AI features should use provider-neutral model or agent interfaces where practical.

AI integration must preserve:

- explicit user intent;
- permissions;
- source references;
- proposed status;
- reversibility;
- cost controls;
- provider substitution;
- safe failure.

No single AI provider may become the only representation of project knowledge.

## 54.17 Deployment environments

The architecture should distinguish:

- local development;
- automated test;
- preview;
- internal integration;
- internal alpha;
- staging where later approved;
- production where later approved.

Environment separation should include:

- data;
- credentials;
- configuration;
- logging;
- feature availability;
- release authority.

## 54.18 Configuration

Configuration should be:

- explicit;
- environment-aware;
- validated at startup;
- separated from secrets;
- portable;
- testable.

Invalid required configuration should fail clearly rather than silently selecting unsafe defaults.

## 54.19 Feature flags

Feature flags may support:

- staged development;
- internal testing;
- provider adapters;
- experimental UI;
- safe rollback.

Flags must not permanently replace:

- release governance;
- permissions;
- entitlement;
- migration.

## 54.20 API principles

Application APIs should be:

- version-aware;
- permission-enforced;
- idempotent for mutations where practical;
- explicit about errors;
- stable-ID based;
- pagination-aware;
- provider-neutral;
- observable;
- testable.

## 54.21 Error model

Technical errors should distinguish:

- validation;
- authentication;
- authorization;
- entitlement;
- missing dependency;
- conflict;
- stale state;
- provider unavailable;
- migration required;
- rate or cost limit;
- internal failure;
- recovery required.

User-facing text may be simplified, but machine error codes should remain stable.

## 54.22 Background work

Background work may be used for:

- indexing;
- pack validation;
- media derivatives;
- exports;
- backups;
- large migrations;
- report generation.

A background operation should have:

- operation ID;
- state;
- progress where meaningful;
- actor;
- input fingerprint;
- result;
- failure;
- retry policy;
- receipt.

## 54.23 Scheduling

Scheduled work may support:

- maintenance;
- backups;
- cleanup;
- index reconciliation;
- expiration;
- notifications.

No scheduled task should silently perform owner-only actions such as public release or destructive production migration.

## 54.24 Cost direction

The technical program should minimize recurring cost before usage requires scaling.

Cost controls should include:

- local development;
- free or low-cost development tiers where lawful and sufficient;
- bounded AI calls;
- cache and indexing efficiency;
- resource limits;
- observability;
- provider substitution.

No paid service is authorized merely because it is named as a possible adapter.

## 54.25 Performance direction

Performance work should prioritize:

- shell and current context;
- content search;
- character loading;
- scene activation;
- action proposal latency;
- GM approval latency;
- reconnect;
- large-corpus browsing;
- pack lifecycle.

Performance requirements should be measured in realistic vertical slices.

## 54.26 Reliability direction

Reliability should include:

- transactional mutations;
- idempotency;
- retry-safe operations;
- health checks;
- backups;
- restore testing;
- event and snapshot integrity;
- provider degradation;
- reconnect;
- explicit recovery states.

## 54.27 Security direction

Security should be applied across:

- identity;
- authorization;
- secrets;
- input validation;
- pack ingestion;
- uploads;
- logging;
- exports;
- AI context;
- provider adapters;
- CI.

Security design is expanded in Chapter 61.

## 54.28 Repository architecture

The application repository and governance repository have different responsibilities.

### `Multiversal-app`

Contains active application implementation, contracts, adapters, tests, and workflows.

### `multiversal-aioc`

Contains governance, roadmaps, canonical programs, Development Brain, current-state records, and AI operating instructions.

The application must not depend at runtime on conversational access to the governance repository.

## 54.29 Definition of implemented

A technical capability is implemented only when repository evidence confirms:

- code exists;
- contract is present;
- tests pass;
- CI evidence exists where required;
- work is merged;
- documentation reflects the resulting state.

## 54.30 Current verified boundary

The verified project state records P9-06-001 through P9-06-007 as complete and merged.

The next authorized implementation item is P9-06-008, backup, restore, and provider-exit export ports.

This Bible must not imply that later planned services, UI stages, deployment, or public release are already complete.

## 54.31 Controlling references

- `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
- `governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md`
- P9-04 provider-neutral architecture contract
- P9-05 one-pass technical spike
- P9-06 implementation backlog and acceptance gates
- Stage A UI Implementation Program
- application and AIOC repository evidence

**Status:** Canonical technical direction. Implementation is partial and must be verified by repository evidence.

---

# 55. Provider-Neutral Service Architecture

## 55.1 Purpose

Define the port-and-adapter architecture that prevents Multiversal from becoming dependent on one identity, database, realtime, storage, search, AI, or deployment provider.

## 55.2 Provider-neutral principle

Domain services depend on Multiversal contracts.

Provider adapters depend on provider SDKs.

Domain code must not require provider-specific:

- IDs;
- tokens;
- exceptions;
- query syntax;
- webhook formats;
- realtime channels;
- storage URLs;
- migration metadata.

## 55.3 Ports and adapters

A port defines the capability Multiversal requires.

An adapter implements that capability for a specific provider or local environment.

Representative port families include:

- identity;
- authorization policy;
- entitlement;
- persistence;
- schema migration;
- realtime transport;
- authoritative session;
- backup;
- restore;
- provider-exit export;
- media storage;
- search;
- notification delivery;
- AI completion or agent execution;
- observability.

## 55.4 Contract requirements

Every service port should define:

- purpose;
- operations;
- inputs;
- outputs;
- stable errors;
- idempotency;
- transaction behavior;
- consistency expectations;
- security;
- observability;
- versioning;
- test contract;
- adapter responsibilities;
- unsupported behavior.

## 55.5 Stable internal types

Ports should use internal stable types such as:

- `SubjectId`;
- `CampaignId`;
- `PackId`;
- `ObjectId`;
- `SessionId`;
- `OperationId`;
- `EntitlementDecision`;
- `PersistenceReceipt`;
- `MigrationReceipt`;
- `RealtimeEnvelope`;
- `BackupManifest`.

The exact type names remain implementation-specific, but provider values should not leak into the domain model.

## 55.6 Error normalization

Adapters should translate provider errors into stable internal error classes.

Examples include:

- unavailable;
- timeout;
- authentication failed;
- authorization denied;
- conflict;
- duplicate operation;
- not found;
- unsupported;
- rate limited;
- invalid configuration;
- integrity failure.

The original provider diagnostic may be retained for authorized logs without becoming the public contract.

## 55.7 Adapter configuration

Adapters should receive validated configuration through explicit dependency injection or equivalent composition.

Domain modules must not read arbitrary provider environment variables directly.

## 55.8 Local adapters

Each important port should have a local or test adapter where practical.

Local adapters support:

- development;
- deterministic tests;
- CI;
- offline prototypes;
- provider substitution;
- failure simulation.

A local adapter does not need to reproduce every provider performance characteristic, but it must satisfy the contract.

## 55.9 Contract tests

Every adapter should pass the same contract test suite.

Contract tests should verify:

- inputs and outputs;
- stable errors;
- idempotency;
- version behavior;
- permission boundaries;
- concurrency;
- failure recovery;
- data portability.

Provider-specific tests may add behavior beyond the shared contract.

## 55.10 Capability discovery

An adapter may declare supported optional capabilities.

Examples include:

- transaction isolation;
- realtime presence;
- full-text search;
- object versioning;
- signed URLs;
- bulk export.

Domain code should select only approved capability branches and define fallback behavior.

## 55.11 Provider selection

Provider selection is configuration and deployment policy, not domain logic.

Selecting a provider should consider:

- capability;
- reliability;
- portability;
- cost;
- privacy;
- security;
- legal requirements;
- operational complexity;
- exit path.

## 55.12 Multi-provider operation

The architecture may support different providers by environment or capability.

Examples:

- local identity in development;
- hosted identity in production;
- local filesystem for development assets;
- object storage for hosted environments.

Multi-provider operation must not create incompatible canonical data.

## 55.13 Provider migration

Changing providers should preserve:

- internal stable IDs;
- domain state;
- event history;
- permissions;
- entitlement records;
- pack registry;
- media identity;
- backups;
- audit.

Provider-specific mappings may change.

## 55.14 Identity port

The identity port should support:

- authentication result;
- internal subject resolution;
- provider-link management;
- session validation;
- logout or revocation;
- account recovery integration;
- provider-exit mapping.

Authentication is distinct from authorization.

## 55.15 Entitlement port

The entitlement port should answer whether a subject may access a content capability under:

- plan;
- ownership;
- campaign grant;
- sponsored access;
- role;
- timing;
- content tier.

It should return a structured decision and reason.

## 55.16 Persistence port

The persistence port should support:

- transactional mutation;
- typed repositories or units of work;
- optimistic concurrency;
- idempotency;
- event and snapshot persistence;
- receipts;
- health and readiness.

It should not expose provider query builders throughout domain code.

## 55.17 Migration port

The migration port should support:

- current schema inspection;
- plan;
- apply;
- verify;
- receipt;
- rollback or recovery metadata;
- lock or concurrency protection.

## 55.18 Realtime transport port

The realtime transport port should support:

- connect;
- authenticate;
- subscribe;
- publish;
- acknowledge;
- disconnect;
- presence where approved;
- error and retry behavior.

It transports messages but does not own authoritative game state.

## 55.19 Authoritative-session port

The authoritative-session service should support:

- session creation;
- participant connection;
- role-filtered projection;
- proposal submission;
- validation;
- calculation handoff;
- GM decision;
- accepted event;
- synchronization;
- reconnect;
- pause;
- checkpoint;
- recovery.

## 55.20 Backup port

The backup port should support:

- plan;
- create;
- verify;
- list or locate;
- retention metadata;
- manifest;
- receipt.

The backup contract should be provider-independent.

## 55.21 Restore port

The restore port should support:

- inspect backup;
- compatibility check;
- dry-run plan;
- restore;
- verify;
- recovery receipt;
- failure reporting.

## 55.22 Provider-exit export port

The export port should produce a documented portable package containing, as permitted:

- internal identities;
- content and pack registry;
- campaign and character state;
- events;
- snapshots;
- media metadata;
- permissions;
- entitlements;
- provider mappings;
- checksums;
- schemas;
- manifests;
- migration guidance.

## 55.23 Media storage port

The media port should support:

- write;
- read;
- verify hash;
- metadata;
- visibility-safe access;
- delete or withdraw;
- derivative linkage;
- export.

Canonical media identity must remain separate from storage URL.

## 55.24 Search port

The search port should support:

- index;
- remove;
- query;
- filter;
- permission and entitlement scope;
- locale;
- pagination;
- rebuild;
- health.

Search results must retain stable canonical identity.

## 55.25 AI provider port

An AI provider port may support:

- bounded completion;
- structured output;
- embeddings;
- tool-capable execution;
- usage reporting;
- cancellation;
- error normalization.

The domain layer should preserve prompt purpose, permission context, sources, and proposal status independently of the provider.

## 55.26 Notification port

A notification port may support:

- in-app;
- email;
- push;
- another approved channel.

The domain event determines the notification. The delivery provider does not become the event authority.

## 55.27 Observability port

Observability should permit:

- metrics;
- structured logs;
- traces;
- health;
- audit references.

Adapters must redact secrets and protected content.

## 55.28 Adapter boundaries

Provider adapters may contain:

- SDK initialization;
- provider IDs;
- provider queries;
- provider error parsing;
- provider retry policy;
- provider-specific observability.

They must not contain owner policy, game rules, or canonical content decisions.

## 55.29 Anti-corruption layer

Where a provider model differs substantially from Multiversal, an anti-corruption layer should translate:

- identity;
- data shape;
- lifecycle;
- consistency;
- errors.

The project should not distort its domain model to imitate a provider.

## 55.30 Provider lock-in tests

Architecture review should detect lock-in such as:

- provider ID stored as primary domain ID;
- provider query language in UI or domain service;
- provider event format persisted as canonical event;
- storage URL used as asset identity;
- provider-only migration metadata with no export;
- authentication claims used directly as permanent authorization.

## 55.31 Exit readiness

A provider is acceptable only when there is a documented exit path appropriate to the project phase.

Exit readiness should identify:

- exported data;
- retained identity;
- replacement adapter;
- migration;
- downtime;
- cost;
- verification.

## 55.32 Cost controls

Adapters should expose or report usage where cost matters.

Possible controls include:

- quotas;
- request limits;
- cache;
- batching;
- development adapters;
- disabled expensive features;
- owner approval for paid activation.

## 55.33 Security controls

Adapters should follow least privilege.

Provider credentials should be:

- environment-scoped;
- secret-managed;
- rotated;
- unavailable to clients;
- excluded from logs;
- excluded from source control.

## 55.34 Current verified boundary

The P9-06 implementation program has completed and merged provider-neutral foundations through the authoritative-session service boundary.

Backup, restore, and provider-exit export ports remain the next authorized implementation item.

The existence of ports does not prove that every production adapter is selected or complete.

## 55.35 Controlling references

- P9-04 provider-neutral architecture contract
- P9-05 one-pass Apple and technical spike package
- P9-06 implementation backlog
- merged application repository evidence through P9-06-007
- backup, restore, and provider-exit design packages
- provider-neutral content and pack architecture

**Status:** Canonical architecture; core port foundations are partially implemented, while production adapters and later ports remain incomplete.

---

# 56. Identity and Authorization

## 56.1 Purpose

Define how Multiversal identifies users and service actors, maps external providers to internal identities, establishes sessions, and enforces role-, resource-, campaign-, and action-level authorization.

## 56.2 Authentication and authorization

Authentication answers:

> Who or what is making the request?

Authorization answers:

> Is that subject allowed to perform this operation on this resource in this context?

The two must remain separate.

## 56.3 Internal subject identity

Every authenticated human or service actor should map to an internal stable subject ID.

The internal ID must remain stable across:

- provider changes;
- email changes;
- display-name changes;
- linked identity providers;
- device changes.

## 56.4 Provider identity mapping

A provider mapping should identify:

- internal subject;
- provider;
- provider subject ID;
- environment or tenant;
- verified attributes;
- created time;
- revoked time;
- mapping status.

Provider subject IDs must not become the primary domain identity.

## 56.5 Subject types

Subject types may include:

- human user;
- service account;
- AI service;
- automated worker;
- recovery operator;
- test subject.

Each subject type requires appropriate permissions and audit.

## 56.6 User profile

A user profile may include:

- display name;
- avatar;
- locale;
- accessibility preferences;
- workspace preferences;
- notification settings.

Profile data is separate from authentication credentials.

## 56.7 Account linking

A user may link multiple identity providers when supported.

Linking should require:

- authenticated existing account;
- verified new provider;
- conflict detection;
- audit;
- recovery path.

## 56.8 Account recovery

Recovery should preserve internal identity.

The process must not create a new subject accidentally and orphan:

- characters;
- campaigns;
- ownership;
- entitlements;
- history.

## 56.9 Session identity

An authenticated application session should identify:

- internal subject;
- authentication strength;
- issued time;
- expiry;
- device or client;
- provider mapping;
- revocation state;
- environment.

## 56.10 Reauthentication

High-impact operations may require recent or stronger authentication.

Examples include:

- credential changes;
- provider linking;
- ownership transfer;
- destructive export;
- account deletion;
- production administration.

## 56.11 Roles

Roles describe broad responsibility.

Representative roles include:

- Player;
- Game Master;
- Content Creator;
- Reviewer;
- Owner/Admin;
- service actor.

Roles alone are insufficient for all authorization.

## 56.12 Resource relationships

Authorization may depend on relationships such as:

- campaign member;
- campaign GM;
- character owner;
- delegated controller;
- asset owner;
- asset custodian;
- pack maintainer;
- submission reviewer;
- organization member.

## 56.13 Permission model

A permission decision should evaluate:

- subject;
- action;
- resource;
- campaign or workspace context;
- role;
- ownership or relationship;
- visibility;
- entitlement;
- object state;
- session state;
- policy version.

## 56.14 Service-level enforcement

Permissions must be enforced in trusted services.

UI hiding is useful presentation but not security.

## 56.15 Default deny

When no explicit permission grants access, the system should deny.

This is especially important for:

- GM-only data;
- unrevealed clues;
- private notes;
- owner operations;
- canonical promotion;
- secrets;
- exports.

## 56.16 Campaign roles

Campaign roles may include:

- owner;
- GM;
- assistant GM;
- player;
- observer;
- invited participant;
- suspended participant.

The exact role set remains implementation-controlled.

## 56.17 Character permissions

Character operations may require:

- ownership;
- delegated control;
- campaign membership;
- GM authority;
- current session control;
- advancement permission.

## 56.18 Asset permissions

Asset permissions may depend on:

- ownership;
- custody;
- authorized use;
- station;
- campaign policy;
- current controller.

## 56.19 Content permissions

Content operations may include:

- view;
- use;
- edit draft;
- review;
- submit;
- validate;
- package;
- promote;
- deprecate;
- publish.

Proposal-only contributors must not receive promotion authority.

## 56.20 Owner-only operations

Owner-only gates include, unless explicitly delegated:

- public release;
- production credentials;
- paid-provider activation;
- irreversible provider commitment;
- global canon promotion;
- internal-alpha approval;
- production deployment;
- destructive organization-wide operations.

## 56.21 Visibility

Visibility is a content or state property used during authorization.

Visibility categories may include:

- public;
- authenticated;
- campaign;
- party;
- owner;
- GM;
- participant-specific;
- private;
- hidden until reveal.

## 56.22 Field-level authorization

A subject may access an object but not every field.

Examples include:

- player sees NPC name but not motive;
- player sees condition but not hidden source;
- creator sees validation but not production credential;
- observer sees scene but cannot submit actions.

## 56.23 Query authorization

Authorization must apply to queries and search, not only individual object reads.

A query should not reveal hidden data through:

- counts;
- sorting;
- filters;
- pagination;
- errors;
- existence checks.

## 56.24 Mutation authorization

A mutation should check authorization at execution time.

A previously rendered button or stale token is not sufficient proof.

## 56.25 Authorization receipts

High-impact decisions should retain:

- subject;
- action;
- resource;
- policy version;
- result;
- reason;
- time;
- correlation ID.

## 56.26 Policy versioning

Authorization policies should be versioned.

A policy change may affect:

- active sessions;
- cached permissions;
- offline content;
- exports;
- audit.

## 56.27 Permission caching

Permission decisions may be cached when safe.

Cache keys should include:

- subject;
- resource;
- action;
- campaign;
- role;
- policy version;
- relationship version;
- entitlement version.

## 56.28 Revocation

Permission revocation should take effect promptly for:

- campaign removal;
- role change;
- account suspension;
- provider revocation;
- ownership transfer;
- entitlement expiry.

Offline behavior must define how revocation is enforced on reconnect or expiry.

## 56.29 Service actors

AI and background workers should have narrow service identities.

A service actor should receive only the permissions needed for:

- indexing;
- backup;
- notification;
- validation;
- another bounded task.

## 56.30 Impersonation

Administrative impersonation should be prohibited or tightly controlled.

When permitted for support, it should require:

- owner-approved policy;
- reauthentication;
- clear UI;
- audit;
- time limit;
- no secret exposure beyond necessity.

## 56.31 Invitations

An invitation should identify:

- campaign or resource;
- intended recipient;
- intended role;
- issuer;
- expiry;
- status;
- permitted acceptance.

An invitation token should be single-purpose and time-bounded.

## 56.32 Ownership transfer

Ownership transfer requires:

- current owner authority;
- recipient validation;
- affected resource;
- consequences;
- confirmation;
- event or receipt;
- rollback or dispute policy where appropriate.

## 56.33 Account deletion

Account deletion is distinct from deleting project or campaign history.

The process should determine:

- data that may be deleted;
- data that must be retained;
- transferred ownership;
- anonymization;
- legal obligations;
- export;
- recovery period;
- owner approval where required.

## 56.34 Test strategy

Authorization tests should include:

- allowed case;
- denied case;
- wrong campaign;
- wrong character;
- wrong role;
- stale role;
- revoked access;
- hidden field;
- query inference;
- offline cache;
- service actor;
- owner-only gate.

## 56.35 AI boundary

AI must operate under a subject and permission context.

AI must not:

- infer broader access;
- use GM data for a player response;
- promote content;
- transfer ownership;
- reveal private notes;
- execute owner-only actions.

## 56.36 Current verified boundary

The provider-neutral identity service port is part of the completed P9-06 foundation.

Production provider selection, account-recovery implementation, complete policy coverage, and UI integration remain later work unless separately verified in the application repository.

## 56.37 Controlling references

- identity service port
- contributor registry
- application role and permission architecture
- campaign, character, ownership, visibility, and entitlement contracts
- Stage A identity, dashboard, and workspace requirements
- security and audit requirements

**Status:** Canonical authorization architecture; provider-neutral identity foundations are implemented, while full production integration remains incomplete.

---

# 57. Entitlements and Freemium Policy

## 57.1 Purpose

Define how Multiversal determines access to content and capabilities under free access, paid or sponsored access, campaign grants, ownership, roles, and temporary policies without confusing entitlement with in-world ownership or canon.

## 57.2 Entitlement principle

Entitlement answers:

> May this subject access or use this content or capability under the current policy?

Entitlement does not answer:

- Does the character own the item?
- Is the content canonical?
- Is the pack installed?
- Does the user have permission to edit it?
- Is the user a campaign member?
- Is the action valid in the current scene?

These decisions interact but remain separate.

## 57.3 Entitlement inputs

An entitlement decision may consider:

- subject;
- content or capability;
- plan;
- purchase or grant;
- campaign;
- role;
- sponsored access;
- time;
- content tier;
- pack installation;
- region or legal restriction;
- policy version.

## 57.4 Entitlement result

A structured decision should include:

- allowed or denied;
- reason;
- source of access;
- expiry;
- scope;
- policy version;
- remediation or acquisition path where lawful;
- whether campaign state remains usable;
- whether export remains available.

## 57.5 Free-access philosophy

The free experience should be genuinely usable for:

- joining campaigns;
- creating and using characters within the approved free rules;
- participating in sessions;
- accessing core rules and permitted content;
- preserving owned and campaign state.

Free access must not become a misleading trial that prevents ordinary tabletop participation.

## 57.6 Ability-tree policy

The approved free-access policy limits ability trees to the first two tiers.

This limit applies to:

- direct selections;
- granted abilities;
- abilities received through other content.

The entitlement engine must not allow a higher-tier grant to bypass the policy silently.

## 57.7 Campaign grants

A campaign may grant access to content for campaign use.

A campaign grant should identify:

- campaign;
- subject or role;
- content scope;
- source;
- start;
- expiry;
- revocation;
- offline behavior;
- export behavior.

A campaign grant does not transfer global ownership.

## 57.8 Sponsored access

Sponsored access temporarily provides approved access under a sponsor or campaign policy.

A sponsored period should record:

- sponsor;
- beneficiary;
- scope;
- start;
- end;
- reason;
- policy;
- revocation;
- resulting access.

Sponsored access should expire predictably and must not erase historical state.

## 57.9 Sponsored-month behavior

The approved architecture includes sponsored-month behavior.

The entitlement service must determine access based on the sponsored period without duplicating or mutating canonical content.

When the period ends:

- new restricted selections may become unavailable;
- historical campaign and character references remain preserved;
- export and recovery obligations remain;
- campaign policy may provide continued access where approved;
- the system should explain the result clearly.

## 57.10 Content ownership

A user or account may hold a purchase, license, or permanent grant.

Content ownership should record:

- subject;
- content;
- source;
- scope;
- acquired time;
- revocation or refund where applicable;
- policy version.

The exact commercial model remains separately gated.

## 57.11 Pack installation

A user may be entitled to content that is not installed.

A pack may be installed but inaccessible to a particular user.

The UI should distinguish:

- entitled and installed;
- entitled but not installed;
- installed through campaign grant;
- installed but not entitled;
- unavailable.

## 57.12 Role-based access

Some content access comes from role rather than plan.

Examples may include:

- GM access to campaign-enabled content;
- creator access to owned draft packs;
- reviewer access to submissions;
- owner access to administration.

Role access must not become a permanent consumer license unless policy explicitly says so.

## 57.13 Campaign-enabled content

A GM may enable installed content for a campaign where entitlement and campaign policy permit.

Enabling content does not automatically:

- grant it to every user outside the campaign;
- reveal hidden content;
- create character ownership;
- bypass free-tier selection rules without a valid campaign grant.

## 57.14 Historical state

Entitlement expiry or revocation must not silently delete:

- character history;
- campaign events;
- item instances;
- advancement records;
- adventure state;
- notes;
- receipts.

Historical records may become read-only or restricted according to policy, but identity and recovery must remain intact.

## 57.15 Active use after expiry

Policy should define what happens when restricted content is already active.

Possible governed behaviors include:

- continue within the granting campaign;
- become read-only;
- remain usable until session end;
- require replacement before next advancement;
- disable new activation while preserving history.

The system must not invent the policy at runtime.

## 57.16 Character validation

Character validation should identify entitlement problems such as:

- selected content no longer accessible;
- grant expired;
- campaign changed;
- tier exceeds policy;
- missing pack;
- content withdrawn.

The result should separate entitlement from mechanical invalidity.

## 57.17 Offline entitlement

Offline use should rely on a signed, versioned, or otherwise verifiable entitlement snapshot where required.

Offline entitlement should define:

- expiry;
- scope;
- revocation behavior;
- reconnect validation;
- grace period if approved;
- protected content removal.

## 57.18 Entitlement caching

Caching should include:

- subject;
- content;
- campaign;
- policy version;
- grant version;
- expiry;
- decision reason.

Revocation and expiry must invalidate cached decisions.

## 57.19 Search behavior

Search should not expose restricted content details beyond approved discovery policy.

The UI may show a lawful summary or acquisition path without revealing protected rules text, assets, or hidden campaign content.

## 57.20 AI behavior

AI retrieval must respect entitlement.

AI must not use inaccessible content to:

- answer rules questions;
- build characters;
- suggest equipment;
- generate scenes;
- summarize packs.

AI may explain that access is unavailable without exposing the protected content.

## 57.21 Exports

Users should be able to export their lawful data.

An export may include references to content they do not own, but must follow license and policy.

The export should preserve:

- stable IDs;
- campaign or character state;
- source pack references;
- entitlement metadata;
- unavailable-content markers;
- recovery guidance.

## 57.22 Refunds and revocation

A refund or revocation should update entitlement without deleting campaign history.

The system should distinguish:

- refund;
- fraud or abuse revocation;
- provider failure;
- content withdrawal;
- legal restriction;
- owner administrative correction.

## 57.23 Content withdrawal

A pack may become unavailable because of:

- rights;
- security;
- legal issue;
- canon withdrawal;
- provider outage.

The entitlement system should preserve references and provide policy-specific fallback or migration.

## 57.24 Freemium separation from game balance

Free and paid access policy must not silently redefine mechanical balance.

A paid tier may provide more content choices, but source records and rules remain canonical and versioned.

## 57.25 No pay-to-adjudicate

The GM’s adjudication authority must not depend on paying for a higher plan.

Commercial access may affect content or service limits, but must not sell hidden mechanical advantage through unrecorded outcome control.

## 57.26 Usage limits

Future plans may include usage limits for:

- storage;
- AI;
- campaigns;
- media;
- exports;
- collaboration.

Any limit should be:

- explicit;
- measurable;
- user-visible;
- recoverable;
- non-destructive;
- owner-approved.

## 57.27 Payment boundary

Payment processing, billing provider, taxes, refunds, and commercial terms remain separate technical and legal programs.

This chapter does not authorize:

- charging users;
- creating paid plans;
- selecting a billing provider;
- public sales;
- production commerce credentials.

## 57.28 Policy versioning

Entitlement policy should be versioned.

A decision should identify the policy version used.

Policy migration should consider:

- active grants;
- historical purchases;
- sponsored periods;
- offline snapshots;
- character selections;
- campaign content.

## 57.29 Audit

Entitlement changes should produce evidence for:

- grant;
- purchase;
- sponsorship;
- expiry;
- revocation;
- refund;
- policy migration;
- administrative correction.

## 57.30 Privacy

Entitlement data may reveal:

- purchases;
- campaign membership;
- sponsorship;
- financial relationships.

Access and logging must be restricted.

## 57.31 Testing

Entitlement tests should cover:

- free tier;
- first and second ability tiers;
- higher-tier denial;
- granted higher-tier content;
- campaign grant;
- sponsored month;
- expiry;
- revocation;
- offline state;
- search;
- AI retrieval;
- export;
- historical character state.

## 57.32 Current verified boundary

The entitlement and freemium architecture is approved.

The provider-neutral entitlement service port is part of the completed P9-06 foundation.

Commercial billing, production plans, paid provider enrollment, and public activation remain unauthorized and unimplemented unless later owner-approved repository evidence says otherwise.

## 57.33 Controlling references

- P9-01 entitlement and freemium architecture
- sponsored-month policy
- P9-04 provider-neutral architecture contract
- entitlement service port
- character progression and ability-tier policy
- campaign grant architecture
- application roadmap and owner-only commercial gates

**Status:** Canonical policy architecture with provider-neutral service foundation implemented; commercial execution remains gated.



# 58. Persistence and Migration

## 58.1 Purpose

Define how Multiversal stores canonical content, campaign state, events, snapshots, ownership, permissions, entitlements, pack state, and operational evidence while preserving provider neutrality, transactions, stable identity, deterministic migrations, and recoverability.

## 58.2 Persistence principle

Persistence is the durable representation of accepted state.

The persistence layer must preserve:

- stable internal identity;
- one authoritative accepted state;
- immutable evidence for important changes;
- referential integrity;
- campaign and tenant isolation;
- optimistic or explicit concurrency control;
- provider-independent domain contracts;
- migrations;
- backup and restore compatibility;
- provider-exit exportability.

The application must not treat browser storage, realtime messages, search indexes, or caches as the only copy of authoritative state.

## 58.3 Postgres-centered direction

The approved architecture class is Postgres-centered.

This direction is appropriate because Multiversal requires:

- relational references;
- transactions;
- uniqueness;
- ownership;
- campaign membership;
- authorization;
- content registries;
- session state;
- ordered events;
- migrations;
- reporting;
- backup and restore.

The architecture remains provider-neutral. A hosted Postgres provider may implement the contract, but provider-specific APIs must remain inside adapters.

## 58.4 Logical data areas

The technical contract identifies logical areas including:

- subjects and external identity mappings;
- application sessions and refresh state;
- plans, subscriptions, grants, sponsored periods, and entitlement evaluations;
- campaigns, members, and roles;
- content packs, versions, installations, canonical objects, and relationships;
- game sessions, participants, commands, events, and projections;
- checkpoints and restore attempts;
- audit and security events;
- transactional outbox events;
- schema migrations.

The exact table layout may evolve through governed implementation and migration. Logical responsibilities must remain explicit even when a provider or framework uses different physical structures.

## 58.5 Definition and live-state separation

Reusable canonical Definitions should be stored separately from mutable campaign and session state.

A reusable Definition update must not silently overwrite:

- character selections;
- item instances;
- campaign placements;
- discovered information;
- relationship history;
- objective progress;
- damage;
- ownership;
- timeline divergence.

Migrations and projections connect the layers without collapsing them.

## 58.6 Aggregate ownership

Each authoritative aggregate should have a clear write boundary.

Representative aggregates include:

- subject or account;
- campaign;
- character;
- inventory or owned asset;
- game session;
- adventure state;
- pack installation;
- entitlement grant;
- backup operation.

A service should not update another aggregate’s internal state by directly mutating unrelated tables without the domain contract.

## 58.7 Transactional mutations

A mutation that represents one accepted operation should commit atomically where practical.

Examples include:

- action acceptance and resulting effects;
- ownership transfer;
- inventory move;
- character advancement;
- campaign invitation acceptance;
- pack installation;
- entitlement grant;
- checkpoint creation.

A partial commit must either be prevented or handled through explicit compensation with complete evidence.

## 58.8 Authoritative row metadata

Mutable authoritative records should include, as applicable:

- stable ID;
- scope ID;
- version;
- created time;
- updated time;
- creating actor;
- updating actor;
- lifecycle status;
- schema version;
- content or state fingerprint.

Provider timestamps do not replace domain sequence where deterministic ordering is required.

## 58.9 Scope isolation

Tenant-, campaign-, workspace-, or user-scoped records must carry their scope identity.

Isolation should be enforced through both:

- trusted service authorization; and
- database-level policies or equivalent storage isolation where supported.

Service checks do not justify removing database isolation.

## 58.10 Optimistic concurrency

Mutations should include an expected version or equivalent concurrency precondition when stale writes could cause loss or duplication.

A conflict response should identify:

- expected version;
- current version;
- affected aggregate;
- whether retry, refresh, merge, or correction is safe.

## 58.11 Idempotency

Mutating operations should support idempotency where retries are expected.

A durable idempotency record may include:

- operation or command ID;
- subject;
- scope;
- input fingerprint;
- status;
- result reference;
- created and expiry times.

The same idempotency key with different input must be rejected.

## 58.12 Event persistence

Important accepted changes should produce immutable events.

An event should preserve:

- event ID;
- aggregate;
- sequence;
- actor;
- authority;
- type;
- input or proposal reference;
- source rules and content versions;
- result;
- visibility;
- correlation and causation;
- timestamp;
- schema version.

Events should be append-only except for tightly governed legal or security procedures that preserve audit evidence.

## 58.13 Current projections

Current projections provide efficient reads.

They may include:

- current character state;
- current campaign dashboard;
- current scene;
- inventory summary;
- relationship graph;
- adventure progress;
- session participant view.

A projection should be reproducible or verifiable from authoritative state, events, snapshots, and versioned rules.

## 58.14 Snapshots

Snapshots accelerate recovery and loading.

A snapshot should include:

- aggregate or session ID;
- event cursor;
- state projection;
- installed pack versions;
- rules version;
- schema versions;
- checksum or digest;
- creation reason;
- created time;
- recovery compatibility.

A snapshot with incompatible or invalid metadata must not be applied silently.

## 58.15 Transactional outbox

Realtime publication and background reactions should use a transactional outbox or equivalent reliability pattern.

The mutation transaction should:

1. validate and authorize;
2. update authoritative state;
3. append events;
4. enqueue outbound messages;
5. commit.

A separate dispatcher may publish messages with retry and deduplication.

## 58.16 Repository interfaces

Domain services should depend on provider-neutral repository or unit-of-work contracts.

Contracts should expose domain operations rather than generic provider query builders throughout the application.

Provider-specific query optimization remains inside adapters.

## 58.17 Query models

Read-heavy interfaces may use specialized query models.

Examples include:

- object browser;
- campaign dashboard;
- participant roster;
- relationship graph;
- investigation timeline;
- pack registry.

Query models remain permission-aware and derived.

## 58.18 Persistence port

The provider-neutral persistence port should define:

- transaction boundary;
- aggregate reads and writes;
- expected-version behavior;
- idempotency;
- event append;
- snapshot storage;
- outbox enqueue;
- stable errors;
- health;
- receipts.

## 58.19 Migration port

The migration port should define:

- inspect current version;
- list or plan pending migrations;
- dry run where possible;
- apply;
- verify;
- produce receipt;
- handle lock or concurrency;
- report rollback or forward-repair path.

## 58.20 Schema versioning

Schema versions should be explicit for:

- database structure;
- canonical objects;
- pack manifests;
- events;
- snapshots;
- exports;
- API payloads.

These versions may evolve independently and require compatibility mappings.

## 58.21 Migration ordering

Migrations should be:

- ordered;
- version controlled;
- repeatable in a clean environment;
- applied once in a target environment;
- deterministic;
- reviewed;
- validated.

Ad hoc manual production edits are not acceptable migration evidence.

## 58.22 Expand–migrate–contract

Breaking changes should normally use:

### Expand

Add compatible new structures without removing old ones.

### Migrate

Backfill or transform data while both structures are supported.

### Contract

Remove old structures only after compatibility and rollback requirements are satisfied.

This pattern reduces client and deployment coupling.

## 58.23 Destructive migration

A destructive migration requires:

- explicit classification;
- verified backup;
- affected-data report;
- owner or release-gate authorization where required;
- tested migration;
- rollback or forward-repair instructions;
- compatibility window;
- final validation.

## 58.24 Backfill

A backfill must identify:

- source fields;
- transformation;
- provenance;
- default behavior;
- records that cannot be safely derived;
- validation;
- restart and idempotency behavior.

Guessed data must not be represented as source-derived truth.

## 58.25 Data reset

Development and test environments should have deterministic reset behavior.

Reset should:

- target only the approved environment;
- refuse production or unknown environments;
- remove intended test state;
- reapply migrations;
- load deterministic fixtures;
- report final fingerprints;
- verify zero unintended residue.

## 58.26 Seed fixtures

Seed fixtures should provide minimal deterministic data for:

- identities;
- campaigns;
- characters;
- content packs;
- entitlements;
- sessions;
- hidden information;
- action proposals;
- checkpoints.

Fixtures must be clearly nonproduction and free of real credentials or private user data.

## 58.27 Pack and object migrations

Pack and canonical-object schemas remain independently migratable from the application database schema.

A pack update may require:

- object transformation;
- stable-ID mapping;
- relationship remapping;
- live-state compatibility;
- event upcasting;
- index rebuild.

## 58.28 Event evolution

Historical events should be preserved.

When event schemas evolve, the application may use:

- versioned readers;
- upcasters;
- compatibility adapters;
- migration only when unavoidable.

Rewriting historical events should not be the default.

## 58.29 Snapshot evolution

A snapshot may be discarded and rebuilt when incompatible if authoritative events and state permit.

If it is required for recovery, migration must preserve:

- event cursor;
- rules and pack versions;
- checksum;
- permission state;
- recovery evidence.

## 58.30 Data retention

Retention policy should distinguish:

- canonical content;
- current state;
- events;
- security events;
- operational telemetry;
- drafts;
- exports;
- backups;
- deleted-account data;
- legal or support evidence.

No production retention period is authorized by this chapter without a later privacy and release decision.

## 58.31 Data deletion

Deletion must distinguish:

- logical archive;
- tombstone;
- withdrawal;
- user-requested deletion;
- campaign removal;
- backup expiry;
- legal deletion.

Deleting an account must not corrupt shared campaign or audit history.

## 58.32 Import

An import should:

- validate manifest;
- validate schema;
- map stable IDs;
- detect conflicts;
- preserve provenance;
- stage changes;
- produce a plan;
- require appropriate authority;
- apply transactionally;
- produce a receipt.

## 58.33 Export compatibility

Persistence must support export without requiring provider-specific database access by end users.

Exports should preserve:

- schema versions;
- stable IDs;
- relationships;
- events;
- snapshots;
- pack registry;
- media references;
- permissions;
- checksums;
- migration history.

## 58.34 Failure behavior

Persistence failures should return stable typed errors such as:

- conflict;
- duplicate operation;
- unavailable;
- integrity failure;
- migration required;
- invalid schema;
- transaction aborted;
- insufficient storage;
- timeout.

The UI should state whether the operation committed.

## 58.35 Observability

Persistence telemetry should measure:

- transaction latency;
- failure rate;
- conflict rate;
- connection saturation;
- query latency;
- migration duration;
- outbox backlog;
- snapshot duration;
- storage growth.

Protected content must not be logged.

## 58.36 Testing

Persistence tests should include:

- transaction success;
- rollback;
- concurrent update;
- duplicate command;
- stale version;
- event append;
- projection update;
- outbox retry;
- migration from supported versions;
- clean install;
- reset;
- import;
- export;
- adapter contract parity.

## 58.37 Current verified boundary

Provider-neutral persistence and migration ports are recorded as complete and merged under P9-06-006.

That completion establishes interfaces, contract tests, and local/provider-neutral foundations. It does not by itself prove that every production schema, provider adapter, migration, or operational drill is complete.

The active roadmap places backup, restore, and provider-exit ports next under P9-06-008.

## 58.38 Controlling references

- P9-04 Postgres-Centered Architecture Contract
- P9-06-006 provider-neutral persistence and migration ports
- canonical object, event, snapshot, pack, and lifecycle architecture
- migration and supersession maps
- deterministic fixtures and reset requirements
- application repository contract tests and CI evidence

**Status:** Canonical persistence architecture; provider-neutral ports are implemented, while later concrete schemas, adapters, and operational rehearsals remain repository-governed.

---

# 59. Realtime and Authoritative Sessions

## 59.1 Purpose

Define the technical services and message contracts that support connected participants, authoritative session commands, ordered events, hidden-information-safe projections, reconnect, checkpoint recovery, and transport substitution.

## 59.2 Authority principle

Committed server state is authoritative.

Realtime delivery is advisory transport.

A message received by a client is not authoritative unless it represents committed accepted state and carries the corresponding authoritative version or event sequence.

## 59.3 Service separation

The architecture separates:

- realtime transport;
- authoritative session command handling;
- persistence;
- projection generation;
- checkpoint management;
- authorization;
- domain rules execution.

A realtime provider must not become the game-state authority.

## 59.4 Realtime transport port

The transport port should support:

- connection;
- authentication binding;
- subscription;
- scoped publication;
- acknowledgement;
- disconnect;
- retry behavior;
- presence where approved;
- adapter health.

It should not decide whether a game command is legal.

## 59.5 Session command port

The session command contract should support:

- command submission;
- authentication;
- authorization;
- expected state version;
- idempotency;
- validation;
- execution;
- accepted events;
- stable errors;
- result receipt.

## 59.6 Session identity

A game session should have stable identity and record:

- campaign;
- scene;
- lifecycle state;
- current authoritative version;
- current event sequence;
- active rules and pack versions;
- participants;
- checkpoint cursor;
- creation and update actors.

## 59.7 Participant identity

A session participant record should identify:

- session;
- internal subject;
- role;
- assigned character or controlled entities;
- permissions;
- connection state;
- last acknowledged event;
- device or client identifier where appropriate;
- joined and left times.

## 59.8 Command envelope

A command should include:

- command ID;
- session ID;
- actor;
- submitting subject;
- expected state version;
- command type;
- payload;
- payload schema version;
- client timestamp;
- idempotency context;
- correlation ID.

## 59.9 Command transaction

Command execution should occur through one authoritative transactional flow:

1. authenticate;
2. authorize;
3. reject duplicate or stale command safely;
4. validate domain preconditions;
5. acquire version or lock protection;
6. calculate deterministic result;
7. append command and events;
8. update authoritative state and projections;
9. enqueue realtime notifications;
10. commit;
11. return authoritative receipt.

## 59.10 Duplicate commands

Commands should be idempotent within their session scope.

A duplicate command with the same input should return the stored result or equivalent status.

A duplicate command ID with different input must be rejected.

## 59.11 Stale commands

A stale command references a version no longer current.

The service should decide deterministically whether to:

- reject;
- revalidate safely;
- return for correction;
- request refresh.

It must not apply a command against hidden newer state without validation.

## 59.12 Event sequence

Events should have monotonic ordering per session or an equivalent deterministic order.

Clients should track the last acknowledged sequence.

Gaps trigger synchronization rather than guessing.

## 59.13 Delivery guarantees

Realtime delivery may be:

- duplicated;
- delayed;
- temporarily unavailable;
- reconnected.

The client and server must tolerate at-least-once-style delivery where applicable.

Exactly-once business effects come from idempotent authoritative command handling, not transport promises.

## 59.14 Transactional publication

Messages should be published from a transactional outbox or equivalent mechanism.

This prevents a committed state change from being lost merely because the realtime provider was temporarily unavailable.

## 59.15 Projection generation

The service should generate role-filtered projections before publication.

A projection may differ for:

- GM;
- acting player;
- party;
- observer;
- disconnected returning client;
- AI assistant.

## 59.16 Hidden information

Hidden data must be excluded before publication.

The system must not send complete GM state to a player client and rely on interface hiding.

Protected data includes, as applicable:

- hidden tokens;
- NPC motives;
- unrevealed clues;
- secret objectives;
- hidden conditions;
- private notes;
- undiscovered locations;
- protected rolls;
- other participants’ private data.

## 59.17 Message envelope

A realtime message should include:

- message ID;
- session;
- event or projection type;
- sequence or version;
- schema version;
- recipient scope;
- correlation;
- payload;
- integrity metadata where required.

## 59.18 Presence

Presence may indicate:

- connected;
- reconnecting;
- idle;
- active device;
- GM availability.

Presence is ephemeral and not authoritative campaign history unless an event explicitly records something material.

## 59.19 Two-device use

The architecture should support at least two distinct connected devices in internal-alpha acceptance.

The test should demonstrate:

- independent authentication;
- correct roles;
- synchronized scene state;
- proposal and approval;
- hidden-information isolation;
- disconnect and reconnect;
- persistence across reload.

## 59.20 Multiple devices for one subject

A subject may connect from multiple devices under policy.

The service should define:

- active control device;
- read-only secondary device;
- control handoff;
- duplicate submission handling;
- revocation;
- reconnect.

## 59.21 Proposal flow

The Player client submits a proposal.

The service:

- verifies control;
- validates state;
- calculates result;
- determines approval requirement;
- creates the GM approval projection;
- preserves proposal status.

The proposal remains pending until the authorized decision.

## 59.22 Approval flow

The GM may:

- approve;
- deny;
- modify;
- return for correction.

The service validates the decision and applies accepted effects through the same persistence boundary.

## 59.23 GM-controlled actions

A GM-controlled action may use a streamlined command, but it should still:

- validate;
- calculate;
- preserve result;
- confirm or modify;
- apply;
- emit events.

## 59.24 Reactions and nested windows

Reactions should use linked commands and correlation.

The authoritative session defines:

- trigger;
- eligible subjects;
- order;
- expiry when governed;
- pass;
- continuation.

## 59.25 Connection loss before submission

An unsent local proposal remains a draft.

The client should not claim that it is pending on the server.

## 59.26 Connection loss after submission

The client should preserve the command ID and ask the authoritative service for status after reconnect.

It must not resubmit with a new command ID automatically.

## 59.27 Connection loss after commit

On reconnect, the committed event should be retrieved from sequence synchronization.

The command must not be reapplied.

## 59.28 Reconnect protocol

Reconnect should:

1. authenticate the subject;
2. resolve session participation;
3. submit last acknowledged sequence and known state version;
4. verify client protocol compatibility;
5. return missed permitted events or a fresh permitted projection;
6. reconcile command statuses;
7. update acknowledgements;
8. resume live state.

## 59.29 Gap recovery

When event gaps are too large or incompatible, the service may return:

- current permitted snapshot or projection;
- checkpoint;
- subsequent events;
- reset instruction for local derived state.

## 59.30 Checkpoint

A checkpoint should preserve:

- session version;
- event sequence;
- rules and pack versions;
- canonical state digest;
- permitted object references;
- reason;
- SHA-256 or equivalent integrity hash;
- creation actor and time.

## 59.31 Restore semantics

Restoring a session should not erase history.

A restore should:

- verify checkpoint;
- validate compatibility;
- create recovery operation;
- apply state through governed persistence;
- append recovery event;
- establish new authoritative version;
- synchronize participants.

## 59.32 Pause

A paused session should define:

- command types accepted;
- pending approvals;
- timer behavior;
- presence;
- checkpoint state;
- resume authority.

## 59.33 End and finalize

Session end should stop ordinary play commands and persist final state.

Finalization may perform:

- unresolved command review;
- objective updates;
- rewards;
- recap;
- checkpoint;
- backup trigger;
- archival transition.

## 59.34 Transport substitution

The same session contract should work over:

- local test transport;
- WebSocket adapter;
- hosted realtime adapter;
- another approved channel.

Transport-specific channel names and provider event formats must not enter canonical event history.

## 59.35 Backpressure

The system should handle slow or disconnected clients without blocking authoritative progress indefinitely.

Backpressure policy may include:

- bounded queues;
- reconnect snapshot;
- message coalescing for derived projections;
- dropping obsolete presence messages;
- preserving authoritative events.

## 59.36 Rate and size limits

The service should limit:

- command size;
- message size;
- command frequency;
- subscriptions;
- malformed retries.

Limits should not prevent legitimate accessibility tools or ordinary live play.

## 59.37 Observability

Realtime and session telemetry should include:

- connected participants;
- command latency;
- validation failure;
- approval latency;
- outbox delay;
- delivery lag;
- reconnect success;
- sequence gaps;
- duplicate commands;
- stale commands;
- checkpoint duration.

## 59.38 Security

Realtime security should include:

- authenticated connection;
- scoped subscriptions;
- authorization on each mutation;
- expiry and revocation;
- message validation;
- origin or client controls where appropriate;
- no privileged secrets in clients;
- hidden-data filtering;
- rate limits.

## 59.39 Contract tests

Shared tests should verify:

- connect and authenticate;
- permitted subscription;
- denied subscription;
- command success;
- duplicate command;
- stale command;
- ordered delivery;
- duplicate delivery;
- hidden filtering;
- disconnect;
- reconnect;
- checkpoint;
- restore;
- transport adapter parity.

## 59.40 Current verified boundary

Provider-neutral realtime and authoritative-session service ports are recorded as complete and merged under P9-06-007, with squash commit `149b866f530f3a8896170bfe3ba6af0c01fb2f72`.

This establishes interfaces, local or contract foundations, and CI evidence. It does not prove that the full production command handler, hosted transport adapter, UI workflow, two-device acceptance suite, or internal-alpha deployment is complete.

## 59.41 Controlling references

- P9-02 Authoritative Session Architecture
- P9-04 Postgres-Centered Architecture Contract
- P9-06-007 realtime and authoritative-session service ports
- action proposal and approval architecture
- deterministic randomness and replay
- checkpoint, persistence, authorization, and hidden-information contracts
- application repository PR and CI evidence

**Status:** Canonical architecture with provider-neutral service ports implemented; complete online internal-alpha behavior remains future verified work.

---

# 60. Backup, Restore, and Provider-Exit Export

## 60.1 Purpose

Define the contracts and operational practices required to preserve Multiversal data, restore service after failure, recover sessions and campaigns, and move the project away from any provider without losing identity, state, provenance, or history.

## 60.2 Recovery principle

A backup is useful only when it can be verified and restored.

An export is useful only when it is complete, documented, and importable into a replacement environment.

## 60.3 Scope

Backup and exit coverage should include, as applicable:

- database schema and data;
- canonical content registry;
- pack registry and installed versions;
- campaign and character state;
- events;
- snapshots;
- identity mappings;
- authorization relationships;
- entitlement grants and evaluations;
- media originals and permitted derivatives;
- localization;
- audit and security evidence;
- migration history;
- configuration templates without secrets;
- manifests and checksums.

## 60.4 Backup types

The architecture may support:

- full backup;
- incremental backup;
- transaction-log or point-in-time recovery;
- object-storage backup;
- pack archive backup;
- configuration backup;
- checkpoint;
- campaign export;
- provider-exit export.

These serve different purposes and must not be mislabeled as interchangeable.

## 60.5 Backup port

The provider-neutral backup port should support:

- create plan;
- execute;
- verify;
- report manifest;
- report checksum;
- identify encryption and storage class;
- identify retention metadata;
- return receipt;
- expose stable failures.

## 60.6 Restore port

The restore port should support:

- inspect backup;
- verify integrity;
- check compatibility;
- produce dry-run plan;
- restore into approved target;
- verify result;
- return receipt;
- report partial or failed state;
- support retry or forward repair.

## 60.7 Provider-exit export port

The export port should support:

- select scope;
- produce portable manifest;
- serialize data in documented formats;
- include stable IDs and version metadata;
- include checksums;
- include relationship and dependency maps;
- include lawful media or retrieval references;
- include migration guidance;
- verify completeness;
- return receipt.

## 60.8 Backup manifest

A backup manifest should identify:

- backup ID;
- environment;
- scope;
- created time;
- actor or scheduled policy;
- source versions;
- database version;
- schema versions;
- pack versions;
- event cursor ranges;
- media inventory;
- encryption metadata;
- file list;
- checksums;
- previous backup relationship;
- verification result.

## 60.9 Export manifest

A provider-exit manifest should identify:

- export ID;
- source environment;
- export contract version;
- included domains;
- excluded data and reason;
- stable identities;
- provider mappings;
- schemas;
- formats;
- files;
- checksums;
- encryption;
- import order;
- compatibility;
- validation;
- legal or rights restrictions.

## 60.10 Portable formats

Portable export should prefer documented, broadly usable formats such as:

- SQL schema and data where appropriate;
- CSV for tabular data where lossless;
- JSON or JSON Lines for structured records and events;
- archive files for packs;
- original media files;
- checksums;
- Markdown or JSON documentation.

A provider-native backup may also exist, but it is not sufficient as the only exit artifact.

## 60.11 Internal identities

Exports must preserve internal stable IDs.

Provider-specific identity IDs should be included as mappings, not replacements.

A restored or migrated environment should reconnect:

- users;
- characters;
- campaigns;
- ownership;
- entitlements;
- events;
- media;
- pack references.

## 60.12 Secrets exclusion

Backups and exports must not include live secrets by default.

They may include:

- configuration keys or names;
- required secret inventory;
- rotation instructions;
- environment templates.

Actual credentials require separate approved secret-management backup policy.

## 60.13 Encryption

Backups containing protected data should be encrypted:

- in transit;
- at rest;
- in portable transfer where required.

Encryption keys must not be stored beside the encrypted backup in a way that defeats protection.

## 60.14 Access control

Backup and restore permissions should be narrowly granted.

Authorized operations should require:

- appropriate role;
- environment;
- scope;
- reauthentication for high-impact operations where appropriate;
- audit;
- receipt.

## 60.15 Retention

Retention policy should define:

- backup frequency;
- retention period;
- legal or policy requirements;
- deletion;
- media history;
- provider costs;
- protected-data minimization.

No production schedule is approved merely by this architecture.

## 60.16 Recovery objectives

Before internal-alpha trust, the project should define:

- recovery point objective;
- recovery time objective;
- acceptable session loss;
- campaign restore expectations;
- media recovery expectations;
- provider outage behavior.

Targets must be based on tested capability and cost.

## 60.17 Backup verification

Verification should include:

- manifest parse;
- checksum;
- expected file count;
- schema and version presence;
- decryptability;
- sample reads;
- event continuity;
- pack registry completeness;
- media inventory;
- entitlement and identity mappings.

## 60.18 Restore drill

A restore drill should:

1. select a verified backup;
2. create an isolated target;
3. validate compatibility;
4. restore;
5. apply required migrations;
6. rebuild derived indexes;
7. run integrity checks;
8. run representative application scenarios;
9. compare expected fingerprints;
10. produce a drill report.

A backup has not passed the trust gate until a restore drill succeeds.

## 60.19 Point-in-time recovery

Where a provider supports point-in-time recovery, the adapter may use it.

The provider-neutral contract should still preserve:

- target time or event;
- plan;
- affected data;
- verification;
- receipt;
- portable backup fallback.

## 60.20 Session recovery

Session recovery may use:

- committed database state;
- events;
- snapshots;
- checkpoints;
- pack and rules versions.

A recovered session should append a recovery event rather than erasing the failed history.

## 60.21 Campaign recovery

Campaign recovery should preserve:

- members;
- characters;
- relationships;
- inventory;
- adventures;
- discoveries;
- world state;
- events;
- media references;
- permissions.

## 60.22 Pack recovery

Recovery should restore:

- pack identities;
- exact versions;
- manifests;
- checksums;
- ownership map;
- migrations;
- installed state.

If lawful pack bytes cannot be included, the export must identify the required retrieval source and compatibility constraints.

## 60.23 Media recovery

Media recovery should preserve:

- stable asset ID;
- original file where permitted;
- derivatives or rebuild profile;
- hash;
- rights;
- visibility;
- subject links;
- storage-independent metadata.

## 60.24 Search and cache recovery

Search indexes and caches are derived and should normally be rebuilt.

The recovery package should preserve:

- source data;
- index schema or configuration;
- model or embedding version where semantic search is used;
- rebuild procedure.

## 60.25 Provider-exit rehearsal

A provider-exit rehearsal should demonstrate:

- export from source adapter;
- validation of portable package;
- import into local or replacement adapter;
- preserved stable IDs;
- preserved relationships;
- preserved events and snapshots;
- rebuilt indexes;
- representative user and session behavior;
- documented gaps and cost.

## 60.26 Export completeness

Completeness checks should compare:

- source registry counts;
- export manifest counts;
- stable IDs;
- relationship counts;
- event ranges;
- pack versions;
- media inventory;
- identity mappings;
- entitlement records;
- migration history.

## 60.27 Import rehearsal

An export is not complete until a compatible import path is tested.

Import should:

- validate;
- stage;
- map provider identities;
- preserve internal IDs;
- apply migrations;
- rebuild derived data;
- verify;
- produce receipt.

## 60.28 Corruption handling

A corrupted backup should be:

- rejected;
- quarantined;
- retained for diagnosis where safe;
- reported with the failing checks;
- excluded from automatic restore.

## 60.29 Partial backup

A partial backup must be labeled clearly.

It should identify:

- included scope;
- excluded scope;
- reason;
- dependencies;
- restore limitations.

A campaign-only export is not a full provider-exit export.

## 60.30 Deletion and expiry

Backup deletion should be:

- authorized;
- policy-driven;
- audited;
- verified;
- coordinated with legal and incident requirements.

Deleting a primary record does not guarantee immediate deletion from valid retained backups; policy must explain this.

## 60.31 Disaster scenarios

Recovery planning should test scenarios such as:

- accidental deletion;
- failed migration;
- database corruption;
- provider outage;
- lost object storage;
- compromised credential;
- invalid pack update;
- failed session projection;
- account-provider exit;
- region or service unavailability.

## 60.32 Ransomware and destructive compromise

The architecture should consider:

- immutable or isolated backup copies;
- separate credentials;
- restoration into clean environment;
- key rotation;
- audit preservation;
- incident revocation.

## 60.33 Operational runbook

A recovery runbook should identify:

- trigger;
- authority;
- communication;
- backup selection;
- isolation;
- restore;
- validation;
- reopen criteria;
- rollback;
- evidence preservation.

## 60.34 Cost controls

Backup cost should be monitored for:

- storage;
- retention;
- transfer;
- restore;
- object versions;
- egress.

Cost optimization must not eliminate the only tested restore path.

## 60.35 Privacy and rights

Exports and backups contain sensitive data.

They must preserve:

- least privilege;
- encryption;
- retention;
- user privacy;
- content rights;
- campaign secrecy;
- audit.

Provider exit does not grant new rights to redistribute content.

## 60.36 Testing

Contract and operational tests should cover:

- create backup;
- verify;
- corrupt file detection;
- restore;
- incompatible version;
- partial scope;
- encrypted artifact;
- provider-exit export;
- import;
- identity mapping;
- media recovery;
- deterministic fingerprint;
- failure receipt.

## 60.37 Current verified boundary

The active roadmap identifies P9-06-008 as the next executable repository task:

> implement backup, restore, and provider-exit export ports.

This work is authorized only within the bounded provider-neutral scope and must include deterministic contracts, fixtures, validation, CI, recovery integrity, export completeness, and no hosted-service or credential commitment.

This chapter does not claim that P9-06-008 has been completed.

## 60.38 Controlling references

- P9-04 backup, restore, checkpoint, and provider-exit contract
- P9-05 bounded spike and cost guardrails
- active Application Implementation Roadmap
- P9-06-008 current task
- canonical identity, pack, event, snapshot, media, entitlement, and migration architecture
- future provider-exit rehearsal and acceptance gates

**Status:** Canonical architecture and active next implementation scope; ports and rehearsals remain unfinished unless later repository evidence verifies completion.

---

# 61. Security, Privacy, and Secrets

## 61.1 Purpose

Define the security, privacy, credential, data-protection, incident, and trust requirements that apply to local development, CI, preview, internal alpha, provider adapters, content ingestion, live sessions, exports, and future production.

## 61.2 Security principle

Security is a system property.

It cannot be provided only by:

- hidden UI controls;
- one provider;
- one firewall;
- one secrets file;
- one review;
- one automated scanner.

Security must be enforced through identity, authorization, storage, code, operations, CI, observability, backup, and recovery.

## 61.3 Current authorization boundary

The owner has authorized bounded repository implementation through P9-06-023.

The authorization does not permit:

- production credentials;
- paid-provider enrollment;
- production deployment;
- public release;
- irreversible vendor coupling;
- spending beyond a separate owner gate.

Security work must remain within this boundary.

## 61.4 Local-only development contract

The local development environment should:

- run without production credentials;
- use local or test adapters;
- use deterministic fixtures;
- bind only to intended interfaces;
- avoid real private user data;
- identify environment clearly;
- prevent destructive commands against unknown or production targets.

The local-only environment contract is recorded as complete under P9-06-002.

## 61.5 Secrets isolation policy

Secrets should be:

- excluded from source control;
- excluded from fixtures;
- excluded from screenshots and artifacts;
- environment-scoped;
- least-privileged;
- rotated;
- revocable;
- unavailable to untrusted clients;
- referenced through documented configuration names.

The secrets and environment isolation policy is recorded as complete under P9-06-003, completing Acceptance Gate AG-01.

## 61.6 Secret categories

Secret categories may include:

- identity-provider credentials;
- database credentials;
- storage keys;
- realtime-provider keys;
- AI-provider keys;
- signing keys;
- encryption keys;
- notification credentials;
- deployment tokens;
- webhook secrets.

Each category requires an owner, environment, rotation, and revocation procedure before production use.

## 61.7 Configuration versus secret

Configuration may be committed when it is nonsecret and environment-safe.

Examples include:

- feature names;
- local ports;
- schema versions;
- provider adapter selection;
- public callback paths.

Secrets include values that grant authority or decrypt protected data.

## 61.8 Secret injection

Secrets should enter applications through an approved secret-management or environment mechanism.

They must not be embedded in:

- client bundles;
- source files;
- logs;
- error messages;
- pack files;
- canonical content;
- documentation examples.

## 61.9 Secret scanning

Repositories and CI should use secret scanning appropriate to the environment.

A detected secret should trigger:

1. containment;
2. revocation or rotation;
3. history assessment;
4. incident record;
5. repair;
6. verification.

Deleting the visible line is not sufficient if the secret was committed.

## 61.10 Least privilege

Every human, service, adapter, database role, and CI job should receive only the required permissions.

Examples:

- a search indexer reads permitted source data but cannot change campaign state;
- a backup worker reads required data but cannot adjudicate sessions;
- a client cannot access privileged database credentials;
- a proposal-only creator cannot promote canon.

## 61.11 Deny by default

Unknown subjects, roles, fields, routes, actions, and provider callbacks should be denied unless explicitly permitted.

## 61.12 Defense in depth

Security layers may include:

- authentication;
- authorization;
- database isolation;
- schema validation;
- input limits;
- transport encryption;
- storage encryption;
- output filtering;
- audit;
- rate limits;
- dependency scanning;
- backup;
- revocation;
- monitoring.

## 61.13 Data classification

Data should be classified by sensitivity.

Representative classes include:

- public canonical content;
- licensed or entitlement-controlled content;
- campaign-visible data;
- party-visible data;
- player-private notes;
- GM-only data;
- identity and contact data;
- entitlement and transaction data;
- security events;
- secrets;
- owner-only release data.

Classification determines access, logging, export, retention, and incident response.

## 61.14 Data minimization

The system should collect and retain only data required for the approved function.

Future analytics, billing, marketing, moderation, and public-community data require separate review.

## 61.15 Privacy principle

User conversations, notes, character content, campaign state, and private GM material should remain private to the authorized scope.

Provider adapters should receive only the minimum data needed.

## 61.16 Protected game information

Hidden game content is both a gameplay and privacy boundary.

Protected information includes:

- GM notes;
- unrevealed clues;
- hidden map layers;
- NPC motives;
- secret objectives;
- private player notes;
- participant-specific information.

Protection applies to storage, search, AI, logs, exports, notifications, and caches.

## 61.17 Personally identifiable information

Identity and contact data should be isolated from ordinary game content where practical.

Access should be limited to the services that need it.

## 61.18 Authentication security

Authentication should support:

- secure session tokens;
- expiry;
- revocation;
- provider mapping;
- secure callback validation;
- account recovery;
- reauthentication for sensitive actions.

Production mechanisms remain provider-selection work.

## 61.19 Authorization security

Authorization should be checked:

- at service boundaries;
- at database or storage boundaries where supported;
- for queries;
- for fields;
- for mutations;
- for subscriptions;
- for exports;
- for AI retrieval.

## 61.20 Client security

Clients must not contain:

- privileged credentials;
- unrestricted service keys;
- complete hidden campaign state;
- trusted authorization decisions;
- unvalidated executable pack code.

Client storage of offline data must follow permission, encryption, expiry, and revocation policy.

## 61.21 API security

APIs should use:

- schema validation;
- parameterized queries;
- stable authentication;
- authorization;
- request-size limits;
- rate limits;
- idempotency;
- safe errors;
- origin and transport controls where applicable;
- audit.

## 61.22 Input validation

All external input should be treated as untrusted, including:

- forms;
- API payloads;
- pack archives;
- CSV and JSON files;
- images;
- maps;
- localization;
- AI output;
- provider webhooks;
- imported exports.

## 61.23 Pack and archive security

Pack ingestion should defend against:

- path traversal;
- archive bombs;
- duplicate-path tricks;
- malformed encodings;
- executable payloads;
- unsafe migrations;
- schema abuse;
- spoofed ownership;
- checksum mismatch.

## 61.24 Upload security

Uploads should be validated for:

- type;
- size;
- content;
- filename normalization;
- metadata;
- malware or unsafe content where appropriate;
- rights;
- visibility;
- storage isolation.

## 61.25 Database security

Database controls should include:

- least-privileged roles;
- row or scope isolation;
- parameterized queries;
- encrypted transport;
- protected backups;
- migration controls;
- audit;
- restricted administrative access.

## 61.26 Realtime security

Realtime channels should enforce:

- authenticated connection;
- authorized subscription;
- scoped publication;
- revocation;
- hidden-data filtering;
- message validation;
- rate and size limits;
- sequence integrity.

## 61.27 AI security

AI integrations should defend against:

- prompt injection;
- hidden-data exfiltration;
- tool overreach;
- unauthorized actions;
- untrusted generated code or schemas;
- provider retention concerns;
- excessive context;
- credential leakage.

AI output remains untrusted until validated.

## 61.28 Prompt and retrieval boundaries

AI prompts should include only the authorized context needed.

Retrieved content should preserve:

- subject;
- campaign;
- role;
- entitlement;
- source;
- provenance;
- visibility.

## 61.29 Tool authorization

Every AI tool call that can mutate state should enforce the same authorization as a direct human request.

The AI’s presence does not grant additional authority.

## 61.30 Dependency security

Dependencies should be:

- pinned or lockfile-controlled;
- scanned;
- updated through review;
- minimized;
- sourced from trusted registries;
- verified in CI.

A dependency update must not be merged solely to silence a scanner without compatibility testing.

## 61.31 Supply-chain security

Release and CI should preserve:

- source commit;
- dependency lock;
- build environment;
- artifacts;
- checksums;
- attestations where later approved;
- reviewer and CI evidence.

## 61.32 CI security

CI should:

- use least-privileged tokens;
- avoid exposing secrets to untrusted branches;
- isolate artifacts;
- redact logs;
- pin actions or tools where practical;
- protect release workflows;
- prevent forked or proposal-only code from accessing privileged credentials.

## 61.33 Logging

Logs must not contain by default:

- passwords;
- access tokens;
- encryption keys;
- full private notes;
- unrevealed GM content;
- sensitive identity data;
- complete exported data;
- payment details.

Use identifiers and correlation IDs instead.

## 61.34 Audit events

Security-sensitive operations should create append-only audit evidence, including:

- login and recovery;
- role change;
- permission denial;
- ownership transfer;
- entitlement change;
- backup and restore;
- export;
- secret rotation;
- administrative action;
- canonical promotion;
- provider change.

## 61.35 Security events

Security events should be separate from ordinary product analytics.

They may include:

- repeated failed authentication;
- suspicious token use;
- unauthorized subscription;
- secret detection;
- rate-limit abuse;
- pack-integrity failure;
- export anomaly;
- privilege escalation attempt.

## 61.36 Encryption

Protected data should use encryption:

- in transit;
- at rest where appropriate;
- in backups;
- in portable exports.

Encryption design requires key-management and recovery procedures.

## 61.37 Key management

Keys should have:

- owner;
- environment;
- purpose;
- creation;
- rotation;
- revocation;
- backup or escrow policy where appropriate;
- access audit.

No production key-management provider is selected by this chapter.

## 61.38 Rate limiting

Rate limits should protect:

- authentication;
- command submission;
- search;
- exports;
- uploads;
- AI requests;
- invitations;
- password or recovery attempts.

Limits should provide safe errors and avoid discriminatory impact on accessibility tools or shared networks.

## 61.39 Abuse and moderation boundary

Public communities, public content sharing, marketplaces, and moderation are outside the current internal-alpha scope unless later approved.

The architecture should not claim moderation readiness before those programs exist.

## 61.40 Privacy rights

Future production must define processes for:

- access;
- correction;
- export;
- deletion;
- account closure;
- consent;
- retention;
- minors if applicable;
- legal requests.

Exact obligations depend on deployment jurisdictions and require later legal review.

## 61.41 Backup privacy

Backups retain protected data and require:

- encryption;
- access control;
- retention;
- deletion policy;
- incident handling;
- restore audit.

## 61.42 Export privacy

Exports should:

- require authority;
- minimize scope;
- protect files;
- redact excluded data;
- record operation;
- expire temporary delivery links;
- preserve legal and content-rights restrictions.

## 61.43 Incident response

An incident process should include:

1. detect;
2. contain;
3. preserve evidence;
4. revoke or rotate;
5. assess affected systems and data;
6. recover;
7. validate;
8. communicate under approved policy;
9. document corrective action.

## 61.44 Vulnerability handling

A vulnerability report should record:

- affected component;
- severity;
- reproducibility;
- exposure;
- mitigation;
- fix;
- validation;
- disclosure status.

## 61.45 Security testing

Testing should include:

- authorization denied cases;
- cross-campaign isolation;
- field-level secrecy;
- query inference;
- pack traversal;
- malformed upload;
- duplicate command;
- stale session;
- rate limit;
- secret scanning;
- dependency scanning;
- backup access;
- export scope;
- AI prompt injection;
- log redaction.

## 61.46 Privacy testing

Privacy tests should verify:

- player cannot access GM data;
- one campaign cannot access another;
- private notes remain private;
- exports contain only permitted data;
- logs exclude protected fields;
- AI context is minimized;
- deleted or revoked access behaves according to policy.

## 61.47 Production gate

Before production or public release, the project requires:

- threat model;
- security review;
- privacy policy;
- data inventory;
- retention policy;
- incident plan;
- credential and key management;
- backup and restore drill;
- dependency and vulnerability review;
- owner approval;
- any required legal review.

## 61.48 Current verified boundary

The repository baseline, local-only environment contract, and secrets/environment isolation policy are recorded as complete through P9-06-003 and Acceptance Gate AG-01.

This does not prove full production security or privacy readiness.

Production credentials, hosted provider enrollment, public deployment, and formal privacy claims remain gated.

## 61.49 Controlling references

- P9-06-002 local-only development environment contract
- P9-06-003 secrets and environment isolation policy
- Acceptance Gate AG-01
- P9-04 security contract
- identity, authorization, entitlement, realtime, backup, export, AI, and pack security requirements
- application repository security tests and CI

**Status:** Canonical security and privacy architecture; initial repository safety gate is complete, while production readiness remains future owner-gated work.



# 62. Observability, Performance, and Cost Controls

## 62.1 Purpose

Define how Multiversal measures system behavior, diagnoses failures, protects hidden information in operational data, validates performance in realistic workflows, and keeps infrastructure and AI costs within owner-approved limits.

## 62.2 Observability principle

Observability should answer:

- What happened?
- Which operation, subject, campaign, session, pack, or provider adapter was involved?
- Did accepted state change?
- Where did time or resources go?
- Can the problem be reproduced?
- Does the evidence expose protected content?
- Does the condition require action?

Observability is not unrestricted logging.

## 62.3 Observability signals

The architecture may use:

- structured logs;
- metrics;
- traces;
- audit events;
- security events;
- health checks;
- readiness checks;
- cost signals;
- validation artifacts;
- user-visible operation receipts.

Each signal has a different purpose and retention policy.

## 62.4 Structured logs

Logs should use stable fields such as:

- environment;
- service or module;
- operation ID;
- correlation ID;
- subject ID where lawful;
- campaign or session ID where required;
- adapter;
- action type;
- status;
- error class;
- duration;
- version;
- timestamp.

Logs should avoid unstructured dumps of entire requests or state objects.

## 62.5 Redaction

Operational logs must not contain by default:

- secrets;
- access tokens;
- encryption keys;
- full private notes;
- GM-only content;
- unrevealed clues;
- complete character exports;
- payment details;
- provider credentials;
- raw AI prompts containing protected content.

Redaction should occur before transport to external observability providers.

## 62.6 Correlation and causation

A request or background operation should preserve correlation through:

- client request;
- API operation;
- domain command;
- persistence transaction;
- outbox message;
- realtime delivery;
- background worker;
- result receipt.

Causation IDs should connect derived events without implying that every correlated event caused every other event.

## 62.7 Audit versus operational logs

Audit events preserve authoritative evidence for sensitive or important operations.

Operational logs support diagnosis and may expire sooner.

Audit events may include:

- role changes;
- entitlement changes;
- ownership transfers;
- GM modifications;
- pack installation;
- migration;
- restore;
- export;
- canonical promotion;
- administrative actions.

Operational logs must not be treated as the sole audit record.

## 62.8 Security events

Security events should be separate from ordinary product activity.

They may include:

- repeated authentication failure;
- unauthorized subscription attempt;
- permission escalation attempt;
- invalid pack signature or checksum;
- secret detection;
- export anomaly;
- suspicious command rate;
- backup access failure.

## 62.9 Metrics

Metrics should be aggregated and low-cardinality where practical.

Useful areas include:

- request count;
- error rate;
- command latency;
- proposal-to-approval latency;
- realtime lag;
- reconnect success;
- outbox backlog;
- database saturation;
- search latency;
- pack installation time;
- migration time;
- backup duration;
- restore success;
- storage growth;
- AI request count;
- estimated cost.

Protected stable IDs should not be used as unbounded metric labels.

## 62.10 Traces

Distributed or in-process traces may follow a bounded operation across modules and adapters.

Trace spans should identify:

- module;
- operation;
- adapter;
- duration;
- stable error class;
- retry;
- result state.

Trace payloads must be redacted.

## 62.11 Health checks

A health check answers whether a component is operating.

Health categories may include:

- process health;
- dependency reachability;
- database connectivity;
- outbox dispatcher;
- realtime adapter;
- search index;
- storage adapter;
- migration status.

A public health endpoint should reveal minimal information.

## 62.12 Readiness checks

Readiness should determine whether an instance can safely receive work.

Readiness may fail when:

- migrations are incomplete;
- required configuration is invalid;
- database is unavailable;
- provider contract test failed;
- required pack registry is inconsistent;
- recovery mode is active.

## 62.13 User-visible operation status

Long operations should expose safe status for:

- pack validation;
- installation;
- migration;
- backup;
- restore;
- export;
- index rebuild;
- media processing.

Status should identify:

- queued;
- running;
- succeeded;
- failed;
- cancelled;
- recovery required.

Exact states remain implementation-controlled.

## 62.14 Service-level indicators

Before production service-level objectives are approved, internal indicators may track:

- successful command rate;
- action latency;
- reconnect recovery;
- restore success;
- backup verification;
- search response;
- error recovery;
- hidden-information failures.

Targets should be based on measured internal-alpha needs rather than copied from unrelated products.

## 62.15 Performance principle

Performance work should optimize complete user workflows rather than isolated synthetic endpoints.

Priority workflows include:

- shell and current-context load;
- object search;
- character open;
- campaign dashboard;
- scene activation;
- proposal submission;
- GM approval;
- accepted result synchronization;
- reconnect;
- large inventory;
- large relationship graph;
- pack installation;
- backup and restore.

## 62.16 Performance budgets

Each major workflow should eventually have a measurable budget for:

- server latency;
- client interaction latency;
- payload size;
- memory;
- CPU;
- database queries;
- network transfer;
- mobile responsiveness.

Budgets remain internal targets until validated and owner-approved.

## 62.17 Latency measurement

Latency should distinguish:

- client input to request;
- network;
- authentication;
- authorization;
- validation;
- domain calculation;
- persistence;
- outbox;
- realtime delivery;
- client render.

A single total number is insufficient for diagnosis.

## 62.18 Large-corpus performance

The content system must be tested against the actual governed corpus, including the validated 19,199-record registry baseline.

Large-corpus tests should cover:

- index build;
- search;
- filtering;
- object inspection;
- relationship traversal;
- pack ownership queries;
- provenance lookup;
- mobile pagination or virtualization.

## 62.19 Large-session performance

Session tests should consider:

- multiple participants;
- many scene entities;
- many conditions;
- large action history;
- reconnect after missed events;
- hidden projections;
- map updates;
- GM approval queue.

## 62.20 Client performance

Client performance should address:

- initial bundle;
- route loading;
- rendering large lists;
- map complexity;
- graph complexity;
- memory growth;
- background tabs;
- touch responsiveness;
- low-powered devices.

## 62.21 Server performance

Server performance should address:

- database query plans;
- transaction contention;
- connection pools;
- outbox throughput;
- projection generation;
- serialization;
- adapter latency;
- backup load;
- migration locks.

## 62.22 Caching

Caching may improve:

- canonical object reads;
- permitted search results;
- rules inspection;
- content summaries;
- localized text;
- static media metadata.

Cache correctness requires keys that include relevant:

- version;
- permissions;
- entitlement;
- campaign;
- locale;
- override state.

## 62.23 Rate and resource limits

Limits may protect:

- login;
- commands;
- search;
- uploads;
- exports;
- AI calls;
- background jobs.

Limits should be explicit, observable, and tested for ordinary gameplay and accessibility use.

## 62.24 Degradation

When a nonauthoritative provider is degraded, the application should prefer safe degraded behavior.

Examples include:

- search temporarily unavailable while direct ID access remains;
- realtime unavailable while committed state persists;
- optional media unavailable while rules remain usable;
- AI unavailable while manual workflow continues.

The application must not imply that accepted state was lost when only a derived service failed.

## 62.25 Cost principle

Infrastructure and AI cost should remain bounded, visible, and owner-controlled.

The approved technical spike established:

- a target operating envelope of **$0–$25 per month** for the bounded internal-alpha class; and
- mandatory owner review above **$35 per month**.

These figures are planning guardrails, not permission to spend.

## 62.26 Cost categories

Cost tracking should distinguish:

- database;
- storage;
- bandwidth and egress;
- realtime;
- search;
- AI inference;
- media processing;
- logging and telemetry;
- backups;
- deployment;
- notification delivery;
- platform fees.

## 62.27 Cost signals

Adapters should expose cost-relevant usage where practical, including:

- request count;
- compute duration;
- storage volume;
- transfer volume;
- active connections;
- AI tokens or equivalent units;
- backup size;
- artifact retention.

## 62.28 Cost budgets

A development or internal-alpha environment may define budgets by:

- provider;
- capability;
- day;
- month;
- workspace;
- AI feature.

A budget should produce warning and blocking behavior according to owner-approved policy.

## 62.29 Owner spending gate

Any paid enrollment, production commitment, or expected spend beyond authorized limits requires owner approval.

Automated systems must not:

- upgrade plans;
- activate paid add-ons;
- increase quotas with cost;
- provision production resources;
- accept irreversible provider commitments.

## 62.30 AI cost controls

AI features should support:

- bounded context;
- retrieval before generation;
- structured responses;
- caching where safe;
- task-specific models;
- cancellation;
- usage reporting;
- per-feature limits;
- local or non-AI fallback.

Cost optimization must not remove provenance or permission checks.

## 62.31 Storage controls

Storage management should include:

- content-addressed media;
- derivative cleanup;
- backup retention;
- artifact expiry;
- duplicate detection;
- compression;
- export planning.

Cleanup must preserve lawful retention and recovery.

## 62.32 Telemetry cost

Observability systems can create significant cost.

The project should control:

- event volume;
- trace sampling;
- log retention;
- artifact retention;
- high-cardinality labels;
- development verbosity;
- protected-data filtering.

## 62.33 Cost alarms

Alarms may trigger on:

- monthly estimate;
- sudden usage growth;
- storage growth;
- bandwidth spike;
- AI request spike;
- backup cost;
- provider quota.

An alarm is not permission to modify a paid plan automatically.

## 62.34 Performance testing

Performance tests should include:

- repeatable fixtures;
- realistic data volume;
- warm and cold behavior;
- concurrency;
- low-powered client;
- degraded provider;
- reconnect;
- measurement artifacts.

## 62.35 Load testing boundary

Load testing must not target public or production services without authorization.

Local, preview, or isolated test environments should use controlled data and limits.

## 62.36 Regression

Performance and cost baselines should be versioned.

A regression report should identify:

- workflow;
- baseline;
- current result;
- change;
- confidence;
- likely cause;
- remediation;
- approval if a budget changes.

## 62.37 Observability acceptance

Operational readiness requires evidence that the system can detect and diagnose:

- failed authentication;
- denied authorization;
- persistence failure;
- duplicate command;
- stale command;
- realtime lag;
- reconnect failure;
- backup failure;
- restore failure;
- cost threshold;
- protected-data logging violation.

## 62.38 Current verified boundary

P9-04 defines required observability and cost signals.

The active backlog reserves later work for structured audit, operational telemetry, and cost threshold alarms.

The roadmap records P9-06-001 through P9-06-007 as complete. It does not establish that later telemetry and cost-control items are complete.

## 62.39 Controlling references

- P9-04 observability and cost contract
- P9-05 bounded technical spike and cost envelope
- P9-06 operations and exit workstream
- golden performance and regression principles
- Stage A internal-alpha hardening
- provider-neutral adapter contracts

**Status:** Canonical architecture and cost guardrails. Complete operational telemetry, performance baselines, and cost alarms remain future verified implementation work.

---

# 63. Testing and CI Architecture

## 63.1 Purpose

Define the layered test strategy and continuous-integration architecture used to verify canonical content, service contracts, migrations, permissions, sessions, UI workflows, recovery, performance, and release evidence.

## 63.2 Testing principle

Completion requires executable evidence.

A plan, document, fixture proposal, local claim, opened pull request, or started workflow does not prove that a capability is complete.

## 63.3 Test layers

The project should use complementary layers:

- static checks;
- schema validation;
- unit tests;
- property and invariant tests;
- contract tests;
- integration tests;
- migration tests;
- permission tests;
- realtime and reconnect tests;
- UI component tests;
- end-to-end vertical-slice tests;
- accessibility tests;
- golden regression tests;
- performance tests;
- backup and restore drills;
- provider-exit rehearsals;
- platform-specific tests.

## 63.4 Static checks

Static checks may include:

- formatting;
- linting;
- type checking;
- dependency policy;
- forbidden imports;
- secrets scanning;
- schema compilation;
- generated-file consistency;
- documentation links.

Static checks should be deterministic and runnable locally.

## 63.5 Unit tests

Unit tests should verify bounded domain behavior without unnecessary provider dependencies.

Representative areas include:

- rules calculations;
- entitlement decisions;
- ID generation;
- validation;
- relationship rules;
- migration transforms;
- permission predicates;
- pack planning.

## 63.6 Invariant and property tests

Property tests may verify invariants such as:

- quantity conservation;
- no inventory duplication;
- stable ID determinism;
- event sequence monotonicity;
- idempotent command handling;
- relationship directionality;
- container cycle rejection;
- hidden-data exclusion.

## 63.7 Schema tests

Schema tests should cover:

- valid fixtures;
- invalid fixtures;
- boundary values;
- unknown fields;
- versions;
- conditional requirements;
- extension namespaces;
- migration inputs and outputs.

## 63.8 Contract tests

Every provider-neutral adapter should pass shared contract tests.

Contract tests should verify:

- operation shape;
- stable errors;
- idempotency;
- concurrency;
- permissions;
- retries;
- exportability;
- unsupported capabilities.

## 63.9 Persistence integration tests

Persistence tests should verify:

- transaction commit;
- rollback;
- concurrency conflict;
- event append;
- projection update;
- outbox;
- snapshot;
- migration;
- reset;
- import and export.

## 63.10 Authorization tests

Authorization tests must include allowed and denied paths.

They should cover:

- wrong campaign;
- wrong character;
- wrong role;
- revoked access;
- hidden field;
- query inference;
- export scope;
- AI retrieval;
- realtime subscription;
- owner-only gate.

## 63.11 Entitlement tests

Entitlement tests should cover:

- free access;
- ability tiers one and two;
- higher-tier denial;
- grants;
- sponsored access;
- expiry;
- cancellation;
- campaign grant;
- offline snapshot;
- search;
- export.

## 63.12 Session tests

Authoritative-session tests should cover:

- connect;
- role projection;
- proposal;
- validation;
- approval;
- denial;
- modification;
- duplicate command;
- stale command;
- ordered events;
- hidden information;
- disconnect;
- reconnect;
- checkpoint;
- restore.

## 63.13 Two-device tests

The internal-alpha acceptance suite must use two distinct connected clients or devices.

It should verify:

- separate identity;
- correct permissions;
- synchronized scene;
- Player proposal;
- GM decision;
- persistent result;
- hidden-data isolation;
- reconnect;
- recovery.

## 63.14 Pack lifecycle tests

Pack tests should cover:

- integrity;
- manifest;
- index;
- dependencies;
- ownership;
- install;
- repeat install;
- update;
- migration;
- blocked removal;
- safe removal;
- reinstall;
- zero unintended residue;
- export.

## 63.15 Content tests

Content tests should verify:

- schema;
- stable IDs;
- source provenance;
- relationships;
- mechanics references;
- completeness;
- conflicts;
- coverage;
- deterministic packaging.

## 63.16 Golden tests

Golden tests preserve approved expected output.

The existing Golden Test Corpus and Balance Harness provide validated deterministic evidence across domains.

Golden expectations may change only through reviewed, versioned baseline updates.

## 63.17 Replay tests

Replay tests should verify that recorded:

- seeds;
- rolls;
- actions;
- events;
- versions;
- checkpoints;

produce the expected authorized projection.

Replay must not create new events.

## 63.18 UI component tests

Component tests should verify:

- rendering;
- keyboard behavior;
- focus;
- touch-equivalent action;
- validation;
- disabled state;
- permission state;
- loading;
- error;
- responsive behavior.

## 63.19 End-to-end tests

End-to-end tests should prioritize vertical slices such as:

- identity to correct workspace;
- character creation and save;
- campaign creation and invitation;
- scene construction;
- Player proposal and GM approval;
- inventory transfer;
- investigation discovery;
- content submission;
- pack install and restore.

## 63.20 Accessibility tests

Accessibility testing should include:

- automated scanning;
- keyboard-only execution;
- screen-reader testing;
- zoom and text scaling;
- focus;
- contrast;
- reduced motion;
- map and graph alternatives;
- mobile touch.

Automated scans are not sufficient.

## 63.21 Performance tests

Performance tests should use realistic governed data.

They should cover:

- large object catalog;
- large character;
- large inventory;
- complex scene;
- relationship graph;
- action latency;
- reconnect;
- pack installation;
- index rebuild.

## 63.22 Backup and restore tests

Tests should verify:

- backup creation;
- manifest;
- checksum;
- corruption detection;
- restore plan;
- successful restore;
- incompatible restore rejection;
- rebuilt indexes;
- representative application behavior.

## 63.23 Provider-exit rehearsal

The rehearsal should:

- export from one adapter;
- validate portable artifacts;
- import to local or replacement adapter;
- preserve internal IDs;
- preserve relationships;
- preserve events and snapshots;
- rebuild derived data;
- run acceptance scenarios.

## 63.24 Test data

Test data should be:

- deterministic;
- synthetic or approved;
- free of real credentials;
- free of private production data;
- versioned;
- minimal for unit tests;
- realistic for integration and performance tests.

## 63.25 Test isolation

Tests should not depend on:

- execution order;
- another test’s data;
- external mutable provider state;
- production services;
- hidden developer machine configuration.

## 63.26 CI workflow structure

CI may use separate workflows or jobs for:

- static checks;
- unit tests;
- schemas;
- contract tests;
- integration tests;
- content validation;
- migration;
- pack lifecycle;
- UI tests;
- accessibility;
- platform builds;
- release evidence.

## 63.27 Changed-scope optimization

CI may target changed areas for speed, but required full gates should run at appropriate merge or release boundaries.

Optimization must not allow a cross-domain regression to escape because only one folder was tested.

## 63.28 Required checks

Protected branches should require the checks appropriate to the changed scope.

Required checks should be:

- named clearly;
- stable;
- reproducible;
- difficult to bypass;
- documented.

## 63.29 Independent verification

High-risk outputs should receive independent verification.

Examples include:

- generated migrations;
- generated manifests;
- checksums;
- baseline updates;
- release artifacts;
- export completeness.

The same generator should not be the only validator when practical.

## 63.30 CI secrets

CI should use no production secrets for ordinary pull-request validation.

Privileged workflows should:

- be isolated;
- require protected branches or environments;
- use least-privileged tokens;
- avoid untrusted contributions;
- record approval.

## 63.31 Artifacts

CI artifacts may include:

- test reports;
- validation reports;
- coverage matrices;
- screenshots;
- accessibility reports;
- pack files;
- checksums;
- migration receipts;
- replay bundles;
- performance results.

Artifacts should identify commit, workflow, and version.

## 63.32 Failure triage

When CI fails:

1. inspect exact failing job and step;
2. retrieve logs or artifact;
3. reproduce locally when practical;
4. identify root cause;
5. repair code, test, fixture, migration, or workflow;
6. rerun smallest relevant test;
7. rerun required suite;
8. preserve evidence;
9. continue automatically unless an owner-only decision is reached.

## 63.33 Flaky tests

A flaky test should not be ignored.

The team should:

- reproduce;
- identify timing or isolation cause;
- stabilize;
- quarantine only with explicit tracking;
- prevent quarantined tests from being treated as passing evidence for the affected gate.

## 63.34 Baseline updates

A baseline update should require:

- explained behavioral change;
- reviewed diff;
- compatibility impact;
- approval;
- old baseline retention;
- new fingerprint.

## 63.35 Coverage

Code coverage may assist review but must not become the sole quality measure.

The project also needs:

- domain coverage;
- permission coverage;
- source coverage;
- scenario coverage;
- migration coverage;
- error and recovery coverage.

## 63.36 Pull-request evidence

A completed repository item should provide, as applicable:

- implementation files;
- tests;
- CI;
- documentation;
- pull request;
- review;
- merge commit or squash commit;
- updated current-state record.

## 63.37 Merge truth

A pull request being open, approved, or green does not prove it is merged.

The final evidence should confirm the target branch contains the change.

## 63.38 Acceptance gates

The Phase 9 program defines eight acceptance gates:

- AG-01 Repository safety;
- AG-02 Provider-neutral boundaries;
- AG-03 Data foundation;
- AG-04 Identity and entitlements;
- AG-05 Authoritative sessions;
- AG-06 Operations and exit;
- AG-07 Two-device alpha;
- AG-08 Owner release decision.

Each gate requires its defined criteria and evidence.

## 63.39 Current verified boundary

Repository evidence records:

- P9-06-001 through P9-06-007 complete and merged;
- Acceptance Gate AG-01 complete;
- provider-neutral foundations through realtime and authoritative-session service ports;
- P9-06-008 as the next executable task under the active roadmap.

Later acceptance gates and backlog items remain incomplete unless newer repository evidence proves otherwise.

## 63.40 Controlling references

- P9-06 implementation backlog and acceptance gates
- active Application Implementation Roadmap
- Golden Test Corpus and Balance Harness
- Stage A batch requirements
- repository workflows, contract tests, and merged PR evidence
- canonical schema, pack, migration, security, and recovery architecture

**Status:** Canonical testing and CI architecture. Existing validated corpus and early Phase 9 gates are complete; later gates remain future work.

---

# 64. Deployment and Platform Boundaries

## 64.1 Purpose

Define the environments, release boundaries, deployment responsibilities, platform adapters, configuration rules, and owner gates that separate local development from previews, internal alpha, production, public launch, and platform-specific distribution.

## 64.2 Deployment principle

A build artifact, preview, simulator run, or successful CI workflow is not a production deployment.

Each environment has its own:

- purpose;
- data;
- credentials;
- configuration;
- access;
- retention;
- observability;
- cost;
- approval.

## 64.3 Environment classes

The architecture should distinguish:

- local development;
- automated test;
- pull-request or branch preview;
- internal integration;
- internal alpha;
- staging;
- production;
- platform packaging or certification environment.

Not every environment must exist immediately.

## 64.4 Local development

Local development should:

- use local or test adapters;
- require no production credentials;
- use deterministic fixtures;
- support reset;
- prevent accidental production access;
- provide reproducible startup and test commands.

## 64.5 Automated test

Automated test environments should:

- be ephemeral or isolated;
- use synthetic data;
- apply migrations from clean state;
- run contract and integration tests;
- produce evidence;
- remove or expire resources.

## 64.6 Preview environments

A preview may support:

- UI interaction review;
- branch testing;
- owner review;
- integration verification.

A preview should clearly identify:

- commit or branch;
- environment;
- test data;
- limitations;
- access policy;
- expiry.

## 64.7 Internal integration environment

An integration environment may combine real adapters or realistic substitutes before internal alpha.

It should support:

- cross-module validation;
- migrations;
- realtime;
- backup rehearsal;
- observability;
- permission tests.

## 64.8 Internal alpha

Internal alpha requires:

- verified core workflows;
- controlled testers;
- real or production-like service integration;
- tested recovery;
- security review appropriate to scope;
- accessible primary workflows;
- known risks;
- owner approval.

The current implementation authorization does not itself authorize internal-alpha release.

## 64.9 Staging

A staging environment should approximate production where practical.

It may include:

- production-like configuration;
- migration rehearsal;
- deployment rehearsal;
- monitoring;
- backup and restore;
- load testing;
- release candidate.

Staging is not required until the release program reaches that need.

## 64.10 Production

Production is the live environment trusted for user data and public or approved private use.

Production requires separate owner authorization and completed release gates.

No current planning or repository implementation should be interpreted as production approval.

## 64.11 Platform categories

Potential platforms include:

- responsive web;
- installable web application;
- desktop wrapper;
- iOS;
- iPadOS;
- other future platforms.

Shared domain and service contracts should remain platform-neutral.

## 64.12 Web platform

The web application should provide the primary cross-device experience unless a later decision changes the implementation direction.

It should support:

- modern browsers;
- responsive layouts;
- keyboard and touch;
- offline or reconnect behavior where implemented;
- secure session handling;
- provider-neutral APIs.

## 64.13 Native wrappers

A native wrapper may provide:

- installable shell;
- local file access;
- platform notifications;
- secure storage;
- device integration;
- app-store packaging.

The wrapper must not fork the canonical game logic into a separate implementation.

## 64.14 Platform adapter boundary

Platform-specific code should remain inside adapters or thin integration layers.

Examples include:

- secure credential storage;
- file picker;
- notifications;
- camera or media selection;
- share sheet;
- background behavior;
- platform lifecycle;
- store receipts.

## 64.15 Configuration by environment

Each environment should define validated configuration for:

- adapter selection;
- service URLs;
- feature flags;
- logging;
- data scope;
- content packs;
- AI features;
- limits;
- build identity.

## 64.16 Secrets by environment

Secrets must be isolated by environment.

A local or preview environment must not receive production credentials unless a specific owner-approved workflow requires it.

## 64.17 Build identity

Every build should identify:

- application version;
- commit;
- build time where needed;
- environment;
- schema compatibility;
- pack compatibility;
- feature profile.

## 64.18 Release artifact

A release artifact should be reproducible or traceable to:

- source commit;
- dependency lock;
- build workflow;
- tests;
- checksums;
- signatures or attestations where later required;
- release notes.

## 64.19 Database deployment

A deployment that includes database changes should:

- inspect current version;
- validate migration plan;
- verify backup;
- use expand–migrate–contract where appropriate;
- apply;
- verify;
- monitor;
- support forward repair or rollback.

## 64.20 Application compatibility

Deployment must consider compatibility among:

- client version;
- API version;
- database schema;
- event schema;
- pack versions;
- canonical object schema;
- realtime protocol;
- export contract.

## 64.21 Rolling and staged deployment

Future hosted deployment may use:

- rolling;
- blue-green;
- canary;
- staged cohort;
- maintenance window.

The strategy should match actual scale and cost rather than adding unnecessary complexity.

## 64.22 Feature release

Feature flags may separate deployment from activation.

Activation still requires:

- permissions;
- data readiness;
- migration;
- owner or release approval where applicable;
- monitoring;
- rollback.

## 64.23 Rollback

Rollback must distinguish:

- application binary rollback;
- configuration rollback;
- feature deactivation;
- database forward repair;
- pack rollback;
- content withdrawal.

A database rollback may be unsafe after accepted user mutations. Forward repair is often preferable.

## 64.24 Deployment health

Post-deployment validation should check:

- health;
- readiness;
- migrations;
- authentication;
- authorization;
- content registry;
- session command;
- realtime;
- search;
- backup;
- critical UI route;
- observability.

## 64.25 Release monitoring

A release should monitor:

- error rate;
- latency;
- authorization denial anomalies;
- session failures;
- reconnect;
- migration errors;
- cost;
- storage growth;
- security events.

## 64.26 Deployment records

A deployment record should identify:

- environment;
- version;
- commit;
- actor;
- approval;
- workflow;
- migrations;
- configuration fingerprint;
- result;
- rollback or repair;
- timestamp.

## 64.27 Data separation

Production, staging, preview, and local data must remain separated.

Copying production data into lower environments requires explicit privacy-safe policy and sanitization.

## 64.28 Test accounts

Nonproduction environments should use synthetic or approved test accounts.

Production identities and credentials must not be embedded in fixtures.

## 64.29 Domain and network boundaries

Future hosted environments should define:

- public endpoints;
- private services;
- database access;
- storage access;
- administrative access;
- firewall or network policy;
- TLS;
- callback URLs.

## 64.30 Dependency deployment

Provider SDK or infrastructure updates should be reviewed for:

- compatibility;
- security;
- cost;
- lock-in;
- migration;
- rollback.

## 64.31 Media deployment

Media release should preserve:

- asset hashes;
- rights;
- variants;
- cache invalidation;
- provider-exit references;
- visibility.

## 64.32 Content deployment

Content-pack release may be independent from application deployment where contracts permit.

Content release still requires:

- pack validation;
- compatibility;
- migration;
- ownership;
- release status;
- rollback or withdrawal plan.

## 64.33 AI deployment

An AI provider or model change should be treated as a controlled adapter or feature change.

Review should include:

- capability;
- output quality;
- permissions;
- privacy;
- cost;
- context limits;
- failure behavior;
- fallback.

## 64.34 Platform certification

App-store or platform certification may require:

- signing;
- provisioning;
- privacy declarations;
- entitlements;
- screenshots;
- packaging;
- review compliance;
- device testing.

Those tasks belong to the later platform track and do not authorize public distribution.

## 64.35 Borrowed Mac boundary

The Mac-dependent Apple track is intentionally bounded.

The borrowed Mac is for one-time Apple-only work that cannot be completed elsewhere, such as:

- build;
- signing;
- simulator or device validation;
- provisioning;
- packaging;
- certification-related checks.

The machine is not the primary development environment, and project material must be removable afterward.

Detailed Apple execution belongs to Chapter 79.

## 64.36 Release channels

Future release channels may include:

- internal developer;
- owner review;
- internal alpha;
- closed alpha;
- beta;
- production;
- app-store review.

Each channel requires explicit criteria and authority.

## 64.37 Public release gate

Public release requires a formal program covering:

- security;
- privacy;
- legal;
- content rights;
- moderation where applicable;
- billing where applicable;
- support;
- backup;
- recovery;
- performance;
- accessibility;
- rollback;
- owner approval.

## 64.38 Spending and provider gate

Deployment may create recurring cost or vendor commitments.

No automation may:

- create paid accounts;
- upgrade plans;
- bind production domains;
- issue production certificates;
- accept marketplace agreements;
- publish to app stores;

without the required owner gate.

## 64.39 CI/CD boundary

Continuous integration may run automatically.

Continuous deployment to production is not authorized by default.

Protected environments should require explicit approval.

## 64.40 Current verified boundary

The active implementation program permits local/provider-neutral repository work, tests, and CI.

It explicitly does not authorize:

- paid services;
- production deployment;
- public release;
- production credentials;
- irreversible vendor coupling.

The UI implementation program is owner approved but remains planned and repository-verification dependent.

## 64.41 Controlling references

- active Application Implementation Roadmap
- P9-04 architecture contract
- P9-05 bounded spike and cost guardrails
- P9-06 acceptance gates
- Stage A UI Implementation Program
- WP-011 bounded Apple spike package
- local-only development and secrets-isolation policies

**Status:** Canonical deployment boundary. Production, internal-alpha release, public distribution, paid services, and platform publication remain owner-gated.

---

# Tranche 6 Integration Review

## T6.1 Coverage

Volume VI now consolidates:

- system context;
- technical direction;
- provider-neutral ports;
- identity;
- authorization;
- entitlements;
- persistence;
- migrations;
- realtime;
- authoritative sessions;
- backup;
- restore;
- provider exit;
- security;
- privacy;
- secrets;
- observability;
- performance;
- cost;
- testing;
- CI;
- deployment;
- platform boundaries.

## T6.2 Provider-neutral invariant

Domain services depend on Multiversal contracts.

Provider-specific SDKs, IDs, errors, queries, channels, and storage URLs remain inside adapters.

## T6.3 Authority invariant

The server or trusted authoritative service controls:

- identity mapping;
- authorization;
- entitlement decisions;
- accepted state transitions;
- hidden information;
- session commands;
- checkpoints;
- audit.

Clients submit commands and render authorized projections.

## T6.4 Persistence invariant

Accepted state must be:

- transactional;
- attributable;
- versioned;
- idempotent where required;
- recoverable;
- exportable.

Caches, indexes, and realtime messages are derived.

## T6.5 Security invariant

Security requires:

- least privilege;
- default deny;
- secret isolation;
- provider-neutral identity;
- field- and query-level permission safety;
- protected logs;
- secure backups and exports;
- incident and recovery capability.

## T6.6 Recovery invariant

The project must be able to:

- verify backups;
- restore;
- recover sessions;
- preserve stable IDs;
- preserve pack and schema versions;
- rebuild derived indexes;
- export to provider-neutral formats.

## T6.7 Evidence invariant

Technical completion requires:

- repository files;
- tests;
- CI;
- pull request;
- merge evidence;
- updated governance.

A design chapter does not prove implementation.

## T6.8 Cost invariant

The bounded internal-alpha architecture targets **$0–$25 per month** and requires owner review above **$35 per month**.

These guardrails do not authorize spending.

## T6.9 Current verified implementation

Verified completed and merged work remains:

- P9-06-001 repository baseline;
- P9-06-002 local-only development environment;
- P9-06-003 secrets and environment isolation;
- P9-06-004 identity service port;
- P9-06-005 entitlement service port;
- P9-06-006 persistence and migration ports;
- P9-06-007 realtime and authoritative-session ports.

The active next task remains P9-06-008 under the newer roadmap.

## T6.10 Remaining boundaries

Volume VI does not claim completion of:

- concrete production provider adapters;
- full database schema;
- complete identity and entitlement implementations;
- complete authoritative command handler;
- hosted realtime;
- backup and restore ports;
- provider-exit rehearsal;
- full observability;
- two-device alpha acceptance;
- internal-alpha release;
- staging;
- production;
- public launch.

## T6.11 Tranche status

Volume VI is complete at the technical-architecture level.

Implementation continues through the bounded Phase 9 backlog and later application programs.

**Tranche 6 status:** Complete — canonical technical architecture consolidated.


# Volume VII — AI Development Operations

# 65. AI Team Structure

## 65.1 Purpose

Define the durable organizational functions used to plan, implement, review, validate, release, document, and recover Multiversal work through replaceable AI agents under the permanent authority of John Brandon Turner.

The structure is role-based rather than model-based. A role may be filled by different agents over time, but its mission, inputs, outputs, restrictions, review obligations, and handoff requirements remain stable.

## 65.2 Governing principle

AI agents are replaceable workers.

They are not:

- project owners;
- sources of canon;
- permanent authorities;
- irreplaceable repositories of project knowledge;
- substitutes for evidence;
- substitutes for required human decisions.

The human owner role is non-substitutable.

## 65.3 Validated operating baseline

The completed 8D-008B Agent Team Structure and Role Catalog validated:

- 14 permanent roles;
- one human owner role;
- thirteen replaceable AI roles;
- six organizational cells;
- eighteen capability definitions;
- four staffing modes;
- twenty separation-of-duties rules;
- forty paired compliant and violation cases;
- twelve authority domains covered by responsible leads and review relationships;
- 478 acceptance checks passed;
- zero acceptance failures.

This establishes the organizational model. It does not activate every role for every task.

## 65.4 Owner, Product, and Canon Authority

**Role type:** Human  
**Replaceability:** Non-replaceable  
**Holder:** John Brandon Turner

The owner provides controlling decisions for:

- canon;
- product scope;
- priorities;
- public claims;
- spending;
- production actions;
- release;
- material risk acceptance;
- reserved delegations;
- final dispute resolution.

The owner may delegate bounded authority through an explicit record but remains the project’s final authority.

No AI may impersonate the owner or infer owner approval from silence, tool access, past behavior, or a broad statement of trust.

## 65.5 Lead Orchestrator

The Lead Orchestrator converts approved goals into bounded work.

Responsibilities include:

- work intake;
- work-order formation;
- task decomposition;
- dependency ordering;
- role activation;
- context-loading coordination;
- review routing;
- blocker tracking;
- durable disposition;
- owner-facing decision preparation.

The Lead Orchestrator coordinates specialists but does not overrule valid specialist findings, approve owner-reserved work, or become the sole reviewer of its own material output.

## 65.6 Product Requirements Steward

The Product Requirements Steward translates owner-approved intent into traceable requirements.

Responsibilities include:

- preserving owner meaning;
- defining measurable outcomes;
- distinguishing requirement from suggestion;
- linking requirements to sources;
- identifying ambiguity;
- tracking scope;
- maintaining acceptance criteria.

This role may record priorities but may not invent owner priorities or silently broaden product scope.

## 65.7 System Architect

The System Architect maintains coherent technical boundaries.

Responsibilities include:

- architecture decisions;
- module boundaries;
- service contracts;
- provider neutrality;
- dependency impact;
- data-flow integrity;
- migration impact;
- technical-risk identification.

The role may recommend architecture but may not rewrite canon, product intent, or owner decisions to simplify implementation.

## 65.8 Canon and Rules Steward

The Canon and Rules Steward protects approved game meaning.

Responsibilities include:

- interpreting approved rules;
- identifying source conflicts;
- mapping canon into implementable contracts;
- detecting semantic invention;
- reviewing rules-runtime behavior;
- preserving variants and uncertainty;
- routing owner-reserved canon questions.

The role may interpret but cannot approve an owner-reserved semantic change.

## 65.9 Pack, Data, and Migration Engineer

This role implements governed content and persistence structures.

Responsibilities include:

- pack content;
- schemas;
- stable IDs;
- indexes;
- source mappings;
- migrations;
- save compatibility;
- installation and removal behavior;
- provider-exit data preparation.

The role must preserve provenance and cannot alter source meaning merely to satisfy a schema or migration.

## 65.10 Rules Runtime and Simulation Engineer

This role implements deterministic game execution.

Responsibilities include:

- action validation;
- resolution;
- effects;
- conditions;
- resources;
- event processing;
- deterministic randomness;
- replay;
- simulation adapters;
- runtime-state transitions.

The role implements approved canon and may not redefine it.

## 65.11 Backend and Integration Engineer

This role implements trusted application services.

Responsibilities include:

- APIs;
- domain services;
- persistence adapters;
- queues;
- identity and entitlement adapters;
- realtime integration;
- storage integration;
- background operations;
- external-service boundaries.

The role must remain within approved architecture and security boundaries.

## 65.12 Frontend and Interaction Engineer

This role implements the visible application.

Responsibilities include:

- responsive interfaces;
- interaction flows;
- object browsing;
- character and campaign workspaces;
- live-session controls;
- loading and recovery states;
- accessible component use;
- client-side integration.

The role may not create hidden mechanics, permissions, or canon through interface behavior.

## 65.13 UX and Accessibility Reviewer

This role independently reviews human-facing workflows.

Responsibilities include:

- cognitive load;
- navigation clarity;
- task completion;
- keyboard use;
- touch;
- assistive technology;
- responsive behavior;
- language clarity;
- error recovery.

Automated or heuristic review may identify issues but cannot be represented as completed human validation.

## 65.14 QA, Test, and Balance Engineer

This role owns independent quality evidence.

Responsibilities include:

- deterministic tests;
- golden baselines;
- regression enforcement;
- test design;
- balance-harness operation;
- defect classification;
- failure retention;
- release evidence review.

The role may not alter expected outputs merely to make a failing test pass.

## 65.15 Security, Privacy, and Dependency Reviewer

This role independently reviews risk.

Responsibilities include:

- threats;
- identity;
- authorization;
- hidden information;
- privacy;
- secrets;
- dependencies;
- licensing;
- vendors;
- supply-chain risk;
- incident concerns.

The role recommends treatment but may not accept material owner risk.

## 65.16 Release and DevOps Engineer

This role prepares reproducible release and operating evidence.

Responsibilities include:

- CI;
- builds;
- artifacts;
- environments;
- deployment plans;
- migration plans;
- rollback;
- operational runbooks;
- release receipts;
- platform packaging.

The role prepares but does not authorize production action or public release.

## 65.17 Documentation, Provenance, and Handoff Steward

This role preserves project continuity.

Responsibilities include:

- source references;
- decision records;
- changed-artifact lists;
- evidence indexes;
- current-state updates;
- handoffs;
- recovery records;
- owner decision queues;
- agent replacement.

The role may clarify records but may not rewrite evidence to remove a failure or conflict.

## 65.18 Organizational cells

The validated model groups roles into six cells.

### Owner and Governance

Human authority, product intent, canon sovereignty, approval, and risk acceptance.

### Coordination and Requirements

Work intake, decomposition, dependency management, requirements traceability, and owner-facing clarification.

### Architecture and Canon

Technical boundaries, canonical interpretation, architecture integrity, and domain interfaces.

### Implementation, Data, and Runtime

Pack data, schemas, migrations, rules execution, simulation, backend services, and integrations.

### Experience

Frontend interaction, responsive behavior, usability, accessibility, and human-facing workflow quality.

### Assurance and Release

Testing, deterministic evidence, security, privacy, dependencies, CI, release engineering, documentation, provenance, and handoff.

## 65.19 Task-specific activation

Not every role is active for every work order.

Each task should identify:

- primary executor;
- material authors;
- independent reviewers;
- approvers;
- supporting roles;
- owner role;
- roles intentionally inactive.

Role activation should follow the work type, authority domains, risk, output, and review requirements.

## 65.20 Staffing mode: single agent, owner supervised

**Agent instances:** one

This mode is suitable for:

- planning;
- documentation;
- inventory;
- source inspection;
- small reversible A0 or A1 work;
- owner-supervised analysis.

One agent may wear multiple compatible hats but must declare them.

It cannot manufacture independent review. Material work blocks when a mandatory independent reviewer is unavailable.

## 65.21 Staffing mode: compact AI team

**Agent instances:** three to five

This mode is suitable for:

- early implementation;
- isolated features;
- pack tooling;
- bounded prototypes;
- narrow migrations.

Compatible implementation roles may be combined, but the material implementer, required independent reviewer, and release preparer must remain separated when the work requires independence.

## 65.22 Staffing mode: standard AI development team

**Agent instances:** six to nine  
**Recommended primary development mode**

This mode supports parallel:

- frontend;
- backend;
- data;
- runtime;
- architecture;
- assurance;
- release;
- documentation.

Most specialist functions are separately seated. Adjacent roles may combine only where self-review, security review, release, canon, and risk conflicts remain absent.

## 65.23 Staffing mode: expanded parallel team

**Agent instances:** ten to thirteen

This mode is suitable for:

- large migrations;
- multi-repository work;
- release candidates;
- parallel workstreams;
- incident response;
- broad platform programs.

Each AI role may be separately seated. Assurance reviewers remain independent from material authors.

## 65.24 Role combination

Role combination is task-specific.

An agent holding several compatible roles must declare the active hats in the work record.

A role combination is invalid when it allows an agent to:

- approve its own material work;
- become its own sole independent reviewer;
- accept owner risk;
- rewrite canon;
- alter a baseline to pass;
- authorize release;
- conceal a specialist conflict;
- bypass a mandatory reviewer.

## 65.25 Separation of duties

Permanent separation rules include:

- the owner cannot be substituted;
- material implementation requires independent review where governed;
- security-critical authors cannot be their sole security reviewer;
- release preparers cannot authorize release;
- Canon Stewards cannot approve owner-reserved semantic changes;
- QA cannot edit expected results merely to pass;
- orchestrators cannot overrule specialist findings;
- frontend work cannot invent permission behavior;
- UX automation cannot claim human validation;
- documentation cannot erase negative evidence;
- agent replacement requires a durable handoff.

## 65.26 Team-cell handoffs

A normal material workstream may flow through:

1. Owner or approved requirement source.
2. Lead Orchestrator.
3. Product Requirements Steward.
4. System Architect and Canon Steward as applicable.
5. Implementation roles.
6. QA and protected-domain reviewers.
7. Release and DevOps preparation where applicable.
8. Documentation and Handoff Steward.
9. Owner checkpoint where required.

The exact route depends on the work order.

## 65.27 Independent review

Independent review requires a distinct reviewing agent instance when material independence is required.

Declaring a second role inside the same agent does not create independent evidence.

A reviewer should receive:

- approved scope;
- exact changed artifacts;
- context receipt;
- tests;
- known failures;
- acceptance criteria;
- approval boundary.

## 65.28 Role startup packets

Each role has a startup packet defining:

- mission;
- authority boundary;
- required inputs;
- required outputs;
- capabilities;
- prohibited behavior;
- review relationships;
- startup checklist;
- handoff obligations.

A generic model prompt should not replace the role startup packet.

## 65.29 Agent identity

Model or agent identity may be recorded for operational evidence, but authority belongs to the role assignment and work order.

Changing the model does not change:

- owner authority;
- source hierarchy;
- approval state;
- work-order scope;
- required review;
- canon;
- accepted evidence.

## 65.30 Agent replacement

An active agent may be replaced when:

- unavailable;
- context is corrupted;
- behavior violates policy;
- capabilities are insufficient;
- cost or platform changes;
- work is transferred.

Replacement requires:

- work-state snapshot;
- evidence location index;
- open blockers;
- approvals;
- context digest;
- branch or worktree state;
- recipient acceptance.

## 65.31 Scaling the team

Team size should increase only when it provides real parallelism without creating coordination waste.

Useful reasons include:

- independent review;
- separate frontend and backend work;
- simultaneous migration and validation;
- cross-platform work;
- release preparation;
- incident response.

Adding agents without bounded ownership may increase conflict and credit use.

## 65.32 Human participation

Human review is required where the architecture calls for:

- owner decision;
- actual user validation;
- risk acceptance;
- commercial or legal decision;
- production credential use;
- platform agreement;
- public release;
- physical-device access unavailable to the AI environment.

Human involvement should be requested through a concise decision packet rather than by transferring the entire project burden to the owner.

## 65.33 Current activation boundary

The role structure and startup assets are complete and validated as an operating package.

That does not mean a persistent multi-agent team is currently running.

Agents are activated per work order, environment, available tooling, and authority.

## 65.34 Controlling references

- 8D-008A Operating Scope and Governance Basis
- 8D-008B Agent Team Structure and Role Catalog
- 8D-008C Authority, Approval, and Escalation Matrix
- role startup packets
- separation-of-duties catalog
- staffing-mode catalog
- P9-11 milestones and AI-team operating roadmap
- 8D-008J AI Development Team Operating Package

**Status:** Canonical and validated organizational structure.

---

# 66. Authority, Approval, and Stop Conditions

## 66.1 Purpose

Define which decisions AI agents may execute, record, recommend, review, approve, escalate, or stop, and preserve the owner’s reserved authority without forcing ordinary reversible work back to the owner unnecessarily.

## 66.2 Authority principle

Responsibility does not imply approval authority.

A role may be responsible for:

- producing work;
- reviewing work;
- recommending a decision;
- detecting risk;
- preparing release evidence;

without being allowed to approve the final action.

## 66.3 Permission types

The operating model separates permissions including:

- execute;
- recommend;
- review;
- approve;
- delegate;
- escalate;
- stop work.

Each role receives domain-specific permissions through the authority matrix.

## 66.4 Decision level A0: execute approved work

A0 permits an agent to perform an explicitly assigned reversible action exactly inside the approved work order.

A0 does not permit:

- material judgment outside scope;
- canon change;
- product-scope change;
- risk acceptance;
- spending;
- deployment;
- public claims.

Examples may include:

- run an approved validator;
- gather an identified artifact;
- update a generated index through an approved script;
- perform a defined file conversion;
- collect repository evidence.

## 66.5 Decision level A1: recorded implementation choice

A1 permits an agent to choose among approved reversible implementation options inside locked architecture.

The choice requires a decision record.

A1 may cover ordinary choices such as:

- local variable naming;
- internal file organization within approved boundaries;
- compatible implementation details;
- choosing an existing approved helper;
- repairing an ordinary test failure without changing expected behavior.

A1 may not alter owner decisions, canon, public claims, or product priorities.

## 66.6 Decision level A2: peer-reviewed material change

A2 applies to material changes affecting areas such as:

- cross-component behavior;
- schemas;
- migrations;
- tests;
- UI workflows;
- security;
- operations;
- dependencies;
- architecture;
- baselines.

A2 requires:

- independent review;
- applicable quality gates;
- retained review evidence;
- authorized A2 approval.

Owner approval is still required when an owner-reserved domain is affected.

## 66.7 Decision level A3: owner approval required

A3 applies when work affects a reserved owner power or closes an explicit owner decision.

Agents may:

- investigate;
- compare options;
- recommend;
- prepare evidence;
- draft implementation or release plans.

Agents may not commit or represent owner approval.

## 66.8 Decision level A4: prohibited

A4 actions violate a non-negotiable boundary.

They cannot be approved by:

- an agent;
- a reviewer;
- the orchestrator;
- delegated authority;
- emergency language;
- the owner.

The required response is:

1. stop the affected action;
2. retain evidence;
3. record the prohibition;
4. escalate;
5. do not create an executable plan for the prohibited action.

## 66.9 Risk classes

Work orders also classify risk from low to highest governed risk.

Risk and decision level must agree.

A low decision level cannot be used to disguise a high-risk operation.

## 66.10 Authority domains

Authority domains include areas such as:

- canon;
- product scope;
- architecture;
- data and stable identity;
- rules runtime;
- experience;
- security and privacy;
- dependencies and licensing;
- vendors and cost;
- release;
- production;
- public claims.

The exact catalog remains machine-governed.

## 66.11 Owner-reserved powers

Owner-reserved powers include, as applicable:

- canon approval;
- product-scope decisions;
- priority decisions;
- public claims;
- material risk acceptance;
- spending;
- paid-provider enrollment;
- production credentials;
- internal-alpha release;
- public release;
- irreversible vendor coupling.

No agent may infer permission in these domains.

## 66.12 Approval binding

Every A2 or A3 approval must bind to the exact approved target.

The binding should include:

- work-order ID and version;
- requested action;
- scope;
- artifact or target digest;
- named executor;
- environment;
- conditions;
- expiration or single-use rule;
- approving authority.

## 66.13 Material change invalidation

An approval becomes invalid when a material change affects:

- scope;
- artifact digest;
- requested action;
- executor;
- environment;
- risk;
- cost;
- dependency;
- test result;
- rollback;
- security finding;
- owner conditions.

The work must pause and obtain new approval.

## 66.14 Owner approval procedure

A valid owner request should:

1. freeze the exact decision brief;
2. state the requested action and scope;
3. attach controlling sources;
4. attach specialist reviews;
5. attach quality-gate evidence;
6. state consequences;
7. state rollback or reversibility;
8. identify artifact digest, executor, and environment;
9. state expiration or single-use condition;
10. request approve, reject, revise, or hold.

Silence is not approval.

## 66.15 Decision packet design

Owner decision packets should minimize owner burden.

A packet should lead with:

- exact question;
- recommended option;
- why;
- alternatives;
- irreversible consequences;
- cost;
- security or privacy risk;
- what proceeds after approval.

The full evidence remains attached or linked.

## 66.16 Approval states

The validated authority package defines nine approval states and fourteen allowed transitions.

An approval record should move only through allowed states.

A task may not treat:

- requested;
- under review;
- conditionally recommended;
- expired;
- revoked;

as equivalent to approved.

## 66.17 Rejection

A rejection should preserve:

- requested action;
- evidence;
- reason;
- rejected version;
- possible revision path;
- final authority;
- time.

Rejection does not authorize a slightly altered version automatically.

## 66.18 Requested changes

When the owner or reviewer requests changes:

- the work order or decision packet is versioned;
- affected context is refreshed;
- affected digests are recalculated;
- prior approval remains superseded or invalid;
- the revised request is resubmitted.

## 66.19 Delegation

Owner delegation must be:

- explicit;
- versioned;
- named;
- scope-limited;
- time-limited or single-use;
- revocable;
- no broader than the owner’s own authority.

Silence, role assignment, access to tools, or previous behavior does not create delegation.

## 66.20 Subdelegation

Subdelegation is prohibited unless the owner’s delegation record explicitly permits it.

Even when permitted, it cannot create authority beyond the original scope.

## 66.21 Agent task delegation

An AI role may delegate work only when:

- the work is already permitted;
- the recipient role is authorized;
- scope remains bounded;
- review requirements remain;
- approval authority is not transferred;
- a durable handoff occurs;
- the recipient accepts.

Task delegation expires with closure, revocation, or material change.

## 66.22 Revocation

Authority or delegation may be revoked.

Revocation should identify:

- record;
- scope;
- effective time;
- affected work;
- containment;
- required reauthorization;
- owner or authorized revoker.

Affected actions must stop promptly.

## 66.23 Escalation

Escalation is required when:

- authority is missing;
- sources conflict materially;
- required context is unavailable;
- an owner-reserved decision is reached;
- a mandatory reviewer is unavailable;
- a quality gate fails;
- risk exceeds authority;
- cost or provider commitment changes;
- security or privacy concerns arise;
- work drifts from scope;
- an A4 request appears.

## 66.24 Escalation record

An escalation should contain:

- trigger;
- affected scope;
- evidence;
- actions already taken;
- containment;
- options;
- recommended path;
- required authority;
- resume condition;
- urgency.

## 66.25 Stop-work principle

Stop-work is a reversible safety control.

It is not:

- a product decision;
- a canon decision;
- risk acceptance;
- release authorization;
- permanent cancellation.

The hold remains until the required authority records a disposition and applicable gates pass.

## 66.26 Universal A4 stop authority

Every active role must stop an A4 action.

No override is available.

## 66.27 Specialist stop authority

Specialist roles may stop affected work in protected domains.

### Canon conflict

The Canon and Rules Steward may hold semantic implementation when authoritative sources conflict or invention risk exists.

### Architecture integrity

The System Architect may hold merge or migration when a material architecture contract is violated or a destructive design lacks recovery.

### Quality gate

The QA, Test, and Balance Engineer may block merge or release when required deterministic evidence fails.

### Security, privacy, and dependency

The Security Reviewer may stop work involving material threats, secrets, licensing, identity, privacy, or supply-chain concerns.

### Release safety

The Release and DevOps Engineer may block release when build, rollback, backup, environment, or release evidence is missing.

### Provenance loss

The Documentation and Handoff Steward may hold disposition or release when source identity, evidence, decision records, or handoff are missing.

### Owner hold

The owner may stop named work, revoke delegation, or reject a reserved decision.

## 66.28 Stop-work record

A stop-work record should identify:

- trigger;
- protected domain;
- affected work;
- evidence;
- immediate containment;
- required authority;
- current state;
- resume conditions;
- record author;
- time.

## 66.29 Resume

Work may resume only when:

- the blocker has a recorded disposition;
- required authority acts;
- work order is updated when necessary;
- context is refreshed;
- approval is renewed where invalidated;
- applicable gates pass;
- recipient roles acknowledge the resumed state.

## 66.30 Owner risk acceptance

The owner may accept a bounded A3 risk.

The record should state:

- identified risk;
- scope;
- evidence;
- mitigation;
- residual risk;
- time limit;
- review point;
- rollback or containment;
- accepted authority.

The owner cannot authorize A4.

## 66.31 Independent review

A material author cannot be the sole independent reviewer.

Multi-role operation must declare hats and use a separate reviewing agent instance when independence is required.

## 66.32 Mandatory reviewer unavailable

When a mandatory independent reviewer is unavailable, the work should:

- block;
- reduce scope to compatible A0 or A1 work;
- be reassigned;
- activate another qualified reviewer;
- be deferred.

It must not invent independence.

## 66.33 Approval and tool permissions

Technical tool access does not grant governance authority.

An agent capable of:

- writing files;
- merging code;
- deploying;
- spending;
- using credentials;

may still be prohibited from doing so.

Governance controls whether the capability may be used.

## 66.34 Approval and repository state

An owner approval record does not prove execution.

Execution still requires:

- exact approved digest;
- correct branch and environment;
- tests;
- review;
- merge or release evidence;
- final receipt.

## 66.35 Unsupported claims

Agents must not claim:

- canon approval;
- balance proof;
- human testing;
- accessibility conformance;
- production readiness;
- deployment;
- merge;
- public release;

without the required evidence and authority.

## 66.36 Validated authority baseline

The completed 8D-008C release validated:

- fourteen role authority profiles;
- twelve authority domains;
- 168 role-domain permission assignments;
- seven permission types;
- nine approval states;
- fourteen allowed approval transitions;
- twenty-two approval routes;
- all ten owner-reserved powers;
- twelve delegation rules;
- fourteen escalation routes;
- eight stop-work authorities;
- twenty separation-rule enforcement bindings;
- sixty paired authority cases;
- 845 acceptance checks passed;
- zero failed.

## 66.37 Current project application

The current implementation authorization permits bounded repository implementation through P9-06-023.

It does not authorize:

- paid services;
- production deployment;
- public release;
- production credentials;
- spending beyond a separate gate;
- irreversible provider coupling.

The AI team should continue automatically through ordinary failures and stop only at genuine owner-only gates or prohibited boundaries.

## 66.38 Controlling references

- 8D-008A Decision Levels and Owner Reserved Powers
- 8D-008B Separation of Duties
- 8D-008C Authority, Approval, Delegation, Escalation, and Stop Work
- active Application Implementation Roadmap
- P9-06 owner authorization
- role authority addenda
- approval and escalation schemas

**Status:** Canonical and validated governance architecture.

---

# 67. Context Loading and Credit Optimization

## 67.1 Purpose

Define how an AI agent loads the minimum complete, authoritative, fresh, and task-relevant project context while preserving source identity, exact evidence, known conflicts, and owner authority.

This chapter also defines how to reduce repeated model-credit, token, tool-call, and retrieval cost without under-contextualizing material work.

## 67.2 Context principle

Context is assembled from the work order.

It is not assembled from:

- a generic prompt;
- filename similarity;
- an unqualified “latest” file;
- the largest available archive;
- model memory;
- an old conversation summary alone.

## 67.3 Source-of-truth registry

The source registry records:

- stable source ID;
- authority tier;
- status;
- scope;
- locator;
- version;
- digest;
- freshness policy;
- source group;
- relationships;
- availability;
- conflict status.

Authority and availability are separate.

An authoritative source may be unavailable. An easily accessible historical document may be non-normative.

## 67.4 Stable source resolution

Sources must be resolved by:

- stable source ID;
- exact version;
- exact locator;
- exact digest;
- applicable scope.

Filename similarity is insufficient.

## 67.5 Authority eligibility

Authority is not a relevance score.

Before optional ranking, the resolver must enforce:

- source status;
- authority tier;
- scope;
- version;
- digest;
- owner record requirements;
- A4 eligibility;
- work-order binding.

An ineligible source cannot become eligible because it appears semantically relevant.

## 67.6 Governance core

Every material task loads the governance core.

The governance core should include the rules needed to answer:

- who may act;
- what is prohibited;
- what approval is required;
- what evidence is required;
- what happens on conflict;
- what must be preserved.

## 67.7 Owner records

Owner records must be loaded when:

- the decision level is A3;
- an owner ruling controls the affected scope;
- delegation is claimed;
- spending or providers are involved;
- production or release is involved;
- an owner hold or exception applies.

Dynamic owner records should be refreshed at each A3 decision point.

## 67.8 Work-type profiles

The validated context system defines sixteen work types and sixteen context profiles.

Representative work types include:

- feature implementation;
- bug repair;
- workflow UI change;
- rules runtime change;
- schema or contract change;
- structured content change;
- source reconciliation;
- stable-ID migration;
- test-baseline change;
- security or dependency change;
- documentation and provenance;
- architecture research;
- balance evaluation;
- incident rollback;
- release deployment;
- canon change.

Each profile defines required source groups and loading rules.

## 67.9 Role baseline

The active role also contributes required context.

A Frontend Engineer, Canon Steward, QA Reviewer, Security Reviewer, and Release Engineer do not receive identical baseline context.

Role context supplements the work-type profile but does not override authority.

## 67.10 Authority-domain binding

Affected authority domains add required source groups.

For example, a vendor or cost decision may require:

- governance core;
- owner records;
- security and release sources;
- architecture and data sources.

## 67.11 Context manifest

A context manifest is a sealed statement of exactly which sources the work may rely on.

It records:

- work order;
- work type;
- active role;
- decision level;
- authority domains;
- source snapshots;
- selected sources;
- exclusions;
- conflicts;
- approvals;
- load state;
- digest.

## 67.12 Manifest invalidation

A manifest becomes invalid when material changes affect:

- work-order scope;
- role;
- decision level;
- authority domain;
- source identity;
- source version;
- digest;
- source status;
- conflict disposition;
- approval binding.

Work pauses until context is refreshed.

## 67.13 Context load receipt

Every material context load should produce a receipt covering:

- request;
- selected sources;
- source digests;
- exact fragments;
- structured queries;
- cache results;
- failures;
- exclusions;
- conflicts;
- resolver version;
- bundle digest;
- final status.

The receipt makes context reproducible and reviewable.

## 67.14 Required loading sequence

The validated retrieval protocol uses twelve deterministic stages:

1. Normalize the work order and requested output.
2. Bind work type, role, decision level, and authority domains.
3. Expand all required source groups.
4. Apply authority, status, scope, approval, and A4 gates.
5. Resolve stable IDs, versions, locators, and digests.
6. Verify source snapshots.
7. Query structured sources with explicit fields and filters.
8. Rank only eligible optional context.
9. Choose an approved load mode.
10. Apply ordered compaction.
11. detect and route conflicts.
12. Seal the context bundle and receipt.

## 67.15 Retrieval request

A retrieval request should identify:

- work order;
- requested output;
- stable IDs;
- target files;
- affected domains;
- required fields;
- acceptance criteria;
- role;
- decision level;
- maximum budget profile;
- known conflicts.

## 67.16 Required versus optional context

Required context is selected by governance, work type, authority domain, role, approvals, and exact targets.

Optional context may improve understanding but cannot:

- displace required context;
- override authority;
- justify a prohibited action;
- conceal a known conflict;
- become canonical merely by ranking highly.

## 67.17 Exact identifiers before semantic search

When a stable ID, path, schema, work-order ID, PR, commit, or pack ID is known, exact retrieval takes priority.

Semantic search is useful for discovering candidates, not for replacing exact source resolution.

## 67.18 Structured query discipline

Structured queries should declare:

- source;
- fields;
- filters;
- ordering;
- limit;
- result IDs;
- result-set digest.

The receipt should allow the same query result to be reproduced or explained.

## 67.19 Load modes

The context system supports eight governed load modes.

Modes may include:

- exact full artifact;
- exact fragment;
- structured query result;
- verified metadata;
- derived summary;
- archive index;
- exact archive excerpt;
- excluded or unavailable record.

The exact catalog remains machine-governed.

## 67.20 Exact context

The following normally remain exact:

- schemas;
- contracts;
- approvals;
- owner records;
- manifests;
- tests;
- expected outputs;
- baselines;
- seeds;
- replay evidence;
- migration mappings;
- exact repository evidence.

These should not be replaced by a prose summary when exact structure matters.

## 67.21 Exact fragments

Large directives or canon sources may be loaded as exact fragments when:

- the fragment boundary is reproducible;
- the full-source locator is retained;
- surrounding context is sufficient;
- no omitted section controls the decision.

## 67.22 Derived summaries

A derived summary may assist comprehension.

It must preserve:

- source ID;
- source digest;
- derivation digest;
- summary version;
- limitations;
- reopenable locator.

A summary is not the controlling source.

## 67.23 Citation requirement

Reusable project claims should retain:

- source ID;
- source digest;
- exact fragment or structured-query evidence;
- result or record identity.

This allows another agent to reopen the evidence rather than relying on the prior agent’s memory.

## 67.24 Context budget measurement

The validated protocol measures active context in UTF-8 bytes rather than model-specific tokens.

Token estimates may be used operationally, but byte budgets provide stack-neutral reproducibility.

## 67.25 Budget profile: focused fix

Suitable for small A0 or A1 repair with narrow identifiers.

- exact bytes: 131,072;
- derived-summary bytes: 32,768;
- maximum selected sources: 24;
- minimum exact reserve: 65%;
- governance reserve: 20%.

## 67.26 Budget profile: standard work

Suitable for normal documentation, feature, or bounded implementation.

- exact bytes: 393,216;
- derived-summary bytes: 98,304;
- maximum selected sources: 48;
- minimum exact reserve: 55%;
- governance reserve: 15%.

## 67.27 Budget profile: material change

Suitable for A2 schema, runtime, workflow, security, or baseline changes.

- exact bytes: 1,048,576;
- derived-summary bytes: 262,144;
- maximum selected sources: 96;
- minimum exact reserve: 50%;
- governance reserve: 15%.

## 67.28 Budget profile: owner decision

Suitable for A3 owner decision packets.

- exact bytes: 1,572,864;
- derived-summary bytes: 393,216;
- maximum selected sources: 128;
- minimum exact reserve: 55%;
- governance reserve: 20%.

## 67.29 Budget profile: release audit

Suitable for release, migration, rollback, and full gate review.

- exact bytes: 4,194,304;
- derived-summary bytes: 524,288;
- maximum selected sources: 256;
- minimum exact reserve: 60%;
- governance reserve: 15%.

## 67.30 Budget profile: archive research

Suitable for historical research using indexes, exact excerpts, and summaries.

- exact bytes: 2,097,152;
- derived-summary bytes: 1,048,576;
- maximum selected sources: 320;
- minimum exact reserve: 25%;
- governance reserve: 10%.

The lower exact reserve reflects the use of archive indexes and derived research aids, not permission to summarize controlling current authority.

## 67.31 Compaction ladder

When the active context exceeds budget, apply these steps in order:

1. Remove digest-identical duplicates.
2. Drop redundant optional context.
3. Narrow optional artifacts to exact relevant sections.
4. Summarize eligible supporting context.
5. Reduce historical archives to indexes and exact excerpts.
6. Split the work order.
7. Block if required exact evidence still does not fit.

## 67.32 Required evidence cannot be evicted

Budget pressure is never permission to remove:

- governance core;
- controlling owner record;
- exact approval;
- schema;
- test baseline;
- source conflict;
- known failure;
- migration mapping;
- required security evidence.

## 67.33 Credit optimization principle

Credit optimization means eliminating repeated, low-value processing while preserving governing evidence.

It does not mean:

- guessing from memory;
- using summaries as canon;
- omitting conflicts;
- skipping tests;
- avoiding required web or repository verification;
- claiming completion from a plan.

## 67.34 Stable-context cache

Immutable bytes should be cached by digest.

A cached item may be reused when:

- stable source ID matches;
- digest matches;
- scope matches;
- authority remains valid;
- the task permits the load mode.

Filename or title alone is not a valid cache key.

## 67.35 Cache classes

The validated protocol distinguishes eight cache classes, including separate treatment for:

- immutable source bytes;
- mutable repository files;
- structured query results;
- derived summaries;
- archive indexes;
- dynamic owner records;
- failed resolutions;
- other governed context artifacts.

Each class has its own refresh behavior.

## 67.36 Refresh triggers

Refresh should occur when relevant changes affect:

- scope;
- work type;
- role;
- decision level;
- domain;
- source;
- approval;
- conflict;
- repository commit;
- branch;
- worktree;
- file state;
- quality gate;
- owner record.

## 67.37 Negative-result caching

A failed source resolution may be cached briefly to avoid repeated identical calls.

Negative cache entries should expire quickly because:

- files may appear;
- repository access may change;
- a branch may merge;
- a connector may recover.

## 67.38 Repository-aware loading

For repository work, context should bind to:

- repository;
- branch or worktree;
- commit;
- target files;
- open pull request where applicable;
- current CI state;
- current diff.

A branch change invalidates affected mutable context.

## 67.39 Archive-first indexing

Large archives should first be indexed by:

- path;
- size;
- type;
- package;
- likely domain;
- stable identifiers.

Only relevant files should then be extracted and loaded.

This avoids repeatedly injecting entire source archives.

## 67.40 Local extraction and scripting

When source archives are available locally, use deterministic tools for:

- listing;
- hashing;
- exact extraction;
- CSV filtering;
- schema parsing;
- line selection;
- duplicate detection;
- package inventory.

Model context should receive the relevant results and exact locators rather than raw unrelated archive contents.

## 67.41 Reference context tools

The 8D-008J package includes reference tools such as:

- `context_protocol.py`;
- `control_protocol.py`;
- `task_packet_protocol.py`;
- `workflow_protocol.py`;
- `continuity_protocol.py`.

These provide stack-neutral reference behavior and validation aids.

They are not independent governance authority and should not be mistaken for production services.

## 67.42 Batch tool use

Compatible retrieval and verification calls should be batched when this:

- reduces repeated startup cost;
- preserves source distinctions;
- does not exceed tool limits;
- does not mix unrelated tasks;
- keeps outputs inspectable.

## 67.43 Progressive loading

A task should load context progressively:

1. governance and work-order core;
2. exact target artifacts;
3. required domain sources;
4. current repository evidence;
5. optional supporting sources;
6. archive excerpts only when gaps remain.

## 67.44 Decision-focused retrieval

A decision packet should load only the evidence needed to distinguish the real options and consequences.

The owner should not be forced to reread the entire project for a bounded decision.

## 67.45 Reopenable context

A compact context bundle should retain locators for full sources.

Another agent should be able to reopen:

- exact file;
- commit;
- line range;
- archive member;
- source row;
- schema;
- receipt.

## 67.46 Partial availability

Work must block when any of the following affects required scope:

- unavailable authoritative source;
- digest mismatch;
- missing A3 owner record;
- incomplete structured result;
- unresolved material conflict;
- required exact context that cannot fit.

Optional or historical absence may produce a degraded bundle only when no controlling requirement is lost.

## 67.47 Conflict handling

A material conflict loads all relevant sides.

The resolver may apply an already-governed hierarchy rule.

It may not invent:

- a compromise;
- a hidden mechanic;
- a new owner ruling;
- a synthetic canonical statement.

## 67.48 Freshness

Freshness policy depends on source class.

Examples:

- immutable release pack: verify digest;
- repository file: refresh on branch, commit, or worktree change;
- dynamic current-state file: compare against newer repository evidence;
- owner decision: refresh at A3;
- web or provider information: verify current state when material.

## 67.49 Conversation summaries

A conversation or handoff summary is useful for continuity.

It is not automatically the source of truth.

Material claims should be checked against:

- repository;
- canonical package;
- owner decision;
- exact artifact;
- current validator evidence.

## 67.50 Context load states

A context request may be:

- incomplete;
- resolving;
- blocked;
- degraded;
- complete;
- invalidated;
- superseded.

Only a valid complete or explicitly allowed degraded receipt may support execution.

## 67.51 Context and independent review

A reviewer should receive sufficient independent context to verify the work.

The author’s summary alone is not adequate review input.

At minimum, the reviewer should receive:

- work order;
- exact change;
- controlling sources;
- tests;
- failures;
- approval boundary;
- context receipt.

## 67.52 Context and AI privacy

Context retrieval must enforce:

- identity;
- role;
- campaign;
- entitlement;
- visibility;
- provider policy;
- data minimization.

A credit-saving shared cache must not cross permission boundaries.

## 67.53 Validated context baseline

8D-008D validated:

- 35 registered sources;
- twelve source groups;
- 49 memberships;
- sixteen work types;
- sixteen context profiles;
- twelve domain bindings;
- fourteen role profiles;
- twenty context rules;
- sixty-four paired cases;
- four example manifests;
- 1,100 acceptance checks passed;
- zero failed.

8D-008E validated:

- ten retrieval intents;
- twelve retrieval stages;
- eight relevance dimensions totaling 100 points;
- eight load modes;
- ten content-form rules;
- six byte-budget profiles;
- seven compaction steps;
- eight cache classes;
- fourteen refresh triggers;
- ten partial-availability policies;
- twelve citation rules;
- twenty-four operating rules;
- eighty paired cases;
- seven materialized examples;
- 824 acceptance checks passed;
- zero failed.

## 67.54 Controlling references

- 8D-008D Context Manifest and Source-of-Truth Registry
- 8D-008E Context Loading and Retrieval Protocol
- source registry
- context profiles
- source groups
- role retrieval policies
- context budget model
- context loading reference tool
- 8D-008J startup and operating assets

**Status:** Canonical and validated context-loading architecture.

---

# 68. Work Orders and Bounded Execution

## 68.1 Purpose

Define how an approved goal becomes a versioned, executable, reviewable, and closable assignment with explicit scope, authority, context, tests, evidence, rollback, and handoff.

## 68.2 Work-order principle

A natural-language prompt, chat message, ticket title, branch name, or spoken instruction is not by itself an executable material work order.

It may begin intake.

Material execution begins only after the approved work is normalized into the required work-order and task-packet structure.

## 68.3 Work order versus task packet

### Work order

Defines the approved objective, scope, authority, roles, dependencies, acceptance, outputs, and boundaries.

### Task packet

The sealed execution envelope containing the work order and all subordinate records required by the work type.

A task packet cannot be assigned until the Definition of Ready passes.

## 68.4 Stable identity

Every work order should have:

- stable work-order ID;
- version;
- title;
- objective;
- created time;
- creating role;
- current status;
- canonical digest when sealed.

A material change creates a new version rather than overwriting approved history.

## 68.5 Objective

The objective should be specific and testable.

A valid objective states:

- what will change or be produced;
- for whom or what;
- inside which boundary;
- what evidence proves completion.

“Improve the app” is not a complete material objective.

## 68.6 Registered work type

Each work order selects a registered work type.

The work type determines:

- minimum decision level;
- required roles;
- required context;
- required records;
- required tests;
- protected-domain review;
- output expectations;
- quality gates.

## 68.7 Decision level

The work order records A0, A1, A2, A3, or A4.

The selected level cannot be lower than the work-type minimum.

A4 cannot become executable.

## 68.8 Risk class

The work order records a governed risk class.

Risk should consider:

- reversibility;
- data impact;
- canon impact;
- security;
- privacy;
- dependency;
- migration;
- release;
- cost;
- user impact.

## 68.9 Priority

Priority is explicit and owner- or roadmap-grounded.

Priority must not be inferred solely from:

- who asked most recently;
- file order;
- branch name;
- agent preference;
- easiest implementation.

## 68.10 Authority domains

The packet declares all affected authority domains.

This controls:

- source loading;
- protected reviewers;
- approval route;
- stop-work authority;
- owner decision requirements.

## 68.11 Target environment

The work order should identify the target environment, such as:

- documentation artifact;
- local repository;
- test environment;
- preview;
- internal integration;
- borrowed Mac worktree;
- owner decision packet.

A packet does not imply permission for production.

## 68.12 In-scope boundary

The work order must state what is included.

Useful scope statements identify:

- files;
- stable IDs;
- modules;
- schemas;
- behaviors;
- tests;
- environments;
- expected artifacts.

## 68.13 Out-of-scope boundary

The work order must state what is excluded.

Out-of-scope examples may include:

- production deployment;
- new provider selection;
- canon change;
- paid service;
- unrelated refactor;
- public release;
- user-data migration.

## 68.14 Affected identifiers and files

Known affected stable IDs and files should be listed.

When none are known, the packet should state that explicitly.

Discovery of new affected material may be a material-change trigger.

## 68.15 Assumptions

Assumptions should be:

- explicit;
- testable;
- attributable;
- revisited when evidence changes.

A hidden assumption cannot be used as approval.

## 68.16 Constraints

Constraints may include:

- no production credentials;
- no paid service;
- preserve provider neutrality;
- preserve stable IDs;
- no canon invention;
- exact source fidelity;
- borrowed-machine cleanup;
- required CI;
- no baseline manipulation.

## 68.17 Roles

The work order declares:

- one primary executor role;
- author roles;
- reviewer roles;
- approver roles;
- support roles;
- explicit owner role.

One agent may hold several compatible hats, but independence rules remain.

## 68.18 Context references

Every executable packet references:

- context request;
- context manifest;
- load receipt;
- bundle digest;
- relevant source citations;
- context status.

Blocked context blocks the task.

## 68.19 Dependencies

Dependencies must be explicit even when empty.

Dependency types may include:

- work-order dependency;
- artifact dependency;
- schema dependency;
- pack dependency;
- approval dependency;
- test dependency;
- environment dependency;
- reviewer dependency;
- tool dependency;
- provider dependency.

## 68.20 Acceptance criteria

Acceptance criteria should be:

- measurable;
- evidence-linked;
- pass or fail;
- explicit about blocking behavior;
- scoped to the objective.

An acceptance criterion should not be satisfied by a verbal claim alone.

## 68.21 Required records

The packet declares subordinate records such as:

- implementation plan;
- decision record;
- change record;
- test plan;
- test evidence;
- review request;
- review report;
- migration plan;
- rollback plan;
- release request;
- blocker record;
- handoff record;
- approval reference.

## 68.22 Required tests

Tests should be named before execution where practical.

They may include:

- exact commands;
- fixture IDs;
- contract tests;
- golden tests;
- schema validators;
- migration tests;
- UI tests;
- accessibility checks;
- CI workflows;
- restore drills.

## 68.23 Rollback

Material reversible work should declare a rollback or recovery plan.

The plan should state:

- what can be restored;
- required backup;
- rollback trigger;
- procedure;
- limitations;
- validation.

## 68.24 Output artifacts

Expected outputs should be declared by type.

Examples include:

- code;
- schema;
- pack;
- migration;
- test report;
- validation report;
- decision record;
- architecture record;
- release artifact;
- handoff;
- owner decision packet.

Final artifacts should carry checksums where required.

## 68.25 Handoff

Every transferred or closed material task requires a durable handoff.

The handoff should identify:

- completed work;
- current state;
- changed artifacts;
- tests;
- failures;
- decisions;
- approvals;
- blockers;
- branch or worktree;
- next actions;
- evidence locations.

## 68.26 Definition of Ready

The validated Definition of Ready contains twenty-eight blocking criteria.

They cover:

- identity;
- testable objective;
- registered work type;
- decision level;
- risk;
- authority domains;
- in-scope and out-of-scope boundaries;
- affected IDs and files;
- constraints;
- assumptions;
- executor;
- reviewers;
- approvers;
- separation;
- context request;
- context receipt;
- context bundle;
- dependencies;
- acceptance;
- required records;
- required tests;
- rollback;
- outputs;
- handoff;
- approval;
- no A4 action.

A packet that fails any required criterion is not ready.

## 68.27 Definition of Done

The validated Definition of Done contains thirty-two blocking criteria.

They cover:

- scope compliance;
- exact change record;
- stable-ID behavior;
- current context;
- valid approvals;
- resolved dependencies;
- implementation disposition;
- executed tests;
- mandatory quality gates;
- retained failures;
- unchanged baselines unless governed;
- complete independent review;
- security review;
- UX review;
- migration evidence;
- rollback evidence;
- release evidence;
- provenance;
- acceptance;
- unresolved risks;
- checksummed outputs;
- documentation;
- handoff;
- next actions;
- final status;
- final digest;
- retention;
- supported claims;
- no unapproved spending;
- no unapproved deployment;
- owner-only closure.

## 68.28 Task states

The validated standard defines eighteen task lifecycle states and twenty-eight permitted transitions.

Typical conceptual states include:

- draft;
- context pending;
- blocked;
- ready;
- assigned;
- executing;
- review;
- approval pending;
- testing;
- failed;
- superseded;
- completed;
- closed.

The exact catalog controls allowed transitions.

## 68.29 Ready packet seal

When ready, the task packet should be sealed with:

- packet version;
- work-order digest;
- context receipt digest;
- context bundle digest;
- approval target digest where required;
- readiness receipt.

Execution should verify the seal before material work.

## 68.30 Bounded execution

The executor performs only the approved scope.

During execution, the agent should:

1. verify current branch, worktree, files, and environment;
2. verify context and approval;
3. make the smallest coherent change;
4. preserve source and history;
5. run the nearest tests;
6. repair ordinary failures;
7. run required full gates;
8. record exact artifacts and evidence;
9. stop at material drift or owner gate;
10. prepare handoff or closure.

## 68.31 Ordinary implementation judgment

Inside A1 boundaries, the executor may resolve routine details without repeatedly asking the owner.

Examples include:

- fixing syntax;
- updating imports;
- selecting an existing helper;
- correcting a deterministic test setup;
- reformatting through approved tooling;
- repairing CI configuration consistent with the contract.

The decision should be recorded when material enough to affect future understanding.

## 68.32 Automatic failure recovery

When ordinary implementation or CI fails, the agent should:

- inspect the error;
- find the root cause;
- repair within scope;
- rerun the narrow check;
- rerun required gates;
- continue.

It should not stop merely because the first attempt failed.

## 68.33 Genuine stop conditions

Execution should stop when:

- A3 owner decision is reached;
- A4 action appears;
- paid service or spending is required;
- production credentials are required;
- deployment or public release is required;
- required source is unavailable;
- material source conflict remains;
- required reviewer is unavailable;
- scope drift is material;
- approval is invalid;
- destructive migration lacks recovery;
- security or privacy risk exceeds authority.

## 68.34 Material-change triggers

The validated standard defines sixteen material-change triggers.

Material changes may include:

- scope expansion;
- target-file expansion;
- stable-ID change;
- schema or contract change;
- migration change;
- risk change;
- dependency change;
- environment change;
- executor change;
- cost change;
- security finding;
- acceptance change;
- failed gate;
- artifact digest change after approval.

The packet is versioned and affected context, review, or approval is refreshed.

## 68.35 Scope drift

Scope drift should produce:

- detected difference;
- affected files or IDs;
- risk;
- whether the drift is necessary;
- revised packet or rejected expansion;
- approval route.

Agents must not normalize scope drift after the fact.

## 68.36 Approval and digest binding

A3 approval applies only to the exact target digest, named executor, environment, and validity window.

A revised implementation after approval may require reapproval.

## 68.37 Quality-gate binding

The locked 8D-007J release is a blocking gate for affected:

- implementation;
- schema;
- migration;
- rules runtime;
- test baseline;
- security and dependency;
- release work.

Failures remain retained.

Expected outputs may not be rewritten merely to pass.

## 68.38 Independent review packet

The reviewer should receive:

- work order;
- exact diff or artifacts;
- context receipt;
- acceptance criteria;
- tests and results;
- known failures;
- decisions;
- security, canon, UX, or migration concerns;
- approval boundary.

## 68.39 Evidence-first completion

A task may close only when evidence exists for:

- implementation;
- tests;
- review;
- approval;
- migration or rollback where required;
- checksums;
- acceptance;
- documentation;
- provenance;
- handoff.

## 68.40 Failure retention

Failed, blocked, cancelled, rejected, and superseded evidence remains retained.

This includes:

- failed tests;
- rejected designs;
- invalid approvals;
- unsuccessful migrations;
- owner rejection;
- unresolved risk;
- discarded options.

## 68.41 No implicit spending

A work order cannot authorize spending by implication.

A line such as “use the best service” does not authorize:

- account creation;
- paid enrollment;
- plan upgrade;
- recurring charges;
- marketplace agreement.

## 68.42 No implicit deployment

A work order cannot authorize production or publication by implication.

“Finish the feature” does not mean:

- deploy publicly;
- use production credentials;
- publish to an app store;
- invite internal-alpha users;
- release a canonical pack.

## 68.43 Repository execution

For repository work, the packet should identify:

- repository;
- base branch;
- work branch or worktree;
- target paths;
- required commands;
- CI workflows;
- PR requirements;
- merge evidence;
- cleanup.

## 68.44 One-pass execution packets

A one-pass packet may be designed for an agent to complete a bounded job with minimal owner intervention.

It should include:

- all required context locators;
- exact commands;
- environment checks;
- preflight;
- known failure modes;
- fallback paths;
- test order;
- artifact collection;
- cleanup;
- stop conditions.

One-pass does not mean unbounded authority.

## 68.45 Borrowed-machine packet

A borrowed-machine work order should additionally define:

- no unnecessary setup;
- preloaded dependencies where practical;
- exact Apple-only tasks;
- no persistent credentials;
- project cleanup;
- evidence copied out;
- fallback if signing or provisioning blocks;
- owner-only account and agreement boundaries.

## 68.46 Credit-efficient packet execution

Credit usage is reduced by:

- exact work scope;
- sealed context bundle;
- cached immutable sources;
- deterministic scripts;
- batched compatible validation;
- narrow failure reproduction;
- retained receipts;
- concise handoff;
- no repeated re-explanation of the full project.

Credit reduction must not weaken evidence or authority.

## 68.47 “Continue” behavior

Within this project, “Continue” means:

- perform the next verified unfinished operation;
- respect dependency order;
- use the active work order and current repository evidence;
- repair ordinary failures automatically;
- preserve outputs and provenance;
- report the next step.

It does not mean provide another plan instead of work.

## 68.48 Example packet outcomes

The validated release includes executable examples demonstrating:

- ordinary bug repair passing;
- feature implementation passing;
- schema change passing;
- security dependency work passing;
- documentation work passing;
- incident rollback passing;
- canon change proceeding only with owner approval;
- missing owner approval blocking;
- post-approval scope drift blocking;
- A4 prohibited work blocking.

## 68.49 Validated work-order baseline

The completed 8D-008F release validated:

- sixteen record types;
- eighteen lifecycle states;
- five risk classes;
- four priority classes;
- ten dependency types;
- twelve acceptance-criterion types;
- sixteen output-artifact types;
- sixteen material-change triggers;
- twenty-eight Definition-of-Ready criteria;
- thirty-two Definition-of-Done criteria;
- forty packet rules;
- sixteen work-type profiles;
- fourteen role responsibility bindings;
- twenty-eight permitted state transitions;
- eighty paired test cases;
- ten executable examples;
- 460 acceptance checks passed;
- zero failed.

Seven valid examples proceeded. Missing owner approval, scope drift after approval, and A4 requests blocked as required.

## 68.50 Current project application

The current bounded implementation roadmap functions as an approved program-level work order.

Individual backlog items still require:

- exact repository context;
- task-specific scope;
- roles;
- tests;
- CI;
- artifacts;
- handoff;
- merge evidence.

The next active item remains governed by the current repository roadmap rather than by stale handoff text.

## 68.51 Controlling references

- 8D-008F Work-Order and Task-Packet Standard
- Definition-of-Ready catalog
- Definition-of-Done catalog
- task-state catalog
- material-change trigger catalog
- role-to-responsibility map
- context receipt schemas
- 8D-007J blocking quality gate
- 8D-008J operating manual and reference tools
- active Application Implementation Roadmap

**Status:** Canonical and validated bounded-execution standard.



# 69. Repository Workflow

## 69.1 Purpose

Define how Multiversal work moves from an approved task packet into isolated repository changes, local verification, independent review, continuous integration, merge evidence, release preparation, documentation, and durable closure.

The repository workflow must support several AI agents without allowing shared mutable state, private conversation memory, direct main-branch changes, or unsupported completion claims to become project authority.

## 69.2 Repository principle

The repository is a controlled evidence system.

It contains:

- source files;
- contracts;
- schemas;
- migrations;
- fixtures;
- tests;
- workflows;
- review records;
- release artifacts;
- documentation;
- provenance;
- current-state evidence.

A repository is not merely a place to store generated code.

## 69.3 Current repository responsibilities

The project currently distinguishes two major repository responsibilities.

### Application repository

`cybalicistjt-stack/Multiversal-app`

The application repository contains or is intended to contain:

- executable application code;
- provider-neutral service ports;
- adapters;
- schemas;
- migrations;
- fixtures;
- tests;
- CI;
- application documentation;
- build and release evidence.

### Governance and AIOC repository

`cybalicistjt-stack/multiversal-aioc`

The governance repository contains:

- owner-approved roadmaps;
- governance;
- Development Brain material;
- role and workflow contracts;
- current-state records;
- canonical planning packages;
- work-order and AI-team operating assets.

Runtime application behavior must not depend on an AI agent rereading conversational history from the governance repository.

## 69.4 Planned monorepo direction

The approved Phase 9 repository roadmap selected one governed application monorepo for coordinated cross-language development.

The planned structure includes major areas such as:

```text
apps/
packages/
crates/
domains/
schemas/
content/
fixtures/
tests/
infra/
ci/
scripts/
tools/
docs/
release/
.agent/
```

This structure is a target architecture and does not prove that every directory or package is currently implemented.

## 69.5 Dependency-direction rules

The planned repository direction establishes these principles:

- `apps/` composes product modules and adapters;
- other modules do not import from an application shell;
- `packages/` owns portable TypeScript contracts and logic;
- `crates/` owns native capabilities;
- `domains/` owns bounded product domains after decomposition;
- `schemas/` is the canonical cross-language contract source;
- `infra/` contains optional provider profiles and activation records;
- `release/` contains generated manifests and receipts;
- generated release files are not edited by hand.

CI should enforce dependency direction rather than relying on convention alone.

## 69.6 Work-order prerequisite

Every material repository change begins with:

- approved work order;
- sealed task packet;
- current context receipt;
- assigned executor;
- required reviewers;
- declared environment;
- allowed and forbidden paths;
- acceptance criteria;
- rollback or recovery plan.

A prompt, issue, branch, or tool result is insufficient authority by itself.

## 69.7 Branch naming

The planned standard uses a work-order branch such as:

`wo/<work-order-id>-<slug>`

Branch naming should retain the stable work-order identity so that:

- commits;
- pull requests;
- CI;
- reviews;
- handoffs;
- release receipts;

can be connected to the approved task.

## 69.8 Protected main branch

The primary branch should be protected.

Ordinary policy should prohibit:

- direct commits;
- force pushes;
- bypassing required checks;
- deletion of retained evidence;
- unreviewed material changes;
- release changes without the appropriate authorization.

Emergency procedures remain governed and must preserve evidence.

## 69.9 Worktree isolation

Each participating agent should receive a separate worktree outside the repository root.

A conceptual layout is:

`../multiversal-worktrees/<work-order>/<role>`

Agents must not share a mutable worktree.

Separate worktrees reduce:

- file collisions;
- accidental staging;
- hidden local changes;
- cross-agent assumptions;
- corrupted review evidence.

## 69.10 Workspace allocation record

Each worktree allocation should identify:

- work order;
- repository;
- branch;
- worktree path;
- role;
- agent instance;
- base commit;
- allowed paths;
- forbidden paths;
- environment;
- creation time;
- cleanup requirements.

## 69.11 Preflight

Before editing, the executor should verify:

- correct repository;
- correct branch;
- correct worktree;
- expected base commit;
- clean or fully enumerated status;
- required tools;
- required context;
- valid approvals;
- local environment profile;
- absence of production credentials.

A mismatch blocks material execution until resolved.

## 69.12 Allowed and forbidden paths

The task packet should list known allowed and forbidden paths.

A forbidden path may include:

- production configuration;
- release keys;
- unrelated domain files;
- canonical baselines;
- generated release artifacts;
- owner-decision records;
- another agent’s worktree.

Discovery that additional files must change may trigger packet revision.

## 69.13 Minimal coherent change

The executor should make the smallest coherent change that satisfies the approved objective.

The workflow should avoid:

- unrelated refactors;
- opportunistic dependency changes;
- broad formatting churn;
- renaming stable IDs;
- altering expected tests;
- replacing architecture merely because another approach is familiar.

## 69.14 Local-first execution

The first executable environments are local and zero-service.

Local repository work should not require:

- hosted application API;
- hosted database;
- payment service;
- email provider;
- cloud campaign store;
- remote telemetry;
- mandatory relay.

Hosted CI may mirror the repository-owned command when the security and cost posture permits.

A provider outage or invoice must not prevent local validation.

## 69.15 Canonical CI entrypoint

The repository should own the canonical validation entrypoint.

The same logical command should run:

- locally;
- in CI;
- during recovery;
- during release preparation.

Hosted workflow configuration is an adapter around the repository-owned validation contract.

## 69.16 Repository-owned tools

Repository tooling may include:

- environment setup;
- schema validation;
- migration control;
- fixture generation;
- pack validation;
- source reconciliation;
- test orchestration;
- artifact assembly;
- release verification;
- cleanup.

Tools must remain version controlled and must not become hidden manual procedures.

## 69.17 Change record

A material change record should identify:

- work order;
- changed files;
- changed stable IDs;
- before and after digests;
- schema or contract impact;
- migrations;
- tests;
- decisions;
- reviewers;
- known limitations.

## 69.18 Commit discipline

Commits should be:

- attributable;
- scoped;
- readable;
- free of secrets;
- connected to the work order;
- compatible with the selected merge strategy.

A commit message does not replace the task packet or change record.

## 69.19 Generated files

Generated files should identify:

- generator;
- generator version;
- source inputs;
- configuration;
- output digest;
- reproducibility command.

Generated release files should not be manually edited to conceal generator defects.

## 69.20 Pull-request creation

A pull request should include:

- work-order ID;
- objective;
- scope;
- changed-artifact summary;
- test commands and results;
- migration impact;
- security or privacy impact;
- screenshots or interaction evidence where applicable;
- known limitations;
- rollback;
- review assignments;
- approval boundary.

## 69.21 Pull-request review

Review should examine:

- compliance with scope;
- source and requirement traceability;
- architecture;
- code and schema quality;
- tests;
- permission behavior;
- migration;
- rollback;
- documentation;
- negative evidence;
- release claims.

A green workflow does not eliminate independent human or agent review where required.

## 69.22 Review independence

A material author cannot be the sole independent reviewer.

Agents may review each other’s work only when:

- worktrees are separate;
- reviewer context is current;
- reviewer did not materially author the change;
- authority and role are appropriate;
- review evidence is retained.

## 69.23 CI execution

CI should run the gates selected by the work-type profile.

Representative CI areas include:

- repository policy;
- formatting;
- TypeScript and Rust static analysis;
- unit and integration tests;
- schemas and contracts;
- migrations;
- pack lifecycle;
- golden mechanics;
- entitlements;
- session protocol;
- offline or zero-service operation;
- secrets and privacy;
- dependencies and licenses;
- import direction;
- reproducibility;
- recovery;
- release artifacts;
- documentation and handoff.

## 69.24 CI failure handling

A failed workflow should trigger:

1. exact job and step inspection;
2. log and artifact retrieval;
3. local reproduction where practical;
4. root-cause classification;
5. repair within scope;
6. targeted rerun;
7. full required rerun;
8. retention of failed evidence.

The correct response is not to restart blindly until a transient pass appears.

## 69.25 Stale CI

CI becomes stale when material changes occur after the run.

Material changes include:

- new commit;
- amended artifact;
- changed migration;
- changed lockfile;
- changed expected output;
- changed approval digest;
- rebased branch affecting relevant files.

Required gates rerun.

## 69.26 Merge eligibility

A change becomes merge-eligible only when:

- task packet remains valid;
- context remains current;
- approvals remain valid;
- required gates pass;
- independent review completes;
- blocking findings are resolved or governed;
- provenance and documentation are complete;
- merge strategy is allowed.

Merge eligibility is not merge completion.

## 69.27 Merge strategies

The validated workflow defines six merge strategies:

### No merge

Used for research, documentation-only disposition, blocked work, or cancelled work without repository artifact integration.

### Squash merge

Allowed for bounded tasks when required evidence remains preserved.

### Merge commit

Preserves the branch boundary and review history.

### Fast-forward

Allowed only when protections and audit evidence remain intact.

### Approved cherry-pick

Used for isolated recovery or backport with exact approval and evidence.

### Release promotion

Promotes an already verified artifact without rebuilding it in place.

## 69.28 Merge evidence

Completion evidence should confirm:

- pull request;
- final commit or squash commit;
- target branch;
- merge time;
- required checks;
- review state;
- resulting file state.

An open, approved, or green pull request is not a merged pull request.

## 69.29 Post-merge verification

After merge, the workflow may require:

- target-branch CI;
- checksum verification;
- integration smoke tests;
- documentation update;
- current-state update;
- cleanup;
- handoff.

## 69.30 Branch cleanup

After verified merge or closure:

- preserve required evidence;
- remove disposable worktree;
- remove obsolete local branch where appropriate;
- retain remote branch according to repository policy;
- confirm no uncommitted work is lost;
- record cleanup.

## 69.31 Release branches

Release branches should contain only validated release fixes.

They must not become alternate long-lived development branches.

## 69.32 Release artifact preparation

Release preparation may include:

- deterministic build;
- manifest;
- checksums;
- signatures or attestations where authorized;
- release notes;
- migration notes;
- rollback plan;
- known limitations;
- quality-gate receipts.

Release preparation does not authorize release.

## 69.33 Service-activation locks

A service SDK, endpoint, secret, or required network dependency should remain blocked unless an approved activation record identifies:

- measured trigger;
- scope;
- cost ceiling;
- expiration;
- data classes;
- fallback;
- exit path;
- approving authority.

## 69.34 Repository and environment progression

The approved environment progression moves conceptually through:

1. planning and package-only work;
2. local zero-service development;
3. local isolated multi-client loopback;
4. real-device direct-connect spike;
5. optional free-tier signaling;
6. private-alpha static distribution;
7. complete product alpha;
8. invite public beta;
9. paid public production.

Advancement requires evidence and owner gates.

## 69.35 Current application evidence

The active roadmap records merged application work through P9-06-007.

The current repository task remains the next verified unfinished item in the active roadmap.

The older planning package and newer roadmap may differ in backlog naming or numbering; the newer active roadmap and repository evidence control execution.

## 69.36 Claims boundary

Repository workflow compliance does not prove:

- final canon;
- final balance;
- human testing;
- accessibility conformance;
- production performance;
- internal-alpha release;
- public launch.

## 69.37 Controlling references

- 8D-008F Work-Order and Task-Packet Standard
- 8D-008G Development Workflow and Quality Gates
- P9-04 Repository Strategy and Monorepo Layout
- P9-04 Branch, Worktree, and Agent Isolation Standard
- P9-04 CI, Quality, and Service-Activation Gates
- P9-04 Environment and Zero-Service Profile Standard
- active Application Implementation Roadmap
- repository PR, commit, CI, and merge evidence

**Status:** Canonical repository workflow. The planned monorepo and later environment stages remain implementation- and evidence-dependent.

---

# 70. Review and Quality Gates

## 70.1 Purpose

Define the ordered workflow stages, mandatory quality gates, evidence requirements, reviewer independence, remediation behavior, merge eligibility, release integrity, and claims boundaries used for material Multiversal work.

## 70.2 Gate principle

A gate is a blocking evidence decision.

A required gate may not be:

- skipped;
- converted into a warning without authority;
- satisfied by a plan;
- satisfied by the author’s unsupported statement;
- overwritten by a later passing run;
- bypassed because a deadline or tool limitation exists.

## 70.3 Ordered workflow

The validated workflow contains twenty stages:

1. Request Intake.
2. Packet Authoring.
3. Context Resolution.
4. Definition of Ready Gate.
5. Assignment.
6. Implementation Planning.
7. Approval Gate.
8. Isolated Execution.
9. Local Verification.
10. Specialist Quality Gates.
11. 8D-007J Regression Gate.
12. Independent Review.
13. Remediation.
14. Merge Eligibility Gate.
15. Merge or Integration.
16. Release Preparation.
17. Owner Release Approval.
18. Release or Deployment.
19. Post-Release Verification.
20. Closure and Handoff.

Not every task reaches release stages. The work-type profile selects the applicable route.

## 70.4 Gate tiers

The eighteen quality gates are organized into four tiers.

### G0 — Packet and Eligibility

Before execution:

- task packet;
- context;
- authority;
- workspace;
- scope and digest.

### G1 — Implementation Verification

Local and targeted:

- build and static analysis;
- functional tests;
- schemas;
- deterministic behavior;
- migration compatibility.

### G2 — Independent Assurance

Specialist and independent:

- security;
- privacy;
- dependencies;
- UX and accessibility;
- performance;
- simulation and balance;
- 8D-007J regression;
- independent review;
- provenance and handoff.

### G3 — Integration and Release

Integration and release:

- merge integrity;
- release artifact integrity;
- rollback;
- owner approval;
- deployment;
- post-release verification.

## 70.5 Gate 1: Task Packet Validity

The task packet gate verifies:

- stable packet identity;
- current version;
- Definition of Ready;
- work type;
- decision level;
- risk;
- scope;
- roles;
- dependencies;
- acceptance;
- outputs;
- handoff.

## 70.6 Gate 2: Context Receipt Current

This gate verifies:

- required sources resolved;
- digests match;
- context is fresh;
- conflicts are routed;
- load receipt is complete;
- bundle digest matches;
- required exact evidence remains present.

## 70.7 Gate 3: Authority and Approval Valid

This gate verifies:

- executor authority;
- reviewer authority;
- owner-reserved domains;
- delegation;
- approval state;
- artifact digest;
- environment;
- validity window;
- no A4 action.

## 70.8 Gate 4: Isolated Workspace

This gate verifies:

- correct repository;
- branch;
- worktree;
- base commit;
- environment;
- allowed paths;
- local status;
- no shared mutable workspace;
- no production credentials.

## 70.9 Gate 5: Scope and Digest Match

This gate verifies:

- current work matches approved scope;
- artifact digest matches approval;
- changed files are permitted;
- material drift is absent or reapproved;
- required source and packet versions remain current.

## 70.10 Gate 6: Build, Lint, and Static Analysis

This gate may include:

- compilation;
- formatting;
- linting;
- type checking;
- import-direction checks;
- generated-file checks;
- forbidden API checks;
- secrets scanning.

## 70.11 Gate 7: Unit and Functional Tests

This gate verifies bounded behavior through:

- unit tests;
- functional tests;
- property tests;
- invariants;
- error paths;
- permission paths;
- representative fixtures.

## 70.12 Gate 8: Schema and Contract Validation

This gate verifies:

- schemas;
- stable IDs;
- API contracts;
- pack contracts;
- event contracts;
- extension contracts;
- provider-neutral service contracts;
- cross-language compatibility.

## 70.13 Gate 9: Deterministic Replay

This gate verifies, where applicable:

- recorded input;
- seed;
- roll;
- event order;
- version;
- replay result;
- absence of duplicate effects.

## 70.14 Gate 10: Migration and Compatibility

This gate verifies:

- migration plan;
- source and target versions;
- backup;
- restore proof;
- stable-ID mappings;
- count reconciliation;
- rollback or forward repair;
- live-state compatibility;
- deterministic result.

## 70.15 Gate 11: Security, Privacy, and Dependency

This gate verifies:

- threat and data-flow impact;
- authorization;
- hidden information;
- secrets;
- protected data;
- dependency origin and version;
- license;
- provider and cost implications;
- exit or fallback;
- unresolved vulnerabilities.

## 70.16 Gate 12: UX and Accessibility Review

This gate verifies, when applicable:

- workflow completion;
- navigation;
- keyboard;
- touch;
- focus;
- screen-reader behavior;
- responsive layouts;
- loading;
- error;
- offline;
- forbidden;
- recovery.

Automated checks do not constitute completed human validation.

## 70.17 Gate 13: Performance and Resource Budget

This gate verifies:

- latency;
- memory;
- CPU;
- database use;
- payload;
- storage;
- network;
- AI use;
- cost guardrails;
- regression against approved baseline.

## 70.18 Gate 14: Simulation and Balance Evidence

This gate applies when game behavior or balance is affected.

It verifies:

- defined peer group;
- metrics;
- seeds;
- sample count;
- uncertainty;
- practical delta;
- retained outliers;
- review disposition.

It does not authorize automatic canon changes.

## 70.19 Gate 15: 8D-007J Full Regression

The locked Golden Test Corpus and Balance Harness is a mandatory blocking gate for affected work types.

The existing verified baseline includes:

- 3,717 passing checks;
- 259 active canonical cases;
- 220 exact product baselines;
- 39 executed regression cases;
- 18 RNG conformance cases;
- 339 approved baseline objects;
- 21 retained E4 simulation runs;
- 3,080,000 retained candidate trials;
- seven replay bundles;
- seven closed controls;
- zero unexpected findings;
- 957 final acceptance checks with zero failures.

Expected outputs may not be changed merely to make this gate pass.

## 70.20 Gate 16: Independent Material Review

A qualified non-author reviews:

- scope;
- implementation;
- tests;
- failures;
- security;
- migrations;
- architecture;
- canon;
- UX;
- evidence;
- claims.

The reviewer must record findings and disposition.

## 70.21 Gate 17: Provenance, Documentation, and Handoff

This gate verifies:

- source references;
- changed-artifact index;
- decisions;
- failures;
- checksums;
- documentation;
- current-state update;
- evidence locators;
- handoff;
- next executable action.

## 70.22 Gate 18: Merge, Release, and Rollback Integrity

This gate verifies:

- merge strategy;
- exact artifact;
- manifest;
- checksums;
- approvals;
- backup;
- restore;
- rollback;
- release environment;
- post-release observation;
- production or owner gate.

## 70.23 Gate selection

The registered work type determines which gates are required.

Examples:

- documentation work may not require migration or performance;
- schema change requires schema, migration, independent review, and provenance;
- security dependency work requires security review;
- rules-runtime change requires deterministic and 8D-007J regression;
- release work requires all applicable G3 controls.

## 70.24 Gate order

Gate order is binding.

A downstream gate cannot compensate for a missing upstream eligibility gate.

For example:

- passing tests do not fix stale approval;
- a review does not fix invalid context;
- a release checksum does not fix a failed security gate;
- owner approval does not convert A4 work into allowed work.

## 70.25 Gate run record

Every gate run should record:

- gate ID;
- work order;
- packet digest;
- context digest;
- artifact digest;
- executor instance;
- reviewer instance;
- evidence artifacts;
- evidence digests;
- start and end time;
- result;
- notes;
- rerun relationship.

## 70.26 Gate outcomes

The validated model defines eight gate outcomes.

Conceptually, outcomes distinguish conditions such as:

- pass;
- fail;
- block;
- not applicable;
- expired;
- quarantined;
- superseded;
- pending.

Only an eligible passing or governed not-applicable result satisfies a required gate.

## 70.27 Failure permanence

Failure evidence is permanent.

Remediation creates a new run.

The system must not:

- overwrite a failed report;
- delete the failing fixture;
- regenerate expected output;
- remove an outlier;
- hide a vulnerability;
- collapse failed and passed runs into one ambiguous result.

## 70.28 Downstream reruns

A remediated gate may invalidate downstream evidence.

The workflow should rerun affected gates when:

- source changes;
- implementation changes;
- migration changes;
- artifact digest changes;
- environment changes;
- approval changes;
- review findings change behavior.

## 70.29 Failure dispositions

The validated workflow defines twelve dispositions:

- remediate and rerun;
- return to planning;
- refresh context;
- reapprove;
- quarantine evidence;
- security stop work;
- canon stop work;
- rollback;
- incident response;
- cancel;
- supersede;
- owner escalation.

Every disposition retains evidence.

## 70.30 Remediation

Remediation should identify:

- failed gate;
- root cause;
- corrective change;
- changed artifacts;
- affected approvals;
- affected downstream gates;
- new run;
- final status.

## 70.31 Gate expiry

A gate may expire because of:

- artifact change;
- context change;
- environment change;
- approval expiry;
- dependency update;
- elapsed validity period;
- new security advisory;
- repository rebase;
- source change.

Expired gates rerun.

## 70.32 Quarantine

Evidence should be quarantined when:

- digest mismatch;
- suspected tampering;
- secret contamination;
- unknown provenance;
- incompatible schema;
- unsafe archive;
- untrusted external output.

Quarantined evidence cannot satisfy a gate.

## 70.33 Self-review failure

A material author cannot satisfy the independent-review gate by changing role labels.

The validated examples explicitly block self-review.

## 70.34 Stale approval failure

An approval bound to an older scope or digest blocks current execution.

The validated examples explicitly block stale approval.

## 70.35 Missing production owner approval

Build, test, or release preparation may pass while production action remains blocked.

The validated examples explicitly block missing owner approval for production.

## 70.36 A4 failure

A prohibited A4 request blocks immediately and retains the request and disposition.

No downstream technical gate may authorize it.

## 70.37 Merge eligibility

Merge eligibility requires all mandatory G0, G1, and G2 gates for the work type.

Required G3 prerequisites apply before release or deployment.

## 70.38 Release claims

A workflow PASS establishes only that the governed workflow passed.

It does not establish:

- Canon 1.0;
- final balance;
- human playtest sufficiency;
- usability;
- accessibility;
- security certification;
- legal compliance;
- production performance;
- production readiness.

## 70.39 Validated workflow baseline

The completed 8D-008G release defines:

- twenty workflow stages;
- eighteen blocking gates;
- four gate tiers;
- eight gate outcomes;
- six environments;
- sixteen evidence types;
- twelve failure dispositions;
- six merge strategies;
- forty-four workflow rules;
- sixteen work-type gate profiles;
- eighteen gate-order bindings;
- twenty stage-role bindings;
- eighteen gate-review bindings;
- eighty-eight paired test cases;
- thirteen executable examples;
- 2,055 acceptance checks passed;
- zero failed.

Eight valid workflows completed. The 8D-007J failure, self-review, stale approval, missing production owner approval, and A4 examples blocked as required.

## 70.40 Change-control integration

The completed 8D-008H control package adds:

- fourteen control domains;
- twelve change classes;
- fifteen migration phases;
- twenty-four security controls;
- sixteen work-type control profiles;
- eighteen quality-gate bindings;
- twenty-two executable examples;
- one hundred paired cases;
- 2,516 acceptance checks passed;
- zero failed.

These controls bind migrations, secrets, dependencies, licensing, backup, release, rollback, destructive actions, and incidents into the gate workflow.

## 70.41 Controlling references

- 8D-008G Development Workflow and Quality Gates
- Workflow Stage Catalog
- Quality Gate Catalog
- Gate Tier Catalog
- Gate Execution and Evidence Guide
- Failure Remediation and Stop-Work Guide
- 8D-008H Change, Migration, Security, and Release Controls
- 8D-007J Golden Test Corpus and Balance Harness
- work-type gate profiles and repository CI

**Status:** Canonical and validated quality-gate architecture.

---

# 71. Checkpoints, Handoffs, and Recovery

## 71.1 Purpose

Define how Multiversal work survives interrupted agents, lost sessions, tool failures, environment replacement, repository handoff, owner delays, and task closure without depending on an AI model’s private memory.

## 71.2 Continuity principle

A successor reconstructs exact work state from durable records before acting.

A successor does not inherit authority from:

- agent name;
- prior conversation;
- tool access;
- branch access;
- a vague handoff;
- an assumption that the predecessor “probably finished.”

## 71.3 Continuity layers

Continuity should preserve:

- work order;
- task packet;
- context receipt;
- authority;
- approval;
- workspace;
- changed artifacts;
- dependencies;
- gates;
- failures;
- migrations;
- security state;
- owner decisions;
- open work;
- next executable action;
- evidence locations.

## 71.4 Handoff triggers

A handoff may be required because of:

- planned role transfer;
- agent interruption;
- context-limit risk;
- tool failure;
- environment shutdown;
- borrowed-machine cleanup;
- branch transfer;
- reviewer transfer;
- owner-decision wait;
- incident;
- task closure.

## 71.5 Handoff envelope

The handoff envelope is the sealed root record for a transfer.

It should identify:

- predecessor;
- successor or required successor role;
- work order;
- current state;
- reason;
- scope;
- continuity digest;
- required records;
- blocked or ready state;
- created time;
- expiration or supersession.

## 71.6 Work-state snapshot

The work-state snapshot captures:

- task packet;
- current workflow stage;
- workspace;
- commit;
- uncommitted changes;
- generated files;
- changed stable IDs;
- tests;
- gate results;
- failures;
- decisions;
- approvals;
- blockers;
- next action.

It does not replace repository commits or authoritative artifacts.

## 71.7 Continuity receipt

A continuity receipt proves that the successor resolved and verified required handoff references.

It should record:

- handoff envelope;
- reconstruction checks;
- resolved sources;
- digests;
- unavailable evidence;
- conflicts;
- successor role;
- result;
- activation decision.

## 71.8 Evidence-location index

Every continuity artifact should have a stable index entry with:

- evidence ID;
- type;
- locator;
- resolver;
- version;
- digest;
- availability;
- required or optional status;
- retention class;
- access restriction.

## 71.9 Agent replacement record

A replacement record should identify:

- predecessor;
- successor;
- reason;
- active roles;
- revoked or expired access;
- transferred scope;
- limitations;
- activation conditions;
- owner or orchestrator authority.

## 71.10 Recovery plan

A recovery plan should state:

- interruption;
- affected work;
- evidence to preserve;
- authority impact;
- security and secret impact;
- data or migration impact;
- required reconstruction checks;
- gate reruns;
- stop conditions;
- resume action;
- fallback.

## 71.11 Recovery execution record

Every recovery attempt should be append-only.

It should record:

- plan;
- actions;
- results;
- failures;
- new evidence;
- quarantined evidence;
- final state;
- next disposition.

## 71.12 Owner decision queue

Owner-reserved A3 decisions should be preserved in a queue rather than in private conversation memory.

The queue never authorizes execution.

## 71.13 Owner decision item

A queue item should contain:

- exact question;
- alternatives;
- implications;
- recommendation;
- evidence digest;
- current state;
- urgency;
- prohibited execution until decision;
- required approval binding.

## 71.14 Open-work register

The open-work register should identify:

- remaining steps;
- blockers;
- dependencies;
- reviewers;
- gate obligations;
- approvals;
- next executable action;
- tasks no longer valid;
- owner decisions.

## 71.15 Workspace-state record

For repository work, the workspace record should identify:

- repository;
- branch;
- worktree;
- environment;
- commit;
- status;
- uncommitted files;
- generated files;
- local configuration;
- cleanup state.

## 71.16 Gate-state register

The gate register should identify:

- required gates;
- run IDs;
- results;
- evidence;
- failures;
- expired results;
- rerun obligations;
- downstream invalidation.

## 71.17 Approval-state register

The approval register should identify:

- approval record;
- decision level;
- scope digest;
- artifact digest;
- executor;
- environment;
- expiration;
- invalidation triggers;
- current state.

## 71.18 Incident continuity

During an incident, continuity records should preserve:

- current facts;
- severity;
- containment;
- incident owner;
- secret and credential state;
- affected data;
- recovery phase;
- communication status;
- next safe action.

## 71.19 Replacement activation

A successor may act only after a replacement-activation record confirms:

- role acceptance;
- authority;
- context reconstruction;
- workspace access;
- continuity digest;
- unresolved blockers;
- exact next action;
- no prohibited continuation.

## 71.20 Closure handoff

Every material task should end with a closure handoff.

It should preserve:

- final outputs;
- checksums;
- tests;
- reviews;
- approvals;
- limitations;
- retained failures;
- owner decisions;
- current repository state;
- follow-up obligations;
- next roadmap action.

## 71.21 Handoff exception

When continuity cannot be proven, create a handoff-exception record.

It should identify:

- unavailable evidence;
- reason;
- affected scope;
- degraded mode;
- blocking disposition;
- required owner or specialist decision;
- safe work still permitted.

## 71.22 Recovery states

The validated model defines fourteen recovery states:

1. Not Required.
2. Interruption Detected.
3. Evidence Preserved.
4. Recovery Triage.
5. Handoff Required.
6. Reconstruction Pending.
7. Reconstruction Blocked.
8. State Reconstructed.
9. Verification Pending.
10. Gate Rerun Required.
11. Owner Decision Pending.
12. Resume Authorized.
13. Recovered.
14. Quarantined.

Only Recovered and Quarantined are terminal in the validated catalog.

## 71.23 Detection

Recovery begins by detecting:

- interruption;
- replacement;
- continuity risk;
- digest mismatch;
- missing source;
- lost workspace;
- expired approval;
- secret contamination;
- unretained failure;
- unavailable reviewer.

## 71.24 Evidence preservation

The first response is preservation, not reconstruction from memory.

Preserve:

- repository state;
- logs;
- artifacts;
- receipts;
- test failures;
- context records;
- approvals;
- worktree status;
- owner queue;
- environment metadata.

## 71.25 Recovery triage

Triage classifies impact on:

- authority;
- security;
- secrets;
- protected data;
- migrations;
- backups;
- quality gates;
- source truth;
- owner decisions;
- release.

## 71.26 Predecessor access

Predecessor access should be revoked or allowed to expire when replacement occurs.

Revocation may include:

- worktree allocation;
- service token;
- temporary credentials;
- session;
- role assignment;
- deployment permission.

## 71.27 Successor compatibility

The successor must have:

- compatible role;
- appropriate capabilities;
- required tool access;
- current authority;
- independent-review eligibility;
- no prohibited conflict.

## 71.28 Reconstruction checks

The validated model defines twenty-four blocking reconstruction checks:

- packet identity;
- work-order scope;
- context receipt;
- source availability;
- role assignment;
- authority matrix;
- approval scope;
- delegation validity;
- workspace location;
- workspace cleanliness;
- change register;
- dependency register;
- open work;
- gate register;
- failure retention;
- migration state;
- security state;
- secret scan;
- incident state;
- owner decision queue;
- review independence;
- output locations;
- handoff completeness;
- continuity digest.

Failure of a required check blocks reconstruction.

## 71.29 Continuity digest

The continuity digest binds the reconstructed state.

It should cover the records necessary to prove:

- task identity;
- scope;
- context;
- authority;
- workspace;
- evidence;
- open work;
- next action.

A mismatch blocks continuation.

## 71.30 Gate rerun

A recovery may require rerunning gates because:

- environment changed;
- executor changed;
- evidence expired;
- artifact changed;
- repository moved;
- secrets were rotated;
- migration state changed;
- the prior run was incomplete.

The 8D-007J gate reruns when the affected work type requires it.

## 71.31 Recorded next action

The successor’s first material action is the retained next executable action.

If that action is no longer safe or valid, the work returns to:

- planning;
- context resolution;
- approval;
- remediation;
- quarantine.

The successor does not improvise a new objective.

## 71.32 Prohibited continuation

Continuation is blocked when:

- A4 work exists;
- required evidence is missing;
- secret-contaminated evidence is present;
- digest mismatch remains;
- authority is missing;
- approval is invalid;
- self-review would be required;
- failed evidence was destroyed;
- migration or backup state is unknown;
- material conflict is unresolved.

## 71.33 Operating drill

The validated operating drill uses eighteen phases:

1. Governance Check.
2. Role Activation.
3. Authority Check.
4. Source Resolution.
5. Context Load.
6. Task Packet.
7. Workflow Start.
8. Control Check.
9. Implementation Progress.
10. Interruption Injection.
11. Evidence Preservation.
12. Handoff Generation.
13. Replacement Activation.
14. State Reconstruction.
15. Gate Rerun.
16. Resume and Complete.
17. Closure Handoff.
18. Lessons and Remediation.

## 71.34 Drill result

The completed drill passed with:

- injected agent interruption;
- state preservation;
- replacement activation;
- exact reconstruction;
- 8D-007J rerun;
- independent review;
- closure handoff.

This proves the governance fixture, not production application recovery.

## 71.35 Borrowed-machine continuity

A borrowed-machine handoff should additionally preserve:

- exact machine-only tasks completed;
- build and simulator evidence;
- signing and provisioning state without exposing secrets;
- artifacts copied out;
- repository commit state;
- cleanup confirmation;
- unresolved owner-only account actions;
- next non-Mac action.

## 71.36 Conversation loss

When a prompt, reply, or conversation disappears, work continuity should be checked against durable artifacts.

The recovery process should verify:

- current master file;
- backup;
- checksum;
- last completed chapter or task;
- final next-step record;
- repository evidence where applicable.

Conversation visibility alone should not determine whether work was preserved.

## 71.37 Validated handoff baseline

The completed 8D-008I release defines:

- eighteen handoff record types;
- fourteen recovery states;
- twenty-four reconstruction checks;
- sixteen agent replacement rules;
- fourteen role profiles;
- sixteen work-type profiles;
- eighteen executable continuity examples;
- one hundred twenty paired test cases;
- eighteen operating-drill phases;
- four owner-decision queue items;
- twelve schemas;
- twenty-six workbook sheets;
- 751 acceptance checks passed;
- zero failed.

## 71.38 Controlling references

- 8D-008I Handoff, Recovery, and Operating Drill Standard
- Agent Replacement and State Reconstruction Guide
- Owner Decision Queue and Evidence Location Guide
- Handoff Record Type Catalog
- Recovery State Catalog
- Reconstruction Check Catalog
- Operating Drill Phase Catalog
- 8D-008J recovery checklist and operating manual

**Status:** Canonical and validated continuity architecture.

---

# 72. Documentation and Decision Preservation

## 72.1 Purpose

Define how Multiversal preserves governing decisions, source identity, architecture intent, implementation evidence, negative results, current state, release records, and future handoff context so that the project remains understandable without relying on one person, one agent, one chat, or one provider.

## 72.2 Documentation principle

Documentation is part of the system.

Material work is incomplete when the code or artifact exists but the project cannot answer:

- why it exists;
- which source controls it;
- what changed;
- who approved it;
- what evidence passed;
- what failed;
- how to recover;
- what remains unresolved;
- what the next agent should do.

## 72.3 Documentation categories

The documentation architecture should distinguish:

- owner decisions;
- governance;
- requirements;
- architecture decisions;
- canonical rules and content;
- repository and environment standards;
- work orders;
- change records;
- test and review evidence;
- migration and rollback records;
- release and deployment records;
- current-state records;
- handoffs;
- historical and provenance sources;
- user-facing help.

## 72.4 Normative versus informative

Every major document should indicate whether it is:

- normative;
- approved;
- proposed;
- descriptive;
- historical;
- generated;
- deprecated;
- superseded;
- provenance-only.

An informative summary must not silently become normative.

## 72.5 Authority metadata

A governing document should identify, as applicable:

- document ID;
- version;
- status;
- owner;
- approving authority;
- effective date;
- scope;
- superseded documents;
- controlling sources;
- checksum or release identity.

## 72.6 Stable document identity

Documents should use stable IDs independent of:

- filename;
- folder;
- title;
- formatting;
- storage provider.

A renamed document normally retains its identity.

## 72.7 Decision records

A decision record should identify:

- decision ID;
- question;
- context;
- alternatives;
- recommendation;
- decision;
- authority;
- scope;
- date;
- consequences;
- reversibility;
- affected artifacts;
- supersession;
- evidence.

## 72.8 Architecture decision records

An architecture decision record should preserve:

- technical problem;
- constraints;
- considered options;
- selected direction;
- reasons;
- tradeoffs;
- compatibility;
- migration;
- provider-exit impact;
- revisit trigger.

The current implementation should not silently diverge from an active ADR.

## 72.9 Owner decision records

Owner decisions should preserve:

- exact bounded question;
- decision;
- recommendation as advice;
- scope;
- artifact digest;
- executor;
- environment;
- cost;
- risk;
- validity;
- conditions;
- revocation or supersession.

A category-wide future approval should be rejected when a bounded approval is required.

## 72.10 Requirements traceability

Requirements should link to:

- owner source;
- product brief;
- work order;
- implementation;
- test;
- acceptance evidence;
- status.

A requirement should not disappear because the implementation changed.

## 72.11 Canon traceability

Canonical content should retain:

- source registry entry;
- source coordinate;
- candidate;
- mapping;
- stable ID;
- owner pack;
- release;
- conflicts;
- open decisions.

## 72.12 Change record

A change record should preserve:

- before state;
- after state;
- reason;
- affected stable IDs;
- files;
- contracts;
- migration;
- tests;
- reviewers;
- approval;
- release.

## 72.13 Negative evidence

Negative evidence must remain retained.

Examples include:

- failed test;
- rejected design;
- invalid approval;
- blocked migration;
- unresolved conflict;
- security finding;
- owner rejection;
- rolled-back release;
- superseded packet;
- quarantined artifact.

A correction creates a new record or version.

## 72.14 Append-only released evidence

Released evidence should be immutable.

Corrections should:

- preserve the original;
- create a new version;
- link supersession;
- state reason;
- update indexes;
- retain digests.

## 72.15 Current-state records

A current-state record should summarize:

- completed work;
- active work;
- blockers;
- next task;
- repository state;
- approvals;
- environment;
- limitations.

Current-state summaries must be compared with newer repository evidence.

A stale current-state file must not overrule a newer merged roadmap, bootstrap, PR, or commit.

## 72.16 Freshness hierarchy

When project records disagree, the resolver should consider:

- authority;
- status;
- scope;
- exact artifact;
- date;
- version;
- repository evidence;
- owner decision;
- supersession.

Newer is not automatically authoritative, but a superseded current-state summary should not control newer verified implementation.

## 72.17 Source citations

A reusable claim should identify its source through:

- stable source ID;
- exact artifact;
- digest;
- line, row, page, or object locator;
- structured query result where applicable.

A prior agent’s prose summary alone is insufficient for a material claim.

## 72.18 Evidence index

An evidence index should connect:

- work order;
- source;
- context receipt;
- artifact;
- tests;
- review;
- approval;
- merge;
- release;
- handoff.

## 72.19 Checksums

Checksums help verify:

- package integrity;
- release artifact;
- export;
- context source;
- handoff;
- backup;
- generated output.

A checksum proves byte identity, not correctness or approval.

## 72.20 Manifests

A manifest should list:

- artifact paths;
- types;
- sizes;
- digests;
- roles;
- required or optional status;
- versions;
- generation source.

## 72.21 Generated documentation

Generated documentation should record:

- generator;
- source data;
- version;
- command;
- output digest.

Generated docs must not be edited manually when they are intended to be reproducible.

## 72.22 Human-authored documentation

Human-authored or owner-authored records should preserve:

- author;
- review;
- status;
- approval;
- source;
- changed version.

## 72.23 Documentation alongside code

Code and contract changes should update nearby documentation when behavior changes.

Examples include:

- README;
- module contract;
- schema notes;
- migration guide;
- API reference;
- recovery procedure;
- test command;
- user workflow.

## 72.24 Repository documentation boundary

Documentation belongs in the repository that owns the truth.

Examples:

- active code behavior belongs with the application implementation;
- project governance belongs in the governance repository;
- canonical pack documentation belongs with the pack;
- owner decision records belong in the governed decision registry.

Cross-references should connect them.

## 72.25 Development Bible role

The Multiversal Development Bible is the consolidated human-readable architecture and operating reference.

It does not replace:

- exact schemas;
- code;
- pack records;
- repository evidence;
- owner decision records;
- CI receipts.

When implementation evolves, the Bible should be updated through a governed editorial pass.

## 72.26 Startup documentation

The AI Development Team Operating Package includes startup assets such as:

- Owner Start Here;
- AI Team Bootstrap;
- Lead Orchestrator startup prompt;
- role startup packets;
- work-type entry points;
- session-start checklist;
- task-start checklist;
- recovery checklist;
- release checklist;
- owner-decision request template.

These reduce repeated context transfer.

## 72.27 Operating manual chain

The operating manual preserves the control chain:

1. governance and owner sovereignty;
2. role structure;
3. authority;
4. source registry;
5. context loading;
6. work orders;
7. workflow and gates;
8. change and security controls;
9. handoff and recovery.

An agent should not start in the middle without confirming upstream controls.

## 72.28 Claims and limitations

Every release should state both:

### What it establishes

Verified capabilities, artifacts, tests, and status.

### What it does not establish

Unbuilt features, unapproved authority, unavailable human validation, unresolved legal or security claims, production restrictions, and deferred work.

## 72.29 Completion reports

A completion report should include:

- status;
- scope;
- counts;
- tests;
- failures;
- checksums;
- limitations;
- next handoff;
- release boundary.

## 72.30 Handoff documents

A handoff should preserve:

- current objective;
- completed work;
- open work;
- next action;
- source and context;
- repository state;
- tests;
- failures;
- approvals;
- evidence locations;
- cleanup.

## 72.31 Decision queue

Open owner decisions should be maintained in a dedicated queue.

A queue item should not be buried inside:

- chat;
- code comment;
- test failure;
- README note;
- private agent scratchpad.

## 72.32 Open decisions

An open-decision register should classify:

- owner required;
- source recovery;
- architecture;
- implementation;
- legal;
- security;
- content;
- deferred human testing.

An unresolved decision should not be filled with an invented default.

## 72.33 Release notes

Release notes should distinguish:

- user-visible change;
- technical change;
- schema change;
- migration;
- deprecation;
- security correction;
- content change;
- known limitation.

## 72.34 Migration documentation

Migration documentation should preserve:

- source and target;
- preconditions;
- data impact;
- backup;
- procedure;
- validation;
- rollback or forward repair;
- receipt.

## 72.35 Incident documentation

Incident documentation should preserve:

- timeline;
- detection;
- containment;
- affected scope;
- evidence;
- recovery;
- communication;
- root cause;
- corrective action;
- closure;
- unresolved risk.

Reusable secrets must not be included.

## 72.36 Security documentation

Security documentation should identify:

- threat boundary;
- controls;
- secret inventory names;
- rotation procedure;
- provider access;
- dependency review;
- incident path;
- known limitations.

## 72.37 User-facing documentation

User documentation should remain separate from internal governance.

It may include:

- onboarding;
- help;
- rules browser;
- recovery guidance;
- accessibility instructions;
- release notes.

It must not reveal protected internal or GM information.

## 72.38 Documentation review

Documentation review should verify:

- accuracy;
- current version;
- authority;
- links;
- examples;
- commands;
- permission safety;
- claims boundary;
- accessibility;
- localization readiness.

## 72.39 Documentation tests

Documentation may be tested through:

- link checks;
- code-block execution;
- schema validation;
- generated-index comparison;
- checksum verification;
- required-section validation;
- stale-reference detection.

## 72.40 Archival policy

Historical documents should remain available when needed for:

- provenance;
- migration;
- audit;
- supersession;
- source comparison;
- legal or licensing evidence.

Historical documents must be labeled so they are not mistaken for current instructions.

## 72.41 Conversation continuity

Conversation archives may help explain intent and history.

They should be treated as:

- supporting evidence;
- handoff context;
- discovery source.

They do not automatically outrank owner-approved documents, canonical packages, or repository evidence.

## 72.42 Documentation and agent memory

Agents must not rely on private memory for:

- current task;
- approval;
- source truth;
- next action;
- failure state;
- owner decision;
- repository status.

These belong in durable project records.

## 72.43 AI-authored documentation

AI may draft, summarize, index, and validate documentation.

AI must:

- preserve source citations;
- label proposals;
- retain uncertainty;
- avoid invented completion claims;
- avoid rewriting owner decisions;
- preserve negative evidence.

## 72.44 Documentation closure

A documentation work order closes only when:

- target artifact exists;
- previous content is preserved or superseded correctly;
- required sources are represented;
- checks pass;
- next step is explicit;
- checksum is recorded where required;
- handoff is complete.

## 72.45 AI operating-package baseline

The completed 8D-008J release verified:

- nine 8D-008 component packs;
- 9,403 component acceptance checks represented;
- fourteen role startup packets;
- sixteen work-type entry points;
- sixty-six indexed schemas;
- eight practical nonexecuting templates;
- fifty release rules;
- one hundred paired release cases;
- 725 package acceptance checks passed;
- embedded 8D-007J gate PASS;
- zero current open owner actions;
- twelve Phase 9 planning workstreams.

This closed 8D-008 and created the startup-ready operating package.

It did not build the application or authorize production.

## 72.46 Claims boundary

Documentation completeness does not prove:

- code implementation;
- merged repository state;
- deployment;
- final canon;
- final balance;
- human playtesting;
- accessibility conformance;
- legal compliance;
- security certification;
- public readiness.

## 72.47 Controlling references

- 8D-008I continuity and evidence-location standards
- 8D-008J AI Development Team Operating Manual
- 8D-008J Owner Operations Guide
- 8D-008J Claims and Limitations
- startup and role packets
- source registry and context receipt architecture
- work-order, review, migration, release, and handoff schemas
- repository current-state and decision records
- Multiversal Development Bible governance

**Status:** Canonical documentation and decision-preservation architecture.

---

# Tranche 7 Integration Review

## T7.1 Coverage

Volume VII now consolidates:

- AI team roles;
- staffing modes;
- separation of duties;
- authority levels;
- owner-reserved powers;
- approvals;
- delegation;
- escalation;
- stop-work;
- context loading;
- credit optimization;
- work orders;
- task packets;
- repository workflow;
- quality gates;
- handoff;
- recovery;
- agent replacement;
- documentation;
- decision preservation.

## T7.2 Owner-sovereignty invariant

John Brandon Turner remains the nonreplaceable final authority.

No agent may infer owner approval from:

- silence;
- prior behavior;
- tool access;
- repository access;
- broad trust;
- urgency;
- technical capability.

## T7.3 Evidence invariant

Material claims require durable evidence.

Conversation memory, plans, open pull requests, started workflows, and generated prose are insufficient by themselves.

## T7.4 Context invariant

Execution uses a sealed, task-specific context manifest and load receipt.

Authority, exact schemas, approvals, tests, baselines, conflicts, and failures cannot be compacted away.

## T7.5 Work-order invariant

Material work requires:

- stable task identity;
- scope;
- decision level;
- risk;
- roles;
- dependencies;
- context;
- acceptance;
- tests;
- rollback;
- outputs;
- handoff.

## T7.6 Repository invariant

Agents work in isolated branches and worktrees.

Main is protected.

Merge is allowed only after the required evidence and reviews pass.

## T7.7 Quality-gate invariant

A failure remains retained.

Remediation creates a new run and reruns affected downstream gates.

No baseline may be rewritten merely to make a gate pass.

## T7.8 Continuity invariant

Every session, interruption, replacement, or closure ends with a durable handoff or explicit blocked state.

A successor reconstructs exact state and begins with the recorded next executable action.

## T7.9 Documentation invariant

Released evidence is append-only.

Corrections create a new version and preserve the prior artifact, failure, decision, and digest.

## T7.10 Validated operating package

The 8D-008 operating program is complete and validated through 8D-008J.

The release provides:

- organizational structure;
- authority;
- context;
- work-order;
- workflow;
- change control;
- security;
- release;
- recovery;
- startup;
- operating documentation.

## T7.11 Current boundary

The operating package makes an AI development team governable and startup-ready.

It does not mean:

- a permanent autonomous team is running;
- the application is complete;
- every repository task is implemented;
- production is authorized;
- spending is authorized;
- public release is authorized.

## T7.12 Tranche status

Volume VII is complete at the AI-development-operations level.

Future AI work should execute through these controls and the active repository roadmap rather than through ad hoc conversation alone.

**Tranche 7 status:** Complete — canonical AI development operations consolidated.


# Volume VIII — Roadmap, Verification, and Release

# 73. Completed Project Phases

## 73.1 Purpose

Record what the Multiversal project has actually completed, distinguish completed planning and validation from application implementation, preserve the evidence boundary for each phase, and prevent future agents from restarting finished work or treating a plan as a shipped product.

## 73.2 Completion principle

A project phase may be complete at one level while later implementation remains unfinished.

The project distinguishes:

- source creation;
- product definition;
- planning;
- architecture;
- canonicalization;
- validation;
- operating-package preparation;
- repository implementation;
- user-interface construction;
- internal testing;
- release.

A completed architecture phase does not prove that the corresponding product feature exists in executable form.

## 73.3 Phase 0 — Legacy source creation

Phase 0 consists of the original game and setting material created by John Brandon Turner and his brother.

This phase established the legacy source corpus, including:

- game rules;
- abilities;
- creatures;
- items;
- settings;
- adventures;
- world material;
- supporting concepts and prose.

**Status:** Complete as source creation.

The legacy files remain source evidence. Their existence does not mean every claim was originally normalized, reconciled, balanced, or implementation-ready.

## 73.4 Phase 0.5 — Multiversal Definition Document

The Definition Document established Multiversal as a broad tabletop role-playing platform rather than a single narrow game or campaign application.

It defined the high-level product identity, including support for:

- many genres;
- many settings;
- many play styles;
- modular rules and content;
- Player and Game Master workflows;
- extensible packs;
- AI-assisted creation and play;
- long-term platform growth.

**Status:** Complete as product definition.

## 73.5 Phases 1–7 — Planning and architecture

Phases 1–7 developed the project’s broad planning and architecture.

The work included:

- product conception;
- functional design;
- data and pack architecture;
- mechanics architecture;
- content-domain architecture;
- interface and workflow design;
- governed repository preparation;
- stable-ID and schema direction;
- campaign, character, world, and runtime concepts;
- contributor and authority boundaries.

**Status:** Complete at the planning and architecture level.

These phases did not deliver a finished public application.

## 73.6 Phase 8 — Canonicalization and validation

Phase 8 converted the planning and source-recovery work into governed standards, canonical structures, validated content, and reusable operating packages.

The major Phase 8 achievements include:

- canonical pack and object standards;
- domain-by-domain normalization;
- cross-domain mechanics consolidation;
- source coverage and provenance;
- final domain validation;
- golden regression and balance infrastructure;
- AI Development Team operating infrastructure;
- CSV-first canonical conversion.

**Status:** Complete.

## 73.7 Phase 8A — Standards

Phase 8A established the standards needed for later conversion and runtime use.

The standards include:

- pack naming and extension rules;
- stable identifiers;
- object families;
- schemas;
- references;
- ownership;
- provenance;
- validation;
- lifecycle expectations.

The approved pack extension is `.pack`.

## 73.8 Phase 8B — Abilities and progression

Phase 8B normalized abilities, progressions, grants, prerequisites, domains, and related mechanics.

The work preserved:

- source distinctions;
- incomplete information;
- progression relationships;
- environmental adaptations;
- domain classifications;
- shared runtime behavior.

The associated simulation program used deterministic large-sample evidence, including the retained `legacy-balance-parity-200000` baseline.

## 73.9 Phase 8C — Shared mechanics

Phase 8C established the reusable mechanics architecture for:

- Actions;
- Effects;
- Conditions;
- Resources;
- modifiers;
- rules profiles;
- progression;
- grants;
- shared validation.

The architecture prevents each content domain from inventing a separate incompatible rules engine.

## 73.10 Phase 8D — Assurance and AI operations

Phase 8D delivered two major permanent programs.

### 8D-007 — Golden Test Corpus and Balance Harness

The completed release records:

- nine verified component packs;
- 3,717 passing checks;
- 259 active canonical cases;
- 220 exact product baselines;
- 39 executed regression cases;
- 18 RNG conformance cases;
- 339 approved baseline objects;
- 21 retained E4 simulation runs;
- 3,080,000 retained candidate trials;
- seven replay bundles;
- seven closed controls;
- zero unexpected findings;
- zero open owner-action review items;
- 957 final acceptance checks;
- zero failures.

This proves the governed regression and balance-harness release.

It does not prove:

- final balance;
- sufficient human playtesting;
- final Canon 1.0;
- production performance;
- user-interface quality.

### 8D-008 — AI Development Team Operating Package

The completed package provides:

- permanent team roles;
- staffing modes;
- authority and approval rules;
- source-of-truth registry;
- context loading;
- work orders;
- quality gates;
- change and security controls;
- handoff and recovery;
- startup assets;
- operating manual;
- reference tools.

The release represents 9,403 component acceptance checks and a final package validation with zero failures.

It creates a governable AI-development operating environment. It does not mean a permanent autonomous development team is continuously active.

## 73.11 Phase 8E — Domain and content completion

Phase 8E handled the remaining major content domains and cross-domain validation.

The work addressed, among other areas:

- species and forms;
- items;
- creatures;
- NPCs;
- vehicles;
- mecha;
- starships;
- settings;
- regions;
- locations;
- environments;
- factions;
- cultures;
- lore;
- history;
- adventures;
- campaigns;
- scenes;
- clues;
- objectives;
- dependencies;
- release assembly.

## 73.12 8E-006 — Settings and adventures

The setting and adventure integration program established:

- shared setting baseline;
- cosmological relationships;
- world and Reality structure;
- regions, settlements, and locations;
- environments;
- factions, cultures, religions, lore, and timelines;
- adventure Definitions;
- campaign templates;
- scenes;
- routes;
- quests;
- clues;
- rewards;
- pack dependencies;
- integrated provider profiles.

The program preserved unresolved source claims instead of inventing missing worlds, labels, placements, or mechanics.

## 73.13 8E-007 — Cross-domain consolidation

8E-007 consolidated duplicate or overlapping:

- Actions;
- Effects;
- Conditions;
- Resources;
- progression structures;
- rules profiles;
- cross-domain mechanics.

**Status:** Complete at the canonical consolidation level.

## 73.14 8E-008 — Final domain validation

8E-008 validated:

- release structures;
- cross-pack dependencies;
- stable identities;
- schemas;
- installation;
- uninstallation;
- source coverage;
- provenance;
- cumulative compatibility.

**Status:** Complete.

The validation does not authorize public release or prove production runtime performance.

## 73.15 8E-009 — Canonical Object Template and CSV-first Program

The completed 8E-009 program records:

- 20 governed datasets;
- 19,199 source rows;
- 19,199 promoted records;
- zero unprocessed rows;
- zero partially processed datasets;
- deterministic canonical identity;
- passing source-coordinate uniqueness;
- passing registry-identity uniqueness;
- passing provenance;
- passing runtime validation;
- passing installation;
- passing uninstallation;
- zero unintended uninstall residue.

The final reconciliation SHA-256 is:

`112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40`

**Status:** Complete.

This proves processing of the registered 20 datasets. It does not prove that no unregistered legacy source contains additional material.

## 73.16 Phase 9 architecture packages

The canonical Phase 9 package delivered the application-readiness architecture.

Completed packages include:

- P9-01 entitlements and freemium architecture;
- sponsored-month amendment;
- P9-02 authoritative-session architecture;
- P9-03 technology and service decision;
- P9-04 Postgres-centered provider-neutral architecture contract;
- P9-05 bounded technical spike and cost envelope;
- P9-06 implementation backlog and acceptance gates.

**Status:** Complete as architecture and implementation planning.

## 73.17 P9-01 — Entitlements

P9-01 established:

- subscriptions;
- sponsored months;
- campaign grants;
- restrictions;
- cancellation;
- portability;
- ability-tier access;
- entitlement history;
- provider-neutral evaluation.

The approved free-access policy permits the first two ability-tree tiers, including abilities received through grants, unless another approved access source applies.

## 73.18 P9-02 — Authoritative sessions

P9-02 established:

- server-authoritative commands;
- two-device multiplayer;
- role-filtered projections;
- hidden information;
- reconnect;
- checkpoints;
- deterministic recovery;
- transport abstraction.

## 73.19 P9-03 and P9-04 — Technology direction

The owner-approved architecture class is Postgres-centered and provider-neutral.

The architecture establishes:

- stable internal identity;
- transactional persistence;
- ordered session commands;
- append-only evidence;
- realtime abstraction;
- backup and restore;
- provider exit;
- security;
- migration;
- observability.

No particular production provider is authorized by this decision.

## 73.20 P9-05 — Bounded technical spike

The bounded technical spike established a planning cost envelope of:

- target: **$0–$25 per month**;
- owner review required above **$35 per month**.

These are guardrails, not spending authorization.

## 73.21 P9-06 — Implementation program

P9-06 converted the architecture into an ordered repository implementation program with:

- seven workstreams;
- twenty-four planned backlog items;
- eight acceptance gates.

John Brandon Turner authorized bounded implementation of P9-06-001 through P9-06-023.

The authorization excludes:

- paid services;
- production deployment;
- public release;
- production credentials;
- unapproved spending;
- irreversible vendor coupling.

## 73.22 Completed application repository foundations

Repository evidence verifies the following merged application work:

1. **P9-06-001 — Repository baseline**  
   PR #71  
   Commit `d5d74140704115acebb03f4a899e3abf2d378b26`

2. **P9-06-002 — Local development environment contract**  
   PR #72  
   Commit `0225d90959fc77baa5b895dcbefeea0f55b2ba4d`

3. **P9-06-003 — Secrets and environment isolation**  
   PR #73  
   Commit `97a90ba1204125d4baf2be1763f9fc78f4dc301f`  
   Acceptance Gate AG-01 complete.

4. **P9-06-004 — Identity service port**  
   PR #74  
   Commit `f06d8733ba7478f58b82fa523e55d51ec8a72a66`

5. **P9-06-005 — Entitlement service port**  
   PR #75  
   Commit `4e7934a4ad6fef2a31c2e6ecab5a66c838e160af`

6. **P9-06-006 — Persistence and migration ports**  
   PR #76  
   Commit `f8a34a43e58dd7d12f2eb2602e80c4aeacce8034`

7. **P9-06-007 — Realtime and authoritative-session ports**  
   PR #77  
   Squash commit `149b866f530f3a8896170bfe3ba6af0c01fb2f72`

**Status:** Complete and merged through P9-06-007.

## 73.23 Completed Stage A repository work

The application repository also contains verified Stage A work.

### Stage A A0 — UI Baseline Audit

The A0 audit established that the previous client was a placeholder and that the repository had:

- zero verified product routes;
- zero verified Multiversal product screens;
- zero verified reusable product components;
- zero verified end-to-end product workflows.

The audit prevented structural placeholders and platform spike evidence from being mistaken for the product.

**Status:** Complete.

### Stage A A1 — Client Foundation

The repository records a merged client-foundation change:

- PR #69;
- commit `398f4d14fc189f8fc786aa093377a96e01d28548`;
- portable React/Vite client;
- shared UI primitives;
- responsive shell;
- recoverable application states;
- interaction tests;
- automated accessibility checks;
- responsive contracts;
- governed dependency installation.

**Status:** Foundation implemented and merged.

This does not mean the remaining Stage A screens or workflows are complete.

## 73.24 Completed governed repository bootstrap

The project also completed governed repository and startup packages, including:

- MS-01 WP-004 Governed Repository Bootstrap;
- startup instructions;
- contributor authority;
- repository-first recovery;
- current-roadmap authority;
- bounded Apple preparation.

These assets reduce the risk that a future conversation restarts completed work or acts on stale handoff text.

## 73.25 What is not complete

The following remain incomplete unless later repository evidence says otherwise:

- the rest of the P9-06 implementation backlog;
- complete database schema and runtime services;
- backup, restore, and provider-exit ports;
- full identity and entitlement implementations;
- full authoritative command handler;
- hosted realtime;
- complete universal object experience;
- character, campaign, scene, combat, inventory, investigation, social, world-builder, and AI interfaces;
- internal-alpha acceptance;
- closed alpha;
- beta;
- production;
- public release.

## 73.26 Completion boundary

The project has completed an unusually large amount of source, architecture, canonicalization, testing, governance, and operating preparation.

The remaining program is primarily:

- verified repository implementation;
- full application integration;
- internal testing;
- release hardening;
- platform certification;
- commercial and public readiness.

## 73.27 Controlling references

- active Multiversal New Conversation Bootstrap
- Application Implementation Roadmap
- Canonical Object Template Program
- 8D-007 completion release
- 8D-008 AI Development Team Operating Package
- 8E-008 final validation
- 8E-009 completion governance
- application repository commits and merged pull requests
- Stage A A0 UI Baseline Audit
- Stage A A1 client-foundation merge evidence

**Status:** Canonical project-completion record through the currently verified repository state.

---

# 74. Current Implementation Program

## 74.1 Purpose

Define the exact active implementation program, repository truth, execution order, current completed boundary, current next task, ordinary continuation behavior, owner-only stop conditions, and the relationship between Phase 9 services and Stage A product implementation.

## 74.2 Active repositories

The canonical repositories are:

### Application

`cybalicistjt-stack/Multiversal-app`

This repository is the primary source of truth for active implementation.

### Governance and AIOC

`cybalicistjt-stack/multiversal-aioc`

This repository governs:

- authority;
- roadmaps;
- current-state recovery;
- canonical planning;
- AI-team behavior;
- object-system programs;
- Development Brain;
- source recovery.

## 74.3 Repository-first rule

Before continuing material implementation, the active agent should verify:

- current default-branch commit;
- recent commits;
- open pull requests;
- active branches;
- CI;
- current roadmap;
- current bootstrap;
- relevant handoff records.

When a handoff or summary conflicts with newer repository evidence, the newer verified repository evidence controls.

## 74.4 Current active workstream

The active workstream is:

> **P9-06 bounded application implementation**

The work occurs primarily in `Multiversal-app`.

The program implements the provider-neutral foundations required before complete product integration.

## 74.5 Verified completed boundary

The current verified default-branch head remains:

`149b866f530f3a8896170bfe3ba6af0c01fb2f72`

This is the merged P9-06-007 realtime and authoritative-session ports release.

No newer application commit was found during the latest repository verification used for this chapter.

## 74.6 Current next executable action

The active roadmap and bootstrap identify the next task as:

> **P9-06-008 — Implement backup, restore, and provider-exit export ports.**

Required characteristics include:

- provider-neutral interfaces;
- deterministic backup manifest;
- integrity checksums;
- restore planning;
- restore validation;
- restore execution;
- restore receipts;
- provider-exit export;
- identity mappings;
- entitlement data;
- session state;
- audit and provenance;
- schema and version metadata;
- recovery and corruption failures;
- schemas;
- fixtures;
- validator;
- dedicated CI;
- no hosted provider;
- no credentials;
- no paid service;
- no production data;
- no deployment.

## 74.7 Stale backlog conflict

An older P9-06 backlog JSON assigns the label P9-06-008 to an initial logical schema migration.

The newer active roadmap and active bootstrap assign P9-06-008 to backup, restore, and provider-exit ports.

The project’s recovery rule says newer verified repository governance and roadmap evidence control when older handoff or planning records conflict.

Therefore the active implementation should follow the newer roadmap definition.

The conflicting older record should remain preserved as historical planning evidence rather than silently rewritten.

## 74.8 Execution authorization

John Brandon Turner authorized bounded implementation through P9-06-023.

The agent may:

- inspect repositories;
- create bounded branches;
- update files;
- add tests;
- run validation;
- inspect CI;
- repair ordinary failures;
- open pull requests;
- merge verified work through repository-permitted methods;
- continue through dependency order.

## 74.9 Prohibited implementation actions

The authorization does not permit:

- paid-provider enrollment;
- purchasing;
- production credentials;
- production deployment;
- public release;
- internal-alpha release without its gate;
- irreversible vendor coupling;
- public claims beyond evidence;
- owner-reserved canon or product-scope decisions.

## 74.10 Continue behavior

Within the active program, “Continue” means:

1. verify current repository state;
2. identify the exact unfinished dependency-ordered item;
3. execute repository work in the current response;
4. run tests and CI;
5. repair ordinary failures;
6. merge only after required evidence passes;
7. update governance if stale;
8. report the exact next task.

A “Continue” response should not substitute a plan for executable work when repository tools are available.

## 74.11 Ordinary ambiguity

The owner has approved using the assistant’s best recommendation for ordinary reversible ambiguity.

The agent should:

- choose the most reasonable compatible option;
- preserve provider neutrality;
- record the choice where material;
- continue;
- stop only for a genuine owner-only gate.

## 74.12 Failure behavior

An ordinary failure should trigger:

- log inspection;
- root-cause diagnosis;
- repair;
- targeted rerun;
- full required rerun;
- retained failure evidence.

The agent should not stop merely because the first attempt failed.

## 74.13 Workstream relationship

The implementation program combines two related tracks.

### Phase 9 service foundation

Builds:

- environment safety;
- identity;
- entitlement;
- persistence;
- migration;
- realtime;
- sessions;
- backup;
- restore;
- provider exit;
- authorization;
- telemetry;
- recovery.

### Stage A product implementation

Builds:

- client foundation;
- design system;
- universal object experience;
- identity and dashboards;
- character workspace;
- campaign and scene workspace;
- proposal and approval loop;
- combat;
- inventory and vehicles;
- investigation and social;
- world and content tools;
- contextual AI;
- internal-alpha hardening.

The tracks should converge through tested vertical slices.

## 74.14 Stage A current state

Verified Stage A state includes:

- A0 baseline audit complete;
- A1 client foundation merged.

Remaining Stage A work includes:

- universal object experience;
- identity, dashboard, and permissions integration;
- character workspace;
- campaign and scene builder;
- live approval loop;
- combat;
- inventory and vehicles;
- investigation and social;
- world and content tools;
- contextual AI;
- hardening.

## 74.15 Stage A vertical-slice rule

Every Stage A batch must include:

- navigation;
- real governed data;
- actions;
- permissions;
- persistence;
- loading and error states;
- offline or recovery behavior where applicable;
- desktop and mobile behavior;
- automated tests;
- reproducible preview;
- owner review.

Disconnected mock screens do not satisfy Stage A.

## 74.16 P9 and Stage A sequencing

The project should not wait for every theoretical backend feature before building visible vertical slices.

It should also not build product screens that bypass unfinished service contracts.

The correct pattern is:

1. implement the next required provider-neutral service boundary;
2. connect it to the smallest meaningful real workflow;
3. validate permissions, persistence, and recovery;
4. expand through dependency order.

## 74.17 Current service foundation

Verified port foundations exist for:

- identity;
- entitlement;
- persistence;
- migration;
- realtime;
- authoritative sessions.

These are interface and contract foundations.

They do not yet prove complete production adapters or complete end-to-end workflows.

## 74.18 Next service foundation

Backup, restore, and provider-exit export ports are the next active service boundary.

This work is important because later internal-alpha state should not be trusted before:

- backup can be created;
- integrity can be verified;
- restore can be rehearsed;
- provider exit can preserve identity and history.

## 74.19 Later Phase 9 implementation sequence

After the active task, later work should continue in dependency order through authorized items covering, as applicable:

- concrete schema;
- deterministic fixtures;
- migration checks;
- identity mapping;
- authorization;
- entitlements;
- session command handling;
- ordered delivery;
- hidden information;
- reconnect;
- telemetry;
- cost controls;
- provider-exit rehearsal;
- two-device acceptance.

Exact numbering and wording should be read from the current active roadmap and repository at execution time.

## 74.20 Current implementation claims

The project may accurately claim:

- substantial canonical content is complete;
- Phase 8 is complete;
- Phase 9 architecture packages are complete;
- Stage A A0 and A1 are complete;
- P9-06-001 through P9-06-007 are merged;
- provider-neutral port foundations exist through authoritative sessions.

The project must not claim:

- the application is complete;
- internal alpha is ready;
- production is deployed;
- public users can use the platform;
- complete GM and Player workflows exist;
- backup and provider exit are implemented;
- commercial readiness is complete.

## 74.21 Current branch and PR policy

Active work should:

- use a bounded branch;
- preserve work-order identity;
- avoid direct main changes;
- run repository-owned validation;
- use independent review where required;
- merge through the repository-permitted strategy;
- preserve final commit evidence.

The application repository may require squash merges.

## 74.22 Current governance maintenance

When repository implementation advances, the agent should update stale governance through a verified change.

Important current-state files should not continue to report an earlier phase after newer work merges.

## 74.23 Cost and provider boundary

The current program remains local and provider-neutral.

It should not create:

- hosted database accounts;
- paid storage;
- production identity tenants;
- paid realtime;
- paid AI;
- production domains.

A later owner gate may authorize a bounded provider activation.

## 74.24 Internal-alpha boundary

Implementation through P9-06-023 is not the same as releasing internal alpha.

Internal-alpha release requires:

- acceptance evidence;
- security and privacy review;
- backup and restore;
- two-device behavior;
- owner decision;
- controlled tester documentation;
- known-risk disclosure.

## 74.25 Parallel Apple boundary

The WP-011 Apple spike remains separate from the main critical path.

Most implementation should proceed without waiting for the borrowed Mac.

The Mac is reserved for the small set of Xcode, signing, provisioning, simulator, device, packaging, and certification tasks that cannot be completed elsewhere.

## 74.26 Reporting requirement

After each verified repository item, report:

- exact backlog item;
- files or capabilities added;
- tests;
- CI;
- PR;
- merge or squash commit;
- restrictions preserved;
- exact next task.

## 74.27 Controlling references

- Multiversal New Conversation Bootstrap v4.0
- Application Implementation Roadmap v2.0
- Stage A UI Implementation Program
- Stage A A0 UI Baseline Audit
- Stage A A1 merge evidence
- current application repository commit history
- P9-04 architecture contract
- P9-06 owner authorization
- repository-first recovery rule

**Status:** Active canonical implementation program as of the latest verified repository state.

---

# 75. Acceptance Gates

## 75.1 Purpose

Define the formal gates that separate repository safety, provider-neutral foundations, data readiness, identity and entitlement correctness, authoritative sessions, operational recovery, two-device internal alpha, owner release decisions, Stage A workflow completion, and later public-release readiness.

## 75.2 Gate principle

A gate is satisfied only by evidence.

Evidence may include:

- repository files;
- test results;
- CI;
- artifacts;
- checksums;
- migration receipts;
- restore drills;
- review records;
- owner approval;
- merge evidence;
- reproducible interaction.

A plan, conversation, partial implementation, or green unrelated test does not satisfy a gate.

## 75.3 Gate families

The project uses several related gate families:

- P9-06 implementation acceptance gates;
- 8D-008 quality gates;
- 8D-007 regression gate;
- Stage A exit conditions;
- internal-alpha readiness gates;
- release and owner decision gates;
- platform-specific gates.

## 75.4 AG-01 — Repository Safety

AG-01 requires:

- protected baseline verified;
- no secrets committed;
- local environment reproducible.

Verified evidence includes:

- P9-06-001 repository baseline;
- P9-06-002 local development contract;
- P9-06-003 secrets and environment isolation;
- merged PRs #71–73;
- repository validation.

**Status:** Complete.

## 75.5 AG-02 — Provider-Neutral Boundaries

AG-02 requires the governed service boundaries and adapter isolation.

Evidence should include:

- provider-neutral interfaces;
- no provider SDK leakage into domain contracts;
- stable internal types;
- schemas;
- fixtures;
- validators;
- contract tests;
- CI.

Verified foundations currently exist for:

- identity;
- entitlement;
- persistence;
- migration;
- realtime;
- authoritative sessions.

The complete gate state should be determined from the current repository and active gate definition, not inferred solely from the existence of six merged items.

## 75.6 AG-03 — Data Foundation

AG-03 requires, according to the governing active implementation package:

- required logical schema representation;
- migration compatibility;
- deterministic fixtures;
- reset behavior;
- backup and restore;
- export;
- zero unintended residue;
- validation.

Because the active roadmap reassigns the current next item to backup, restore, and provider-exit ports, AG-03 remains incomplete unless newer repository evidence proves otherwise.

## 75.7 AG-04 — Identity and Entitlements

AG-04 requires:

- provider-independent user identity mapping;
- campaign isolation;
- row or equivalent authorization;
- subscription behavior;
- sponsored-month behavior;
- campaign grants;
- cancellation;
- entitlement transitions;
- permission-safe tests.

The current identity and entitlement ports are foundations. Full gate completion requires concrete behavior and tests.

## 75.8 AG-05 — Authoritative Sessions

AG-05 requires:

- server authority;
- idempotent commands;
- stale-command safety;
- ordered events;
- hidden-information protection;
- reconnect;
- deterministic restoration;
- checkpoints;
- two-role projections;
- acceptance tests.

The current realtime and session ports are foundations. They do not by themselves satisfy all AG-05 behavior.

## 75.9 AG-06 — Operations and Exit

AG-06 requires:

- structured audit;
- operational telemetry;
- cost monitoring;
- backup verification;
- restore;
- provider-exit rehearsal;
- export completeness;
- replacement-adapter procedure.

**Status:** Incomplete unless later repository evidence proves otherwise.

## 75.10 AG-07 — Two-Device Alpha

AG-07 requires:

- two distinct devices or clients;
- separate identities;
- Player and GM roles;
- synchronized session;
- action proposal;
- GM approval, denial, or modification;
- hidden-information safety;
- disconnect and reconnect;
- deterministic recovery;
- zero unexpected blocking failures.

**Status:** Incomplete.

## 75.11 AG-08 — Owner Release Decision

AG-08 requires:

- complete evidence package;
- known risks;
- current limitations;
- internal-alpha scope;
- rollback;
- recovery;
- tester documentation;
- owner decision.

No technical subsystem may self-authorize this gate.

**Status:** Owner-gated and incomplete.

## 75.12 8D-007J regression gate

The 8D-007J Golden Test Corpus and Balance Harness remains a blocking gate for affected:

- rules;
- content;
- schemas;
- migrations;
- deterministic runtime;
- balance baselines;
- release candidates.

The expected outputs may not be changed merely to make a test pass.

## 75.13 8D-008 quality gates

The AI operating program defines eighteen quality gates across:

- packet eligibility;
- context;
- authority;
- workspace isolation;
- scope;
- static analysis;
- tests;
- schemas;
- deterministic replay;
- migration;
- security;
- privacy;
- dependencies;
- accessibility;
- performance;
- simulation;
- independent review;
- provenance;
- merge and release integrity.

These gates apply according to work type.

## 75.14 Stage A A0 exit gate

A0 required an evidence-based audit of the actual repository.

It established:

- framework and workspace state;
- implemented routes and screens;
- component state;
- services;
- mock data;
- accessibility;
- platform boundaries;
- blockers;
- ordered next work.

**Status:** Complete.

## 75.15 Stage A A1 exit gate

A1 requires a reusable client and design-system foundation.

Evidence includes:

- portable client;
- approved framework;
- build;
- tests;
- reusable primitives;
- responsive shell;
- accessibility behavior;
- recoverable application states;
- platform composition boundary.

The repository records the merged A1 client foundation.

**Status:** Complete at foundation level.

## 75.16 Stage A A2 exit gate

A2 requires a real universal object vertical slice.

A user must be able to:

- browse;
- search;
- filter;
- open;
- inspect;
- review provenance;
- traverse relationships;
- select an object;
- pass it into another workflow;
- use desktop and mobile.

**Status:** Incomplete unless later repository evidence proves otherwise.

## 75.17 Stage A A3 exit gate

A3 requires:

- identity entry;
- dashboard;
- workspace selection;
- campaign and character selection;
- notifications;
- invitations;
- permissions enforced at service level.

**Status:** Incomplete.

## 75.18 Stage A A4 exit gate

A4 requires a player to:

- create;
- open;
- modify;
- save;
- validate;
- advance;
- use a character in a scene.

**Status:** Incomplete.

## 75.19 Stage A A5 exit gate

A5 requires a GM to:

- create a campaign;
- invite a player;
- build a scene;
- add real governed objects;
- save;
- reopen;
- launch the scene into a live session.

**Status:** Incomplete.

## 75.20 Stage A A6 exit gate

A6 requires the full vertical slice:

> Campaign → Character → Scene → Action proposal → GM inspection, modification, or approval → Result → synchronized persistent state

The workflow must survive save and reload.

**Status:** Incomplete.

## 75.21 Stage A A7 exit gate

A7 requires a complete encounter without development-only tools.

It includes:

- timing or initiative;
- actions;
- targets;
- movement;
- resources;
- conditions;
- NPC actions;
- GM review;
- rules inspection;
- history;
- persistence;
- reconnect.

**Status:** Incomplete.

## 75.22 Stage A A8 exit gate

A8 requires:

- personal inventory;
- shared inventory;
- ownership;
- transfers;
- equipment;
- crafting;
- repair;
- salvage;
- vehicles;
- no duplication or loss.

**Status:** Incomplete.

## 75.23 Stage A A9 exit gate

A9 requires persistent noncombat play through:

- clues;
- evidence;
- hypotheses;
- hidden information;
- relationships;
- faction standing;
- reputation;
- promises;
- debts;
- social conditions.

**Status:** Incomplete.

## 75.24 Stage A A10 exit gate

A10 requires governed content creation through:

- create;
- clone;
- vary;
- relate;
- validate;
- preview;
- submit;
- package;
- approval-gated promotion.

**Status:** Incomplete.

## 75.25 Stage A A11 exit gate

A11 requires contextual AI that is:

- permission-aware;
- source-linked;
- visibly proposed;
- reversible;
- bounded;
- approval-gated.

**Status:** Incomplete.

## 75.26 Stage A A12 exit gate

A12 requires internal-alpha hardening across:

- accessibility;
- responsive layouts;
- performance;
- large-corpus behavior;
- reconnect;
- offline behavior;
- permissions;
- destructive actions;
- autosave;
- recovery;
- onboarding;
- help;
- telemetry;
- consistency.

**Status:** Incomplete.

## 75.27 Internal-alpha content gate

Internal alpha should not begin with empty or misleading content.

The content gate should verify:

- required canonical packs;
- campaign fixture;
- character options;
- creatures;
- items;
- environments;
- scenes;
- rules;
- visible provenance;
- installation and migration.

## 75.28 Internal-alpha data gate

The data gate should verify:

- stable IDs;
- schemas;
- migrations;
- deterministic fixtures;
- backup;
- restore;
- provider exit;
- current projections;
- event history;
- zero unintended residue.

## 75.29 Internal-alpha security gate

The security gate should verify:

- identity;
- deny-by-default authorization;
- campaign isolation;
- hidden information;
- secret isolation;
- audit;
- upload and pack validation;
- dependency review;
- no production credentials in clients;
- incident procedures.

## 75.30 Internal-alpha recovery gate

The recovery gate should verify:

- autosave;
- draft recovery;
- reconnect;
- checkpoint;
- restore drill;
- backup integrity;
- stale command handling;
- duplicate command handling;
- session recovery;
- provider-exit artifact.

## 75.31 Internal-alpha accessibility gate

The accessibility gate should verify core workflows through:

- keyboard;
- screen reader;
- touch;
- text scaling;
- reduced motion;
- noncolor indicators;
- responsive layouts;
- map and graph alternatives;
- error recovery.

A formal conformance claim requires current audit evidence.

## 75.32 Internal-alpha performance gate

The performance gate should use:

- actual governed content corpus;
- realistic characters;
- realistic scenes;
- multiple participants;
- large inventory;
- relationship graph;
- index and search;
- reconnect;
- backup and restore.

## 75.33 Internal-alpha documentation gate

Testers need:

- onboarding;
- account and access instructions;
- current supported workflows;
- known limitations;
- issue-reporting process;
- privacy guidance;
- recovery instructions;
- data-retention explanation;
- support contact;
- version identity.

## 75.34 Owner decision gate

The owner decision should receive:

- exact release candidate;
- build and commit;
- test and gate summary;
- known failures;
- security findings;
- privacy scope;
- cost;
- tester count;
- content scope;
- rollback;
- backup and restore evidence;
- recommendation.

## 75.35 Gate status presentation

Every gate should be represented as:

- complete;
- incomplete;
- blocked;
- expired;
- not applicable;
- owner decision pending.

A partially implemented foundation should not be labeled complete for the broader gate.

## 75.36 Gate regression

A completed gate may reopen when:

- implementation changes materially;
- security advisory appears;
- schema changes;
- provider changes;
- migration changes;
- content pack changes;
- release candidate changes;
- approval expires.

## 75.37 No gate bundling by assumption

Passing AG-01 does not satisfy AG-02.

Passing port contract tests does not satisfy end-to-end session behavior.

Passing automated accessibility checks does not prove human accessibility validation.

Passing internal alpha does not authorize public launch.

## 75.38 Current gate summary

At the latest verified state:

- AG-01: complete;
- AG-02: foundations present; final status requires exact current gate evidence;
- AG-03: incomplete;
- AG-04: incomplete;
- AG-05: incomplete;
- AG-06: incomplete;
- AG-07: incomplete;
- AG-08: owner-gated and incomplete;
- Stage A A0: complete;
- Stage A A1: complete;
- Stage A A2–A12: incomplete unless newer evidence proves otherwise.

## 75.39 Controlling references

- P9-06 acceptance-gate package
- active Application Implementation Roadmap
- Stage A UI Implementation Program
- Stage A A0 audit
- Stage A A1 repository evidence
- 8D-007J Golden Test Corpus
- 8D-008G Quality Gate Catalog
- security, backup, recovery, accessibility, and release chapters
- owner release-decision boundary

**Status:** Canonical acceptance-gate architecture and current evidence-aware status summary.

---

# 76. Internal Alpha

## 76.1 Purpose

Define the first controlled release in which authorized internal testers use integrated Multiversal workflows with durable state, real governed content, two-device session behavior, recovery, issue reporting, and explicit owner-approved limitations.

Internal alpha is a product-validation stage. It is not a public launch.

## 76.2 Internal-alpha objective

Internal alpha should answer:

- Can a Player and GM complete the core tabletop workflows?
- Does state remain correct?
- Does hidden information remain protected?
- Can users recover after interruption?
- Can the team diagnose defects?
- Are the most important interfaces understandable and accessible?
- Does the current cost and provider architecture remain acceptable?
- Is the platform ready for a broader closed alpha?

## 76.3 Entry authority

Internal alpha requires explicit owner approval.

Repository implementation authorization does not authorize internal-alpha release.

The owner decision must bind to:

- exact release candidate;
- exact environment;
- tester scope;
- content scope;
- cost;
- limitations;
- data and privacy policy;
- backup and rollback;
- start and end conditions.

## 76.4 Tester scope

Internal alpha should begin with a small controlled group.

Testers may include:

- owner;
- trusted GM;
- trusted players;
- approved internal creators;
- technical reviewers.

The tester list should be explicit.

Invitation to internal alpha must not become public registration.

## 76.5 Environment

The internal-alpha environment should be isolated from:

- development;
- preview;
- production;
- public services.

It should have:

- separate configuration;
- separate credentials;
- separate data;
- limited access;
- observability;
- backup;
- restore;
- documented shutdown.

## 76.6 Provider boundary

Internal alpha may use:

- local or privately hosted adapters;
- free-tier providers when separately approved;
- controlled direct-connect or relay behavior;
- isolated storage;
- test identity.

It must not automatically enroll in paid services or exceed the approved cost gate.

## 76.7 Release candidate

The internal-alpha candidate should identify:

- application version;
- commit;
- build artifact;
- schemas;
- migrations;
- pack versions;
- content scope;
- environment configuration;
- feature flags;
- known limitations;
- checksums.

## 76.8 Minimum core workflow

The minimum integrated core is:

1. identity entry;
2. correct workspace;
3. campaign selection;
4. character creation or selection;
5. GM scene preparation;
6. Player session entry;
7. action proposal;
8. GM inspection;
9. approve, deny, or modify;
10. accepted result;
11. synchronized persistent state;
12. disconnect;
13. reconnect;
14. safe resumption.

Without this loop, the release is a technical preview rather than the intended internal alpha.

## 76.9 Campaign workflow

A GM should be able to:

- create or open a campaign;
- configure rules and packs;
- invite a Player;
- assign or approve a character;
- create a session;
- prepare a scene;
- save;
- reopen;
- launch.

## 76.10 Character workflow

A Player should be able to:

- create a draft;
- select campaign and rules context;
- make legal choices;
- validate;
- save;
- submit if approval is required;
- reopen;
- use the character;
- preserve history.

## 76.11 Scene workflow

A GM should be able to:

- select real governed content;
- add creatures or NPCs;
- add environments;
- add objectives or clues;
- configure hidden information;
- add a map or use theater of the mind;
- preview Player view;
- validate;
- launch.

## 76.12 Session workflow

The session should support:

- separate Player and GM identities;
- role-filtered projections;
- proposal;
- calculation;
- approval;
- modification;
- denial;
- result;
- event history;
- reconnect;
- checkpoint.

## 76.13 Combat scope

Internal alpha should include enough combat to test:

- timing or initiative;
- actions;
- targets;
- movement or zones;
- resources;
- conditions;
- NPC or enemy actions;
- GM adjudication;
- encounter end.

The first alpha need not include every optional combat subsystem.

## 76.14 Noncombat scope

Internal alpha should test at least one structured noncombat workflow.

Examples include:

- investigation;
- social interaction;
- exploration;
- downtime;
- crafting.

The selected workflow should produce persistent consequences.

## 76.15 Inventory and ownership

The alpha should test:

- item acquisition;
- ownership;
- custody;
- equipment;
- transfer;
- shared asset;
- no duplication;
- save and reload.

## 76.16 Content scope

The internal-alpha content set should be bounded.

It should include enough real content to exercise:

- character creation;
- actions;
- creatures;
- items;
- environments;
- a campaign;
- scenes;
- rules;
- relationships;
- packs.

The content set should be version-pinned for reproducibility.

## 76.17 Canon boundary

Internal alpha uses approved canonical or clearly marked test content.

Testers should be able to distinguish:

- canonical content;
- campaign-local content;
- sample content;
- temporary fixture;
- AI proposal.

Alpha feedback does not automatically change canon.

## 76.18 Identity and permissions

The release should verify:

- stable internal subject identity;
- campaign membership;
- Player and GM roles;
- character control;
- creator permissions where enabled;
- owner-only gates;
- revocation;
- denied access.

## 76.19 Hidden information

The alpha must test hidden information across:

- scene objects;
- map layers;
- clues;
- NPC motives;
- conditions;
- GM notes;
- search;
- notifications;
- AI context;
- exports;
- reconnect.

A hidden-information failure is a release-blocking defect.

## 76.20 Entitlements

The alpha should test the approved access model, including:

- free tier;
- ability tiers one and two;
- campaign grants;
- sponsored access if enabled;
- expiration;
- restricted content;
- historical-state preservation.

No billing is required merely to test entitlement behavior.

## 76.21 Persistence

Accepted state must survive:

- page reload;
- client restart;
- temporary network loss;
- server restart where in scope;
- session pause;
- scene transition;
- checkpoint.

## 76.22 Backup

Before trusting internal-alpha data, the environment should have:

- backup procedure;
- manifest;
- integrity verification;
- retention;
- authorization;
- operational receipt.

## 76.23 Restore drill

A successful restore drill should occur before testers are told that their data is durable.

The drill should verify:

- identities;
- campaigns;
- characters;
- packs;
- events;
- snapshots;
- permissions;
- indexes;
- representative workflow.

## 76.24 Provider exit

The alpha environment should be able to export sufficient provider-neutral data to avoid trapping the project or testers in one provider.

The export should preserve:

- internal IDs;
- state;
- events;
- pack versions;
- identity mappings;
- entitlements;
- media metadata;
- schemas;
- checksums.

## 76.25 Reconnect and recovery

Test scenarios should include:

- Player disconnect before submission;
- Player disconnect after submission;
- Player disconnect after commit;
- GM disconnect with pending approval;
- stale client;
- duplicate command;
- reconnect after missed events;
- restore from checkpoint;
- recovery after service restart.

## 76.26 Error states

Core workflows must include usable:

- loading;
- empty;
- error;
- offline;
- forbidden;
- stale;
- migration-required;
- recovery states.

An internal alpha that works only on the happy path does not satisfy the purpose.

## 76.27 Accessibility

Internal-alpha primary workflows should be tested for:

- keyboard;
- touch;
- focus;
- screen reader;
- text scaling;
- reduced motion;
- contrast;
- noncolor status;
- mobile layout;
- map alternatives.

The project should label the evidence accurately and avoid claiming formal conformance without a complete audit.

## 76.28 Responsive behavior

The alpha should test at least:

- desktop browser;
- mobile browser;
- tablet or equivalent responsive layout;
- two-device Player and GM combination.

Native packaging is not required for the web-based internal-alpha gate unless separately approved.

## 76.29 Performance

Performance testing should use:

- real governed content;
- representative characters;
- representative scene;
- multiple participants;
- realistic event history;
- large-corpus object search;
- inventory;
- reconnect;
- backup.

## 76.30 Observability

The team should be able to diagnose:

- login failure;
- permission denial;
- proposal failure;
- persistence failure;
- realtime lag;
- reconnect failure;
- hidden-information defect;
- backup failure;
- restore failure;
- migration problem;
- cost threshold.

Logs must not expose protected content.

## 76.31 Cost

The alpha should operate within the approved bounded cost policy.

The evidence package should include:

- provider list;
- free or paid status;
- expected monthly cost;
- observed usage;
- storage;
- bandwidth;
- AI use;
- threshold alarms;
- exit cost.

Any paid commitment requires separate owner approval.

## 76.32 AI scope

AI may be disabled, local, or narrowly enabled during early internal alpha.

When enabled, AI must be:

- permission-aware;
- source-linked;
- clearly proposed;
- reversible;
- cost-limited;
- nonauthoritative.

The core tabletop loop must remain usable when AI is unavailable.

## 76.33 Tester onboarding

Testers should receive:

- access instructions;
- supported devices;
- current features;
- unsupported features;
- known issues;
- privacy expectations;
- data durability statement;
- issue-reporting process;
- emergency contact or shutdown instructions;
- version and environment identity.

## 76.34 Feedback collection

Feedback should classify:

- defect;
- usability issue;
- accessibility issue;
- rules ambiguity;
- content issue;
- performance issue;
- recovery issue;
- feature request;
- security or privacy issue.

A feature request should not be mixed with a release-blocking defect.

## 76.35 Defect severity

The internal-alpha process should define severity levels.

Release-blocking examples include:

- data loss;
- ownership duplication;
- hidden-information leakage;
- unauthorized access;
- unrecoverable session;
- corrupted migration;
- secret exposure;
- inability to complete the core loop.

## 76.36 Feedback provenance

Feedback should preserve:

- tester;
- version;
- environment;
- device;
- workflow;
- steps;
- expected result;
- actual result;
- screenshots or logs where safe;
- severity;
- disposition.

## 76.37 Change control during alpha

Alpha fixes should use the same:

- work orders;
- branches;
- tests;
- review;
- gates;
- migration controls;
- release evidence.

The existence of testers does not justify uncontrolled hot fixes.

## 76.38 Update policy

An alpha update should identify:

- version;
- change;
- migration;
- downtime;
- backup;
- rollback;
- known risk;
- tester action.

## 76.39 Data reset policy

A reset may be allowed in early alpha only when:

- testers were informed;
- backup and export obligations are met;
- purpose is explicit;
- owner approves if user data is materially affected;
- the reset is audited.

The project should not promise durable campaign history while routinely discarding it.

## 76.40 Privacy

Internal alpha should minimize data collection.

The project should define:

- identity data;
- campaign data;
- logs;
- AI provider data;
- backups;
- retention;
- access;
- deletion;
- export.

No public privacy claim should exceed the implemented policy.

## 76.41 Security review

Before opening alpha access, review:

- authentication;
- authorization;
- database isolation;
- client secrets;
- uploads;
- dependencies;
- logging;
- exports;
- backups;
- AI context;
- incident response.

## 76.42 Release checklist

The internal-alpha release checklist should include:

- exact candidate;
- all required gates;
- restore drill;
- two-device suite;
- tester documentation;
- cost;
- security and privacy review;
- accessibility evidence;
- known limitations;
- rollback;
- owner approval.

## 76.43 Owner decision packet

The owner packet should lead with:

- recommendation;
- exact tester scope;
- exact environment;
- exact candidate;
- cost;
- known risks;
- recovery proof;
- unsupported features;
- requested decision.

## 76.44 Alpha start

After approval, the release should:

- freeze the candidate;
- record approval;
- enable the environment;
- invite only approved testers;
- verify health;
- create initial backup;
- monitor;
- preserve the release receipt.

## 76.45 Alpha operations

During alpha, the team should maintain:

- issue triage;
- uptime and error monitoring;
- backup verification;
- cost monitoring;
- security event review;
- release notes;
- tester communication;
- current known-issue list.

## 76.46 Alpha pause

The owner or authorized incident process may pause alpha for:

- security issue;
- privacy issue;
- data loss;
- restore failure;
- cost breach;
- provider outage;
- invalid migration;
- hidden-information defect;
- owner hold.

## 76.47 Alpha end

The alpha should end with:

- final backup;
- export;
- issue summary;
- metrics;
- tester feedback;
- known risks;
- retained evidence;
- recommendation for closed alpha;
- owner decision.

## 76.48 Exit criteria

Internal alpha may be considered complete when:

- the core Player and GM loop works;
- state is durable;
- hidden information is protected;
- recovery works;
- two-device acceptance passes;
- core accessibility evidence exists;
- blocking defects are resolved or explicitly held;
- costs are understood;
- documentation exists;
- owner accepts the result.

## 76.49 What internal alpha does not prove

Internal alpha does not prove:

- public scalability;
- commercial readiness;
- legal readiness;
- full moderation;
- final UX;
- final accessibility;
- final balance;
- all devices;
- app-store readiness;
- production reliability;
- public support capacity.

## 76.50 Current status

Internal alpha has not been authorized or completed.

The current project remains in bounded implementation.

The internal-alpha architecture and gates are prepared so that the release can occur deliberately after the required repository evidence exists.

## 76.51 Controlling references

- Phase 13 Internal Alpha Completion roadmap
- P9-06 AG-07 and AG-08
- P9-02 authoritative-session scenarios
- P9-04 security, backup, restore, and provider-exit contract
- Stage A A0–A12
- internal-alpha hardening requirements
- owner release boundary
- accessibility, testing, security, privacy, deployment, and recovery chapters

**Status:** Canonical internal-alpha release architecture; entry remains incomplete and owner-gated.



# 77. Closed Alpha and Beta

## 77.1 Purpose

Define the controlled expansion from internal alpha to closed alpha and then beta, including entry criteria, participant scope, feature maturity, migration and recovery expectations, privacy and support obligations, defect thresholds, telemetry, content scope, and owner release gates.

## 77.2 Release progression

The release path should proceed through evidence-based stages:

1. Internal alpha.
2. Closed alpha.
3. Beta stabilization.
4. Commercial and public-release readiness.
5. Staged production launch.

A stage may be repeated or paused.

Passing a later build does not erase failed evidence from an earlier stage.

## 77.3 Closed-alpha objective

Closed alpha should answer:

- Can trusted users outside the immediate development loop complete the product’s primary workflows?
- Can multiple campaigns operate without cross-campaign leakage?
- Are onboarding and recovery understandable without direct developer guidance?
- Can the team receive, reproduce, triage, and repair real-use defects?
- Is the current architecture stable enough for a larger beta?
- Are provider cost, security, privacy, backup, and support demands understood?

## 77.4 Closed-alpha entry gate

Closed alpha requires:

- successful internal-alpha disposition;
- owner approval;
- exact release candidate;
- stable environment;
- backup and restore drill;
- provider-exit rehearsal appropriate to scope;
- two-device acceptance;
- permission and hidden-information validation;
- primary workflow accessibility evidence;
- controlled tester onboarding;
- known-risk register;
- rollback and shutdown plan.

## 77.5 Participant scope

Closed alpha should use invited participants only.

Participants may include:

- trusted Game Masters;
- trusted Players;
- approved content creators;
- accessibility reviewers;
- technical reviewers;
- owner-approved external testers.

The invitation system should preserve:

- inviter;
- intended role;
- campaign or program scope;
- expiry;
- acceptance;
- revocation;
- privacy acknowledgement;
- tester agreement where required.

## 77.6 Campaign scope

Closed alpha should support more than one campaign and more than one GM so the team can test:

- campaign isolation;
- different rules profiles;
- different content packs;
- varied session styles;
- different device combinations;
- independent world state;
- multiple ownership and permission patterns.

## 77.7 Product scope

Closed alpha should include stable versions of the primary workflows:

- account and workspace entry;
- character creation and advancement;
- campaign and scene building;
- Player action proposal;
- GM approval, denial, and modification;
- combat;
- inventory and shared assets;
- at least one structured investigation or social flow;
- content browsing and rules help;
- save, reconnect, and recovery.

Optional or experimental features should be feature-flagged and clearly labeled.

## 77.8 Content scope

The content set should be larger than internal alpha but still bounded and versioned.

It should include:

- a representative core-rules pack;
- several character paths;
- species and forms;
- abilities;
- items;
- creatures and NPCs;
- environments;
- adventures or campaign templates;
- vehicles or operational assets where tested;
- rules references;
- sample and owner-approved content.

## 77.9 Pack lifecycle

Closed alpha should test:

- installation;
- dependency validation;
- update;
- migration;
- blocked removal;
- safe removal;
- reinstall;
- campaign compatibility;
- content withdrawal;
- provider-exit export.

## 77.10 Migration expectations

Unlike an early disposable prototype, closed alpha should preserve tester state through normal updates.

Every update should define:

- source version;
- target version;
- affected data;
- backup;
- migration;
- validation;
- rollback or forward repair;
- tester-visible impact.

## 77.11 Data durability

Testers should receive an accurate statement about:

- what is backed up;
- expected retention;
- restore capability;
- planned maintenance;
- circumstances allowing reset;
- export availability;
- known limitations.

## 77.12 Recovery expectations

Closed alpha should test recovery from:

- interrupted update;
- failed migration;
- stale client;
- duplicate command;
- session disconnect;
- service restart;
- corrupted snapshot;
- missing media;
- index rebuild;
- entitlement transition.

## 77.13 Identity and account recovery

Closed alpha should validate:

- provider-independent internal subject identity;
- account linking where enabled;
- recovery;
- invitation acceptance;
- role changes;
- revocation;
- campaign removal;
- ownership transfer;
- account closure behavior.

## 77.14 Permissions and hidden information

The program should repeat permission tests across:

- multiple campaigns;
- multiple GMs;
- multiple Players;
- observers;
- content creators;
- assistant GMs;
- shared assets;
- private notes;
- hidden clues;
- maps;
- AI context;
- exports.

A hidden-information leak remains a release-blocking defect.

## 77.15 Entitlement behavior

Closed alpha may test:

- free access;
- campaign grants;
- sponsored access;
- restricted content;
- expiry;
- cancellation;
- historical-state preservation;
- offline entitlement snapshots.

Billing is not required to test the entitlement engine.

## 77.16 AI behavior

When AI is enabled, closed alpha should test:

- source grounding;
- role safety;
- campaign isolation;
- entitlement safety;
- visible proposal status;
- reversibility;
- cost;
- refusal and degraded behavior;
- non-AI fallback.

AI must remain optional for the core tabletop loop.

## 77.17 Accessibility program

Closed alpha should include dedicated accessibility testing across:

- Player and GM workflows;
- character creation;
- live sessions;
- combat;
- inventory;
- investigation;
- content browsing;
- error and recovery states;
- mobile and desktop.

The program should recruit testers with varied access needs where feasible.

## 77.18 Device matrix

The closed-alpha device matrix should include representative:

- desktop browsers;
- mobile browsers;
- tablets;
- keyboard and mouse;
- touch;
- screen readers;
- high zoom;
- reduced motion;
- low-powered devices;
- unstable networks.

Native Apple builds remain a separate platform track unless approved for the alpha.

## 77.19 Performance program

Closed alpha should measure:

- startup;
- campaign load;
- character load;
- object search;
- scene launch;
- command latency;
- GM approval latency;
- reconnect;
- map and graph performance;
- large inventory;
- backup;
- migration;
- index rebuild.

## 77.20 Reliability program

Reliability evidence should include:

- uptime appropriate to the test;
- successful command rate;
- reconnect success;
- backup verification;
- restore success;
- migration success;
- no duplicate inventory or effects;
- no unexpected cross-campaign access;
- incident response.

## 77.21 Observability

The team should maintain:

- structured operational logs;
- audit events;
- security events;
- error tracking;
- performance measurements;
- cost signals;
- release identity;
- correlation IDs;
- issue links.

Protected content must remain redacted.

## 77.22 Feedback system

Closed-alpha feedback should use a governed intake system with:

- stable issue ID;
- release version;
- tester;
- role;
- campaign;
- device;
- reproduction;
- expected and actual result;
- severity;
- evidence;
- privacy classification;
- disposition.

## 77.23 Defect classes

Defects should be separated into:

- security;
- privacy;
- data loss;
- hidden-information leakage;
- permission failure;
- migration or recovery;
- game-rule behavior;
- performance;
- accessibility;
- usability;
- content;
- visual;
- feature request.

## 77.24 Blocking defects

Closed alpha should pause or reject a candidate for defects such as:

- unauthorized access;
- secret exposure;
- persistent data loss;
- unrecoverable migration;
- duplicated ownership or inventory;
- hidden-information leakage;
- corrupted campaign history;
- broken restore;
- inability to complete the core loop;
- severe inaccessible blocking workflow.

## 77.25 Nonblocking defects

A nonblocking defect may remain when:

- impact is bounded;
- workaround exists;
- risk is understood;
- issue is documented;
- owner accepts it for the release scope;
- no security, privacy, data-integrity, or authority boundary is violated.

## 77.26 Release cadence

Closed-alpha release cadence should prioritize stability over frequency.

A release should not be pushed merely because new code exists.

Each candidate should have:

- change set;
- tests;
- migration;
- backup;
- known issues;
- rollback;
- release notes;
- owner or delegated approval.

## 77.27 Support model

Closed alpha requires a defined support process:

- issue intake;
- acknowledgement;
- severity triage;
- emergency contact;
- service-status communication;
- account recovery;
- data export;
- known-issue updates.

The support scope should match the small invited audience.

## 77.28 Privacy and tester agreement

Testers should understand:

- what data is collected;
- who can access it;
- how AI providers are used;
- how long data is retained;
- whether sessions are logged;
- how to request export or deletion;
- that the product is unfinished;
- confidentiality expectations where applicable.

## 77.29 Closed-alpha exit criteria

Closed alpha may exit when:

- primary workflows complete reliably;
- campaign isolation is proven;
- migrations preserve state;
- backup and restore operate;
- blocking defects are resolved;
- accessibility findings have a disposition;
- performance is understood;
- support can handle the next cohort;
- cost remains acceptable;
- owner approves beta entry.

## 77.30 Beta objective

Beta should answer:

- Can the platform support a meaningfully larger invited or public cohort?
- Are workflows stable across varied campaigns and devices?
- Can operations, support, privacy, recovery, and releases scale?
- Are commercial and public-launch requirements understood?
- Can the product improve without frequent destructive migration or reset?

## 77.31 Beta types

The program may use:

### Private beta

Larger invited cohort with controlled registration.

### Public beta

Open or waitlisted access under explicit beta terms.

Public beta is a public release action and requires separate owner approval and readiness evidence.

## 77.32 Beta entry gate

Beta requires:

- closed-alpha completion;
- owner approval;
- stable release process;
- tested migrations;
- backup and restore;
- security and privacy readiness appropriate to cohort;
- scalable identity and authorization;
- support process;
- abuse and moderation plan where public interaction exists;
- cost model;
- performance baseline;
- known limitations;
- rollback.

## 77.33 Beta feature policy

Beta should emphasize stabilization.

New features should be admitted only when they:

- address a critical gap;
- support release readiness;
- are safely feature-flagged;
- have complete tests and migration;
- do not destabilize the core loop.

## 77.34 Beta data policy

Beta should avoid routine resets.

The project should preserve:

- accounts;
- campaigns;
- characters;
- ownership;
- history;
- content;
- entitlements;
- exports.

Any possible reset must be disclosed before participation.

## 77.35 Beta scale testing

Beta should measure:

- concurrent sessions;
- active campaigns;
- storage growth;
- media transfer;
- search load;
- realtime connections;
- backup duration;
- restore time;
- support volume;
- cost;
- abuse or rate-limit patterns.

## 77.36 Beta security

Before public beta, the program should include:

- current threat model;
- vulnerability review;
- dependency audit;
- authorization testing;
- incident plan;
- secrets and key management;
- export controls;
- upload security;
- abuse controls;
- security contact.

## 77.37 Beta privacy

Before public beta, the program should include:

- privacy notice;
- data inventory;
- retention;
- deletion;
- export;
- consent where required;
- AI-provider disclosure;
- analytics disclosure;
- jurisdiction review;
- minors policy if applicable.

## 77.38 Moderation boundary

Moderation is required only for features that permit public or shared user-generated content beyond private campaign use.

If such features exist, beta readiness should define:

- reporting;
- blocking;
- takedown;
- appeal;
- prohibited content;
- enforcement;
- audit;
- support.

The project should not claim moderation readiness before those features and controls exist.

## 77.39 Beta accessibility

Beta should complete a broader accessibility audit and remediation cycle.

The evidence should identify:

- tested workflows;
- standards target;
- automated and manual results;
- assistive technologies;
- unresolved defects;
- owner-approved limitations;
- public claims allowed.

## 77.40 Beta performance and capacity

The team should define capacity expectations based on measured usage.

The program should know:

- safe user count;
- safe session count;
- storage growth;
- recovery limits;
- provider quotas;
- cost thresholds;
- scale-up procedure;
- scale-down and exit procedure.

## 77.41 Beta support and operations

Beta operations should include:

- service status;
- incident communication;
- on-call or response ownership;
- knowledge base;
- account recovery;
- release notes;
- known issues;
- privacy requests;
- security reports;
- escalation.

## 77.42 Beta exit criteria

Beta may exit toward production when:

- core workflows are stable;
- blocking defects are zero;
- migrations and recovery are proven;
- security and privacy gates pass;
- support can handle projected use;
- accessibility evidence supports the intended claims;
- cost and capacity are understood;
- commercial requirements are ready;
- owner approves production release.

## 77.43 Release claims

Closed alpha and beta do not prove:

- final balance;
- perfect usability;
- universal accessibility;
- unlimited scale;
- legal readiness in every jurisdiction;
- app-store approval;
- commercial success;
- permanent provider suitability.

## 77.44 Current status

Closed alpha and beta have not begun.

Their architecture is defined so the project can advance without confusing an internal technical milestone with an approved public release.

## 77.45 Controlling references

- Internal Alpha chapter
- P9-06 AG-07 and AG-08
- Phase 13 roadmap
- public-live path in the Application Implementation Roadmap
- security, privacy, accessibility, testing, backup, recovery, observability, cost, and deployment chapters
- owner release authority

**Status:** Canonical closed-alpha and beta architecture; both stages remain future and owner-gated.

---

# 78. Commercial and Public-Release Readiness

## 78.1 Purpose

Define the product, commercial, legal, privacy, security, operational, support, billing, content-rights, platform, and owner-decision requirements that must be completed before Multiversal may charge users, make public availability claims, or operate as a production service.

## 78.2 Readiness principle

A technically functioning application is not automatically commercially or publicly ready.

Public release requires coordinated readiness across:

- product;
- content;
- operations;
- security;
- privacy;
- legal;
- accessibility;
- billing;
- support;
- moderation where applicable;
- recovery;
- platform distribution;
- owner authority.

## 78.3 Owner authority

The following remain owner-reserved:

- commercial model;
- pricing;
- paid-provider enrollment;
- billing activation;
- production credentials;
- public claims;
- platform agreements;
- public launch;
- acceptance of material residual risk.

No agent may activate commerce or publish the product without an exact owner decision.

## 78.4 Public-release scope

A release decision should define:

- regions;
- platforms;
- languages;
- user types;
- plans;
- content catalog;
- AI features;
- community features;
- support hours;
- capacity;
- launch cohort;
- exclusions.

## 78.5 Product readiness

Product readiness should verify:

- complete primary Player and GM workflows;
- stable identity and permissions;
- durable character and campaign state;
- content browsing;
- live sessions;
- recovery;
- inventory and ownership;
- noncombat play;
- creator workflows where offered;
- onboarding;
- help;
- consistent responsive behavior.

## 78.6 Content readiness

The public content catalog should have:

- owner-pack assignment;
- stable IDs;
- provenance;
- source authority;
- licensing or ownership evidence;
- schema validation;
- dependency validation;
- installation and migration;
- player-safe presentation;
- localization status;
- withdrawal procedure.

## 78.7 Rules readiness

Public rules should be:

- versioned;
- searchable;
- source-linked;
- internally consistent;
- tested;
- migration-aware;
- clearly distinguished from house rules and AI proposals.

Public release does not require the claim that all balance is final.

## 78.8 Commercial model

The owner must approve:

- free plan;
- paid plans;
- campaign grants;
- sponsored access;
- content ownership;
- subscriptions;
- cancellation;
- refunds;
- regional availability;
- limits;
- AI usage;
- storage;
- taxes and fees.

## 78.9 Pricing

Pricing decisions should be supported by:

- cost model;
- competitive research;
- user value;
- support cost;
- payment fees;
- taxes;
- provider cost;
- content and creator obligations;
- refund exposure;
- growth assumptions.

Pricing is not an AI implementation decision.

## 78.10 Billing boundary

Billing architecture may use a provider-neutral commercial interface, but payment processing introduces provider, legal, security, and tax obligations.

Before activation, the project should define:

- payment provider;
- account ownership;
- production credentials;
- webhook security;
- product and price IDs;
- subscription lifecycle;
- cancellation;
- refund;
- dispute;
- failed payment;
- tax handling;
- receipt;
- provider exit.

## 78.11 No billing secrets in clients

Clients must not receive:

- secret API keys;
- webhook secrets;
- privileged account tokens;
- administrative billing credentials.

## 78.12 Entitlement and billing separation

Billing events create or revoke entitlement through governed records.

The billing provider must not become the only source of product access truth.

Entitlement history should survive provider replacement.

## 78.13 Cancellation

Cancellation policy should define:

- effective time;
- continued access;
- campaign grants;
- sponsored access;
- historical character state;
- exports;
- refunds;
- renewal;
- reactivation.

## 78.14 Refunds and disputes

Refund or dispute handling should preserve:

- entitlement history;
- affected period;
- campaign and character state;
- transaction evidence;
- privacy;
- provider record;
- customer communication.

## 78.15 Tax and financial obligations

Public commerce may require:

- sales tax or VAT;
- invoices;
- merchant records;
- regional restrictions;
- accounting;
- payout handling;
- creator compensation if offered.

These require qualified legal and accounting review.

## 78.16 Terms of service

Public release should have owner-approved terms covering, as applicable:

- account use;
- subscriptions;
- content licenses;
- user-generated content;
- campaign privacy;
- prohibited conduct;
- termination;
- refunds;
- disclaimers;
- dispute process;
- governing law.

## 78.17 Privacy policy

The privacy policy should accurately describe:

- data collected;
- purpose;
- legal basis where required;
- identity providers;
- analytics;
- AI providers;
- billing providers;
- storage;
- retention;
- export;
- deletion;
- security;
- user rights;
- contact;
- jurisdiction.

The policy must match actual implementation.

## 78.18 Data inventory

A production data inventory should cover:

- account data;
- profile;
- campaign and character data;
- private notes;
- GM-only information;
- media;
- logs;
- security events;
- billing references;
- AI prompts and outputs;
- backups;
- support communications.

## 78.19 Retention and deletion

Production policy should define:

- active data retention;
- inactive account retention;
- backup retention;
- security-event retention;
- support data;
- billing records;
- deletion timing;
- anonymization;
- legal holds;
- content-rights constraints.

## 78.20 Data rights workflow

The application or support process should handle:

- access;
- correction;
- export;
- deletion;
- account closure;
- objection or restriction where applicable;
- identity verification;
- response tracking.

## 78.21 Minors

If minors may use the service, the project needs an owner-approved and legally reviewed policy for:

- minimum age;
- parental consent where required;
- data minimization;
- communication;
- community features;
- billing;
- reporting.

The product should not assume unrestricted minor access.

## 78.22 Security readiness

Public release requires:

- current threat model;
- least privilege;
- secure authentication;
- authorization and campaign isolation;
- secrets and key management;
- dependency and supply-chain review;
- upload and pack security;
- AI security;
- incident response;
- vulnerability intake;
- backup and restore;
- disaster recovery;
- security monitoring.

## 78.23 Security testing

Production readiness should include:

- authorization testing;
- penetration or equivalent adversarial review appropriate to risk;
- dependency scanning;
- secret scanning;
- static and dynamic checks;
- upload validation;
- webhook validation;
- rate limits;
- export security;
- incident drill.

## 78.24 Incident response

The public service should define:

- incident owner;
- detection;
- severity;
- containment;
- revocation;
- restoration;
- communication;
- legal escalation;
- user notification;
- postincident review.

## 78.25 Reliability readiness

Reliability should include:

- documented service targets;
- health and readiness;
- capacity;
- backup;
- restore;
- provider exit;
- migration;
- rollback;
- status communication;
- maintenance procedures;
- operational ownership.

## 78.26 Backup and disaster recovery

Before public launch:

- automated backups should operate;
- restore drills should pass;
- recovery objectives should be measured;
- media recovery should be tested;
- provider-exit export should be rehearsed;
- backup access should be audited.

## 78.27 Support readiness

Public support should define:

- channels;
- hours;
- response expectations;
- severity;
- account recovery;
- billing support;
- data requests;
- security reports;
- known issues;
- escalation;
- documentation.

## 78.28 Moderation readiness

Moderation is required for public-facing user content or community features.

Controls may include:

- report;
- block;
- mute;
- takedown;
- appeal;
- audit;
- prohibited-content policy;
- repeat-abuse handling;
- emergency escalation.

Private campaign content still requires privacy and abuse safeguards but may use a different moderation model.

## 78.29 Accessibility readiness

Public claims should be based on:

- defined standards target;
- automated and manual audit;
- keyboard testing;
- assistive-technology testing;
- responsive testing;
- issue remediation;
- documented limitations;
- accessibility contact;
- ongoing regression process.

## 78.30 Localization readiness

A localized release requires:

- translated interface;
- translated help;
- terminology registry;
- locale formatting;
- right-to-left support where applicable;
- font coverage;
- content fallback;
- review by competent speakers;
- localized legal terms where required.

## 78.31 Performance and capacity

Public readiness should define:

- expected users;
- concurrent sessions;
- storage growth;
- media use;
- search volume;
- AI use;
- database load;
- realtime capacity;
- backup window;
- cost thresholds;
- scaling procedure.

## 78.32 Cost and financial controls

The project should maintain:

- provider budget;
- monthly forecast;
- alert thresholds;
- unit cost;
- AI cost;
- storage and egress;
- backup cost;
- support cost;
- gross margin assumptions where applicable;
- owner spending approval.

## 78.33 Provider contracts

A production provider decision should consider:

- data location;
- security;
- privacy;
- uptime;
- export;
- deletion;
- pricing;
- limits;
- support;
- lock-in;
- incident terms;
- legal terms.

## 78.34 Provider exit

Production readiness requires:

- documented export;
- stable internal IDs;
- replacement adapter;
- import rehearsal;
- provider-specific limitations;
- expected downtime;
- cost;
- media migration;
- identity mapping;
- billing transition where applicable.

## 78.35 Content rights

Every public asset should have evidence for:

- ownership;
- license;
- attribution;
- permitted modification;
- permitted distribution;
- commercial use;
- withdrawal.

AI-generated assets require a documented provider and rights policy.

## 78.36 User-generated content rights

Terms should define:

- user ownership;
- license to operate the service;
- privacy;
- export;
- deletion;
- prohibited content;
- takedown;
- public sharing;
- AI use.

## 78.37 Creator and marketplace boundary

A creator marketplace would add:

- creator onboarding;
- identity;
- rights;
- review;
- pricing;
- payouts;
- taxes;
- refunds;
- moderation;
- fraud;
- ranking;
- support.

A marketplace is deferred unless separately approved.

## 78.38 Analytics

Production analytics should be:

- minimal;
- disclosed;
- privacy-aware;
- purpose-limited;
- separated from protected campaign content;
- configurable;
- subject to retention.

Analytics should not record private narrative content by default.

## 78.39 AI commercial readiness

Public AI features should define:

- provider;
- cost;
- privacy;
- data retention;
- user disclosure;
- model limits;
- permission controls;
- provenance;
- refusal;
- fallback;
- user controls;
- output responsibility.

## 78.40 Platform readiness

For each platform, verify:

- build;
- packaging;
- signing;
- updates;
- accessibility;
- privacy declarations;
- store requirements;
- crash reporting;
- support;
- rollback or withdrawal.

## 78.41 Web release readiness

The web release should verify:

- production domain;
- TLS;
- secure headers;
- authentication callbacks;
- browser support;
- caching;
- accessibility;
- privacy;
- rollback;
- status monitoring.

## 78.42 App-store readiness

App-store submission requires:

- current supported toolchain;
- developer account;
- signing;
- provisioning;
- bundle identity;
- privacy labels;
- screenshots;
- review metadata;
- store agreements;
- platform policy compliance;
- owner approval.

WP-011 is not an app-store submission package.

## 78.43 Release candidate freeze

A production candidate should be frozen by:

- commit;
- artifact;
- schemas;
- migrations;
- pack versions;
- configuration;
- provider profile;
- feature flags;
- checksums.

Material changes require refreshed gates.

## 78.44 Production launch plan

A launch plan should identify:

- date and cohort;
- environment;
- candidate;
- migration;
- backup;
- monitoring;
- support;
- incident ownership;
- rollback;
- communication;
- success criteria;
- stop conditions.

## 78.45 Staged launch

The project should prefer staged exposure, such as:

- owner and staff;
- small production cohort;
- invited cohort;
- waitlist;
- broader release.

Staging reduces irreversible impact.

## 78.46 Launch stop conditions

Launch should stop for:

- security issue;
- privacy issue;
- data loss;
- restore failure;
- migration failure;
- hidden-information leak;
- billing defect;
- entitlement defect;
- cost breach;
- severe accessibility blocker;
- provider outage;
- owner hold.

## 78.47 Public claims

Marketing and public documentation should claim only what evidence supports.

The project must not claim:

- perfect security;
- final balance;
- universal accessibility;
- every setting;
- unlimited AI;
- guaranteed uptime;
- provider independence without tested exit;
- app-store availability before approval.

## 78.48 Launch receipt

A launch receipt should preserve:

- owner approval;
- candidate;
- environment;
- migration;
- backup;
- provider profile;
- checksums;
- gates;
- known risks;
- deployment result;
- monitoring;
- rollback state.

## 78.49 Post-launch verification

After launch, verify:

- health;
- authentication;
- entitlement;
- payment;
- campaign creation;
- session flow;
- backup;
- observability;
- security events;
- cost;
- support intake.

## 78.50 Post-launch operations

The project should maintain:

- incident review;
- release cadence;
- dependency updates;
- privacy requests;
- content updates;
- provider monitoring;
- backup drills;
- accessibility regression;
- cost review;
- support documentation.

## 78.51 Current status

Commercial, production, and public-release readiness are not complete.

No paid service, billing activation, production deployment, public release, or app-store submission is authorized by the current implementation program.

## 78.52 Controlling references

- Application Implementation Roadmap public-live path
- entitlement and freemium architecture
- security, privacy, backup, provider-exit, accessibility, observability, cost, deployment, testing, and platform chapters
- owner-reserved authority
- future legal, accounting, and commercial review
- platform certification requirements

**Status:** Canonical commercial and public-release readiness architecture; all execution remains future and owner-gated.

---

# 79. Parallel Apple Platform Track

## 79.1 Purpose

Define the bounded Apple-specific work that must be performed on a borrowed Mac, preserve the one-pass execution package, minimize time and credit use, establish PASS and HARD_GATE outcomes, protect the machine owner’s data, retain durable evidence, and prevent the Apple track from blocking ordinary non-Apple development.

## 79.2 Track identity

The Apple work package is:

> **MS-02 WP-011 — Tauri iOS/iPadOS Spike**

The audited execution kit is:

`Multiversal_MS-02_WP-011_One-Pass_Apple_Spike_v0.4.0`

## 79.3 Track purpose

WP-011 is an engineering spike to prove or disprove:

- phone shell;
- tablet shell;
- iOS/iPadOS generation;
- simulator build;
- install and launch;
- lifecycle behavior;
- local-storage persistence;
- missing-record safety;
- corrupt-record safety;
- accessibility smoke behavior.

It must operate at the exact approved repository commit and produce durable evidence for WP-012.

## 79.4 Non-goals

WP-011 does not include:

- App Store submission;
- production signing;
- production provisioning;
- broad redesign;
- Android work;
- unsupported macOS patching;
- unrelated dependency upgrades;
- general application development;
- public release.

## 79.5 Borrowed-machine boundary

The Mac is borrowed and available once.

It is not the project’s permanent development machine.

The session should:

- minimize discovery;
- minimize downloads;
- run the prepared one-pass package;
- keep all work inside a disposable workspace;
- avoid persistent credentials;
- preserve evidence externally;
- remove Multiversal files and temporary access afterward.

## 79.6 Audited host

The v0.4.0 package was prepared for a:

- Mid-2015 Intel Mac;
- macOS Monterey 12.7.6;
- Xcode 14.2 engineering-spike ceiling.

The package treats this Mac as an engineering-spike host, not a current App Store submission host.

## 79.7 Exact repository binding

The package is bound to:

- repository: `cybalicistjt-stack/Multiversal-app`;
- expected branch: `main`;
- exact commit: `f1f49b504c414a56a5b8b762b175a5f6705c0f05`;
- work branch: `wp011/apple-spike`;
- bundle identifier: `app.multiversal.desktop-spike`.

The package must not silently substitute a newer `HEAD`.

If the project intentionally rebases WP-011 to a newer commit, that requires a revised, validated package rather than editing the sealed commit during the borrowed session.

## 79.8 Toolchain binding

The repository-specific audit records:

- Node `24.18.0`;
- pnpm `11.17.0`;
- Rust `1.97.1`;
- Tauri CLI `2.11.4`;
- Tauri application at `apps/desktop-tauri`.

## 79.9 Prepared source acquisition

The preferred source path is an offline verified Git bundle such as:

`multiversal-wp011.bundle`

Network cloning is the secondary path and only when permitted.

The exact commit must be available before the session begins.

## 79.10 Prepared Xcode

The external drive should contain:

- Xcode 14.2 `.xip`;
- recorded SHA-256;
- enough free space;
- any lawful reusable offline dependency caches.

The package should not spend the borrowed session discovering or downloading large prerequisites.

## 79.11 Owner preparation

Before borrowing the Mac, confirm:

- exact repository URL;
- approved branch;
- exact commit;
- WP-010 handoff;
- sealed WP-011 work order;
- pinned Node, package manager, Rust, Tauri, and lockfiles;
- bundle identifier;
- non-Mac tests passing at the same commit;
- administrator-password holder present;
- evidence destination writable;
- four to eight uninterrupted hours;
- at least 45–50 GB free.

## 79.12 Configuration

The session configuration declares:

- repository URL;
- offline bundle;
- expected branch;
- expected commit;
- work branch;
- bundle ID;
- disposable workspace;
- Xcode application;
- Xcode installer;
- external evidence directory;
- network policy;
- install policy;
- push policy;
- physical-device requirement;
- free-space requirement;
- iPhone and iPad simulator hints.

Placeholder external-drive paths must be filled before execution.

## 79.13 Codex access

Codex should receive full access only to:

- the disposable WP-011 package;
- the disposable repository workspace;
- required external evidence destination.

It should not receive broad full-disk access.

## 79.14 One-pass prompt

The owner should paste the prepared:

`prompts/CODEX_ONE_PASS_PROMPT.md`

The prompt directs the agent through preflight, acquisition, context, tools, build, simulator tests, evidence, handoff, and cleanup.

## 79.15 One-pass sequence

The required sequence is:

1. Verify package integrity and configuration.
2. Capture untouched-machine preflight.
3. Acquire the exact source.
4. Verify clean exact commit and create work branch.
5. Load minimum authoritative context.
6. Expand or select Xcode and install only missing pinned prerequisites.
7. Run baseline gates.
8. Generate and build the Tauri iOS target.
9. Use the repository-specific adapter.
10. Run one iPhone simulator.
11. Run one iPad simulator.
12. Test lifecycle, storage, corruption recovery, and accessibility.
13. Classify PASS or HARD_GATE.
14. Generate WP-012 handoff.
15. Preserve branch, patch, bundle, and evidence externally.
16. Independently verify checksums.
17. Present cleanup plan.
18. Clean only after owner approval.
19. Verify removal and sign-out.

## 79.16 Repository-specific commands

The audited adapter requires iOS generation using:

`pnpm --dir apps/desktop-tauri tauri ios init --ci --skip-targets-install`

The simulator build should use the repository-pinned Tauri CLI and `aarch64-sim`.

The generic `cargo tauri` path was removed because it did not match the repository’s governed setup.

## 79.17 Adapter behavior

The repository adapter should:

1. verify exact pinned commit and clean checkout;
2. rebuild the simulator target;
3. locate the generated `.app`;
4. boot the selected simulator;
5. uninstall stale app;
6. install fresh app;
7. launch;
8. capture clean-launch and relaunch screenshots;
9. exercise terminate and relaunch;
10. record container and logs;
11. update automated result rows.

## 79.18 Result matrix

The sealed result matrix covers:

- iOS project generation;
- phone simulator build;
- phone launch;
- tablet simulator build;
- tablet launch;
- cold launch;
- background and foreground;
- terminate and relaunch;
- storage write and read;
- storage after relaunch;
- missing record;
- corrupt record;
- accessibility smoke review.

All rows begin as `NOT_RUN` in the package.

## 79.19 PASS

PASS means every required check passed with linked evidence.

Evidence should include:

- exact commit;
- environment manifests;
- context receipt;
- dependency and baseline logs;
- generation and build logs;
- phone and tablet proof;
- lifecycle;
- storage;
- corruption behavior;
- accessibility review;
- changed-file manifest;
- blocker ledger;
- WP-012 recommendation;
- external checksums;
- cleanup receipt.

## 79.20 HARD_GATE

HARD_GATE is a successful spike disposition when:

- the exact approved commit cannot complete under the fixed Monterey/Xcode ceiling;
- the incompatibility is reproduced;
- attempts are bounded;
- evidence is complete;
- WP-012 fallback input is generated.

HARD_GATE is not the same as an incomplete session.

## 79.21 INCOMPLETE

INCOMPLETE means:

- prerequisite missing;
- evidence missing;
- cleanup unverified;
- exact source unavailable;
- required simulator unavailable;
- no durable disposition.

INCOMPLETE is not an acceptable one-pass final outcome.

## 79.22 Failure handling

The failure playbook defines bounded responses for:

- missing Xcode;
- license or component block;
- low disk;
- Git failure;
- commit mismatch;
- Node or Rust mismatch;
- dependency failure;
- baseline test failure;
- Tauri generation failure;
- missing simulator;
- simulator hang;
- launch failure;
- unobservable storage behavior;
- rejected push;
- checksum mismatch;
- uncertain cleanup.

## 79.23 Retry limit

The sealed work order allows no more than two remediation attempts for one root cause.

After the bounded attempts, the result should be classified honestly rather than consuming the entire borrowed session.

## 79.24 Human gates

Codex may pause only for:

- administrator authentication;
- macOS privacy confirmation;
- credential or 2FA entry;
- access outside the disposable workspace;
- a genuine scope or architecture decision.

The package batches human requests in:

`records/human-gates.json`

## 79.25 Accessibility evidence

VoiceOver, text scaling, target size, orientation, and detailed persistence or corrupt-data behavior require UI interaction with the simulator.

Codex should perform these through simulator UI capabilities and save evidence.

They are not owner-decision gates.

## 79.26 Storage behavior

The spike should verify:

- write and immediate read;
- persistence after relaunch;
- safe missing-record behavior;
- governed corrupt-record failure or recovery.

A bounded diagnostic hook may be added only when needed to observe approved behavior.

## 79.27 Physical device

The package sets:

`REQUIRE_PHYSICAL_DEVICE="false"`

Simulator-only WP-011 should not require:

- iCloud login;
- production certificate;
- provisioning profile;
- Apple Developer Program login.

Physical-device validation may occur in a later separately approved track.

## 79.28 Evidence preservation

Before cleanup, preserve externally:

- branch;
- patch;
- Git bundle;
- logs;
- screenshots;
- manifests;
- result matrix;
- blocker records;
- context receipts;
- checksums;
- WP-012 handoff;
- cleanup plan.

The evidence should be opened and verified on another machine.

## 79.29 Checksum verification

Destination checksums must match before cleanup.

If a hash fails:

- recopy the affected item;
- use a new destination folder if necessary;
- verify again;
- do not clean the Mac until evidence is valid.

## 79.30 Security

Prefer the offline Git bundle.

Avoid:

- iCloud sign-in;
- production signing;
- persistent credentials;
- broad privacy permissions;
- owner Keychain changes;
- global destructive cleanup.

## 79.31 Session-created asset inventory

The package records created:

- paths;
- simulators;
- keychain fingerprints;
- provisioning profiles;
- credential-helper entries;
- logins;
- privacy permissions;
- caches;
- shell-history markers.

Cleanup should use this inventory.

## 79.32 Cleanup gate

Cleanup is prohibited until:

- external evidence exists;
- destination checksums match;
- PASS or HARD_GATE record exists;
- WP-012 record exists;
- source changes are preserved;
- owner has reviewed the exact cleanup plan.

## 79.33 Cleanup sequence

Cleanup should:

1. sign out temporary sessions;
2. remove temporary tokens and credential entries;
3. remove only recorded keychain items and profiles;
4. remove only session-created simulators;
5. remove disposable workspace and session caches;
6. empty Trash only for session-owned items;
7. verify removal;
8. obtain owner confirmation of GUI sign-outs.

## 79.34 Prohibited cleanup

Never:

- erase the Mac;
- reset the owner’s Keychain;
- remove pre-existing simulators;
- clear all shell history;
- delete global tools present before preflight;
- guess which files are safe to remove.

## 79.35 WP-012 handoff

The spike feeds WP-012.

The handoff should identify:

- PASS or HARD_GATE;
- exact commit;
- tested toolchain;
- phone and tablet result;
- lifecycle result;
- storage result;
- accessibility result;
- changed files;
- blockers;
- fallback input;
- recommended next platform step.

## 79.36 Main-track independence

Ordinary application development should continue before and after WP-011.

The project should not wait for the borrowed Mac to implement:

- provider-neutral services;
- web client;
- design system;
- application workflows;
- tests;
- content;
- documentation.

## 79.37 Rebinding rule

The current WP-011 package is bound to an earlier exact commit than the latest verified application head.

That is intentional for the sealed spike.

Rebinding to a later commit requires:

- updated source bundle;
- updated preflight;
- updated baseline evidence;
- updated repository adapter audit;
- updated checksums;
- revised sealed work order;
- validated package release.

The borrowed session should not improvise the rebind.

## 79.38 Current status

WP-011 is prepared but not executed.

The v0.4.0 package has corrected prior orchestration and evidence gaps and includes a repository-specific adapter.

The actual Mac run, simulator evidence, PASS or HARD_GATE result, WP-012 handoff, and cleanup receipt remain incomplete.

## 79.39 Controlling references

- `Multiversal_MS-02_WP-011_One-Pass_Apple_Spike_v0.4.0`
- package README
- Owner Before Mac
- Master Operations Plan
- Failure Playbook
- Security and Cleanup
- Owner Quick Card
- Repository-Specific Adapter Audit
- sealed work order
- result matrix
- session configuration
- active Application Implementation Roadmap

**Status:** Canonical prepared Apple spike; execution remains pending.

---

# 80. Risks, Deferred Work, and Owner Decisions

## 80.1 Purpose

Maintain a clear, noninvented record of material risks, intentionally deferred work, unresolved decisions, owner-only gates, stale-source conflicts, and conditions that should stop implementation or release.

## 80.2 Risk principle

A known risk must be:

- identified;
- scoped;
- evidenced;
- assigned;
- mitigated where possible;
- reviewed;
- retained;
- connected to a decision or gate.

A risk does not disappear because the project continues.

## 80.3 Risk categories

The project should track risk across:

- canon;
- source completeness;
- rules;
- balance;
- content;
- architecture;
- data;
- migrations;
- identity;
- authorization;
- entitlement;
- realtime;
- security;
- privacy;
- provider lock-in;
- cost;
- performance;
- accessibility;
- usability;
- platform;
- legal;
- commercial;
- operations;
- support;
- AI;
- schedule;
- owner availability.

## 80.4 Planning-to-implementation risk

Multiversal’s planning and canonical architecture are far more complete than the executable product.

Risk:

- documents may be mistaken for implemented features;
- agents may claim completion from plans;
- UI may be designed without live services;
- later work may restart already completed architecture.

Mitigation:

- repository-first verification;
- explicit status vocabulary;
- vertical slices;
- acceptance gates;
- current-state evidence;
- this Bible’s implementation boundaries.

## 80.5 Source-completeness risk

The 20 governed datasets are fully processed, but unregistered legacy sources may still contain additional material.

Mitigation:

- retain source registry;
- preserve coverage reports;
- distinguish processed registry from global corpus claim;
- allow governed intake of newly discovered sources;
- avoid “all possible content recovered” claims.

## 80.6 Canon-invention risk

Incomplete or conflicting source material may tempt an agent to invent:

- stats;
- lore;
- world relationships;
- mechanics;
- names;
- placements.

Mitigation:

- preserve unresolved state;
- use source authority hierarchy;
- route owner decisions;
- retain variants;
- mark examples and proposals;
- block silent promotion.

## 80.7 Balance risk

The balance harness provides strong deterministic regression evidence but not final human-play balance.

Mitigation:

- preserve E4 evidence;
- require peer groups and practical deltas;
- retain outliers;
- defer human-playtest sufficiency claims;
- never auto-edit canon from a finding.

## 80.8 Rules-runtime risk

The canonical mechanics architecture is complete, but complete executable coverage across every domain remains future implementation.

Mitigation:

- shared Action, Effect, Condition, Resource contracts;
- golden tests;
- replay;
- deterministic seeds;
- staged implementation;
- no domain-specific shadow engines.

## 80.9 Data-migration risk

Future schemas and pack updates may affect:

- stable IDs;
- character state;
- ownership;
- event history;
- installed packs;
- permissions.

Mitigation:

- expand–migrate–contract;
- backup;
- restore;
- supersession maps;
- deterministic fixtures;
- count reconciliation;
- provider-exit export.

## 80.10 Provider-lock-in risk

The selected architecture class may still drift into a specific provider through:

- SDK leakage;
- provider IDs;
- hosted realtime formats;
- storage URLs;
- billing records;
- proprietary backup.

Mitigation:

- ports and adapters;
- stable internal IDs;
- contract tests;
- local adapters;
- export;
- replacement rehearsals;
- service-activation records.

## 80.11 Backup and recovery risk

The active project does not yet have verified completed backup, restore, and provider-exit ports under the current roadmap.

Mitigation:

- prioritize P9-06-008;
- do not trust internal-alpha durability before restore drill;
- preserve events and snapshots;
- verify manifests and checksums.

## 80.12 Identity and authorization risk

Current identity and entitlement ports are foundations, not complete production behavior.

Risk includes:

- cross-campaign leakage;
- stale permissions;
- provider-ID coupling;
- hidden-field exposure;
- export inference.

Mitigation:

- stable internal subjects;
- default deny;
- service and database isolation;
- field- and query-level tests;
- revocation;
- audit.

## 80.13 Realtime risk

Port contracts do not yet prove:

- ordered hosted delivery;
- complete command handler;
- reconnect at scale;
- hidden projection safety;
- two-device acceptance.

Mitigation:

- authoritative persistence;
- idempotency;
- outbox;
- monotonic sequence;
- checkpoint;
- AG-05 and AG-07.

## 80.14 Security risk

Production security is incomplete.

Risks include:

- secret leakage;
- insecure uploads;
- dependency compromise;
- prompt injection;
- unauthorized exports;
- insufficient incident response.

Mitigation:

- AG-01;
- least privilege;
- secret isolation;
- dependency scanning;
- pack validation;
- AI tool authorization;
- incident and recovery plans;
- later security review.

## 80.15 Privacy risk

Multiversal may store highly private campaign, character, and GM material.

Mitigation:

- scope-based permissions;
- data minimization;
- protected logs;
- AI context minimization;
- export controls;
- retention policy;
- privacy review before broader release.

## 80.16 Cost risk

Hosted database, storage, realtime, search, AI, telemetry, backups, and support can exceed the bounded budget.

Mitigation:

- local-first development;
- provider-neutral adapters;
- usage signals;
- target $0–$25 per month for bounded internal-alpha class;
- owner review above $35 per month;
- no automatic paid upgrades.

## 80.17 Performance risk

The product must handle a large canonical corpus and complex live scenes.

Mitigation:

- actual-corpus tests;
- virtualization;
- indexes;
- query models;
- performance budgets;
- low-powered-device testing;
- staged capacity planning.

## 80.18 Accessibility risk

Automated checks may be mistaken for full accessibility validation.

Mitigation:

- manual keyboard and screen-reader testing;
- map and graph alternatives;
- mobile and touch review;
- reduced-motion support;
- honest claims;
- alpha and beta remediation cycles.

## 80.19 UX complexity risk

The project has many domains and may overwhelm Players and GMs.

Mitigation:

- role-based workspaces;
- progressive disclosure;
- universal object components;
- focused live-session hierarchy;
- Player logs secondary;
- GM approval details contextual;
- usability testing.

## 80.20 Editorial ordering consistency

The earlier Master Table of Contents inconsistency between Investigation/Social and Inventory/Shared Assets was resolved during the final editorial audit.

The audited order now follows the Stage A implementation sequence:

- Chapter 49 — Inventory, Shared Assets, Crafting, and Vehicles;
- Chapter 50 — Investigation and Social Workspaces.

The chapter content was preserved. The Table of Contents, chapter headings, progress records, and release audit now agree.

Residual control:

- future editorial changes must update the Table of Contents and chapter heading together;
- automated documentation validation must compare every numbered Table of Contents entry with the corresponding chapter heading.

## 80.21 Platform-fragmentation risk

Separate web, desktop, iOS, and Android implementations could drift.

Mitigation:

- portable client;
- shared contracts;
- thin platform adapters;
- one canonical rules runtime;
- WP-011 bounded spike;
- platform-specific code isolated.

## 80.22 Borrowed-Mac risk

The Apple session may fail because of:

- old hardware;
- Monterey ceiling;
- Xcode ceiling;
- missing simulator runtime;
- disk space;
- administrator access;
- exact commit mismatch;
- long downloads.

Mitigation:

- one-pass package;
- offline source bundle;
- prepared Xcode;
- exact preflight;
- PASS/HARD_GATE;
- retry limit;
- external evidence;
- cleanup inventory.

## 80.23 Legal and rights risk

Public content, media, AI assets, subscriptions, user-generated content, and app-store distribution require legal and rights review.

Mitigation:

- provenance;
- rights metadata;
- owner review;
- commercial readiness gate;
- no unsupported public claims;
- defer marketplace and public sharing until governed.

## 80.24 Support risk

A broad release could exceed available support capacity.

Mitigation:

- staged cohorts;
- known-issue documentation;
- triage;
- severity;
- support channels;
- account-recovery procedures;
- cost and staffing review.

## 80.25 Owner-bottleneck risk

Too many minor questions could overwhelm the owner.

Mitigation:

- approved recommendation process;
- A0–A2 agent authority;
- concise owner decision packets;
- batch related decisions;
- stop only at genuine owner-only gates.

## 80.26 AI-credit risk

Repeatedly loading large archives or re-explaining the project can waste credits and increase inconsistency.

Mitigation:

- source registry;
- digest cache;
- exact extraction;
- context budgets;
- reference tools;
- sealed task packets;
- durable handoffs;
- batched validation;
- archive indexes.

## 80.27 AI-overreach risk

An AI agent may:

- infer approval;
- act on stale context;
- hide failure;
- rewrite baselines;
- claim merge or deployment without evidence;
- expose protected data.

Mitigation:

- authority matrix;
- A4 stop;
- exact approval binding;
- independent review;
- repository verification;
- retained negative evidence;
- tool-level permissions;
- owner sovereignty.

## 80.28 Stale-governance risk

Some current-state or backlog documents may lag newer repository evidence.

Known example:

- older P9-06 backlog numbering conflicts with the newer active roadmap’s definition of P9-06-008.

Mitigation:

- newer verified evidence controls;
- preserve old record as historical;
- update stale governance through a verified PR;
- do not silently merge meanings.

## 80.29 Deferred human playtesting

Human playtesting remains deferred until a usable application or governed test kit exists.

This includes:

- balance feel;
- table pacing;
- GM workload;
- Player comprehension;
- long-session behavior;
- emergent social and investigation play.

Simulation does not replace this work.

## 80.30 Deferred formal accessibility conformance

Formal accessibility conformance remains deferred until:

- primary workflows exist;
- target platforms are selected;
- audit scope is defined;
- manual testing occurs;
- defects are remediated.

## 80.31 Deferred production provider selection

A specific production provider remains deferred.

The project may research and prototype adapters but should not create irreversible coupling or paid commitments without owner approval.

## 80.32 Deferred billing and commerce

Billing provider selection, plan activation, pricing, taxes, refunds, and production commerce remain deferred.

The entitlement architecture is ready to support later decisions without requiring commerce now.

## 80.33 Deferred public community and moderation

Public social features, discovery, marketplace, public content sharing, and moderation remain deferred unless separately approved.

## 80.34 Deferred marketplace

A creator marketplace is not part of the current implementation program.

It requires separate:

- rights;
- review;
- payments;
- taxes;
- fraud;
- moderation;
- support;
- ranking;
- creator policy.

## 80.35 Deferred app-store submission

App-store submission is deferred.

WP-011 is an engineering spike, not a store-release package.

A current supported toolchain, developer account, signing, provisioning, privacy declarations, store agreements, and owner approval will be required later.

## 80.36 Deferred production AI automation

Autonomous AI actions that change campaign or canonical state remain deferred.

Current AI should:

- retrieve;
- explain;
- propose;
- summarize;
- assist.

Mutations remain explicit and approval-gated.

## 80.37 Deferred advanced platform features

Features such as:

- push notifications;
- background sync;
- platform billing;
- device camera;
- offline peer-to-peer relay;
- advanced native integrations;

remain deferred until core product workflows are stable.

## 80.38 Deferred scale commitments

The project has not committed to:

- unlimited users;
- global regions;
- enterprise uptime;
- high-volume media;
- public marketplace scale;
- large support organization.

Capacity targets should follow measured beta use.

## 80.39 Open owner decisions

Owner decisions will be required before:

- paid-provider enrollment;
- production credentials;
- internal-alpha release;
- public beta;
- pricing;
- billing activation;
- public launch;
- app-store agreements;
- material legal risk acceptance;
- public community features;
- marketplace;
- major canon changes.

## 80.40 Current owner-decision state

The completed AI Development Team package recorded zero current open owner actions at its release.

That does not mean future implementation will never reach owner gates.

The current active implementation task is bounded and does not itself require a new owner decision unless it encounters one of the reserved conditions.

## 80.41 Decision packet requirements

A future owner decision packet should contain:

- exact question;
- recommendation;
- alternatives;
- cost;
- risk;
- affected artifacts;
- evidence;
- reversibility;
- requested action;
- validity;
- next step after approval.

## 80.42 Risk acceptance

The owner may accept bounded A3 residual risk.

The record should state:

- risk;
- scope;
- evidence;
- mitigation;
- residual exposure;
- duration;
- review point;
- rollback.

A4 actions remain prohibited.

## 80.43 Risk review cadence

Risk should be reviewed:

- at material architecture change;
- before migration;
- before provider activation;
- before internal alpha;
- before closed alpha;
- before public beta;
- before production;
- after incident;
- after major dependency or security advisory.

## 80.44 Risk ownership

Representative ownership includes:

- owner: product, canon, spending, release;
- architect: architecture and provider neutrality;
- Canon Steward: semantic conflict;
- QA: tests, balance, regression;
- Security Reviewer: security, privacy, dependencies;
- Release Engineer: deployment, rollback, environment;
- Documentation Steward: provenance and continuity.

## 80.45 Risk disposition

A risk may be:

- mitigated;
- avoided;
- transferred through approved contract;
- accepted by authorized owner;
- deferred;
- monitored;
- blocked;
- superseded.

The disposition and evidence should be recorded.

## 80.46 Final preimplementation priorities

The highest immediate priorities remain:

1. complete the current provider-neutral backup, restore, and provider-exit task;
2. continue Phase 9 implementation in dependency order;
3. connect service foundations to meaningful Stage A vertical slices;
4. preserve tests, recovery, permissions, and provenance;
5. execute WP-011 only when the borrowed Mac and prepared package are available;
6. avoid production, spending, and release gates until evidence is ready.

## 80.47 Controlling references

- all prior volumes of this Project Bible
- active Application Implementation Roadmap
- Multiversal New Conversation Bootstrap
- 8D-007 and 8D-008 completion packages
- 8E-008 and 8E-009 completion evidence
- Stage A A0 and A1 repository evidence
- P9-01 through P9-06
- WP-011 v0.4.0 one-pass package
- owner authority and decision records
- current repository commits and CI evidence

**Status:** Canonical risk, deferral, and owner-decision register for the current project stage.

---

# Tranche 8 Integration Review

## T8.1 Coverage

Volume VIII now consolidates:

- completed phases;
- current implementation state;
- acceptance gates;
- internal alpha;
- closed alpha;
- beta;
- commercial readiness;
- public-release readiness;
- Apple platform spike;
- risks;
- deferred work;
- owner decisions.

## T8.2 Completion invariant

Completed planning, canonicalization, validation, and operating packages must not be restarted without evidence of a defect or owner-directed revision.

Completed architecture must not be represented as completed product implementation.

## T8.3 Current repository invariant

The latest verified application state used by this volume remains merged through:

- P9-06-007;
- commit `149b866f530f3a8896170bfe3ba6af0c01fb2f72`.

The current active task remains P9-06-008 as defined by the newer roadmap and bootstrap.

## T8.4 Gate invariant

No release stage proceeds from elapsed time, enthusiasm, or partial technical success.

Each stage requires:

- exact candidate;
- evidence;
- recovery;
- security;
- privacy;
- accessibility;
- cost;
- known risks;
- owner authority.

## T8.5 Alpha invariant

Internal alpha is a controlled product-validation release.

Closed alpha broadens trusted use.

Beta stabilizes for a larger cohort.

None of these stages authorizes production or public commerce automatically.

## T8.6 Commercial invariant

Billing, pricing, taxes, legal terms, public claims, production providers, and app-store agreements remain owner-gated.

## T8.7 Apple invariant

WP-011 is bounded to:

- exact commit;
- borrowed Mac;
- simulator-focused engineering spike;
- PASS or HARD_GATE;
- durable evidence;
- cleanup.

It is not a general development or App Store track.

## T8.8 Risk invariant

Known failures, unresolved decisions, stale-governance conflicts, and deferred work remain explicit.

The project must not fill them with plausible but unsupported completion claims.

## T8.9 Roadmap status

The roadmap and release architecture are complete at the documentation level.

Active repository implementation, acceptance gates, alpha, beta, commercial readiness, Apple execution, and public launch remain evidence-driven future work.

## T8.10 Tranche status

Volume VIII is complete at the roadmap, verification, and release-architecture level.

**Tranche 8 status:** Complete — canonical roadmap and release architecture consolidated.


# Appendix A — Glossary

## A.1 Purpose

This glossary defines the controlling project vocabulary used throughout the Multiversal Project Bible.

Definitions in this appendix are concise reference definitions. The full governing rule remains in the relevant numbered chapter, schema, decision record, repository contract, or canonical pack.

## A.2 Authority note

A glossary entry does not:

- create new canon;
- override a schema;
- replace an owner decision;
- authorize implementation;
- resolve a known conflict;
- convert planned work into implemented work.

When a glossary definition conflicts with a more specific active governing source, the more specific active source controls.

## A.3 Terms

### Ability

A governed capability available to an actor through character creation, progression, species, form, item, condition, environment, campaign grant, or another approved source.

An Ability may grant Actions, Effects, modifiers, Resources, permissions, or other structured behavior.

### Ability domain

A classification used to group related Abilities and Powers.

A domain does not create a separate incompatible rules engine.

### Acceptance criterion

A measurable condition that must pass before a work order, feature, migration, pack, gate, or release may be considered complete.

### Acceptance gate

A blocking evidence decision that separates one governed project state from another.

Examples include repository safety, provider-neutral boundaries, data foundation, authoritative sessions, internal alpha, and owner release approval.

### Action

A versioned executable rules object representing an intentional or automatic operation.

An Action defines, as applicable:

- actor;
- timing;
- prerequisites;
- targets;
- costs;
- check or deterministic resolution;
- Effects;
- failure;
- visibility;
- source.

### Actor

The governed subject performing an Action or participating in a rules resolution.

An actor may be:

- character;
- creature;
- NPC;
- group;
- vehicle;
- mecha;
- starship;
- environment;
- facility;
- another approved operational object.

### Adapter

A provider- or platform-specific implementation of a Multiversal port.

Adapters isolate external SDKs, provider IDs, storage URLs, transport formats, and provider errors from domain logic.

### Adjudication

An attributable Game Master decision used when approved rules require judgment or when an ambiguous situation must be resolved.

Adjudication is recorded. It must not silently rewrite the underlying rule or prior calculation.

### Adventure Definition

A reusable governed object describing an adventure’s structure, such as:

- hooks;
- acts;
- routes;
- quests;
- objectives;
- scenes;
- clues;
- cast;
- rewards;
- consequences.

Placing an Adventure Definition in a campaign creates live adventure state without changing the source Definition.

### Agent

A replaceable AI worker assigned one or more governed roles for a bounded work order.

An agent is not the owner, canon authority, or permanent repository of project knowledge.

### Aggregate

A domain object or related group of objects with a clear authoritative mutation boundary.

Examples include a Character, Campaign, Session, Pack Installation, or owned Asset.

### AI Development Team Operating Package

The completed 8D-008 package defining:

- permanent roles;
- authority;
- context loading;
- work orders;
- quality gates;
- change controls;
- recovery;
- startup and handoff assets.

It makes AI development governable. It does not mean a permanent autonomous team is continuously active.

### AI proposal

AI-generated material that remains explicitly noncanonical and nonauthoritative until reviewed and approved through the required process.

### Alpha

A controlled product-validation stage.

Multiversal distinguishes:

- internal alpha;
- closed alpha.

Neither stage is a public production launch.

### Application repository

`cybalicistjt-stack/Multiversal-app`

The canonical repository for active application implementation, service contracts, adapters, tests, CI, and product code.

### Approval

A versioned, attributable decision that permits a specific bounded action.

Material approvals bind to:

- work-order version;
- scope;
- artifact digest;
- executor;
- environment;
- conditions;
- validity window.

### Approval queue

A durable register of pending decisions.

An item in the queue is not approval.

### Archive

A retained historical artifact that is not current operational authority unless explicitly reactivated.

### Asset

A governed owned or usable object, including:

- item;
- container;
- vehicle;
- mecha;
- starship;
- facility;
- shared operational object.

### Audit event

An append-only record of a material or sensitive operation.

Examples include:

- role change;
- ownership transfer;
- entitlement change;
- migration;
- restore;
- export;
- canonical promotion;
- release.

### Authoritative service

The trusted server or service layer that validates, accepts, persists, and sequences canonical runtime state changes.

Clients submit commands and render authorized projections.

### Authoritative state

The accepted durable state controlled by trusted services and persistence.

Local drafts, caches, search indexes, previews, and uncommitted realtime messages are not authoritative state.

### Authorization

The decision that determines whether a subject may perform an action on a resource in the current context.

Authorization is distinct from authentication and entitlement.

### Backup

A protected copy of data and metadata intended for recovery.

A backup is not considered trustworthy until it can be verified and successfully restored.

### Balance finding

A governed review result created when defined peer-relative and practical-effect thresholds are met.

A balance finding does not automatically alter canon.

### Baseline

An approved expected result, fixture, artifact, or measured state used for regression comparison.

A baseline may change only through a reviewed and versioned update.

### Beta

A larger stabilization stage following closed alpha.

A public beta is a public release action and requires separate owner approval.

### Branch

A version-control reference used to isolate repository work.

Material work should occur on a bounded work-order branch rather than directly on the protected primary branch.

### Branch, cosmological

A governed setting or cosmological object used to organize Realities, Worlds, layers, timelines, and related structures.

This is distinct from a version-control branch.

### Build artifact

A generated executable, package, archive, report, or other output traceable to:

- source commit;
- dependencies;
- build command;
- environment;
- checksum.

### Campaign

A persistent governed workspace containing:

- members;
- characters;
- rules profile;
- settings and packs;
- adventures;
- scenes;
- events;
- relationships;
- ownership;
- live state.

### Campaign grant

A scoped entitlement allowing a user to access approved content within a particular Campaign.

A campaign grant does not necessarily create global content ownership.

### Campaign-local content

Content created for one Campaign.

It remains separate from reusable canonical pack content unless explicitly submitted, reviewed, and promoted.

### Canon

Owner-approved controlling project meaning.

Canon may include rules, content, definitions, policies, and decisions.

Implementation code does not become canon merely by existing.

### Canonical

The status of an approved controlling specification or content record.

Canonical does not necessarily mean implemented in the application.

### Canonical object

A governed stable-identity record represented through the Multiversal object architecture.

Canonical objects may include Definitions, relationships, capabilities, sources, and lifecycle metadata.

### Canonical Object Template

The schema-driven object template used to represent governed object families consistently across domains.

### Capability

A reusable structured behavior or feature attached to an object, service, role, or adapter.

### Capability badge

A setting-readiness indicator used to record which major features or domains a setting supports.

### Character

A governed actor aggregate containing identity, campaign binding, species or forms, attributes, abilities, Resources, Conditions, inventory, relationships, progression, presentation, and history.

### Check

A deterministic or random resolution operation comparing defined inputs to an approved rule.

### Checkpoint

A verified recovery artifact containing a session or aggregate state, event cursor, versions, references, and integrity digest.

A checkpoint does not erase prior history when restored.

### CI

Continuous integration.

CI runs repository-owned validation such as builds, tests, schemas, migrations, security checks, and artifact verification.

### Claim

A statement about project state, source meaning, implementation, validation, release, or readiness.

Material claims require evidence and must preserve limitations.

### Closed alpha

An invited product-testing stage following internal alpha.

It expands real use while retaining controlled access and explicit owner gates.

### Command

A request submitted to an authoritative service to attempt a state change.

A session command normally includes:

- command ID;
- subject;
- actor;
- expected version;
- type;
- payload;
- schema version;
- correlation.

### Compensating event

A new event used to correct or reverse an accepted prior operation without deleting or rewriting history.

### Condition

A governed state attached to an actor, object, scene, or other subject.

A Condition defines lifecycle, source, duration, stacking, visibility, mechanical effects, and removal.

### Conflict

Two or more claims, records, versions, or operations that cannot all control the same scope without a governed resolution.

Material conflicts must be preserved and routed, not silently blended.

### Connection receipt

Evidence that a client or participant established a session connection with the resolved subject, role, permissions, and protocol state.

### Container

An inventory-holding object with capacity, restrictions, access, ownership, location, and nesting rules.

Container cycles are prohibited.

### Content Definition

A reusable governed object representing content independent of Campaign placement or live instance state.

### Content pack

A governed `.pack` archive containing reusable content, schemas, indexes, dependencies, provenance, and lifecycle metadata.

### Content registry

The governed catalog of canonical content identities, ownership, versions, and relationships.

### Context bundle

The sealed set of exact and derived sources provided to an agent for a specific task.

### Context manifest

The record of which sources are required, eligible, selected, excluded, conflicted, and loaded for a work order.

### Context receipt

The durable evidence of what context was actually resolved and loaded, including digests, fragments, queries, failures, and final status.

### Control plane

The project mechanisms that govern work rather than execute gameplay.

Examples include:

- authority;
- approvals;
- work orders;
- CI;
- release gates;
- source registry;
- recovery records.

### Correlation ID

An identifier connecting operations that belong to one wider request or workflow.

### Causation ID

An identifier recording which prior command or event caused a new event.

### Cost envelope

The approved planning range for expected service cost.

The bounded internal-alpha architecture targets $0–$25 per month and requires owner review above $35 per month.

These limits do not authorize spending.

### Creator

A user or agent producing governed content drafts, proposals, packs, or documentation.

Creator authority does not include automatic canonical promotion.

### Current projection

An efficient read representation of authoritative state.

A projection is derived and permission-scoped.

### Current-state record

A summary of completed work, active work, blockers, repository state, and next action.

A stale current-state record does not overrule newer verified repository evidence.

### Custody

The current physical or operational possession of an Asset.

Custody is distinct from ownership, authorization, and entitlement.

### Data foundation

The schemas, migrations, fixtures, persistence, backup, restore, and provider-exit capabilities required for trustworthy state.

### Decision level

A governed authority classification:

- A0 — execute an approved bounded action;
- A1 — recorded reversible implementation judgment;
- A2 — peer-reviewed material change;
- A3 — owner approval required;
- A4 — prohibited.

### Decision record

An attributable record of a question, options, selected decision, authority, consequences, evidence, and supersession.

### Definition

A reusable canonical object separate from placements, instances, events, snapshots, and projections.

### Definition of Done

The blocking completion criteria required before a material work order may close.

### Definition of Ready

The blocking criteria required before a material work order may be assigned and executed.

### Delegation

An explicit, scoped, revocable authority record.

Silence, tool access, or previous behavior is not delegation.

### Dependency

A required relationship among:

- packs;
- schemas;
- objects;
- services;
- work orders;
- environments;
- approvals;
- tools;
- reviewers.

### Deprecated

Superseded but retained for migration, compatibility, or history.

### Derived summary

A compact explanation generated from controlling sources.

A derived summary retains source identity and does not replace the controlling source.

### Deterministic

Capable of producing the same governed result from the same defined input, versions, and random seed.

### Digest

A cryptographic or deterministic fingerprint used to verify byte identity or structured state.

A digest proves identity, not semantic correctness.

### Domain

A bounded area of rules, content, product behavior, or service responsibility.

Examples include:

- combat;
- social play;
- items;
- creatures;
- identity;
- persistence.

### Downtime project

A governed long-running activity occurring outside immediate scene or combat resolution.

### Effect

A bounded governed state change produced by an Action, rule, trigger, environment, or another approved source.

### Entitlement

A policy decision determining whether a subject may access content or a capability.

Entitlement is separate from:

- authorization;
- Campaign membership;
- in-world ownership;
- installation;
- canon.

### Environment

A rules and content object representing conditions such as:

- terrain;
- atmosphere;
- weather;
- gravity;
- visibility;
- hazards;
- adaptation requirements.

Environment also means a technical deployment context such as local, preview, alpha, or production. The surrounding chapter determines the meaning.

### Event

An immutable or append-only record of an accepted material occurrence.

Events preserve actor, sequence, source, result, versions, visibility, and causation.

### Evidence

A durable artifact supporting a project claim.

Examples include:

- source fragment;
- schema;
- test report;
- commit;
- pull request;
- checksum;
- migration receipt;
- screenshot;
- restore drill;
- owner decision.

### Evidence location index

A stable registry of where evidence can be retrieved and how its identity is verified.

### Extension

A governed namespaced addition to a target object or schema that preserves ownership and compatibility boundaries.

### Fixture

A deterministic data set used by tests, migration rehearsals, examples, or local development.

### Form

A governed alternate state or embodiment of an actor, species, creature, vehicle, or other object.

### Game Master

The campaign role responsible for scene preparation, hidden information, adjudication, NPC control, approval decisions, and campaign continuity.

### Gate

A blocking check that must reach an allowed passing state before a downstream workflow may proceed.

### Golden test

A regression test comparing current output with an approved exact expected result.

### Governance repository

`cybalicistjt-stack/multiversal-aioc`

The canonical repository for project governance, roadmaps, source recovery, current-state records, Development Brain, and AI operating rules.

### Grant

An approved record providing a capability, Ability, Resource, entitlement, permission, or another scoped benefit.

### HARD_GATE

The valid WP-011 Apple-spike disposition used when the exact approved commit is proven incompatible with the fixed borrowed-Mac toolchain ceiling and complete evidence is preserved.

HARD_GATE is not an incomplete run.

### Handoff

A durable transfer record preserving exact work state, evidence, blockers, authority, repository state, and next action.

### Hidden information

Campaign or user data that must not be disclosed outside the authorized scope.

Examples include:

- GM notes;
- unrevealed clues;
- hidden map layers;
- secret Conditions;
- private player notes.

### Historical source

A retained prior document or source that may provide provenance but is not current authority.

### House rule

A Campaign-scoped approved rule override or addition.

A house rule does not rewrite global canon.

### Idempotency

The property that retrying the same governed operation does not apply the business effect more than once.

### Identity

The stable internal representation of a human, service actor, Campaign subject, object, or content record.

### Implementation receipt

Evidence describing what was changed, where, by whom, under which work order, and with which tests and result.

### Implemented

Present in repository code or governed runtime data.

Implemented does not necessarily mean validated, operational, or released.

### Incomplete

A state in which required evidence, prerequisites, execution, or closure is missing.

### Independent review

Review performed by a qualified agent or human who did not materially author the reviewed work.

### Index

A derived structure supporting efficient lookup, search, or navigation.

An index is not the canonical source record.

### Instance

A specific runtime or Campaign occurrence derived from a Definition.

### Integrity check

A deterministic verification that artifacts, data, relationships, counts, versions, or checksums remain consistent.

### Internal alpha

The first controlled product-validation release using integrated real workflows and approved testers.

### Inventory

The governed collection of item and Asset instances held by a Character, party, container, vehicle, scene, campaign, or organization.

### Issue

A recorded defect, finding, request, risk, or task requiring disposition.

### Local-first

The principle that core development and validation should be runnable without mandatory paid or hosted providers.

### Localization

The governed translation and locale adaptation of presentation text, help, metadata, dates, numbers, and interface layout.

Executable rules and stable IDs remain unchanged.

### Manifest

A structured inventory of artifacts, files, schemas, versions, dependencies, checksums, or release contents.

### Material change

A change significant enough to invalidate context, approval, tests, review, migration, risk, or release evidence.

### Mechanics

The executable rules behavior governing Actions, Effects, Conditions, Resources, modifiers, timing, and outcomes.

### Migration

A governed transformation from one schema, content, pack, event, snapshot, or state version to another.

### Modifier

A governed adjustment, replacement, multiplier, cap, floor, suppression, or priority rule affecting a calculation.

### Monorepo

A single governed repository containing multiple applications, packages, domains, schemas, fixtures, tools, tests, and release assets.

### Multiversal

The tabletop role-playing platform and project owned by John Brandon Turner.

### Noncanonical

Not approved as controlling canon.

A noncanonical record may still be useful as a draft, example, proposal, fixture, or Campaign-local object.

### Object picker

The reusable interface used to find and select governed objects while enforcing type, permission, entitlement, installation, and compatibility constraints.

### Observability

The logs, metrics, traces, health checks, audit evidence, and cost signals used to understand system behavior.

### Offline

Operating without current network access.

Offline capability remains governed by cached permissions, entitlement snapshots, conflict rules, and reconnect validation.

### Open decision

A question requiring governed resolution before affected work may proceed.

### Operational

In active project use.

Operational does not necessarily mean public or production.

### Outbox

A transactionally persisted queue of messages to be delivered after authoritative state commits.

### Owner

John Brandon Turner, the final project, product, canon, spending, and release authority.

### Owner pack

The single canonical pack responsible for a stable reusable record.

### Ownership

The governed legal or in-world control relationship for an Asset.

Ownership is distinct from custody, access, location, station, and entitlement.

### Pack

A governed `.pack` archive containing reusable Multiversal content and metadata.

### Pack installation

The governed process of validating, resolving dependencies, registering, migrating, and activating a pack for a scope.

### Participant

A subject connected to a Campaign or live Session under a defined role.

### PASS

A final state indicating that every required criterion for the governed scope passed with evidence.

PASS proves only that defined scope.

### Permission

A specific allowed action evaluated through authorization.

### Placement

A Campaign, scene, or world binding that locates or configures a reusable Definition without changing the source Definition.

### Player

A Campaign participant who controls permitted Characters and proposes actions through the Player experience.

### Port

A provider-neutral interface describing a capability required by Multiversal.

### Preview

A nonauthoritative rendering or calculated projection shown before acceptance, publication, or canonical promotion.

### Product baseline

An approved exact expected product behavior or output used in regression testing.

### Production

The live trusted environment serving approved users under production credentials, operations, privacy, and support.

No current planning package authorizes production.

### Progression

The governed process by which a Character or other object gains, spends, selects, unlocks, or changes capabilities over time.

### Projection

A role-, permission-, and context-filtered representation of authoritative state.

### Prompt injection

Untrusted content attempting to redirect an AI agent away from approved instructions, permissions, or task scope.

### Proposal

A submitted but not yet accepted request or content change.

Examples include:

- Player Action proposal;
- AI proposal;
- creator submission;
- architecture proposal.

### Provider

An external service supplying identity, database, storage, realtime, search, AI, notifications, deployment, billing, or another capability.

### Provider exit

The ability to export, restore, and import Multiversal state into a replacement environment while preserving internal identity and history.

### Provider-neutral

Designed so domain contracts do not depend on one named vendor’s identity, SDK, event format, query language, or storage representation.

### Provenance

The retained chain connecting a canonical record to source files, source coordinates, mappings, transformations, reviewers, versions, and releases.

### Quality gate

A blocking evidence check applied during work execution, review, merge, migration, or release.

### Reaction

An Action or decision opportunity triggered by another event, action, or condition.

### Readiness track

A setting or release dimension measured independently rather than collapsed into one misleading completion percentage.

### Realtime

Low-latency delivery of role-filtered session messages.

Realtime transport is advisory; committed persistence remains authoritative.

### Receipt

A durable evidence record proving that a governed operation, validation, context load, approval, migration, restore, release, or handoff occurred.

### Record

A structured governed unit of data with stable identity, status, source, version, and lifecycle.

### Recovery

The governed process of restoring work, data, Sessions, environments, or agent continuity after interruption or failure.

### Regression

An unintended difference from approved behavior, schema, baseline, performance, or compatibility.

### Relationship

A typed, directional or nondirectional governed connection between objects.

### Release

A versioned approved distribution of content, application code, package, operating assets, or another deliverable.

### Release candidate

An exact frozen artifact proposed for a release gate.

### Release receipt

Evidence preserving the exact candidate, approval, checksums, environment, migration, rollback, and result.

### Repository evidence

Verified repository state such as:

- file;
- commit;
- pull request;
- review;
- CI;
- branch;
- merge.

Repository evidence may supersede stale handoff summaries.

### Resource

A typed quantity, pool, capacity, meter, charge, currency, time value, or other governed expendable or recoverable state.

### Restore

The governed process of applying a verified backup, checkpoint, or export to recover compatible state.

### Result matrix

A structured list of required checks and their states.

WP-011 uses a result matrix beginning with `NOT_RUN`.

### Review finding

A reviewer’s recorded issue, recommendation, rejection, approval condition, or risk.

### Risk

A possible future event or condition that may negatively affect canon, product, users, security, data, cost, schedule, release, or another project objective.

### Role

A durable organizational function with defined mission, authority, inputs, outputs, restrictions, and review obligations.

### Rollback

A governed process restoring a prior safe application, configuration, pack, or environment state.

Database and accepted user-state changes may require forward repair rather than destructive rollback.

### Rules profile

A governed configuration selecting or parameterizing approved rules for a Campaign, setting, scene, or product mode.

### Runtime

The executing rules and state system used during application or play.

### Scene

A Campaign-bound playable situation with participants, location, environment, objectives, hidden information, triggers, content placements, and live state.

### Schema

A machine-readable contract describing allowed data shape, fields, types, versions, constraints, and validation.

### Search index

A derived permission-aware structure used to find governed content.

It must not leak hidden or restricted content.

### Security event

An append-only record of a security-relevant occurrence.

### Seed

A recorded deterministic input used to reproduce a random resolution.

### Service actor

A nonhuman internal subject such as a background worker, AI service, indexer, or backup process.

### Session

A live or planned period of Campaign play with participants, authoritative state, commands, events, projections, and recovery.

### Snapshot

A stored state representation bound to versions and an event cursor.

### Source

An artifact or record supporting a claim, mapping, rule, content object, or decision.

### Source coordinate

A reproducible location inside a source, such as:

- page;
- line;
- row;
- section;
- archive member;
- object path.

### Source registry

The governed catalog of source identities, authority, status, locators, versions, digests, and scope.

### Sponsored month

A time-bounded entitlement source defined by P9-01.

Its expiration must not delete historical state.

### Stable ID

A persistent machine identity independent of display name, file path, locale, provider ID, or presentation.

### Stale

No longer current because an authoritative version, repository state, approval, context, or event sequence changed.

### Stop-work

A reversible hold applied when authority, evidence, safety, scope, or a required gate is invalid.

### Superseded

Replaced by a newer controlling version while retained for history and migration.

### Task packet

The sealed execution envelope containing the work order and required subordinate records.

### Telemetry

Operational measurements such as metrics, traces, logs, health, errors, and cost signals.

Telemetry should not expose protected content.

### Tenant

A technical isolation scope used by an implementation.

The term must not override Campaign, user, or ownership semantics.

### Test fixture

Deterministic data used to verify behavior.

A fixture is not production or canonical content unless explicitly released as such.

### Tool receipt

Evidence recording a tool operation, input identity, result, and errors.

### Transaction

A persistence boundary in which related state changes commit together or do not commit.

### Transactional outbox

An outbox written in the same transaction as authoritative state so delivery can be retried without losing committed events.

### Universal object experience

The shared browse, search, filter, inspect, compare, select, relationship, provenance, and preview workflow used across content domains.

### Validated

Verified through the defined tests, schemas, governance checks, or review appropriate to the stated scope.

### Validation

The process of determining whether data, behavior, workflow, migration, or evidence satisfies a defined contract.

### Variant

A governed related object that differs from a base object while retaining explicit lineage and compatibility.

### Version

An explicit identifier for the state of a document, schema, object, event, pack, API, application, artifact, or policy.

### Visibility

The governed scope in which information may be disclosed.

### Work order

The versioned approved assignment defining objective, scope, authority, roles, context, acceptance criteria, tests, rollback, outputs, and handoff.

### Workspace

The product context in which a user performs work, or the isolated repository environment in which an agent performs implementation.

The surrounding chapter determines the meaning.

### Worktree

A separate Git working directory bound to a branch and used to isolate one agent or work order.

### World

A governed setting Definition inside Multiversal cosmology.

A World may contain Regions, Settlements, Locations, Environments, factions, history, and content references without duplicating those Definitions.

### World Builder

The governed authoring interface for Worlds, Realities, Regions, Locations, factions, history, adventures, and related content.

### Zero-service

A local development or validation mode that does not require mandatory hosted providers, paid services, production credentials, or network availability.

---

# Appendix B — Abbreviations

## B.1 Purpose

This appendix expands common abbreviations used in Multiversal planning, repositories, packs, tests, implementation, and release records.

An abbreviation may have a more specific meaning in a governing package. The governing package controls.

## B.2 Project and program abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| AIOC | AI-Orchestrated Coordination, or the project’s AI operating and governance system | Governance repository, role structure, work orchestration, current-state recovery |
| DB | Development Bible or Development Brain, depending on document context | Canonical documentation and operating packages |
| MV | Multiversal | Document and artifact prefixes |
| MS | Milestone Series | Governed repository and platform work packages |
| WP | Work Package | Bounded implementation or preparation package |
| P9 | Phase 9 | Application-readiness and implementation program |
| P10 | Phase 10 | Core Application Implementation |
| P11 | Phase 11 | GM and Player Experience |
| P12 | Phase 12 | AI Team and Automation |
| P13 | Phase 13 | Internal Alpha Completion |
| RC | Release Candidate | Frozen artifact proposed for release validation |
| ADR | Architecture Decision Record | Technical decision preservation |
| DR | Decision Record | General governed decision preservation |

## B.3 Phase 8 abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| 8A | Phase 8 standards work | Pack, identity, schema, and object standards |
| 8B | Phase 8 abilities and progression work | Ability and progression canonicalization |
| 8C | Phase 8 shared mechanics work | Actions, Effects, Conditions, Resources, modifiers, profiles |
| 8D | Phase 8 validation and AI operating work | Golden tests, balance harness, AI Development Team |
| 8E | Phase 8 remaining-domain canonicalization | Species, items, creatures, settings, adventures, final validation |
| 8D-007 | Golden Test Corpus and Balance Harness | Deterministic regression and balance evidence |
| 8D-008 | AI Development Team Operating Package | Roles, authority, context, workflow, recovery |
| 8E-008 | Final Domain Validation | Cross-pack, schema, lifecycle, coverage validation |
| 8E-009 | Canonical Object Template and CSV-first Conversion | Final governed dataset promotion |

## B.4 Phase 9 and Stage A abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| P9-01 | Entitlements and Freemium Architecture | Access policy, sponsored months, campaign grants |
| P9-02 | Authoritative Session Architecture | Commands, projections, reconnect, checkpoints |
| P9-03 | Technology Decision Package | Architecture-class decision |
| P9-04 | Postgres-Centered Architecture Contract | Provider-neutral service and data boundaries |
| P9-05 | Bounded Technical Spike and Cost Envelope | Technology verification and cost guardrails |
| P9-06 | Implementation Backlog and Acceptance Gates | Ordered repository implementation |
| A0 | Stage A UI Baseline Audit | Verified starting implementation state |
| A1 | Stage A Client Foundation | Portable client, UI primitives, responsive shell |
| A2 | Universal Object Experience | Browse, search, inspect, select, provenance |
| A3 | Identity, Dashboard, and Workspace Selection | User entry and permission-aware navigation |
| A4 | Character Workspace | Character creation, validation, advancement |
| A5 | Campaign and Scene Workspace | GM campaign and scene building |
| A6 | First Playable Action and Approval Loop | Player proposal to GM result |
| A7 | Full Combat Interface | Complete encounter workflow |
| A8 | Inventory, Equipment, Crafting, and Vehicles | Assets and ownership workflows |
| A9 | Investigation and Social Workspaces | Persistent noncombat workflows |
| A10 | World Builder and Content Creation | Governed authoring tools |
| A11 | Contextual AI Interfaces | Permission-aware source-linked assistance |
| A12 | Internal-Alpha Hardening | Accessibility, recovery, performance, onboarding |

## B.5 Acceptance and authority abbreviations

| Abbreviation | Expansion | Meaning |
|---|---|---|
| AG | Acceptance Gate | P9-06 implementation gate |
| AG-01 | Repository Safety | Protected baseline, no secrets, reproducible local environment |
| AG-02 | Provider-Neutral Boundaries | Ports, adapter isolation, contract tests |
| AG-03 | Data Foundation | Schemas, migrations, fixtures, backup, restore, export |
| AG-04 | Identity and Entitlements | Mapping, isolation, access transitions |
| AG-05 | Authoritative Sessions | Server authority, hidden information, reconnect |
| AG-06 | Operations and Exit | Audit, cost monitoring, provider exit |
| AG-07 | Two-Device Alpha | Distinct clients, Player and GM workflow |
| AG-08 | Owner Release Decision | Exact release evidence and owner approval |
| A0 | Execute approved bounded work | Decision level; distinct from Stage A A0 when context is authority |
| A1 | Recorded reversible implementation choice | Decision level |
| A2 | Peer-reviewed material change | Decision level |
| A3 | Owner approval required | Decision level |
| A4 | Prohibited | Decision level |
| DoR | Definition of Ready | Blocking task-entry criteria |
| DoD | Definition of Done | Blocking task-closure criteria |
| SoD | Separation of Duties | Required independence among roles |
| RACI | Responsible, Accountable, Consulted, Informed | General responsibility model where used; Multiversal authority still uses its own permission matrix |

## B.6 Technical abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| API | Application Programming Interface | Service and client contracts |
| CI | Continuous Integration | Automated repository validation |
| CD | Continuous Delivery or Deployment | Must be distinguished; production deployment remains owner-gated |
| CRUD | Create, Read, Update, Delete | Basic persistence operations |
| DB | Database | Technical context only |
| DDL | Data Definition Language | Database schema operations |
| DTO | Data Transfer Object | Boundary payload, not canonical domain object |
| E2E | End to End | Complete workflow testing |
| ETL | Extract, Transform, Load | Source recovery or data migration |
| FTS | Full-Text Search | Search implementation option |
| HTTP | Hypertext Transfer Protocol | Web service transport |
| HTTPS | HTTP over TLS | Secure web transport |
| ID | Identifier | Stable identity or provider identity, as qualified |
| JWT | JSON Web Token | Possible authentication token format; not mandated |
| JSON | JavaScript Object Notation | Structured data format |
| JSONL | JSON Lines | One JSON record per line |
| MCP | Model Context Protocol | Tool and app integration context where used |
| ORM | Object-Relational Mapping | Optional persistence implementation detail |
| PII | Personally Identifiable Information | Protected identity and contact data |
| RLS | Row-Level Security | Database isolation control where supported |
| SDK | Software Development Kit | Provider or platform adapter dependency |
| SLA | Service-Level Agreement | External contractual target; not currently claimed |
| SLI | Service-Level Indicator | Measured reliability or performance signal |
| SLO | Service-Level Objective | Internal or contractual target |
| SQL | Structured Query Language | Relational data and portable export |
| TLS | Transport Layer Security | Encryption in transit |
| TTL | Time to Live | Cache, token, or temporary-artifact lifetime |
| UI | User Interface | Human-facing application |
| URI | Uniform Resource Identifier | Stable locator syntax |
| URL | Uniform Resource Locator | Network locator |
| UX | User Experience | Workflow clarity and usability |
| UUID | Universally Unique Identifier | Possible stable-ID primitive |
| WebSocket | Persistent bidirectional web transport | Possible realtime adapter |
| CSV | Comma-Separated Values | Source-recovery and portable tabular format |
| SHA-256 | Secure Hash Algorithm, 256-bit | Artifact and state integrity digest |

## B.7 Testing and quality abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| RNG | Random Number Generator | Seeded deterministic rules testing |
| E4 | Highest retained evidence class used by the balance program | Permanent balance claims require defined E4 evidence |
| Z-score | Standardized statistical distance | Robust peer-relative balance analysis |
| WCAG | Web Content Accessibility Guidelines | Accessibility reference target; exact release claim requires current audit |
| a11y | Accessibility | Common shorthand in code and testing |
| perf | Performance | Informal repository shorthand |
| lint | Static style and defect analysis | CI gate |
| smoke test | Narrow proof that a critical path starts and functions | Not full acceptance |
| contract test | Shared test proving an adapter satisfies a port | Provider-neutral verification |
| golden test | Exact expected-output regression test | 8D-007J and product baselines |

## B.8 Platform abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| iOS | Apple mobile operating system | WP-011 phone platform |
| iPadOS | Apple tablet operating system | WP-011 tablet platform |
| macOS | Apple desktop operating system | Borrowed-Mac host |
| Xcode | Apple development environment | Simulator and Apple build tooling |
| Tauri | Cross-platform desktop/mobile application framework | Current platform spike |
| PWA | Progressive Web App | Possible installable web direction |
| IPA | iOS application archive | Later packaging artifact; not a current WP-011 requirement |
| UDID | Unique Device Identifier | Apple simulator or device identity |
| 2FA | Two-Factor Authentication | Human credential gate where required |

## B.9 Release and operations abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| RPO | Recovery Point Objective | Maximum acceptable data loss interval |
| RTO | Recovery Time Objective | Target recovery duration |
| PITR | Point-in-Time Recovery | Provider capability for database restore |
| DR | Disaster Recovery | Service and data recovery program |
| UGC | User-Generated Content | Future public content and moderation boundary |
| ToS | Terms of Service | Public-release legal requirement |
| VAT | Value-Added Tax | Commercial tax requirement |
| MRR | Monthly Recurring Revenue | Future commercial metric; not current project status |
| MAU | Monthly Active Users | Future product metric |
| DAU | Daily Active Users | Future product metric |

## B.10 Repository and workflow abbreviations

| Abbreviation | Expansion | Project use |
|---|---|---|
| PR | Pull Request | Reviewed repository change |
| SHA | Secure Hash Algorithm digest or Git commit hash | Repository and artifact identity |
| WO | Work Order | Stable bounded assignment |
| WP | Work Package | Governed project package |
| ADR | Architecture Decision Record | Architecture evidence |
| CI run | Continuous-integration workflow execution | Gate evidence |
| RC | Release Candidate | Frozen release target |
| PASS | Required checks passed for stated scope | Final valid result |
| HARD_GATE | Evidence-complete incompatibility disposition | WP-011 |
| NOT_RUN | Required check not yet executed | WP-011 matrix and similar plans |
| N/A | Not Applicable | Allowed only when the governing profile permits it |

---

# Appendix C — Naming and Stable-ID Reference

## C.1 Purpose

Provide a concise reference for naming records, files, packages, schemas, branches, work orders, decisions, events, migrations, releases, and stable machine identities.

This appendix summarizes governing principles. Exact schemas and registries remain controlling.

## C.2 Core identity principle

A display name answers:

> What should a human see?

A stable ID answers:

> Which governed object is this?

A file path answers:

> Where is one representation currently stored?

A provider ID answers:

> How does one external system identify it?

These must not be collapsed.

## C.3 Stable-ID requirements

A stable ID should be:

- unique in its defined namespace;
- deterministic where the governing program requires determinism;
- independent of display name;
- independent of locale;
- independent of file path;
- independent of repository;
- independent of provider;
- preserved across ordinary edits;
- preserved across moves and renames;
- retained through deprecation and supersession;
- compatible with export and migration.

## C.4 Names are mutable

A display name may change because of:

- spelling correction;
- capitalization;
- localization;
- owner decision;
- lore revision;
- UI shortening;
- accessibility;
- product terminology.

A name change does not normally create a new stable ID.

## C.5 New identity threshold

A new stable ID is normally required when the record becomes a materially distinct governed object rather than a revised presentation of the same object.

Examples include:

- independent variant;
- separate timeline entity;
- cloned Campaign-local content promoted as a new reusable Definition;
- new Action with materially different semantics;
- replacement schema contract;
- new Work Order version where the governing standard requires immutable version identity.

## C.6 Recommended ID anatomy

The project uses several governed ID families.

A conceptual object ID may include:

```text
<namespace>:<object-family>:<stable-key>
```

A conceptual document or work package ID may include:

```text
MV-<PROGRAM>-<SEQUENCE>
```

A conceptual work-order ID may include:

```text
WO-<PROGRAM>-<ITEM>-<SEQUENCE>
```

The exact syntax is controlled by the applicable schema or registry.

## C.7 Namespace

A namespace identifies the owning authority or extension domain.

Namespaces help prevent collisions among:

- core content;
- setting packs;
- adventure packs;
- campaign-local content;
- extensions;
- third-party future content;
- provider mappings.

A namespace does not grant canonical authority by itself.

## C.8 Stable key

A stable key should prefer a durable normalized identifier over a current display phrase.

Avoid stable keys derived only from text likely to change.

## C.9 Case

Machine IDs should use the case required by the schema.

Do not assume case-insensitive comparison unless the contract says so.

Human display names preserve approved capitalization.

## C.10 Characters

Stable IDs should normally use a restricted portable character set.

Recommended portable characters are:

- lowercase ASCII letters;
- digits;
- hyphen;
- underscore;
- colon or period only when the governing schema assigns meaning.

Avoid spaces and locale-dependent punctuation in machine IDs.

## C.11 Reserved separators

Separators must not be used ambiguously.

If `:` separates namespace, it should not also appear unescaped inside a segment.

If `/` is used as a path separator, it should not be treated as part of the stable ID unless the schema explicitly defines a URI.

## C.12 Slugs

A slug is a human-readable normalized string used for:

- URLs;
- filenames;
- branch names;
- search;
- display.

A slug is not automatically the stable ID.

Slugs may change. Stable IDs normally remain.

## C.13 Aliases

Aliases may preserve:

- legacy names;
- alternate spellings;
- translated names;
- abbreviations;
- prior titles;
- source labels.

An alias should point to the stable record rather than creating a duplicate.

## C.14 Source IDs

A source ID should remain stable across:

- file movement;
- archive extraction;
- display-title change;
- reindexing.

A source registry record should also preserve:

- locator;
- version;
- digest;
- authority;
- status;
- scope.

## C.15 Source coordinates

A source coordinate should identify a reproducible location such as:

```text
source-id + page
source-id + line range
source-id + CSV row key
source-id + JSON pointer
source-id + archive member path
```

Coordinates should not rely only on a viewer’s temporary pagination.

## C.16 Canonical object IDs

Canonical object IDs should be used for:

- references;
- relationships;
- grants;
- actions;
- effects;
- pack ownership;
- migrations;
- events;
- search;
- exports.

Display text should not be used as a foreign key.

## C.17 Definition, placement, and instance IDs

A reusable Definition, a Campaign placement, and a live instance require separate identities.

Example conceptual identities:

```text
definition-id
placement-id
instance-id
```

A placement references a Definition.

An instance may reference both a placement and Definition.

## C.18 Event IDs

An Event should have:

- stable event ID;
- aggregate or Session ID;
- sequence;
- event type;
- schema version.

Event sequence and Event ID serve different purposes.

## C.19 Command IDs

A Session command ID supports idempotency.

The command ID should be scoped as defined by the service contract, normally including the Session context.

Reusing a command ID with different input is invalid.

## C.20 Operation IDs

Long-running operations such as:

- backup;
- restore;
- export;
- migration;
- index rebuild;
- pack installation;

should have stable operation IDs used by status, logs, receipts, and retry handling.

## C.21 Subject IDs

Internal subject IDs are independent of:

- email;
- username;
- provider user ID;
- display name;
- device.

External provider identities are mappings to the internal subject.

## C.22 Campaign IDs

Campaign IDs remain stable across:

- title change;
- GM change;
- pack update;
- archive;
- export;
- provider migration.

## C.23 Character IDs

Character IDs remain stable across:

- advancement;
- form change;
- display-name change;
- migration;
- controller delegation;
- Campaign transfer where policy permits;
- retirement.

A clone creates a new Character ID.

## C.24 Asset-instance IDs

Every unique Asset instance should have stable identity when history, ownership, condition, modification, or location matters.

Stacks may use a stack identity plus governed quantity, but split operations normally create or preserve explicit instance lineage.

## C.25 Pack IDs

A pack ID identifies the pack across versions.

A pack-version ID or version field identifies a specific release.

Do not use the archive filename as the only pack identity.

## C.26 Owner-pack rule

Each stable reusable record has one owner pack.

Other packs may:

- reference;
- extend;
- place;
- grant;
- override through approved mechanisms.

They must not silently duplicate ownership.

## C.27 Pack filenames

Release archives should use a deterministic descriptive filename containing, as applicable:

- project;
- program or pack identity;
- title;
- version;
- extension.

The approved content-pack extension is:

`.pack`

ZIP archives may be used for project handoff or development packages, but a released content pack remains a `.pack`.

## C.28 Document IDs

Governed documents should use stable IDs such as:

```text
MV-APP-UI-001
MV-AI-BOOTSTRAP-001
MV-P9-06-IMPLEMENTATION-BACKLOG-001
```

The exact format is program-controlled.

## C.29 Work-order IDs

A work-order ID should identify:

- program;
- backlog or package item;
- bounded sequence where required.

The ID remains connected to:

- branch;
- commits;
- PR;
- tests;
- reviews;
- handoff;
- closure.

## C.30 Branch names

The preferred conceptual form is:

```text
wo/<work-order-id>-<short-slug>
```

Examples should remain portable and avoid:

- spaces;
- secrets;
- personal data;
- uncontrolled punctuation.

## C.31 Commit messages

A material commit message should identify the bounded purpose.

For backlog work, include the work item where practical.

Examples from verified repository history include:

```text
Complete P9-06-006 persistence and migration ports
Complete P9-06-007 realtime and authoritative session ports
```

## C.32 Pull-request titles

A PR title should identify:

- work item;
- outcome;
- bounded capability.

The PR description carries scope, tests, migration, security, rollback, and limitations.

## C.33 Migration IDs

Migration IDs should be:

- ordered;
- unique;
- immutable after release;
- environment-independent;
- connected to source and target schema versions.

A migration filename should not be renamed after application if the migration system depends on its identity.

## C.34 Schema IDs

Schemas should identify:

- schema family;
- version;
- object or contract type;
- namespace where applicable.

A schema file path is not the only schema identity.

## C.35 API versions

API and message versions should be explicit.

Do not infer compatibility from application version alone.

Relevant independent versions may include:

- API;
- command payload;
- event;
- snapshot;
- pack;
- canonical object;
- export;
- migration.

## C.36 Semantic versions

When semantic versioning is used:

- major indicates incompatible change;
- minor indicates backward-compatible capability;
- patch indicates backward-compatible correction.

The project may use a different governed version model for drafts, datasets, migrations, or documents.

## C.37 Draft versions

Draft versions should remain distinguishable from approved releases.

A draft number does not imply approval or implementation.

## C.38 Release IDs

A release should bind:

- release name or ID;
- exact artifact;
- commit;
- manifest;
- versions;
- checksums;
- approval;
- environment where applicable.

## C.39 Decision IDs

A decision record should have stable identity independent of its title.

Superseding a decision creates a new record or version linked to the prior decision.

## C.40 Approval IDs

An approval ID should identify:

- authority;
- exact requested action;
- target digest;
- executor;
- environment;
- validity.

An approval title is not sufficient binding.

## C.41 Gate-run IDs

Every gate execution should have unique identity.

A rerun creates a new run ID and links to the prior run.

A later PASS does not delete a prior FAIL.

## C.42 Test-case IDs

Canonical tests should use stable test-case IDs so:

- expected output;
- fixtures;
- runs;
- failures;
- baseline changes;
- release evidence;

remain traceable across file movement.

## C.43 Fixture IDs

Fixtures should identify their intended scope.

Examples include:

- identity fixture;
- entitlement fixture;
- Session fixture;
- pack lifecycle fixture;
- migration fixture;
- balance fixture.

A fixture should not masquerade as production content.

## C.44 Media IDs

Media identity should be stable and separate from:

- filename;
- CDN URL;
- storage bucket;
- derivative path.

Media metadata should include content hash, rights, visibility, and derivative relationships.

## C.45 Localization keys

Localization keys should be stable and independent of translated text.

Changing English copy should not require changing the localization key unless the concept changes.

## C.46 Environment names

Environment names should be explicit:

- local;
- test;
- preview;
- integration;
- internal-alpha;
- staging;
- production.

Avoid ambiguous labels such as `live-test`.

## C.47 Provider mappings

Provider mappings should preserve:

```text
internal-id
provider-name
provider-id
environment-or-tenant
status
```

The provider ID never replaces the internal stable ID.

## C.48 Naming object types

Object-type names should be singular in schema definitions unless the governing standard says otherwise.

Collections may use plural names.

Examples:

```text
Action
Effect
Condition
Resource
Character
Creature
Item
Vehicle
Scene
Campaign
```

## C.49 File naming

File names should be:

- descriptive;
- portable;
- deterministic where generated;
- free of secrets;
- connected to stable document or package identity;
- versioned where release identity requires it.

## C.50 Generated output naming

Generated outputs should include enough identity to distinguish:

- source;
- version;
- environment;
- run;
- artifact type.

A generated file should not overwrite a released artifact without a new version.

## C.51 Checksums

Checksum files should identify the artifact they verify.

Recommended format:

```text
<artifact-name>.sha256
```

The checksum record should include the algorithm and exact byte artifact.

## C.52 Supersession

A superseded record should retain:

- old stable ID;
- replacement ID;
- reason;
- effective version;
- migration;
- compatibility;
- status.

Do not recycle the old ID for an unrelated object.

## C.53 Deprecation

Deprecation should identify:

- deprecated ID;
- replacement;
- release;
- warnings;
- migration;
- removal conditions.

Deprecated does not mean deleted.

## C.54 Tombstones

A tombstone preserves the identity of a removed or withdrawn object so:

- references remain explainable;
- imports detect absence;
- history remains intact;
- the ID is not reused.

## C.55 Collision handling

When two source claims would produce the same stable ID:

1. preserve both source claims;
2. inspect authority and identity;
3. determine duplicate, alias, variant, or conflict;
4. assign governed IDs;
5. retain mapping and disposition.

Do not append an arbitrary number without recording the reason.

## C.56 Canonical naming review

Naming review should check:

- source fidelity;
- owner-approved terminology;
- collision;
- alias;
- localization;
- pronunciation or readability where relevant;
- object-family consistency;
- stable identity;
- pack ownership.

## C.57 Legacy names

Legacy names remain in provenance and aliases when they support:

- source tracing;
- migration;
- user recognition;
- compatibility.

They should not control current display text if superseded.

## C.58 Example identity layers

Conceptual example:

```text
Pack ID:            pack:core-rules
Pack version:       1.0.0
Definition ID:      mv:action:basic-strike
Display name:       Basic Strike
Campaign placement: placement:campaign-123:basic-strike
Live command ID:    command:session-456:client-generated-id
Accepted event ID:  event:session-456:sequence-908
```

The exact production syntax remains schema-controlled.

## C.59 Validation

Stable-ID validation should check:

- required format;
- namespace;
- uniqueness;
- ownership;
- immutability;
- references;
- supersession;
- migration mapping;
- export preservation;
- case behavior.

## C.60 Final rule

Never repair an identity problem by silently changing IDs in place.

Use:

- mapping;
- supersession;
- migration;
- alias;
- tombstone;
- versioned decision;
- retained evidence.

---

# Appendix D — Canonical Repository Map

## D.1 Purpose

Provide a practical map of the canonical repositories, major governing paths, verified implementation areas, planned architecture areas, and repository-first recovery order.

The repository is authoritative only for what is actually present and verified at the current commit.

## D.2 Canonical repositories

### Governance and AIOC

```text
cybalicistjt-stack/multiversal-aioc
```

Primary responsibilities:

- governance;
- owner authority;
- current-state recovery;
- Development Brain;
- source recovery;
- object-system programs;
- roadmaps;
- AI operating assets;
- Phase 9 planning;
- startup instructions.

### Application

```text
cybalicistjt-stack/Multiversal-app
```

Primary responsibilities:

- active application implementation;
- client and platform shells;
- service ports;
- schemas;
- fixtures;
- validators;
- CI;
- tests;
- implementation work orders;
- build and release evidence.

## D.3 Repository-first recovery order

A new implementation session should:

1. verify access to both repositories;
2. read the canonical bootstrap;
3. read contributor authority;
4. inspect current-state and handoff records;
5. read the active Application Implementation Roadmap;
6. inspect recent application commits;
7. inspect open PRs and CI;
8. resolve the exact next unfinished item;
9. trust newer verified repository evidence over stale summaries;
10. update stale governance through a verified change.

## D.4 Governance repository map

### `governance/ai/`

Known purpose:

- mandatory AI bootstrap;
- conversation recovery protocol;
- AI operating instructions;
- startup behavior.

Key known artifact:

```text
governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md
```

### `governance/access/`

Known purpose:

- contributor identity;
- authority;
- proposal-only status;
- role and access records.

Key known artifact:

```text
governance/access/AIOC_CONTRIBUTOR_REGISTRY.json
```

### `governance/current-state/`

Known purpose:

- current workstream;
- session handoff;
- operational handoff;
- deployment baseline;
- recovery evidence.

Known artifacts include:

```text
governance/current-state/AIOC_CURRENT_STATE.md
governance/current-state/SESSION_HANDOFF.md
governance/current-state/AIOC_OPERATIONAL_HANDOFF.md
governance/current-state/AIOC_DEPLOYMENT_BASELINE.md
```

Caution:

A current-state file may become stale. Verify against newer commits, merged PRs, roadmap, and bootstrap.

### `governance/application-planning/`

Known purpose:

- application roadmap;
- Stage A program;
- UI implementation order;
- owner-approved product planning.

Known artifacts include:

```text
governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md
governance/application-planning/STAGE_A_UI_IMPLEMENTATION_PROGRAM.md
```

### `governance/phase9/`

Known purpose:

- entitlement architecture;
- authoritative-session architecture;
- technology decision;
- Postgres-centered architecture contract;
- bounded spike;
- implementation backlog and acceptance gates.

Representative artifacts include:

```text
governance/phase9/P9-03A_OWNER_TECHNOLOGY_SELECTION_RECORD.md
governance/phase9/P9-04_POSTGRES_CENTERED_ARCHITECTURE_CONTRACT.md
governance/phase9/P9-05_SPIKE_EXECUTION_AND_COST_GUARDRAILS.md
governance/phase9/P9-05_BOUNDED_TECHNICAL_SPIKE_AND_COST_ENVELOPE.json
governance/phase9/P9-06_IMPLEMENTATION_BACKLOG_AND_ACCEPTANCE_GATES.json
```

Caution:

The older backlog JSON contains a known numbering conflict with the newer active roadmap for P9-06-008. The newer active roadmap and bootstrap control active execution.

### `governance/object-system/`

Known purpose:

- canonical object architecture;
- canonical object template program;
- stable identity;
- object-system planning and state.

Key known artifact:

```text
governance/object-system/CANONICAL_OBJECT_TEMPLATE_PROGRAM.md
```

### `governance/development-brain/`

Known purpose:

- Development Brain entry point;
- canonical planning and implementation knowledge;
- durable project context.

Key known artifact:

```text
governance/development-brain/README.md
```

### `governance/content-recovery/`

Known purpose:

- legacy source recovery;
- governed source intake;
- coverage and conversion roadmap.

Key known artifact:

```text
governance/content-recovery/CONTENT_RECOVERY_ROADMAP.md
```

### `governance/project-memory/`

Known purpose:

- durable project facts;
- current canonical memory;
- replacement for reliance on private agent memory.

Key known artifact:

```text
governance/project-memory/PROJECT_MEMORY.json
```

### Other governance areas

The repository may also contain governed areas for:

- repository strategy;
- service activation;
- release;
- roles;
- work orders;
- quality gates;
- source registry;
- handoff;
- recovery;
- migrations;
- security;
- decisions.

Exact current paths should be verified at the current commit before use.

## D.5 Application repository verified map

### `.ai/ready-work-orders/`

Verified purpose:

- ready bounded implementation work orders.

Known artifact:

```text
.ai/ready-work-orders/STAGE-A-A1-client-foundation.md
```

### `docs/application-planning/`

Verified purpose:

- implementation-facing product planning and repository audit evidence.

Known artifact:

```text
docs/application-planning/STAGE_A_A0_UI_BASELINE_AUDIT.md
```

### `apps/client-ui/`

A0 state:

- structural placeholder;
- zero product routes and screens.

A1 merged state:

- portable client foundation;
- React/Vite direction;
- responsive shell;
- recoverable application states;
- interaction and accessibility checks.

Always inspect the current default branch rather than relying only on A0.

### `packages/ui-system/`

A0 state:

- planned workspace area without verified product design-system implementation.

A1 merged state:

- shared UI primitives and foundation.

Later Stage A work should extend this area through governed reusable components.

### `apps/desktop-tauri/`

Verified purpose:

- Tauri desktop and Apple-spike shell.

Known WP-011 uses:

- repository-pinned Tauri CLI;
- iOS generation;
- simulator build;
- local note or storage spike behavior.

This is not the full Multiversal product UI.

### Provider-neutral port areas

P9-06-004 through P9-06-007 introduced verified repository foundations for:

- identity;
- entitlement;
- persistence;
- migration;
- realtime;
- authoritative sessions.

Exact file paths should be resolved from the current commit before implementation.

### Schemas, fixtures, validators, and CI

The verified port PRs added:

- schemas;
- contract fixtures;
- validators;
- dedicated CI validation.

The precise directory layout should be read from the repository rather than inferred from PR titles.

## D.6 Planned application monorepo areas

The approved repository strategy includes conceptual top-level areas such as:

```text
apps/
packages/
crates/
domains/
schemas/
content/
fixtures/
tests/
infra/
ci/
scripts/
tools/
docs/
release/
.agent/
```

Status:

- some areas may exist;
- some may be partial;
- some remain planned;
- none should be claimed as implemented without repository verification.

## D.7 Intended area responsibilities

### `apps/`

Application shells and composed product entry points.

Examples may include:

- web client;
- desktop Tauri;
- mobile Tauri;
- Capacitor;
- static site;
- signaling or local relay.

### `packages/`

Portable TypeScript contracts and reusable logic.

Examples may include:

- contracts;
- capabilities;
- rules runtime;
- packs;
- entitlements;
- Session protocol;
- local storage;
- projections;
- export/import;
- diagnostics;
- UI system;
- testing;
- configuration;
- security.

### `crates/`

Rust-native capabilities used by Tauri or platform integration.

### `domains/`

Bounded product domains after decomposition.

Examples may include:

- identity;
- Campaign;
- Character;
- inventory;
- Session;
- search;
- packs.

### `schemas/`

Canonical machine-readable contracts.

### `content/`

Governed content sources or compiled content outputs, according to repository policy.

### `fixtures/`

Deterministic test and local-development data.

### `tests/`

Cross-package integration, acceptance, replay, and lifecycle tests.

### `infra/`

Optional provider and environment profiles.

Infrastructure files do not authorize provider activation.

### `ci/`

Repository-owned CI scripts and shared validation entrypoints.

### `scripts/`

Bounded automation and maintenance scripts.

### `tools/`

Reusable validators, generators, migration tools, and developer utilities.

### `docs/`

Implementation-facing architecture, work orders, runbooks, and evidence.

### `release/`

Generated release manifests, receipts, checksums, and notes.

### `.agent/` or `.ai/`

Agent startup, ready work orders, task packets, and bounded execution material.

The exact active hidden directory should follow current repository practice.

## D.8 Canonical content package locations

The large Phase 8 completion packages currently exist primarily as governed release archives and source packages.

The Development Bible should not invent permanent repository paths for artifacts that have not yet been imported into the canonical repository.

When imported, preserve:

- package identity;
- version;
- checksums;
- source registry;
- owner-pack map;
- release manifest;
- migration.

## D.9 Local project artifacts

The current master Bible artifact is maintained at:

```text
/mnt/data/MULTIVERSAL_PROJECT_BIBLE_v2.0.md
```

This sandbox path is a working delivery artifact, not the permanent canonical repository path.

A later governed repository integration should decide:

- destination repository;
- canonical path;
- document ID;
- release version;
- review;
- checksum;
- supersession.

## D.10 Uploaded source archives

Project source archives in the working environment include packages for:

- Phase 8;
- Phase 9;
- DB-004 Game Framework;
- repository bootstrap;
- WP-011 Apple spike;
- source coverage and provenance;
- prior conversation and catch-up packages.

These working paths support current editorial and recovery work.

They do not replace the source registry or canonical repository.

## D.11 Repository evidence precedence

When records disagree, use this process:

1. identify authority and scope;
2. verify current repository file;
3. verify commit and branch;
4. inspect merge evidence;
5. inspect CI;
6. compare roadmap and bootstrap dates;
7. preserve historical conflicting record;
8. follow newer controlling evidence;
9. update stale governance through a reviewed change.

## D.12 Safe repository claims

A safe claim names:

- repository;
- path or commit;
- branch;
- status;
- exact evidence;
- limitation.

Example:

> P9-06-007 is merged in `Multiversal-app` at squash commit `149b866f530f3a8896170bfe3ba6af0c01fb2f72`.

Unsafe example:

> Realtime is finished.

The safe claim distinguishes port foundations from the full product workflow.

## D.13 Repository write boundary

Repository writes should occur only under:

- owner authorization;
- bounded work order;
- approved branch;
- current context;
- allowed paths;
- required review;
- CI;
- merge policy.

## D.14 Repository cleanup

After verified completion:

- preserve commits and PR evidence;
- preserve required artifacts;
- remove disposable worktrees;
- avoid deleting historical branches or evidence outside policy;
- update current state;
- create handoff.

## D.15 Canonical map maintenance

This appendix should be updated when:

- repositories change;
- paths become canonical;
- planned areas become implemented;
- current-state records move;
- Development Bible is integrated;
- provider or platform repositories are added;
- release structure changes.

---

# Appendix E — Decision Register

## E.1 Purpose

Consolidate the major active project decisions, authority, status, implications, supersession, and unresolved owner gates.

This register is a human-readable index.

The controlling decision remains the exact owner record, governance document, schema, repository evidence, or released package.

## E.2 Decision status vocabulary

| Status | Meaning |
|---|---|
| Active | Current controlling decision |
| Implemented foundation | Decision has verified repository foundation but broader work remains |
| Complete program | Planning, validation, or package program is complete |
| Owner-gated | Requires a future bounded owner decision |
| Deferred | Intentionally postponed |
| Superseded | Replaced by a newer controlling decision |
| Historical conflict | Retained prior record that conflicts with newer active evidence |
| Prohibited | Cannot be authorized under current governance |

## E.3 Ownership and authority decisions

### DEC-001 — Final project authority

**Decision:** John Brandon Turner is the owner and final authority for Multiversal.

**Status:** Active.

**Controls:**

- canon;
- product scope;
- priorities;
- spending;
- paid providers;
- production credentials;
- internal-alpha release;
- public release;
- public claims;
- material risk acceptance.

**Implication:** AI agents may recommend and execute bounded approved work but may not substitute for the owner.

### DEC-002 — Proposal-only contributor status

**Decision:** `zakvalentine` remains proposal-only unless a newer contributor-registry record explicitly changes that status.

**Status:** Active.

**Implication:** Contributions may be drafted and submitted but not promoted to canon or release without the required authority.

### DEC-003 — AI agents are replaceable workers

**Decision:** Authority belongs to roles, work orders, approvals, and repository evidence rather than to a particular model or agent identity.

**Status:** Active.

**Implication:** Agent replacement requires durable handoff and reconstruction.

### DEC-004 — A0 through A4 authority model

**Decision:** Work uses decision levels A0, A1, A2, A3, and A4.

**Status:** Active and validated.

**Implication:** A3 stops for owner approval. A4 is prohibited.

## E.4 Product and canon decisions

### DEC-005 — Product identity

**Decision:** Multiversal is a broad tabletop role-playing platform rather than one single game or campaign app.

**Status:** Active.

**Implication:** Architecture supports many settings, genres, rules profiles, play styles, content packs, and Campaigns.

### DEC-006 — Canon remains owner controlled

**Decision:** AI, tests, code, data conversion, popularity, or repeated use cannot independently create canon.

**Status:** Active.

**Implication:** Canonical promotion requires the governing authority.

### DEC-007 — Incomplete source content remains marked

**Decision:** Missing or conflicting source information is preserved as incomplete, variant, conflict, or open decision.

**Status:** Active.

**Implication:** Agents must not invent missing stats, lore, placements, worlds, or mechanics.

### DEC-008 — Shared mechanics are canonical infrastructure

**Decision:** Actions, Effects, Conditions, Resources, modifiers, rules profiles, grants, and progression use shared governed contracts.

**Status:** Complete program at architecture and canonicalization level.

**Implication:** Domains should not create separate incompatible engines.

### DEC-009 — Data is authoritative for executable behavior

**Decision:** Governed data and contracts control runtime behavior; prose alone does not become hidden executable logic.

**Status:** Active.

**Implication:** Mechanics must be structured, versioned, validated, and source-linked.

### DEC-010 — Deterministic resolution and replay

**Decision:** Inputs, ordering, seeds or rolls, Effects, and event history must support deterministic verification and replay.

**Status:** Active and validated through the 8D-007 framework.

### DEC-011 — GM adjudication is attributable

**Decision:** GM decisions are recorded and preserve original calculation and final accepted result.

**Status:** Active.

**Implication:** Adjudication must not silently rewrite history.

## E.5 Pack and object decisions

### DEC-012 — Content-pack extension

**Decision:** Released content packs use the `.pack` extension.

**Status:** Active.

### DEC-013 — One owner pack per stable record

**Decision:** Each reusable stable record has one owner pack.

**Status:** Active.

**Implication:** Other packs reference, extend, grant, or place the record rather than duplicating ownership.

### DEC-014 — Definition, placement, instance, event, snapshot, and projection are separate

**Decision:** The object architecture keeps reusable Definitions distinct from Campaign bindings and runtime state.

**Status:** Active.

### DEC-015 — Stable IDs survive rename and relocation

**Decision:** Stable identity is independent of display name, file path, locale, and provider ID.

**Status:** Active.

### DEC-016 — CSV-first canonical conversion

**Decision:** The final registered Phase 8E-009 datasets were promoted through the governed CSV-first object pipeline.

**Status:** Complete program.

**Evidence:** 20 datasets, 19,199 source rows, 19,199 promoted, zero unprocessed.

### DEC-017 — No claim beyond registered-source coverage

**Decision:** 8E-009 proves complete processing of the registered datasets, not that no unregistered legacy source remains.

**Status:** Active limitation.

## E.6 Balance and quality decisions

### DEC-018 — 8D-007J is a blocking regression gate

**Decision:** Affected rules, schema, migration, content, balance, and release work must pass the locked Golden Test Corpus and Balance Harness.

**Status:** Active.

### DEC-019 — Baselines cannot be edited merely to pass

**Decision:** A failing expected output remains evidence.

**Status:** Active and validated.

### DEC-020 — Balance findings do not auto-edit canon

**Decision:** Outliers and findings create review work, not automatic canonical changes.

**Status:** Active.

### DEC-021 — Human-playtest claims remain deferred

**Decision:** Simulation and deterministic tests do not prove table feel, pacing, usability, or final balance.

**Status:** Deferred pending a usable application and human testing.

## E.7 Application-experience decisions

### DEC-022 — Stage A uses vertical slices

**Decision:** Each application batch must connect navigation, screen, real data, actions, permissions, persistence, error states, responsive behavior, tests, preview, and owner review.

**Status:** Active.

### DEC-023 — Portable shared client

**Decision:** Product UI should be portable and shared across web and platform shells rather than duplicated independently.

**Status:** Implemented foundation through Stage A A1.

### DEC-024 — Player information hierarchy

**Decision:** The Player live view prioritizes:

- scene;
- character summary;
- available actions;
- targets;
- costs;
- proposal confirmation;
- result.

Action logs and My Proposals remain accessible but secondary.

**Status:** Active product requirement.

### DEC-025 — GM approval information

**Decision:** A GM approval item shows:

- actor;
- Player;
- Action;
- rule summary;
- targets;
- costs;
- roll;
- modifiers;
- computed result;
- proposed Effects;
- warnings.

**Status:** Active product requirement.

### DEC-026 — GM decision options

**Decision:** The GM may approve, deny, or modify a proposed result.

**Status:** Active product requirement.

### DEC-027 — Universal object experience before broad feature duplication

**Decision:** Shared browse, search, inspect, relationship, provenance, and picker components should be implemented before many domain-specific screens.

**Status:** Active; Stage A A2 remains incomplete.

### DEC-028 — Accessibility is built in

**Decision:** Accessibility is a feature-completion requirement, not a final cosmetic pass.

**Status:** Active.

## E.8 Technical-architecture decisions

### DEC-029 — Postgres-centered architecture class

**Decision:** The selected backend architecture class is Postgres-centered and provider-neutral.

**Status:** Active owner-approved architecture.

**Implication:** Relational integrity and transactions are primary, but no specific hosted provider is selected.

### DEC-030 — Provider-neutral ports and adapters

**Decision:** Domain services depend on Multiversal ports; named provider SDKs remain inside adapters.

**Status:** Active; foundations implemented through P9-06-007.

### DEC-031 — Stable internal subject identity

**Decision:** Internal subject identity is independent of provider account IDs.

**Status:** Active; identity-port foundation implemented.

### DEC-032 — Server-authoritative accepted state

**Decision:** Trusted services control identity, authorization, entitlements, session commands, hidden information, canonical state transitions, checkpoints, and audit.

**Status:** Active.

### DEC-033 — Realtime transport is advisory

**Decision:** Committed persistence is authoritative; realtime messages may duplicate or arrive late and must be reconciled.

**Status:** Active.

### DEC-034 — Transactional command execution

**Decision:** Authoritative commands validate, authorize, reject stale or duplicate input, append events, update state, enqueue publication, and commit atomically.

**Status:** Active architecture; complete end-to-end command handler remains future work.

### DEC-035 — Transactional outbox

**Decision:** State changes and outbound event records should commit together.

**Status:** Active architecture.

### DEC-036 — Restore preserves history

**Decision:** Recovery creates a new recovery event rather than erasing accepted history.

**Status:** Active.

### DEC-037 — Local-first and zero-service development

**Decision:** Core development and validation should run without mandatory hosted services, paid providers, or production credentials.

**Status:** Active; local-environment foundation implemented.

### DEC-038 — Modular-monolith direction

**Decision:** Early implementation should favor a modular monolith with explicit boundaries rather than premature microservices.

**Status:** Active architectural direction.

**Revisit trigger:** demonstrated scaling, isolation, operational, security, or release need.

## E.9 Entitlement and commercial decisions

### DEC-039 — Free ability tiers

**Decision:** Free access includes the first two Ability-tree tiers.

**Status:** Active.

### DEC-040 — Grants do not bypass tier policy silently

**Decision:** Higher-tier Abilities received through grants remain subject to entitlement evaluation.

**Status:** Active.

### DEC-041 — Campaign grants are scoped

**Decision:** A Campaign may grant content use within the Campaign without creating global ownership.

**Status:** Active.

### DEC-042 — Sponsored-month architecture

**Decision:** Sponsored-month access is time-bounded and must preserve historical state on expiry.

**Status:** Active.

### DEC-043 — Billing is not currently authorized

**Decision:** Entitlement architecture may be implemented and tested without activating public billing or commerce.

**Status:** Active restriction.

### DEC-044 — No paid services by implication

**Decision:** Tool access, implementation authorization, or a recommendation does not authorize paid enrollment or spending.

**Status:** Active.

## E.10 Cost and provider decisions

### DEC-045 — Bounded internal-alpha cost target

**Decision:** The bounded technical target is $0–$25 per month.

**Status:** Active planning guardrail.

### DEC-046 — Owner review above $35 per month

**Decision:** Expected cost above $35 per month requires owner review.

**Status:** Active.

### DEC-047 — Cost guardrails are not spending approval

**Decision:** A budget target does not authorize purchase, provider activation, or recurring charges.

**Status:** Active.

### DEC-048 — Provider exit is required

**Decision:** Identity, state, packs, events, media metadata, entitlements, and migration history must be exportable to a replacement environment.

**Status:** Active architecture; full current implementation remains incomplete.

## E.11 AI-development decisions

### DEC-049 — Role-based team structure

**Decision:** The AI team uses fourteen permanent roles, including one nonreplaceable human owner role.

**Status:** Complete and validated.

### DEC-050 — Independent review is real separation

**Decision:** A single agent changing hats does not create independent review.

**Status:** Active and validated.

### DEC-051 — Context is task-specific

**Decision:** Material work uses a sealed context manifest and load receipt.

**Status:** Active and validated.

### DEC-052 — Exact evidence cannot be compacted away

**Decision:** Schemas, approvals, baselines, conflicts, failures, and controlling records remain exact when required.

**Status:** Active.

### DEC-053 — Work requires a task packet

**Decision:** Natural-language prompts and issue titles do not replace a ready work order and task packet for material execution.

**Status:** Active.

### DEC-054 — “Continue” means execute

**Decision:** In this project, “Continue” means perform the next verified unfinished operation rather than provide only a plan.

**Status:** Active.

### DEC-055 — Ordinary failures are repaired automatically

**Decision:** Agents inspect, repair, rerun, and continue through ordinary implementation and CI failures.

**Status:** Active.

### DEC-056 — Stop only at genuine owner or prohibited gates

**Decision:** Work should not repeatedly return ordinary reversible choices to the owner.

**Status:** Active.

## E.12 Repository and implementation decisions

### DEC-057 — Canonical repositories

**Decision:** The canonical repositories are:

- `cybalicistjt-stack/Multiversal-app`;
- `cybalicistjt-stack/multiversal-aioc`.

**Status:** Active.

### DEC-058 — Repository evidence beats stale handoff

**Decision:** When newer verified repository state conflicts with a stale handoff, follow the newer evidence and update the stale governance record.

**Status:** Active.

### DEC-059 — Protected branch and isolated worktree workflow

**Decision:** Material work occurs through bounded branches, isolated worktrees, review, CI, and repository-permitted merge.

**Status:** Active.

### DEC-060 — P9-06 implementation authorization

**Decision:** John authorized bounded implementation of P9-06-001 through P9-06-023.

**Status:** Active.

**Restrictions:**

- no paid service;
- no production deployment;
- no public release;
- no production credentials;
- no irreversible vendor commitment;
- no unapproved spending.

### DEC-061 — Verified application boundary

**Decision record:** P9-06-001 through P9-06-007 are verified merged.

**Status:** Current verified repository state.

**Latest verified commit:** `149b866f530f3a8896170bfe3ba6af0c01fb2f72`

### DEC-062 — Current active task

**Decision:** The next active repository task is P9-06-008, backup, restore, and provider-exit export ports, as defined by the newer active roadmap and bootstrap.

**Status:** Active.

### DEC-063 — Older P9-06-008 label retained as historical conflict

**Decision:** The older backlog JSON’s use of P9-06-008 for an initial logical schema migration is historical planning evidence and does not control the current active task.

**Status:** Historical conflict.

**Implication:** Preserve the record; do not silently rewrite it.

### DEC-064 — Stage A A0 and A1 complete

**Decision record:** The UI baseline audit and portable client foundation are verified complete.

**Status:** Implemented foundation.

### DEC-065 — Stage A A2 through A12 remain incomplete

**Decision record:** Later universal object, workspace, gameplay, AI, and hardening stages require repository evidence.

**Status:** Active limitation.

## E.13 Release decisions

### DEC-066 — Internal alpha requires a separate owner gate

**Decision:** Repository implementation authorization does not authorize internal-alpha release.

**Status:** Owner-gated.

### DEC-067 — Public beta is a public release action

**Decision:** Public beta requires separate owner approval and public-readiness evidence.

**Status:** Owner-gated.

### DEC-068 — Production deployment is not authorized

**Decision:** No current package authorizes production credentials or deployment.

**Status:** Active restriction.

### DEC-069 — Public launch is not authorized

**Decision:** Public launch requires commercial, legal, security, privacy, accessibility, support, recovery, and owner gates.

**Status:** Owner-gated.

### DEC-070 — App-store submission is not authorized

**Decision:** WP-011 does not authorize App Store submission, production signing, or public distribution.

**Status:** Active restriction.

## E.14 Apple-track decisions

### DEC-071 — Borrowed Mac is one-time and Apple-only

**Decision:** The borrowed Mac is used only for the necessary Apple-specific spike and evidence work.

**Status:** Active.

### DEC-072 — WP-011 is bound to an exact commit

**Decision:** The sealed WP-011 v0.4.0 package is bound to:

`f1f49b504c414a56a5b8b762b175a5f6705c0f05`

**Status:** Active for that package.

### DEC-073 — PASS or HARD_GATE are valid final dispositions

**Decision:** WP-011 must end with evidence-complete PASS or HARD_GATE.

**Status:** Active.

### DEC-074 — Cleanup occurs after evidence verification and owner review

**Decision:** Project files, temporary access, and session-created assets are removed only after external evidence and checksums are verified.

**Status:** Active.

### DEC-075 — Main development does not wait for WP-011

**Decision:** Non-Apple implementation continues independently.

**Status:** Active.

## E.15 Documentation decisions

### DEC-076 — One master Markdown Bible

**Decision:** The working Development Bible is maintained as one master Markdown file.

**Status:** Active editorial decision.

**Current working artifact:**

```text
MULTIVERSAL_PROJECT_BIBLE_v2.0.md
```

### DEC-077 — Released evidence is append-only

**Decision:** Corrections create new versions and preserve prior evidence.

**Status:** Active.

### DEC-078 — Conversation memory is supporting context, not final authority

**Decision:** Material claims are verified against exact sources, repositories, owner records, and released artifacts.

**Status:** Active.

## E.16 Pending owner-gated decisions

The following decisions remain intentionally open until the relevant evidence exists:

1. Internal-alpha release candidate approval.
2. Closed-alpha entry.
3. Public-beta entry.
4. Production provider selection.
5. Paid-provider enrollment.
6. Production credentials.
7. Pricing and commercial plans.
8. Billing-provider activation.
9. Public launch.
10. App-store agreements and submission.
11. Public community and moderation scope.
12. Creator marketplace.
13. Material legal and jurisdictional risk acceptance.
14. Major future canon changes.
15. Residual risks that exceed delegated authority.

## E.17 Deferred decisions

The following remain deferred:

- human-playtest sufficiency;
- formal accessibility conformance;
- final balance;
- production scale;
- public moderation;
- marketplace;
- production AI automation;
- broad native-platform integrations;
- permanent Apple distribution toolchain;
- final commercial support model.

## E.18 Prohibited decisions

No authority may approve:

- falsifying evidence;
- concealing failure;
- rewriting a failed baseline merely to pass;
- fabricating owner approval;
- representing unimplemented work as implemented;
- exposing credentials intentionally;
- silently inventing canon from missing source material;
- destroying required audit and provenance evidence.

## E.19 Register maintenance

Update this register when:

- owner decision changes;
- roadmap changes;
- repository implementation advances;
- a gate completes;
- a provider is selected;
- a release is approved;
- a conflict is resolved;
- an architecture decision is superseded;
- the master Bible is released into a canonical repository.

Every update should preserve the prior decision and supersession relationship.



# Appendix F — Source and Provenance Index

## F.1 Purpose

Provide a durable human-readable index of the principal source families, repository records, released packages, uploaded archives, provenance rules, coverage evidence, source conflicts, and retrieval practices used to build and maintain the Multiversal Project Bible.

This appendix is an index. It does not replace the source registry, exact artifacts, repository evidence, release manifests, schemas, or owner decisions.

## F.2 Source principle

Every material claim should be traceable to one or more sources with:

- stable source identity;
- authority;
- status;
- version;
- locator;
- digest where available;
- applicable scope;
- relationship to superseded or conflicting sources.

A convenient file, recent conversation, summary, or search result is not automatically authoritative.

## F.3 Source authority layers

### F.3.1 Owner decisions

Highest authority for:

- canon;
- product scope;
- priority;
- spending;
- release;
- public claims;
- provider commitment;
- risk acceptance;
- final dispute resolution.

Owner decisions should be exact, bounded, versioned, and attributable.

### F.3.2 Active governance

Controls:

- authority;
- contributor status;
- repository-first recovery;
- active roadmap;
- work-order behavior;
- approval and stop conditions;
- current implementation program.

### F.3.3 Canonical released packages

Control the approved content, architecture, schemas, validation, and operating standards within their declared scope.

### F.3.4 Verified repository evidence

Controls current implementation truth when newer than planning or handoff summaries.

Repository evidence includes:

- current files;
- commits;
- merged pull requests;
- CI;
- release artifacts;
- branch state.

### F.3.5 Historical and provenance sources

Preserve:

- original wording;
- prior architecture;
- superseded plans;
- legacy names;
- source conflicts;
- migration context.

Historical sources remain important but do not automatically control current execution.

### F.3.6 Derived summaries

Support comprehension and handoff.

A derived summary must retain source identity and limitations. It does not replace the source.

## F.4 Canonical repository sources

### F.4.1 Governance repository

**Repository:** `cybalicistjt-stack/multiversal-aioc`

Primary source areas include:

- `governance/ai/`
- `governance/access/`
- `governance/current-state/`
- `governance/application-planning/`
- `governance/phase9/`
- `governance/object-system/`
- `governance/development-brain/`
- `governance/content-recovery/`
- `governance/project-memory/`

### F.4.2 Application repository

**Repository:** `cybalicistjt-stack/Multiversal-app`

Primary source areas include:

- active code;
- service ports;
- schemas;
- fixtures;
- validators;
- CI;
- implementation work orders;
- Stage A evidence;
- platform shells;
- build and test artifacts.

## F.5 Principal governance records

### F.5.1 New Conversation Bootstrap

**Path:**

```text
governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md
```

**Known version:** 4.0.0  
**Known status:** ACTIVE  
**Owner:** John Brandon Turner

Controls:

- mandatory repository-first recovery;
- execution-first behavior;
- repository permissions;
- current verified implementation boundary;
- current next task;
- owner-only restrictions;
- stale-evidence handling.

### F.5.2 Contributor Registry

**Path:**

```text
governance/access/AIOC_CONTRIBUTOR_REGISTRY.json
```

Controls:

- contributor identity;
- role;
- authority;
- proposal-only status;
- permitted actions.

Known standing instruction:

- `zakvalentine` remains proposal-only unless a newer registry entry changes the status.

### F.5.3 Application Implementation Roadmap

**Path:**

```text
governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md
```

Known active version used in this Bible:

- version 2.0.0;
- updated 2026-08-05.

Controls:

- completed Phase 8 state;
- Phase 9 architecture completion;
- P9-06 implementation authorization;
- current completed repository boundary;
- current next executable task;
- later application programs;
- production and spending restrictions.

### F.5.4 Stage A UI Implementation Program

**Path:**

```text
governance/application-planning/STAGE_A_UI_IMPLEMENTATION_PROGRAM.md
```

Known document ID:

`MV-APP-UI-001`

Known status:

`OWNER APPROVED — PLANNED`

Controls:

- A0 through A12 order;
- vertical-slice requirements;
- Player and GM interaction hierarchy;
- owner review expectations;
- real-data, permission, persistence, responsive, and test requirements.

### F.5.5 Canonical Object Template Program

**Path:**

```text
governance/object-system/CANONICAL_OBJECT_TEMPLATE_PROGRAM.md
```

Controls:

- object architecture;
- source recovery;
- 8E-009;
- deterministic identity;
- CSV-first conversion;
- canonical record promotion.

## F.6 Current-state and handoff sources

Known current-state paths include:

```text
governance/current-state/AIOC_CURRENT_STATE.md
governance/current-state/SESSION_HANDOFF.md
governance/current-state/AIOC_OPERATIONAL_HANDOFF.md
governance/current-state/AIOC_DEPLOYMENT_BASELINE.md
```

These records provide continuity but require freshness verification.

A known stale-state example is an earlier `AIOC_CURRENT_STATE.md` that still identified 8D-007 as active after later roadmap and bootstrap evidence recorded subsequent completion.

## F.7 Phase 0 and legacy-source family

Phase 0 includes the original game, setting, creature, item, ability, adventure, and world materials created by John Brandon Turner and his brother.

Legacy sources may contain:

- authoritative original wording;
- incomplete records;
- duplicate records;
- conflicting claims;
- layout-specific grouping;
- examples mixed with canon;
- mechanics embedded in prose.

Legacy sources are preserved through provenance even after normalization.

## F.8 Multiversal Definition Document

The Phase 0.5 Definition Document establishes:

- product identity;
- broad platform scope;
- intended participants;
- long-term capabilities;
- distinction between Multiversal and a single game application.

It controls high-level product intent but does not replace later detailed architecture.

## F.9 DB-004 Game Framework package

**Working archive:**

```text
Multiversal_DB-004_Game_Framework_v0.1.0.zip
```

**Working extracted path:**

```text
/mnt/data/db004_extract/Multiversal_DB-004_Game_Framework_v0.1.0/
```

Principal documents include:

```text
DevelopmentBible/02-game-framework/README.md
DevelopmentBible/02-game-framework/core-rules-model.md
DevelopmentBible/02-game-framework/characters-and-progression.md
DevelopmentBible/02-game-framework/actions-effects-conditions-and-resources.md
DevelopmentBible/02-game-framework/combat.md
DevelopmentBible/02-game-framework/social-play.md
DevelopmentBible/02-game-framework/investigation.md
DevelopmentBible/02-game-framework/exploration-and-environments.md
DevelopmentBible/02-game-framework/downtime-and-projects.md
DevelopmentBible/02-game-framework/crafting-and-economy.md
DevelopmentBible/02-game-framework/powers-and-ability-domains.md
DevelopmentBible/02-game-framework/creatures-npcs-and-species.md
DevelopmentBible/02-game-framework/items-vehicles-mecha-and-starships.md
```

Primary architectural principles incorporated into this Bible include:

- data authority;
- deterministic resolution;
- traceability;
- declaration, validation, resolution, application;
- explicit serializable inputs;
- deterministic ordering;
- recorded random results;
- no hidden partial mutation;
- separate Character composition and state;
- event-based progression;
- versioned Actions;
- bounded Effects;
- Condition lifecycle;
- typed Resources;
- explicit stacking;
- first-class combat, social, investigation, exploration, and downtime;
- advisory AI.

## F.10 Phase 8 source family

### F.10.1 Phase 8A

Controls:

- pack standards;
- `.pack` extension;
- stable IDs;
- schemas;
- references;
- ownership;
- provenance;
- lifecycle.

### F.10.2 Phase 8B

Controls:

- Abilities;
- Powers;
- progression;
- grants;
- prerequisites;
- environmental adaptations;
- simulation baselines.

### F.10.3 Phase 8C

Controls:

- Actions;
- Effects;
- Conditions;
- Resources;
- modifiers;
- rules profiles;
- shared progression and grant behavior.

### F.10.4 Phase 8D

Controls:

- golden tests;
- balance harness;
- AI-team roles;
- authority;
- context loading;
- work orders;
- quality gates;
- recovery;
- startup assets.

### F.10.5 Phase 8E

Controls:

- species;
- forms;
- items;
- creatures;
- NPCs;
- operational assets;
- settings;
- worlds;
- regions;
- locations;
- factions;
- lore;
- adventures;
- final validation;
- CSV-first promotion.

## F.11 8D-007 Golden Test Corpus sources

Principal source packages include the 8D-007 subpackages through final completion.

The validated release provides evidence for:

- 17 metric formulas;
- seven peer-group templates;
- four threshold profiles;
- five uncertainty profiles;
- seven domain evaluation models;
- 24 deterministic conformance cases;
- 175 inherited expectations;
- review thresholds;
- seeded bootstrap;
- Wilson intervals;
- 200,000-trial balance baseline;
- findings and disposition workflow;
- final release checks.

Principal final counts:

- 3,717 passing checks;
- 259 active canonical cases;
- 220 exact product baselines;
- 39 regression cases;
- 18 RNG conformance cases;
- 339 approved baseline objects;
- 21 retained E4 runs;
- 3,080,000 candidate trials;
- seven replay bundles;
- zero unexpected findings;
- 957 final acceptance checks;
- zero failures.

## F.12 8D-008 AI Development Team sources

Principal packages:

- 8D-008A Operating Scope and Governance Basis;
- 8D-008B Agent Team Structure and Role Catalog;
- 8D-008C Authority, Approval, and Escalation Matrix;
- 8D-008D Context Manifest and Source-of-Truth Registry;
- 8D-008E Context Loading and Retrieval Protocol;
- 8D-008F Work-Order and Task-Packet Standard;
- 8D-008G Development Workflow and Quality Gates;
- 8D-008H Change, Migration, Security, and Release Controls;
- 8D-008I Handoff, Recovery, and Operating Drill;
- 8D-008J AI Development Team Operating Package.

These packages control Volume VII and relevant developer appendices.

## F.13 8E-006 setting and adventure sources

The `Aaac (1).zip` working archive includes 8E-006 source packages covering:

- shared setting baseline;
- Branches, Realities, Worlds, and relationships;
- Regions, Settlements, Locations, and Environments;
- factions, cultures, lore, history, and timelines;
- world-pack assembly and dependencies;
- integrated setting and adventure release candidate.

Key validated distinctions include:

- Definitions separate from live state;
- Worlds reference Regions;
- Locations reference Environment Definitions;
- factions and cultures remain reusable Definitions;
- live reputation, membership, discovery, and control remain Campaign state;
- adventure Definitions reference scenes, objectives, clues, cast, routes, and rewards;
- GM truth remains separate from Player-safe information.

## F.14 8E-008 final validation sources

The final-domain validation family covers:

- cross-pack dependency testing;
- stable-ID verification;
- schema validation;
- installation;
- update;
- removal;
- source coverage;
- provenance;
- migration;
- cumulative release compatibility.

A dedicated source-coverage and provenance archive is available in the working environment:

```text
Multiversal_8E-008G_Source_Coverage_and_Provenance_Audit_v0.1.0.zip
```

## F.15 8E-009 canonical conversion sources

The final canonical conversion program establishes:

- 20 governed datasets;
- 19,199 source rows;
- 19,199 promoted records;
- zero unprocessed rows;
- deterministic stable identity;
- provenance;
- runtime validation;
- installation;
- uninstallation;
- zero unintended residue.

Final reconciliation digest recorded in the governing material:

```text
112ef5116b4090cc266eefe36e1c539b6567f022d6b857db6e1d2bdd77e30e40
```

## F.16 Phase 9 package sources

Working Phase 9 archive:

```text
Phase9.zip
```

Principal source areas include:

- P9-01 entitlements and freemium;
- sponsored-month amendment;
- P9-02 authoritative sessions;
- P9-03 technology decision;
- P9-04 Postgres-centered provider-neutral architecture;
- P9-05 bounded technical spike and cost envelope;
- P9-06 backlog and acceptance gates.

Known architecture contract path:

```text
governance/phase9/P9-04_POSTGRES_CENTERED_ARCHITECTURE_CONTRACT.md
```

## F.17 Application repository implementation evidence

Verified merged implementation evidence represented in this Bible:

| Item | PR | Commit |
|---|---:|---|
| P9-06-001 repository baseline | 71 | `d5d74140704115acebb03f4a899e3abf2d378b26` |
| P9-06-002 local environment | 72 | `0225d90959fc77baa5b895dcbefeea0f55b2ba4d` |
| P9-06-003 secrets isolation | 73 | `97a90ba1204125d4baf2be1763f9fc78f4dc301f` |
| P9-06-004 identity port | 74 | `f06d8733ba7478f58b82fa523e55d51ec8a72a66` |
| P9-06-005 entitlement port | 75 | `4e7934a4ad6fef2a31c2e6ecab5a66c838e160af` |
| P9-06-006 persistence and migration ports | 76 | `f8a34a43e58dd7d12f2eb2602e80c4aeacce8034` |
| P9-06-007 realtime and authoritative-session ports | 77 | `149b866f530f3a8896170bfe3ba6af0c01fb2f72` |
| Stage A A1 client foundation | 69 | `398f4d14fc189f8fc786aa093377a96e01d28548` |

## F.18 Stage A A0 source

Verified application path:

```text
docs/application-planning/STAGE_A_A0_UI_BASELINE_AUDIT.md
```

The A0 audit established the real pre-A1 baseline:

- zero product routes;
- zero product screens;
- zero reusable product components;
- zero connected product workflows;
- structural placeholders and platform spike evidence only.

## F.19 Stage A A1 source

Verified work-order path:

```text
.ai/ready-work-orders/STAGE-A-A1-client-foundation.md
```

Verified merge evidence records:

- portable React/Vite client;
- shared UI primitives;
- responsive shell;
- recoverable states;
- interaction tests;
- automated accessibility checks;
- responsive contracts;
- governed dependencies.

## F.20 WP-011 Apple source family

Working archive:

```text
Multiversal_MS-02_WP-011_One-Pass_Apple_Spike_v0.4.0.zip
```

Controls:

- exact commit binding;
- borrowed-Mac preflight;
- Xcode ceiling;
- repository-specific adapter;
- phone and tablet simulator testing;
- lifecycle;
- storage;
- accessibility smoke review;
- PASS or HARD_GATE;
- evidence preservation;
- cleanup.

## F.21 Governed repository bootstrap source

Working archive:

```text
Multiversal_MS-01_WP-004_Governed_Repository_Bootstrap_v0.1.0.zip
```

Controls:

- repository governance;
- startup;
- access and authority;
- one-pass repository operation;
- continuity and cleanup.

## F.22 Uploaded working archive inventory

The current working environment includes the following source archives or related artifacts:

```text
Aaab.zip
Current.zip
mvPreFinal.zip
Conversation.zip
Aaac (1).zip
Multiversal_8E-008G_Source_Coverage_and_Provenance_Audit_v0.1.0.zip
Aaad.zip
Phase9.zip
Multiversal_DB-004_Game_Framework_v0.1.0.zip
Multiversal_DB-004_Game_Framework_v0.1.0.zip.sha256
Multiversal_MS-01_WP-004_Governed_Repository_Bootstrap_v0.1.0.zip
Multiversal_MS-02_WP-011_One-Pass_Apple_Spike_v0.4.0.zip
Catch up.zip
```

These paths are working-environment references.

They should be represented in the permanent source registry before being treated as canonical repository sources.

## F.23 Archive-role notes

### `Aaab.zip`

Large Phase 8 canonicalization source family.

### `Aaad.zip`

Contains 8D-007 balance and validation materials used by the Bible.

### `Aaac (1).zip`

Contains 8E-006 setting and adventure integration materials.

### `mvPreFinal.zip`

Contains source material used by setting and source-reconciliation programs.

### `Conversation.zip`

Conversation-history support and project continuity source.

Conversation archives remain supporting evidence, not automatic authority.

### `Current.zip`

Current-state working package whose exact authority must be resolved by manifest and contents.

### `Catch up.zip`

Continuity package whose current status must be resolved before reuse.

## F.24 Provenance chain

The preferred provenance chain is:

1. Source registry record.
2. Exact source artifact and digest.
3. Exact source coordinate.
4. Raw claim.
5. Extracted candidate.
6. Normalized field or object.
7. Conflict or duplicate analysis.
8. Stable canonical identity.
9. Owner-pack assignment.
10. Validation.
11. Release.
12. Runtime or application projection.

## F.25 Provenance record fields

A provenance record should include:

- source ID;
- source type;
- authority;
- status;
- version;
- digest;
- locator;
- coordinate;
- raw claim;
- normalized claim;
- transformation;
- target stable ID;
- reviewer;
- confidence;
- conflict state;
- release;
- notes.

## F.26 Source status values

Useful source status values include:

- active;
- approved;
- canonical;
- proposed;
- historical;
- superseded;
- provenance-only;
- unavailable;
- conflicted;
- quarantined;
- withdrawn.

## F.27 Authority and confidence

Authority and confidence are separate.

An owner-approved statement may have high authority even when source detail remains incomplete.

A machine extraction may have high confidence that text was copied accurately but no authority to resolve its meaning.

## F.28 Source conflicts

A source conflict record should preserve:

- all claims;
- all sources;
- authority;
- date and version;
- scope;
- field or object affected;
- proposed interpretations;
- owner decision status;
- runtime impact;
- migration impact.

## F.29 Known source conflict: P9-06-008

An older P9-06 backlog artifact associates P9-06-008 with an initial logical schema migration.

The newer active roadmap and bootstrap associate P9-06-008 with backup, restore, and provider-exit ports.

Current execution follows the newer active roadmap and bootstrap.

The older record remains historical planning evidence.

## F.30 Known source staleness: current-state record

An older `AIOC_CURRENT_STATE.md` reports 8D-007 as active.

Newer completion packages, roadmap, bootstrap, and repository evidence show later progress.

The stale record must not control current execution.

## F.31 Source freshness rules

### Repository file

Refresh when:

- branch changes;
- commit changes;
- worktree changes;
- file changes;
- pull request merges.

### Owner record

Refresh at every A3 decision point.

### Released package

Verify digest and release status.

### Dynamic roadmap

Check version and last update.

### Historical archive

Use manifest, digest, and exact archive member.

### Web or provider information

Verify current state when material to the task.

## F.32 Exact locator formats

Preferred locators include:

```text
repo://owner/repository@commit/path
archive://source-id/member/path
file://registered-source-id
csv://source-id#row-key
json://source-id#/json/pointer
pdf://source-id#page=<n>
decision://decision-id@version
pack://pack-id@version/object-id
```

The exact implementation may use another governed URI syntax.

## F.33 Coverage mapping by Bible volume

### Volume I

Principal sources:

- Definition Document;
- owner decisions;
- governance;
- repository bootstrap;
- 8D-008 operating scope.

### Volume II

Principal sources:

- DB-004 Game Framework;
- Phase 8B;
- Phase 8C;
- 8D-007;
- domain validation packs.

### Volume III

Principal sources:

- 8E-006;
- setting source corpus;
- adventure acceptance packs;
- content-production standards.

### Volume IV

Principal sources:

- Phase 8A;
- canonical object program;
- 8E-008;
- 8E-009;
- pack and provenance schemas.

### Volume V

Principal sources:

- Stage A program;
- owner UI instructions and mockups;
- application workflow plans;
- DB-004 domain behavior;
- authoritative-session architecture.

### Volume VI

Principal sources:

- P9-01 through P9-06;
- application port PRs;
- security and recovery architecture;
- Stage A technical constraints.

### Volume VII

Principal sources:

- 8D-008A through 8D-008J;
- 8D-007J;
- repository and worktree standards;
- active bootstrap.

### Volume VIII

Principal sources:

- roadmap;
- bootstrap;
- repository commits;
- acceptance gates;
- WP-011;
- completion packages;
- owner release boundaries.

## F.34 Source-coverage limitation

This index represents the principal sources used to draft the Bible.

It is not a complete machine source registry.

A final canonical repository integration should produce:

- source registry export;
- evidence manifest;
- chapter-to-source matrix;
- exact digests;
- source availability report;
- unresolved conflict report.

## F.35 Source addition checklist

Before adding a source:

- assign stable source ID;
- record authority;
- record status;
- record version;
- compute digest;
- record locator;
- record scope;
- record rights;
- identify conflicts;
- identify supersession;
- update source groups;
- validate retrieval.

## F.36 Source removal checklist

A source should not be deleted merely because it is superseded.

Before withdrawal:

- identify dependent claims;
- preserve digest;
- preserve provenance;
- record replacement;
- record migration;
- update indexes;
- retain historical copy where policy requires.

## F.37 Source citation template

```text
Source ID:
Title:
Version:
Status:
Authority:
Locator:
Digest:
Exact coordinate:
Claim supported:
Limitations:
Supersedes:
Superseded by:
```

## F.38 Final provenance rule

No material claim should become harder to verify after normalization, implementation, migration, release, or editorial consolidation.

---

# Appendix G — Developer Checklists

## G.1 Purpose

Provide practical checklists for AI agents and human developers performing bounded Multiversal work.

These checklists supplement work-type profiles, schemas, quality gates, and repository instructions.

## G.2 New-session bootstrap checklist

- [ ] Confirm GitHub access to both canonical repositories.
- [ ] Read the active New Conversation Bootstrap.
- [ ] Read the Contributor Registry.
- [ ] Read the active Application Implementation Roadmap.
- [ ] Inspect current-state and handoff records.
- [ ] Inspect recent `Multiversal-app` commits.
- [ ] Inspect open pull requests.
- [ ] Inspect relevant CI.
- [ ] Resolve the latest merged P9-06 item.
- [ ] Resolve the exact next unfinished item.
- [ ] Prefer newer verified repository evidence over stale summaries.
- [ ] Record the current commit and source digests.
- [ ] Do not begin production, paid, or release actions.

## G.3 Work-order intake checklist

- [ ] Stable work-order ID exists.
- [ ] Work-order version exists.
- [ ] Objective is measurable.
- [ ] Registered work type is selected.
- [ ] Decision level is correct.
- [ ] Risk class is correct.
- [ ] Priority is source-grounded.
- [ ] Authority domains are listed.
- [ ] In-scope work is explicit.
- [ ] Out-of-scope work is explicit.
- [ ] Known affected files are listed.
- [ ] Known affected stable IDs are listed.
- [ ] Assumptions are explicit.
- [ ] Constraints are explicit.
- [ ] Primary executor is assigned.
- [ ] Required reviewers are assigned.
- [ ] Owner role is explicit.
- [ ] Dependencies are explicit.
- [ ] Acceptance criteria are measurable.
- [ ] Required records are listed.
- [ ] Required tests are listed.
- [ ] Rollback or recovery is defined.
- [ ] Output artifacts are listed.
- [ ] Handoff destination is defined.
- [ ] No A4 action is present.

## G.4 Context-loading checklist

- [ ] Governance core loaded.
- [ ] Owner records loaded when required.
- [ ] Work-type profile applied.
- [ ] Role profile applied.
- [ ] Authority-domain bindings applied.
- [ ] Exact target files resolved.
- [ ] Repository commit resolved.
- [ ] Source versions resolved.
- [ ] Source digests verified.
- [ ] Structured queries record fields and filters.
- [ ] Optional context cannot displace required context.
- [ ] Known conflicts are loaded.
- [ ] Missing required sources block execution.
- [ ] Context bundle fits approved budget.
- [ ] Required exact evidence remains exact.
- [ ] Context receipt is sealed.
- [ ] Bundle digest recorded.

## G.5 Repository preflight checklist

- [ ] Correct repository.
- [ ] Correct default branch.
- [ ] Correct work branch.
- [ ] Correct worktree.
- [ ] Correct base commit.
- [ ] Worktree is clean or all changes are enumerated.
- [ ] Allowed paths are known.
- [ ] Forbidden paths are known.
- [ ] Required tools are available.
- [ ] Tool versions match the work order.
- [ ] Environment is local or approved.
- [ ] No production credentials are present.
- [ ] No unrelated work is mixed into the branch.
- [ ] Current task packet and approvals remain valid.

## G.6 General implementation checklist

- [ ] Make the smallest coherent change.
- [ ] Preserve stable IDs.
- [ ] Preserve source provenance.
- [ ] Preserve negative evidence.
- [ ] Do not invent canon.
- [ ] Do not broaden scope silently.
- [ ] Use provider-neutral contracts.
- [ ] Keep external SDKs inside adapters.
- [ ] Add or update tests with the behavior.
- [ ] Add error and recovery behavior.
- [ ] Add loading, empty, forbidden, and stale states where applicable.
- [ ] Add documentation.
- [ ] Record implementation choices.
- [ ] Recalculate affected digests.
- [ ] Revalidate approval after material change.

## G.7 Schema checklist

- [ ] Schema has stable identity.
- [ ] Schema version is explicit.
- [ ] Required fields are correct.
- [ ] Optional fields are intentional.
- [ ] Conditional requirements are encoded.
- [ ] Unknown-field behavior is defined.
- [ ] Extension namespace behavior is defined.
- [ ] Stable-ID fields are typed.
- [ ] Relationship fields use IDs, not display names.
- [ ] Source and provenance fields are available.
- [ ] Lifecycle status is represented.
- [ ] Visibility is represented where needed.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Boundary-value fixtures exist.
- [ ] Migration path is defined.
- [ ] Cross-language generation or validation passes.

## G.8 Stable-ID checklist

- [ ] ID belongs to the correct namespace.
- [ ] ID format validates.
- [ ] ID is unique.
- [ ] ID is independent of display name.
- [ ] ID is independent of file path.
- [ ] ID is independent of provider ID.
- [ ] Owner pack is defined.
- [ ] Aliases are recorded.
- [ ] Supersession is recorded.
- [ ] Migration mapping is recorded.
- [ ] Export preserves the ID.
- [ ] No ID is recycled.

## G.9 Canonical content checklist

- [ ] Source ID exists.
- [ ] Source coordinate exists.
- [ ] Raw claim is preserved.
- [ ] Normalization is explicit.
- [ ] Missing information remains marked.
- [ ] Conflicts remain recorded.
- [ ] Duplicate analysis completed.
- [ ] Definition versus variant is correct.
- [ ] Owner pack is correct.
- [ ] Dependencies are correct.
- [ ] Mechanics reference shared contracts.
- [ ] Player-safe and GM-only information are separate.
- [ ] Provenance validates.
- [ ] Coverage status is updated.
- [ ] Promotion authority is valid.

## G.10 Pack-development checklist

- [ ] Pack ID is stable.
- [ ] Version is explicit.
- [ ] Manifest validates.
- [ ] Owner-pack assignments are unique.
- [ ] Dependencies resolve.
- [ ] Optional dependencies are explicit.
- [ ] Extensions use approved namespaces.
- [ ] Indexes validate.
- [ ] Source and provenance metadata are included.
- [ ] Media and localization indexes are included where applicable.
- [ ] Installation succeeds.
- [ ] Repeat installation is idempotent.
- [ ] Update succeeds.
- [ ] Migration succeeds.
- [ ] Blocked removal blocks correctly.
- [ ] Safe removal succeeds.
- [ ] Reinstallation succeeds.
- [ ] Zero unintended residue remains.
- [ ] Export includes the pack.
- [ ] Checksum matches.

## G.11 Character-system checklist

- [ ] Character identity is stable.
- [ ] Campaign scope is explicit.
- [ ] ownership and control are separate.
- [ ] Species and forms are references.
- [ ] Attributes and derived values are deterministic.
- [ ] Abilities and grants identify source.
- [ ] Resources are typed.
- [ ] Conditions preserve lifecycle.
- [ ] Inventory ownership is correct.
- [ ] Relationships are typed.
- [ ] Progression events are retained.
- [ ] Entitlement is validated separately from mechanics.
- [ ] Character validation distinguishes error classes.
- [ ] Save and reopen work.
- [ ] Migration preserves history.
- [ ] Export preserves IDs and source references.

## G.12 Rules-runtime checklist

- [ ] Action is versioned.
- [ ] Actor is explicit.
- [ ] Targets are explicit.
- [ ] Preconditions validate before cost unless the rule says otherwise.
- [ ] Costs are explicit.
- [ ] Check inputs are serializable.
- [ ] Random seed or roll is recorded.
- [ ] Modifier ordering is deterministic.
- [ ] Effects identify origin.
- [ ] Conditions identify source and duration.
- [ ] Resources cannot underflow without a governed rule.
- [ ] Failure behavior is explicit.
- [ ] No hidden partial mutation occurs.
- [ ] Accepted result creates Events.
- [ ] Replay reproduces the result.
- [ ] 8D-007J runs when applicable.

## G.13 Persistence checklist

- [ ] Transaction boundary is explicit.
- [ ] Aggregate ownership is clear.
- [ ] Expected-version behavior is defined.
- [ ] Idempotency is implemented.
- [ ] Duplicate key with different input rejects.
- [ ] Events append atomically.
- [ ] Projections update safely.
- [ ] Outbox writes atomically.
- [ ] Snapshot metadata is complete.
- [ ] Campaign or tenant scope is enforced.
- [ ] Provider-specific query types do not leak.
- [ ] Failure states identify commit status.
- [ ] Backup compatibility is considered.
- [ ] Export compatibility is considered.
- [ ] Contract tests pass.

## G.14 Migration checklist

- [ ] Migration ID is unique.
- [ ] Source version is explicit.
- [ ] Target version is explicit.
- [ ] Migration is deterministic.
- [ ] Clean install path passes.
- [ ] Upgrade path passes.
- [ ] Backfill preserves provenance.
- [ ] Missing derivable data is not guessed.
- [ ] Stable IDs are preserved or mapped.
- [ ] Event compatibility is handled.
- [ ] Snapshot compatibility is handled.
- [ ] Pack compatibility is handled.
- [ ] Backup exists.
- [ ] Restore proof exists.
- [ ] Rollback or forward repair exists.
- [ ] Counts reconcile.
- [ ] Repeated execution is safe or blocked.
- [ ] Receipt is generated.

## G.15 Identity checklist

- [ ] Internal subject ID is stable.
- [ ] Provider ID is only a mapping.
- [ ] Provider and environment are recorded.
- [ ] Session expiry is enforced.
- [ ] Revocation works.
- [ ] Account linking verifies both sides.
- [ ] Recovery preserves the internal subject.
- [ ] Service actors have narrow identities.
- [ ] Logs do not expose tokens.
- [ ] Export preserves identity mappings.
- [ ] Authorization is separate from authentication.

## G.16 Authorization checklist

- [ ] Default deny.
- [ ] Service-level checks.
- [ ] Database or storage isolation where supported.
- [ ] Campaign isolation.
- [ ] Resource relationship checked.
- [ ] Field-level visibility checked.
- [ ] Query inference tested.
- [ ] Search inference tested.
- [ ] Realtime subscription checked.
- [ ] Mutation checks at execution time.
- [ ] Revocation invalidates cache.
- [ ] Owner-only operations remain owner-gated.
- [ ] AI tools enforce the same authorization.
- [ ] Denied-case tests exist.

## G.17 Entitlement checklist

- [ ] Subject and content scope are explicit.
- [ ] Decision reason is structured.
- [ ] Policy version is recorded.
- [ ] Free tiers one and two behave correctly.
- [ ] Higher-tier grants do not bypass policy.
- [ ] Campaign grant is scoped.
- [ ] Sponsored-month behavior is correct.
- [ ] Expiry is predictable.
- [ ] Cancellation preserves history.
- [ ] Search does not reveal protected content.
- [ ] AI retrieval enforces entitlement.
- [ ] Offline snapshot is bounded.
- [ ] Export preserves entitlement metadata.
- [ ] Billing remains separate.

## G.18 Realtime checklist

- [ ] Transport is replaceable.
- [ ] Connection authenticates.
- [ ] Subscription authorizes.
- [ ] Session identity is stable.
- [ ] Participant role is explicit.
- [ ] Command ID is stable.
- [ ] Expected version is checked.
- [ ] Duplicate command is idempotent.
- [ ] Stale command is rejected or revalidated.
- [ ] Event sequence is monotonic.
- [ ] Outbox handles delivery.
- [ ] Hidden data is removed before publication.
- [ ] Client tracks last acknowledged sequence.
- [ ] Gap recovery works.
- [ ] Reconnect works.
- [ ] Multiple-device policy is defined.
- [ ] Contract tests pass.

## G.19 Live-session checklist

- [ ] Player and GM use distinct identities.
- [ ] Actor control is verified.
- [ ] Player proposal includes Action, target, cost, and expected result.
- [ ] Server recalculates or validates.
- [ ] GM sees complete permitted approval detail.
- [ ] GM may approve, deny, or modify.
- [ ] Original calculation is retained.
- [ ] Accepted result persists.
- [ ] Role-filtered Events broadcast.
- [ ] Disconnect before submit remains local draft.
- [ ] Disconnect after submit recovers command status.
- [ ] Disconnect after commit recovers Event.
- [ ] Checkpoint exists.
- [ ] Replay works.
- [ ] Hidden information does not leak.

## G.20 Backup checklist

- [ ] Backup scope is explicit.
- [ ] Backup ID is stable.
- [ ] Environment is explicit.
- [ ] Schema versions recorded.
- [ ] Pack versions recorded.
- [ ] Event ranges recorded.
- [ ] Media inventory recorded.
- [ ] Manifest generated.
- [ ] Checksums generated.
- [ ] Encryption applied where required.
- [ ] Access is least privileged.
- [ ] Verification passes.
- [ ] Receipt generated.
- [ ] Retention metadata exists.
- [ ] Restore drill scheduled or completed.

## G.21 Restore checklist

- [ ] Backup manifest parses.
- [ ] Checksums pass.
- [ ] Decryption succeeds.
- [ ] Target environment is approved.
- [ ] Compatibility plan passes.
- [ ] Restore is isolated.
- [ ] Required migrations apply.
- [ ] Derived indexes rebuild.
- [ ] Identity mappings preserve internal IDs.
- [ ] Campaign and Character state verify.
- [ ] Events and snapshots verify.
- [ ] Packs verify.
- [ ] Media verifies.
- [ ] Representative workflows pass.
- [ ] Restore receipt generated.
- [ ] Failure evidence retained.

## G.22 Provider-exit checklist

- [ ] Export contract version is explicit.
- [ ] Internal IDs preserved.
- [ ] Provider mappings included.
- [ ] Campaign and Character state included.
- [ ] Events included.
- [ ] Snapshots included.
- [ ] Entitlements included.
- [ ] Pack registry included.
- [ ] Media metadata included.
- [ ] Schemas included.
- [ ] Migration history included.
- [ ] Rights restrictions identified.
- [ ] Checksums generated.
- [ ] Import order documented.
- [ ] Replacement import tested.
- [ ] Completeness counts reconcile.
- [ ] Exit receipt generated.

## G.23 Frontend checklist

- [ ] Uses shared UI system.
- [ ] Uses real governed data or an explicitly governed adapter.
- [ ] Does not implement trusted permission logic only in the client.
- [ ] Does not include production secrets.
- [ ] Loading state exists.
- [ ] Empty state exists.
- [ ] Error state exists.
- [ ] Offline or reconnect state exists.
- [ ] Forbidden state exists.
- [ ] Stale state exists where applicable.
- [ ] Keyboard behavior works.
- [ ] Focus is predictable.
- [ ] Touch behavior works.
- [ ] Desktop layout works.
- [ ] Tablet layout works.
- [ ] Mobile layout works.
- [ ] Screen-reader labels exist.
- [ ] Noncolor status indicators exist.
- [ ] Tests exist.
- [ ] Reproducible preview exists.

## G.24 Universal-object checklist

- [ ] Browse works.
- [ ] Search works.
- [ ] Filters work.
- [ ] Exact stable-ID lookup works.
- [ ] Object inspector works.
- [ ] Provenance view works.
- [ ] Relationship traversal works.
- [ ] Version comparison works.
- [ ] Variant comparison works.
- [ ] Permission and entitlement filter results.
- [ ] Hidden result counts do not leak.
- [ ] Picker restricts valid object types.
- [ ] Selection passes stable ID to another workflow.
- [ ] Desktop and mobile behavior work.

## G.25 Accessibility checklist

- [ ] Semantic headings and landmarks.
- [ ] Every interactive control has correct role.
- [ ] Labels persist.
- [ ] Keyboard-only completion.
- [ ] Visible focus.
- [ ] Focus restored after dialog.
- [ ] Screen-reader names and states.
- [ ] Realtime announcements are prioritized.
- [ ] Color is not the only indicator.
- [ ] Contrast meets selected target.
- [ ] Text scales without loss.
- [ ] Touch targets are adequate.
- [ ] Drag has a nondrag alternative.
- [ ] Hover has focus or tap alternative.
- [ ] Reduced motion is respected.
- [ ] Timers provide governed accommodation.
- [ ] Error summary and field errors work.
- [ ] Maps have text alternatives.
- [ ] Graphs have list or table alternatives.
- [ ] Automated checks pass.
- [ ] Manual review evidence exists.

## G.26 Security checklist

- [ ] Threat impact reviewed.
- [ ] Secrets absent from code and logs.
- [ ] Least-privileged credentials.
- [ ] Default deny.
- [ ] Input validation.
- [ ] Parameterized database access.
- [ ] Upload limits and type validation.
- [ ] Pack archive traversal prevented.
- [ ] Rate limits applied.
- [ ] Auth callbacks validate.
- [ ] Realtime subscriptions authorize.
- [ ] AI prompt injection considered.
- [ ] AI tools use service authorization.
- [ ] Dependency scan passes.
- [ ] License review passes.
- [ ] Backup and export access are restricted.
- [ ] Security events exist.
- [ ] Incident path exists.
- [ ] Independent security review completed when required.

## G.27 Privacy checklist

- [ ] Data inventory updated.
- [ ] Data minimization applied.
- [ ] Private notes remain private.
- [ ] GM-only content remains protected.
- [ ] Logs are redacted.
- [ ] AI context is minimized.
- [ ] Provider data handling is documented.
- [ ] Retention is defined for the environment.
- [ ] Export scope is correct.
- [ ] Deletion behavior is defined.
- [ ] Backups are included in privacy analysis.
- [ ] Lower environments use synthetic data.
- [ ] Public privacy claims match implementation.

## G.28 AI-feature checklist

- [ ] User intent is explicit.
- [ ] AI role is clear.
- [ ] Subject and Campaign context are bound.
- [ ] Permissions are enforced.
- [ ] Entitlements are enforced.
- [ ] Sources are cited.
- [ ] Uncertainty is disclosed.
- [ ] Output is visibly proposed.
- [ ] Mutation requires explicit approval.
- [ ] Hidden data is excluded.
- [ ] Prompt injection is considered.
- [ ] Tool permissions are narrow.
- [ ] Cost limits exist.
- [ ] Non-AI fallback exists.
- [ ] Provider failure is safe.
- [ ] AI cannot promote canon.

## G.29 Test checklist

- [ ] Static checks.
- [ ] Unit tests.
- [ ] Invalid-input tests.
- [ ] Permission-denied tests.
- [ ] Entitlement-denied tests.
- [ ] Contract tests.
- [ ] Integration tests.
- [ ] Migration tests.
- [ ] Replay tests.
- [ ] UI interaction tests.
- [ ] Accessibility tests.
- [ ] Reconnect tests.
- [ ] Duplicate-command tests.
- [ ] Backup and restore tests.
- [ ] Provider-exit tests.
- [ ] Performance tests where required.
- [ ] 8D-007J where required.
- [ ] Failed evidence retained.
- [ ] Full required suite rerun after repair.

## G.30 Pull-request checklist

- [ ] Work-order ID in title or description.
- [ ] Objective stated.
- [ ] Scope stated.
- [ ] Out-of-scope stated.
- [ ] Changed files listed.
- [ ] Changed stable IDs listed.
- [ ] Tests and commands listed.
- [ ] CI status linked.
- [ ] Migration impact stated.
- [ ] Security and privacy impact stated.
- [ ] Accessibility impact stated.
- [ ] Screenshots or interaction evidence included when applicable.
- [ ] Rollback stated.
- [ ] Known limitations stated.
- [ ] Required reviewers assigned.
- [ ] Approval boundary stated.
- [ ] No unsupported completion claim.

## G.31 Merge checklist

- [ ] Required gates pass.
- [ ] Context remains current.
- [ ] Approval remains valid.
- [ ] Review is independent.
- [ ] Blocking findings resolved.
- [ ] Branch is mergeable.
- [ ] Required merge strategy selected.
- [ ] Final artifact digest recorded.
- [ ] Final CI is not stale.
- [ ] Merge completes.
- [ ] Target-branch commit verified.
- [ ] Postmerge validation passes.
- [ ] Current-state record updated.
- [ ] Handoff created.
- [ ] Worktree cleanup recorded.

## G.32 Release-preparation checklist

- [ ] Exact candidate frozen.
- [ ] Commit recorded.
- [ ] Build reproducible.
- [ ] Dependency lock recorded.
- [ ] Schemas recorded.
- [ ] Migrations recorded.
- [ ] Pack versions recorded.
- [ ] Manifest generated.
- [ ] Checksums generated.
- [ ] Tests pass.
- [ ] Security review passes.
- [ ] Privacy review passes.
- [ ] Accessibility evidence exists.
- [ ] Performance and cost evidence exists.
- [ ] Backup verified.
- [ ] Restore passes.
- [ ] Rollback exists.
- [ ] Known risks recorded.
- [ ] Owner approval requested when required.
- [ ] Release not executed before approval.

## G.33 Internal-alpha developer checklist

- [ ] Core Player and GM loop complete.
- [ ] Two distinct devices or clients tested.
- [ ] Hidden information safe.
- [ ] Identity and Campaign isolation tested.
- [ ] Entitlement paths tested.
- [ ] Save and reload tested.
- [ ] Reconnect tested.
- [ ] Duplicate and stale commands tested.
- [ ] Backup exists.
- [ ] Restore drill passes.
- [ ] Provider-exit artifact exists.
- [ ] Tester onboarding exists.
- [ ] Known issues exist.
- [ ] Issue intake exists.
- [ ] Cost understood.
- [ ] Security and privacy review complete.
- [ ] Accessibility evidence complete for primary workflows.
- [ ] Exact owner decision obtained.

## G.34 Borrowed-Mac checklist

- [ ] WP-011 package integrity verified.
- [ ] Exact commit available offline.
- [ ] Expected branch verified.
- [ ] Xcode installer present.
- [ ] Xcode checksum verified.
- [ ] Required free space available.
- [ ] Administrator-password holder available.
- [ ] External evidence destination writable.
- [ ] Disposable workspace configured.
- [ ] No production credentials planned.
- [ ] One-pass prompt ready.
- [ ] Baseline tests pass.
- [ ] iPhone simulator available.
- [ ] iPad simulator available.
- [ ] Lifecycle tests performed.
- [ ] Storage tests performed.
- [ ] Accessibility smoke review performed.
- [ ] PASS or HARD_GATE classified.
- [ ] WP-012 handoff generated.
- [ ] Branch, patch, bundle, logs, and screenshots copied out.
- [ ] Destination checksums verified.
- [ ] Cleanup plan shown to owner.
- [ ] Cleanup approved.
- [ ] Session-created assets removed.
- [ ] Sign-outs confirmed.

## G.35 Handoff checklist

- [ ] Work order and version.
- [ ] Current status.
- [ ] Current branch and commit.
- [ ] Changed files.
- [ ] Changed stable IDs.
- [ ] Tests and results.
- [ ] Failed evidence.
- [ ] Reviews.
- [ ] Approvals.
- [ ] Decisions.
- [ ] Blockers.
- [ ] Open owner decisions.
- [ ] Evidence locations.
- [ ] Context receipt.
- [ ] Next executable action.
- [ ] Cleanup state.
- [ ] Continuity digest.
- [ ] Successor acceptance.

## G.36 Completion-report checklist

- [ ] Exact backlog item.
- [ ] Exact scope completed.
- [ ] Files or capabilities added.
- [ ] Tests.
- [ ] CI.
- [ ] Pull request.
- [ ] Merge or squash commit.
- [ ] Restrictions preserved.
- [ ] Known limitations.
- [ ] Exact next step.
- [ ] Artifact link.
- [ ] No unsupported claim.

---

# Appendix H — Validation and Release Checklists

## H.1 Purpose

Provide stage-specific validation and release checklists for artifacts, content packs, data migrations, service ports, application vertical slices, internal alpha, closed alpha, beta, and production readiness.

## H.2 Validation principle

Validation proves only the defined scope.

A PASS for:

- a schema;
- a service port;
- a pack;
- a simulator spike;
- an internal alpha;

does not prove the entire platform is complete or publicly ready.

## H.3 Artifact-integrity checklist

- [ ] Artifact exists.
- [ ] Artifact type is correct.
- [ ] Filename matches manifest.
- [ ] Size matches manifest.
- [ ] SHA-256 matches.
- [ ] Version is explicit.
- [ ] Source commit is recorded.
- [ ] Generator is recorded.
- [ ] Environment is recorded.
- [ ] Manifest parses.
- [ ] Required files are present.
- [ ] No unexpected files are present.
- [ ] No secrets are present.
- [ ] Artifact opens or installs.
- [ ] Verification receipt generated.

## H.4 Document-release checklist

- [ ] Document ID.
- [ ] Version.
- [ ] Status.
- [ ] Owner.
- [ ] Approving authority.
- [ ] Effective date.
- [ ] Scope.
- [ ] Normative or informative status.
- [ ] Controlling sources.
- [ ] Superseded documents.
- [ ] Required sections present.
- [ ] Cross-references valid.
- [ ] Claims have evidence.
- [ ] Limitations stated.
- [ ] Change log updated.
- [ ] Checksum recorded.
- [ ] Release location recorded.

## H.5 Source and provenance checklist

- [ ] Source registered.
- [ ] Source digest verified.
- [ ] Source status correct.
- [ ] Authority correct.
- [ ] Exact coordinate recorded.
- [ ] Raw claim preserved.
- [ ] Normalized claim recorded.
- [ ] Transformation recorded.
- [ ] Target stable ID recorded.
- [ ] Conflict status recorded.
- [ ] Reviewer recorded.
- [ ] Release recorded.
- [ ] Coverage updated.
- [ ] No source claim silently discarded.

## H.6 Canonical object checklist

- [ ] Object ID validates.
- [ ] Object family correct.
- [ ] Owner pack unique.
- [ ] Display name present.
- [ ] Aliases recorded.
- [ ] Source and provenance present.
- [ ] Lifecycle status valid.
- [ ] Capabilities valid.
- [ ] Relationships valid.
- [ ] Visibility valid.
- [ ] Extension namespace valid.
- [ ] Required fields present.
- [ ] No duplicate stable ID.
- [ ] Runtime projection validates.
- [ ] Migration path exists when replacing a prior object.

## H.7 Pack validation checklist

- [ ] Pack ID valid.
- [ ] Version valid.
- [ ] `.pack` extension correct.
- [ ] Manifest valid.
- [ ] Checksums valid.
- [ ] Schemas valid.
- [ ] Indexes valid.
- [ ] Owner-pack map valid.
- [ ] Required dependencies resolve.
- [ ] Optional dependencies behave correctly.
- [ ] Extension targets exist.
- [ ] Source metadata present.
- [ ] Provenance present.
- [ ] Media rights recorded.
- [ ] Localization indexes valid.
- [ ] Install succeeds.
- [ ] Repeat install is idempotent.
- [ ] Update succeeds.
- [ ] Migration succeeds.
- [ ] Blocked removal blocks.
- [ ] Safe removal succeeds.
- [ ] Reinstall succeeds.
- [ ] Export succeeds.
- [ ] Zero unintended residue.

## H.8 Schema-release checklist

- [ ] Schema ID.
- [ ] Version.
- [ ] Compatibility policy.
- [ ] Valid fixtures.
- [ ] Invalid fixtures.
- [ ] Boundary fixtures.
- [ ] Conditional fields.
- [ ] Unknown-field behavior.
- [ ] Stable-ID behavior.
- [ ] Extension behavior.
- [ ] Generated types.
- [ ] Cross-language validation.
- [ ] Migration.
- [ ] Deprecation.
- [ ] Documentation.
- [ ] Contract tests.
- [ ] Release checksum.

## H.9 Migration-release checklist

- [ ] Migration ID.
- [ ] Source version.
- [ ] Target version.
- [ ] Scope.
- [ ] Affected count.
- [ ] Backup verified.
- [ ] Restore verified.
- [ ] Dry run.
- [ ] Deterministic transformation.
- [ ] Stable-ID mapping.
- [ ] Provenance preservation.
- [ ] Event compatibility.
- [ ] Snapshot compatibility.
- [ ] Pack compatibility.
- [ ] Permission compatibility.
- [ ] Entitlement compatibility.
- [ ] Count reconciliation.
- [ ] Failure behavior.
- [ ] Restart behavior.
- [ ] Rollback or forward repair.
- [ ] Receipt.
- [ ] Owner gate for destructive behavior.

## H.10 Service-port validation checklist

- [ ] Port purpose documented.
- [ ] Inputs defined.
- [ ] Outputs defined.
- [ ] Stable errors defined.
- [ ] Idempotency defined.
- [ ] Transaction behavior defined.
- [ ] Security defined.
- [ ] Observability defined.
- [ ] Versioning defined.
- [ ] Local adapter exists.
- [ ] Contract fixtures exist.
- [ ] Shared contract tests pass.
- [ ] Provider SDK does not leak.
- [ ] Provider IDs do not replace internal IDs.
- [ ] Export or exit behavior defined.
- [ ] Dedicated CI passes.

## H.11 Identity validation checklist

- [ ] Provider login maps to internal subject.
- [ ] Same subject survives provider change.
- [ ] Display-name change preserves subject.
- [ ] Account linking works.
- [ ] Conflict detection works.
- [ ] Recovery preserves subject.
- [ ] Revocation works.
- [ ] Session expiry works.
- [ ] Service identities are narrow.
- [ ] Export preserves mappings.
- [ ] Logs are redacted.
- [ ] Denied cases pass.

## H.12 Authorization validation checklist

- [ ] Unknown subject denied.
- [ ] Wrong Campaign denied.
- [ ] Wrong Character denied.
- [ ] Wrong role denied.
- [ ] Revoked role denied.
- [ ] Hidden field excluded.
- [ ] Query count does not leak.
- [ ] Search does not leak.
- [ ] Realtime subscription denied.
- [ ] Mutation rechecks permission.
- [ ] Offline cache expires.
- [ ] AI retrieval respects scope.
- [ ] Owner-only operation denied.
- [ ] Audit receipt created.

## H.13 Entitlement validation checklist

- [ ] Free access succeeds.
- [ ] Tier one succeeds.
- [ ] Tier two succeeds.
- [ ] Higher tier denies without valid access.
- [ ] Higher-tier grant remains evaluated.
- [ ] Campaign grant works only in scope.
- [ ] Sponsored month works.
- [ ] Sponsored month expires.
- [ ] Cancellation preserves history.
- [ ] Search hides protected details.
- [ ] AI hides protected details.
- [ ] Offline snapshot expires correctly.
- [ ] Export preserves state.
- [ ] Billing remains unnecessary for contract validation.

## H.14 Persistence validation checklist

- [ ] Transaction commits all state.
- [ ] Transaction rollback leaves no partial mutation.
- [ ] Optimistic conflict detected.
- [ ] Duplicate operation returns prior result.
- [ ] Different input with same key rejects.
- [ ] Event sequence is correct.
- [ ] Projection is current.
- [ ] Outbox is durable.
- [ ] Snapshot checksum validates.
- [ ] Campaign isolation holds.
- [ ] Provider outage returns stable error.
- [ ] Adapter contract passes.
- [ ] Reset is safe.
- [ ] Import and export preserve IDs.

## H.15 Authoritative-session validation checklist

- [ ] Distinct Player and GM identities.
- [ ] Correct role projections.
- [ ] Proposal accepted.
- [ ] Proposal denied.
- [ ] Proposal modified.
- [ ] Original calculation retained.
- [ ] Duplicate command safe.
- [ ] Stale command safe.
- [ ] Event order correct.
- [ ] Hidden data excluded.
- [ ] Disconnect before submit safe.
- [ ] Disconnect after submit recovers.
- [ ] Disconnect after commit recovers.
- [ ] Event gap recovers.
- [ ] Checkpoint validates.
- [ ] Restore appends recovery event.
- [ ] Two-device acceptance passes.

## H.16 Backup validation checklist

- [ ] Full required scope included.
- [ ] Manifest complete.
- [ ] Checksums pass.
- [ ] Encryption verified.
- [ ] Schema versions recorded.
- [ ] Pack versions recorded.
- [ ] Event ranges continuous.
- [ ] Media inventory complete.
- [ ] Identity mappings included.
- [ ] Entitlements included.
- [ ] Audit included where policy permits.
- [ ] Access is restricted.
- [ ] Retention recorded.
- [ ] Restore drill passes.

## H.17 Restore validation checklist

- [ ] Backup verified before restore.
- [ ] Compatibility plan passes.
- [ ] Isolated target.
- [ ] Migrations apply.
- [ ] Stable IDs preserved.
- [ ] Accounts resolve.
- [ ] Campaigns resolve.
- [ ] Characters resolve.
- [ ] Ownership resolves.
- [ ] Events resolve.
- [ ] Snapshots resolve.
- [ ] Packs resolve.
- [ ] Media resolves.
- [ ] Search rebuilds.
- [ ] Core workflow passes.
- [ ] Receipt and drill report complete.

## H.18 Provider-exit validation checklist

- [ ] Portable formats used.
- [ ] Export contract versioned.
- [ ] Internal IDs preserved.
- [ ] Provider mappings included.
- [ ] Data counts reconcile.
- [ ] Relationship counts reconcile.
- [ ] Event ranges reconcile.
- [ ] Pack versions reconcile.
- [ ] Media inventory reconciles.
- [ ] Schemas included.
- [ ] Migration guidance included.
- [ ] Rights restrictions included.
- [ ] Import into replacement succeeds.
- [ ] Core workflow succeeds after import.
- [ ] Exit gaps documented.

## H.19 Universal-object vertical-slice checklist

- [ ] Shell route exists.
- [ ] Real governed data loads.
- [ ] Browse works.
- [ ] Search works.
- [ ] Filters work.
- [ ] Object opens.
- [ ] Provenance opens.
- [ ] Relationships open.
- [ ] Picker works.
- [ ] Stable ID passes to another workflow.
- [ ] Permissions enforced in service.
- [ ] Entitlement enforced.
- [ ] Loading, empty, error, forbidden, and stale states exist.
- [ ] Desktop works.
- [ ] Mobile works.
- [ ] Keyboard works.
- [ ] Screen reader works.
- [ ] Tests pass.
- [ ] Preview reproducible.
- [ ] Owner review recorded.

## H.20 Character vertical-slice checklist

- [ ] Identity entry.
- [ ] Campaign selection.
- [ ] Character draft.
- [ ] Species or form selection.
- [ ] Ability selection.
- [ ] Tier entitlement validation.
- [ ] Equipment selection.
- [ ] Derived values.
- [ ] Validation.
- [ ] Save.
- [ ] Reopen.
- [ ] Submit or approve where required.
- [ ] Advance.
- [ ] Use in scene.
- [ ] History preserved.
- [ ] Mobile and desktop.
- [ ] Accessibility.
- [ ] Tests.

## H.21 Campaign-and-scene checklist

- [ ] Campaign creates.
- [ ] Rules profile selects.
- [ ] Packs bind.
- [ ] Player invites.
- [ ] Character associates.
- [ ] Scene creates.
- [ ] Location selects.
- [ ] Environment selects.
- [ ] Creatures or NPCs place.
- [ ] Hidden information configures.
- [ ] Objectives and clues configure.
- [ ] Map or theater-of-mind works.
- [ ] Player preview works.
- [ ] Validation passes.
- [ ] Save and reopen.
- [ ] Session launches.
- [ ] Tests pass.

## H.22 Live-action loop checklist

- [ ] Player sees available Actions.
- [ ] Player selects target.
- [ ] Costs display.
- [ ] Proposal preview displays.
- [ ] Proposal submits.
- [ ] Service validates.
- [ ] GM notification appears.
- [ ] GM can inspect rule.
- [ ] GM sees Player, target, roll, modifiers, result, Effects, warnings.
- [ ] GM approves.
- [ ] GM denies.
- [ ] GM modifies.
- [ ] Result persists.
- [ ] Player receives permitted result.
- [ ] Logs remain secondary.
- [ ] Reconnect preserves status.
- [ ] Tests pass.

## H.23 Combat validation checklist

- [ ] Encounter starts.
- [ ] Roster correct.
- [ ] Timing or initiative correct.
- [ ] Movement works.
- [ ] Targeting works.
- [ ] Actions work.
- [ ] Costs apply.
- [ ] Damage applies.
- [ ] Conditions apply.
- [ ] Resources update.
- [ ] Reactions work.
- [ ] NPC actions use governed loop.
- [ ] Hidden actors remain hidden.
- [ ] Objectives and environments apply.
- [ ] Defeat and end work.
- [ ] Replay works.
- [ ] Reconnect works.
- [ ] Keyboard and touch work.
- [ ] Performance acceptable.
- [ ] 8D-007J passes where affected.

## H.24 Inventory and Asset checklist

- [ ] Item acquired.
- [ ] Ownership recorded.
- [ ] Custody recorded.
- [ ] Equip works.
- [ ] Unequip works.
- [ ] Transfer works.
- [ ] Shared Asset works.
- [ ] Borrowing works.
- [ ] Container rules work.
- [ ] Stack split and merge work.
- [ ] Crafting works.
- [ ] Repair works.
- [ ] Upgrade works.
- [ ] Salvage works.
- [ ] Vehicle crew permissions work.
- [ ] No duplication.
- [ ] No loss.
- [ ] Save and reload.
- [ ] History preserved.

## H.25 Investigation and social checklist

- [ ] Investigation creates.
- [ ] Clue discovers.
- [ ] Evidence links.
- [ ] Hypothesis remains noncanonical.
- [ ] GM truth remains hidden.
- [ ] Player-safe reveal works.
- [ ] Nonlinear leads work.
- [ ] Timeline works.
- [ ] Relationship view works.
- [ ] Faction standing works.
- [ ] Promise or debt persists.
- [ ] Social Action proposal works.
- [ ] GM result modifies.
- [ ] Consequence persists.
- [ ] Graph has list alternative.
- [ ] Mobile and accessibility pass.

## H.26 World Builder checklist

- [ ] Definition creates.
- [ ] Duplicate search runs.
- [ ] Stable ID assigns.
- [ ] Owner pack assigns.
- [ ] Provenance attaches.
- [ ] Relationships create.
- [ ] Hierarchy and graph render.
- [ ] Location and Environment link.
- [ ] Faction and culture separate from live state.
- [ ] Timeline supports uncertainty.
- [ ] Adventure structure validates.
- [ ] Runtime preview works.
- [ ] Player-safe preview works.
- [ ] Submission works.
- [ ] Review works.
- [ ] Pack assembly works.
- [ ] Promotion remains authority-gated.

## H.27 Search and help checklist

- [ ] Exact ID search.
- [ ] Name search.
- [ ] Alias search.
- [ ] Filter.
- [ ] Match explanation.
- [ ] Permission-safe count.
- [ ] Entitlement-safe result.
- [ ] Source view.
- [ ] Version comparison.
- [ ] Variant comparison.
- [ ] Relationship traversal.
- [ ] Contextual help.
- [ ] Glossary.
- [ ] Error help.
- [ ] Offline index.
- [ ] AI answer cites source.
- [ ] AI uncertainty visible.
- [ ] Keyboard and screen reader pass.

## H.28 Accessibility release checklist

- [ ] Standards target defined.
- [ ] Automated audit passes.
- [ ] Keyboard audit passes.
- [ ] Screen-reader audit passes.
- [ ] Zoom and text scale pass.
- [ ] Contrast pass.
- [ ] Reduced motion pass.
- [ ] Touch pass.
- [ ] Orientation pass.
- [ ] Map alternatives pass.
- [ ] Graph alternatives pass.
- [ ] Error and recovery pass.
- [ ] Mobile primary workflows pass.
- [ ] Unresolved defects recorded.
- [ ] Public claim matches evidence.
- [ ] Accessibility contact or support path exists for public release.

## H.29 Security release checklist

- [ ] Threat model current.
- [ ] Authentication secure.
- [ ] Authorization review complete.
- [ ] Campaign isolation tested.
- [ ] Hidden information tested.
- [ ] Secret scan passes.
- [ ] Dependency scan passes.
- [ ] License review passes.
- [ ] Upload and archive security pass.
- [ ] Rate limits pass.
- [ ] AI security passes.
- [ ] Logging redaction passes.
- [ ] Backup access reviewed.
- [ ] Export access reviewed.
- [ ] Incident plan tested.
- [ ] Vulnerability intake exists.
- [ ] Residual risk owner-approved.

## H.30 Privacy release checklist

- [ ] Data inventory current.
- [ ] Privacy notice matches implementation.
- [ ] AI provider disclosure accurate.
- [ ] Analytics disclosure accurate.
- [ ] Billing provider disclosure accurate.
- [ ] Retention defined.
- [ ] Deletion defined.
- [ ] Export defined.
- [ ] Account closure defined.
- [ ] Backup retention explained.
- [ ] User-rights process exists.
- [ ] Minor-use policy exists where applicable.
- [ ] Lower environments exclude production data.
- [ ] Legal review completed where required.

## H.31 Performance and cost checklist

- [ ] Core workflow budgets defined.
- [ ] Actual corpus tested.
- [ ] Large Character tested.
- [ ] Large inventory tested.
- [ ] Complex scene tested.
- [ ] Multiple participants tested.
- [ ] Search tested.
- [ ] Reconnect tested.
- [ ] Backup duration measured.
- [ ] Restore duration measured.
- [ ] Database saturation measured.
- [ ] Realtime lag measured.
- [ ] AI use measured.
- [ ] Storage growth measured.
- [ ] Estimated monthly cost recorded.
- [ ] Target envelope respected.
- [ ] Owner review obtained above threshold.
- [ ] No automatic paid upgrade.

## H.32 Internal-alpha release checklist

- [ ] AG-01 complete.
- [ ] Required provider-neutral boundaries complete.
- [ ] Data foundation complete for alpha scope.
- [ ] Identity and entitlement behavior complete.
- [ ] Authoritative Session behavior complete.
- [ ] Backup and restore pass.
- [ ] Provider-exit artifact verified.
- [ ] Two-device suite passes.
- [ ] Core Player and GM loop passes.
- [ ] At least one combat workflow passes.
- [ ] At least one noncombat workflow passes.
- [ ] Hidden information passes.
- [ ] Accessibility evidence passes.
- [ ] Performance acceptable.
- [ ] Cost understood.
- [ ] Tester documentation complete.
- [ ] Known issues complete.
- [ ] Rollback complete.
- [ ] Owner approval exact and current.

## H.33 Closed-alpha release checklist

- [ ] Internal-alpha disposition complete.
- [ ] Invited tester list approved.
- [ ] Multiple Campaigns tested.
- [ ] Multiple GMs tested.
- [ ] Migration preserves state.
- [ ] Account recovery tested.
- [ ] Support intake ready.
- [ ] Privacy acknowledgement ready.
- [ ] Security review current.
- [ ] Accessibility testing expanded.
- [ ] Device matrix expanded.
- [ ] Reliability measured.
- [ ] Cost measured.
- [ ] Blocking defects zero.
- [ ] Owner approval exact and current.

## H.34 Beta release checklist

- [ ] Closed-alpha exit complete.
- [ ] Cohort and registration model approved.
- [ ] Public or private beta classification explicit.
- [ ] Data-reset policy disclosed.
- [ ] Security and privacy programs ready.
- [ ] Moderation ready if public UGC exists.
- [ ] Support capacity ready.
- [ ] Performance and capacity understood.
- [ ] Provider quotas understood.
- [ ] Cost forecast approved.
- [ ] Accessibility audit and remediation complete for claims.
- [ ] Release and rollback proven.
- [ ] Owner approval exact and current.

## H.35 Commercial readiness checklist

- [ ] Commercial model approved.
- [ ] Pricing approved.
- [ ] Plans approved.
- [ ] Billing provider approved.
- [ ] Production credentials approved.
- [ ] Subscription lifecycle tested.
- [ ] Cancellation tested.
- [ ] Refund and dispute process defined.
- [ ] Taxes reviewed.
- [ ] Accounting reviewed.
- [ ] Terms approved.
- [ ] Privacy policy approved.
- [ ] Content rights verified.
- [ ] Support ready.
- [ ] Provider exit covers billing and entitlements.
- [ ] Owner approval exact and current.

## H.36 Production-release checklist

- [ ] Product readiness complete.
- [ ] Content readiness complete.
- [ ] Security complete.
- [ ] Privacy complete.
- [ ] Accessibility evidence supports claims.
- [ ] Reliability and capacity complete.
- [ ] Backup and disaster recovery complete.
- [ ] Provider-exit rehearsal complete.
- [ ] Support complete.
- [ ] Legal and commercial complete.
- [ ] Platform packaging complete.
- [ ] Candidate frozen.
- [ ] Manifest and checksums complete.
- [ ] Migration complete.
- [ ] Rollback complete.
- [ ] Monitoring complete.
- [ ] Launch stop conditions complete.
- [ ] Owner release approval exact and current.
- [ ] Deployment receipt generated.
- [ ] Postlaunch verification passes.

## H.37 Claim-validation checklist

Before publishing a claim, ask:

- [ ] Is the claim about planning, implementation, validation, release, or production?
- [ ] Which exact source supports it?
- [ ] Is the source current?
- [ ] Does repository evidence support it?
- [ ] Does a gate support it?
- [ ] Is owner approval required?
- [ ] Are limitations stated?
- [ ] Does the wording exceed the evidence?
- [ ] Could a reader mistake a port, prototype, or plan for the complete product?
- [ ] Could a reader mistake internal alpha for public availability?

## H.38 Final validation rule

A release may be delayed by missing evidence.

It must never be accelerated by redefining incomplete work as complete.

---

# Appendix I — AI Prompt and Work-Order Templates

## I.1 Purpose

Provide reusable templates for AI startup, work-order creation, context loading, repository execution, review, testing, migration, owner decisions, handoff, recovery, and completion reporting.

These templates do not grant authority.

They must be populated from current governing sources and exact repository evidence.

## I.2 Template-use rules

Before using a template:

- verify the current bootstrap;
- verify the current roadmap;
- verify contributor authority;
- verify repository state;
- replace every placeholder;
- remove inapplicable sections only when allowed;
- bind exact artifacts and digests;
- preserve owner-only gates;
- preserve limitations;
- retain resulting records.

## I.3 New-conversation recovery prompt

```text
You are continuing the Multiversal project owned by John Brandon Turner.

Do not restart the project or treat earlier planning as disposable.

Mandatory recovery:
1. Verify access to:
   - cybalicistjt-stack/multiversal-aioc
   - cybalicistjt-stack/Multiversal-app
2. Read:
   - governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md
   - governance/access/AIOC_CONTRIBUTOR_REGISTRY.json
   - governance/application-planning/APPLICATION_IMPLEMENTATION_ROADMAP.md
   - required current-state and handoff records
3. Inspect recent commits, open PRs, active branches, and CI.
4. Identify the latest merged P9-06 item.
5. Resume the exact next unfinished item from newer verified repository evidence.
6. Treat stale summaries as supporting context, not current truth.
7. Continue through ordinary implementation and CI failures automatically.
8. Stop only for a genuine owner-only gate, prohibited action, spending, production credentials, deployment, public release, or irreversible provider commitment.
9. Report exact files, tests, PR, merge commit, restrictions, and next task.

Current owner: John Brandon Turner.
Do not infer approval from silence or tool access.
```

## I.4 “Continue” execution prompt

```text
Continue the active Multiversal work.

Interpret “Continue” as:
- verify current repository or artifact state;
- execute the next dependency-ordered unfinished operation now;
- use the current work order and exact sources;
- repair ordinary failures automatically;
- run required validation;
- preserve evidence and provenance;
- stop only at a true owner-only or prohibited gate;
- report the exact completed item and exact next step.

Do not return only a plan.
Do not claim completion without evidence.
```

## I.5 Lead Orchestrator startup template

```text
ROLE: Lead Orchestrator
PROJECT: Multiversal
OWNER: John Brandon Turner

MISSION
Convert owner-approved goals into bounded executable work while preserving authority, source truth, dependencies, review independence, evidence, and continuity.

REQUIRED STARTUP
- load governance core;
- verify active roadmap;
- verify repository state;
- identify active work order;
- identify affected authority domains;
- activate required roles;
- create or verify task packet;
- ensure Definition of Ready;
- route owner-only decisions;
- preserve next executable action.

MAY
- decompose approved work;
- sequence dependencies;
- assign qualified roles;
- choose ordinary reversible implementation options;
- route review;
- repair workflow failures;
- prepare owner decision packets.

MAY NOT
- approve owner-reserved decisions;
- overrule a valid specialist stop;
- claim independent review of own work;
- alter canon;
- authorize spending, production, or release;
- conceal failure.

OUTPUTS
- work-order state;
- role assignments;
- context receipt;
- gate route;
- blocker record;
- owner decision packet where required;
- closure handoff.
```

## I.6 Role startup template

```text
ROLE ID:
ROLE NAME:
AGENT INSTANCE:
WORK ORDER:
WORK TYPE:
DECISION LEVEL:
RISK CLASS:
AUTHORITY DOMAINS:

MISSION:
[Exact role mission]

REQUIRED INPUTS:
- work order and version;
- context receipt and digest;
- target files and IDs;
- acceptance criteria;
- required tests;
- approval references;
- repository and environment state.

PERMITTED ACTIONS:
[List]

PROHIBITED ACTIONS:
[List]

MANDATORY REVIEWS:
[List]

STOP CONDITIONS:
[List]

REQUIRED OUTPUTS:
[List]

HANDOFF DESTINATION:
[Role or record]

ACKNOWLEDGEMENT:
I accept this bounded role and will not infer broader authority.
```

## I.7 Work-order template

```text
WORK ORDER ID:
VERSION:
TITLE:
STATUS:
CREATED BY:
CREATED AT:

OWNER:
PROGRAM:
BACKLOG ITEM:
REGISTERED WORK TYPE:
DECISION LEVEL:
RISK CLASS:
PRIORITY:

OBJECTIVE:
[Testable objective]

SUCCESS OUTCOME:
[Observable result]

AUTHORITY DOMAINS:
- [ ]

TARGET REPOSITORY OR ARTIFACT:
TARGET BRANCH:
TARGET ENVIRONMENT:
BASE COMMIT OR VERSION:

IN SCOPE:
- [ ]

OUT OF SCOPE:
- [ ]

AFFECTED FILES:
- [ ]

AFFECTED STABLE IDS:
- [ ]

ASSUMPTIONS:
- [ ]

CONSTRAINTS:
- no production credentials;
- no paid provider;
- no public release;
- [additional]

PRIMARY EXECUTOR:
MATERIAL AUTHORS:
INDEPENDENT REVIEWERS:
APPROVERS:
SUPPORT ROLES:
OWNER ROLE:

DEPENDENCIES:
- ID:
  TYPE:
  STATUS:

CONTEXT REQUEST ID:
CONTEXT MANIFEST ID:
CONTEXT RECEIPT ID:
CONTEXT BUNDLE DIGEST:

ACCEPTANCE CRITERIA:
1. ID:
   DESCRIPTION:
   EVIDENCE:
   BLOCKING: true

REQUIRED RECORDS:
- [ ]

REQUIRED TESTS:
- COMMAND:
  EXPECTED:

ROLLBACK OR RECOVERY:
[Exact plan]

OUTPUT ARTIFACTS:
- TYPE:
  PATH:
  REQUIRED DIGEST:

HANDOFF DESTINATION:

OWNER APPROVAL REQUIRED:
OWNER APPROVAL RECORD:
APPROVAL TARGET DIGEST:

MATERIAL-CHANGE TRIGGERS:
- scope;
- artifact digest;
- executor;
- environment;
- risk;
- migration;
- cost;
- security;
- [additional]

DEFINITION OF READY RESULT:
TASK PACKET DIGEST:
```

## I.8 Context-request template

```text
CONTEXT REQUEST ID:
WORK ORDER:
REQUESTED OUTPUT:
ACTIVE ROLE:
WORK TYPE:
DECISION LEVEL:
RISK CLASS:
AUTHORITY DOMAINS:

REQUIRED SOURCE GROUPS:
- governance core;
- [ ]

EXACT SOURCE IDS:
- [ ]

TARGET REPOSITORY:
TARGET COMMIT:
TARGET FILES:
- [ ]

STABLE IDS:
- [ ]

STRUCTURED QUERIES:
- SOURCE:
  FIELDS:
  FILTERS:
  ORDER:
  LIMIT:

KNOWN CONFLICTS:
- [ ]

REQUIRED EXACT CONTENT:
- schemas;
- approvals;
- tests;
- baselines;
- [ ]

OPTIONAL SUPPORTING CONTENT:
- [ ]

BUDGET PROFILE:
FRESHNESS REQUIREMENTS:
EXPECTED RECEIPT:
```

## I.9 Context-receipt template

```text
CONTEXT RECEIPT ID:
REQUEST ID:
WORK ORDER:
RESOLVER VERSION:
STARTED:
COMPLETED:
STATUS:

SELECTED SOURCES:
- SOURCE ID:
  VERSION:
  STATUS:
  LOCATOR:
  DIGEST:
  LOAD MODE:
  EXACT BYTES:
  DERIVED BYTES:
  REASON:

STRUCTURED QUERY RESULTS:
- QUERY ID:
  RESULT IDS:
  RESULT DIGEST:

EXCLUDED SOURCES:
- SOURCE ID:
  REASON:

FAILED RESOLUTIONS:
- SOURCE ID:
  ERROR:
  BLOCKING:

CONFLICTS:
- CONFLICT ID:
  SOURCES:
  DISPOSITION:

APPROVAL RECORDS:
- [ ]

CONTEXT BUNDLE DIGEST:
LIMITATIONS:
INVALIDATION TRIGGERS:
```

## I.10 Implementation-plan template

```text
IMPLEMENTATION PLAN ID:
WORK ORDER:
AUTHOR:
ARTIFACT DIGEST:

CURRENT STATE:
[Verified repository or artifact state]

PROPOSED CHANGE:
[Smallest coherent change]

FILES:
- [ ]

STABLE IDS:
- [ ]

CONTRACT IMPACT:
- [ ]

DATA IMPACT:
- [ ]

MIGRATION IMPACT:
- [ ]

PERMISSION IMPACT:
- [ ]

ENTITLEMENT IMPACT:
- [ ]

SECURITY AND PRIVACY IMPACT:
- [ ]

ACCESSIBILITY IMPACT:
- [ ]

PERFORMANCE AND COST IMPACT:
- [ ]

TEST ORDER:
1. [narrow test]
2. [contract test]
3. [integration]
4. [required full gate]

FAILURE FALLBACK:
- [ ]

ROLLBACK:
- [ ]

MATERIAL DECISIONS:
- [ ]

OWNER GATE:
- [none or exact question]
```

## I.11 Repository-preflight record template

```text
PREFLIGHT ID:
WORK ORDER:
REPOSITORY:
WORKTREE:
BRANCH:
BASE COMMIT:
CURRENT HEAD:
ENVIRONMENT:
AGENT INSTANCE:
ROLE:

STATUS CLEAN:
UNCOMMITTED FILES:
ALLOWED PATHS:
FORBIDDEN PATHS:
REQUIRED TOOLS:
TOOL VERSIONS:
PRODUCTION CREDENTIALS PRESENT: false
CONTEXT RECEIPT CURRENT:
APPROVAL CURRENT:
PREFLIGHT RESULT:
BLOCKERS:
```

## I.12 Change-record template

```text
CHANGE RECORD ID:
WORK ORDER:
AUTHOR:
START COMMIT:
END COMMIT OR ARTIFACT:

CHANGED FILES:
- PATH:
  BEFORE DIGEST:
  AFTER DIGEST:

CHANGED STABLE IDS:
- ID:
  CHANGE TYPE:

BEHAVIOR CHANGE:
[ ]

SCHEMA OR CONTRACT CHANGE:
[ ]

MIGRATION:
[ ]

SOURCE AND PROVENANCE:
[ ]

TESTS:
[ ]

KNOWN LIMITATIONS:
[ ]

DECISIONS:
[ ]

APPROVAL IMPACT:
[ ]

FINAL DIGEST:
```

## I.13 Test-evidence template

```text
TEST EVIDENCE ID:
WORK ORDER:
ARTIFACT DIGEST:
ENVIRONMENT:
EXECUTOR:
STARTED:
COMPLETED:

TEST RUNS:
- RUN ID:
  COMMAND:
  FIXTURE:
  EXPECTED:
  ACTUAL:
  RESULT:
  LOG OR ARTIFACT:
  DIGEST:

FAILED RUNS RETAINED:
- [ ]

RERUN RELATIONSHIPS:
- [ ]

8D-007J REQUIRED:
8D-007J RESULT:
FINAL TEST STATUS:
LIMITATIONS:
```

## I.14 Independent-review request template

```text
REVIEW REQUEST ID:
WORK ORDER:
REVIEW TYPE:
AUTHOR AGENT:
REVIEWER ROLE:
REVIEWER AGENT:
ARTIFACT DIGEST:

OBJECTIVE:
SCOPE:
OUT OF SCOPE:
CONTROLLING SOURCES:
CONTEXT RECEIPT:
CHANGED ARTIFACTS:
TEST EVIDENCE:
KNOWN FAILURES:
MIGRATION:
SECURITY:
PRIVACY:
ACCESSIBILITY:
APPROVAL BOUNDARY:
REQUIRED FINDING FORMAT:
DUE OR BLOCKING CONDITION:
```

## I.15 Review-report template

```text
REVIEW REPORT ID:
REQUEST ID:
WORK ORDER:
REVIEWER:
INDEPENDENCE CONFIRMED:
CONTEXT RECEIPT:
ARTIFACT DIGEST:

FINDINGS:
- FINDING ID:
  SEVERITY:
  DOMAIN:
  DESCRIPTION:
  EVIDENCE:
  REQUIRED ACTION:
  BLOCKING:
  DISPOSITION:

SCOPE COMPLIANCE:
ARCHITECTURE:
CANON:
TESTS:
MIGRATION:
SECURITY:
PRIVACY:
ACCESSIBILITY:
PROVENANCE:
CLAIMS:

RECOMMENDATION:
- approve;
- approve with conditions;
- changes required;
- reject;
- stop work.

FINAL DIGEST:
```

## I.16 Security-review template

```text
SECURITY REVIEW ID:
WORK ORDER:
ARTIFACT DIGEST:
REVIEWER:

ASSETS:
TRUST BOUNDARIES:
SUBJECTS:
DATA CLASSES:
EXTERNAL PROVIDERS:
SECRETS:
ENTRY POINTS:
MUTATIONS:
EXPORTS:
AI TOOLS:

THREATS:
- ID:
  SCENARIO:
  IMPACT:
  LIKELIHOOD:
  CONTROL:
  RESIDUAL RISK:

AUTHENTICATION:
AUTHORIZATION:
HIDDEN INFORMATION:
INPUT VALIDATION:
UPLOADS:
DEPENDENCIES:
LOGGING:
BACKUP:
INCIDENT:
PROVIDER EXIT:

BLOCKING FINDINGS:
OWNER RISK ACCEPTANCE REQUIRED:
RECOMMENDATION:
```

## I.17 Migration-plan template

```text
MIGRATION PLAN ID:
WORK ORDER:
MIGRATION ID:
SOURCE VERSION:
TARGET VERSION:
ARTIFACT DIGEST:

SCOPE:
AFFECTED RECORDS:
AFFECTED STABLE IDS:
SOURCE FIELDS:
TARGET FIELDS:
TRANSFORMATION:
DEFAULTS:
UNRESOLVABLE DATA:
PROVENANCE:
EVENT COMPATIBILITY:
SNAPSHOT COMPATIBILITY:
PACK COMPATIBILITY:
PERMISSION IMPACT:
ENTITLEMENT IMPACT:

PRECONDITIONS:
BACKUP:
RESTORE PROOF:
DRY RUN:
COUNT RECONCILIATION:
INTEGRITY CHECKS:
ROLLBACK:
FORWARD REPAIR:
RESTART BEHAVIOR:
RECEIPT:
OWNER GATE:
```

## I.18 Owner-decision request template

```text
OWNER DECISION ID:
OWNER: John Brandon Turner
REQUESTED BY:
WORK ORDER:
DECISION LEVEL: A3
STATUS: requested

EXACT QUESTION:
[One bounded decision]

RECOMMENDATION:
[Best recommendation]

WHY:
[Concise reasons]

OPTIONS:
1. OPTION:
   BENEFITS:
   COST:
   RISK:
   REVERSIBILITY:

2. OPTION:
   BENEFITS:
   COST:
   RISK:
   REVERSIBILITY:

CONTROLLING SOURCES:
- [ ]

SPECIALIST REVIEWS:
- [ ]

AFFECTED ARTIFACT:
ARTIFACT DIGEST:
EXECUTOR:
ENVIRONMENT:
VALIDITY OR SINGLE-USE CONDITION:
ROLLBACK:
CONSEQUENCES OF NO DECISION:
NEXT ACTION AFTER APPROVAL:

REQUESTED RESPONSE:
- approve;
- reject;
- revise;
- hold.

Silence is not approval.
```

## I.19 Owner-approval record template

```text
APPROVAL ID:
OWNER:
DECISION REQUEST:
WORK ORDER:
APPROVED ACTION:
SCOPE:
ARTIFACT DIGEST:
EXECUTOR:
ENVIRONMENT:
CONDITIONS:
VALID FROM:
EXPIRES:
SINGLE USE:
REVOCATION:
OWNER SIGN-OFF OR RECORD:
STATUS:
```

## I.20 Stop-work template

```text
STOP-WORK ID:
WORK ORDER:
TRIGGER:
DECISION LEVEL:
PROTECTED DOMAIN:
RECORDING ROLE:
AFFECTED SCOPE:
EVIDENCE:
IMMEDIATE CONTAINMENT:
REQUIRED AUTHORITY:
CURRENT STATE:
RESUME CONDITIONS:
OWNER NOTIFICATION:
CREATED:
```

## I.21 Failure-remediation template

```text
REMEDIATION ID:
WORK ORDER:
FAILED GATE:
FAILED RUN:
ROOT CAUSE:
AFFECTED ARTIFACTS:
CORRECTIVE CHANGE:
APPROVAL INVALIDATED:
CONTEXT INVALIDATED:
DOWNSTREAM GATES INVALIDATED:
TARGETED RERUN:
FULL RERUN:
NEW EVIDENCE:
FINAL DISPOSITION:
```

## I.22 Handoff template

```text
HANDOFF ID:
WORK ORDER:
FROM AGENT:
FROM ROLE:
TO ROLE OR AGENT:
REASON:
STATUS:

CURRENT OBJECTIVE:
COMPLETED:
OPEN WORK:
NEXT EXECUTABLE ACTION:

REPOSITORY:
BRANCH:
WORKTREE:
HEAD:
UNCOMMITTED CHANGES:

CHANGED FILES:
CHANGED STABLE IDS:
OUTPUT ARTIFACTS:
CHECKSUMS:

CONTEXT RECEIPT:
APPROVALS:
DECISIONS:
TESTS:
FAILED EVIDENCE:
REVIEWS:
BLOCKERS:
OWNER DECISION QUEUE:
EVIDENCE LOCATIONS:
CLEANUP STATE:
CONTINUITY DIGEST:
SUCCESSOR ACKNOWLEDGEMENT:
```

## I.23 Recovery-plan template

```text
RECOVERY PLAN ID:
INTERRUPTION:
DETECTED:
WORK ORDER:
AFFECTED AGENT:
AFFECTED ROLE:
AFFECTED ENVIRONMENT:

EVIDENCE TO PRESERVE:
- [ ]

AUTHORITY IMPACT:
SECURITY IMPACT:
SECRET IMPACT:
DATA IMPACT:
MIGRATION IMPACT:
GATE IMPACT:

RECONSTRUCTION CHECKS:
- packet identity;
- context receipt;
- authority;
- approval;
- workspace;
- changes;
- dependencies;
- gates;
- failures;
- owner queue;
- continuity digest.

SUCCESSOR REQUIREMENTS:
GATES TO RERUN:
STOP CONDITIONS:
RECORDED NEXT ACTION:
FALLBACK:
```

## I.24 Completion-report template

```text
COMPLETION REPORT
Project: Multiversal
Work item:
Work order:
Status:

Actually completed:
- [ ]

Changed artifacts:
- [ ]

Tests:
- [ ]

CI:
- [ ]

Pull request:
Merge or squash commit:

Validation:
- [ ]

Preserved restrictions:
- no production deployment;
- no paid service;
- no public release;
- [additional]

Known limitations:
- [ ]

Evidence:
- [ ]

Exact next step:
[ ]

Artifact links:
- [ ]
```

## I.25 Documentation-editor prompt

```text
You are editing the canonical Multiversal Project Bible.

Requirements:
- preserve all existing approved material;
- do not restart or redesign the project;
- use the exact master table of contents;
- distinguish canonical, planned, implemented, validated, operational, and released;
- preserve owner authority;
- preserve source citations and provenance;
- preserve known conflicts and limitations;
- do not claim repository completion without verification;
- insert new material before Current Editorial Progress;
- maintain exactly one final Next Step statement;
- create a backup before editing;
- validate chapter and appendix counts;
- calculate SHA-256;
- provide the complete master file.

Owner: John Brandon Turner.
```

## I.26 Content-normalization prompt

```text
Normalize the provided Multiversal source into governed canonical candidates.

Do:
- preserve source ID and exact coordinate;
- preserve raw wording;
- separate Definition, placement, instance, and live state;
- identify object family;
- propose stable ID without overwriting existing identity;
- identify owner pack;
- identify dependencies;
- map Actions, Effects, Conditions, Resources, modifiers, grants, and rules profiles;
- preserve uncertainty;
- identify duplicate, alias, variant, or conflict;
- validate against schema;
- produce provenance records.

Do not:
- invent missing lore or mechanics;
- flatten variants;
- remove unresolved conflicts;
- promote canon;
- alter source wording silently;
- duplicate an existing owner record.
```

## I.27 UI vertical-slice prompt

```text
Implement one bounded Multiversal UI vertical slice.

Required:
- current Stage A work order;
- shared UI system;
- real governed data or explicit temporary adapter;
- service-level permissions;
- persistence;
- loading, empty, error, forbidden, stale, and recovery states;
- desktop, tablet, and mobile behavior;
- keyboard and screen-reader behavior;
- interaction tests;
- automated accessibility checks;
- reproducible preview;
- changed-artifact and test evidence.

Do not:
- create disconnected mock screens;
- implement trusted permission logic only in the client;
- duplicate feature code across platform shells;
- use production credentials;
- broaden to unrelated features.
```

## I.28 Repository-repair prompt

```text
Inspect the failing Multiversal CI or test run.

Perform:
1. retrieve exact failing job, step, logs, and artifacts;
2. reproduce locally when practical;
3. identify root cause;
4. repair within current work-order scope;
5. preserve the failed evidence;
6. rerun the narrow test;
7. rerun all required gates;
8. verify approval and context remain current;
9. update the pull request and handoff;
10. merge only when required checks pass.

Do not:
- delete the failing test;
- rewrite expected output merely to pass;
- conceal the failure;
- broaden scope without a revised packet.
```

## I.29 WP-011 one-pass wrapper template

```text
Use the sealed WP-011 v0.4.0 package and its repository-specific prompt.

Before execution verify:
- exact package checksum;
- exact repository commit;
- correct borrowed Mac;
- Xcode and toolchain ceiling;
- external evidence destination;
- disposable workspace;
- no production credentials;
- owner present for human gates.

Follow the package exactly.
End only with:
- PASS; or
- HARD_GATE;
plus complete external evidence and cleanup receipt.

Do not improvise a newer commit or App Store submission.
```

## I.30 Template validation rule

A template is ready only when:

- no unresolved placeholder remains;
- current source and repository state are attached;
- authority is correct;
- exact scope is bounded;
- required tests are named;
- evidence locations are defined;
- owner-only gates are explicit.

---

# Appendix J — Change Log

## J.1 Purpose

Record the editorial evolution, scope additions, backups, milestone states, and integrity checks of the consolidated Multiversal Project Bible.

This change log covers the current master-document reconstruction effort.

It does not replace Git history after the Bible is integrated into a canonical repository.

## J.2 Working document identity

**Working filename:**

```text
MULTIVERSAL_PROJECT_BIBLE_v2.0.md
```

**Owner and final authority:** John Brandon Turner

**Working location during this editorial program:**

```text
/mnt/data/MULTIVERSAL_PROJECT_BIBLE_v2.0.md
```

The working sandbox path is not the permanent canonical repository location.

## J.3 Editorial method

The manuscript was built through large verified tranches.

Each tranche:

- preserved prior content;
- created a backup;
- inserted new chapters or appendices before Current Editorial Progress;
- updated progress;
- retained exactly one Next Step statement;
- validated chapter or appendix count;
- calculated SHA-256.

## J.4 Volume and chapter milestones

### J.4.1 Volume I — Project Foundation

Added:

1. Project Identity.
2. Vision, Mission, and Product Boundaries.
3. Project History and Architectural Evolution.
4. Canon, Governance, and Authority.
5. Repository and Documentation Architecture.
6. AI Contributor Operating Model.

### J.4.2 Volume II — Multiversal Game System

Added Chapters 7–26 covering:

- runtime contract;
- resolution;
- Characters;
- progression;
- Actions;
- Effects;
- Conditions;
- Resources;
- modifiers;
- Abilities;
- combat;
- social;
- investigation;
- exploration;
- downtime;
- crafting;
- Assets;
- creatures;
- species;
- balance.

Added Tranche 2 Integration Review.

### J.4.3 Volume III — World and Content Architecture

Added Chapters 27–33 covering:

- cosmology;
- content domains;
- setting packs;
- adventure and Campaign content;
- factions and relationships;
- content production;
- art, media, and localization.

Added Tranche 3 Integration Review.

### J.4.4 Volume IV — Object and Data Architecture

Added Chapters 34–41 covering:

- canonical object model;
- stable IDs;
- schemas;
- pack lifecycle;
- dependencies and extensions;
- provenance;
- installation and migration;
- runtime indexing.

Added Tranche 4 Integration Review.

### J.4.5 Volume V — Application Design

Added Chapters 42–53 covering:

- product shell;
- Player experience;
- GM experience;
- Character workspace;
- Campaign and Scene Builder;
- live approval loop;
- combat;
- inventory and Assets;
- investigation and social;
- World Builder;
- search and help;
- accessibility and themes.

Added Tranche 5 Integration Review.

### J.4.6 Volume VI — Technical Architecture

Added Chapters 54–64 covering:

- system context;
- provider-neutral ports;
- identity;
- authorization;
- entitlements;
- persistence;
- migration;
- realtime;
- sessions;
- backup;
- restore;
- provider exit;
- security;
- observability;
- testing;
- deployment.

Added Tranche 6 Integration Review.

### J.4.7 Volume VII — AI Development Operations

Added Chapters 65–72 covering:

- team roles;
- authority;
- context loading;
- credit optimization;
- work orders;
- repository workflow;
- quality gates;
- handoff;
- recovery;
- documentation.

Added Tranche 7 Integration Review.

### J.4.8 Volume VIII — Roadmap, Verification, and Release

Added Chapters 73–80 covering:

- completed phases;
- current implementation;
- acceptance gates;
- internal alpha;
- closed alpha;
- beta;
- commercial readiness;
- public release;
- Apple track;
- risks and owner decisions.

Added Tranche 8 Integration Review.

## J.5 Appendix milestones

### J.5.1 Appendices A–E

Added:

- Appendix A — Glossary;
- Appendix B — Abbreviations;
- Appendix C — Naming and Stable-ID Reference;
- Appendix D — Canonical Repository Map;
- Appendix E — Decision Register.

### J.5.2 Appendices F–J

Added:

- Appendix F — Source and Provenance Index;
- Appendix G — Developer Checklists;
- Appendix H — Validation and Release Checklists;
- Appendix I — AI Prompt and Work-Order Templates;
- Appendix J — Change Log.

## J.6 Major editorial corrections preserved

The manuscript preserves or calls out:

- stale current-state records;
- the P9-06-008 numbering conflict;
- the difference between port foundations and complete behavior;
- the difference between planning and implementation;
- the difference between internal alpha and public release;
- the exact WP-011 commit binding;
- the Chapter 49/50 TOC inconsistency, resolved by synchronizing the Table of Contents with the Stage A order;
- incomplete human playtesting and formal accessibility claims.

## J.7 Repository verification added during drafting

The editorial program verified:

- P9-06-001 through P9-06-007 commits;
- Stage A A0 baseline;
- Stage A A1 merge;
- current latest verified application commit;
- bootstrap current-state rules;
- current active next task.

## J.8 Known verified repository commits represented

```text
d5d74140704115acebb03f4a899e3abf2d378b26
0225d90959fc77baa5b895dcbefeea0f55b2ba4d
97a90ba1204125d4baf2be1763f9fc78f4dc301f
f06d8733ba7478f58b82fa523e55d51ec8a72a66
4e7934a4ad6fef2a31c2e6ecab5a66c838e160af
f8a34a43e58dd7d12f2eb2602e80c4aeacce8034
149b866f530f3a8896170bfe3ba6af0c01fb2f72
398f4d14fc189f8fc786aa093377a96e01d28548
```

## J.9 Backup history

Backups preserved during the editorial program include:

```text
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_sprints_4_6.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_sprints_7_8.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche2_backup.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche3_sprints_1_3.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche3_sprints_4_6.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche4_sprints_1_3.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche4_sprints_4_6.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche5_sprints_1_3.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche5_sprints_4_6.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche5_sprints_7_9.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche6_sprints_1_3.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche6_sprints_4_6.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche6_sprints_7_9.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche7_sprints_1_3.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche7_sprints_4_6.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche8_sprints_1_3.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_tranche8_sprints_4_6.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_appendices_A_E.md
.MULTIVERSAL_PROJECT_BIBLE_v2.0.pre_appendices_F_J.md
```

These backups are working-session safety artifacts.

They are not the permanent released version history.

## J.10 Selected integrity milestones

Known recorded master-document SHA-256 values include:

### After Tranche 5, Sprints 4–6

```text
f435ace89f280b8eaf8d42b7037d9478dd60f130acc4996be3e9ce584ef93dca
```

### After Tranche 6, Sprints 4–6

```text
9661b9703d0068d60cf8c2efa0f6c8f1eb907f75b2bc9a6f5445dca49f79f603
```

### After Tranche 8, Sprints 1–3

```text
ecc7c71a6fee00734e1d383cc8048ddcd2b1874ea1ae5e6da46d3d69ee1fdbe4
```

### After Tranche 8, Sprints 4–6

```text
d434d1994ac36336aa18afcf5bf2dadbf813db5c14951fcfa5e23252985efa67
```

### After Appendices A–E

```text
1d24abb1c96ce017f1b09507de019e8886d0a1ba07ec5062e6e8dfe7a1a2e571
```

### After Appendices F–J, before final editorial audit

```text
ee78f01288a86b22c139293bfac3633347904aafdbeb28cf3e9c2051ea7c267a
```

The exact final audited-master checksum is maintained in the companion `.sha256` file and release manifest. It is not embedded in the audited Markdown because embedding the file's own checksum would change the file and invalidate that checksum.

## J.11 Manuscript status after Appendices F–J

The working manuscript contains:

- 80 numbered chapters;
- eight volumes;
- seven tranche integration reviews after Volume II;
- ten appendices;
- current editorial progress;
- one final Next Step statement.

## J.12 Final editorial audit result

The final editorial audit completed with a **PASS** result on 2026-08-05.

Verified:

- all 80 numbered chapters are present exactly once and in sequence;
- all ten appendices are present exactly once and in sequence;
- all eight volume headings are present;
- all seven tranche integration reviews are present and listed in the Table of Contents;
- the Table of Contents matches every numbered chapter heading;
- the Chapter 49/50 order is resolved consistently;
- numbered chapter subsections use the correct chapter prefix and sequential numbering;
- top-level headings are unique;
- Markdown code fences are balanced;
- exactly one final `Next Step` statement remains;
- the latest verified application head remains `149b866f530f3a8896170bfe3ba6af0c01fb2f72`;
- the latest verified governance head used for this audit is `29278c8568114ffc77ba4176aa88b664875ca35a`;
- P9-06-001 through P9-06-007 remain the verified merged application boundary;
- P9-06-008 remains the active next repository task under the newer roadmap;
- the P9-06-008 historical numbering conflict remains explicitly documented;
- planning, implementation, validation, operational, alpha, production, and public-release states remain distinguished;
- owner and contributor authority remains explicit;
- the audited Markdown, audit report, manifest, checksum, validator, and repository handoff are assembled as a companion handoff package.

Limitations preserved:

- the Bible is an audited release candidate, not yet merged into a canonical repository;
- this editorial audit did not rerun the application repository's complete CI suite;
- the source and provenance appendix is a human-readable index, not the final machine source-registry export;
- no internal-alpha, production, commerce, public-release, or App Store action is authorized by this audit.

## J.13 Final-release versioning recommendation

Recommended final editorial release process:

1. Freeze the audited Markdown.
2. Assign final document ID.
3. Assign release version.
4. Record owner and status.
5. Generate source and evidence manifest.
6. Generate checksum.
7. Create a release backup.
8. Integrate through a governed repository PR.
9. Run documentation validation.
10. Record merge commit.
11. Supersede prior Development Bible artifacts explicitly.
12. Preserve the complete working history.

## J.14 Change-log maintenance rule

Future changes should add a dated entry containing:

- version;
- status;
- author or agent role;
- work order;
- changed sections;
- reason;
- source changes;
- implementation-state changes;
- tests;
- approvals;
- checksum;
- supersession.

Do not rewrite prior entries.

## J.15 Final editorial audit entry

**Date:** 2026-08-05  
**Status:** PASS  
**Input digest:** `ee78f01288a86b22c139293bfac3633347904aafdbeb28cf3e9c2051ea7c267a`  
**Application repository verified head:** `149b866f530f3a8896170bfe3ba6af0c01fb2f72`  
**Governance repository verified head:** `29278c8568114ffc77ba4176aa88b664875ca35a`

Changes made:

- synchronized the Table of Contents with Chapters 49 and 50;
- added all seven tranche integration reviews to the Table of Contents;
- resolved the documented ordering inconsistency;
- completed the missing Tranche 6 milestone checksum;
- normalized release-candidate metadata;
- verified heading, numbering, appendix, code-fence, cross-reference, and Next Step invariants;
- generated the companion audit report, release manifest, validator, checksums, and canonical-repository handoff package.

The exact final audited-master digest is recorded outside the Markdown in the companion checksum and manifest.


# Current Editorial Progress

## Final editorial state

### Structure

- 80 numbered chapters complete and audited
- eight volumes complete
- seven tranche integration reviews complete and indexed
- ten appendices complete and audited
- Master Table of Contents synchronized with chapter and appendix order
- Chapter 49/50 ordering inconsistency resolved
- one final Next Step statement retained

### Repository status verified for this audit

- application repository: `cybalicistjt-stack/Multiversal-app`
- verified application head: `149b866f530f3a8896170bfe3ba6af0c01fb2f72`
- governance repository: `cybalicistjt-stack/multiversal-aioc`
- verified governance head: `29278c8568114ffc77ba4176aa88b664875ca35a`
- P9-06-001 through P9-06-007 remain the verified merged application boundary
- Stage A A0 and A1 remain complete
- P9-06-008 remains the active next repository task under the newer roadmap

### Release-candidate artifacts

The audited handoff set includes:

- complete Markdown master;
- SHA-256 checksum;
- final editorial audit report;
- release manifest;
- reusable documentation validator;
- canonical-repository handoff instructions;
- compressed handoff package and package checksum.

### Preserved boundary

This editorial PASS does not claim that every described application feature is implemented.

Later acceptance gates, alpha stages, production, commerce, public release, and App Store distribution remain incomplete and owner-gated.

---

**Next Step:** Canonical Repository Integration — place the audited Bible and companion release files in `multiversal-aioc` through a governed branch and pull request, run documentation validation, merge, and record the canonical release commit.
