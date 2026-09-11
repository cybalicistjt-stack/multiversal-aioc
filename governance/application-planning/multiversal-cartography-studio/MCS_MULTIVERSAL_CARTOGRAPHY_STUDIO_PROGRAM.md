# MCS — Multiversal Cartography Studio

**Program ID:** MCS  
**Program name:** Multiversal Cartography Studio  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after PCA-16  
**Successor:** SMB-08  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** none

## Purpose

MCS makes Multiversal capable of creating finished world, regional, settlement, city, dungeon, interior, tactical, scene, isometric and atlas maps inside the product at a quality and flexibility comparable to dedicated cartography tools, while going beyond them by preserving optional semantic links to the actual playable World, Scene, Exploration, Combat, Settlement, Route, Discovery and other owner-domain records.

MCS is not a replacement canonical World model and it does not make artwork authoritative gameplay truth. It is the map-specific authoring, procedural generation, precision editing, styling, structured interchange and semantic-binding layer over the already completed or planned Multiversal foundations.

## Product target

A creator should be able to make the kinds of maps currently produced with specialist world generators, fantasy cartography applications, dungeon/battlemap editors and vector/raster design tools without leaving Multiversal for ordinary map-production work.

A map element can remain presentation-only or, when the owning domain permits it, bind explicitly to canonical game/world semantics. The distinction must always be visible and reversible.

Examples:

- a painted road may remain artwork or bind to a canonical route;
- a settlement symbol may remain a decorative marker or reference a canonical settlement;
- a forest region may remain a texture/mask or bind to environment/biome records;
- a dungeon entrance may link to another map/scene/location without inventing topology;
- a door may carry presentation geometry while Scene/Combat/Visibility retain runtime authority;
- fog may be manually authored for presentation or projected from campaign/party discovery state where the owning system supplies that state.

## Placement

MCS is a future interstitial program:

`SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10`

Rationale:

1. PCA supplies reusable procedural, texture/material, style-generation and production-recipe primitives that MCS can consume rather than rebuilding.
2. MCS then supplies the human-facing cartography studio before SMB-08 begins substantial first-party library/content production.
3. SMB-08/09 and later SAA can therefore consume finished map-authoring, generator, atlas and export workflows.
4. MCS does not change the current ARI family, current work pointer or implementation authority.

## Benchmark provenance and clean-room boundary

Planning benchmark set:

- Inkarnate
- Azgaar's Fantasy Map Generator
- Wonderdraft
- Dungeondraft
- DungeonFog
- Affinity
- Inkscape
- Campaign Cartographer 3+ / Fractal Terrains-class workflows

The detailed benchmark is recorded in `MCS_BENCHMARK_CAPABILITY_MATRIX.md`.

MCS follows the existing PCM clean-room rules. It studies public product documentation, lawful ordinary-use behavior, documented interchange formats and observable workflows to identify capability requirements. It does not copy proprietary source, protected assets, distinctive UI expression, private protocols, sample projects or vendor-specific implementation details.

Vendor names are planning provenance only and do not become Multiversal product identity.

## Local-first / non-reimplementation boundary

MCS owns the Multiversal-specific cartography experience, semantic binding, deterministic document/recipe model, validation, provenance, accessibility and game-aware authoring.

It does **not** attempt to recreate a full general-purpose Affinity/Inkscape/CAD/GIS/DCC suite. Generic vector/raster geometry, image processing, font shaping, color management, codecs, GIS transforms and similar commodity capabilities should use lawful mature libraries or local tools behind replaceable boundaries when practical.

The in-app precision studio implements the bounded map-production subset required to finish maps without external software. External round-trip remains supported for advanced specialist workflows.

## Upstream ownership and reuse

MCS consumes rather than duplicates:

