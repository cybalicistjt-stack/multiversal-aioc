# CAB-06 — XP Cost Calibration Framework

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-06  
**State:** `completed_verified` analysis; owner calibration gates recorded separately  
**Owner/final authority:** John Brandon Turner

## 1. Purpose

Establish a governed method for converting permanent Character advancement burden into XP prices without reviving AP, treating tier as a universal price, or pretending that every source family already shares a coherent economy.

CAB-06 defines **how prices are calibrated** and provides working test anchors. It does not silently reprice the 4,816-record Ability corpus. CAB-07/08/10/11–15 and CAB-16/18 may later supply evidence that changes a working anchor before final integration.

## 2. Authority inherited

CAB-06 inherits:

- XP is the ordinary spendable advancement currency.
- AP is deprecated.
- XP does not establish eligibility or prerequisites.
- five tiers are developmental depth, not universal power or price;
- ordinary purchasable progressions normally pay one-time T2–T5 access XP plus individual Ability prices;
- special progression modes may replace the ordinary access method when explicitly authored;
- no universal prior-tier quantity ladder;
- Prestige progressions may legitimately begin at Tier 3 with explicit entry requirements and no phantom T1/T2 content;
- breadth is not inherently imbalance;
- action economy, resources, stacking, grants, and acquisition remain separately governed;
- the 1,300-XP normal-start value is a working default subject to later calibration.

## 3. Source-economy finding: the current numbers are not one calibrated system

The bounded Ability corpus contains:

- 4,816 total records;
- 1,712 records with a numeric direct Ability XP cost;
- 1,338 records with a numeric or source-expressed tier-unlock XP amount;
- 402 records with a numeric upgrade XP amount.

Direct Ability XP is extremely dispersed. Among the 1,712 numeric direct costs:

- 5th percentile: 150 XP;
- 10th percentile: 200 XP;
- 25th percentile: 387.5 XP;
- median: 700 XP;
- 75th percentile: 2,500 XP;
- 90th percentile: 5,000 XP;
- 95th percentile: 7,500 XP;
- 99th percentile: 20,000 XP;
- observed maximum: 50,000 XP.

Common complete-tree direct-price ladders include:

- 500 / 1,000 / 2,000 / 3,500 / 5,000;
- 175 / 500 / 1,250 / 2,750 / 6,250;
- 50 / 75 / 150 / 200 / 300;
- 3,000 / 7,500 / 15,000 / 25,000 / 40,000.

The most common recovered tier-unlock ladder is 500 / 2,000 / 5,000 / 10,000 / 20,000, but alternative ladders also occur and some progression families do not use separate unlock costs.

This spread is too wide to treat source prices as a unified balance standard.

## 4. Core pricing principle

CAB-06 separates **developmental depth cost** from **effect cost**.

- **Tier-access XP** prices how deeply the Character has committed to an ordinary progression.
- **Direct Ability XP** prices the actual permanent capability the Character receives.
- **Progression-opening XP** prices access to a new ordinary progression graph after creation.
- **Upgrade XP** prices the incremental capability added by an upgrade.
- **Grant/reference value** records the balance value of something received free without charging the Character.

This avoids double-counting tier as if every higher-tier node were automatically powerful merely because it is deeper.

A narrow Tier-5 technique can therefore have a modest direct Ability price while still requiring the Character to have paid or otherwise earned Tier-5 access. A very broad Tier-3 capability can legitimately have a larger direct Ability price than that narrow Tier-5 technique.

## 5. Calibration Unit (CU)

CAB recommends a **working Calibration Unit of 250 XP**.

CU is **not a Character currency, not AP, not player-facing money, and not stored as a spendable balance**. It is a design/QA normalization aid used to express relative anchors before final pacing is known.

Working conversion:

> **1 CU = 250 XP**

Why 250 XP is a useful working unit:

