# CAB-01 Completion Report

**Program:** CAB — Character Advancement & Balance  
**Work item:** CAB-01 — Authority, Source Census & AP Retirement  
**State:** `completed_verified`  
**Strict successor:** CAB-02 — Current XP Economy Reconstruction  

## Completed

CAB-01 established the durable CAB program and backlog, bounded all 23 tranches below the 25-minute tool cutoff, classified the principal advancement/balance source families, and formalized the owner's decision that Ability Points are deprecated.

Created:

- `CAB_CHARACTER_ADVANCEMENT_BALANCE_PROGRAM.md`
- `CAB_PROGRAM_BACKLOG.json`
- `CAB-01_AUTHORITY_AND_AP_RETIREMENT_CONTRACT.md`
- `CAB-01_SOURCE_CENSUS.md`
- `CAB-01_COMPLETION_REPORT.md`

## Findings

1. The current Character architecture does not require Ability Points. It already represents progression balances generically and governs advancement through award → proposal → validation/cost ledger → decision where required → exactly-once commit → history/receipt.
2. AP-bearing source material belongs to older/recovered advancement generations. It remains useful for provenance and for recovering non-AP intent, but CAB now classifies AP currency/threshold/purchase mechanics as deprecated.
3. Direct XP pricing, tier structures, prerequisites, species/environment ability families, creation budgets, training and respec concepts survive across recovered sources independently of AP and therefore require separate reconstruction rather than being discarded with AP.
4. PPIA-11 already supplies the correct balance philosophy for CAB: multidimensional capability and pressure analysis, explicit uncertainty, action/resource/environment sensitivity, benchmark comparison and post-playtest calibration; no universal CR/power scalar is authorized.
5. PPIA-07 supplies a useful precedent that structural complexity, resource cost and actual play power are separate axes; CAB must likewise avoid equating tier, price and power.
6. The source census confirms that numerical XP economy questions are materially unresolved and belong to CAB-02 onward. CAB-01 deliberately did not select among conflicting starting budgets, tier costs, XP ladders or award schemes.

## Owner decision made durable

**Ability Points (AP) are deprecated.**

AP no longer governs:

- character creation budgets;
- advancement purchases;
- ability/tree/tier access;
- attributes, skills or proficiencies;
- species/environment/innate advancement;
- XP thresholds or award schedules;
- balance calculations.

Legacy AP references remain historical source evidence only. Any later restoration of AP would require a new explicit owner decision superseding CAB-01.

## Recommendations

### Recommended

- Treat XP as the single ordinary spendable advancement currency while CAB reconstructs the actual economy.
- Preserve the current Character transaction/history architecture unchanged unless a later CAB tranche identifies a specific conflict.
- Preserve five tiers provisionally, but do not use them as universal price or power units.
- Let CAB-02 reconstruct all XP earning/spending/conversion uses before CAB-03 chooses a character-creation baseline.
- Do not rewrite or delete AP-bearing source records; classify them as mechanically deprecated so provenance survives.

### Not recommended

- Translating every historical AP value into XP with a fixed conversion ratio. The sources do not support a reliable universal AP→XP conversion and doing so would silently preserve a deprecated economy.
- Using old AP threshold tables as advancement pacing evidence without re-evaluating the XP economy.
- Repricing the ability corpus before CAB-06 establishes the cost-calibration framework.

## Questionnaire

No owner questionnaire is required at this boundary. CAB-02 is an evidence-reconstruction tranche and can proceed without a new design decision. Owner questions should be deferred until the XP economy has been reconstructed and conflicts can be presented with concrete consequences and recommendations.

## Verification

The CAB branch was directly re-read after creation. The program and backlog agree on the 23-tranche sequence and execution envelope; the AP-retirement contract preserves XP as the working ordinary currency while explicitly deferring numeric XP decisions; the source census separates current architecture, completed balance methodology, legacy rules, structured content, design precedent and unresolved evidence.

Repository code search also confirms that AP/"Ability Points" references occur in historical/recovered/design material rather than being required by the current Character advancement transaction contract. No current authority inspected requires AP to remain active.

## Terminal state

**CAB-01 is complete.**

`CAB_PROGRAM_BACKLOG.json` now selects **CAB-02 — Current XP Economy Reconstruction** as `selected_not_started`.

CAB-02 must reconstruct every current/recovered XP earning, spending, grant, refund, conversion and prerequisite use; classify conflicts and unknowns; preserve AP retirement; and avoid deciding the Character-creation baseline owned by CAB-03.
