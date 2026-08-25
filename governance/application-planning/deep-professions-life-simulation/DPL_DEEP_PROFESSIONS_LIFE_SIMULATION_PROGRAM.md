# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-04; DPL-05 SELECTED_NOT_STARTED  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science  
**Current item:** DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery  
**Implementation branch:** none — next owner Continue required  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner  
**Planned:** 2026-08-20

## Purpose

DPL converts retained profession, science, industry, business, medicine, augmentation, arts and household material into deep gameplay loops over APW Projects, CEL, Economy, Crafting, ICF, Bases, Relationships and Character progression. It specifically prevents substantial source systems from disappearing inside generic Crafting or later content production.

## Current state

DPL-01 through DPL-04 are `completed_verified` with exact evidence preserved.

DPL-04 completed on application PR #301. Exact validated head `188d7ce85dcdacd560e0d763daf18ecd28bf1502` passed Repository Health `32815232747/97702049958`, Validation Core `32815232802`, Linux `97702050265`, Windows `97702050329` and deterministic comparison `97702612853`, with deterministic receipt `f92b1b51150f9447d4b13a0357f998824603e00dfdb666bb1b60826220045f05`. The first exact-head candidate passed without a CI repair cycle and squash-merged as `0ebd5c59f25369b41ab25c4840c346655fc8ef04`.

DPL-04 delivered source-backed scientific chemistry definitions rather than real-world procedures: 4 formula definitions, 4 toxicology delivery profiles and 4 laboratory environments; source-authored DC/time and failure-margin metadata; unresolved unsupported purity/concentration/contamination values; DPL-03/MIB-12/MIB-14/D17/Character/Condition/ICF/World/MSS owner handoffs; no owner mutation, transformation, effect application or health progression. Scientific chemistry remains distinct from MSS magical alchemy.

Strict DPL order now selects **DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery** as `selected_not_started`. Selection grants no implementation authority and no application branch exists. The next owner **Continue** is required to governed-start DPL-05 from then-current canonical AIOC/application main.

## Tranches

1. **DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk** — `completed_verified`
2. **DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts** — `completed_verified`
3. **DPL-03 — Research, Study, Discovery & Experimentation Loop** — `completed_verified`
4. **DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science** — `completed_verified`  
   Source-backed scientific chemistry, pharmaceutical/toxicology definition and laboratory-reference layer; no real-world synthesis procedures and no live health progression.
5. **DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery** — `selected_not_started`  
   Diagnosis, treatment, procedures, disease incubation/progression, exposure, poison dose/decay, lasting injury, rehabilitation, immunity/resistance and care Projects over existing Character/Condition/ICF systems. No implementation before the next owner Continue.
6. **DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction** — `planned`
7. **DPL-07 — Refining, Industrial Processing, Manufacturing & Supply Chains** — `planned`
8. **DPL-08 — Business, Enterprise, Staffing, Operations & Growth** — `planned`
9. **DPL-09 — Apprenticeship, Mentorship, Teaching & Workforce Development** — `planned`
10. **DPL-10 — Arts, Performance, Recreation, Festivals & Cultural Practice** — `planned`
11. **DPL-11 — Household, Family, Dependents, Legacy & Inheritance** — `planned`
12. **DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery** — `planned`
13. **DPL-13 — Cybernetics, Symbiotes, Cloning & Biotech Augmentation** — `planned`
14. **DPL-14 — Economy, Cozy, Base, Project Integration, Balance & Golden Life Proof** — `planned`

## DPL-05 selection boundary

If governed-started, DPL-05 must:

1. consume DPL-01 disease/healing/poison/status-condition source/provenance classifications rather than general medical assumptions;
2. consume DPL-04 pharmaceutical/toxicology effect/delivery handoffs without rewriting scientific chemistry;
3. preserve Character-Actors, Condition and ICF as live identity/body/condition/biological owners rather than create a universal health ledger;
4. route treatment/recovery/rehabilitation time through APW/D26 rather than wall-clock progress;
5. keep medicines, tools, consumables and assistive equipment in D17 Asset ownership;
6. preserve World-Hazard-Action ownership for exposure/injury/environmental hazards;
7. make diagnosis/treatment/procedure/disease/poison/injury/recovery rules explicitly source/provenance and setting/profile scoped;
8. preserve consent and privacy/visibility for invasive procedures and sensitive health projections;
9. avoid inferred universal real-world disease, medical, pharmacokinetic or toxicology formulas;
10. implement no DPL-06+ mechanics, real-money commerce, provider activation or migration `0022` without a genuine durable schema delta.

## Invariants

- APW, CEL, MIB-12/13/14, D17 Asset, ICF, Character, Progression-Abilities, Condition and Social-Relations retain owning truth.
- Science/chemistry remains distinct from magical alchemy except explicit crossover definitions.
- Research/discovery preserves provenance, unresolved/contradictory evidence and hidden-knowledge controls.
- Disease, injury, poison and medical mechanics remain setting/content-sensitive; no game-source rule is silently promoted to universal real-world truth.
- Invasive treatment and irreversible body/identity changes cannot bypass consent, player/GM/setting authority or privacy/visibility owners.
- Disease, psychological and household mechanics are never globally forced.
- Augmentation cannot silently change Character identity, consent or agency.
- No real-money commerce is introduced.
- DPL-01 through DPL-04 are completed_verified and have no further implementation authority.
- DPL-05 is selected_not_started and has no implementation authority until the next owner Continue.
- DPL-06 and later DPL tranches remain unauthorized until selected and governed-started in strict order.
- Migration `0022` remains unreserved.