- it already appears repeatedly in recovered creation/progression material;
- it sits near the low-to-middle direct-Ability price region;
- it supports simple half-step or whole-step content pricing;
- it allows later pacing work to rescale the entire economy by changing the XP value of a CU without redesigning every ratio.

CAB-16 may recommend a different absolute XP scale. If so, the preferred migration is to scale the working unit and starting/award economy coherently rather than independently drifting thousands of prices.

## 6. Direct Ability reference bands

Direct Ability price is based on **actual effect burden**, not automatically on tier.

Working reference anchors:

| Band | Working reference | Current XP anchor | Typical use |
|---|---:|---:|---|
| G | 0 CU debit | 0 XP debit | Explicit grant/included feature; still receives reference value for balance audit. |
| A | 1 CU | 250 XP | Minor/narrow permanent capability or modest situational improvement. |
| B | 2 CU | 500 XP | Standard reliable single-purpose capability. |
| C | 4 CU | 1,000 XP | Significant capability with meaningful combat, utility, defense, mobility, or reliability value. |
| D | 8 CU | 2,000 XP | Major encounter/problem-shaping capability, broad defense/control, strong passive, or substantial multi-target effect. |
| E | 16 CU | 4,000 XP | Exceptional capability, major transformation component, broad immunity/negation, major persistent effect, or high-flexibility package. |
| F | 32 CU+ | 8,000 XP+ | Extreme/transformative capability requiring explicit manual review; may extend to 48, 64, or more CU when justified. |

The anchors are not tier floors or ceilings.

### 6.1 Burden dimensions

Pricing review must inspect at least:

1. effect magnitude/severity;
2. breadth/flexibility of situations solved;
3. reliability and failure/defense interaction;
4. action economy required to deliver the effect;
5. usage frequency;
6. duration/persistence;
7. number of targets/area/range;
8. resource cost and regeneration burden;
9. scaling with attributes, ranks, level-like state, forms, equipment, or other owned options;
10. stacking/synergy exposure;
11. summons/minions/extra bodies and action multiplication;
12. immunity/negation or automatic-success behavior;
13. information, movement, social, crafting, or other challenge-bypass reach;
14. transformation/form bundles and duplicate benefit channels.

Complexity by itself is not power and does not automatically increase XP price.

Narrative rarity, prerequisites, training time, eligibility, or special acquisition are separate gates and do not automatically discount a powerful effect.

### 6.2 Band movement

CAB does not adopt a fake-precision additive point formula. Reviewers assign an initial reference band from the core effect, then move the proposal only when the actual delivery conditions materially alter burden.

Typical upward pressure:

- passive/no-action delivery;
- free extra actions or reactions;
- broad area/multi-target reach;
- long/permanent duration;
- high reliability or defense bypass;
- strong scaling;
- broad applicability;
- summon/action multiplication;
- immunity/automatic negation;
- strong stacking or resource-loop potential.

Typical downward pressure:

- genuinely narrow context;
- meaningful action opportunity cost;
- hard limited-use frequency;
- meaningful scarce-resource expenditure;
- real self-risk or drawback;
- substantial failure/defense chance.

Multiple high-risk signals trigger manual review rather than unlimited mechanical band shifts.

## 7. Manual-review triggers

The following cannot be normalized safely by a simple band alone:

- additional actions/reactions or action duplication;
- persistent summons/minion economies;
- broad immunities or automatic negation;
- multiplicative numerical stacking;
- self-sustaining resource regeneration;
- broad permanent transformation bundles;
- effects that duplicate benefits across forms;
- remote/large-scale information or control;
- permanent creation of assets/capabilities;
- effects whose value grows strongly with other owned options;
- unlimited replication, chaining, or recursive grant behavior.

CAB-07/08/13 must specifically stress-test these classes.

## 8. Ordinary progression opening and tier-access anchors

CAB recommends the following **working** schedule for later tests:

| Access event | CU | Current XP anchor |
|---|---:|---:|
| Open one additional ordinary progression/tree after creation | 4 CU | 1,000 XP |
| Unlock Tier 2 | 2 CU | 500 XP |
| Unlock Tier 3 | 5 CU | 1,250 XP |
| Unlock Tier 4 | 10 CU | 2,500 XP |
| Unlock Tier 5 | 20 CU | 5,000 XP |

Tier 1 has no separate tier tax once the progression is legitimately opened.

The T2–T5 sequence is intentionally cheaper than the dominant recovered 2,000 / 5,000 / 10,000 / 20,000 ladder at the current 250-XP CU. If CAB-16 later doubles the absolute CU to 500 XP, the same relative schedule becomes 1,000 / 2,500 / 5,000 / 10,000 without changing the ratio architecture.

The schedule is therefore a **relative calibration proposal**, not a claim that final pacing has already been solved.

### 8.1 Why the extra-tree opening cost remains 4 CU

The recovered 1,000-XP extra-tree concept is retained as a working anchor because opening a new ordinary progression creates future option breadth but does not itself deliver every Ability in that tree.

CAB-14/18 must test whether 4 CU over-penalizes breadth in long campaigns. If it does, the opening cost may be lowered without changing direct Ability value.

## 9. Prestige progression cost treatment

Prestige classes/progressions legitimately begin at Tier 3 when their explicit entry requirements are satisfied.

CAB recommendation for the ordinary Prestige entry transaction:

- do **not** charge phantom T1 or T2 unlock costs;
- do **not** automatically stack an ordinary extra-tree opening charge on top of the Prestige starting-tier charge;
- the default XP access debit is the **Tier-3 access anchor** for the declared Prestige scope (5 CU / 1,250 working XP), after all explicit Prestige requirements are satisfied;
- the first Prestige Ability still has its own direct Ability price unless granted;
- an owning Prestige rule may explicitly define a different entry cost or grant mode.

This treats the advanced entry requirements as acquisition/prerequisite gates while preserving a visible XP depth commitment.

## 10. Special progression families

CAB-06 does not force every domain into ordinary tree economics.

Examples:

- Species/Innate may grant access or capabilities without a tier-access debit;
- environmental/adaptation content may require exposure/acquisition rather than ordinary shopping access;
- milestone/faction progressions may grant tiers or nodes;
- spell systems may price capacity/slots while individual structured spells remain zero direct learning XP under their owning rules;
- transformation/artifact/implant progressions may use special acquisition and direct reference value.

When a special progression uses no actual XP debit, its granted mechanical value should still be representable in the balance audit.

## 11. Grants and Reference Advancement Value

CAB recommends separating **actual XP debit** from **Reference Advancement Value (RAV)**.

RAV is expressed in XP for comparison but is not spendable currency.

Each permanent progression event should be able to record:

- `source_price_xp` — preserved source/recovered number if present;
- `reference_advancement_value_xp` — CAB-calibrated effect/access value;
- `base_xp_debit`;
- explicit waiver/grant/substitution;
- `final_xp_debit` actually removed from the Character;
- grant source/reason.

A Species-granted Ability may therefore have:

- final debit = 0 XP;
- reference value = 2,000 XP, for example.

That does **not** charge the Character 2,000 XP. It makes free grants visible to later Species/build/equal-XP balance analysis instead of pretending zero price means zero mechanical value.

## 12. Upgrades

An upgrade is priced from the **incremental burden it adds**, not automatically as a percentage of the base Ability and not automatically cheaper than the base Ability.

An upgrade that only improves a narrow parameter may cost 1–2 CU. An upgrade that adds a second mode, extra target, persistent effect, transformation, action-economy gain, or broad new capability may equal or exceed the original Ability's direct price.

The recovered 402 numeric upgrade prices remain source evidence, not a calibrated schedule.

## 13. Permanent HP purchases

CAB-03 retained direct permanent HP purchase at creation, but the recovered 300 / 750 / 1,250 / 2,000 cumulative ladder is not yet calibrated against survivability.

