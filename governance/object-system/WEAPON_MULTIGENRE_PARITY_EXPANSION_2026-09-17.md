# Weapon Multigenre Parity Expansion — 2026-09-17

## Result

The under-expanded weapon families were brought to the same 31-genre working matrix used by the mature expanded object catalogs.

| Family | Preserved seed | New authored expansion | Current v2 total |
|---|---:|---:|---:|
| Melee | 327 | 673 | 1,000 |
| Ranged | 230 | 770 | 1,000 |

### Melee v2
- Library path: `/Multiversal Canonical Game Objects/expanded_melee_weapons_canonical_multigenre_v2.csv`
- SHA-256: `cfe5f95ecc40b8b84068bc9ddb1b374e0349360c852a0c47bedf4df21caddf9f`
- New authored rows per genre family: 21–22
- Original 327 seed rows retained with original fields unchanged.
- Existing genre labels are preserved; `Genre_Family` is a normalized projection.

### Ranged v2
- Library path: `/Multiversal Canonical Game Objects/expanded_ranged_weapons_canonical_multigenre_v2.csv`
- SHA-256: `affec9f1a2678326addfa2bbe8394ffdec4cf78154f6a64e8ea6a37c6bb28d71`
- New authored rows per genre family: 24–25
- Original 230 seed rows retained with original fields unchanged.
- Because the seed ranged CSV had no Genre column, seed `Genre_Family` is labeled `CONSTRAINED_DERIVED_FROM_NAME_CATEGORY_TECH_TIER`.

## 31-genre matrix

- Age of Sail
- Atompunk
- Biopunk
- Classical / Imperial
- Clockpunk
- Contemporary
- Cosmic Horror
- Cyberpunk
- Dark Fantasy / Necromantic
- Dieselpunk
- Elemental / Planar
- Far-Future Posthuman
- Hard Science Fiction
- High Fantasy
- Interdimensional
- Mecha
- Medieval Low Fantasy
- Modern Military
- Multiversal / Core Rules
- Mythic Antiquity
- Post-Apocalyptic
- Psionic
- Renaissance / Da Vincian
- Solarpunk
- Space Opera
- Steampunk
- Stone Age / Tribal
- Superhero
- Underwater / Oceanic
- Urban Fantasy
- Weird West

## Authorship and provenance

New records are not presented as recovered source material. Every generated row is labeled:

- `Source_Kind = AUTHORED_EXPANSION`
- `Provenance_State = OWNER_AUTHORIZED_AUTHORED_EXPANSION`
- `Genre_Assignment_State = OWNER_AUTHORIZED_AUTHORED_EXPANSION`

Seed rows retain their existing `Origin` and all original mechanics.

## Ranged quality correction

The first ranged generation draft reused firearm-shaped templates too broadly in pre-industrial genres. It was replaced before governance lock.

The published ranged v2 uses genre-appropriate families:

- Stone Age / Tribal: slings, bows, blowguns, atlatls, javelins, bolas, throwing disks, sling staffs, fire/acid pots, nets, harpoons and rare supernatural projectors.
- Classical / Imperial: bows, crossbows, atlatls, javelins, fire pots, repeating crossbows, hand ballistae, harpoons and setting-appropriate arcane projectors.
- Medieval / High Fantasy / Mythic: bows, crossbows, alchemical projectiles, siege-portable weapons and magical projectors.
- Age of Sail / Renaissance / Weird West: black-powder and hybrid weapon families.
- Industrial / Modern: ballistic, automatic, launcher, less-lethal and specialist projectile families.
- Advanced / Posthuman: beam, plasma, ion, coil, particle, gravity, cryo, microwave, nanite and smart-launcher families.
- Exotic domains: arcane, psionic, elemental, interdimensional and multiversal analogues.

All new ranged rows populate baseline range/capacity/ammo-or-power/reload fields instead of leaving the old capacity ambiguity pattern unresolved.

## Status

The v2 files are **current source-population authority** once referenced by `CURRENT_GAME_OBJECT_SOURCE_AUTHORITY.json`.

They are not automatically GAME_READY. FIAA must still audit content, integration, runtime binding, validation and playtest.
