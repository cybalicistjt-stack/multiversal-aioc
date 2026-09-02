# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-01; SCL-02 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Current state

SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — is `completed_verified` on application PR `385`, validated head `065d3a92429ee19431067b558f6181a7182f971b`, validation run `33664804272`, selector/repository-health job `100363793870`, Linux job `100363841608`, Windows job `100363841486`, deterministic comparison job `100364036387`, deterministic receipt `9d74f2ad2fddc9bef729938764acb6de775028fe26d0d02b198b6ca9e007555a`, zero historical predecessor fanout, zero application feature-repair cycles, and application merge `5c1188e5608e7d4c98de762dffece7ee37b6d9fe`.

SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — is the strict successor and is `selected_not_started` from exact application main `5c1188e5608e7d4c98de762dffece7ee37b6d9fe` with no implementation branch and no implementation authority. A future owner `Continue` must perform bounded governed start before SCL-02 product mutation.

## Purpose

SCL adds governed play above the individual encounter: squads, units, formations, armies, fleets and other organized forces. It reuses ordinary Combat, Character, Vehicle, Economy, Organization, World and Event authority, adding scale-aware command/order/resolution contracts rather than a second combat ledger.

Recovered mine-note RDC-03 scale-transition intent is routed into SCL rather than creating another program. ODL supplies organization/load/delegation semantics before SCL; SCL preserves identity when projecting individuals/assets into units and when later reconciling aggregate results back down.

## Frozen SCL-01 contract

SCL-01 freezes the governed source inventory as A6 Action; A7 Combat; D17 Asset plus MIB-14 operational platform/base; MIB-11/D18/A10 World; MIB-13 Economy; D25/MIB-09 social/reputation; completed ODL-01..09; WCI-05 continuity/consequence analysis; and RDC-03 recovered scale-transition intent as noncanonical routing input.

It freezes `individual`, `squad`, `unit`, `formation`, `force`, and `theater` as scale/aggregation vocabulary. These labels are roles rather than universal numeric size caps. Only `individual` references canonical constituent truth; above-individual records are governed projections/context. Exact membership/composition/profile semantics belong to SCL-02.

Up-scale projection carries explicit canonical constituent ids, owner references and provenance and cannot copy or fork authoritative Character, Asset, inventory, Vehicle, damage, casualty, Event, Organization, Economy or World state. SCL-01 performs no down-scale mutation. Missing, hidden, conflicting or identity-incompatible evidence remains explicit unresolved/conflict/incompatible and is never auto-reconciled.

Permission/visibility filtering occurs before source/projection inclusion, counts, aggregation, summaries, search, provenance, deterministic receipts or AI context. Hidden source existence and hidden cardinality remain undisclosed.

SCL-03/04 retain future command/order/resolution authority; SCL-08 retains future platform/fleet integration authority; SCL-09 is the primary future casualty/damage reconciliation point; SCL-10 retains future owner-domain strategic consequence integration. AI has no command/order/adjudication authority. No durable SCL-01 persistence or migration `0022` was introduced.

## SCL-01 validation closeout

Acceptance-first application commit `40aca594c7e7c0f75debdf4bb189ac9a7ad838ee` initially exposed one current-family transition seam before product validation: `ACTIVE_FAMILY_CONTRACT.json` still named completed ODL. The changed head `0cb642a6a0a99998be6c59d29cab6ee23b037e65` transitioned only the validation family to SCL while sealing ODL-09 at application baseline `f0fbab87d41e8962faf092da3599913d919ce6a5` and keeping historical profiles inert.

That exact changed head established genuine RED in run `33664542491`: selector/repository health passed and selected exactly one SCL-01 profile; self-hosted Linux and Windows both failed at the intended `client-typecheck` boundary while production contract/panel were absent; both generated matching deterministic receipt `8d7e62a6c34fe33e2f3264a9b07dd56c943e943201b5a86f4e1fa8f0efd397a0`; deterministic comparison passed. No historical predecessor profile ran.

The production contract and accessible panel then landed atomically at head `065d3a92429ee19431067b558f6181a7182f971b`. The first complete production head passed the full SCL-01 profile on self-hosted Linux and Windows plus deterministic comparison in run `33664804272`, with receipt `9d74f2ad2fddc9bef729938764acb6de775028fe26d0d02b198b6ca9e007555a`. There were zero application feature-repair cycles and zero unchanged-evidence reruns.

Application PR `385` was squash-merged as `5c1188e5608e7d4c98de762dffece7ee37b6d9fe`.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — completed_verified.
2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model** — selected_not_started.  
   Define reusable unit/formation profiles, membership, composition, capabilities, readiness, equipment/vehicle references and derived projections without duplicating member truth. Explicitly distinguish canonical constituent state from aggregate projection state.
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

- Ordinary Combat/Action/Event truth remains canonical.
- SCL-01 source inventory, scale taxonomy and owner authority map remain frozen completed authority.
- Units/formations are governed projections/aggregates over canonical members/assets, not duplicate Characters, inventories or owner-domain truth.
- Constituent identity persists across scale; aggregation/projection cannot silently fork authoritative state.
- Aggregate resolution cannot create double damage, duplicate casualties or hidden authority shortcuts.
- Organization/faction/settlement/economy/world consequences commit only through their owning domains.
- AI may advise future command decisions where separately governed but never issues authoritative orders or adjudicates outcomes.
- SCL-02 selection grants no unit/profile implementation, command/order mechanics, strategic resolution, owner mutation, persistence, migration `0022`, provider activation, tester distribution, release or deployment.
