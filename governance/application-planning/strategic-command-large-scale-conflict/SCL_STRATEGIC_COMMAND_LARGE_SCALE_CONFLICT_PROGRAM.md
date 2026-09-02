# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — SCL-01 IN_PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Current governed tranche

ODL completed_verified through ODL-09 on application main `f0fbab87d41e8962faf092da3599913d919ce6a5`.

SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — is `in_progress` from that exact application main on branch `integration/scl-01-source-inventory-scale-taxonomy-authority-map` with one bounded implementation authority.

The governed-start context is sealed to the current SCL program/backlog; MIB-14, MIB-13, MIB-09, WCI-05; completed ODL authority; A6 Action, A7 Combat, D17 Asset and MIB-11/D18/A10 World authority; and the current validation-core surfaces. Unrelated history, connected business systems, providers, release/deployment and future SCL mechanics remain blocked unless changed evidence names a concrete dependency.

## Purpose

SCL adds governed play above the individual encounter: squads, units, formations, armies, fleets and other organized forces. It reuses ordinary Combat, Character, Vehicle, Economy, Organization, World and Event authority, adding scale-aware command/order/resolution contracts rather than a second combat ledger.

Recovered mine-note RDC-03 scale-transition intent is routed into SCL rather than creating another program. ODL supplies organization/load/delegation semantics before SCL; SCL must explicitly preserve identity when projecting individuals/assets into units and when reconciling aggregate results back down.

## SCL-01 frozen governed-start contract

### Source inventory and authority map

- **A6 Action** remains sole Action proposal/review/decision/atomic accepted-result authority. SCL-01 may retain only read-only canonical Action/result references.
- **A7 Combat** remains ordinary combat authority. SCL-01 creates no second combat or Event ledger.
- **D17 Asset/inventory/state** remains canonical for Assets and their state. **MIB-14** retains reusable vehicle/platform/base operational definitions, capacity/crew/module/facility seams and governed transition routing. SCL-01 may reference canonical constituent/platform ids only.
- **MIB-11/D18/A10 World** remains authoritative for World/Reality/Timeline/location identity and canonical world state. SCL-01 treats those references as strategic context only.
- **MIB-13 Economy** retains versioned economic scopes, trade links, costs and settlement. SCL-01 may surface logistics/economic source references but cannot mutate economy.
- **D25/MIB-09** retain relationship/social runtime truth and derived reputation semantics. SCL-01 may consume visible social/reputation references only.
- **ODL-01..09** remain completed authority for organization, load, cohesion/loyalty, delegation, resources, crisis, integration, GM/advisory and organizational golden-proof semantics. SCL-01 does not reopen ODL mechanics.
- **WCI-05** remains read-only continuity/dependency/consequence analysis over owner domains. Strategic consequences remain committed only by their owning domains.
- **RDC-03 recovered scale-transition material** is noncanonical source intent routed into SCL; it can inform identity-preserving scale transitions but never becomes runtime truth by itself.

### Scale taxonomy

SCL-01 freezes these scale labels as role/aggregation vocabulary, not universal numeric size caps:

1. `individual` — one canonical Character/Creature/Vehicle/Asset actor resolved by existing owner systems;
2. `squad` — a small coordinated command grouping of canonical constituents;
3. `unit` — a reusable aggregate grouping of canonical constituents/assets;
4. `formation` — a coordinated grouping of units under a strategic relationship;
5. `force` — army/fleet-level grouping of formations, units and platforms;
6. `theater` — multi-force strategic context over owner-authored World/Scene/Objective references.

Only `individual` owns constituent truth. `squad`, `unit`, `formation`, `force` and `theater` are governed projections/context. Exact membership/profile composition belongs to SCL-02.

### Identity-preserving projection and handoff

Up-scale projection carries explicit canonical constituent ids, visible state references and provenance. It does not copy or fork authoritative Character, Asset, inventory, Vehicle, damage, casualty, Event, Organization, Economy or World state.

