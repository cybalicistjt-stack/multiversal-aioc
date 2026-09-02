# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-03; SCL-04 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-03 are `completed_verified`. SCL-03 completed on application PR `387`, exact validated head `d66d150107b7e27e3cd266d6da42c5ee686abc2a`, validation run `33678334569`, deterministic receipt `95314bbd572d973ad8856fa97031e78abc7278d6e863833cd418ba126fa3ff33`, zero historical predecessor fanout, zero application feature-repair cycles, and application merge `a4913b3cb162c0c05e4efaf7a98b856f7d57c92a`.

SCL-04 — Command Phases & Deterministic Order Resolution — is the strict successor and is `selected_not_started` from exact application main `a4913b3cb162c0c05e4efaf7a98b856f7d57c92a`. It has no implementation branch and no implementation authority.

## Frozen SCL-01/SCL-02 contracts

SCL-01 remains authoritative for source/scale/owner-domain routing, visibility-first filtering, identity-preserving projection and the scale vocabulary `individual`, `squad`, `unit`, `formation`, `force`, `theater`.

SCL-02 remains authoritative for reusable `squad`, `unit`, `formation`, `fleet`, and `army` profile projections, explicit canonical leaf identity, visible composition/capability/readiness/equipment/platform references and conservative unresolved evidence. It creates no command or resolution authority.

## Frozen SCL-03 contract

SCL-03 defines read-only command relationship, explicit ODL-04-backed delegation, order intent/lifecycle and descriptive communication projections. Relationship roles are `commander`, `subordinate`, `staff`, `liaison`. Order types are `directive`, `task`, `constraint`, `coordination`; lifecycle is `proposed`, `issued`, `acknowledged`, `received`, `superseded`, `cancelled`. Communication range bands are `unknown`, `local`, `linked`, `remote`; delay bands are `unknown`, `none`, `delayed`, `extended`; states are `available`, `delayed`, `interrupted`, `unknown`.

Permission/visibility filtering precedes command/order/communication existence, counts, summaries, provenance, receipts or AI context. Missing, unknown, conflict and incompatible visible evidence remains unresolved. SCL-03 performs no order issuance mutation, delegated Action execution, mechanical resolution, owner mutation, AI command/adjudication, persistence or migration.

## SCL-04 selection boundary

SCL-04 is selected only. This selection intentionally does **not** decide or implement the exact phase vocabulary, order eligibility/precedence, simultaneous/conflicting order treatment, deterministic resolution inputs/outputs, partial/blocked/invalid outcomes, canonical Action/Combat/Event handoffs or receipt contract. Those semantics must be resolved during the next bounded governed-start pass from the exact application baseline.

SCL-04 may later own command-phase and deterministic order-resolution coordination while ordinary Action/Combat/Event truth remains canonical and may not be duplicated or double-applied. SCL-05/SCL-06 retain morale/logistics mechanics, SCL-08 fleet/platform integration, SCL-09 casualty/damage reconciliation and SCL-10 strategic consequences.

No autonomous AI command/adjudication, owner mutation, system permission, hidden-data reveal, persistence, migration `0022`, provider activation, tester distribution, release or deployment is authorized by SCL-04 selection.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — completed_verified.
2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model** — completed_verified.
3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication** — completed_verified.
4. **SCL-04 — Command Phases & Deterministic Order Resolution** — selected_not_started; future owner Continue required.
5. **SCL-05 — Morale, Cohesion, Leadership & Discipline** — planned.
6. **SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness** — planned.
7. **SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position** — planned.
8. **SCL-08 — Vehicle, Mecha, Ship & Fleet Integration** — planned.
9. **SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery** — planned.
10. **SCL-10 — Faction, Settlement, World & Campaign Consequence Integration** — planned.
11. **SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof** — planned.

## Invariants

- Ordinary Action/Combat/Event and canonical constituent/owner-domain truth remain authoritative.
- SCL-01 through SCL-03 remain frozen with retired implementation authority.
- SCL-04 is selected without implementation authority or an implementation branch.
- No AI autonomous command/adjudication, owner mutation, hidden-data reveal, duplicate ledger, persistence or migration `0022` is authorized.
