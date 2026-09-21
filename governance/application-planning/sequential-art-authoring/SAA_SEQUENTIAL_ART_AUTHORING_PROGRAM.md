# SAA — Sequential Art Authoring

**Program ID:** SAA  
**Program name:** Sequential Art Authoring  
**Version:** 0.2.0  
**Status:** OWNER-APPROVED — IN PROGRESS; SAA-01 COMPLETED_VERIFIED; SAA-02 SELECTED_NOT_STARTED  
**Activation:** after SMB10A under current normalized roadmap authority  
**Successor:** SMB10B after SAA-30  
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
- Reusable cast placements, identity-consistent pose/expression sets, scene/shot/focus presets and saveable panel templates provide the fast dress-up/staging workflow associated with Gacha-style comic creation.
- Static comic export, print-oriented output, responsive webtoon output and digital multimedia presentation are separate capabilities. Digital projects may optionally bind AAI/media cues; static outputs simply omit multimedia.
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

### SAA-20 — Core Integrated Desktop/Mobile Golden Comic Proof
Prove the original core SAA authoring path end to end across desktop/mobile before the professional/collaborative extension: imported/user-owned, native and generated assets; Character actors; map/tile background; dialogue; derivative registration; rights filtering; accessibility projection; save/recovery and static export. This is a core milestone, not terminal SAA closure.


### SAA-21 — Real-Time Collaboration, Review & Multi-Device Sync
Provide authorized coauthoring over the same comic project with role-aware edit permissions, page/panel/layer presence, review comments, explicit conflict handling, multi-device continuation and offline/reconnect recovery. Collaboration may coordinate edits but never creates a second canonical asset/provenance or source-domain ledger.

### SAA-22 — Advanced Lettering, Balloon Styling & Story Text Editor
Extend the basic SAA-09/10 text contract with speech/thought/shout/whisper and custom balloon styles, tail/border/fill controls, font fallback, kerning/spacing/alignment, batch story-dialogue editing, search/replace and speech-to-text authoring input while preserving text as editable semantic state.

### SAA-23 — Pro Raster/Vector Drawing, Masks & Layer Interop
Provide or consume governed drawing-layer capabilities for raster and editable vector strokes, pressure-aware brushes, selections, masks, clipping, layer folders/comps and non-destructive filters. Prefer PAPT/other existing studio owners where they already own the primitive; SAA owns comic-project composition semantics, not a duplicate renderer.

### SAA-24 — Comic Finishing Materials, Tones, Effect Lines, Rulers & Perspective
Expose ARI-governed comic materials such as brushes, fonts, tones/halftones, pattern/background materials and decoration stamps plus speed/action lines, perspective/symmetry/radial/snap guides and reusable effect presets. Material bytes/provenance remain ARI-owned.

### SAA-25 — 3D Reference, Pose/Scene Staging & Line Extraction
Allow governed 3D/Scene/Character reference staging for camera, pose, hand/head/body reference, props and backgrounds, plus non-authoritative image/3D-to-line or tone proposals where existing renderers support them. Reference staging never becomes Character/Scene truth.

### SAA-26 — Webtoon & Responsive Scroll Authoring Preview
Support long-scroll/webtoon project grammar, insert/remove vertical space, responsive device/smartphone preview, scroll reading-order proof and governed split/single-file export profiles without weakening ordinary page-comic identity.

### SAA-27 — Print Prepress, CMYK & Bound-Book Preview
Add print-specific output profiles: trim/bleed/safe marks, page numbering/spreads, color-space/CMYK preview or conversion through approved renderers, printer-facing checks and a local bound-book/spread preview. This does not authorize printing purchases or commercial publication.

### SAA-28 — Multimedia/Interactive Comic, Localization & Accessible Read-Aloud
Extend digital comics with optional AAI narration/cues, permitted video/animated media, hyperlinks/hotspots, captions/transcripts, speech-to-text/text-to-speech/read-aloud, translation/localization projections and accessibility metadata. Static export remains valid when multimedia is absent, and no network/provider is mandatory.

### SAA-29 — Industry Interchange & Layer-Aware Roundtrip
Add capability-filtered import/export/roundtrip for appropriate open/standard or independently supported formats, including layer-aware raster interchange, PDF/e-book style outputs where applicable and preservation of editable text/layer semantics when the format supports them. Private/proprietary formats require independently lawful support; no undocumented reverse-engineered dependency is assumed.

### SAA-30 — Expanded Professional/Collaborative Golden Comic Proof
Prove the full SAA-01..29 family in one rights-safe, provider-off-capable end-to-end project spanning page and webtoon presentation, reusable templates, actors/poses, professional lettering, materials/finishing, drawing-layer interop, collaboration/review, multi-device recovery, multimedia/accessibility/localization, print preview, industry interchange and deterministic recovery. SAA-30 is the terminal SAA golden gate consumed by SMB10B.

## Competitive capability expansion

SAA deliberately includes the feature classes demonstrated by Canva Comic Strip Maker, Pixton, Book Creator, Clip Studio Paint and MediBang Paint where they are relevant to Multiversal sequential-art creation. The binding capability map is maintained in `SAA_COMPETITIVE_CAPABILITY_EXPANSION_2026-09-21.md`. The comparison is clean-room and feature-level only: it does not authorize copying proprietary code, assets, protected expression, undocumented protocols or private save formats.

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

SAA completes only when SAA-01..30 are `completed_verified`, users can author and recover an end-to-end comic project without developer tooling, resource/provenance identity remains intact, third-party rights are respected at use/export boundaries, accessibility-equivalent text/reading state exists, and SMB10B/SMB-11 can consume the finished authoring/package contracts instead of rebuilding them.