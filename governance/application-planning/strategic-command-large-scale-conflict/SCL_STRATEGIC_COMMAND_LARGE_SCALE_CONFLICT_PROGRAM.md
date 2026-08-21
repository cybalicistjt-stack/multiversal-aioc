# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL  
**Activation:** after WCI-05  
**Successor:** VTI-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Purpose

SCL adds governed play above the individual encounter: squads, units, formations, armies, fleets and other organized forces. It reuses ordinary Combat, Character, Vehicle, Economy, Organization, World and Event authority, adding scale-aware command/order/resolution contracts rather than a second combat ledger.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map**  
   Reconcile retained squad/fleet/command/mass-conflict material with Combat, MIB-14, MIB-13, MIB-09, WCI and World authorities; define scale boundaries and cross-scale handoffs.

2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model**  
   Define reusable unit/formation profiles, membership, composition, capabilities, readiness, equipment/vehicle references and derived projections without duplicating member truth.

3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication**  
   Implement commanders, subordinate roles, command capacity, order types, communication/range/delay/interruption and delegated authority with explicit permission boundaries.

4. **SCL-04 — Command Phases & Deterministic Order Resolution**  
   Support command/movement/action/resolution-style phases where authored, simultaneous/ordered actions, conflicts, reactions and deterministic aggregate resolution with traceable receipts.

5. **SCL-05 — Morale, Cohesion, Leadership & Discipline**  
   Model morale/cohesion/readiness, leadership effects, panic/rout/rally, discipline and command disruption through profile-driven rules rather than universal assumptions.

6. **SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness**  
   Connect ammunition/resources, supply, fuel, maintenance, fatigue, replacements, reinforcement, staging and readiness to Economy, Vehicles/Bases and Projects.

7. **SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position**  
   Represent objectives, control, fronts/zones, fortifications, sieges, terrain/environment effects and strategic positioning over World/MAI semantic locations without making map art canonical.

8. **SCL-08 — Vehicle, Mecha, Ship & Fleet Integration**  
   Integrate crewed vehicles/platforms into units and fleet formations, including stations, cargo/fuel, damage, repair, formation roles and command interactions.

9. **SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery**  
   Define how individual actions/characters affect units and how aggregate results map back to members/assets, casualties, injuries, captured/missing states, damaged equipment and recovery without double-applying effects.

10. **SCL-10 — Faction, Settlement, World & Campaign Consequence Integration**  
    Connect strategic outcomes to organizations, territory, diplomacy, settlements, economy, reputation, Adventures and World Events through explicit owner-domain mutations.

11. **SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof**  
    Deliver command dashboards, accessible non-map views, unit/fleet packs and scenarios proving individual combat → squad → fleet/army → campaign consequences with recovery and deterministic evidence.

## Invariants

- Ordinary Combat/Action/Event truth remains canonical.
- Units/formations are governed projections/aggregates over canonical members/assets, not duplicate Characters or inventories.
- Aggregate resolution cannot create double damage, duplicate casualties or hidden authority shortcuts.
- Organization/faction/settlement/economy/world consequences commit only through their owning domains.
- AI may advise command decisions but never issues authoritative orders or adjudicates outcomes.
