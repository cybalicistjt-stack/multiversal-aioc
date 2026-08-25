# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-01; DPL-02 SELECTED_NOT_STARTED  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk  
**Current item:** DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts  
**Implementation branch:** none; DPL-02 selection grants no implementation authority  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Purpose

DPL converts retained profession, science, industry, business, medicine, augmentation, arts and household material into deep gameplay loops over APW Projects, CEL, Economy, Crafting, ICF, Bases, Relationships and Character progression. It specifically prevents substantial source systems from disappearing inside generic Crafting or later content production.

## Current state

DPL-01 is `completed_verified` on application PR #298. Exact validated head `f579dc5d70694c60cb3ef479f12cd27cf0db0beb` passed Repository Health `32805418340/97674484510`, Validation Core `32805418516`, Linux `97674484888`, Windows `97674485105` and deterministic comparison `97674543238`, with deterministic receipt `8d33869b0a095e290a150130d7667015cc0317971865a171d5aa7689041e5d75`. It squash-merged as `e6a4eebfb5c7efe603424b20155a9a52af04c240` after three bounded verifier-evidence repair cycles.

DPL-01 inventoried 27 PDFs / 567 pages, 7 structured catalogs / 6,809 rows, all 11 retained profession source-tree families and 58 retained concept dispositions. It preserved APW/D26, CEL/APM, MIB-12/13/14, D17 Asset, Character-Actors, Progression-Abilities, Condition, Social-Relations, ICF, World/Hazard/Action, MSS and CCP authority and proved that scientific chemistry/pharmaceuticals remain distinct from magical alchemy/enchanting.

Strict order now selects **DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts** as `selected_not_started`. No DPL-02 implementation branch exists and selection alone grants no implementation authority. The next owner `Continue` must governed-start DPL-02 from the then-current canonical AIOC/application heads.

## Tranches

1. **DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk** — `completed_verified`  
   Reconciled profession/science/medicine/business/mining/arts/augmentation/life sources with current owner domains and classified profession profiles, Projects, recipes/processes, services, conditions and content.

2. **DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts** — `selected_not_started`  
   Reusable profession profiles with skills/knowledge, tools, facilities, authored credentials, services, quality/risk/time, Project templates and progression/economy hooks. Must reference existing owners rather than create duplicate truth.

3. **DPL-03 — Research, Study, Discovery & Experimentation Loop** — `planned`  
   Question/hypothesis → plan → research/experiment → evidence/result → contradiction/failure/partial success → discovery → application/publication, usable by science, magic, archaeology and engineering with provenance and hidden-knowledge controls.

4. **DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science** — `planned`  
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

## DPL-02 handoff from DPL-01

DPL-02 must:

1. reference canonical Character/Progression abilities rather than copying them;
2. reference APW Projects/tasks for durable work rather than creating a scheduler;
3. reference MIB-12 transformations, MIB-13 economy and MIB-14 facilities rather than duplicating them;
4. carry explicit source/provenance references and setting/profile scope;
5. allow profession profiles to point toward later science, health, extraction, industry, business, teaching, culture, household and augmentation verticals without implementing those later mechanics;
6. preserve science/alchemy separation;
7. introduce no real-money commerce and reserve no migration `0022`.

## Invariants

- APW, CEL, MIB-12/13/14, D17 Asset, ICF, Character, Progression-Abilities, Condition and Social-Relations retain owning truth.
- Science/chemistry remains distinct from magical alchemy except explicit crossover definitions.
- Disease, psychological and household mechanics are setting/content-sensitive and never globally forced.
- Augmentation cannot silently change Character identity, consent or agency.
- No real-money commerce is introduced.
- DPL-01 is completed_verified and has no further implementation authority.
- DPL-02 is selected_not_started and has no implementation authority until a later owner Continue governed-starts it.
- DPL-03 and later DPL tranches remain unauthorized until selected and governed-started in strict order.
- Migration `0022` remains unreserved.
