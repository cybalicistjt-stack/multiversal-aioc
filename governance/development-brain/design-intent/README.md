# Design Intent Memory

Release E Step 13 preserves explicit reasons behind governed systems and decisions without inventing rationale.

## Inputs

- `governance/development-brain/memory/AIOC_PROJECT_MEMORY.json`
- generated Unified Object Inventory

## Output

`AIOC_DESIGN_INTENT.generated.json` contains stable intent records and explicit unresolved subjects.

Each intent preserves:

- subject identities;
- title and goal;
- intended outcome;
- problem addressed;
- documented tradeoffs;
- documented rejected alternatives;
- invariants;
- extension notes;
- authority and confidence;
- source evidence.

Empty arrays mean the governed source does not document that field. They are not invitations for an AI to fill the gap silently.

## Derivation boundary

An intent may only be generated from an active governed project-memory entry that contains both an explicit summary and rationale. Object names, code layout, implementation details, lexical similarity, and model preference cannot establish design intent.

Inventory subjects without explicit linked rationale remain unresolved. The artifact is derived and advisory; it cannot mutate, promote, certify, approve, assign, or schedule work.
