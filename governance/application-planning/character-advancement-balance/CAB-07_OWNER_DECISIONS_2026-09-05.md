# CAB-07 — Owner Decisions

**Program:** CAB — Character Advancement & Balance  
**Source:** Owner approval of all recommendations in `CAB-07_OWNER_QUESTIONNAIRE.md`  
**Date:** 2026-09-05  
**Authority:** explicit owner decision

## CAB-Q07-01 — Default combat action envelope

**Decision:** Option A.

Before explicit exceptions, a Character normally has:

- 1 Action on their turn;
- 1 Bonus Action on their turn, when a rule provides a Bonus-Action option;
- movement up to the current movement allowance on their turn;
- 1 Reaction per round when a valid trigger occurs.

Free Actions require explicit rules. Passive effects consume no activation action. Owning multiple Abilities that use the same channel does not increase the number of uses of that channel.

## CAB-Q07-02 — Anti-recursion for Action/Reaction multiplication

**Decision:** Option A.

Action-multiplier effects do not recursively generate or refresh the same multiplier class by default. An extra Action normally cannot activate another Ability whose primary purpose is to grant or refresh Actions/Reactions. Extra-Reaction loops and unbounded summon/action chains are likewise blocked by default.

A deliberate exception must explicitly define a finite recursion limit, frequency, resource cost, allowed action subset, and pass manual balance review.

## CAB-Q07-03 — Consequential Free/No-Action effects

**Decision:** Option A.

A mechanically consequential Free Action or no-action effect must carry an explicit trigger, frequency, resource, state, or other meaningful limiter. A Free Action label never authorizes unlimited repetition of the same consequential effect in one turn. Trivial interactions may remain repeatable when their owning rules permit.

## CAB-Q07-04 — Summons, companions, familiars, mounts, drones, and minions

**Decision:** Option A.

A companion is not penalized merely for existing. Balance review measures the meaningful independent combat action economy it adds. Command costs, shared action pools, restricted action lists, hard frequency/resource limits, and short duration can mitigate that burden. Persistent autonomous full turns are manual-review effects and receive appropriate direct/reference value.

This applies across mounts, familiars, pets, drones, summoned creatures, controlled creatures, NPC-like companions, and comparable entities.

## CAB-Q07-05 — Default authoring posture for action multiplication

**Decision:** Option A.

Action compression and bounded additional attacks are legitimate design tools. Full unrestricted extra Actions, additional Reactions, and ally Action grants should be uncommon, explicit, limited, and appropriately priced.

Additional Reactions must state count and refresh window. Ally Action grants must state allowed action types and frequency. No multiplier implicitly grants Bonus Actions or Reactions unless explicitly stated.

## CAB-08 handoff consequences

CAB-08 — Stacking, Synergy & Power Multiplication may execute and must inherit:

1. the owner-approved 1 Action + 1 Bonus Action + movement / 1 Reaction baseline;
2. anti-recursion for action/reaction multiplier chains;
3. explicit limiters for consequential Free/No-Action effects;
4. companion/minion balance based on meaningful independent combat actions rather than existence alone;
5. high-throughput action multiplication as uncommon, explicit, limited, and effect-burden priced;
6. no breadth cap, readied-Ability slot system, Character Level, CR, or scalar power score is introduced.

## Supersession

These decisions resolve all five CAB-07 questionnaire items. Earlier `pending_owner_answers`, `candidate`, or recommendation-only language for these policy gates is superseded by this artifact.