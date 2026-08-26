# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..08 COMPLETED_VERIFIED; MAI-09 IN_PROGRESS  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench  
**Current item:** MAI-09 — World, Scene, Combat, Exploration & Creator Integration  
**Implementation branch:** `integration/mai-09-world-scene-combat-exploration-creator-integration`  
**Implementation authority:** bounded MAI-09 only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-08 are `completed_verified` with no further implementation authority. MAI-08 exact application head `7792f765a7eb662372c32f59d237998f0bb85392` passed Repository Health, the complete self-hosted Linux/Windows Validation Core workflow and deterministic cross-platform comparison with zero repair cycles, then squash-merged as `7d073bd3c9487d665751c76d2b5a69d3991ab305`.

Owner `Continue` on 2026-08-26 freshly verified AIOC main `b166659b44ffa0799415bd391a30442a9f08ea72` and application main `7d073bd3c9487d665751c76d2b5a69d3991ab305`, re-read MAI-08 and the current MIB-11/D18 World, A5 Scene, visibility-projection and D29 authoring-provenance seams, and governed-started MAI-09. MAI-10 remains unauthorized.

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

## Binding MAI-01..08 foundation

The completed foundation establishes provider-neutral source/license/authority evidence, canonical visual asset/package/provenance records, deterministic presentation coordinates/projections, visual-only terrain/connectivity, descriptive geometry, deterministic source-specific import translation with raw-source preservation, permission/provenance-aware semantic resolution, explicit manual/placeholder/unresolved outcomes, and deterministic reversible `presentation-authoring-draft` snapshots/receipts.

No provider schema, artwork, visual construct, resolver choice, draft or draft receipt becomes World/gameplay/runtime/publication truth by implication.

## MAI-09 governed integration contract

MAI-09 owns **integration orchestration evidence**, not the truths it integrates. The bounded implementation may validate a MAI-08 draft and produce deterministic owner requests, expected-version references, operation identities, acknowledgements and reconciliation records. It may not independently mutate owner domains.

### Input and preflight

MAI-09 consumes a MAI-08 deterministic draft snapshot and receipt plus preserved MAI-01..08 evidence. Before producing any owner request it must fail closed when:

- the draft/receipt is invalid or stale;
- blocking source/import/provenance evidence remains;
- an assignment intended for activation is `visibly-unresolved`;
- permission is denied, unknown or revoked;
- an owner reference/version is stale or unavailable.

A draft is authoring intent/evidence only. Save/export never creates live state.

### World — MIB-11 / D18

Current owner seams include `world-reality-taxonomy-engine.ts` and `world-structure.ts`. MAI-09 may carry explicit stable World/location/taxonomy references and source evidence. Presentation layers, pixel/projection coordinates, visual connectivity and visual geometry may not create World identity, hierarchy, topology, routes, chronology, compatibility or navigation truth.

### Scene/Tabletop — A5

Current owner seams include `scene-placement-port.ts` and `scene-repository-port.ts`. MAI-09 may construct explicit Scene/map-version/placement **proposals** carrying source-definition references, semantic locations, visibility-policy references, expected owner versions and operation IDs. Draft coordinates alone are never sufficient semantic location. Only an A5 owner result creates or mutates runtime Scene state.

### Visibility / Permissions

MAI-09 may carry visibility-policy references and MAI occlusion hints as evidence only. Audience visibility, hidden/reveal state, occlusion authorization and line-of-sight remain owned by authorization/visibility-projection systems. A visual occlusion hint never becomes permission truth.

### Combat / Exploration

MAI-09 may carry explicit governed object/action/interaction references for owner review. MAI-04 visual connectivity and MAI-05 geometry/collision/cover/movement/interaction/portal hints remain descriptive until the owning gameplay domain accepts an explicit binding. A drawn wall, doorway, terrain feature, portal or interactable cannot automatically block movement, grant cover, trigger an Action or cause a consequence.

### Creator / D29 authoring-provenance

Current owner seams include `authoring-proposal-review-port.ts`, authoring draft/recovery/status ports and their authority controls. MAI-09 may create or reference an authoring proposal and attach MAI draft/provenance evidence. Review, approval and publication remain D29 operations. A MAI-09 integration receipt is never a `PublicationReceipt`, and canonical promotion remains separately gated.

### Reconciliation and recovery

- Owner acknowledgements are recorded explicitly per requested binding.
- Partial acceptance remains partial; MAI does not erase accepted history or pretend the whole integration committed atomically when owner domains did not.
- Stale/rejected owner requests leave the draft and current owner truth unchanged.
- Ambiguous outcomes require owner operation-status lookup using the original operation/idempotency identity before retry.
- Permission/provenance revocation before owner commit fails closed; later revocation is handled by the owning domain and surfaced as reconciliation-required.

### Deterministic receipt and persistence

Canonical ordering of draft receipt, owner requests, expected versions, decisions and diagnostics produces a platform-neutral MAI-09 integration-plan/reconciliation receipt. The receipt proves deterministic orchestration evidence only.

The resolved contract demonstrates **no new MAI-owned durable owner-state or integration ledger**. Existing owner version/operation/provenance records remain authoritative. Migration `0022` therefore remains unreserved unless implementation later demonstrates a separate durable delta and governance explicitly approves it.

## Persistent owner boundaries

- **MIB-11 / D18 World** owns World/location/hierarchy/topology/navigation/transfer truth.
- **D29 authoring-provenance** owns review/publication/provenance workflow and canonical-promotion handoff.
- **A5 Scene/Tabletop** owns runtime Scene/map-version/layer/object placement and mutation.
- **Visibility/Permissions** owns audience visibility, hidden/reveal state, occlusion authorization and line-of-sight.
- **Combat/Exploration and Action owners** own collision, cover, movement, interaction, triggers, portals and gameplay consequences.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `completed_verified`
6. **MAI-06 — Universal Import Adapter Framework** — `completed_verified`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `completed_verified`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `completed_verified`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `in_progress`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Current governed gate

Implement the bounded MAI-09 candidate on `integration/mai-09-world-scene-combat-exploration-creator-integration` from application baseline `7d073bd3c9487d665751c76d2b5a69d3991ab305`. The candidate must provide deterministic draft preflight, explicit owner request/acknowledgement plans, fail-closed stale/permission/unresolved handling, D29 creator handoff, reconciliation/recovery evidence and deterministic receipts while preserving MAI-01..08 and owner regressions.

Its exact candidate head must pass Repository Health, self-hosted Linux and Windows Validation Core, deterministic cross-platform comparison and applicable focused/predecessor/owner regressions before merge. MAI-10 may not start under this authority.

## Invariants

MAI-01..08 have no further implementation authority. MAI-09 is bounded to explicit integration orchestration on its governed branch. No vendor/editor/provider is canonical. No asset pack is assumed complete. Semantic requirements and selected art remain separable. Permissions are evidence-driven and unknown/denied/revoked stays unresolved/ineligible. Visibly-unresolved assignments cannot activate. MAI cannot infer World, Scene, visibility, gameplay or publication truth. No automatic provider acquisition exists. Migration `0022` remains unreserved absent a demonstrated durable schema delta.
