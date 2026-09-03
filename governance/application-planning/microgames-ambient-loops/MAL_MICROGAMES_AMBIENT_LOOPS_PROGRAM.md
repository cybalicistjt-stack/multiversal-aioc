# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-05; MAL-06 IN_PROGRESS  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 through MAL-05 are `completed_verified`. MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops — is `in_progress` from exact application main `e5ee04672a1dac4d28fa2e954d0201f384cb0482` on `integration/mal-06-aniloops-travel-repair-downtime-transition-spacewalk` with bounded implementation authority.

Parallel ENV/CEW content work and GCL execution remain outside MAL-06 work selection unless a named dependency proves insufficient.

## Frozen contracts

- **MAL-01:** provenance/source/originality classification; no proprietary copying or parallel owner truth.
- **MAL-02:** device-neutral semantic inputs, deterministic logical timing, ephemeral MAL-local state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts.
- **MAL-03:** original MAL-local movement/navigation/room/connector/door/key-reference/traversal projections. Hidden or unauthorized passage state remains unresolved; key checks never mutate Inventory; traversal and `transition-ready` never move canonical Character, World/Scene or Travel truth.
- **MAL-04:** original MAL-local interaction/simple-conflict/hazard/pickup-reference/objective projections. Hidden interaction state remains unresolved; canonical Combat, Character, World, Inventory, Event, Project, progression and reward truth remain externally owned.
- **MAL-05:** original MAL-local NPC/enemy behavior and tiny deterministic state machines. Hidden or unauthorized intent, awareness, targets, pathing and owner state remain unresolved; behavior never creates autonomous canonical NPC/Character agency or mutates canonical movement, Combat, Inventory, World/Scene, Travel, Event, Project, progression or reward truth.

## MAL-06 governed contract

MAL-06 defines original reusable deterministic MAL-local Aniloop compositions only.

- **Aniloop kinds:** `travel-local`, `repair-local`, `downtime-local`, `transition-local`, `spacewalk-local`.
- **Loop phases:** `ready-local`, `active-local`, `checkpoint-local`, `paused-local`, `completed-local`, `failed-local`, `unresolved`.
- **Composition step kinds:** `traversal`, `interaction`, `behavior`, `objective`, `timing-gate`, `authorized-owner-reference`.
- **Loop outcomes:** `hold-local`, `progress-local`, `checkpoint-local`, `complete-local`, `blocked-local`, `setback-local`, `unresolved`.

Aniloops compose frozen MAL-02 timing/input/session semantics, MAL-03 traversal projections, MAL-04 interaction/objective projections and MAL-05 behavior/state-machine projections. They do not introduce replacement primitive systems or owner-domain mechanics.

Definitions are authored, ordered and deterministic: the same definition, MAL-local state, logical tick and authorized owner references produce the same next step, phase, outcome and deterministic receipt.

`travel-local` may sequence traversal, interaction, timing and objective steps, but never moves canonical Characters/NPCs, changes World/Scene or Travel truth, consumes fuel/resources or commits arrival/departure.

`repair-local` may sequence interaction, objective and timing steps, but never consumes Inventory/Asset truth, changes canonical asset condition, commits Project progress, spends currency/resources or grants rewards.

`downtime-local` may sequence timing, interaction and objective steps, but never advances canonical campaign/world time, heals damage, restores conditions/resources, trains, crafts, progresses Projects or grants advancement/rewards.

`transition-local` may sequence traversal and interaction into a MAL-local transition-ready/completed state, but never changes canonical scenes, locations, travel legs, Events or campaign state.

`spacewalk-local` may compose traversal, hazard, interaction and behavior projections, but never applies canonical damage/conditions, consumes oxygen/fuel, changes equipment/Inventory, moves canonical Characters or mutates World/Scene/Combat truth.

Unknown, hidden or unauthorized owner-domain state remains `unresolved`. Pause/retry/accessibility-equivalent controls remain governed by MAL-02, and pausing never advances canonical time. AI may propose loop definitions but cannot invent hidden owner state or commit canonical outcomes.

MAL-06 does **not** implement GM composition/GCL integration, canonical owner mutation, reward integration, persistence, migration `0022`, tester distribution, release or deployment.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — completed_verified.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — completed_verified.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — completed_verified.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — in_progress with bounded implementation authority.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01..05 remain frozen. MAL-06 must establish genuine matching self-hosted Linux/Windows acceptance RED before production mutation, then pass exact-head Linux/Windows GREEN plus deterministic comparison with exactly one MAL-06 Validation Core profile and zero historical predecessor fanout. MAL-07+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
