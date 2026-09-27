# RBCE-02 — Retrobit 2D Projection Runtime

**Program:** Retrobit Arcade & Creation Engine (RBCE)  
**Work item:** RBCE-02  
**Status:** OWNER-APPROVED DESIGN BASELINE  
**Owner and final authority:** John Brandon Turner  
**Operational authority:** none; this design does not select live implementation work and cannot override OPS3

## 1. Purpose

RBCE-02 defines the dedicated 2D projection/runtime layer used by Retrobit Game Projects. It converts governed Retrobit project data, GPR gameplay state and MAI/ISE spatial assets into a responsive 2D arcade presentation without creating a second gameplay, rules, campaign, scene, persistence or content authority.

The default Retrobit engine is a **modern 2D runtime with optional retro constraint profiles**. Historical console studies inform optional 8-bit/16-bit-inspired authoring constraints; Retrobit is not a console emulator and does not require historical hardware limitations.

## 2. Authority boundary

### GPR owns semantic gameplay truth

GPR remains authoritative for deterministic gameplay-instance state, semantic input normalization, collision/trigger outcomes, ordered transitions, gameplay operations and typed owner-domain handoff.

RBCE-02 may prepare projection geometry and movement proposals for GPR evaluation, but it may not independently decide canonical collision outcomes, damage, inventory changes, quest progress, objective completion, dialogue truth, rewards or campaign mutation.

### RBCE-02 owns projection behavior

RBCE-02 owns presentation-local and projection-specific behavior including:

- tile/layer rendering;
- sprite batching and draw ordering;
- sprite animation presentation;
- projection-space geometry compilation;
- top-down, side-scroll and fixed-room camera behavior;
- parallax presentation;
- pixel-grid and pixel-perfect scaling modes;
- local interpolation and animation timing that cannot alter semantic outcomes;
- projection adapters for platforms, slopes, ladders, one-way surfaces, moving surfaces, hazards, checkpoints and spawn markers;
- render-safe fallback presentation for missing optional art.

### Other owner systems remain authoritative

- **MRCS** owns governed reusable definitions.
- **MAI** owns asset/source/provenance semantics and structured sprite/tile/map interchange.
- **ISE** owns general Scene/spatial/trigger semantics where reused.
- **AAI/MSAS** own audio definitions/runtime contracts where applicable.
- canonical campaign/character/combat/inventory/world owners retain their own state.
- the Retrobit UI skin remains presentation only.

## 3. Runtime data flow

The required flow is:

`RBCE-01 project + resolved owner definitions + MAI assets + GPR gameplay snapshot`
→ `RBCE-02 projection resolver`
→ `projection profile + movement profile + optional constraint profile`
→ `projection geometry + presentation snapshot`
→ `semantic input / motion proposal`
→ `GPR deterministic evaluation`
→ `accepted gameplay transition`
→ `RBCE-02 render snapshot`

Presentation frame rate, interpolation, particles, screen shake, scanlines, palette effects or display refresh rate may never determine semantic state order.

## 4. Core projection profiles

RBCE-02 v1 defines three required projection families referenced by RBCE-01 `projectionProfileRef` values.

### `projection:top-down-2d`

Required capabilities:

- free or grid-aligned movement projection;
- 4-direction and 8-direction facing presentation;
- tile and polygon collision geometry adapters;
- depth ordering by explicit layer and optional authored Y-sort band;
- doors, exits, portals and region transitions;
- push/interact/trigger geometry;
- follow, bounded and room camera policies.

Representative uses include adventure exploration, action RPGs, dungeon rooms, maze games and overhead action.

### `projection:side-scroll-2d`

Required capabilities:

- gravity-aware movement projection;
- ground/air state presentation;
- platform, ledge, ladder and climb-zone adapters;
- one-way surface adapters;
- slope geometry adapters;
- moving-platform attachment/projection;
- checkpoint and fall/death-volume markers;
- horizontal/vertical/bounded scrolling;
- camera dead-zone and look-ahead policies.

Representative uses include platformers, run-and-gun games, side-scrolling exploration and action-adventure.

### `projection:fixed-room-2d`

Required capabilities:

- locked or bounded camera framing;
- single-screen or connected-room layout;
- authored room-edge/door/portal transitions;
- arcade arena, puzzle-room and dialogue/interior presentation;
- optional platform or top-down movement profile inside the fixed viewport.

