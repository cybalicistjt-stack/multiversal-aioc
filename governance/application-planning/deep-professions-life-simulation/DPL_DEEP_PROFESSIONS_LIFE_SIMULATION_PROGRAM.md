# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-05; DPL-06 IN_PROGRESS  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery  
**Current item:** DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction  
**Implementation branch:** `integration/dpl-06-mining-prospecting-quarrying-drilling-resource-extraction`  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

DPL-01 through DPL-05 are `completed_verified` with exact evidence preserved. DPL-05 completed on application PR #302, exact validated head `43e03b0d38dd8a50727caf5fee283421ba1f1bec`, Repository Health `32817104041/97707507231`, Validation Core `32817104139`, Linux `97707505865`, Windows `97707506107`, comparison `97708026764`, deterministic receipt `49b987c43cb40b66e8ff4b940acaf4d332c41cdae32f60efce1adf4a4da0b629`, and squash merge `86588ac5d95486a0c662d8c841b73c64f2567a4d`. The first exact-head candidate passed with zero CI repair cycles.

Owner **Continue** on 2026-08-25 governed-started **DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction** from exact AIOC `4b0330531916b58045817302772cf4c7c6f367e0` and application `86588ac5d95486a0c662d8c841b73c64f2567a4d`. DPL-06 is `in_progress` on `integration/dpl-06-mining-prospecting-quarrying-drilling-resource-extraction` with DPL-06-only implementation authority.

DPL-06 must build source/profile-scoped survey, prospecting, deposit/vein, extraction, depletion, hazard, facility and material-output definitions/orchestration over APW/D26, World-Hazard-Action, D17 and MIB-14 owners. Retained mining yields/depletion remain game-source/profile rules rather than universal formulas. Raw extraction ends at a D17 material-output handoff; refining, smelting, milling, industrial processing, manufacturing and supply chains remain DPL-07.

## Tranches

1. DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk — `completed_verified`
2. DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts — `completed_verified`
3. DPL-03 — Research, Study, Discovery & Experimentation Loop — `completed_verified`
4. DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science — `completed_verified`
5. DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery — `completed_verified`
6. DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction — `in_progress`
7. DPL-07 — Refining, Industrial Processing, Manufacturing & Supply Chains — `planned`
8. DPL-08 — Business, Enterprise, Staffing, Operations & Growth — `planned`
9. DPL-09 — Apprenticeship, Mentorship, Teaching & Workforce Development — `planned`
10. DPL-10 — Arts, Performance, Recreation, Festivals & Cultural Practice — `planned`
11. DPL-11 — Household, Family, Dependents, Legacy & Inheritance — `planned`
12. DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery — `planned`
13. DPL-13 — Cybernetics, Symbiotes, Cloning & Biotech Augmentation — `planned`
14. DPL-14 — Economy, Cozy, Base, Project Integration, Balance & Golden Life Proof — `planned`

## DPL-06 governed scope

DPL-06 must:

1. consume retained `Mining Rules.PDF` and mining profession vocabulary through DPL-01 source/provenance classifications rather than generic mining assumptions;
2. preserve DPL-02/Progression profession, capability and mastery references rather than create a mining-specific progression ledger;
3. route survey, access, drilling, quarrying and extraction through APW/D26 Project/task/campaign-time references rather than wall-clock progress;
4. route geology/location truth, depletion, environmental consequences and extraction hazards through World-Hazard-Action references rather than silently mutate World state;
5. keep tools, equipment and extracted ore/mineral/material outputs in D17 Asset ownership;
6. use MIB-14 facility/platform capability references where source/profile definitions author mines, drills, quarries or extraction equipment, without inferring compatibility;
7. preserve LSS/ICF and existing material/loot boundaries so mining does not become salvage, foraging or creature-processing truth;
8. keep source-authored yield, deposit, grade, depletion and hazard values explicitly source/profile scoped and leave unsupported values unresolved;
9. stop raw extraction at a canonical material-output handoff; refining, smelting, milling, industrial processing, manufacturing and supply chains remain DPL-07;
10. implement no DPL-07+ mechanics, real-money commerce, provider activation or migration `0022` without a genuine durable schema delta.

## Invariants

- DPL-01 through DPL-05 have no further implementation authority.
- DPL-06 authority is tranche- and branch-bounded.
- APW/D26 retains Project/task/campaign-time truth.
- World-Hazard-Action retains geology/location/depletion/environment/hazard truth.
- D17 retains tools/equipment and extracted material/Asset truth.
- MIB-14 retains facility/platform compatibility truth.
- DPL-02/Progression retains profession/capability/mastery truth.
- LSS/ICF retain their existing salvage/foraging/biological-material boundaries.
- DPL-07 retains refining/processing/manufacturing successor mechanics.
- Source mining yield/depletion tables are not silently universalized.
- No real-money commerce is introduced.
- DPL-07 and later DPL tranches remain unauthorized.
- Migration `0022` remains unreserved.
