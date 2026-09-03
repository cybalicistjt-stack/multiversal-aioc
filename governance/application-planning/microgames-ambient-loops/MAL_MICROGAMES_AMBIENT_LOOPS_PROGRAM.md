# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-01; MAL-02 IN_PROGRESS  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy — is `completed_verified` on exact application main `adf77329574666e1fde5d0f9b86c77d4fa924478`. Owner `Continue` governed-starts MAL-02 — Primitive Input, Timing, State & Goal Contract — from that exact baseline on `integration/mal-02-primitive-input-timing-state-goal` with bounded implementation authority.

Parallel ENV/CEW content work and parallel GCL execution remain outside MAL-02 work selection and do not widen MAL authority.

## Purpose

MAL turns recovered microgame/Aniloop ideas into an original, reusable, governed interaction library. It supports short experiential interactions without becoming a separate game engine and consumes canonical Action/Event, Character, Project, World/Scene, ISE, MAI, AAI, GCL, Permission/visibility and owner-domain state rather than duplicating it.

Recovered basis remains provenance and inspiration only; MAL-01 originality and owner-authority boundaries are frozen.

## Frozen MAL-01 contract

MAL-01 provides source/authority/originality classification and boundary semantics only. Recovered examples must become original MAL designs with stable MAL IDs, explicit provenance and canonical owner references. Proposal classification never canonizes content or outcomes. AI remains proposal-only.

## MAL-02 governed contract

MAL-02 creates reusable primitive interaction contracts only:

- **Semantic input intents:** `directional-intent`, `primary-action`, `secondary-action`, `confirm`, `cancel`, `pause`, `retry`, `accessibility-equivalent`.
- **Timing modes:** `untimed`, `countdown`, `elapsed-limit`, `cadence-window`.
- **Session phases:** `ready`, `active`, `paused`, `succeeded`, `failed`, `cancelled`.
- **Goal kinds:** `counter-target`, `timer-survive`, `progress-target`, `reference-collection`, `ordered-step`.

Inputs are semantic, device-neutral intents. Keyboard, gamepad, touch, switch, assistive and other accessibility-equivalent mappings normalize to the same governed intent rather than becoming separate gameplay truth.

Timing is deterministic logical timing using authored integer ticks/durations/windows. Wall-clock timestamps, animation-frame timing, network latency and refresh rate are excluded from outcome truth and deterministic receipts.

MAL session state is ephemeral/local only. Success, failure, cancellation, counters, timers, progress and reference collections do not mutate canonical Combat, Inventory, Project, Travel, progression, Event, Character or World truth. Later authorized integration must explicitly map a MAL result reference into the owning domain.

Pause freezes MAL logical progression without advancing campaign/world time. Retry creates a new deterministic attempt identity from the same authored definition and does not erase owner history.

Deterministic receipts preserve stable MAL definition/attempt IDs, normalized semantic inputs, logical tick progression, resulting local phase/goal/progress state, source/provenance and canonical owner references. Presentation prose, wall-clock time, raw device identity and unauthorized hidden data are excluded.

MAL-02 does **not** implement movement/navigation/rooms/doors/keys/traversal recipes, conflict/hazards, NPC state machines, Aniloops, owner-domain rewards/outcome commits, persistence or migration `0022`.

## MAL-01 validation evidence

Application PR `396` merged as `adf77329574666e1fde5d0f9b86c77d4fa924478`. Final exact head `559df151053e7af65abda72630384d8827338030` passed selector/repository health, self-hosted Linux, self-hosted Windows and deterministic comparison with receipt `a28dfe0c5b79a11a2e3d120d6343176eb85f0902016f83ff33cbb9dceec6fb15`.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — in_progress with bounded implementation authority.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — planned.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — planned.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — planned.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — planned.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01 remains frozen. MAL-02 must establish genuine matching self-hosted Linux/Windows acceptance RED before production mutation, then pass exact-head Linux/Windows GREEN plus deterministic comparison with exactly one MAL-02 Validation Core profile and zero historical predecessor fanout. MAL-03+, ALP-01+, provider activation, tester distribution, release and deployment remain unauthorized.
