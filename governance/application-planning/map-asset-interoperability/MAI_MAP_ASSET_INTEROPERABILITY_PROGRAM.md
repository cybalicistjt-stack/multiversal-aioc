# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..04 COMPLETED_VERIFIED; MAI-05 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-04 — Terrain, Autotile & Connectivity Grammar  
**Current item:** MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry  
**Implementation branch:** none  
**Implementation authority:** none; MAI-05 selection only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-04 are `completed_verified` and have no further implementation authority.

MAI-04 application PR #315 used exact validated head `b5b7e3213a83ce38a890a3b577a2beaad087a3f7`. Repository Health run `32921844538` job `98036808168`, Validation Core run `32921844837`, Linux job `98036809657`, Windows job `98036809752`, and deterministic comparison job `98038279918` all passed. Linux and Windows matched receipt `0eb0718acabb41b1c11d4262c013857b75915670a47ee984c316d63051d6633c`; comparison artifact `9590264218` has digest `sha256:39a3d1cdbcb3ef1d7064d280f7028ae4b1b525d466ba62acc11782ad0f666cdb`. No repair cycle was required. PR #315 squash-merged as `bf72b52d07c62ca81604f9fbc15b6c80b2f1a0eb`.

Strict MAI order selects MAI-05 only. MAI-05 has checkpoint `governance/ai/work-state/MAI-05-attempt-001.json`, no implementation branch, and no implementation authority. MAI-06 and later remain unauthorized.

## Binding completed foundation

MAI-01..04 now establish:

- provider-neutral source/license/authority survey and explicit incomplete-pack outcomes;
- canonical vendor-neutral map asset/placeable/package/source/provenance schema;
- deterministic provider-neutral grid/coordinate/scale/projection mechanics;
- deterministic provider-neutral visual terrain/autotile/connectivity grammar;
- no vendor/editor or source format as canonical Multiversal truth;
- explicit preservation of unknown permission and unsupported source metadata;
- semantic requirements separated from selected art and missing/incompatible art kept explicit;
- map coordinates, projections and visual connectivity remaining presentation constructs rather than canonical World/gameplay truth;
- MIB-11/D18 World authority and D29 authoring-provenance authority preserved.

## MAI-04 completed contract

MAI-04 completed stable terrain IDs, explicit square/hex local visual ports, connection channels/compatibility declarations, four-state neighbor signatures (`connected`, `incompatible`, `absent`, `unknown`), gridless explicit non-autotile behavior, and deterministic permission-aware variant selection by explicit priority then stable asset/variant IDs.

The proof covers three terrain descriptors, four visual variants, four square primary ports, six hex ports, explicit gridless behavior, and preserved unsupported source metadata. It creates no World topology, gameplay traversability, runtime geometry, importer/resolver/workbench/runtime-owner integration, migration `0022`, or real-money activity.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location identity, hierarchy, topology, navigation and transfer edges.
- **D29 authoring-provenance** retains governed publication/provenance workflow.
- **Scene/tabletop** remains the owner seam for runtime scene/layer/object placement and mutation truth.
- **Visibility/Permissions** remains the owner seam for GM/player visibility and occlusion authorization truth.
- **Combat/Exploration** remains the owner seam for movement, collision, cover, interactive geometry consequences and combat/exploration truth.
- Visual source geometry must not silently become any of those owner truths.

## MAI-05 selection contract

MAI-05 is selected but not started. Before any implementation, a future owner `Continue` must freshly verify both repository heads, re-read MAI-01..04 completed evidence and exact contracts, and resolve the runtime owner seams for:

- layer and object presentation/ordering;
- overhead visual layers;
- occlusion/visibility descriptors;
- walls, doors, regions or other interactive geometry representations;
- the distinction between descriptive/imported geometry and owner-authoritative runtime collision, movement, visibility, interaction or gameplay state.

No implementation branch may exist until that governed start is validated and merged.

## Explicit non-authorization

MAI-05 is not authorized yet. MAI-06 universal import adapters, MAI-07 asset availability/substitution resolver, MAI-08 workbench UI, MAI-09 runtime owner integration, and MAI-10 corpus/performance proof remain unauthorized. Migration `0022`, tester distribution, release/deployment, real-money commerce and provider/payment activation remain unauthorized.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `selected_not_started`
6. **MAI-06 — Universal Import Adapter Framework** — `planned`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `planned`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Invariants

- MAI-01..04 have no further implementation authority.
- MAI-05 is selection-only with no implementation branch or authority.
- MAI-06+ have no implementation authority.
- No vendor/editor or source format is canonical Multiversal map truth.
- No pack is assumed complete; semantic requirement and chosen visual asset remain separable.
- World, visibility, collision, movement, combat or interactive runtime truth cannot be silently inferred from visual geometry.
- No real-money commerce, tester distribution, release/deployment or provider/payment activation is authorized.
- Migration `0022` remains unreserved absent a demonstrated durable schema delta.
