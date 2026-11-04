# PXR — Procedural Pixel Rendering Recovery

**Status:** PXR-01 OWNER-SELECTED, IN PROGRESS in the proposed OPS5 CURRENT.json projection; PXR-02..05 blocked, no visual-quality acceptance or production certification. Canonical activation requires protected-main publication of PR #1965.
**Date:** 2026-11-03
**Owner:** John Brandon Turner
**Proposed family:** PXR (Procedural Pixel Renderer)
**Tranches:** FIVE, PXR-01 through PXR-05. No automatic PXR-06, no one-tranche-per-species, and no rebranding partial source work as a completed stage.
**Main goal:** One genuinely parameter-driven, pixel-level character appearance generator, high visual quality and equal coverage for all current Core 26, with open-ended user-created Species using the very same engine.

## Owner art-direction correction — binding for PXR-01 (2026-11-04)

The owner explicitly rejected the previously tested glossy/3D-like, volumetric primitive and low-detail thick-outline cartoon appearance. **The now-authorized visual direction is high-detail, finely painted 2D character illustration with modular separately illustrated anatomical pieces.** The initial full-body *art source* review target is **2048 × 2560 truly authored pixels**, not a 24×32/128×160/384×480 output scaled up to a larger empty canvas. High-resolution source artwork must retain materially fine detail at 100% zoom. Heavy black silhouettes, toon outlines, generic 2.5D surface shading, reconstructed whole-limb chunks presented as rig-ready and coarse nearest-neighbor enlargement are rejected.

This section **supersedes the obsolete volume-generated pixel-construction baseline, source dimension comparisons and material/lighting synthesizer as the PXR-01 art-generation path** elsewhere in this historical program. Smaller CASI full-body, portrait, token and retrobit sizes remain *separate requested delivery profiles or derivatives*, never evidence that the HD master is artistically detailed. The five outcome-based tranches remain intact; no 26-species expansion until owner review of a real high-resolution detailed neutral character and actual source-layer anatomy.

The working implementation in Multiversal-app draft PR #879 is a native-source-painted transparent PNG compositor with per-layer original RGBA SHA-256, parent/pivot poses and fail-closed source provenance. It is still **only a compositor, not the promised finished appearance generator**: 54 independently illustrated neutral Vespin parts, concealed joint surfaces, high-detail appearance variants and their final art rights are missing. No green technical check, generated mood board, schema, mock Vespin or compilation may be recorded as artwork acceptance. Source-art assembly must be parameter-driven: recoloring/mask/marking/pose, swapping independently authored anatomical parts, and cross-species novel topology without a canned whole-character swap. Native 2048×2560 illustrated art, visual review and creator variability must all be proven.

**UI review constraint:** user can inspect source pixels on a phone via a fit-to-screen view or pan/zoom 100% and 200%, without interpreting a low-resolution screenshot as original master detail. Keep owner-approved detailed style reference as the target and explicitly reject later flatter/thicker-outlined boards.

## 1. Reconciled starting truth

The authoritative OPS5 entrypoint is operations/BOOTSTRAP.md and CURRENT.json. Current Core-26 identity comes from governance/application-planning/species-reconciliation/CORE_26_SPECIES_AUTHORITY_v1.0.0.json, not the older immutable 25-species PPIA evidence. The separate CORE_26_GAME_READY_STANDARD_v1.0.0.json requires equal standards, including morphology, presentation and cross-system reuse.

