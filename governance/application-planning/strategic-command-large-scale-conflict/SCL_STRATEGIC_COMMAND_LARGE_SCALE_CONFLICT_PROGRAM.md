# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-08; SCL-09 IN_PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-08 remain `completed_verified`. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — is governed-started from exact application baseline `1de481381d0d65d3a88d0e1cdc1af77ebe73dfb6` on `integration/scl-09-individual-unit-casualty-damage-recovery` with bounded implementation authority.

## Governed SCL-09 contract

SCL-09 is a visibility-first deterministic **read-only reconciliation projection** over explicit canonical owner results. It maps visible SCL-02 membership/profile identity to explicit Character/Creature, Condition, Combat/Action/Event, Asset/Vehicle damage/repair and recovery result references, then derives only deterministic unit-level summaries and handoffs.

Governed effect kinds are `casualty`, `damage`, `recovery`, `condition`, `stability`, `destruction`, `repair`. Subject kinds are `character`, `creature`, `asset`, `vehicle`. Evidence states are `resolved`, `unknown`, `conflict`, `incompatible`.

Retained source authority is preserved rather than generalized: `Squad & Fleet.PDF` supplies collective squad-HP and repair language; `Non-lethal Damage 11-13-24.PDF` supplies lethal/non-lethal zero-HP stability and negative-HP death-threshold language; `Resist,immune,damage.PDF` supplies massive-damage/injury/recovery language; `Healing 11-7-24.PDF` supplies healing/recovery effects. These remain source-scoped mechanics. SCL-09 may represent their explicit inputs/results, but does not execute them or promote them into a universal SCL health/damage system.

Canonical ownership remains with Character/Creature body and agency, Condition live injury/status/effect state, Combat/Action/Event mechanical resolution, D17/F008 Asset damage/repair history, F014 Vehicle transitions, SCL-02 membership/profile identity, and Permission/visibility. No SCL-09 projection may mutate those owners.

The source squad collective-HP rule may be projected only when the selected source rule and all required compatible **visible** member HP inputs are explicitly supplied. It is not a durable HP ledger and never replaces owner HP truth. Missing, hidden, unknown, conflicting or incompatible inputs leave the rollup unresolved.

No damage, casualty or recovery automatically propagates between vehicles, crew, passengers, nested Assets, squads, fleets or other constituents. Each cross-entity effect requires an explicit canonical owner-result reference. SCL-09 does not infer crew injury from vehicle damage, nested-Asset damage from parent damage, or member death from aggregate loss.

Visibility filters before member/effect inclusion, counts, totals, classifications, summaries, search, provenance, handoffs, deterministic receipts or AI context. Hidden existence/cardinality is undisclosed. Stable identifiers and stable ordering are mandatory. Duplicate visible canonical constituent/effect identity makes completeness false rather than being silently reconciled.

SCL-09 does **not** deal damage, change HP, heal, stabilize, kill, resurrect, apply/remove Conditions, mutate Asset/Vehicle damage state, advance recovery time, commit owner-domain consequences, invoke autonomous AI adjudication, create a duplicate casualty/damage/recovery ledger, persist new durable state, or reserve migration `0022`. SCL-10 retains faction/settlement/world/campaign consequences.

## Validation contract

Acceptance-first production mutation is prohibited until exactly one SCL-09 Validation Core profile proves a genuine matching self-hosted Linux/Windows RED at the missing-production `client-typecheck` boundary and deterministic receipts compare equal. Final validation requires exact-head Linux and Windows GREEN, deterministic comparison, zero historical predecessor profile fanout, and conservative hidden/unknown/conflict behavior.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — completed_verified.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — completed_verified.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — completed_verified.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — in_progress.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — planned.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

Only the sealed SCL-09 read-only reconciliation projection is authorized. SCL-10+, MAL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
