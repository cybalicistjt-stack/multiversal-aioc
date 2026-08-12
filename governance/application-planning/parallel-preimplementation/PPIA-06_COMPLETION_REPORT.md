# PPIA-06 — Character Appearance Creator Completion Report

Status: **COMPLETION CANDIDATE — NOT COMPLETE UNTIL THIS EXACT HEAD PASSES REQUIRED VALIDATION AND MERGES**

This package closes the PPIA-06 design tranche only after exact-head hosted validation and merge evidence exist. It does not activate application runtime, STAGE-A-A2, release, deployment, tester access, paid services, or production credentials.

## Verified milestone chain entering completion

1. **Appearance Foundation** — exact head `d788d42187c5d53d2121a1f738b9d3445d0f67d8`; PR #269; all 45 applicable hosted workflows passed; squash merge `66789fcb140b06c7873231e28baf1c00dec8db91`.
2. **Species Visual & Morphology Addendum** — exact head `17b333d950b8748e625f1b96cc294d1ec582bc63`; PR #270; all 46 applicable hosted workflows passed; squash merge `65b6a7cd9d2cbaa72cad20aab1b72781df37f145`.
3. **Appearance Inspector / Action / Reference** — exact head `4c25ea2e59b0fc40639387eed6654bf74a83d64c`; PR #271; all 47 applicable hosted workflows passed; squash merge `f4657ba33c4c9ad48ee97354be0ad3eed55433c2`.
4. **All-Species Integrated Workflow / Traceability** — exact head `58222dacbbf7e3ed40c5d8dad1630a01acf32876`; PR #272; all 48 applicable hosted workflows passed, including `Validate PPIA-06 Integrated Workflow and Traceability Contracts` run `31617379430`; squash merge `37b974e0395c77d546276ea5a5a20fe3859334c3`.

## Canonical completion-gate proof

The canonical backlog requires an **implementation-ready appearance-studio specification with species-aware controls, randomization/presets, nonhumanoid/mobile/accessibility behavior, portrait handoff, and scope boundary**.

PPIA-06 satisfies that gate through the verified milestone chain:

- **Species-aware appearance studio:** the Appearance Studio is generated from authorized Species/Form morphology and profile state rather than a universal humanoid slider model. Unknown/source-unspecified anatomy stays unknown; no human/humanoid default is synthesized.
- **All 25 governed Species are explicit:** Human, Elf, Dwarf, Goblin, Orc, Giantkin, Stygian, Sharr, Gray, The Free, Ratman, Furashin, Rog, Rohai, Moravi, Vespin, Rakuuta, Traiga, Kola-Ha, Toba-Madra, Arborae, Mythragara, Suula, Nekron and ManyToms all participate in the governed Species profile and integrated workflow surface.
- **Renderer-independent semantic state:** eighteen stable semantic identity/state layers separate Character appearance truth from renderer assets. They cover appearance identity/version, morphology/current Form, body topology/proportion, surface material, head/face, covering/appendage style, coloration, markings/history, age, presentation wardrobe, equipment projection, hidden/persistent biology, pose/view/portrait/token framing, preset/randomization locks, renderer coverage/fallback and accessibility/nonvisual summary.
- **Compatibility model:** five independent compatibility dimensions preserve biological validity, appearance-choice compatibility, renderer compatibility, equipment visual compatibility and view/pose compatibility. Renderer support is explicitly `supported`, `partial`, `unsupported`, or `unknown`; renderer gaps never invalidate a valid Character.
- **Morphology graph:** body roots, torsos, heads, limbs, nested appendages, structural appendages, tails, wings, surface regions and composite constituent bodies are first-class. Moravi two-arm/four-leg, Vespin four-arm/two-leg, Suula nested hand/claw and ManyToms composite-body cases are preserved without humanoid collapse.
- **Source/owner provenance:** written Species sources, inherited contracts, owner canon decisions, owner concept art, player-authored appearance, presentation wardrobe, equipment projections, renderer metadata and unresolved gaps remain distinguishable. Filename/prompt labels are non-authoritative.
- **OVC-027 Furashin/Ratman separation:** all ten ratman-labelled rat-humanoid images in `Arthold.zip` are governed as Furashin reference art under OVC-027 even when filenames/prompts say ratman. This does not remove, merge or rename the separate canonical Ratman Species. AI art remains noncanonical reference/inspiration unless separately promoted.
- **Special biological/profile behavior:** Arborae four seasonal appearance profiles, Mythragara derived hybrid, Nekron one-time transition customization, Suula persistent/active Adaptation visuals, Furashin live fur phenotype, ManyToms constituent/collective identity, Stygian wing-function boundary, Toba-Madra ursine/dye/cybernetic separation, The Free humanoid-android bound, Rakuuta ear/facial-feather correction, Kola-Ha baseline-vs-Form and Traiga covering/tail rules are explicit.
- **Inspector and actions:** twenty permission-safe projection groups expose the complete appearance surface. Thirty governed actions comprise twelve reads, ten nonmutating analysis/proposal actions and eight narrowly scoped writes.
- **Mutation/recovery:** every write uses `P06-MUT-001` and requires explicit authorization, `expected_version` against `appearance_state_version`, and stable `operation_id`. Stale writes reject atomically; ambiguous results require operation-status/current-version/receipt checks before retry; compatible duplicate operation IDs converge and conflicting reuse fails without mutation.
- **Randomization, presets and import/export:** deterministic randomization uses stable seed/version/eligible-choice-set/lock inputs and touches only authorized player-authored choices. Presets/imports use stable semantic IDs and explicit compatible/unavailable/incompatible/missing-pack/unsupported/restricted/partially-recoverable classifications. Required anatomy, Species/Form truth, persistent history, hidden state and actual equipment cannot be randomized or silently substituted.
- **Presentation wardrobe vs actual equipment:** presentation wardrobe is curated visual-only content and grants no inventory or mechanics. Actual equipped-item rendering remains a permission-safe projection from PPIA-03 with topology-compatible variants or explicit unsupported fallback; Appearance Studio never equips, unequips, grants, consumes or transfers Assets.
- **Pixel-art renderer:** `pixel-art-v1` is the first fully specified renderer over renderer-independent semantic state. It uses stable asset IDs, semantic render bands, universal/topology-specific anchors, explicit occlusion, semantic palette zones and deterministic render-plan identity. The authoring master is fixed full-body three-quarter, with portrait/zoom and tactical-token views. Arbitrary rotation and pseudo-3D are prohibited.
- **Future renderer boundary:** core Character state cannot require sprite/pixel-specific fields. Renderer metadata is separate from Character truth and the contract explicitly preserves future 3D or other renderer adapters.
- **Permission/privacy boundary:** permission filtering precedes protected reference resolution, counts/diagnostics, renderer asset selection, derivatives, presets, export, portrait/token outputs and AI context. Hidden biology/equipment cannot leak through silhouette, layer count, missing-asset diagnostics, palette, anchors, occlusion, support state or exports.
- **Accessibility/mobile parity:** mobile, keyboard-only, screen-reader/nonvisual, text/high-zoom, reduced-motion and noncolor behavior are governed. Every meaningful visual state has semantic nonvisual representation; color is never the sole state carrier.
- **Character Builder and downstream handoffs:** Character Builder supplies authoritative Character/rules/species/equipment context; Appearance Studio returns versioned appearance/presentation references. Portrait/token consumers receive derivatives and never become appearance authority.

