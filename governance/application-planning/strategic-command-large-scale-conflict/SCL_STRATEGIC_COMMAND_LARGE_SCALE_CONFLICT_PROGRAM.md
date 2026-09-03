# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-09; SCL-10 IN_PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-09 are `completed_verified`. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — is governed-started from exact application main `6a562277beabbdeffd8b1514d5c006224aab15ef` on branch `integration/scl-10-strategic-consequence-integration`.

## Governed SCL-10 contract

SCL-10 is a visibility-first deterministic read-only integration projection over explicit canonical strategic-consequence owner observations. Governed target kinds are `faction`, `settlement`, `world`, and `campaign`; projection evidence states are `resolved`, `unknown`, `conflict`, and `incompatible`.

Canonical owners remain authoritative: MIB-09 for faction/relationship/reputation truth; MIB-11 and WCI for settlement/world truth; APW-D26 for Project/campaign-time truth; Event for event/consequence truth; Permission/visibility for disclosure. ODL-07 supplies identity-preserving settlement/faction SCL reference links but does not become the consequence owner.

Every represented consequence requires an explicit visible canonical owner observation with stable consequence id, target kind/reference, owner authority/reference, SCL source/result reference, context, provenance and visibility references. SCL-10 may reconcile repeated visible observations and emit deterministic read-only owner-handoff lines; it never creates or commits the owner consequence.

No battle, order, objective, casualty, damage, readiness or other SCL result automatically changes faction standing, settlement control/status, world state, campaign state or campaign time. The sealed sources/current contracts provide no universal reputation/control/territory/resource/settlement/world/campaign conversion formula, so that remains an explicit gap rather than an invented mechanic.

Visibility filters before all consequence rows, counts, target/reference lists, summaries, search, provenance, handoffs, deterministic receipts and AI context. Hidden existence/cardinality is undisclosed. Missing, hidden, unknown, conflict or incompatible evidence stays conservative. Duplicate visible canonical consequence identity with incompatible owner/target/source tuples makes completeness false rather than being silently merged.

SCL-10 performs no owner mutation, Event creation, campaign-time advancement, consequence synthesis, autonomous AI adjudication, duplicate durable ledger, persistence or migration `0022`. SCL-11 retains workbench, scenario packs, balance and cross-scale golden proof.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — completed_verified.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — completed_verified.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — completed_verified.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — completed_verified.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — in_progress.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

Production mutation is bounded to the governed SCL-10 read-only strategic-consequence integration contract and acceptance-first validation. SCL-11+, MAL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
