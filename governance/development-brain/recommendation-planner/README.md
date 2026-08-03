# Recommendation and Task Planner

## Purpose

This derived planner converts validated Development Brain priorities into explainable recommendations and bounded task proposals without editing source content or overriding owner and governance authority.

## Inputs

- Unified Object Inventory
- Dependency Graph
- Structure Intelligence
- Completion and Readiness Engine
- Priority and Impact Engine

## Classifications

Every recommendation is classified as exactly one of:

- `executable` — bounded governed work may be proposed;
- `owner-decision` — an explicit owner decision is required before implementation;
- `blocked` — prerequisites must be resolved before implementation;
- `observation-only` — retain and reassess when upstream evidence changes.

## Task contract

Tasks include stable IDs, deterministic sequence, a concrete action, a bounded outcome, and an `executionAllowed` safeguard. Non-executable classifications cannot contain executable tasks.

## Governance boundaries

- Recommendations and tasks are advisory only.
- The planner does not assign people or agents.
- The planner does not schedule work.
- The planner does not mutate, promote, certify, or silently repair source content.
- Owner decisions and governance records remain authoritative.
- Governed execution still requires the normal repository approval, validation, and evidence process.

## Validation

`validate-recommendation-planner.mjs` checks stable identities, contiguous ranks, valid classifications, bounded tasks, prerequisites, evidence, summary consistency, and authority safeguards.

The CI workflow generates and publishes `aioc-recommendation-planner` as the governed Step 7 artifact.
