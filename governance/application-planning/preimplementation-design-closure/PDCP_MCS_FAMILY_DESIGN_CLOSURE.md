# PDCP — MCS Family Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Family:** MCS — Multiversal Cartography Studio  
**Status:** design_closed_for_family_reduction  
**Implementation authority:** none  
**Baseline:** 21 tranches  
**Reduced implementation/proof shape:** 12 tranches  
**Capability loss detected:** no

## Closure decision

MCS remains Multiversal's map-specific creator for world, regional, settlement, city, dungeon, interior, tactical, isometric and atlas cartography. It is not a second World model, Scene runtime, spatial-law engine, built-environment simulator, procedural-generation platform, provenance/review platform, or general-purpose CAD/GIS/DCC application.

The reduction keeps distinct implementation kernels where editing mode, map scale or owner binding materially changes the work, while folding seams that share the same map-document/editor/generator/interchange substrate and returning generic infrastructure to existing owners.

## Owner boundaries locked

- MAI retains canonical map-asset/package schemas, projection/grid/coordinate/scale, autotile/connectivity, descriptive geometry, resolver/composer and import-adapter foundations.
- ISE/Scene/Tabletop retain live scene canvas, placement, runtime interaction, camera and scene-state authority.
- SSA retains semantic spatial authoring/construction semantics.
- World/Environment/Exploration/Settlement/Kingdom/Faction/Economy/Visibility/Combat retain their canonical truth.
- PCA-02/PCA-03 retain generic procedural DAG/recipe/seed/cache and terrain/ecology/flora/settlement/spatial generator primitives. MCS supplies map-specific generator configuration, preview, proposal and manual-edit continuity.
- PCA-12/Packet 08 retain generic simulation/graph/solvability/optimization machinery. MCS may provide map/spatial analysis adapters and interpret results for cartographic workflows only.
- ARI/PCA retain generic resource identity, rights/provenance, derivative lineage, version/review/locking and import/export governance.
- Packet 07 retains generic preview/dry-run/explanation/recovery/collaboration semantics. MCS supplies map-domain operations and lenses.
- reduced MBES retains built-environment/facility truth; reduced MSLR retains spatial-law runtime; reduced MSWI retains systemic consequence propagation.

## Intra-family folding

### MCS-01 absorbs MCS-02
The unified cartography document/workspace and large-map canvas/renderer/viewport/tile-cache are one application shell. The document identity, authority states, viewport, culling, tiling, cache invalidation and export composition must share one document/render lifecycle.

### MCS-03 absorbs MCS-04
Selection, transform, snapping, guides, history and precision vector/path editing are one precision-object editing kernel. Map-bounded vector geometry remains distinct from raster painting but does not require its own standalone tranche.

### MCS-05 absorbs MCS-06
Raster brushes/masks/textures/blends and symbols/stamps/scatter/reusable components share one paint/place/scatter asset-authoring substrate over ARI/MAI resources, with deterministic seeded placement where claimed.

### MCS-07 absorbs MCS-17
Typography, labels, legends, frames, atlas navigation, styles, themes, templates, color grading and publishing layouts form one map-presentation/layout/profile kernel. PCA/ARI retain generic style-generation and asset/provenance infrastructure.

### MCS-08 absorbs MCS-09
Landmass/coastline/terrain/elevation and rivers/lakes/roads/paths/borders/networks share one geographic-feature authoring substrate: editable fields, paths/networks, regional masks and owner-binding proposals. Canonical routes, territory and hydrology remain owner-controlled.

### MCS-10 absorbs MCS-11 and MCS-12
All map-facing procedural world proposals use the same PCA recipe/seed/cache substrate. MCS implements one map-specific generator workbench with independently switchable/promotable packs for geography/elevation, hydrology/climate/biome/resources, and population/settlement/culture/state/routes/trade proposals. Generic generation execution stays PCA-owned; each proposal category remains independently previewable, regenerable, rejectable and owner-promotable.

