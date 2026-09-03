# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-04; SCL-05 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-04 are `completed_verified`. SCL-04 — Command Phases & Deterministic Order Resolution — completed on application PR `388`, validated head `b40318b0adb0be3c64d91ec0cdd5260f9bed3347`, validation run `33685813220`, deterministic receipt `faf79a5bb2fec8c08003fa3426899f0ead040394eb3992e484a314998456cbed`, zero historical predecessor fanout, zero application feature-repair cycles, and application merge `f85be31982530f5fcc9d8ef9b9ef25e30451923e`.

SCL-05 — Morale, Cohesion, Leadership & Discipline — is the strict successor and is `selected_not_started` from exact application main `f85be31982530f5fcc9d8ef9b9ef25e30451923e`. It has no implementation branch and no implementation authority. A future owner `Continue` is required before governed start and any application mutation.

## Frozen SCL-04 contract

SCL-04 freezes phase vocabulary `intake`, `eligibility`, `precedence`, `resolution`, `handoff`, `closed` and outcome vocabulary `ready`, `partial`, `blocked`, `invalid`, `conflict`. Handoff domains are `action`, `combat`, `event`.

SCL-04 defines no implicit order-type priority hierarchy. Only explicit visible dependency, supersession and conflict references affect precedence; independent orders use stable order-id ordering solely for deterministic receipts. Missing dependencies block. Cycles and unresolved explicit conflicts remain conflict and never auto-select a winner.

SCL-04 coordinates order outcomes and owner-domain handoff requests only. Canonical Action, Combat and Event domains execute and commit results. SCL-04 does not execute Action, apply Combat effects, commit Event outcomes, advance campaign time or create replayable duplicate outcome truth. Permission/visibility filters before graph evaluation, outcomes, counts, search, provenance and deterministic receipts; hidden existence and cardinality remain undisclosed.

## SCL-05 selection boundary

SCL-05 is selected only. This selection intentionally does not decide or implement the exact morale/cohesion/discipline vocabularies, leadership influence model, evidence states, triggers, recovery, thresholds, mechanical effects, or owner-domain handoffs. Those semantics must be resolved during the next bounded governed-start pass from the exact application baseline.

SCL-05 may later own bounded morale, cohesion, leadership and discipline semantics. SCL-06 retains logistics, supply, fatigue, reinforcement and readiness mechanics. SCL-07 retains terrain/objectives, SCL-08 vehicle/fleet integration, SCL-09 casualty/damage recovery and SCL-10 strategic consequences.

No autonomous AI command/adjudication, owner mutation, system permission, hidden-data reveal, persistence, migration `0022`, provider activation, tester distribution, release or deployment is authorized by SCL-05 selection.

## Tranches

1. **SCL-01 — Source Inventory, Scale Taxonomy & Authority Map** — completed_verified.
2. **SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model** — completed_verified.
3. **SCL-03 — Command Hierarchy, Roles, Orders & Communication** — completed_verified.
4. **SCL-04 — Command Phases & Deterministic Order Resolution** — completed_verified.
5. **SCL-05 — Morale, Cohesion, Leadership & Discipline** — selected_not_started; future owner Continue required.
6. **SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness** — planned.
7. **SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position** — planned.
8. **SCL-08 — Vehicle, Mecha, Ship & Fleet Integration** — planned.
9. **SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery** — planned.
10. **SCL-10 — Faction, Settlement, World & Campaign Consequence Integration** — planned.
11. **SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof** — planned.

## Invariants

- Ordinary Combat/Action/Event and canonical constituent/owner-domain truth remain authoritative.
- SCL-01 through SCL-04 completed contracts remain frozen and implementation authority is retired.
- SCL-05 is selected without implementation authority or an implementation branch.
- Logistics/readiness mechanics remain SCL-06.
- No AI autonomous command/adjudication, owner mutation, hidden-data reveal, duplicate ledger, persistence or migration `0022` is authorized.
