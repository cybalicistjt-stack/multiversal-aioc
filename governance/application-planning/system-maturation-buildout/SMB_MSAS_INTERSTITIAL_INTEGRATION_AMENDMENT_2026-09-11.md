# SMB — MSAS Interstitial Integration Amendment

**Date:** 2026-09-11  
**Owner and final authority:** John Brandon Turner  
**Status:** OWNER-APPROVED FUTURE PLANNING  
**Affects:** future dependency order only; no current implementation authority

## Decision

The production/content portion of the future SMB sequence becomes:

`SMB-01 → SMB-02 → SMB-03 → SMB-04 → SMB-05 → SMB-06 → SMB-07 → CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → MAS-01..21 → MSAS-01..21 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10 → SMB-11 → SMB-12 → SMB-13 → SMB-14 → SMB-15 → SMB-16 → BRP-01..11 → SMB-17 → SMB-18`

This supersedes the direct `MAS-21 → SMB-08` handoff.

## Rationale

PCA supplies reusable production/audio primitives; MCS supplies maps; MCCS supplies character/creature presentation; MAS supplies playable Adventure assembly; MSAS supplies finished music/SFX/ambience/voice/adaptive-audio production and live-GM audio workflows. SMB-08/09 can therefore build first-party libraries and the first complete campaign without inventing one-off audio pipelines.

## Boundary

Planning only. This does not change current ARI execution, reopen AAI, start MSAS, authorize paid providers/credentials, voice impersonation, external recording/streaming, tester distribution, or release/deployment.