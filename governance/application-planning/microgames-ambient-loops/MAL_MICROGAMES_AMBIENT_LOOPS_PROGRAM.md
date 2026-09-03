# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-04; MAL-05 IN_PROGRESS  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 through MAL-04 are `completed_verified`. MAL-05 — NPC/Enemy Behavior & Tiny State Machines — is `in_progress` from exact application main `d0f246ea192ccaf964abb66756f06de454a02ecd` on `integration/mal-05-npc-enemy-behavior-tiny-state-machines` with bounded implementation authority.

Parallel ENV/CEW content work and GCL execution remain outside MAL-05 work selection unless a named dependency proves insufficient.

## Frozen contracts

- **MAL-01:** provenance/source/originality classification; no proprietary copying or parallel owner truth.
- **MAL-02:** device-neutral semantic inputs, deterministic logical timing, ephemeral MAL-local state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts.
- **MAL-03:** original MAL-local movement/navigation/room/connector/door/key-reference/traversal projections. Hidden or unauthorized passage state remains unresolved; key checks never mutate Inventory; traversal and `transition-ready` never move canonical Character, World/Scene or Travel truth.
- **MAL-04:** original MAL-local interaction/simple-conflict/hazard/pickup-reference/objective projections. Hidden or unauthorized interaction state remains unresolved. Conflict never mutates canonical Combat, Character or World truth; hazards never apply canonical damage or conditions; pickup completion never mutates Inventory or rewards; objective completion never commits Event, Project, campaign, progression, reputation, advancement or reward truth.

## MAL-05 governed contract

MAL-05 defines original reusable MAL-local NPC/enemy behavior and tiny deterministic state-machine primitives only.

- **Behavior roles:** `passive-local`, `patrol-local`, `guard-local`, `pursue-local`, `evade-local`.
- **Machine states:** `dormant`, `observe-local`, `approach-local`, `engage-local`, `withdraw-local`, `reset-local`, `unresolved`.
- **Transition triggers:** `semantic-input`, `local-proximity-threshold`, `local-objective-state`, `local-hazard-state`, `deterministic-tick-threshold`, `authorized-owner-reference`, `unresolved`.
- **Behavior outcomes:** `hold-local`, `move-local`, `interact-local`, `contest-local`, `withdraw-local`, `reset-local`, `unresolved`.

MAL-05 consumes frozen MAL-02 semantic inputs/deterministic logical ticks plus MAL-03 traversal and MAL-04 interaction projections. Raw device identity, wall-clock time, animation frames, latency, refresh rate and nondeterministic randomness never become behavior truth.

NPC/enemy references are MAL-local projections over authorized canonical NPC/Character references. MAL-05 does not create autonomous canonical agency, personality, goals, knowledge, allegiance, hostility, statistics, position, inventory or encounter truth.

State machines are tiny, explicit and deterministic. Transition priority is authored data; the same authorized local state and logical tick produce the same next state and deterministic receipt.

Unknown, hidden or unauthorized NPC intent, awareness, target knowledge, pathing truth, Combat state or owner-domain state remains `unresolved` and is never inferred.

Patrol, approach, pursue, evade and withdraw outcomes update MAL-local behavior/session projections only. They never move canonical Characters/NPCs or mutate World/Scene or Travel truth.

`engage-local` and `contest-local` may reference MAL-04 simple-conflict projections, but they never initiate or resolve canonical Combat, damage, conditions, wounds, initiative or defeat.

Authorized owner references may gate transitions, but MAL-05 cannot reveal hidden data or commit Action/Event, Project, campaign, progression, reward, reputation or advancement outcomes. AI may propose behavior definitions but cannot invent hidden knowledge, make canonical NPC decisions or commit outcomes.

MAL-05 does **not** implement Aniloops, travel/repair/downtime/transition/spacewalk loops, owner-domain mutation, persistence, migration `0022`, tester distribution, release or deployment.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — completed_verified.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — completed_verified.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — in_progress with bounded implementation authority.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — planned.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01..04 remain frozen. MAL-05 must establish genuine matching self-hosted Linux/Windows acceptance RED before production mutation, then pass exact-head Linux/Windows GREEN plus deterministic comparison with exactly one MAL-05 Validation Core profile and zero historical predecessor fanout. MAL-06+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
