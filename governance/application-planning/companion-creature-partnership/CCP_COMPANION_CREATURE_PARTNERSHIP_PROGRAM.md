# CCP — Companion & Creature Partnership

**Program ID:** CCP  
**Status:** IN PROGRESS — CCP-01..03 COMPLETED_VERIFIED — CCP-04 SELECTED_NOT_STARTED  
**Completed through:** CCP-03  
**Current item:** CCP-04  
**Owner and final authority:** John Brandon Turner

## Current state

CCP-01 and CCP-02 remain `completed_verified`, with their exact evidence preserved.

**CCP-03 — Taming, Recruitment, Rescue & Bond Formation** is now `completed_verified`. Application PR #289 merged as `84f8e9df1382bcf05af621dec84bbddeb8ab5012` from exact validated head `acae6952d95c21d1b4c75c005a2961d27564d976`. Repository health, Linux, Windows and deterministic comparison all passed; deterministic receipt `20f14628329c0bfa0f59d9d48336d2bb2fc474e68d2c9beb114363ed386cfd7d`.

CCP-03 implemented a deterministic source- and agency-aware pathway/proposal layer covering four distinct pathways: rescue, recruitment, taming and authored bond formation. It preserves CCP-02 creature/profile identity and association semantics, keeps MIB-09 as relationship identity/numeric-state authority, forbids taming source-confirmed sapient beings, requires explicit voluntary consent for accepted sapient relationship formation, and makes rescue explicitly nonbonding. It defines no universal eligibility or success formula, creates no ownership or automatic obedience, and implements no CCP-04+ mechanics.

Strict program order now selects **CCP-04 — Training, Commands, Tasks, Tricks & Behavior** as `selected_not_started`. It has no implementation branch or implementation authority until a future owner **Continue** governed-starts it.

## Tranches

1. **CCP-01 — Source Inventory, Creature Catalog Crosswalk & Authority Map** — `completed_verified`
2. **CCP-02 — Companion Identity, Bond, Intelligence, Agency & Role Model** — `completed_verified`
3. **CCP-03 — Taming, Recruitment, Rescue & Bond Formation** — `completed_verified`
4. **CCP-04 — Training, Commands, Tasks, Tricks & Behavior** — `selected_not_started`
5. **CCP-05 — Care, Needs, Health, Recovery, Aging & Welfare** — `planned`
6. **CCP-06 — Mounts, Pack, Service, Work & Travel Integration** — `planned`
7. **CCP-07 — Combat Companions, Familiars & Supernatural Bond Seam** — `planned`
8. **CCP-08 — Breeding, Reproduction, Lineage & Inheritance** — `planned`
9. **CCP-09 — Habitats, Herds, Stables, Kennels & Facility Operations** — `planned`
10. **CCP-10 — Creature Ecology, Social Behavior, Lifecycle & World Integration** — `planned`
11. **CCP-11 — Content Packs, Search, Workbench & Golden Partnership Proof** — `planned`

## CCP-03 exact evidence

Application PR #289; exact validated head `acae6952d95c21d1b4c75c005a2961d27564d976`; repository-health run/job `32760384084` / `97537562232`; Validation Core run `32760385069`; Linux `97537564782`; Windows `97537564507`; deterministic comparison `97538521618`; receipt `20f14628329c0bfa0f59d9d48336d2bb2fc474e68d2c9beb114363ed386cfd7d`; squash merge `84f8e9df1382bcf05af621dec84bbddeb8ab5012`.

Reference proof covered four pathway proposals and all four pathway kinds. `rescue_creates_bond=false`, `sapient_taming_allowed=false`, `automatic_obedience_allowed=false`, and no historical owner ledger was mutated.

## Preserved boundaries

CCP-01 owner-routing, canonical creature/Character identity, MIB-09 relationship identity/state, CCP-02 sapient agency/non-property/explicit-consent/no-automatic-obedience semantics, CCP-03 source-scoped pathway eligibility and rescue/nonbond separation, ICF, MIB-14, Combat, World, Economy, APW, MSS and Campaign/GM/visibility boundaries remain in force.

CCP-04 may later define training, commands, tasks, tricks and learned-behavior semantics, but it must not assume universal trainability, automatic obedience, or a universal difficulty/duration/reliability/success formula. CCP-05+ remain unauthorized until selected and governed-started in strict order.

Migration `0022` remains unreserved. No release/deployment/tester/provider/payment activation is authorized.
