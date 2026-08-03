# AIOC Dependency Graph

The dependency graph is the deterministic, derived relationship model for Development Brain Release A, Step 3.

## Authority and inputs

The graph is generated from the unified inventory. It does not replace canonical content, shared working state, or governed project memory. Nodes preserve the inventory authority layer and lifecycle.

## Stable identities

- Node IDs are `NODE-<stableId>`.
- Edge IDs are deterministic SHA-256-derived identifiers over source, relationship, and target.
- Duplicate source/relationship/target triples are prohibited.

## Relationship vocabulary

- `requires`
- `grants`
- `contains`
- `parent-of`
- `variant-of`
- `validates`
- `affects`
- `supersedes`
- `blocks`
- `member-of-pack`

Every edge includes source evidence, a source pointer, derivation description, and confidence classification.

## Validation controls

Generation and validation detect and fail on:

- dangling sources or targets;
- duplicate edge triples;
- self-dependencies;
- cycles in `requires`, `parent-of`, `variant-of`, `supersedes`, and `blocks`;
- incomplete evidence;
- vocabulary or summary inconsistencies.

## Commands

```bash
node scripts/development-brain/generate-unified-inventory.mjs /tmp/AIOC_UNIFIED_INVENTORY.json
node scripts/development-brain/generate-dependency-graph.mjs /tmp/AIOC_UNIFIED_INVENTORY.json /tmp/AIOC_DEPENDENCY_GRAPH.json
node scripts/development-brain/validate-dependency-graph.mjs /tmp/AIOC_DEPENDENCY_GRAPH.json
```

CI publishes the generated graph as a temporary artifact. The generated JSON remains derived and is not hand-maintained.
