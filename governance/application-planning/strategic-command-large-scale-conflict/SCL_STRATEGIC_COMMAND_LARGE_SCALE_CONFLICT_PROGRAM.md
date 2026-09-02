# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-02; SCL-03 IN PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 and SCL-02 remain `completed_verified`. SCL-02 application merge is `e7821465a60a9508b993e941ebe9f1c48144b90f`.

SCL-03 — Command Hierarchy, Roles, Orders & Communication — is `in_progress` from exact application main `e7821465a60a9508b993e941ebe9f1c48144b90f` on `integration/scl-03-command-hierarchy-orders-communication` with one bounded implementation authority.

## Frozen predecessor contracts

SCL-01 remains authoritative for source/scale/owner-domain routing, visibility-first filtering, identity-preserving projection and the scale vocabulary `individual`, `squad`, `unit`, `formation`, `force`, `theater`.

SCL-02 remains authoritative for reusable `squad`, `unit`, `formation`, `fleet`, and `army` profile projections, explicit canonical leaf identity, visible composition/capability/readiness/equipment/platform references and conservative unknown/conflict handling. It creates no command authority or mechanics.

ODL-04 remains authoritative for explicit organization role, delegation, authority-scope and communication owner evidence. Those records are descriptive owner evidence and do not themselves grant system permission, Action authority or SCL mechanical command resolution.

## SCL-03 governed contract

SCL-03 defines read-only command-relationship, order-lifecycle and communication projections over explicit visible predecessor evidence.

Relationship roles are `commander`, `subordinate`, `staff`, and `liaison`. They are SCL projection roles only and do not assign canonical ODL roles, ownership, Permission or Action authority. Delegated command scope must cite explicit visible ODL-04 role/delegation/authority-scope owner evidence; missing or conflicting evidence remains unresolved.

Order types are `directive`, `task`, `constraint`, and `coordination`. Lifecycle vocabulary is `proposed`, `issued`, `acknowledged`, `received`, `superseded`, `cancelled`. SCL-03 may represent existing visible intent/lifecycle evidence but performs no issuance mutation, delegated Action execution, Combat/Event resolution or outcome adjudication. SCL-04 retains mechanical/deterministic order resolution.

Communication range bands are `unknown`, `local`, `linked`, `remote`; delay bands are `unknown`, `none`, `delayed`, `extended`; communication states are `available`, `delayed`, `interrupted`, `unknown`. These are descriptive projections only and create no travel-time, action-cost, initiative, morale, logistics or resolution effect.

Permission/visibility filtering occurs before command relationship, delegation scope, order existence/state, communication existence/state, counts, summaries, search text, provenance, deterministic receipts or AI context. Hidden existence and cardinality remain undisclosed. Missing, unknown, conflict or incompatible visible evidence is never guessed or auto-reconciled.

Stable relationship-id, order-id, communication-id and canonical-reference ordering determines projection and receipt truth. AI may advise only where separately governed; SCL-03 grants no autonomous command, order issuance, adjudication, Permission, owner mutation or completion authority. No durable SCL-03 ledger or migration `0022` is authorized.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — completed_verified.
2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model** — completed_verified.
3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication** — in_progress.
4. **SCL-04 — Command Phases & Deterministic Order Resolution** — planned.
5. **SCL-05 — Morale, Cohesion, Leadership & Discipline** — planned.
6. **SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness** — planned.
7. **SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position** — planned.
8. **SCL-08 — Vehicle, Mecha, Ship & Fleet Integration** — planned.
9. **SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery** — planned.
10. **SCL-10 — Faction, Settlement, World & Campaign Consequence Integration** — planned.
11. **SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof** — planned.

## Invariants

- Ordinary Action/Combat/Event and canonical constituent/owner-domain truth remain authoritative.
- SCL-01 and SCL-02 remain frozen with retired implementation authority.
- ODL-04 and Permission/visibility remain authoritative for their own owner evidence.
- SCL-03 is read-only command intent/relationship/communication projection; SCL-04 retains mechanical resolution.
- No AI autonomous command/adjudication, owner mutation, hidden-data reveal, duplicate ledger, persistence or migration `0022` is authorized.
