# MCS — Multiversal Cartography Studio

**Program ID:** MCS  
**Program name:** Multiversal Cartography Studio  
**Version:** 0.2.0 — PDCP reduced  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** ROADMAP_DEPENDENCY_GRAPH typed MCS start gates; parallel-safe with MCCS/MRCS/MSAS  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none

## Purpose

MCS is Multiversal's map-specific creator for finished world, regional, settlement, city, dungeon, interior, tactical, scene, isometric, deck-plan and atlas cartography. It preserves optional semantic links to playable World, Scene, Exploration, Combat, Settlement, Route, Discovery and other owner-domain records without making artwork authoritative game truth.

The governing flow is:

`owner truth / MAI spatial records → cartography document + presentation draft/proposals → map-specific render/interchange profiles → explicit owner binding/acceptance where allowed`

Pixels, vectors, labels, generator results, imported metadata and map projections remain presentation/proposal state unless an owning domain explicitly accepts them.

## PDCP reduction

Historical baseline: **21 tranches**. Effective implementation/proof plan: **12 tranches**.

The authoritative receipt is `governance/application-planning/preimplementation-design-closure/PDCP_MCS_REDUCTION_RECEIPT.json`; detailed closure is `PDCP_MCS_FAMILY_DESIGN_CLOSURE.md`.

The surviving order is:

`MCS-01 → MCS-03 → MCS-05 → MCS-07 → MCS-08 → MCS-10 → MCS-13 → MCS-14 → MCS-15 → MCS-18 → MCS-19 → MCS-21`

This sparse order is intentional. Historical IDs remain provenance; removed standalone tranches have complete residual mappings in the PDCP receipt.

## Owner boundaries

MCS consumes rather than duplicates:

- **ARI:** resource identity, rights/provenance, derivative lineage and asset governance.
- **MAI:** map-asset/package schemas, projections, coordinates/scales, grids, connectivity, descriptive geometry, resolver/composer and import-adapter foundations.
- **ISE / Scene / Tabletop:** live canvas, placements, runtime scene state, camera and interaction.
- **SSA / World / MSLR:** semantic spatial construction, topology and runtime spatial-law truth.
- **World / Environment / Exploration / Settlement / Kingdom / Faction / Economy:** canonical world, social, territorial, population, route and economy state.
- **Combat / Visibility / Permissions:** runtime collision, range, cover, hazards, lighting/LOS/fog authorization and hidden state.
- **PCA-02 / PCA-03:** reusable procedural DAG/recipe/seed/cache and terrain/ecology/flora/settlement/spatial generator primitives.
- **PCA-09:** generic style-locked generation orchestration.
- **PCA-12 / PDCP Packet 08:** generic simulation, graph, feasibility and formal-analysis substrate.
- **PCA-15 / ARI / PDCP Packet 07:** generic production governance, locking, version/review/collaboration, preview/recovery/debug and publication controls.
- **reduced MBES:** built-environment/facility truth.
- **reduced MSWI:** systemic consequence propagation.
- **VTI:** provider-neutral structured map/scene/token external interoperability.

MCS owns the cartography document/editor experience, map-specific generator packs, map-specific presentation/layout, semantic-binding UX, permission-safe cartographic projections, map interchange/loss reporting and final golden proof.

## Reduced program tranches

### MCS-01 — Cartography Workspace, Document, Large-Map Canvas, Viewport & Authority Contract

Implement one versioned cartography workspace over MAI/ARI records with stable object/layer IDs, presentation/binding dispositions, pan/zoom/rotation, multi-resolution raster/vector rendering, culling, viewport tiling, cache invalidation, extension retention, recovery and deterministic export composition. Do not mint a second map-asset or World ledger.

### MCS-03 — Precision Selection, Transform, Snapping, Vector Geometry, Paths & Edit History

Implement the map-bounded object/vector editing kernel: selection/group/lock, transform/alignment/distribution, rulers/guides, square/hex/isometric/object snapping, keyboard manipulation, path/node/handle editing, shapes, strokes/fills, clipping/boolean/offset helpers and reversible creator history. Canonical owner history remains separate.

### MCS-05 — Raster, Mask, Texture, Blend, Symbol, Stamp, Scatter & Reusable Component Studio

Implement the map-specific paint/place substrate: raster/texture brushes, erase/masks/fills/gradients/blends, tileable textures, ARI/MAI symbol/stamp/component palettes, brush-along-path placement, seeded scatter/density/randomization and custom authorized map art. Generic image/vector kernels remain replaceable libraries/PCA capabilities.

### MCS-07 — Typography, Labels, Legends, Styles, Themes, Templates, Atlas & Publishing Layout

