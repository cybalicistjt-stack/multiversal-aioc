# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-03; DPL-04 SELECTED_NOT_STARTED  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-03 — Research, Study, Discovery & Experimentation Loop  
**Current item:** DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science  
**Implementation branch:** none; DPL-04 selection grants no implementation authority  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Purpose

DPL converts retained profession, science, industry, business, medicine, augmentation, arts and household material into deep gameplay loops over APW Projects, CEL, Economy, Crafting, ICF, Bases, Relationships and Character progression. It specifically prevents substantial source systems from disappearing inside generic Crafting or later content production.

## Current state

DPL-01 and DPL-02 remain `completed_verified` with their prior exact evidence preserved.

DPL-03 is `completed_verified` on application PR #300. Exact validated head `4a09540d6d83eace26ff4de84c556c5917f46c1f` passed Repository Health `32812245186/97693684488`, Validation Core `32812246552`, Linux `97693687775`, Windows `97693687773` and deterministic comparison `97694250415`, with deterministic receipt `c281ee62af2f1c665a0f3d669ce689aa20113da9b658119813b75aab845073c4`. It squash-merged as `8ff3403698fcaef8fed6c40bd46e802240b3c9ef` after one bounded repair cycle replacing a stale historical APW-I06 migration-0019 validator with a current D26 ownership invariant.

DPL-03 delivered a common provenance-preserving research loop across scientific, magical, archaeological and engineering contexts: 4 questions, 4 hypotheses, 4 plans, 5 evidence records, 4 results and 4 discoveries. Contradictory evidence remains explicit, visibility is filtered before projection/publication, discovery/publication are never automatic, and science remains distinct from magic.

Strict order now selects **DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science** as `selected_not_started`. No DPL-04 implementation branch exists and selection alone grants no implementation authority. The next owner `Continue` must governed-start DPL-04 from the then-current canonical AIOC/application heads.

## Tranches

1. **DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk** — `completed_verified`  
   Reconciled profession/science/medicine/business/mining/arts/augmentation/life sources with current owner domains and classified profession profiles, Projects, recipes/processes, services, conditions and content.

2. **DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts** — `completed_verified`  
   Reusable profession/activity profiles, owner-backed mastery/credential definitions and professional service contracts composed by reference to existing owners.

3. **DPL-03 — Research, Study, Discovery & Experimentation Loop** — `completed_verified`  
   Provenance-preserving research loop across science, magic, archaeology and engineering with explicit contradiction/failure states and hidden-knowledge-safe projection/publication handoffs.

4. **DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science** — `selected_not_started`  
   Laboratory formulas, reagents, synthesis, purity/concentration, stability, contamination, hazardous failure, pharmaceuticals, toxins and experimental compounds without collapsing science into magical alchemy.

5. **DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery** — `planned`  
   Diagnosis, treatment, procedures, disease incubation/progression, exposure, poison dose/decay, lasting injury, rehabilitation, immunity/resistance and care Projects over existing Character/Condition/ICF systems.

6. **DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction** — `planned`  
   Survey/prospecting, deposits/veins, grade, access, tools/facilities, extraction, depletion, hazards, workforce, World consequences and canonical material outputs.

7. **DPL-07 — Refining, Industrial Processing, Manufacturing & Supply Chains** — `planned`  
   Refining, smelting, milling, industrial/chemical processing, batch production, manufacturing capacity, storage, logistics, waste/byproducts and facility integration while MIB-12 owns transformations.

8. **DPL-08 — Business, Enterprise, Staffing, Operations & Growth** — `planned`  
   Sustained enterprises with staffing, wages/costs, capacity, inventory/services, contracts, customers, reputation, branches, management roles, supply chains, reinvestment and setbacks; no real-money commerce.

9. **DPL-09 — Apprenticeship, Mentorship, Teaching & Workforce Development** — `planned`  
   Trainers/mentors/apprentices, curricula/tasks, supervised practice, teaching Projects, credentials and workforce development without bypassing Character advancement.

10. **DPL-10 — Arts, Performance, Recreation, Festivals & Cultural Practice** — `planned`  
    Artistic creation/performance, commissions, competitions, hobbies, games/leisure, festivals, audiences, cultural practice, reputation and authored social/economic effects.

11. **DPL-11 — Household, Family, Dependents, Legacy & Inheritance** — `planned`  
    Optional household/family/partner/dependent structures, household Projects/resources, inheritance/succession and long-term life events, separate from MIB-17 parental-control authority.

12. **DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery** — `planned`  
    Setting-profiled fear/horror/stress/trauma/sanity mechanics, temporary/persistent effects, treatment/rest/recovery and privacy-safe projections; never globally mandatory.

13. **DPL-13 — Cybernetics, Symbiotes, Cloning & Biotech Augmentation** — `planned`  
    Character-integrated augmentation procedures, anatomy/slot compatibility, installation, power/upkeep, rejection/complications, damage/repair, symbiote bond/agency, clone identity/provenance and biotech mutation.

14. **DPL-14 — Economy, Cozy, Base, Project Integration, Balance & Golden Life Proof** — `planned`  
    Prove cross-profession loops spanning research, production, health, extraction, business, training, culture, household and augmentation with bounded APW/CEL automation, Workbench surfaces and no-AI operation.

## DPL-04 handoff from DPL-03

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
- DPL-04 is selected_not_started and has no implementation authority until a later owner Continue governed-starts it.
- DPL-05 and later DPL tranches remain unauthorized until selected and governed-started in strict order.
- Migration `0022` remains unreserved.
