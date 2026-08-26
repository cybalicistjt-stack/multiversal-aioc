# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..04 COMPLETED_VERIFIED; MAI-05 IN_PROGRESS  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-04 — Terrain, Autotile & Connectivity Grammar  
**Current item:** MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry  
**Implementation branch:** `integration/mai-05-layers-objects-overhead-occlusion-interactive-geometry`  
**Implementation authority:** MAI-05 only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-04 remain `completed_verified` and have no further implementation authority. Owner `Continue` freshly verified AIOC `49476b68d61515fc46fb2fe244b9b3e2b5d8a216` and application `bf72b52d07c62ca81604f9fbc15b6c80b2f1a0eb`, re-read completed MAI evidence and resolved MAI-05 runtime owner seams before governed start.

MAI-05 alone may implement on the registered branch. MAI-06 and later remain unauthorized.

## Binding completed foundation

MAI-01..04 establish provider-neutral source/license/provenance truth, canonical visual asset/layer/placeable records, deterministic coordinate/projection transforms, deterministic visual terrain/connectivity, explicit incomplete-pack outcomes, preserved unsupported metadata and no inferred permissions. None of those presentation constructs creates canonical World/gameplay truth.

## Resolved MAI-05 contract

### Layers and objects

MAI-05 extends MAI-02 layer/placeable semantics with deterministic descriptive presentation roles and ordering only. Stable order/elevation plus stable IDs may determine presentation order. Runtime Scene mutation remains owned by Scene/Tabletop.

### Geometry primitives

Provider-neutral geometry primitives are `point`, `segment`, `polyline`, `polygon`, `rectangle`, and `ellipse`, expressed in MAI-03 projection space with finite coordinates, stable IDs and provenance/source references. Geometry does not itself create World topology, collision, cover, movement, line-of-sight or interaction state.

### Overhead and occlusion candidates

Overhead records may describe visual stacking, clipping/mask candidates and source geometry. Occlusion classes are descriptive hints: `none`, `opaque-candidate`, `mask-candidate`, and `overhead-candidate`. A visibility-policy reference may be carried, but Visibility/Permissions remains sole authority for audience visibility, occlusion authorization, hidden state and line-of-sight.

### Interactive geometry candidates

MAI-05 may preserve descriptive hints such as `door-candidate`, `trigger-candidate`, `region-candidate`, `portal-candidate` or `generic-candidate`. Any non-none hint requires an explicit external owner reference. MAI does not own or mutate open/closed state, trigger state, collision, cover, movement, combat effects, teleport/transfer truth or other runtime interaction state.

## Persistent owner boundaries

- **Scene/Tabletop** owns runtime scene, layer and object placement/mutation/publication truth.
- **Visibility/Permissions** owns audience visibility, occlusion authorization, hidden-state and line-of-sight truth. Existing visibility projection filters unauthorized information before topology/cardinality or derived outputs.
- **Combat/Exploration** owns movement, collision, cover, range/reach, line/visibility validation and interaction/gameplay consequences.
- **MIB-11 / D18 World** owns canonical World/location identity, hierarchy, topology, navigation and transfer edges.
- **D29 authoring-provenance** owns governed publication/provenance workflow.
- MAI-05 may carry stable owner references but performs no owner mutation or adjudication.

## Deterministic behavior

MAI-05 validates finite geometry, primitive-specific minimum shape requirements, stable references and explicit owner seams. Presentation layers/placeables/geometry are sorted by explicit order/elevation and then stable IDs. Equivalent input must produce platform-identical normalized descriptors and receipts.

## Explicit non-authorization

MAI-05 does **not** implement MAI-06 import adapters, MAI-07 resolver/substitution automation, MAI-08 workbench UI, MAI-09 runtime-owner integration or MAI-10 corpus/performance proof. It does not implement Scene mutation, visibility authorization, line-of-sight calculation, collision/cover/movement adjudication, World topology, canonical interaction state, vendor-specific canonical models, permission inference, unsupported-metadata discard, migration `0022`, tester distribution, release/deployment or real-money/provider/payment activation.

## Validation contract

The exact MAI-05 candidate must pass the focused MAI-05 verifier, client typecheck and integration regression; MAI-04, MAI-03, MAI-02 and MAI-01 predecessor regressions; World/visibility owner regressions; exact-head Repository Health; self-hosted Linux and Windows Validation Core; and deterministic cross-platform comparison.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `in_progress`
6. **MAI-06 — Universal Import Adapter Framework** — `planned`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `planned`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Invariants

MAI-01..04 have no further authority; MAI-05 authority is tranche- and branch-bounded; MAI-06+ remain unauthorized. No vendor/editor is canonical. No asset pack is assumed complete. World, Scene, visibility, collision, movement, cover, combat and interaction runtime truth cannot be inferred from visual geometry. Migration `0022` remains unreserved absent a demonstrated durable schema delta.
