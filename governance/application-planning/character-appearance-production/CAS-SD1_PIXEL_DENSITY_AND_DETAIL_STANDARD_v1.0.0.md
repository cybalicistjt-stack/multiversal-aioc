# Multiversal CAS-SD1 Pixel Density and Detail Standard

**Document ID:** MV-CAS-SD1-PIXEL-STANDARD-001  
**Version:** 1.0.0  
**Status:** CANONICAL — OWNER APPROVED  
**Effective date:** 2026-10-03  
**Owner and final authority:** John Brandon Turner  
**Domain:** Character Appearance Studio (CAS), CAPP, PAPT, Retrobit appearance derivatives  
**Renderer family:** `pixel-art-v1`

## 1. Canon decision

The approved Multiversal Character Appearance Studio standard-definition pixel-art foundation is **CAS-SD1**.

CAS-SD1 exists to preserve a deliberate pixel-art visual language while allowing meaningful character and clothing customization, minimizing authored-art burden, minimizing stored raster duplication, and keeping the core appearance renderer deterministic and usable without generative AI.

This document locks the native logical resolutions, presentation resolutions, density relationship, derivative sizes, coordinate rules, resampling rules, detail priorities, and renderer boundaries required for future CAS/CAPP/PAPT work.

This standard extends the existing PPIA-06/CAPP pixel-art contracts. For pixel density, logical-vs-output resolution, and derivative interpretation, this document is the later owner-approved authority. Existing CAPP rules that do not conflict with this standard remain in force.

## 2. Normative resolution classes

| Profile | Native logical grid | Standard output | Scale | Safe inset, native | Safe inset, output | Purpose |
|---|---:|---:|---:|---:|---:|---|
| `cas_sd_full_body` | **128 × 160** | **256 × 320** | **2×** | **8 px** | **16 px** | Primary CAS standard-definition full-body view |
| `cas_sd_portrait` | **96 × 96** | **192 × 192** | **2×** | **6 px** | **12 px** | Face/head customization and portrait presentation |
| `cas_sd_token` | **64 × 64** | **128 × 128** | **2×** | **4 px** | **8 px** | Tactical/token presentation |
| `retrobit_detailed` | **64 × 80** | integer-scaled as needed | profile-defined | profile-defined | derived | Detailed Retrobit character sprite |
| `retrobit_normal` | **32 × 40** | integer-scaled as needed | profile-defined | profile-defined | derived | Normal Retrobit character sprite |
| `retrobit_micro` | **16 × 20** | integer-scaled as needed | profile-defined | profile-defined | derived | Micro/board/iconic Retrobit character sprite |

### 2.1 Interpretation of existing CAPP canvases

The existing CAPP dimensions:

- 256 × 320 full-body,
- 192 × 192 portrait,
- 128 × 128 tactical token,

are retained as the standard **2× presentation/output canvases** for CAS-SD1.

They are no longer to be interpreted, for future CAS-SD1 production, as the native authored logical density.

The corresponding native authored logical grids are 128 × 160, 96 × 96, and 64 × 64.

### 2.2 Logical pixel

A **logical pixel** is the smallest authored raster unit in CAS-SD1.

A 2× output pixel block represents one logical pixel. Scaling a native asset to its standard output adds no visual information and may not introduce new edge smoothing, intermediate colors, or subpixel placement.

## 3. Coordinate and density contract

For CAS-SD1:

- origin is the top-left of the logical canvas;
- X increases rightward;
- Y increases downward;
- authored anchors use integer logical-pixel coordinates;
- masks use the same logical coordinate space as the asset they control;
- occupancy bounds are integer logical-pixel bounds;
- palette zones are resolved before output scaling;
- standard output coordinates are exactly native coordinates multiplied by 2;
- fractional anchor placement is forbidden;
- fractional raster translation is forbidden;
- non-integer sprite scaling is forbidden for canonical pixel-art output.

Display/UI zoom may use any **integer nearest-neighbor multiplier** without becoming a new canonical asset class.

## 4. Raster and transformation rules

CAS-SD1 core sprite layers require:

- nearest-neighbor sampling;
- hard pixel edges;
- integer translation;
- integer-aligned layer composition;
- deterministic layer ordering;
- deterministic mask application;
- deterministic palette-zone resolution.

The following are forbidden in canonical `pixel-art-v1` CAS-SD1 rendering unless a later owner-approved renderer profile explicitly replaces this rule:

