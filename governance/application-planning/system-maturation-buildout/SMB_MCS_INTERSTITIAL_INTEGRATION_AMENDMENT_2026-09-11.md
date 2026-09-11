# SMB — MCS Interstitial Integration Amendment

**Date:** 2026-09-11  
**Owner and final authority:** John Brandon Turner  
**Status:** OWNER-APPROVED FUTURE PLANNING  
**Affects:** future dependency order only; no current implementation authority

## Decision

The production/content portion of the future SMB sequence is amended to:

`SMB-01 → SMB-02 → SMB-03 → SMB-04 → SMB-05 → SMB-06 → SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10 → SMB-11 → SMB-12 → SMB-13 → SMB-14 → SMB-15 → SMB-16 → BRP-01..11 → SMB-17 → SMB-18`

This supersedes the earlier direct `PCA-16 → SMB-08` handoff recorded by the PCA interstitial amendment. PCA remains in place and hands off to MCS.

## Dependency rationale

- PCA supplies reusable production/generator primitives.
- MCS turns those primitives plus MAI/ISE/SSA/ARI/VTI owner contracts into the finished user-facing cartography studio.
- SMB-08 first-party content-library work and SMB-09 first-complete-campaign work can then create/reuse maps through one governed studio rather than inventing one-off mapping pipelines.
- SAA remains after SMB-09.

## Boundary

This is planning only. It does not change current ARI execution, start MCS, modify completed MAI/ISE/SSA/VTI authority, authorize paid providers, or activate release/tester workflows.
