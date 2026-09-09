# PCM — Proprietary Capability Mining Catalog

**Status:** OWNER-APPROVED PARALLEL EVALUATION  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-09-09  
**Implementation authority:** none  
**Rights/control:** `PCM_CLEAN_ROOM_AND_RIGHTS_RULES.md`

## Purpose

Survey the small fraction of proprietary/commercial products whose proven workflows could materially improve Multiversal or reduce recurring development/content/AI-service cost. The goal is not feature cloning. The goal is to identify independent Multiversal requirements, learn from public product behavior/documentation, and decide whether to use, temporarily license, study, or build a narrow native equivalent.

Products below are the initial high-leverage set. Their brands, proprietary content, protected expression, source code, private protocols and assets are not Multiversal implementation inputs.

## Priority catalog

### PCM-01 — articy:draft X — `BUILD_MULTIVERSAL_NATIVE`

**Why it matters:** mature narrative-authoring workflow combining flow editing, templates, a game-object database, scripting, localization/VO management, validation/checkup tooling, customizable exports and engine integration.

**Native capability target:** one governed narrative/content workbench over existing Multiversal Story/CSW/CNI truth: visual flow editing, typed narrative objects, conditions/context queries, reference/dependency inspection, localization/VO line state and deterministic generic export. Do not create a second Story authority.

**Likely owners:** CNI, CSW, WCI, LNG/localization, AAI for VO projections.

### PCM-02 — Foundry Virtual Tabletop — `STUDY_PATTERNS` + bounded `BUILD_MULTIVERSAL_NATIVE`

**Why it matters:** mature package/module ecosystem, World/scene/document organization, role and document-level permissions, compendiums, extensible runtime and map/vision workflows.

**Native capability target:** strengthen Multiversal package manifests, per-object visibility/permission projection, compendium/resource browsing, module compatibility/diagnostics and scene-runtime ergonomics where existing owners need them. Do not reproduce Foundry APIs or branded systems.

**Likely owners:** CNI, WCI, MAI, ARI, Campaign/Scene, permissions.

### PCM-03 — Dungeon Alchemist — `BUILD_MULTIVERSAL_NATIVE`

**Why it matters:** converts high-level map intent into an immediately editable result and exports useful structural data such as walls/lighting to VTTs.

**Native capability target:** semantic/procedural map-assistance that converts room/environment intent into editable MAI/SSA geometry plus doors, blockers, lighting anchors, furnishing suggestions and deterministic export metadata. Generated output must remain editable and provenance-linked.

**Likely owners:** MAI, SSA, ARI, PAPT/CAPP, future Creator UX.

### PCM-04 — RPG Maker MZ — `BUILD_MULTIVERSAL_NATIVE`

**Why it matters:** decades-refined no-code event authoring: database-backed content, switches/variables, conditional branches, reusable common events, event commands, playtest controls, plugins and searchable references.

**Native capability target:** a safe, typed, no-code event/action authoring grammar over Multiversal Actions/Events and CNI predicates; reusable event templates/common flows; deterministic playtest overrides; global reference search; plugin/extension commands only through governed capability contracts.

**Likely owners:** CNI, MSS, WCI, Adventure/Scene, developer/creator tooling.

### PCM-05 — D&D Beyond — `STUDY_PATTERNS`

**Why it matters:** strong integration of builder → live character sheet → rules/content references → campaign → maps/encounters → shared rolls/game log. One user object projects consistently into multiple play surfaces.

**Native capability target:** preserve Multiversal's existing domain ownership while making projections feel seamless: Character state should flow to map/encounter/session surfaces without duplicate ledgers; context help should expose the exact applicable rule/content; GM and player views should remain synchronized and role-safe.

**Boundary:** no D&D rules text, content, artwork, branded UX or licensed database material.

### PCM-06 — World Anvil + LegendKeeper — `STUDY_PATTERNS`

**Why they matter:** rich interlinked world knowledge, templates, atlas/map links, timelines/calendars, secrets/permissions, search and collaboration. LegendKeeper additionally demonstrates offline editing/sync and linked whiteboards/boards.

