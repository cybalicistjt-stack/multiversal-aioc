# AKWI-01 — Playable Species Core

Version: 1.0.0  
Status: COMPLETED / VERIFIED  
Owner authority: John Brandon Turner  
Authorized: 2026-08-30  
Completed: 2026-08-30  
Application repository: `cybalicistjt-stack/Multiversal-app`  
Application branch: `integration/akwi-01-playable-species-core`  
Application baseline: `88cb2b44b216fcb661c3d8199bff7b06d7b1db50`  
Tested application head: `148364c8d4a9ed6005cd8df3e913447de4c76e9c`  
Application PR: `#354`  
Application merge: `a69d12843a49d7903a81ea2dd942fd5e5cb719c2`  
Validation run: `33323890646`  
AIOC repository: `cybalicistjt-stack/multiversal-aioc`  
AIOC branch: `integration/akwi-01-playable-species-core`  
AIOC baseline: `60f75d15eb7d197dde2abffccb7a071cbea321f5`

## 1. Objective

AKWI-01 integrates Akwi as a governed playable Species through the existing Universal Object and Character Creation architecture without creating Akwi-specific UI, a parallel Character system, a parallel rules engine, or unsupported canonical facts.

Completion is intentionally bounded to the current implemented A2/A4/content-contract boundary. It does not claim that the placeholder rules runtime executes live exhaustion or injury.

## 2. Source basis and evidence classes

The tranche was grounded in three supplied source families:

1. `Akwi Concept Design.mht` — source conversation and Akwi biological/mechanical assertions.
2. `akwi_game_integration_package_v0.1.zip` — normalized Species, feature, Character Creation, mechanics, provenance/truth, visibility, and decision material.
3. `akwi_npc_suite_400.csv` — downstream NPC corpus. Its packaged copy was verified byte-for-byte identical to the separately supplied CSV.

Implemented claims preserve these evidence classes:

- `SOURCE_ESTABLISHED`: supported by supplied source or source-backed normalized records.
- `OWNER_APPROVED`: explicitly resolved by the Owner for AKWI-01.
- `IMPLEMENTATION_POLICY`: deterministic game interpretation required for playability where exact system math is not source canon.
- `PROPOSED` / `UNKNOWN`: remains noncanonical/nonexecuting until separately approved.

Implementation policy is not rewritten as source canon.

## 3. Owner-approved AKWI-01 rulings

### Hearing

- Preserve approximately 20% stronger attentive hearing than the supplied human comparison baseline.
- Additional useful detail requires attention.
- No universal die, DC, or numeric modifier is invented.
- A future rules profile may translate the source percentage only when it exposes an appropriate auditory quantity.

### Magnetic orientation

- Magnetoreception is a weak biological environmental sense.
- On a’Wiio, the shifting magnetic field is experienced more like a moving ocean and does not naturally provide a stable compass direction.
- Reliable directional use requires a stable field at least Earth strength, the Akwi to stop, calm/focus, and no meaningful local interference.
- Successful use gives weak direction information only. It is not radar, creature detection, dimensional sensing, or perfect passive compass knowledge.

### Pressure and airflow

- Akwi passively receive meaningful nearby pressure and airflow information through the aural sensory complex.
- This is not echolocation or a substitute for vision.
- Subtle or obstructed cases remain rules-profile-specific rather than receiving invented universal numbers.

### Spring-Leg Anatomy

- Akwi have an explicit enhanced-jumping/mobility capability.
- The biological reference is a standing vertical jump around two to three times the Akwi's height at a’Wiio-equivalent gravity without meaningful burden.
- Safe controlled landing from the Akwi's own jump output is preserved.
- No single exact gameplay multiplier is defined until a governing movement rules profile supplies the quantity and translation.

### Burst

Source/approved constraints preserved:

- a fully recovered Akwi has two ordinary Burst reserves;
- normal Burst use must be frequent enough to make the Species meaningful in play;
- uses 1–2 in a full-recovery cycle are the safe band and add no Burst-specific exhaustion;
- forced uses 3–6 are the strain band and add escalating strain/exhaustion;
- use 7 and above is overload, beyond the 3:1 boundary relative to the two-use safe capacity, and requires severe exhaustion plus injury risk;
- ideal full recovery is approximately 48 hours with safe rest/sleep and substantial nourishment;
- no unsupported partial-recovery formula is invented;
- no universal injury die/check formula is invented because the current generic live exhaustion/injury runtime does not yet exist.

The generic contract classifies these outcomes deterministically but does not mutate Characters, apply Conditions, heal, or roll injuries.

## 4. Implemented reusable content

The merged application contains exactly one Akwi Species record plus 15 governed reusable feature records.

Species:

- `species.akwi`

Reusable feature records:

- `feature.akwi.aural-sensory-complex`
- `sense.akwi.enhanced-hearing`
- `sense.akwi.magnetoreception`
- `sense.akwi.pressure-airflow-integration`
- `trait.akwi.ear-spatial-calibration`
- `trait.akwi.expressive-ear-physiology`
- `limitation.akwi.exposed-sensory-ears`
- `feature.akwi.spring-leg-anatomy`
- `trait.akwi.short-burst-physiology`
- `ability.akwi.burst`
- `trait.akwi.accelerated-metabolism`
- `trait.akwi.high-register-vocal-range`
- `trait.akwi.thick-nail-claws`
- `trait.akwi.furred-body-covering`
- `trait.akwi.body-size-variation`

