# ICF-01 — Source Inventory & Reconciliation

**Program:** ICF — Ingredient, Cultivation & Foodcraft Foundation  
**Work item:** ICF-01  
**Status:** implementation candidate  
**Authority boundary:** reconciliation only; no final ICF-02 schema decisions are made here.

## 1. Purpose

ICF-01 inventories and reconciles the source material that will feed the canonical ingredient system. Its job is to preserve what each source actually says, identify overlaps and contradictions, and make the unresolved normalization work explicit before ICF-02 defines stable IDs, canonical vocabularies, profiles, units and validation rules.

The controlling rule is: **source values remain provenance-scoped assertions until an explicit ICF rule reconciles them.** A later normalized value must not erase the original source term.

## 2. Source inventory

### Legacy rule packages

- `Cooking 11-24-24.mht` — ingredient rarity examples, ordinary and enchanted cooking, specialized/alchemical/elemental/experimental cooking, signature recipes, dimensional cuisine and reality-bending cuisine.
- `Agriculture Base Add-on.mht` — crops, growth/yield/water/power/value examples, foraging zones, magical agriculture, storage/spoilage, agriculture facilities, livestock integration and crafting/trade crossover.
- `Alchemy.mht` — ingredient rarity/identification, gathering, preparation/mixing/catalyzing/stabilizing, substitution/research, failures/salvage, shelf life and sample formulas.

The exact source file hashes are preserved in `ICF-01_SOURCE_RECONCILIATION_CROSSWALK.json`.

### Master CSV sources

`MV_Master_01_Core.zip` contains no dedicated `Ingredients.csv` or `Livestock.csv`. The main ICF-relevant catalogs are:

- `Items.csv` — 761 rows; 155 broad food/cooking/alchemy/plant/animal/material matches. It is primarily a finished-item/consumable catalog rather than primary ingredient authority.
- `Bases_Facilities.csv` — 1,080 rows; 305 broad ICF-related matches and 10 explicit Agricultural Material rows. It contains agriculture/foraging outputs and facilities but mixes definitions, production abstractions and inferred normalized values.
- `Profession_Crafting_Abilities.csv` — 221 rows; 69 broad ICF-related matches, including 24 Cooking-tree and 24 Alchemy-tree matches. It is rules/progression authority, not ingredient identity authority.

### Current governed App seams

- `DevelopmentBible/02-game-framework/crafting-and-economy.md` makes materials, food and trade goods governed content and treats values as context-dependent offers/references rather than immutable global truth.
- `DevelopmentBible/02-game-framework/creatures-npcs-and-species.md` gives creature records biology plus **loot or harvest references where authored** and explicitly forbids fabrication of incomplete source creature lore.
- MIB-12 provides explicit deterministic recipe and owner-domain Asset mutation seams.
- MIB-13 provides explicit/versioned currencies, independent markets and contextual prices/trade routes. ICF therefore must not turn legacy `gp`, `CR`, `credits`, `MC`, or inferred costs into one universal price table.

## 3. Explicit ingredient/source examples

### Cooking

Cooking explicitly classifies ingredients by rarity and magical properties:

- Common examples/classes: vegetables, grains, basic meat.
- Uncommon examples: `Frostberries`, `Dragonfruit`, `Basilisk Eggs`.
- Rare examples: `Phoenix Feathers`, `Chrono-Crystals`, `Voidfruit`.
- Enchantment examples include `mana salts`, `phoenix feathers`, and `elemental fruits`.

Cooking also defines Alchemical Cooking, Elemental Cooking, Experimental Cooking, Signature Recipes, Dimensional Cuisine and Reality-Bending Cuisine. Those are later rule inputs; ICF-01 does not reinterpret them into properties yet.

### Agriculture

The Agriculture sample crop table explicitly contains:

| Crop | Source type | Yield | Growth DC | Water/Power | Source base value |
|---|---|---:|---:|---|---:|
| Wheat | Common | 200 units | 10 | 10 gal water | 5 CR |
| Medicinal Herbs | Rare | 100 bundles | 15 | 15 gal water | 20 CR |
| Fire Blossom | Exotic | 50 blooms | 18 | 25 gal water or 1 power | 50 CR |
| Etherleaf | Supernatural | 10 leaves | 25 | 50 gal water + 1 mana | 175 CR |

