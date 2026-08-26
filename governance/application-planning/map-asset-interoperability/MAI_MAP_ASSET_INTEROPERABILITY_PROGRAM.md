# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..08 COMPLETED_VERIFIED; MAI-09 SELECTED_NOT_STARTED  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench  
**Current item:** MAI-09 — World, Scene, Combat, Exploration & Creator Integration  
**Implementation branch:** none  
**Implementation authority:** none — MAI-09 selection only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-08 are `completed_verified` with no further implementation authority. MAI-08 exact application head `7792f765a7eb662372c32f59d237998f0bb85392` passed Repository Health, the complete self-hosted Linux/Windows Validation Core workflow and deterministic cross-platform comparison with zero repair cycles, then squash-merged as `7d073bd3c9487d665751c76d2b5a69d3991ab305`.

Strict MAI order now selects MAI-09 as `selected_not_started` only. MAI-09 has no implementation branch and no implementation authority. A future owner `Continue` must freshly verify canonical AIOC/application heads, re-read completed MAI-01..08 evidence plus current owner contracts, resolve the exact integration seams and governed-start MAI-09 before implementation. MAI-10 remains unauthorized.

## MAI-08 completion evidence

- Application PR: **#319**
- Exact validated head: `7792f765a7eb662372c32f59d237998f0bb85392`
- Repository Health: run `32939863908`, job `98088448674` — PASS
- Validation Core: run `32939863798` — PASS
- MAI-08 Linux job: `98088448621` — PASS
- Linux artifact: `9596253071`, digest `sha256:93de084e486f8a43c0252a63ae9cdc1dcd6da9b24a3b296e7e687536ae9f2ab4`
- MAI-08 Windows job: `98088448655` — PASS
- Windows artifact: `9596319934`, digest `sha256:f7ec56194ffc00ec5dc713c9bd7384208ad3bb3254d8a1651226aa18e393bbf7`
- MAI-08 deterministic comparison job: `98090202095` — PASS
- Comparison artifact: `9596387530`, digest `sha256:84cfda40da61ebc728cdbebd1f8198e83460980f7dd438096bd9b7ed98263b28`
- Deterministic receipt: `86a925a25ffaf35cd43ce0233b2cc461a714b5441ba774c49b06160482d6a4e3`
- Application squash merge: `7d073bd3c9487d665751c76d2b5a69d3991ab305`
- Repair cycles: **0**

## Completed MAI-08 contract

MAI-08 completed the governed provider-neutral authoring layer over MAI-01..07:

- intake is limited to supplied/catalogued source/package/asset evidence and completed import evidence;
- source/checksum/license/provenance/import findings remain explicit and denied/unknown/unsupported evidence fails closed;
- the palette projects MAI-07 eligibility evidence and keeps denied, unknown, incompatible and unverified candidates visible but non-authorizing;
- manual assignment/override, approved-placeholder and visibly-unresolved outcomes remain first-class and reversible;
- composer/workbench state is only deterministic reversible `presentation-authoring-draft` state;
- layers, placeables and semantic assignments are draft presentation intent rather than runtime owner state;
- canonical draft serialization produces platform-stable evidence/receipts independent of input collection ordering;
- save/export yields later integration input only and does not publish or mutate World/Scene/Visibility/Combat/D29 truth;
- no provider acquisition/download/authentication/scraping/payment was introduced;
- no durable schema delta was demonstrated, so migration `0022` remains unreserved.

## Binding completed foundation

MAI-01..08 now establish provider-neutral source/license/authority truth, canonical visual asset/package/provenance records, deterministic coordinates/projections, visual-only terrain connectivity, descriptive geometry, deterministic source-specific adapter translation with raw-source preservation, permission/provenance-aware catalog resolution, explicit manual/placeholder/unresolved outcomes, and a deterministic reversible presentation-authoring workbench.

No provider schema, visual construct, resolver choice, authoring draft or draft receipt becomes World/gameplay/runtime truth by implication.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location/topology/navigation/transfer truth.
- **D29 authoring-provenance** retains governed publication/provenance workflow.
- **Scene/Tabletop** retains runtime scene/layer/object placement and mutation.
- **Visibility/Permissions** retains audience visibility, hidden state, occlusion authorization and line-of-sight.
- **Combat/Exploration** retains collision, cover, movement, interaction, trigger/portal and gameplay consequences.
- MAI-08 draft output is only integration input. MAI-09 must resolve explicit seams to these owners before any live integration exists.

## MAI-09 selection boundary

MAI-09 is selected but not started. Its future governed start must resolve, at minimum:

- the exact handoff from MAI-08 draft snapshots/receipts into existing owner-domain commands or references;
- MIB-11/D18 World integration without deriving World topology, identity or navigation from presentation state;
- Scene/Tabletop placement/mutation integration without treating drafts as live runtime state;
- Visibility/Permissions integration without bypassing hidden-state, audience or line-of-sight authorization;
- Combat/Exploration integration without promoting visual connectivity/geometry hints into collision, movement, cover, interaction or consequence truth;
- D29/creator submission, approval, versioning and provenance handoff;
- stale/revoked/unresolved/conflicting draft reconciliation and rollback behavior;
- deterministic integration evidence/receipts and any demonstrated persistence delta before migration `0022` may be reserved.

Selection does **not** authorize creation of an implementation branch, runtime integration, migration `0022`, tester/release/deployment activation, provider/payment activation or real-money activity.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `completed_verified`
6. **MAI-06 — Universal Import Adapter Framework** — `completed_verified`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `completed_verified`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `completed_verified`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `selected_not_started`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Next governed gate

No MAI-09 candidate exists yet. The next owner `Continue` must freshly verify canonical heads and resolve the bounded integration/creator contract before a governed-start may create an implementation branch or authorize code. Once started, its exact candidate must use the project’s governed exact-head Repository Health, self-hosted Linux/Windows Validation Core, deterministic comparison and applicable predecessor/owner regressions before merge.

## Invariants

MAI-01..08 have no further implementation authority. MAI-09 is selection only. No vendor/editor/provider is canonical. No asset pack is assumed complete. Semantic requirements and selected art remain separable. Permissions are evidence-driven and unknown remains unresolved. Manual selection, approved-placeholder and visibly-unresolved outcomes remain first-class. No automatic provider acquisition exists. MAI-08 drafts are intent/evidence, not owner truth. Migration `0022` remains unreserved absent a demonstrated durable schema delta.
