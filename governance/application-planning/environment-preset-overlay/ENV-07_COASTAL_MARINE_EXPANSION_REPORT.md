# ENV-07 — Coastal & Marine Expansion Report

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-07  
**Authority:** owner-authorized new content architecture and preset content  
**Application implementation authority:** none

## Result

ENV-07 adds six modular coastal/marine presets:

1. Coast / Shoreline / Beach
2. Tidal Flats
3. Coral Reef
4. Kelp Forest
5. Deep Ocean / Abyssal
6. Ocean Trench

Together with ENV-05 and ENV-06, the governed preset count becomes **52**.

## Archetype decision

ENV-03 left `reef/kelp dense aquatic structure` as an explicit gap watch item. ENV-07 resolves that question with **one** new reusable archetype: `ARCH-AQUATIC-STRUCTURE`.

The new archetype is justified because reef and kelp environments share persistent three-dimensional structure that affects route choice, line-of-sight, concealment, collision/entanglement exposure, vertical layering and shelter geometry. `ARCH-SUBMERGED` supplies the underwater medium but not dense internal structure. Reusing terrestrial `ARCH-FOREST` would incorrectly mix land and marine semantics.

No other ENV-07 archetype promotion is warranted:

- Coast / Shoreline / Beach uses `ARCH-COASTAL + ARCH-OPEN-COUNTRY`.
- Tidal Flats uses `ARCH-COASTAL + ARCH-WETLAND`.
- Coral Reef uses `ARCH-AQUATIC-STRUCTURE + ARCH-SUBMERGED`.
- Kelp Forest uses `ARCH-AQUATIC-STRUCTURE + ARCH-SUBMERGED`.
- Deep Ocean / Abyssal uses `ARCH-SUBMERGED`.
- Ocean Trench uses `ARCH-SUBMERGED` with trench topography as preset/local parameterization rather than inventing a trench archetype.

The composed archetype count therefore becomes **17**.

## Preset versus overlay boundaries

ENV-07 intentionally distinguishes stable environmental structure from variable conditions:

- **Tidal Flats versus a high-tide/flood condition:** the preset establishes intertidal terrain; exact tide timing, water rise and storm surge remain hydrology/weather/local authority.
- **Deep Ocean versus Extreme Pressure:** depth and isolation define the preset; pressure severity is deferred to ENV-12.
- **Abyssal darkness:** deep-water presentation anticipates limited light, but the governed extreme-darkness condition remains ENV-12 rather than being hard-coded as universal mechanics.
- **Coral Reef/Kelp Forest versus severe current or storm:** dense structure is baseline; current/storm severity remains ENV-11/12/local authority.
- **Ocean Trench versus geologic disaster:** trench topography is stable preset structure; earthquakes, vent hazards, eruptions or landslides require later geologic/local authority.

ENV-07 does not author executable Tide, Storm Surge, Hurricane, Extreme Pressure, Extreme Cold, Darkness, Toxic Water, Magical Saturation or other concrete overlays. Overlay-family hints remain nonexecuting pointers into ENV-11/12/13.

## ENV-06 delta/estuary handoff

ENV-06 established River Delta / Estuary as `ARCH-FLOWING-WATER + ARCH-WETLAND + ARCH-COASTAL` and explicitly deferred detailed marine/tidal treatment. ENV-07 closes that handoff by defining adjacent coast, tidal-flat and marine structured/open-depth presets. River Delta / Estuary remains its own freshwater/brackish river-mouth preset; it is not replaced by Tidal Flats or Coast.

## Content completeness

Each of the six presets contains:

- Overview
- Environmental features
- Movement and navigation
- Hazards
- Encounters and challenges
- Rest and shelter
- Random encounters (d12)

Encounter tables use ecological roles, signs and environmental events instead of inventing canonical creature identities. CEW retains creature identity/distribution authority.

## Deferred work remains intact

- ENV-08 retains grasslands/open-country/dry-landform expansion.
- ENV-09 retains ice/glacier archetype evaluation and cold/polar presets.
- ENV-10 retains road/trail archetype evaluation and infrastructure expansion.
- ENV-11 retains weather/climate/disaster overlay definitions.
- ENV-12 retains pressure, thermal, darkness, gravity, atmosphere and other planetary/physical-condition overlays.
- ENV-13 retains magical/supernatural/multiversal overlays.
- ENV-15 retains exact Habitat Signature vocabulary.
- ENV-16 retains the GM environment-to-creature discovery projection.
- CEW retains creature identity, ecology and geographic/world distribution.

## Non-interference

ENV-07 changes only governed content/design/provenance material and its control-plane validation. It grants no authority to mutate `Multiversal-app`, SCL runtime, terrain mechanics, migrations, encounter runtime, creature runtime, environment UI, mount/pet/familiar systems or NPC behavior.
