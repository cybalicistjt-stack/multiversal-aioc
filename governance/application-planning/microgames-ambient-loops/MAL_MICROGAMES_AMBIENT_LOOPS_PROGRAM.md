# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-05; MAL-06 SELECTED_NOT_STARTED  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 through MAL-05 are `completed_verified`. MAL-05 merged to exact application main `e5ee04672a1dac4d28fa2e954d0201f384cb0482`. MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops — is the strict successor and is `selected_not_started` from that exact baseline with implementation branch `null` and implementation authority `false`.

Parallel ENV/CEW content work and GCL execution remain outside MAL product selection unless a named dependency proves insufficient.

## Frozen contracts

- **MAL-01:** provenance/source/originality classification; no proprietary copying or parallel owner truth.
- **MAL-02:** device-neutral semantic inputs, deterministic logical timing, ephemeral MAL-local state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts.
- **MAL-03:** original MAL-local movement/navigation/room/connector/door/key-reference/traversal projections. Hidden or unauthorized passage state remains unresolved; key checks never mutate Inventory; traversal and `transition-ready` never move canonical Character, World/Scene or Travel truth.
- **MAL-04:** original MAL-local interaction/simple-conflict/hazard/pickup-reference/objective projections. Hidden interaction state remains unresolved; canonical Combat, Character, World, Inventory, Event, Project, progression and reward truth remain externally owned.
- **MAL-05:** original MAL-local NPC/enemy behavior and tiny deterministic state machines. Hidden or unauthorized intent, awareness, targets, pathing and owner state remain unresolved; behavior never creates autonomous canonical NPC/Character agency or mutates canonical movement, Combat, Inventory, World/Scene, Travel, Event, Project, progression or reward truth.

## MAL-05 validation evidence

Governed-start AIOC PR `934` passed Repository Health run `33810432330`, job `100830717357`, validated exact head `e9c7713defc7b9356391fa0d6b5e5e48168614f0`, and merged as `b84ec8602d4787f812ccbd0343566188df3080ed`.

Genuine matching acceptance RED used exact head `607c7b617e5f35ef4c29214ae72bbb1c8341ded5`, run `33810670454`, selector `100831480799`, Linux `100831513073`, Windows `100831513250`, comparator `100831655710`, receipt `0def6b1e0e3211ef4837b42717a1d4e5e2beb86e1118bd55ee1e3469fc28a4e4`. No acceptance repair was required.

Production contract and panel were introduced atomically. First production head `fde08f79d21bf946023f4bce742fbb5771e0a639` passed run `33810842588`, selector/repository-health `100832053475`, Linux `100832085448`, Windows `100832085546`, comparator `100832242141`, receipt `a6d0770a38e6d8c87c8db4af1bd2e36060c4fc9f09b1d0c3d3650e5d563871e2`. Application PR `400` merged as `e5ee04672a1dac4d28fa2e954d0201f384cb0482`.

Historical predecessor profile fanout, unchanged-evidence reruns, no-progress cycles and post-merge stale-pointer incidents remained zero. No validation-contract, production feature or repository-state repair was required.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — completed_verified.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — completed_verified.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — completed_verified.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — selected_not_started; no implementation authority.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01..05 remain frozen with implementation authority retired. A future owner `Continue` must governed-start MAL-06 from exact application main `e5ee04672a1dac4d28fa2e954d0201f384cb0482` before any Aniloop/travel/repair/downtime/transition/spacewalk application mutation. Canonical Travel, Character/NPC, Combat, Inventory/Asset, Action/Event, World/Scene, Project/progression and Permission owners remain authoritative. MAL-07+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
