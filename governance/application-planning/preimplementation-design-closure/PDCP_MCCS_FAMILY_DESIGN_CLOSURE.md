# PDCP — MCCS Family Design Closure

**Project:** PDCP — Preimplementation Design Closure Project  
**Family:** MCCS — Multiversal Character & Creature Studio  
**Status:** design_closed_for_family_reduction  
**Implementation authority:** none  
**Baseline:** 21 tranches  
**Reduced implementation/proof shape:** 11 tranches  
**Capability loss detected:** no

## Closure decision

MCCS remains the creator-facing **appearance/presentation authoring and derivative-output studio** over existing Character/NPC/Creature, Species/Form, CAPP/PPIA, PAPT/PCA and ARI authority. It is not a second entity database, Form state machine, population generator, asset-governance engine, animation runtime or general-purpose DCC application.

The reduction preserves distinct implementation kernels where creator interaction or technical risk materially differs, while folding seams that shared one authoring/rendering substrate and returning generic infrastructure to its existing owner.

## Owner boundaries locked

- Character/NPC/Creature and Species/Form owners retain identity, body topology eligibility, Form/state, mechanics and live state.
- CAPP/PPIA retain renderer-neutral appearance authority and appearance compilation semantics.
- PAPT/PCA retain reusable character-asset, rig, garment, motion, style-generation, image/sprite production and local-production primitives.
- ARI/PCA retain generic resource identity, rights/provenance, derivative lineage, version/review and import/export infrastructure.
- MNCS retains NPC/creature identity, population/group composition and progressive NPC/creature generation; MCCS may only provide visual-variation recipes and presentation outputs for those entities/groups.
- Animation/Scene/Combat/Dialog owners retain runtime pose/action/placement authority.
- Packet 07 retains generic preview/dry-run/commit/explanation/recovery semantics; MCCS supplies appearance-domain lenses and operations.
- P3D remains deferred and separate. MCCS may emit a future-renderer handoff package but cannot activate P3D or make physical-renderer fields canonical Character truth.

## Intra-family folding

### MCCS-01 absorbs MCCS-02
Creator workspace, renderer-neutral projection, draft overlay, stale-owner detection, rebase/refresh and authority dispositions are one document/workspace implementation shell.

### MCCS-03 absorbs MCCS-04 and MCCS-08
Topology family, morphology/proportion/silhouette and modular appendage/anatomy compatibility use one topology-aware component/parameter validation kernel. Face/sensory authoring remains separate because it has distinct topology specialization, expression anatomy and accessibility/preview behavior.

### MCCS-06 absorbs MCCS-07
Hair/fur/feather/scale/shell/skin coverings and color/material/pattern/marking layers share the same layered surface/material authoring substrate.

### MCCS-09 absorbs MCCS-10
Wardrobe/armor/equipment fit and accessory/prop/mount/familiar/companion composition share the same presentation-composition, attachment, layering and linked-entity visualization shell. Canonical ownership/relationships stay external.

### MCCS-11 absorbs MCCS-12
Pose/posture/gesture/expression authoring and rig/anchor/IK/retarget preview are one pose/rig preview kernel. This remains presentation-only and does not become animation-runtime authority.

### MCCS-13 absorbs MCCS-14 and MCCS-15
Portrait/bust/reference-card, token/paper-doll/top-down/isometric and sprite/stance/animation-sheet outputs are derivative render profiles over one appearance workspace. Output-profile differences remain adapters, not separate semantic engines.

### MCCS-16 absorbs the MCCS-specific residual from MCCS-17
Style packs/templates/renderer profiles and deterministic **visual** variant recipes share configuration, seeded variation and profile application infrastructure. NPC/crowd/herd/population identity/composition is MNCS-owned; MCCS only varies presentation within owner-supplied eligibility/ranges.

### MCCS-18 remains
Multi-Form, lifecycle and transformation appearance inheritance/staleness is a distinct adapter over owner Form/state truth and cannot be safely hidden inside generic style switching.

### MCCS-19 absorbs MCCS-20
Appearance-package interchange, external-specialist round-trip, cross-renderer serialization and P3D/future-renderer handoff are one interchange contract. Generic review/provenance/version rights remain ARI/PCA; MCCS owns appearance-specific mapping/loss reporting.

### MCCS-21 remains
The final golden proof retains all cross-output, topology, multi-Form, accessibility, provenance, offline/local-first and owner-boundary obligations.

## Reduced surviving tranches

1. `MCCS-01` — Creator Workspace, Renderer-Neutral Projection, Draft/Rebase & Authority Contract
2. `MCCS-03` — Topology, Morphology, Silhouette, Appendage & Modular Anatomy Authoring
3. `MCCS-05` — Head, Face, Sensory Feature & Expression Anatomy Authoring
4. `MCCS-06` — Coverings, Color, Material, Pattern, Marking & Surface-Layer Studio
5. `MCCS-09` — Wardrobe, Equipment Fit, Accessories, Props & Linked-Being Presentation Composition
6. `MCCS-11` — Pose, Gesture, Expression, Rig, Anchor, IK & Retarget Preview
7. `MCCS-13` — Multi-Profile Derivative Rendering: Portrait/Token/Paper-Doll/Top-Down/Isometric/Sprite/Stance
8. `MCCS-16` — Style Packs, Templates, Renderer Profiles & Visual Variant Recipes
9. `MCCS-18` — Multi-Form, Transformation, Lifecycle & Appearance-State Management
10. `MCCS-19` — Appearance Interchange, Round-Trip, Cross-Renderer & Future-P3D Handoff
11. `MCCS-21` — Golden Character & Creature Capability / Semantic-Integration Proof

