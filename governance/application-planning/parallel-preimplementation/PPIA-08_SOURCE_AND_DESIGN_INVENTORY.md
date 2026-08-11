# PPIA-08 — Campaign / Scene / Session Authoring Depth Source & Design Inventory

**Work item:** PPIA-08  
**Status:** FOUNDATION CANDIDATE — NOT PPIA-08 COMPLETE  
**Owner and final authority:** John Brandon Turner  
**Transition base:** `ccdad24fc26ca853b92411ad1066eb6b7ec1f0f5`

## 1. Purpose

This inventory establishes the authority boundary for PPIA-08 before deeper Campaign, Scene, Session, map and dungeon-authoring contracts are written.

PPIA-08 deepens the already-approved Internal Alpha Campaign/Scene/Session architecture. It does not replace that architecture, reopen completed PPIA object domains, or turn map authoring into an independent tactical rules engine.

## 2. Authority order

1. Owner decisions and current canonical repository state.
2. Current PPIA backlog, checkpoints, transition evidence and completed PPIA contracts.
3. `MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md` and shared Internal Alpha permission/recovery/action contracts.
4. Completed PPIA-02/03/04/05/12 domain boundaries.
5. Screen/UI/Feature Bible material as retained supporting design evidence.
6. Later PPIA-08 proposals only where the higher authorities leave a gap.

Unknown mechanics remain unknown. PPIA-08 may define authoring structure; it may not invent unrelated combat, balance, ownership or source mechanics.

## 3. Canonical governing repository sources

### A. Campaign / Scene / Session authority

`governance/application-planning/internal-alpha/feature-packets/MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md`

Source-backed requirements retained by PPIA-08 include:

- Campaign, Scene and Session are distinct governed aggregates/lifecycles.
- Scene content references reusable source Definitions rather than silently copying or mutating those Definitions.
- Campaign-local placements, overrides, visibility and current state remain Campaign-local.
- Session launch uses an immutable launch snapshot/version boundary.
- hidden information is projected server-side before serialization.
- autosave/reconnect/recovery and bounded offline behavior remain governed.
- a required nonvisual alternative exists wherever a Scene uses map/media presentation.

MV-IA-F005 intentionally excluded full map authoring from its bounded alpha slice. The owner has now explicitly added map-image calibration, cell-addressable content assignment and a basic dungeon construction kit to **PPIA-08 depth**. That owner decision supersedes only the earlier scope exclusion; MV-IA-F005's authority, privacy, snapshot, recovery and source-Definition boundaries remain controlling.

### B. Permissions / hidden information

`governance/application-planning/internal-alpha/feature-packets/MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md`

PPIA-08 must filter authorization before hidden Scene facts, cells, areas, placements, encounter links, notes, hazards, doors, discoveries, counts, search results, map layers, notifications, exports, diagnostics or AI context are resolved or serialized.

### C. Recovery / bounded offline

`governance/application-planning/internal-alpha/feature-packets/MV-IA-F021_AUTOSAVE_RECONNECT_RECOVERY_AND_BOUNDED_OFFLINE_USE.md`

Authoritative Campaign/Scene/Session/map mutations use stable operation identity, expected versions and status/current-version lookup before retry after ambiguous outcomes. Offline authoring may preserve safe drafts; it does not silently commit authoritative Session/map state.

### D. Encounter ownership

`governance/application-planning/internal-alpha/feature-packets/MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md`

PPIA-08 may place/reference an Encounter or encounter trigger in a Scene/cell/area. It does not absorb Encounter definition, simulation or balance authority. PPIA-11 retains final encounter/balance calibration.

### E. Reusable World/Setting boundary

`governance/application-planning/parallel-preimplementation/PPIA-12_WORLD_SETTING_AUTHORING_EXPERIENCE_SPEC_v1.0.0.md`

Reusable Setting Definitions and environment templates remain separate from Campaign instance/current state. Map placement, destruction, discovery, occupation, doors opened, hazards disabled and similar live state cannot rewrite reusable world/setting source facts.

### F. Owning object domains

Completed PPIA-02, PPIA-03, PPIA-04 and PPIA-05 retain ownership of Creature/NPC, Item/Inventory, Vehicle and Species/Form Definitions. PPIA-08 owns only Campaign/Scene placement, local visibility, local state references and authoring composition around those objects.

## 4. Retained design-bible evidence

The retained project design sources establish surrounding interface intent:

### Screen Design Bible

