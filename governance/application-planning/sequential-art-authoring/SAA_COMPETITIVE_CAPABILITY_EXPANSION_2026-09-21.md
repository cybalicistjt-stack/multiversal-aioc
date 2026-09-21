# SAA Competitive Capability Expansion — 2026-09-21

**Status:** OWNER-REQUESTED CURRENT PLANNING AMENDMENT  
**Scope:** SAA feature-family completeness only  
**Implementation authority created:** none  
**Current execution preserved:** SAA-02 remains selected_not_started  
**Clean-room rule:** adopt product capabilities and user outcomes only. Do not copy proprietary code, protected expression, assets, private file formats, undocumented protocols or vendor-specific implementation details.

## Products reviewed

Official product material was reviewed for:

- Canva Comic Strip Maker — https://www.canva.com/create/comic-strips/
- Canva AI Comic Generator — https://www.canva.com/ai-comic-generator/
- Pixton — https://www.pixton.com/ and https://www.pixton.com/learner-variability
- Pixton character consistency/editor surface — https://www.pixton.com/canva-app
- Pixton product updates — https://www.pixton.com/change-log
- Book Creator comics — https://bookcreator.com/features/comics/
- Book Creator feature set — https://bookcreator.com/pricing/
- Book Creator accessibility/updates — https://bookcreator.com/accessibility/ and https://bookcreator.com/features/whats-new-in-book-creator/
- Clip Studio Paint comics/manga/webtoons — https://www.clipstudio.net/en/comics-manga/
- Clip Studio paneling/text/export/3D tools — https://www.clipstudio.net/en/comics-manga/tool/paneling/ ; https://www.clipstudio.net/en/comics-manga/tool/text-balloons/ ; https://www.clipstudio.net/en/comics-manga/tool/exporting-printing/ ; https://www.clipstudio.net/en/comics-manga/tool/3d/
- MediBang Paint comic/drawing features — https://medibangpaint.com/en/pc/about/
- MediBang cloud/group-project surface — https://medibangpaint.com/en/cloud/ and https://medibangpaint.com/en/medibangpaint/

## Capability comparison and SAA disposition

| Product-observed capability class | Existing SAA coverage | Amendment |
| --- | --- | --- |
| Ready-made grids/templates; drag/drop frames; custom frame layouts | SAA-02/03 | SAA-02 explicitly gains saveable custom templates, deterministic divider/frame-split grammar and template-wide gutter/border edits. |
| Searchable illustration/material libraries; uploaded/user art | SAA-04/07/08 + ARI | Preserve ARI as the one resource/material library; expand material types through SAA-24 rather than create a comic-only store. |
| Reusable characters, expressions, poses and identity consistency | SAA-05/06/12 | Require identity-consistent actor reuse across pose/expression/style projections; no private Pixton-like avatar truth replaces Character/CAPP/PAPT. |
| Speech/thought/shout/whisper balloons; rich fonts; batch story text | SAA-09/10 | Add SAA-22 for professional lettering, balloon styling, script-wide editing/search/replace and speech-to-text input. |
| Real-time collaboration, group projects, comments/review and multi-device continuation | Partial versioning only in SAA-13 | Add SAA-21. |
| Comic page management / story-at-a-glance | SAA-01/11/13 | Keep core page identity/order; SAA-21 adds collaborative/project continuation and SAA-26 adds scroll preview. |
| Brushes, raster/vector drawing, selections, masks, layer folders/comps, filters | Not explicit | Add SAA-23, consuming PAPT/studio primitives where they already exist. |
| Tones/halftones, backgrounds/materials, speed/action lines, rulers/perspective/snap guides | Partial props/effects only | Add SAA-24 with ARI-owned materials and governed guide/effect semantics. |
| 3D figures/props/backgrounds, pose/camera reference, photo/3D line extraction | Not explicit | Add SAA-25. |
| Webtoon long-scroll editing and smartphone/responsive preview | Not explicit | Add SAA-26. |
| Print CMYK, trim/bleed, binding/spread/3D book preview | Partial bleed/export only | Add SAA-27. |
| Audio/video/interactive media, hyperlinks, read-aloud, TTS/STT, translation, captions/transcripts | Audio + accessibility only | Add SAA-28 while retaining AAI/media/source authority and provider-off baseline. |
| PSD/layer-aware interchange, PDF/e-book style outputs and roundtrip | Packaging/static export only | Add SAA-29; support only lawful documented formats/capabilities. |
| Remix/reuse of projects/templates | SAA-12/18 | Make remix/fork lineage explicit in SAA-18/29 and preserve provenance. |
| Optional AI image/layout/character assistance | SAA-19 | Preserve proposal-only authority, identity/provenance visibility, provider-off blocking workflows and no silent edits. |
| Full professional + collaborative end-to-end proof | SAA-20 was core proof | SAA-20 becomes core milestone; SAA-30 becomes terminal family proof. |

## Tranche architecture

The original SAA-01..20 core path is preserved. SAA-20 is renamed **Core Integrated Desktop/Mobile Golden Comic Proof** and remains useful as an intermediate quality barrier.

New bounded tranches:

- **SAA-21** Real-Time Collaboration, Review & Multi-Device Sync
- **SAA-22** Advanced Lettering, Balloon Styling & Story Text Editor
- **SAA-23** Pro Raster/Vector Drawing, Masks & Layer Interop
- **SAA-24** Comic Finishing Materials, Tones, Effect Lines, Rulers & Perspective
- **SAA-25** 3D Reference, Pose/Scene Staging & Line Extraction
- **SAA-26** Webtoon & Responsive Scroll Authoring Preview
- **SAA-27** Print Prepress, CMYK & Bound-Book Preview
- **SAA-28** Multimedia/Interactive Comic, Localization & Accessible Read-Aloud
- **SAA-29** Industry Interchange & Layer-Aware Roundtrip
- **SAA-30** Expanded Professional/Collaborative Golden Comic Proof

The 24-minute tranche rule remains binding. If any of these cannot credibly fit before governed start, split that tranche rather than weakening acceptance or silently overloading an earlier tranche.

## Downstream gate

Current roadmap authority is amended so SAA terminal proof is **SAA-30**, not SAA-20. SMB10B may not governed-start on the basis of the old core proof alone.

## Current execution preservation

This amendment performs planning only. It does not governed-start SAA-02. SAA-02 remains selected_not_started and gains only the additional clean-room template/frame acceptance above.
