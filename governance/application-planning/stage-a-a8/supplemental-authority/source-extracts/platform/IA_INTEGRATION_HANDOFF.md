# Multiversal Platform & Catalog v2 — Internal Alpha Integration Handoff

**Package version:** 0.11.0  
**Preparation status:** COMPLETE FOR SHELVING / NOT YET PRODUCTION-INTEGRATED  
**Current source bundle SHA-256:** `52f94512bdfab406c9c35cb5a6b438757518cc506e1d8f7caee9083040fcbd9a`

## Purpose

This handoff converts the completed preparation tranches into an implementation-ready Internal Alpha package for spacecraft, mecha, and vehicles. It is designed so the later implementation team can execute the subsystem without re-solving taxonomy, creator identity, lineage, market/history, model-vs-asset separation, legacy extraction, coverage analysis, or re-mechanization policy during the live build.

## Authority and quarantine

`PREPARATION_BOUNDARY.md` remains binding. Current repository evidence at implementation time supersedes this snapshot for branch/status/schema facts. This package does **not** authorize current-build changes.

## Prepared subsystem

The future subsystem consists of:

1. Universal platform taxonomy layered beside protected domain-native classes/scales.
2. Persistent creator/manufacturer ecosystem with typed catalog boundaries.
3. Product-family/platform/model/variant/trim lineage graph.
4. Contextual market, availability, access, service, parts, and production-history metadata.
5. Factory configuration separated from individual asset state.
6. Individual asset identity, provenance, ownership, condition, modification, maintenance, and history.
7. Legacy source/concept preservation and governed current-rule re-mechanization; **legacy mechanics are non-authoritative** and cannot be promoted by direct conversion.
8. Read-only coverage analysis for portfolio and content-gap review.

## Integration strategy

Use an **expand → project → validate → review → enable** sequence. Do not begin by modifying the existing CSVs or making new fields required.

- Expand persistence with dormant additive structures.
- Seed stable controlled registries.
- Project current records into v2 structures without mutation.
- Import legacy evidence as review-only provenance.
- Run all validators in shadow mode.
- Adopt reviewed metadata in small governed batches.
- Expose read surfaces before write surfaces.
- Execute re-mechanization only after current mechanics anchors are verified.
- Activate individual assets last, after runtime dependencies are ready.

See `IA_MIGRATION_SEQUENCE.csv` and `IA_IMPLEMENTATION_SEQUENCE.csv`.

## Current preparation evidence

- Current catalog records inventoried: **5,628**.
- Current platform/model records analyzed by the read-only analyzer: **2,984**.
- Legacy source pages covered: **11/11**.
- Legacy source occurrences structured: **367**.
- Legacy concept identities resolved: **326**, with **1 deliberately unresolved vague concept**.
- Legacy product seeds retained: **244**.
- Re-mechanization work queue: **326** items, including **244 future candidates**, **81 current-ancestry reconciliations**, and **1 identity hold**.
- Current catalog fields assessed for individual-asset state: **221 fields; zero require reinterpretation as instantiated asset state**.

## Skiff invariant

Skiff is a specialist creator of **personal-sized spacecraft**, plus the single **H1v3 Model S Space Station** exception. Generic uses of the noun *skiff* are not manufacturer references. No later implementation may infer a broader Skiff catalog without explicit owner-approved canon.

## Files that implement this handoff

- `IA_FUTURE_DATA_MODEL_MANIFEST.csv`
- `IA_DEPENDENCY_MAP.csv`
- `IA_FEATURE_GATE_CONTRACT.md`
- `IA_MIGRATION_SEQUENCE.csv`
- `IA_ROLLBACK_PLAN.md`
- `IA_VALIDATOR_REGISTRY.csv`
- `IA_ACCEPTANCE_MATRIX.csv`
- `IA_IMPLEMENTATION_SEQUENCE.csv`
- `IA_TEST_FIXTURES.jsonl`
- `IA_FIXTURE_EXPECTATIONS.csv`
- `IA_HANDOFF_MANIFEST.json`
- `STEP12_INTEGRATION_BASELINE.md`
- `STEP12_VALIDATION_REPORT.json`
- `tools/validate_step12.py`

## Implementation-time mandatory refresh

Before executing IA-0, re-read the then-current repository bootstrap, roadmap, schemas, migrations, tests, permissions model, and catalog storage. Any current implementation fact in this package is a snapshot, not an instruction to override newer repository state.

## Definition of prepared-complete

This preparation series is ready to shelve when:

- every future entity has a persistence/authority owner;
- migration order is additive and reversible;
- rollback behavior is explicit;
- validators cover identity, provenance, lineage, market, legacy, and asset boundaries;
- deterministic test fixtures cover known dangerous cases;
- feature gates prevent accidental activation;
- no current-build artifact has been modified.

Step 12 satisfies those conditions subject to the included validation report.