Additional explicit agriculture/foraging/crafting terms include `Snow Moss`, `Lumina Berries`, `Dream Moss`, `Moonflower`, `Iceleaf`, `Ironroot`, and `Lava Beetle Shell`.

The source also contains ordinary or magical foraging outputs such as medicinal herbs, wild berries, mushrooms, water plants, insect carapaces, glow mushrooms, crystal fragments, exotic fruits, colorful feathers, ice herbs, fur pelts, mana-infused herbs and obsidian shards. Those are source terms; whether each becomes a primary ingredient, material, derived preparation or generic source class is intentionally deferred.

### Alchemy

Alchemy uses Common, Uncommon, Rare and Exotic ingredient categories and specifies identification checks of DC 10/12/15/18 respectively.

Explicit sample formula ingredients include:

- `Redleaf`
- `Soothewort`
- `Fire Salamander Tongue`
- `Sulfur`
- `Charcoal Dust`
- `Giant's Toenail`
- `Ogre's Blood`
- `Rockroot`

Alchemy also contains Adaptive Alchemy substitution and Enhanced Ingredient Quality rules. Those require later schema support for substitution groups and quality overlays, but ICF-01 does not invent those mappings.

## 4. Existing normalized Agricultural Material rows

`Bases_Facilities.csv` currently contains 10 Agricultural Material records:

- Medicinal Herbs — Common — 20 credits/unit inferred.
- Fireblossom — Uncommon — 40 credits/unit inferred.
- Dream Moss — Rare — 75 credits/unit inferred.
- Etherleaf — Rare — 90 credits/unit inferred.
- Moonflower — Rare — 85 credits/unit inferred.
- Lumina Berries — Uncommon — 60 credits/unit inferred.
- Iceleaf — Uncommon — 40 credits/unit inferred.
- Snow Moss — Common — 25 credits/unit inferred.
- Ironroot — Common — 35 credits/unit inferred.
- Lava Beetle Shell — Uncommon — 55 credits/unit inferred.

These rows are valuable reconciliation evidence, but their rarity/value fields are not automatically preferred over the original Agriculture source because several are already transformed or explicitly marked inferred.

## 5. Confirmed alias and identity candidates

Two direct alias candidates are established now:

1. `Fire Blossom` in the Agriculture source ↔ `Fireblossom` in `Bases_Facilities.csv`.
2. `Phoenix Feathers` in Cooking ↔ `Phoenix Feather` in `Bases_Facilities.csv`.

ICF-01 does **not** assign the canonical stable ID. ICF-02 must define normalization rules for spacing, singular/plural forms, aliases and display names while retaining source forms.

No relevant exact duplicate-name groups were found inside the examined `Items.csv` or `Bases_Facilities.csv` normalized-name sets; the important duplication problem is cross-source identity and transformed source rows rather than repeated identical rows within those two catalogs.

## 6. Confirmed vocabulary conflicts

### Rarity/classification conflict

The legacy sources do not share a single top-level rarity vocabulary:

- Cooking: Common / Uncommon / Rare / **Legendary**.
- Alchemy: Common / Uncommon / Rare / **Exotic**.
- Agriculture sample crop types: Common / Rare / **Exotic / Supernatural**.
- `Bases_Facilities.csv` normalizes its Agricultural Material subset mostly to Common / Uncommon / Rare.

`Legendary`, `Exotic` and `Supernatural` cannot be assumed equivalent. More importantly, `Supernatural` may be a nature/classification dimension rather than scarcity. ICF-02 must separate these concepts instead of forcing them into one ordinal field.

### Direct source/CSV rarity contradictions

At least three named records conflict between the Agriculture source and later CSV normalization:

- Medicinal Herbs: Agriculture `Rare`; CSV `Common`.
- Fire Blossom/Fireblossom: Agriculture `Exotic`; CSV `Uncommon`.
- Etherleaf: Agriculture `Supernatural`; CSV `Rare`.

Both values remain preserved with provenance until ICF-02 defines mapping semantics.

### Value/currency conflict

Legacy source values use different economic vocabularies:

- Cooking uses `gp`.
- Agriculture and Alchemy use `CR`.
- CSV normalization uses `credits` and sometimes `MC`, often explicitly marked inferred.
- MIB-13 now treats price as market/context/version dependent.

