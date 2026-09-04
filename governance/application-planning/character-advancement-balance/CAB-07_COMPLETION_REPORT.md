# CAB-07 — Action Economy & Simultaneous Power Completion Report

**Program:** CAB — Character Advancement & Balance  
**Tranche:** CAB-07  
**State:** `completed_verified` analysis; owner policy answers pending  
**Owner/final authority:** John Brandon Turner

## Completed

CAB-07 defined the action-economy and simultaneous-power framework that CAB-06 pricing, CAB-08 stacking, and later corpus audits must use.

Durable outputs:

- `CAB-07_ACTION_ECONOMY_AND_SIMULTANEOUS_POWER.md` — human-readable framework;
- `CAB-07_ACTION_ECONOMY_AUDIT.md` — bounded source/corpus audit;
- `CAB-07_SIMULTANEOUS_POWER_MODEL_v0.1.0.json` — machine-readable model;
- `CAB-07_OWNER_QUESTIONNAIRE.md` — five owner policy gates.

## Findings

### 1. Multiversal already uses a real action-channel vocabulary

The current content database contains structured action-type objects for Action, Bonus Action, Reaction, Free Action, Passive, and Downtime. Recovered gameplay content extensively uses Bonus Actions and Reactions.

The action-type objects do not themselves state the full per-turn/per-round allowance, so CAB-07 does not silently assume the final baseline without owner confirmation.

### 2. Corpus timing metadata is incomplete

Only 418 of the 4,816 bounded Ability records have a meaningful populated `Action_Economy` field. Only 476 meaningfully classify Passive/Active, 548 usage frequency, 337 resource cost, and 829 duration.

Unknown timing cannot be treated as free, passive, or balanced. CAB-11/13 must classify high-risk missing records before automated repricing.

### 3. Action multiplication is not hypothetical

Source/text review found real examples of:

- extra Actions;
- additional/refreshing Reactions;
- action compression from Action to Bonus Action;
- free-action attacks/interactions;
- ally Action grants;
- mounts/companions receiving extra actions;
- temporal and transformation mechanics that add actions.

Signal scans also surface substantial summon/minion/companion coverage for later audit.

### 4. Opportunity cost is a pricing dimension

An identical effect delivered as an Action, Bonus Action, Reaction, Free/No Action, or Passive does not carry identical simultaneous burden. CAB-06 direct effect pricing must therefore consider what other meaningful choices remain available in the same turn/round.

### 5. Full extra Actions are qualitatively different from extra attacks

CAB-07 distinguishes:

- action compression;
- additional attacks inside an existing channel;
- full unrestricted extra Actions;
- extra/refreshed Reactions;
- ally Action grants;
- independent summon/minion action economies.

This prevents one generic "extra action" label from hiding very different power multipliers.

### 6. Anti-recursion is necessary

Action-grant and Reaction-refresh chains can compound explosively. CAB recommends a default anti-recursion rule while allowing explicit finite exceptions that state their limits and pass manual review.

### 7. Companion balance should follow actual throughput

Mounts, pets, familiars, drones, summoned creatures, and similar companions are not inherently imbalanced. The relevant question is whether they add meaningful independent combat actions, how autonomous those actions are, and what command/resource/frequency restrictions apply.

### 8. Breadth remains distinct from simultaneous power

CAB-07 does not introduce readied-Ability slots, arbitrary known-Ability caps, or escalating prices merely because a veteran owns many abilities. The control layer is delivery opportunity cost, resource/frequency limits, stacking rules, and action multiplication.

## Architecture established without owner gate

CAB-07 establishes structurally that:

1. action economy is a first-class effect-burden dimension in CAB-06 pricing;
2. Action, Bonus Action, Reaction, Free/No Action, Passive, and movement delivery must remain distinguishable;
3. action compression, extra attacks, full extra Actions, extra Reactions, ally Action grants, and independent-body actions are separate multiplier classes;
4. a non-scalar Simultaneous Power Profile is required for serious balance review;
5. missing timing data is unresolved, not assumed free;
6. full extra Actions/Reactions and persistent autonomous action economies are manual-review classes;
7. CAB-08 owns stacking/combination policy and CAB-13 owns high-risk record audit.

## Recommendations requiring owner answer

1. Use a default combat envelope of **1 Action + 1 Bonus Action + movement on the Character's turn and 1 Reaction per round**, before explicit exceptions.
2. Adopt a default anti-recursion rule for action/reaction multiplication.
3. Require meaningful limiters on consequential Free/No-Action effects.
4. Evaluate companions by the meaningful independent action economy they add rather than by existence alone.
5. Keep action compression/additional attacks available, but make unrestricted extra Actions, additional Reactions, and ally Action grants uncommon, explicit, limited, and appropriately priced.

## Owner questionnaire

`CAB-07_OWNER_QUESTIONNAIRE.md` records five questions:

- CAB-Q07-01 — default combat envelope: **A recommended**;
- CAB-Q07-02 — anti-recursion: **A recommended**;
- CAB-Q07-03 — Free/No-Action limits: **A recommended**;
- CAB-Q07-04 — companion/minion action treatment: **A recommended**;
- CAB-Q07-05 — action-multiplier authoring posture: **A recommended**.

Unanswered questions remain unresolved and do not silently default.

## Forward routing

- owner answers -> record before CAB-08 execution;
- passive/action multiplier combinations and stacking -> CAB-08;
- acquisition/eligibility -> CAB-09;
- initiative/attribute interactions -> CAB-10;
- action field classification -> CAB-11;
- multiplier placement/tree structure -> CAB-12;
- high-risk extra-action/reaction/summon audit -> CAB-13;
- equal-XP build throughput -> CAB-14/15;
- frequency/rest pacing -> CAB-16/17;
- veteran simultaneous-power accumulation -> CAB-18.

## Completion statement

CAB-07's bounded analysis is complete when these artifacts are merged, the CAB backlog marks CAB-07 `completed_verified`, and CAB-08 is selected but held pending the five owner policy answers. No Multiversal-app implementation authority is created.

## Exact successor

**CAB-08 — Stacking, Synergy & Power Multiplication** — selected after CAB-07 closeout, with execution held until CAB-07 owner answers are recorded or explicitly deferred.
