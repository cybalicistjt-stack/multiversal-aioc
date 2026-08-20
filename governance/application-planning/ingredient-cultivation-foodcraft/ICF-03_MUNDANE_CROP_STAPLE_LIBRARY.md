# ICF-03 — Mundane Crop & Staple Plant Library

**Program:** ICF — Ingredient, Cultivation & Foodcraft Foundation  
**Work item:** ICF-03  
**Library version:** 1.0.0  
**Definition contract:** `ICF-02_CANONICAL_INGREDIENT_SCHEMA.json`  
**Total primary ingredient definitions:** 176

## Purpose

ICF-03 establishes a substantial governed first-party mundane plant baseline that later cooking, agriculture, economy, recipe, production and Cozy/Downtime systems can reference through stable ingredient identities. It does not define current inventory, current quality/condition, universal prices, world-specific production yields, magical properties, or creature biology.

## Content composition

The library contains 176 `primary-ingredient` definitions split across four machine-readable packs:

- grains, pseudograins and legumes — 36;
- vegetables and roots/tubers — 68;
- fruits — 46;
- nuts, seeds and industrial staples — 26.

Category counts:

- `allium_brassica` — 14
- `citrus` — 10
- `fruiting_vegetable` — 18
- `grain` — 14
- `industrial_staple` — 12
- `leafy` — 18
- `legume` — 16
- `nut_seed` — 14
- `pseudograin` — 6
- `root_tuber` — 18
- `temperate_fruit` — 18
- `tropical_fruit` — 18

## Authorship and source rule

Exactly one ICF-03 record, `ingredient:wheat`, is **hybrid** because the Agriculture source explicitly names Wheat and supplies a sample crop row. That record preserves five source assertions: identity, source classification, source-unit wording, growth/yield/resource data, and the legacy `5 CR` base-value observation.

The other 175 records are **governed-first-party** generic content. Their names and baseline mundane agricultural metadata are new governed authoring, not claims that they appeared in Cooking, Agriculture, Alchemy or the master CSVs.

This distinction is structural in every record through `authorship.class` and `authoringRecordRefs`.

## Baseline rarity and availability

ICF-03 gives ordinary crop definitions a governed generic mundane-baseline rarity of `common`. This means only that the content is intended as ordinary mundane agricultural material in the generic ICF baseline. It does **not** mean that every crop is common in every World, Reality, settlement or market.

World/Reality content may author scoped rarity/availability overrides. MIB-13 remains authoritative for current market scarcity, price, tariffs, route costs and actual trading opportunities.

Fruit and fresh-vegetable categories commonly use `seasonal` as their baseline acquisition availability; durable grains, pulses, nuts, roots and industrial staples generally use `available`. These remain reusable content defaults, not live market state.

## Units and live-state boundary

All ICF-03 definitions use mass as their canonical transaction/reference dimension through `unit:kilogram`, with explicit exact kilogram↔gram conversion rules.

The Agriculture source's Wheat yield is still preserved as `200 units`. ICF-03 does **not** infer a conversion from that generic source unit into kilograms. The Wheat record therefore keeps a source-unit coverage gap for ICF-13 production binding.

Current quantity, owner/custody, quality and condition remain D17 Asset Instance state. Definitions explicitly set `definitionMaySetCurrentInstanceState=false`.

## Profile coverage

Every record includes:

- stable `ingredient:<slug>` identity and version;
- mundane/botanical taxonomy;
- governed rarity and acquisition availability;
- typed units;
- physical form and perishability;
- renewable ecology;
- cultivation eligibility and crop-field facility compatibility;
- MIB-13 economy authority references;
- culinary edibility and broad first-party flavor-family tags where appropriate;
- D17 quality/condition ownership;
- provenance/authorship;
- coverage status and tags.

ICF-03 intentionally does **not** add magical-culinary effects, creature-source claims, or alchemical effect tags simply from general knowledge. Those domains are populated only by their later governed tranches or by explicit source evidence.

## Included crop families

The library covers staple cereals and millets, pseudograins, major pulses, leafy vegetables, brassicas, alliums, fruiting vegetables, gourds, roots and tubers, temperate fruits, berries, citrus, tropical/subtropical fruits, nuts, edible/oil seeds, sugar crops, oil crops, and plant fiber staples.

It deliberately avoids herbs/spices/fungi/wild forage reserved for ICF-04, livestock/aquatic content reserved for ICF-05, and magical/exotic content reserved for ICF-06.

## Validation

`ICF-03_LIBRARY_VALIDATION_SUMMARY.json` records deterministic content checks across all 176 definitions:

- globally unique stable IDs;
- canonical `ingredient:<slug>` ID syntax;
- only primary-ingredient records;
- D17 live-state authority retained;
- MIB-13 current-price and market-scarcity authority retained;
- no live owner/quantity/current-price/current-quality/current-condition fields;
- no derived lineage;
- no magical-culinary or creature-source claims;
- all records cultivation eligible;
- source-vs-first-party authorship separation;
- preservation of the Wheat source unit/value assertions without converting them into universal truth.

AIOC repository health remains the canonical repository-level acceptance gate.

## Boundaries carried forward

ICF-03 does not authorize ICF-04 or later work before closeout. It creates no universal price table, production provider, live inventory ledger, magical crop subsystem, world-specific yield simulator, or migration 0022. Later ICF tranches may enrich these stable definitions by reference without changing their canonical identity.
