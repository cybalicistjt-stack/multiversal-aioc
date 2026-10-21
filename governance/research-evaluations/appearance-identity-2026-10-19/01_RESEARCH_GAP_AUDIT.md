# 01 — External findings and evidence-graded FDE gap audit

## Evidence grades
- **E1 official confirmed:** official developer/publisher wording or actual repository source.
- **E2 scoped code observation:** feature present/absent in the explicitly inspected module; *not* an assertion about the entire application.
- **H hypothesis:** useful extrapolation; no independently verified behavior.
- **P proposed:** Multiversal-specific design; no production implementation proven.

## Xbox Labs — opportunities and limits
**E1:** Xbox's 2026-10-13 announcement describes a small experimental group exploring platform translation/recompilation, WebAssembly/WebGPU browser access, remixing, game preservation and player creation. It is an initiative, not a published general-purpose Multiversal-ready SDK. Source: https://news.xbox.com/en-us/2026/10/13/introducing-xbox-labs/
- P: build **portable, renderer-neutral creation recipes** and browser-accessible tools; keep platform transport separate from game data/authority.
- P: AI may suggest draft choices and flag mismatches, but canonical semantics use deterministic validation and user/GM review.
- Rejected: assuming an Xbox Labs API, porting their game code, ingesting third-party proprietary assets, claiming Windows/macOS/web compatibility without independent runtime testing.
- Watch only: actual SDK/source drop, supported platforms, legal/asset use policy, performance/security proof, cost. No procurement commitment.

## Infinity Nikki — independently documented mechanics
**E1, official April 2025 guide:** outfit and hair dyeing, glossiness, garment patterns including opacity/density, effect recoloring for eligible outfits, saved/shared/imported color schemes. https://infinitynikki.infoldgames.com/en/news/170
**E1, official v2.8:** scene preview at current location, camera/presentation direction adjustments and four lighting conditions; effect visibility toggle; styling scheme import for ability outfits; explicit unavailable-piece notices; specialized mount-mode styling with incompatibility fallback. https://infinitynikki.infoldgames.com/en/news/560
**E1, official v2.9:** ability hand-held presentation color may differ during actual ability use, evidence that preview fidelity/ability mode limitations must be disclosed. https://infinitynikki.infoldgames.com/en/news/583
- P: add bounded lighting/background contexts; show effect toggles with preview-vs-runtime honesty; package editable appearance schemes as portable recipes referencing existing FDE/CAPP systems; warn about unavailable assets/unsupported topology before proposing changes.
- Rejected: importing Nikki garments/assets; equating rarity with gameplay power; introducing hidden paid dye resources.

## Dance of Theseus — demo-confirmed mechanics
**E1, Steam demo:** craft body parts and blueprints, gather resources, match color/texture of interchangeable body parts for combos, turn-based ballroom judging, social/romance progression; playable demonstration is about five in-game days / one hour. https://store.steampowered.com/app/4136020/Dance_of_Theseus_Demo/
**E1, developer update:** planned wings/tails/halos and mineral/liquid/fiber/aether textures are **future prospects** as described, not established playable demo features. Their prior monolithic Spine-outfit and manually generated thumbnail workflow created maintainability/bloat problems. https://steamcommunity.com/app/3581260
- P: modular form/augmentation proposals, component-based rig/anchor targets, precomputed coverage/fail-closed behavior; GM-authored social presentation challenges.
- Rejected: appearance editor silently installing functional limbs/abilities or replacing Species/Form state; copying its dance scoring or asset-organization pitfalls.
- No claim that Multiversal requires ballroom minigames or romance loops.

## Existing Multiversal capability, not a gap
| Area | Observed source and assessment |
|---|---|
| 15 garment construction parameters | FGA-PARAM-1, already defined; reuse |
| Fit for difficult nonhuman topologies | FGA-02/FGA-06 and FDE-07, sealed proof; preserve |
| Designer controls/catalog | `Fde02DesignerControls.tsx` and FDE-02 complete; preserve |
| Multi-view full-body/portrait/token | `Fga04FashionDesignStudio.tsx` and `Fde03VisualGarmentPreview.tsx` confirm available controls |
| Persistent garment designs / versioning / duplicate / import review | `Fde04DesignRepository.ts` and FDE-04; extend only if necessary |
| Appearance-specific preset/export and nonhumanoid inspectability | PPIA-06 and CAPP-07 already specify these, so **do not rebuild a preset system without first verifying runtime support** |
| Actual equipment vs cosmetic garment separation | FGA-PARAM-1, CAS-WARD-001, CAPP-07; hard boundary |
| Local/provider-off editing | FDE-07 proof; baseline |

## Candidate deltas — validate before calling them missing
| Candidate | Observed narrow source | Unresolved investigation |
|---|---|---|
| Background and four-condition lighting | `Fde03VisualGarmentPreview.tsx` renders a semantic SVG/avatar with three profile views; no scene-context selector in that file | Audit shared renderer / scene runtime for reusable non-gameplay lighting projection before implementing |
| Effect visibility and ability style association | FDE workspace inspected has no such control | Check ability, spell and equipment owner contracts; no visual state changes to action outcomes |
| Cross-owner portable composite recipes | FDE-04 garment export exists; CAPP-07 appearance presets already specified | Determine whether integration/import pipeline already composes both before defining new envelope |
| Functional limb and augmentation creation | PPIA-06 controls are source-bounded; wardrobe cannot alter body | Find actual Species/Form, augments and injury/rehabilitation contracts; propose to owning systems |
| Social presentation evaluation | existing social system & app NoncombatRuntime render social scenes | Verify rules authority/scoring and prevent invented universal bonuses |
| Optional AI suggestion workflow | FGA-05 accepts reviewed clothing-photo proposals | Extend a proposal pathway, not a new AI canonical editor |

## Non-functional risks
1. **Combinatorial explosion:** 25 species x forms x clothing variants x presentations x environments. Compute reusable components and capability fingerprints, not a unique asset per combination.
2. **Data authority:** appearance must not grant inventory, stats, magic effects, equipped items, new form or GM-visible secrets.
3. **Fidelity:** state is still valid when image assets are unsupported; report coverage and diagnostics visibly.
4. **Import safety:** no arbitrary URLs, executable SVG scripts, HTML, remote fetches, or opaque provider prompts in portable recipe.
5. **IP/licensing:** evaluate upstream license/terms independently before using third-party code or assets; reuse conceptual lessons only.
6. **Accessibility and cost:** keyboard, screen reader, reduced motion, color-vision safety, provider-off baseline, no unapproved external inference.

## Priority decision
High: context previews (bounded visual states) and cross-owner recipe compatibility.
Medium: conditional visual effects/ability cosmetics; modular form proposal design; GM-authored social challenge.
Later: social creator ecosystem, public sharing/monetization and optional provider-assisted synthesis.

This research is **not a field/playtest performance claim**.