`fixed-room-2d` is a camera/room projection family, not a separate gameplay rules engine.

## 5. Movement profiles

Movement feel is data-driven. RBCE-02 must not hard-code one universal arcade physics model.

Initial governed movement profile families are:

- `movement:top-down-free`
- `movement:top-down-grid`
- `movement:platform-standard`
- `movement:platform-floaty`
- `movement:platform-heavy`
- `movement:fixed-room-free`

A movement profile may configure bounded parameters such as acceleration, deceleration, friction, gravity scale, jump impulse, air control, terminal speed, coyote window, jump buffer, climb speed and slope handling when the selected GPR operation family supports those parameters.

Movement profiles configure governed GPR-compatible primitives. They do not create independent gameplay code or unrestricted scripting.

## 6. Geometry and collision adapter contract

RBCE-02 compiles structured 2D scene/map information into deterministic geometry descriptors consumed by the gameplay runtime.

Supported v1 geometry classes:

- axis-aligned rectangle;
- circle;
- convex polygon;
- tile mask / tile cell set;
- line/segment surface;
- one-way surface;
- ladder/climb zone;
- trigger region;
- hazard region;
- spawn/checkpoint marker;
- moving-surface attachment reference.

Authoring/render hitboxes and hurtboxes are explicit semantic roles; they are not inferred from opaque sprite pixels at runtime.

Collision evaluation remains GPR authority. RBCE-02 may generate deterministic geometry/contact candidates and projection metadata, but the accepted gameplay transition is the GPR result.

## 7. Coordinate and timing model

RBCE-02 uses a logical 2D world coordinate space independent of physical display pixels.

Requirements:

- logical world coordinates are stable across render resolutions;
- project rendering may opt into integer/pixel-grid snapping;
- camera/render interpolation is non-authoritative;
- gameplay stepping must use the deterministic fixed-step contract supplied by GPR rather than display refresh timing;
- normalized project output must not depend on object-key order, editor zoom, window size or monitor refresh rate;
- exact numeric representation and fixed-step frequency remain implementation decisions unless an existing GPR contract already fixes them.

## 8. Tile and layer model

A projected scene may resolve ordered layers with semantic roles such as:

- background;
- parallax-background;
- terrain;
- collision-overlay;
- object-below-actors;
- actors;
- object-above-actors;
- effects;
- foreground;
- UI-overlay.

Layers may reference MAI-resolved tilemaps, tilesets, sprite assets or generated presentation primitives.

Collision/trigger semantics must not be inferred solely from visual layer order. Semantic geometry and trigger bindings remain explicit.

Parallax is presentation-only unless a governed gameplay object independently exists at that depth.

## 9. Sprite and animation model

RBCE-02 consumes MAI sprite-sheet/atlas/frame metadata when available.

A presentation binding may define:

- semantic sprite role;
- atlas/frame reference;
- anchor/origin;
- draw offset;
- facing transform policy;
- animation state map;
- frame sequence;
- frame duration or rate;
- loop mode;
- transition presentation;
- hitbox/hurtbox role references;
- palette/material presentation options.

Animation state is a projection of semantic state or presentation-local timing. An animation frame may not become canonical gameplay truth unless a governed GPR operation explicitly exposes a semantic timing/event boundary for that purpose.

## 10. Camera model

Camera state is presentation state.

Supported v1 camera policies:

- fixed;
- follow;
- bounded-follow;
- room-snap;
- dead-zone-follow;
- look-ahead-follow;
- scripted-presentation path where the script is a governed declarative sequence, not arbitrary code.

Camera shake, smoothing and interpolation never change collision, range, visibility or trigger truth unless a separate canonical owner explicitly defines those semantics.

## 11. Retro constraint profiles

Retro constraints are optional authoring/presentation constraints layered over the modern engine.

### `constraint:retrobit-standard`

Default. Modern 2D capabilities within implementation performance budgets. Pixel-art friendly; no artificial historical console limits.

### `constraint:8bit-inspired`

Optional deliberately constrained profile. It may bound logical resolution, palette size, sprite dimensions/count presentation, layer complexity, tile dimensions and animation complexity.

### `constraint:16bit-inspired`

Optional richer retro profile permitting broader palette, larger/more animated sprites, multiple scrolling layers, parallax and richer effects.

### `constraint:custom`

Creator-selected bounded constraint values from supported fields.

These profiles are inspired presentation/authoring profiles, not NES/SNES compatibility claims.

