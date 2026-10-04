# CAS Integration Design Closure — Parameter → MCCS → CAPP → PAPT

**Document ID:** MV-CAS-INTEGRATION-CLOSURE-001  
**Version:** 1.0.0  
**Status:** DESIGN CLOSED FOR IMPLEMENTATION PLANNING  
**Effective date:** 2026-10-03  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none

## What is now defined

The CAS appearance stack now has durable design authority for:

1. **CAS-SD1** — native pixel density, derivative sizes, detail grammar and no-generative-core rendering.
2. **CAS-PARAM-1** — 61 stable core parameter paths plus topology-gated structural feature instances.
3. **CAS/MCCS/CAPP/PAPT interoperation** — CAS is a constrained product/profile layer over MCCS, not a second engine.
4. **CAS-CAPP-HANDOFF-1** — deterministic request, validation, resolver, coverage and PAPT-demand behavior.
5. **CAS-MCCS-TRANSPORT-1** — exact use of existing MCCS contracts plus the bounded MCCS-05 detailed-head scalar transport gap.
6. **CAS-CAPP05-EXT-1** — design changes required for CAPP-05 to consume CAS-PARAM-1 and CAS-SD1.
7. **CAS-PAPT-DEMAND-1** — reusable asset-production demand families and anti-combinatorial rules.
8. **CAS-GOLDEN-1** — ten golden Species/profile proofs spanning ordinary and difficult topology/state cases.

## Key architecture

```
owner truth
   ↓
CAS-PARAM-1
   ↓
MCCS workspace/authoring transport
   ↓
CAPP validation + deterministic resolution
   ↑
PAPT reusable asset coverage
   ↓
CAS-SD1 renderer
   ↓
full body / portrait / token / Retrobit
```

## What the design deliberately does not do

- no second CAS engine beside MCCS;
- no 300+ unconstrained 3D slider model;
- no required generative image rendering;
- no baked-raster character combinations as the default asset model;
- no silent nearest-value snapping;
- no humanoid fallback for nonhuman topology;
- no equipment/biology/mechanics mutation through appearance controls;
- no runtime activation by virtue of these design documents.

## Implementation-ready deltas

### A. MCCS

Implement the bounded CAS parameter adapter/transport:

- body values bind to MCCS-03 stable parameter/control IDs;
- detailed face values gain a compatible MCCS-05 parameter channel or immediately-adjacent adapter;
- surface refs use MCCS-06;
- wardrobe/equipment use MCCS-09;
- presentation uses MCCS-11;
- outputs use MCCS-13;
- Forms/interchange use MCCS-18/19.

### B. CAPP

Extend CAPP-05 to accept CAS-PARAM-1 semantic state and CAS-SD1 profiles, then emit:

- semantic appearance hash;
- parameter/feature resolution receipts;
- projection-loss declarations;
- PAPT production-demand diagnostics;
- logical/native/output canvas metadata.

Historical CAPP assets remain provenance-preserved and require explicit CAS-SD1 migration classification.

### C. PAPT

PAPT begins with reusable vocabulary coverage, not character combinations:

- body/silhouette foundations;
- bounded body proportion variants/anchor profiles;
- head/face families and modifiers;
- covering families;
- palette/material/pattern/marking infrastructure;
- topology-gated features;
- wardrobe/equipment fit assets;
- view-specific semantic derivatives.

The first asset pack targets CAS-GOLDEN-1, not all Species at once.

### D. Golden certification

Prove Human, Gray, Vespin, Moravi, Rakuuta, Arborae, Suula, ManyToms, Mythragara and Toba-Madra through all CAS-SD1 views. This is the point where we can judge whether 61 semantic paths provide enough real customization without false precision.

## Image matching comes after the deterministic golden path

Once the manual semantic controls compile correctly, image/reference matching may propose CAS-PARAM-1 values. It must use the same downstream validation and rendering path. That prevents scan-in technology from becoming a separate appearance system.

## Fashion comes after this base is proven

CAS-WARD-001 already provides the wardrobe bridge. Detailed garment construction is intentionally the next separate authority: garment family, silhouette, length, sleeve structure, neckline/collar, fit, hem, closure, panels, pockets, material, pattern, trim, palette and topology accommodation.

The Fashion authority will therefore reuse:

- CAS-SD1 density/detail limits;
- CAS parameter/profile conventions;
- CAPP fit/anchor/mask/occlusion rules;
- MCCS-09 presentation composition;
- PAPT reusable component production;
- the same optional image-reference proposal architecture.

## Implementation boundary

This content-design closure makes the work **implementation-ready** but does not start a software implementation lane.

Starting application changes must be separately selected/governed under OPS3 so active GPR/CWKS work is not silently borrowed or disrupted.
