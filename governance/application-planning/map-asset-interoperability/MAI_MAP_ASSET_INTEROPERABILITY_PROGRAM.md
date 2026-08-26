# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01 COMPLETED_VERIFIED; MAI-02 IN_PROGRESS  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-01 — Ecosystem, Format, License & Authority Survey  
**Current item:** MAI-02 — Canonical Map Asset, Placeable & Package Schema  
**Implementation branch:** `integration/mai-02-canonical-map-asset-placeable-package-schema`  
**Implementation authority:** MAI-02 only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

**MAI-01** remains `completed_verified` on application PR **#312**, merged as `82dc4c8838876e66361b942f0243a63f3b1f20d8` after exact-head Repository Health and governed self-hosted Linux/Windows deterministic validation.

Owner **Continue** on 2026-08-25 America/Chicago freshly verified exact AIOC `bfcea52308b53d5f328fe350042f6a78fdc00b59` and application `82dc4c8838876e66361b942f0243a63f3b1f20d8`, re-read the completed MAI-01 survey and this program/backlog, resolved the MAI-02 schema/authority evidence set, and governed-started **MAI-02**.

MAI-02 alone may implement on `integration/mai-02-canonical-map-asset-placeable-package-schema`. MAI-03 and later tranches remain unauthorized.

## MAI-01 binding predecessor contract

MAI-02 consumes, but may not weaken, the MAI-01 survey foundation:

- 14 provider-neutral visual/map source classes;
- 10 explicit license-evidence classes;
- 6 authority-crosswalk concerns;
- 5 explicit incomplete-pack outcomes;
- canonical vendor/editor: none;
- license permission inference: forbidden;
- silent unsupported-metadata discard: forbidden;
- silent missing-asset invention: forbidden;
- artwork/maps/coordinates becoming World/combat truth: forbidden.

## MAI-02 resolved owner evidence

Three owner surfaces bound the schema before implementation:

1. **MAI-01 survey registry** — source classes, permission evidence, incomplete-pack outcomes and unsupported-metadata requirements remain provider-neutral and explicit.
2. **MIB-11 / D18 World** — canonical World/location identity, hierarchy, topology, navigation/transfer edges, availability/discovery and canonical World state remain outside MAI. MAI geometry and artwork are projection/presentation metadata only.
3. **D29 authoring-provenance** — governed payloads remain in established owning domains and are referenced by stable IDs/versions/provenance. MAI-02 may carry asset/source/checksum/license/evidence/import lineage but may not promote non-owner records to canonical World truth.

No durable persistence delta is required by the bounded contract/schema tranche, so migration `0022` remains unreserved.

## MAI-02 implementation contract

MAI-02 may define stable vendor-neutral contract records and relationships for:

- `MapAsset`;
- `Tile`;
- `TerrainSet`;
- `ObjectAsset`;
- `Module`;
- `Battlemap`;
- `Layer`;
- `Placeable`;
- package/source/provenance records.

The schema may express identity, dimensions, transforms, anchors, grid descriptors, elevation metadata, variants, animation descriptors, dependencies, source/checksum/license/evidence/import lineage and explicit unsupported-source metadata.

### Required boundaries

- Geometry descriptors are data, not the MAI-03 coordinate/projection engine.
- Terrain relationships are data, not MAI-04 autotile/connectivity mechanics.
- Layer/placeable records are data, not MAI-05 occlusion or interactive-geometry runtime ownership.
- Source/import lineage is data, not the MAI-06 adapter framework.
- Dependency and semantic-requirement references are data, not MAI-07 availability/substitution resolution.
- No MAI-08 workbench UI, MAI-09 runtime owner integration or MAI-10 corpus/performance work is authorized.
- World, Scene/tabletop, Combat/Exploration, visibility/permissions and authoring-provenance owners are referenced by stable external IDs; MAI-02 does not mutate their truth.
- License permissions remain evidence-driven. Unknown/unverified rights remain unresolved.
- Unsupported source metadata is preserved/reported explicitly rather than silently discarded.
- Semantic requirements remain separable from the visual asset chosen to satisfy them.

## Critical incomplete-pack rule

No tileset or asset package is assumed complete. Schema records must be able to represent a semantic requirement separately from any selected art and preserve the five MAI-01 outcomes: exact compatible asset, compatible permitted cross-pack asset, manual GM/user selection, explicitly approved placeholder, or visibly unresolved. MAI-02 records these states/references only; automatic resolution remains MAI-07 work.

## Validation contract

MAI-02 requires focused schema/contract validation plus predecessor/owner regression coverage for MAI-01 and MIB-11/D18 World. The exact candidate head must then pass application Repository Health, self-hosted Linux and Windows Validation Core, and deterministic cross-platform comparison before merge.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `in_progress`
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

- MAI-01 has no further implementation authority.
- MAI-02 authority is tranche- and branch-bounded.
- MAI-03+ have no implementation authority.
- Missing art never blocks theater-of-the-mind/non-map play.
- No pack is assumed complete.
- Semantic requirement and chosen visual asset remain separable.
- MIB-11/D18 World and D29 authoring-provenance owner truth is not mutated by MAI-02.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
