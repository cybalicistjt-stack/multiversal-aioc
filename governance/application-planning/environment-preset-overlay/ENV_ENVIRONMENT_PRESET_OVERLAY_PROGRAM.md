# ENV — Environment Preset & Overlay Program

**Program ID:** ENV  
**Status:** in_progress_parallel_content_authoring  
**Completed through:** ENV-14  
**Current:** ENV-15 — Habitat Signature & Ecological Matching Contract  
**Current governed preset count:** 76  
**Current composed archetype count:** 19  
**Current concrete overlay count:** 47 (22 ENV-11 + 15 ENV-12 + 10 ENV-13)  
**Owner and final authority:** John Brandon Turner  
**Application implementation authority:** none  
**Parallel-track rule:** ENV may advance as governed content/design work while the application software roadmap continues. ENV must not mutate `Multiversal-app` runtime schemas, terrain mechanics, SCL behavior, migrations, encounter runtime, or environment UI until a separately governed application-integration tranche is authorized.

## Purpose

Convert the environment library from isolated comprehensive profiles into a reusable composition model built from:

1. **Environment Archetype** — reusable environmental structure such as River, Forest, Cave, Wetland, Urban or Transport Corridor.
2. **Environment Preset** — ready-to-use combinations such as Mangrove Swamp, Cyberpunk City, Arctic Tundra or Asteroid Field.
3. **Environment Overlay** — composable conditions such as Flood, Blizzard, Low Gravity, Radiation or Magical Saturation.
4. **Local Environment Instance** — setting/campaign-specific realization of an archetype/preset plus overlays and local content.

Historical/source profiles remain preserved as source/provenance evidence. The modular representation must not erase source text or silently reinterpret source-authored mechanics.

ENV-01 additionally establishes **Resolved Environment** as a derived read-only evaluation projection, not a fifth durable authored identity. The durable composition contract is defined in `ENV-01_ENVIRONMENT_MODEL_COMPOSITION_CONTRACT_v1.0.0.md` and `ENV-01_COMPOSITION_MODEL_v1.0.0.json`.

## Cross-program contract

Every archetype, preset and overlay must expose a machine-readable **Habitat Signature** usable by CEW creature ecology matching. Creature discovery must primarily match environmental properties, while preserving explicit source/world distribution restrictions.

ENV owns environment-side composition semantics. CEW owns creature-side habitat/distribution/ecology classification. Neither owns the other's canonical identity.

## Tranches

1. **ENV-01 — Environment Model & Composition Contract** — `completed_verified`  
   Defines archetype, preset, overlay, local-instance and resolved-environment responsibilities; field/domain ownership; immutable inheritance; provenance preservation; explicit delta semantics; compound-preset support; composition order; and non-interference boundaries.

2. **ENV-02 — Existing 40 Completeness Repair** — `completed_verified`  
   Completed missing content in the current forty promoted profiles before decomposition without fabricating absent source-backed ability links.

3. **ENV-03 — Archetype Library Extraction** — `completed_verified`  
   Extracted fifteen reusable environmental archetypes from the existing forty and identified explicit later gap-watch items instead of pre-creating speculative archetypes.

4. **ENV-04 — Overlay Taxonomy & Stacking Rules** — `completed_verified`  
   Defined twelve overlay families, compatibility/relations, intensity, deterministic stacking, effect-key deduplication and visible conflict behavior without authoring later concrete overlay libraries.

5. **ENV-05 — Existing 40 Preset Conversion** — `completed_verified`  
   Represented all forty promoted environments as governed presets through archetype composition while preserving their source profiles and completed content as immutable provenance/reference.

6. **ENV-06 — Freshwater & Wetland Expansion** — `completed_verified`  
   Added six freshwater/wetland presets and `ARCH-FLOWING-WATER`, taking the library to forty-six presets and sixteen archetypes.

7. **ENV-07 — Coastal & Marine Expansion** — `completed_verified`  
   Added six coastal/marine presets and `ARCH-AQUATIC-STRUCTURE`, taking the library to fifty-two presets and seventeen archetypes.

8. **ENV-08 — Grasslands, Open Country & Dry Landforms** — `completed_verified`  
   Added eight open-country/dry-landform presets with no new archetype, taking the library to sixty presets and seventeen archetypes.

9. **ENV-09 — Cold, Alpine & Polar Expansion** — `completed_verified`  
   Added six cold/alpine/polar presets and `ARCH-ICE-MASS`, preserving the source-backed Arctic Tundra and Taiga preset and taking the library to sixty-six presets and eighteen archetypes.

10. **ENV-10 — Settled, Industrial & Infrastructure Expansion** — `completed_verified`  
   Added Farmland/Agricultural Countryside, Suburb/Residential District, Frontier Outpost, Road/Wilderness Trail, Mine/Quarry, Factory/Refinery, Power Plant/Utility Complex, Fortress/Military Base, Transit Hub/Terminal and Harbor/Dockyards. Resolved the final ENV-03 archetype watch item with `ARCH-TRANSPORT-CORRIDOR`, taking the library to seventy-six presets and nineteen archetypes. Existing source-backed Industrial Zones, Skeletons of Highways, Port City and Flooded Suburbs remain distinct immutable presets.

11. **ENV-11 — Weather, Climate & Disaster Overlays** — `completed_verified`  
   Authored twenty-two reusable ordinary weather, active climate-state and natural-disaster overlays. All definitions follow the ENV-04 typed-delta/effect-key contract; cross-overlay relations never activate another condition automatically.