- **ARI:** resource identity, content-addressed bytes, derivative lineage, rights/use capability, tagging, query and asset picking.
- **MAI:** MapAsset/Tile/TerrainSet/ObjectAsset/Module/Battlemap/Layer/Placeable records, projection, grid/coordinate/scale, autotile/connectivity, descriptive geometry, import adapters, resolver and composer foundations.
- **ISE / Scene / Tabletop:** live scene canvas, placements, runtime scene state, interaction and camera/viewport semantics.
- **SSA:** semantic spatial authoring and construction semantics.
- **World / MIB-11 / later World owners:** location identity, hierarchy, topology, routes, transfer/navigation and canonical world state.
- **Exploration:** travel, discovery, environment, navigation, fog-of-war and encounter truth.
- **Combat:** movement, cover, range, collision, effects, hazards and tactical adjudication.
- **Visibility/Permissions:** hidden state, audience projection, GM-only material, occlusion/LOS authorization.
- **Settlement/Kingdom/Faction/Economy:** settlements, districts, political territory, routes, trade and related canonical state.
- **D29 authoring/provenance:** governed publication and provenance.
- **PCA:** production recipes, procedural graph execution, spatial/environment generators, texture/material pipeline and style-locked generation.
- **VTI:** provider-neutral structured scene/map/token projection and external VTT interoperability.

MCS may create presentation documents, reversible authoring drafts, generated proposals, map-specific derived assets, structured export packages and binding proposals. It cannot silently promote those outputs into canonical owner state.

## Core architectural doctrine

### One map document, multiple authoring modes

World Generator, Cartography Studio, Dungeon/Tactical Studio and Precision Studio operate over one versioned Multiversal cartography document. They are not separate formats.

The document supports:

- stable object/layer IDs;
- vector and raster layers;
- symbols/placeables;
- map-specific procedural recipes and seeds;
- transforms, masks, brushes, fills and effects;
- text/label objects;
- grids/projections/calibration;
- style/theme references;
- semantic-binding references;
- owner-domain projection references;
- history/version/provenance;
- structured unsupported-extension retention.

### Presentation is not game truth

Every map element has an explicit authority disposition such as:

- `presentation-only`;
- `bound-readonly`;
- `binding-proposal`;
- `owner-projected`;
- `runtime-derived`;
- `unresolved`.

Pixels, vectors, imported vendor fields or procedural output never silently create World topology, route existence, collision, visibility, diplomacy, population, economy or other canonical facts.

### Deterministic where practical, artistic where appropriate

Procedural operations expose stable seeds/parameters and reproducible receipts. Freehand artistic edits remain ordinary user edits with version/provenance history rather than pretending to be algorithmically reproducible.

## Program tranches

### MCS-01 — Cartography Document, Workspace & Authority Contract

Define the unified versioned cartography document, stable object/layer identity, presentation-vs-semantic authority states, map-type metadata, version/provenance model, undo/history contract, extension namespaces and explicit owner references. Reuse MAI records rather than minting a second asset ledger.

### MCS-02 — Large-Map Canvas, Renderer, Viewport & Tile Cache

Implement the map-specific canvas/render surface for pan/zoom/rotation, large documents, multi-resolution raster/vector presentation, culling, viewport tiling, cache invalidation and deterministic export composition. Establish performance tiers without requiring whole-map rasterization or whole-library memory residency.

### MCS-03 — Selection, Transform, Snapping, Guides & Editing History

Implement single/multi/range selection, move/scale/rotate/flip, alignment/distribution, rulers/guides, square/hex/isometric snapping, object snapping, keyboard movement, copy/duplicate/group/lock and reversible edit history.

### MCS-04 — Precision Vector Geometry & Path Studio

Implement map-bounded vector authoring: pen/path creation, node/handle editing, Bézier and polyline tools, shapes, stroke/fill, boolean operations, offsets/expansion where justified, clipping paths, map-specific contour editing and SVG-compatible structural representation. Do not become a general-purpose DCC/CAD clone.

### MCS-05 — Raster Brush, Mask, Texture & Blend Studio

Implement pressure-capable raster/texture brushes, erase, masks, textured fills, gradients, pattern fills, blend/opacity controls, non-destructive adjustments required for cartography, tileable texture handling and bounded image-to-vector/selection helpers where lawful libraries provide them.

