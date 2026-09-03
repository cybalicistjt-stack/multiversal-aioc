# ENV — Environment Preset & Overlay Program

**Program ID:** ENV  
**Status:** in_progress_parallel_content_authoring  
**Completed through:** ENV-11  
**Current:** ENV-12 — Planetary & Physical-Condition Overlays  
**Current governed preset count:** 76  
**Current composed archetype count:** 19  
**Current concrete ENV-11 overlay count:** 22  
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
   Authored twenty-two reusable ordinary weather, active climate-state and natural-disaster overlays: Heavy Rain, Monsoon Regime, Fog, Thunderstorm, Heavy Snow, Blizzard, Windstorm/Gale, Hurricane/Cyclone, Tornado, Sandstorm/Dust Storm, Hailstorm, Flood, Flash Flood, Drought, Storm Surge, Tsunami/Seiche, Wildfire, Volcanic Ash, Volcanic Eruption, Earthquake, Avalanche and Landslide/Mudslide. All definitions follow the ENV-04 required typed-delta/effect-key contract. Cross-overlay relations never activate another condition automatically; both overlays must already be active in overlapping scopes. No presets or archetypes were added, so the library remains seventy-six presets and nineteen archetypes.

12. **ENV-12 — Planetary & Physical-Condition Overlays** — `selected_not_started`  
   Author Extreme Heat/Cold, Toxic or Corrosive Atmosphere, Low Oxygen, High/Low Pressure, Radiation, extreme illumination/darkness, Low/High/Zero Gravity, Vacuum and other planetary physical-condition overlays.

13. **ENV-13 — Magical, Supernatural & Multiversal Overlays**  
   Author Magical Saturation, Magical Dead Zone, Reality Instability, Dimensional Bleed, Portal Activity, Psychic Influence, Corruption, Temporal Instability, Chaos/Foam Influence, Dream Influence and appropriate Gehenna-related conditions. Reconcile source-backed Chaos/Foam environment ability material without inventing unsupported facts.

14. **ENV-14 — Ability, Adaptation, Creator & Full-Library Reconciliation**  
   Reconcile environment-linked abilities/adaptations against properties where source authority permits; preserve exact source relationships otherwise. Validate the complete preset/overlay library and environment-creator composition contract.

15. **ENV-15 — Habitat Signature & Ecological Matching Contract**  
   Define environment-side habitat vocabulary including terrestrial/aquatic/aerial use, freshwater/salt/brackish water, temperature, moisture, vegetation density, substrate, elevation/depth, light, atmosphere, shelter, food/resource conditions, settlement intensity and special planar/magical properties.

16. **ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection**  
   Define the content/API contract by which a composed environment returns eligible creatures as native/common, possible, migratory/seasonal, introduced, rare, overlay-enabled or excluded while respecting World/Reality distribution, visibility and GM-only information. Application UI/runtime implementation is explicitly deferred.

## Locked model decisions through ENV-11

- durable layers are Archetype, Preset, Overlay and Local Environment Instance;
- Resolved Environment is derived/read-only and cannot become a fifth authoring truth;
- presets use one primary archetype and may use secondary component archetypes for genuinely compound environments;
- presets inherit rather than duplicate complete archetype rule bodies;
- overlays are explicit deltas, not new base environment identities;
- overlay resolution is deterministic, input-order-independent, effect-key deduplicated and never hidden last-write-wins;
- composition precedence does not supersede source/canonical authority;
- existing source profiles remain immutable provenance/evidence;
- Character, Species, Creature, Ability, Item, Vehicle, World/Reality/Place, Encounter and runtime owners remain external;
- `ARCH-FLOWING-WATER` is the sole ENV-06 archetype extension;
- `ARCH-AQUATIC-STRUCTURE` is the sole ENV-07 archetype extension;
- ENV-08 adds no archetype because Open Country and Highland already cover the reusable structure;
- `ARCH-ICE-MASS` is the sole ENV-09 archetype extension;
- `ARCH-TRANSPORT-CORRIDOR` is the sole ENV-10 archetype extension because generic roads/trails share linear continuity, junction, crossing, shoulder/clearance, route-condition and chokepoint behavior not cleanly owned by heavy Industrial & Infrastructure;
- Farmland is distinct from unmanaged Grassland/Prairie;
- ordinary Suburb/Residential District is distinct from the existing Flooded Suburbs source preset;
- Road/Wilderness Trail is distinct from source-backed Skeletons of Highways;
- Factory/Refinery and Power Plant/Utility Complex are narrower reusable site presets distinct from generic Industrial Zones;
- Harbor/Dockyards is a waterfront logistics facility distinct from the broader Port City settlement identity;
- Fortress/Military Base does not imply an active siege;
- Transit Hub/Terminal remains technology-neutral at the preset level and does not own vehicle mechanics;
- ENV-11 concrete overlays conform to the ENV-04 required definition and typed-delta contract and use stable effect keys for deduplication;
- **interaction is not causation**: Heavy Rain does not auto-create Flood, Drought does not auto-create Wildfire, Earthquake does not auto-create Landslide/Tsunami, Hurricane does not auto-create Storm Surge/Tornado, Volcanic Eruption does not auto-create a separate Volcanic Ash activation, and Blizzard does not auto-create Avalanche;
- explicit `amplifies`, `dampens`, `supersedes` and `transforms_with` relations apply only when the referenced conditions are already active in materially overlapping scopes;
- ENV-11 authors no universal damage, movement, endurance, structural, exposure, weather-generation or disaster-simulation formulas;
- Extreme Heat/Cold, Low Oxygen, pressure, toxic/corrosive atmosphere, Radiation, illumination extremes, altered Gravity and Vacuum remain ENV-12 authority;
- magical, supernatural and Multiversal conditions remain ENV-13 authority;
- Habitat Signature has a stable envelope but exact vocabulary remains deferred to ENV-15.

## Completion invariants

- existing source profiles remain preserved and attributable;
- presets are compositions, not duplicated independent rulesets;
- overlays compose deterministically and do not double-apply equivalent effects;
- custom/local environments can begin from presets and alter overlays/parameters without rewriting a full profile;
- Habitat Signature is stable enough for CEW consumption by ENV-15;
- environment-to-creature discovery distinguishes ecological suitability from canonical geographic distribution;
- no ENV tranche grants `Multiversal-app` implementation authority;
- active software-roadmap work remains independent until explicit integration is authorized.
