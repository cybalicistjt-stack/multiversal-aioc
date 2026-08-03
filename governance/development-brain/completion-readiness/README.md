# AIOC Completion and Readiness Engine

Release B, Step 5 derives explainable readiness assessments from the unified inventory, dependency graph, and structure intelligence.

## Outputs

Each object receives:

- six dimension scores: identity, content, evidence, structure, dependencies, and governance;
- an overall score from 0 to 100;
- a status of `ready`, `review-ready`, `blocked`, or `incomplete`;
- explicit blockers and reasons;
- source evidence for every conclusion;
- a derived `promotionReady` signal.

## Governance boundary

`promotionReady` is advisory only. It never edits content, changes lifecycle state, performs promotion, or overrides owner approval. Canonical objects remain canonical; working objects remain governed working state until approved through the certified content pipeline.

## Determinism

The generated artifact is derived and reproducible. It is not hand-maintained and must not become a second content database.

## Validation

CI generates and validates all prerequisite artifacts, requires the readiness artifact to exist, validates internal consistency and authority rules, and publishes `aioc-completion-readiness` for inspection.

```bash
node scripts/development-brain/generate-completion-readiness.mjs tmp/AIOC_UNIFIED_INVENTORY.json tmp/AIOC_DEPENDENCY_GRAPH.json tmp/AIOC_STRUCTURE_INTELLIGENCE.json tmp/AIOC_COMPLETION_READINESS.json
node scripts/development-brain/validate-completion-readiness.mjs tmp/AIOC_COMPLETION_READINESS.json
```