Actual Multiversal-app code exposes:
- PCV-02 Pixel2D person-scale 24x32 technical/first-party fallback, explicitly not nonhuman-complete: apps/client-ui/src/product/pixelAvatar.ts and governance/application-planning/product-convergence/PCV-02_PRIMARY_PIXEL_ASSET_PACK.json.
- CASI-03 six semantic output profiles: native 128x160 full body with standard 256x320 derivative; native 96x96 portrait to 192x192; native 64x64 token to 128x128, plus retrobit 64x80, 32x40 and 16x20 semantic rerenders. These are **profile definitions**, not proof of actual high-fidelity artwork. The user-supplied Vespin quality reference is materially above the currently demonstrated rendering result.
- MCCS/MVPS typed morphology and topology, 66 noncanonical future-body-plan stress examples, abstract cardinalities and parent relationships. These contain NO complete authored geometry/rig/light/camera/material construction for arbitrary bodies. The symbolic validator explicitly leaves physical limbs/manipulators and renderer fit unresolved.
- AXI-02 custom-Species source drafts can add custom body regions/parent relationships/counts and choose material/texture/color/pattern/marking per region; stage surface intent to CASI through owner checks. Current draft semantics do not specify how every imaginable shape looks in pixels.
- FGA/FDE garment parameters, topology fit and primitive demands are useful, but FDE-03 overlays simple SVG garment geometry on the tiny PCV-02 sprite.
- PCA/PAPT asset/rig/material production plans and ARI rights/provenance contracts are useful pipeline orchestration, but not evidence of executed production visuals.
- AXI-06 tracks 26 actual playable species plus eight synthetic radical test demands across six profiles = **204** visual-evidence obligations. That is an evidence requirement, not 204 verified art outputs.
- Isolated app PR #878 (draft) prevents conflating semantic coverage with real rendering; it does not create the missing high-quality renderer.

Diagnosis: there is a large gap between semantic contracts and an actual expressive procedural raster engine. More schema-only tranches cannot solve it.

## 2. What "actual generator" means

The final image must be *computed from current internal character appearance parameters*, not a selection of entire pre-rendered characters. Art must remain correct across widely different topology and user-customized anatomy, and at high visual quality.

Pipeline:
Current Species/Form and A4 identity + AXI Creator draft
 -> validated topology and visual-construction descriptor
 -> parameterized procedural anatomy builder: shapes, proportions, appendage attachment and articulation, perspective, pose and occlusion
 -> raster-stage masks and structured surface maps
 -> per-pixel material/lighting/shading/edge/detail synthesizer
 -> image compositor, foreground equipment/garments/wing membranes and transparency
 -> independently constructed full-body/portrait/token/Retrobit profile outputs
 -> reproducible immutable recipe and output receipts; local display/cache/export; rights/owner gates.

Minimum *render-geometry grammar* beyond today's body-graph labels:
- per-region local transform, axial or radial orientation, bounding proportions and contour control points;
- parent attachment anchors, joint axes and angle/pose limits; number of repeated limbs/rays/segments;
- volume or depth hint, front/back/overlap order, occlusion, cutout and masking;
- procedural contour vocabulary (organic chitin plates, muscle/soft tissue, segmented cylinders, branching roots, feathers, wings/membranes, fur, stone, machines, fluid/energy/distributed body particles);
- internal material zones, per-pixel palette ramps, normal/curvature/depth approximations, edge/outline discipline, controlled highlights/shadows, texture synthesis, scars/markings/patterns and color;
- stable view-space landmarks and profile-specific composition; independent head detail and token simplification;
- seed-driven variety and explicit user locks; source revision, content fingerprints and failure diagnostics.

This is **not 26 separate handcoded renderers**. The *engine* is species-agnostic. Canonical species MAY supply separate data-driven visual blueprints, uniquely sourced motifs, authored masks/style primitives and quality constraints—without dispatching by Species name in rendering code. No silent humanoid fallback.

User-created Species use the exact same visual grammar and visual-construction editor. Known shape primitives can autogenerate a meaningful baseline. An entirely novel organism requires creator-specified visual geometry, shape/pattern choices or owner-approved source artwork to reach sophisticated quality. Unknown shape nouns alone never authorize invented biology or promise an aesthetically convincing result; the editor must explain what construction information is missing and let the creator supply it.

## 3. Rendering technology decision and falsifiable prototype

**Candidate baseline:** deterministic CPU logical-pixel pipeline implemented as ImageData/typed-array raster generation in the existing TypeScript web/Tauri client. Worker isolation, incremental dirty-region recomputation, seeded geometry/noise, reusable contour/mask caches, and separate display scaling. HTML Canvas can display pixel buffers; optional PixiJS v8/WebGL2 can accelerate multipass compositing, but its WebGPU path is not assumed portable. A renderer framework **draws provided geometry**; it does not supply anatomical art quality by itself. No required third-party paid API or online generative image model at runtime.

