# CAB-19 — Respec, Correction & Migration

## Purpose

Define how permanent advancement can be voluntarily changed, corrected after rules/data errors, and migrated from legacy economics without deleting history, breaking dependent choices, or creating retroactive XP debt.

## Three distinct workflows

### Voluntary respec

A voluntary respec is a player-requested redesign, not a correction. Availability is controlled by Campaign/GM policy, downtime, retraining opportunity, safe location, milestone, service, or another explicit rule. It is **not** assumed available as tactical at-will swapping.

When voluntary respec is allowed, the normal refund is **100% of actual Character XP debited for the removed paid advancements**. Abuse is controlled by respec availability/process rather than an arbitrary refund haircut.

Free grants and RAV produce **0 XP refund** because the Character paid 0 XP. A granted option may be removed only if the owning grant/respec rule allows it.

### Correction / errata / system error

When a Character state is invalid because of data corruption, implementation error, rule correction, source reconciliation, mistaken charge, or governed errata, the Character is made whole. The correction has no punitive fee and restores/refunds actual overcharges or invalid purchases as required.

A player is not penalized because the system or source data was wrong.

### CAB/legacy migration

Migration reconciles a Character created under older AP/XP/tier/pricing structures with the final CAB economy. It is a one-time governed transition, not a recurring shopping opportunity.

## Dependency cascade

Removing or replacing an advancement requires a dependency plan before commit.

The system must identify:

- direct dependent Abilities/nodes;
- tier access that would become unsupported;
- Skills/Knowledges/Proficiencies/Attributes whose only source is being removed;
- grants and replacements downstream;
- forms/dependencies/relationships affected;
- currently equipped/readied/current-state references;
- acquisition eligibility that may close.

A respec cannot silently leave an impossible Character state. The proposal must remove/replace dependents, preserve them through another valid requirement path, or block the respec until the dependency is resolved.

## Refund ledger

Refund is based on **historical actual XP debit**, not current RAV and not necessarily the current list price.

A receipt records:

- removed advancement stable/source-qualified identity;
- original purchase receipt/version;
- original actual XP debit;
- refund amount;
- dependencies removed/replaced/preserved;
- new purchases/debits, if any;
- before/after XP balance and Character version;
- reason/workflow type;
- GM/Campaign authority when required.

## Repricing after purchase

### Price increases

A later increase in an Ability/tier/Attribute/Skill price does **not** create retroactive XP debt. The existing purchase remains historically valid unless the mechanic itself is corrected for balance/safety. Future purchases use the current price.

### Price decreases

A later decrease does not silently inject XP into every Character. If a migration/correction policy explicitly normalizes historical purchases, it may issue a credit with a receipt. Otherwise historical debit remains historical.

This avoids constant ledger churn from ordinary calibration changes.

## Legacy CAB migration policy

For the planned CAB transition:

1. reconstruct paid advancement from authoritative receipts where available;
2. use source-qualified identity because CAB-11 found file-local Record_ID collisions;
3. validate current choices under CAB eligibility/prerequisite/tier/acquisition rules;
4. translate AP-only references into their supported XP/grant/tier semantics without creating AP debt;
5. calculate CAB price for retained paid advancement for migration comparison;
6. when authoritative evidence proves the Character **overpaid** under a conflicting legacy price, credit the difference;
7. when CAB price would be higher than the historical valid payment, **do not create negative XP or retroactive debt**; grandfather the paid purchase and record the delta for provenance/RAV/balance review;
8. zero-debit grants remain zero-debit and refund zero;
9. invalid/unresolvable choices are routed to correction/replacement with player/GM visibility rather than silently deleted;
10. append a migration receipt; never rewrite old receipts.

## High-risk mechanic correction

If CAB-22 changes the *mechanic* of a high-risk Ability rather than merely its price, owners must receive a governed correction choice appropriate to the change: retain the corrected version, replace/respec it, or receive the actual paid XP back. No player is forced to keep a materially different purchased mechanic without a correction path.

## Adopted decisions

Under standing owner delegation:

- voluntary respec is Campaign-governed, not at-will by default;
- permitted voluntary respec refunds 100% of actual paid XP for removed paid advancement;
- free grants/RAV refund 0;
- correction/system error is nonpunitive and makes the Character whole;
- repricing upward creates no retroactive debt;
- repricing downward creates no automatic credit except through explicit migration/correction;
- CAB migration credits proven overpayment but grandfathers valid underpayment instead of creating debt;
- dependency cascades and append-only receipts are mandatory.

No delegation guardrail triggered.

**Successor:** CAB-20 — Integrated Advancement Balance Model.