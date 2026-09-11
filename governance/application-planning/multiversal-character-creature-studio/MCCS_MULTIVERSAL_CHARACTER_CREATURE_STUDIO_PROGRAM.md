# MCCS — Multiversal Character & Creature Studio

**Program ID:** MCCS  
**Program name:** Multiversal Character & Creature Studio  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after MCS-21  
**Successor:** SMB-08  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-11  
**Implementation authority:** none

## Purpose

MCCS makes Multiversal capable of creating and refining the visual presentation of essentially any governed Character, NPC, intelligent species member, animal, mount, familiar, pet, monster, creature, construct or alternate Form inside the product, while preserving the distinction between canonical entity truth and presentation.

MCCS is not a second Character, Species, Form, Creature, Inventory or Asset database. It is the creator-facing visual authoring, customization, composition, pose/expression, derivative-output and review layer over completed CAPP/PPIA appearance foundations plus PAPT/PCA production capabilities and ARI provenance/resource identity.

The governing direction is:

`canonical entity/body/equipment truth → renderer-neutral appearance projection → creator draft/override layer → renderer/output profile`

Possible outputs include portraits, dialogue busts, reference cards, tokens, paper-doll views, top-down/isometric derivatives, sprites, stance sheets, animation-ready presentation packages and future physical/3D handoffs. Pixel art remains the current governed production-content art language unless a later owner-approved art-direction change supersedes it.

## Product target

A creator should be able to visually author ordinary Multiversal people and nonhuman beings without leaving Multiversal for routine character/creature creation work. The creator must support both approachable preset/slider/component workflows and deeper bounded precision controls, without assuming that every being is humanoid.

The same semantic identity should be reusable across multiple visual outputs. Changing renderer/output format must not require rewriting Character truth or inventing new Species/Form facts.

Examples:

- a Character's equipped armor may be projected visually without MCCS changing item ownership or equipped state;
- a dragon's wings, tail, scales and posture may be authored from eligible Species/Form features without MCCS inventing anatomy;
- an intelligent Havalaea animal may use the same NPC/Character-linked appearance workflow while retaining its animal topology;
- a shapeshifter may maintain multiple owner-approved Form appearances under one entity identity;
- a scar, tattoo, hairstyle or presentation outfit may be an appearance-layer fact where the owning appearance contract allows it, while mechanical injury/equipment truth remains elsewhere;
- an unsupported anatomy, attachment or renderer feature remains visibly unsupported/unresolved instead of being silently approximated as canon.

## Placement

MCCS is a future interstitial program:

`SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10`

Rationale:

1. PCA supplies reusable production recipes, character asset/rig/garment/LOD tooling, motion/facial tooling and style-locked generation primitives.
2. MCS closes the map/cartography creator surface first and hands off to MCCS rather than directly to first-party content production.
3. MCCS then provides the entity-centric creator experience over CAPP/PPIA/PAPT/PCA before SMB-08/09 begin major library/campaign production.
4. SAA can later consume consistent Character/creature portraits, sprites and reference assets rather than inventing a separate visual-identity pipeline.
5. P3D remains a separately deferred future physicalization program; MCCS preserves a clean handoff seam but does not activate or absorb P3D.
6. MCCS does not change the current ARI family, current work pointer or implementation authority.

## Benchmark provenance and clean-room boundary

Planning benchmark set:

- Hero Forge
- TitanCraft
- Reallusion Character Creator
- VRoid Studio
- Daz Studio / Genesis workflows
- MakeHuman Community / MPFB workflows
- Adobe Mixamo
- Cascadeur
- Blender character/sculpt/rig workflows
- ZBrush character/creature sculpting workflows

The detailed benchmark is recorded in `MCCS_BENCHMARK_CAPABILITY_MATRIX.md`.

MCCS follows the existing PCM clean-room rules. It studies public product documentation, lawful ordinary-use behavior, documented interchange formats and observable workflows to identify capability requirements. It does not copy proprietary source, protected assets, distinctive UI expression, private protocols, sample projects, vendor-specific implementation details or branded character styles.

Vendor names are planning provenance only and do not become Multiversal product identity.

## Local-first / non-reimplementation boundary

MCCS owns the Multiversal-specific character/creature creator experience, topology-aware authoring, semantic appearance projection, deterministic variant recipes, review/provenance, accessibility and game-aware output workflows.

It does **not** attempt to recreate a full Blender/ZBrush/Maya/3ds Max/Daz/Character Creator-class DCC suite. Generic mesh operations, image processing, rigging helpers, retargeting, texture processing, geometry kernels, codecs and similar commodity capabilities should use lawful mature libraries or local tools behind replaceable boundaries when practical.