The first tranche must evaluate three genuinely native logical working sizes: existing 128x160, candidate 256x320, candidate 384x480, by rendering the SAME detailed visual descriptors and comparing *newly authored/derived actual pixels*. Do not mistake 2x nearest-neighbor enlargement or a 1024px picture of blocks for higher native information. Owner-approved final quality and profile choice controls the design; the candidates do not unilaterally rewrite CASI-03 or original style authority. High-detail pixel aesthetic can incorporate nuanced controlled ramps/dithering/transparency where reference quality demands it; Retrobit remains a separate reduced-detail semantic rerender.

Render output must be independently generated for portrait/token rather than cropped low-resolution full-body images. Preserve input seed + semantic ID + renderer version + asset lock for replay.

## 4. Hard rules: no hidden substitution, no product-quality theater

1. Real preview pixels must visibly change under material, anatomical, shape, proportions, equipment/wardrobe and pose changes. A changed JSON/checksum without changed image is not a render test.
2. A visually acceptable sample image from an image model is concept art, **not a working generator**. End-to-end samples must be generated by the same running local code and parameter grammar that will ship.
3. 26/26 Core species is mandatory at equal *render-quality* acceptance and correct current authority, not merely a populated dropdown. Do not synthesize missing canon; flag and resolve against owner authority.
4. A valid custom Species cannot be forced into Human. Unknown features must be editable visual-grammar inputs or explicit unsupported diagnostics. Not all conceivable art is automatically derivable from text tags.
5. Do not counterfeit screenshot, independent visual review, ARI rights, native installed-device, or live-service receipts; negative cases matter.
6. Do not infer gameplay anatomy/abilities, wardrobe/equipment ownership or legal rights from a rendered body silhouette.
7. No per-species secret code branches, canned whole-character swaps passed as procedural generation, shape-placeholder diagrams, upscaled tiny sprites, synthetic-only certificates or milestone splitting to hide incompletion.
8. Quality acceptance requires the owner's actual review against supplied high-detail insectoid reference. A green unit test alone is not sufficient.
9. Reference illustration informs **quality**, not permission to copy its design or replace canonical Vespin anatomy; Vespin requires four arms, two legs, wings and a stinger in the current supported example.
10. Preserve current CORE26-CURRENT-01, GPR/PCV-03F, MTLC-14 and current AXI work and independent branches. No product release or non-authorized payment.

## 5. Exactly five outcome-based tranches

### PXR-01 — Quality-first falsification / vertical engine slice
**Scope:** Actual source-backed browser runtime for generic morphology/visual construction -> procedural raster -> high-detail output, using Human, canon-accurate Vespin, and an *invented unknown creator-defined nonhuman body plan* (not secretly pre-registered in code). At least four meaningful parameter mutations per exemplar, including topology variation, material/color, body proportion and an overlapping appendage or garment. Comparison against owner's insectoid quality reference at the three candidate native resolutions, with exact source PNG artifacts and reproducible recipes. Add an accessible comparison page and readback diagnostics.
**Hard acceptance:** Owner can inspect original full-resolution render outputs and interactive differences; each exemplar has clearly different anatomy and recognizable materials, no copied/static image swaps, no human fallbacks. At least one user-origin novel appendage/location is drawn and remains attached in 3/4 perspective. Code/integration tests and actual browser capture agree.
**Stop condition:** If the user-visible images do not meet the reference's quality *class*, stop and redesign the generative representation **inside PXR-01**; do not expand to 26, declare "foundation complete" or invent extra tranches. This is the early feasibility kill gate.

### PXR-02 — General-purpose pixel construction and rendering engine
**Scope:** Complete the validated visual-descriptor schema; extensible typed body-part/contour grammar, topology compiler, complex occlusion, pose, per-pixel material/shading/lighting/pattern pipeline, view-dependent composition, deterministic variants and locks, state/cache architecture, provenance and missing-visual-authoring diagnostics. Render independent full-body/portrait/token, Retrobit semantic down-detail. Compare CPU backend on Android/Windows; optional GPU backend only after actual benchmark.
**Hard acceptance:** Run heterogeneous generated shapes (biped, multi-arm, winged, radial/branching, elongated, distributed, amorphous) without a per-species code fork; demonstrate same seed identity, head/body variant changes, no off-canvas anatomy or visual occlusion collapse, deterministic replay and fallback failure clarity. Maintain output quality from PXR-01.