## Cross-family absorptions

Historical `MCCS-17` no longer owns NPC/crowd/herd/creature population generation. MNCS owns identity/group/population construction; PCA owns generic procedural-generation substrate. `MCCS-16` retains only deterministic visual-variation recipes over owner-supplied populations and eligibility.

Historical `MCCS-19` no longer implies a generic provenance/version/review/import-export platform. ARI/PCA own that infrastructure. `MCCS-19` retains appearance-schema mapping, round-trip loss reporting, renderer-package serialization and future-renderer handoff.

Generic mesh/image/rig/texture/codec/DCC primitives remain lawful replaceable local tools/libraries or PCA/PAPT capabilities rather than MCCS implementations.

## Golden vectors

The reduced family must preserve at least these 48 proof vectors:

1. Humanoid Character opens from owner projection without copying Character truth.
2. Quadruped opens with topology-appropriate controls and no forced humanoid mapping.
3. Serpentine being exposes unsupported humanoid-only controls rather than inventing equivalents.
4. Winged/multi-limbed topology validates anchors and appendages.
5. Construct/modular body uses modular anatomy without implying biological Species facts.
6. Owner-version change marks an appearance draft stale.
7. Rebase preserves compatible manual presentation overrides.
8. Rebase reports conflicts instead of silently discarding edits.
9. Draft appearance mutation does not change canonical Species/Form truth.
10. Morphology slider never mutates mechanical size unless owner operation separately does so.
11. Face/sensory authoring supports nonhuman head plans.
12. Expression preview does not become canonical emotional state.
13. Covering layers support hair/fur/feathers/scales/shell with renderer capability reporting.
14. Material/pattern/marking edits preserve ARI provenance for imported/generated textures.
15. Required semantic state has non-color-only representation.
16. Equipment projection reflects owner equipment state without changing ownership.
17. Appearance-only outfit remains presentation-only.
18. Accessory/prop composition does not imply Inventory ownership.
19. Mount/familiar/pet/companion presentation preserves separate canonical identities.
20. Pose authoring remains presentation unless runtime owner explicitly projects state.
21. IK/contact preview reports incompatibility instead of silently deforming canon.
22. Retarget preview records source/target profile and limitations.
23. Portrait output derives from the same workspace as token output.
24. Token output cannot mutate map collision/scale truth.
25. Paper-doll/inventory derivative cannot mutate equipped state.
26. Top-down/isometric derivative retains renderer/profile provenance.
27. Sprite/stance output cannot invent missing Actions or animation availability.
28. Stale source appearance invalidates/reflags affected derivatives.
29. Style-profile switch preserves identity-defining appearance semantics.
30. Visual preset/template is configuration, not a new entity definition.
31. Seeded visual variation is reproducible where determinism is claimed.
32. Visual crowd/herd variants do not create demographic/population truth.
33. MNCS group member IDs remain authoritative when MCCS renders group variation.
34. Multi-Form entity keeps one entity identity with form-specific appearance states.
35. Form transition preview does not mutate the owning Form state machine.
36. Lifecycle-stage appearance inheritance preserves owner stage truth.
37. Disguise/presentation identity cannot overwrite hidden canonical identity.
38. Structured appearance export reports unsupported semantics/loss.
39. Reimport round-trip preserves supported appearance semantics and provenance.
40. External specialist asset import remains candidate/presentation material until accepted.
41. ARI rights/use restrictions are enforced before derivative publication/export.
42. Cross-renderer handoff distinguishes required semantics from optional renderer hints.
43. P3D handoff does not activate P3D or require printable geometry.
44. Generic review/version/provenance actions resolve to ARI/PCA owners rather than a second MCCS ledger.
45. Blocking authoring works with paid/cloud providers disabled.
46. Keyboard/touch/screen-reader equivalents exist for essential creator operations.
47. Undo/recovery restores creator draft state without deleting canonical owner history.
48. Golden suite proves cross-output consistency for humanoid, nonhuman, animal, companion, monster, crowd/herd variant, multi-Form and constructed/modular cases.

## Residual implementation mapping

- PCA/PAPT: production primitives, renderer/tool adapters and local processing substrate.
- CAPP/PPIA: renderer-neutral appearance authority and compilation.
- ARI/PCA: generic rights, provenance, versioning, review and import/export infrastructure.
- MNCS: NPC/creature/group/population identity and composition.
- MCCS survivors: entity-centric creator UX, appearance-domain validation/adapters, derivative profiles, visual variation, appearance-state adapters and final proof.

## DAG / OPS3

`MCCS-01` and `MCCS-21` survive with equivalent-or-stronger milestone semantics. No DAG change is required for this family reduction. PDCP grants no implementation authority and does not mutate `operations/CURRENT.json`.