The in-app creator implements the bounded controls needed to finish ordinary Multiversal character/creature visual work without external software. External round-trip remains available for specialist sculpting, bespoke mesh construction, advanced cloth/hair simulation and other expert workflows.

## Upstream ownership and reuse

MCCS consumes rather than duplicates:

- **Character / NPC / Creature owners:** canonical identity, mechanics, current state and entity relationships.
- **Species / Form / PPIA-05:** body topology, eligible anatomy, current/persistent biology and form truth.
- **CAPP / PPIA-06:** renderer-neutral appearance authority, deterministic appearance compilation, fit/coverage/version/accessibility contracts and Character Appearance Creator architecture.
- **PAPT:** current pixel-art production language, Character/Creature forges, sprite assembly, equipment-fit QA, portrait/token derivatives, batch QA, regeneration and human-review workflow.
- **Inventory / Asset / equipment owners:** ownership, equipped/install state and item mechanics.
- **Mount / familiar / pet / companion owners:** relationship and gameplay truth where those systems apply.
- **ARI:** resource identity, bytes/reference state, derivative lineage, rights/use capability, tagging, query, asset picking and reusable output registration.
- **PCA:** production recipes, character asset/rig/garment/LOD tooling, motion/facial performance, style-locked generation, review/locking and local-first production primitives.
- **Animation / Scene / Combat / dialogue owners:** runtime motion, placement, action, visibility and interaction authority.
- **D29 authoring/provenance and current accessibility/design authorities:** governed publication, provenance, keyboard/touch/screen-reader and visual-accessibility requirements.
- **P3D (future/deferred):** physical-pixel and detailed physical renderer/miniature pipeline when separately activated.

MCCS may create creator drafts, presentation-only overrides, appearance proposals, renderer-specific derivatives, output packages and future-renderer handoff packages. It cannot silently promote those outputs into canonical Character, Species, Form, Creature, Inventory or relationship state.

## Core architectural doctrine

### One entity appearance workspace, multiple outputs

Portrait, token, paper-doll, sprite, stance-sheet and future-renderer handoff workflows operate over one versioned creator workspace referencing the same owner-governed entity and renderer-neutral appearance projection. They are not independent character definitions.

The workspace supports:

- stable draft/component IDs;
- owner-record/version references;
- renderer-neutral appearance references from CAPP/PPIA;
- topology/family and Form references;
- parameter/component selections and eligible manual overrides;
- surface/material/pattern and presentation layers;
- wardrobe/equipment visual projection references;
- pose/posture/expression intents;
- renderer/output profiles;
- deterministic variant seeds/recipes where claimed;
- custom authorized asset references through ARI;
- history/version/provenance;
- unsupported/unresolved extension retention.

### Appearance authoring is not canonical body/game truth

Every creator mutation has an explicit authority disposition such as:

- `owner-projected`;
- `appearance-draft`;
- `appearance-proposal`;
- `presentation-only`;
- `renderer-derived`;
- `manual-presentation-override`;
- `unsupported`;
- `unresolved`.

Sliders, generated geometry, pixels, textures, imported meshes or pose controls never silently create anatomy, Species/Form eligibility, equipment ownership, current injuries, mechanics, relationships or other canonical facts.

### Topology-first, not humanoid-first

MCCS must support extensible topology families rather than treating every nonhuman as a decorated human. Required family coverage includes at minimum humanoid/biped, quadruped, serpentine/elongate, winged/avian-style, multi-limbed, aquatic, composite, constructed/modular and extensible nonstandard families. Radial, amorphous, swarm/collective or other unusual beings must have explicit extension paths and unsupported states rather than forced humanoid mapping.

### Deterministic where practical, artistic where appropriate

Preset assembly, seeded variation and automated derivative production expose stable parameters/seeds and reproducible receipts. Freehand/manual presentation edits retain history/provenance but are not falsely presented as deterministic generation.

## Program tranches

### MCCS-01 — Creator Workspace, Document & Authority Contract

Define the versioned entity-appearance workspace over CAPP/PPIA owner references, stable draft IDs, authority dispositions, history/undo, renderer/output profiles, ARI asset references, accessibility metadata and explicit unsupported/unresolved states. Do not mint a second Character or appearance authority.

### MCCS-02 — Renderer-Neutral Appearance Projection & Draft Overlay

Expose CAPP/PPIA renderer-neutral appearance as an editable creator projection with separate draft/override state. Define stale-owner detection, refresh/rebase behavior, draft conflict reporting, manual override provenance and proposal routing without rewriting owner records.

