# AIOC GitHub Pages Deployment Baseline

**Status:** IMPLEMENTED — LIVE VERIFICATION PENDING  
**Step:** Infrastructure Cleanup Step 5  
**Canonical workflow:** `.github/workflows/deploy-pages.yml`  
**Public default:** `/operational/`

## Single deployment contract

GitHub Pages is controlled by one workflow: `Deploy Unified AIOC Pages`.

The workflow publishes one assembled artifact containing:

- the repository root redirect;
- the operational AIOC frontend;
- implementation documentation linked by the command center;
- the promoted 487-record certified canonical content database;
- governed current-state, handoff, dispatch, and narrow legacy-quarantine records;
- `deployment-manifest.json` and `/operational/health.json`.

## Preserved and excluded scope

- Recent COS capability work is preserved.
- The obsolete migration landing shell is not the public default.
- The corrupted Base64 seed path is not part of deployment or database generation.
- No recent COS source tree is deleted by the Pages workflow.

## Required live checks

A deployment is successful only when the workflow verifies all of the following from the public site:

1. The root resolves to the operational surface.
2. `/operational/health.json` matches the deployed commit.
3. `/deployment-manifest.json` matches the deployed commit and reports recent COS work preserved.
4. `/content-db/index.json` reports exactly 487 certified canonical records.

A failure in any check must be captured by the repository CI failure recorder before further governed work proceeds.
