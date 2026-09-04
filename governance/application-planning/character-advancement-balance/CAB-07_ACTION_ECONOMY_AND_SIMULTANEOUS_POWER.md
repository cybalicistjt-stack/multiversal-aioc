# CAB-07 — Action Economy & Simultaneous Power

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-07  
**State:** `completed_verified` analysis; owner policy gates recorded separately  
**Owner/final authority:** John Brandon Turner

## 1. Purpose

Define how Multiversal measures and controls the amount of acquired capability that can matter **at the same time**, especially through Actions, Bonus Actions, Reactions, Free/No-Action delivery, passive effects, action compression, extra Actions/Reactions, ally action grants, and independent summons/minions.

CAB-07 does not cap how many Abilities a veteran may know. It governs **delivery throughput** and identifies which Ability effects must pay a higher direct XP burden or receive special limits because they multiply simultaneous power.

CAB-08 owns stacking/synergy among multiple effects. CAB-13 owns high-risk record review. CAB-14/15 own benchmark-character and multidimensional balance tests.

## 2. Authority inherited

CAB-07 inherits:

- XP is the ordinary spendable Character-advancement currency; AP is deprecated.
- Tier is developmental depth, not raw power or price.
- Breadth is not inherently imbalance.
- Direct Ability price follows actual effect burden using the CAB-06 calibration framework.
- Working direct Ability reference bands are 250 / 500 / 1,000 / 2,000 / 4,000 / 8,000+ XP.
- Extra Actions/Reactions, passive/no-action delivery, summons/minions, and other multipliers are manual-review triggers.
- Free/granted progression can retain non-spendable Reference Advancement Value.
- PPIA-11 rejects one-dimensional power scores and requires separate treatment of action economy, resources, environment, capability profile, and uncertainty.

## 3. Core principle

> **Ownership breadth and simultaneous throughput are different balance problems.**

A Character may know dozens of narrow or situational Abilities without destabilizing play if only a limited subset can influence a given moment. Conversely, a Character with a smaller Ability list can be severely unbalanced if several passives stack, Actions multiply, Reactions refresh, summons add independent turns, or one Ability compresses multiple major effects into a single low-cost channel.

CAB-07 therefore asks two separate questions:

1. **What options does the Character own?** — advancement breadth.
2. **How much meaningful capability can the Character deliver or maintain simultaneously?** — simultaneous power.

CAB controls the second problem through timing, action opportunity cost, frequency, resources, recursion rules, and pricing—not through arbitrary limits on the total number of known Abilities.

## 4. Action-channel vocabulary

The current content database contains canonical action-type objects for:

- `Action`;
- `Bonus Action`;
- `Reaction`;
- `Free Action`;
- `Passive`;
- `Downtime`.

Recovered content also uses source-defined movement/Move actions. CAB-07 treats movement as a separate throughput dimension rather than automatically equating it to the main Action channel.

The current action-type objects name these channels but do not themselves publish the complete per-turn/per-round combat allowance. CAB-07 therefore records the default envelope as an owner gate.

## 5. Recommended default combat envelope

CAB recommendation:

During a normal combat turn/round, before explicit Ability exceptions:

- **1 Action** on the Character's turn;
- **1 Bonus Action** on the Character's turn, usable only when a rule provides a Bonus-Action option;
- **movement up to the Character's current movement allowance** on the Character's turn, distinct from the Action unless a rule says otherwise;
- **1 Reaction per round** when a valid trigger occurs;
- **Free Actions** only where a rule explicitly permits them and subject to anti-abuse limits;
- **Passive effects** require no activation action but remain subject to duration, condition, stacking, resource, and simultaneous-effect rules.

A Character does not gain extra uses of a channel merely because they own many Abilities using that channel.

This recommendation is CAB-Q07-01.

## 6. Opportunity cost and delivery burden

The same mechanical effect is not equally costly when delivered through different channels.

### 6.1 Main Action

An Action normally has the highest ordinary opportunity cost because using one Action prevents another main Action that turn.

An effect requiring an Action can therefore justify a lower direct XP price than an otherwise identical effect that requires no meaningful action opportunity cost.

### 6.2 Bonus Action

A Bonus Action is limited but usually leaves the main Action free. Strong effects delivered as Bonus Actions therefore increase turn compression and must be reviewed for what additional Action can still be performed that turn.

### 6.3 Reaction

A Reaction is normally trigger-bound and competes with other Reactions, but it adds **out-of-turn throughput** and can alter an opponent's action after commitment. Strong Reaction effects therefore receive special value from timing even when their raw magnitude looks modest.

### 6.4 Free / no-action delivery