### MCCS-03 — Topology-Family & Form Compatibility Studio

Provide topology-aware creator navigation for humanoid/biped, quadruped, serpentine, winged, multi-limbed, aquatic, composite and constructed/modular families plus extension contracts for unusual anatomies. Consume Species/Form eligibility and expose unsupported combinations rather than guessing.

### MCCS-04 — Morphology, Proportion, Silhouette & Body-Profile Authoring

Implement governed size/proportion/silhouette/body-profile controls using eligible parameters/components. Support presets, bounded sliders, symmetry/asymmetry where permitted, comparative silhouette preview and renderer coverage diagnostics without converting visual morphology into mechanical stats.

### MCCS-05 — Head, Face, Sensory Feature & Expression Anatomy Authoring

Implement topology-aware cranial/head modules, eyes/sensory organs, ears, mouths/beaks/mandibles, horns/antlers/tusks/crests and related eligible facial features. Human-face assumptions must not be required for creature families.

### MCCS-06 — Hair, Fur, Feather, Scale, Shell & Surface-Covering Studio

Implement reusable covering systems for hair/facial hair, fur, feathers, scales, shell/plates, skin-like surfaces and extensible coverings. Support length/density/direction/style/pattern parameters where the renderer and owner contracts allow them, with explicit renderer limitations.

### MCCS-07 — Color, Material, Pattern, Marking & Surface-Layer Studio

Implement palette/material/surface roles, markings, stripes/spots, tattoos, scars where appearance-authorized, makeup/paint, emissive/glow presentation and layered texture/pattern editing. Required state cannot be communicated by color alone; all generated/imported textures retain ARI provenance.

### MCCS-08 — Appendage & Modular Anatomy Authoring

Implement eligible tails, wings, fins, extra limbs, tentacles, horns, antennae, modular construct parts and other topology-specific appendages with anchor/fit validation. Component assembly must respect Species/Form topology and cannot create unsupported anatomy silently.

### MCCS-09 — Wardrobe, Armor, Equipment Fit & Outfit Authoring

Project eligible worn/carried equipment and presentation clothing through CAPP/PAPT fit/layer/occlusion rules. Support appearance-only outfits where permitted, outfit presets, layer ordering, masks, fit diagnostics and alternate display states while Inventory/Asset owners retain ownership/equipped truth.

### MCCS-10 — Accessories, Props, Mount, Familiar & Companion Composition

Provide composition workflows for presentation accessories/props and linked mounts, familiars, pets or companions. Linked beings retain separate canonical identities unless the owning domain explicitly defines a composite entity. Composition never implies ownership or relationship state.

### MCCS-11 — Pose, Posture, Gesture & Expression Authoring

Provide topology-aware neutral, social, combat-presentation and reference poses; facial/expression intent where supported; mirrored/variant poses; ground/contact guides; and user-adjustable controls. Pose/expression state is presentation unless an owning runtime explicitly projects current state.

### MCCS-12 — Rig, Anchor, IK & Retarget Preview Integration

Integrate existing/future PAPT/PCA/local rigging and retarget helpers for preview and export preparation. Support topology-specific skeleton/anchor profiles, equipment anchors, IK/contact preview and explicit incompatibility reporting. MCCS does not become animation-runtime or canonical anatomy authority.

### MCCS-13 — Portrait, Dialogue Bust & Reference-Card Renderer

Produce deterministic/reviewable portraits, busts, profile/reference cards, transparent cutouts and approved framing/crop variants from the same appearance workspace, with style/output profiles, accessibility descriptions, stale-derivative invalidation and ARI registration.

### MCCS-14 — Token, Paper-Doll, Top-Down & Isometric Derivative Renderer

Produce tactical tokens, paper-doll/inventory views, top-down/isometric presentation derivatives, thumbnails and other game-facing identity views using the same semantic appearance source. Output geometry/style remains presentation and must not change map/scene/collision truth.

### MCCS-15 — Sprite, Stance & Animation-Sheet Composition

Consume PAPT sprite/animation assembly and PCA motion primitives to produce topology-aware idle/walk/presentation stance sheets and animation-ready sprite packages. Animation availability/coverage is reported explicitly; absence of a visual loop cannot invent or remove an action mechanic.

### MCCS-16 — Style Packs, Templates & Renderer Profiles

Provide reusable visual style packs, creator presets, outfit/look templates, palette/material sets and renderer/output profiles while preserving identity-defining appearance semantics. Current pixel-art authority remains default product language; later owner-approved renderers can be added without rewriting Character truth.

