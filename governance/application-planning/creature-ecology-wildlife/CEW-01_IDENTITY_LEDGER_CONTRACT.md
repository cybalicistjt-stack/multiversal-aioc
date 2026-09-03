# CEW-01 — Creature Source Census & Identity Ledger Contract

**Contract ID:** `CEW-ID-1.0`  
**Work item:** CEW-01 — Creature Source Census & Identity Ledger  
**Authority:** governed content/recovery/provenance only; no application implementation authority.

## Purpose

CEW-01 establishes a source census and identity-state ledger without pretending that every creature-like source fragment is already a canonical Creature Definition. It preserves the distinction between current governed definitions, source-backed records that can be recovered later, formally deferred R1 candidates, unresolved semantic/GPT review evidence, and source systems explicitly rejected as creature-identity authority.

The census is an accountability layer, not a mass-promotion step.

## Identity states

### `canonical_definition`

A stable currently governed `mv.object.creature-definition` identity in the canonical content index.

A canonical Definition may still be incomplete relative to the retained PDFs. Canonical identity does not prove complete ecology, complete mechanics, complete source coverage, or broad World distribution.

### `recoverable_source_record`

Source-backed creature/statblock evidence from the retained creature corpus that has not been separately normalized and bound to a governed Creature Definition.

Recoverability is not promotion. The ICF-09 source evidence remains unbound until separately normalized.

### `formally_deferred_source_candidate`

A PPIA-02/R1 candidate whose source identity and coordinates are provenance-accounted but whose public-canon disposition remains open.

Formal deferral is neither canonical promotion nor exclusion.

### `unresolved_recovery_candidate`

Noncanonical semantic/GPT/review evidence or a possible identity relationship whose binding cannot be established from current authority.

A review packet, confidence score, matching name, pluralized heading, or nearby text does not establish identity.

### `rejected_identity_authority`

A source/system explicitly excluded from Creature/NPC content authority. The earlier unsuccessful 487-object semantic-parse database is retained only as historical/compatibility evidence and cannot seed canonical creature identity.

## Duplicate and alias rules

CEW-01 permits identity collapse only when one of these is true:

1. the records already carry the exact same governed stable ID; or
2. explicit source/governance evidence establishes an alias or identity-equivalence relationship.

Name similarity alone never establishes creature identity. The following are insufficient by themselves:

- case-insensitive or normalized-name equality;
- singular/plural resemblance;
- shared CR, size, type, stat block, ability, or description;
- semantic similarity;
- source proximity;
- a GPT/recovery confidence score;
- an inferred relationship between a stage, form, template, modifier, summoned state, or playable conversion and a base creature.

Accordingly, CEW-01 records **zero confirmed duplicate merges and zero confirmed alias bindings**. This is conservative by design. CEW-02 and later tranches may establish supported taxonomy or relationships without retroactively pretending CEW-01 had identity evidence it did not have.

## Current canonical catalog

`content-db/indexes/by-type.json` currently contains 27 governed `mv.object.creature-definition` IDs. Those IDs are the canonical-definition set for this census.

The sparse bodies of legacy creature-definition objects are not treated as complete source truth. Original retained sources remain source evidence for later recovery.

## Retained source corpus

The retained dedicated creature corpus contains 23 Creature PDFs. ICF-09 records:

- 826 source statblock evidence records;
- 324 source-signature candidates;
- 878 candidate starts across the per-document scan.

These counts describe source evidence, not 826 or 324 new canonical identities.

`Player Creatures.PDF` is inventoried separately because it defines a source-to-playable conversion procedure. A playable result is not identity-equivalent to the source creature instance/Definition.

## R1 formal deferrals

PPIA-02 recovered 93 formally deferred creature candidates. Their exact row-level identity/source/page/heading ledger remains:

`governance/application-planning/parallel-preimplementation/PPIA-02_R1_DEFERRED_CREATURE_CANDIDATES.csv`

CEW-01 references rather than duplicates that row ledger. It does not quick-add, stat, normalize, auto-bind, or silently exclude those records.

The near-name case `Rift-Touched Animals (Optional)` versus canonical `mv.adventure.lost-key.creature.rift-touched-animal` remains unresolved. Pluralization and heading similarity do not establish an alias.

## Semantic, GPT and Evernote recovery

The current semantic-recovery evidence contains 18 creature-family direct-review candidates, 9 pending semantic-validation creature candidates, and 3 GPT diagnostic creature packets. These are noncanonical review/evaluation evidence and default to `unresolved_recovery_candidate`.

Current canonical repository search does not expose an independent Evernote creature identity ledger. CEW-01 therefore does not invent one. Evernote-labelled or legacy-source material that appears through governed R1/source-recovery evidence remains under the provenance/disposition state supplied by that evidence.

## Related sources

`Havalaea.PDF` supplies setting/world context; world-local creature claims remain world-scoped unless separately promoted.

`Animal training.PDF` supplies training/relationship context; it does not create base creature identities.

## Non-interference boundaries

CEW-01 does not:

- recover or normalize the creature-type taxonomy owned by CEW-02;
- infer habitat/ecology fields owned by CEW-04;
- infer canonical geographic distribution owned by CEW-05;
- invent intelligence, personhood, domestication, mount, pet, familiar or NPC capability;
- mutate `Multiversal-app` creature schemas, UI, runtime, migrations, encounter state, or companion systems;
- create a second creature catalog outside governed creature identity.

## Closeout

The source census and identity-state ledger are complete for CEW-01. The strict successor is **CEW-02 — Creature Type System Recovery & Taxonomy Audit**.
