# ENV — Environment Preset & Overlay Program

**Program ID:** ENV  
**Status:** in_progress_parallel_content_authoring  
**Completed through:** ENV-09  
**Current:** ENV-10 — Settled, Industrial & Infrastructure Expansion  
**Current governed preset count:** 66  
**Current composed archetype count:** 18  
**Owner and final authority:** John Brandon Turner  
**Application implementation authority:** none  
**Parallel-track rule:** ENV may advance as governed content/design work while the application software roadmap continues. ENV must not mutate `Multiversal-app` runtime schemas, terrain mechanics, SCL behavior, migrations, encounter runtime, or environment UI until a separately governed application-integration tranche is authorized.

## Purpose

Convert the environment library from isolated comprehensive profiles into a reusable composition model built from:

1. **Environment Archetype** — reusable environmental structure such as River, Forest, Cave, Wetland, Urban, Grassland.
2. **Environment Preset** — ready-to-use combinations such as Mangrove Swamp, Cyberpunk City, Arctic Tundra or Asteroid Field.
3. **Environment Overlay** — composable conditions such as Flooded, Blizzard, Low Gravity, Radiation or Magical Saturation.
4. **Local Environment Instance** — setting/campaign-specific realization of an archetype/preset plus overlays and local content.

Historical/source profiles remain preserved as source/provenance evidence. The modular representation must not erase source text or silently reinterpret source-authored mechanics.

ENV-01 additionally establishes **Resolved Environment** as a derived read-only evaluation projection, not a fifth durable authored identity. The durable composition contract is defined in `ENV-01_ENVIRONMENT_MODEL_COMPOSITION_CONTRACT_v1.0.0.md` and `ENV-01_COMPOSITION_MODEL_v1.0.0.json`.

## Cross-program contract

Every archetype, preset and overlay must expose a machine-readable **Habitat Signature** usable by CEW creature ecology matching. Creature discovery must primarily match environmental properties, while preserving explicit source/world distribution restrictions.

ENV owns environment-side composition semantics. CEW owns creature-side habitat/distribution/ecology classification. Neither owns the other's canonical identity.

## Tranches

1. **ENV-01 — Environment Model & Composition Contract** — `completed_verified`  
   Defines archetype, preset, overlay, local-instance and resolved-environment responsibilities; field/domain ownership; immutable inheritance; provenance preservation; explicit delta semantics; compound-preset support; composition order; and non-interference boundaries. Detailed overlay conflict/stacking remains ENV-04 and Habitat Signature vocabulary remains ENV-15.

2. **ENV-02 — Existing 40 Completeness Repair** — `completed_verified`  
   Completed missing content in the current forty promoted profiles before decomposition. Source-backed ability links were not fabricated merely to fill absent links.

3. **ENV-03 — Archetype Library Extraction** — `completed_verified`  
   Extracted fifteen reusable environmental archetypes from the existing forty and identified explicit later gap-watch items instead of pre-creating speculative archetypes.

4. **ENV-04 — Overlay Taxonomy & Stacking Rules** — `completed_verified`  
   Defined twelve overlay families, compatibility/relations, intensity, deterministic stacking, effect-key deduplication and visible conflict behavior without authoring later concrete overlay libraries.

5. **ENV-05 — Existing 40 Preset Conversion** — `completed_verified`  
   Represented all forty promoted environments as governed presets through archetype composition while preserving their source profiles and completed content as immutable provenance/reference.

6. **ENV-06 — Freshwater & Wetland Expansion** — `completed_verified`  
   Added River/Stream, Lake/Pond, Floodplain, River Delta/Estuary, Marsh/Bog/Fen and Flooded Forest coverage. Resolved the flowing-water gap with `ARCH-FLOWING-WATER`, taking the composed archetype count to sixteen and the preset count to forty-six.

7. **ENV-07 — Coastal & Marine Expansion** — `completed_verified`  
   Added Coast/Shoreline/Beach, Tidal Flats, Coral Reef, Kelp Forest, Deep Ocean/Abyssal and Ocean Trench. Resolved the reef/kelp structural gap with `ARCH-AQUATIC-STRUCTURE`, taking the composed archetype count to seventeen and the preset count to fifty-two. River Delta/Estuary remains a distinct ENV-06 river-mouth preset.

8. **ENV-08 — Grasslands, Open Country & Dry Landforms** — `completed_verified`  
   Added Grassland/Prairie, Savanna, Steppe, Scrubland/Chaparral, Hills/Uplands, Canyon/Badlands, Rocky Desert and Salt Flats. No new archetype was justified; Open Country and Highland cover the reusable structure while vegetation, substrate and aridity remain preset/overlay dimensions. The preset count became sixty and the composed archetype count remained seventeen.

