# CAB-20 — Integrated Advancement Balance Model

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-20  
**State:** `completed_verified` analysis; standing-delegation decisions recorded separately  
**Owner/final authority:** John Brandon Turner

## 1. Purpose

Integrate CAB-01 through CAB-19 into one coherent Character advancement and balance model without creating a Character Level, CR analogue, universal power score, Ability-count cap, readied-Ability slot system, or replacement currency.

The model is governed by one foundational principle:

> **XP regulates how fast a Character acquires permanent power. Prerequisites regulate what development makes sense. Tiers regulate depth. Action economy, resources, stacking and dependencies regulate how much acquired power can matter at once.**

This model is game-rules/content governance only. It creates no application implementation or release authority.

## 2. Advancement currencies and ledgers

### Spendable Character advancement currency

- **XP** is the ordinary spendable permanent Character advancement currency.
- Ability Points/AP remain deprecated.
- Wealth, credits, ordinary transferable equipment, vehicles, drones, refits and upkeep use their owning economies rather than Character XP.
- XP-to-credits conversion is not part of normal creation or advancement.

### Non-spendable analysis values

- **Calibration Unit (CU): 1 CU = 250 XP.** CU exists only for design/QA comparison.
- **Reference Advancement Value (RAV)** records the non-spendable advancement value of free/granted permanent capability. RAV never creates XP debt and does not make a free grant a purchase.

## 3. Normal Character-creation baseline

Unless Campaign policy explicitly overrides the starting XP grant:

1. all six core Attributes begin at 10;
2. apply Species modifiers;
3. allocate one free 12-point Attribute pool;
4. establish base HP as `max(10, Constitution)` plus governed modifiers/grants;
5. base Species selection is free;
6. Homeworld Type, Cultural Influence and Early Life Profession core selections are free;
7. select five free eligible Ability Trees;
8. Tier-1 access in those five trees is free;
9. select five free eligible Tier-1 Abilities;
10. apply source-defined free Knowledges, proficiencies, Actions, Resources, spells or other creation grants;
11. receive **1,300 starting advancement XP** as the current normal-start default;
12. starting wealth/equipment is separately GM/Campaign-defined;
13. unspent XP carries into play.

Creation-only innate or special options retain their acquisition rules and do not become ordinary later purchases merely because XP exists.

## 4. Permanent advancement gate order

A permanent advancement proposal evaluates distinct gates:

1. authority;
2. source/rules-profile availability;
3. Character eligibility;
4. explicit prerequisites;
5. tier/depth access;
6. learning/acquisition readiness where required;
7. affordability in XP after explicit grants/waivers/substitutions;
8. conflicts/exclusions and CAB-08 interaction legality;
9. approval where Campaign policy requires it;
10. exactly-once commit with immutable before/after evidence.

No gate substitutes for another. In particular, enough XP never creates Species biology, faction standing, exposure history, a creature relationship, a Prestige qualification, a spellcasting archetype, or another missing eligibility fact.

## 5. Five-tier depth model

The common tier structure is:

- **Tier 1 — Foundation**
- **Tier 2 — Developed**
- **Tier 3 — Advanced**
- **Tier 4 — Expert**
- **Tier 5 — Apex**

Tier means relative developmental depth inside the owning progression. Tier does not establish universal damage, rarity, world impact, XP price, Character Level or encounter rating.

Ordinary purchasable progressions normally use one-time higher-tier XP access purchases in addition to individual Ability prices. Short progressions may intentionally cap early. Unexplained internal gaps are content/provenance warnings; CAB never invents filler.

Prestige progressions may legitimately declare Tier 3 as their first tier when explicit entry requirements establish the advanced starting scope. They do not owe Tier-1/Tier-2 back-costs.

## 6. XP calibration model

### Direct Ability effect bands

Working reference bands are approximately:

- 250 XP;
- 500 XP;
- 1,000 XP;
- 2,000 XP;
- 4,000 XP;
- 8,000+ XP with high-risk/manual review as necessary.

Direct price follows actual effect burden, not tier or source family. Review considers action economy, frequency, duration, breadth, targets, reliability, resources, scaling, stacking, summons/companions, immunities, challenge bypass, transformations and other meaningful mechanical burden.

### Ordinary progression access anchors

