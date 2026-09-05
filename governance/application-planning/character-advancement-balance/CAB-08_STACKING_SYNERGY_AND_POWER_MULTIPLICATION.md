# CAB-08 — Stacking, Synergy & Power Multiplication

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-08  
**State:** `completed_verified` analysis; owner policy gates recorded separately  
**Owner/final authority:** John Brandon Turner

## 1. Purpose

Define how multiple owned or granted effects interact when active at the same time, so Multiversal can preserve broad Character customization without allowing accidental additive, multiplicative, recursive, transformation, defense, or resource-loop explosions.

CAB-08 governs **interaction semantics and synergy review**. It does not cap total known Abilities, create readied slots, assign a Character Level/CR, or collapse combinations into one power score.

## 2. Authority inherited

CAB-08 inherits:

- XP is the ordinary spendable advancement currency; AP is deprecated.
- Tier is developmental depth, not universal power or price.
- Direct Ability price follows actual effect burden under CAB-06.
- 1 CU = 250 XP is the current non-spendable calibration unit.
- Reference Advancement Value may represent free/granted mechanical value without charging XP.
- Ownership breadth is not itself imbalance.
- Default combat throughput is 1 Action + 1 Bonus Action + movement on turn and 1 Reaction per round before explicit exceptions.
- Consequential Free/No-Action effects require meaningful limiters.
- Action/reaction multiplier chains do not recurse by default.
- Persistent autonomous companion/minion action economies are manual-review effects.
- Full unrestricted extra Actions, additional Reactions, and ally Action grants remain uncommon, explicit, limited, and appropriately priced.
- PPIA-11 requires factor-specific analysis, explicit interaction rules, uncertainty, and indeterminate results rather than invented precision.

## 3. Source audit findings

The bounded five-file Ability corpus contains 4,816 records. Explicit stacking language is rare compared with the number of effects that can interact.

Screening over the record fields and source text found:

- 6 records containing explicit `stack/stacks/stacking` language;
- 2 records explicitly saying an effect does not stack;
- 683 records with bonus language;
- 121 with penalty language;
- 614 with advantage language;
- 128 with disadvantage language;
- 202 with resistance language;
- 119 with immunity language;
- 168 with `for each`/selected `per ...` scaling signals;
- 69 with multiply/double/triple signals;
- 238 with summon/minion/companion/familiar/drone signals;
- 192 with transformation/form signals.

These are **screening signals, not final classifications**. Full source text can contain tree summaries and repeated wording, so CAB-11/13 must inspect individual records before repricing.

Field coverage also shows substantial interaction-bearing material:

- 1,534 records meaningfully populate `Roll_Bonus_or_Penalty`;
- 615 populate `Scaling_or_Additional_Bonus`;
- 549 populate `Condition`;
- 402 populate `Upgrade_Effect`;
- 347 populate `Special_Rules`.

The explicit stacking examples prove that authored exceptions exist. Examples include:

- `Culinary Masterpiece`: permanent buffs explicitly stack once per Character;
- `Final Modding Mastery`: multiple firearm mods may have stacking effects;
- `Hardened Exoskeleton`: AC explicitly stacks with armor but not shields;
- Blood Weapon Mastery material explicitly permits stacking/simultaneous weapon traits.

Therefore CAB cannot impose a rule that makes explicit authored stacking impossible. Conversely, six explicit `stack` records are far too few to infer that every other overlapping effect automatically stacks.

## 4. Core distinction: coexistence is not stacking

CAB-08 separates four questions:

1. **Can both effects be active at once?** — coexistence.
2. **Do they modify the same mechanical quantity/state?** — overlap.
3. **If they overlap, how are their magnitudes resolved?** — stacking mode.
4. **Does their combination unlock or multiply a third effect?** — synergy.

Two Abilities can coexist without numerically stacking. Two bonuses can stack without creating a new trigger. A transformation can coexist with a passive but not with another mutually exclusive full form. A summon can coexist with a buff while still creating dangerous action-economy synergy.