**Native capability target:** improve Multiversal world/campaign knowledge traversal, linked entities, player-secret projection, timeline/calendar navigation, map-linked lore and lightweight boards without creating a separate wiki truth store.

**Likely owners:** World, WCI, KFR, ODL, MAI, Campaign, CNI.

### PCM-07 — Arkenforge Master's Toolkit — `BUILD_MULTIVERSAL_NATIVE`

**Why it matters:** unusually strong local/offline tabletop workflow: animated maps, fog/lighting, separate GM/player screens, map-linked audio/soundscapes, broad media import and touchscreen physical-mini interaction.

**Native capability target:** local-first in-person session mode combining role-safe second-screen presentation, MAI fog/vision, AAI map-linked sound emitters/soundscapes, hot-seat/table display and optional physical-token/touch integration.

**Likely owners:** MAI, AAI, WCI, Campaign/Session, future physical-table integration.

### PCM-08 — TaleSpire — `STUDY_PATTERNS`

**Why it matters:** building and playing share the same persistent synchronized space; GMs can modify scenes live; supports reusable scene pieces, multiple GMs, measurement, turn/cinematic modes and soundscape presentation.

**Native capability target:** study live edit/play transitions, reversible scene edits, reusable scene chunks, collaborative GM staging and presentation/cinematic controls. 3D implementation remains subordinate to renderer-neutral Scene/World truth.

**Likely owners:** Scene, MAI, WCI, P3D, multiplayer.

### PCM-09 — Hero Forge — `BUILD_MULTIVERSAL_NATIVE` through P3D/CAPP

**Why it matters:** demonstrates an extremely effective parametric character/miniature assembly workflow, including modular parts, positioning/scaling, kitbashing, posing, color/material choices and printability constraints.

**Native capability target:** renderer-neutral composable character/creature part system with slots/anchors, morph parameters, equipment/accessory placement, pose projection, topology eligibility and printability validation. Existing Character/species/form/equipment truth remains authoritative.

**Likely owners:** P3D, CAPP/PAPT, Character, ARI.

### PCM-10 — Reallusion Character Creator / AccuRIG — `STUDY_PATTERNS` + bounded `BUILD_MULTIVERSAL_NATIVE`

**Why it matters:** generalized morphing, automatic humanoid rigging, skin weighting, facial rigging, clothing/accessory workflows, characterization of imported actors and optimization for different runtime targets.

**Native capability target:** automated renderer pipeline from governed appearance snapshot to rig/topology family, anchors, skinning validation, facial/expression channels and LOD/runtime variants. Prefer existing open components where adequate rather than recreating a general DCC suite.

**Likely owners:** P3D, CAPP, PAPT, Character/creature rendering.

### PCM-11 — Adobe Substance 3D Designer/Painter — `BUILD_MULTIVERSAL_NATIVE` subset

**Why it matters:** node-based non-destructive parametric material authoring, integrated baking and reusable smart material/mask workflows dramatically reduce repeated texture labor.

**Native capability target:** a bounded procedural material/texture derivative pipeline using open standards/components where possible: parameterized material graphs, reusable masks/presets, mesh-map baking, deterministic derivative registration and batch variant generation. Do not attempt to reproduce the entire Substance editor.

**Likely owners:** PAPT/CAPP, P3D, ARI derivative lineage.

### PCM-12 — Live2D Cubism / comparable parametric 2D puppetry — `BUILD_MULTIVERSAL_NATIVE` subset

**Why it matters:** parameter-driven deformation, expressions, motion, physics and runtime playback make a relatively small authored character asset set produce many reusable presentations.

**Native capability target:** optional parameterized 2D actor representation for portraits/comics/dialogue/animated presentation: standardized expression/pose parameters, simple secondary-motion physics and deterministic state projection. Use original/open implementation components; do not copy Cubism file formats or editor behavior.

**Likely owners:** PAPT/CAPP, SAA, Character presentation, AAI lip/voice projection if later approved.

