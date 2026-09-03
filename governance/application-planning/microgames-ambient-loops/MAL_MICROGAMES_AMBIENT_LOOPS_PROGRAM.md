# MAL — Microgames & Ambient Loops

**Program ID:** MAL  
**Status:** OWNER-APPROVED — COMPLETED_VERIFIED THROUGH MAL-02; MAL-03 SELECTED_NOT_STARTED  
**Activation:** after completed_verified SCL-11  
**Successor:** ALP-01  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-27

## Current state

MAL-01 and MAL-02 are `completed_verified`. MAL-02 merged to exact application main `3b8b20916b6390a720fe49ee9685b7ca1ea00238`. MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives — is the strict successor and is `selected_not_started` from that exact baseline with `implementation_branch = null` and `implementation_authority = false`.

Parallel ENV/CEW content work and GCL execution remain outside MAL work selection unless a named dependency proves insufficient.

## Frozen MAL-01 contract

Recovered material is provenance/inspiration only; copying proprietary game/ROM logic, data, maps, scripts, audiovisual assets, names, rule tables or level layouts is not authorized. MAL classifications reference canonical owner domains and never create parallel truth. AI remains proposal-only.

## Frozen MAL-02 contract

MAL-02 established reusable primitive interaction semantics:

- **Semantic input intents:** `directional-intent`, `primary-action`, `secondary-action`, `confirm`, `cancel`, `pause`, `retry`, `accessibility-equivalent`.
- **Timing modes:** `untimed`, `countdown`, `elapsed-limit`, `cadence-window`.
- **Session phases:** `ready`, `active`, `paused`, `succeeded`, `failed`, `cancelled`.
- **Goal kinds:** `counter-target`, `timer-survive`, `progress-target`, `reference-collection`, `ordered-step`.

Inputs remain device-neutral and accessibility-equivalent. Timing truth remains deterministic logical integer timing rather than wall-clock/frame-rate/latency truth. Session state and goals remain ephemeral MAL-local state. Pause/retry, success/failure and reference collection never mutate canonical owner domains. Deterministic receipts exclude raw device identity, wall-clock time, presentation prose and unauthorized hidden data.

## MAL-02 validation evidence

Governed start AIOC PR `921` merged as `5da9cae5002229ba06a671813f56b1a0b4a564de` after one repository-state maintenance-history projection repair; passing Repository Health run `33793725017`, job `100776260435`.

Genuine matching RED used application head `dd3261d3632edb3569669653549bf95168c93588`, run `33794055025`, Linux job `100777396723`, Windows job `100777396679`, comparator `100777629990`, receipt `e4f8ab5c567c33b5fb3d4461de7b2ef76b4a4040f96efd3a7d6818e290ae12a2`.

The first production head exposed one case-sensitive governed panel-marker mismatch. The bounded presentation/source-governance repair produced exact head `c337bfc98de15913a5af8f521caa67c57a177cb4`, which passed run `33794429491`: selector/repository-health job `100778572122`, Linux `100778661705`, Windows `100778661735`, comparator `100778910190`, receipt `d73b9aedadc00018d0a0c8de3852f61ebaec9d3c7fd099155539e3d906567f90`. Application PR `397` merged by repository-allowed squash as `3b8b20916b6390a720fe49ee9685b7ca1ea00238`.

Historical predecessor profile fanout, unchanged-evidence reruns, no-progress cycles and post-merge stale-pointer incidents remained zero.

## MAL-03 selection boundary

MAL-03 is selected only. A future owner `Continue` must governed-start it before product mutation. Its future scope is movement, navigation, rooms, doors, keys and traversal primitives over the frozen MAL-01/02 contracts.

Canonical World/Scene, Action/Event, Character, Inventory, Travel, Project and Permission/visibility owners remain authoritative. MAL-03 may eventually reference them but may not create parallel owner truth. MAL-04+ conflict/hazards/pickups/objectives, NPC behavior, Aniloops, reward/integration mechanics, persistence, migration `0022`, tester distribution, release and deployment remain unauthorized.

## Tranches

1. **MAL-01 — Source/Authority/Originality Boundary & Microgame Taxonomy** — completed_verified.
2. **MAL-02 — Primitive Input, Timing, State & Goal Contract** — completed_verified.
3. **MAL-03 — Movement, Navigation, Rooms, Doors, Keys & Traversal Primitives** — selected_not_started, no implementation authority.
4. **MAL-04 — Interaction, Simple Conflict, Hazards, Pickups & Objective Primitives** — planned.
5. **MAL-05 — NPC/Enemy Behavior & Tiny State Machines** — planned.
6. **MAL-06 — Aniloops, Travel, Repair, Downtime, Transition & Spacewalk Loops** — planned.
7. **MAL-07 — GM Composition Recipes & GCL Integration** — planned.
8. **MAL-08 — Character, World, Project & Event Integration / Reward Boundaries** — planned.
9. **MAL-09 — Accessibility, Mobile/Input, Performance & Nonblocking Fallbacks** — planned.
10. **MAL-10 — Starter Library & Golden Microgame/Aniloop Proof** — planned.

## Current invariant

MAL-01/02 are frozen. MAL-03 has no implementation authority until a future governed start from exact application main `3b8b20916b6390a720fe49ee9685b7ca1ea00238`. No later MAL, ALP, provider, tester, release or deployment authority is implied by selection.
