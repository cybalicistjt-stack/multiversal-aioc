# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..06 COMPLETED_VERIFIED; MAI-07 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-06 — Universal Import Adapter Framework  
**Current item:** MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution  
**Implementation branch:** none  
**Implementation authority:** none; MAI-07 selection only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-06 are `completed_verified` with no further implementation authority. MAI-06 application PR #317 used exact validated head `8d27e4545ff9b58420ba7f565312dda1418fe9f3`; Repository Health, self-hosted Linux/Windows Validation Core and deterministic comparison all passed with matching receipt `9ee149eef76814d5f9469d8645df5e2b7923ec262a037dd46d4f0918600bff39` and zero repair cycles before squash merge `bc217bab20e166799b76526f6ef5d9537191b79f`.

Strict MAI order selects MAI-07 only. It has no implementation branch and no implementation authority. MAI-08 and later remain unauthorized.

## Binding completed foundation

MAI-01..06 now establish provider-neutral source/license/authority truth, canonical visual asset/package/provenance records, deterministic coordinates/projections, visual-only terrain connectivity, descriptive geometry, and deterministic source-specific adapter translation with full raw-source preservation. No provider schema or presentation construct becomes World/gameplay truth.

## MAI-06 completed contract

MAI-06 completed deterministic explicit-or-detected adapter selection with bounded `tiled-json`, `ldtk-json`, and `foundry-scene-json` proof adapters. Explicit adapter choice outranks detection; automatic detection requires exactly one strong match; ambiguous/no-match inputs fail explicitly. Provider-specific fields map only when their semantics are explicit; all raw source data, checksums, license/permission evidence, import lineage and unsupported metadata remain preserved. The adapter layer performs no network/provider ingestion and no owner mutation.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location/topology/navigation/transfer truth.
- **D29 authoring-provenance** retains governed publication/provenance workflow.
- **Scene/Tabletop** retains runtime scene/layer/object placement and mutation.
- **Visibility/Permissions** retains audience visibility, occlusion authorization and line-of-sight.
- **Combat/Exploration** retains collision, cover, movement, interaction and gameplay consequences.
- Visual requirements, availability and substitutions may only choose presentation assets and cannot mutate these owners.

## MAI-07 selection contract

MAI-07 is selected but not started. Before any implementation, a future owner `Continue` must freshly verify both repository heads and resolve:

- a provider-neutral semantic asset taxonomy that describes visual requirements independently from any pack/provider;
- explicit availability states that distinguish present/permitted, present-but-denied, incompatible, missing and unknown/unverified evidence;
- deterministic permission- and provenance-aware candidate filtering/ranking;
- manual assignment and manual override as first-class choices;
- explicit approved-placeholder and visibly-unresolved outcomes;
- deterministic cross-pack substitution that never invents compatibility, permission or semantic equivalence;
- stable resolver receipts and explainable rejection diagnostics.

Resolution may operate only over supplied/catalogued evidence. It may not download, buy, authenticate to, scrape or otherwise acquire provider assets.

## Explicit non-authorization

MAI-07 is not authorized yet. MAI-08 workbench UI, MAI-09 runtime owner integration and MAI-10 corpus/performance proof remain unauthorized. Migration `0022`, tester distribution, release/deployment, real-money commerce and provider/payment activation remain unauthorized.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `completed_verified`
6. **MAI-06 — Universal Import Adapter Framework** — `completed_verified`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `selected_not_started`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Invariants

MAI-01..06 have no further implementation authority. MAI-07 is selection-only with no implementation branch or authority. No vendor/editor/provider is canonical. No asset pack is assumed complete. Semantic requirements and selected art remain separable. Permissions are evidence-driven and unknown remains unresolved. Manual selection, approved-placeholder and visibly-unresolved outcomes remain first-class. No automatic provider acquisition exists. Owner-domain truth cannot be inferred from resolver choices. Migration `0022` remains unreserved absent a demonstrated durable schema delta.
