# CCTI-01 — Corpus and Sidecar Reconstruction

**Mode:** read-only  
**Date:** 2026-08-17  
**Source/canonical mutation:** none

## Accounting

All twelve owner-selected catalogs are represented in Content V2 `RECORD_PROVENANCE_PROFILE_v1.0.0.csv`: **11,017 / 11,017 rows**.

- 11,011 rows carry a current canonical Definition ID.
- Six legacy/reference-only `Weapons_Ammo.csv` rows deliberately lack a current Definition target.
- All 36 `Weapons_Ammo.csv` rows remain reference-only; 30 link to a current Definition and six remain reference identities.

CCTI therefore does not need to replace the existing identity system.

## Existing sidecar work recovered

Identity foundation and closure evidence shows frozen Source Record/Definition identities for catalogs that lacked direct IDs, while catalogs with governed IDs retain those IDs. Target cross-catalog identity evidence contains **56 participant rows across 30 governed identity-decision IDs**. Same-name identity remains evidence-gated, never automatic.

Typed-normalization evidence touching the target corpus contains:

- **144,336** normalized field-value rows;
- **3,980** normalization review-queue pattern rows;
- **24,653** field-value occurrences represented by those review patterns.

CCTI must reuse raw/effective values, parse state/method, confidence, corrections, identity decisions, provenance, aliases, supersession, resolved relationships, and review queues rather than starting normalization over.

## Existing cross-package relationships

Conservative exact-ID/catalog matching finds **216 resolved relationship rows** touching the target corpus in the current cross-package relationship registry:

- 189 `PRIMARY_ATTACK_USES`;
- 27 `CARRIES_EQUIPMENT`.

No current unresolved-relationship row directly targets the twelve CCTI catalogs under exact catalog/ID matching. Broad Platform component/product relationships are not yet represented in this cross-package layer and remain a CCTI-07 reconciliation area; this does not imply their structured catalog fields contain no relationship evidence.

## Platform routing

The 5,628 Platform-catalog rows split exactly under existing `Record_Type` evidence:

- **2,984 platform/model rows**;
- **2,644 component/module/rules/support rows**.

Vehicles: 953 model + 247 non-model.  
Mecha: 930 model + 1,187 non-model.  
Spacecraft: 1,101 model + 1,210 non-model.

This exactly reconciles the Platform v0.11.0 handoff statement that 5,628 current catalog rows were inventoried while 2,984 platform/model records were analyzed. A migration that simply treats every Vehicle/Mecha/Spacecraft CSV row as a platform model would be structurally wrong.

## Deterministic working envelope

A private read-only one-row-per-target reconstruction ledger was generated from the inspected session source without publishing the entire game corpus into the public governance repository:

- rows: 11,017;
- ledger SHA-256: `7e27dc50b8e9fea0dc1ea67ec60dd40caf394c7dd51fb6010047e0d9d24e206b`;
- aggregate metrics SHA-256: `0fc9f93aca3aff38bc461cb6f11c150715f1e747eebf7d61f5745e513ad5697a`.

These are working evidence only and create no row-level taxonomy-write authority.

## CCTI-02 boundary

The source/identity/provenance/normalization reconstruction is sufficient to build deterministic preprojection envelopes. Complete controlled-registry row projection still requires recovery of the exact checksum-bound Item v0.12.0 and Platform v0.11.0 archives. Repository extracts may guide architecture but must not be treated as the complete registries.
