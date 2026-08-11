# PPIA-01 — Earlier Semantic-Parse Database Retirement Assessment

**Status:** RETIREMENT CANDIDATE — NOT SAFE TO DELETE YET  
**Scope:** Earlier 487-object semantic-parse/content-database path

## Finding

The 487-object repository content database is not the content authority for PPIA-01 and should not be used to measure Multiversal content completeness. The later 8E-009 CSV-first registry is the relevant content program for that purpose.

However, deleting `content-db/` and its pipeline immediately would break current AIOC operational surfaces.

## Confirmed direct consumers

### Browser content loader

`content-database.js` directly loads:

- `./content-db/index.json`
- `./content-db/manifest.json`
- `./content-db/source-registry.json`
- `./content-db/content-record.schema.json`

It also hard-codes `CERTIFIED_RECORD_COUNT=487` and rejects a different record count.

### MCP bridge

`bridge/mcp-server/src/server-v3.mjs` directly fetches `${RAW_BASE}/content-db/index.json` for AIOC content-database operations.

### Build/certification/promotion automation

The repository retains workflows and scripts that build, certify, promote, and verify the 487-record database, including the current operational-baseline validation surface.

### Development-brain/operational projections

Several development-brain inventory, dependency, completion/readiness, and Pages/operations surfaces reference the repository content database.

## Retirement recommendation

Do not spend PPIA-01 effort improving the 487 objects. Treat the entire path as compatibility debt.

Retire it only through a bounded migration:

1. Define a replacement read projection over the current CSV-first registry. Do not expose raw 19,199-row source data directly to consumers that need a normalized view.
2. Move the browser content loader to the replacement projection and remove the hard-coded 487 count.
3. Move MCP content lookup/search to the replacement projection.
4. Update development-brain and operational consumers.
5. Replace or retire the old build/certification/promotion workflows and associated tests.
6. Run AIOC operational baseline, MCP, Pages, content-library, and development-brain regression checks against the replacement.
7. Only after the replacement is green, delete `content-db/`, the 487-object source materialization/certification path, and dead compatibility code.

## PPIA-01 boundary

PPIA-01 may document this retirement dependency and avoid the obsolete database entirely. The migration/deletion itself is a separate repository cleanup operation because it affects AIOC runtime/tooling surfaces rather than game-content quality.
