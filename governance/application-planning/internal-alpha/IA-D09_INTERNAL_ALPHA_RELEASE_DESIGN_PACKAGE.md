# IA-D09 — Internal Alpha Release-Design Package

**Program:** MV-IA-001  
**Work item:** IA-D09  
**Status:** DESIGN PACKAGE — release not authorized  
**Authority:** owner-governed repository evidence

## 1. Purpose

This package closes the Internal Alpha design program by consolidating the verified IA-D01 through IA-D08 design outputs into one engineering-facing release-design boundary. It defines what must be implemented and proven before an owner may later decide whether to approve an Internal Alpha release. It does not perform, approve, schedule, or imply a release.

## 2. Scope

The package governs ten release-design dimensions:

1. bidirectional traceability from IA design work to implementation and acceptance evidence;
2. a bounded deterministic fixture catalog;
3. consolidated permission and authority boundaries;
4. consolidated accessibility requirements;
5. interruption, reconnect, stale-state, rollback, and recovery expectations;
6. explicit product and runtime budgets;
7. tester onboarding and entry requirements;
8. a dependency-ordered implementation queue;
9. an owner-decision register for gates that cannot be delegated;
10. final design-completion review.

## 3. Design-program coverage

| Series | Design domain | Release-design disposition |
|---|---|---|
| IA-D01 | program foundation | required baseline |
| IA-D02 | shared foundations | required baseline |
| IA-D03 | character and campaign preparation | required core |
| IA-D04 | first playable loop | required core |
| IA-D05 | relationship, social, investigation | required core |
| IA-D06 | combat and assets | required core |
| IA-D07 | world, adventure, creator, campaign-local content | required core |
| IA-D08 | optional AI, deferred advanced/offline, experimental isolation | optional/isolation boundary |

A release candidate may not substitute optional IA-D08 capabilities for missing IA-D03 through IA-D07 core behavior.

## 4. Release-design state model

The design package distinguishes five states:

- `design_complete`: design requirements are merged and traceable;
- `implementation_ready`: dependencies and acceptance evidence are defined;
- `candidate_built`: application implementation exists but is not approved for release;
- `candidate_validated`: required implementation validation has passed;
- `release_approved`: owner-only decision, outside IA-D09.

IA-D09 may only establish the first two states. It cannot set `release_approved`.

## 5. Core release boundary

The Internal Alpha candidate must preserve all of the following when optional systems are disabled or unavailable:

- character and campaign preparation;
- session and encounter preparation;
- first playable action, GM review, authoritative result, and history;
- social, relationship, reputation, organization/faction, and investigation workflows;
- combat, inventory, shared assets, bounded maps, and basic vehicle operations;
- world, adventure, creator, and Campaign-local content workflows;
- explicit permissions, provenance, recovery, accessibility, and validation visibility.

Optional AI, broad offline authority, advanced map/vehicle behavior, provider-specific capabilities, and experimental processors may enhance the experience but may not become hidden prerequisites for the core candidate.

## 6. Release evidence contract

A future Internal Alpha release decision must be based on evidence, not design completion alone. At minimum, the candidate must provide:

- exact implementation commit and build identity;
- dependency-complete implementation queue evidence;
- passing targeted and integration validators for implemented domains;
- permission and hidden-information isolation proof;
- keyboard, screen-reader, touch, reduced-motion, high-contrast, and text-scaling evidence appropriate to implemented surfaces;
- reconnect and interruption recovery evidence;
- authoritative Event/history replay evidence;
- bounded fixture execution results;
- known-limitations register;
- owner-decision register with all release-blocking decisions resolved.

## 7. Non-negotiable governance boundaries

The candidate may not silently:

- grant AI canonical authority;
- invent provenance;
- reveal hidden or GM-only data;
- use a provider-specific identifier as canonical identity;
- fabricate canonical Events while offline;
- use silent last-write-wins for governed conflicts;
- promote unsupported extension data into canonical semantics;
- bypass approval requirements;
- treat a design document, mockup, branch, commit, PR, or green partial check as a release.

## 8. Implementation handoff contract

Implementation must follow `IA-D09_IMPLEMENTATION_QUEUE.json`. A slice may start only when its declared dependencies are complete enough to support deterministic validation. Work may be parallelized only where data ownership and event contracts do not create hidden cross-slice mutation.

Implementation teams must preserve stable IDs, canonical authority, provider neutrality, proposal/approval semantics, append-only history where specified, and opaque extension preservation.

## 9. Tester-entry contract

A tester may enter only a bounded Internal Alpha candidate whose build identity, test data, account role, permissions, reset/recovery procedure, known limitations, support path, and data-handling boundaries are explicit. Real-user data collection, public enrollment, paid-provider commitments, production credentials, and public release remain separately gated.

## 10. Exit criteria for IA-D09

IA-D09 design work is complete when:

- all required release-design artifacts exist;
- traceability covers IA-D01 through IA-D08 at series level and maps required implementation evidence;
- the fixture catalog is explicitly bounded and not represented as the complete game;
- permission, accessibility, and recovery matrices contain blocking acceptance conditions;
- budgets and tester-entry rules are explicit;
- implementation queue dependencies are deterministic;
- owner-only decisions are separated from ordinary engineering work;
- the targeted validator passes;
- repository PR, CI, and merge evidence are recorded.

Completion of IA-D09 means **Internal Alpha design complete and implementation handoff ready**. It does not mean **Internal Alpha released**.