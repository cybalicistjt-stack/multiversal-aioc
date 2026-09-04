# CAB-01 — Advancement & Balance Source Census

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-01  
**Classification:** governed source census  

## Purpose

Identify the source families CAB must consume without confusing current architecture, superseded mechanics, recovered legacy rules, authored proposals, or balance methodology.

## A. Current governing architecture

### Character creation and advancement

`governance/application-planning/internal-alpha/feature-packets/MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md`

Current implementation-ready Character architecture. Relevant CAB semantics include:

- Campaign/rules-profile/advancement-policy binding;
- progression balances and advancement ledger;
- authoritative advancement award/proposal/cost-ledger/decision/receipt;
- authoritative validation of costs, prerequisites and limits;
- append-only Character history;
- explicit correction/respec proposal and receipt;
- source/provenance retention;
- Character definitions separated from live Character-owned state.

**CAB classification:** CURRENT ARCHITECTURAL INPUT. Does not itself settle final numeric XP economy.

### Encounter and balance methodology

`governance/application-planning/parallel-preimplementation/PPIA-11_*`

Completed PPIA-11 Encounter & Balance Design Laboratory. Relevant CAB semantics include multidimensional capability/pressure analysis, action economy, resource depletion, environment, uncertainty, benchmark comparison and post-playtest calibration.

**CAB classification:** COMPLETED_VERIFIED GOVERNING HISTORICAL INPUT. Preserve its prohibition on a universal CR/power scalar and guaranteed-balance claims.

### Character biology/species/forms

`governance/application-planning/parallel-preimplementation/PPIA-05_*`

Defines Character Species/Form progression/correction handoffs and preserves biology/acquisition boundaries rather than treating temporary Effects, equipment or environments as permanent biology.

**CAB classification:** DOMAIN INPUT for later acquisition/eligibility analysis; does not independently price CAB advancement.

### Related owning domains

Current/provenance-preserving Character, progression, inventory, profession, relationship, environment, creature and world systems may constrain eligibility or consequences. CAB must consume their authority rather than creating duplicate ledgers.

**CAB classification:** BOUNDED DOMAIN INPUT when a later tranche reaches that concern.

## B. Recovered legacy advancement mechanics

Recovered source material contains multiple generations of progression rules, including:

- Ability Points awarded from XP thresholds;
- AP used for some access/unlock concepts;
- direct XP purchase prices for abilities and other Character improvements;
- five-tier ability structures;
- tier-entry costs and prior-tier quantity requirements in some sources;
- flat or low-cost species/environment ability families;
- starting Character budgets and examples that do not all reconcile numerically;
- historical XP-to-credit conversion language;
- later-access costs for additional trees/archetypes;
- respec/correction and training-related concepts.

**CAB classification:** LEGACY/HISTORICAL RULE EVIDENCE. AP-bearing mechanics are mechanically deprecated by owner decision. Non-AP design intent remains eligible for later evaluation.

## C. Structured ability/content corpus

The recovered structured corpus includes large ability datasets such as:

- `Abilities_Core.csv`;
- `Species_Innate_Abilities.csv`;
- `Magic_Faction_Abilities.csv`;
- `Prestige_Env_Abilities.csv`;
- `Profession_Crafting_Abilities.csv`;
- semantic-recovery/audit records containing source-derived ability descriptions and XP signals.

Prior governed audit work identified thousands of ability/content rows and substantial missing/unspecified cost information. Numeric XP pricing exists unevenly across the corpus, and tier labels do not imply a single universal XP price.

**CAB classification:** SOURCE-BACKED/RECOVERED CONTENT CORPUS. CAB-11 and later may statistically audit it; CAB-01 does not reprice it.

## D. Rune progression candidate

`governance/application-planning/parallel-preimplementation/PPIA-07_COST_STABILITY_PROGRESSION_CANDIDATE.md`

Useful design precedent: complexity, resource cost, structural stability and actual play power are separate axes. It explicitly refuses to invent a universal XP equation where source evidence does not support one.

**CAB classification:** AUTHORED DESIGN PRECEDENT, not a universal Character pricing rule.

## E. Learning/practice/achievement systems

`governance/application-planning/achievements-learning-practice/ALP_ACHIEVEMENTS_LEARNING_PRACTICE_PROGRAM.md`

ALP explicitly avoids inventing a second Character advancement ledger where training/learning has canonical Character effects.

**CAB classification:** FUTURE/ADJACENT DOMAIN INPUT. CAB remains the advancement-economy authority for the design program; ALP may later consume existing Character/progression ownership.

## F. Drive/Keep recovered design notes

Recovered design notes include the owner-identified concern that some abilities use tier trees/unlock costs/progressive XP while species/environment abilities may be flat/low cost, producing concern about veteran accumulation of inexpensive abilities. Notes also reference GM `awardXP` behavior and active play tooling.

**CAB classification:** LEGACY DESIGN INTENT / PROBLEM STATEMENT. Useful for explaining why CAB exists; not authoritative numeric rules.

## G. Explicitly retired source concept

### Ability Points (AP)

All AP-based currency, AP threshold, AP award and AP purchase mechanics are classified:

**DEPRECATED — DO NOT GOVERN CURRENT CHARACTER ADVANCEMENT.**

Retirement does not delete source history. Later CAB work may recover the design purpose behind an AP-era rule, but must express any accepted modern rule in the XP-based architecture unless the owner explicitly supersedes CAB-01.

## H. Unresolved source classes for CAB-02+

CAB-01 intentionally leaves the following as unresolved evidence questions rather than making assumptions:

- which direct XP schedules are current versus superseded;
- the complete set of XP-earning rules;
- the complete set of XP-spending rules;
- starting XP and free/granted creation selections;
- tier unlock XP costs;
- prior-tier count requirements;
- XP-to-credit scope;
- attribute/skill/proficiency prices;
- respec/refund economics;
- training/downtime interactions;
- species/environment/innate acquisition rules;
- whether specific high-cost/low-cost ladders represent deliberate magnitude differences or legacy inconsistency.

These are ordered inputs for CAB-02 through CAB-19 and must not be silently collapsed during CAB-01.
