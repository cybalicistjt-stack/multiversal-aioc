# Appearance & Identity Creator Research — Xbox Labs, Infinity Nikki, Dance of Theseus
Date: 2026-10-19 | Status: **owner-approved research and design proposal; NOT implementation certified**
Lane: OPS5 on-demand `research-evaluation`; no persistent lane selected or altered.

## Purpose
Evaluate three external approaches and convert verified mechanics into Multiversal-specific, testable proposals. The owner approved all five research directions on 2026-10-19. This package completes the **first evidence-and-specification pass**, not application implementation, cross-platform acceptance, or new game canon.

## Package
1. [01 — Competitive research and verified gaps](01_RESEARCH_GAP_AUDIT.md)
2. [02 — Appearance composition and portability](02_COMPOSITION_INTEROPERABILITY.md)
3. [03 — Modular anatomy and social presentation](03_MODULAR_ANATOMY_SOCIAL.md)
4. [04 — Fashion preview UX](04_FASHION_PREVIEW_UX.md)
5. [05 — Executable-style acceptance roadmap](05_ACCEPTANCE_ROADMAP.md)
6. [Draft example recipe](appearance-recipe.example.json) — demonstration data, NOT production schema or imported game object.

## Existing Multiversal authority must remain intact
- FGA-PARAM-1 (15 garment parameters); FGA-02 fit; FGA-03 primitive demand; FGA-05 clothing-reference review.
- FDE-01..07 and FDE-GOLDEN-1: **completed_verified**. No replacement fashion editor.
- CAS/CASI/CAPP/PPIA/MCCS: Species/Form and appearance ownership, nonhumanoid topology, skin/face/profile/preset, equipment projection, three presentation profiles.
- CAS-WARD-001: presentation wardrobe only. FGA must not mutate anatomy, equipment truth, inventory or mechanics.
- CAPP-07 / PPIA-06 already propose profile and import/export controls. This study does **not** rediscover those features as missing.
- GPR/PCV-03F and MTLC-14 remain independently active; their selectors and state are untouched.
- World/environment, actions/abilities, equipment/augmentation, social rules and GM/Player authority remain with their owners.
- No public sharing, marketplace, paid AI provider, reverse-engineered commercial game assets, or unauthorized deployment is introduced here.

## Proposed design order (not an OPS5 selector)
UX-01 evidence/scene-context preview → COMP-01 cross-owner appearance recipe/import review → FORM-01 body modification proposal seam → SOC-01 GM-authored social presentation challenge → PORT-01 portable creator interfaces and AI-assisted proposals. The first two are the highest value; later slices must preserve proof of the earlier boundary.

## Release of research vs software
The deliverables are descriptive and executable-style examples. Each item in 05 lists an owner-source verification, focused mock/deterministic proof, independent integration proof and negative authority tests required before a future application implementation may be called complete. No acceptance badge should be inferred from this research PR.

## Sources
- Xbox Wire, "Introducing XBOX Labs" (2026-10-13): https://news.xbox.com/en-us/2026/10/13/introducing-xbox-labs/
- Infinity Nikki, official DIY Workshop/Glow Up feature guide (2025-04-28): https://infinitynikki.infoldgames.com/en/news/170
- Infinity Nikki, version 2.8 official clothing changes (2026): https://infinitynikki.infoldgames.com/en/news/560
- Infinity Nikki, version 2.9 notes: https://infinitynikki.infoldgames.com/en/news/583
- Citreat Studio, Dance of Theseus demo (2026-08-10): https://store.steampowered.com/app/4136020/Dance_of_Theseus_Demo/
- Citreat Studio September developer update: https://steamcommunity.com/app/3581260
- Multiversal source: `governance/application-planning/fashion-design-engine/FDE_FASHION_DESIGN_ENGINE_PROGRAM.md`
- Multiversal source: `governance/application-planning/fashion-garment-authority/FGA_PARAMETER_AUTHORITY_v0.1.0.md`
- Multiversal source: `governance/application-planning/parallel-preimplementation/PPIA-06_APPEARANCE_STUDIO_CONTROL_SURFACE_v0.1.0.json`
- Multiversal source: `governance/application-planning/character-appearance-production/CAPP-07_APPEARANCE_STUDIO_IMPLEMENTATION_SPEC_v0.1.0.json`
- App repo files: `apps/client-ui/src/fde/Fde01FashionDesignWorkspace.tsx`, `Fde03VisualGarmentPreview.tsx`, `Fde04DesignRepository.ts`, `Fde07ProductGoldenProof.ts` (inspected at the time of this proposal).