### MCS-06 — Symbols, Stamps, Scatter, Brushes & Reusable Components

Build the ARI/MAI-backed palette for symbols, props, vegetation, mountains, buildings and modular pieces; searchable tags/families; custom art; brush-along-path placement; density/randomization controls; smart scatter; reusable grouped components; and deterministic seeded distribution where requested.

### MCS-07 — Typography, Labels, Legends, Frames & Atlas Navigation

Implement map labels, path-following text, presets/styles, collision/placement assistance, legends, keys, scale bars, coordinate labels, frames, title blocks, compass/navigation ornaments as replaceable assets, hyperlinks/cross-map links and campaign-atlas navigation.

### MCS-08 — Landmass, Coastline, Terrain & Elevation Authoring

Implement land/water painting, coastline sculpting and smoothing, terrain regions, contour/elevation fields, cliff/ridge representation, terrain texture blending, erosion-style authoring operations where provided by PCA/local workers, and style-preserving regeneration limited to selected regions.

### MCS-09 — Rivers, Lakes, Roads, Paths, Borders & Network Authoring

Implement artistic and precision water/path/network tools with confluence/coast connection behavior, variable width/style, bridges/fords/passages, roads/trails, political/administrative borders and optional binding proposals to canonical route/territory owners. Visual connectivity alone remains noncanonical.

### MCS-10 — Seeded Procedural World Generator Core

Build deterministic world-generation recipes over PCA primitives: configurable world extent/projection, height/elevation synthesis, land/ocean distribution, editable generation masks, region locks, partial regeneration, stable seeds and reproducible receipts. Generated geography remains proposal/presentation until accepted by World owners.

### MCS-11 — Hydrology, Climate, Biome & Resource Generator

Generate/edit river basins, lakes, drainage, temperature/precipitation fields, climate/biome regions and resource-placement proposals from explicit input models. Every generated field remains inspectable, overrideable and separately promotable; no hidden universal simulation assumptions.

### MCS-12 — Population, Settlement, Culture, State, Route & Trade Proposal Generator

Use owner-domain inputs to propose population distribution, settlement candidates, cultural/language/religion regions where applicable, political/state/province candidates, routes and trade networks. Each category has independent enable/disable, regeneration and acceptance controls; MCS cannot create canonical social/economic truth by drawing it.

### MCS-13 — Settlement, City, District & Street Cartography

Implement settlement-scale map authoring and generation: districts, blocks, lots, streets/alleys, walls, gates, waterways, building footprints, landmarks, service/resource markers, density patterns and reusable urban styles. Existing Settlement/Kingdom data may seed/bind the map without being duplicated.

### MCS-14 — Dungeon, Cave, Interior & Multi-Level Builder

Implement room/wall/floor tools, connected passages, doors/windows/openings, cave/tunnel generation, stairs/ladders/elevators, roofs/overheads, object placement, reusable room templates, level/floor management, blueprint/reference tracing, secret/GM layers and deterministic dungeon/cave recipes.

### MCS-15 — Tactical Scene, Lighting, Fog, Elevation & Hazard Authoring

Provide square/hex/gridless tactical maps, measurement/calibration, templates, spawn/waypoint zones, cover/elevation annotations, hazards, light-source authoring, wall/door occlusion geometry and fog painting/preview. Runtime LOS, collision, cover and visibility remain owned by their current systems; MCS authors inputs/proposals and previews rather than adjudicating them.

### MCS-16 — Isometric, Deck-Plan, Section & Multi-Level Projection

Support isometric/staggered presentation, vertical level relationships, building/deck sections, stacked floors, cutaway/roof presentation, elevation-aware symbols and map-specific lightweight extrusion/projection where useful. Full general 3D terrain/DCC authoring remains outside MCS.

### MCS-17 — Styles, Themes, Templates, Color Grading & Publishing Layout

