# ICF-05 — Livestock, Animal & Aquatic Ingredient Library

Status: IMPLEMENTED — validation pending repository gate

## Purpose

ICF-05 establishes reusable mundane animal-derived and aquatic ingredient identities on the ICF-02 canonical ingredient schema. It supplies ordinary food and crafting inputs needed by cooking, trade, husbandry, aquaculture, crafting, later recipe work and Cozy/Downtime production without creating a second inventory, economy, creature, or harvest authority.

## Library scope

The deterministic source materializes **234 primary ingredient definitions**:

- 26 livestock/game meat identities, including the generic source-backed `ingredient:animal-meat`;
- 20 poultry/game-bird meat identities;
- 11 raw milk identities, including source-backed `ingredient:animal-milk`;
- 16 egg identities;
- 23 fiber/hide/secretion identities, including source-backed `ingredient:animal-wool` and `ingredient:animal-leather`;
- 30 freshwater fish identities;
- 45 marine fish identities;
- 20 crustacean identities;
- 25 mollusk/cephalopod identities; and
- 18 other aquatic animal ingredients including roe and ordinary aquatic foods.

This yields **138 aquatic definitions** and **96 terrestrial/husbandry definitions**.

## Source-backed Animal Pen seam

The master `Bases_Facilities.csv` Animal Pen row explicitly lists weekly **meat, milk, wool, or leather** output. ICF-05 preserves those exact generic source terms as hybrid definitions. It does **not** infer species, per-animal yields, butchery procedures, quality grades, current prices, legality, cultural acceptability, or anatomy from that row.

`ingredient:animal-leather` carries an explicit processing-lineage coverage gap because the source lists leather as a direct facility output but does not author hide-to-leather processing. ICF-10 must reconcile that legacy output with derived-preparation lineage rather than silently inventing a tanning chain here.

## Governed first-party mundane coverage

The remaining 230 definitions are governed first-party mundane baseline identities. Species-named meat, milk, egg, fish and shellfish records are reusable ingredient definitions only. They do not assert that every world contains the source animal, that every culture eats it, that trade is legal everywhere, or that a creature instance yields a particular amount. World presence remains governed by authored setting/world bindings; current availability and price remain market-scoped.

Entries with significant preparation, conservation, legal, or cultural variability use `conditional` edibility where appropriate. No universal legality flags are authored.

## Authority boundaries

- **D17 Asset Instance** owns live quantity, ownership, quality, condition, reservation and consumption state.
- **MIB-13** owns current prices, market scarcity, merchant/service availability and transaction settlement.
- **MIB-11** owns World/Reality identity and scope.
- **ICF-06** owns magical, exotic and multiversal ingredient expansion.
- **ICF-07** owns creature-specific harvest and butchery procedures, anatomy evidence, harvest opportunities and yield resolution.
- **ICF-10** owns processing/derived-preparation lineage such as hide-to-leather, rendered fats, preserved meats, cured fish and dairy transformations.

ICF-05 does not create creature harvest profiles, harvest-yield rules, creature anatomy, magical culinary properties, alchemical effects, current price fields, owner state, or real-money behavior.

## Husbandry and aquaculture integration

Animal-product records may declare husbandry eligibility; aquatic records may declare a provider-neutral aquaculture facility tag. These flags make the definitions usable by later production integration. They do not grant automatic production, background simulation, or wall-clock progress. ICF-13 and existing Downtime/Project/Cozy authority remain responsible for governed production execution.

## Deterministic materialization

`ICF-05_LIBRARY_SOURCE.json` is the compact canonical source. `ICF-05_LIBRARY_MATERIALIZER.py` deterministically expands it into three logical packs and validates tranche invariants. Generated packs are reproducible artifacts and are not separate authority.

## Completion criteria satisfied by the content package

The package provides stable IDs, provenance/authorship, typed units, physical/husbandry/aquatic/culinary/crafting crossover metadata, preserves the explicit Animal Pen output seam, and keeps D17, MIB-13, ICF-06, ICF-07 and ICF-10 boundaries explicit. Final tranche completion still requires exact-head repository-health validation and merge evidence.
