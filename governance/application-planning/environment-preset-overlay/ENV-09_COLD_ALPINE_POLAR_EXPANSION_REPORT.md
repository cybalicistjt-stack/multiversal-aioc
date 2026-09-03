# ENV-09 — Cold, Alpine & Polar Expansion Report

## Result

ENV-09 adds six owner-authorized modular presets: Taiga / Boreal Forest, Tundra, Alpine / High Mountain, Glacier / Icefield, Polar Ice, and Sea Ice.

The existing source-backed `Arctic Tundra and Taiga` preset is preserved unchanged as historical/source provenance. ENV-09 does not delete or rewrite it; the six new presets provide the current modular coverage needed by the ENV architecture.

The governed preset count becomes **66**: 40 ENV-05 source-backed presets + 6 ENV-06 + 6 ENV-07 + 8 ENV-08 + 6 ENV-09.

## Archetype decision

ENV-03 left `ice/glacier traversal behavior` as an explicit watch item. ENV-09 resolves it by adding exactly one archetype: `ARCH-ICE-MASS` — Persistent Ice / Cryosphere.

This promotion is justified because glaciers, polar ice and sea ice share intrinsic substrate behavior not adequately supplied by Open Country or Highland alone: load-bearing frozen surface/mass, fracture and crevasse/lead formation, melt channels/pools, unstable edges, pressure ridges/hummocks, and slow movement or deformation of the substrate itself.

No separate Taiga, Tundra, Alpine, Glacier, Polar or Sea-Ice archetypes are created. Taiga reuses Forest, Tundra reuses Open Country, Alpine reuses Highland, Glacier composes Ice Mass + Highland, Polar Ice composes Ice Mass + Open Country, and Sea Ice composes Ice Mass + Open Water.

The composed archetype count therefore becomes **18**.

## Preset versus overlay boundaries

The following distinctions are locked:

- **Taiga / Boreal Forest does not imply Extreme Cold, Heavy Snow or Blizzard.** It is a forest preset that can receive those conditions.
- **Tundra does not imply permanent snow cover or an active Extreme Cold overlay.** It is treeless exposed open country with seasonally variable surface state.
- **Alpine / High Mountain does not imply snow, ice, low oxygen or avalanche.** Highland structure is baseline; those are later physical/weather conditions.
- **Glacier / Icefield is distinct from temporarily frozen Highland terrain.** Persistent ice-mass topology is baseline; Extreme Cold and Blizzard remain overlays.
- **Polar Ice does not hard-code prolonged darkness, perpetual daylight or whiteout.** Those are light/weather/local conditions.
- **Sea Ice is distinct from a temporary Freeze/Frozen-Water overlay on ordinary Open Water.** The preset represents an environment where persistent or seasonally dominant marine ice is the baseline navigable structure.
- **Active Avalanche, Whiteout, Blizzard, Extreme Cold, Low Oxygen and unusual Pressure are not authored here.** Weather/disaster content remains ENV-11 and planetary/physical-condition content remains ENV-12.

## Source and provenance boundary

The existing `Arctic Tundra and Taiga` source-backed preset remains immutable. Its source trait note already identified `compound profile split deferred to ENV-09`; ENV-09 fulfills that downstream refinement without asserting that the new authored text was present in the source profile.

## Creature and habitat boundary

No canonical creature identities, ranges, mounts, familiars, pets/companions or NPC relationships are authored by ENV-09. Encounter content uses generic ecological signs or roles. CEW owns creature ecology/distribution and relationship crosswalks. Habitat Signature vocabulary remains ENV-15.

## Application boundary

ENV-09 grants no `Multiversal-app`, SCL, runtime, migration, encounter-runtime or environment-UI implementation authority. It remains parallel governed content-authoring work.
