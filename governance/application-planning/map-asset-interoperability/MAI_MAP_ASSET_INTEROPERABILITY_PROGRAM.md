# MAI — Map & Visual Asset Interoperability

**Program ID:** MAI  
**Status:** IN PROGRESS — MAI-01..07 COMPLETED_VERIFIED; MAI-08 IN_PROGRESS  
**Activation:** DPL-14 completed_verified  
**Completed through:** MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution  
**Current item:** MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench  
**Implementation branch:** `integration/mai-08-asset-intake-wizard-map-composer-palette-workbench`  
**Implementation authority:** active for MAI-08 bounded scope only  
**Successor after MAI:** AAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

MAI-01 through MAI-07 are `completed_verified` with no further implementation authority. Owner `Continue` freshly verified canonical AIOC head `0c231bfc74909960692863d890cead0301deba14` and application head `c7aeff6470199366ba033cce892e6816f9253d8a`, re-read the completed MAI-01..07 evidence chain, and resolved the bounded MAI-08 intake/composer/palette/workbench contract.

MAI-08 is now `in_progress` only on `integration/mai-08-asset-intake-wizard-map-composer-palette-workbench`. MAI-09 and later remain unauthorized.

## Binding completed foundation

MAI-01..07 establish provider-neutral source/license/authority truth, canonical visual asset/package/provenance records, deterministic coordinates/projections, visual-only terrain connectivity, descriptive geometry, deterministic source-specific adapter translation with full raw-source preservation, and a catalog-only semantic availability resolver with explicit permission/provenance evidence, deterministic cross-pack substitution, manual control, and explicit placeholder/unresolved outcomes.

No provider schema, presentation construct, resolver choice or workbench choice becomes World/gameplay truth.

## Persistent owner boundaries

- **MIB-11 / D18 World** retains canonical World/location/topology/navigation/transfer truth.
- **D29 authoring-provenance** retains governed publication/provenance workflow.
- **Scene/Tabletop** retains runtime scene/layer/object placement and mutation.
- **Visibility/Permissions** retains audience visibility, hidden state, occlusion authorization and line-of-sight.
- **Combat/Exploration** retains collision, cover, movement, interaction, trigger/portal and gameplay consequences.
- MAI-08 may author presentation drafts and evidence-backed asset assignments only. Integration into those owner domains is MAI-09 work and is not authorized here.

## MAI-08 governed contract

### Asset intake wizard

Intake is limited to user-supplied or already-catalogued source/package/asset evidence and completed MAI-06 import results. The bounded stages are:

1. source evidence;
2. import-adapter validation;
3. license/provenance review;
4. catalog/semantic classification;
5. eligibility/resolution preview;
6. workbench accept or explicit unresolved outcome.

Unsupported, malformed, denied, unknown or unverified evidence remains explicit. The wizard performs no provider API ingestion, automatic download, purchase, authentication, scraping, payment or acquisition.

### Palette

The palette consumes MAI-07 semantic requirements, availability evidence and resolver outcomes. Permitted-compatible candidates may be selectable. Denied, unknown-permission, incompatible, missing and unknown/unverified states remain visible evidence but cannot be converted into allowed use.

Manual assignment/override remains first-class. An ineligible manual request stays explicitly rejected/`visibly-unresolved`; it cannot silently fall back. Approved placeholders remain explicit, must themselves be permitted, and are never silently substituted.

### Map composer and workbench

The composer/workbench owns only a reversible `presentation-authoring-draft`. It may consume:

- MAI-02 asset/package/layer/placeable records;
- MAI-03 projection/transform data;
- MAI-04 visual terrain/connectivity grammar;
- MAI-05 descriptive geometry/overhead/occlusion/interaction hints;
- MAI-06 source/import diagnostics and provenance;
- MAI-07 semantic requirements, eligibility evidence, diagnostics and selected asset references.

Bounded draft operations include staging/removing asset references, adding/removing draft layers/placeables, setting presentation transforms/order, assigning/clearing semantic assets, selecting/clearing approved placeholders, and preserving explicit unresolved states. Every operation must be reversible and must not rewrite source evidence or owner truth.

### Deterministic save boundary

Save/export produces a deterministic MAI-08 draft snapshot/receipt for later MAI-09 integration. Canonical serialization must use stable IDs and ordered evidence/diagnostics so input collection ordering or platform cannot change the receipt.

This governed start demonstrates no required durable database schema delta. Migration `0022` remains unreserved. MAI-08 implementation must remain in contract/client-local/test-fixture boundaries unless a concrete persistence requirement is separately demonstrated and governed.

## Validation gate

The MAI-08 exact candidate must pass:

- a focused MAI-08 verifier;
- client typecheck and integration regression;
- MAI-07..01 predecessor regressions;
- applicable MIB-11/D18, D29, Scene/Tabletop, Visibility/Permissions and Combat/Exploration owner-boundary checks;
- exact-head Repository Health;
- self-hosted Linux and Windows Validation Core;
- deterministic cross-platform comparison.

## Tranches

1. **MAI-01 — Ecosystem, Format, License & Authority Survey** — `completed_verified`
2. **MAI-02 — Canonical Map Asset, Placeable & Package Schema** — `completed_verified`
3. **MAI-03 — Grid, Coordinates, Scale & Projection Engine** — `completed_verified`
4. **MAI-04 — Terrain, Autotile & Connectivity Grammar** — `completed_verified`
5. **MAI-05 — Layers, Objects, Overhead, Occlusion & Interactive Geometry** — `completed_verified`
6. **MAI-06 — Universal Import Adapter Framework** — `completed_verified`
7. **MAI-07 — Semantic Asset Taxonomy, Availability Resolver & Cross-Pack Substitution** — `completed_verified`
8. **MAI-08 — Asset Intake Wizard, Map Composer, Palette & Workbench** — `in_progress`
9. **MAI-09 — World, Scene, Combat, Exploration & Creator Integration** — `planned`
10. **MAI-10 — Diverse Corpus, Performance & Interoperability Proof** — `planned`

## Invariants

MAI-01..07 have no further implementation authority. MAI-08 is authorized only on its governed branch and only for supplied/catalogued intake, presentation-authoring draft/composer, evidence-aware palette/workbench, manual/reversible controls, explicit placeholder/unresolved states and deterministic draft diagnostics/receipts. No vendor/editor/provider is canonical. No asset pack is assumed complete. Semantic requirements and selected art remain separable. Permissions are evidence-driven and unknown remains unresolved. No automatic provider acquisition exists. Owner-domain truth cannot be inferred from authoring or resolver choices. MAI-09+ remain unauthorized. Migration `0022` remains unreserved absent a demonstrated durable schema delta.