- `SD-302 — Battle Map`: grid/gridless, fog of war, elevation, terrain, hazards, templates, waypoints, measurement and ping; pan/zoom/select/move/inspect/multi-select interactions.
- `SD-1003 — Scene Builder`: Scene hierarchy, canvas, map, actors, triggers, notes, validation and inspector; drag/drop composition, layers, lighting/audio hooks and transitions.
- `SD-1004 — Encounter Builder`: participants, spawn zones, hazards, objectives, rewards and difficulty analysis.
- shared authoring: autosave, undo/redo, keyboard shortcuts, command palette, rule/provenance inspection, offline recovery and responsive layouts.
- accessibility: keyboard-first authoring, screen-reader landmarks, high-contrast map editing, non-color status and touch alternatives.

### UI Design Bible

Scene Builder supports Scene hierarchy, maps, notes, objectives, lighting, audio hooks, environmental effects, triggers and Scene transitions, using a Scene canvas, Inspector, asset browser and validation panel.

### Feature Bible

Exploration/discovery design includes maps, hazards, governed hidden discoveries and `Dungeon` as a Discovery type. Encounter objects use stable IDs, trigger conditions, environment, participants, rewards, risks and provenance.

These sources support map/Scene authoring context. They do **not** specify the exact uploaded-image grid calibration transform or dungeon primitive schema defined below; those are owner-directed/governed PPIA-08 design.

## 5. Owner-directed blocking PPIA-08 map requirement

The owner added the following first-class requirement on 2026-08-11:

1. A GM can upload an image to use as a map.
2. A square grid can be scaled to match the image.
3. The grid can be panned/translated into the correct position over the image.
4. Once calibrated, individual cells and multi-cell areas can be addressed for Scene authoring.
5. Cells/areas can receive governed references such as Items, Hazards, Encounters and other Scene content.
6. A basic dungeon map construction kit can build maps without requiring an uploaded image.

The canonical PPIA backlog completion gate now makes this requirement blocking.

## 6. Foundation interpretation of that requirement

The foundation adopts these bounded semantics:

- uploaded image bytes remain an asset; grid calibration is separate versioned Scene metadata;
- initial governed grid kinds are `square` and `gridless`; square is required by owner direction and gridless is preserved by prior design;
- square-grid calibration minimally stores cell size/scale and X/Y origin offset relative to the underlying image;
- camera pan/zoom is view state; **grid pan/alignment** is calibration state and must not be conflated with camera movement;
- cells use stable integer column/row coordinates with an optional human-readable label such as A1;
- areas may reference one or many cells so large hazards, rooms, vehicles, encounters or zones do not duplicate owning objects per square;
- placed content uses stable owning-domain ID/version references plus Campaign-local placement metadata;
- hidden placements are filtered before counts, labels, autocomplete, thumbnails, exports or AI context;
- launch snapshots freeze the map asset reference, calibration version and placement set used by a Session;
- later calibration changes do not silently reposition an already-launched Session; they require a governed new snapshot or live amendment path;
- every required map function has a semantic list/coordinate/zone representation for keyboard and screen-reader use.

## 7. Basic dungeon-construction boundary

The foundation defines a **basic authoring geometry kit**, not a procedural dungeon generator or a tactical simulation engine.

Required primitive families:

- room/floor region;
- corridor/path region;
- wall segment;
- door/opening;
- terrain/feature region;
- stair/portal/transition marker;
- simple reusable tile/stamp;
- erase/remove plus undo/redo through shared authoring behavior.

The kit may generate a Scene-owned map geometry layer and/or renderable map asset projection. It does not create combat cover/LOS/damage rules unless owning rules explicitly supply them.

## 8. Explicit non-assumptions

PPIA-08 foundation does not assume:

- a map must use a grid;
- a square is automatically a fixed real-world distance;
- hex support is required in the first implementation-ready contract;
- uploaded images contain discoverable scale metadata;
- image pixels become authoritative game coordinates without calibration;
- placing an Item/Creature/Vehicle copies its source Definition;
- placing an Encounter transfers Encounter/balance ownership to PPIA-08;
- fog, lighting, LOS, pathfinding or movement legality can be inferred from artwork alone;
- dungeon walls automatically imply collision, cover or visibility mechanics;
- hidden placements can contribute to unauthorized counts or previews;
- AI-generated rooms/placements become accepted Campaign state without governed acceptance.

## 9. Foundation outcome

PPIA-08 foundation must now formalize:

- Campaign/Scene/Session semantic layers;
- map asset + calibration + coordinate model;
- cell/area/zone placement ownership;
- basic dungeon geometry;
- hidden/reveal, launch snapshot and live amendment boundaries;
- source Definition handoffs;
- recovery/accessibility requirements;
- downstream ownership of tactical resolution and final balance.

This is a foundation candidate only. PPIA-08 remains `started` until later inspector/workflow/completion milestones are independently validated and merged.