Implement cartographic labels/path text, legends/keys/scale/coordinate aids, frames/title blocks/navigation, semantic style tokens, map themes/templates, color grading/effects, print/page layouts, export profiles and atlas navigation. PCA/ARI own generic style-generation/resource governance.

### MCS-08 — Geographic Terrain, Elevation, Water, Route, Border & Network Authoring

Implement manual and precision geographic feature authoring for land/coastlines, terrain regions, contours/elevation, cliffs/ridges, water bodies, rivers, roads/trails, bridges/fords/passages, borders and other map networks. Visual connectivity remains noncanonical; owner bindings/proposals are explicit.

### MCS-10 — Map-Specific Procedural World Proposal Workbench over PCA

Consume PCA-02/PCA-03 recipe/seed/cache/spatial-generator infrastructure rather than rebuilding it. Provide map-specific masks/locks/extent/projection, preview/dry-run receipts, partial regeneration, manual-edit continuity and independently switchable/promotable proposal packs for geography/elevation, hydrology/climate/biome/resources, population/settlement/culture/state and routes/trade. Every result is proposal/presentation state until its owner accepts it.

### MCS-13 — Settlement, City, District & Street Cartography

Implement urban map authoring for districts, blocks, lots, streets/alleys, walls/gates, waterways, building footprints, landmarks/service markers, density patterns and reusable urban map styles. Settlement/MBES data may seed or bind maps without being duplicated or mutated by drawing.

### MCS-14 — Dungeon, Cave, Interior, Isometric, Deck-Plan, Section & Multi-Level Builder

Implement the shared room/level/vertical-projection kernel: walls/floors/rooms/passages, caves/tunnels, doors/windows/openings, stairs/ladders/elevators, roofs/overheads, object placement, room templates, floor/level management, blueprint/reference tracing, GM layers, isometric/staggered views, sections/cutaways/deck plans and elevation-aware presentation. Runtime topology/3D truth remains owner-controlled.

### MCS-15 — Tactical Scene, Lighting, Fog, Elevation & Hazard Authoring

Provide tactical-map authoring for square/hex/gridless calibration, measurement/templates, spawn/waypoint zones, cover/elevation annotations, hazard/light inputs, wall/door occlusion geometry and fog painting/preview. Runtime LOS, collision, cover, movement and hazard adjudication stay with Scene/Combat/Visibility owners.

### MCS-18 — Semantic Binding, World Sync & Discovery/Fog Projection

Implement explicit bindings/proposals between map elements and governed owner records such as locations, regions, settlements, routes, environments, territories, scenes, portals and discoveries. Provide owner-version references, stale-binding detection, refresh/rebase, map-only overrides, typed owner routing and party/campaign discovery projections that filter hidden truth before rendering.

### MCS-19 — Map Interchange, Round-Trip, Campaign Atlas, Review, Versions & Publishing

Implement map-specific structured packages, flattened/vector outputs where representable, VTI/MAI external interchange, GeoJSON-class mapping where justified, print-at-scale output, external-editor round-trip, linked campaign/world atlas packaging, unsupported-semantics retention/loss reporting, map-specific review/conflict projections and publish/archive adapters over ARI/PCA/Packet-07 infrastructure.

### MCS-21 — Golden Cartography Capability & Semantic-Integration Proof

Prove world, regional, settlement/city, dungeon/interior multi-level, tactical, isometric/deck-plan and linked campaign-atlas workflows. Evidence must cover generator→manual-edit continuity, vector/raster editing, custom assets, styles/templates, large-map performance, structured/flattened export, offline/local-first blocking workflows, accessibility alternatives, deterministic procedural receipts, rights/provenance, import-loss reporting, permission filtering and explicit presentation-only versus owner-bound comparisons.

## Family execution rule

When MCS is eventually selected, each surviving tranche targets at most 24 active minutes with at least 8 minutes protected for focused validation, evidence verification, reconciliation and successor marking. If a surviving tranche cannot credibly preserve that reserve, split it before governed start rather than during execution.

One owner `Continue` carries a governed-started tranche through implementation, validation, verified closeout and next-tranche selection unless an OPS3 owner-only boundary or genuine external blocker is reached. Load only that tranche's dependency closure; block unrelated archaeology and other-family work.

## Completion standard

MCS is complete only when the 12 surviving tranches are `completed_verified`, `MCS-21` proves the complete cartography capability battery, blocking workflows work without paid/cloud mapping providers, map generation remains proposal-safe, structured/flattened interchange preserves declared fidelity/provenance, large-map interaction meets declared budgets, accessibility alternatives cover essential operations, and downstream consumers can use MCS without inventing parallel map-generation/cartography systems.

No MCS implementation authority exists now. `operations/CURRENT.json` remains the sole live product selector.
