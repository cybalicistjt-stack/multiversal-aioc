# PPIA-06 — Character Appearance Creator Foundation Candidate

**Status:** bounded foundation candidate; PPIA-06 remains `started`.

This package establishes the source/design and renderer-architecture foundation for PPIA-06 without claiming completion.

## Delivered foundation

- six evidence/provenance classes separating source truth, inherited contracts, approved design contracts, Player-authored appearance, renderer metadata, and unresolved gaps;
- eighteen renderer-independent appearance identity/state layers;
- four separate compatibility dimensions;
- four renderer-support states: supported, partial, unsupported, unknown;
- a `pixel-art-v1` first-renderer contract with eight semantic render bands, stable asset IDs, semantic anchors, occlusion masks, palette zones/ramps, topology and pose support matrices, deterministic composition, deterministic lock-aware randomization, permission-safe export, and explicit failure behavior;
- seven authority domains and six cross-domain handoffs;
- twenty-four noncanonical deterministic foundation reference cases.

## Preserved boundaries

PPIA-05 remains authoritative for Species/Form biology, morphology, current Form, transformations, compatibility, visibility, hidden biological information, and unknown/source-unspecified anatomy. PPIA-06 never human-defaults unknown anatomy and never treats renderer topology as Species taxonomy.

PPIA-03 remains authoritative for Item/Asset ownership and equipment/runtime state. Equipment preview is visual projection only.

Permission filtering occurs before rendering or derivatives. Hidden Form, marker, or equipment state cannot leak through silhouettes, layer counts, missing-asset warnings, palettes, anchors, occlusion, exports, diagnostics, or AI context.

A valid Character stays valid when `pixel-art-v1` support is partial, unsupported, or unknown. Missing assets/anchors/masks never authorize silent substitution or anatomical approximation.

`pixel-art-v1` is the first renderer, not the permanent appearance model. Core Character appearance state requires no sprite, pixel, texture, mesh, or bone fields, preserving a future-3D adapter boundary.

Accessibility is semantic: mobile, keyboard, touch, screen-reader/nonvisual, high-zoom, reduced-motion, and noncolor behavior are required; color is never the only information channel.

Randomization changes only eligible Player-authored appearance choices, respects locks, is deterministic from versioned inputs, and never changes source-owned morphology/current Form, hidden data, or equipment ownership.

## Completion claim

None. This is the first bounded PPIA-06 milestone. PPIA-06 remains `started`; Inspector/action/reference and integrated workflow/completion gates remain future work.

No application runtime, STAGE-A-A2, release, deployment, tester, paid-service, production-credential, or unsupported-canon activation is authorized.