- antialiasing;
- bilinear/bicubic filtering;
- blur used to smooth sprite edges;
- subpixel transforms;
- arbitrary-angle raster rotation;
- pseudo-3D orbit;
- freeform raster warping to force one topology into another;
- silent anatomy approximation;
- silent garment/equipment fit distortion.

Discrete authored orientations, poses, topology variants, or replacement assets are allowed. They are not arbitrary transforms.

## 5. Native-first storage rule

Canonical pixel asset source rasters SHOULD be stored at their native logical resolution.

The normal 2× presentation outputs are derivatives and SHOULD be produced deterministically at render/export time or stored only as caches/exports when needed.

This rule exists to:

1. reduce redundant asset storage;
2. prevent the 2× presentation raster from becoming a second source of truth;
3. ensure the same native asset can feed CAS, token, export, and derived render profiles;
4. preserve exact reproducibility.

Stable asset identity, provenance, topology compatibility, masks, anchors, palette zones, and semantic metadata remain authoritative over filenames or display names.

## 6. View independence

The CAS-SD1 portrait and token are **semantic render profiles**, not mandatory crops or naïve resizes of the full-body raster.

The same semantic appearance state may therefore produce:

- a 128 × 160 full-body representation;
- a 96 × 96 portrait representation with materially greater face/head readability;
- a 64 × 64 token representation optimized for tactical recognition.

A facial choice may be strongly visible in the portrait and only subtly visible in the full-body view without representing different character truth.

No view may invent a semantic feature absent from authorized appearance state.

## 7. Retrobit derivation rule

Retrobit appearances consume the same authorized semantic appearance state used by CAS.

The canonical Retrobit profiles are:

- Detailed: 64 × 80;
- Normal: 32 × 40;
- Micro: 16 × 20.

These are **semantic re-renders**, not mandatory downscaled screenshots of the 128 × 160 full-body sprite.

When moving to a smaller profile, the renderer intentionally simplifies low-priority detail while preserving identity-critical information.

The same character may therefore be represented by different raster abstractions while remaining the same semantic appearance.

## 8. Detail-priority grammar

When a target profile cannot carry every authored detail, preserve information in this priority order:

1. **Topology and silhouette** — body topology, limb/appendage count and placement, major outline, height/width relationship.
2. **Major body proportions** — torso/limb/head proportions and posture cues that materially distinguish the appearance.
3. **Identity-critical head/face structures** — head silhouette, muzzle/beak/snout, ears, horns, antennae, prominent facial field, major eye/hair/covering placement.
4. **Hair/covering silhouette** — hairstyle, mane, feather, crest, fur or equivalent major covering shape.
5. **Garment silhouette and layering** — jacket/coat length, sleeve shape, trouser/skirt/dress silhouette, major armor or clothing layers.
6. **Major palette zones** — biological base coloration, large garment color blocks, high-value contrast relationships.
7. **Recognizable accessories and large garment construction** — belts, boots, collars, lapels, large closures, bags, major jewelry, armor plates.
8. **Medium markings/patterns/trim** — stripes, motifs, piping, paneling, visible seams or patterned zones.
9. **Microdetail** — tiny fasteners, stitching, very small jewelry, individual decorative marks, micro-highlights.

A smaller derivative may simplify or omit lower-priority details. It may not silently change higher-priority semantic identity.

## 9. CAS-SD1 clothing readability target

At the 128 × 160 native full-body standard, clothing must be capable of communicating meaningful differences in at least:

- garment family;
- overall silhouette;
- garment length;
- sleeve or limb-covering structure;
- neckline/collar class when visually relevant;
- waist position or major fit relationship;
- hem shape;
- major layering order;
- major closure placement;
- major pockets/panels where readable;
- boots/shoes/footwear silhouette;
- belts and medium-to-large accessories;
- palette zones;
- material-class cues through controlled pixel treatment;
- large pattern or trim motifs;
- topology accommodations such as additional arms, wings, tails, unusual heads, nested appendages, or composite bodies when supported.

CAS-SD1 is not required to resolve every real-world stitch, textile weave, micro-embroidery element, pore, eyelash, or other sub-pixel-scale physical detail.

The design target is **meaningful customization through silhouette, construction, palette, material cues, and selective detail**, not simulation of unlimited physical detail.

## 10. Palette and shading boundary

CAS-SD1 inherits CAPP/PPIA requirements for:

