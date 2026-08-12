# PPIA-06 — Character Appearance Integrated Workflow & Traceability Candidate

**Work item:** PPIA-06 — Character Appearance Creator  
**Version:** 0.1.0  
**State:** INTEGRATED WORKFLOW / TRACEABILITY CANDIDATE — NOT PPIA-06 COMPLETE  
**Inspector / Action / Reference merge:** `f4657ba33c4c9ad48ee97354be0ad3eed55433c2`

## Purpose

Integrate the verified Species-aware appearance foundation and Inspector / Action / Reference contracts into bounded end-to-end workflows covering Character Builder entry/reopen, all governed Species profiles, Species/Form/live-biology changes, authored appearance, presentation wardrobe, actual equipment projection, deterministic randomization/presets/import, fixed-view rendering, portrait/token handoff, permissions/accessibility and versioned recovery.

This milestone explicitly covers **all 25 Species profiles**, not only the unusual or recently corrected Species. Special morphology cases are additional constraints on the same appearance architecture rather than substitutes for ordinary Species coverage.

## Owner visual provenance correction

Owner decision **OVC-027** broadens the earlier rat-ninja correction: **all rat-humanoid images in `Arthold.zip` are Furashin reference art**, even when a filename or embedded generation prompt says `ratman`. Filename/prompt text is non-authoritative metadata.

This visual-provenance ruling does **not** remove, rename or merge the separate canonical **Ratman** Species. Ratman continues to use its written Species profile. The supplied Arthold rat-humanoid images are simply not Ratman reference art.

AI-generated art remains noncanonical reference/inspiration unless the owner separately promotes a particular image.

## Integrated workflow surface

The package defines **16 end-to-end workflows**:

1. Character Builder entry, ordinary bounded appearance authoring, save and reopen;
2. Species/lineage/variant changes and explicit appearance rebase;
3. unusual-topology authoring/rendering for insectoid, reptilian, aquatic and other nonstandard bodies;
4. Arborae four-season profile editing and reopen;
5. Mythragara base/animal authoring with derived hybrid and current-Form updates;
6. Nekron one-time transition followed by derived second customization;
7. Suula persistent adaptation history, active biology and nested-hand live state;
8. Furashin live phenotype plus Furashin/Ratman art/species separation;
9. ManyToms constituent identity, cohesive collective composition, presets and views;
10. Stygian conditional wings and actual-equipment visual fit without anatomy mutation;
11. The Free broad humanoid android grammar plus Toba-Madra dye/cybernetic authority separation;
12. presentation-only wardrobe versus actual PPIA-03 equipment projection;
13. deterministic randomization, preset save/apply and reviewed import/export;
14. fixed 3/4 full-body, portrait/zoom and tactical-token rendering/handoff;
15. permission filtering, hidden-state safety, mobile, keyboard and nonvisual parity across the full Species surface; and
16. `expected_version` / `operation_id` mutation receipts, stale-write handling, ambiguous-result recovery and reopen convergence.

Fourteen workflows may contain a narrowly scoped PPIA-06 appearance/presentation write and therefore use `P06-MUT-001`. Two are deliberately read/analysis-only. No workflow writes upstream Species/Form biology or actual equipment state.

## Complete all-Species traceability

The workflow, Species coverage and traceability matrices jointly prove:

- **25 / 25** governed Species profiles covered;
- **20 / 20** Inspector projection groups, derived from the governed action-group definitions;
- **30 / 30** governed actions;
- **48 / 48** Inspector / Action / Reference cases assigned exactly once;
- **36 / 36** Species Visual cases assigned exactly once;
- **32 / 32** new integrated workflow cases assigned exactly once;
- **116** effective deterministic cases across the three retained surfaces;
- **18 / 18** semantic appearance layers inherited;
- **5 / 5** compatibility dimensions inherited; and
- **9 / 9** authority handoffs exercised.

The 32 integrated cases include all 25 Species. Human, Elf, Dwarf, Goblin, Orc and Sharr exercise ordinary bounded authoring rather than being skipped in favor of unusual anatomy. Giantkin, Gray, Ratman and Rog exercise distinct Species/lineage boundaries. Rohai, Moravi, Vespin, Rakuuta, Traiga and Kola-Ha exercise different nonstandard topology/surface constraints. Toba-Madra, Arborae, Mythragara, Suula, Nekron, ManyToms, Stygian, Furashin and The Free exercise their owner/source-specific rules.

## Character Builder and upstream authority

Character Builder supplies the Character, rules snapshot, selected Species/lineage and equipment context. PPIA-06 consumes those references and returns appearance/presentation state; it does not rewrite Character Creation mechanics.

