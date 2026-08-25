# DPL — Deep Professions & Life Simulation

**Program ID:** DPL  
**Status:** IN PROGRESS — completed_verified through DPL-11; DPL-12 IN_PROGRESS  
**Activation:** CCP-11 completed_verified  
**Completed through:** DPL-11 — Household, Family, Dependents, Legacy & Inheritance  
**Current item:** DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery  
**Implementation branch:** `integration/dpl-12-fear-stress-sanity-trauma-psychological-recovery`  
**Successor:** MAI-01  
**Owner and final authority:** John Brandon Turner

## Current state

DPL-01 through DPL-11 are `completed_verified` with exact evidence preserved. DPL-11 completed on application PR #308, exact validated head `ccd3e8d36e8024ec58f31e19bc502eaf523129f6`, deterministic receipt `fca994c4c61fe0b788878de74f10114b863488b739573704bff1a457cf05d2f6`, and squash merge `5e219f0625a439ec8708be8b0aaa011371eb06b4`.

Owner **Continue** on 2026-08-25 governed-started **DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery** from exact AIOC `f7b463120b233a9a9942ff5ea80f174e7aba6c77` and application `5e219f0625a439ec8708be8b0aaa011371eb06b4` after re-reading DPL-01 source disposition and directly inspecting the retained DPL-12 sources.

DPL-01 routes `sanity-horror` to DPL-12 over **DPL + Condition + Character-Actors** and explicitly keeps `status-condition-source` under existing **Condition** authority. DPL-01 also explicitly rejects globally mandatory Sanity Point mechanics. Therefore source formulas are retained only as source/profile-scoped references unless the owning domain executes them.

## Resolved DPL-12 source set

- `Sanity and Horror 11-13-24.PDF` — 6 pages, SHA-256 `a843d06c11f5e69a1482f42e184c05de9864b43bc7bad99bc4f35ca50203ff97`; authored Sanity Point, fear/horror, fear-effect, madness, trigger and recovery vocabulary.
- `Hazards_Traps.csv` — 1,901 rows, SHA-256 `391854834b50bdf175fe0bdd949280adbff67918889daae662fb40c40c418417`; ten retained `Psychological Hazards` rows `HTR-0067` through `HTR-0076` are DPL-12 references while **World-Hazard-Action** retains hazard adjudication.
- `Status Conditions 11-13-24.PDF` — 7 pages, SHA-256 `a070e11649a46dd8dd83da6cc67396573618280263683e89da546788ced30f32`; existing **Condition** authority, including `Frightened`, is referenced rather than copied.

The retained Sanity/Horror source explicitly says its madness terminology is not intended to mimic real mental illness and should be handled sensitively. DPL-12 preserves that boundary and does not infer real-world diagnosis, pathology or clinical claims from source terminology.

## Tranches

1. DPL-01 — Source Inventory, Profession Taxonomy & Authority Crosswalk — `completed_verified`
2. DPL-02 — Profession Activity Profiles, Mastery, Credentials & Service Contracts — `completed_verified`
3. DPL-03 — Research, Study, Discovery & Experimentation Loop — `completed_verified`
4. DPL-04 — Chemistry, Pharmaceuticals, Toxicology & Laboratory Science — `completed_verified`
5. DPL-05 — Medicine, Disease, Injury, Poison & Long-Term Recovery — `completed_verified`
6. DPL-06 — Mining, Prospecting, Quarrying, Drilling & Resource Extraction — `completed_verified`
7. DPL-07 — Refining, Industrial Processing, Manufacturing & Supply Chains — `completed_verified`
8. DPL-08 — Business, Enterprise, Staffing, Operations & Growth — `completed_verified`
9. DPL-09 — Apprenticeship, Mentorship, Teaching & Workforce Development — `completed_verified`
10. DPL-10 — Arts, Performance, Recreation, Festivals & Cultural Practice — `completed_verified`
11. DPL-11 — Household, Family, Dependents, Legacy & Inheritance — `completed_verified`
12. DPL-12 — Fear, Stress, Sanity, Trauma & Psychological Recovery — `in_progress`
13. DPL-13 — Cybernetics, Symbiotes, Cloning & Biotech Augmentation — `planned`
14. DPL-14 — Economy, Cozy, Base, Project Integration, Balance & Golden Life Proof — `planned`

## DPL-12 governed scope

DPL-12 must:

1. preserve exact retained-source provenance and keep authored Sanity/Fear/Horror/Madness/Trigger/Recovery rules profile-scoped rather than universal;
2. expose the ten retained psychological hazard records as read-only references while **World-Hazard-Action** retains trigger/save/DC/damage/environment execution;
3. reference **Condition** for `Frightened`, confusion/exhaustion-like effects and all live psychological condition state rather than creating a DPL condition ledger;
4. keep **Character-Actors** as identity, personality, consent and agency truth; source effects may not silently rewrite a Character;
5. compose support context through **Social-Relations**, bounded routines through **CEL/APM**, and durable recovery activities through **APW/D26** without duplicate ledgers or wall-clock progression;
6. treat therapy, narrative healing, restoration spells, special rituals/items and other recovery statements as source/profile metadata only; medical truth remains with DPL-05/medical owners, magical execution remains with MSS where applicable, and no real-world clinical efficacy is claimed;
7. represent absent universal stress/trauma/clinical semantics as unresolved source gaps rather than inventing formulas;
8. stop before DPL-13 augmentation mechanics and all later tranches;
9. introduce no real-money commerce and reserve no migration `0022` without demonstrated durable schema need.

## Invariants

- DPL-01 through DPL-11 have no further implementation authority.
- DPL-12 authority is tranche- and branch-bounded.
- Globally mandatory Sanity Points remain noncanonical.
- Character-Actors retains identity/personality/agency truth.
- Condition retains live condition state and effect execution.
- World-Hazard-Action retains psychological hazard adjudication.
- Social-Relations retains relationship/support truth.
- DPL-05/medical owners retain medical truth.
- CEL/APM retains bounded routines/human stops; APW/D26 retains Projects/tasks/campaign time.
- Source madness terminology remains supernatural/narrative strain and is not a real-world mental-illness model.
- DPL-13+ remain unauthorized.
- No real-money commerce is introduced.
- Migration `0022` remains unreserved.
