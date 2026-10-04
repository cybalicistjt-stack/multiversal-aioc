# CAS / MCCS / CAPP / PAPT Interoperation Authority

**Document ID:** MV-CAS-INTEROP-001  
**Version:** 1.0.0  
**Status:** CANONICAL DESIGN AUTHORITY  
**Effective date:** 2026-10-03  
**Implementation authority:** none

## Core rule

**CAS is a product/profile layer, not a second authoring engine.**

- **CAS** owns the user-facing appearance control vocabulary and character-focused workflow.
- **MCCS** owns the generalized character/creature creator workspace, draft orchestration, topology-first editing surfaces and cross-output authoring workflow.
- **CAPP/PPIA** retain renderer-neutral appearance authority, Species/Form eligibility constraints, deterministic compilation, fit/coverage/version semantics and no-silent-fallback behavior.
- **PAPT/PCA** produce and validate the reusable art/component vocabulary and production derivatives consumed by CAPP/MCCS.
- **CAS-SD1** is the common pixel-density/detail authority.

## Canonical data flow

```
owner truth
(Character / Species / Form / Equipment)
          ↓ read/projection
CAS-PARAM-1 eligible semantic state
          ↓ draft lifecycle
MCCS workspace
          ↓ validation / compile request
CAPP compiler
          ↓ deterministic render plan
PAPT asset/component registry
          ↓ resolved components
CAS-SD1 renderer
          ↓
full body / portrait / token / Retrobit
```

## Ownership matrix

| Concern | Authority |
|---|---|
| Species topology / required anatomy / Form truth | Species/Form/PPIA |
| Character identity/mechanics | Character owner domain |
| Actual equipment ownership/equipped state | Inventory/Asset/Equipment |
| Appearance semantics / eligibility / renderer-neutral compilation | CAPP/PPIA |
| CAS control IDs and semantic buckets | CAS-PARAM-1 under CAPP/PPIA constraints |
| Draft workspace, edit/rebase/recovery orchestration | MCCS |
| Pixel component production, style/palette tools, QA | PAPT/PCA |
| Pixel density/detail | CAS-SD1 |
| Runtime pose/action/emotion truth | owning runtime systems |
| Photo/image matching | optional proposal adapter only |

## MCCS bindings

| CAS concern | Existing MCCS home | Disposition |
|---|---|---|
| Body proportions/silhouette | MCCS-03 | Reuse directly through stable CAS parameter IDs and ordinal→numeric adapter. |
| Appendages/modular anatomy | MCCS-03 | Reuse topology/anchor structures; Species/Form still controls eligibility/cardinality. |
| Head/sensory structures | MCCS-05 | Reuse feature/anchor model. |
| Detailed face scalar modifiers | MCCS-05 | **Gap:** add bounded parameter transport/adapter; do not create a new engine. |
| Hair/fur/feather/scale/plant coverings | MCCS-06 | Compile CAS covering parameters to governed layer/material/pattern refs. |
| Palette/material/marking layers | MCCS-06 | Reuse directly through CAPP-governed refs. |
| Wardrobe/equipment presentation | MCCS-09 | Reuse composition/fit/occlusion authority. |
| Pose/expression presentation | MCCS-11 | Reuse; never runtime action/emotion truth. |
| Portrait/token/sprite derivatives | MCCS-13 | Bind to CAS-SD1 output profiles. |
| Style/templates | MCCS-16 | Reuse configuration/profile semantics. |
| Forms/lifecycle appearance | MCCS-18 | Reuse owner-bound state adapters. |
| External/reference interchange | MCCS-19 | Use for stable semantic path mapping and loss reporting. |

## CAPP handoff shape

The future CAPP input must add a renderer-neutral CAS parameter state containing:

- CAS-PARAM-1 version;
- appearance-state ID/version;
- Species/Form/profile/topology refs;
- sorted stable parameter ID/value pairs;
- topology-gated feature instances;
- palette/layer references;
- presentation wardrobe references;
- actual-equipment projection references;
- view/output profile;
- permission projection.

CAPP validates eligibility, resolves each parameter to supported component/variant/palette choices, emits explicit unsupported/partial diagnostics where coverage is absent, and produces the deterministic render plan. Missing art never invalidates the semantic character.

## PAPT handoff shape

PAPT does **not** create arbitrary one-off character images as the core production strategy. It receives asset demand generated from CAS/CAPP parameter coverage:

```
parameter family × eligible topology × view/profile
                 ↓
required reusable component/variant/mask/anchor/palette coverage
                 ↓
PAPT production + QA
                 ↓
manifested assets
                 ↓
CAPP coverage analyzer/compiler
```

This makes art growth proportional to reusable vocabulary/coverage rather than the combinatorial number of possible characters.

## Reference-image adapter

A face/clothing/reference importer maps external evidence to **CAS semantic proposals**, not directly to renderer pixels. The same MCCS/CAPP validation path is used after import as after manual editing.

## Implementation sequence

1. Extend CAPP/CAS contracts to consume CAS-PARAM-1 and CAS-SD1 explicitly.
2. Add the MCCS-05 bounded head/face parameter adapter.
3. Generate the PAPT asset-demand/coverage ledger.
4. Produce golden reusable asset packs across easy and difficult topologies.
5. Wire the player-facing CAS UI to the existing MCCS workspace.
6. Prove deterministic full-body/portrait/token/Retrobit output.
7. Add image/reference matching.
8. Add separate Fashion/Garment Parameter Authority and clothing-reference matching.
