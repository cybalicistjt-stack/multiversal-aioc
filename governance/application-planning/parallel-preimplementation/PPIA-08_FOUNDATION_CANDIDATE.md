# PPIA-08 — Campaign / Scene / Session Authoring Depth Foundation Candidate

**State:** FOUNDATION CANDIDATE — NOT PPIA-08 COMPLETE  
**Owner:** John Brandon Turner  
**Transition merge:** `ccdad24fc26ca853b92411ad1066eb6b7ec1f0f5`

## Foundation package

This candidate establishes the implementation boundary for later PPIA-08 authoring workflows and acceptance material.

It adds:

- `PPIA-08_SOURCE_AND_DESIGN_INVENTORY.md`;
- `PPIA-08_SOURCE_MANIFEST_v0.1.0.json`;
- `PPIA-08_CAMPAIGN_SCENE_SESSION_TAXONOMY_v0.1.0.json`;
- `PPIA-08_MAP_GRID_DUNGEON_AUTHORING_CONTRACT_v0.1.0.json`;
- `PPIA-08_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json`;
- deterministic foundation validation and CI.

## What is source-backed

Canonical MV-IA-F005 establishes Campaign/Scene/Session separation, source Definition references, Campaign-local placements/overrides, launch snapshots, hidden-information projections, recovery and required nonvisual map/media alternatives.

Retained Screen/UI/Feature Bible material establishes Battle Map grid/gridless operation, map pan/zoom/select/inspect, terrain/hazards/templates/measurement, Scene Builder maps/layers/actors/triggers/notes/validation, Encounter Builder spawn zones/hazards/objectives, and Dungeon as a Discovery type.

MV-IA-F020 and F021 preserve permission-before-resolution and expected-version/idempotent recovery. Completed PPIA-02/03/04/05/12 preserve owning-domain Definitions.

## Owner-directed PPIA-08 addition

The owner explicitly required the deeper map-authoring capability that MV-IA-F005 had deferred from its smaller alpha slice.

This is now blocking PPIA-08 scope:

1. GM uploads an image as a map.
2. GM scales a **square grid** to the image.
3. GM pans/translates the grid overlay into alignment by X/Y offset.
4. Calibration is versioned and can be locked/revised without rewriting the image asset.
5. Each cell and multi-cell area can become a stable Scene location.
6. Items, hazards, encounters, creatures/NPCs, vehicles, objectives, triggers, notes, environmental features, doors/transitions and other governed content can be assigned by stable owning-object reference.
7. Gridless Scene operation remains available.
8. A basic dungeon construction kit provides rooms/floors, corridors, walls, doors/openings, terrain/features, stairs/portals/transitions and reusable tiles/stamps.
9. Map authoring has keyboard, touch, screen-reader and semantic list/coordinate equivalents.

## Calibration model

The minimal square-grid transform is:

- `cellSizePx`;
- `originOffsetXPx`;
- `originOffsetYPx`;
- source `mapMediaReferenceId` + asset version;
- calibration ID + version + lock state.

Rotation is not required by owner direction and is not introduced as a foundation requirement.

Camera pan/zoom changes the user's view. Grid pan/translation changes calibration. They are separate state domains.

## Placement model

A Scene placement records stable placement identity, Scene identity, placement kind, owning-domain object ID/version, location reference, visibility state, version and provenance.

Location references can be:

- one square cell;
- a multi-cell area;
- a named zone;
- a gridless semantic location.

The same reusable Definition may be placed more than once. Large objects or hazards reference an area instead of cloning the underlying Definition into every square.

## Launch and live-session boundary

Session launch snapshots freeze the map asset version, grid calibration version, Scene version and placement versions used for that Session.

A later authoring recalibration cannot silently reposition an active Session. Applying it to live play requires a governed live amendment or a new launch snapshot.

## Dungeon-kit boundary

The basic dungeon kit is authored geometry and presentation metadata. It is not a procedural-generation requirement and it does not infer tactical collision, line of sight, cover, movement cost, damage, lighting or balance rules from geometry alone.

## Hidden information and accessibility

Authorization/filtering occurs before hidden cells, layers, hazards, encounters, doors, notes, discoveries, counts or AI/export/diagnostic projections are produced.

A visual map is never the only authoritative representation. Semantic coordinates, named zones, ordered placement lists and nonvisual descriptions preserve complete required authoring operation.

## Deferred beyond foundation

Later PPIA-08 milestones still need to define:

- Campaign/Scene/Session inspector and action contracts;
- complete Scene hierarchy/template/branching workflows;
- map asset upload/replace/calibrate/recalibrate workflows;
- placement/layer/hidden-reveal workflows;
- dungeon construction workflows;
- preparation/live/post-session amendment workflows;
- reference campaign/Scene/map cases;
- final acceptance traceability and completion contract.

Advanced dynamic lighting/fog simulation, tactical LOS/pathfinding/movement legality and Encounter balance are not silently added by this foundation.

PPIA-08 remains `started` until those later milestones are independently validated and merged.