### MCS-13 remains
Settlement/city/district/street cartography has a distinct urban authoring UX and semantic binding surface even though built-environment truth stays with Settlement/MBES owners.

### MCS-14 absorbs MCS-16
Dungeon/cave/interior/multi-level authoring and isometric/deck-plan/section/cutaway projection share one room/level/vertical-relationship implementation kernel. Runtime topology and 3D truth remain external.

### MCS-15 remains
Tactical-scene calibration, light/fog/elevation/hazard authoring and preview is a distinct map-authoring seam over ISE/Scene/Combat/Visibility owners.

### MCS-18 remains
Semantic binding, owner-version sync, discovery/fog projection and map-only override handling are central cross-owner adapters and require a dedicated tranche.

### MCS-19 absorbs MCS-20
Structured map interchange, external round-trip, campaign-atlas packaging, map-specific review/version/conflict/publish workflows and loss reporting are one lifecycle seam. Generic rights/provenance/version/review/collaboration infrastructure stays ARI/PCA/Packet 07.

### MCS-21 remains
The final golden proof retains all map classes, generation→manual-edit continuity, large-map performance, accessibility, deterministic receipts, provenance, interchange-loss, offline/local-first and presentation-vs-canonical proof obligations.

## Reduced surviving tranches

1. `MCS-01` — Cartography Workspace, Document, Large-Map Canvas, Viewport & Authority Contract
2. `MCS-03` — Precision Selection, Transform, Snapping, Vector Geometry, Paths & Edit History
3. `MCS-05` — Raster, Mask, Texture, Blend, Symbol, Stamp, Scatter & Reusable Component Studio
4. `MCS-07` — Typography, Labels, Legends, Styles, Themes, Templates, Atlas & Publishing Layout
5. `MCS-08` — Geographic Terrain, Elevation, Water, Route, Border & Network Authoring
6. `MCS-10` — Map-Specific Procedural World Proposal Workbench over PCA
7. `MCS-13` — Settlement, City, District & Street Cartography
8. `MCS-14` — Dungeon, Cave, Interior, Isometric, Deck-Plan, Section & Multi-Level Builder
9. `MCS-15` — Tactical Scene, Lighting, Fog, Elevation & Hazard Authoring
10. `MCS-18` — Semantic Binding, World Sync & Discovery/Fog Projection
11. `MCS-19` — Map Interchange, Round-Trip, Campaign Atlas, Review, Versions & Publishing
12. `MCS-21` — Golden Cartography Capability & Semantic-Integration Proof

## Cross-family absorptions

Historical `MCS-10` no longer implies a generic procedural graph/generator engine; PCA-02/PCA-03 own that substrate. Reduced `MCS-10` is map-specific configuration, preview, proposal, selective regeneration and acceptance UI over those capabilities.

Historical `MCS-20` no longer implies a generic collaboration/version/review/provenance platform. ARI/PCA/Packet 07 own that infrastructure. Reduced `MCS-19` keeps map-package serialization, atlas packaging, map-specific conflict/loss reporting, permission projections and publication adapters.

Historical `MCS-17` no longer implies a generic style-generation engine. PCA-09/ARI own reusable generation/resource governance; reduced `MCS-07` keeps cartographic style/profile/layout authoring.

MCS tactical, city, interior and semantic-binding tools remain projections/adapters over ISE/Scene/Combat/Visibility, MBES/Settlement, SSA/World and other canonical owners; pixels/vectors never become authoritative by themselves.

## Golden vectors

The reduced family must preserve at least these 48 proof vectors:

