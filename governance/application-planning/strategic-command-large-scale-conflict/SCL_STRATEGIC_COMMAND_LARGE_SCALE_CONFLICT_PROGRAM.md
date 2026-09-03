# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-06; SCL-07 IN_PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-06 are `completed_verified`. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — is governed-started `in_progress` from exact application baseline `92821565cfc0035059c15808c265411b4d419157` on branch `integration/scl-07-terrain-objectives-zones-sieges-strategic-position` with bounded implementation authority only for the contract below.

## Frozen SCL-06 contract

SCL-06 provides visibility-first deterministic projection of explicit owner-backed logistics/readiness observations with states `resolved`, `unknown`, `conflict`, and `incompatible`. Supported observation kinds are `supply`, `fatigue`, `reinforcement`, `readiness`, `repair-support`, and `resupply-support`. Readiness remains descriptive only using `unknown`, `unready`, `limited`, and `ready`.

The projection preserves read-only owner-domain references and support handoffs. It does not consume or transfer Asset/inventory resources, settle Economy state, apply HP repair, commit reinforcement arrival, advance campaign time, auto-derive readiness, reveal hidden data, mutate canonical owner state, create a duplicate logistics ledger, add durable persistence, reserve migration `0022`, or grant autonomous AI command/adjudication.

## Governed SCL-07 contract

The bounded source pass uses retained `MV_Master_01_Core/02_PDF_Sources/P3/Rules/Squad & Fleet.PDF`, SHA-256 `20d7a5bbeafb7fccf2213aee5470741cb35760270907ff56e075f86ee83ae8da`, plus completed SCL-01..06 and only the canonical World/location, Combat/Action/Event, Asset, Organization and Permission/visibility owner seams needed for SCL-07.

The retained source says some zones may affect movement. A **Nebula** halves speed and grants stealth bonuses. An **Asteroid Field** requires evasion rolls at DC 12–18 to avoid collision. Its defense scenario says terrain such as asteroid fields can enhance evasion. Its all-out-battle example gives victory conditions of destroying the flagship, reducing morale to 0, or retreat.

SCL-07 preserves those rules as explicit visible source/effect or objective references and owner-domain handoffs. It does **not** itself halve speed, grant stealth, roll or resolve collision/evasion, enhance evasion, destroy a flagship, change morale, order retreat, complete an objective, or mutate World/Combat/Action/Event/Asset/Organization truth.

SCL-07 record kinds are `terrain`, `zone`, `objective`, `siege`, and `strategic-position`; evidence states are `resolved`, `unknown`, `conflict`, and `incompatible`. Source terrain profiles are `nebula` and `asteroid-field`. Missing authority stays explicit: the source does not establish a universal terrain catalog/stacking precedence, objective lifecycle/scoring/completion authority, siege clock/breach/attrition/supply formula, or strategic-position advantage derivation formula. SCL-07 must not invent any of them.

Visibility filters before record inclusion, counts, state, effect/objective references, summaries, search, provenance, handoffs, deterministic receipts, or AI context. Missing, unknown, conflict, and incompatible evidence stays conservative and is never auto-reconciled. Stable record-ID ordering is deterministic only and grants no priority or authority.

No autonomous AI command/adjudication, owner mutation, hidden-data reveal, duplicate terrain/objective ledger, durable persistence, or migration `0022` is authorized. SCL-08 retains vehicle/mecha/ship/fleet integration; SCL-09 retains casualty/damage/recovery; SCL-10 retains faction/settlement/world/campaign consequences.

## SCL-06 validation evidence

SCL-06 governed start: AIOC PR `887`, exact head `45d5779a094a31d7eeb3f05c57bd5fb51bdc988d`, Repository Health run `33715820108`, job `100524671772`, merge `e9e1fc1fe7945b927a553f193a79651a71128330`.

Genuine acceptance-first RED: head `a126247041b03d8818e92c6271c8a2e6a186b13f`, run `33716002955`, selector `100525209387`, Linux `100525236913`, Windows `100525236904`, comparator `100525340237`, deterministic receipt `5be2448fb6dbdf81e727eb5d8da208efe0b10822031b65f117f4acaa2c8f7f25`.

Final exact head `ee40aa6b4aaa2a8139d0e4e13b29a9671c0f0657` passed run `33716147352`: selector/repository health `100525628839`, Linux `100525651803`, Windows `100525651601`, comparator `100525763815`, receipt `f5eb264313b9a4cb8434e56e8a49a92fafe3d4a8104ba7d6923b01567c309f1b`. Historical predecessor profile fanout was zero. Application feature repairs and validation-contract repairs were both zero.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — completed_verified.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — in_progress; governed branch and authority active.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — planned.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — planned.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — planned.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

No SCL-07 production mutation may precede a genuine acceptance-first current-family RED on the exact application branch. Final validation must use exactly one SCL-07 profile, self-hosted Linux and Windows exact-head validation, deterministic comparison, zero historical predecessor profile fanout, and zero unchanged-evidence reruns. SCL-08+, MAL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