The Species record has 15 resolved `HAS_SPECIES_FEATURE` relationships and the supplemental package has provenance coverage for all 16 records.

The fixed Character-facing Species grant bundle is deliberately smaller than the complete descriptive feature catalog and currently references:

- `feature.akwi.aural-sensory-complex`
- `feature.akwi.spring-leg-anatomy`
- `ability.akwi.burst`
- `trait.akwi.accelerated-metabolism`
- `trait.akwi.expressive-ear-physiology`
- `trait.akwi.furred-body-covering`
- `trait.akwi.high-register-vocal-range`
- `trait.akwi.thick-nail-claws`
- `trait.akwi.body-size-variation`

Child/component sensory and limitation records remain reusable resolvable definitions without being duplicated as extra stacked grants.

## 5. A2 content integration

Akwi uses the generic `P-A2-SPECIES` presentation profile. Its reusable Species Perks use the existing generic ability presentation path.

AKWI-01 added a generic governed supplemental-corpus seam rather than rewriting the large generated base corpus or injecting Akwi directly into a picker. The generated corpus and supplemental files are merged into one immutable corpus before authorization, facets, search, counts, relationship traversal, provenance, comparison, or Picker use.

Duplicate stable IDs across base and supplemental sources are a blocking integrity error, so supplemental records cannot silently shadow canonical generated objects.

## 6. A4 Character Creation integration

Akwi reuses the existing single-selection `species-or-form` Character Creation category.

Selection continues to produce nonauthoritative local draft intent and a stable-ID selection receipt until normal authoritative A4 validation/save boundaries run. No Akwi-specific Character Creation screen was added.

AKWI-01 establishes no approved Akwi lineage, subspecies, alternate Form, or optional Species branch. None was fabricated.

Culture, language, background, profession, equipment, and upbringing are not inherited Species biology and are not automatically granted merely by choosing Akwi.

## 7. Generic physiology contract

`packages/contracts/src/a4/species-physiology-port.ts` provides deterministic generic policy evaluation for:

- magnetic orientation eligibility; and
- physiological Burst use bands.

The contract is Species-reusable and does not create an Akwi-only hidden rules engine.

The current `packages/rules-runtime` remains a placeholder; therefore AKWI-01 completion does not claim authoritative live Condition/exhaustion/injury mutation.

## 8. Visibility and provenance

Player-visible Species truth remains subject to normal authorization and entitlement projection boundaries.

Proposed authoring notes, unresolved mechanics, hidden weaknesses, private Character facts, GM-only facts, protected counts, and unrevealed biology are not promoted into ordinary player truth by AKWI-01.

The 400-NPC corpus and generated world dependencies were not promoted simply because they exist downstream.

## 9. Explicit exclusions preserved

AKWI-01 did not implement or authorize:

- bulk import of the 400 Akwi NPCs;
- canonization/import of the generated NPC setting/faction/location dependency universe;
- bulk Twil/Twii language integration;
- full culture/background/homeworld package integration beyond currently approved Species-facing references;
- invented Akwi lineages, subspecies, alternate Forms, transformations, or adaptations;
- a universal live exhaustion/injury engine;
- an Akwi-specific Character Creation UI;
- a durable persistence migration;
- changes to the active SSA software-family ownership or software-track work pointer.

## 10. Verification evidence

Exact candidate head: `148364c8d4a9ed6005cd8df3e913447de4c76e9c`

GitHub Actions run `33323890646` produced:

- Current family selector and repository health: **PASS**
- Explicit reviewed-integration profile selection for `AKWI-01`: **PASS**
- AKWI-01 Linux shared validation: **PASS**
- AKWI-01 Windows shared validation: **PASS**
- Deterministic Linux/Windows receipt comparison: **PASS**
- Unrelated historical validation fanout observed: **0**

The first Linux attempt failed only because the focused test used an environment-dependent `import.meta.url` file path. That evidence caused a bounded repair to resolve fixture files from the client workspace. The fresh exact-head run above passed both platforms and deterministic comparison.

Application PR `#354` was squash-merged only after that evidence, producing application main commit `a69d12843a49d7903a81ea2dd942fd5e5cb719c2`.

## 11. Completion statement

AKWI-01 is complete and verified.

This means Akwi is integrated as a governed playable Species at the current application's implemented A2/A4/content-contract boundary: governed Species and reusable feature records exist, the Species is discoverable/inspectable through the generic Universal Object model, it is compatible with the existing A4 `species-or-form` selection flow, its provenance and relationships are present, and its owner-approved magnetic/Burst semantics have deterministic generic contracts and exact-head cross-platform evidence.

It does **not** mean the placeholder rules runtime now executes live exhaustion/injury, nor does it mean AKWI-02 lore/culture or AKWI-03 NPC-library content has been implemented.
