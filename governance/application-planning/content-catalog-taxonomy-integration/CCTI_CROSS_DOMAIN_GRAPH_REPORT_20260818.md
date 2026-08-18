# CCTI Cross-Domain Graph — Governed Candidate Edge Resolution

**Date:** 2026-08-18  
**Status:** candidate graph tranche complete; new edges not adopted

This tranche advances CCTI-07/CCTI-10 from read-only relationship-signal inventory into a governed, additive candidate graph without mutating the canonical Content V2 relationship registry.

## Preserved canonical relationship layer

The existing Content V2 relationship registry contains **216 resolved relationships touching the CCTI corpus** under exact current Definition/source-ID matching:

- **189** `PRIMARY_ATTACK_USES`;
- **27** `CARRIES_EQUIPMENT`.

Those rows are copied into the private review artifact byte-for-byte as a preservation/reference set. They are not rewritten, re-identified, or re-promoted.

## New candidate edges

A conservative structured-field resolver produced **260** new cross-catalog candidate edges.

Evidence methods:

- **14** `EXACT_FULL_FIELD_UNIQUE_NAME` — the complete structured field equals one unique current canonical CCTI Definition name;
- **246** `EXACT_SPLIT_TOKEN_UNIQUE_NAME` — a delimiter-separated multi-word token equals one unique current canonical CCTI Definition name.

Candidate confidence/posture:

- **14 high-confidence review candidates** from exact whole-field identity;
- **246 medium-confidence review candidates** from exact multi-word enumerated tokens;
- all **260 remain `CANDIDATE_REVIEW`**, not canonical relationship promotions.

Source catalogs represented: Spacecraft **154**, Mecha **90**, EVA Suits **15**, Ranged Weapons **1**.

Target catalogs represented: Items **120**, Ranged Weapons **92**, Mecha **32**, Vehicles **15**, Computers **1**.

All resolved candidate endpoints use existing CCTI stable/current Definition identities. No fuzzy matching or same-name identity creation is used.

## Withheld exact-name signals

**96** otherwise exact-name signals were deliberately withheld rather than converted to edges:

- **95** occurrences of the one-word common term `Sonar`, which would otherwise collide with the canonical augmentation named `Sonar`; common-word equality is not sufficient evidence of intended cross-domain identity;
- **1** `Energy Shield Generator` signal where the exact name is self-colliding/ambiguous across current records and therefore cannot establish a cross-domain target automatically.

This is intentional evidence preservation, not missing accounting.

## Relationship semantics boundary

The new graph records only what the structured source field supports. It distinguishes definition-level signals such as:

- `DEFINITION_SYSTEM_REFERENCE`;
- `RESOURCE_OR_POWER_REFERENCE`.

It does **not** claim any runtime Asset Instance is installed, equipped, carried, owned, attached, fueled, loaded, or currently present. A definition stating that a mecha may use a named weapon or a spacecraft uses a named reactor is not an A8 runtime-instance ownership/custody/equipment fact.

Likewise:

- compatibility is not installation;
- an exact name is not a same-name identity merge;
- generic text is not a canonical target;
- unresolved/common-term signals remain reviewable rather than forced.

## Validation

PASS:

- all 260 candidate edge IDs are deterministic and unique;
- every candidate source and target Definition ID exists in the 11,017-row CCTI provenance reconstruction;
- zero candidate self-edges;
- all 216 existing relationship IDs remain unique and their CCTI target identities remain valid;
- no source/master CSV mutation;
- no canonical relationship-registry mutation;
- no runtime-instance state relationship was created.

## Private artifact

`CCTI_Cross_Domain_Graph_20260818.zip`  
SHA-256 `3656a30ec986de41bcf82f59f449f4a77a7b71202fc51823bc66976ce472e9ad`

The package contains the preserved 216-row resolved relationship reference, 260 new candidate edges, 96 withheld exact-name signals, and deterministic summary. Row-level candidate evidence remains private and checksum-referenced.

## Next

Proceed to the shared **context/compatibility candidate adoption** tranche using the exact governed shared-context authority. Preserve intrinsic/affinity/compatibility distinctions and do not promote source genre/style language directly into intrinsic identity or runtime compatibility facts.
