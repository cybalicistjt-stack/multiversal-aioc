# MVPS-08 Completion Report

**Work item:** MVPS-08 — Lineage/Subspecies Inheritance and Composition  
**Result:** completed_verified  
**Completed:** 2026-09-18

MVPS-08 defines lineage/subspecies records as exact-version, source-backed deltas over a base SpeciesDefinition rather than copied parent definitions.

## Delivered

- `MVPS.LineageDefinition` with exact parent species/version references, explicit relationship evidence and typed delta operations.
- Add, exclude, remove, replace and descriptive-override operations with source/provenance and stable operation order.
- `MVPS.LineageComposition` with deterministic replay ordering that does not use order as semantic conflict resolution.
- Explicit conflict records for parent-version mismatch, unknown targets, colliding replacements/removals and missing relationship authority.
- Duplicate/stacking/suppression/replacement mechanic interactions defer to shared owners rather than a lineage-local stacking engine.
- Base species identity and selection history remain preserved.
- Runtime form, progression and active contribution projection remain reserved for MVPS-09, MVPS-10 and MVPS-13.
- Synthetic fixtures prove additive, explicit replacement, shared-owner duplicate, same-target conflict and parent-version-mismatch paths.
- Permanent MVPS-08 regression coverage in repository health validation.

## Evidence

- Causal RED: run `35382218285`, head `f59bd69164f84e43d485ac675ef00abffc65d801`.
- Initial GREEN: run `35382373920`, head `872ce4cedf2848d4d79f030af0285ac5d08982e6`.
- Replayed GREEN: run `35382865993`, head `97fcf986c7adb004c8cfd9c8eb7bdd964c127f85`.
- Final FIFO publication validation: run `35384256512`, head `9886727af1d2dd46076457ae7db0bbdb526de130`.
- Implementation PR: #1413.
- Durable implementation merge: `47f450b4e97d06074a91cf7f7c478e98c1051702`.

## FIFO publication behavior

Every stale-base race failed closed; no stale MVPS candidate was merged. The implementation was replayed unchanged only after a fresh FIFO reservation activated, then revalidated on the exact publication head.

## Execution conformance

Product completion is valid. This tranche required a second owner Continue because FIFO stale-main races and the stall-recovery handoff interrupted the original execution turn; the checkpoint records that process-conformance miss explicitly.

## Successor

Fresh DAG reconciliation leaves strict MVPS order intact. `MVPS-09 — Forms and Transformation Semantics` is selected_not_started with no implementation authority.
