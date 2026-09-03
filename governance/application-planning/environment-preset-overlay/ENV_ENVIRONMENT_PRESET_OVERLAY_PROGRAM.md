# ENV — Environment Preset & Overlay Program

**Program ID:** ENV  
**Status:** planned_parallel_content_authoring  
**Owner and final authority:** John Brandon Turner  
**Application implementation authority:** none  
**Parallel-track rule:** ENV may advance as governed content/design work while the application software roadmap continues. ENV must not mutate `Multiversal-app` runtime schemas, terrain mechanics, SCL behavior, migrations, encounter runtime, or environment UI until a separately governed application-integration tranche is authorized.

## Purpose

Convert the environment library from isolated comprehensive profiles into a reusable composition model built from:

1. **Environment Archetype** — reusable environmental structure such as River, Forest, Cave, Wetland, Urban, Grassland.
2. **Environment Preset** — ready-to-use combinations such as Mangrove Swamp, Cyberpunk City, Arctic Tundra or Asteroid Field.
3. **Overlay** — composable conditions such as Flooded, Blizzard, Low Gravity, Radiation or Magical Saturation.
4. **Local Environment Instance** — setting/campaign-specific realization of an archetype/preset plus overlays and local content.

Historical/source profiles remain preserved as source/provenance evidence. The modular representation must not erase source text or silently reinterpret source-authored mechanics.

## Cross-program contract

Every archetype, preset and overlay must expose a machine-readable **Habitat Signature** usable by CEW creature ecology matching. Creature discovery must primarily match environmental properties, while preserving explicit source/world distribution restrictions.

ENV owns environment-side composition semantics. CEW owns creature-side habitat/distribution/ecology classification. Neither owns the other's canonical identity.

## Tranches

1. **ENV-01 — Environment Model & Composition Contract**  
   Define archetype, preset, overlay and local-instance responsibilities; field ownership; provenance preservation; and composition boundaries.

2. **ENV-02 — Existing 40 Completeness Repair**  
   Complete missing content in the current forty promoted profiles before decomposition. Add missing random encounter tables to Swamps, Temperate Forest, Rainforest/Jungle, Post-Apocalyptic Overgrown City, Bustling Metropolis, Port City, Small Town/Hamlet and Nomadic Camp; add encounter/challenge material to Bustling Metropolis; add rest/shelter material to Post-Apocalyptic Overgrown City. Do not fabricate environment-ability links merely to fill absent links.

3. **ENV-03 — Archetype Library Extraction**  
   Extract reusable environmental behavior from the existing forty and identify the smallest useful archetype library without flattening meaningful differences.

4. **ENV-04 — Overlay Taxonomy & Stacking Rules**  
   Define overlay families, compatibility, exclusions, intensity/severity, stacking, temporary/persistent states, conflict precedence and double-application prevention.

5. **ENV-05 — Existing 40 Preset Conversion**  
   Represent all current promoted environments through archetype + preset + overlay composition while preserving their source profiles as provenance/reference.

6. **ENV-06 — Freshwater & Wetland Expansion**  
   Add River/Stream, Lake/Pond, Floodplain, River Delta/Estuary, Marsh/Bog/Fen and Flooded Forest coverage with reusable mechanics and overlay hooks.

7. **ENV-07 — Coastal & Marine Expansion**  
   Add Coast/Shoreline/Beach, Tidal Flats, Coral Reef, Kelp Forest, Deep Ocean/Abyssal and Ocean Trench coverage while reusing existing Open Ocean and Underwater foundations.

8. **ENV-08 — Grasslands, Open Country & Dry Landforms**  
   Add Grassland/Prairie, Savanna, Steppe, Scrubland/Chaparral, Hills/Uplands, Canyon/Badlands, Rocky Desert and Salt Flats.

9. **ENV-09 — Cold, Alpine & Polar Expansion**  
   Separate Taiga/Boreal Forest, Tundra, Alpine/High Mountain, Glacier/Icefield, Polar Ice and Sea Ice where useful; move generic cold/altitude effects toward composable overlays/properties.

10. **ENV-10 — Settled, Industrial & Infrastructure Expansion**  
    Add Farmland/Agricultural Countryside, Road/Wilderness Trail, Frontier Outpost, Mine/Quarry, Factory/Refinery, Fortress/Military Base, Transit Hub/rail-air-spaceport and related infrastructure presets.

11. **ENV-11 — Weather, Climate & Disaster Overlays**  
    Author reusable Heavy Rain/Monsoon, Fog, Thunderstorm, Blizzard/Heavy Snow, Hurricane/Cyclone, Tornado, Sandstorm/Dust Storm, Flood, Drought, Wildfire, Volcanic Ash, Avalanche/Landslide and related natural-condition overlays.

12. **ENV-12 — Planetary & Physical-Condition Overlays**  
    Author Extreme Heat/Cold, Toxic or Corrosive Atmosphere, Low Oxygen, High/Low Pressure, Radiation, extreme illumination/darkness, Low/High/Zero Gravity, Vacuum and other planetary physical-condition overlays.

13. **ENV-13 — Magical, Supernatural & Multiversal Overlays**  
    Author Magical Saturation, Magical Dead Zone, Reality Instability, Dimensional Bleed, Portal Activity, Psychic Influence, Corruption, Temporal Instability, Chaos/Foam Influence, Dream Influence and appropriate Gehenna-related conditions. Reconcile source-backed Chaos/Foam environment ability material without inventing unsupported facts.

14. **ENV-14 — Ability, Adaptation, Creator & Full-Library Reconciliation**  
    Reconcile environment-linked abilities/adaptations against properties where source authority permits; preserve exact source relationships otherwise. Validate the complete preset/overlay library and environment-creator composition contract.

15. **ENV-15 — Habitat Signature & Ecological Matching Contract**  
    Define environment-side habitat vocabulary including terrestrial/aquatic/aerial use, freshwater/salt/brackish water, temperature, moisture, vegetation density, substrate, elevation/depth, light, atmosphere, shelter, food/resource conditions, settlement intensity and special planar/magical properties. Define how overlays alter suitability without duplicating creature taxonomy.

16. **ENV-16 — Environment Creature-Discovery Contract & GM Preset Projection**  
    Define the content/API contract by which a composed environment returns eligible creatures as native/common, possible, migratory/seasonal, introduced, rare, overlay-enabled or excluded while respecting World/Reality distribution, visibility and GM-only information. Application UI/runtime implementation is explicitly deferred.

## Completion invariants

- existing source profiles remain preserved and attributable;
- current promoted environment content is completed before modular conversion;
- presets are compositions, not duplicated independent rulesets;
- overlays compose deterministically and do not double-apply equivalent effects;
- custom/local environments can begin from presets and alter overlays/parameters without rewriting a full profile;
- Habitat Signature is stable enough for CEW consumption;
- environment-to-creature discovery distinguishes ecological suitability from canonical geographic distribution;
- no ENV tranche grants `Multiversal-app` implementation authority;
- active software-roadmap work, including SCL terrain/zone authority, remains independent until explicit integration is authorized.
