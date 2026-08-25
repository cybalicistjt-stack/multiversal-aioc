# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-03; DPL-04 IN_PROGRESS  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-03 — Research, Study, Discovery & Experimentation Loop  
**Current item:** DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science  
**Implementation branch:** `integration/dpl-04-chemistry-pharmaceuticals-toxicology-laboratory-science`  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Purpose

DPL converts retained profession, science, industry, business, medicine, augmentation, arts and household material into deep gameplay loops over APW Projects, CEL, Economy, Crafting, ICF, Bases, Relationships and Character progression. It specifically prevents substantial source systems from disappearing inside generic Crafting or later content production.

## Current state

DPL-01 through DPL-03 are `completed_verified` with exact evidence preserved. DPL-03 completed on application PR #300, exact validated head `4a09540d6d83eace26ff4de84c556c5917f46c1f`, squash merge `8ff3403698fcaef8fed6c40bd46e802240b3c9ef`, deterministic receipt `c281ee62af2f1c665a0f3d669ce689aa20113da9b658119813b75aab845073c4`.

Owner **Continue** on 2026-08-25 governed-started **DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science** from exact AIOC `0b46334e506bf2b69f2cefcfec45945c74de292a` and application `8ff3403698fcaef8fed6c40bd46e802240b3c9ef`. DPL-04 is `in_progress` on `integration/dpl-04-chemistry-pharmaceuticals-toxicology-laboratory-science` with DPL-04-only implementation authority.

DPL-04 defines game-facing scientific chemistry/laboratory contracts for authored formulas, reagents, synthesis/process references, purity/concentration, stability, contamination, hazardous failure, pharmaceuticals, toxins and experimental compounds while composing over DPL-03 research and existing owner domains. Scientific chemistry remains distinct from MSS magical alchemy, and DPL-05 retains disease/injury/poison progression and long-term treatment/recovery.

## Tranches

1. **DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk** — `completed_verified`
2. **DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts** — `completed_verified`
3. **DPL-03 — Research, Study, Discovery & Experimentation Loop** — `completed_verified`
4. **DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science** — `in_progress`  
   Laboratory formulas, reagents, synthesis, purity/concentration, stability, contamination, hazardous failure, pharmaceuticals, toxins and experimental compounds without collapsing science into magical alchemy.
5. **DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery** — `planned`
6. **DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction** — `planned`
7. **DPL-07 — Refining, Industrial Processing, Manufacturing & Supply Chains** — `planned`
8. **DPL-08 — Business, Enterprise, Staffing, Operations & Growth** — `planned`
9. **DPL-09 — Apprenticeship, Mentorship, Teaching & Workforce Development** — `planned`
10. **DPL-10 — Arts, Performance, Recreation, Festivals & Cultural Practice** — `planned`
11. **DPL-11 — Household, Family, Dependents, Legacy & Inheritance** — `planned`
12. **DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery** — `planned`
13. **DPL-13 — Cybernetics, Symbiotes, Cloning & Biotech Augmentation** — `planned`
14. **DPL-14 — Economy, Cozy, Base, Project Integration, Balance & Golden Life Proof** — `planned`

## DPL-04 governed scope

DPL-04 must:

1. use DPL-03 research/evidence/discovery references for experimental chemistry rather than create a separate research ledger;
2. define scientific chemistry/process records with explicit source/provenance and setting/profile scope;
3. reference DPL-02 profession/activity profiles and APW/D26 Projects/tasks for laboratory work rather than create duplicate progression or scheduling truth;
4. reference MIB-12 for transformations/synthesis and MIB-14 for laboratory/facility capability rather than creating parallel process/facility state;
5. reference D17 Asset/Item/material ownership for reagents, samples, equipment and products;
6. represent authored purity, concentration, stability and contamination without silently inventing universal formulas or owner-state changes;
7. represent pharmaceutical/toxin effect handoffs while Character/Condition/ICF retain live biological/health state and DPL-05 retains disease/injury/poison progression and long-term treatment/recovery mechanics;
8. preserve World-Hazard-Action/Condition ownership for authored laboratory hazards and failures;
9. keep scientific chemistry distinct from MSS magical alchemy/enchanting except explicit authored crossovers;
10. introduce no real-money commerce and reserve no migration `0022` without demonstrated durable schema delta.

## Invariants

- APW, CEL, MIB-12/13/14, D17 Asset, ICF, Character, Progression-Abilities, Condition and Social-Relations retain owning truth.
- Science/chemistry remains distinct from magical alchemy except explicit crossover definitions.
- Research/discovery preserves provenance, unresolved/contradictory evidence and hidden-knowledge controls.
- DPL-05 retains disease/injury/poison progression and long-term recovery/treatment ownership.
- Disease, psychological and household mechanics are setting/content-sensitive and never globally forced.
- Augmentation cannot silently change Character identity, consent or agency.
- No real-money commerce is introduced.
- DPL-01 through DPL-03 are completed_verified and have no further implementation authority.
- DPL-04 implementation authority is bounded to the registered branch and this tranche only.
- DPL-05 and later DPL tranches remain unauthorized until selected and governed-started in strict order.
- Migration `0022` remains unreserved.
