# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..06 COMPLETED_VERIFIED; MAI-07 IN_PROGRESS  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-06 — Universal Import Adapter Framework  
**Current item:** MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution  
**Implementation branch:** `integration/mai-07-semantic-asset-taxonomy-availability-resolver-cross-pack-substitution`  
**Implementation authority:** MAI-07 only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-06 are `completed_verified` with no further implementation authority. Owner `Continue` freshly verified canonical AIOC `759855bbeb44f38075a9a8ecf314f6c0c0c16370` and application `bc217bab20e166799b76526f6ef5d9537191b79f`, confirmed no competing MAI-07 branch or PR, re-read the completed MAI foundation, and governed-started MAI-07.

Strict MAI order authorizes MAI-07 only on the registered integration branch. MAI-08 and later remain unauthorized.

## Binding completed foundation

MAI-01..06 establish provider-neutral source/license/authority truth, canonical visual asset/package/provenance records, deterministic coordinates/projections, visual-only terrain connectivity, descriptive geometry, and deterministic source-specific adapter translation with full raw-source preservation. No provider schema or presentation construct becomes World/gameplay truth.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location/topology/navigation/transfer truth.
- **D29 authoring-provenance** retains governed publication/provenance workflow.
- **Scene/Tabletop** retains runtime scene/layer/object placement and mutation.
- **Visibility/Permissions** retains audience visibility, occlusion authorization and line-of-sight.
- **Combat/Exploration** retains collision, cover, movement, interaction and gameplay consequences.
- Visual requirements, availability and substitutions may only choose presentation assets and cannot mutate these owners.

## MAI-07 resolved contract

MAI-07 implements a provider-neutral semantic asset taxonomy and a catalog-only deterministic resolver.

### Semantic requirements

A requirement descriptor remains independent from any provider or asset pack. It can constrain acceptable MAI-02 asset kinds, semantic role, required tags and explicit compatibility tokens. Requirement identity never becomes World, Scene, Visibility or Combat truth.

### Availability evidence

Resolution distinguishes at least these states:

- `present-permitted-compatible`
- `present-denied`
- `present-unknown-permission`
- `present-incompatible`
- `missing`
- `unknown-unverified`

A candidate is eligible only when supplied/catalogued evidence establishes semantic compatibility and `useInExperience` permission is explicitly `granted`. Unknown permission remains unresolved. Denied permission is ineligible.

### Cross-pack substitution

Cross-pack substitution additionally requires explicit semantic compatibility evidence and `substitute: granted`; it never infers equivalence from filenames, provider identity, visual similarity or missing metadata. Same-pack exact-compatible candidates rank ahead of permitted cross-pack candidates when policy and requirement evidence otherwise tie.

### Deterministic ranking and manual control

Eligible candidates are filtered before ranking. Ranking uses explicit compatibility/specificity evidence plus stable package/asset/source identifiers so registry order cannot change the result. Manual assignment and override remain first-class. If a manually pinned candidate is ineligible, the resolver returns an explained unresolved/manual-rejected result rather than silently selecting another asset.

### Outcomes

The resolver preserves the established incomplete-pack outcomes:

- `exact-compatible`
- `cross-pack-permitted`
- `manual-selection`
- `approved-placeholder`
- `visibly-unresolved`

An approved placeholder is an explicit caller policy choice, never a silent fallback. Missing, incompatible, denied or unknown evidence remains visible when no authorized outcome exists.

### Receipts and diagnostics

Resolver receipts are deterministic and include requirement identity, policy, ordered candidate evidence, selected asset when any, final outcome and ordered rejection diagnostics. Rejection reasons are explainable and preserve relevant source/package/asset/provenance references.

### Acquisition boundary

Resolution operates only over supplied/catalogued evidence. It may not download, buy, authenticate to, scrape, call provider acquisition APIs, activate payment, or otherwise obtain assets.

## Explicit non-authorization

MAI-07 does not authorize MAI-08 workbench UI, MAI-09 runtime owner integration or MAI-10 corpus/performance proof. It does not authorize automatic provider acquisition/download/authentication/scraping, permission inference, unsupported-metadata discard, owner-domain mutation, migration `0022`, tester distribution, release/deployment, provider/payment activation or real-money activity.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `completed_verified`
6. **MAI-06 — Universal Import Adapter Framework** — `completed_verified`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `in_progress`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `planned`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Validation gate

The exact MAI-07 application candidate must pass the focused verifier, client typecheck and integration regression; MAI-06/05/04/03/02/01 and MIB-11 owner regressions; exact-head Repository Health; self-hosted Linux and Windows Validation Core; and deterministic cross-platform comparison before merge.

## Invariants

MAI-01..06 have no further implementation authority. MAI-07 authority is restricted to the registered branch. No vendor/editor/provider is canonical. No asset pack is assumed complete. Semantic requirements and selected art remain separable. Permissions are evidence-driven and unknown remains unresolved. Manual selection, approved-placeholder and visibly-unresolved outcomes remain first-class. No automatic provider acquisition exists. Owner-domain truth cannot be inferred from resolver choices. Migration `0022` remains unreserved absent a demonstrated durable schema delta.