SCL-01 performs no down-scale mutation. Later aggregate outcomes must reconcile through explicit owner-domain proposals/commits. SCL-09 is the primary casualty/damage reconciliation tranche and may not double-apply effects.

SCL-03/04 own future command/order/resolution mechanics; SCL-08 owns platform/fleet integration; SCL-09 owns individual-to-unit effects; SCL-10 owns owner-domain strategic consequence integration. SCL-01 supplies only the source/scale/authority map.

Permission/visibility filtering occurs before source inclusion, counts, aggregation, projection, search text, provenance, deterministic receipts or AI context. Hidden source existence and hidden cardinality remain undisclosed. Missing, hidden, conflicting or identity-incompatible evidence remains explicit `unknown`, `conflict` or `incompatible` and is never auto-reconciled.

AI may only advise where separately governed. SCL-01 invokes no provider and grants AI no command, order, adjudication, permission, mutation or completion authority.

No durable SCL-01 ledger or migration is authorized. Migration `0022` remains unreserved.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — in_progress.  
   Implement the frozen read-only source inventory, nonnumeric scale taxonomy, authority map and identity-preserving projection/handoff contract under the exact governed-start boundaries above.

2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model**  
   Define reusable unit/formation profiles, membership, composition, capabilities, readiness, equipment/vehicle references and derived projections without duplicating member truth. Explicitly define authoritative constituent state versus aggregate projection state.

3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication**  
   Implement commanders, subordinate roles, command capacity, order types, communication/range/delay/interruption and delegated authority with explicit permission boundaries, consuming ODL semantics where applicable.

4. **SCL-04 — Command Phases & Deterministic Order Resolution**  
   Support command/movement/action/resolution-style phases where authored, simultaneous/ordered actions, conflicts, reactions and deterministic aggregate resolution with traceable receipts.

5. **SCL-05 — Morale, Cohesion, Leadership & Discipline**  
   Model morale/cohesion/readiness, leadership effects, panic/rout/rally, discipline and command disruption through profile-driven rules rather than universal assumptions, reusing ODL relationship/organization pressure where appropriate.

6. **SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness**  
   Connect ammunition/resources, supply, fuel, maintenance, fatigue, replacements, reinforcement, staging and readiness to Economy, Vehicles/Bases and Projects.

7. **SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position**  
   Represent objectives, control, fronts/zones, fortifications, sieges, terrain/environment effects and strategic positioning over World/MAI/SSA semantic locations without making map art canonical.

8. **SCL-08 — Vehicle, Mecha, Ship & Fleet Integration**  
   Integrate crewed vehicles/platforms into units and fleet formations, including stations, cargo/fuel, damage, repair, formation roles and command interactions.

9. **SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery**  
   Define how individual actions/characters affect units and how aggregate results map back to members/assets, casualties, injuries, captured/missing states, damaged equipment and recovery without double-applying effects. This tranche is the primary recovered RDC-03 reconciliation point.

10. **SCL-10 — Faction, Settlement, World & Campaign Consequence Integration**  
    Connect strategic outcomes to organizations, territory, diplomacy, settlements, economy, reputation, Adventures and World Events through explicit owner-domain mutations.

11. **SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof**  
    Deliver command dashboards, accessible non-map views, unit/fleet packs and scenarios proving individual combat → squad → fleet/army → campaign consequences with recovery and deterministic evidence.

## Invariants

- Ordinary Combat/Action/Event truth remains canonical.
- Units/formations are governed projections/aggregates over canonical members/assets, not duplicate Characters or inventories.
- Constituent identity persists across scale; aggregation/projection cannot silently fork authoritative state.
- Aggregate resolution cannot create double damage, duplicate casualties or hidden authority shortcuts.
- Organization/faction/settlement/economy/world consequences commit only through their owning domains.
- AI may advise command decisions but never issues authoritative orders or adjudicates outcomes.
- SCL-01 implementation authority grants only the frozen source inventory/scale/authority-map surfaces; no unit aggregate truth, command/order mechanics, strategic resolution, owner mutation, persistence, migration `0022`, provider activation, tester distribution, release or deployment is authorized.