PPIA-05 remains authoritative for Species, lineage/variant biological constraints, morphology, current Form, transition eligibility, persistent acquired biology and active biological state. Appearance may author only source-bounded choices that PPIA-05 exposes as editable. A Species/Form/current-body change can invalidate or rebase appearance choices, but it never permits PPIA-06 to fabricate anatomy.

Unknown/source-unspecified anatomy stays unknown. There is no human/humanoid fallback.

## Species-specific integrated behavior

The workflow surface proves, among other rules:

- **Arborae:** four separately customizable seasonal profiles; upstream current season selects the active presentation.
- **Mythragara:** base and animal identity are authored; hybrid is deterministic/derived and retains identity markings.
- **Nekron:** appearance cannot trigger ascension; after one upstream outcome, a derived second customization is available for that outcome only.
- **Suula:** persistent adaptation markers cannot be erased; active adaptations update live appearance; nested hands/claws are first-class live state.
- **Furashin:** preferred/live fur phenotype respects the maximum of three simultaneous colors plus pattern/texture; all Arthold rat-humanoid art binds to Furashin under OVC-027.
- **Ratman:** remains a separate canonical Species profile despite the Arthold art-label correction.
- **ManyToms:** one constituent identity plus cohesive collective presentation; the renderer is not required to draw exactly seventeen visible figures.
- **Stygian:** optional wings may be functional or vestigial only when upstream morphology provides them; appearance cannot grant flight.
- **The Free:** extremely broad humanoid android design is supported, but arbitrary quadrupedal/nonhumanoid topology is not.
- **Vespin:** four arms/two legs remain intact.
- **Moravi:** two arms/four legs remain intact.
- **Rakuuta:** ears are not horns and the raven-shaped facial field is actual black feathers.
- **Traiga:** two arms/two legs/tail with source-valid feathered/scaled/mixed covering; no invented extra wing pair.
- **Kola-Ha:** baseline fins/tail remain separate from Bioengineering Form anatomy.
- **Toba-Madra:** ursine baseline, natural fur, cosmetic dye, cosmetic tech plating and actual installed cybernetics remain distinct authority channels.

## Appearance write and recovery boundary

Every authoritative appearance write uses `P06-MUT-001` with explicit human authorization, `expected_version` against `appearance_state_version`, and stable `operation_id`.

A stale version fails atomically. An ambiguous result requires operation-status and current-version lookup before retry. Compatible duplicate operation IDs converge on the prior receipt and never double-apply. Conflicting operation-ID reuse fails safely. Save/reopen uses the committed semantic state and operation receipts rather than treating rendered pixels as authority.

PPIA-06 writes are limited to eligible player-authored appearance, profile-specific appearance, accepted deterministic randomization, appearance presets/imports, presentation wardrobe, and supported saved pose/expression/presentation state. Source-owned biology/history/current Form, transition state, equipment ownership/equipped state and renderer support cannot be mutated through these actions.

## Wardrobe and equipment

The customizer's curated wardrobe is presentation-only. It may contain clothing, armor, weapon and gear visuals that are useful for designing the Character even when they do not correspond to inventory. They grant no mechanics.

Actual equipment preview is a separate permission-safe PPIA-03 projection. Topology-compatible visual variants are preferred. If a compatible visual asset is unavailable, the renderer reports unavailable/unsupported rather than warping an asset or changing the actual equipment state.

## Renderer, portrait and token handoff

`pixel-art-v1` remains a renderer adapter over renderer-independent semantic appearance state. The master composition is a fixed **3/4 full-body** view with switchable portrait/zoom and tactical-token views. Arbitrary rotation and pseudo-3D are prohibited.

Portrait/token outputs are versioned derivatives. Missing assets, anchors, masks, palette ramps, topology support or a particular view can produce partial/unsupported renderer status while the Character remains valid. Downstream portrait/token consumers do not become semantic appearance authority.

## Permission, hidden-state and accessibility rules

Permission filtering happens before protected reference resolution, derived appearance state, renderer asset selection, counts/diagnostics, presets/import/export and AI context. Hidden markers cannot leak through missing-asset diagnostics, option counts, omitted labels, generated summaries or renderer choices.

The same semantic workflow is required on mobile, keyboard-only and screen-reader/nonvisual projections. Color is never the sole carrier of state. High zoom/reflow cannot hide required actions. The visual preview is not required to understand what changed or whether an operation succeeded.

AI may summarize, compare and propose from the authorized projection only. AI cannot commit changes, infer hidden biology, promote reference art to canon, grant equipment, trigger Form/transition changes or convert renderer output into Character truth.

## Milestone boundary

This is the PPIA-06 **Integrated Workflow / Traceability** milestone only. PPIA-06 remains `started` until the later final completion gate verifies the complete Character Appearance Creator package.

No application runtime, STAGE-A-A2, release, deployment, tester access, paid service or production credential is activated by this milestone.
