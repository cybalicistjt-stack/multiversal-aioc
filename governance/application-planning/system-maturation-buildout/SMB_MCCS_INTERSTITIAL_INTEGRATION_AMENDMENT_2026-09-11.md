# SMB — MCCS Interstitial Integration Amendment

**Date:** 2026-09-11  
**Owner and final authority:** John Brandon Turner  
**Status:** OWNER-APPROVED FUTURE PLANNING  
**Affects:** future dependency order only; no current implementation authority

## Decision

The production/content portion of the future SMB sequence is amended to:

`SMB-01 → SMB-02 → SMB-03 → SMB-04 → SMB-05 → SMB-06 → SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10 → SMB-11 → SMB-12 → SMB-13 → SMB-14 → SMB-15 → SMB-16 → BRP-01..11 → SMB-17 → SMB-18`

This supersedes the earlier direct `MCS-21 → SMB-08` handoff. PCA and MCS remain in place; MCS now hands off to MCCS, then MCCS hands off to SMB-08.

## Dependency rationale

- PCA supplies reusable production/generator, character asset/rig/garment, motion/facial and style-generation primitives.
- MCS supplies the finished map/cartography creator surface.
- MCCS supplies the finished Character/creature visual-creation surface over CAPP/PPIA/PAPT/PCA/ARI foundations.
- SMB-08 first-party content-library work and SMB-09 first-complete-campaign work can then create/reuse maps and Character/creature presentation assets through governed creator systems rather than one-off production pipelines.
- SAA remains after SMB-09 and can consume those governed visual assets.

## Boundary

This is planning only. It does not change current ARI execution, start MCS or MCCS, modify completed CAPP/PPIA/PAPT authority, activate P3D, authorize paid providers, or activate release/tester workflows.
