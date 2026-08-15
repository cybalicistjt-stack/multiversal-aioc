# Multiversal Item Taxonomy & Catalog System — Internal Alpha Integration Handoff

**Package version:** 0.12.0  
**Preparation status:** COMPLETE FOR SHELVING / NOT PRODUCTION-INTEGRATED  
**Master source snapshot SHA-256:** `c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec`

## Purpose

This handoff converts Item Steps 1–11 into an implementation-ready Internal Alpha package. It is designed so a later implementation team can execute the item taxonomy/catalog subsystem without re-solving universal item classification, setting/genre facets, intrinsic-vs-affinity semantics, compatibility inference, product identity, creator/origin modeling, source recovery, coverage analysis, content enrichment, or functional coverage-profile policy during the live build.

## Authority and quarantine

`PREPARATION_BOUNDARY.md` remains binding. At implementation time, current GitHub repository evidence, bootstrap/governance, roadmap, schemas, migrations and runtime authorities supersede snapshot implementation facts in this package. This package does **not** authorize current-build changes by itself.

## Prepared subsystem

1. Universal Item Taxonomy: 10 independent axes / 171 controlled values layered beside protected domain-native mechanics.
2. Setting/content facets: setting family, genre tradition, era, technology, power, environment, play domain, tone and content scale.
3. Intrinsic vs. affinity vs. compatibility semantics with four-dimensional context compatibility and explicit exceptions.
4. Product identity graph from generic concepts through families/lines/models/variants/configurations without automatic name merges.
5. Shared Creator Entity + brand/culture/origin relationships; generic items never require invented manufacturers.
6. Read-only source/current crosswalks and provenance recovery, including Armor & Shields and Materials source concepts.
7. Read-only coverage analyzer across 35 functional domains and setting/facet dimensions.
8. Content enrichment/re-mechanization workflow: preserve current mechanics by default; build missing source concepts under verified current rules.
9. Composable Item Coverage Profile Library: 28 profiles × 35 domains = 980 qualitative expectations with 9 satisfaction modes; **not quotas**.
10. A8 integration boundary: product/catalog definitions may feed A8 definitions/snapshots, while A8 remains sole authority for item instances and inventory state.

**Source/legacy mechanics are non-authoritative.** They preserve intent/provenance only and cannot be promoted by direct numeric conversion.

## Integration strategy

Use **expand → project → validate → review → enable**:

- expand persistence with dormant additive structures;
- seed stable controlled registries and coverage profiles;
- project current records into shadow metadata without source mutation;
- import source evidence/recovery queues as review-only provenance;
- run validators in shadow mode;
- adopt reviewed taxonomy/product/creator metadata in governed batches;
- enable compatibility and coverage read surfaces before authoring;
- enrich/re-mechanize only through current domain rules and acceptance gates;
- integrate governed definitions with A8 last, without duplicating A8 runtime state.

## Current preparation evidence

- Current item records: **5,389**.
- Current records with minimum domain-defining mechanics/effect fields: **5,389 / 5,389**.
- Current source-linked provenance occurrences: **1,050**.
- Recovered Armor & Materials source concepts: **55**.
- Recovered concepts absent from current catalogs and requiring future current-rule build: **54**.
- Full enrichment/re-mechanization queue: **5,443** work items.
- Universal item taxonomy controlled values: **171** across **10** axes.
- Setting/content facet controlled values: **241** across **9** facets.
- Coverage domains: **35**.
- Composable coverage profiles: **28**.
- Coverage expectation rows: **980**.
- Current setting-family profile evidence review cells with no current analytical evidence at supporting-or-higher importance: **67**; these are review signals, not content mandates.

## Files implementing this handoff

- `IA_ITEM_FUTURE_DATA_MODEL_MANIFEST.csv`
- `IA_ITEM_DEPENDENCY_MAP.csv`
- `IA_ITEM_FEATURE_GATE_CONTRACT.md`
- `IA_ITEM_MIGRATION_SEQUENCE.csv`
- `IA_ITEM_ROLLBACK_PLAN.md`
- `IA_ITEM_VALIDATOR_REGISTRY.csv`
- `IA_ITEM_ACCEPTANCE_MATRIX.csv`
- `IA_ITEM_IMPLEMENTATION_SEQUENCE.csv`
- `IA_ITEM_UI_SEARCH_FILTER_REQUIREMENTS.csv`
- `IA_COVERAGE_SATISFACTION_ASSERTION_SCHEMA.csv`
- `IA_ITEM_TEST_FIXTURES.jsonl`
- `IA_ITEM_FIXTURE_EXPECTATIONS.csv`
- `IA_ITEM_HANDOFF_MANIFEST.json`
- `STEP12_ITEM_INTEGRATION_BASELINE.md`
- `STEP12_ITEM_VALIDATION_REPORT.json`
- `tools/validate_item_step12.py`

## Implementation-time mandatory refresh

Before IA-I0, re-read the current repository bootstrap, roadmap, current item/A8/Economy/crafting/domain schemas, migrations, tests, permissions model, search/indexing architecture, offline/save-load contracts and current source/catalog storage. Do not freeze implementation syntax, ORM/table names, migration numbers or UI components from this preparation snapshot.

## Prepared-complete definition

The item preparation series is ready to shelve when:

- every future entity has a persistence/authority boundary;
- migration is additive and rollback-safe;
- feature gates default off;
- validators protect source data, IDs, domain-native mechanics, compatibility semantics, provenance, A8 and Economy boundaries;
- deterministic fixtures cover known dangerous cases and prior analyzer false positives;
- coverage profiles remain qualitative/non-quota and support non-item satisfaction;
- current records are not unnecessarily re-mechanized;
- the 54 missing Armor/Materials concepts have a governed future build path;
- no current-build artifact has been modified.

Step 12 satisfies those preparation conditions subject to `STEP12_ITEM_VALIDATION_REPORT.json`.
