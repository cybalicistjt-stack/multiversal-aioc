# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-03; MAL-04 SELECTED_NOT_STARTED  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01, MAL-02 and MAL-03 are `completed_verified`. MAL-03 merged to exact application main `87d08c663606e0d0e1afc9955b069891367b8f83` after a clean governed start, genuine matching self-hosted RED, one bounded acceptance-proof marker repair, and first-production exact-head GREEN. MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives — is the strict successor and is `selected_not_started` with no branch or implementation authority.

Parallel ENV/CEW content work and GCL execution remain outside MAL work selection unless a named dependency proves insufficient.

## Frozen contracts

- **MAL-01:** provenance/source/originality classification; no proprietary copying or parallel owner truth.
- **MAL-02:** device-neutral semantic inputs, deterministic logical timing, ephemeral MAL-local state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts.
- **MAL-03:** original MAL-local movement/navigation/room/connector/door/key-reference/traversal projections. Hidden or unauthorized passage state remains unresolved; key checks never mutate Inventory; traversal and `transition-ready` never move canonical Character, World/Scene or Travel truth.

## MAL-03 validation evidence

Governed start AIOC PR `925` passed Repository Health run `33800696132`, job `100799201254`, and merged as `3ba13b0355f294e180c1e97cf9f8b91acafdd11b`. The initial RED package head `716910859bcccc003804f533708f06c4ab167d8a` exposed one case-sensitive proof-marker mismatch. After that bounded acceptance repair, genuine RED head `42ec393a02df29e848f48f8a001b907c41fb3542` failed on both self-hosted lanes at `client-typecheck`; run `33801011788`, Linux `100800283726`, Windows `100800283715`, comparator `100800471277`, receipt `d77aa1f7203c622ce953079b94d9b703c2e477bea40177afbf9bdd0cc2dff5c5`. Production contract and panel were then introduced atomically. First production head `222a378b802207b1f5abd01072a33f47abaf1dcc` passed selector/repository health `100800995351`, Linux `100801050111`, Windows `100801050365`, comparator `100801269326` in run `33801244250`, receipt `3c4f2b66c53ae0f4888a8fdef2bbd3fce7919114685d032a9bd63101c32114f3`. Application PR `398` merged as `87d08c663606e0d0e1afc9955b069891367b8f83`.

Historical predecessor fanout, unchanged-evidence reruns, no-progress cycles and post-merge stale-pointer incidents remained zero.

## MAL-04 selection boundary

MAL-04 is selection only. A future governed start may define original reusable interaction, simple-conflict, hazard, pickup-reference and objective primitives over frozen MAL-01..03.

Selection does **not** authorize Combat/damage/condition mutation, Inventory creation/ownership/loot/reward mutation, Event/Project/progression outcome mutation, Character or World mutation, NPC behavior, Aniloops, reward integration, persistence, migration `0022`, tester distribution, release or deployment. Unknown and hidden state remains unresolved. AI remains proposal-only.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — completed_verified.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — selected_not_started.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — planned.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — planned.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01..03 remain frozen. MAL-04 has no implementation authority until a future owner `Continue` completes governed start from exact application main `87d08c663606e0d0e1afc9955b069891367b8f83`. MAL-05+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
