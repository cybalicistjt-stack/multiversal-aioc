# CCTI Shared Context and Compatibility Candidate Review

**Date:** 2026-08-18  
**Status:** candidate tranche complete; not enabled; compatibility outcomes not evaluated

This tranche advances the CCTI-08/CCTI-10 shared context/compatibility work using the exact checksum-verified Reality v0.14.0 shared-context authority and the exact Item v0.12.0 / Platform v0.11.0 preparation evidence.

## Exact shared authority

The Reality v0.14.0 preparation copies the nine shared content facets verbatim from the Item preparation authority. The exact shared registry contains **241 controlled values** across:

- Setting Family — 10;
- Era / Development — 14;
- Technology Paradigm — 31;
- Power Paradigm — 24;
- Environment — 27;
- Play Domain — 26;
- Tone / Style — 20;
- Content Scale — 13;
- Genre Tradition — 76.

Exact Reality v0.14.0 ZIP SHA-256: `928aaacbd84082d88ea9e64fc6c3506a321f26633bce718cfb46199b5364f4d6`.

## Item corpus

All **5,389** Item/reference rows are carried forward from the exact Item v0.12.0 prepared row-level crosswalk rather than remapped from scratch.

- **5,181** rows contain one or more prepared shared-context candidate IDs;
- **208** rows contain no shared-context candidate IDs in the preparation preview;
- **63** exact `All Genres` rows remain a broad compatibility source signal and are **not** converted into a genre/family taxonomy identity;
- the original prepared mapping/review state remains visible and noncanonical.

Exact Item v0.12.0 ZIP SHA-256: `d12feab1375930e1ef5c121d485aee8622f2abfc34c05f23babb26a293ee47ca`.

## Platform corpus

All **5,628** Vehicle/Mecha/Spacecraft-domain rows retain their raw Genre, Technology/Style and environment source strings as provenance. Platform context candidates are added only where an exact governed mapping can be reused safely.

**2,680** Platform rows receive one or more shared-context candidate IDs. **2,948** remain source-signal-only with no normalized shared-context ID in this tranche.

Genre signal handling:

- **2,516** rows reuse an exact source-value mapping already governed by the Item v0.12.0 genre crosswalk;
- **668** rows retain `Multiversal / Core Rules` as a broad compatibility source signal with no taxonomy identity assignment;
- **163** rows have an exact unique shared-registry name match and are retained as review-required candidates;
- **2,281** rows remain unmapped source signals rather than receiving invented semantic mappings.

Technology/style handling:

- **491** rows reuse an exact source-value mapping already governed by the Item v0.12.0 technology crosswalk;
- **544** rows hit an exact existing crosswalk entry whose disposition is review-required and therefore receive no forced ID;
- **4,593** rows remain unmapped technology/style source signals.

Environment handling:

- all **5,628** Platform rows preserve their current environment/operating-theater source evidence;
- no platform environment string exactly matched a complete governed Environment value under the conservative whole-value rule, so no keyword-derived Platform environment taxonomy assertion is introduced here.

Exact Platform v0.11.0 ZIP SHA-256: `621b498b6d0fa1b99c86a96eac7446f682c715cb576cf0803d233ec2ffe0bdb6`.

## Required semantic separation

The exact preparation rules are preserved:

- universal taxonomy assertions describe what the object is and must not be replaced by genre/setting affinities;
- source Genre/Tech/Environment strings remain provenance after normalized candidates exist;
- affinity describes contexts the content strongly evokes;
- compatibility is evaluated from intrinsic requirements, setting/profile state, governed exceptions and rules support;
- broad compatibility does not create a taxonomy identity;
- compatibility does not mean common, legal, inexpensive, available, or narratively important.

**No final compatibility result is calculated in this tranche.** Every row remains `compatibility_outcome = NOT_EVALUATED`. The package is a context/compatibility candidate-evidence layer, not a runtime compatibility service or canonical enablement package.

## Validation

PASS:

- **11,017/11,017** CCTI rows accounted;
- all normalized candidate IDs belong to the exact 241-value shared authority;
- source record keys are unique within the twelve-catalog corpus;
- exact Item prepared candidates are preserved rather than regenerated;
- Platform mappings use exact pre-governed source-value equality or exact unique shared-registry name equality only;
- no fuzzy semantic mapping was used;
- no runtime compatibility outcome or Asset-instance state was invented;
- no source/master CSV mutation;
- no canonical context/compatibility enablement;
- no `GAME_READY` claim;
- deterministic private artifact rebuild reproduces the same SHA-256.

## Private artifact

`CCTI_Shared_Context_Compatibility_Candidates_20260818.zip`  
SHA-256 `f915b046c963a6ac2a9849f429946fb3b6cefbc23beeeb737c6c8cb19d9ec106`

The package contains the complete 11,017-row candidate ledger, review queue, exact shared-authority manifest and deterministic aggregate summary. Row-level private corpus evidence remains outside the governance repository and is checksum-referenced.

## Next

Proceed to **CCTI-11 full candidate-package validation**. Validate the complete 11,017-row CCTI candidate state across Item taxonomy, Platform taxonomy/routing, cross-domain candidate relationships, shared context candidates, identity/provenance preservation, and Definition/Model-versus-runtime-Asset boundaries. CCTI-12 app-facing integration remains owner-gated and must not start merely because CCTI-11 passes.
