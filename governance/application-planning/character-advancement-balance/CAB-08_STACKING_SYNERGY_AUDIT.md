# CAB-08 — Stacking & Synergy Source Audit

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-08  
**Scope:** bounded five-file portable Ability corpus plus current CAB/PPIA balance authority  
**State:** analysis evidence

## 1. Corpus boundary

Files reviewed from `MV_Master_01_Core/03_CSV_Sources`:

| Source | Records |
|---|---:|
| Abilities_Core.csv | 1,256 |
| Species_Innate_Abilities.csv | 2,203 |
| Magic_Faction_Abilities.csv | 118 |
| Prestige_Env_Abilities.csv | 1,018 |
| Profession_Crafting_Abilities.csv | 221 |
| **Total** | **4,816** |

The audit screened `Ability_Name`, `Effect`, `Mechanics`, `Scaling_or_Additional_Bonus`, `Upgrade_Effect`, `Special_Rules`, `Tree_Core_Mechanics`, and `Full_Source_Text` for interaction signals.

Because full source text can repeat tree summaries or parent material, keyword counts are **triage counts only**, not final record classifications.

## 2. Explicit stack/non-stack language is sparse

Across the bounded corpus:

- explicit `stack/stacks/stacking`: **6** records;
- explicit `does not stack`/equivalent: **2** records.

By file:

| Source | Stack signal | Explicit non-stack |
|---|---:|---:|
| Abilities_Core | 2 | 0 |
| Species_Innate | 2 | 2 |
| Magic_Faction | 1 | 0 |
| Prestige_Env | 0 | 0 |
| Profession_Crafting | 1 | 0 |

This is far too little explicit wording to derive a universal interaction rule directly from corpus frequency.

## 3. Explicit examples that must survive normalization

### Culinary Masterpiece

`Profession_Crafting_Abilities.csv`, `ABL4-00104` states that permanent meal buffs **stack once per character**.

Implication: CAB needs an explicit cumulative mode and cannot globally prohibit stacking.

### Final Modding Mastery

`Abilities_Core.csv`, `ABLREC-01254` allows five firearm mods and states those mods can have **stacking effects**, including multiple damage upgrades.

Implication: equipment/crafting systems may deliberately opt into additive/cumulative behavior.

### Blood Weapon Mastery — Specialized Weaponry

`Abilities_Core.csv`, `ABLREC-00489` includes upgrade language allowing traits to stack or be applied simultaneously.

Implication: a record may intentionally layer distinct traits even where a generic same-effect rule would not.

### Hardened Exoskeleton

`Species_Innate_Abilities.csv`, `ABLREC-00206` grants +1 AC that **stacks with other armor but does not stack with shields**, plus resistance to non-magical piercing damage.

Implication: source-authored compatibility can be more specific than simple same-name/different-name logic and must take precedence when authoritative.

## 4. Broader interaction signals

Screening counts across all 4,816 records:

| Signal | Records |
|---|---:|
| bonus | 683 |
| penalty | 121 |
| advantage | 614 |
| disadvantage | 128 |
| resistance | 202 |
| immunity | 119 |
| selected `for each` / `per ...` scaling phrases | 168 |
| multiply/double/triple | 69 |
| summon/minion/companion/familiar/drone | 238 |
| transformation/form | 192 |

These categories can interact even when no record uses the word `stack`.

A screening overlap pass found:

- **799** records with at least two of the selected interaction-risk signals;
- **226** with at least three;
- **75** with at least four.

These numbers are triage evidence only. Tree-level summary rows and repeated source text can raise counts. They demonstrate breadth of the interaction problem, not a balance verdict.

## 5. Structured field coverage relevant to synergy

Meaningfully populated fields:

- `Roll_Bonus_or_Penalty`: **1,534** records;
- `Scaling_or_Additional_Bonus`: **615**;
- `Condition`: **549**;
- `Upgrade_Effect`: **402**;
- `Special_Rules`: **347**.

This supports CAB-08 treating stacking/synergy as a first-class data requirement rather than an edge-case note.

## 6. Representative high-interaction records

These are examples, not the only high-risk records.

### Avatar of Divinity — `ABL3-00641`

Tier 5; combines transformation, immunity to non-magical damage, resistance to magical damage, and +5 to all saving throws for one minute.

Risk: full-form bundle plus defense overlap and persistent numerical bonus.

### Avatar of Nature — `ABL3-00112`

Tier 5; transformation plus physical immunity, magical resistance, and repeatable hazardous-terrain creation every round.

Risk: full-form compatibility, defense stacking, persistent area generation, and repeatable effect throughput.

### Avatar of Glory — `ABL3-00618`

Tier 5; transformation plus +5 attack, immunity to non-magical damage, and an additional attack per turn.

Risk: transformation bundle plus action-economy multiplication and large attack modifier.

### Sentinel's Defense — `ABLREC-00097`

Tier 3; temporary resistance to all melee damage, with an upgrade granting advantage to a subsequent Shield Bash.

Risk: defense state plus conditional offensive synergy.

### Master Duelist — `ABLREC-00020`

Tier 5; persistent +2 attack and AC in a single-enemy context, with upgrade causing an attack against the Character to have disadvantage in multi-enemy conditions.

Risk: stacked offense/defense modifiers plus condition-sensitive binary state.

### Totemic Form: Wolf Hybrid — `ABL5-00073`

Tier 4; transformation granting movement, Dexterity-check Advantage, and bludgeoning resistance.

Risk: interaction with other forms, native traits, movement bonuses, and defense states.

## 7. Why source provenance cannot decide stacking

The corpus contains compatible and incompatible interactions inside the same broad source families. A Species feature may stack with armor but not shields. Crafting explicitly permits certain stacked mods. Transformations package multiple simultaneous effects. Martial trees include passive numerical bonuses and Advantage/Disadvantage.

Therefore rules such as `different trees always stack`, `same source never stacks`, or `Species bonuses always stack` are unsupported and mechanically unsafe.

The relevant identity is the **mechanical quantity/state being modified and its interaction group**.

## 8. PPIA-11 constraint

PPIA-11 requires analysis to validate explicit interaction rules and permits an **indeterminate** result where the evidence does not establish an interaction. It prohibits invented precision and universal scalar reduction.

CAB-08 inherits that discipline:

- explicit source interaction text is preserved;
- missing interaction text is not silently completed during audit;
- authored methodology may propose defaults, but owner approval is required before they become CAB policy;
- later corpus repair must retain source truth and provenance.

## 9. Audit conclusion

The source corpus supports the need for governed stacking semantics but does **not** provide one complete universal stacking system.

CAB-08 therefore requires:

1. stable interaction groups;
2. explicit stacking modes;
3. same-effect reapplication semantics;
4. separate binary-state handling;
5. separate defense-state handling;
6. form/transformation exclusivity/compatibility metadata;
7. multiplier and resource-cycle review;
8. unresolved states when the source is insufficient;
9. preservation of explicit authored exceptions.

CAB-11/13 must perform the record-level classification and high-risk audit rather than treating these screening counts as final repairs.
