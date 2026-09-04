# CAB-03 — Character-Creation Baseline Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-03  
**State:** `completed_verified`  
**Owner/final authority:** John Brandon Turner  
**Owner decisions:** `CAB-03_OWNER_DECISIONS_2026-09-04.md`

## Completed

CAB-03 reconciled the supported Character-creation baseline from current Character architecture, CAB-01/02 decisions, recovered owner-authored creation rules, specialized attribute/background/health/knowledge/skill/proficiency sources, and the resolved CAB-03 owner questionnaire.

Durable outputs:

- `CAB-03_CHARACTER_CREATION_BASELINE.md` — final human-readable creation baseline;
- `CAB-03_CREATION_BASELINE_LEDGER_v0.1.0.json` — machine-readable creation ledger and resolved conflict register;
- `CAB-03_OWNER_QUESTIONNAIRE.md` — preserved questionnaire with resolved answers;
- `CAB-03_OWNER_DECISIONS_2026-09-04.md` — explicit owner authority.

## Final findings and decisions

### 1. Starting XP

The current normal-start advancement grant is **1,300 XP**. A GM/Campaign creation policy may explicitly choose another starting grant for a different campaign power level. The 1,300 number is not immutable: CAB may later recommend adjustment after cost calibration, equal-XP benchmarks, pacing analysis and integrated simulation.

### 2. Starting wealth

Starting money/equipment is separate from advancement XP and is set by GM/Campaign creation policy. There is no ordinary XP-to-money conversion.

### 3. Free creation foundation

The normal creation foundation retains:

- free base Species;
- free Homeworld Type core benefits;
- free Cultural Influence core benefits;
- free Early Life Profession core benefits;
- five free eligible Ability Trees;
- free Tier-1 access in those trees;
- five free eligible Tier-1 Abilities;
- source-defined free Knowledges, spells, proficiencies and other grants;
- carry-forward of unspent starting XP.

### 4. Attributes

The recovered Regular/High/Hyper numbers are internally inconsistent and do not govern current creation.

The operative normal-start rule is:

- all six attributes begin at 10;
- apply Species modifiers;
- allocate one free **12-point pool**;
- further permanent increases use the later calibrated XP economy.

Physical/Mental/Balanced may remain example distributions.

The **concept** of Regular/High/Hyper may survive as optional alternate Campaign starting-power packages, but they must be fully rebuilt and benchmarked before use. Their current point totals and prices are rejected.

### 5. Backgrounds

There is no universal 1,800-XP background customization cap. The three core background components remain free; optional upgrades spend available advancement XP and obey eligibility/prerequisites. Campaign policy may impose a category cap where desired.

### 6. HP

Base starting HP remains `max(10, Constitution)` plus explicit Species modifiers and governed grants.

Creation-only purchase of additional permanent HP remains a valid XP-buy concept. The recovered +5/+10/+15/+20 HP and 300/750/1,250/2,000-XP ladder is provisional and must be calibrated in CAB-06.

### 7. Skills, Knowledges, proficiencies, Ability/tier prices and magic

These remain valid advancement domains where their owning rules allow them, but their conflicting legacy prices are not finalized by CAB-03.

- CAB-10 owns attributes/Skills/proficiencies reconciliation.
- CAB-04/05/06 own tree/tier/Ability access and pricing architecture.
- Direct spell purchase is not a universal rule; structured spell evidence continues to point toward capacity/slot progression under owning magic rules.

## Creation ledger

CAB-03 requires creation to distinguish:

- `granted_free`;
- `selected_free`;
- `xp_purchased`;
- `campaign_granted`;
- `wealth_purchased`;
- `deferred`;
- `unavailable`.

This prevents free grants, XP purchases and ordinary wealth purchases from collapsing into one ambiguous starting budget.

## Recommendations carried forward

1. Treat 1,300 XP as the current working normal-start default and test it rather than protecting it from evidence.
2. Preserve the 12-point normal attribute pool as the baseline while later evaluating optional rebuilt Regular/High/Hyper campaign profiles.
3. Do not restore the universal 1,800-XP background cap.
4. Retain creation-only HP investment but calibrate the exact cost.
5. Preserve the creation-ledger distinction between grants, XP purchases, Campaign grants and wealth purchases.
6. Do not reintroduce AP, XP-to-money conversion, or ordinary percentage XP multipliers.

## Forward routing

- advancement architecture and learning/training attachment -> CAB-04;
- five-tier semantics -> CAB-05;
- XP price calibration and HP pricing -> CAB-06;
- acquisition eligibility -> CAB-09;
- attributes/Skills/proficiencies and Intelligence/Wisdom learning role -> CAB-10;
- equal-XP creation benchmarks -> CAB-14;
- progression pacing and starting-XP validation -> CAB-16;
- integrated starting-budget simulation -> CAB-21.

## Completion statement

CAB-03 is `completed_verified`. All four owner gates are resolved. No application implementation authority is created.

## Exact successor

**CAB-04 — Advancement Architecture** — `selected_not_started` and cleared to execute.
