# MCS Benchmark Capability Matrix

**Program:** MCS — Multiversal Cartography Studio  
**Checked:** 2026-09-11  
**Purpose:** clean-room capability/workflow benchmark only  
**Implementation authority:** none

## Rule

The products below are references for user-visible capabilities and workflow outcomes, not implementation sources. MCS must independently implement Multiversal-specific behavior from existing owner contracts and lawful reusable components. It must not copy proprietary source, protected art/assets, distinctive UI expression, private protocols or branded styles.

## Benchmark products

| Product | Public source checked | Capability classes retained as requirements |
|---|---|---|
| Inkarnate | https://inkarnate.com/ and https://inkarnate.com/faq | approachable world/region, city/village, battle/interior, scene/isometric map creation; line/shape tools; large asset catalog; custom art; high-resolution output |
| Azgaar's Fantasy Map Generator | https://azgaar.github.io/ | seeded/generated world workflow; independently editable structured layers; SVG/image output; GeoJSON and JSON export; routes/rivers/zones/cells structured exchange |
| Wonderdraft | https://wonderdraft.net/ | generated/painted landmasses, beautified coastlines, rivers/roads, grouped mountain/tree placement, themes, label presets, large offline maps |
| Dungeondraft | https://dungeondraft.net/ | fast tactical workflow, smart tiling, object scattering, terrain painting, lighting, dungeon/cave generation, object tagging, Universal-VTT-oriented export |
| DungeonFog | https://www.dungeonfog.com/ and https://www.dungeonfog.com/foundry/ | vector room/building/terrain editor, multi-level maps, doors/passages, asset placement, lighting, templates, fog/play workflows, structured VTT export retaining walls/doors/windows/lights |
| Affinity | https://www.affinity.studio/graphic-design-software | precision curve/path editing, shape construction, bitmap/pattern/gradient fills, image tracing, non-destructive editing, typography and raster/vector crossover |
| Inkscape | https://inkscape.org/ and https://inkscape.org/en/develop/about-svg/ | open SVG-native vector editing, paths/shapes/text/fill/stroke, gradients/patterns, clipping/masking/compositing, metadata and broad structured interchange |
| Campaign Cartographer 3+ / ProFantasy ecosystem | https://www.profantasy.com/products/campaign-cartographer-3 and https://www.profantasy.com/collections | world/city/dungeon mapping, drawing tools, symbols/fills, layers/sheets/effects, square/hex grids, real-world scale, vector output, linked maps/interactive atlas, procedural terrain companion workflows |

## Consolidated MCS capability targets

### A. Easy artistic cartography

MCS must let a non-illustrator produce attractive maps using presets, brushes, terrain tools, stamps/symbols, scatter, textures, labels, themes and templates without requiring precision-vector expertise.

### B. Procedural world generation

MCS must support deterministic seeded generation, editing and partial regeneration for geography and governed proposal layers such as hydrology, climate/biomes, settlements, political regions and routes. Generated outputs must remain separately reviewable/promotable.

### C. Tactical/dungeon construction

MCS must support room/wall/floor/door/window/cave tools, multi-level maps, objects, roofs/overheads, lighting authoring, fog, grid calibration, tactical annotations and structured VTT exchange.

### D. Precision finishing

MCS must support the map-specific vector/raster subset needed for professional finishing: paths/nodes, shapes, booleans, snapping/guides, masks/clipping, gradients/patterns/textures, effects, typography, rulers and print/export layouts.

### E. Structured/open interchange

MCS must preserve structure where the source/export supports it. It must not silently flatten layers, geometry, links, provenance or semantic references merely because raster export is also available.

### F. Custom assets and reusable styles

Creators must be able to ingest authorized custom art, build reusable map components, create style/theme/template packs, and use ARI/MAI discovery rather than depending on a single vendor catalog.

### G. Large-map / publication output

MCS must support large interactive maps through viewport/tile/caching strategies and high-resolution/print-at-scale exports without requiring the entire document to be flattened at working resolution.

### H. Multiversal semantic advantage

Unlike a conventional map maker, MCS supports explicit links between presentation objects and canonical owner-domain records while preserving authority boundaries. The same visual document can therefore serve as an illustration, authoring surface, exploration map, tactical map or world/atlas projection without becoming a duplicate game-state database.

## What is deliberately not copied

- vendor branding, art packs, sample maps or proprietary styles;
- exact vendor UI layouts or iconography;
- proprietary project formats unless publicly documented and lawfully interoperable;
- undocumented service APIs/protocols;
- vendor-specific algorithms or reverse-engineered generation logic.

## Acceptance implication

MCS-21 must prove capability coverage across the consolidated targets above using original Multiversal content and Multiversal-owned contracts. Exact visual imitation of any benchmark product is not an acceptance criterion.

MCS does not copy proprietary source, protected assets, sample projects, distinctive product-facing expression, private protocols or vendor-specific implementation details.
