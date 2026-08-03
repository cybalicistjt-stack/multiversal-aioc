# Obsolete COS Migration-Shell Quarantine

**Status:** NARROWLY QUARANTINED  
**Quarantined component:** obsolete COS migration-control entry shell and corrupted Phase 1–7 seed path  
**Preserved component:** all recent COS capability work, engines, tools, tests, workflows, records, and reusable UI modules  
**Public default:** `/operational/`

## Decision

Only the obsolete migration-control entry shell is excluded from the public default and active content build. Recent COS work is active project work and must not be discarded, relabeled as obsolete, deleted, or excluded merely because it resides under a historical path.

## Enforced boundaries

- The repository root redirects to `./operational/`.
- The operational command center is the public default.
- Recent COS capabilities remain available for integration into the operational AIOC.
- No rule may delete or broadly quarantine the `/v2/` tree or other COS work.
- The obsolete migration entry screen must not become the public root without an explicit governed decision.
- The corrupted Phase 1–7 Base64 seed fragments remain excluded from active generation.
- COS engines, tools, tests, migration results, and reusable interface modules must remain preserved in repository history and source.

## Content database relationship

The active database currently certifies the 487 governed canonical objects. This does not invalidate broader COS work or the approved 1,347-row 8E-008G inventory. The larger inventory may be restored when its intact authoritative audit source is imported and independently certified.

## Integration rule

The next frontend work must reconcile and integrate useful recent COS capabilities into the operational AIOC rather than rebuilding them from scratch. Only migration-shell-specific presentation and the damaged seed decoder are quarantined.
