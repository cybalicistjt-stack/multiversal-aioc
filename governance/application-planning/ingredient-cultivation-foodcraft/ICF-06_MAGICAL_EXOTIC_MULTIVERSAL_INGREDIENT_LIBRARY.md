# ICF-06 — Magical, Exotic & Multiversal Ingredient Library

Status: IMPLEMENTATION CANDIDATE  
Work item: ICF-06  
Schema authority: `ICF-02_CANONICAL_INGREDIENT_SCHEMA.json`

## Purpose

ICF-06 supplies the protected magical/exotic/multiversal primary-ingredient layer that ICF-03 through ICF-05 intentionally did not absorb. It preserves explicit Agriculture, Cooking and Alchemy terms and adds governed first-party content broad enough for later cooking, alchemy, ritual, magitech, economy and worldbuilding use.

The tranche defines **ingredient identity and descriptive affinities**, not executable effects. ICF-11 owns alchemical formula mechanics, ICF-12 owns culinary/magical-culinary mechanics, ICF-07 owns creature-specific harvest/butchery, ICF-09 owns the creature catalog crosswalk, ICF-10 owns processing lineage, MIB-13 owns current price/market scarcity, D17 owns live Asset state, and MIB-11 owns World/Reality scope.

## Library scale

The canonical compact source materializes **312 primary ingredient definitions**:

- 287 governed first-party magical/exotic/multiversal definitions;
- 25 hybrid/source-backed definitions;
- 7 source-backed creature-derived terms with explicit unbound creature/harvest crosswalk gaps.

This brings ICF-03 + ICF-04 + ICF-05 + ICF-06 to **964 primary ingredient definitions**, within the program's approximately 700–1000 primary-ingredient target before later tranches add processing/recipes rather than parallel primary identities.

## Source-backed rules

### Cooking

Cooking explicitly defines an ingredient rarity chart and names Frostberries, Dragonfruit and Basilisk Eggs as Uncommon, and Phoenix Feathers, Chrono-Crystals and Voidfruit as Rare. Those rarity assertions may map directly.

Cooking also names mana salts, phoenix feathers and elemental fruits as enchantment ingredients. That supports an enchantment-ingredient role, but not a specific raw-ingredient effect unless separately authored.

Finished dish effects are not silently copied to raw ingredients. Frostberry Jam, Voidfruit Parfait, Chrono-Crème and Phoenix Egg Omelet therefore retain recipe-level attribution gaps for ICF-12.

### Agriculture

Agriculture supplies magical/exotic cultivation and foraging terms including Glow Mushrooms, Exotic Fruits, Ice Herbs, Mana-Infused Herbs, Lumina Berries, Fire Blossom, Dream Moss, Moonflower, Ironroot, Iceleaf and Etherleaf.

Agriculture's `Exotic` and `Supernatural` crop classifications are preserved as source classifications, not automatically converted to canonical rarity. In particular, Fire Blossom's `Exotic` crop type and Etherleaf's `Supernatural` crop type remain source observations.

The source's Fire Blossom and Etherleaf crop-table yield/growth/resource/value assertions are retained as provenance. Their `CR` values are historical/source value observations only; they do not replace MIB-13 current pricing.

### Alchemy

Alchemy explicitly classifies Fire Salamander Tongue as an example Uncommon Ingredient, Giant's Toenail as a Rare Ingredient, and Ogre's Blood as an Uncommon Ingredient in sample formulas. Those rarity terms map directly because Alchemy defines Common/Uncommon/Rare/Exotic as ingredient rarity.

The Potion of Fire Breath and Elixir of Giant Strength effects remain formula outputs. ICF-06 does not assign those finished effects to the raw creature-derived ingredients.

## Governed first-party affinities

First-party content may carry broad authored affinity descriptors such as fire, cold, storm, water, earth, void, astral, fey, infernal, celestial, shadow, time, phase, echo, gravity or reflection. These are **descriptive properties for downstream rule grammars**, not self-executing buffs, damage, healing, resurrection, rerolls or other mechanics.

## Creature boundary

Source-authored creature-derived terms such as Phoenix Feather, Basilisk Egg, Lava Beetle Shell, Fire Salamander Tongue, Giant's Toenail and Ogre's Blood preserve only the part identity actually present in the source term. No creature biology, yield, legality, sentience, edibility, harvest procedure or anatomical detail is invented. The corresponding records deliberately carry creature-crosswalk gaps for ICF-07/09.

## World/reality and economy boundary

No magical ingredient is globally available merely because it exists in the library. Definition records leave concrete `worldRealityRefs` empty unless a source supplies a governed scope. MIB-11-owned settings/worlds/realities later bind availability. MIB-13 markets independently determine current scarcity, price, trade opportunity, access, route cost and legality.

## Deterministic artifacts

- `ICF-06_LIBRARY_SOURCE.json` — compact canonical content source.
- `ICF-06_LIBRARY_INDEX.json` — counts and materialization metadata.
- `ICF-06_LIBRARY_MATERIALIZER.py` — deterministic materializer and invariant validator.
- `ICF-06_LIBRARY_VALIDATION_SUMMARY.json` — checked-in validation result.

The materializer can emit three expanded packs for review/consumption without making generated output the canonical authoring surface.
