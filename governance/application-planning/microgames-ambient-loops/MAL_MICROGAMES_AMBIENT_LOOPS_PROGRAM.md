# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-04; MAL-05 SELECTED_NOT_STARTED  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 through MAL-04 are `completed_verified`. MAL-04 merged to exact application main `d0f246ea192ccaf964abb66756f06de454a02ecd`. MAL-05 — NPC/Enemy Behavior & Tiny State Machines — is the strict successor and is `selected_not_started` from that exact baseline with implementation branch `null` and implementation authority `false`.

Parallel ENV/CEW content work and GCL execution remain outside MAL product selection unless a named dependency proves insufficient.

## Frozen contracts

- **MAL-01:** provenance/source/originality classification; no proprietary copying or parallel owner truth.
- **MAL-02:** device-neutral semantic inputs, deterministic logical timing, ephemeral MAL-local state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts.
- **MAL-03:** original MAL-local movement/navigation/room/connector/door/key-reference/traversal projections. Hidden or unauthorized passage state remains unresolved; key checks never mutate Inventory; traversal and `transition-ready` never move canonical Character, World/Scene or Travel truth.
- **MAL-04:** original MAL-local interaction/simple-conflict/hazard/pickup-reference/objective projections. Hidden or unauthorized interaction state remains unresolved. Conflict never mutates canonical Combat, Character or World truth; hazards never apply canonical damage or conditions; pickup completion never mutates Inventory or rewards; objective completion never commits Event, Project, campaign, progression, reputation, advancement or reward truth.

## MAL-04 validation evidence

Governed-start AIOC PR `930` passed Repository Health run `33806212574`, job `100817186863`, and merged as `dd99bed7649e6b4453d05344dbf7f2b976db23a4`.

The initial acceptance head `d780d2d7e4f9fb0f062bc5fac0853d1ddc04d224` exposed one case-sensitive governed proof-marker mismatch. After one bounded validation-contract repair, genuine matching RED used exact head `18959997549427c531a26f3b711c9340cb9d2458`, run `33806564900`, Linux `100818380409`, Windows `100818380596`, comparator `100818551107`, receipt `ec284051c9d7b79ae695a5baa027fc64271f249290c593d74cbabfddd4f4061d`.

Production contract and panel were then introduced atomically. First production head `b5a6193dd50ae9831eec03b62240b477571e5021` passed run `33806823707`, selector/repository-health `100819175197`, Linux `100819212041`, Windows `100819212005`, comparator `100819391588`, receipt `e76f63502ca8485cc883cc30f34b2c2af25a8bdf85f69b42d10b35412ec0a81b`. Application PR `399` merged as `d0f246ea192ccaf964abb66756f06de454a02ecd`.

Historical predecessor profile fanout, unchanged-evidence reruns, no-progress cycles and post-merge stale-pointer incidents remained zero. No production feature repair or repository-state repair was required.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — completed_verified.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — completed_verified.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — selected_not_started; no implementation authority.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — planned.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01..04 remain frozen with implementation authority retired. A future owner `Continue` must governed-start MAL-05 from exact application main `d0f246ea192ccaf964abb66756f06de454a02ecd` before any NPC/enemy behavior or tiny state-machine application mutation. Canonical NPC/Character, Combat, Inventory, Action/Event, World/Scene, Project/progression and Permission owners remain authoritative. MAL-06+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
