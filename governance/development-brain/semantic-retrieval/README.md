# Semantic Retrieval and Reasoning Context

Step 12 assembles deterministic, bounded, source-backed context packages for AI use across browser, MCP, REST, and Codex surfaces.

## Contract

Each package is anchored to one semantic entity and contains ranked context items separated into:

- source facts;
- derived findings;
- recommendations;
- governance constraints;
- unresolved questions.

Every item retains authority, confidence, freshness, and source evidence. Ranking is deterministic, duplicates are removed, stale packages are rejected, and each package is limited to 24 items and 12,000 serialized characters.

## Authority boundary

Context packages are read-only and advisory. Retrieval does not grant execution, mutation, assignment, scheduling, approval, promotion, or certification authority. Recommendations remain recommendations; unresolved questions remain unresolved; derived findings are never represented as canonical facts.

## Freshness

Each package carries a fingerprint derived from all upstream governed and generated sources. Consumers must reject packages whose fingerprint no longer matches the active source set.

## Validation

The validator enforces stable IDs, deterministic ranks, budget limits, evidence requirements, category separation, freshness, duplicate removal, summary accuracy, and authority safeguards.
