# CCTI Write Phase — Tranche 4: Item IAX-04 Use-Relation Candidate Projection

**Date:** 2026-08-17  
**Status:** candidate sidecars produced; source masters unchanged; canonical adoption disabled

Exact Item Taxonomy v0.12.0 defines `IAX-04 use_relation` as a **multi-select** axis with **20 controlled values**.

## Result

All **5,389 Item-corpus rows** have an explicit disposition:

- **2,850** rows: high-confidence candidate set only.
- **2,408** rows: one or more medium-confidence/review-required candidates.
- **95** rows: explicitly unresolved because current structured evidence did not safely establish a use relation.
- **36** `Weapons_Ammo.csv` legacy/reference-only rows: not applicable.
- silently unaccounted rows: **0**.

The 5,353 current Item Definition rows therefore contain **5,258** rows with one or more use-relation candidates plus **95** explicit unresolved rows.

Candidate assertions: **9,429** total — **6,362 high-confidence** and **3,067 medium-confidence**.

Largest candidate relations: `bonded` 2,299; `operated` 1,167; `held` 1,062; `read_consulted` 968; `installed` 918; `wielded` 671; `implanted` 561; `mounted` 419; `slotted` 405; `worn` 329. Additional controlled relations remain represented where source evidence supports them.

Use semantics remain domain-specific: weapons use wield/hand/mount evidence; computer software/AI/modules distinguish operated/autonomous/installed/slotted; EVA chassis are donned and modules installed/mounted/slotted; Living Spellbooks are read/consulted and may be bonded/autonomous; Symbiote/Cybernetic definitions preserve implanted/bonded semantics; general Items/Magitech distinguish worn, operated, deployed, loaded, read/consulted and evidence-backed consumption-delivery relations.

The **95 unresolved rows** are retained rather than coerced: 92 `Items.csv` rows and 3 Symbiotes/Cybernetics support-item rows.

## Validation

PASS:
- exact `IAX-04 use_relation` multi-select authority;
- 20 exact v0.12.0 controlled values, zero foreign IDs;
- 5,389/5,389 source-row accounting;
- 5,353/5,353 current Definition candidate-or-explicit-unresolved accounting;
- 36/36 reference-only accounting;
- zero duplicate same-value assertions per row;
- source/master mutation false for every assertion;
- canonical adoption remains `CANDIDATE_SIDECAR_NOT_ENABLED`.

Private assertion SHA-256: `b443d5e7ad7625b274c462db1340495e53271f0e31d20b49c65fcd74dd25f6d8`  
Private row-summary SHA-256: `77c4a495e9af24bd2527cdf6d546f8494781622fca65e93eac256309796d95a4`  
Rule-usage SHA-256: `54e892d0e5ac16aec65fefa97c61907fda623aa6711b5dfdc2a3c934b8b302f5`  
Baseline SHA-256: `b5aa5c83664080a554c05f488291b92a85bc9e31d6b1edb58a7fb49ed64d85c9`

Private artifact: `CCTI_Item_Taxonomy_Tranche4_IAX04_20260817.zip`  
SHA-256: `d431451325832d6560ae66903f0a561c96607d5eb9d1f08fea78dfba149f1421`

## Exact next content operation

Proceed to **IAX-05 — portability_scale**, the next single-select axis. Mechanics reauthoring remains outside taxonomy projection.