A Free Action or no-action effect has little or no ordinary opportunity cost. It can be balanced only when its magnitude, frequency, trigger, resource cost, or other restrictions are sufficiently bounded.

A repeatable mechanical effect cannot become effectively unlimited merely because it is labeled Free Action.

### 6.5 Passive delivery

Passive effects consume no activation channel and can remain simultaneously active with other choices. A strong passive may therefore carry more direct effect burden than an otherwise similar activated effect.

CAB-08 must separately determine how multiple passives stack.

## 7. Action-economy multiplication taxonomy

CAB-07 distinguishes several different multiplier classes rather than calling all of them "extra actions."

### 7.1 Action compression

Action compression changes an effect from a more expensive channel to a cheaper channel, for example:

- cast an Action-time spell as a Bonus Action;
- Dash or Hide as a Bonus Action;
- stabilize or repair as a Free Action;
- attack as a Bonus Action after another Action.

Compression increases simultaneous throughput even when it does not literally add a new Action.

### 7.2 Additional attack inside an existing channel

An extra attack attached to an Action/Bonus Action/Reation increases output but is narrower than granting a completely unrestricted extra Action. It is still a throughput increase and must be priced from the actual attack/effect and any frequency limits.

### 7.3 Full extra Action

A full additional Action is a major multiplier because it can potentially deliver any Action-valid capability. Full extra Actions are manual-review effects.

### 7.4 Additional / refreshed Reaction

An extra Reaction expands out-of-turn throughput and can become especially strong in counterattack, interception, defense, and opportunity-trigger builds. Refreshes and multiple Reactions are manual-review effects.

### 7.5 Ally action grant

Granting another Character an immediate Action can multiply the value of the strongest option in the party, not merely the granter's own kit. It must be evaluated against the recipient's available Actions and any chain potential.

### 7.6 Independent summon/minion/companion action economy

A persistent summoned body, familiar, drone, construct, mount, companion, or minion that receives meaningful independent actions creates party-side throughput beyond the summoner's own turn. Its burden depends heavily on whether it:

- consumes the controller's Action/Bonus Action/Reation to command;
- shares the controller's action pool;
- receives a restricted action list;
- acts independently every round;
- persists between encounters;
- can itself summon, grant Actions, or create further bodies.

Free, independent, persistent extra turns are a high-risk multiplier class.

## 8. Anti-recursion principle

Action multiplication can become explosive when a granted Action generates another granted Action, restores the resource that granted it, or creates a body that grants further Actions.

CAB recommendation:

- an extra Action, extra Reaction, action grant, or action-refresh event **does not recursively generate another event of the same multiplier class by default**;
- an Action granted by an Ability cannot normally be used to activate another Ability whose primary effect is to grant/refresh Actions or Reactions;
- a granted extra Reaction cannot normally be used to trigger a Reaction-refresh loop;
- independent summons/minions cannot recursively create unbounded new action economies unless an owning rule explicitly defines a bounded chain and passes manual balance review;
- explicit exceptions must state their recursion limit, frequency, resource cost, and allowed action subset.

This is not a blanket ban on combo design. It is a default anti-infinite-chain rule. CAB-Q07-02 asks for owner approval.

## 9. Simultaneous Power Profile

Every Ability audited for balance should be able to project a non-scalar **Simultaneous Power Profile** containing at least:

- activation channel;
- whether it consumes or preserves the main Action;
- trigger timing / own-turn versus out-of-turn;
- use frequency;
- resource cost and regeneration cadence;
- duration/persistence;
- number of targets/area;
- concentration/maintenance/stance/form requirement if any;
- passive or no-action state;
- extra Action/Reation/attack/compression behavior;
- ally action grant behavior;
- independent-body/minion behavior;
- whether the effect can trigger from itself or another multiplier;
- stacking group / overlap metadata for CAB-08;
- interruption/counterplay conditions;
- source and uncertainty status.

This profile is descriptive, not a single score.

## 10. Pricing interaction with CAB-06

CAB-07 does not replace the CAB-06 effect-burden bands. It refines one of their most important dimensions.

### 10.1 Upward price pressure

For comparable effect magnitude, direct price burden normally rises when the Ability:

- uses a Bonus Action instead of an Action while preserving a strong main Action;
- uses a Reaction to add out-of-turn output or negate committed enemy output;
- is Passive/Free/No-Action with meaningful repeatable effect;
- compresses multiple major effects into one channel;
- grants extra attacks without substantial opportunity cost;
- grants unrestricted extra Actions;
- grants or refreshes Reactions;
- grants an ally Actions;
- creates independent persistent bodies/actions;
- multiplies action economy for multiple allies/targets;
- can recursively trigger another multiplier.

