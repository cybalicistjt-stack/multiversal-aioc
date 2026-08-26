# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..02 COMPLETED_VERIFIED; MAI-03 IN_PROGRESS  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-02 — Canonical Map Asset, Placeable & Package Schema  
**Current item:** MAI-03 — Grid, Coordinates, Scale & Projection Engine  
**Implementation branch:** `integration/mai-03-grid-coordinates-scale-projection-engine`  
**Implementation authority:** MAI-03 only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 remains `completed_verified` on application PR #312, merged as `82dc4c8838876e66361b942f0243a63f3b1f20d8`.

MAI-02 remains `completed_verified` on application PR #313. Repaired exact head `994bf0f5551e5d04239978d3728360f94bcb20a1` passed Repository Health, self-hosted Linux/Windows Validation Core and deterministic comparison, then squash-merged as `78c07e2102fdf6a7939a00a47b58e25150e66018` with deterministic receipt `83c5404498405dcce6efcfe9b75e8c5c1b9428f0b1e922328857b3426d0b5e07`.

Owner Continue on 2026-08-25 America/Chicago freshly verified exact AIOC `fc0b4e8f82a1e1808d5b80b8b7f876aa66d3215f` and application `78c07e2102fdf6a7939a00a47b58e25150e66018`, re-read the completed MAI-01 survey, MAI-02 schema/contracts, MAI program/backlog, MIB-11/D18 World evidence and D29 authoring-provenance seam, resolved the bounded MAI-03 mechanics contract, and governed-started MAI-03.

MAI-03 alone may implement on `integration/mai-03-grid-coordinates-scale-projection-engine`. MAI-04 and later tranches remain unauthorized.

## Binding completed foundation

MAI-01 and MAI-02 establish provider-neutral source/license/authority/schema truth:

- no canonical vendor/editor;
- 14 provider-neutral source classes and 10 license-evidence classes;
- explicit unsupported metadata preservation and unresolved permission state;
- explicit incomplete-pack outcomes and semantic-requirement/selected-art separation;
- canonical MapAsset/Tile/TerrainSet/ObjectAsset/Module/Battlemap/Layer/Placeable/package/source records;
- MAI-02 dimensions, anchors, transforms and grid descriptors are descriptive schema data;
- no art, map, coordinate or projection becomes canonical World/combat identity.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location identity, hierarchy, topology, navigation/transfer edges and World state.
- **D29 authoring-provenance** retains governed publication/provenance workflow; MAI references stable owner IDs/versions/provenance.
- Existing Scene/tabletop, Combat/Exploration and Visibility/Permissions owners retain runtime gameplay and visibility truth.
- License permission is evidence-driven and never inferred.
- Missing art does not block theater-of-the-mind/non-map play.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.

## MAI-03 resolved implementation contract

MAI-03 implements a pure deterministic projection layer over completed MAI-02 records.

### Coordinate spaces

- `asset-local-pixel`;
- `map-pixel`;
- `grid-coordinate`;
- `normalized-map`.

### Supported grid/projection families

- square;
- gridless;
- hex with explicit flat/point axis orientation;
- isometric;
- staggered.

Unknown or invalid projection metadata remains explicit failure state. No vendor/editor coordinate convention becomes canonical.

### Authorized mechanics

MAI-03 may implement deterministic:

- grid-coordinate → map-pixel projection;
- map-pixel → grid-coordinate inverse projection;
- asset-local → map-pixel transform using MAI-02 transform descriptors;
- map-pixel → asset-local inverse transform;
- map-pixel ↔ normalized-map conversion;
- finite positive pixels-per-unit scale conversion with explicit unit labels/references;
- round-trip validation within explicit numeric tolerance.

Scale remains presentation metadata only and never establishes canonical World distance, World location, topology or combat identity.

### Required boundaries

- consume MAI-02 identity/dimensions/anchors/transforms/grid descriptors rather than redefining asset identity;
- no terrain connectivity/autotile semantics (MAI-04);
- no occlusion/wall/interactive-geometry runtime ownership (MAI-05);
- no import adapters (MAI-06);
- no availability/substitution automation (MAI-07);
- no workbench UI (MAI-08);
- no owner-domain runtime integration (MAI-09);
- no corpus/performance proof (MAI-10);
- no license inference, unsupported-metadata discard, World/combat mutation, migration 0022 or real-money/provider/release activation.

## Validation contract

The MAI-03 exact candidate must pass:

1. focused MAI-03 projection/round-trip/authority verifier;
2. workspace install;
3. client TypeScript typecheck;
4. focused MAI-03 integration regression;
5. MAI-02 predecessor regression;
6. MAI-01 survey regression;
7. MIB-11/D18 World-owner regression;
8. exact-head application Repository Health;
9. self-hosted Linux and Windows Validation Core;
10. deterministic cross-platform comparison.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `in_progress`
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
- MAI-03 authority is tranche- and branch-bounded.
- MAI-04+ have no implementation authority.
- No vendor/editor or source format is canonical Multiversal map truth.
- No pack is assumed complete; semantic requirement and chosen visual asset remain separable.
- MIB-11/D18 World and D29 authoring-provenance owner truth is not mutated by MAI.
- Coordinates/transforms/scale/projections are presentation data, not World/combat identity truth.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
