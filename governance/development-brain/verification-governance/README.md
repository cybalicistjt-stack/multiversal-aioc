# Verification and Governance Integration

## Purpose

This layer verifies Step 7 recommendations and task proposals against evidence, prerequisites, lifecycle compatibility, authority constraints, approval requirements, and executable eligibility.

## Verification statuses

- `verified-executable` — proposal checks pass; normal governed repository approval and validation still apply.
- `requires-approval` — owner or governance approval is required before execution eligibility can be established.
- `blocked` — one or more prerequisites, evidence requirements, or compatibility checks fail.
- `observation-only` — no execution is proposed.

## Governance boundaries

- Verification records are advisory and auditable.
- Verification does not execute, assign, schedule, mutate, promote, or certify source content.
- Owner decisions are never inferred or substituted.
- A verified-executable record is not permission to bypass repository review, CI, or owner/governance controls.
- Failed checks remain explicit findings and are never silently repaired.

## Validation

The validator checks stable identities, deterministic order, complete check sets, classification compatibility, approval rules, evidence presence, summary consistency, and advisory authority safeguards.

The CI workflow generates and publishes the `aioc-verification-governance` artifact.
