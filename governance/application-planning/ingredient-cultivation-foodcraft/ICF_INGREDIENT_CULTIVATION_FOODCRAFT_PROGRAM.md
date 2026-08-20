# ICF — Ingredient, Cultivation & Foodcraft Foundation

**Program ID:** ICF  
**Program name:** Ingredient, Cultivation & Foodcraft Foundation  
**Version:** 0.2.0  
**Status:** OWNER-APPROVED — PLANNED INTERSTITIAL SUBPROJECT  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-20  
**Roadmap position:** after MIB-13 and before MIB-14

## 1. Purpose

ICF creates one canonical ingredient ecology for Multiversal so agriculture, foraging, livestock, creature harvesting/butchery, cooking, magical cooking, alchemy, medicine, ritual, crafting, trade and later base/settlement production can reference the same stable ingredient definitions rather than maintain parallel lists.

The program consolidates and normalizes the approved Cooking, Agriculture and Alchemy source packages; existing CSV/material/facility records; existing governed starter content; and creature harvest/loot seams. Source terminology and provenance remain traceable even where old rarity, currency, preparation or classification vocabularies differ.

## 2. Core architecture

One canonical ingredient definition may expose multiple governed profiles:
- identity/provenance/version/aliases/tags;
- physical form, units, edible/harvestable parts, perishability, shelf life, storage, toxicity and preparation requirements;
- ecology/cultivation/foraging/husbandry data;
- economy/rarity/availability/value/trade metadata;
- culinary properties, flavor/texture/technique/pairing/nutrition/restoration/preservation properties;
- magical-culinary affinities, potency, elemental/dimensional/reality-law compatibility and overload contribution;
- alchemical essences, effects, catalyst/stabilizer/solvent/binder/preservative roles, volatility, extraction/preparation and substitution groups;
- creature-source/harvest references where applicable.

Live inventory/Asset Instances remain owned by the existing inventory authority. Ingredient definitions are reusable content, not a second live-state ledger.

## 3. Creature harvesting rule

Any authored creature may expose a governed harvest profile through the existing creature `loot or harvest references` seam. Potential outputs can include ordinary meat, organs, fat, blood, bone, hide, scales, shell, eggs, milk, venom, glands, secretions, magical organs/cores/essences, spores, ooze materials or other authored biological/planar components.

Harvestability does not imply edibility, legality, cultural acceptability or alchemical usefulness. Those remain explicit data. Harvest outcome may depend on anatomy, creature condition, cause of death, time/decomposition, contamination, tools/workstation, harvester skill/knowledge and the selected procedure. Renewable live harvests such as milk, eggs, wool, venom, silk, honey, shed scales or analogous setting-specific outputs are supported separately from butchery.

Creature definitions point to canonical ingredient/material definitions; actual recovered outputs become ordinary owner-domain Asset/ingredient instances. The system must not create a parallel creature-loot or inventory ledger.

## 4. Creature part/effect inheritance rule

ICF does not make every creature part bespoke and does not make every same-named organ mechanically identical. It defines a governed inheritance grammar:

`part baseline → body-plan/creature-type profile → creature affinity/trait profile → explicit species/variant override → harvested-instance quality/condition`

Examples of broad part baselines may include blood/ichor as a vitality/lineage/affinity carrier, heart/core as vigor or concentrated power, eyes as perception plus authored gaze traits, liver/kidneys as purification/toxin interaction, bone/horn/shell as structural/mineral/protection properties, venom glands as toxin delivery, feathers as insulation/air plus authored supernatural affinity, and magical organs/cores as concentrated supernatural properties. These are tendencies and reusable effect families, never permission to infer unsupported creature lore.

Creature-type/body-plan profiles may be combined where appropriate, including mammalian, avian, reptilian, amphibian, piscine/aquatic, arthropod, molluscan, plant, fungal, ooze, draconic, giant, elemental, undead, celestial/divine, infernal/fiendish, aberrant/psychic, spirit/ectoplasmic, synthetic/biotech, construct-with-biological-components and extradimensional/reality-anomalous life.

Specific canonical creatures receive explicit harvest crosswalks. A signature creature may strengthen, suppress or replace a generic part tendency only through authored/governed evidence. Missing anatomy or magical properties are tracked as coverage gaps rather than fabricated.

## 5. Tranche plan