Implement reusable map styles/themes, semantic style tokens, terrain/symbol/text presets, template documents, color grading, shadow/glow/blur/effect stacks, print/page layouts, export profiles and user-created style packs. No proprietary vendor style/art may be copied.

### MCS-18 — Semantic Binding, World Sync & Discovery/Fog Projection

Implement explicit binding workflows between map elements and existing owner records: locations, regions, settlements, routes, environments, factions/territories, scenes, portals, discoveries and other supported entities. Provide stale-binding detection, owner-version references, projection refresh, map-only override handling and governed binding proposals. Support party/campaign discovery projections without revealing hidden truth.

### MCS-19 — Structured Import/Export, Round-Trip & Campaign Atlas

Support high-resolution PNG/JPEG, SVG/PDF where representable, structured Multiversal map packages, documented VTT/UVTT-class interchange through VTI/MAI, GeoJSON-class exchange where appropriate, custom asset packages, print-at-scale output, external-editor round-trip and linked campaign/world atlas packaging. Unsupported source semantics are reported/preserved rather than silently flattened.

### MCS-20 — Collaboration, Review, Versions & Publishing Workflow

Implement safe multi-user authoring semantics appropriate to Multiversal: edit/review states, comments/annotations, conflict detection, version comparison, branch/copy workflows, locks where needed, proposal/approval, publish/archive, permission-aware GM/player projections and recovery. Reuse existing identity/permission/provenance infrastructure.

### MCS-21 — Golden Cartography Capability & Semantic-Integration Proof

Create an original Multiversal golden suite proving at least:

1. world map;
2. regional map;
3. settlement/city map;
4. dungeon/interior multi-level map;
5. tactical battlemap;
6. scene/isometric or deck-plan map;
7. linked campaign atlas.

The proof must demonstrate generator→manual-edit continuity, precision vector/raster editing, custom assets, styles/templates, large-map performance, high-resolution and structured export, offline/local-first blocking workflows, accessibility alternatives, deterministic procedural receipts, rights/provenance, import-loss reporting and at least one explicit presentation-only vs canonical-bound comparison.

## Cross-cutting requirements

Every MCS tranche must preserve:

- undo/redo and recovery appropriate to its mutations;
- keyboard/touch alternatives and non-pointer-only workflows;
- screen-reader/list/structured alternatives for essential map state;
- high-contrast/non-color-only semantic indicators;
- responsive review on smaller screens, with desktop/tablet as primary authoring targets;
- offline/local-first operation for blocking core authoring where practical;
- exact rights/provenance through ARI;
- deterministic procedural receipts where generation is claimed deterministic;
- unsupported/unresolved states instead of silent flattening or guessing;
- performance budgets appropriate to large maps and large asset libraries;
- world/campaign-specific styles without allowing them to break core usability.

## Explicit non-goals

MCS does not:

- replace World, Scene, Combat, Exploration, Visibility, Settlement, Economy or other canonical owners;
- create canonical facts from pixels, vectors, labels or generator output;
- recreate a general Photoshop/Affinity/Inkscape/CAD/GIS/Blender-class application;
- copy proprietary vendor assets, styles, UI layouts or implementation;
- require a paid mapping service for blocking workflows;
- make external VTTs authoritative;
- implement unrestricted map scripting or unreviewed executable extensions;
- authorize provider credentials, paid spend, public release or tester distribution.

## Family execution rule

When MCS is eventually selected, it receives its own sealed family preflight. Every execution unit must target 24 active minutes or less under a healthy governed environment with protected closeout reserve. Any unit that cannot credibly fit is split before governed start.

No MCS implementation authority exists now.

## Completion standard

MCS is complete only when all 21 tranches are `completed_verified`, the golden suite proves the required map classes and semantic-boundary behavior, blocking map creation works without paid/cloud mapping providers, structured and flattened exports preserve declared fidelity/provenance, large-map interaction meets its declared performance tiers, accessibility alternatives exist for essential operations, and SMB-08 can consume the studio without inventing a parallel map-generation or cartography system.
