# CAB-10 — Attributes, Skills & Proficiencies

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-10  
**State:** `completed_verified` candidate under standing owner delegation  
**Owner/final authority:** John Brandon Turner

## Purpose

Reconcile Attribute advancement, general Skills, Knowledge fields, and Proficiencies with the CAB XP economy without reviving AP, flattening everything into Ability tiers, or allowing high Intelligence/Wisdom to become a global XP multiplier.

## Governing separation

Attributes, Skills, Knowledges, Proficiencies, and Abilities are different progression objects. Attributes are broad statistics; Skills use the retained 1–20 rank surface; Knowledges are five-tier fields; Proficiencies are bounded mastery states; Abilities remain discrete nodes. A requirement in one domain does not silently become another domain's requirement or cost.

## Attribute advancement

CAB-03 already establishes the normal creation baseline: all six core Attributes begin at 10, Species modifiers apply, then the Character receives a free 12-point creation allocation.

Post-creation permanent Attribute increases are bought one point at a time. Temporary effects do not affect advancement price.

Price each purchased +1 from the **resulting permanent Attribute score after Species and other permanent source modifiers but before temporary effects**:

| Resulting score | XP |
|---|---:|
| 11–12 | 250 |
| 13–14 | 500 |
| 15–16 | 1,000 |
| 17–18 | 2,000 |
| 19–20 | 4,000 |
| 21+ | 8,000+ and explicit source/Campaign permission/manual review |

This is not a universal hard cap. The old Regular/High/Hyper creation packages are not post-creation pricing shortcuts.

## Skill ranks

The retained Skill system has 20 ranks and a strongly progressive legacy cost curve. CAB-10 keeps the 20-rank structure but normalizes cost into CAB calibration units.

For Skill rank `n` from 1–20:

- marginal cost to buy rank `n` = `250 × n` XP;
- cumulative XP from rank 0 to rank `n` = `125 × n × (n + 1)` XP.

Examples: rank 1 = 250 cumulative; rank 5 = 3,750; rank 10 = 13,750; rank 15 = 30,000; rank 20 = 52,500. A Skill's actual check contribution remains its authored Skill modifier/rank behavior; CAB does not invent a second universal proficiency bonus.

## Knowledge fields

The retained five tiers remain Basic Understanding, Proficient, Advanced Expertise, Mastery, and Pioneer. Knowledge tier is not Ability-tree tier.

Marginal XP by new Knowledge tier: 250 / 500 / 1,000 / 2,000 / 4,000 XP, for 7,750 cumulative XP to Tier 5. The source's +1 relevant-check bonus per tier is retained subject to CAB-08 stacking groups.

For task applicability, exact/highly-similar fields can use full tier where confirmed; somewhat similar fields may function one tier lower; lightly related fields provide context/assistance; unrelated fields provide no direct benefit. For explicit prerequisites, similarity does not silently substitute: the owning rule or attributable GM/Campaign ruling must authorize the substitution.

Higher Knowledge may eliminate rolls for genuinely routine, uncontested tasks within established expertise. It does not auto-succeed against opposed actors, dangerous/high-stakes uncertainty, hidden information, explicit gates, or encounter mechanics.

## Proficiencies

Base states remain Unproficient, Proficient, Expertise, Mastery. Advanced Mastery is specific Ability content rather than a fifth generic state.

For an ordinary narrow proficiency domain, working marginal anchors are 250 XP to become Proficient, +500 to Expertise, +1,000 to Mastery. Broad categories may use higher effect-burden prices. Specific mastery techniques are separately priced Abilities and remain subject to CAB-07/08.

Proficiency state does not invent a universal attack/check bonus; the owning system defines the mechanical benefit.

## Intelligence/Wisdom faster learning

When an owning learning project identifies Intelligence or Wisdom as its learning Attribute:

`learning_time_multiplier = max(0.50, 1.00 - 0.05 × max(0, relevant_attribute - 10))`

Each permanent point above 10 reduces baseline learning time by 5%, capped at 50%. Thus 12→90%, 14→80%, 16→70%, 18→60%, and 20+→50% of baseline time.

The owning project chooses Intelligence, Wisdom, or an explicit governed combination. Both do not automatically multiply. Mentoring/facilities may modify learning progress under owning rules, but do not create spendable XP. Legacy `1d6 × 10 XP` teaching wording is therefore retired as XP generation while mentorship survives as learning assistance.

## Prerequisites, stacking, grants

Attribute thresholds inspect the owning required state. Skill/Knowledge/Proficiency prerequisites use stable IDs and ranks/tiers/states. CAB-08 interaction groups govern overlapping bonuses. Enough XP never substitutes for required competency. Creation/Species/background/profession/Campaign grants retain source and Reference Advancement Value and create no XP debt.

## Adopted recommendations

Under the standing CAB owner delegation CAB-10 adopts: progressive Attribute bands; `250 × next rank` Skill pricing; five Knowledge tiers at 250/500/1,000/2,000/4,000; task-only default Knowledge similarity; four base Proficiency states with narrow 250/500/1,000 anchors; and the capped 5%-per-point Int/Wis learning formula. No delegation guardrail triggered.