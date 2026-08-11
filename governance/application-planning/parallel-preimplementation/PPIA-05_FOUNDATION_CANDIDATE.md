# PPIA-05 — Foundation Candidate

**Work item:** PPIA-05 — Species, Forms & Character Biology  
**State:** FOUNDATION CANDIDATE — NOT A VERIFIED MILESTONE UNTIL EXACT-HEAD VALIDATION AND MERGE  
**Owner:** John Brandon Turner

## Candidate contents

This bounded foundation candidate contains:

- `PPIA-05_SOURCE_AND_DESIGN_INVENTORY.md`;
- `PPIA-05_SPECIES_FORMS_BIOLOGY_TAXONOMY_v0.1.0.json`;
- `PPIA-05_ABILITY_BIOLOGY_ROUTING_v0.1.0.json`;
- `scripts/validate-ppia05-foundation.py`;
- `.github/workflows/validate-ppia-05-foundation.yml`.

## Verified source-accountability targets encoded by the candidate

- 29 direct Species/Form/Biology PDFs / 654 pages;
- 6 supporting environment/Adaptation PDFs / 233 pages;
- governed 2,203-row mixed Species/Elementalist/Innate Ability dataset;
- 260 Species Perks, 539 Innate Abilities, and 1,404 Elementalist rows kept distinct for ownership classification;
- governed 1,018-row prestige/environment/special Ability dataset with 296 Environment-Based Ability Collection rows used only as an Adaptation/classification cross-check;
- 60 detailed Shapeshifter Abilities and 57 pricing-only source rows, with zero automatic merges;
- 13 Species/Form/Biology identity/state layers;
- 12 presentation profiles;
- culture-versus-biology separation;
- explicit Character, Creature, Item/Asset, appearance, environment-authoring, balance, and world-setting handoffs.

## Non-promotion and non-activation boundary

This candidate does not:

- modify source PDFs or raw CSVs;
- create canonical Species/Form Definitions from dataset membership;
- classify all Species Perks as physiology;
- classify all Innate Abilities as biology;
- classify environment perks as biological Adaptations without explicit evidence;
- merge Shapeshifter pricing-only rows with detailed Abilities by name/tier/similarity;
- convert culture, philosophy, society, belief, profession, equipment, temporary Effects, or Campaign environment into permanent source biology;
- implement application runtime;
- activate STAGE-A-A2;
- authorize release, deployment, tester access, paid services, production credentials, or unsupported canonical promotion.

## Milestone gate

The foundation may be treated as a verified PPIA-05 milestone only after the exact PR head passes the PPIA-05 Foundation validator plus all applicable repository-wide continuity/regression gates and the PR merges into canonical `main`. Post-merge checkpoint projection must then record the exact validated head, PR, merge SHA, and next PPIA-05 substep.
