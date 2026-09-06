# CAB-22 — Final Character Advancement Rules

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-22  
**State:** `completed_verified` rules synthesis; content repair remains separately queued  
**Owner/final authority:** John Brandon Turner

## 1. Authority and scope

These are the final CAB game-rule conclusions derived from CAB-01 through CAB-21. They govern Character advancement and balance semantics. They do **not** by themselves rewrite every legacy Ability row, authorize application implementation, or certify that the retained 4,816-record corpus is already normalized.

Where an individual source record conflicts with these CAB-wide defaults, preserve the source record as provenance and route the conflict through the CAB-22 repair map rather than silently mutating either side.

## 2. Advancement currency

- XP is the ordinary spendable permanent Character-advancement currency.
- Ability Points/AP are deprecated.
- CU and RAV are non-spendable analysis values.
- ordinary wealth/equipment/vehicles/upkeep use their owning economy rather than Character XP.
- no ordinary XP-to-credits conversion exists at creation or advancement.

## 3. Normal creation

Unless Campaign policy explicitly chooses a different starting XP grant:

- core Attributes begin at 10;
- apply Species modifiers;
- allocate one free 12-point Attribute pool;
- base HP is `max(10, Constitution)` plus governed source modifiers/grants;
- base Species is free;
- Homeworld Type, Cultural Influence and Early Life Profession core selections are free;
- five eligible Ability Trees are free;
- Tier-1 access is free in those five trees;
- five eligible Tier-1 Abilities are free;
- source-defined free Knowledges/proficiencies/Actions/Resources/spells/etc. remain free grants;
- normal starting advancement grant is **1,300 XP**;
- starting wealth/equipment is separately GM/Campaign-defined;
- unspent XP carries into play.

Creation-only options retain their own acquisition restrictions.

## 4. Advancement transaction

Every permanent advancement evaluates separately:

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

Enough XP does not substitute for any prior gate.

## 5. Five tiers

The common developmental-depth structure is:

- T1 Foundation;
- T2 Developed;
- T3 Advanced;
- T4 Expert;
- T5 Apex.

Tier is not Character Level, CR, universal damage, universal rarity, universal price or a scalar power score.

There is no universal 5/4/3/2 or other prior-tier quantity ladder. A specific progression may require explicit prior nodes, Skills, Knowledges, Attributes, milestones, proficiencies, or a tree-local mastery count where genuinely authored.

Short progressions may cap before T5. Tiers should normally be contiguous from declared start through declared cap unless the owning progression is explicitly sparse/special. Missing tiers are review states, never filler-generation instructions.

### Prestige

Prestige progressions may legitimately declare **T3 as their starting tier** when explicit entry requirements establish the advanced scope. T1/T2 are not missing. Requirements remain mandatory. Prestige entry normally pays the T3 access event only, with no T1/T2 back-pay and no automatically stacked ordinary extra-tree opening charge.

## 6. XP calibration

### Direct Ability prices

Use effect burden, not tier or source family, to calibrate direct Ability price.

Working reference bands:

**250 / 500 / 1,000 / 2,000 / 4,000 / 8,000+ XP**.

High-risk effects require manual review regardless of source price or tier.

### Ordinary progression access

- open an extra ordinary progression: 1,000 XP;
- T2 access: 500 XP;
- T3 access: 1,250 XP;
- T4 access: 2,500 XP;
- T5 access: 5,000 XP.

Opening/access cost and individual Ability price are separate.

### Direct permanent HP

The currently governed creation-authorized cumulative direct-HP purchases are:

- +5: 500 XP;
- +10: 1,250 XP;
- +15: 2,250 XP;
- +20: 3,750 XP.

Do not extrapolate beyond +20 without new survivability evidence.

## 7. Attributes, Skills, Knowledges and Proficiencies

### Attribute marginal cost by resulting score

- 11–12: 250 XP/point;
- 13–14: 500 XP/point;
- 15–16: 1,000 XP/point;
- 17–18: 2,000 XP/point;
- 19–20: 4,000 XP/point;
- 21+: 8,000+ XP/point plus explicit review.

### Skills

Skills retain 20 ranks.

Marginal cost of new rank `r`:

`250 × r XP`.

### Knowledge

Five steps use marginal costs:

250 / 500 / 1,000 / 2,000 / 4,000 XP.

### Narrow proficiency

Default states:

Unproficient → Proficient → Expertise → Mastery

with marginal anchors 250 / 500 / 1,000 XP where no more specific owning rule controls.

## 8. Learning and faster learning

Learning/development projects are required only when the owning rule or explicit GM/Campaign policy requires study, practice, instruction, exposure, acclimation, attunement, research or similar development.

GM/Campaign policy may explicitly add, waive, shorten, extend or otherwise modify a learning requirement. That override affects the learning/readiness gate only unless another explicit rule changes something else.

Use the learning mode's relevant Intelligence or Wisdom hook; both do not automatically stack.

Learning-time multiplier:

`max(0.50, 1.00 - 0.05 × max(0, relevant_attribute - 10))`

This does not increase XP awards and is not a blanket XP-price discount.

## 9. Action economy

Default combat envelope before explicit exceptions:

- 1 Action;
- 1 Bonus Action;
- movement on the Character's turn;
- 1 Reaction per round.

Owning multiple abilities for a channel does not create more uses of the channel.

