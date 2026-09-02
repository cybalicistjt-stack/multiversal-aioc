# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-01; SCL-02 IN_PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Current state

SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — is `completed_verified` on application PR `385`, validated head `065d3a92429ee19431067b558f6181a7182f971b`, validation run `33664804272`, deterministic receipt `9d74f2ad2fddc9bef729938764acb6de775028fe26d0d02b198b6ca9e007555a`, zero historical predecessor fanout, zero application feature-repair cycles, and application merge `5c1188e5608e7d4c98de762dffece7ee37b6d9fe`.

SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — is `in_progress` from exact application main `5c1188e5608e7d4c98de762dffece7ee37b6d9fe` on branch `integration/scl-02-unit-formation-definition-model` with one bounded implementation authority.

The governed-start context is sealed to completed SCL-01; current Character/Creature canonical identity references; D17 Asset/inventory ownership; MIB-14 vehicle/platform/base operational definitions and capability references; completed ODL organization/load/delegation projections; MV-IA-F020 Permission/visibility; and the current SCL validation-family contract. Unrelated history, connected business systems, provider activation, release/deployment and future SCL mechanics remain blocked unless changed evidence identifies a concrete dependency.

## Purpose

SCL adds governed play above the individual encounter: squads, units, formations, armies, fleets and other organized forces. It reuses ordinary Combat, Character, Creature, Vehicle, Economy, Organization, World and Event authority, adding scale-aware projections and later command/order/resolution contracts rather than a second combat or constituent ledger.

Recovered mine-note RDC-03 scale-transition intent is routed into SCL rather than creating another program. SCL must preserve identity when projecting individuals/assets into groups and when later reconciling aggregate results back down.

## Frozen SCL-01 contract

SCL-01 freezes the source inventory, owner authority map and the scale vocabulary `individual`, `squad`, `unit`, `formation`, `force`, `theater`. Scale labels are coordination/aggregation roles, not universal numeric size caps. Up-scale projections carry explicit canonical constituent ids, owner references and provenance and cannot copy or fork authoritative Character, Creature, Asset, inventory, Vehicle, damage, casualty, Event, Organization, Economy or World state.

Permission/visibility filtering occurs before source/projection inclusion, counts, aggregation, summaries, search, provenance, deterministic receipts or AI context. Hidden existence and hidden cardinality remain undisclosed. Missing, hidden, conflicting or identity-incompatible evidence remains unresolved/conflict/incompatible and is never auto-reconciled.

## SCL-02 frozen governed-start contract

### Profile kinds and scale mapping

SCL-02 defines reusable read-only profile projections for exactly these profile kinds:

1. `squad` → SCL-01 `squad` scale;
2. `unit` → SCL-01 `unit` scale;
3. `formation` → SCL-01 `formation` scale;
4. `fleet` → SCL-01 `force` scale;
5. `army` → SCL-01 `force` scale.

The profile kind is descriptive composition vocabulary. It does not imply a universal numeric size cap, command hierarchy, order authority, combat power or resolution mechanic. `theater` remains strategic context, not an SCL-02 reusable force profile.

### Membership and composition

Every visible membership row carries a stable membership id, the owning SCL-02 profile id, a member kind, a member reference id, explicit leaf canonical constituent ids, owner references, provenance and visibility authorization.

Member kinds are `character`, `creature`, `asset`, `platform`, and `projected-group`. A projected group may reference another aggregate profile only when its leaf canonical constituent ids remain explicit. SCL-02 never treats a nested profile id as a substitute for canonical leaf identity.

Composition is the deterministic visible set of identity-preserving membership rows plus role tags. Empty canonical identity, divergent profile identity, explicit unknown/conflict/incompatible membership evidence, or contradictory identity remains incomplete and is never guessed or auto-reconciled.

No profile creates a duplicate Character, Creature, Asset, inventory, Vehicle, Organization, Combat, Event or World record. No membership automatically grants role/delegation, command, action, system permission or ownership authority.

### Capability, readiness and equipment/platform projections

Capability tags are explicit visible derived projection labels supported by source evidence. SCL-02 computes no numeric combat power, qualification, command capacity, mechanical bonus or universal capability threshold.

