# PPIA-11 — Encounter & Balance Design Laboratory Foundation Candidate

**Work item:** PPIA-11  
**Milestone:** Source / Design Foundation  
**State:** CANDIDATE — requires exact-head hosted validation and merge  
**Application runtime/STAGE-A-A2 activation:** No

## Foundation result

PPIA-11 now has a bounded starting contract for encounter and balance design without inventing a universal challenge rating or rewriting source mechanics.

The foundation consists of:

- `PPIA-11_SOURCE_AND_DESIGN_INVENTORY.md`;
- `PPIA-11_SOURCE_MANIFEST_v0.1.0.json`;
- `PPIA-11_ENCOUNTER_BALANCE_TAXONOMY_v0.1.0.json`;
- `PPIA-11_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json`.

## Verified benchmark anchor

The completed 8D-007 harness supplies 18 coverage domains, 36 deterministic fixtures, 24 deterministic scenarios, 72 recorded scenario executions, ten observation areas, 36 non-destructive recommendations and seven mutation-sensitivity cases. Completion records zero source-truth changes, zero installation residue and zero blocking observations.

This evidence is deliberately bounded. Its target-band contract permits deterministic **within-domain** comparison and does not establish a universal cross-domain scalar.

## Inherited encounter inputs

PPIA-11 consumes completed contracts from:

- PPIA-02 Creature/NPC — definitions, placements, live instances and advisory encounter analysis;
- PPIA-03 Items/Equipment — equipment, mutable Item state and governed resource use;
- PPIA-04 Vehicles/Mecha/Starships — stations, systems, semantic movement/environment, resources and damage;
- PPIA-05 Species/Forms/Biology — forms, adaptations, senses, movement, compatibility and vulnerabilities;
- PPIA-07 Rune Construction — owning-rule outputs plus SCI/CSL with the explicit rule that SCI is not power and CSL is not a failure/damage formula;
- PPIA-08 Campaign/Scene/Session — encounter placement, objectives, hazards, semantic locations, environment, triggers and immutable Session context.

Those contracts retain their owning-domain authority.

## Five-class evidence model

Every later encounter-analysis statement must be classifiable as one of:

1. source truth;
2. inherited governed contract;
3. observed benchmark;
4. PPIA-11-authored methodology;
5. unresolved gap.

Observation and recommendation are never silently promoted to source truth.

## Encounter-factor taxonomy

The foundation defines 20 independently inspectable factor families covering encounter intent, participants, capability, output, survivability, action economy, resources, mobility/range, environment, objectives, hazards, mixed scale, boss/solo structure, waves/reinforcements, retreat/alternatives, information/uncertainty, benchmark evidence, observed peer comparison, calibration and provenance.

The taxonomy is an authored analysis vocabulary, **not** an automatic weighting formula.

## Uncertainty contract

Assessments may use `low`, `moderate`, `high` or `indeterminate` uncertainty. These labels communicate evidence quality and unresolved context; they do not represent probability of victory or numerical difficulty.

An `indeterminate` result is valid when governing mechanics or comparable evidence are insufficient. The system must prefer that result over fabricated certainty.

## Cross-domain boundaries

Ten explicit handoffs preserve Creature/NPC, Item, Vehicle, Biology, Rune, Scene/Session, Action, Permission, Recovery and 8D-007 benchmark ownership. PPIA-11 may consume authorized projections and generate recommendations; it does not absorb the authority to mutate those domains.

## Blocking invariants

- No universal CR, encounter-level, threat number or power scalar is invented.
- No within-domain target band becomes cross-domain equivalence.
- Source mechanics remain immutable under balance analysis.
- Benchmark observations and recommendations remain separate from source truth.
- Automatic balance rewrite is prohibited.
- Unknown values remain unknown and raise uncertainty rather than receiving numeric defaults.
- Action economy, environment, objectives and resource pressure remain separately visible.
- Cross-scale analysis requires explicit governing interaction rules.
- Map art, token density and dungeon geometry do not determine threat.
- Boss/wave/reinforcement/retreat methodology cannot invent missing source mechanics.
- AI may summarize, compare and propose only; consequential changes remain human/governed.
- No guaranteed-balance claim is permitted.
- No application runtime, STAGE-A-A2, release, deployment, tester, paid-service or production-credential activation occurs.

## Exact next milestone after foundation verification

After this foundation passes one exact-head hosted gate and merges, PPIA-11 should build the **Encounter Methodology & Benchmark Contract**: define human-facing encounter assessment/authoring steps, benchmark-encounter schema and initial deterministic encounter reference set over these factor families, while preserving uncertainty and calibration instead of promising guaranteed balance.