CAB recommends **increasing marginal cost** because permanent HP improves survivability across many encounters and can otherwise become an efficient universal sink.

Working test schedule by +5 HP block:

| Added block | Marginal CU | Marginal XP | Cumulative added HP | Cumulative XP |
|---|---:|---:|---:|---:|
| first +5 | 2 CU | 500 | +5 | 500 |
| second +5 | 3 CU | 750 | +10 | 1,250 |
| third +5 | 4 CU | 1,000 | +15 | 2,250 |
| fourth +5 | 6 CU | 1,500 | +20 | 3,750 |

Further direct HP blocks require later survivability evidence rather than assuming indefinite linear purchasing.

CAB-14/15 must compare these anchors against defensive Abilities, Constitution, healing, mitigation, and expected incoming damage before final integration.

## 14. Attributes, Skills, Knowledges, and proficiencies

Recovered creation anchors include 250 XP per Attribute +1, 250 XP per Skill rank, 500 XP per Knowledge tier, and 750 XP per proficiency. CAB-06 does **not** approve these values as final.

CAB-10 owns their valuation because:

- Attributes can affect many rolls and derived systems simultaneously;
- Skills/Knowledges vary in breadth and campaign usefulness;
- proficiencies may unlock whole progression families;
- Intelligence/Wisdom also interact with learning speed.

CAB-06 requires CAB-10 to price them against the same reference-value framework and prevent broad-stat dominance or double-counting.

## 15. Starting XP interaction

The current normal-start value remains 1,300 XP.

At a 250-XP working CU, this is 5.2 CU of discretionary creation advancement **on top of** the free creation foundation already approved in CAB-03.

CAB-06 does not change 1,300 yet. CAB-14, CAB-16, and CAB-21 must test whether the combined creation package and calibrated prices make 1,300 too low, too high, or appropriate.

If the normal-start amount changes, the preferred change is an explicit economy-wide pacing adjustment rather than silently modifying unrelated prices.

## 16. Price migration and provenance

CAB does not overwrite source prices silently.

Any later content repair should preserve:

- source/recovered cost;
- CAB calibrated reference value;
- adopted actual cost;
- reason for difference;
- calibration version;
- owner/GM/Campaign override where applicable;
- migration receipt for existing Characters if a live price changes.

Existing Characters are not retroactively mutated merely because an audit proposes a new price. CAB-19 owns refund/migration policy.

## 17. CAB-06 decisions established without owner gate

The following are structural outcomes of CAB-01 through CAB-05 plus the bounded audit:

1. source prices are not internally coherent enough to be adopted wholesale;
2. direct effect price and tier-access price must remain separate;
3. tier cannot independently determine direct Ability price;
4. complexity, acquisition rarity, and prerequisites do not automatically set price;
5. grants require zero-debit capability plus separately auditable mechanical value;
6. upgrades are priced by incremental effect burden;
7. attributes/Skills/Knowledges/proficiencies require CAB-10-specific calibration;
8. high-risk action/stacking/resource classes require later CAB stress tests;
9. source cost provenance must survive any normalization.

## 18. Owner gates

The working unit, direct burden-band policy, access schedule, HP anchors, and grant-reference-value policy materially affect later balance testing. They are presented in `CAB-06_OWNER_QUESTIONNAIRE.md` for explicit owner decision.

## 19. Forward routing

- action-economy multipliers and free-action risk -> CAB-07;
- stacking/synergy -> CAB-08;
- special acquisition and Prestige eligibility -> CAB-09;
- Attributes/Skills/Knowledges/proficiencies and learning formula -> CAB-10;
- corpus repricing audit -> CAB-11/12/13;
- equal-XP and survivability benchmarks -> CAB-14/15;
- CU/start-XP/award pacing scale -> CAB-16/17;
- veteran economy stress -> CAB-18;
- migration/refunds -> CAB-19.
