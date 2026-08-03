# Semantic Ontology and Knowledge Graph

## Purpose

Step 10 adds a deterministic semantic layer over the Unified Object Inventory and Dependency Graph so AI integrations can retrieve meaning-bearing concepts and evidence-backed assertions rather than only raw records.

## Inputs

- Unified Object Inventory
- Dependency Graph

## Outputs

The generated artifact contains:

- semantic entities for inventory objects;
- concepts for explicit object types, authority layers, lifecycle states, packs, and relationship vocabulary;
- assertions connecting entities to concepts and other entities;
- confidence, inference method, and source evidence for every assertion;
- unresolved semantic findings where explicit support is absent.

## Derivation rules

Only two inference methods are permitted:

1. `field-mapping` — direct projection of explicit inventory fields;
2. `graph-projection` — projection of validated dependency-graph edges.

Names, lexical similarity, model intuition, and unstated domain assumptions do not create semantic claims.

## Governance boundaries

- All concepts and assertions are derived and advisory.
- Semantic output cannot mutate, promote, certify, assign, schedule, or reinterpret canonical content.
- Unknown meaning remains unresolved.
- Every assertion retains evidence and confidence.
- Canonical-versus-working authority remains visible.

## Validation

`validate-semantic-ontology.mjs` verifies stable unique identities, valid references, supported inference methods, evidence, confidence, advisory safeguards, summary consistency, and the unresolved-semantics policy.

The CI workflow generates and publishes `aioc-semantic-ontology` as the governed Step 10 artifact.
