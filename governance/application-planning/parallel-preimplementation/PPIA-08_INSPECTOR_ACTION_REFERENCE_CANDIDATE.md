# PPIA-08 — Inspector / Action / Reference-Case Candidate

**Work item:** PPIA-08 — Campaign / Scene / Session Authoring Depth  
**State:** MILESTONE CANDIDATE — NOT PPIA-08 COMPLETE  
**Owner:** John Brandon Turner  
**Verified foundation merge:** `327ae916f61cf3e9bba16397ada4c5abe7950d92`

## 1. Purpose

This milestone converts the verified PPIA-08 foundation into concrete inspection, action and reference-case contracts without yet defining the final integrated authoring workflows or completion package.

The milestone adds:

- `PPIA-08_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json`;
- `PPIA-08_REFERENCE_CASES_v0.1.0.json`;
- deterministic inspector/action/reference validation and CI.

## 2. Inspector coverage

The contract defines **16 inspector projection groups**, mapped one-to-one to the verified 16-layer Campaign/Scene/Session taxonomy:

1. Campaign definition and policy;
2. membership, roles, delegation and actor control;
3. Scene definition and hierarchy;
4. Scene templates and branching;
5. reusable source references;
6. Campaign-local placements and permitted overrides;
7. map/media asset references;
8. square-grid calibration and coordinate transform;
9. cell, multi-cell-area, named-zone and gridless addressing;
10. map content placement and layering;
11. dungeon geometry and construction;
12. hidden/reveal/knowledge state;
13. Encounter/objective/trigger/Event links;
14. launch readiness, immutable snapshot and Session binding;
15. governed live amendment and post-session history;
16. permissions, provenance, recovery and accessibility.

Projection happens server-side after authorization. Protected Scene/map facts do not become visible through counts, labels, search, autocomplete, layer serialization, errors, exports, diagnostics, notifications or AI context.

## 3. Governed action coverage

The contract defines **26 actions**, of which **22 are authoritative mutations** and 4 are read/validation actions.

The action set covers:

- Campaign inspection/policy and membership/delegation;
- Scene inspection, composition, templates and branching;
- stable reusable Definition references and Campaign-local override boundaries;
- map-image upload and replacement;
- square-grid creation, alignment, lock and versioned recalibration;
- square cell, multi-cell area, named zone and gridless semantic location creation;
- placement, movement, layering and visibility/reveal;
- all seven verified dungeon primitive families through create/edit/duplicate/remove operations;
- Encounter/objective/trigger links without taking Encounter/balance ownership;
- launch readiness and immutable snapshot creation;
- proposed/accepted/rejected live-Session amendments;
- post-session history and recovery/accessibility inspection.

Every authoritative mutation requires current authorization, current versions, `expected_version`, a stable `operation_id`, and status/current-version lookup before retry after an ambiguous response.

## 4. Owner-required map workflow

The 26-case corpus explicitly proves the map-authoring requirement end to end:

1. upload a map image as a versioned media reference;
2. create a separate square-grid calibration using `cellSizePx`, `originOffsetXPx` and `originOffsetYPx`;
3. pan/translate the **grid calibration** independently of camera pan/zoom;
4. lock or revise calibration as a new version without rewriting image pixels;
5. create stable cell, multi-cell-area and named-zone locations;
6. place Items, Hazards, Encounters, Creature/NPCs, Vehicles, Objectives, Triggers, Notes and other governed Scene content through owning-object references;
7. preserve large multi-cell objects as one placement rather than duplicate source objects;
8. hide/reveal protected content through server-side role-safe projection;
9. pin map, calibration and placement versions into the Session launch snapshot;
10. prevent later recalibration from silently moving an active Session;
11. apply any live change through a governed live-amendment path;
12. preserve gridless and semantic nonvisual operation.

## 5. Dungeon construction coverage

Reference cases cover all verified primitive families:

- room/floor region;
- corridor/path region;
- wall segment;
- door/opening;
- terrain/feature region;
- stairs/portal/transition marker;
- reusable tile/stamp.

Dungeon geometry remains authored Scene geometry. It does not independently establish collision, cover, line of sight, movement legality, damage, lighting, fog or encounter balance.

## 6. Reference corpus

The milestone contains **26 contiguous reference cases** `PPIA08-RC-001..026`.

Coverage includes:

- Campaign policy and bounded delegation;
- Scene hierarchy/templates/branching;
- stable Setting/source references and local overrides;
- map upload/replacement;
- square-grid calibration and camera/calibration separation;
- single-cell, named-zone and multi-cell-area addressing;
- Item/Hazard/Encounter/Creature/Vehicle/objective placement;
- gridless Scenes;
- dungeon construction;
- hidden placement non-leak and governed reveal;
- launch snapshot pinning;
- post-launch recalibration isolation;
- live Session amendment;
- post-session history;
- stale expected-version conflict;
- duplicate operation retry;
- keyboard/screen-reader semantic map authoring and revocation.

Every one of the 16 projection groups and all 26 actions is exercised by at least one case.

## 7. Ownership and authority boundaries

This milestone preserves the verified foundation handoffs:

- MV-IA-F005 retains Campaign/Scene/Session aggregate and launch semantics;
- PPIA-12 retains reusable Setting Definitions and setting-local rules;
- PPIA-02/03/04/05 retain Creature/NPC, Item/Inventory, Vehicle and Species/Form Definitions;
- MV-IA-F012/PPIA-11 retain Encounter definition, simulation and final balance calibration;
- MV-IA-F020 retains permission/hidden-information authority;
- MV-IA-F021 retains recovery/idempotency authority;
- PPIA-08 owns Campaign/Scene composition, map calibration, placement, dungeon authoring geometry, launch packaging and Campaign-local live/post-session authoring state.

## 8. Explicit non-assumptions

This milestone does not introduce:

- automatic image-scale inference;
- required rotation or hex support;
- a universal distance per square;
- map-art-derived collision/LOS/cover/movement rules;
- automatic procedural dungeon generation;
- automatic dynamic lighting/fog simulation;
- Encounter balance ownership;
- source Definition copying into cells;
- hidden information in unauthorized aggregates;
- offline authoritative map or Session mutation;
- AI-generated accepted state without governed authoring acceptance.

## 9. Readiness and next milestone

This package becomes a verified PPIA-08 milestone only after its exact PR head passes the dedicated inspector/reference validator plus every applicable repository regression gate and merges into canonical `main`.

PPIA-08 remains `started` after this milestone. The next bounded milestone is the integrated Campaign/Scene/Session authoring workflow contract: preparation, hierarchy/branching, map upload/calibration, placement/layers/reveal, dungeon construction, launch, live amendment, post-session, recovery and accessibility workflows mapped to these 16 projections, 26 actions and 26 cases.
