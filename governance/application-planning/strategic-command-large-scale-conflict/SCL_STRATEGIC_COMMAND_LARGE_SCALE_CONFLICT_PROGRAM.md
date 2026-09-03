# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-05; SCL-06 IN PROGRESS  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-05 are `completed_verified`. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — was governed-started by owner `Continue` from exact AIOC authority `79b53bd01e985c469f25ecf873a987eb6f59316f` and exact application baseline `ca951f2283939e196bab55088cd6ec078eeb87f4` on `integration/scl-06-logistics-supply-fatigue-reinforcement-readiness`. The intervening CORE-26 governance reconciliation explicitly preserved SCL-06 as the strategic-command successor and changed no application baseline.

## Frozen SCL-05 contract

The retained `Squad & Fleet.PDF` source profile supports explicit morale checks triggered by `hp-loss-over-50-percent`, `fleet-commander-loss`, and `ambush-first-round-hp-loss-25-percent`. A source-profile check uses an explicit visible d20 plus explicit Leadership modifier against source DC 15 plus only explicit visible battlefield adjustment. SCL-05 generates no random roll.

Failed morale preserves reduced-efficiency and retreat as owner-domain consequence references but SCL-05 never chooses or executes either. Incomplete source morale-point statements remain reference-only because initial/max/accumulation semantics are unresolved; no universal morale pool exists. ODL-03 organization cohesion remains canonical, tactical cohesion is explicit profile/context evidence only, ODL-04/SCL-03 roles do not manufacture Leadership modifiers, and the source supplies no universal discipline scale/check/threshold/consequence.

MIB-09 Relationship/Reputation, Character-Actors, DPL-12, Permission/visibility and ordinary Action/Combat/Event owners remain authoritative. SCL-05 performs no owner mutation, downstream consequence execution, duplicate ledger, persistence, migration `0022`, autonomous AI command or adjudication.

## Governed SCL-06 source and authority contract

The retained `Squad & Fleet.PDF` is source-profile evidence, not a new owner ledger. Its relevant SCL-06 statements include battle-support repair/resupply, Repair Drone, Emergency Repairs, post-combat repair supplies, attrition language and delayed-reinforcement scenario context. Those statements are preserved as explicit references and owner-domain handoff candidates; SCL-06 does not silently expand them into universal resource, fatigue, reinforcement or readiness mechanics.

SCL-06 defines evidence states `resolved`, `unknown`, `conflict`, `incompatible` and observation kinds `supply`, `fatigue`, `reinforcement`, `readiness`, `repair-support`, `resupply-support`. Readiness reuses the completed SCL-02 vocabulary `unknown`, `unready`, `limited`, `ready`.

### Supply, repair and resupply boundary

Supply exists here only as explicit visible owner/profile evidence carrying canonical D17 Asset/inventory/resource references. SCL-06 consumes, transfers, reserves, prices, settles, fabricates and infers no quantity or capacity.

Repair Drone, Emergency Repairs, battle-support repair and post-combat repair-supply text remain read-only support/handoff references. SCL-06 restores no HP and changes no damage. Canonical Combat/Asset owners and SCL-09 retain damage/repair/recovery execution.

Source resupply is a read-only Action/resource handoff candidate. It does not transfer Assets, consume resources or settle Economy state in SCL-06.

### Fatigue, reinforcement and readiness boundary

The retained source supplies no general fatigue meter, threshold, accumulation, recovery or modifier formula. Character-Actors/Condition and separately governed profiles remain authoritative. SCL-06 may expose explicit visible fatigue evidence state and provenance only; it invents no universal fatigue mechanic.

The source mentions delayed reinforcements as scenario context but supplies no arrival formula. SCL-06 may project explicit visible reinforcement references and evidence states only. It never spawns units, chooses arrival, advances campaign time, inserts reinforcements into Combat or reveals hidden reinforcement existence/cardinality.

Readiness resolves only from explicit visible owner/profile evidence. It is never auto-derived from supply, fatigue, reinforcement, morale, formation size or hidden evidence.

### Owner and visibility boundary

D17 Asset/inventory, MIB-13 Economy, APW/D26 Project/task/campaign time, Character-Actors/Condition, A6 Action, A7 Combat, Event, World/location and Permission/visibility remain canonical. SCL-06 performs no owner mutation.

Permission/visibility filtering occurs before observation inclusion, state, readiness, counts, summaries, search, provenance, deterministic receipts, handoffs or AI context. Hidden existence and hidden cardinality remain undisclosed. Missing, unknown, conflicting and incompatible visible evidence remains conservative and is never auto-reconciled.

Stable observation ids and explicit owner/profile/context/provenance/handoff references determine deterministic ordering. Presentation prose and hidden evidence are excluded from receipt truth.

SCL-07 retains terrain/objectives/zones/sieges/strategic position, SCL-08 fleet operational integration, SCL-09 casualty/damage/repair/recovery reconciliation and SCL-10 strategic consequence commits. AI may advise only where separately governed; SCL-06 invokes no provider and grants no autonomous command, logistics allocation, reinforcement timing, adjudication, permission or owner-mutation authority. No durable SCL-06 ledger is introduced and migration `0022` remains unreserved.

## Acceptance-first TDD contract

The first application mutation must contain only the SCL-06 acceptance regression, governed proof, exactly one SCL-06 Validation Core profile and invariant verifier. The production contract `logistics-supply-fatigue-reinforcement-readiness.ts` and accessible panel `SclLogisticsSupplyFatigueReinforcementReadinessPanel.tsx` must remain absent until genuine RED is established.

The RED candidate must pass SCL-06 invariants and workspace installation on self-hosted Linux and Windows, then fail at client typecheck because only the production contract/panel are missing. Deterministic cross-platform comparison must agree on that failure. The first complete production candidate must pass exactly one current-family SCL-06 profile on self-hosted Linux and Windows plus deterministic comparison with zero historical predecessor profile fanout.

## SCL-05 validation evidence

SCL-05 governed start: AIOC PR `884`, exact head `90f7874c5778c4551fdd2514f3d5da7a435c63bc`, Repository Health run `33709259744`, job `100505056306`, merge `e299932972adc299e49d66d6e1b8c333f92acb16`.

Genuine acceptance-first RED: head `cb3a18e14d5f2aba0df234af3f213de4e6d56898`, run `33709453598`, selector `100505624413`, Linux `100505647759`, Windows `100505647686`, comparator `100505752096`, deterministic receipt `7e0fce758d5d5711a0381f02291b9145c9d526c1c0f38587b1f594eab2d20898`.

Final exact head `4d4f54cda9ca71d838c0853e182801de53b4742d` passed run `33709758216`: selector/repository health `100506522988`, Linux `100506549414`, Windows `100506549403`, comparator `100506661891`, receipt `a1a967d08a7106dfeaacec0ce3ec09323e9232f066039dbbfa66d9f3ad8849d4`. Historical predecessor profile fanout was zero. One validation-contract repair corrected three missing acceptance-test closing parentheses; application feature repairs remained zero.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — in_progress under bounded implementation authority.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — planned.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — planned.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — planned.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — planned.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

SCL-06 must remain within the sealed contract above and must complete acceptance-first RED, bounded production implementation, exact-head self-hosted Linux/Windows GREEN, deterministic comparison, application merge and governed closeout before SCL-07 can be selected. SCL-07+, MAL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