## 5. Interaction identity

Source file, tree name, Species, class, faction, or acquisition method is provenance and eligibility information, not a universal stacking rule.

Balance-capable records should be able to expose:

- `effect_instance_id`;
- `effect_name` / stable Ability ID;
- `interaction_group_id`;
- `stacking_mode`;
- target statistic/state/resource;
- magnitude/sign;
- duration;
- source Character/entity;
- whether reapplication refreshes duration;
- whether the effect is exclusive with another state/form;
- whether it is a multiplier;
- trigger relationships;
- resource input/output relationships;
- explicit authored exception text;
- source/provenance and uncertainty.

## 6. Stacking modes

CAB-08 uses explicit modes rather than one universal yes/no flag.

Supported modes include:

- `coexist` — effects operate independently and do not resolve the same quantity;
- `additive` — magnitudes add;
- `highest_only` — only the strongest applicable magnitude in the group applies;
- `lowest_only` — rare inverse case where the lowest value controls;
- `highest_benefit_plus_highest_penalty` — strongest positive and strongest negative both apply, but duplicates on either side do not accumulate;
- `replace` — newest/authorized effect replaces the prior one;
- `refresh_duration` — magnitude does not increase; reapplication renews remaining duration;
- `exclusive` — only one member of the group can be active;
- `binary_noncompounding` — additional sources do not strengthen the state;
- `capped_additive` — bonuses add only to an explicit cap;
- `multiplicative_explicit` — multiplication is authorized and the owning rule states ordering/limits;
- `trigger_chain` — interaction is a sequence rather than a numeric stack;
- `prohibited_recursive` — cycle is blocked by default.

An effect with missing interaction semantics can remain `balance_unresolved_stacking` rather than receiving an invented rule during audit.

## 7. Exact-effect reapplication — candidate default

CAB recommends that the **same named mechanical effect does not increase its magnitude by repeated application unless the owning rule explicitly says it stacks**.

Recommended overlap behavior:

- identical effect at equal magnitude: no numeric increase;
- identical effect at different magnitude: strongest applicable magnitude controls while overlap lasts;
- duration-based identical effect: a valid reapplication may refresh duration rather than multiply magnitude, unless its rule says otherwise;
- separately tracked consumable charges, wounds, tokens, marks, or counters may accumulate when their owning mechanic explicitly defines them as quantities rather than duplicate effects.

This prevents one low-cost buff/debuff from becoming an unlimited same-effect engine while preserving explicit authored stacking such as Culinary Masterpiece or mod systems.

Owner gate: CAB-Q08-01.

## 8. Distinct numerical modifiers — candidate default

CAB does not recommend a universal rule that every different-named bonus stacks, nor a universal rule that different bonuses never stack.

Recommended model:

- numerical effects that alter the same mechanical quantity declare an `interaction_group_id`;
- effects in **different compatible groups** may combine;
- effects in the **same noncumulative group** use the group's resolution rule rather than accumulating solely because their names/sources differ;
- a common default for ordinary positive/negative modifiers is `highest_benefit_plus_highest_penalty`;
- explicitly cumulative mechanics use `additive` or `capped_additive`;
- an authored exception controls over the default if authoritative and unambiguous.

Example: two generic armor-hardening bonuses classified into the same armor-enhancement group would not automatically add, while an armor enhancement and a distinct situational cover bonus could combine if their groups are compatible.

Owner gate: CAB-Q08-02.

## 9. Advantage and disadvantage — candidate default

The corpus contains hundreds of advantage/disadvantage references but does not supply a sufficiently explicit universal stacking rule in the bounded source set.

CAB recommends treating them as **binary noncompounding states**:

