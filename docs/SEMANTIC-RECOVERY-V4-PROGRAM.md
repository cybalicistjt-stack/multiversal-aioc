# Semantic Recovery v4, Golden Corpus, Baseline Lock, and UI/UX Transition

Status: Implemented as a governed pipeline; measured convergence and owner certification remain required before baseline lock.

## Program sequence

1. Hierarchical section and layout reconstruction
2. Table, form, and key-value reconstruction
3. Document-family grammar classification
4. Object Assembly Engine
5. Object completeness scoring
6. Relationship assembly
7. Canonical candidate envelope generation
8. Stratified Golden Corpus annotation packet
9. Golden Corpus precision, recall, F1, duplicate, boundary, relationship, and schema evaluation
10. Parser convergence iterations without full-corpus rescans
11. Engineering baseline pass
12. Explicit owner certification
13. Semantic baseline lock
14. Begin UXC-001: AIOC UI/UX discovery and workflow inventory

## Object Assembly Engine

The unit of recovery is an assembled game object rather than a text chunk. Generic sections such as Actions, Traits, Origin, Objectives, Equipment, Effects, Variants, and Prerequisites attach to a parent object and cannot independently authorize an object identity.

Each assembled object includes:

- stable assembly ID;
- proposed object family;
- root and child evidence nodes;
- document grammar;
- section map;
- expected, present, and missing fields;
- completeness score;
- family scores and margin;
- full provenance;
- non-canonical authority status.

## Document grammars

Dedicated grammars exist for rules, abilities, creatures, items, species, NPCs, vehicles, environments, worlds, factions, and adventures. Each grammar defines required and expected sections. Completeness is measured against the relevant grammar rather than one generic schema.

## Relationship assembly

Typed relationships include requires, locatedIn, belongsTo, and usedBy. Scalar mechanics such as DC values, distances, dice expressions, durations, XP, and currency cannot become relationship targets. Exact aliases may resolve automatically; unresolved targets remain review work.

## Canonical candidate builder

Every candidate receives the common Multiversal envelope:

- stable ID, type, and name;
- lifecycle status and authority note;
- structured specification;
- relationships;
- provenance;
- recovery completeness and missing fields;
- validation gates;
- review route.

No v4 process imports or merges candidates into canon automatically.

## Golden Corpus

The automated packet samples up to twenty candidates per surviving family. A record becomes part of the measured Golden Corpus only after an expert checks the source and marks it verified. The verified manifest is version controlled at `audit/golden-corpus-v4.json`.

The Golden Corpus must contain at least twenty-five verified records across at least five object families before convergence can pass. This is an initial engineering floor, not the final target. The long-term target remains a broad representative corpus including positive, negative, boundary, table, relationship, and duplicate cases for every family.

## Convergence gates

The current minimum measured gates are:

- precision at least 0.90;
- recall at least 0.80;
- F1 at least 0.85;
- verified corpus exists;
- at least five verified object families;
- all pipeline stages successful;
- complete provenance;
- schema-valid canonical envelopes;
- no scalar relationship violations.

Future convergence iterations should add boundary accuracy, field-level accuracy, relationship precision/recall, duplicate rate, and table reconstruction accuracy as the annotated corpus grows.

## Baseline lock

The semantic baseline locks only when both conditions are true:

1. `engineeringConvergencePassed` is true in the Golden Corpus evaluation.
2. `ownerCertified` is true in the versioned Golden Corpus manifest.

A successful workflow run alone is not sufficient.

## UI/UX Consultancy transition

When baseline lock is true, the generated lock status changes the UI/UX Consultancy phase to `ready-to-start`. The first active stage is UXC-001: discovery and workflow inventory. Until then, major navigation redesign remains blocked to avoid designing around unstable semantic data.

## Operational outputs

Compact outputs publish under `v2/audit-data/semantic-recovery-v4/`. Full assembled objects, canonical candidates, Golden Corpus packet, and evaluation details remain in the workflow artifact.
