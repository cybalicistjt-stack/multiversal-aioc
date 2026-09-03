# ENV-01 Completion Report — Environment Model & Composition Contract

**Status:** completed_verified candidate pending exact-head repository-health validation  
**Program:** ENV  
**Application implementation authority:** none

## Source basis used

ENV-01 was grounded in the retained Batch 8B environment promotion package and DB-004 exploration/environment framework excerpt. The current promoted package contains forty reusable Environment Definitions and preserves full source text/provenance separately from definition identity.

The controlling environment framework states that environments may define terrain, climate, gravity, atmosphere, pressure, light, radiation, corruption/supernatural influence, hazards, movement constraints, visibility, resources, encounters and adaptations; it also requires species, equipment, vehicles, powers and temporary adaptations to be evaluated against the environment rather than duplicated into it.

## Completed decisions

1. Established four durable authoring layers: **Environment Archetype**, **Environment Preset**, **Environment Overlay**, and **Local Environment Instance**.
2. Established **Resolved Environment** as a derived read-only evaluation projection, not a fifth canonical source-of-truth object.
3. Established presets as composition recipes rather than duplicated comprehensive rulebooks.
4. Allowed a preset to have one primary archetype plus optional secondary component archetypes for genuinely compound environments.
5. Established overlays as reusable environmental deltas rather than base environment identities.
6. Established the composition order: archetype baseline(s) → preset defaults → local instance configuration → active overlays → runtime scene state → participant evaluation.
7. Explicitly separated composition precedence from source/canonical authority precedence.
8. Established immutable inheritance: editing a higher layer never mutates referenced lower-layer definitions or historical source records.
9. Established typed explicit override/delta intent rather than implicit last-write-wins replacement.
10. Preserved historical/source environment profiles and their provenance through modularization.
11. Preserved external ownership of Character/Species/Creature/Ability/Item/Vehicle/World/Place/Encounter/runtime state.
12. Established a Habitat Signature envelope for later CEW consumption without prematurely freezing the vocabulary before ENV-15.
13. Deferred detailed overlay conflict/stacking/severity semantics to ENV-04; conflicts remain visible until governed resolution rather than being guessed.
14. Preserved the parallel-content boundary: no `Multiversal-app`, SCL, migration, runtime encounter, or environment UI mutation is authorized.

## Produced artifacts

- `ENV-01_ENVIRONMENT_MODEL_COMPOSITION_CONTRACT_v1.0.0.md`
- `ENV-01_COMPOSITION_MODEL_v1.0.0.json`
- `tests/control_plane/test_env01_composition_contract.py`
- updated `ENV_PROGRAM_BACKLOG.json`
- updated `ENV_ENVIRONMENT_PRESET_OVERLAY_PROGRAM.md`

## Verification target

Repository health must validate the exact PR head and run the control-plane regression suite including `test_env01_composition_contract.py`.

## Exact next tranche

**ENV-02 — Existing 40 Completeness Repair**

ENV-02 must complete the known missing random encounter / encounter-challenge / rest-shelter content in the existing forty source-backed profiles before ENV-03/04/05 decompose them into reusable archetypes, overlays and presets. It must not fabricate missing environment-Ability links merely for field completeness.
