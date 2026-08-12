# PPIA-08 — Integrated Campaign / Scene / Session Authoring Workflow Candidate

**Work item:** PPIA-08 — Campaign / Scene / Session Authoring Depth  
**State:** MILESTONE CANDIDATE — NOT PPIA-08 COMPLETE  
**Verified foundation merge:** `327ae916f61cf3e9bba16397ada4c5abe7950d92`  
**Verified inspector/action/reference merge:** `91cc220c846f132ca539531574b42f56425e9a57`

## Purpose

This milestone integrates the verified PPIA-08 foundation, map/grid/dungeon contract, authority matrix, **16 inspector projections**, **12 presentation profiles**, **26 governed actions**, **26 reference cases**, and **10 domain handoffs** into **17 end-to-end authoring workflows**.

It is an implementation-ready workflow candidate, not PPIA-08 completion.

## The 17 workflows

1. Campaign setup, policy, membership and bounded delegation.
2. Scene hierarchy, templates and explicit branching.
3. Reusable source-reference preparation and permitted Campaign-local overrides.
4. Map-image asset upload, replacement and attribution.
5. Square-grid calibration, preview, lock and recalibration.
6. Cell, multi-cell-area, named-zone and semantic location authoring.
7. Scene content placement, movement, layering and multi-cell occupancy.
8. Hidden content, knowledge state and governed reveal.
9. Basic dungeon construction and semantic geometry editing.
10. Encounter, objective, trigger and Event-link authoring.
11. Launch readiness, immutable snapshot and Session binding.
12. Governed live-Session amendment proposal and decision.
13. Post-session outcome, history and reusable-definition isolation.
14. Reconnect, stale-write conflict and ambiguous-operation recovery.
15. Semantic nonvisual map, Scene and history authoring.
16. Gridless Scene authoring and placement.
17. Post-launch map replacement or recalibration isolation and adoption.

Exactly **14 workflows perform authoritative mutation**. Mutation workflows use the verified global mutation protocol: reauthorize, revalidate current versions, require `expected_version`, require a stable `operation_id`, and perform operation-status/current-version lookup before retry after an ambiguous outcome.

## End-to-end map authoring

The owner-required map workflow is fully connected:

`upload/replace map image → create square-grid calibration → set cellSizePx → pan/translate the grid with originOffsetXPx/originOffsetYPx independently of camera pan/zoom → preview/lock/recalibrate by version → define square cells, multi-cell areas, named zones or gridless semantic locations → place owning-domain content → move/layer/hide/reveal → build dungeon geometry → link Encounters/objectives/triggers → validate launch → pin immutable snapshot → govern live amendment → record post-session history`.

Uploaded map pixels are never destructively rewritten for grid alignment.

## Placement and domain ownership

Campaign-local placement records retain stable `ownerDomain`, `objectId`, and `objectVersion` references. A large Vehicle or other multi-cell object remains **one owning object and one placement over one semantic area**, never one cloned object per cell.

Reusable Definitions remain owned by:

- PPIA-12 — Setting/environment;
- PPIA-02 — Creature/NPC;
- PPIA-03 — Item/Inventory;
- PPIA-04 — Vehicle;
- PPIA-05 — Species/Form.

PPIA-08 owns Campaign/Scene composition, placement, local allowed overrides, map calibration, dungeon authoring geometry, launch packaging and Campaign-local live/post-session authoring state.

## Dungeon construction

The workflow contract preserves **all seven verified primitive families**:

- room/floor;
- corridor/path;
- wall;
- door/opening;
- terrain/feature;
- stairs/portal/transition;
- reusable tile/stamp.

They are authoring geometry only. Geometry does not itself define collision, cover, line of sight, movement legality, damage, lighting, fog or balance.

## Encounter boundary

PPIA-08 may place Encounter references, objectives, hazards, triggers and location/spawn-zone metadata. **MV-IA-F012 / PPIA-11 retains Encounter definition, simulation, tactical resolution and final balance authority.**

## Hidden information

Authorization and permission filtering happen before protected reference resolution or aggregation. Hidden Scene/map content contributes nothing to unauthorized counts, labels, search/autocomplete, layer serialization, errors, exports, diagnostics, notifications or AI context.

Reveal is an explicit governed knowledge-state mutation, not merely a client-side visibility toggle.

## Launch and live-session integrity

Launch readiness resolves an exact version set. The launch snapshot pins Campaign, Scene, map asset, calibration, placement and visibility-policy versions.

Later map replacement, recalibration, placement change or visibility change never silently alters an active Session. Adoption into live play requires a governed amendment or a separately created future launch snapshot.

## Recovery

Authoritative writes use `expected_version` and stable `operation_id`. Ambiguous responses require operation-status/current-version lookup before retry. Compatible duplicate retry returns the prior status/result instead of duplicating state. Stale writes fail safely; blind last-write-wins is prohibited.

Offline operation may preserve safe drafts but may not silently commit authoritative Campaign, map or Session state.

## Accessibility

Every visual map/grid/layer/drag/geometry workflow has keyboard, touch, high-zoom/reflow, screen-reader and semantic nonvisual operation. The visual map is never the sole authoritative representation, and required meaning never depends only on drag, hover, color, animation or pixel position.

Gridless Scenes are first-class rather than a degraded fallback.

## Traceability

`PPIA-08_WORKFLOW_TRACEABILITY_MATRIX_v0.1.0.json` proves **zero gaps** across:

- 16 projection groups;
- 12 presentation profiles;
- 26 governed actions;
- 26 reference cases;
- 10 domain handoffs.

It also records 11 end-to-end assertions for map upload, calibration, semantic addressing, placement identity, hidden information, dungeon geometry, Encounter ownership, immutable snapshots, live amendments/history, recovery and accessible nonvisual authoring.

## Explicit exclusions

This workflow milestone does not:

- invent universal distance-per-square;
- require hex grids, map rotation, automatic image-scale inference, procedural dungeon generation, dynamic lighting or fog simulation;
- infer collision/LOS/cover/movement/damage/balance from image or dungeon geometry;
- copy source Definitions into Campaign placements;
- leak hidden content through unauthorized aggregates;
- silently rewrite launch snapshots;
- permit blind last-write-wins or duplicate authoritative retry;
- permit AI to directly commit accepted Campaign/Scene/Session state;
- activate application runtime, STAGE-A-A2, release, deployment, tester access, paid services or production credentials.

## Next milestone

After this exact workflow candidate passes `Validate PPIA-08 Workflow Contracts` plus every applicable repository regression gate and merges, PPIA-08 remains `started`.

The next bounded milestone is the **final PPIA-08 Campaign / Scene / Session Authoring Experience Specification v1.0.0**, final acceptance/traceability matrix, completion report, deterministic completion validator and CI gate.
