# CAB-03 — Character-Creation Baseline Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-03  
**State:** `completed_verified` candidate pending merge  
**Owner/final authority:** John Brandon Turner  

## Completed

CAB-03 reconciled the supported Character-creation baseline from current Character architecture, CAB-01/02 decisions, recovered owner-authored creation rules, creation PDFs, and specialized attribute/background/health/knowledge/skill/proficiency sources.

Durable outputs:

- `CAB-03_CHARACTER_CREATION_BASELINE.md` — human-readable source reconciliation and recommended default baseline;
- `CAB-03_CREATION_BASELINE_LEDGER_v0.1.0.json` — machine-readable creation ledger and conflict register;
- `CAB-03_OWNER_QUESTIONNAIRE.md` — four informed owner gates.

## Findings

### 1. The 1,300-XP starting value is strongly supported

The owner explicitly corrected an earlier assistant error with `Starting xp is 1300`, and the recovered Character Creation PDF repeats 1,300 XP throughout its introduction, FAQ, worksheet and budget summary.

CAB-03 therefore rejects the older assistant-generated 10,000-XP claim.

### 2. The default Character already receives a substantial free foundation

The recovered owner-authored creation rules provide:

- free base Species;
- free Homeworld Type core benefits;
- free Cultural Influence core benefits;
- free Early Life Profession core benefits;
- five free starting Ability Trees;
- free Tier 1 access in those trees;
- five free Tier 1 Abilities;
- source-defined free Tier 1 Knowledges/grants;
- unspent starting XP may remain available after activation.

This means 1,300 XP is customization budget on top of a playable foundation rather than the price of constructing the entire Character from zero.

### 3. Starting wealth is now cleanly separated

CAB-02 owner decisions supersede every creation rule that converts XP to Credits or makes ordinary equipment an XP purchase. Starting money/equipment is a separate GM/Campaign creation-policy decision.

### 4. The Attribute Modes are mechanically inconsistent

The Regular/High/Hyper source contradicts its own stated point pools, focus templates, example allocations and 250-XP-per-+1 price. The modes cannot be accepted as written.

CAB recommends one free 12-point starting allocation after base 10 plus Species modifiers, with later XP increases calibrated in CAB-10/CAB-06.

### 5. Background core structure is stable; its 1,800-XP category cap is not

The three core background components are consistently free. Optional upgrades are source-attested XP purchases. An earlier owner draft gives a 1,800-XP maximum, while the later Character Creation PDF omits that limit.

CAB recommends no universal category cap; available XP, eligibility and Campaign policy already bound the purchase.

### 6. Starting HP has a later explicit source rule

The May 2025 health source sets starting HP to `max(10, Constitution)` plus Species modifiers and permits creation-only XP investment in permanent HP. CAB recommends retaining the concept but sending the listed prices through later balance calibration.

### 7. Skill/Knowledge/proficiency categories survive, but their creation prices do not reconcile

The simple prices in Character Creation conflict with specialized source documents. CAB-03 therefore recognizes them as valid XP-spend categories without canonizing the legacy numbers. CAB-10 owns reconciliation.

### 8. Ability/tier prices remain deferred

Five free trees and five free Tier-1 Abilities are retained as creation grants, but extra-tree, tier-unlock and Ability purchase prices are not finalized here. CAB-04/05/06 own those decisions.

### 9. Direct spell XP purchase is not a universal creation rule

CAB-02's structured spell evidence says the spell itself costs 0 direct XP while capacity/slot progression is purchased under owning archetype rules. Starting spells are therefore grants from source mechanics, not a general per-spell creation shopping list.

## Recommended default baseline

Subject to the four explicit owner gates:

1. 1,300 starting advancement XP.
2. Base attributes 10 plus Species modifiers.
3. One free 12-point starting attribute allocation.
4. Free base Species.
5. Free Homeworld Type, Cultural Influence and Early Life Profession core selections.
6. Starting HP = `max(10, Constitution)` plus Species modifiers.
7. Five free eligible Ability Trees.
8. Tier 1 access free in those trees.
9. Five free eligible Tier 1 Abilities.
10. Source-defined free Knowledges, spells, proficiencies and other grants apply normally.
11. Starting wealth/equipment is separately set by GM/Campaign policy.
12. XP may be spent on eligible permanent Character advancement, not ordinary assets.
13. Unspent creation XP carries into play.

## Recommendations

1. Treat **1,300 XP as the normal-start default**, with explicit Campaign-policy override for experienced/high-power/low-power starts rather than inventing Character levels.
2. Replace the broken Attribute Modes with **one free 12-point pool**; make Physical/Mental/Balanced examples only.
3. Remove the universal **1,800-XP background cap**; allow Campaign profiles to set one if desired.
4. Keep **creation-only permanent HP investment** as a valid XP-buy concept, but recalibrate its exact prices later.
5. Preserve the creation ledger distinction between free grants, free selections, XP purchases, Campaign grants and wealth purchases.
6. Do not reintroduce XP-to-money conversion, AP, or direct per-spell shopping through old creation text.

## Established decisions inherited

- AP is deprecated.
- XP is ordinary Character advancement currency.
- ordinary assets do not use XP;
- starting wealth is GM/Campaign-defined;
- no ordinary XP-to-money conversion;
- no ordinary percentage XP multipliers;
- high Intelligence/Wisdom must later receive a governed faster-learning benefit without a blanket XP multiplier;
- hazard/trap XP values remain reference evidence rather than automatic payouts.

## Owner questionnaire

`CAB-03_OWNER_QUESTIONNAIRE.md` asks four questions, with recommendations:

1. starting-XP rigidity — **B**;
2. Attribute Mode replacement — **A**;
3. background 1,800-XP cap — **A**;
4. creation-only permanent HP buy — **A**.

Unanswered items remain unresolved and are not silently defaulted.

## Forward routing

- starting baseline owner answers -> record before CAB-04 execution;
- advancement gate architecture -> CAB-04;
- five-tier semantics -> CAB-05;
- XP price calibration -> CAB-06;
- acquisition eligibility -> CAB-09;
- attributes/skills/proficiencies and Intelligence/Wisdom learning role -> CAB-10;
- progression pacing -> CAB-16;
- XP awards -> CAB-17;
- respec/migration -> CAB-19.

## Completion statement

CAB-03's bounded source-reconciliation work is complete when these artifacts are merged, the CAB backlog marks CAB-03 `completed_verified`, CAB-04 is selected_not_started, and the four owner gates are recorded as awaiting answers. CAB-04 must not silently resolve those questions.

## Exact successor

**CAB-04 — Advancement Architecture** — selected after CAB-03 closeout, with execution held until the CAB-03 owner answers are recorded.