Readiness vocabulary is exactly `unknown`, `unready`, `limited`, `ready`. These are descriptive projection bands only. SCL-02 defines no readiness threshold, resource consumption, morale/cohesion calculation, fatigue rule, maintenance failure, action restriction or mechanical effect. SCL-05 and SCL-06 retain later morale/logistics/readiness mechanics.

Equipment and platform references remain canonical D17/MIB-14 references with owner/provenance. SCL-02 does not copy their state, inventory, cargo, crew, module, facility, fuel, damage or maintenance truth and does not implement SCL-08 fleet/platform mechanics.

### Visibility, provenance, conflict and determinism

MV-IA-F020 deny-by-default authorization is applied before membership inclusion, visible counts, composition, capability tags, readiness, equipment/platform references, summaries, search text, provenance, deterministic receipts or AI context. Hidden existence and hidden cardinality remain undisclosed.

Missing, explicit unknown, conflicting or identity-incompatible visible evidence stays conservative and cannot be promoted to a complete profile. Provenance and owner references are never fabricated.

Stable profile-kind, membership-id, canonical-reference and evidence-id ordering determines canonical projection/receipt truth. Presentation prose is excluded from deterministic receipt truth.

### Authority handoffs

- SCL-03 retains command hierarchy, roles, orders and communication.
- SCL-04 retains mechanical and deterministic order resolution.
- SCL-05 retains morale, cohesion, leadership and discipline mechanics.
- SCL-06 retains logistics, supply, fatigue, reinforcement and readiness mechanics.
- SCL-08 retains vehicle, mecha, ship and fleet operational integration.
- SCL-09 retains casualty, damage and recovery reconciliation.
- SCL-10 retains owner-domain strategic consequence integration.

AI may advise only where separately governed. SCL-02 invokes no provider and grants AI no command, order, adjudication, permission, mutation or completion authority.

No durable SCL-02 ledger or migration is authorized. Migration `0022` remains unreserved.

## Test-first implementation contract

The acceptance regression, governed proof, SCL-02 validation profile and invariant verifier are the first application mutation. The production contract and accessible panel must be absent on the RED head and appear together atomically only after genuine RED is established.

The RED head must pass SCL-02 invariants and workspace installation on self-hosted Linux and self-hosted Windows, then fail at client typecheck because only `unit-formation-definition-model` and `SclUnitFormationDefinitionModelPanel` production surfaces are intentionally missing. Cross-platform deterministic comparison must agree on that RED state.

The first complete production head must pass exactly one SCL-02 current-family profile on self-hosted Linux and self-hosted Windows plus deterministic comparison. Historical predecessor profile fanout must remain zero.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — completed_verified.
2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model** — in_progress.  
   Implement the frozen reusable profile, identity-preserving membership/composition, visible capability/readiness and equipment/platform projection contract above.
3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication** — planned.
4. **SCL-04 — Command Phases & Deterministic Order Resolution** — planned.
5. **SCL-05 — Morale, Cohesion, Leadership & Discipline** — planned.
6. **SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness** — planned.
7. **SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position** — planned.
8. **SCL-08 — Vehicle, Mecha, Ship & Fleet Integration** — planned.
9. **SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery** — planned.
10. **SCL-10 — Faction, Settlement, World & Campaign Consequence Integration** — planned.
11. **SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof** — planned.

## Invariants

- Ordinary Combat/Action/Event and canonical constituent/owner-domain truth remain authoritative.
- SCL-01 source inventory, scale taxonomy and owner authority map remain frozen completed authority.
- SCL-02 profiles are governed projections over explicit canonical members/assets, not duplicate Characters, Creatures, inventories, vehicles or organization truth.
- Constituent identity persists through nested profile composition; projected-group references cannot replace leaf canonical ids.
- Capability/readiness/equipment data is derived projection only and cannot silently create mechanics or owner state.
- Aggregate resolution cannot create double damage, duplicate casualties or hidden authority shortcuts.
- AI may advise where separately governed but never issues authoritative orders or adjudicates outcomes.
- No command/order, resolution, morale/logistics effect, casualty/damage mapping, strategic consequence, owner mutation, persistence, migration `0022`, provider activation, tester distribution, release or deployment is authorized by SCL-02.
