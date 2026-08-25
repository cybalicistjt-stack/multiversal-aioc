# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-04; DPL-05 IN_PROGRESS  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science  
**Current item:** DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery  
**Implementation branch:** `integration/dpl-05-medicine-disease-injury-poison-long-term-recovery`  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner

## Purpose

DPL converts retained profession, science, industry, business, medicine, augmentation, arts and household material into deep gameplay loops over APW Projects, CEL, Economy, Crafting, ICF, Bases, Relationships and Character progression while preserving each existing owner domain.

## Current state

DPL-01 through DPL-04 are `completed_verified` with exact evidence preserved. DPL-04 completed on application PR #301, exact validated head `188d7ce85dcdacd560e0d763daf18ecd28bf1502`, deterministic receipt `f92b1b51150f9447d4b13a0357f998824603e00dfdb666bb1b60826220045f05`, and squash merge `0ebd5c59f25369b41ab25c4840c346655fc8ef04` with zero CI repair cycles.

Owner **Continue** on 2026-08-25 governed-started **DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery** from exact AIOC `5aa3d21d1369068118be660578b7653792b39fed` and application `0ebd5c59f25369b41ab25c4840c346655fc8ef04`. DPL-05 is `in_progress` on `integration/dpl-05-medicine-disease-injury-poison-long-term-recovery` with DPL-05-only implementation authority.

DPL-05 must build source-backed diagnosis, treatment, disease, poison, injury and recovery definitions/orchestration over Character-Actors, Condition, ICF, APW/D26, D17 and World-Hazard-Action owners. It consumes DPL-04 pharmaceutical/toxicology handoffs by reference and must preserve consent, privacy/visibility and setting/profile scope. It may not infer universal real-world medical or toxicology truth from game sources.

## Tranches

1. **DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk** — `completed_verified`
2. **DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts** — `completed_verified`
3. **DPL-03 — Research, Study, Discovery & Experimentation Loop** — `completed_verified`
4. **DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science** — `completed_verified`
5. **DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery** — `in_progress`
6. **DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction** — `planned`
7. **DPL-07 — Refining, Industrial Processing, Manufacturing & Supply Chains** — `planned`
8. **DPL-08 — Business, Enterprise, Staffing, Operations & Growth** — `planned`
9. **DPL-09 — Apprenticeship, Mentorship, Teaching & Workforce Development** — `planned`
10. **DPL-10 — Arts, Performance, Recreation, Festivals & Cultural Practice** — `planned`
11. **DPL-11 — Household, Family, Dependents, Legacy & Inheritance** — `planned`
12. **DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery** — `planned`
13. **DPL-13 — Cybernetics, Symbiotes, Cloning & Biotech Augmentation** — `planned`
14. **DPL-14 — Economy, Cozy, Base, Project Integration, Balance & Golden Life Proof** — `planned`

## DPL-05 governed scope

DPL-05 must:

1. consume DPL-01 disease/healing/poison/status-condition source/provenance classifications rather than general medical assumptions;
2. consume DPL-04 pharmaceutical/toxicology effect/delivery handoffs without rewriting scientific chemistry;
3. preserve Character-Actors, Condition and ICF as live identity/body/condition/biological owners rather than create a universal health ledger;
4. route treatment, recovery and rehabilitation time through APW/D26 rather than wall-clock progress;
5. keep medicines, tools, consumables and assistive equipment in D17 Asset ownership;
6. preserve World-Hazard-Action ownership for exposure, injury and environmental hazards;
7. make diagnosis, treatment, procedure, disease, poison, injury and recovery rules explicitly source/provenance and setting/profile scoped;
8. preserve consent and privacy/visibility for invasive procedures and sensitive health projections;
9. avoid inferred universal real-world disease, medical, pharmacokinetic or toxicology formulas;
10. implement no DPL-06+ mechanics, real-money commerce, provider activation or migration `0022` without a genuine durable schema delta.

## Invariants

- Character-Actors, Condition and ICF retain live health/body/biological truth.
- APW/D26 retains Project/task/campaign-time authority.
- D17 retains medicines, tools, consumables and assistive equipment as Assets/Items.
- World-Hazard-Action retains exposure, injury and environmental-hazard truth.
- DPL-04 remains scientific chemistry/pharmaceutical/toxicology definition authority and remains distinct from MSS magical alchemy.
- Disease, injury, poison and medical mechanics are setting/content-sensitive and are never silently promoted to universal real-world truth.
- Invasive treatment and irreversible body/identity changes cannot bypass consent or privacy/visibility owners.
- No real-money commerce is introduced.
- DPL-01 through DPL-04 have no further implementation authority.
- DPL-05 authority is branch- and tranche-bounded.
- DPL-06 and later DPL tranches remain unauthorized until selected and governed-started in strict order.
- Migration `0022` remains unreserved.