9. **ENV-09 — Cold, Alpine & Polar Expansion** — `completed_verified`  
   Added Taiga/Boreal Forest, Tundra, Alpine/High Mountain, Glacier/Icefield, Polar Ice and Sea Ice while preserving the source-backed Arctic Tundra and Taiga preset. Resolved the ENV-03 ice/glacier watch item with `ARCH-ICE-MASS`, taking the governed preset count to sixty-six and the composed archetype count to eighteen. Generic cold, Blizzard/Whiteout, Active Avalanche and Low Oxygen remain later overlay authority.

10. **ENV-10 — Settled, Industrial & Infrastructure Expansion** — `selected_not_started`  
    Add Farmland/Agricultural Countryside, Road/Wilderness Trail, Frontier Outpost, Mine/Quarry, Factory/Refinery, Fortress/Military Base, Transit Hub/rail-air-spaceport and related infrastructure presets; resolve the ENV-03 road/trail corridor watch item.

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

## Locked model decisions through ENV-09

- durable layers are Archetype, Preset, Overlay and Local Environment Instance;
- Resolved Environment is derived/read-only and cannot become a fifth authoring truth;
- presets use one primary archetype and may use secondary component archetypes for genuinely compound environments;
- presets inherit rather than duplicate complete archetype rule bodies;
- overlays are explicit deltas, not new base environment identities;
- overlay resolution is deterministic, input-order-independent, effect-key deduplicated and never hidden last-write-wins;
- composition order is archetype baseline(s) → preset parameterization → local instance configuration → active overlays → current runtime state → external participant evaluation;
- composition precedence does not supersede source/canonical authority;
- existing source profiles remain immutable provenance/evidence;
- Character, Species, Creature, Ability, Item, Vehicle, World/Reality/Place, Encounter and runtime owners remain external;
- `ARCH-FLOWING-WATER` is the sole ENV-06 archetype extension because channelized directional flow is not cleanly represented by Open Water Surface or Wetland;
- `ARCH-AQUATIC-STRUCTURE` is the sole ENV-07 archetype extension because reef and kelp environments share reusable dense three-dimensional underwater structure not supplied by Submerged alone;
- ENV-08 adds no archetype: Grassland, Savanna, Steppe, Scrubland and Salt Flats reuse Open Country, while Hills, Canyon/Badlands and Rocky Desert compose Highland where relief matters;
- `ARCH-ICE-MASS` is the sole ENV-09 archetype extension because persistent glacier, polar and sea-ice environments share fracture, crevasse/lead, melt-feature, unstable-edge and slow substrate-movement behavior that Open Country/Highland do not own;
- Taiga reuses Forest, Tundra reuses Open Country and Alpine reuses Highland rather than becoming new archetypes;
- the existing source-backed Arctic Tundra and Taiga preset remains immutable provenance even after the modular ENV-09 split;
- Glacier/Icefield is distinct from temporarily frozen Highland; Sea Ice is distinct from temporarily frozen Open Water;
- Extreme Cold, Blizzard/Whiteout, Active Avalanche, Low Oxygen and unusual pressure/light states remain ENV-11/12 conditions, not implicit universal mechanics of cold presets;
- Floodplain geography is distinct from an active Flood overlay;
- Flooded Forest baseline is distinct from temporarily flooding an ordinary forest;
- River Delta/Estuary remains distinct from Coast and Tidal Flats;
- Tidal Flats terrain is distinct from a temporary high-tide/flood state;
- Deep Ocean/Abyssal and Ocean Trench do not hard-code universal pressure, darkness or temperature mechanics;
- Grassland/Prairie, Savanna, Steppe and Scrubland do not hard-code Wildfire, Drought, Extreme Heat, Dust Storm or other later overlays;
- Rocky Desert remains distinct from the existing Sandy Desert because rock/gravel/broken relief and dunes/loose sand are different preset structures;
- Salt Flats do not universally imply caustic chemistry, extreme temperatures or supernatural mirage effects;
- Habitat Signature has a stable envelope but exact vocabulary remains deferred to ENV-15.

## Completion invariants

- existing source profiles remain preserved and attributable;
- current promoted environment content is completed before modular conversion;
- presets are compositions, not duplicated independent rulesets;
- overlays compose deterministically and do not double-apply equivalent effects;
- custom/local environments can begin from presets and alter overlays/parameters without rewriting a full profile;
- Habitat Signature is stable enough for CEW consumption by ENV-15;
- environment-to-creature discovery distinguishes ecological suitability from canonical geographic distribution;
- no ENV tranche grants `Multiversal-app` implementation authority;
- active software-roadmap work, including SCL terrain/zone authority, remains independent until explicit integration is authorized.
