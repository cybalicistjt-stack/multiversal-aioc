# CAB-13 — High-Risk Ability Audit

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-13

## Purpose

Identify Ability classes and concrete records where individually plausible mechanics can multiply simultaneous power, bypass encounter pressures, or become impossible to balance deterministically without missing timing/resource/interaction data. This is a review queue, not a ban list and not a wholesale rewrite.

## Screening counts

Regex/source-field screening across all 4,816 Ability records found the following candidate signals: action multiplier 28; additional attack 28; Free/No Action 17; Immunity 117; Resistance 202; summon/companion 249; multiplier/double/triple 110; per-each scaling 83; Passive 81; regeneration 47; auto-success 43; ignore/bypass 46; transformation/form 198; resource generation 84; permanent 38.

These overlap heavily and are triage signals, not final classifications.

## Missing mechanics inside high-risk screens

The screening confirms that historical source prices often coexist with missing delivery constraints. Examples:

- action-multiplier candidates: 28 total, only 12 numeric direct prices; 11 lack meaningful Action Economy, 12 frequency, 22 Resource Cost;
- summon/companion: 249 total, only 17 numeric prices; 212 lack Action Economy, 206 frequency, 216 Resource Cost;
- transformation: 198 total, 31 numeric prices; 160 lack Action Economy, 150 frequency, 160 Resource Cost;
- immunity: 117 total, 41 numeric prices; 96 lack Action Economy, 90 frequency, 96 Resource Cost;
- resource-generation: 84 total, 42 numeric prices; 60 lack Action Economy, 58 frequency, 69 Resource Cost.

A consequential high-risk record missing timing/frequency/resource/stacking information is **not balance-certified by having a tier or XP price**. It remains `high_risk_mechanics_unresolved` until the owning source or governed repair supplies the missing semantics.

## Manual-review classes

The following classes always receive manual balance review when materially consequential:

1. full extra Actions or refreshed Actions;
2. additional/refreshed Reactions;
3. ally Action grants or persistent independent action economies;
4. autonomous summons/companions/minions with meaningful full turns;
5. broad immunities or multi-type defensive bundles;
6. regeneration/recovery that materially changes attrition;
7. transformations/forms bundling multiple offensive/defensive/mobility benefits;
8. same-quantity multipliers or exponential scaling;
9. automatic-success or challenge-bypass effects;
10. effects that ignore/bypass defenses, prerequisites, positioning, or normal counters;
11. resource generation/refund loops;
12. unbounded `per target`, `for each`, stack-count, or trigger-chain scaling;
13. persistent global/passive bundles that materially alter many checks/targets;
14. permanent changes whose acquisition/interaction consequences are unclear.

High-risk does **not** mean banned, Tier 5 only, or automatically 8,000 XP. Duration, resource cost, narrow triggers, dependency, opportunity cost, counterplay, target scope, and rarity of use can reduce burden. Conversely, a low-tier or cheap source record can still require major repricing.

## Concrete review examples

### Countermastery — Counteroffensive Combat T5
Passive; successful counterattack can grant an extra Reaction this turn, with a later twice-per-round expansion. CAB-07 anti-recursion applies. Direct XP is unspecified. Manual action-economy review required.

### Master of War Mounts — Mounted Combat T5
Mount gains an extra Action every turn usable to attack or Dash. Timing/frequency/resource data are otherwise sparse. This is persistent companion action multiplication and requires Character cost/RAV plus companion-throughput review.

### Avatar of Glory — Champion Path T5 — source price 5,000 XP
One-minute transformation grants +5 attack rolls, immunity to nonmagical damage, and an additional attack each turn. This is a multi-axis high-risk bundle; 5,000 XP is provenance, not accepted calibration.

### Personal Time Dilation — Temporal & Reality Bending Science T3 — 2,000 XP
Once per long rest; doubles movement and grants an extra Action for one minute. The finite frequency helps, but unrestricted repeated full Actions make this a manual-review/repricing candidate.

### Ethereal Overdrive — Spellsword T5
One-minute enhanced state: resistance to all damage, +2 attacks/saves, regenerate 10 HP/turn, 15 mana cost, later immunity/regen upgrades. Multi-axis defense/output/recovery bundle; manual benchmark required.

### Regenerative Shift — Combat Forms T5
Regain 5 HP at start of turn while transformed if at least 1 HP, suppressed by recent fire/necrotic damage. Requires survivability/attrition benchmark rather than tier-only pricing.

### Perfect Timing — Counteroffensive T3
Once per turn when an enemy misses, gain an additional Reaction even if already used. Distinct from another same-named Parrying ability; source-qualified identity is mandatory. High-risk reaction generation.

### Supreme Rider’s Reflexes — Mounted Combat T5
Extra Reaction per round while mounted. Manual action-economy review required.

## Source-boundary defect: Rain of Arrows

`Abilities_Core.csv` record `ABLREC-00483`, Rain of Arrows, contains its own once/day 20-ft-radius 6d10 effect but its Mechanics field continues into a long unrelated Blood Weapons rules section. This is a **P0 source-field boundary/integrity defect**, not merely a balance question. Repair must recover source boundaries and preserve both pieces with provenance rather than deleting or guessing.

Long Mechanics text is only a screening heuristic. Other long rows require source confirmation before being labeled contamination.

## Pricing posture

CAB-06 remains controlling:

- source XP is provenance;
- high-risk effects use effect burden, not tier, to select a direct band;
- unrestricted full action multipliers, broad defensive bundles, or several simultaneous high-impact axes will often fall in the 8,000+ manual-review band;
- meaningful resource/frequency/duration/counterplay can justify lower prices;
- free/granted high-risk mechanics still carry RAV for benchmark comparison.

## Adopted decisions

Under standing owner delegation:

- high-risk mechanics are legal design space but always manually reviewed;
- missing critical delivery/interaction data blocks deterministic balance classification;
- CAB-07 anti-recursion and CAB-08 stacking/multiplier defaults remain global safeguards;
- source price never immunizes a record from repricing;
- source-boundary/data-integrity defects outrank ordinary repricing;
- CAB-13 creates a review queue, not automatic corpus edits.

No delegation guardrail triggered.

**Successor:** CAB-14 — Equal-XP Benchmark Characters.