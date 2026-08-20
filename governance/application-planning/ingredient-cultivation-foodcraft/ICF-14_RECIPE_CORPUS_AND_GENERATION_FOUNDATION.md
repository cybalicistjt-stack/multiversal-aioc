# ICF-14 — Recipe Corpus & Recipe-Generation Foundation

**Status:** implementation candidate  
**Work item:** ICF-14  
**Corpus version:** 1.0.0  
**Owning mechanics:** ICF-11 alchemy; ICF-12 culinary/magical culinary; ICF-10 preparation lineage

## Result

ICF-14 supplies a deterministic governed recipe corpus of **319 records**: **216 concrete first-party recipes**, **92 governed templates**, and **11 source-backed recipes/formulas**. The corpus covers ordinary meals, baked goods, beverages, fresh sides, sauces, preservation, survival food, abstract cultural/regional templates, enchanted/elemental food, alchemical food, and the alchemical potion/tonic/elixir/poison/oil/salve/powder/reagent formulation surface.

The corpus is deliberately setting-neutral. A regional/cultural template is only a composition shape; it must bind to separately authored World/Setting/culture context before a setting-specific name, tradition, origin, taboo, availability, or history becomes canonical.

## Composition rules

A concrete first-party culinary recipe uses stable canonical ICF ingredient/preparation references with typed roles and quantities. Ordinary recipes do not hard-code a new mechanical food effect: cooking success and quality resolve through ICF-12. Preservation recipes map an exact canonical input to an already-governed ICF-10 preparation output and transformation rule.

Template generation is fail-closed. Every ingredient/preparation selector must resolve to a canonical definition before execution. Substitution must use explicit governed compatibility. Names, folklore, broad creature affinities, ICF-08 tendencies, or source co-occurrence cannot satisfy a property/effect requirement by inference.

## Magical and elemental food

First-party enchanted/elemental templates bind a normal base meal to an **ICF-12 `food-enchantment:*` definition**. They separately require a canonical enchantment ingredient whose eligibility is supported by governed evidence. The enchantment's effect is never copied onto the raw ingredient. ICF-12 remains the sole outcome authority.

The eight Cooking source recipe examples are retained exactly at source-recipe outcome scope. Where the governed ICF-12 assertion did not enumerate a recipe's exact component list, ICF-14 leaves the input list empty rather than reconstructing it.

## Alchemical food and formulas

The three ICF-11 source formulas are retained with their source rarity/composition/effect rules: Healing Potion, Potion of Fire Breath, and Elixir of Giant Strength.

ICF-14 does **not** convert ICF-11 example ingredients into exact signature requirements. The first-party alchemical expansion provides 32 formulation templates spanning eight output forms and all four ICF-11 rarity profiles. A template remains non-executable until it binds to an already governed formula/effect specification; ICF-14 invents no potion effect.

Alchemical-food templates reference both a governed ICF-11 formula and ICF-12 Alchemical Cooking. Their combined interaction is not precomputed when the owning rules do not specify it.

## Owner-domain boundary

- ICF-10 owns derived-preparation identity and processing lineage.
- ICF-11 owns alchemical formula/effect, rarity composition and brewing mechanics.
- ICF-12 owns ordinary/magical culinary outcomes, checks, quality, preservation and overload.
- ICF-13 supplies acquisition/production seams, not recipe truth.
- D17/Asset/inventory owns live quantities, condition, ownership, consumption and output instances.
- MIB-13 owns current price and market scarcity.
- World/Setting/culture owners supply actual setting/cultural canon.
- ICF-14 creates no scheduler, Cozy authority, provider-dependent authority, real-money behavior, or migration `0022`.

## Deterministic artifacts

- `ICF-14_RECIPE_SCHEMA.json`
- `ICF-14_RECIPE_CORPUS_SOURCE.json`
- `ICF-14_SOURCE_RECIPES.json`
- `ICF-14_GENERATION_GRAMMAR.json`
- `ICF-14_REFERENCE_FIXTURES.json`
- `ICF-14_RECIPE_MATERIALIZER.py`
- `ICF-14_VALIDATION_SUMMARY.json`

Expanded review packs are materializer outputs; the checked-in compact source plus deterministic materializer is the canonical recipe authoring surface.
