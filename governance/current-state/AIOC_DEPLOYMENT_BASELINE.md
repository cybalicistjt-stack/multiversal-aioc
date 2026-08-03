# AIOC Deployment Baseline

**Status:** CERTIFIED BASELINE  
**Repository:** `cybalicistjt-stack/multiversal-aioc`  
**Default branch:** `main`  
**Public surface:** `/operational/`  
**Recorded:** 2026-08-03

## Completed cleanup sequence

The seven-step repository and deployment cleanup is complete:

1. Current deployment and workflow inventory completed.
2. Legacy content generation decoupled from Pages.
3. Corrupted seed-dependent database pipeline replaced by the governed canonical-object pipeline.
4. The obsolete migration entry shell was narrowly quarantined while all recent COS capability work was preserved.
5. GitHub Pages was consolidated into one deployment workflow and one public operational surface.
6. A unified validation workflow was added for smoke, semantic, content, deployment, link, and COS-preservation contracts.
7. This deployment baseline was recorded as the new canonical operating state.

## Certified content contract

- Pipeline mode: `CANONICAL_OBJECTS_ONLY`
- Certified records: 487
- Certification result: PASS
- Certification run: `30811292940`
- Promotion run: `30811314910`
- Promoted database commit: `94ad7253167c661f79555b6b2de173cccfe43c23`
- Legacy damaged seed inventory: quarantined pending intact authoritative import

## Deployment contract

- Exactly one Pages deployment workflow is authoritative: `.github/workflows/deploy-pages.yml`.
- The repository root redirects to `./operational/`.
- The public artifact includes the operational frontend, governed implementation documentation, current-state records, and the certified content database.
- The public artifact exposes `deployed-build.json`, `operational/health.json`, and `content-db/index.json`.
- The deployment workflow verifies the root, health record, deployment manifest, commit identity, COS-preservation marker, and certified record count after publication.

## COS preservation contract

All recent COS capability work remains part of the active AIOC codebase and may be integrated into the operational command center. Only the obsolete migration entry behavior and corrupted legacy seed execution path are quarantined.

## Failure evidence rule

Before every governed operation, read:

`governance/ci-failures/INDEX.md` on branch `ci/failure-records`.

Any recorded failure is repaired before new work begins.

## Next executable action

Return to active AIOC capability delivery and Multiversal application orchestration. The current external dependency remains WP-011 — Tauri iOS/iPadOS Spike on a supported Mac. While WP-011 awaits Mac execution, AIOC work should focus on integrating preserved COS capabilities into the operational command center in bounded, feature-complete batches.