### PXR-03 — All 26 canonical Species, equal quality
**Scope:** Source-map each current playable Species to actual canon-specific visual blueprint/parameters and style motifs; build missing authored grammar inputs, geometry/texture patterns and distinct anatomy as data. Wire all through one renderer; generate variations and separate profile output for every Core-26 name. Supply source/rights ledger and owner-visible review gallery.
**Hard acceptance:** All 26 appear correctly identified, canonical/current version, with visually distinct anatomy where canon distinguishes them; no legacy Nekrons in place of Morganthyr, no missing Akwi. At minimum four distinct parameter-selected visible variants per species and three independently constructed main views: >= 26 x 4 x 3 = **312 actual output cases** with nonblank PNGs and real golden visual captures. Automated checks cannot waive owner image-quality review. Record any source-canon absence as a blocker, never invent missing biology. PXR-03 stays unfinished until 26/26 proof is achieved.

### PXR-04 — Full user-created Species and appearance/wardrobe editor
**Scope:** Connect existing AXI-02/MCCS user-defined graph and surfaces to construction controls for silhouette, anchors, joint/shape/appendage geometry, materials, pose, body-part counts and custom regions; optional template reuse/import with rights and owner/Creator registration checks. Programmatic generation from user-created unknown species through same renderer, save/reopen, export/round trip, version and permission boundaries. Fit FGA without invented garment compatibility; render true visual outfits when proven.
**Hard acceptance:** Users can build and visualize at least five *novel* previously unencoded body plans, including six/multiple limbs, radial or segmented, plant/branching, fluid/amorphous, and a user-added part; change and save native pixels in full-body/portrait/token without developer edits. Both registered and unregistered paths preserve distinct authorization. Unspecified or impossible form constraints block with actionable diagnostics rather than a Human image.

### PXR-05 — Installed standalone visual test app and terminal certification
**Scope:** Package a genuine source-linked standalone Appearance Studio for Windows and Android; use identical renderer/authoring source, drag/edit/pan/zoom/compare, native-resolution view, save/reopen/export, mobile screen/touch UX, diagnostics and bug report export. Finish independent capture/rights review across existing AXI-06 204 required Core26/radical x six-profile cells. Measure real physical-device performance and tune.
**Hard acceptance:** Owner can make multiple compelling new species in installed test apps, persist edits, reopen, compare variation, export results and confirm each supported output. Every required evidence cell has a real independently reviewable status; 204/204 only when genuinely demonstrated. **No production-complete label unless all mandatory Core-26 visuals, novelty/creator tests, profile views, actual native-platform runs, image quality and authorization/provenance proof pass.** If a radical fixture is not representable, report that failure and keep the total gate open.

Each tranche is a meaningful multi-step execution package, not a single commit. Work continues through intermediate implementation, internal iterations and failures within the same tranche. Do not hand back after a single substep when independent authorized work remains.

## 6. Effort, critical path, and what can be reused

The number "five" is an *acceptance grouping*, not a claim the task is small. The largest work is (a) a high-quality open generative pixel geometry/material language and (b) enough honest Core26 visual blueprints to produce consistently good output. Native device proof and creator edit workflow are additional real work. Expect a major graphics-engine/art engineering effort, not a CSS/HTML task; a precise cost, schedule or person-hour quote is **not supportable** until the PXR-01 pixel experiments resolve achievable quality and visual-complexity per species.

Reuse without reopening source owners: MVPS/PPIA canonical species data; MCCS-03/06 and 66 tests; AXI-02 draft authoring, imports and owner gates; CASI parameter schemas and output profiles; FGA/FDE composition/fit semantics; PCA/PAPT production plans; ARI rights and source registration; A3/A4 persistence. Add only the missing *render geometry, pixel synthesis, art descriptors and real visual proof*. A graphic API (Canvas/Pixi) is an implementation helper, **not** the appearance intelligence.

