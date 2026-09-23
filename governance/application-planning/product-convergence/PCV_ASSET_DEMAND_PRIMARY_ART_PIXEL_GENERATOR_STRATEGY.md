# PCV Asset Demand, Primary-Art & Onboard Pixel Generator Strategy

**Owner amendment:** 2026-09-23  
**Applies to:** PCV-01 through PCV-10

## Purpose

Use the current Multiversal product/engine implementation to determine what media the real app actually requires, then minimize hand-authored artwork by generating compatible pixel-style derivatives from a compact governed set of primary assets.

This is not a return to old-Bible asset assumptions. The live product surface, later convergence work, current UISK presentation system, MAI/AAI interoperability, and post-Bible feature families determine current demand.

## Asset Demand Ledger

PCV-01 must produce a machine-readable ledger. Each row records at least:

- stable asset-need ID;
- owning product feature/screen/runtime;
- asset family;
- semantic role;
- required dimensions/view/density;
- morphology or topology family where applicable;
- animation/pose requirements;
- variation dimensions;
- generation mode;
- required primary asset IDs;
- compatible substitution rules;
- palette/material parameters;
- provenance/license requirements;
- mobile/desktop use;
- fallback/placeholder policy;
- golden-path blocking state;
- implementation state.

### Asset families

1. character/player/NPC visuals;
2. creature/animal/monster/entity visuals;
3. portraits/tokens/badges;
4. clothing/armor/weapons/tools/equipment;
5. consumables/materials/currency/loot/item icons;
6. terrain/floors/walls/roads/water/vegetation/environment tiles;
7. structures/doors/furniture/props/facilities/base/vehicle parts;
8. maps/scenes/placeables/overlays;
9. spell/power/effect/hazard/weather/status animation;
10. UI/skin ornament and specialty-surface imagery;
11. audio/music/ambience/one-shots/voice where required;
12. 3D/specialty media where a current feature truly needs it.

## Pixel-art generation modes

- **primary-authored** — hand/generated-and-reviewed source art that defines style/silhouette;
- **palette-parametric** — semantic indexed regions recolored from Character Designer or object parameters;
- **layer-composited** — body/head/hair/clothing/armor/equipment/marking/effect layers assembled by manifest;
- **template-morphed** — discrete approved morphology/proportion variants using authored anchors/templates; no arbitrary scaling that destroys pixel readability;
- **procedural** — deterministic tiles, patterns, markings, simple icons, gradients/noise/material fills or effect particles generated from governed recipes;
- **imported-permitted** — rights/provenance-approved external asset through MAI/AAI or other owner system;
- **fallback/placeholder** — intentionally designed presentation, not an accidental missing box;
- **unresolved** — visible debt; prohibited on PCV-10 golden path.

## Onboard Pixel Generator

The generator is a deterministic presentation subsystem, not gameplay authority.

A generated visual specification should include:

- primary-pack/version;
- morphology template;
- body/proportion variant;
- viewpoint/direction;
- animation/pose;
- semantic palette;
- skin/fur/scale/material parameters;
- facial/head/hair feature IDs;
- markings/scars/tattoos/pattern IDs;
- clothing/armor layer IDs;
- held/equipped item layer IDs;
- accessory/ornament IDs;
- status/effect overlay IDs;
- deterministic seed where procedural variation is used.

The same spec must produce the same output across Android and Windows for the same renderer/version.

### Character Designer binding

Character Designer owns user visual choices but not rule truth. Changing a supported presentation field updates the generated sprite/portrait/token immediately. Rule-owned changes such as equipped armor may propose or select presentation layers through existing ownership rules.

### Primary-art philosophy

Do not create one source sprite for every combination. Invest art effort in:

- silhouettes;
- clean anatomy/morphology templates;
- animation key poses;
- layerable equipment shapes;
- expressive heads/hair/features;
- semantic palette/mask quality;
- readable item/prop silhouettes;
- tile/terrain edge grammar;
- effects with strong visual language.

Use those primaries to create the combinatorial breadth.

### Creature/entity extension

Later PCV work extends the same system through morphology families rather than species-by-species duplication. Expected families include humanoid/bipedal, quadruped, serpentine, avian/winged, aquatic, arthropod/multi-limbed, plant/fungal, construct, amorphous/ooze and swarm/collective where the live creature corpus requires them. Exact families/counts come from the Asset Demand Ledger, not from this planning document.

### Item/world extension

Items should prefer primary silhouettes + material/palette/condition/quality variants where legibility permits. Environment art should prefer tileset/autotile/prop grammars and MAI-compatible composition over unique flattened images for every scene.

## Provenance

Every primary retains source, license, checksum and version. Every generated derivative records its generator version and primary references. Generated pixels do not create world/gameplay truth and do not erase the rights/provenance of their primaries.

## Performance and storage

Generation must be usable offline on Android and Windows. Prefer deterministic 2D composition/palette operations suitable for Canvas/WebGL/WASM or equivalent local rendering. Cache derivatives by visual-spec hash and invalidate only when primary/generator versions change.

Do not make on-device ML inference a dependency for ordinary rendering.

## PCV gates

- PCV-01: Asset Demand Ledger exists and is derived from current live product needs.
- PCV-02: first onboard generator + governed primary character pack works in real Character Designer and survives restart.
- PCV-04..07: extend primary/generator families alongside the gameplay verticals that consume them.
- PCV-08: converge stranded MAI/AAI/generator/import/source tooling.
- PCV-09: finish presentation integration and eliminate accidental blank/generic surfaces.
- PCV-10: no unresolved asset need remains on the representative first-party two-human golden path.
