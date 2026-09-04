# CAB-02 — Current XP Economy Reconstruction

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-02  
**State:** reconstruction candidate pending closeout  
**Owner/final authority:** John Brandon Turner  

## 1. Purpose

Reconstruct how XP is currently or historically used across Multiversal without deciding the final Character-creation budget, final prices, tier design, reward pacing, or balance calibration.

CAB-02 inherits CAB-01:

- Ability Points are deprecated and cannot be revived by reconstruction;
- XP is the working ordinary spendable Character-advancement currency;
- current Character architecture owns authoritative award/proposal/cost-ledger/decision/receipt semantics;
- PPIA-11 multidimensional balance boundaries remain intact;
- current rules, recovered source mechanics, historical rules, authored proposals, conflicts and unknowns remain distinct.

## 2. Reconstructed economy layers

The source base does **not** support one already-reconciled universal XP table. It supports several distinct XP uses that must be separated before numeric calibration.

### Layer A — authoritative Character progression accounting

Current Character architecture supports:

1. an authorized progression/advancement award;
2. a Character progression balance;
3. a Player advancement proposal;
4. a cost ledger;
5. authoritative validation of costs, prerequisites and limits;
6. approval where Campaign policy requires it;
7. exactly-once advancement commit;
8. before/after evidence and append-only advancement history.

**CAB-02 classification:** CURRENT ARCHITECTURE. The accounting path is current; the numeric earning and spending schedules are not settled by this architecture.

### Layer B — direct XP purchases of Character capabilities

The portable structured corpus exposes three recurring XP-bearing fields across ability families:

- `Ability_XP_Cost` — direct purchase of an Ability/capability;
- `Tier_Unlock_XP` — access/unlock expenditure in some trees;
- `Upgrade_Cost_XP` — purchase of an improvement to an existing Ability/capability.

Five major structured ability files contain 4,816 rows total. Numeric coverage is uneven and therefore cannot be treated as a complete current price book:

| Source | Rows | Numeric Ability XP | Numeric Tier Unlock XP | Numeric Upgrade XP |
|---|---:|---:|---:|---:|
| `Abilities_Core.csv` | 1,256 | 642 | 676 | 374 |
| `Species_Innate_Abilities.csv` | 2,203 | 318 | 0 | 15 |
| `Magic_Faction_Abilities.csv` | 118 | 65 | 82 | 7 |
| `Prestige_Env_Abilities.csv` | 1,018 | 478 | 396 | 6 |
| `Profession_Crafting_Abilities.csv` | 221 | 209 | 184 | 0 |

Observed direct Ability XP values range from very low-cost minor capabilities to tens of thousands of XP. Observed tier-unlock schedules also vary substantially. These are source/recovered values, not CAB-approved normalized prices.

**CAB-02 classification:** SOURCE-BACKED/RECOVERED SPENDING MECHANISMS; numeric values remain subject to later CAB calibration and provenance review.

### Layer C — XP-gated tree/tier access

Some source trees combine:

- an XP entry/unlock cost;
- prior-tier quantity or explicit node prerequisites;
- a separate XP price for the purchased Ability.

Profession/crafting records include explicit tree-entry language such as a 500 XP tree unlock. Other trees publish tier unlock schedules commonly including values such as 500 / 2,000 / 5,000 / 10,000 / 20,000 XP, while alternative ladders also exist.

Species/innate records are notably different: the structured species file contains direct Ability XP costs but no numeric `Tier_Unlock_XP` rows in the recovered portable corpus.

**CAB-02 classification:** RECOVERED ACCESS MECHANISMS, NOT YET UNIVERSAL. CAB-05 owns final tier semantics and CAB-09 owns acquisition eligibility.

### Layer D — magic XP economy

The structured `Magic_Spells.csv` contains 385 spells. The `Learning_XP_Cost` field states that the spell itself costs 0 XP and that XP purchases spell slots or ready/known capacity under the archetype rules.

Recovered magic-rule material also contains older/proposal-stage XP purchases for:

- caster level;
- spell-level access;
- spell slots;
- learned spells;
- prepared slots;
- known-spell capacity.

