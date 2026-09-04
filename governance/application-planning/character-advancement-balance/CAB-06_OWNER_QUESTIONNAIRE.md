# CAB-06 — Owner Questionnaire

**Program:** CAB — Character Advancement & Balance  
**Purpose:** resolve the five XP-calibration policy choices that materially affect CAB-07+ balance testing. Unanswered items remain unresolved and do not silently default.

## CAB-Q06-01 — Use a 250-XP working Calibration Unit?

**Decision impact:** HIGH  
**CAB recommendation:** **A**.

A. **Recommended:** use **1 CU = 250 XP** as a design/QA normalization unit. CU is not spendable, not player-facing, and not an AP replacement. CAB-16 may later rescale the absolute XP value of one CU together with starting XP and award pacing while preserving the relative ratios.

B. Use 1 CU = 500 XP immediately.

C. Do not use a calibration unit; author every XP amount independently.

D. Use another working unit you specify.

**Reasoning:** the current corpus is too fragmented to calibrate thousands of values independently. A non-spendable design unit gives CAB stable relative ratios while allowing later pacing work to change absolute XP scale coherently.

---

## CAB-Q06-02 — How should direct Ability prices be determined?

**Decision impact:** VERY HIGH  
**CAB recommendation:** **A**.

A. **Recommended:** direct Ability price follows **actual effect burden**, using tier-independent reference bands of approximately 250 / 500 / 1,000 / 2,000 / 4,000 / 8,000+ working XP. Tier depth, eligibility, prerequisites, training, and acquisition remain separate. Action economy, frequency, persistence, breadth, resources, targets, reliability, scaling, stacking, summons, immunity, challenge bypass, and transformations determine the burden review. High-risk effects require manual review rather than a mechanical point sum.

B. Give each tier a fixed direct Ability price and allow only rare exceptions.

C. Use source-family-specific price tables (martial, magic, psionic, Species, environment, etc.).

D. Keep existing source prices unless a record is obviously broken.

**Reasoning:** the corpus contains >100x price spread at comparable nominal depth and clear low/high outliers. Tier and source family cannot safely substitute for effect review.

---

## CAB-Q06-03 — Adopt the working progression-opening and tier-access anchors?

**Decision impact:** VERY HIGH  
**CAB recommendation:** **A**.

A. **Recommended working schedule:**

- extra ordinary progression/tree opening after creation: **4 CU = 1,000 XP**;
- Tier 2 access: **2 CU = 500 XP**;
- Tier 3 access: **5 CU = 1,250 XP**;
- Tier 4 access: **10 CU = 2,500 XP**;
- Tier 5 access: **20 CU = 5,000 XP**.

These are test anchors, not an assertion that final pacing is solved. CAB-16 may scale the XP value of CU globally.

For a Prestige progression that legitimately starts at Tier 3, the recommended default is: satisfy its explicit entry requirements, pay the Tier-3 access anchor once, **do not back-pay T1/T2**, and do not automatically stack the ordinary extra-tree opening charge on top of the Tier-3 entry charge. The first Prestige Ability still has its own direct XP price. An owning Prestige rule may explicitly define another entry cost/grant mode.

B. Use the later recovered generic higher-tier schedule: T2 1,000 / T3 2,500 / T4 5,000 / T5 10,000 XP, plus 1,000 XP tree opening.

C. Use the dominant source unlock schedule: T2 2,000 / T3 5,000 / T4 10,000 / T5 20,000 XP, plus tree opening where applicable.

D. Keep only the relative idea and defer all numeric access anchors to CAB-16.

E. Another schedule you specify.

**Reasoning:** Option A preserves a real specialization cost without recreating the very high legacy depth tax. Because CU can later be rescaled, CAB can test relative balance now and absolute advancement speed later.

---

## CAB-Q06-04 — How should direct permanent HP purchases scale?

**Decision impact:** HIGH  
**CAB recommendation:** **A**.

A. **Recommended working test schedule with increasing marginal cost:**

- first +5 HP: 500 XP;
- second +5 HP: +750 XP (1,250 cumulative for +10);
- third +5 HP: +1,000 XP (2,250 cumulative for +15);
- fourth +5 HP: +1,500 XP (3,750 cumulative for +20).

Further direct HP blocks are not automatically authorized by this schedule; CAB-14/15 must establish whether and how they continue.

B. Keep the recovered cumulative 300 / 750 / 1,250 / 2,000 XP ladder unchanged.

C. Use a flat cost per +5 HP block.

D. Keep HP purchasable but defer every numeric HP price to CAB-14/15.

E. Another schedule you specify.

**Reasoning:** permanent HP is broadly useful across encounters. Increasing marginal cost prevents it from becoming an indefinitely efficient universal advancement sink while preserving the owner-approved ability to buy HP.

---

## CAB-Q06-05 — Track a Reference Advancement Value for free/granted progression?

**Decision impact:** VERY HIGH  
**CAB recommendation:** **A**.

A. **Recommended:** yes. A free or granted Ability/tier can have **final XP debit = 0** while retaining a CAB-calibrated `reference_advancement_value_xp` for balance analysis. This value is not spendable, is not debt, and never charges the Character. It allows Species grants, Campaign grants, innate features, milestone rewards, and other free advancement to remain visible during equal-XP/species/build balance audits.

B. No. If something is free/granted, treat its balance value as 0 XP for all CAB comparisons.

C. Track reference value only for Species/Innate grants, not other grants.

D. Defer to CAB-14.

**Reasoning:** zero debit and zero mechanical value are not the same thing. Without a reference value, heavily granted Characters or Species can appear artificially equal to builds that paid XP for equivalent permanent capabilities.

## Already established and not being re-asked

- AP is deprecated.
- XP remains the only ordinary spendable advancement currency.
- CU/RAV are audit/design metadata only, not currencies.
- tier is developmental depth, not a universal direct price.
- ordinary progressions use one-time higher-tier access costs in principle.
- Prestige can legitimately begin at Tier 3 with explicit requirements.
- no T1/T2 Prestige backfill is required.
- Attributes/Skills/Knowledges/proficiencies receive deeper valuation in CAB-10.
- absolute progression pacing and XP awards remain CAB-16/17 work.

## Response format

You can answer compactly, for example:

`Q1 A, Q2 A, Q3 A, Q4 A, Q5 A`

You can qualify any answer. Unanswered items remain unresolved.
