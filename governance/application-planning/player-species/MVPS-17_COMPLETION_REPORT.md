# MVPS-17 Completion Report

**Work item:** MVPS-17 — Core-26 Canon Lock and Production Baseline  
**Result:** completed_verified  
**Completed:** 2026-09-20

MVPS-17 makes the owner's Core-26 roster a forward-loaded current-canon authority and establishes one equal game-ready certification standard for all 26.

## Canon lock

`operations/CURRENT.json` now references `CORE26-CURRENT-01` as the player-species domain authority. OPS3 startup and the global operating contract require relevant work to load CURRENT-referenced domain authority before historical species artifacts or generated catalogs. Historical material cannot override the current authority.

Current canon is exactly:

Human, Elf, Dwarf, Goblin, Orc, Giantkin, Stygian, Sharr, Gray, The Free, Ratman, Furashin, Rog, Rohai, Moravi, Vespin, Rakuuta, Traiga, Kola-Ha, Toba-Madra, Arborae, Mythragara, Suula, Morganthyr, ManyToms, Akwi.

Morganthyr is current; Nekron/Nekrons are historical aliases. Akwi is a peer Core-26 species regardless of supplemental storage. Ratman remains one core species with nine subordinate recovered lineage/subspecies candidates.

## Equal standard

`CORE26.GAME_READY.v1` defines 19 common certification dimensions. All 26 use the same standard. Lineage/subspecies, forms/transformation, and progression/maturation may be explicitly not applicable when source-backed; mandatory dimensions must be certified.

## Baseline

The baseline has exactly 26 rows and intentionally certifies **0** species as game-ready at the new standard. Existing evidence is preserved but is not inflated into certification.

Key object-level gaps recorded for MVPS-18:
- 22 current-name species objects exist as structured drafts.
- Morganthyr currently has a legacy Nekron object requiring current-identity migration.
- Rog and Suula lack current content-db SpeciesDefinition objects.
- Akwi has completed governed supplemental runtime integration but requires current catalog convergence.

## TDD and publication evidence

- Causal RED: run `35509983377`, head `2d95f910ff7471fc80c26768595011c1c508dbf8`.
- Initial GREEN: run `35510087746`, head `317d42848e05f232a677e3c474409f0117262242`.
- Parallel MRCS closeout moved main; FIFO was preserved.
- Fresh-base replay GREEN: run `35510233298`, head `a8f031ad84cc09f87413f63c2ffd28108cc01e0a`.
- Application PR: #1471.
- Durable application merge: `867564dba956e3c6fdbfddbae2fa8a54ed5ac3a9`.

## Successor

MVPS-18 — Core-26 Canonical Object Reconciliation — is selected_not_started.
