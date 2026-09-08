# P3D — Physical 3D & Miniature Pipeline

**Program ID:** P3D  
**Program name:** Physical 3D & Miniature Pipeline  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — DEFERRED FUTURE PROJECT; NO IMPLEMENTATION AUTHORITY  
**Critical path:** no  
**Automatic successor/predecessor:** none  
**Owner and final authority:** John Brandon Turner  
**Recorded:** 2026-09-07

## Purpose

P3D is the future physicalization pipeline that turns Multiversal semantic Character/creature/asset appearance into poseable 3D representations and printable miniatures. It must support at least two deliberately different visual outputs:

1. **physical-pixel-v1** — a stepped/voxel/pixel-style miniature that preserves Multiversal's pixel-art visual language in physical form;
2. **physical-detailed-v1** — a more detailed composable 3D miniature driven by the same renderer-neutral semantic appearance state.

P3D is recorded now so current asset, Character and provenance systems preserve the seams it will need later. It is deliberately **not ready to implement** and must not block the core product roadmap.

## Core architectural rule

The detailed 3D miniature is not primarily reconstructed from a low-resolution pixel sprite. Pixel art and 3D are sibling renderers over the same governed semantic appearance truth:

`Character / creature / asset truth → renderer-neutral appearance snapshot → renderer`

Possible renderers include `pixel-art-v1`, `physical-pixel-v1`, `physical-detailed-v1` and future approved renderers. Pixel fields, meshes and renderer-specific metadata must not become required Character truth.

This preserves the existing PPIA/CAPP future-renderer boundary: canonical Character state remains renderer-independent, and each renderer retains its own version/provenance/coverage metadata.

## Component strategy

P3D should use **composable atomic parts plus parametric morphing**, not a rigid one-mesh-per-character library. Species/form/topology authority determines eligible families. Typical atomic classes include heads, torsos, limbs, hands/feet, tails, wings, horns/ears, hair/surface components, equipment, props and bases. Parametric fitting handles proportions and controlled variation; attachment/anchor contracts handle equipment and appendages.

The resolver may approximate an appearance only when its approximation class and confidence are explicit. Unsupported or low-confidence anatomy remains visible to the user and may require manual choice; the program must not silently invent canonical anatomy.

## Tranche sizing rule

Every eventual P3D implementation tranche is designed for a **24-minute-or-less bounded execution target under a healthy governed environment**, including its focused construction/validation package. If the actual acceptance surface cannot credibly fit that bound, it must be split before governed start. This record creates no implementation authority.

## Future tranche map

1. **P3D-01 — Renderer-Neutral Physical Appearance Snapshot** — projection from CAPP/species/form/equipment semantics without pixel-field dependency.
2. **P3D-02 — 3D Topology-Family Contract** — humanoid, quadruped, serpentine, winged, multi-limbed and extensible nonhumanoid families.
3. **P3D-03 — Atomic Part Schema** — stable IDs, sockets/anchors, semantic roles, bounds and renderer/rights provenance.
4. **P3D-04 — Species/Form Part Eligibility & Compatibility Rules** — topology/anatomy constraints and explicit unsupported states.
5. **P3D-05 — Parametric Humanoid Component Kit** — first golden component family, not a universal anatomy assumption.
6. **P3D-06 — Nonhumanoid Component-Kit Extension Contract** — new topology kits without changing Character truth.
7. **P3D-07 — Semantic Part Resolver & Approximation Evidence** — deterministic selection/ranking, confidence and manual override.
8. **P3D-08 — Parametric Fit & Proportion Morphing** — controlled body/profile variation without unique meshes per Character.
9. **P3D-09 — Attachment, Equipment & Prop Anchor Standard** — semantic attachment compatible with Character/equipment state.
10. **P3D-10 — Rig / Skeleton Family Contract** — renderer-owned rigs mapped from topology and pose intent.
11. **P3D-11 — Pose Library, IK & Procedural Adjustment** — pose selection and constrained adaptation without mechanical-state mutation.
12. **P3D-12 — Print-Safe Pose Rules** — balance, contacts, fragile appendages, minimum clearances and support-aware alternatives.
13. **P3D-13 — Detailed Physical Renderer (`physical-detailed-v1`)** — composable detailed presentation pipeline.
14. **P3D-14 — Pixel/Stepped Physical Renderer (`physical-pixel-v1`)** — deliberately blocky/pixel-silhouette physical pipeline.
15. **P3D-15 — Equipment / Prop Composition** — wear/hold/display the Character's eligible presentation equipment without changing ownership/equipped truth.
16. **P3D-16 — Mesh Union, Cleanup & Watertight Validation** — manifold/intersection/normal/degeneracy checks and bounded repair.
17. **P3D-17 — Base, Scale, Thickness & Support-Contact Validation** — miniature profiles and printability constraints.
18. **P3D-18 — 3D Preview & Export Profiles** — GLB-class interactive preview plus governed 3MF/STL-class print outputs as appropriate.
19. **P3D-19 — Interactive Turntable & Pose Preview** — user approval surface before export.
20. **P3D-20 — ARI Registration & Derivative Provenance** — every generated mesh/preview/export registered as an ARI derivative with exact semantic inputs and renderer version.
21. **P3D-21 — Golden Cross-Renderer Character Proof** — one semantic Character → pixel sprite → pixel-style miniature → detailed miniature with shared identity/provenance and no Character rewrite.
22. **P3D-22 — Optional Print-Service / Manufacturer Adapter** — separately gated commercial/provider integration; not required for local 3D creation/export.

## Activation prerequisites

P3D remains deferred until a later owner decision explicitly selects it. Before that decision, the following foundations should normally exist:

- CAPP/PPIA renderer-neutral appearance and species/form topology authority remains valid;
- **ARI-22** is `completed_verified` so meshes/previews/exports have one reusable resource/provenance destination;
- **PAPT-16** or an explicitly sufficient replacement provides mature cross-family visual production semantics and source assets;
- **SMB-11** creator-package/version/provenance contracts are available if 3D project interchange is in scope;
- an evidence-based decision exists for the actual 3D/mesh/preview/print technology stack and licensing;
- the owner separately approves any paid generation service, print service, manufacturer, commerce or fulfillment integration.

These prerequisites are readiness conditions, not automatic activation. Completion of them must not silently place P3D on the critical path.

## Rights, safety and authority boundaries

- P3D may transform only resources/appearance elements whose rights capabilities permit the requested private/export/share/commercial action.
- Generated 3D geometry is presentation/derivative state; it cannot invent Character mechanics, species anatomy, equipment ownership, current form or canonical appearance facts.
- Third-party art/reference ownership does not imply permission to manufacture or sell derivative miniatures.
- Printability repair may change mesh engineering details but must report material visual deviations rather than silently changing identity-defining traits.
- Commercial printing/ordering is outside the core renderer and remains a later provider/commerce gate.

## Why this is deferred

ARI and SAA create immediate product leverage from assets users already have or Multiversal already generates. P3D has additional technology, geometry, topology, licensing, printability and provider questions and should not delay core gameplay, creator UX, beta readiness or release. Recording it now prevents today's systems from making renderer-specific choices that would make physicalization expensive later.