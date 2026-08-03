# AIOC Unified Object Inventory

The unified inventory is the Development Brain's normalized view of all Multiversal game-object work.

It is **derived**, not manually edited. The generator combines:

1. `content-db/index.json` — canonical certified content;
2. `governance/shared-state/AIOC_SHARED_STATE.json` — drafts, structure decisions, packs, evidence, and review state;
3. `governance/development-brain/memory/AIOC_PROJECT_MEMORY.json` — governed project-memory references.

## Authority boundary

Each inventory object has exactly one current authority layer:

- `canonical` — no shared working copy currently overrides the view;
- `working` — a shared draft exists and is the active development view.

A working view never changes or replaces the underlying canonical record. Canonical promotion remains a separate governed process.

## Stable identity

- `stableId` is the project's existing canonical or working-object identifier.
- `inventoryId` is derived as `INV-<stableId>`.
- Duplicate stable IDs are a validation failure.

## Included relationships

Each normalized object may reference:

- structure classification and parent/canonical target;
- packs;
- balance evidence;
- testing evidence;
- review queue entries;
- governed project-memory entries;
- declared dependencies;
- canonical and working source positions.

## Generation

```bash
node scripts/development-brain/generate-unified-inventory.mjs /tmp/AIOC_UNIFIED_INVENTORY.json
node scripts/development-brain/validate-unified-inventory.mjs /tmp/AIOC_UNIFIED_INVENTORY.json
```

CI publishes the generated inventory as a temporary validation artifact. A later Development Brain integration step will expose the same normalized model through the browser, REST API, and MCP tools.