### PCM-13 — BrowserStack/Percy — `BUILD_MULTIVERSAL_NATIVE` locally, `USE_AS_IS` only for unavailable real-device coverage

**Why it matters:** automated cross-browser/platform visual rendering, responsive diffs, screenshot baselines and review workflows catch expensive UI regressions without manual inspection.

**Native capability target:** self-hosted Playwright-based browser matrix, deterministic screenshot capture, responsive breakpoints, baseline/diff artifacts, dynamic-content stabilization, accessibility coupling and governed review receipts. Use external device farms only for devices/OS combinations we cannot realistically own.

**Likely owners:** developer toolbelt, Validation Core, SMB-13/15/16, BRP.

### PCM-14 — Sentry SaaS product workflow — `BUILD_MULTIVERSAL_NATIVE` subset

**Why it matters:** correlates errors with breadcrumbs, traces, releases and session replay so developers can reproduce what actually happened instead of paying AI to infer a failure from sparse logs.

**Native capability target:** privacy-minimized diagnostic bundles with error fingerprinting, structured breadcrumbs, action/event IDs, local/session replay where appropriate, release/build identity, traces and automatic redaction. Prefer OpenTelemetry and existing local tooling. AI summaries remain optional downstream interpretation, not required evidence.

**Likely owners:** MIB diagnostics, developer toolbelt, SMB-13/15, BRP operations.

### PCM-15 — ElevenLabs audio production stack — `LICENSE_TEMPORARILY` + `BUILD_MULTIVERSAL_NATIVE` core

**Why it matters:** integrated TTS, STT, voice design, multi-speaker expressive speech, dubbing/localization and low-latency voice workflows can make game/content audio production dramatically faster but carry recurring credit cost.

**Native capability target:** local fictional-character voice registry, local TTS/STT, pronunciation/line manifests, batch generation, consistent speaker IDs, timing/alignment, multilingual pipeline and optional local dubbing experiments using consented/original voices only. Preserve an external-provider adapter for exceptional quality requirements rather than assuming local models immediately match frontier hosted quality.

**Likely owners:** AAI, localization, SAA/digital presentation, content production.

## Initial priority bands

### Band 1 — likely to save major development/AI-credit cost

PCM-01 articy:draft X patterns; PCM-03 Dungeon Alchemist; PCM-04 RPG Maker event authoring; PCM-07 Arkenforge local session integration; PCM-09 Hero Forge/P3D assembly; PCM-13 BrowserStack/Percy local QA; PCM-14 Sentry-style diagnostic evidence; PCM-15 ElevenLabs/local audio pipeline.

### Band 2 — major product-quality references; implement only owned subsets

PCM-02 Foundry VTT; PCM-05 D&D Beyond; PCM-06 World Anvil/LegendKeeper; PCM-08 TaleSpire; PCM-10 Character Creator; PCM-11 Substance; PCM-12 parametric 2D puppetry.

## Evaluation rule

For each catalog item, a later PCM evaluation may produce one or more Multiversal capability candidates. A candidate becomes implementation work only after overlap analysis against current canonical owners, a clean-room capability specification, cost/benefit estimate, open-source alternative review, and an explicit roadmap placement/owner decision. No catalog entry itself creates implementation authority.

## Public capability sources checked 2026-09-09

- articy:draft X public feature list/documentation.
- Foundry VTT public documentation, including users/permissions.
- Dungeon Alchemist public Foundry/Roll20 export documentation.
- RPG Maker MZ public product documentation/blog.
- D&D Beyond public Character Builder/Maps documentation.
- World Anvil and LegendKeeper public feature documentation.
- Arkenforge public feature/press-kit documentation.
- TaleSpire public product description.
- Hero Forge public product/kitbashing documentation.
- Reallusion Character Creator public feature documentation.
- Adobe Substance 3D Designer/Painter public documentation.
- Live2D Cubism public editor/SDK documentation.
- BrowserStack Percy public visual-testing documentation.
- Sentry public product/changelog/API documentation.
- ElevenLabs public documentation.
