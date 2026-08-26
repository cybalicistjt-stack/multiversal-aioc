# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..03 COMPLETED_VERIFIED; MAI-04 IN_PROGRESS  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-03 — Grid, Coordinates, Scale & Projection Engine  
**Current item:** MAI-04 — Terrain, Autotile & Connectivity Grammar  
**Implementation branch:** `integration/mai-04-terrain-autotile-connectivity-grammar`  
**Implementation authority:** MAI-04 only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 remains `completed_verified` on application PR #312, MAI-02 on PR #313, and MAI-03 on PR #314. MAI-03 exact repaired head `223cd0d64ae3c38f3edb2e16dddfbbbf6294ce1a` passed Repository Health, self-hosted Linux/Windows Validation Core and deterministic comparison with receipt `1f8c80bd7f3a252fdd43097abb1e1355e34cae0ae81a39d386676d38a232d19c`, then squash-merged as `16a4e2c8422be4a8a1677ea98247a6eb62c05f72` after one bounded TypeScript typing repair.

Owner Continue freshly verified exact AIOC `0008c22af2d1b7942a5f08ff6f9bb6443f32fe22` and application `16a4e2c8422be4a8a1677ea98247a6eb62c05f72`, re-read completed MAI-01..03 evidence, resolved the bounded MAI-04 terrain/autotile/connectivity grammar, and governed-started MAI-04.

MAI-04 alone may implement on `integration/mai-04-terrain-autotile-connectivity-grammar`. MAI-05 and later tranches remain unauthorized.

## Binding completed foundation

MAI-01..03 establish provider-neutral source/license/authority/schema/projection truth:

- no canonical vendor/editor or source format;
- source permissions remain evidence-driven, with unknown/unverified state explicit;
- unsupported structured metadata is preserved rather than silently discarded;
- no pack is assumed complete; semantic requirements remain separate from selected art;
- canonical MAI-02 asset/package/source/provenance records remain authoritative for visual identity and lineage;
- MAI-03 coordinate/projection/scale mechanics are deterministic presentation transforms only;
- MIB-11/D18 retains canonical World/location/topology/navigation truth;
- D29 authoring-provenance retains governed publication/provenance workflow ownership;
- Scene/tabletop, Combat/Exploration and Visibility/Permissions retain their runtime truth.

MAI-01 specifically recognizes provider-neutral source class `autotile-tileset` with examples `autotile`, `wang-set`, and `terrain-set`, and metadata `tile-grid` plus `connectivity-or-transition-metadata-when-present`. That source evidence is not itself canonical mechanics.

## MAI-04 resolved implementation contract

### Terrain descriptors

MAI-04 may define stable provider-neutral terrain descriptors with:

- stable terrain ID and label;
- optional semantic owner reference;
- explicit visual connection channels/compatibility sets;
- source/provenance references inherited from MAI-02;
- optional visual variant grouping and priority metadata.

Terrain descriptors describe visual composition semantics. A terrain ID does not create World region identity, location identity, movement cost, hazard truth or gameplay traversability.

### Connection grammar

The normalized grammar uses local visual ports rather than a vendor-specific bitmask.

For square-like projected layouts, primary edge ports are `north`, `east`, `south`, `west`; optional visual-corner ports are `north-east`, `south-east`, `south-west`, `north-west`.

For hex projections, ports are `east`, `north-east`, `north-west`, `west`, `south-west`, `south-east`.

Gridless projection has no canonical autotile adjacency ports. Attempts to derive an autotile neighbor signature from gridless projection must return an explicit unsupported finding rather than inventing a grid.

Two visual ports connect only when explicit connection channels and compatibility declarations agree. Physical proximity or MAI-03 grid adjacency alone never implies semantic compatibility.

### Deterministic neighbor signatures

MAI-04 may compute a normalized signature from explicit local neighbor observations. The signature records, in canonical port order, whether each neighbor is:

- compatible on an explicit channel;
- explicitly incompatible;
- absent;
- unknown/unresolved.

Unknown source semantics remain unknown; they may not be coerced into compatible/incompatible state merely to select art.

### Autotile selection

Given a terrain descriptor, normalized neighbor signature and eligible visual variants, MAI-04 may deterministically select a visual candidate by:

1. rejecting candidates whose explicit required/forbidden port conditions do not match;
2. rejecting assets that fail source/license/permission constraints supplied by predecessor truth;
3. sorting remaining candidates by explicit priority, then stable asset/tile ID;
4. returning the first eligible candidate without mutating any owner state.

If no compatible permitted visual exists, MAI-04 must return an explicit MAI-01 incomplete-pack outcome (`manual-selection`, `approved-placeholder`, or `visibly-unresolved` as appropriate) rather than inventing or silently substituting art. Automated cross-pack search/substitution remains MAI-07.

### Source-specific metadata

Tiled Wang sets, terrain sets, LDtk terrain/rule metadata, or any future provider-specific representation may later be mapped by MAI-06 adapters into this normalized grammar. MAI-04 itself does not implement import adapters and does not promote any source model to canonical status. Unsupported source fields remain in MAI-02 envelopes.

## Owner boundaries

- **MIB-11 / D18 World** remains sole canonical owner of World/location identity, hierarchy, topology, navigation/transfer edges and canonical World state.
- Visual terrain connectivity cannot create World adjacency, route existence, movement permission or traversability.
- **Scene/tabletop** owners retain scene/runtime placement and mutation truth.
- **Combat/Exploration** owners retain movement, collision, cover, hazard, encounter and combat truth.
- **Visibility/Permissions** owners retain player/GM visibility truth.
- **D29 authoring-provenance** retains governed publication/provenance workflow.
- MAI-04 is a pure deterministic visual-composition grammar and performs no owner-domain mutation.

## Explicit non-authorization

MAI-04 does **not** implement:

- MAI-05 walls, overhead/occlusion or interactive runtime geometry;
- MAI-06 universal import adapters;
- MAI-07 semantic availability/substitution resolver automation;
- MAI-08 asset intake/composer/workbench UI;
- MAI-09 World/Scene/Combat/Exploration runtime integration;
- MAI-10 diverse-corpus/performance proof;
- vendor/editor-specific canonical autotile semantics;
- World topology/navigation/traversability or gameplay state inferred from visual connectivity;
- license permission inference or unsupported-metadata discard;
- migration `0022`;
- tester distribution, release/deployment, real-money commerce or provider/payment activation.

## Validation contract

The MAI-04 exact candidate must pass:

1. focused MAI-04 terrain/autotile/connectivity invariant verifier;
2. workspace dependency preparation;
3. client TypeScript typecheck;
4. focused MAI-04 integration regression;
5. MAI-03 predecessor regression;
6. MAI-02 schema regression;
7. MAI-01 survey regression;
8. MIB-11/D18 World-owner regression;
9. exact-head application Repository Health;
10. self-hosted Linux and Windows Validation Core;
11. deterministic cross-platform comparison.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `in_progress`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `planned`
6. **MAI-06 — Universal Import Adapter Framework** — `planned`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `planned`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Invariants

- MAI-01..03 have no further implementation authority.
- MAI-04 authority is tranche- and branch-bounded.
- MAI-05+ have no implementation authority.
- No vendor/editor or source format is canonical Multiversal map truth.
- No pack is assumed complete; semantic requirement and chosen visual asset remain separable.
- Visual terrain/autotile/connectivity never creates World topology, navigation or gameplay truth.
- Missing/incompatible/unpermitted art remains explicit.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
