# ICF-12 - Culinary & Magical Culinary Rules

**Work item:** ICF-12  
**Status:** implementation candidate  
**Source basis:** `Cooking 11-24-24.mht`, canonical PDF `MV_Master_01_Core/02_PDF_Sources/Part 1/Downtime/Cooking 11-24-24.PDF`, SHA-256 `3c4bac0dd4ab1952d4c2e06895e8d4b93ecb907e4b6cecb353f01c53ae952c85`.

## Rule hierarchy

ICF-12 preserves source-authored outcomes at the narrowest scope that actually owns them: ingredient definition -> derived preparation -> recipe/meal -> enchantment -> ability/perk overlay -> consumption/overload state. Finished-dish effects do not flow backward into raw ingredients. ICF-08 affinity tendencies remain proposal/search inputs only.

Ordinary meal quality is source-exact: Poor restores 5 HP or 10 stamina, Average 10/20, High 20/30, Gourmet 40/50. Unless a recipe says otherwise, effects last one hour. The default ordinary-food rule permits one active food effect; narrower explicitly random systems such as Chaos Chow may override stacking within their own scope.

Cooking uses `1d20 + Cooking modifier` versus Food DL. The source generic tool classes are Basic +0, Advanced +2, Enchanted +5. Natural 20 yields legendary quality plus a random additional minor effect; success prepares perfectly; a miss by 1-5 remains edible but loses its full intended effect; a miss by 6+ ruins the food. Basic recipes take one in-game hour and enchanted/complex recipes may take four or more hours.

Unpreserved food spoils after one in-game day. Salt curing, refrigeration and magical preservation are source examples. Enchanted food spoils twice as fast unless preserved. Separate equipment/perk preservation multipliers are retained as authored overlays, but ICF-12 does not invent a multiplication/order-of-operations rule where the source does not provide one.

## Enchantment and magical cuisine

Enchanted food requires a Cooking check, an enchantment ingredient, and a spellcaster or enchanted tool. The source has two tier vocabularies that must not be flattened: the early mechanics table calls DL 15/20/25 Basic/Advanced/Legendary, while the ability tree uses Minor DL15, Intermediate DL20 and Advanced DL25. ICF-12 keeps those labels section-scoped.

The source's six effect families are Healing, Stat Buffs, Combat Enhancements, Utility, Environmental and Unique Magical. Twelve named enchantments are encoded exactly as source outcomes, ranging from Healing Touch through Time's Favor. Eight example meals are retained as recipe-level source assertions. None of these effects is assigned to Frostberry, Phoenix Feather, Chrono-Crystal or any other raw ingredient merely because the ingredient appears in a related dish.

Alchemical Cooking may combine a governed potion output with food, but ICF-11 remains the potion/formula authority. Elemental Cooking may produce damage-based buffs only through an explicit recipe/enchantment rule; an elemental ingredient affinity does not select a damage type by itself. Experimental Cooking uses explicit randomized rules where authored. Signature Recipes may reduce DL for their creator and be upgraded, but the source gives no numeric reduction, so none is invented.

The advanced ability overlays preserve Dimensional Cuisine, Culinary Masterpiece, Reality-Bending Cuisine and Eternal Feast exactly at meal/ability scope. Reality-Bending Cuisine requires exotic ingredients, Cooking DL 30 and is limited to one meal per long rest. Permanent Culinary Masterpiece buffs stack once per character and require legendary ingredients.

## Canonical source bindings

Eight explicit Cooking-source ingredient terms bind to existing canonical ICF definitions: Frostberry, Dragonfruit, Basilisk Egg, Phoenix Feather, Chrono-Crystal, Voidfruit, Mana Salt and Elemental Fruit. These bindings prove identity/participation only. They do not grant the associated finished meal's effect, harvestability, safety, legality, exact substitution, or current price.

Adaptive Ingredient Use remains an ability-gated substitution override. The source permits replacement of up to three missing Rare ingredients and later Exotic ingredients, but ICF-12 requires a governed compatibility/substitution relationship rather than guessing similarity from names, folklore or creature type.

## Enchantment Sickness and Chaos Chow

The normal Enchantment Sickness rule is preserved: multiple enchanted foods within one hour trigger a Constitution save at `DC = 10 + total enchantments consumed`; each failed save adds +2 to subsequent saves until cured. The twelve-result sickness table, optional severity scaling, source cure/mitigation rules and DC 15 analysis check are encoded.

Chaos Chow is kept as a narrower random-food ruleset: half ordinary restoration, explicit spoilage check, 20-result random enchantment table and 10-result overload table. Its stacking rule overrides the ordinary one only inside Chaos Chow. The source contains a genuine numeric conflict: one line says every Chaos Chow meal in the hour increases overload DC by +2, while the next gives `DC = 10 + number of Chaos Chow meals consumed`. ICF-12 records both and refuses to normalize one executable formula without an explicit later ruling.

## Authority boundaries

D17 remains live Asset/quantity/condition authority. MIB-13 remains current price and market-scarcity authority; Cooking `gp` prices are source provenance, not current universal prices. MIB-11 remains World/Reality authority. ICF-07/09 remain creature harvest/crosswalk authority. ICF-10 remains processing lineage. ICF-11 remains alchemical formula authority. No parallel inventory/economy/world ledger, real-money behavior, or migration 0022 is introduced.
