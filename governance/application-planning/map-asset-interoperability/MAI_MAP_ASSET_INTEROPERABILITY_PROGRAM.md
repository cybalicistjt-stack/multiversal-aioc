# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..02 COMPLETED_VERIFIED; MAI-03 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-02 — Canonical Map Asset, Placeable & Package Schema  
**Current item:** MAI-03 — Grid, Coordinates, Scale & Projection Engine  
**Implementation branch:** none  
**Implementation authority:** none until future owner Continue governed-starts MAI-03  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

**MAI-01** remains `completed_verified` on application PR **#312**, merged as `82dc4c8838876e66361b942f0243a63f3b1f20d8`.

**MAI-02** is `completed_verified` on application PR **#313**. Repaired exact head `994bf0f5551e5d04239978d3728360f94bcb20a1` passed application Repository Health plus governed self-hosted Linux/Windows Validation Core and deterministic comparison, then squash-merged as `78c07e2102fdf6a7939a00a47b58e25150e66018`. The matching deterministic receipt was `83c5404498405dcce6efcfe9b75e8c5c1b9428f0b1e922328857b3426d0b5e07`. Repair cycles: **1**, limited to Validation Core failure-blame metadata.

Strict MAI order now selects **MAI-03** only. MAI-03 has no implementation branch and no implementation authority until a future owner **Continue** freshly verifies canonical AIOC/application heads, re-reads the completed MAI-01 survey and MAI-02 schema/evidence plus owner boundaries, resolves the exact grid/coordinate/scale/projection contract, and governed-starts MAI-03.

## Binding completed foundation

MAI-01 and MAI-02 together establish the provider-neutral source, license, authority and canonical schema foundation:

- 14 provider-neutral visual/map source classes;
- 10 explicit license-evidence classes;
- 6 authority-crosswalk concerns;
- 5 explicit incomplete-pack outcomes;
- canonical vendor/editor: none;
- vendor-neutral records for `MapAsset`, `Tile`, `TerrainSet`, `ObjectAsset`, `Module`, `Battlemap`, `Layer`, `Placeable` and package/source/provenance;
- source/checksum/license/evidence/import lineage and unresolved permission state are explicit;
- unsupported source metadata is preserved/reported rather than silently discarded;
- semantic requirements remain separate from selected visual assets;
- no tileset or asset package is assumed complete.

MAI-02 deterministic proof covers 2 source records, all 6 canonical asset kinds, 3 layers, 4 placeables and all 5 incomplete-pack outcomes.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location identity, hierarchy, topology, navigation/transfer edges and canonical World state. MAI artwork, geometry, coordinate, scale and projection records do not become World truth.
- **D29 authoring-provenance** retains governed publication/provenance workflow. MAI references stable owner IDs/versions/provenance and does not mutate owner-domain truth.
- Existing Scene/tabletop and Combat/Exploration owners retain runtime gameplay truth.
- Hidden/GM-only layers remain permission-scoped.
- License permissions remain evidence-driven; silence is not permission.
- Manual GM/user asset assignment remains first-class.
- Missing art never blocks theater-of-the-mind/non-map play.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.

## MAI-03 selection contract

MAI-03 may eventually implement the grid, coordinate, scale and projection engine over the completed MAI-02 schema. A future governed start must resolve the exact contract before mechanics are written.

Selection-time requirements:

- consume MAI-02 dimensions, transforms, anchors and grid descriptors rather than redefining asset identity;
- support provider-neutral grid/coordinate/scale/projection concepts without making Tiled, LDtk, Foundry or another ecosystem canonical;
- preserve World/combat authority separation: a map coordinate or projection never creates canonical World/location or combat identity;
- preserve MAI-01/02 license, provenance, unsupported-metadata and incomplete-pack rules;
- keep semantic requirements separate from selected visual assets;
- do not implement MAI-04 autotile/connectivity grammar, MAI-05 runtime geometry, MAI-06 adapters, MAI-07 resolver automation, MAI-08 workbench, MAI-09 runtime integration or MAI-10 corpus/performance work from selection state.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `selected_not_started`
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

- MAI-01 and MAI-02 have no further implementation authority.
- MAI-03 is selection-only until a future owner Continue governed-starts it.
- MAI-04+ have no implementation authority.
- No vendor/editor or source format is canonical Multiversal map truth.
- No pack is assumed complete; semantic requirement and chosen visual asset remain separable.
- MIB-11/D18 World and D29 authoring-provenance owner truth is not mutated by MAI.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
