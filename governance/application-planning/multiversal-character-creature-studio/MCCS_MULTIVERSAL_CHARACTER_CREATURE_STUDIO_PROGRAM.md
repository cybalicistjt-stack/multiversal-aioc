# MCCS — Multiversal Character & Creature Studio

**Program ID:** MCCS  
**Program name:** Multiversal Character & Creature Studio  
**Version:** 0.2.0 — PDCP reduced  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after MCS effective golden gate  
**Successor:** MNCS-01  
**Owner and final authority:** John Brandon Turner  
**Implementation authority:** none

## Purpose

MCCS is Multiversal's entity-centric **appearance/presentation creator** for governed Characters, NPCs, creatures, animals, mounts, familiars, pets, monsters, constructs and alternate Forms. It is not a second Character, Species, Form, Creature, Inventory, population or Asset database.

The governing flow remains:

`canonical entity/body/equipment truth → renderer-neutral appearance projection → creator draft/override layer → renderer/output profile`

Appearance authoring is **presentation-only unless an owning contract explicitly accepts a proposal**. Pixels, meshes, sliders, poses, textures, visual variants and renderer derivatives never silently become body, mechanics, equipment ownership, relationship, population or live-state truth.

## PDCP reduction

Historical baseline: **21 tranches**. Effective implementation/proof plan: **11 tranches**.

The authoritative family reduction receipt is `governance/application-planning/preimplementation-design-closure/PDCP_MCCS_REDUCTION_RECEIPT.json`; detailed closure is `PDCP_MCCS_FAMILY_DESIGN_CLOSURE.md`.

The surviving order is:

`MCCS-01 → MCCS-03 → MCCS-05 → MCCS-06 → MCCS-09 → MCCS-11 → MCCS-13 → MCCS-16 → MCCS-18 → MCCS-19 → MCCS-21`

Sparse historical IDs are intentional. `MCCS-01` and `MCCS-21` remain stable start/golden milestones.

## Owner boundaries

MCCS consumes rather than duplicates:

- **Character/NPC/Creature + Species/Form/PPIA:** canonical identity, topology eligibility, Form/state, mechanics and live entity truth.
- **CAPP/PPIA:** renderer-neutral appearance authority, compilation, fit/coverage/version/accessibility semantics.
- **PAPT/PCA:** reusable character-asset, rig, garment, motion, image/sprite, style-generation and local-production primitives.
- **Inventory/Asset/equipment owners:** ownership, equipped/install state and item mechanics.
- **Mount/familiar/pet/companion owners:** relationship and gameplay truth.
- **MNCS:** NPC/creature/group/population identity and progressive construction. MCCS may visually vary an owner-supplied group but never creates population truth.
- **ARI/PCA:** generic resource identity, rights/provenance, derivative lineage, version/review and import/export infrastructure.
- **Animation/Scene/Combat/Dialogue:** runtime pose/action/placement authority.
- **PDCP Packet 07:** generic preview, draft, recovery, explanation and debug semantics.
- **P3D:** future physical/3D implementation when separately activated.

MCCS remains topology-first, not humanoid-first. Unsupported anatomy or renderer features remain explicit `unsupported`/`unresolved` states rather than being forced into humanoid approximations.

## Effective tranches

### MCCS-01 — Creator Workspace, Renderer-Neutral Projection, Draft/Rebase & Authority Contract

Implement one versioned appearance workspace over owner records and CAPP/PPIA renderer-neutral projection. Include stable draft IDs, authority dispositions, stale-owner detection, refresh/rebase, conflict reporting, history/recovery, output-profile references and ARI asset references. This tranche absorbs historical MCCS-01 and MCCS-02.

### MCCS-03 — Topology, Morphology, Silhouette, Appendage & Modular Anatomy Authoring

Implement the topology-aware component/parameter kernel for humanoid/biped, quadruped, serpentine, winged, multi-limbed, aquatic, composite, constructed/modular and extensible families. Include proportion/silhouette controls and eligible tails, wings, fins, extra limbs, tentacles and modular parts with compatibility/anchor validation. This tranche absorbs historical MCCS-03, MCCS-04 and MCCS-08.

### MCCS-05 — Head, Face, Sensory Feature & Expression Anatomy Authoring

Implement topology-aware head/sensory anatomy including eyes or other sensory organs, mouths/beaks/mandibles, ears, horns/antlers/tusks/crests and expression-capable structures without requiring a human face plan.

### MCCS-06 — Coverings, Color, Material, Pattern, Marking & Surface-Layer Studio

