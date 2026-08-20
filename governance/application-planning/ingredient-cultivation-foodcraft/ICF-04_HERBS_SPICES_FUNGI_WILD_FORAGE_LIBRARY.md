# ICF-04 — Herbs, Spices, Fungi & Wild Forage

**Program:** ICF — Ingredient, Cultivation & Foodcraft Foundation  
**Work item:** ICF-04  
**Library version:** 1.0.0  
**Definition contract:** `ICF-02_CANONICAL_INGREDIENT_SCHEMA.json`  
**Total primary ingredient definitions:** 242

## Purpose

ICF-04 establishes a broad reusable herb, spice, fungus, fermentation-culture and wild-forage baseline for later cooking, alchemy, agriculture, production, trade, recipe generation and Cozy/Downtime play. It extends the ICF-03 compact-source/materializer convention rather than creating a parallel catalog format.

The library is reusable **definition content**, not live state. D17 remains authoritative for owned quantities, quality, condition and custody. MIB-13 remains authoritative for current price and market scarcity. MIB-11 remains authoritative for World/Reality/location identity.

## Content composition

The canonical compact source materializes **242** primary ingredients:

- 29 culinary herbs;
- 30 spice seeds/fruits;
- 25 aromatic roots, barks, gums, saps and resins;
- 34 tea/medicinal botanical terms;
- 31 edible/general fungi;
- 10 fermentation cultures;
- 25 wild greens/flowers;
- 26 wild berries/fruits;
- 21 aquatic/sea vegetables and water plants;
- 11 lichens, mosses and related wild fungal/botanical resources.

There are **233 governed-first-party** mundane baseline records and **9 hybrid/source-backed** records.

## Source-backed records

### Alchemy

`Redleaf` and `Soothewort` are explicitly named by `Alchemy.mht` as examples of **Common Herbs** in the Healing Potion formula. ICF-04 preserves their Common rarity and formula participation. It does **not** infer that either herb individually owns the potion's healing effect.

`Rockroot` is explicitly named by `Alchemy.mht` as an **Uncommon Ingredient** in Elixir of Giant Strength. The source does not say that Rockroot alone causes the strength effect. ICF therefore preserves rarity and formula participation without inventing an ingredient-specific effect. Its botanical/root classification is governed ICF authoring, not a claimed source fact.

### Agriculture / foraging

`Agriculture Base Add-on.mht` explicitly authors these standard foraging outputs represented here:

- Medicinal Herbs — Forest Grove, `2d6`;
- Wild Berries — Forest Grove, `1d4`;
- Mushrooms — Swamp Pod, `1d4`;
- Water Plants — Swamp Pod, `1d4`;
- Medicinal Plants — Jungle Biodome, `1d4`;
- Snow Moss — Arctic Dome, `1d2`.

Generic source terms remain generic definitions where the source does not identify a species. Later specific ingredients may reference or replace those generic recipe/production roles through explicit stable-ID mappings; they are not silently assumed to be any one real-world plant or fungus.

## Protected ICF-06 boundary

The Agriculture source also names overtly magical/exotic or clearly advanced setting ingredients. ICF-04 records their existence but deliberately does **not** normalize their properties here:

`Glow Mushrooms`, `Exotic Fruits`, `Ice Herbs`, `Mana-Infused Herbs`, `Lumina Berries`, `Fire Blossom`, `Dream Moss`, `Moonflower`, `Ironroot`, `Iceleaf`, and `Etherleaf`.

They remain input evidence for **ICF-06 — Magical, Exotic & Multiversal Ingredients**, preserving the protected roadmap boundary.

## Mundane first-party authoring policy

The remaining records provide a generic mundane baseline covering familiar herbs, spices, fungi, fermentation cultures, wild greens, berries, aquatic vegetables, lichens/mosses, roots, barks, gums and resins.

A generic baseline may author stable ingredient identity, broad botanical/fungal nature, physical form, perishability, cultivation/foraging eligibility, acquisition mode, broad culinary flavor/edibility class, and a generic mundane rarity/availability band. It does **not** make the ingredient equally common in every world. World/reality scoped availability may differ, and actual market scarcity/pricing remains MIB-13 state.

## Alchemy and medicine boundary

General botanical familiarity does not authorize a mechanical medicinal or alchemical effect. First-party records in this tranche do not receive healing, poison, stat, resistance, spell, ritual or other individual effect properties merely because a real-world or folkloric association exists.

Source-backed Alchemy records preserve only what the source actually supports: identity, rarity where given, and formula participation. ICF-11 later defines the alchemical grammar that can turn governed properties into formula behavior.

## Culinary boundary

ICF-04 may classify familiar mundane ingredients as edible, conditional, unsafe or inedible and may supply broad flavor/profile tags for recipe search. Those tags are content metadata, not nutritional or medical advice and do not imply a mechanical benefit.

## Deterministic representation

Checked-in canonical artifacts:

- `ICF-04_LIBRARY_SOURCE.json` — compact authoring source;
- `ICF-04_LIBRARY_MATERIALIZER.py` — deterministic expansion/validation;
- `ICF-04_LIBRARY_INDEX.json` — counts, pack routing and authority boundaries;
- `ICF-04_LIBRARY_VALIDATION_SUMMARY.json` — deterministic library-level checks;
- this document.

The materializer emits three expanded ICF-02-shaped packs on demand. Generated packs are projections; the compact source and materializer are canonical, avoiding repetitive generated JSON while keeping every stable ID reviewable.

## Validation result

The deterministic library check passes with 242 unique `ingredient:<slug>` IDs, 242 primary-ingredient records, 233 governed-first-party plus 9 hybrid/source-backed records, MIB-13 economy authority preserved, D17 live-state authority preserved, no current-price/owner fields, no magical-culinary or creature-source claims, no ingredient-specific alchemical effect claims, all selected source-backed Agriculture/Alchemy terms preserved, and overtly magical/exotic source terms deferred to ICF-06.

Repository health remains the canonical tranche gate.