Extra Actions/Reactions do not recursively generate/refresh their own multiplier class by default. Mechanically consequential Free/No-Action effects require meaningful limits. Full unrestricted extra Actions, additional Reactions and ally Action grants remain uncommon, explicitly bounded and manually reviewed.

Companions/minions are evaluated by the meaningful independent action economy they add, not merely by existing.

## 10. Stacking and synergy

Source provenance/tree/family is not a stacking type.

Defaults:

- same named effect: noncompounding, strongest magnitude, valid duration refresh unless explicit stacking applies;
- ordinary numerical interaction group: strongest benefit plus strongest penalty;
- Advantage/Disadvantage: binary, noncompounding; at least one of each cancels absent explicit priority;
- same-type Resistance: noncompounding and never becomes Immunity by duplication;
- applicable Immunity supersedes Resistance;
- one full replacement form active at a time unless explicit nesting applies;
- same-group multipliers use the strongest applicable multiplier unless deliberate compound multiplication defines ordering/limits;
- unbounded closed trigger/resource/grant cycles are not presumed legal and require manual review.

## 11. Acquisition and eligibility

Eligibility is permission to receive an option. Acquisition is the governed event/process that actually makes it owned, granted, learned, active, bonded, installed, inducted or otherwise available.

Acquisition modes may include:

- ordinary purchase;
- creation selection;
- source grant;
- source-qualified selection;
- training/instruction/practice;
- exposure/acclimation;
- membership/induction/standing;
- Prestige entry;
- archetype/magic access;
- bond/installation/attunement;
- creature relationship pathway;
- milestone/narrative acquisition;
- temporary/state grant.

Source silence is `acquisition_unresolved`, not inferred eligibility or ineligibility.

### Species/innate

Dataset membership, `Species Perk`, `Innate Ability`, biological-sounding naming or adjacency does not by itself prove automatic biology. Cross-Species or post-creation acquisition requires an explicit bridge where the source makes the option biologically or creation restricted.

### Environment

Current presence may satisfy use context or exposure opportunity but does not automatically create permanent advancement.

### Factions/professions

Learned permanent capability normally remains learned after membership loss unless the owning rule makes it dependent on ongoing affiliation/patronage/office/relic/link/facility/etc. Loss of membership can still close future acquisition or suspend source-dependent grants.

### Structured spells

The current 385 structured spells retain archetype/school/focus access and minimum caster tier. The spell itself has **0 direct learning XP**; XP purchases the owning capacity/slot/ready-known resource rather than a universal per-spell cost.

### External sources and creature relationships

Implants, symbiotes, relics, artifacts, forms and other dependencies may grant capability without converting the external object into Character-owned permanent XP advancement. Losing the dependency may suspend the grant without deleting history.

Mount/pet/familiar/companion eligibility does not create ownership, obedience, training, placement or consent. Person-level/sapient partners require voluntary consent under the owning relationship authority.

## 12. Balance evaluation

Do not assign one universal Character power number.

Use the CAB 16-dimension Character Balance Profile, including offense, burst, sustain, action economy, defense, recovery, control, mobility/reach, information/perception, social influence, utility, resource efficiency, companion contribution, transformation breadth, challenge-bypass/immunity coverage, and reliability/persistence/dependency burden.

Track separately:

- XP actually paid;
- RAV for free/granted permanent capability;
- external/temporary grants;
- source/runtime uncertainty.

Equal XP does not imply equal damage or identical roles.

## 13. Campaign pacing and awards

Long-run target profiles per substantive session:

- Slow: 250 XP;
- **Standard: 500 XP**;
- Fast: 750 XP;
- Accelerated: 1,000 XP.

These are Campaign pacing targets, not automatic session stipends.

Accomplishment award bands:

- 0 XP;
- 250 XP minor;
- 500 XP standard substantive;
- 750 XP major;
- 1,000 XP exceptional/campaign-significant.

Shared objectives normally award participating Characters equally regardless of whether the meaningful solution was combat, negotiation, stealth, avoidance, disabling, rescue, research or another valid approach.

No automatic kill XP, trap/hazard payout, training-time XP or checklist farming.

## 14. Veteran play

Broad veteran Characters are allowed. CAB does not introduce:

- known-Ability caps;
- readied Ability slots;
- blanket breadth taxes;
- global diminishing-return Ability pricing.

The primary nonlinear safeguards remain action economy, resource limits, stacking, dependencies, acquisition and high-risk manual review.

## 15. Respec, correction and migration

Voluntary respec availability is GM/Campaign-governed.

When permitted:

- refund 100% of XP actually paid for removed paid advancement;
- free grants/RAV refund 0 XP;
- dependent removals require an explicit cascade plan;
- preserve append-only before/after receipts.

Correction/errata is nonpunitive.

- later higher prices do not create retroactive XP debt;
- proven CAB migration overpayment may be credited;
- valid historical underpayment is grandfathered unless explicit owner authority says otherwise.

## 16. Content readiness boundary

The rules above are final CAB rules. The legacy corpus is not declared fully repaired merely because the rules are final.

A record remains content-unready where a consequential mechanic still has unresolved source boundaries, identity, acquisition, timing, resource, prerequisite, interaction, dependency or price semantics.

`CAB-22_CONTENT_REPAIR_MAP_v1.0.0.json` is the governing CAB handoff for those repairs.