Therefore a source cost is a provenance-bearing observation, not a universal ingredient value. ICF-02 must model value references in a way MIB-13 markets can consume without flattening independent economies.

### Generic production-unit conflict

Agriculture/facility records also use generic outputs such as `Food Units`, `Material Units`, or `resource unit`. These cannot become canonical ingredient identity. ICF-13 will eventually bind production to typed outputs, but ICF-02 must first give ingredient/material records a unit vocabulary capable of representing the original source text without silently converting it.

## 7. Confirmed coverage gaps

The source inventory exposes structural gaps that ICF is intended to fill:

- no dedicated primary ingredient catalog;
- no dedicated livestock catalog;
- many explicit Cooking ingredients are absent as primary named records from the examined master item/material catalogs (`Frostberries`, `Dragonfruit`, `Basilisk Eggs`, `Chrono-Crystals`, `Voidfruit`, `Mana Salts`, `Elemental Fruits`);
- the Agriculture crop example `Wheat` is not present as a primary named material record in the examined catalogs;
- the sample Alchemy ingredients `Redleaf`, `Soothewort`, `Fire Salamander Tongue`, `Sulfur`, `Charcoal Dust`, `Giant's Toenail`, `Ogre's Blood`, and `Rockroot` are not present there as primary named ingredient records;
- creature records provide a harvest-reference seam, but missing creature anatomy/harvest evidence must remain a coverage gap rather than be inferred;
- existing finished potion/food/alchemical items cannot substitute for a primary-ingredient ontology because they are outputs, not raw ingredient identity.

## 8. Livestock and production reconciliation

`Bases_Facilities.csv` confirms an `Animal Pen` that breeds livestock and yields weekly meat, milk, wool or leather. A Homesteading variant instead expresses output as `5 Food and 2 Material Units per week`. Crop Field, Greenhouse and Orchard likewise express production at different abstraction levels.

ICF must preserve these as separate source assertions until ICF-13 binds facilities to typed ingredient/material outputs. The existence of a livestock-producing facility does not itself define species, breed, meat cut, milk type or other biological details.

## 9. Creature harvest boundary

The current creature Bible is sufficient to authorize the later ICF harvest architecture because a creature record already owns biology and authored loot/harvest references. ICF therefore needs no parallel creature-loot database.

ICF-07/08/09 may later add governed harvest profiles and crosswalks, but ICF-01 establishes a strict provenance rule: **where the creature catalog lacks enough anatomy or harvest evidence, record a coverage gap; do not manufacture species-specific organs, edibility, magical effects or lore.**

## 10. MIB integration constraints carried forward

### MIB-12

ICF recipes and processing eventually feed the existing explicit-recipe deterministic crafting model. Primary or derived ingredient definitions are reusable definitions; live harvested/crafted quantities remain owner-domain Asset state.

### MIB-13

Ingredient rarity and availability must remain separable from current market scarcity and price. The same ingredient may be common biologically yet expensive in a distant or embargoed market, or rare locally but cheap where it is cultivated. Independent market differences are a feature and must survive ICF normalization.

## 11. ICF-02 open decisions

ICF-01 deliberately hands the following unresolved decisions to ICF-02:

1. canonical ingredient stable-ID and alias rules;
2. canonical rarity/tier model plus source mappings;
3. separation of biological/magical classification, rarity, availability and market scarcity;
4. units, quantities and conversion rules;
5. market-value metadata compatible with MIB-13;
6. primary ingredient vs derived preparation boundary;
7. physical, edible, toxic, perishable and preparation fields;
8. cultivation/foraging/husbandry profile boundaries;
9. culinary, magical-culinary and alchemical property namespaces;
10. quality/condition overlays and substitution-group representation;
11. source-derived vs governed first-party authoring flags;
12. lifecycle for aliases, conflicts and coverage gaps;
13. creature-harvest reference fields that preserve the existing creature authority boundary.

## 12. Completion assessment

ICF-01 is complete when this report and its machine-readable crosswalk are repository-health clean and canonical. They provide a provenance-preserving inventory of the required source families, named overlaps, current catalog coverage, direct conflicts, facility/livestock/creature seams and explicit open decisions for ICF-02 without prematurely normalizing the data.
