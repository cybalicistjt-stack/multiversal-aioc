# ENV-10 — Settled, Industrial & Infrastructure Expansion Report

## Result

ENV-10 adds ten modular presets: Farmland / Agricultural Countryside, Suburb / Residential District, Frontier Outpost, Road / Wilderness Trail, Mine / Quarry, Factory / Refinery, Power Plant / Utility Complex, Fortress / Military Base, Transit Hub / Terminal, and Harbor / Dockyards.

The governed preset count becomes **76**: 40 ENV-05 source-backed presets + 6 ENV-06 + 6 ENV-07 + 8 ENV-08 + 6 ENV-09 + 10 ENV-10.

## Archetype decision

ENV-03 left `road/trail corridor behavior` as an explicit watch item. ENV-10 resolves it by adding exactly one archetype: `ARCH-TRANSPORT-CORRIDOR`.

The archetype is justified because roads and trails share reusable linear-route behavior not cleanly supplied by surrounding terrain or by the heavier `ARCH-INFRASTRUCTURE`: continuity, junctions/forks, crossings and gates, shoulders/clearance, route-surface condition, chokepoints and route markers. It does not own vehicle rules, traffic law, bridge-object mechanics or active disaster conditions.

No separate Farmland, Suburb, Mine, Factory, Utility, Fortress, Terminal or Harbor archetypes are created. Existing Open Country, Settlement, Urban, Infrastructure, Built Complex, Subterranean, Highland and Coastal semantics compose those presets.

The composed archetype count therefore becomes **19**.

## Preset boundaries

The following distinctions are locked:

- **Farmland / Agricultural Countryside is not Grassland/Prairie.** It is deliberately cultivated and managed land, although it may reuse Open Country structure.
- **Suburb / Residential District is not the existing Flooded Suburbs source preset.** Flooded Suburbs remains an immutable source-backed post-apocalyptic/flooded preset; the new preset provides ordinary residential coverage.
- **Road / Wilderness Trail is not Skeletons of Highways.** The source-backed Highway Skeletons preset remains a ruined post-apocalyptic transport environment; the new corridor preset is generic and functional.
- **Mine / Quarry is not Caves and Caverns.** Extraction topology and engineered access are baseline; natural cave behavior may coexist only where applicable.
- **Factory / Refinery and Power Plant / Utility Complex remain distinct from generic Industrial Zones.** The source-backed Industrial Zones preset remains preserved, while ENV-10 supplies narrower reusable site presets.
- **Harbor / Dockyards is not Port City.** Port City is a broader urban/coastal settlement identity; Harbor/Dockyards is an active waterfront logistics facility that can exist inside or outside a city.
- **Fortress / Military Base does not imply an active siege.** Siege/bombardment remains external encounter/runtime or later condition authority.
- **Transit Hub / Terminal does not imply a particular technology level.** Rail, road, air and space variants share interchange behavior while vehicle rules remain externally owned.

## Overlay boundaries

ENV-10 authors no executable weather, disaster, physical-condition or supernatural overlays. Flood, Wildfire, Landslide, Blackout/Systems Failure, Toxic Release, Radiation, Severe Storm and related active conditions remain ENV-11/12/13 or externally governed event/runtime states as appropriate. Registry overlay-family hints are nonexecuting composition hooks only.

## Source and provenance boundary

Existing source-backed presets including Industrial Zones, Skeletons of Highways, Port City, Flooded Suburbs, Small Town or Hamlet, Nomadic Camp, Underground Bunker Network and other ENV-05 identities remain immutable. ENV-10 expansion prose is authored content and is never represented as recovered source text.

## Creature and habitat boundary

ENV-10 creates no canonical creature identities, ranges, mounts, familiars, pets/companions or NPC relationships. CEW owns those mappings. Habitat Signature vocabulary remains ENV-15.

## Application boundary

ENV-10 grants no `Multiversal-app`, SCL, runtime, migration, encounter-runtime, vehicle, settlement-management or environment-UI implementation authority. It remains parallel governed content-authoring work.
