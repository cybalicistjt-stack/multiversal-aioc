# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-05; SCL-06 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-05 are `completed_verified`. SCL-05 merged to application main as `ca951f2283939e196bab55088cd6ec078eeb87f4` after exact-head self-hosted Linux/Windows validation and deterministic comparison. Strict successor SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — is `selected_not_started` from that exact application baseline with no implementation branch and no implementation authority.

## Frozen SCL-05 contract

The retained `Squad & Fleet.PDF` source profile supports explicit morale checks triggered by `hp-loss-over-50-percent`, `fleet-commander-loss`, and `ambush-first-round-hp-loss-25-percent`. A source-profile check uses an explicit visible d20 plus explicit Leadership modifier against source DC 15 plus only explicit visible battlefield adjustment. SCL-05 generates no random roll.

Failed morale preserves reduced-efficiency and retreat as owner-domain consequence references but SCL-05 never chooses or executes either. Incomplete source morale-point statements remain reference-only because initial/max/accumulation semantics are unresolved; no universal morale pool exists. ODL-03 organization cohesion remains canonical, tactical cohesion is explicit profile/context evidence only, ODL-04/SCL-03 roles do not manufacture Leadership modifiers, and the source supplies no universal discipline scale/check/threshold/consequence.

MIB-09 Relationship/Reputation, Character-Actors, DPL-12, Permission/visibility and ordinary Action/Combat/Event owners remain authoritative. SCL-05 performs no owner mutation, downstream consequence execution, duplicate ledger, persistence, migration `0022`, autonomous AI command or adjudication.

## Validation evidence

SCL-05 governed start: AIOC PR `884`, exact head `90f7874c5778c4551fdd2514f3d5da7a435c63bc`, Repository Health run `33709259744`, job `100505056306`, merge `e299932972adc299e49d66d6e1b8c333f92acb16`.

Genuine acceptance-first RED: head `cb3a18e14d5f2aba0df234af3f213de4e6d56898`, run `33709453598`, selector `100505624413`, Linux `100505647759`, Windows `100505647686`, comparator `100505752096`, deterministic receipt `7e0fce758d5d5711a0381f02291b9145c9d526c1c0f38587b1f594eab2d20898`.

Final exact head `4d4f54cda9ca71d838c0853e182801de53b4742d` passed run `33709758216`: selector/repository health `100506522988`, Linux `100506549414`, Windows `100506549403`, comparator `100506661891`, receipt `a1a967d08a7106dfeaacec0ce3ec09323e9232f066039dbbfa66d9f3ad8849d4`. Historical predecessor profile fanout was zero. One validation-contract repair corrected three missing acceptance-test closing parentheses; application feature repairs remained zero.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — selected_not_started; no branch or authority.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — planned.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — planned.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — planned.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — planned.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

A future owner Continue must perform one bounded SCL-06 governed-start recovery pass from exact application main `ca951f2283939e196bab55088cd6ec078eeb87f4` before any logistics, supply, fatigue, reinforcement or readiness product mutation. SCL-07+, MAL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
