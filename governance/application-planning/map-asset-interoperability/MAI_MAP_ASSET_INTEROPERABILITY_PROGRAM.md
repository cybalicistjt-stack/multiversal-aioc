# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL  
**Activation:** after LNG-06  
**Successor:** WCI-01  
**Owner and final authority:** John Brandon Turner

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

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey**  
   Catalog sprite sheets, image collections, autotiles, modular pieces, props, overheads, complete/layered battlemaps, animation, hex/isometric sets and structured editor/VTT exports. Establish provenance/license and map-vs-World authority boundaries.

2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema**  
   Define MapAsset, Tile, TerrainSet, ObjectAsset, Module, Battlemap, Layer, Placeable, anchors, dimensions, transforms, grid metadata, elevation, variants, animation, dependencies and source provenance.

3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine**  
   Square, gridless, flat/point hex, isometric, staggered and free-position layouts; snapping, native resolution, game distance, rotation/scaling and coordinate conversion.

4. **MAI-04 — Terrain, Autotile & Connectivity Grammar**  
   Normalize center/edge/corner/transition/connectivity semantics for terrain, roads, rivers, walls and coastlines; adapt source-specific autotile conventions into one deterministic terrain grammar.

5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry**  
   Background/ground/object/token-relative/foreground/roof/GM layers plus walls, doors, windows, portals, collision, elevation, light/vision boundaries and permission-safe projections.

6. **MAI-06 — Universal Import Adapter Framework**  
   Provider-neutral importer contract plus adapters for common raw and structured formats. Partial imports must report unsupported metadata instead of silently discarding it.

7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution**  
   Tag terrain/objects/structures/environment/style/scale; resolve semantic needs against actually available assets; support GM/user choice, style-lock, cross-pack compatible substitution, explicit placeholders and unresolved states.

8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench**  
   Folder/ZIP/package recognition, import preview, asset classification, search/filter, terrain paint, stamps, modular assembly, layers, transforms, provenance and undo/redo. User correction always overrides uncertain classification.

9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration**  
   Bind maps to MIB-11/World locations and existing Scene/Combat/Exploration projections without making coordinates or artwork canonical identity; preserve GM/player visibility.

10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof**  
    Validate deliberately different sources: pixel sheet, autotiles, loose props, modular rooms, full battlemap, structured VTT scene, hex, isometric and animated assets; prove deterministic import metadata, deduplication, provenance, fallback behavior and cross-platform compatibility.

## Invariants

- Artwork is a projection/presentation resource, not World or combat truth.
- Missing art never blocks non-map/theater-of-the-mind play.
- No pack is assumed complete.
- Semantic requirement and chosen visual asset remain separable.
- Manual GM/user asset assignment is first-class.
- License/source/provenance metadata is preserved.
- Hidden/GM-only layers remain permission-scoped.
