# AKWI-02 — Akwi Lore & Culture Pack

Version: 1.0.0  
Status: COMPLETED_VERIFIED  
Owner authority: John Brandon Turner  
Authorized: 2026-08-30  
Completed: 2026-08-30  
Application baseline: `a69d12843a49d7903a81ea2dd942fd5e5cb719c2`  
Tested application head: `33e274b566054e9c6cf326f91f858bd615006ace`  
Application PR: `#355`  
Application merge: `0c12b20b96add5aa2a82583d7bd33cb86f08c8f8`  
Validation run: `33324968994`  
AIOC baseline: `884f0833a0f0a86b0329244328462918f1a5564c`

## Objective

Integrate the source-backed and already-accepted Akwi lore layer that supports the playable Species without silently promoting proposed language or generated NPC scaffolding into canon.

## Implemented content

AKWI-02 publishes exactly 33 governed records from `akwi_game_integration_package_v0.1.zip`:

- five `SUPPLIED_CANON` culture/institution/tradition rows from `akwi_cultures.csv`;
- five `SUPPLIED_CANON` homeworld/core-lore rows from `akwi_homeworld_core.csv`;
- ten `ACCEPTED_IN_THIS_CONVERSATION` background concepts from `akwi_backgrounds.csv`, with exact grants/mechanics still unresolved;
- the accepted working `language.twil` language object;
- exactly twelve `ACCEPTED_IN_THIS_CONVERSATION` Twil lexemes.

The corpus also contains exactly 36 governed relationships and provenance coverage for all 33 records.

## Preserved exclusions

The following were deliberately not promoted:

- proposed `culture.akwi.halionian-diaspora`;
- inferred Twiloni/Azerkiji region objects or stable-ID references;
- 90 proposed/inferred Twil lexemes;
- all 80 proposed phrasebook rows;
- automatic Twil inheritance from `species.akwi`;
- exact mechanical background grants;
- the 400-NPC library and its generated setting/faction/location dependency universe.

## Boundaries

- Culture, language, background, profession, equipment, and social institutions are not inherited Species biology.
- Selecting `species.akwi` does not automatically grant Twil.
- Background records are descriptive/semantic until a rules profile approves exact grants or mathematics.
- The Protective-Duty Tradition remains source-backed and retains its non-biological, non-compulsory, non-ownership framing and content-review status.
- Unknown homeworld facts remain unknown.
- Generic A2 profiles are reused. No Akwi-only lore UI was created.
- SSA software-track authority remains unchanged.
- AKWI-03 NPC-library work is separately Owner-authorized and must begin from this verified AKWI-02 merge baseline.

## Verification evidence

Exact application head `33e274b566054e9c6cf326f91f858bd615006ace` passed validation run `33324968994`:

- current-family selector and repository health: PASS;
- AKWI-02 Linux shared validation: PASS;
- AKWI-02 Windows shared validation: PASS;
- deterministic cross-platform comparison: PASS.

The final profile included the AKWI-02 source invariant verifier, client typecheck, focused AKWI-02 tests, A2 runtime-projection regression, and AKWI-01 playable-Species regression.

Two evidence-backed repairs were required before the green run: removal of a residual proposed diaspora stable-ID reference, and correction of the focused test's runtime fixture path. Neither repair widened scope.

AKWI-02 is therefore complete at the current implemented A2 lore/content boundary. AKWI-03 remains a separate content-library tranche.