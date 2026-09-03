# SCL — Strategic Command & Large-Scale Conflict

**Program ID:** SCL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH SCL-08; SCL-09 SELECTED_NOT_STARTED  
**Activation:** after completed_verified ODL-09  
**Successor:** MAL-01  
**Owner and final authority:** John Brandon Turner

## Current state

SCL-01 through SCL-08 are `completed_verified`. SCL-08 merged to application main as `1de481381d0d65d3a88d0e1cdc1af77ebe73dfb6` after genuine cross-platform acceptance RED and first-production exact-head self-hosted Linux/Windows GREEN with zero feature or validation-contract repairs. Strict successor SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — is `selected_not_started` from that exact application baseline with no implementation branch and no implementation authority.

## Frozen SCL-08 contract

SCL-08 is a visibility-first deterministic read-only integration projection. It links explicit SCL profile/membership identity to canonical F008 Asset Instances and F014 Vehicle Operations, optional operational class/state, explicit crew/station actor and authority references, optional explicit flagship/command reference, and visible command/resource/position/handoff/nested-Asset/owner/provenance references.

Integration kinds are `vehicle`, `mecha`, `ship`. Evidence states are `resolved`, `unknown`, `conflict`, `incompatible`. F014 operational classes are `ground`, `water`, `air`, `space`, `submersible`, `walker`, `mecha`, `mount`, `hybrid`, `abstract`. Stations remain the canonical F014 station vocabulary.

Ownership, custody, control, access and station authority remain distinct. Actor/crew identity remains separate from machine Asset identity. SCL-08 never merges actor and machine state or infers actor damage from vehicle/mecha damage.

Retained `Squad & Fleet.PDF` source language describing a squad as 1–5 ships and a fleet led by a flagship/command ship is preserved as explicit source evidence only. It does not replace SCL-01/SCL-02 taxonomy, impose a universal numeric cap, or auto-select/infer a flagship.

Carried craft, cargo, passengers and nested Assets keep separate identity. Command/resource/position references are read-only handoffs. SCL-08 does not issue/resolve orders, move/place Assets, consume Resources, apply Action/Combat effects, transfer ownership/control, or mutate nested children.

SCL-09 owns casualty/damage/recovery reconciliation. SCL-08 performs no cross-asset, crew, passenger, nested-craft, squad or fleet damage/casualty propagation. SCL-10 retains strategic consequences.

Visibility filters before integration rows, crew/station rosters, fleet bindings, counts, classes, states, source references, summaries, search, provenance, handoffs, deterministic receipts or AI context. Missing/source-unspecified/unknown/conflict/incompatible evidence remains conservative. Hidden existence/cardinality is undisclosed.

No owner mutation, autonomous AI command/adjudication, duplicate vehicle/fleet ledger, durable persistence or migration `0022` was introduced.

## SCL-08 validation evidence

Governed start: AIOC PR `897`, exact head `46f6124ed8502067129b2c5b017fa7e034556389`, Repository Health run `33751788835`, job `100636762296`, merged as `84ba98673cfb3e853dd3789bf1fce0f753450157` with zero repairs.

Genuine acceptance-first RED: head `3c988221d684094946d9fc73a77d8ab3ecd37e24`, run `33752103675`, selector `100637776879`, Linux `100637813669`, Windows `100637813587`, comparator `100637978759`, deterministic receipt `ced84fabe9a801e001ed09193bb9ac6a05858f926191b35003f3c8b7b305062a`.

First production head `16f4b1eded3ae90c577184b2dc84cce9feff67bd` passed run `33752347595`: selector/repository health `100638564408`, Linux `100638603430`, Windows `100638603596`, comparator `100638773125`, receipt `d0defc9bfd6f544cd0b2e69d0d7ac1bd13d93d103977297223cf5a8f1460d7be`. Historical predecessor profile fanout was zero. Application feature repairs and validation-contract repairs were both zero.

Application PR `392` merged as `1de481381d0d65d3a88d0e1cdc1af77ebe73dfb6`.

## Tranches

1. SCL-01 — Source Inventory, Scale Taxonomy & Authority Map — completed_verified.
2. SCL-02 — Unit, Formation, Squad, Fleet & Army Definition Model — completed_verified.
3. SCL-03 — Command Hierarchy, Roles, Orders & Communication — completed_verified.
4. SCL-04 — Command Phases & Deterministic Order Resolution — completed_verified.
5. SCL-05 — Morale, Cohesion, Leadership & Discipline — completed_verified.
6. SCL-06 — Logistics, Supply, Fatigue, Reinforcement & Readiness — completed_verified.
7. SCL-07 — Terrain, Objectives, Zones, Sieges & Strategic Position — completed_verified.
8. SCL-08 — Vehicle, Mecha, Ship & Fleet Integration — completed_verified.
9. SCL-09 — Individual-to-Unit Effects, Casualties, Damage & Recovery — selected_not_started; no branch or authority.
10. SCL-10 — Faction, Settlement, World & Campaign Consequence Integration — planned.
11. SCL-11 — Workbench, Scenario Packs, Balance & Cross-Scale Golden Proof — planned.

## Current invariant

A future owner Continue must perform one bounded SCL-09 governed-start recovery pass from exact application main `1de481381d0d65d3a88d0e1cdc1af77ebe73dfb6` before any individual-to-unit effect, casualty, damage or recovery product mutation. SCL-10+, MAL-01+, provider activation, tester distribution, release and deployment remain unauthorized.