Those recovered magic pages explicitly present themselves as a framework/suggested XP-cost structure and coexist with AP-era mana calculations that CAB-01 has already deprecated.

**CAB-02 classification:** SPELL ITSELF = SOURCE-BACKED ZERO DIRECT LEARNING XP IN THE STRUCTURED CORPUS; CAPACITY/SLOT ADVANCEMENT = RECOVERED XP DESIGN FAMILY REQUIRING LATER RECONCILIATION. AP-derived mana math remains deprecated.

### Layer E — background, species, environmental and setting-linked XP options

Manual recovery catalogs repeatedly preserve direct XP options attached to backgrounds, species/culture packages, environmental adaptations and setting-specific capabilities, frequently in the 300–600 XP range with many higher exceptions. Examples include XP-priced proficiencies, rerolls, environmental advantages, contacts, rituals and special actions.

These records demonstrate a historical design intent that XP can deepen a background or setting-linked development after the initial package. They do **not** establish that every such option is freely purchasable by every Character merely because an XP price exists.

**CAB-02 classification:** RECOVERED DIRECT CHARACTER-PROGRESSION SPENDING. Purchase eligibility is unresolved and belongs to CAB-09.

### Layer F — XP awards and encounter rewards

Current Character architecture supports authoritative XP/progression awards but does not settle the amount schedule.

The structured `Hazards_Traps.csv` contains 1,901 non-unspecified `XP_or_Reward` values. The dominant recovered values are:

- 100 XP — 114 rows;
- 250 XP — 727 rows;
- 500 XP — 954 rows;
- 1,000 XP — 90 rows;
- 0 XP — 16 rows.

Source hazard examples associate 100 with moderate/T2 hazards and 250 with high/T3 hazards; 500 appears on severe/T4 examples. Some 1,000-XP records are original cross-genre expansions rather than source-PDF values.

Recovered civilian-vehicle challenge material also includes **Style Points: bonus XP for creative or skilled performance**.

**CAB-02 classification:** SOURCE/RECOVERED XP-AWARD SIGNALS, NOT A UNIVERSAL CURRENT REWARD TABLE. CAB-16 owns pacing and CAB-17 owns the XP award framework.

### Layer G — training and XP multipliers

Recovered spacecraft material includes an Expanded Crew Quarters effect that "allows onboard training, boosting XP gain by 10% during downtime."

This is materially different from paying XP for permanent advancement: it changes the rate at which permanent advancement currency enters the Character economy.

**CAB-02 classification:** RECOVERED CONTENT-SPECIFIC XP MULTIPLIER; unresolved and potentially destabilizing. It is not promoted to a general current rule by CAB-02.

### Layer H — XP used as asset acquisition/upkeep currency

Recovered spacecraft/drone material includes examples such as:

- 2,000 XP acquisition per drone;
- 10,000 XP for a six-drone swarm pack;
- 300 XP upkeep per swarm per downtime phase;
- 3,500 XP acquisition for another drone type;
- 400 XP upkeep per drone per downtime phase;
- XP-priced refits/upgrades.

This makes XP function as an equipment/asset operating currency rather than solely a permanent Character advancement currency.

**CAB-02 classification:** LEGACY/RECOVERED ECONOMY CONFLICT. CAB recommends that ordinary asset acquisition, refits and upkeep be owned by credits/resources/economy systems rather than consuming permanent Character advancement XP unless a narrowly exceptional rule explicitly establishes otherwise.

### Layer I — conversion, replacement and partial-cost rules

The CAB-01 source census preserves historical XP-to-credit conversion language. CAB-02's bounded source set also recovered Kola-Ha form-development language allowing an old Form to be converted into a new one at half XP cost under narrative/emotional evolution conditions.

No universal XP refund/respec percentage was found in the current Character architecture or the bounded CAB-02 source review. Current architecture supports governed correction/respec receipts, but economics remain rule-specific/unresolved.

**CAB-02 classification:** CONVERSION/REFUND ECONOMICS UNRESOLVED. CAB-03 owns creation-budget conversion questions; CAB-19 owns respec/correction/migration economics.