### ICF-01 — Source Inventory & Reconciliation
Inventory Cooking, Agriculture, Alchemy, livestock, creature-harvest references, Items/Bases/Facilities/profession CSVs and existing MIB content. Produce a provenance-preserving crosswalk of duplicates, aliases, conflicts, rarity/value vocabularies and missing records.

### ICF-02 — Canonical Ingredient Schema & Taxonomy
Define the shared ingredient identity, physical, ecological, agricultural, economic, culinary, magical-culinary and alchemical profiles; stable IDs; quality/condition overlays; substitution groups; provenance; lifecycle; and validation rules.

### ICF-03 — Mundane Crop & Staple Plant Library
Build a substantial first-party library of grains, pseudograins, legumes, vegetables, roots/tubers, fruits, nuts, seeds, oil/sugar/fiber crops and other staple plants with cultivation and culinary/alchemical crossover fields.

### ICF-04 — Herbs, Spices, Fungi & Wild Forage
Build culinary herbs, medicinal herbs, spices, flowers, fungi, lichens, mosses, sea vegetables, wild greens, berries, resins, saps, gums, aromatic materials and fermentation organisms.

### ICF-05 — Livestock, Animal & Aquatic Ingredient Library
Define livestock, fish, shellfish, insect/apiary and other husbandry outputs including meats, organs, blood, bone, fat, dairy, eggs, honey/wax, hides, horn/shell and other governed products.

### ICF-06 — Magical, Exotic & Multiversal Ingredients
Preserve the originally approved ICF-06. Consolidate and expand magical/exotic ingredients such as Etherleaf, Fireblossom, Dream Moss, Moonflower, Lumina Berries, Iceleaf, Frostberries, Dragonfruit, Voidfruit and other elemental, psychic, planar, chronal, necrotic, divine, alien, synthetic/biotech and Reality-specific ingredients using the same canonical schema as mundane ingredients.

### ICF-07 — Creature Harvest, Butchery & Biological Ingredient System
Implement authored harvest profiles for potentially any creature; biological-family templates with creature overrides; renewable harvest versus post-mortem butchery/extraction; condition/cause-of-death/contamination/tool/skill/procedure effects; deterministic yield and quality; food-safety, taboo/legal/protected-status fields; and canonical outputs into ingredient/material Asset Instances. Nonstandard creatures such as elementals, oozes, plant/fungal beings, constructs, undead and alien life use the same extensible harvest vocabulary without assuming ordinary meat.

### ICF-08 — Creature Part Effect Taxonomy & Affinity Grammar
Define reusable part classes, anatomy/body-plan profiles, creature-type affinity profiles and deterministic inheritance/override rules for culinary, magical-culinary, alchemical and crafting properties. Establish broad effect families for blood/ichor, hearts/cores, neural tissue, eyes, organs, lungs/gills, glands, fat/oils, bone/horn/antler, teeth/claws, hide/skin, scale/shell/chitin, feathers, muscle/meat, marrow, eggs/roe, silk/webbing, slime/mucus, magical organs/cores and extensible setting-specific parts. Generic tendencies may propose candidate properties but cannot invent creature-specific anatomy or lore.

### ICF-09 — Creature Catalog Harvest Crosswalk & Signature Ingredient Library
Walk the existing governed creature catalog and bind suitable creatures to ICF-07 harvest profiles and ICF-08 part/effect grammar. Record body plan/type, renewable and post-mortem outputs, edible/unsafe/alchemical/magical-culinary/crafting roles, harvest difficulty, tools/knowledge, preservation, contamination, affinities/effects, substitutions and signature exact-creature ingredients. Produce explicit coverage-gap records where source creatures lack sufficient anatomy/harvest evidence rather than fabricating missing facts.

### ICF-10 — Preparation, Processing & Derived Ingredients
Define deterministic transformations such as grain→flour, milk→cream/butter/cheese, herb→dry/powder/extract/tincture, fruit→juice/syrup/wine/vinegar, seed→oil/meal, bone→stock/gelatin/ash and magical raw material→distillate/essence/crystallized extract while retaining lineage to primary ingredients.

### ICF-11 — Alchemical Ingredient Rules & Formula Grammar
Reconcile the approved alchemy rules into computable ingredient roles, rarity/identification/harvest/preparation/quality/catalyst/stabilization/substitution/research behavior and a governed formula grammar such as base/solvent + active + modifier + catalyst + stabilizer + optional enhancer. Recipes may require either property/effect thresholds or exact signature ingredients where explicitly authored.

