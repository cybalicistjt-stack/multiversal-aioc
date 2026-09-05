# CAB-08 — Stacking, Synergy & Power Multiplication Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-08  
**State:** `completed_verified` analysis; owner policy answers pending  
**Owner/final authority:** John Brandon Turner

## Completed

CAB-08 established a governed interaction model for simultaneous effects without limiting Character breadth or creating a scalar power system.

Durable outputs:

- `CAB-08_STACKING_SYNERGY_AND_POWER_MULTIPLICATION.md` — interaction and synergy architecture;
- `CAB-08_STACKING_SYNERGY_AUDIT.md` — bounded source/corpus evidence;
- `CAB-08_INTERACTION_MODEL_v0.1.0.json` — machine-readable interaction model;
- `CAB-08_OWNER_QUESTIONNAIRE.md` — six owner policy gates.

## Findings

### 1. Explicit stacking language is too sparse to govern the whole game

Only six bounded records explicitly use stack/stacks/stacking language and two explicitly state a non-stack condition, while hundreds of records contain bonuses, penalties, Advantage/Disadvantage, Resistance/Immunity, scaling, forms, summons, or multipliers that can interact.

Therefore missing explicit stack wording cannot safely mean either `stacks` or `does_not_stack`.

### 2. Explicit authored interaction exceptions exist and must survive

Examples include Culinary Masterpiece stacking permanent buffs once per Character, firearm mods with stacking effects, Blood Weapon traits that can stack/apply simultaneously, and Hardened Exoskeleton stacking with armor but not shields.

CAB must support explicit content-local exceptions.

### 3. Source provenance is not a stacking rule

Different tree, Species, faction, class, document, or source file is not enough to decide interaction. Mechanical quantity/state and interaction group must control.

### 4. Coexistence, overlap, stacking, and synergy are different questions

Two effects can be simultaneously active without modifying the same quantity. Overlapping effects may resolve by highest-only, additive, capped, binary, exclusive, replacement, refresh, or another explicit mode. Synergy can arise even when no numeric stack occurs.

### 5. High-risk synergy extends beyond numeric bonuses

CAB-08 identifies enabling, compressive, multiplicative, persistent-bundle, trigger-chain, resource-loop, and grant/substitution-chain synergies in addition to ordinary additive stacking.

### 6. Closed resource/trigger cycles inherit CAB-07 anti-recursion discipline

A loop that can repeat without an external bounded input is manual-review territory. Self-refunding resource loops, recursive trigger chains, and unbounded grant replication cannot be presumed valid simply because each individual edge is legal.

### 7. The corpus needs explicit interaction metadata

Later audits require stable interaction groups, stacking modes, transformation compatibility, multiplier groups, trigger/resource relationships, and unresolved states. CAB-11/13 must classify records rather than silently normalize them.

## Structural architecture established without new owner gate

CAB-08 establishes that:

1. source provenance is not stacking identity;
2. explicit authoritative interaction wording is preserved;
3. missing interaction semantics may remain unresolved;
4. interaction must distinguish coexistence, overlap, resolution mode, and synergy;
5. balance review uses a non-scalar Synergy Review Profile;
6. synergy classes include redundant, additive, enabling, compressive, multiplicative, persistent-bundle, trigger-chain, resource-loop, grant/substitution-chain, and mixed;
7. CAB-07 anti-recursion extends to closed trigger/resource/grant cycles;
8. deliberate finite loops require explicit bounds/reset cadence;
9. CAB-06 pricing/RAV may rise when an Ability predictably amplifies many other options;
10. final repricing waits for CAB-13/14/15 evidence rather than being performed silently here.

## Recommendations requiring owner answer

1. Same named mechanical effect is noncompounding by default; strongest magnitude applies and valid reapplication may refresh duration unless explicit stacking is authored.
2. Different numerical modifiers use mechanical interaction groups; compatible groups combine, while ordinary same-group modifiers default to strongest beneficial plus strongest detrimental unless explicitly cumulative.
3. Advantage/Disadvantage are binary noncompounding states and cancel to normal when both apply unless an explicit priority rule says otherwise.
4. Same-type Resistance does not compound or become Immunity; Immunity supersedes Resistance; different damage types coexist; other defense mechanics use separate groups.
5. Full replacement transformations/forms are exclusive by default; explicit nesting/compatible augmentations remain possible.
6. Same-quantity multipliers do not sequentially compound by default; strongest same-group multiplier applies unless deliberate compound multiplication is explicitly authored and manually reviewed.

## Forward routing

- owner answers -> record before CAB-09 execution;
- acquisition/eligibility and access to combinations -> CAB-09;
- Attribute/Skill/proficiency modifier groups -> CAB-10;
- corpus-wide interaction classification -> CAB-11;
- tree/branch synergy structure -> CAB-12;
- actual high-risk combos/loops/forms/defenses -> CAB-13;
- equal-XP and multidimensional benchmark validation -> CAB-14/15;
- veteran accumulation stress -> CAB-18.

## Completion statement

CAB-08 bounded analysis is complete when these artifacts are merged, CAB-08 is marked `completed_verified`, and CAB-09 is selected but held pending the six owner policy decisions. No application runtime, software-roadmap, release, deployment, schema-migration, or content-repricing authority is created.

## Exact successor

**CAB-09 — Acquisition & Eligibility** — selected after CAB-08 closeout, with execution held until CAB-08 owner answers are recorded or explicitly deferred.
