# CAB — Character Advancement & Balance

**Program ID:** CAB  
**Status:** `COMPLETED_VERIFIED`  
**Owner and final authority:** John Brandon Turner  
**Opened:** 2026-09-04  
**Closed:** 2026-09-05

## Purpose

CAB reconciled Multiversal Character advancement into a coherent XP-buy economy and established a durable multidimensional balance method for creation, progression, tiers, prerequisites, acquisition eligibility, Ability costs, simultaneous-power controls, stacking/synergy, rewards, veteran play, correction and migration.

CAB is a **game-rules/content-governance program**. Completion does not itself grant Multiversal-app implementation, migration, deployment or release authority.

## Final governing principle

> **XP regulates how fast a Character acquires permanent power. Prerequisites and acquisition rules regulate coherent development and eligibility. Tiers regulate depth. Action economy, resources, stacking and dependencies regulate how much acquired power can matter at once.**

## Final canonical reading order

1. `CAB-22_FINAL_ADVANCEMENT_RULES.md` — concise final Character advancement rules.
2. `CAB-20_INTEGRATED_ADVANCEMENT_BALANCE_MODEL.md` and `CAB-20_INTEGRATED_MODEL_v1.0.0.json` — integrated architecture.
3. `CAB-21_REFERENCE_CHARACTER_AND_CAMPAIGN_SIMULATION.md` and `CAB-21_SIMULATION_LEDGER_v1.0.0.json` — validation of starting XP, pacing and long-horizon opportunity costs.
4. `CAB-22_CONTENT_REPAIR_MAP_v1.0.0.json` — prioritized legacy Ability-content repair/repricing handoff.
5. `CAB-19_RESPEC_CORRECTION_AND_MIGRATION.md` — respec, correction and nonpunitive migration.
6. `CAB-23_COMPLETION_AUDIT.md`, `CAB-23_FINAL_HANDOFF.md` and `CAB-23_COMPLETION_INDEX_v1.0.0.json` — closure evidence and recovery authority.
7. Earlier tranche artifacts remain authoritative provenance for detailed decisions and source evidence.

## Final settled rules

### Advancement economy

- **Ability Points/AP are deprecated.**
- XP is the ordinary spendable permanent Character-advancement currency.
- Wealth, ordinary assets, vehicles, refits and upkeep use their owning economies rather than Character XP.
- There is no ordinary XP-to-credits conversion.
- **1 CU = 250 XP** is a non-spendable design/QA calibration unit.
- **Reference Advancement Value (RAV)** may record the non-spendable advancement value of free/granted permanent capability without creating XP debt.

### Normal Character creation

Unless Campaign policy explicitly selects another starting XP grant:

- six core Attributes begin at 10;
- Species modifiers apply;
- one free 12-point Attribute pool is allocated;
- base HP is `max(10, Constitution)` plus governed source modifiers/grants;
- base Species is free;
- Homeworld Type, Cultural Influence and Early Life Profession core selections are free;
- five eligible Ability Trees are free;
- Tier-1 access in those five trees is free;
- five eligible Tier-1 Abilities are free;
- source-defined free Knowledges, proficiencies, Actions, Resources, spells and other creation grants remain free;
- **normal starting advancement XP = 1,300**;
- starting wealth/equipment is separately GM/Campaign-defined;
- unspent XP carries into play.

CAB-21 simulation validates the 1,300-XP normal-start default.

### Advancement transaction

Permanent advancement evaluates separately:

1. authority;
2. source/rules-profile availability;
3. eligibility;
4. prerequisites;
5. tier/depth access;
6. learning/acquisition readiness where required;
7. XP affordability after explicit grants/waivers/substitutions;
8. conflicts/exclusions/interaction legality;
9. approval where Campaign policy requires it;
10. exactly-once commit with append-only before/after evidence.

Enough XP never substitutes for another gate.

### Five-tier model

The shared developmental-depth structure is:

- T1 **Foundation**;
- T2 **Developed**;
- T3 **Advanced**;
- T4 **Expert**;
- T5 **Apex**.

Tier is not Character Level, CR, universal damage, universal rarity, universal price or a scalar power score.

There is no universal prior-tier quantity ladder. Specific progressions may use explicit prior nodes, Skills, Knowledges, Attributes, milestones, proficiencies or tree-local mastery evidence where genuinely authored.

Short progressions may cap early. CAB never invents filler merely to populate all five tiers.

**Prestige classes/progressions may legitimately begin at Tier 3 with explicit entry requirements.** T1/T2 are not missing and no T1/T2 back-pay is created.

### XP calibration

Direct Ability prices follow **actual effect burden**, not tier or source family.

Working direct reference bands:

**250 / 500 / 1,000 / 2,000 / 4,000 / 8,000+ XP**.

Ordinary progression access anchors:

- extra ordinary progression opening: 1,000 XP;
- T2 access: 500 XP;
- T3 access: 1,250 XP;
- T4 access: 2,500 XP;
- T5 access: 5,000 XP.

Prestige T3 entry normally pays the T3 access event after requirements, with no T1/T2 back-pay and no automatically stacked ordinary extra-tree opening charge. The first Prestige Ability remains separately priced or granted.

Creation-authorized cumulative direct HP:

- +5 = 500 XP;
- +10 = 1,250 XP;
- +15 = 2,250 XP;
- +20 = 3,750 XP.

Do not extrapolate direct HP beyond +20 without new survivability evidence.

### Attributes, Skills, Knowledges and Proficiencies

Attribute marginal XP by resulting score:

- 11–12: 250 XP/point;
- 13–14: 500;
- 15–16: 1,000;
- 17–18: 2,000;
- 19–20: 4,000;
- 21+: 8,000+ plus explicit review.

Skills retain 20 ranks. Marginal cost for new rank `r` is:

`250 × r XP`

Knowledge uses five marginal steps:

250 / 500 / 1,000 / 2,000 / 4,000 XP.

Default narrow proficiency progression:

Unproficient → Proficient → Expertise → Mastery

with marginal anchors 250 / 500 / 1,000 XP where no more specific owning rule controls.

### Learning and Intelligence/Wisdom

Learning/development projects are conditional rather than universal. They apply when the owning rule or explicit GM/Campaign policy requires study, practice, instruction, exposure, acclimation, research, attunement or another development process.

GM/Campaign policy may explicitly add, waive, shorten, extend or otherwise modify learning requirements without silently changing unrelated prices or eligibility.

The learning mode selects the relevant Intelligence or Wisdom hook. Both do not automatically stack.

Learning-time multiplier:

`max(0.50, 1.00 - 0.05 × max(0, relevant_attribute - 10))`

This changes applicable learning/readiness time, not XP awards or blanket purchase price.

### Action economy and simultaneous power

Default combat throughput before explicit exceptions:

- 1 Action;
- 1 Bonus Action;
- movement on the Character's turn;
- 1 Reaction per round.

Owning multiple options for a channel does not create extra uses of that channel.

Extra Actions/Reactions and similar multipliers do not recursively generate or refresh their own multiplier class by default. Consequential Free/No-Action effects require a meaningful limiter. Companions/minions are evaluated by the meaningful independent action economy they add.

Full unrestricted extra Actions, additional Reactions and ally Action grants remain uncommon, explicitly bounded and manually reviewed.

### Stacking and synergy

Source provenance/tree/family is not a stacking type.

Defaults include:

- same named effect: noncompounding, strongest magnitude, valid duration refresh unless explicit stacking applies;
- ordinary numerical interaction group: strongest benefit plus strongest penalty;
- Advantage/Disadvantage: binary, noncompounding; at least one of each cancels absent explicit priority;
- same-type Resistance: noncompounding and does not become Immunity through duplication;
- applicable Immunity supersedes Resistance;
- one full replacement form active at a time unless explicit nesting applies;
- same-group multipliers use the strongest applicable multiplier unless deliberate compound multiplication defines order/limits;
- unbounded closed trigger/resource/grant cycles require manual review and are not presumed legal.

### Acquisition and eligibility

Eligibility, acquisition and affordability are separate concepts.

Governed acquisition modes include ordinary purchase, creation selection, source grant, source-qualified selection, training, exposure/acclimation, membership/induction, Prestige entry, archetype/magic access, bond/install/attunement, creature relationship pathway, milestone/narrative acquisition and temporary/state grants.

Key defaults:

- Species/Innate dataset membership or naming does not automatically prove biology or grant status;
- cross-Species or post-creation acquisition requires an explicit bridge when the owning rule makes the option restricted;
- current environmental presence does not automatically create permanent advancement;
- learned faction/profession capability normally remains learned after membership loss unless explicitly dependency-bound;
- the current 385 structured spells retain **0 direct per-spell learning XP** and use their owning archetype/capacity rules;
- dependency-granted capabilities may suspend when the dependency is absent without deleting history;
- mount/pet/familiar/companion eligibility does not create ownership, obedience, training, placement or consent;
- source silence remains `acquisition_unresolved`.

### Multidimensional Character balance

CAB does not assign one universal Character power number.

Use the 16-dimension Character Balance Profile covering:

1. direct offense;
2. burst throughput;
3. sustained throughput;
4. action economy;
5. defense;
6. recovery/regeneration;
7. control;
8. mobility/reach;
9. information/perception;
10. social influence;
11. utility/problem solving;
12. resource independence/efficiency;
13. companion/summon independent contribution;
14. transformation/state breadth;
15. challenge bypass/immunity coverage;
16. reliability/persistence/dependency burden.

Track paid XP, RAV, external/temporary grants and uncertainty separately. Equal XP does not imply equal damage or identical roles.

