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

## Owner boundaries locked

- Character/NPC/Creature and Species/Form owners retain identity, topology eligibility, Form/state, mechanics and live state.
- CAPP/PPIA retain renderer-neutral appearance authority and compilation semantics.
- PAPT/PCA retain reusable character-asset, rig, garment, motion, image/sprite, style-generation and local-production primitives.
- ARI/PCA retain generic resource identity, rights/provenance, derivative lineage, version/review and import/export infrastructure.
- MNCS retains NPC/creature/group/population identity and progressive construction. MCCS may only provide visual-variation recipes and presentation outputs for owner-supplied entities/groups.
- Animation/Scene/Combat/Dialogue owners retain runtime pose/action/placement authority.
- Packet 07 retains generic preview/dry-run/commit/explanation/recovery semantics; MCCS supplies appearance-domain lenses and operations.
- P3D remains deferred and separate.

## Fold decisions

- `MCCS-01 + MCCS-02 → MCCS-01`: workspace, renderer-neutral projection, draft overlay, stale-owner detection, rebase/refresh and authority dispositions are one document/workspace kernel.
- `MCCS-03 + MCCS-04 + MCCS-08 → MCCS-03`: topology, morphology/proportion/silhouette and modular appendage/anatomy compatibility share one topology-aware component/parameter kernel.
- `MCCS-05` stays distinct: face/sensory/expression anatomy has different topology specialization and preview/accessibility behavior.
- `MCCS-06 + MCCS-07 → MCCS-06`: coverings and color/material/pattern/marking use one layered surface/material substrate.
- `MCCS-09 + MCCS-10 → MCCS-09`: wardrobe/equipment fit and accessory/prop/linked-being presentation use one composition/attachment/layering shell.
- `MCCS-11 + MCCS-12 → MCCS-11`: pose/expression and rig/anchor/IK/retarget preview are one pose/rig preview kernel.
- `MCCS-13 + MCCS-14 + MCCS-15 → MCCS-13`: portraits/cards, tactical derivatives and sprite/stance outputs are renderer/output profiles over one appearance workspace.
- `MCCS-16` remains and absorbs the visual-only residual of historical `MCCS-17`: style/templates/renderer profiles and deterministic visual-variant recipes share configuration/seeded-variation infrastructure. MNCS owns population/group identity; PCA owns generic recipe/generation substrate.
- `MCCS-18` remains: multi-Form/lifecycle/transformation appearance inheritance/staleness is a distinct adapter over owner Form/state truth.
- `MCCS-19 + MCCS-20 → MCCS-19`: appearance interchange, external round-trip, cross-renderer serialization and future-P3D handoff are one interchange contract; ARI/PCA retain generic provenance/version/review.
- `MCCS-21` remains as final golden proof.

## Reduced surviving order

`MCCS-01 → MCCS-03 → MCCS-05 → MCCS-06 → MCCS-09 → MCCS-11 → MCCS-13 → MCCS-16 → MCCS-18 → MCCS-19 → MCCS-21`

## Golden vectors

The reduced family preserves these 48 proof vectors:

1. Humanoid Character opens from owner projection without copying Character truth.
2. Quadruped opens with topology-appropriate controls and no forced humanoid mapping.
3. Serpentine being exposes unsupported humanoid-only controls rather than inventing equivalents.
4. Winged/multi-limbed topology validates anchors and appendages.
5. Construct/modular body uses modular anatomy without implying biological Species facts.
6. Owner-version change marks an appearance draft stale.
7. Rebase preserves compatible manual presentation overrides.
8. Rebase reports conflicts instead of silently discarding edits.
9. Draft appearance mutation does not change canonical Species/Form truth.
10. Morphology slider never mutates mechanical size unless an owner operation separately does so.
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
44. Generic review/version/provenance actions resolve to ARI/PCA rather than a second MCCS ledger.
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

## DAG / OPS3 reconciliation

Historical `MCCS-02` was a live MNCS rotation/start milestone. Because reduced `MCCS-01` absorbs the entire historical `MCCS-02` renderer-neutral projection/draft-overlay contract, the reduction performs an **atomic equivalent gate rewrite**:

- `MNCS.program_edges.start_requires`: `MCCS-02` → `MCCS-01`;
- `milestone_gates.rotation[MNCS-01]`: `MCCS-02` → `MCCS-01`;
- parallel execution map: MNCS may start from reduced `MCCS-01` plus its unchanged MIB-09/DPL prerequisites.

This is a gate-equivalence repair, not earlier activation: reduced `MCCS-01` includes all capability previously promised by `MCCS-02`. `MCCS-21` remains the MNCS golden-proof dependency. PDCP grants no product implementation authority and does not mutate `operations/CURRENT.json`.
