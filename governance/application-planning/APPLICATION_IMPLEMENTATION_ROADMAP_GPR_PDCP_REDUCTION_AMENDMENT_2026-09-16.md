# Application Implementation Roadmap — GPR PDCP Reduction Amendment — 2026-09-16

**Status:** OWNER-APPROVED PDCP PLANNING RECONCILIATION  
**Program:** GPR — Gameplay Pattern Runtime & Loop Minis  
**Implementation authority:** none

## Decision

PDCP family closure reduces the historical GPR implementation plan from **16 baseline tranches to 10 surviving implementation/proof tranches** without capability loss.

Historical baseline provenance remains preserved in `PDCP_GPR_REDUCTION_RECEIPT.json`. The effective future execution order is now:

`GPR-01 → GPR-03 → GPR-05 → GPR-06 → GPR-07 → GPR-08 → GPR-09 → GPR-10 → GPR-12 → GPR-16`

## Fold map

- `GPR-01 + GPR-02 → GPR-01` — runtime authority, contract registry/import and MAL/MRCS convergence;
- `GPR-03` retained — deterministic gameplay state/input/collision kernel;
- `GPR-04 + GPR-05 → GPR-05` — owner-domain operation/objective/route execution adapters;
- `GPR-06` retained — specialist puzzle/sports/vehicle/party/strategy/social/stealth pattern modules;
- `GPR-07` retained — encounter/autonomy/score/timing/loadout/skill runtime;
- `GPR-08` retained — loop-mini composer/authoring schema;
- `GPR-09 + GPR-14 → GPR-09` — seven delivery modes plus GPR-specific Creator/GM/world/roster binding;
- `GPR-10 + GPR-11 → GPR-10` — rights-safe semantic presentation plus camera/UI/audio/accessibility/device projection;
- `GPR-12 + GPR-13 → GPR-12` — multiplayer/replay plus persistence/snapshot/migration/recovery/version continuity;
- `GPR-15 + GPR-16 → GPR-16` — complete conformance/regression plus golden cross-system proof/handoff.

## Shared-owner reductions

This amendment does not move canonical owner truth into GPR.

- MRCS/canonical domains retain reusable definition authority.
- Action/Event and domain owners retain canonical mutations.
- MAL remains completed_verified and frozen.
- Packet 07 owns generic preview/commit/intervention/debug/recovery semantics.
- PCA-12/Packet 08 own generic simulation/formal-analysis infrastructure.
- ARI/PCA own generic resource identity, rights, provenance, version/review/import-export.
- Specialist creator families retain their presentation/content authoring domains.
- Reduced MERA/MBES/MSLR/MSWI consume GPR execution rather than duplicating it.

## Stable roadmap gates

No `ROADMAP_DEPENDENCY_GRAPH.json` mutation is required:

- `GPR-01` remains the GPR rotation/start milestone;
- `GPR-05` remains the existing MERA rotation prerequisite;
- `GPR-16` remains the GPR golden proof and downstream requirement for MERA/MSLR/MSWI where already referenced.

Sparse IDs are intentionally preserved rather than renumbering the family.

## Completion standard

The removed standalone tranche count is **6**. No capability is deleted. `GPR-16` now owns the historical GPR-15 conformance obligations as part of the final proof, including the full 168-pattern / 85-operation / 672-variant battery.

This planning amendment grants no implementation authority and does not modify `operations/CURRENT.json`.