## Final implementation-ready surface

- 25 governed Species profiles.
- 27 inventoried Species/supporting PDFs and 88 inventoried visual-art assets in the governed Species visual source package.
- 27 owner visual-canon decisions through OVC-027.
- 18 renderer-independent semantic appearance layers.
- 5 compatibility dimensions.
- 4 renderer support states.
- 20 permission-safe projection groups.
- 30 governed actions: 12 reads / 10 analysis-proposals / 8 writes.
- 1 versioned/idempotent write protocol: `P06-MUT-001`.
- 16 integrated workflows: 14 mutation-capable / 2 read-analysis-only.
- 9 explicit authority/domain handoffs.
- 48 Inspector/Action/Reference cases.
- 36 Species Visual cases.
- 32 integrated workflow cases.
- 116 effective deterministic cases with inherited case assignment exactly once.
- Full 25/25 Species workflow coverage.
- `pixel-art-v1` fixed 3/4 full-body, portrait/zoom and tactical-token view contract.
- Explicit future-renderer boundary and unsupported/unknown fallback semantics.

## Blocking boundaries retained

- PPIA-05 remains Species/Form/current-body/persistent/live biology authority.
- PPIA-03 remains actual Asset ownership/equipment/install-state authority.
- Appearance never grants or changes mechanics by changing how something looks.
- Appearance never creates anatomy, Species eligibility, transformations, ascension, Adaptations or current Form state.
- Unknown/source-unspecified anatomy is never defaulted to human/humanoid.
- Renderer topology profiles are compatibility classes, never Species taxonomy.
- Renderer/view support never determines Character validity.
- AI artwork does not become canon merely because it is present or named; filename/prompt text is non-authoritative.
- Presentation wardrobe does not imply ownership and grants no mechanics.
- Actual equipment preview cannot mutate equipment state.
- Hidden information is filtered before every protected derivative and diagnostic.
- Randomization/presets/import cannot mutate source-owned biology, hidden state, persistent history or equipment authority.
- No silent latest-asset, topology, anatomy or preset substitution is permitted.
- Arbitrary rotation/pseudo-3D is not represented by the 2D renderer.
- Color is not the sole semantic carrier.
- Offline authoritative mutation and blind retry after ambiguous writes are prohibited.
- AI may summarize/explain/propose only from authorized projections and has no irreversible appearance authority.
- No application runtime, STAGE-A-A2, release, deployment, tester access, paid service or production credential is activated.

## Completion integrity

This report does **not** itself make PPIA-06 complete. The exact completion-candidate head must pass `Validate PPIA-06 Completion Contract` and every applicable repository regression, then merge. Only immutable final-head / PR / validation-run / merge evidence can support `completed_verified`.

Canonical backlog transition is intentionally deferred to a separate **PPIA-06 → PPIA-13 transition** so generalized PPIA continuity never sees a completed current tranche without an initialized successor.

## Exact next governed operation after verified completion

After the completion candidate merges and post-merge completion evidence is recorded on the governed PPIA-06 branch, execute the separate PPIA-06 → PPIA-13 transition. That transition must atomically project PPIA-06 to `completed_verified`, initialize PPIA-13 — Onboarding, Help & In-App Teaching Content as `started`, select PPIA-13 in runtime continuity, preserve all PPIA-06 immutable evidence, and exact-head validate before merge.
