# MIB — ARI Interstitial Integration Amendment — 2026-09-07

**Status:** OWNER-APPROVED PLANNING AMENDMENT  
**Implementation authority:** none  
**Controls:** resumed MIB-16..18 relationship after the new SGC → ARI insertion.

## Dependency change

The resumed MIB sequence no longer follows SGC-08 directly. The planned dependency is:

`SGC-08 → ARI-01..22 → MIB-16 → MIB-17 → MIB-18`

MIB-01..15 remain completed/retained according to their existing evidence. This amendment does not reopen them.

## MIB-16 integration

MIB-16 — Diagnostics, Provenance, Dependency and Search Engineering Surfaces — must consume the completed ARI resource/catalog/derivative interfaces where relevant. Its diagnostic and reverse-reference surfaces should be able to trace:

- source/import/native/generated/reference-only resource identity;
- ARI derivative lineage and stale/relink state;
- rights-use capability evidence and fail-closed outcomes;
- owning-domain bridges to MAI/AAI/CAPP/PAPT/Scene and later SAA;
- large-library search/index diagnostics without leaking unauthorized assets or counts.

MIB-16 does not become the ARI catalog owner and must not create a duplicate resource/provenance ledger.

## MIB-18 integration

MIB-18 — Backbone Integration, Portability and Gated-Work Readiness Handoff — must include ARI in its compatibility/integration matrix and portability/readiness handoff. The backbone proof should treat ARI as a shared implementation foundation available to later SMB content/Creator surfaces.

SAA is not required to be implemented by MIB-18; SAA occurs later after SMB-09. MIB-18 should preserve the ARI interfaces SAA will consume.

P3D remains a deferred future project and is not a MIB-18 completion dependency. MIB-18 may list P3D's preserved renderer/resource seams as future readiness only.

## Non-activation boundary

This planning amendment does not select MIB-16, alter the current VTI selector, reopen MIB-01..15 or activate ARI/SAA/P3D implementation.