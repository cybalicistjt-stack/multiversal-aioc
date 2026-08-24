# CCP — Companion & Creature Partnership

**Program ID:** CCP  
**Status:** IN PROGRESS — CCP-01..09 COMPLETED_VERIFIED — CCP-10 SELECTED_NOT_STARTED  
**Completed through:** CCP-09  
**Current item:** CCP-10  
**Owner and final authority:** John Brandon Turner

## Current state

CCP-01 through CCP-09 are `completed_verified`, with exact evidence preserved.

**CCP-09 — Habitats, Herds, Stables, Kennels & Facility Operations** is `completed_verified`. Application PR #295 merged as `5b4d56433144d7b50d9c456127882362b31e981e` from exact validated head `9e724f5e9f2502f04736809cdac765a20fca2685`. Repository health, Linux, Windows and deterministic comparison all passed; deterministic receipt `54055ad5b0df2421e867980cbc79cd1a86c404c97e670ce161fc0c07397e7968`.

CCP-09 implemented a deterministic source/profile-aware reference and handoff layer covering habitat requirements, group/herd housing, existing facility references and husbandry/service operations. Five synthetic declarations cover all four seam kinds. Source-confirmed sapient housing or husbandry participation requires explicit voluntary consent. CCP-05/source biology retains welfare and individual needs; Item/facility owners retain facility identity, capacity and condition; Economy/logistics owners retain costs, inventory, staffing, upkeep, throughput, labor and productivity; MIB-09 retains relationship state; World/Campaign/GM owners retain world state. CCP-09 defines no universal habitat, stocking-density, herd-behavior, facility-capacity, upkeep, cost, labor or productivity formula.

The first CCP-09 application candidate passed invariant verification but failed client typecheck on both platforms because a helper default parameter inferred the synthetic source string as a literal type. The bounded repair widened only that helper parameter to `string`; no gameplay or authority semantics changed. The repaired exact head then passed all required gates.

Strict program order now selects **CCP-10 — Creature Ecology, Social Behavior, Lifecycle & World Integration** as `selected_not_started`. It has no implementation branch or authority until a future owner **Continue** governed-starts it.

## Tranches

1. **CCP-01 — Source Inventory, Creature Catalog Crosswalk & Authority Map** — `completed_verified`
2. **CCP-02 — Companion Identity, Bond, Intelligence, Agency & Role Model** — `completed_verified`
3. **CCP-03 — Taming, Recruitment, Rescue & Bond Formation** — `completed_verified`
4. **CCP-04 — Training, Commands, Tasks, Tricks & Behavior** — `completed_verified`
5. **CCP-05 — Care, Needs, Health, Recovery, Aging & Welfare** — `completed_verified`
6. **CCP-06 — Mounts, Pack, Service, Work & Travel Integration** — `completed_verified`
7. **CCP-07 — Combat Companions, Familiars & Supernatural Bond Seam** — `completed_verified`
8. **CCP-08 — Breeding, Reproduction, Lineage & Inheritance** — `completed_verified`
9. **CCP-09 — Habitats, Herds, Stables, Kennels & Facility Operations** — `completed_verified`
10. **CCP-10 — Creature Ecology, Social Behavior, Lifecycle & World Integration** — `selected_not_started`
11. **CCP-11 — Content Packs, Search, Workbench & Golden Partnership Proof** — `planned`

## CCP-09 exact evidence

Application PR #295; exact validated head `9e724f5e9f2502f04736809cdac765a20fca2685`; repository-health run/job `32775933979` / `97586877567`; Validation Core run `32775934033`; Linux `97586877622`; Windows `97586877300`; deterministic comparison `97587797235`; receipt `54055ad5b0df2421e867980cbc79cd1a86c404c97e670ce161fc0c07397e7968`; squash merge `5b4d56433144d7b50d9c456127882362b31e981e`.

Reference proof covered five declarations and all four CCP-09 seam kinds. `forced_sapient_housing_allowed=false`, `forced_sapient_labor_allowed=false`, `automatic_ownership_allowed=false`, `welfare_override_allowed=false`, `universal_facility_operations_formula_defined=false`, `herd_behavior_inference_allowed=false`, `owner_ledgers_owned_by_ccp09=false`, and no historical owner ledger was mutated.

## Preserved boundaries

CCP-01 owner-routing, canonical creature/Character identity, MIB-09 relationship identity/state, CCP-02 sapient agency/non-property/explicit-consent/no-automatic-obedience semantics, CCP-03 pathway boundaries, CCP-04 training/behavior boundaries, CCP-05 biology/health/welfare boundaries, CCP-06 capability/equipment/travel/economy boundaries, CCP-07 Combat/MSS handoffs, CCP-08 reproduction/inheritance boundaries and CCP-09 habitat/facility/economy/World handoffs remain in force.

CCP-10 may later define ecology, social behavior, lifecycle and World-integration **reference seams only**. It must not invent universal ecology, population-growth, carrying-capacity, migration, territory, predation, social-hierarchy, lifecycle or environmental-response formulas; fabricate species social/ecological behavior; automatically mutate relationships; or take over creature, relationship, ecology or World state. CCP-11 remains unauthorized until selected and governed-started in strict order.

Migration `0022` remains unreserved. No release/deployment/tester/provider/payment activation is authorized.
