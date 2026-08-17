# Governed Item Taxonomy Adoption Proposal — Prepared, Not Authorized

**Date:** 2026-08-17  
**Taxonomy authority:** Multiversal IA Item Taxonomy Preparation v0.12.0  
**Corpus:** 5,389 Item/reference rows  
**Decision state:** NOT READY / OWNER GATE NOT REQUESTED YET

## Proposed adoption object

Adopt taxonomy as additive Definition metadata keyed to existing stable/canonical identities. Do not rewrite the nine source/master CSVs. Do not transform candidate metadata into A8 Asset-instance state.

The adoption object should contain:
- one row identity/provenance envelope per source record;
- zero or more governed taxonomy assertions per applicable axis;
- confidence and review state;
- explicit N/A for non-item support/reference rows where appropriate;
- explicit unresolved/unknown where evidence is insufficient;
- correction-overlay provenance pointing back to the sealed historical candidate tranche and the cross-axis review.

## Required preconditions

1. Recover exact row-level IAX-06, IAX-07 and IAX-08 private evidence at their sealed SHA-256 identities **or** produce new versioned superseding reprojections. Never pretend a reconstruction is the original sealed artifact.
2. Apply the cross-axis correction overlay; do not mutate sealed historical tranche evidence.
3. Reconcile all 5,389 rows into one ten-axis candidate adoption ledger.
4. Re-run deterministic validation.
5. Present remaining unresolved/unknown/review-required cohorts to the owner.

## Enablement rule

Canonical adoption is a separate owner decision. This proposal does **not** authorize:
- source/master CSV mutation;
- automatic taxonomy enablement;
- mechanics reauthoring;
- runtime Asset creation;
- app-facing release;
- `GAME_READY` certification.

## Parallel work

Platform v0.11.0 additive candidate projection/review can proceed while this Item adoption gate remains pending.
