# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-02; MAL-03 IN_PROGRESS  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 and MAL-02 are `completed_verified`. MAL-02 merged to exact application main `3b8b20916b6390a720fe49ee9685b7ca1ea00238`. Owner `Continue` governed-starts MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives — from that exact baseline on `integration/mal-03-movement-navigation-traversal` with bounded implementation authority.

Parallel ENV/CEW content work and GCL execution remain outside MAL-03 work selection unless a named dependency proves insufficient.

## Frozen MAL-01 contract

Recovered material is provenance/inspiration only; copying proprietary game/ROM logic, data, maps, scripts, audiovisual assets, names, rule tables or level layouts is not authorized. MAL classifications reference canonical owner domains and never create parallel truth. AI remains proposal-only.

## Frozen MAL-02 contract

MAL-02 established device-neutral semantic input intents, deterministic logical timing, ephemeral MAL-local session state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts. Wall-clock/frame-rate/network/device identity are excluded from outcome truth. MAL-local success/failure never commits canonical owner-domain outcomes.

## MAL-03 governed contract

MAL-03 defines original reusable traversal primitives only:

- **Movement modes:** `stationary`, `step`, `continuous-local`, `transition`.
- **Space primitives:** `position`, `room`, `connector`, `threshold`.
- **Door states:** `open`, `closed`, `blocked`, `locked`, `unresolved`.
- **Key-match states:** `not-required`, `authorized-match`, `authorized-mismatch`, `unresolved`.
- **Traversal outcomes:** `remain`, `advance-local`, `transition-ready`, `blocked-local`, `unresolved`.

Movement consumes frozen MAL-02 semantic input intents and deterministic logical ticks. Device bindings, wall-clock time, animation frames, latency and refresh rate never become movement or traversal truth.

Rooms, positions, connectors and thresholds are MAL-local authored interaction projections. When they correspond to canonical locations they bind stable World/Scene references rather than creating a second map, topology, coordinate system or Travel model.

Navigation is an authored local graph of nodes and permitted edges. Source/reference arrays normalize deterministically while explicit traversal order remains authored data. Hidden or unauthorized nodes, connector state, door state and destination state remain unresolved; absence of visible evidence never implies passability.

Doors and thresholds may observe authorized canonical state. Key checks consume authorized canonical item/key reference IDs only. MAL-03 does not create, duplicate, grant, consume, equip, transfer or delete Inventory ownership.

Successful movement changes MAL-local session position/progress only. A boundary crossing may emit a deterministic `transition-ready` result reference for a later owning integration; it does not move a canonical Character, advance Travel, mutate World/Scene, commit an Event or alter Project/progression truth.

Pause/retry and accessibility-equivalent behavior remain governed by MAL-02. AI may propose traversal definitions but cannot invent hidden topology, key possession, passability, destinations or owner-domain outcomes.

MAL-03 does **not** implement conflict/combat, hazards, pickups/objectives/rewards, NPC behavior/state machines, Aniloops, canonical owner mutation, persistence, migration `0022`, tester distribution, release or deployment.

## MAL-02 validation evidence

Governed start AIOC PR `921` merged as `5da9cae5002229ba06a671813f56b1a0b4a564de`. Genuine matching RED used application head `dd3261d3632edb3569669653549bf95168c93588`, run `33794055025`, receipt `e4f8ab5c567c33b5fb3d4461de7b2ef76b4a4040f96efd3a7d6818e290ae12a2`. Exact production head `c337bfc98de15913a5af8f521caa67c57a177cb4` passed run `33794429491`, Linux `100778661705`, Windows `100778661735`, comparator `100778910190`, receipt `d73b9aedadc00018d0a0c8de3852f61ebaec9d3c7fd099155539e3d906567f90`. Application PR `397` merged as `3b8b20916b6390a720fe49ee9685b7ca1ea00238`.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — in_progress with bounded implementation authority.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — planned.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — planned.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — planned.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01/02 remain frozen. MAL-03 must establish genuine matching self-hosted Linux/Windows acceptance RED before production mutation, then pass exact-head Linux/Windows GREEN plus deterministic comparison with exactly one MAL-03 Validation Core profile and zero historical predecessor fanout. MAL-04+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
