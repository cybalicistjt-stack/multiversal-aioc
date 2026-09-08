# SAA — Sequential Art Authoring

**Program ID:** SAA  
**Program name:** Sequential Art Authoring  
**Version:** 0.1.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL; NOT STARTED  
**Activation:** after SMB-09  
**Successor:** SMB-10  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-07

## Purpose

SAA gives Multiversal users a low-friction, Gacha-like comic/sequential-art creator that composes resources already available to them in Multiversal: imported/user-owned assets, native first-party assets, MAI map/tile resources, CAPP/PAPT character and creature art, props/equipment/icons/effects and optional AAI audio for digital presentation.

The governing rule is that SAA **references ARI resources rather than creating private duplicate copies by default**. A comic panel is a composition of governed resource references plus layout/text/presentation state. New renders/exports may be registered back through ARI as provenance-linked derivatives.

SAA does not replace Character appearance truth, Scene truth, MAI geometry/map authority, PAPT/CAPP renderers, AAI audio semantics, Story/CSW narrative authority, rights/provenance controls, publishing authority or SMB-11 sharing/package authority.

## Product intent

- A user may turn an existing Multiversal Character into a reusable comic actor.
- Pixel-style generated Character/creature/item/environment/tile assets are first-class authoring inputs when available.
- Imported maps/tilesets may be used directly as panel backgrounds or as composition material where their rights permit.
- Existing Scene compositions may be projected to a comic panel without making the comic the authoritative Scene state.
- Reusable cast placements, pose/expression sets, scene/shot presets and panel templates provide the fast dress-up/staging workflow associated with Gacha-style comic creation.
- Static comic export and digital comic presentation are separate capabilities. Digital projects may optionally bind AAI cues; static outputs simply omit audio.
- Rights filtering occurs before an asset is offered for a requested transform/export/share operation.

## Tranche sizing rule

Every SAA implementation tranche is designed for a **24-minute-or-less bounded execution target under a healthy governed environment**, including its focused construction/validation package. If the actual acceptance surface cannot credibly fit that bound, it must be split before governed start rather than expanded. Final repository/runner latency remains an external condition and does not justify weakening acceptance.

## Tranches

### SAA-01 — Comic Project, Page, Panel & Layer Schema
Define stable project/page/panel/layer identity, ARI resource references, transform state, text elements and output metadata without embedding source assets by default.

### SAA-02 — Panel Templates & Page Layout Grammar
Provide common panel grids, gutters, margins, bleed/safe-area rules and freeform panel layouts with deterministic serialization.

### SAA-03 — Layer Composition Canvas
Implement position, scale, crop, rotate, flip, z-order, opacity, lock/hide and clipping behavior with keyboard/non-drag alternatives.

### SAA-04 — ARI Asset Palette & Capability Filtering
Expose one searchable asset palette over ARI with type, collection, rights and requested-operation filters.

### SAA-05 — Character Actor Projection
Create an SAA actor reference over Character/CAPP/PAPT appearance outputs. Actor presentation may change pose/expression/view without mutating Character truth.

### SAA-06 — Pose, Expression, View & Frame Selector
Select governed pose/expression/view/animation-frame variants where available, preserving explicit unsupported states rather than fabricating coverage.

### SAA-07 — Maps, Tilesets & Scene Background Projection
Use MAI/ARI maps, tile families, Scene renders or bounded map crops as panel backgrounds while preserving map/Scene ownership boundaries.

### SAA-08 — Props, Equipment, Effects & Foreground Composition
Compose ARI/PAPT props, equipment, items, effects, overlays and foreground elements with attachment hints that remain presentation-only.

### SAA-09 — Speech, Thought, Caption & Comic SFX Text
Implement dialogue balloons, thought balloons, captions, narration boxes and stylized text sound effects with readable text retained as actual text state.

### SAA-10 — Bubble Tails, Actor Anchoring & Readability Assistance
Bind optional bubble tails to actors/anchors and provide collision/readability warnings/suggestions without silently rewriting authored dialogue/layout.

### SAA-11 — Storyboard, Script & Panel Sequence Binding
Represent page/panel sequence, scene/beat notes, cast presence and dialogue/script references without replacing CSW/Adventure/Story identity.

### SAA-12 — Reusable Cast, Shot, Scene & Expression Presets
Provide quick reusable actor placements, pose/expression sets, shot/framing presets and background/scene presets for rapid Gacha-like authoring.

### SAA-13 — Reversible Edit History & Project Versioning
Provide deterministic commands, undo/redo, autosave/recovery boundaries and project-version lineage.

### SAA-14 — Composition-to-ARI Derivative Registration
Allow a panel/pose/composite render to become a new ARI derivative with exact source references, renderer/compositor version and rights lineage.

### SAA-15 — Static Image & Multipage Export
Export panel/page images and multipage comic packages at governed output profiles, filtering prohibited transforms/redistribution before render/export.

### SAA-16 — Optional Digital-Comic Audio Cue Lane
Bind AAI resources/cues to pages/panels/transitions for digital presentation only; audio remains nonblocking and does not become embedded/exportable unless independent rights allow it.

### SAA-17 — Reading Order, Alt Description & Text Projection
Provide explicit reading order, transcript/text-only projection, alt descriptions and accessibility-equivalent control/state.

### SAA-18 — Comic Project Packaging Contract
Define dependency manifests, resource references/embedded-permitted derivatives, version compatibility and import/export handoff for later SMB-11 controlled sharing.

### SAA-19 — Advisory Authoring Assistance
Permit optional AI or deterministic assistance for shot/layout/dialogue alternatives and asset discovery through existing proposal-only authority. Suggestions never silently alter authored work or hidden/canonical state.

### SAA-20 — Integrated Desktop/Mobile Golden Comic Proof
Prove a complete comic using a mix of imported/user-owned, native and generated assets; Character actors; map/tile background; dialogue; derivative registration; rights filtering; accessibility projection; save/recovery and static export.

## Dependencies and relationships

- **ARI-22** must be complete before SAA activation so the authoring tool consumes the universal resource library rather than creating another one.
- **SMB-09** supplies a mature first-party Campaign/content baseline and precedes SAA in the critical path.
- **SMB-10** follows SAA and owns final production-grade Player/GM/Creator UX integration around the already-working SAA workflow.
- **SMB-11** owns controlled creator interchange/sharing and consumes SAA-18 packaging rather than SAA inventing public sharing/marketplace authority.
- **PAPT** remains a parallel studio/tooling producer; any completed PAPT outputs enter SAA through ARI. SAA base implementation does not require PAPT to be the only asset source.
- **CAPP** remains Character appearance authority. SAA actor choices are presentation projections.
- **MAI/Scene** remain map/spatial/runtime Scene owners. SAA panel backgrounds and scene projections are derivatives/presentation.
- **AAI** remains audio semantics/capability authority. SAA-16 is an optional consumer.

## Non-activation boundary

Planning SAA does not authorize application implementation, public/community publishing, marketplace features, provider activation, unrestricted third-party asset transformation/redistribution, live AI spending, tester distribution or release/deployment. Selection requires a later governed start after ARI-22 and SMB-09.

## Completion standard

SAA completes only when SAA-01..20 are `completed_verified`, users can author and recover an end-to-end comic project without developer tooling, resource/provenance identity remains intact, third-party rights are respected at use/export boundaries, accessibility-equivalent text/reading state exists, and SMB-10/11 can consume the finished authoring/package contracts instead of rebuilding them.