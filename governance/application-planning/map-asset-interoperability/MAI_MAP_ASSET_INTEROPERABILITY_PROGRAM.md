# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..03 COMPLETED_VERIFIED; MAI-04 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-03 — Grid, Coordinates, Scale & Projection Engine  
**Current item:** MAI-04 — Terrain, Autotile & Connectivity Grammar  
**Implementation branch:** none  
**Implementation authority:** none until a future governed start of MAI-04  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 remains `completed_verified` on application PR #312, merged as `82dc4c8838876e66361b942f0243a63f3b1f20d8`.

MAI-02 remains `completed_verified` on application PR #313, merged as `78c07e2102fdf6a7939a00a47b58e25150e66018` with deterministic receipt `83c5404498405dcce6efcfe9b75e8c5c1b9428f0b1e922328857b3426d0b5e07`.

MAI-03 is `completed_verified` on application PR #314. Initial candidate `f601900b85bc6cd1ddd74b59308eefe344b05b44` failed TypeScript client typecheck because the generic failure helper inferred `Mai03ProjectionResult<null>`. One bounded repair cycle changed only the generic result typing. Repaired exact head `223cd0d64ae3c38f3edb2e16dddfbbbf6294ce1a` then passed Repository Health, self-hosted Linux and Windows Validation Core, and deterministic cross-platform comparison with receipt `1f8c80bd7f3a252fdd43097abb1e1355e34cae0ae81a39d386676d38a232d19c`, and squash-merged as `16a4e2c8422be4a8a1677ea98247a6eb62c05f72`.

Strict MAI order now selects **MAI-04 — Terrain, Autotile & Connectivity Grammar** as `selected_not_started`. No MAI-04 branch or implementation authority exists. MAI-05 and later tranches remain unauthorized.

## Binding completed foundation

MAI-01 through MAI-03 establish provider-neutral source/license/authority/schema/projection truth:

- no canonical vendor/editor;
- explicit source/license/provenance evidence and unresolved permission state;
- unsupported metadata preservation and explicit incomplete-pack outcomes;
- semantic requirements separated from selected visual art;
- canonical MapAsset/Tile/TerrainSet/ObjectAsset/Module/Battlemap/Layer/Placeable/package/source records;
- provider-neutral asset-local pixel, map-pixel, grid-coordinate and normalized-map spaces;
- deterministic square, gridless, flat/point hex, isometric and staggered projection descriptors;
- reversible grid projection and MAI-02 asset transforms;
- explicit presentation-only pixels-per-unit scale conversion;
- no art, coordinate, projection, scale or transform becomes canonical World/combat identity.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location identity, hierarchy, topology, navigation/transfer edges and World state.
- **D29 authoring-provenance** retains governed publication/provenance workflow; MAI references stable owner IDs/versions/provenance.
- Existing Scene/tabletop, Combat/Exploration and Visibility/Permissions owners retain runtime gameplay and visibility truth.
- License permission is evidence-driven and never inferred.
- Missing art does not block theater-of-the-mind/non-map play.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.

## MAI-03 completed implementation contract

MAI-03 completed a pure deterministic projection layer over MAI-02 records.

### Coordinate spaces

- `asset-local-pixel`;
- `map-pixel`;
- `grid-coordinate`;
- `normalized-map`.

### Supported projection families

- square;
- gridless;
- hex with explicit flat/point axis orientation;
- isometric;
- staggered.

Unknown or invalid projection metadata remains explicit failure state. Gridless projections do not invent grid coordinates. No vendor/editor coordinate convention becomes canonical.

### Completed mechanics

MAI-03 provides deterministic:

- grid-coordinate → map-pixel projection;
- map-pixel → grid-coordinate inverse projection;
- asset-local → map-pixel transform using MAI-02 transform descriptors;
- map-pixel → asset-local inverse transform;
- map-pixel ↔ normalized-map conversion;
- finite positive pixels-per-unit scale conversion with explicit unit labels/references;
- round-trip validation within explicit numeric tolerance.

Scale remains presentation metadata only and never establishes canonical World distance, World location, topology or combat identity.

## MAI-03 completion evidence

- Application PR: **#314**
- Exact validated head: `223cd0d64ae3c38f3edb2e16dddfbbbf6294ce1a`
- Repository Health: run `32919674724`, job `98030594099` — PASS
- Validation Core run: `32919675012`
- MAI-03 Linux job: `98030595667` — PASS
- MAI-03 Windows job: `98030595750` — PASS
- MAI-03 deterministic comparison job: `98031978726` — PASS
- Linux evidence artifact: `9589464335`, digest `sha256:85b393a8491d4b79dd20c7f68190dd93132d150ae686ace30f1262861ef61055`
- Windows evidence artifact: `9589544628`, digest `sha256:251d8ce4d3c9201c338f14a6618b53914813d73e8578f4a61f6f748cab293aba`
- Comparison artifact: `9589611554`, digest `sha256:87ffd288da8b69d54bb08f5bb0e018d5ec50f0dcbe29b355a925234802b629bd`
- Deterministic receipt: `1f8c80bd7f3a252fdd43097abb1e1355e34cae0ae81a39d386676d38a232d19c`
- Application squash merge: `16a4e2c8422be4a8a1677ea98247a6eb62c05f72`
- Repair cycles: **1**

The single repair corrected TypeScript generic null-result inference. It did not change projection formulas, owner boundaries or acceptance requirements.

## MAI-04 selection contract

MAI-04 is selection-only. A future owner **Continue** must freshly verify then-current AIOC/application heads and re-read completed MAI-01..03 evidence before any branch is created.

The governed start must resolve the exact terrain/autotile/connectivity grammar and owner crosswalk, including at minimum:

- source terrain semantics versus normalized terrain descriptors;
- adjacency/connectivity grammar and deterministic matching rules;
- autotile selection behavior and explicit unresolved/missing-asset outcomes;
- how MAI-03 projection coordinates are consumed without becoming canonical World topology;
- how World, Scene/tabletop, Combat/Exploration and provenance owners remain authoritative;
- whether any durable persistence delta actually exists before migration `0022` can be considered.

No source/vendor-specific autotile model may become canonical merely because it exists in a retained format.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `selected_not_started`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `planned`
6. **MAI-06 — Universal Import Adapter Framework** — `planned`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `planned`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Downstream relationship

AAI follows MAI so provider-neutral asset/provenance patterns can be reused for audio without merging visual and audio ownership. ISE later consumes completed MAI + AAI for native tabletop/canvas experience.

## Invariants

- MAI-01..03 have no further implementation authority.
- MAI-04 is `selected_not_started` with no implementation branch or authority.
- MAI-05+ have no implementation authority.
- No vendor/editor or source format is canonical Multiversal map truth.
- No pack is assumed complete; semantic requirement and chosen visual asset remain separable.
- MIB-11/D18 World and D29 authoring-provenance owner truth is not mutated by MAI.
- Coordinates/transforms/scale/projections are presentation data, not World/combat identity truth.
- Terrain/autotile/connectivity semantics cannot silently create canonical World topology, navigation or gameplay truth.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
