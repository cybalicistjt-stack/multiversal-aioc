# CAB-07 — Action Economy Source Audit

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-07  
**Purpose:** quantify action-economy coverage and identify simultaneous-power risk classes before later corpus-wide repricing.

## 1. Evidence basis

CAB-07 reviewed the bounded 4,816-record portable Ability corpus used by CAB-01 through CAB-06:

- `Abilities_Core.csv` — 1,256 records;
- `Magic_Faction_Abilities.csv` — 118;
- `Prestige_Env_Abilities.csv` — 1,018;
- `Profession_Crafting_Abilities.csv` — 221;
- `Species_Innate_Abilities.csv` — 2,203.

It also reviewed current governed Character/Ability framework material and the recovered Ability PDFs already present in the project source set, especially martial, Prestige, environment, innate, elementalist, and divine material.

## 2. Canonical action-type objects exist, but their throughput semantics are not yet fully governed

The current content database contains structured-draft canonical action-type objects for:

- Action;
- Bonus Action;
- Reaction;
- Free Action;
- Passive;
- Downtime.

The current Character/Ability framework also requires timing/action data as part of Ability records. However, the action-type objects themselves do not yet state a complete default combat budget such as exactly how many Actions, Bonus Actions, Reactions, or Free Actions a Character receives per turn/round.

CAB-07 therefore treats the vocabulary as current structural evidence while presenting the default combat throughput envelope as an owner policy gate rather than silently inventing it.

## 3. Corpus coverage is incomplete

Meaningful populated fields in the 4,816-record corpus:

| Field | Meaningful records | Coverage |
|---|---:|---:|
| `Action_Economy` | 418 | 8.7% |
| `Passive_or_Active` | 476 | 9.9% |
| `Usage_Frequency` | 548 | 11.4% |
| `Activation_Trigger` | 762 | 15.8% |
| `Resource_Cost` | 337 | 7.0% |
| `Duration` | 829 | 17.2% |

Action-economy field values among the 418 meaningful records:

- Bonus action — 107;
- Reaction — 103;
- Move (source-defined) — 80;
- Action — 69;
- Passive — 56;
- Free action — 2;
- No action required — 1.

`Passive_or_Active` contains 360 Active, 74 Passive, and 42 source-defined conditional-perk records among its 476 meaningful rows.

### 3.1 Coverage differs sharply by source family

Meaningful `Action_Economy` coverage:

- Core — 316 / 1,256;
- Magic/Faction — 3 / 118;
- Prestige/Environment — 43 / 1,018;
- Profession/Crafting — 2 / 221;
- Species/Innate — 54 / 2,203.

This means CAB-07 can define the governing model now, but CAB-11/13 must still classify a large number of records before automated corpus-wide repricing can be trusted.

## 4. Recovered sources strongly use bonus-action/reaction language

The recovered martial source is especially action-economy dense. Bounded text review found dozens of explicit Bonus Action and Reaction abilities, multiple Free Action effects, several additional-reaction mechanics, and action-compression mechanics such as casting an Action-time spell as a Bonus Action.

Other recovered sources also explicitly use:

- bonus-action mobility;
- reaction defenses/counterattacks;
- free-action emergency treatment or mounting/dismounting;
- extra Action effects;
- extra Reaction effects;
- attacks delivered through a Bonus Action;
- ally action grants;
- summon/companion/mech/vehicle action expansion.

The vocabulary is therefore not incidental: it is already embedded throughout gameplay content.

## 5. Simultaneous-power risk signals

A bounded regex/text signal pass over action, effect, mechanics, scaling, special-rules, and source-text fields found the following **review signals**, not final exact playable counts:

- extra/additional Action phrasing — 118 records;
- extra/additional Reaction phrasing — 7;
- Free Action / no-action delivery phrasing — 17;
- extra/additional attack phrasing — 22;
- summon/minion/familiar/companion/drone/construct phrasing — 286.

These counts include tree-level descriptions and incomplete recovered records and therefore must not be treated as 118 confirmed extra-Action abilities or 286 confirmed independent-minion engines. They are risk-audit queues.

## 6. Examples proving the risk classes are real

Recovered examples include:

- a bioengineering Ability that grows an additional limb and grants an extra Action for simple tasks;
- Personal Time Dilation granting an extra Action for a minute;
- Prestige War Machine granting an extra Action once per combat;
- a Goblin tactical Ability spending a Bonus Action to grant an ally an immediate additional Action;
- Counteroffensive upgrades granting additional Reactions per round;
- Mounted Combat granting an additional Reaction per round and, separately, an extra Action to a mount;
- a temporal Ability that pauses time to allow an extra Action;
- martial effects that convert Action-time casting to Bonus Action delivery;
- free-action attacks after successful attack sequences.

These examples demonstrate why simultaneous-power control cannot be reduced to direct damage or tier.

## 7. Source-price comparison does not currently price action channels coherently

Where `Action_Economy` and numeric direct Ability XP both exist, bounded medians were approximately:

- Action — 500 XP (21 numeric rows);
- Bonus Action — 450 XP (40);
- Reaction — 400 XP (29).

Those medians are too similar, and coverage too sparse, to establish that source prices already account for the opportunity-cost advantage of Bonus Action/Reaction/free delivery.

CAB-06 already requires action economy to affect direct effect burden. CAB-07 must define how.

## 8. Audit conclusions

1. Multiversal already has a stable action-type vocabulary.
2. Recovered gameplay content heavily depends on Bonus Actions and Reactions.
3. The default per-turn/per-round budget is not sufficiently governed by the current action-type objects and needs explicit policy.
4. Extra Actions/Reactions, action compression, ally action grants, and independent summon/minion turns are major simultaneous-power multipliers.
5. Passive/no-action delivery removes opportunity cost and can be stronger than an identical effect that consumes an Action.
6. Resource and frequency limits can mitigate action-economy burden but do not make action multiplication free.
7. Corpus field coverage is too incomplete for automated action-economy repricing before CAB-11/13 classification work.
8. CAB-07 should regulate **effective simultaneous throughput**, not restrict how many Abilities a veteran may know.
