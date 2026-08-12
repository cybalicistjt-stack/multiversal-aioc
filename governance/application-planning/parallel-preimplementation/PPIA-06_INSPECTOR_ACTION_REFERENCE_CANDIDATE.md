# PPIA-06 — Character Appearance Creator
## Inspector / Action / Reference Candidate

Status: bounded preimplementation milestone candidate. This does **not** claim PPIA-06 completion.

## Purpose

Translate the verified Species-aware Appearance foundation into an implementation-ready Appearance Studio interaction contract: what the Player can inspect, what the system can analyze/preview, what may be written, how special Species/Form profiles behave, how randomization/presets remain deterministic and portable, and how renderer/accessibility failures surface without rewriting Character truth.

This candidate consumes:

- `PPIA-06_APPEARANCE_SEMANTIC_TAXONOMY_v0.2.0.json`;
- `PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json`;
- `PPIA-06_OWNER_VISUAL_CANON_DECISIONS_v0.1.0.json`;
- `PPIA-06_SPECIES_VISUAL_AUTHORITY_MANIFEST_v0.1.0.json`;
- `PPIA-06_PIXEL_ART_RENDERER_CONTRACT_v0.2.0.json`;
- the verified PPIA-05 Species/Form/Biology authority boundary;
- PPIA-03 equipment/Asset authority.

The rat-ninja reference correction is incorporated as `OVC-026`: it is Furashin art even though its filename/prompt says ratman. Filename/prompt text is explicitly non-authoritative metadata.

## 1. Inspector surface

The Appearance Studio exposes 18 semantic Inspector sections rather than a fixed humanoid slider inventory. Controls are generated from authorized Species/Form morphology and editable-profile contracts. The surface includes identity/profile context, body/proportions, head/face, surface/material, color, markings/history, age, Form/season/transition profiles, presentation wardrobe, actual equipment preview, pose/expression, fixed view switching, randomization/locks, presets/import/export, renderer diagnostics, accessibility/nonvisual summary, provenance/authority, and operation recovery/history.

A missing anatomy field does not create a default Human field. Required, optional, source-derived, Form-derived and history-derived morphology nodes remain distinct.

## 2. Species-aware profile behavior

The Inspector/action contract preserves the special behavior proven by the Species corpus:

- **Arborae:** four linked but separately customizable seasonal profiles; current season remains upstream biology.
- **Mythragara:** base and authorized animal appearances are authored; hybrid is derived and read-only as an independent profile.
- **Nekron:** a post-transition customization exists only after the one-time upstream transition; appearance cannot trigger or choose an unavailable ascension.
- **Suula:** persistent adaptation markers and active adaptation biology are read-only; cosmetics can be authored around them. Hand-within-claw state is live/pose state.
- **Furashin:** preferred fur phenotype supports up to three simultaneous colors plus pattern and texture. Mechanics-owned live phenotype is not rewritten as cosmetic state. Rat-ninja reference art is owner-bound to Furashin despite filename wording.
- **ManyToms:** one constituent identity is authored; renderer composition presents a cohesive collective instead of seventeen independent Character records.
- **Stygian:** horns/wings appear only when biologically authorized; wing appearance never grants flight and functionality remains upstream.
- **Toba-Madra:** natural biological fur and any-color cosmetic dye are separate channels; actual cybernetics are mechanics-owned projections.
- **The Free:** very broad humanoid android design grammar, but not arbitrary nonhumanoid topology; installed hardware remains mechanics-owned.
- **Vespin:** four arms/two legs plus wings/abdomen/stinger are structural; clothing/equipment must have compatible four-arm visual variants or report unsupported.
- **Moravi:** two arms/four legs are structural and cannot be collapsed to a two-leg humanoid renderer template.
- **Rakuuta:** swept-back structures are ears and the black raven-shaped facial field is actual feathers; neither may be silently reclassified.

## 3. Projection model

`PPIA-06_APPEARANCE_INSPECTOR_ACTION_CONTRACT_MATRIX_v0.1.0.json` defines 20 projection groups spanning all 18 semantic layers and all five compatibility dimensions:

1. identity/version/authority;
2. morphology graph;
3. current Form/transition/biology;
4. body/proportion/silhouette;
5. head/face structures;
6. surface/covering/material;
7. coloration/palette;
8. markings/scars/tattoos/history;
9. age presentation;
10. profile set/season/variant;
11. live biology/pose state;
12. presentation wardrobe;
13. actual equipment projection;
14. pose/expression presentation;
15. view/portrait/token;
16. presets/randomization/locks;
17. renderer coverage/assets;
18. accessibility/nonvisual summary;
19. provenance/conflict/art authority;
20. history/operation/recovery.

Permission filtering occurs before reference resolution, derivatives, renderer asset selection, diagnostics, presets/export and AI context. Hidden biological facts cannot leak through missing-asset messages, counts, summaries, preset compatibility or renderer diagnostics.

## 4. Governed actions

The contract defines 30 actions:

- **12 permission-filtered reads**;
- **10 nonmutating analysis/proposal actions**;
- **8 narrowly scoped writes**.

Read actions expose Character appearance, morphology, current Form/biology, profile sets, visual layers, presentation wardrobe, actual equipment projection, renderer/view support, presets, provenance and nonvisual/recovery summaries.

Analysis/proposal actions enumerate compatible choices, preview semantic deltas and derived profiles, preview deterministic randomization, validate imports, analyze renderer coverage, preview wardrobe/equipment visual fit, produce nonvisual comparisons and propose safe recovery after ambiguous results.

Writes may only change:

- Player-authored source-bounded appearance choices;
- editable Species/Form/season/transition profile overrides;
- an accepted deterministic randomization result;
- portable appearance presets;
- an explicitly reviewed preset import/application;
- presentation-only wardrobe;
- saved pose/expression presentation.

They may **not** mutate Species/Form biology, current Form, transition occurrence, persistent biological history, hidden source state, equipment ownership/equipped state, renderer support truth, Resources or mechanics.

## 5. Mutation and recovery

All authoritative appearance writes use `P06-MUT-001` and require:

- explicit authorization;
- `expected_version` against `appearance_state_version`;
- unique `operation_id`.

A stale version rejects without partial mutation. A compatible duplicate `operation_id` converges on the prior result instead of double-applying. A conflicting reuse fails safely. An ambiguous result is resolved by querying operation status, current version and committed receipt before any retry.

Successful receipts include operation ID, prior/committed versions, changed semantic field IDs, stable choice IDs and compatibility/renderer revalidation status.

## 6. Presets and deterministic randomization

`PPIA-06_PRESET_RANDOMIZATION_IMPORT_EXPORT_CONTRACT_v0.1.0.json` defines appearance, palette, head/face, wardrobe, presentation and profile-specific preset scopes.

Randomization supports all eligible, unlocked, category and bounded reroll modes. Its deterministic inputs are seed, lock set, eligible-choice-set version, appearance-state version, profile ID, Species morphology-profile version and renderer-independent choice-catalog version.

Randomization is proposal-only until accepted through the mutation protocol. It cannot invent anatomy, remove required anatomy, mutate current Form/history/equipment, access hidden/restricted content, or use renderer filenames as semantic identity.

Preset import explicitly classifies results as compatible, explicitly permitted substitution, unavailable, incompatible, missing-pack, unsupported-renderer, restricted, partially-recoverable or unknown. Silent substitution is prohibited.

## 7. Renderer and view behavior

`pixel-art-v1` remains a renderer profile rather than Character data. The customizer uses:

- fixed 3/4 full-body master view;
- switchable portrait/zoom view;
- switchable tactical-token view.

There is no arbitrary rotation or pseudo-3D orbit. A missing view/pose/asset/anchor/mask/palette/topology can make one renderer output partial or unsupported without invalidating the Character or semantic appearance state.

Presentation wardrobe uses curated visual-only assets and may cover the desired look without matching game inventory. Actual equipment preview is separately sourced from PPIA-03-authorized equipment state. Both use topology-compatible visual variants or explicit unsupported fallback; unrestricted asset warping is forbidden.

## 8. Accessibility

Every appearance state, preview delta, renderer support condition and compatibility result has a semantic nonvisual representation. Mobile/touch, keyboard-only, screen-reader, high-zoom and reduced-motion use cases retain the same authoritative choices and commit semantics.

The preview canvas is never the sole source of information. Color alone is never used to communicate state, validity, support or difference.

## 9. Reference corpus

`PPIA-06_APPEARANCE_INSPECTOR_REFERENCE_CASES_v0.1.0.json` adds **48 deterministic Inspector/Action/Reference cases** while retaining the **36 inherited Species Visual cases**, for an effective regression surface of **84 cases**.

The new cases cover every one of the 20 projection groups and all 30 governed actions, including Vespin/Moravi unusual topology, Arborae seasonal profiles, Mythragara derivation, Nekron transition guard, Suula persistent markers, Furashin phenotype and art provenance, ManyToms composite semantics, hidden-state filtering, wardrobe/equipment separation, missing renderer assets, mobile, keyboard, screen reader, stale version and duplicate-operation recovery.

These fixtures are QA artifacts, not new Species canon.

## 10. Boundary preservation

This milestone does not:

- activate application runtime or STAGE-A-A2;
- alter release/deployment/tester state;
- create paid-service or production-credential dependencies;
- transfer PPIA-05 Species/Form biology authority to PPIA-06;
- transfer PPIA-03 equipment authority to PPIA-06;
- make AI art or filenames authoritative;
- make renderer coverage a Character-validity rule;
- claim PPIA-06 completion.

After this milestone is verified and merged, the next separate PPIA-06 milestone is integrated workflow/traceability across Character Builder → Appearance Studio → profile/Form/biology changes → wardrobe/equipment projection → presets/randomization → portrait/token → reopen/recovery. Final PPIA-06 completion remains a later gate.
