# ENV — Environment Preset & Overlay Program

**Program ID:** ENV  
**Status:** in_progress_parallel_content_authoring  
**Completed through:** ENV-13  
**Current:** ENV-14 — Ability, Adaptation, Creator & Full-Library Reconciliation  
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
   Authored fifteen reusable overlays: Extreme Heat, Extreme Cold, Toxic Atmosphere, Corrosive Atmosphere, Low Oxygen, High Pressure, Low Pressure, Radiation, Extreme Darkness, Extreme Illumination/Glare, Low Gravity, High Gravity, Zero Gravity, Variable/Directional Gravity and Vacuum. Atmosphere composition, oxygen availability, pressure, thermal state, light, radiation and gravity remain modular environment domains. Vacuum directly owns its atmosphere/pressure deltas instead of automatically activating Low Oxygen or Low Pressure. The four gravity conditions share one explicit gravity-regime resolution seam. No universal exposure, damage, pressure, radiation, gravity, equipment or adaptation formulas were invented. No presets or archetypes were added.

13. **ENV-13 — Magical, Supernatural & Multiversal Overlays** — `completed_verified`  
   Authored ten reusable overlays: Magical Saturation, Magical Dead Zone, Reality Instability, Dimensional Bleed, Portal Activity, Psychic Influence, Corruption, Temporal Instability, Chaos/Foam Influence and Dream Influence. All use the ENV-04 typed-delta/effect-key resolver and preserve interaction-is-not-causation. Magical regimes remain environment context rather than spell-resolution rules; reality instability, dimensional bleed and portal activity remain distinct conditions; psychic, corruption and dream influence do not automatically impose participant states; and temporal instability has no universal time-conversion formula. Chaos/Foam receives a source-backed environment-context seam from the retained Environment-Based Abilities/Chaos sources while its exact perks, checks, exposure rules, time ratio, mutation/adaptation mechanics and other source-specific formulas remain for ENV-14 or their owning systems. No Gehenna-specific overlay is fabricated because retained authority establishes Gehenna as a Branch identity, not a reusable environmental condition. No presets or archetypes were added.

14. **ENV-14 — Ability, Adaptation, Creator & Full-Library Reconciliation** — `selected_not_started`  
   Reconcile environment-linked abilities/adaptations against properties where source authority permits; preserve exact source relationships otherwise. Validate the complete preset/overlay library and environment-creator composition contract.

15. **ENV-15 — Habitat Signature & Ecological Matching Contract**  
   Define environment-side habitat vocabulary including terrestrial/aquatic/aerial use, freshwater/salt/brackish water, temperature, moisture, vegetation density, substrate, elevation/depth, light, atmosphere, shelter, food/resource conditions, settlement intensity and special planar/magical properties.

16. **ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection**  
   Define the content/API contract by which a composed environment returns eligible creatures as native/common, possible, migratory/seasonal, introduced, rare, overlay-enabled or excluded while respecting World/Reality distribution, visibility and GM-only information. Application UI/runtime implementation is explicitly deferred.

## Locked model decisions through ENV-13

- durable layers are Archetype, Preset, Overlay and Local Environment Instance;
- Resolved Environment is derived/read-only and cannot become a fifth authoring truth;
- presets use one primary archetype and may use secondary component archetypes for genuinely compound environments;
- presets inherit rather than duplicate complete archetype rule bodies;
- overlays are explicit deltas, not new base environment identities;
- overlay resolution is deterministic, input-order-independent, effect-key deduplicated and never hidden last-write-wins;
- composition precedence does not supersede source/canonical authority;
- existing source profiles remain immutable provenance/evidence;
- Character, Species, Creature, Ability, Item, Vehicle, World/Reality/Place, Encounter and runtime owners remain external;
- `ARCH-FLOWING-WATER`, `ARCH-AQUATIC-STRUCTURE`, `ARCH-ICE-MASS` and `ARCH-TRANSPORT-CORRIDOR` are the only post-ENV-03 archetype extensions through ENV-13;
- ENV-11 concrete overlays preserve **interaction is not causation**: relations only resolve conditions already active in materially overlapping scopes;
- ENV-12 keeps atmosphere composition, oxygen availability and pressure as separate facts rather than collapsing them into a single hostile-atmosphere flag;
- Vacuum directly supplies its atmosphere and pressure deltas and may supersede duplicate Low Oxygen/Low Pressure contributions without auto-activating them;
- Low Gravity, High Gravity, Zero Gravity and Variable/Directional Gravity share `gravity.regime` and `movement.gravity_context`, preventing accidental numeric stacking of incompatible regimes;
- Zero Gravity does not imply Vacuum and Vacuum does not imply Zero Gravity;
- Extreme Heat/Cold do not automatically activate ENV-11 Wildfire, Snow or Blizzard conditions;
- Radiation does not automatically generate mutations, abilities, creature variants or universal dose mechanics;
- source-specific gravity-shift dice, timing, saves, multipliers and event tables remain source/local authority rather than universal ENV-12 rules;
- ENV-12 authors no universal participant, equipment, damage, exposure, pressure, radiation, gravity or adaptation formulas;
- ENV-13 defines ten concrete `OVF-SUPERNATURAL` overlays and preserves the same interaction-is-not-causation resolver rule;
- Magical Saturation and Magical Dead Zone describe ambient environmental regimes only and do not themselves grant, suppress, modify or resolve spells, powers or items;
- Reality Instability, Dimensional Bleed and Portal Activity remain separate identities: none automatically creates another, and portal endpoint/route truth remains externally owned;
- Psychic Influence, Corruption and Dream Influence are environmental contexts and do not automatically impose mental conditions, mutation, possession, alignment, sleep, hallucination or reality manifestation;
- Temporal Instability has no universal time-conversion ratio, aging rule, loop rule or travel formula;
- Chaos/Foam Influence is a source-backed environmental context seam, while exact source perk/adaptation relationships and source-specific mechanics remain ENV-14/owning-system authority;
- no Gehenna-specific overlay is promoted absent source/owner authority for a concrete composable environmental condition; Gehenna remains World/Reality/Branch identity/access authority;
- World/Reality/Branch identity and portal endpoint authority remain external to ENV overlays;
- ability/adaptation reconciliation remains ENV-14;
- Habitat Signature exact vocabulary remains ENV-15;
- creature ecology/distribution remains CEW authority.

## Completion invariants

- existing source profiles remain preserved and attributable;
- presets are compositions, not duplicated independent rulesets;
- overlays compose deterministically and do not double-apply equivalent effects;
- custom/local environments can begin from presets and alter overlays/parameters without rewriting a full profile;
- Habitat Signature is stable enough for CEW consumption by ENV-15;
- environment-to-creature discovery distinguishes ecological suitability from canonical geographic distribution;
- no ENV tranche grants `Multiversal-app` implementation authority;
- active software-roadmap work remains independent until explicit integration is authorized.
