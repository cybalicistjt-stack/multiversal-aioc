# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..07 COMPLETED_VERIFIED; MAI-08 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution  
**Current item:** MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench  
**Implementation branch:** none  
**Implementation authority:** none — MAI-08 selection only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-07 are `completed_verified` with no further implementation authority. MAI-07 exact application head `06e291c68ee79f58b7115d62b878f35e300d700a` passed Repository Health, self-hosted Linux and Windows Validation Core, and deterministic cross-platform comparison, then squash-merged as `c7aeff6470199366ba033cce892e6816f9253d8a`.

Strict MAI order now selects MAI-08 as `selected_not_started` only. MAI-08 has no implementation branch and no implementation authority. A future owner `Continue` must freshly verify canonical AIOC/application heads, re-read completed MAI-01..07 evidence, resolve the exact intake-wizard/composer/palette/workbench contract and ownership boundaries, and governed-start MAI-08 before implementation. MAI-09 and later remain unauthorized.

## MAI-07 completion evidence

- Application PR: **#318**
- Exact validated head: `06e291c68ee79f58b7115d62b878f35e300d700a`
- Repository Health: run `32935412459`, job `98075587069` — PASS
- Validation Core: run `32935412701`
- MAI-07 Linux job: `98075588684` — PASS
- Linux artifact: `9594801142`, digest `sha256:b9a6b14dda47ddc9540e95260e280a17b1558d6e692ba36d1efb3156fc634ba0`
- MAI-07 Windows job: `98075588678` — PASS
- Windows artifact: `9594818885`, digest `sha256:75fe6b4e10a3edaf6583d69312e258d66917c1f1a0ae019383a7d5fa54a19df9`
- MAI-07 deterministic comparison job: `98077001992` — PASS
- Comparison artifact: `9594892255`, digest `sha256:3474e105218d8dd3774505043e348416ae744c824ed0edefadad5fe966448e9c`
- Deterministic receipt: `f94ab58d2e7000910afaf8eceec3e59b13ce58b468bb0e5325d85c25e7723266`
- Application squash merge: `c7aeff6470199366ba033cce892e6816f9253d8a`
- Repair cycles: **1**

## Binding completed foundation

MAI-01..07 establish provider-neutral source/license/authority truth, canonical visual asset/package/provenance records, deterministic coordinates/projections, visual-only terrain connectivity, descriptive geometry, deterministic source-specific adapter translation with full raw-source preservation, and a catalog-only semantic availability resolver with explicit permission/provenance evidence, deterministic cross-pack substitution, manual control, and explicit placeholder/unresolved outcomes.

No provider schema, presentation construct or resolver choice becomes World/gameplay truth.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location/topology/navigation/transfer truth.
- **D29 authoring-provenance** retains governed publication/provenance workflow.
- **Scene/Tabletop** retains runtime scene/layer/object placement and mutation.
- **Visibility/Permissions** retains audience visibility, occlusion authorization and line-of-sight.
- **Combat/Exploration** retains collision, cover, movement, interaction and gameplay consequences.
- Visual intake, authoring, requirements, availability and substitutions may only stage or choose presentation assets and cannot mutate these owners by implication.

## Completed MAI-07 contract

MAI-07 completed a provider-neutral semantic asset taxonomy and catalog-only deterministic resolver.

- Availability distinguishes permitted-compatible, denied, unknown-permission, incompatible, missing and unknown/unverified evidence.
- A candidate is eligible only when supplied/catalogued evidence establishes compatibility and explicit granted use permission.
- Cross-pack substitution additionally requires explicit compatibility plus granted substitute permission.
- Manual assignment and override remain first-class; an ineligible manual pin returns an explained unresolved result rather than silent fallback.
- Approved placeholder is an explicit caller policy outcome, never a silent substitution.
- Resolver receipts and rejection diagnostics are deterministic and platform-identical.
- Resolution performs no provider acquisition, download, purchase, authentication, scraping, provider API ingestion or payment.

## MAI-08 selection boundary

MAI-08 is selected but not started. Its future governed start must resolve, at minimum:

- intake-wizard staging and validation over user-supplied/catalogued assets;
- the exact boundary between map-composer/palette/workbench authoring state and canonical World/Scene/runtime owner state;
- visible handling of MAI-01..07 license, provenance, import, compatibility, permission, unresolved and placeholder evidence;
- first-class manual and reversible authoring controls without silent permission/resolver bypass;
- whether a durable schema delta is actually demonstrated before migration `0022` can be reserved.

Selection does **not** authorize creation of an implementation branch, workbench implementation, MAI-09 runtime integration, provider acquisition, migration `0022`, tester/release/deployment activation, provider/payment activation or real-money activity.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `completed_verified`
6. **MAI-06 — Universal Import Adapter Framework** — `completed_verified`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `completed_verified`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `selected_not_started`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Next governed gate

No MAI-08 candidate exists yet. The next owner `Continue` must freshly verify canonical heads and resolve the bounded MAI-08 contract before a governed-start may create an implementation branch or authorize code. Once started, its exact candidate must use the project’s governed exact-head Repository Health, self-hosted Linux/Windows Validation Core, deterministic comparison and applicable predecessor/owner regressions before merge.

## Invariants

MAI-01..07 have no further implementation authority. MAI-08 is selection only. No vendor/editor/provider is canonical. No asset pack is assumed complete. Semantic requirements and selected art remain separable. Permissions are evidence-driven and unknown remains unresolved. Manual selection, approved-placeholder and visibly-unresolved outcomes remain first-class. No automatic provider acquisition exists. Owner-domain truth cannot be inferred from authoring or resolver choices. Migration `0022` remains unreserved absent a demonstrated durable schema delta.
