# Priority and Impact Engine

## Purpose

This derived engine ranks actionable Development Brain work without editing source content or overriding owner and governance authority.

## Inputs

- Unified Object Inventory
- Dependency Graph
- Structure Intelligence
- Completion and Readiness Engine
- Governed memory references carried by inventory objects

## Ranking components

Each object receives a deterministic 0–100 priority score based on:

1. readiness deficit;
2. dependency centrality;
3. blocker propagation;
4. structural impact;
5. evidence gap;
6. governed-priority signal;
7. estimated unlock value.

The result includes a stable priority ID, deterministic rank, tier, component scores, reasons, evidence, and an explicit advisory safeguard.

## Governance boundaries

- Rankings are advisory only.
- The engine does not edit, promote, certify, schedule, or assign source objects.
- Owner-approved and governance-recorded priorities may influence ranking, but derived ranking cannot supersede them.
- Missing evidence and conflicts remain visible findings rather than silent repairs.
- Equal scores are ordered by stable ID for reproducibility.

## Validation

`validate-priority-impact.mjs` checks identity uniqueness, deterministic ordering, score ranges, tiers, complete components, evidence, summary consistency, and the advisory authority rule.

The CI workflow generates and publishes `aioc-priority-impact` as the governed Step 6 artifact.
