# CCP — Companion & Creature Partnership

**Program ID:** CCP  
**Status:** IN PROGRESS — CCP-01..07 COMPLETED_VERIFIED — CCP-08 SELECTED_NOT_STARTED  
**Completed through:** CCP-07  
**Current item:** CCP-08  
**Owner and final authority:** John Brandon Turner

## Current state

CCP-01 through CCP-06 remain `completed_verified`, with their exact evidence preserved.

**CCP-07 — Combat Companions, Familiars & Supernatural Bond Seam** is now `completed_verified`. Application PR #293 merged as `47468037ae6bb94155068afc8f319f8aa6006f4a` from exact validated head `22112a5ae4753fcd68ed387d5b69b540e0dc1b3e`. Repository health, Linux, Windows and deterministic comparison all passed; deterministic receipt `eb009ed61f4e306a08f08db2f6aca4ffc289c9068c105d0495a8a68f16cb048b`.

CCP-07 implemented a deterministic source/profile-aware combat/familiar/supernatural-bond reference and handoff layer covering combat participation, combat support, familiar references and supernatural-bond references. It preserves Combat/action/effect ownership of combat state, initiative/action economy, targeting, damage/effects and encounter resolution; MSS/source ownership of familiar, pact, summoning, spirit and supernatural-bond mechanics; MIB-09 relationship ownership; and explicit voluntary combat participation for source-confirmed sapient partners. It defines no universal combat-control, initiative, action-economy, damage or targeting formula and infers no familiar powers, telepathy, shared senses, resurrection, dismissal, range or bond effects.

The first implementation candidate failed only at client typecheck because one deterministic sort passed a `Ccp07Declaration` object to `localeCompare` instead of its `declarationId`. The bounded repair changed the comparison to `a.declarationId.localeCompare(b.declarationId)` without changing gameplay or authority semantics; the repaired exact head then passed all gates.

Strict program order now selects **CCP-08 — Breeding, Reproduction, Lineage & Inheritance** as `selected_not_started`. It has no implementation branch or implementation authority until a future owner **Continue** governed-starts it.

## Tranches

1. **CCP-01 — Source Inventory, Creature Catalog Crosswalk & Authority Map** — `completed_verified`
2. **CCP-02 — Companion Identity, Bond, Intelligence, Agency & Role Model** — `completed_verified`
3. **CCP-03 — Taming, Recruitment, Rescue & Bond Formation** — `completed_verified`
4. **CCP-04 — Training, Commands, Tasks, Tricks & Behavior** — `completed_verified`
5. **CCP-05 — Care, Needs, Health, Recovery, Aging & Welfare** — `completed_verified`
6. **CCP-06 — Mounts, Pack, Service, Work & Travel Integration** — `completed_verified`
7. **CCP-07 — Combat Companions, Familiars & Supernatural Bond Seam** — `completed_verified`
8. **CCP-08 — Breeding, Reproduction, Lineage & Inheritance** — `selected_not_started`
9. **CCP-09 — Habitats, Herds, Stables, Kennels & Facility Operations** — `planned`
10. **CCP-10 — Creature Ecology, Social Behavior, Lifecycle & World Integration** — `planned`
11. **CCP-11 — Content Packs, Search, Workbench & Golden Partnership Proof** — `planned`

## CCP-07 exact evidence

Application PR #293; exact validated head `22112a5ae4753fcd68ed387d5b69b540e0dc1b3e`; repository-health run/job `32770875287` / `97570686118`; Validation Core run `32770875551`; Linux `97570686334`; Windows `97570686540`; deterministic comparison `97571634099`; receipt `eb009ed61f4e306a08f08db2f6aca4ffc289c9068c105d0495a8a68f16cb048b`; squash merge `47468037ae6bb94155068afc8f319f8aa6006f4a`.

Reference proof covered four declarations and all four CCP-07 seam kinds. `forced_sapient_combat_allowed=false`, `sapient_combat_requires_explicit_voluntary_consent=true`, `automatic_obedience_allowed=false`, `universal_combat_formula_defined=false`, `familiar_power_inference_allowed=false`, `direct_combat_supernatural_or_relationship_mutation_allowed=false`, `owner_ledgers_owned_by_ccp07=false`, and no historical owner ledger was mutated.

## Preserved boundaries

CCP-01 owner-routing, canonical creature/Character identity, MIB-09 relationship identity/state, CCP-02 sapient agency/non-property/explicit-consent/no-automatic-obedience semantics, CCP-03 source-scoped pathway eligibility/rescue separation, CCP-04 source/profile trainability and behavior-owner boundaries, CCP-05 source/profile biology/health/recovery/aging/welfare boundaries, CCP-06 source/profile capability/equipment/travel/economy boundaries, CCP-07 Combat/MSS/MIB-09 handoff boundaries, ICF, MIB-14, Combat, World, Economy, APW, MSS and Campaign/GM/visibility boundaries remain in force.

CCP-08 may later define breeding, reproduction, lineage and inheritance reference seams, but it must not invent universal fertility, compatibility, gestation/incubation, offspring-count, mutation or inheritance formulas; coerce sapient reproductive participation; fabricate species biology or inherited supernatural powers; or take over canonical identity/biology/genetics/relationship/economy owners. CCP-09+ remain unauthorized until selected and governed-started in strict order.

Migration `0022` remains unreserved. No release/deployment/tester/provider/payment activation is authorized.