- one or more Advantage sources produce Advantage, not double/triple Advantage;
- one or more Disadvantage sources produce Disadvantage, not escalating Disadvantage;
- if at least one applicable Advantage and one applicable Disadvantage are present, they cancel to a normal roll unless an explicit owning rule says one has priority or uses a different mechanic;
- the existence of multiple sources remains visible for provenance/dispelling/suppression even when roll effect does not compound.

Owner gate: CAB-Q08-03.

## 10. Resistance, immunity, vulnerability, and damage reduction — candidate default

CAB recommends separating defensive states by damage/effect type and by mechanic.

Default proposal:

- multiple instances of the same Resistance to the same damage/effect type do not repeatedly halve/reduce damage;
- Immunity to that type supersedes ordinary Resistance while Immunity applies;
- Resistance does not become Immunity merely because multiple Resistance sources exist;
- Resistances to different types coexist independently;
- flat damage reduction is a different interaction group and follows its own stacking rule;
- Vulnerability is separately typed and does not automatically multiply itself with duplicate Vulnerability sources;
- explicit special rules can define a different interaction.

This avoids accidental exponential defenses while preserving different defensive channels.

Owner gate: CAB-Q08-04.

## 11. Transformations, forms, stances, and overlays — candidate default

The screening pass finds 192 transformation/form signals, heavily concentrated in Species/Innate material.

CAB recommends distinguishing:

- **full replacement transformations/forms** — identity/body/state replacement packages;
- **stances** — mutually exclusive tactical states when declared so;
- **augmentations/overlays** — narrower effects that may coexist with a form if explicitly compatible;
- **passive native traits** — retained unless the form rule explicitly suppresses or replaces them.

Default proposal:

- one full replacement transformation/form is active at a time;
- activating another full form replaces/ends the previous full form unless an explicit rule authorizes nesting;
- augmentations may coexist only when their compatibility is explicit or their interaction group is nonexclusive;
- a transformation bundle is priced/reviewed for all simultaneously granted benefits and interaction hooks, not only its headline effect.

This prevents accidental combinations such as multiple Avatar-style full-body packages being assumed simultaneously active simply because each record is individually legal.

Owner gate: CAB-Q08-05.

## 12. Multipliers — candidate default

Effects that multiply the **same underlying quantity** can create exponential growth if naively applied in sequence.

CAB recommends:

- duplicate or same-group multipliers do not multiply one another by default;
- the strongest applicable multiplier in the same multiplier group controls;
- flat/additive modifiers are resolved according to their own groups before the multiplier unless the owning rule defines a different order;
- multipliers to **different mechanical stages/quantities** may combine when explicitly modeled;
- deliberate compound multiplication must state ordering, cap/frequency, and receive manual high-risk review.

This does not ban a specific authored `double` or `triple` effect. It prevents two independently legal doubling effects from silently becoming x4 merely because the sources failed to define interaction.

Owner gate: CAB-Q08-06.

## 13. Synergy classes

CAB-08 distinguishes at least these combination classes:

### 13.1 Redundant

Second effect adds little/no mechanical value while overlap lasts. Example: duplicate same-type Resistance.

### 13.2 Additive

Effects contribute independent or explicitly cumulative magnitudes.

### 13.3 Enabling

One Ability changes the conditions under which another can operate: creates concealment for a concealment-triggered bonus, marks a target for another strike, creates terrain used by a movement feature, etc.

### 13.4 Compressive

One effect lowers the action/time/resource cost of another, increasing throughput without changing its nominal effect.

### 13.5 Multiplicative

Combination increases a quantity by product/feedback rather than a simple sum: damage multiplier plus extra attacks, crit expansion plus damage multiplier, multiple independent full turns, etc.

### 13.6 Persistent bundle

Several passives/forms/auras remain active together across turns/encounters.

### 13.7 Trigger chain

Effect A triggers B, B triggers C, or a reaction/mark/on-hit sequence creates additional events.

### 13.8 Resource loop

An effect generates/restores the resource that pays for itself or another effect, potentially producing net-positive repetition.

### 13.9 Grant/substitution chain

