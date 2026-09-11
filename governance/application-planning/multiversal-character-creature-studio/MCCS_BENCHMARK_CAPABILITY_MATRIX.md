# MCCS Benchmark Capability Matrix

**Program:** MCCS — Multiversal Character & Creature Studio  
**Checked:** 2026-09-11  
**Purpose:** clean-room capability/workflow benchmark only  
**Implementation authority:** none

## Rule

The products below are references for user-visible capabilities and workflow outcomes, not implementation sources. MCCS must independently implement Multiversal-specific behavior from existing owner contracts and lawful reusable components. It must not copy proprietary source, protected art/assets, character bases, distinctive UI expression, private protocols, branded styles or sample projects.

## Benchmark products

| Product / workflow | Public source checked | Capability classes retained as requirements |
|---|---|---|
| Hero Forge | https://www.heroforge.com/ | approachable modular character assembly, immediate visual preview, part/equipment selection, pose/material/color customization and reusable character designs |
| TitanCraft | https://titancraft.com/ | modular Hero/Creature/Mech creation, scene/component composition and advanced bone-level posing suitable as a benchmark for nonhuman/custom miniature workflows |
| Reallusion Character Creator | https://www.reallusion.com/character-creator/ | deep body/face morphing, skin/hair, clothing/accessories, facial/animation rig profiles, auto-rigging, fit/skin-weight tools, LOD/optimization and broad structured interchange |
| VRoid Studio | https://vroid.com/en/studio | approachable presets/sliders, immediate real-time edits, outfit-template layering, pressure-capable direct texture painting, stroke-based hair creation and portable model export |
| Daz Studio / Genesis | https://www.daz3d.com/get_studio/ and https://www.daz3d.com/ | morph-driven figures, mix-and-match clothing/accessories/hair, clothing accommodation across body shapes, pose/render workflows, creature-capable morph combinations and large reusable content libraries |
| MakeHuman Community / MPFB | https://static.makehumancommunity.org/ | parametric human generation, rig-profile selection, IK-compatible workflows, seeded/random character generation, batch-friendly generation and Blender interoperability |
| Adobe Mixamo | https://helpx.adobe.com/creative-cloud/help/mixamo-rigging-animation.html and https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html | simple automatic humanoid rigging, skeleton mapping and animation application; its documented extra-limb/wing/tail limitations are a negative benchmark MCCS must not inherit as a universal topology assumption |
| Cascadeur | https://cascadeur.com/ and https://cascadeur.com/help/tools/animation_tools/autoposing | topology-aware posing/rigging assistance, humanoid and quadruped AutoPosing, retargeting, motion editing and physics-informed pose/motion feedback |
| Blender | https://www.blender.org/features/sculpting/ | specialist sculpting/modeling precision, brushes, dynamic topology, masking and mesh workflows; benchmark for external round-trip depth, not a requirement to recreate Blender inside MCCS |
| ZBrush | https://www.maxon.net/en/zbrush | high-detail character/creature sculpting, painting, morph/brush/layer workflows and specialist organic modeling; benchmark for expert finishing/round-trip rather than core in-app scope |

## Consolidated MCCS capability targets

### A. Approachable visual assembly

MCCS must let non-specialists build a recognizable Character/creature through presets, eligible components, sliders, palettes/materials and live preview without requiring sculpting, rigging or texture-painting expertise.

### B. Deep but bounded customization

MCCS must expose enough topology-aware morphology, head/face/sensory features, appendages, coverings, surfaces, markings, wardrobe/equipment presentation, pose and expression controls to finish ordinary Multiversal visual work in-app. Precision specialist sculpting remains an external round-trip path.

### C. Nonhumanoid-first-class support

Humanoid workflows are not the universal schema. MCCS must support multiple topology families and explicit extensions/unsupported states for unusual anatomy. A nonhuman creature cannot be forced into a humanoid rig/feature model merely because a benchmark product is humanoid-oriented.

### D. Clothing/equipment fit and projection

MCCS must project eligible wardrobe/equipment through governed fit/layer/anchor/occlusion rules, report incompatibilities, and preserve Inventory/Asset ownership authority. Visual fit is not mechanical ownership or equip state.

### E. Pose, expression and rig-aware authoring

MCCS must provide approachable topology-aware pose/posture/expression authoring and integrate rig/IK/retarget preview helpers where available. Runtime animation/action authority stays outside MCCS.

### F. Multiple outputs from one identity

Portraits, dialogue busts, tokens, paper-doll/reference views, top-down/isometric derivatives, sprites/stance sheets and future-renderer handoffs must derive from the same governed appearance source rather than becoming unrelated character definitions.

### G. Custom assets, reusable looks and variation

Creators must be able to ingest authorized custom assets through ARI, save reusable looks/outfits/style profiles, and create seeded NPC/crowd/herd/creature variants with exact provenance and independent review.

### H. Structured/open interchange and specialist round-trip

MCCS must preserve structure where formats/tools support it, report losses explicitly, and permit specialist Blender/ZBrush/DCC round-trip without making those tools blocking dependencies or allowing imported geometry to become canonical Character truth.

### I. Multiversal semantic advantage

Unlike a conventional character maker, MCCS can reference governed Character/Species/Form/equipment/relationship state while keeping presentation authority separate. The same creator workspace can therefore stay synchronized with eligible canonical facts, expose stale bindings, and produce multiple derivatives without duplicating the game-state database.

## Negative benchmark lessons

- Humanoid-only automatic rigging is insufficient for Multiversal; Mixamo's documented limitations around wings, tails and extra appendages demonstrate why topology families must be explicit.
- A large content store/catalog is useful but cannot substitute for ARI rights/provenance or reusable Multiversal source identity.
- High-end sculpt freedom is valuable but does not justify rebuilding a general DCC; bounded creator controls plus structured round-trip are the preferred local-first boundary.
- Generated/morphed appearance is not canonical Species/Form anatomy unless accepted through the owning authority.

## What is deliberately not copied

- vendor branding, proprietary character bases, meshes, art packs, sample characters or branded styles;
- exact vendor UI layouts, iconography or interaction expression;
- proprietary project formats unless publicly documented and lawfully interoperable;
- undocumented service APIs/protocols;
- vendor-specific algorithms, morph libraries or reverse-engineered generation logic.

## Acceptance implication

MCCS-21 must prove capability coverage across the consolidated targets above using original Multiversal content and Multiversal-owned contracts. Exact visual imitation of any benchmark product is not an acceptance criterion.

MCCS does not copy proprietary source, protected assets, sample projects, distinctive product-facing expression, private protocols or vendor-specific implementation details.