- extra ordinary progression opening: **1,000 XP**;
- Tier 2 access: **500 XP**;
- Tier 3 access: **1,250 XP**;
- Tier 4 access: **2,500 XP**;
- Tier 5 access: **5,000 XP**.

A Prestige progression beginning at Tier 3 normally pays the Tier-3 access event after satisfying entry requirements, without Tier-1/Tier-2 back-pay and without an automatically stacked ordinary extra-tree opening charge. Its first Ability remains separately granted or priced.

### Direct permanent HP

Cumulative creation-authorized direct HP investment:

- +5 HP: 500 XP;
- +10 HP: 1,250 XP total;
- +15 HP: 2,250 XP total;
- +20 HP: 3,750 XP total.

Further direct blocks require explicit later balance evidence.

## 7. Attributes, Skills, Knowledges and Proficiencies

### Attributes

Permanent post-creation Attribute increases use rising marginal prices by resulting score:

- 11–12: 250 XP per point;
- 13–14: 500 XP per point;
- 15–16: 1,000 XP per point;
- 17–18: 2,000 XP per point;
- 19–20: 4,000 XP per point;
- 21+: 8,000+ XP and explicit review.

### Skills

Skills retain 20 ranks. The marginal cost to acquire new rank `r` is:

`250 × r XP`

Thus cumulative rank-20 investment is 52,500 XP.

### Knowledge

Five Knowledge depth steps use marginal prices:

250 / 500 / 1,000 / 2,000 / 4,000 XP.

### Narrow proficiencies

The ordinary narrow progression is:

Unproficient → Proficient → Expertise → Mastery

with marginal advancement anchors 250 / 500 / 1,000 XP where the owning proficiency system does not provide a more specific governed rule.

## 8. Learning and Intelligence/Wisdom

Learning/development projects are conditional, not universal. They apply only where the owning rule or explicit GM/Campaign policy requires study, practice, instruction, exposure, acclimation, research, attunement or another development process.

The applicable learning Attribute is chosen by the learning mode. Intelligence and Wisdom do not automatically stack merely because both are high.

For a project governed by one relevant learning Attribute `A`, the current learning-time multiplier is:

`max(0.50, 1.00 - 0.05 × max(0, A - 10))`

This accelerates applicable learning/readiness by up to 50%. It does not increase XP awards or automatically reduce purchase prices.

## 9. Action economy and simultaneous power

Default combat throughput before explicit exceptions:

- 1 Action;
- 1 Bonus Action;
- movement on the Character's turn;
- 1 Reaction per round.

Owning multiple options for a channel does not create additional uses of that channel.

Extra Actions/Reactions and similar multipliers do not recursively generate or refresh their own multiplier class by default. Deliberate finite exceptions must explicitly define frequency, resource cost, limits and permitted follow-up actions.

Mechanically consequential Free/No-Action effects require a meaningful limiter. Companions, minions, familiars, mounts and summons are assessed by the meaningful independent action economy they add rather than merely by existing.

## 10. Stacking and interaction model

Source provenance is not a stacking type.

Default interaction rules include:

- same named effect: noncompounding; strongest magnitude controls; valid reapplication may refresh duration unless explicit stacking applies;
- ordinary numerical modifier group: strongest benefit plus strongest penalty while overlapping;
- Advantage/Disadvantage: binary and noncompounding; at least one of each cancels absent an explicit priority rule;
- same-type Resistance: noncompounding and never becomes Immunity merely through duplication;
- Immunity supersedes applicable Resistance;
- full replacement forms: one active at a time by default unless explicit nesting applies;
- same-group multipliers: strongest applies; no silent sequential multiplication;
- closed unbounded trigger/resource/grant cycles: unresolved/high-risk until explicitly bounded.

## 11. Acquisition and eligibility

Eligibility and acquisition are separate.

Governed acquisition modes include ordinary purchase, creation selection, source grant, source-qualified selection, training, exposure/acclimation, membership/induction, Prestige entry, archetype/magic access, bond/installation/attunement, creature relationship pathway, milestone/narrative acquisition and temporary state grants.

Important defaults:

- Species/Innate dataset membership or naming does not prove biology or automatic grant status;
- cross-Species or post-creation acquisition requires an explicit bridge when the source makes the option creation-only or biologically restricted;
- current environment does not automatically grant permanent environmental advancement;
- learned faction capability normally remains learned after membership loss, while affiliation-dependent grants and future acquisition may suspend;
- the structured 385-spell surface retains 0 direct per-spell learning XP and uses its owning archetype/capacity rules;
- a mount/pet/familiar/companion eligibility fact does not create ownership, obedience, placement or consent;
- source silence remains `acquisition_unresolved`.

## 12. Multidimensional balance model

No Character receives a universal balance score.

CAB evaluates a **16-dimension Character Balance Profile** covering at minimum:

1. direct offense;
2. burst throughput;
3. sustained throughput;
4. action-economy compression/multiplication;
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
16. reliability, persistence and dependency burden.

The profile also records paid XP, RAV, temporary/external grants, uncertainty and unresolved interactions. Equal XP is a comparison condition, not a claim of equal damage or equal role.

## 13. Corpus and tree audit constraints

The 4,816-record bounded Ability corpus is heterogeneous and not fully normalized.

Key audit facts carried forward:

- 3,917 records contain numeric Tier 1–5 values;
- 1,712 contain direct numeric XP values;
- only 418 meaningfully populate Action Economy;
- 1,256 `Record_ID` values collide across source files, affecting 2,512 rows;
- source-qualified identity (`source dataset + Record_ID`) is required until governed global stable IDs exist;
- 158 of 179 tiered progression groups contain all five tiers;
- one unexplained internal tier gap remains a structural repair item;
- advanced/special starts must be distinguished from missing earlier tiers;
- high-risk mechanics require manual review rather than automatic repricing.

## 14. Pacing and XP awards

Campaign progression profiles target long-run average XP per substantive session:

- Slow: 250 XP;
- **Standard: 500 XP**;
- Fast: 750 XP;
- Accelerated: 1,000 XP.

These are pacing targets rather than mandatory per-session payouts.

Award bands are accomplishment-based:

- 0 XP — no qualifying advancement accomplishment;
- 250 XP — minor meaningful accomplishment;
- 500 XP — standard substantive accomplishment;
- 750 XP — major accomplishment;
- 1,000 XP — exceptional/campaign-significant accomplishment.

Shared objective completion normally produces equal Character XP awards for participating Characters regardless of whether resolution was combat, negotiation, stealth, avoidance, rescue, disabling, research or another valid method. No automatic kill XP, trap/hazard XP, training-time XP or checklist farming is created.

## 15. Long-campaign control posture

Veteran breadth is legal. CAB-18 found no evidence requiring:

- a universal known-Ability cap;
- readied Ability slots;
- global diminishing-return purchase prices;
- blanket breadth taxes.

Long-campaign nonlinear risk is instead controlled through CAB-07/08 action economy, stacking, resource, dependency and recursion rules plus CAB-13 high-risk review.

## 16. Respec, correction and migration

When voluntary respec is permitted by Campaign policy, removed paid advancement refunds **100% of actual XP paid**, not current list price or RAV. Free grants refund 0 XP.

Correction/errata is nonpunitive. Valid historical Characters do not receive retroactive XP debt because a later CAB price increases. Proven CAB migration overpayment may be credited; historical underpayment is grandfathered unless the owner explicitly authorizes a different migration policy.

Dependency cascades must be explicit, and all respec/correction/migration changes retain append-only receipts and before/after evidence.

## 17. Integrated validation order

For a Character build or advancement review:

1. separate paid XP, RAV, external/temporary grants and wealth;
2. validate acquisition/eligibility and source authority;
3. validate prerequisites and tier/depth access;
4. validate any learning/acquisition readiness;
5. validate price using CAB calibration rather than legacy source price alone;
6. resolve action economy and interaction groups;
7. review high-risk mechanics and unresolved fields;
8. project the 16-dimension balance profile;
9. compare against equal-XP/RAV-aware benchmarks without scalar collapse;
10. preserve uncertainty and route content defects to CAB-22 repair classes.

## 18. CAB-20 conclusions

CAB-01 through CAB-19 form a coherent advancement architecture without requiring a universal level or CR substitute.

The remaining tasks are validation and closure, not a new architecture:

- CAB-21 tests the integrated anchors with reference Characters and Campaign horizons;
- CAB-22 turns the result into a final rules/content-repair map;
- CAB-23 audits completion and hands the CAB package forward.