## 3. What XP is currently safe to say it does

CAB-02 can establish the following without inventing missing rules:

1. XP is the working ordinary spendable Character-advancement currency.
2. XP may be awarded to a Character through an authoritative advancement event.
3. XP is source-attested as a direct cost for many Abilities and later improvements.
4. XP is source-attested as an access/unlock cost in some—but not all—trees.
5. XP is source-attested for some magic capacity/slot progression while individual structured spells themselves state 0 XP direct learning cost.
6. XP is source-attested for many background/species/environment/setting-linked development options.
7. Source/recovery material contains encounter/hazard reward XP, bonus XP, XP-gain multipliers, asset acquisition/upkeep XP, conversion rules and other non-core uses; these do not automatically become current universal economy rules.
8. No CAB-approved universal XP reward schedule, tier-unlock schedule, refund schedule, creation budget, XP-to-credit exchange rate or asset-XP rule exists yet.

## 4. Conflict map

### Conflict C02-01 — advancement currency vs general-purpose currency

Some recovered sources spend XP on Character development; others spend it on equipment/drone acquisition and upkeep.

**Recommendation:** reserve ordinary XP for permanent Character advancement. Route ordinary asset/economic costs to their owning economies. Preserve rare XP-sacrifice mechanics only if they are intentionally exceptional and explicitly authored as such.

### Conflict C02-02 — direct Ability cost plus access tax plus prerequisite count

Many trees combine separate XP purchase, XP tier unlock and prior-tier purchase counts.

**Recommendation:** do not reconcile in CAB-02. CAB-04/05 should decide which gates have distinct jobs and remove redundant universal gating.

### Conflict C02-03 — spell price vs spellcasting capacity price

Structured spells state 0 direct learning XP while recovered magic frameworks buy slots/known/prepared capacity and sometimes also propose XP to learn spells.

**Recommendation:** preserve the structured zero-direct-spell-cost signal as the stronger current structured evidence, but defer final magic advancement economics to CAB-04/06 and magic owning-domain reconciliation.

### Conflict C02-04 — fixed awards vs accomplishment-based advancement

Hazards/traps publish XP values and some challenge material awards bonus XP for style, while current balance methodology rejects a single universal CR/power scalar.

**Recommendation:** preserve the values as source examples. CAB-17 should build an accomplishment/challenge award method rather than summing every source XP tag mechanically.

### Conflict C02-05 — XP multipliers

A recovered ship facility boosts XP gain by 10% during downtime.

**Recommendation:** do not promote multiplicative XP bonuses as a general rule. They can create compounding advancement inequality and farming incentives. Training should more naturally affect eligibility, time, practice, or a bounded award rather than globally multiplying earned XP.

### Conflict C02-06 — refund/conversion uncertainty

Current architecture supports respec/correction history but no universal economic refund rule is established.

**Recommendation:** leave refunds rule-specific until CAB-19. Do not infer a general 50% refund from a specific Kola-Ha Form-conversion rule.

## 5. Explicit non-decisions

CAB-02 does not decide:

- starting Character XP;
- free starting trees/abilities;
- creation-time XP-to-credit policy;
- final Ability/tier/upgrade prices;
- final tier unlock model;
- final spellcasting capacity prices;
- final XP awards per session/adventure/challenge;
- final respec/refund percentage;
- whether a specific legacy XP-priced asset is repriced in credits/resources;
- final training reward rules;
- final acquisition eligibility for species/environment/innate/background capabilities.

## 6. Handoff to CAB-03

CAB-03 must establish one internally consistent Character-creation baseline using this reconstruction. It must distinguish:

- starting advancement XP;
- free/granted starting mechanical selections;
- XP-bought creation selections;
- equipment/wealth budget;
- any allowed creation-only conversion between budgets;
- species/form/background/environment/innate access;
- what is a grant versus a purchase;
- what creation examples are historical rather than normative.

CAB-03 must not use AP and must not treat legacy asset-upkeep XP or XP multipliers as part of the starting Character budget.