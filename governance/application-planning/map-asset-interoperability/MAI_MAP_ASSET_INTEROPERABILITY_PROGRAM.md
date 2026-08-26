# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01  
**Activation:** DPL-14 completed_verified  
**Current item:** MAI-01 — Ecosystem, Format, License & Authority Survey  
**Implementation branch:** `integration/mai-01-ecosystem-format-license-authority-survey`  
**Implementation authority:** MAI-01 only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

Owner **Continue** on 2026-08-25 freshly verified exact AIOC `7d4600f76d4677c2b775cbca1d84bcdaca2d5ff5` and application `8f4c4aca8e264233284dc631ada807476937176a`, re-read this program/backlog and the retained recovered visual provenance, and governed-started **MAI-01**.

The retained `Now this.zip` archive remains a governed provenance input, not work-selection authority. Its exact SHA-256 is `2a5eae712f483d1fb33ff9fb0087e96c4eb8b71b287cc707c196a4c17a2f78f4`. RSR-01 inventories 12 unique embedded media objects, 11 substantive. Those visuals remain bound to their original source files/checksums and are evidence, not automatically canonical map assets.

## MAI-01 governed survey contract

MAI-01 is a source/ecosystem/authority tranche. It may create survey evidence, format/source-class records, license/provenance classifications, owner-boundary crosswalks and focused validation. It may not implement MAI-02 schema/importer mechanics.

Required coverage:

- raw raster/vector image assets and image collections;
- sprite sheets/atlases;
- autotiles and tilemap ecosystems;
- modular rooms/pieces and props/overheads;
- complete and layered battlemaps;
- animated visual assets;
- square/gridless/hex/isometric-oriented source sets where ecosystem metadata exists;
- structured editor/VTT exports, including explicit handling of unsupported metadata;
- source/license/provenance and permission evidence;
- map/art/coordinates versus World/Scene/Combat authority boundaries;
- GM/player visibility and hidden-layer boundaries;
- incomplete-pack behavior, manual override, placeholders and visibly unresolved requirements.

External ecosystem claims must be grounded in current authoritative vendor/standard/license documentation. MAI-01 must not infer redistribution, transformation or commercial permissions when the source license does not explicitly grant them.

## Critical incomplete-pack rule

No tileset or asset pack is expected to contain every semantic object Multiversal can represent. Semantic scene requirements remain separate from selected art. Resolution may use an exact compatible asset, a compatible permitted asset from another installed pack, GM/user choice, an explicitly approved placeholder, or a visibly unresolved state. Missing or incompatible art is never silently invented or treated as semantic truth.

## Authority rules

- No creator/vendor/editor is the canonical Multiversal map model.
- Artwork, map coordinates and camera/view state are projection/presentation resources, not World or combat identity truth.
- World/location identity remains with established World/Scene owners.
- Combat/exploration state remains with its established owners.
- Hidden/GM-only layers remain permission-scoped.
- License/source/provenance metadata is preserved.
- Permission is evidence-driven and conservative; silence is not permission.
- Manual GM/user asset assignment remains first-class.
- Partial structured imports must surface unsupported/lost semantics rather than silently discarding them.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `in_progress`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `planned`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `planned`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `planned`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `planned`
6. **MAI-06 — Universal Import Adapter Framework** — `planned`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `planned`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Downstream relationship

AAI follows MAI so provider-neutral asset/provenance patterns can be reused for audio without merging visual and audio ownership. ISE later consumes completed MAI + AAI for native tabletop/canvas experience.

## Invariants

- MAI-01 authority is tranche- and branch-bounded.
- MAI-02+ have no implementation authority.
- Missing art never blocks theater-of-the-mind/non-map play.
- No pack is assumed complete.
- Semantic requirement and chosen visual asset remain separable.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
