# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-06; MAL-07 IN_PROGRESS  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 through MAL-06 are `completed_verified`. MAL-07 — GM Composition Recipes & GCL Integration — is `in_progress` from exact application main `472f2ff95100ea6fd2c623f0c5b85b5100cefa59` on `integration/mal-07-gm-composition-recipes-gcl-integration` with bounded implementation authority.

The current AIOC baseline `49c44aa828f46ed807e444b858e634e15c6a1c7c` includes CEW-13. CEW remains unrelated to MAL-07 and is inherited without reinterpretation.

GCL is a named MAL-07 dependency only at its already-completed reference boundary. GCL-01 through GCL-12 are `completed_verified`; GCL-13, GCL-14 and GCL-16 are ready but not completed, and GCL-17 Composition Engine Design is still planned. MAL-07 therefore integrates completed GCL records by reference only and does not pre-empt unfinished GCL work.

## Frozen contracts

- **MAL-01:** provenance/source/originality classification; no proprietary copying or parallel owner truth.
- **MAL-02:** device-neutral semantic inputs, deterministic logical timing, ephemeral MAL-local state/goals, pause/retry, accessibility-equivalent controls and deterministic receipts.
- **MAL-03:** original MAL-local traversal projections. Hidden or unauthorized passage state remains unresolved; traversal never mutates canonical Character, World/Scene, Inventory or Travel truth.
- **MAL-04:** original MAL-local interaction/simple-conflict/hazard/pickup-reference/objective projections. Hidden interaction state remains unresolved; canonical owner domains remain external.
- **MAL-05:** original MAL-local NPC/enemy behavior and tiny deterministic state machines. Hidden intent, awareness, target and pathing state remains unresolved; no autonomous canonical NPC/Character agency is created.
- **MAL-06:** original deterministic MAL-local Aniloop compositions for `travel-local`, `repair-local`, `downtime-local`, `transition-local` and `spacewalk-local`. Loop completion never commits canonical owner-domain truth.

## MAL-07 governed contract

MAL-07 defines original deterministic GM composition recipes and a bounded reference bridge to completed GCL-01..12 records.

### Recipe families

- `microgame-insert-local`
- `aniloop-wrapper-local`
- `scene-segment-local`
- `encounter-overlay-local`
- `session-sequence-local`
- `adventure-bridge-local`

### Recipe states

- `draft-local`
- `validated-local`
- `ready-local`
- `blocked-local`
- `unresolved`

### GCL reference kinds

- `taxonomy-grammar`
- `hook-premise`
- `situation-scene`
- `encounter-archetype`
- `objective-stakes-outcome`
- `complication-escalation`
- `pressure-difficulty`
- `adversary-role`
- `mystery-investigation`
- `adventure-structure`
- `session-kit`
- `campaign-architecture`

### Binding outcomes

- `reference-linked-local`
- `mal-composed-local`
- `ready-local`
- `blocked-local`
- `unresolved`

Recipes are explicit, ordered and deterministic. The same recipe definition, authorized GCL references, MAL-local state and logical tick produce the same binding/result receipt.

GCL integration is reference-based. MAL-07 does not copy or vendor GCL libraries, mutate GCL records, silently reinterpret GCL semantics, or turn GCL into parallel MAL-owned truth. Missing, hidden, unauthorized or not-yet-completed GCL records remain `unresolved`.

MAL-07 expressly does **not** implement GCL-16 discovery/recommendation or GCL-17 Composition Engine Design. It does not auto-search hidden libraries, rank secret choices, or synthesize unavailable GCL records.

GM recipes may bind completed GCL construction references to frozen MAL primitives and Aniloops for local presentation/use. They do not launch sessions, adventures or campaigns; do not move canonical Characters; do not mutate World/Scene, Action/Event, Project/progression, Inventory/Asset, Combat, Travel, reward or Permission truth; and do not create durable persistence.

AI may propose recipes only from explicitly authorized visible references and MAL-local inputs. It cannot invent hidden GCL records, choose secret outcomes, commit canonical consequences or bypass Permission/visibility.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — completed_verified.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — completed_verified.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — completed_verified.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — completed_verified.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — in_progress with bounded implementation authority.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01..06 remain frozen. MAL-07 must establish genuine matching self-hosted Linux/Windows acceptance RED before production mutation, then pass exact-head Linux/Windows GREEN plus deterministic comparison with exactly one MAL-07 Validation Core profile and zero historical predecessor fanout. GCL-13+ unfinished content, GCL-16 discovery/recommendation, GCL-17 composition-engine implementation, MAL-08+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
