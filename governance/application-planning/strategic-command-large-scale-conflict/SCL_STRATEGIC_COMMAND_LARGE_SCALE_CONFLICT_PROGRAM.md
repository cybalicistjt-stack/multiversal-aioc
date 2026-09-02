# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-02; SCL-03 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — remains `completed_verified` on application merge `5c1188e5608e7d4c98de762dffece7ee37b6d9fe`.

SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — is `completed_verified` on application PR `386`, validated head `b30cc7a74ce41694f49940d41b978320d9cc6efa`, validation run `33668999903`, deterministic receipt `24f3be5720f1bc9898959bf7dae3cc3c57f4f127ae8aedf7fd69915e9aedf98c`, zero historical predecessor fanout, zero application feature-repair cycles, and application merge `e7821465a60a9508b993e941ebe9f1c48144b90f`.

SCL-03 — Command Hierarchy, Roles, Orders & Communication — is the strict successor and is `selected_not_started` from exact application main `e7821465a60a9508b993e941ebe9f1c48144b90f`. It has no implementation branch and no implementation authority. A future owner `Continue` is required before governed start and any application mutation.

## Frozen SCL-01 contract

SCL-01 remains authoritative for the source inventory, owner authority map, the scale vocabulary `individual`, `squad`, `unit`, `formation`, `force`, `theater`, visibility-first filtering and identity-preserving up-scale projection. Scale labels are coordination/aggregation roles, not universal numeric size caps. Projections carry explicit canonical constituent ids, owner references and provenance and cannot copy or fork canonical owner-domain state.

## Frozen SCL-02 contract

SCL-02 defines reusable read-only profile projections for `squad`, `unit`, `formation`, `fleet`, and `army`. The scale mapping is `squad→squad`, `unit→unit`, `formation→formation`, and both `fleet→force` and `army→force`.

Visible membership retains a stable membership id, owning profile id, member kind, member reference, explicit canonical leaf constituent ids, role tags, owner references, provenance and authorization. Member kinds are `character`, `creature`, `asset`, `platform`, and `projected-group`. Nested projected groups are valid only when explicit leaf canonical constituent identity remains retained; aggregate profile ids never substitute for leaf identity and duplicate visible leaf membership makes the projection incomplete.

Capability tags are explicit visible derived labels only and create no numeric combat power or mechanical bonuses. Readiness vocabulary is `unknown`, `unready`, `limited`, `ready`; readiness is descriptive projection only, with no thresholds or effects. Equipment and platform references remain canonical D17/MIB-14 references and copy no Asset, inventory, vehicle/platform, damage, fuel or maintenance truth.

MV-IA-F020 authorization is applied before membership, counts, composition, capabilities, readiness, equipment/platform references, search, provenance, receipts or AI context. Hidden existence/cardinality remain undisclosed. Missing, `unknown`, `conflict` and `incompatible` visible evidence remains incomplete and is never guessed or auto-reconciled.

SCL-02 creates no command hierarchy/order, resolution, morale/logistics effects, casualty/damage application, strategic consequence, owner mutation, AI command/adjudication, duplicate owner ledger or durable persistence. Migration `0022` remains unreserved.

## SCL-03 selection boundary

SCL-03 is selected only. This selection intentionally does **not** decide or implement the exact commander/subordinate role vocabulary, delegation and command-capacity representation, order lifecycle/types, communication range/delay/interruption representation, permission model or deterministic receipt contract. Those semantics must be resolved during the next bounded governed-start pass from the exact application baseline.

SCL-03 may later own command hierarchy, roles, orders and communication, but SCL-04 retains mechanical/deterministic order resolution and outcome adjudication. SCL-05/SCL-06 retain morale/logistics mechanics, SCL-08 fleet/platform integration, SCL-09 casualty/damage reconciliation and SCL-10 strategic consequences.

No autonomous AI command, owner mutation, system permission, hidden-data reveal, persistence, migration `0022`, provider activation, tester distribution, release or deployment is authorized by SCL-03 selection.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — completed_verified.
2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model** — completed_verified.
3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication** — selected_not_started; future owner Continue required.
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
- SCL-01 and SCL-02 completed contracts remain frozen and their implementation authority is retired.
- SCL-03 is selected without implementation authority or an implementation branch.
- Mechanical order resolution remains SCL-04.
- No AI autonomous command/adjudication, owner mutation, hidden-data reveal, duplicate ledger, persistence or migration `0022` is authorized.