Implement the shared layered-surface authoring substrate for hair, fur, feathers, scales, shell/plates, skin-like surfaces, palettes, materials, markings, stripes/spots, tattoos/scars where appearance-authorized, paint/makeup and renderer-supported emissive presentation. This tranche absorbs historical MCCS-06 and MCCS-07.

### MCCS-09 — Wardrobe, Equipment Fit, Accessories, Props & Linked-Being Presentation Composition

Implement appearance projection of worn/carried equipment, presentation-only outfits, layer/occlusion/fit diagnostics, accessories/props and composition with separate mounts, familiars, pets or companions. Canonical ownership and relationships remain external. This tranche absorbs historical MCCS-09 and MCCS-10.

### MCCS-11 — Pose, Gesture, Expression, Rig, Anchor, IK & Retarget Preview

Implement topology-aware pose/expression authoring integrated with PAPT/PCA/local rig/anchor/IK/retarget preview helpers. Report incompatibilities explicitly. Pose state remains presentation unless an owning runtime explicitly projects current state. This tranche absorbs historical MCCS-11 and MCCS-12.

### MCCS-13 — Multi-Profile Derivative Rendering

Produce portraits, dialogue busts, reference cards, transparent cutouts, tokens, paper-doll/inventory views, top-down/isometric derivatives, thumbnails, sprites, stance sheets and animation-ready presentation packages from the same semantic appearance workspace. Renderer/output differences are profiles/adapters rather than independent identity systems. This tranche absorbs historical MCCS-13, MCCS-14 and MCCS-15.

### MCCS-16 — Style Packs, Templates, Renderer Profiles & Visual Variant Recipes

Implement reusable style packs, appearance templates, palette/material sets, renderer/output profiles and deterministic visual-variation recipes. Historical MCCS-17 population generation is owner-absorbed: MNCS supplies NPC/crowd/herd/group identities and eligibility; PCA supplies generic procedural substrate; MCCS only produces visual variation and presentation derivatives.

### MCCS-18 — Multi-Form, Transformation, Lifecycle & Appearance-State Management

Support one entity across owner-approved Forms, lifecycle stages, disguises/presentation identities and temporary appearance states. Define inheritance, stale-derivative behavior and comparison/transition previews without replacing the owning Form/state machine.

### MCCS-19 — Appearance Interchange, Round-Trip, Cross-Renderer & Future-P3D Handoff

Implement appearance-schema import/export mapping, external-specialist round-trip, explicit loss reporting and renderer-neutral future-renderer/P3D handoff packages. ARI/PCA retain generic provenance/version/review/import-export infrastructure. This tranche absorbs historical MCCS-19 and MCCS-20 and **does not activate P3D**.

### MCCS-21 — Golden Character & Creature Capability / Semantic-Integration Proof

Prove humanoid and nonhuman Characters, ordinary animal, companion/mount/familiar cases, nonhumanoid creature, visual group variants, multi-Form/transformation and constructed/modular examples. Prove cross-output identity consistency, topology-first authoring, owner-bound vs presentation-only distinctions, equipment projection, pose/rig preview, deterministic visual variants, import-loss reporting, ARI rights/provenance, accessibility, recovery, offline/local-first blocking workflows and paid/cloud-provider-off success.

## Cross-cutting invariants

Every surviving MCCS tranche must preserve:

- definition/owner truth versus appearance draft/proposal/presentation derivative separation;
- stable owner/version references and stale-projection detection;
- no silent canonical mutation from creator controls or renderer output;
- unsupported/unresolved states rather than fabricated compatibility;
- keyboard/touch/screen-reader paths and non-color-only semantic indicators;
- undo/recovery for creator draft state without deleting canonical owner history;
- exact rights/provenance through ARI/PCA;
- deterministic receipts wherever visual generation claims determinism;
- local-first blocking workflows without a required paid/cloud provider;
- bounded controls rather than rebuilding a general-purpose Blender/ZBrush/Maya/Daz-class DCC suite.

## Clean-room boundary

Benchmark products remain capability/workflow provenance only. MCCS does not copy proprietary source, protected assets, distinctive UI expression, private protocols, sample projects, vendor-specific implementation details or branded character styles.

## Execution rule

No MCCS implementation authority exists now. When a surviving tranche is later governed-started by OPS3, one owner `Continue` carries the bounded tranche through implementation, validation, verified closeout and next-tranche selection unless an owner-only boundary or genuine external blocker is reached. Preload only the selected tranche's dependency closure and reserve closeout capacity before starting.
