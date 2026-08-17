# CCTI-08 — Context and Compatibility Signal Baseline

**Mode:** read-only; no normalized context/taxonomy values adopted.

## Item corpus preview reproduced from current source fields

The raw Item-corpus Genre surface reproduces the Item v0.12.0 preparation preview exactly:

- **63** rows carry exact `All Genres` source signal;
- **5,060** rows carry a more specific Genre source signal;
- **266** rows have no Genre field/value available in their source catalog surface.

The 63 exact `All Genres` rows are distributed as 38 Items, 10 EVA Suits, 10 Symbiotes/Cybernetics and 5 Melee Weapons. `All Genres` remains a source compatibility signal, not a normalized genre taxonomy value.

This is independent confirmation that the current 5,389-row Item corpus and the later Item preparation preview refer to the same row body.

## Platform context signals

All 5,628 Vehicle/Mecha/Spacecraft catalog rows carry non-empty Genre values in the retained master catalogs. Additional populated context surfaces include:

- Vehicles: `Domain`, `Tech_Magic_Tier`, `Environment`, `Terrain_Water_Weather`.
- Mecha: `Technology_Style`, `Tier`, `Operating_Environment`, `Compatible_Frame_or_Class`.
- Spacecraft: `Technology_Style`, `Tier`, `Environment_or_Operating_Theater`, `Compatible_Scale_or_Class`.

Mecha exposes 49 distinct raw `Manufacturer_or_Culture` values; Spacecraft exposes 94. These are raw current-catalog values and remain evidence to be mapped through the prepared creator/catalog system rather than treated as already-normalized creator identities.

## Required semantic separation

Later CCTI projection must preserve the prepared distinction:

- intrinsic properties/requirements describe what the object is or requires;
- affinity describes contexts the object strongly evokes;
- compatibility is evaluated from requirements + setting/profile + governed exceptions;
- compatibility does not mean common, legal, cheap, available, or narratively important.

No final compatibility determination is made in this baseline. Complete registry-backed mapping requires the exact checksum-verified Item/Platform preparation archives and the shared context vocabulary.
