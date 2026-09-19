# MVPS-12 Completion Report

**Work item:** MVPS-12 — Validation, Migration and Import/Export  
**Result:** completed_verified  
**Completed:** 2026-09-19

MVPS-12 established the species-facing validation, migration and import/export boundary without creating duplicate generic validation, migration, serialization or runtime-projection engines.

## Delivered

- Explicit species validation states: `playable`, `incomplete`, `invalid`, and `migration_required`.
- Structural, behavioral and integration validation layers with source/provenance-bearing findings.
- A no-fabrication rule for missing, conflicted, hidden or source-unspecified canon.
- Historical `CharacterSpeciesSelection` preservation across deprecation, replacement, entitlement/pack loss and migration.
- Explicit replacement semantics: no silent substitution of species/version references.
- Machine-readable migration receipt and discrepancy/recovery contracts.
- Import/export round-trip requirements preserving stable identity, exact versions, provenance, unresolved/conflict state and owner-domain references without flattening shared mechanics into species-local data.
- Shared-owner handoffs to A4 Character validation/migration/export, generic persistence migration and authoring import/export ports.
- Non-canon fixtures and permanent MVPS-12 repository regression coverage.
- Explicit MVPS-13 boundary for deterministic runtime active-contribution projection.

## TDD evidence

The first workflow attempt, run `35473664947`, was rejected by the OPS3 single-door validator because the candidate incorrectly carried live execution state in the protected checkpoint projection. That attempt was not accepted as causal RED.

After restoring the checkpoint projection, causal RED run `35473694572` on head `022b0b6fc61b5d56e9029a5f31f04fdf9254882e` passed OPS3 and MVPS-01 through MVPS-11, then failed at MVPS-12 because the five required MVPS-12 contract artifacts were absent.

Exact-head GREEN run `35473801265` on `4b0c09a833bf601799641d58f79207c6de0cb93d` passed the full repository-health workflow, including MVPS-01 through MVPS-12, content reconciliation and generated-content immutability checks.

## Publication evidence

- Implementation PR: #1449.
- READY candidate: `MVPS-12-attempt-001-4b0c09a8`.
- Fresh integration base: `5f716e245c6cfdf065a5bf53374f594ac6315a59`.
- Durable implementation merge: `6bd2438a1aba8f6847890fc079d4f6f397be8b7a`.
- Publication queue reconciled at generation 4 with no remaining READY candidate.
- The closeout projection was replayed onto AIOC main `1b8d5ea2ccba952d5b816b286f2352f515d96db5` after the parallel MSAS-04 closeout advanced main; the MSAS-05 selection is preserved unchanged.

## Ownership boundary

MVPS-12 supplies species-facing contracts, findings, fixtures and invariants. A4 Character validation/migration/export, generic persistence migration and authoring import/export remain the authoritative shared owners for their respective operations. MVPS-12 does not compute current active species contributions; that is MVPS-13.

## Successor

Fresh `ROADMAP_DEPENDENCY_GRAPH.json` schema 1.0.4 contains no MVPS interstitial gate overriding strict order. `MVPS-13 — Runtime Projection and Grant Receipts` is selected_not_started and has no implementation authority until a later MVPS-specific owner Continue.
