# ICF-09 — Creature Catalog Harvest Crosswalk & Signature Ingredient Library

**Status:** implementation candidate  
**Work item:** ICF-09  
**Upstream:** ICF-02 canonical ingredient schema; ICF-06 creature-derived source gaps; ICF-07 harvest/butchery contract; ICF-08 part/type/trait tendency grammar; governed `content-db` creature definitions and source creature corpus.

## Purpose

ICF-09 connects the governed creature catalog to the ICF ingredient/harvest architecture without creating a second creature catalog or folklore-derived loot table. It distinguishes three evidence classes: canonical creature identity, authored anatomy/trait evidence, and authored harvest procedure/yield evidence. Only the third class can make an ICF-07 harvest profile executable.

## Canonical catalog result

The current `content-db/indexes/by-type.json` canonical creature-definition set contains **27 creature definitions**. `ICF-09_CANONICAL_CREATURE_CROSSWALK.json` covers all 27 exactly once.

The majority of canonical creature objects currently contain identity/provenance but no authored anatomy or harvest detail. Those entries deliberately remain `evidenceStatus: gap`, with no allowed harvest modes or outputs. Where additional governed evidence exists, ICF-09 records only what that evidence proves.

Examples of conservative bindings include:

- Sapcrawl Varnet: authored `Insectoid` taxonomy supports the ICF-08 `arthropod` body profile and authored chitinous glow-plates support the `scale-shell-chitin` part baseline.
- Jungle-Slip Beetle: authored `Insectoid`, acid-slick shell, and Deterrent Glands support `arthropod`, `scale-shell-chitin`, `gland`, and `acidic` tendency inputs.
- Rootstalker: `Beast (Plant-like)` and tough root-hide are preserved, but `Plant-like` is not silently promoted to the ICF-08 `plant` body profile. The generic plant-creature harvest rule in the source corpus is therefore not auto-applied.
- Rift-Touched Animal and Shadow Rift Entity use exact canonical action names as limited evidence where appropriate, while names such as `rift-touched` do not by themselves establish planar/anomalous anatomy or harvestability.

## Signature ingredient library

ICF-09 creates **7 canonical exact-creature signature ingredient definitions** where canonical identity plus authored part evidence support a stable ingredient identity:

1. Sapcrawl Varnet Chitin Plate
2. Mossling Glider Fur
3. Hisscap Frog Hide
4. Jungle-Slip Beetle Shell
5. Jungle-Slip Beetle Deterrent Gland
6. Rootstalker Root-Hide
7. Shadow Rift Entity Claw

These are ICF-02-shaped primary ingredient definitions. They bind exact canonical creature identity and authored part evidence, but **do not grant a harvest mode, deterministic yield, edibility, safety, legality, preservation rule, alchemical effect, or magical-culinary effect**. Their `creatureSource.evidenceStatus` is `partial`, and their ICF-07 executable harvest surface remains fail-closed until an authored/governed harvest profile supplies the missing procedure and output rules.

Each signature ingredient joins a part-class substitution group as `conditional` and an exact-creature signature group as `signature-exact-only`. This allows ICF-11/12 to define later functional/property-based substitution rules without erasing exact-signature recipe requirements.

## ICF-06 creature-derived gap reconciliation

The seven ICF-06 source-authored creature-derived identities remain explicitly unresolved where no exact canonical creature binding is supported: Basilisk Egg, Fire Salamander Tongue, Giant's Toenail, Lava Beetle Shell, Ogre's Blood, Phoenix Egg, and Phoenix Feather.

Name similarity is not reconciliation. In particular, `Lava Beetle Shell` is not bound to the canonical Jungle-Slip Beetle, and source-only basilisks/ogres do not silently become the generic source creature named by an ICF-06 ingredient.

## Source corpus coverage

The governed creature source corpus spans **23 PDF documents**. ICF-09's provenance/search layer records **826 parsed source statblock/evidence records** and **324 signature-part candidates**. These source-only records are deliberately *not* promoted to canonical creature-definition IDs. Five source records have exact current canonical name matches; all others remain `source-only-unbound` until a separately governed normalization step creates or maps canonical creature identities.

`Creature types.PDF` is retained as a source-family coverage gap because it does not expose safe individual statblock records through the parser. `Plant Creatures.PDF` contains an optional generic plant harvest system; that rule is retained as source evidence but is not assigned to Rootstalker solely from the phrase `Plant-like`.

## Authority and inheritance

ICF-09 consumes the established ICF-08 inheritance order:

`part baseline → body-plan/type → creature affinity/trait → explicit species/variant override → harvested-instance quality/condition`

This is an effect/tendency projection grammar, not an anatomy generator. Every part/body/trait binding in ICF-09 requires authored evidence. ICF-08 tendency tokens remain non-executable; ICF-11 owns exact alchemical formula/effect grammar and ICF-12 owns exact culinary/magical-culinary grammar.

ICF-07 remains harvest execution authority. A creature or ingredient can have authored anatomy and still have no executable harvest profile. D17 remains live Asset/output truth; MIB-13 remains current price and market-scarcity authority; MIB-11 remains World/Reality authority.

## Validation artifacts

- `ICF-09_CANONICAL_CREATURE_CROSSWALK.json`
- `ICF-09_SIGNATURE_INGREDIENT_LIBRARY.json`
- `ICF-09_SOURCE_COVERAGE.json`
- `ICF-09_SYSTEM_VALIDATOR.py`
- `ICF-09_VALIDATION_SUMMARY.json`

The detailed 826-record source-evidence index and 324-candidate signature index were used as noncanonical audit working evidence. Their counts and SHA-256 digests are retained in `ICF-09_SOURCE_COVERAGE.json`; they are intentionally not promoted into canonical repository truth. They cannot mutate runtime creature truth or authorize harvest outputs.

## Completion invariants

- all 27 canonical creature definitions are covered exactly once;
- source-only creature records are never silently promoted to canonical creature identity;
- ICF-08 type/trait tendencies never prove anatomy or exact effects;
- anatomy evidence alone never creates an ICF-07 harvest mode or yield;
- signature ingredients bind exact canonical creature identity and authored part evidence;
- ICF-06 unresolved creature-derived identities remain unresolved where no exact canonical match exists;
- no edibility, safety, legality, preservation, contamination or current-price fact is inferred;
- D17 remains live Asset authority and MIB-13 remains current price/scarcity authority;
- ICF-11/12 remain downstream exact-rule authorities;
- no migration `0022` is required or reserved.