1. One cartography document supports world, regional, city, interior and tactical views without format forks.
2. Presentation-only map objects remain noncanonical.
3. Binding proposals cannot silently create World/Scene truth.
4. Large-map pan/zoom/rotation works without whole-map rasterization.
5. Viewport/tile cache invalidation follows document edits deterministically.
6. Precision selection and transforms preserve stable object IDs.
7. Grid/object snapping remains keyboard-accessible.
8. Vector path/node edits are reversible without rewriting canonical history.
9. Raster painting is nondestructive where the operation claims it.
10. Imported raster/vector resources retain ARI provenance.
11. Symbol/stamp/scatter placement uses MAI/ARI-backed assets.
12. Seeded scatter is reproducible where determinism is claimed.
13. Labels can follow paths without becoming route truth.
14. Legends/scale/frames remain presentation metadata unless explicitly bound.
15. Style/theme/profile switching does not rewrite semantic owner bindings.
16. Publishing layout and atlas navigation remain map presentation concerns.
17. Terrain/elevation authoring can remain presentation-only.
18. River/lake geometry does not create canonical hydrology by appearance alone.
19. Roads/paths/borders do not create canonical routes/territories by appearance alone.
20. Geographic owner bindings expose stale-version detection.
21. Procedural geography preview is noncanonical until accepted by an owner.
22. Generator seed/parameters produce reproducible receipts where claimed.
23. Hydrology/climate/biome/resource proposal packs can be independently enabled or rejected.
24. Population/settlement/culture/state proposals do not create social/world truth from map generation.
25. Route/trade proposals can be accepted independently from settlement proposals.
26. Partial regeneration respects locked regions/accepted owner-bound state.
27. City/district/street maps can bind Settlement records without duplicating Settlement truth.
28. Building footprints on a map do not become MBES facilities unless explicitly accepted by the built-environment owner.
29. Dungeon/interior room geometry can remain map presentation.
30. Multi-level stairs/elevators/links do not invent canonical transfer topology.
31. Isometric/deck/section projection derives from the same map document and level relationships.
32. Tactical lighting/fog preview cannot adjudicate runtime LOS/visibility.
33. Hazard annotations cannot apply Combat effects without owner operations.
34. Calibration/grid/elevation inputs remain explicit and inspectable.
35. Discovery/fog projection filters hidden truth before player-visible output.
36. Owner-version refresh reports binding conflicts instead of silently overwriting map-only edits.
37. Map-only overrides remain distinguishable from owner-projected values.
38. Structured export reports unsupported/lost semantics rather than flattening silently.
39. External round-trip preserves supported map identities and provenance.
40. VTI/MAI interchange remains provider-neutral and nonauthoritative.
41. Campaign atlas packaging preserves cross-map links and owner references.
42. Generic review/version actions resolve to ARI/PCA/Packet-07 infrastructure rather than a second MCS ledger.
43. Permission-aware review/export does not leak GM-only map state.
44. Blocking map authoring works with paid/cloud mapping providers disabled.
45. Keyboard/touch/list/screen-reader alternatives exist for essential map operations.
46. High-contrast/non-color-only cues preserve semantic distinctions.
47. Golden performance evidence covers declared large-map and asset-library budgets.
48. Golden suite proves world, regional, settlement/city, dungeon/interior, tactical, isometric/deck and linked-atlas workflows with explicit presentation-only versus canonical-bound comparisons.

## Residual implementation mapping

- PCA-02/PCA-03/PCA-09/PCA-12: generic generation, style-generation and analysis substrate.
- ARI/PCA/Packet 07: generic rights/provenance/version/review/collaboration/recovery substrate.
- MAI/ISE/SSA/VTI and canonical World/Scene/Combat/Visibility/Settlement/MBES/MSLR owners: schemas/runtime/spatial truth.
- MCS survivors: cartography-document UX, map-specific editing/generator packs, cartographic projections/bindings, map interchange/lifecycle adapters and final proof.

## DAG / OPS3

`MCS-21` survives with equivalent-or-stronger golden semantics and remains the MSLR start requirement plus relevant specialist golden proof. No DAG mutation is required. PDCP grants no implementation authority and does not mutate `operations/CURRENT.json`.