A constraint profile must not silently delete gameplay entities, suppress semantic triggers or change game rules. If a project exceeds a selected constraint profile, validation must either:

1. block publish/play under that profile with typed diagnostics; or
2. apply an explicitly declared deterministic presentation-degradation policy that preserves semantic entities and outcomes.

No degradation policy may change canonical gameplay truth.

## 12. Performance and boundedness

RBCE-02 must expose discoverable implementation limits for at least:

- visible/projected sprites;
- tile layers;
- active animation bindings;
- collision geometry primitives;
- dynamic/moving surfaces;
- parallax layers;
- projected effects;
- render target dimensions.

Exact numeric caps are deferred to implementation/performance certification. Exceeding a hard runtime cap fails closed with a typed diagnostic; it may not silently create nondeterministic behavior.

## 13. Accessibility parity

Consequential gameplay cannot be available only through visual pixel presentation.

RBCE-02 must support projection metadata sufficient for:

- keyboard/gamepad/remappable semantic controls;
- screen-reader summaries of critical room/object state where applicable;
- nonvisual identification of critical interactables/targets/routes where required by the game;
- reduced-motion presentation;
- high-contrast or alternate palette presentation;
- scalable HUD/text independent of the internal pixel-art scale;
- deterministic pause/step/retry behavior where the game mode permits it.

Accessibility changes presentation/input mapping, not canonical outcome rules unless a governed accessibility rule explicitly says otherwise.

## 14. Missing asset and failure behavior

Required semantic assets/geometry fail validation when unresolved.

Optional presentation assets may use an explicit deterministic fallback such as:

- diagnostic checker tile;
- labeled placeholder sprite;
- neutral silhouette;
- no-op optional effect.

Fallbacks must preserve semantic identity and produce diagnostics. They may not invent missing rules, rights or owner definitions.

Representative RBCE-02 failure codes:

- `unsupported-projection-profile`
- `unsupported-movement-profile`
- `unsupported-constraint-profile`
- `invalid-layer-role`
- `invalid-geometry-shape`
- `invalid-hitbox-binding`
- `invalid-hurtbox-binding`
- `invalid-animation-binding`
- `invalid-camera-policy`
- `invalid-parallax-binding`
- `geometry-reference-unresolved`
- `asset-reference-unresolved`
- `gpr-collision-contract-unresolved`
- `gpr-movement-contract-unresolved`
- `constraint-profile-exceeded`
- `runtime-limit-exceeded`
- `nondeterministic-projection-normalization`
- `accessibility-critical-path-missing`

Diagnostics sort deterministically by code, semantic path and stable reference.

## 15. Rights and provenance

RBCE-02 consumes MAI/ARI/PCA rights and provenance evidence. Projection profiles may describe technical style constraints, but production content may not copy protected ROM assets, maps, audiovisual expression, dialogue or proprietary code merely because a retro profile resembles historical hardware.

Research-only console references remain research evidence and are not production dependencies.

## 16. Four-Engine Test Chamber acceptance

RBCE-02 is design-complete only when its contract can express all four original/right-cleared proof rooms from RBCE-01 without game-specific code:

1. top-down plaza traversal and semantic exit transition;
2. connected fixed-room gate with collision and prerequisite state;
3. side-scroll foundry traversal with gravity/platform/hazard/checkpoint projection;
4. fixed-room dialogue presentation with persistent event state driven by GPR/MRCS semantics.

The proof must also demonstrate:

- same semantic outcome across supported display refresh rates;
- same semantic input across at least two input mappings;
- optional retro constraint profile without gameplay mutation;
- deterministic projection normalization;
- missing optional-art fallback;
- accessibility-equivalent critical path.

## 17. Explicit non-goals

RBCE-02 does not:

- emulate a historical console;
- execute ROMs;
- own canonical gameplay state;
- replace GPR collision/trigger authority;
- replace MAI asset/provenance authority;
- replace ISE general Scene semantics;
- add arbitrary JavaScript/Lua/Python/custom scripting;
- define Retrobit Studio UI;
- define the asset workbench;
- define creator-facing Gameplay Parts names;
- define marketplace/store behavior.

Those later concerns remain RBCE-03+.

## 18. Activation boundary

This is a durable design contract only. Product implementation begins only when OPS3 explicitly selects and authorizes RBCE-02 or an equivalent governed implementation work item.
