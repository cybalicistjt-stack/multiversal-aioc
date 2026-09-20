# MVPS-18 Completion Report

**Work item:** MVPS-18 — Core-26 Canonical Object Reconciliation  
**Status:** completed_verified  
**Completed:** 2026-09-20

MVPS-18 makes every Core-26 species durable before deeper production work. The species system no longer depends on a user remembering to separately register new species work after a design session.

## Permanent Core-26 canon registers

All 26 current species now own a versioned source-chain directory:

`content-source/core26-species/<species-slug>/`

Each begins with:

- `register-v1.0.0.json` — stable canon register/source ledger/current definition binding/open-domain and certification bookkeeping;
- `definition-v1.0.0.json` — exact-version current SpeciesDefinition source.

Canon changes append a new versioned source file. Prior versions remain history. Changes that alter the gameplay SpeciesDefinition also require a definition version bump. The canonical database must be rebuilt and certified in the same publication candidate.

## Current identity/catalog reconciliation

- current SpeciesDefinitions: **26/26**;
- permanent species canon registers: **26/26**;
- Rog: source-backed current SpeciesDefinition materialized;
- Suula: source-backed current SpeciesDefinition materialized;
- Morganthyr: current SpeciesDefinition materialized;
- Nekron/Nekrons: retained only as historical alias/provenance resolving to Morganthyr;
- Akwi: brought into the canonical content-db catalog while continuing to reuse the completed_verified AKWI-01 governed rules integration;
- The Free and Ratman: current display identities normalized without changing stable gameplay IDs.

## ManyToms durability repair

The finalized owner-approved `ManyToms_Canonical_Species_Dossier_v1.0.0.docx` is now a real canonical replacement source, not merely provenance embedded in a manually promoted generated object.

The ManyToms register records:

- canonical dossier Drive ID `1Pd9BQFYVDQBZIJBGM_Utnd_KLblHGGQ1`;
- development precursor `Manytomsinfo` Drive ID `1cbrTQjYvpOBwAncFCGJqUjsCPeTzbxLTr2QwyM1Ra-s` as development history, not blanket canon;
- legacy ManyToms source as superseded where the dossier conflicts.

A canonical database rebuild now reproduces the 12-Tom owner-approved species record and the source registry can find the dossier-derived source.

## Pipeline proof

Causal RED:
- head: `58ba9725b1ad139b522710decb8213c2b70f88e6`
- run: `35516850653`
- result: expected failure on missing per-species registers/source chains/exact current definitions.

Exact-head GREEN:
- head: `7d95e928b851cb5bdb8c8cc62bc62dff560af306`
- run: `35517544937`
- result: complete repository-health success, including generated-output parity.

Published application:
- PR #1478
- READY `MVPS-18-app-001`
- merge `617ec2f8bba6b86acaec40abcabe2b7a6c800892`

Rebuilt canonical database:
- effective records: 556;
- source count: 62;
- appended records: 69;
- governed replacement records: 31;
- supplemental input records: 100.

## What MVPS-18 does not claim

The 26 species are not yet game-ready certified. MVPS-18 guarantees that future species work has a durable, versioned canonical home and that the current identities can be rebuilt from registered sources. MVPS-19 now fills the common mechanics/morphology/physiology/environment/capability/interface dimensions without fabricating missing canon.
