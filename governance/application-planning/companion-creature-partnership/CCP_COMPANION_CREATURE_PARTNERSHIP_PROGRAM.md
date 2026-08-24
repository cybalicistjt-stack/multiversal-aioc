# CCP — Companion & Creature Partnership

**Program ID:** CCP  
**Status:** IN PROGRESS — CCP-01 COMPLETED_VERIFIED — CCP-02 SELECTED_NOT_STARTED  
**Completed through:** CCP-01  
**Current item:** CCP-02  
**Owner and final authority:** John Brandon Turner

## SEC repair satisfied

CCP-01 remains genuinely `completed_verified` at application merge `687d29d363714d85e074c23f75e6b09f4aa58958`. CCP-02 had been selected but not started when the owner identified the omitted **SEC-01..09 between MSS-11 and MSS-12** dependency.

That corrective dependency is now fully satisfied. SEC-01..09 is `completed_verified`, and `MSS-12-POST-SEC-REPROOF` is `completed_verified` as an evidence-only re-proof on application merge `872f8692d6ac2cf57584443c225bd4e5dc5758d0`. The re-proof required no rewrite of historical MSS-12 runtime/starter behavior.

The existing `CCP-02-attempt-001` checkpoint therefore resumes as `selected_not_started`. Its SEC-repair suspension is cleared, but **selection still grants no implementation authority**. A future owner **Continue** must governed-start CCP-02 from the then-current canonical AIOC/application heads before any implementation begins.

## Tranches

1. **CCP-01 — Source Inventory, Creature Catalog Crosswalk & Authority Map** — `completed_verified`
2. **CCP-02 — Companion Identity, Bond, Intelligence, Agency & Role Model** — `selected_not_started`
3. **CCP-03 — Taming, Recruitment, Rescue & Bond Formation** — `planned`
4. **CCP-04 — Training, Commands, Tasks, Tricks & Behavior** — `planned`
5. **CCP-05 — Care, Needs, Health, Recovery, Aging & Welfare** — `planned`
6. **CCP-06 — Mounts, Pack, Service, Work & Travel Integration** — `planned`
7. **CCP-07 — Combat Companions, Familiars & Supernatural Bond Seam** — `planned`
8. **CCP-08 — Breeding, Reproduction, Lineage & Inheritance** — `planned`
9. **CCP-09 — Habitats, Herds, Stables, Kennels & Facility Operations** — `planned`
10. **CCP-10 — Creature Ecology, Social Behavior, Lifecycle & World Integration** — `planned`
11. **CCP-11 — Content Packs, Search, Workbench & Golden Partnership Proof** — `planned`

## Preserved CCP-01 evidence

Application PR #277; exact validated head `01e759f3056c0bccdefdba42f55d57c18e2ef757`; repository-health run/job `32678696628` / `97291421243`; Validation Core run `32678696838`; Linux `97291421786`; Windows `97291421917`; deterministic comparison `97291837286`; receipt `a491909caa1d99786e210757cb32ed3c02d85d20e8a3f25b2e30e7fe77c77908`; squash merge `687d29d363714d85e074c23f75e6b09f4aa58958`.

## Completed repair evidence

SEC-09 application merge: `690a8aff7cb2f8600f61b811626e9705dadca48a`.

MSS-12 post-SEC re-proof: application PR #287; exact validated head `15ce9e7aa956b9e41331af28c0289e6cc1165649`; repository-health `32755086697` / `97520651812`; Validation Core `32755087271`; Linux `97520653561`; Windows `97520653950`; comparison `97521583367`; deterministic receipt `05031e96188c5f2caf7e4944d17a6c745b4281dafc7325fbead83647af041e29`; squash merge `872f8692d6ac2cf57584443c225bd4e5dc5758d0`.

## Invariants

All CCP-01 owner-routing, sapient-agency, non-property, no-duplicate-ledger, ICF, MIB-09, MIB-14, Combat, World, Economy, APW, MSS and Campaign/GM/visibility boundaries remain in force. Final SEC/MSS supernatural coverage is an input seam only: it does not authorize CCP to invent supernatural companion mechanics, automatic obedience, ownership of sapient beings, duplicate Character/creature/relationship ledgers, or unsupported biology/training/combat/economy rules.

Migration `0022` remains unreserved. No release/deployment/tester/provider/payment activation is authorized.