### Campaign pacing and awards

Long-run target XP per substantive session:

- Slow: 250;
- **Standard: 500**;
- Fast: 750;
- Accelerated: 1,000.

These are pacing targets, not automatic stipends. CAB-21 validates the 500-XP Standard target.

Accomplishment award bands:

- 0;
- 250 minor;
- 500 standard substantive;
- 750 major;
- 1,000 exceptional/campaign-significant.

Shared objectives normally award participating Characters equally regardless of whether meaningful resolution was combat, negotiation, stealth, avoidance, rescue, disabling, research or another valid approach.

No automatic kill XP, hazard/trap payout, training-time XP or checklist farming.

### Veteran play

Broad veteran Characters are legal. CAB rejects blanket known-Ability caps, readied Ability slots, breadth taxes and global diminishing-return Ability prices.

CAB-18/CAB-21 show substantial opportunity costs remain through very long Campaign horizons. Nonlinear balance risk is governed through action economy, stacking, resources, dependencies, acquisition and high-risk review instead.

### Respec, correction and migration

Voluntary respec availability is GM/Campaign-governed.

When permitted:

- refund 100% of XP actually paid for removed paid advancement;
- free grants/RAV refund 0 XP;
- use explicit dependency cascades;
- preserve append-only before/after receipts.

Correction/errata is nonpunitive. Later higher prices create no retroactive XP debt. Proven CAB migration overpayment may be credited; valid historical underpayment is grandfathered unless explicit later owner authority says otherwise.

## Corpus audit and repair boundary

CAB audited the bounded **4,816-record Ability corpus** but did not silently rewrite it.

Important audit facts include:

- 3,917 records carry numeric Tier 1–5 values;
- 1,712 carry direct numeric XP values;
- only 418 meaningfully populate Action Economy;
- `Record_ID` is not globally unique: 1,256 duplicated values affect 2,512 rows;
- use `source_dataset + Record_ID` until governed global stable IDs exist;
- 158 of 179 tiered progression groups contain all five tiers;
- one unexplained internal tier gap remains;
- high-risk mechanics require manual semantic review rather than automatic repricing;
- Rain of Arrows (`ABLREC-00483` in `Abilities_Core.csv`) has a known source-field boundary contamination requiring exact source recovery.

**CAB rule completion does not mean the legacy corpus is fully repaired.**

The governing repair entry point is `CAB-22_CONTENT_REPAIR_MAP_v1.0.0.json`, with priority order:

1. P0 source integrity and identity;
2. P1 mechanical determinism and high-risk semantics;
3. P2 economic/structural normalization;
4. P3 benchmark validation and presentation.

Content repair must preserve source provenance, never invent missing Abilities/prerequisites, avoid retroactive XP debt for valid historical Characters, and rerun multidimensional benchmarks after material repair batches.

## Completion ledger

All CAB tranches are `completed_verified`:

1. CAB-01 — Authority, Source Census & AP Retirement
2. CAB-02 — Current XP Economy Reconstruction
3. CAB-03 — Character-Creation Baseline
4. CAB-04 — Advancement Architecture
5. CAB-05 — Five-Tier Model
6. CAB-06 — XP Cost Calibration Framework
7. CAB-07 — Action Economy & Simultaneous Power
8. CAB-08 — Stacking, Synergy & Power Multiplication
9. CAB-09 — Acquisition & Eligibility
10. CAB-10 — Attributes, Skills & Proficiencies
11. CAB-11 — Ability Corpus Statistical Audit
12. CAB-12 — Ability-Tree Structural Audit
13. CAB-13 — High-Risk Ability Audit
14. CAB-14 — Equal-XP Benchmark Characters
15. CAB-15 — Multidimensional Character Balance
16. CAB-16 — Progression Pacing
17. CAB-17 — XP Award Framework
18. CAB-18 — Long-Campaign / High-XP Stress Test
19. CAB-19 — Respec, Correction & Migration
20. CAB-20 — Integrated Advancement Balance Model
21. CAB-21 — Reference Character & Campaign Simulation
22. CAB-22 — Final Rules & Content Repair Map
23. CAB-23 — Completion Audit & Handoff

## Owner-authority closure

CAB-02 through CAB-08 preserve explicit owner decisions. The owner then authorized evidence-grounded CAB recommendations through CAB-23 under a bounded standing delegation. No delegation guardrail was triggered.

The standing CAB recommendation delegation **ends with CAB-23** and does not extend to unrelated future work.

There are **no unresolved CAB owner-policy questions**.

## Program closure

CAB is `COMPLETED_VERIFIED`.

There is no active CAB tranche and no CAB successor. Outstanding legacy Ability-content repair is governed by the CAB-22 repair map and does not keep CAB open.

Future substantive changes to settled CAB rules require new explicit governance authority rather than silent mutation of this closed program.
