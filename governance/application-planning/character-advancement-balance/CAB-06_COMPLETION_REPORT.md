# CAB-06 — XP Cost Calibration Framework Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-06  
**State:** `completed_verified` analysis; owner calibration answers pending  
**Owner/final authority:** John Brandon Turner

## Completed

CAB-06 established a governed XP calibration method that separates developmental-depth cost from actual effect cost and preserves source prices as provenance rather than silently adopting them as one coherent economy.

Durable outputs:

- `CAB-06_XP_COST_CALIBRATION_FRAMEWORK.md`;
- `CAB-06_SOURCE_COST_AUDIT.md`;
- `CAB-06_COST_CALIBRATION_MODEL_v0.1.0.json`;
- `CAB-06_OWNER_QUESTIONNAIRE.md`.

## Findings

### 1. The source economy is fragmented

The 4,816-record bounded corpus contains 1,712 numeric direct Ability prices, 1,338 tier-unlock amounts, and 402 numeric upgrade costs. Direct prices range from tens of XP to 50,000 XP, with multiple incompatible full-tier ladders.

### 2. Tier and direct price must be separate

Tier is developmental depth. One-time tier access can price specialization/depth while the direct Ability price reflects what the Ability actually does. This prevents double-counting tier as raw power and permits legitimate cross-tier price overlap.

### 3. A relative calibration unit is useful before pacing is final

CAB recommends a non-spendable working `CU` of 250 XP for design/QA. CAB-16 can later scale the absolute XP value of a CU with starting XP and award pacing while preserving relative ratios.

### 4. Direct Ability pricing needs burden bands, not fixed tier prices

Working anchors are 250 / 500 / 1,000 / 2,000 / 4,000 / 8,000+ XP, selected from actual effect burden. Action economy, reliability, frequency, persistence, area/targets, resources, scaling, stacking, summons, immunity, challenge bypass, and transformations influence review. High-risk mechanics require manual analysis.

### 5. Ordinary access needs a working test schedule

CAB recommends 1,000 XP to open an extra ordinary progression after creation and working tier access of 500 / 1,250 / 2,500 / 5,000 XP for T2–T5. These are relative test anchors, not a final pacing claim.

### 6. Prestige should not pay for nonexistent lower tiers

A Prestige progression legitimately beginning at T3 should satisfy its explicit entry requirements and normally pay the T3 access anchor once, without T1/T2 back-pay and without automatically stacking an ordinary extra-tree opening charge. Its first Ability remains separately priced.

### 7. Zero debit is not zero mechanical value

CAB recommends `reference_advancement_value_xp` so free Species, innate, Campaign, milestone, or other grants can remain zero cost to the Character while still being visible in later balance comparisons.

### 8. HP should have increasing marginal cost

CAB recommends a working +5-HP block test schedule of 500, +750, +1,000, +1,500 XP, producing cumulative +5/+10/+15/+20 costs of 500 / 1,250 / 2,250 / 3,750 XP. CAB-14/15 must test survivability before final integration.

### 9. Broad-stat cost remains CAB-10 work

Recovered 250-XP Attribute/Skill, 500-XP Knowledge, and 750-XP proficiency anchors are not approved as final. Their breadth, derived effects, and learning interactions require CAB-10.

## Structural decisions established without owner gate

1. source prices are not coherent enough for wholesale adoption;
2. progression opening, tier access, direct Ability effect, upgrades, grants, and actual debit are distinct cost concepts;
3. direct Ability price is not mechanically derived from tier;
4. narrative acquisition/prerequisites/training do not automatically discount effect value;
5. source price provenance must survive calibration;
6. upgrades are priced by incremental burden;
7. high-risk action/stacking/resource mechanics require CAB-07/08/13 review;
8. Attributes/Skills/Knowledges/proficiencies remain CAB-10 valuation work.

## Owner questionnaire

Five calibration policy choices are recorded in `CAB-06_OWNER_QUESTIONNAIRE.md`:

- CAB-Q06-01 — 250-XP working CU: **A recommended**;
- CAB-Q06-02 — effect-burden direct pricing: **A recommended**;
- CAB-Q06-03 — working progression/tier access anchors and Prestige treatment: **A recommended**;
- CAB-Q06-04 — increasing-marginal HP schedule: **A recommended**;
- CAB-Q06-05 — Reference Advancement Value for free/granted progression: **A recommended**.

Unanswered items remain unresolved and do not silently default.

## Forward routing

- CAB-07: action economy and simultaneous-power burden;
- CAB-08: stacking/synergy multipliers;
- CAB-09: special acquisition and Prestige eligibility;
- CAB-10: Attributes/Skills/Knowledges/proficiencies and Intelligence/Wisdom formula;
- CAB-11/12/13: corpus repricing/structure/outlier audits;
- CAB-14/15: equal-XP and survivability benchmarks;
- CAB-16/17: absolute CU/start-XP/award pacing scale;
- CAB-18: veteran/high-XP stress;
- CAB-19: migration/refunds.

## Completion statement

CAB-06's bounded calibration work is complete when these artifacts are merged, the CAB backlog marks CAB-06 `completed_verified`, and CAB-07 is selected but held pending the five owner calibration answers. No application implementation authority is created.

## Exact successor

**CAB-07 — Action Economy & Simultaneous Power** — selected after CAB-06 closeout, with execution held until CAB-06 owner answers are recorded or explicitly deferred.
