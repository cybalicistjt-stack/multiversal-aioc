# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-07; SCL-08 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-07 are `completed_verified`. SCL-07 merged to application main as `154a72bbcabfe6fe21a99e219ef1afe1863bb061` after genuine cross-platform RED and exact-head self-hosted Linux/Windows GREEN. Strict successor SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — is `selected_not_started` from that exact application baseline with no implementation branch and no implementation authority.

## Frozen SCL-07 contract

Retained source `MV_Master_01_Core/02_PDF_Sources/P3/Rules/Squad & Fleet.PDF`, SHA-256 `20d7a5bbeafb7fccf2213aee5470741cb35760270907ff56e075f86ee83ae8da`, supplies explicit terrain references: Nebula halves speed and grants stealth bonuses; Asteroid Field requires evasion rolls at DC 12–18 to avoid collision. Its all-out-battle example includes objective references for destroying the flagship, reducing morale to 0, or retreat.

SCL-07 projects visible owner-backed `terrain`, `zone`, `objective`, `siege`, and `strategic-position` records using evidence states `resolved`, `unknown`, `conflict`, and `incompatible`. Source terrain profiles are `nebula` and `asteroid-field`. These are read-only source/effect or objective references and owner-domain handoffs; SCL-07 never mechanically applies terrain effects, resolves evasion/collision, completes objectives, advances sieges, derives strategic advantage, mutates morale, orders retreat, or mutates canonical World/location, Combat/Action/Event, Asset or Organization truth.

The source does not establish a universal terrain catalog/stacking precedence, objective lifecycle/scoring/completion authority, siege clock/breach/attrition/supply formula, or strategic-position advantage derivation formula. Those remain explicit source gaps and are not invented.

Visibility filtering occurs before records, counts, states, source/effect references, objective references, summaries, search, provenance, handoffs, deterministic receipts, or AI context. Hidden existence/cardinality remains undisclosed. Missing, unknown, conflict and incompatible evidence stays conservative. Stable record-ID ordering exists only for deterministic output.

No autonomous AI command/adjudication, owner mutation, duplicate terrain/objective ledger, durable persistence or migration `0022` is authorized. SCL-09 retains casualties/damage/recovery and SCL-10 retains faction/settlement/world/campaign consequences.

## SCL-07 validation evidence

SCL-07 governed start: AIOC PR `891`. Initial exact candidate exposed `MVHEALTH-CONVERGENCE-RETRY`; one bounded validation-contract repair removed the non-null first-start retry basis. Repaired exact head `02648feb95293e017ee918c561b7e6156956c872` passed Repository Health run `33747516222`, job `100623309115`, and merged as `ff3a114b2654f56c6ca487ffeaf275ca6dfa852e`.

Genuine acceptance-first RED: head `f79830902e42fc7bdf08914b5afdaf2d04a45285`, run `33747846184`, selector `100624355837`, Linux `100624393021`, Windows `100624393011`, comparator `100624584428`, deterministic receipt `a7adf7e74d960ae15b7f8eeb2f4c75cf7802025662e9b99bc2e4bdd17e0fdf6e`.

Final exact head `90f5b08f900b76dd73ac505272be8911f0b92f42` passed run `33748097329`: selector/repository health `100625146148`, Linux `100625182245`, Windows `100625182292`, comparator `100625349354`, receipt `cd2323ae15e7b909a45dfd977b2bbce7198ddfc26f7317c28683b6a75a79c97a`. Historical predecessor profile fanout was zero. Application feature repairs were zero; one validation-contract repair occurred at governed start.

Application PR `391` merged as `154a72bbcabfe6fe21a99e219ef1afe1863bb061`.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — completed_verified.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — completed_verified.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — selected_not_started; no branch or authority.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — planned.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — planned.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

A future owner Continue must perform one bounded SCL-08 governed-start recovery pass from exact application main `154a72bbcabfe6fe21a99e219ef1afe1863bb061` before any vehicle, mecha, ship or fleet-integration product mutation. SCL-09+, MAL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