- semantic palette zones;
- controlled ramps;
- biological-versus-cosmetic separation;
- non-color labels;
- color never being the only semantic carrier.

This standard does **not** impose one universal total-color count across all characters, species, materials, garments, effects, or worlds.

Continuous antialiased gradients are not part of the core sprite grammar. Any dithering, special-effect ramp, or material-specific shading grammar remains governed by the applicable pixel style authority and must preserve the CAS-SD1 density rules.

## 11. Non-humanoid and exceptional topology rule

CAS-SD1 density is universal; humanoid geometry is not.

A character is never compressed, warped, amputated, or reinterpreted merely to force it into a humanoid template.

If a valid topology cannot be represented within a standard frame without violating anatomy or identity, the renderer must report partial/unsupported coverage or use a separately governed extended-topology framing profile.

Any future extended topology canvas must preserve the same logical-pixel density and semantic rules. It may not solve the problem by silently lowering density or distorting anatomy.

## 12. Deterministic core and AI boundary

The core CAS-SD1 appearance renderer is **deterministic asset composition**, not generative image synthesis.

Core rendering must remain functional with generative AI disabled.

The renderer may deterministically combine:

- semantic appearance choices;
- topology-compatible body/component assets;
- anchors;
- masks;
- palette zones;
- occlusion rules;
- wardrobe/equipment projections;
- pose/view definitions;
- controlled procedural markings or effects approved by the renderer contract.

AI or ML may later exist as an **optional input/proposal adapter** for operations such as interpreting a photograph, sketch, or clothing reference. Such an adapter may propose supported CAS parameters, but it does not become appearance truth and does not replace the deterministic renderer.

Imported or inferred settings require the same explicit user review/acceptance and constraint validation as manually selected CAS settings.

## 13. Source-to-derivative model

Normative flow:

```
authorized Character / Species / Form truth
                ↓
semantic CAS appearance state
                ↓
deterministic CAPP/CAS render plan
                ↓
native CAS-SD1 logical assets
        ┌───────┼────────┐
        ↓       ↓        ↓
  full body   portrait   token
  128×160     96×96      64×64
        ↓
  optional deterministic 2× presentation/export
        ↓
  256×320 / 192×192 / 128×128

semantic appearance state
        ↓
Retrobit profile compiler
        ↓
64×80 / 32×40 / 16×20 semantic re-renders
```

## 14. Migration and compatibility rule

Existing historical CAPP artifacts are preserved.

This canon does not silently rewrite old raster assets or their provenance.

Future CAS-SD1-compatible assets must declare the new density/profile metadata. A legacy asset that was authored directly at 256 × 320, 192 × 192, or 128 × 128 is not automatically assumed to be a valid 2× CAS-SD1 derivative.

Migration must classify legacy assets explicitly and either:

- verify that they already conform to the CAS-SD1 logical grid;
- derive/re-author an appropriate native source;
- preserve them as a legacy renderer/profile asset;
- or report unsupported/partial migration.

No silent resampling or provenance rewriting is allowed.

## 15. Scope boundary

This canon locks the **visual density foundation**.

It does not, by itself:

- modify the application runtime;
- activate the full Appearance Studio;
- rewrite CAPP-03/CAPP-05/CAPP-07/CAPP-08 implementation;
- create new species biology;
- change equipment ownership or mechanics;
- define the complete CAS parameter registry;
- define the complete fashion/garment primitive registry;
- authorize public marketplace functionality;
- authorize generative-AI dependence.

Those are follow-on design/integration tasks.

## 16. Required follow-on work

Before Fashion Studio is finalized, the next CAS/CAPP design pass must:

1. map existing CAS/CAPP semantic parameters against CAS-SD1 visibility/detail limits;
2. define the minimum useful CAS parameter registry rather than copying 300+ high-resolution 3D face sliders;
3. define image/reference-to-supported-parameter matching as a proposal workflow;
4. update CAPP/PAPT density metadata to consume CAS-SD1 explicitly;
5. define golden reference characters across ordinary and difficult topologies;
6. verify clothing primitives against CAS-SD1 before expanding the fashion system;
7. preserve a non-generative deterministic renderer as the mandatory baseline.

## 17. Golden-reference decision

The owner-approved comparison sheet produced on 2026-10-03 is the visual decision reference for this canon.

The normative authority is this text plus its machine-readable companion. The visual sheet illustrates the intended density/readability target but does not override written dimensions, transformation rules, semantic authority, provenance, or topology constraints.
