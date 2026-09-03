# ENV-06 — Freshwater & Wetland Expansion Report

**Program:** ENV — Environment Preset & Overlay  
**Tranche:** ENV-06  
**Status:** validation candidate  
**Application implementation authority:** none

## Result candidate

ENV-06 adds six authored freshwater/wetland preset identities:

1. River / Stream
2. Lake / Pond
3. Floodplain
4. River Delta / Estuary
5. Marsh / Bog / Fen
6. Flooded Forest

All six use the ENV-01 composition model and ENV-04 overlay-family hooks. They are authored expansion content, not recovered text from the forty historical environment profiles.

## Archetype decision

ENV-03 left flowing-water/channel behavior as an explicit gap watch item for ENV-06. ENV-06 resolves that question by adding exactly one structural archetype: `ARCH-FLOWING-WATER`.

The new archetype is justified because river/stream play has reusable behavior that neither `ARCH-OPEN-WATER` nor `ARCH-WETLAND` owns cleanly:

- directional current with upstream/downstream asymmetry;
- a channel bed and banks;
- longitudinal corridor travel versus cross-current crossing;
- bank access and egress;
- fords, choke points and crossings;
- rapids, bars, snags and other channel obstacles.

No other ENV-06 environment requires another archetype:

- Lake/Pond reuses `ARCH-OPEN-WATER`;
- Floodplain composes `ARCH-WETLAND + ARCH-OPEN-COUNTRY + ARCH-FLOWING-WATER`;
- River Delta/Estuary composes `ARCH-FLOWING-WATER + ARCH-WETLAND + ARCH-COASTAL`;
- Marsh/Bog/Fen parameterizes `ARCH-WETLAND`;
- Flooded Forest composes `ARCH-FOREST + ARCH-WETLAND`.

The composed archetype library therefore moves from 15 to **16** reusable archetypes rather than proliferating one archetype per new preset.

## Preset-content contract

Each new preset contains:

- overview;
- environmental features;
- movement/navigation guidance;
- hazards;
- encounters/challenges;
- rest/shelter guidance;
- d12 random encounter table.

The content is modular: it describes distinguishing preset behavior and uses inherited archetype semantics rather than duplicating the historical comprehensive-profile model.

## Environment distinctions preserved

### Floodplain versus Flood overlay

Floodplain is geography shaped by recurring inundation and can be used when no active flood exists. An exceptional current flood remains later overlay/runtime state. This prevents `Floodplain` and `Flood` from becoming synonyms.

### Flooded Forest versus flooded ordinary forest

Flooded Forest assumes recurrent/persistent waterlogging is part of the forest's ordinary baseline. Applying an exceptional flood to an ordinary forest remains a separate composition.

### Delta/Estuary versus ENV-07 marine work

ENV-06 establishes branching river-mouth channels, sediment/wetland structure and freshwater-to-brackish transition. Detailed tidal flats, marine ecology, surf/coastal behavior and other marine-specific refinement remain ENV-07.

### Marsh/Bog/Fen

These are retained as variants under one preset family because their differences can be expressed as wetland water-source, substrate, nutrient and vegetation parameters without duplicating the Wetland archetype.

## Overlay boundary

ENV-06 records only ENV-04 overlay **family** hooks. It does not author executable Heavy Rain, Flood, Extreme Cold, Toxic Water, Magical Saturation or other concrete overlay identities. Those remain in ENV-11/12/13.

## Creature/ecology boundary

Random encounter content uses environmental events and generic ecological-role cues only. ENV-06 does not establish canonical creature identities, native ranges, rarity or World distribution. CEW owns that work. Exact Habitat Signature vocabulary remains ENV-15.

## Parallel software boundary

ENV-06 creates content/design/provenance authority only. It does not modify or authorize changes to:

- `Multiversal-app`;
- SCL terrain or strategic-position behavior;
- runtime schemas or migrations;
- encounter runtime;
- creature picker/runtime distribution;
- environment UI.

The active software roadmap remains independently governed.
