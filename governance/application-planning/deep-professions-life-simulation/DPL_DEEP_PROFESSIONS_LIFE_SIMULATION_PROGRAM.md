# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-02; DPL-03 IN_PROGRESS  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts  
**Current item:** DPL-03 — Research, Study, Discovery & Experimentation Loop  
**Implementation branch:** `integration/dpl-03-research-study-discovery-experimentation-loop`  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Purpose

DPL converts retained profession, science, industry, business, medicine, augmentation, arts and household material into deep gameplay loops over APW Projects, CEL, Economy, Crafting, ICF, Bases, Relationships and Character progression. It specifically prevents substantial source systems from disappearing inside generic Crafting or later content production.

## Current state

DPL-01 is `completed_verified` on application PR #298 and application merge `e6a4eebfb5c7efe603424b20155a9a52af04c240`.

DPL-02 is `completed_verified` on application PR #299. Exact validated head `2f04a85a92696c51786d8163041cade611a72ec9` passed Repository Health `32807048203/97679083461`, Validation Core `32807048284`, Linux `97679083889`, Windows `97679083915` and deterministic comparison `97679219595`, with deterministic receipt `61ad37be651f41adf2036f80d14cb872cc224f994b1f396a3e91f9ba94c5be72`. It squash-merged as `fd197f6b98a55e0835fbad08a55b28d57f3a127e` after one bounded validation-profile metadata repair cycle.

Owner **Continue** on 2026-08-25 governed-started **DPL-03 — Research, Study, Discovery & Experimentation Loop** from exact AIOC `19eba96921cabf57a18d2925e73a013b4706fd90` and application `fd197f6b98a55e0835fbad08a55b28d57f3a127e`. DPL-03 is `in_progress` on `integration/dpl-03-research-study-discovery-experimentation-loop` with DPL-03-only implementation authority.

DPL-03 defines one reusable question/hypothesis → plan → research/experiment → evidence/result → contradiction/failure/partial success → discovery → application/publication loop. It must preserve explicit source/provenance and setting/profile scope, apply visibility/reveal authorization before projection/publication, and consume DPL-02/APW/Character/Progression/MIB/MSS/World/GM owners by reference rather than creating duplicate truth.

## Tranches

1. **DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk** — `completed_verified`  
   Reconciled profession/science/medicine/business/mining/arts/augmentation/life sources with current owner domains and classified profession profiles, Projects, recipes/processes, services, conditions and content.

2. **DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts** — `completed_verified`  
   Reusable profession/activity profiles, owner-backed mastery/credential definitions and professional service contracts composed by reference to existing owners.

3. **DPL-03 — Research, Study, Discovery & Experimentation Loop** — `in_progress`  
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

## DPL-03 governed scope

DPL-03 must:

1. define reusable question/hypothesis, plan, research/experiment activity, evidence/result, discovery and application/publication contracts;
2. retain contradiction, failure, inconclusive and partial-success outcomes rather than silently resolving them;
3. carry explicit source/provenance and setting/profile scope on evidence, results and discoveries;
4. apply visibility/reveal authorization before search, projection or publication so hidden knowledge cannot leak;
5. reference DPL-02 profession/activity profiles rather than duplicating profession capability truth;
6. reference APW/D26 Projects/tasks/campaign-time rather than create a scheduler or wall-clock progress;
7. reference Character/Progression, MIB-12 transformations, MIB-14 facilities, MSS and World/GM visibility owners rather than replacing them;
8. support scientific, magical, archaeological and engineering contexts through one contract without collapsing science into magic or inventing universal formulas;
9. avoid automatic discovery/publication and require explicit authored/owner authorization for reveal or publication handoffs;
10. implement no DPL-04+ vertical mechanics, no real-money commerce and no migration `0022` reservation.

## Invariants

- APW, CEL, MIB-12/13/14, D17 Asset, ICF, Character, Progression-Abilities, Condition and Social-Relations retain owning truth.
- Science/chemistry remains distinct from magical alchemy except explicit crossover definitions.
- Mastery and credentials cannot silently grant progression, identity, authority or setting status.
- Service contracts do not own prices, balances, settlement, reputation or relationship truth.
- Research/discovery must preserve provenance, unresolved/contradictory evidence and hidden-knowledge controls.
- Discovery and publication cannot bypass visibility, GM, setting or source-profile authority.
- Disease, psychological and household mechanics are setting/content-sensitive and never globally forced.
- Augmentation cannot silently change Character identity, consent or agency.
- No real-money commerce is introduced.
- DPL-01 and DPL-02 are completed_verified and have no further implementation authority.
- DPL-03 implementation authority is bounded to the registered branch and this tranche only.
- DPL-04 and later DPL tranches remain unauthorized until selected and governed-started in strict order.
- Migration `0022` remains unreserved.
