# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** MAI-01 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Current item:** MAI-01 — Ecosystem, Format, License & Authority Survey  
**Implementation branch:** none — selection only  
**Implementation authority:** false until future owner Continue governed-starts MAI-01  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current selection state

DPL-14 completed_verified on application PR #311 and closed the DPL program. Strict application-roadmap order therefore selects **MAI-01 — Ecosystem, Format, License & Authority Survey** as `selected_not_started` only.

MAI-01 has checkpoint `governance/ai/work-state/MAI-01-attempt-001.json`, application baseline `8f4c4aca8e264233284dc631ada807476937176a`, no implementation branch and no implementation authority. A future owner **Continue** must freshly verify canonical state and governed-start MAI-01 before any implementation or survey artifact is treated as current work.

## Purpose

MAI lets Multiversal natively and intuitively ingest practical map/tileset/spatial-visual asset formats, normalize them into a vendor-neutral internal model and make them usable in play without forcing the user to understand the source format.

No creator/vendor or editor is the canonical model. Full battlemaps, sprite sheets, loose image tiles, object/prop packs, modular rooms, autotiles, hex/isometric sets, animated assets and structured VTT/editor exports are different source classes feeding one internal system.

## Critical incomplete-pack rule

No tileset or asset pack is expected to contain every semantic object Multiversal can represent.

A scene therefore stores **semantic requirements separately from selected art**. Resolution may:
1. use an exact compatible asset from the active pack;
2. use a compatible asset from another permitted installed pack;
3. offer ranked available choices to the GM/user;
4. use an explicit placeholder/generic representation if allowed;
5. remain visibly unresolved.

Multiversal must never silently invent a missing asset or pretend an incompatible image satisfies gameplay semantics. Style-lock, source/license constraints and manual override remain available.

## MAI-01 selection boundary

The first tranche is a source/ecosystem/authority survey. Once separately governed-started, it must:

- catalog sprite sheets, image collections, autotiles, modular pieces, props/overheads, complete and layered battlemaps, animation, hex/isometric sets and structured editor/VTT exports;
- identify practical format/source classes and supported metadata without making any vendor/editor canonical;
- preserve source, license and provenance constraints;
- establish map/art-vs-World authority boundaries and permission-sensitive visibility boundaries;
- preserve the incomplete-pack rule and explicit unresolved/placeholder behavior;
- avoid implementing MAI-02 schema/importer mechanics prematurely.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `selected_not_started`  
   Catalog sprite sheets, image collections, autotiles, modular pieces, props, overheads, complete/layered battlemaps, animation, hex/isometric sets and structured editor/VTT exports. Establish provenance/license and map-vs-World authority boundaries.

2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `planned`  
   Define MapAsset, Tile, TerrainSet, ObjectAsset, Module, Battlemap, Layer, Placeable, anchors, dimensions, transforms, grid metadata, elevation, variants, animation, dependencies and source provenance.

3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `planned`  
   Square, gridless, flat/point hex, isometric, staggered and free-position layouts; snapping, native resolution, game distance, rotation/scaling and coordinate conversion. Preserve a path for assisted grid detection plus bounded affine/perspective registration so imperfect scans, photographs or exported maps can be aligned through user-confirmed control points without making camera/view state authoritative.

4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `planned`  
   Normalize center/edge/corner/transition/connectivity semantics for terrain, roads, rivers, walls and coastlines; adapt source-specific autotile conventions into one deterministic terrain grammar.

5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `planned`  
   Background/ground/object/token-relative/foreground/roof/GM layers plus walls, doors, windows, portals, collision, elevation, light/vision boundaries and permission-safe projections.

6. **MAI-06 — Universal Import Adapter Framework** — `planned`  
   Provider-neutral importer contract plus adapters for common raw and structured formats. Partial imports must report unsupported metadata instead of silently discarding it. Structured scene formats such as UVTT-class packages may supply supported grid/geometry/door/light metadata rather than being flattened to pixels.

7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `planned`  
   Tag terrain/objects/structures/environment/style/scale; resolve semantic needs against actually available assets; support GM/user choice, style-lock, cross-pack compatible substitution, explicit placeholders and unresolved states.

8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`  
   Folder/ZIP/package recognition, import preview, asset classification, search/filter, terrain paint, stamps, modular assembly, layers, transforms, provenance and undo/redo. User correction always overrides uncertain classification.

9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`  
   Bind maps to MIB-11/World locations and existing Scene/Combat/Exploration projections without making coordinates or artwork canonical identity; preserve GM/player visibility.

10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`  
    Validate deliberately different sources: pixel sheet, autotiles, loose props, modular rooms, full battlemap, structured VTT scene, hex, isometric and animated assets; prove deterministic import metadata, deduplication, provenance, fallback behavior and cross-platform compatibility.

## Downstream relationship

AAI follows MAI so the same provider-neutral asset/provenance patterns can be reused for audio without merging visual and audio ownership. ISE then consumes completed MAI + AAI to deliver the native playable tabletop/canvas experience; MAI itself remains the visual/map interoperability owner.

## Invariants

- MAI-01 is selection-only until future owner Continue governed-starts it.
- MAI-02+ have no implementation authority.
- Artwork is a projection/presentation resource, not World or combat truth.
- Missing art never blocks non-map/theater-of-the-mind play.
- No pack is assumed complete.
- Semantic requirement and chosen visual asset remain separable.
- Manual GM/user asset assignment is first-class.
- License/source/provenance metadata is preserved.
- Hidden/GM-only layers remain permission-scoped.
- No real-money commerce, release/deployment or provider/payment activation is authorized by MAI selection.
