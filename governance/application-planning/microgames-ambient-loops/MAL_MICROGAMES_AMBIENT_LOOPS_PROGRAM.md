# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-03; MAL-04 IN_PROGRESS  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01, MAL-02 and MAL-03 are `completed_verified`. MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives — is `in_progress` from exact application main `87d08c663606e0d0e1afc9955b069891367b8f83` on `integration/mal-04-interaction-conflict-hazards-pickups-objectives` with bounded implementation authority.

Parallel ENV/CEW content work and GCL execution remain outside MAL-04 work selection unless a named dependency proves insufficient.

## Frozen contracts

- **MAL-01:** provenance/source/originality classification; no proprietary copying or parallel owner truth.
- **MAL-02:** device-neutral semantic inputs, deterministic logical timing, ephemeral MAL-local state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts.
- **MAL-03:** original MAL-local movement/navigation/room/connector/door/key-reference/traversal projections. Hidden or unauthorized passage state remains unresolved; key checks never mutate Inventory; traversal and `transition-ready` never move canonical Character, World/Scene or Travel truth.

## MAL-04 governed contract

MAL-04 defines original reusable MAL-local interaction primitives only:

- **Interaction modes:** `inspect`, `activate`, `operate`, `attempt`.
- **Simple-conflict states:** `idle`, `engaged-local`, `advantage-local`, `setback-local`, `resolved-local`, `unresolved`.
- **Hazard states:** `clear-authorized`, `present-authorized`, `triggered-local`, `avoided-local`, `unresolved`.
- **Pickup states:** `not-applicable`, `available-reference`, `collected-local-reference`, `unresolved`.
- **Objective states:** `inactive`, `active-local`, `progressed-local`, `satisfied-local`, `failed-local`, `unresolved`.
- **Resolution outcomes:** `no-change`, `progress-local`, `setback-local`, `complete-local`, `blocked-local`, `unresolved`.

MAL-04 consumes frozen MAL-02 semantic inputs/deterministic logical ticks and MAL-03 local traversal context. Device identity, wall-clock time, animation frames, latency and refresh rate never become outcome truth.

Interaction primitives operate on MAL-local target references and authorized owner-domain references. Hidden, unknown or unauthorized target/conflict/hazard/pickup/objective state remains `unresolved`; absence of visible evidence never implies availability, safety, defeat, collection or completion.

Simple conflict is a bounded MAL-local contest projection. It may track local engagement, advantage, setback and resolution, but it never creates or mutates canonical Combat initiative, hit points, damage, conditions, wounds, Character position, World state or encounter truth.

Hazards may project authorized hazard references and MAL-local `triggered-local` / `avoided-local` progress only. Triggering a hazard never applies damage, conditions, Inventory loss, Character mutation or World/Scene mutation.

Pickups may reference authorized canonical Inventory/Asset records. `collected-local-reference` records only completion of a MAL-local interaction step; it does not create, grant, transfer, equip, consume, destroy or reward an item.

Objectives track MAL-local interaction progress only. `satisfied-local` or `failed-local` never commits Event, Project, campaign, progression, reputation, advancement or reward truth.

Resolution may emit deterministic owner-reference result identifiers for later owning integrations, but MAL-04 never commits owner-domain outcomes. Pause/retry/accessibility remain governed by MAL-02, and traversal remains governed by MAL-03. AI may propose definitions but cannot invent hidden state, apply damage, grant Inventory, complete canonical objectives or commit outcomes.

MAL-04 does **not** implement NPC behavior/state machines, Aniloops, canonical owner mutation, reward integration, persistence, migration `0022`, tester distribution, release or deployment.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — completed_verified.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — in_progress with bounded implementation authority.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — planned.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — planned.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01..03 remain frozen. MAL-04 must establish genuine matching self-hosted Linux/Windows acceptance RED before production mutation, then pass exact-head Linux/Windows GREEN plus deterministic comparison with exactly one MAL-04 Validation Core profile and zero historical predecessor fanout. MAL-05+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
