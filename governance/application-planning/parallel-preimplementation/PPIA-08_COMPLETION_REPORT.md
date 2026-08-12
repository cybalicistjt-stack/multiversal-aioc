# PPIA-08 — Campaign / Scene / Session Authoring Completion Report

**State:** COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES  
**Work item:** PPIA-08 — Campaign / Scene / Session Authoring Depth

## Completion claim being tested

PPIA-08 has an implementation-ready Campaign / Scene / Session authoring packet satisfying the canonical completion gate, including hierarchy, templates, content placement, hidden state, branching, preparation/live/post-session workflows, reference Campaign material, GM map-image upload, square-grid scale/alignment calibration, cell/area-addressable governed placements, gridless authoring and a basic dungeon-map construction kit.

This report is not itself a completion claim. PPIA-08 may become `completed_verified` only after the exact completion head passes `Validate PPIA-08 Completion Contract` plus every applicable repository regression, merges to canonical main, and post-merge continuity records the validated head, PR and merge.

## Verified milestone anchors

- PPIA-07→PPIA-08 transition: `ccdad24fc26ca853b92411ad1066eb6b7ec1f0f5`.
- PPIA-08 foundation PR #248: `327ae916f61cf3e9bba16397ada4c5abe7950d92`.
- PPIA-08 Inspector/action/reference PR #249: `91cc220c846f132ca539531574b42f56425e9a57`.
- PPIA-08 integrated workflow PR #250: `c85941c8c255eed7be098798bb9cb8d36ee2c3ea`.

## Final implementation-ready design set

The completion candidate preserves:

- **9 canonical repository sources** and **3 retained supporting design-source groups**;
- the blocking owner-directed 2026-08-11 map/grid/dungeon extension;
- **16 semantic layers**;
- **12 presentation profiles**;
- **16 Inspector projection groups**;
- **26 governed actions**, including **22 authoritative mutations** and four read/validation actions;
- **26 contiguous reference cases `PPIA08-RC-001..026`**;
- **17 integrated workflows**, including **15 authoritative-mutation workflows**;
- **10 domain handoffs**;
- **48 blocking acceptance requirements across 16 categories**.

The final experience specification is `PPIA-08_CAMPAIGN_SCENE_SESSION_AUTHORING_EXPERIENCE_SPEC_v1.0.0.md`. The final matrix is `PPIA-08_ACCEPTANCE_TRACEABILITY_MATRIX_v1.0.0.json`.

## Owner-required map and dungeon path

The candidate closes the owner-required path end to end:

`upload/replace map image → create versioned square-grid calibration → set cellSizePx and originOffsetXPx/originOffsetYPx → preview/translate/lock/recalibrate without rewriting image bytes or camera state → define square cells, multi-cell areas, named zones or gridless locations → place stable owning-domain references → move/layer/hide/reveal → create/edit seven dungeon primitive families → attach Encounter/objective/trigger links → validate launch readiness → create immutable launch snapshot → govern any live amendment → retain post-session history and recovery evidence`.

Square and gridless remain the required initial coordinate modes. No universal distance-per-square is invented.

## Seven dungeon primitive families

The completion candidate preserves all seven verified families:

1. room/floor region;
2. corridor/path region;
3. wall segment;
4. door/opening;
5. terrain/feature region;
6. stairs/portal/transition marker;
7. reusable tile/stamp.

These are authoring geometry. They do not themselves define collision, line of sight, cover, movement legality, damage, lighting, fog, Encounter power or balance.

## Source and ownership integrity

Exact uploaded-image calibration, semantic cell addressing and the seven-family dungeon schema are governed PPIA-08 design rather than recovered source canon.

Reusable Definitions remain in their owning domains. Campaign-local placement uses stable `ownerDomain`, `objectId` and `objectVersion`; it never becomes ownership of the referenced Definition. Multi-cell occupancy does not clone the owning object.

PPIA-12 retains reusable Setting ownership; PPIA-02 Creature/NPC; PPIA-03 Items/Inventory; PPIA-04 Vehicles; PPIA-05 Species/Forms. MV-IA-F012 / PPIA-11 retains Encounter definition, simulation, tactical resolution and **final balance authority**.

## Permission integrity

Permission filtering occurs before protected reference resolution or aggregation. Hidden content contributes nothing to unauthorized counts, labels, search/autocomplete, layer serialization, errors, exports, diagnostics, notifications or AI context.

Reveal is a governed knowledge-state mutation rather than a client-only display flag.

## Snapshot and Session integrity

Launch readiness resolves an exact candidate version set. Launch snapshot creation pins exact Campaign, Scene, map asset, grid calibration, placement and visibility-policy versions plus Session-binding inputs.

The launch snapshot is immutable. Later map replacement, recalibration, placement or visibility changes cannot silently alter an active Session. Adoption requires a new snapshot or an explicit governed live amendment.

## Recovery integrity

All authoritative mutations require `expected_version` and a stable `operation_id`. Stale writes fail safely. Ambiguous responses require operation-status/current-version lookup before retry. Compatible duplicate operation-ID retry returns the prior result/status rather than duplicating authoritative state.

Broad offline authoritative Campaign/map/Session mutation remains prohibited.

## Accessibility integrity

The visual map is never the sole authoritative representation. Required Scene/map/dungeon work has semantic nonvisual, keyboard, touch, high-zoom/reflow and screen-reader equivalents. Gridless Scenes are first-class.

## Final acceptance result expected from the deterministic gate

The completion validator must independently prove that the final packet retains:

- 16 layers / 12 profiles;
- 16 projections;
- 26 actions / 22 writes;
- 26 reference cases;
- 17 workflows / 15 mutation workflows;
- 10 handoffs;
- 48 blocking acceptance requirements / 16 categories;
- 9 canonical repository sources / 3 retained design groups;
- square + gridless modes;
- `cellSizePx`, `originOffsetXPx`, `originOffsetYPx` calibration;
- four semantic location types;
- seven dungeon primitive families;
- permission-before-aggregation;
- immutable launch snapshots;
- expected-version/idempotent recovery;
- semantic nonvisual operation;
- PPIA-11 final balance ownership;
- no runtime, STAGE-A-A2, release, deployment, tester, paid-service or production-credential activation.

## Post-merge continuity

If and only if the exact completion candidate passes all applicable gates and merges, the post-merge continuity step must:

1. reset the governed PPIA-08 branch to the canonical completion merge;
2. set the PPIA-08 checkpoint to `completed_verified` with the exact validated head, completion PR and merge;
3. set the PPIA-08 backlog tranche to `completed_verified`;
4. preserve the immutable foundation, Inspector/reference and workflow milestone evidence;
5. move current PPIA selection through a separate governed transition to dependency-optimized **PPIA-09 — Investigation & Mystery Authoring Kit**;
6. leave roadmap prose projection batched unless the transition milestone requires it.

This completion does **not** activate application runtime, STAGE-A-A2, release, deployment, tester access, paid services, production credentials or unsupported canonical promotion.