### ICF-12 — Culinary & Magical Culinary Rules
Reconcile ordinary Cooking, ingredient quality, preparation/technique, food effects, alchemical cooking, elemental cooking, experimental cooking, signature recipes, dimensional cuisine, reality-bending cuisine, preservation and enchantment overload into one coherent deterministic hierarchy. Recipes may use broad ingredient-property requirements or exact named ingredients where the authored recipe is intentionally unique.

### ICF-13 — Agriculture, Foraging, Husbandry & Production Integration
Bind crop fields, greenhouses, orchards, hydroponics, magical agriculture, foraging zones, livestock, fisheries, apiaries, monster husbandry and other production facilities to stable ingredient IDs, deterministic yield/quality and preservation/storage without generic untyped “units”. Expose long-running and repeated production/harvest work through existing Downtime/Project activity seams with explicit time, facilities, inputs, outputs and complications.

### ICF-14 — Recipe Corpus & Recipe-Generation Foundation
Build substantial first-party ordinary meals, cultural/regional dish templates, preservation recipes, beverages, baked goods, stocks/sauces, enchanted/elemental/survival/alchemical foods and potion/tonic/elixir/poison/oil/salve/powder/reagent recipes, plus governed compositional rules that can support large coherent recipe families.

### ICF-15 — Content Packs, Validation, Search & Workbench
Publish deterministic ingredient/recipe/creature-harvest packs; duplicate/alias/property/reference/range/compatibility validation; creature-harvest coverage reporting; search/facets; Ingredient, Recipe and Creature Harvest inspectors; source/provenance display; cross-system fixtures; Downtime/Cozy eligibility metadata validation; Windows/Linux deterministic compilation and evidence.

## 6. Downtime and Cozy integration rule

ICF activities that take meaningful in-world time or repeat as routines must reuse the existing Downtime/Project model rather than create an ICF scheduler. Farming, husbandry, foraging, harvesting, butchery, preservation, processing, cooking, brewing, alchemy and production may expose typed activity/project definitions with prerequisites, facilities, inputs, time, checks/choices, progress, complications and outputs.

ICF definitions may declare whether a particular operation is *eligible to be considered* for bounded Cozy automation, but ICF never grants automation authority. Cozy/APM must still apply its existing delegation, fresh authorization, resource budget, version, ownership, stop-condition and human/GM-choice rules. Routine deterministic work may run one step, until the next meaningful choice, or in an explicitly bounded batch/background profile where already authorized. Wall-clock time does not become game progress merely because Cozy is running.

## 7. Content scale target

The first-party foundation should target roughly 700–1,000 primary ingredients plus approximately 300–500 derived preparations, with broad mundane, botanical, animal/aquatic, mineral/basic reagent and magical/multiversal coverage. Counts are planning targets, not permission to fabricate unsupported setting-specific lore; source-derived entries retain source provenance and newly authored generic content is marked governed first-party authoring.

## 8. Placement and dependency rule

Effective implementation order is:

`MIB-13 → ICF-01 → ICF-02 → ICF-03 → ICF-04 → ICF-05 → ICF-06 → ICF-07 → ICF-08 → ICF-09 → ICF-10 → ICF-11 → ICF-12 → ICF-13 → ICF-14 → ICF-15 → MIB-14`

ICF is not selected while MIB-13 is unfinished. MIB-14 does not begin until ICF completion unless the owner explicitly re-routes the roadmap.

## 9. Boundaries

- No parallel inventory, creature, crafting, cooking, alchemy, World, economy, Downtime/Project or Cozy truth ledger.
- Creature harvest profiles must reference canonical creature definitions and canonical output definitions.
- Generic part/type affinities are reusable tendencies and proposal inputs, not authority to fabricate unsupported creature anatomy or lore.
- Potential harvestability never silently grants edibility, legality, sapience/cultural acceptability or safety.
- Existing source names, classifications and provenance are preserved in the reconciliation layer rather than silently overwritten.
- ICF may expose Downtime/Cozy eligibility metadata but may not widen APM delegation, automate human/GM choices, infer consent, or turn wall-clock elapsed time into game progress by default.
- No production database/search/AI provider selection.
- No real-money/payment integration.
- Migration 0022 remains unreserved unless a selected tranche proves a genuine durable schema delta.
- Later SMB-08 Core Content Production remains the place for broad continuing first-party content expansion after the foundation is established.