### 10.2 Downward pressure / mitigation

Action-economy burden can be meaningfully reduced by:

- once-per-long-rest or similarly hard frequency limits;
- meaningful scarce resource costs;
- strict trigger conditions;
- restricted action subsets;
- short duration;
- command costs consuming the controller's own Action/Bonus Action/Reation;
- concentration/maintenance that excludes other strong states;
- real counterplay/interruption;
- self-risk or severe drawback.

No single mitigation automatically makes a multiplier cheap.

## 11. Free Actions and Passive effects

CAB recommends the following default:

- Free Action is a real action type, but **mechanically consequential Free Actions must have an explicit frequency/trigger or other limiter**.
- A Free Action label does not authorize repeatedly applying the same effect without limit in one turn.
- Pure communication, dropping/releasing an object, trivial mode toggle, or similarly negligible interactions may be repeatable when the owning rules permit.
- Passive effects require no activation Action, but any ongoing resource, stance, form, exclusivity, or maintenance rule remains binding.
- Passive and Free/No-Action effects are priced from their actual simultaneous contribution, not assumed cheap because they are simple to execute.

CAB-Q07-03 asks whether to adopt this default.

## 12. Summons, companions, mounts, drones, familiars, and pets

Multiversal intentionally supports mounts, familiars, pets, drones, creatures, NPCs, and other controlled entities. CAB-07 must not solve their balance by forbidding them.

Recommended principle:

> **The balance question is not whether a companion exists; it is how much independent action economy it adds.**

A mount that mainly provides movement and consumes the rider's choices is different from a mount that gains its own unrestricted extra Action each turn. A familiar that scouts outside combat is different from a familiar adding a full independent combat turn. A drone with a command cost is different from a fleet of autonomous attack drones acting for free.

CAB recommends that independent meaningful combat actions be explicitly accounted for in the Simultaneous Power Profile and direct/reference value. Persistent autonomous action economies require manual review.

This is CAB-Q07-04.

## 13. Baseline extra-action restrictions

CAB recommendation for ordinary authored content:

- **Action compression** may be common at moderate/high burden when the compressed effect is bounded.
- **Additional attacks** may be allowed where their attack/effect, trigger, and frequency are explicit.
- **Full unrestricted extra Actions** should be uncommon and strongly limited by frequency/resource/duration or priced as major/extreme effects.
- **Additional Reactions** should be uncommon and specify the number available and refresh window.
- **Ally Action grants** should be uncommon and specify allowed action types plus frequency.
- No action-multiplier effect should implicitly grant Bonus Actions/Reactions unless explicitly stated.

CAB-Q07-05 asks whether this should be the default authoring standard.

## 14. Missing action-economy data

Only about 8.7% of the bounded Ability corpus has a meaningful populated `Action_Economy` field. CAB-07 therefore establishes two rules for later audits:

1. **Unknown is not free.** Missing timing cannot be treated as Action, Passive, or zero-cost by default.
2. Records whose balance materially depends on timing remain `balance_unresolved_action_economy` until source evidence or governed repair supplies the missing channel/frequency/trigger.

CAB-11 and CAB-13 should prioritize:

- records with extra-action/reaction language;
- free/no-action language;
- summons/minions/companions;
- attack/spell compression;
- persistent passive effects;
- effects with high direct/reference value but missing timing.

## 15. Interaction with later CAB tranches

- CAB-08 — stacking, synergy, overlapping passives, multiplier combinations, recursion across different effect classes;
- CAB-09 — eligibility/acquisition for companion, innate, transformation, faction, and special action-economy effects;
- CAB-10 — attribute/skill interactions with initiative and learning, not extra Actions by default;
- CAB-11 — populate/classify corpus action fields;
- CAB-12 — tree structure and progression placement of multiplier effects;
- CAB-13 — audit extra Actions/Reactions, summons, immunity, loops, and other high-risk records;
- CAB-14/15 — benchmark equal-XP builds and multidimensional character balance;
- CAB-16/17 — ensure frequency/rest assumptions and XP pacing remain coherent;
- CAB-18 — long-campaign accumulation of passives, reactions, companions, and action compression.

## 16. Owner policy gates

CAB-07 exposes five policy choices:

1. default combat action envelope;
2. anti-recursion rule for action multiplication;
3. Free Action / no-action consequence limits;
4. independent summon/companion action-economy treatment;
5. default authoring posture for full extra Actions/Reactions and ally Action grants.

They are recorded in `CAB-07_OWNER_QUESTIONNAIRE.md`.
