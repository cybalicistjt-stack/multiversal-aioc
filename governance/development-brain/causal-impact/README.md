# Causal and Impact Intelligence

## Purpose

This layer derives bounded, evidence-backed impact paths from the validated Semantic Ontology. It distinguishes direct causal evidence from dependency-based and structural impact propagation.

## Classifications

- `direct-causal-evidence` — a single explicit `affects` assertion.
- `dependency-impact` — direct or propagated impact through requires, blocks, validates, grants, supersedes, or mixed multi-hop chains.
- `structural-impact` — direct parent, containment, or variant relationships.

## Safeguards

- Dependency propagation is never proof of causation.
- Propagation is deterministic and limited to four hops.
- Unsupported causal claims remain unresolved hypotheses.
- Blast-radius ratings describe reachable governed entities, not predicted gameplay severity.
- Outputs are derived and advisory and cannot mutate, promote, certify, assign, schedule, or approve source content.

## Validation

The validator checks stable identities, bounded chains, classification compatibility, confidence, evidence, blast-radius records, unresolved-hypothesis safeguards, summary consistency, and the explicit non-causation policy.

CI generates and publishes the `aioc-causal-impact` artifact.
