# ICF-13 — Agriculture, Foraging, Husbandry & Production Integration

Status: IMPLEMENTATION CANDIDATE  
Work item: ICF-13  
Source evidence: `MV_Master_01_Core/02_PDF_Sources/Part 1/Downtime/Agriculture Base Add-on.PDF`  
Source SHA-256: `576ec3b8e82177d252428073879113c51bbb8cf116e3878597b0e478e2961e0d`

## Decision

ICF-13 turns the existing ingredient libraries and Agriculture source into a **typed production integration layer**, not a second inventory, scheduler, economy, creature-harvest system, or Cozy simulator.

Agriculture/foraging/husbandry work is represented as existing Downtime/Project activity. A production task can name facilities, prerequisites, checks, Campaign-time blocks, hazards, source yield expressions and canonical output definitions, but the final quantity/quality/condition/ownership mutation is committed by the owning Asset/inventory domain.

## What is now deterministic

- source Base Turns are abstract authored Project time blocks; wall-clock time never advances production;
- crops use the source three-stage Early → Mid → Mature cycle where that source rule applies;
- source Growth and Harvest outcome bands, acreage/zone health, restoration, hazard ranges and source yield modifiers are preserved;
- the seven source Foraging Zone types, three farm-zone types, agricultural structures/modules/upgrades, portable modules, storage and trade facilities are represented as production capabilities rather than new global object truth;
- source outputs are cross-walked to canonical ingredient IDs when an existing definition is actually available;
- husbandry, aquaculture, apiary and monster-husbandry use the canonical `husbandryEligible`/acquisition/creature seams and require an authored quantity rule before an executable output commit;
- raw harvested-good spoilage is preserved as Agriculture scope and kept separate from ICF-12 finished-food preservation;
- MIB-13 remains current price/scarcity/sale authority, MIB-12 crafting, ICF-10 processing, ICF-11 alchemy, ICF-12 culinary, ICF-07/09 creature harvest/crosswalk, and D17 live Asset state.

## Important fail-closed reconciliations

1. **No universal yield invention.** ICF-03 and ICF-05 deliberately avoided world/species universal yields. ICF-13 therefore requires a typed yield rule per executable production profile. Source examples may be preserved even when their units cannot yet be converted into a canonical quantity.
2. **Animal Pen is typed, not quantified.** Existing source evidence names weekly meat, milk, wool and leather. These bind to `ingredient:animal-meat`, `ingredient:animal-milk`, `ingredient:animal-wool` and `ingredient:animal-leather`, but exact species and quantities remain unasserted; leather processing remains ICF-10-owned.
3. **Foraging generic/material outputs stay honest.** Hardwood Bundles, Insect Carapaces, Mineral Sample, Colorful Feathers, Fur Pelt and Obsidian Shard are not forced into invented ingredient IDs.
4. **Source-count expressions are not mass conversions.** `2d6 Medicinal Herbs`, `1 Fire Blossom`, `200 units Wheat`, etc. remain source-native yield expressions unless a governed unit/conversion rule makes an Asset quantity commit legal.
5. **No quality invention.** Enhanced growth/harvest increases source yield. It does not automatically assign a named D17 quality tier.
6. **No automation grant.** Drones, golems, distribution terminals and source automation only satisfy capabilities inside an already-authorized Project step. They do not create background progression, automatic spending/sales, or Cozy/APM authority.
7. **Economy stays MIB-13.** Source CR values, “50% market cost,” automated sales and +10% income are source assertions/modifiers routed to MIB-13, never a parallel ICF market ledger.
8. **Effects stay with downstream owners.** Agriculture examples of food buffs, elemental crop properties, potion uses and magitech effects do not bypass ICF-11/12/MIB-12 or live-instance authority.

## Source defects retained rather than repaired

The retained PDF visually clips several crop names in its sample crop/value tables and refers to a full crop Appendix that is not present in the 22-page file. Earlier governed ICF-03/06 source assertions already preserve Wheat, Fire Blossom and Etherleaf. ICF-13 reuses those mappings and does not reconstruct clipped labels or fabricate the missing appendix.

## Artifacts

- `ICF-13_PRODUCTION_RULES.json`
- `ICF-13_SOURCE_OUTPUT_BINDINGS.json`
- `ICF-13_REFERENCE_FIXTURES.json`
- `ICF-13_SYSTEM_VALIDATOR.py`
- `ICF-13_VALIDATION_SUMMARY.json`
