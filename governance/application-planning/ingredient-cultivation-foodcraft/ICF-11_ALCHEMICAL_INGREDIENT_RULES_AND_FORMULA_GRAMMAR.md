# ICF-11 - Alchemical Ingredient Rules & Formula Grammar

**Work item:** ICF-11  
**Status:** implementation candidate  
**Source basis:** `Alchemy.mht`, canonical PDF `MV_Master_01_Core/02_PDF_Sources/Part 1/Downtime/Alchemy.PDF`, SHA-256 `020e120dc253204073f170f4b2eb76b6b67c8d56755bf8cad32ca3f64dde13e9`.

## Purpose

ICF-11 converts the approved Alchemy source into a deterministic rules layer without inventing raw-ingredient effects. Formula effects belong to formulas. Ingredient-level roles, properties, substitution groups, and exact effects exist only when explicitly governed. ICF-06 affinity tags and ICF-08 part/type/trait tendencies are candidate/research inputs, never automatic exact effects.

## Canonical source rules

Alchemy source rarity is Common / Uncommon / Rare / Exotic. Identification DCs are 10 / 12 / 15 / 18. Gathering DCs are 10 for Common/Uncommon, 15 Rare, 18 Exotic. Mixing DCs are 10 / 12 / 15 / 18. Catalysis is Intelligence (Alchemy) DC 10 for Common/Uncommon and Intelligence (Arcana) DC 15 for Rare/Exotic. Stabilization is Wisdom (Alchemy) DC 12.

The brewing state machine is Preparation -> Mixing -> Catalysis -> Stabilization. Mixing failure spoils the potion and wastes ingredients. Catalysis failure reduces effectiveness by 25%. Stabilization enhanced success increases potency or duration by 25%; stabilization failure produces an unstable potion with reduced shelf life or source-authored side effects.

Recipe research requires one day per rarity level and Intelligence (Arcana) DC 12 / 15 / 18 / 20. The source's 50 CR/day, recipe costs, ingredient purchase costs, tool costs, and potion selling prices are preserved as historical/source assertions only. MIB-13 remains current price and market-scarcity authority.

## Formula grammar

The governed role vocabulary supports base/solvent, active, modifier, ingredient catalyst, stabilizer, optional enhancer, and the deliberately weak `formula-ingredient` role. A role does not imply an effect. Heat, magic, and time remain valid process catalysts from the source and are not forced into ingredient slots.

Requirements may be exact-definition, rarity-count, explicit property-threshold, or explicit substitution-group requirements. Exact-definition locking is permitted only when the source or later governed content actually requires an exact ingredient. The three sample source recipes use "e.g." ingredient examples; ICF-11 therefore records those named ingredients as source-backed examples, not mandatory signature locks.

Source rarity composition templates are preserved: Common potions use 2-3 Common ingredients; Uncommon use 2 Common plus 1-2 Uncommon; Rare use 1 Common, 2 Uncommon, 1 Rare; Exotic use 1 Uncommon, 2 Rare, 1 Exotic.

## Sample formulas

- **Healing Potion:** Common; Mixing DC 10; restores 2d4 + 2 HP; 2 Common Herbs, with Redleaf and Soothewort as examples.
- **Potion of Fire Breath:** Uncommon; Mixing DC 12; 15 ft cone, 4d6 fire damage, DC 13 Dexterity save for half; 1 Uncommon ingredient (Fire Salamander Tongue example) plus 2 Common ingredients (Sulfur and Charcoal Dust examples).
- **Elixir of Giant Strength:** Rare; Mixing DC 15; Strength becomes 21 for 1 hour; 1 Rare ingredient (Giant's Toenail example) plus 2 Uncommon ingredients (Ogre's Blood and Rockroot examples).

Those finished-potion effects do **not** become effects of the example ingredients.

## Substitution and quality

Adaptive Alchemy is an ability-gated override, not a default formula rule. It can replace up to two Common ingredients with explicitly similar/substitution-group members at no penalty and can substitute Uncommon ingredients with +2 Mixing DC. Similarity must be governed; names, folklore, creature type, or ICF-08 tendencies do not prove it. Rare/Exotic substitution is not authorized by this perk.

Enhanced Ingredient Quality is likewise an ability overlay: with the perk active, Rare/Exotic ingredients increase the brewed potion's effect by 25%. This does not assign an inherent +25% effect to a definition or live item.

## Source contradiction retained fail-closed

The base Preparation Step says failure increases Mixing DC by +1. The `Precise Preparation` perk text says a failed Preparation Check increases Mixing DC by only +1 "instead of the usual +2." Those assertions conflict. ICF-11 records the contradiction rather than silently choosing a universal pre-perk penalty. A later explicit correction or owner decision may resolve it.

## Failure, salvage, shelf life, and research

Minor failure reduces potency by 50%. Major failure makes the potion toxic and causes the source's mild poison effect (1d4 damage). A natural 1 is a critical brewing accident with 1d6 damage within 5 feet and a source repair cost assertion of 25 CR. Salvage is Intelligence (Alchemy) DC 15: success recovers 50% of ingredients. Stable Common/Uncommon potions last one year; Rare/Exotic six months. Unstable potions degrade after 1d4 weeks.

## Authority boundaries

D17 remains live Asset state. MIB-13 remains current price/scarcity. MIB-11 remains World/Reality. ICF-07 and ICF-09 remain creature harvest/crosswalk authority. ICF-10 remains processing lineage. ICF-12 remains culinary/magical-culinary outcome authority. No parallel inventory/economy/world truth and no migration 0022 are introduced.
