# CAB-06 — Owner Decisions

**Program:** CAB — Character Advancement & Balance  
**Source:** Owner responses to `CAB-06_OWNER_QUESTIONNAIRE.md`  
**Date:** 2026-09-04  
**Authority:** explicit owner decision

## CAB-Q06-01 — Working Calibration Unit

**Decision:** Option A.

- Use **1 CU = 250 XP** as a non-spendable design/QA normalization unit.
- CU is not player-facing, not Character currency, and is not an AP replacement.
- CAB-16 may later rescale the absolute XP value of one CU together with starting XP and award pacing while preserving accepted relative ratios unless later evidence requires a governed change.

## CAB-Q06-02 — Direct Ability pricing

**Decision:** Option A.

- Direct Ability price is calibrated from **actual effect burden**, not fixed tier price or source-family price table.
- Working reference bands are approximately **250 / 500 / 1,000 / 2,000 / 4,000 / 8,000+ XP**.
- Tier depth, eligibility, prerequisites, learning, acquisition, and source rarity remain distinct from direct effect price.
- Review factors include action economy, frequency, persistence, breadth, targets, reliability, resources, scaling, stacking exposure, summons/minions, defenses/immunities, recovery, challenge bypass, transformations, and other consequential mechanics.
- High-risk effects require manual review rather than a mechanical point sum.

## CAB-Q06-03 — Progression opening and tier-access anchors

**Decision:** Option A.

Working test anchors:

- extra ordinary progression/tree opening after creation — **1,000 XP (4 CU)**;
- Tier 2 access — **500 XP (2 CU)**;
- Tier 3 access — **1,250 XP (5 CU)**;
- Tier 4 access — **2,500 XP (10 CU)**;
- Tier 5 access — **5,000 XP (20 CU)**.

These are calibration anchors, not a final pacing claim. CAB-16 may rescale CU and absolute XP globally.

### Prestige entry

For a Prestige progression legitimately beginning at Tier 3:

- satisfy all explicit entry requirements;
- pay the Tier-3 access anchor once unless the owning Prestige rule defines another governed entry method;
- do **not** back-pay Tier 1 or Tier 2 access;
- do **not** automatically stack the ordinary extra-tree opening cost on top of the Tier-3 Prestige entry cost;
- individual Prestige Abilities retain their own direct XP costs unless granted/free.

## CAB-Q06-04 — Direct permanent HP purchases

**Decision:** Option A.

Working test schedule uses increasing marginal cost:

- first +5 HP: **500 XP**;
- second +5 HP: **+750 XP** — 1,250 cumulative for +10;
- third +5 HP: **+1,000 XP** — 2,250 cumulative for +15;
- fourth +5 HP: **+1,500 XP** — 3,750 cumulative for +20.

This decision does not automatically authorize unlimited further +5 HP blocks. CAB-14/15 must test survivability and determine any extension or cap.

## CAB-Q06-05 — Reference Advancement Value

**Decision:** Option A.

- Free/granted permanent progression may have **final XP debit = 0** while retaining a non-spendable `reference_advancement_value_xp` for balance analysis.
- Reference Advancement Value is not Character currency, debt, reimbursement, or a later charge.
- It exists so Species grants, innate features, Campaign grants, milestone grants, Prestige grants, and other free advancement remain visible in equal-XP and cross-build balance analysis.
- A zero XP debit does not imply zero mechanical value.

## CAB-07 handoff consequences

CAB-07 — Action Economy & Simultaneous Power may execute immediately and must inherit:

1. CU = 250 XP as the current non-spendable calibration unit;
2. direct Ability prices calibrated from actual effect burden rather than tier/source family;
3. working access anchors of extra tree 1,000 / T2 500 / T3 1,250 / T4 2,500 / T5 5,000 XP;
4. Prestige T3 entry with no T1/T2 back-pay and no automatic stacked ordinary tree-opening charge;
5. increasing-marginal HP working prices through +20 HP;
6. free/granted progression retains Reference Advancement Value for balance analysis;
7. CAB-07 must refine action-economy burden before later corpus-wide repricing.

## Supersession

These decisions resolve all five CAB-06 questionnaire items. Any earlier `candidate`, `recommended`, `awaiting_owner_answers`, or pending-owner language for these five decisions is superseded by this artifact.