### MCCS-17 — NPC, Crowd, Herd & Creature Variant Generator

Create governed seeded variation recipes for NPC populations, crowds, herds, packs and creature families using owner-supplied eligibility/ranges. Preserve stable seed/receipt, exclusions, rarity/weight inputs and independent review; visual population diversity does not create demographic/world truth.

### MCCS-18 — Multi-Form, Transformation, Lifecycle & Appearance-State Management

Support one entity with multiple owner-approved Forms, lifecycle stages, disguises/presentation identities, temporary appearance states and transformations. Define shared-vs-form-specific appearance inheritance, stale derivative behavior and comparison/transition previews without changing the owning Form/state machine.

### MCCS-19 — Structured Import/Export, Round-Trip, Review & Provenance

Support authorized custom components/textures/reference assets, structured Multiversal appearance packages, documented model/image interchange where appropriate, external-specialist round-trip, review annotations, version comparison, approval/publish states and explicit import-loss reporting. Unsupported semantics are preserved/reported rather than silently flattened.

### MCCS-20 — P3D / Future Renderer Handoff & Cross-Renderer Contract

Produce a governed renderer-neutral handoff package for future P3D and later approved renderers: identity, topology family, eligible appearance parameters/components, equipment presentation, pose intent, source/provenance and unsupported coverage. This tranche does not activate P3D, create printable meshes or make 3D fields required Character truth.

### MCCS-21 — Golden Character & Creature Capability / Semantic-Integration Proof

Create an original Multiversal golden suite proving at least:

1. humanoid player Character;
2. nonhuman intelligent species member;
3. ordinary animal;
4. mount or companion-capable animal;
5. familiar/pet example;
6. nonhumanoid monster/creature;
7. NPC/crowd or herd variant family;
8. multi-Form/transformation example;
9. constructed/modular or otherwise non-organic being.

The proof must demonstrate preset-to-manual-edit continuity, topology-aware controls, wardrobe/equipment projection where applicable, pose/expression authoring, portrait/token/sprite or equivalent cross-output identity consistency, custom authorized assets, style/profile switching, deterministic variant receipts, rights/provenance, accessibility alternatives, import-loss reporting, offline/local-first blocking workflows and at least one explicit presentation-only vs owner-bound comparison.

## Cross-cutting requirements

Every MCCS tranche must preserve:

- undo/redo and recovery appropriate to its mutations;
- keyboard/touch alternatives and non-pointer-only workflows;
- structured/list/screen-reader alternatives for essential appearance state and selections;
- high-contrast/non-color-only semantic indicators;
- responsive review on smaller screens, with desktop/tablet as primary deep-authoring targets;
- offline/local-first operation for blocking core authoring where practical;
- exact rights/provenance through ARI;
- deterministic receipts wherever generation claims determinism;
- unsupported/unresolved states instead of silent approximation or invention;
- performance budgets for large component libraries and rapid preview regeneration;
- species/form/world-specific styles without allowing them to break core usability;
- explicit owner-version references so stale projections can be detected and refreshed;
- no sexualized or adult-only asset requirement for core creator completion.

## Explicit non-goals

MCCS does not:

- replace Character, NPC, Creature, Species, Form, Inventory, Asset, mount/familiar/pet or other canonical owners;
- make pixels, sliders, meshes, textures, poses or generated variants authoritative gameplay/body truth;
- replace CAPP/PPIA renderer-neutral appearance authority or PAPT's pixel-production pipeline;
- recreate a general Blender/ZBrush/Maya/3ds Max/Daz/Character Creator-class DCC suite;
- activate P3D or require detailed/physical 3D output for MCCS completion;
- copy proprietary vendor assets, character bases, styles, UI layouts or implementation;
- require a paid/cloud character service for blocking workflows;
- make external animation/rigging providers authoritative;
- authorize provider credentials, paid spend, public release or tester distribution.

## Family execution rule

When MCCS is eventually selected, it receives its own sealed family preflight. Every execution unit must target 24 active minutes or less under a healthy governed environment with protected closeout reserve. Any unit that cannot credibly fit is split before governed start.

No MCCS implementation authority exists now.

## Completion standard

MCCS is complete only when all 21 tranches are `completed_verified`, the golden suite proves broad topology coverage and cross-output identity consistency, blocking character/creature creation works without paid/cloud character providers, PAPT/CAPP/PCA/ARI authority boundaries remain intact, unsupported anatomy/renderer coverage fails visibly rather than being invented, accessibility alternatives exist for essential operations, rights/provenance remain exact, and SMB-08 can consume the studio without inventing a parallel character/creature visual-production system.
