# CAB-02 — Current XP Economy Reconstruction Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-02  
**State:** `completed_verified`  
**Owner/final authority:** John Brandon Turner  

## Completed

CAB-02 reconstructed the bounded current/recovered XP economy without reviving Ability Points and without deciding CAB-03's Character-creation baseline.

Durable outputs:

- `CAB-02_XP_ECONOMY_RECONSTRUCTION.md` — human-readable reconstruction and conflict map;
- `CAB-02_XP_ECONOMY_LEDGER_v0.1.0.json` — machine-readable economy-family ledger;
- `CAB-02_OWNER_QUESTIONNAIRE.md` — owner decisions exposed by the reconstruction.

## Findings

### 1. There is a valid current XP accounting architecture but no single settled numeric economy

Current Character architecture already supports authoritative progression awards, Character balances, advancement proposals, cost ledgers, validation, decisions, exactly-once commits and append-only history. It does not establish final XP awards or prices.

### 2. Direct Character XP spending is strongly source-attested

Across the five major portable ability files there are 4,816 rows. The bounded census found:

- 1,712 rows with numeric `Ability_XP_Cost`;
- 1,338 rows with numeric `Tier_Unlock_XP`;
- 402 rows with numeric `Upgrade_Cost_XP`.

The mechanisms are therefore real source/recovered design families, but coverage and ladders are too inconsistent to declare the current numbers globally balanced.

### 3. Ability families do not share one unlock economy

Species/innate abilities have 318 direct numeric Ability XP costs in the portable corpus but zero numeric `Tier_Unlock_XP` rows. Other families commonly use tier unlock prices as well as direct ability prices and prerequisites. CAB-02 therefore rejects any assumption that a tier unlock tax is already universal.

### 4. Magic uses a distinct XP model

All 385 structured spells state 0 XP for the spell itself, with XP purchasing slots or ready-known capacity under archetype rules. Recovered older magic material additionally proposes XP for caster level, spell-level access, slots, known/prepared capacity and sometimes learning a spell. Those generations conflict and require later reconciliation; AP-derived mana calculations remain deprecated.

### 5. XP reward signals exist but are not a universal payout table

`Hazards_Traps.csv` contains 1,901 non-unspecified XP/reward values: 114 at 100 XP, 727 at 250 XP, 954 at 500 XP, 90 at 1,000 XP and 16 at 0. Some are source hazards/traps; some 1,000-XP records are original expansions. Recovered vehicle challenge material also awards bonus XP for creative/skilled performance.

CAB-02 preserves these as award signals/benchmarks and defers reward pacing to CAB-16/17.

### 6. Recovered sources sometimes use XP as a general-purpose economy

Examples include drone acquisition, refits and recurring upkeep paid in XP. This directly conflicts with CAB's working concept of XP as ordinary Character advancement currency and with the separate asset/economy ownership model.

### 7. Recovered sources contain percentage XP multipliers

One ship facility grants +10% XP gain during downtime. This changes the inflow rate of permanent advancement currency and can compound long-campaign inequality. It is preserved as recovered evidence but not promoted.

### 8. Refund/conversion economics are not settled

Current Character architecture supports correction/respec history but no universal refund percentage. A Kola-Ha-specific Form conversion at half XP cost is too narrow to generalize. CAB-01 also records historical XP-to-credit language, but CAB-02 does not establish a current exchange rule.

## Recommendations

1. **Reserve ordinary XP for permanent Character advancement.** Ordinary transferable assets, refits and upkeep should use credits/resources/economy systems. Permit XP only for explicitly Character-bound progression or intentionally exceptional advancement sacrifices.
2. **Do not use percentage XP-gain multipliers as an ordinary rule.** Training should affect eligibility, time/practice or a bounded award rather than multiply all future XP.
3. **Retain hazard/trap XP tags as source benchmarks, not automatic universal payouts.** CAB-17 should govern actual awards according to accomplishment and challenge resolution.
4. **Keep XP and creation wealth separate by default.** CAB-03 should only preserve a conversion if the owner explicitly selects one or a specific rules profile requires it.
5. **Do not normalize or reprice ability values yet.** CAB-04/05/06 must define architecture, tier semantics and calibration dimensions first.
6. **Do not infer a universal refund from specific partial-cost replacement rules.** CAB-19 owns respec/correction/migration economics.

## Established decisions

Inherited and preserved:

- AP remains deprecated;
- XP remains the ordinary working advancement currency;
- no universal Character Level/CR/power scalar;
- current advancement event/cost-ledger/history architecture remains intact;
- numeric XP values remain provenance-bearing evidence until their owning CAB tranche evaluates them.

CAB-02 itself establishes:

- the XP economy must be represented as distinct earn/spend/access/upgrade/convert/modify-rate families rather than one undifferentiated `XP` field;
- source XP tags do not automatically establish universal current rules;
- XP-priced asset acquisition/upkeep and percentage XP multipliers are explicit conflicts requiring owner/later-tranche disposition, not silent defaults.

## Owner questionnaire

`CAB-02_OWNER_QUESTIONNAIRE.md` contains four bounded questions:

1. ordinary assets paid in XP;
2. percentage XP multipliers;
3. treatment of existing hazard/trap XP values;
4. creation-time XP/wealth conversion.

The recommendations are C / A / B / A respectively. Unanswered questions remain unresolved.

## Unresolved items routed forward

- starting Character XP and creation grants -> CAB-03;
- creation XP/credits relationship -> CAB-03;
- advancement gate architecture -> CAB-04;
- tier access semantics -> CAB-05;
- price calibration -> CAB-06;
- special acquisition eligibility -> CAB-09;
- attributes/skills/proficiencies -> CAB-10;
- corpus repricing/outliers -> CAB-11..13;
- pacing -> CAB-16;
- XP awards -> CAB-17;
- long-campaign multipliers/accumulation -> CAB-18;
- refunds/respec/migration -> CAB-19.

## Completion statement

CAB-02 is complete when these artifacts are merged, the canonical CAB backlog marks CAB-02 `completed_verified`, and CAB-03 is selected_not_started. No application implementation authority is created.

## Exact successor

**CAB-03 — Character-Creation Baseline**.