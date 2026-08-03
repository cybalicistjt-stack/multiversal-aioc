# AIOC Structure Intelligence

Structure Intelligence is Development Brain Release B, Step 4. It is a deterministic derived view over the unified inventory and dependency graph.

It identifies:

- hierarchy and containment;
- parent/child relationships;
- variants;
- pack membership;
- unresolved classifications;
- orphaned objects;
- structural gaps;
- conflicting structure decisions;
- high-impact structural dependencies.

## Authority boundary

This layer does not edit or promote canonical content. It preserves each object's canonical or working authority layer and records evidence for every derived view.

## Commands

```bash
node scripts/development-brain/generate-unified-inventory.mjs tmp/AIOC_UNIFIED_INVENTORY.json
node scripts/development-brain/generate-dependency-graph.mjs tmp/AIOC_UNIFIED_INVENTORY.json tmp/AIOC_DEPENDENCY_GRAPH.json
node scripts/development-brain/generate-structure-intelligence.mjs tmp/AIOC_UNIFIED_INVENTORY.json tmp/AIOC_DEPENDENCY_GRAPH.json tmp/AIOC_STRUCTURE_INTELLIGENCE.json
node scripts/development-brain/validate-structure-intelligence.mjs tmp/AIOC_STRUCTURE_INTELLIGENCE.json
```

The generated artifact is reproducible and must not be hand-maintained. Step 5 may begin only after CI validates this artifact.