One effect grants another Ability, form, summon, tier, action, or capability that can itself grant more capability.

## 14. Resource and trigger cycle rule

CAB-07 already blocks recursive action/reaction multiplier loops by default. CAB-08 generalizes cycle detection across resources and triggers.

Recommended structural rule, inherited unless the owner later overrides:

- a closed loop that can repeat without an external bounded input is a manual-review condition;
- an event cannot be presumed to trigger itself indirectly through another effect merely because every edge is individually legal;
- a resource-spending loop that restores as much or more of its enabling resource per iteration is `high_risk_resource_cycle` unless a hard frequency/cap/external constraint bounds it;
- a grant chain cannot create unbounded permanent or temporary copies of itself;
- authored finite loops must state the loop bound and reset cadence.

This is an extension of the already owner-approved CAB-07 anti-recursion principle, not a new blanket combo ban.

## 15. Synergy Review Profile

Balance review should project combinations using a non-scalar **Synergy Review Profile**.

For a pair/set of effects, record:

- participating stable IDs;
- active interaction groups;
- coexistence/exclusivity;
- stacking mode per shared quantity;
- action-economy interaction;
- duration overlap;
- resource input/output interaction;
- trigger graph and cycles;
- defense/immunity interaction;
- transformation/form compatibility;
- summon/companion interaction;
- scaling/cap interaction;
- whether combination is redundant, additive, enabling, compressive, multiplicative, persistent, recursive, or mixed;
- explicit source interaction rule if present;
- uncertainty/missing data;
- required manual-review reason;
- CAB-06 price/RAV consequences.

No weighted total is required.

## 16. Pricing consequence

CAB-06 prices individual effect burden, but CAB-08 establishes when a seemingly modest individual Ability needs additional burden because it predictably amplifies other owned options.

Upward pressure includes:

- very broad compatibility with many strong effects;
- multiplying attacks/actions/targets/damage rather than adding a fixed effect;
- persistent no-action stacking;
- granting a stackable state to many allies;
- enabling high-value effects without their usual cost/condition;
- resource-positive loops;
- full-form bundles retaining many outside passives;
- effects whose value scales strongly with the number of other owned Abilities.

A combo-sensitive Ability is not automatically overpriced in isolation. CAB-13/14/15 must test actual combinations and equal-XP builds before final repricing.

## 17. Missing interaction data

Source-unspecified interaction semantics remain unresolved.

CAB-11/13 should prioritize records with:

- large flat bonuses or penalties;
- Advantage/Disadvantage plus another roll modifier;
- Resistance/Immunity plus flat reduction;
- multiple persistent passives;
- transformation bundles;
- `for each`/per-target scaling;
- double/triple/multiply language;
- triggers that can feed other triggers;
- resource generation/regeneration;
- summons/companions plus buffs/action grants;
- explicit stack/non-stack wording that must be preserved exactly.

Unknown interaction does not silently mean `stacks`, `does_not_stack`, or `zero balance burden`.

## 18. Forward routing

- CAB-09 — acquisition/eligibility and whether combination access is restricted by source/Species/faction/form/etc.;
- CAB-10 — Attribute/Skill/proficiency numerical modifier families and their stacking groups;
- CAB-11 — corpus-wide statistical classification and missing interaction fields;
- CAB-12 — tree/branch structure and intended synergy placement;
- CAB-13 — high-risk multiplier/resource/defense/form/action combinations;
- CAB-14/15 — equal-XP combination benchmarks and multidimensional balance;
- CAB-18 — veteran accumulation and persistent-buff stress.

## 19. Owner policy gates

CAB-08 exposes six owner decisions:

1. same-effect reapplication;
2. distinct numerical modifier interaction groups;
3. Advantage/Disadvantage stacking;
4. Resistance/Immunity defensive overlap;
5. full transformations/forms;
6. same-quantity multipliers.

These are recorded in `CAB-08_OWNER_QUESTIONNAIRE.md`.