12. **ENV-12 — Planetary & Physical-Condition Overlays** — `completed_verified`  
   Authored fifteen reusable planetary/physical-condition overlays. Atmosphere composition, oxygen availability, pressure, thermal state, light, radiation and gravity remain modular environment domains. Vacuum directly owns its atmosphere/pressure deltas instead of automatically activating Low Oxygen or Low Pressure. No universal exposure, damage, pressure, radiation, gravity, equipment or adaptation formulas were invented.

13. **ENV-13 — Magical, Supernatural & Multiversal Overlays** — `completed_verified`  
   Authored ten reusable supernatural/multiversal overlays. Chaos/Foam receives a source-backed environment-context seam while exact perks and source-specific mechanics remain externally owned; no unsupported Gehenna-specific overlay was fabricated.

14. **ENV-14 — Ability, Adaptation, Creator & Full-Library Reconciliation** — `completed_verified`  
   Reconciled the complete 76-preset / 19-archetype / 47-overlay library against retained environment-ability authority. Preserved all 68 canonical Environment->Ability links unchanged; identified 177 additional environment-specific source member records as source-supported but not canonically promoted; mapped all 36 exact environment-specific source collections to the original source-backed presets; preserved the shared five-member multi-environment collection as ability-system-owned; preserved Chaos/Foam as a context seam rather than an ability bundle; and forbade ability auto-grant or canonical-link inference from archetype, overlay, Habitat Signature, property or creator similarity. The 36 post-ENV-05 expansion presets receive zero inferred ability links.

15. **ENV-15 — Habitat Signature & Ecological Matching Contract** — `selected_not_started`  
   Define environment-side habitat vocabulary including terrestrial/aquatic/aerial use, freshwater/salt/brackish water, temperature, moisture, vegetation density, substrate, elevation/depth, light, atmosphere, shelter, food/resource conditions, settlement intensity and special planar/magical properties.

16. **ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection**  
   Define the content/API contract by which a composed environment returns eligible creatures as native/common, possible, migratory/seasonal, introduced, rare, overlay-enabled or excluded while respecting World/Reality distribution, visibility and GM-only information. Application UI/runtime implementation is explicitly deferred.

## Locked model decisions through ENV-14

- durable layers are Archetype, Preset, Overlay and Local Environment Instance;
- Resolved Environment is derived/read-only and cannot become a fifth authoring truth;
- presets use one primary archetype and may use secondary component archetypes for genuinely compound environments;
- presets inherit rather than duplicate complete archetype rule bodies;
- overlays are explicit deltas, not new base environment identities;
- overlay resolution is deterministic, input-order-independent, effect-key deduplicated and never hidden last-write-wins;
- composition precedence does not supersede source/canonical authority;
- existing source profiles remain immutable provenance/evidence;
- Character, Species, Creature, Ability, Item, Vehicle, World/Reality/Place, Encounter and runtime owners remain external;
- `ARCH-FLOWING-WATER`, `ARCH-AQUATIC-STRUCTURE`, `ARCH-ICE-MASS` and `ARCH-TRANSPORT-CORRIDOR` are the only post-ENV-03 archetype extensions through ENV-14;
- ENV-11 through ENV-13 preserve **interaction is not causation**;
- atmosphere composition, oxygen availability, pressure, gravity and supernatural contexts remain modular rather than bundled hidden mechanics;
- source-specific gravity, Chaos/Foam, exposure, time, perk and participant formulas remain source/owning-system authority rather than universal ENV rules;
- exact source relationships outrank environmental similarity for ability reconciliation;
- the 68 canonical Environment->Ability links are preserved unchanged and remain distinct from 177 environment-specific source-supported member relationships that were not canonically promoted;
- source-supported-but-unpromoted relationships may remain visible with provenance but may not be silently upgraded to canonical links;
- `Special Perks (Applicable to Multiple Environments)` remain ability-system-owned and are not bulk-attached to similar presets;
- selecting a preset, archetype, overlay or local environment never grants an ability;
- archetype, overlay, property and future Habitat Signature similarity never manufacture canonical Environment->Ability authority;
- the 36 post-ENV-05 expansion presets inherit zero old ability-tree links absent explicit later source/owner authority;
- `OVL-SUP-CHAOS-FOAM` may satisfy explicit Chaos/Foam environment context for separately owned source abilities but does not grant or duplicate those abilities;
- the creator may expose canonical and source-supported relationship classes only with visible provenance and selection-is-not-acquisition semantics;
- ability/property predicates may be evaluated by their owning systems against Resolved Environment only when their own source explicitly establishes the relevant context;
- Habitat Signature exact vocabulary remains ENV-15;
- creature ecology/distribution remains CEW authority.

## Completion invariants

- existing source profiles remain preserved and attributable;
- presets are compositions, not duplicated independent rulesets;
- overlays compose deterministically and do not double-apply equivalent effects;
- custom/local environments can begin from presets and alter overlays/parameters without rewriting a full profile;
- ability relationship authority remains provenance-explicit and never inferred from similarity;
- Habitat Signature is stable enough for CEW consumption by ENV-15;
- environment-to-creature discovery distinguishes ecological suitability from canonical geographic distribution;
- no ENV tranche grants `Multiversal-app` implementation authority;
- active software-roadmap work remains independent until explicit integration is authorized.
