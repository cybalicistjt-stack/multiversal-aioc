# CAS → CAPP Compiler Handoff Authority

**Document ID:** MV-CAS-CAPP-HANDOFF-001  
**Contract ID:** CAS-CAPP-HANDOFF-1  
**Version:** 1.0.0  
**Status:** CANONICAL DESIGN AUTHORITY  
**Effective date:** 2026-10-03  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none

## Purpose

This contract defines the exact renderer-neutral handoff from **CAS-PARAM-1 semantic appearance state** into CAPP.

It does not create a second renderer and does not make MCCS or PAPT appearance authority.

```
CAS-PARAM-1 state
       ↓
MCCS draft/workspace lifecycle
       ↓
CAS-CAPP-HANDOFF-1
       ↓
CAPP eligibility + deterministic resolver
       ↓
parameter/feature resolution receipts
       ↓
CAPP render plan
       ↑
PAPT manifested reusable assets
       ↓
CAS-SD1 output profile
```

## Required compile request

A compile request identifies:

- appearance state ID/version;
- CAS-PARAM-1 version;
- CAS-SD1 version;
- owner identity/version;
- Species/Form/profile/topology/biology snapshot;
- sorted parameter values;
- topology-gated feature instances;
- wardrobe and actual-equipment projection refs where applicable;
- renderer/version and locked asset pack/version;
- requested view profile and pose;
- permission projection.

Parameter state is renderer-neutral. It does not store asset filenames.

## Canonical parameter value forms

- **ordinal5:** integer -2..+2;
- **ordinal7:** integer -3..+3;
- **enum_ref:** stable governed family/value ref;
- **palette_zone_set_ref:** stable semantic palette-zone ref;
- **layer_set_ref:** ordered governed layer refs;
- **profile_ref:** stable presentation/profile ref.

Unconstrained floating-point values are not canonical CAS state.

For current MCCS numeric APIs, an adapter may expose ordinal5 as `step/2` and ordinal7 as `step/3`, but the integer CAS semantic step remains authoritative.

## Validation order

1. Verify CAS-PARAM-1 and CAS-SD1 versions.
2. Authorize owner/Species/Form/biology/topology state.
3. Permission-filter before asset matching or diagnostics.
4. Validate parameter IDs/types/bounds.
5. Apply Species/Form/CAPP eligibility and required/read-only constraints.
6. Validate feature kind/cardinality/anchors.
7. Preserve biological versus cosmetic channels.
8. Preserve presentation wardrobe versus actual equipment ownership.
9. Normalize and hash semantic appearance.
10. Resolve semantic values to renderer strategies.
11. Resolve topology/view-compatible assets, variants, masks and palettes.
12. Validate fit/anchors/occlusion.
13. Produce per-parameter and per-feature coverage receipts.
14. Assemble deterministic ordered CAPP render plan.
15. Hash the render plan.
16. Produce the requested CAS-SD1 derivative.

## Resolver classes

| ID | Resolver | Purpose |
|---|---|---|
| CASRES-01 | Component family select | Discrete family chooses reusable asset family. |
| CASRES-02 | Discrete variant select | Ordinal/enum selects an exact supported variant; no freeform raster warp. |
| CASRES-03 | Integer-anchor composition | Recompose compatible segments using integer logical-pixel anchors. |
| CASRES-04 | Palette-zone map | Apply semantic controlled palette without duplicate geometry raster. |
| CASRES-05 | Mask/pattern overlay | Apply governed masks/markings/pattern procedures. |
| CASRES-06 | Layer/profile reference | Resolve wardrobe, age, pose or other governed layer/profile refs. |
| CASRES-07 | Read-only owner projection | Project actual equipment or other external owner state. |
| CASRES-08 | Semantic-only/derived | Preserve semantic/derived state that does not require unique raster art. |

These classes are important because they stop PAPT from producing a complete baked sprite for every possible character combination.

## Allowed deterministic renderer operations

CAPP may use:

- authorized component-family selection;
- discrete variant selection;
- integer logical-pixel anchor movement;
- integer-aligned layer composition;
- masks;
- controlled palette remapping;
- approved deterministic pattern/marking procedures;
- declared occlusion;
- nearest-neighbor integer scaling.

CAPP may not solve missing coverage with freeform raster warping, subpixels, antialiasing repair, arbitrary rotation, silent humanoid substitution, invented anatomy/equipment, or required generative image synthesis.

## Resolution receipts

Every active CAS parameter receives a receipt containing:

- stable parameter ID;
- semantic value;
- resolver class;
- support state;
- resolution refs;
- diagnostics.

Every topology-gated feature receives the analogous feature receipt.

A **semantically valid character may have partial or unsupported renderer coverage**. Missing art is a production problem, not permission to rewrite the character.

## Coverage behavior

If exact semantic coverage is unavailable:

1. keep the semantic value;
2. emit partial/unsupported/unknown coverage;
3. emit a PAPT production-demand diagnostic;
4. render whatever valid layers remain;
5. allow the user to explicitly choose another supported appearance value if they want.

CAPP may **not silently snap** an unsupported semantic value to the nearest supported appearance.

## MCCS reuse

CAS does not duplicate MCCS.

- MCCS-03 carries body morphology/silhouette and structural appendages.
- MCCS-05 carries head/sensory feature topology and anchors.
- MCCS-06 carries surface/material/pattern/marking refs.
- MCCS-09 carries wardrobe/equipment presentation.
- MCCS-11 carries pose/expression presentation.
- MCCS-13 carries derivative/output profiles.

The identified integration gap remains detailed face scalars: current MCCS-05 does not yet provide a generic stable parameter/value channel. The implementation solution is a bounded adapter/contract extension, not another engine.

## PAPT demand bridge

When coverage is missing, demand is expressed in reusable terms:

```
parameter/feature
 + semantic value/family
 + topology
 + requested view
 + resolver class
 + anchors/masks
        ↓
reusable PAPT asset demand
```

PAPT should prefer:

- reusable component families;
- discrete bounded variants;
- palette maps instead of recolored duplicate geometry;
- masks/overlays instead of baked pattern combinations;
- composable independent pieces instead of pre-rendered cross-products.

A bounded variant matrix is justified only where independent composition cannot retain CAS-SD1 quality.

## CAS-SD1 views

| Profile | Native logical | Output/derivation |
|---|---:|---|
| Full body | 128×160 | 256×320 nearest-neighbor 2× |
| Portrait | 96×96 | 192×192 nearest-neighbor 2× |
| Token | 64×64 | 128×128 nearest-neighbor 2× |
| Retrobit Detailed | 64×80 | semantic re-render |
| Retrobit Normal | 32×40 | semantic re-render |
| Retrobit Micro | 16×20 | semantic re-render |

Smaller views may intentionally lose lower-priority detail under CAS-SD1. That is a declared view projection loss, not deletion of semantic appearance.

## Image/reference import

Photo/sketch matching ends **before** this compile handoff. Once the user accepts or edits the proposed match, the result becomes ordinary CAS-PARAM-1 state and follows exactly the same CAPP path as manual customization.

## Next design outputs

1. MCCS-05 bounded CAS head/face parameter transport.
2. CAPP-05 CAS-PARAM-1 input/resolution extension.
3. PAPT parameter-driven asset demand and coverage ledger.
4. Golden cross-topology CAS/CAPP/PAPT reference profiles.

This contract grants no runtime activation or application-code authority.