Risk priority:
- **R1 infeasible quality** under current 128x160 profile: prove native size/quality feasibility in PXR-01, keep style/output profile explicit.
- **R2 unbounded unknown morphology**: close open-ended structure by creator-authored visual descriptors, reusable shape grammar, and fail-closed diagnostic where insufficient.
- **R3 combinatorial occlusion/garment artifacts**: per-region attachments and depth order + fuzz tests + manual review of interactions.
- **R4 missing canonical anatomy or visual motifs**: source-ranked Core26 register, explicit owner decisions; no invention for completion.
- **R5 asset/right uncertainty**: first-party procedural primitives + licensed authored assets only, ARI evidence; concept reference is a comparison target only.
- **R6 performance/offline and platform quality**: CPU deterministic baseline, measured Android/Windows performance and caching, no required runtime cloud or paid provider.
- **R7 appearance passes tests but fails humans**: reference-comparison and owner review in PXR-01 and every subsequent tranche.

## 7. Quality and test minimums

- **Visible pixel quality:** anatomical truth, proportion/perspective, differentiated materials, high-frequency meaningful detail, controlled edge/shading, wing/appendage quality and coherent form. Human review required; never replaced by subjective self-score.
- **Functional variety:** same body plan and seed; alter one parameter at a time. Confirm both desired changed regions and unchanged protected regions. Sample many seeds per model to catch ugly outliers.
- **Coverage:** 26/26 species, including special identities, plus creator-authored novel graphs and synthetic exotic regression. 204 existing source demand cells are separate from 312+ variant snapshots.
- **Render invariants:** nonblank, dimension/bytes verified, deterministic replay, no unintended fallbacks, no absent/phantom limbs, clipping, z-order violations, unstable randomness, or whole-character image swap.
- **Output profiles:** six CASI views must be supported or honestly blocked with tracked evidence; no claim a crop is a new semantic render.
- **Permissions:** custom unregistered drafts never become playable automatically; no counterfeit species grants, rights or unauthorized cross-user reads.
- **Usability:** exact source runtime on real Windows/Android, save/reopen and export, actual interaction screen recordings/screenshots, owner-quality signoff.

## 8. Governance and authorization

This file and PXR_PROGRAM_BACKLOG.json define the bounded five-tranche family, but are not work selectors. Owner Continuation on 2026-11-04 selected PXR-01 as an **on-demand, nonpersistent** implementation lane in the CURRENT.json projection of AIOC PR #1965, with the companion experimental application draft PR #879. This selection becomes canonical only when PR #1965 is durably published under OPS5. The source/CI renderer has not met the visual quality gate, and PXR-02..05 remain blocked. This registration does not grant new spending, public release, a fourth persistent slot, or automatic successor execution. GPR PCV-03F, MTLC-14 and AXI are unaffected.

Do not mark a tranche completed_verified merely because this program is written or because a PR passes source validation. PXR-01 may complete only with **executed interactive art output and owner-visible reference comparison**. Later tranches inherit that quality gate; every unknown remains explicit.

### Source anchors

- OPS5: operations/BOOTSTRAP.md, OPERATING_CONTRACT.md, CURRENT.json, LANES.json.
- Current Core-26: governance/application-planning/species-reconciliation/CORE_26_SPECIES_AUTHORITY_v1.0.0.json; governance/application-planning/player-species/CORE_26_GAME_READY_STANDARD_v1.0.0.json.
- App: apps/client-ui/src/product/pixelAvatar.ts; apps/client-ui/src/axi/Axi02SpeciesCreation.ts; Axi02StructuralPreview.tsx; apps/client-ui/src/axi/Axi06Core26RendererCoverage.ts; apps/client-ui/src/casi/Casi06AppearanceStudioRuntime.ts; apps/client-ui/src/fde/Fde03VisualGarmentPreviewRuntime.ts; packages/contracts/src/character-appearance-standard-integration/casi-03-cas-sd1-derivative-profiles.ts; packages/contracts/src/multiversal-character-creature-studio/mccs-03-open-body-plan-grammar.mjs; packages/contracts/src/production-capability-acceleration/pca-05-character-asset-rig-garment-lod-production-pipeline.ts.
- Owner-supplied quality reference: in conversation (Vespin comparative image), not an asset-rights grant.
- Graphics implementation candidates: W3C Canvas 2D / MDN ImageData APIs, optional PixiJS v8 WebGL2, evaluated but not yet adopted.
