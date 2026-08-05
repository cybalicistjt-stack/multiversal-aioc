# AIOC Integration for Owner–AI Interaction Controls

MV-CONT-005 adds `governance/ai/runtime/INTERACTION_OPERATIONAL_SCORECARD.json` to the compact AIOC runtime surface.

## Fast-path use

The bootstrap reads the compact scorecard after the current-work pointer and checkpoint. The scorecard answers four operational questions without loading the full audit corpus:

1. Did the latest deterministic pilot pass?
2. Are false-completion, privacy, duplicate, owner-gate, and typed-receipt controls currently passing?
3. Were parallel tracks and the roadmap-lite boundary preserved?
4. Is live longitudinal intervention reduction measured or still pending?

## Source of truth

The compact runtime record is generated from:

`governance/ai/interaction-system/pilot/OPERATIONAL_PILOT_SCORECARD.json`

`tools/interaction_pilot.py validate` rejects a stale or manually altered projection.

## Completion routing

After MV-CONT-005 is completed_verified, the continuity side mission has no unfinished item. Unless the owner changes direction, the primary execution route returns to the preserved application track at P9-06-008. IA-D03-003 remains a planned parallel design track.
