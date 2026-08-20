# ICF-07 — Creature Harvest, Butchery & Biological Ingredient System

**Status:** implementation candidate  
**Authority:** ICF-07 only  
**Upstream:** ICF-02 schema; ICF-03..06 ingredient libraries; canonical creature Bible; MIB-12 deterministic owner-domain patterns  
**Reserved downstream:** ICF-08 part-effect taxonomy/affinity grammar; ICF-09 creature-catalog crosswalk; ICF-10 processing lineage

## Purpose

ICF-07 defines a deterministic, provenance-bearing orchestration model for turning an **authored creature harvest opportunity** into canonical ingredient/material output intents without inventing anatomy, loot, edibility, legality, cultural acceptability, yields, or magical effects.

The canonical creature Bible authorizes creature records to carry biology/resources and **“loot or harvest references where authored”** and explicitly says incomplete creatures remain coverage gaps rather than fabricated lore. Absence of authored harvest evidence is therefore a hard fail-closed condition.

## Authority boundaries

- Creature definition/biology/authored harvest references: canonical creature content domain.
- Creature instance state/version and renewable-resource depletion: caller-supplied creature-instance owner domain. ICF-07 creates no parallel creature-state store.
- Inventory/output truth: **D17 Asset Instance**.
- Stable operation identity, expected-version gates, durable receipts, replay/status-before-retry: reuse MIB-03/MIB-12 patterns.
- Current price/market scarcity: **MIB-13**.
- World/Branch/Reality identity: **MIB-11**.
- Part-effect tendencies: **ICF-08**.
- Mass creature-to-harvest mapping: **ICF-09**.
- Tanning/rendering/drying/fermenting/distilling and other processing: **ICF-10**.
- Alchemical/cooking effect grammar: **ICF-11/12**.

## Governed harvest profile

A profile references a creature definition and evidence; it never substitutes for the creature record. It may contain only explicitly authored/configured:

- modes: `renewable-live`, `nonlethal-extraction`, `postmortem-harvest`, `butchery`, `salvage`, `other-authored`;
- output slots referencing canonical `ingredient:*` or `material:*` definitions;
- anatomy/part/harvest evidence references;
- skill, knowledge, tool, workstation/facility, environment and preservation requirements;
- eligibility predicates;
- deterministic yield rules (`fixed`, `outcome-table`, or a controlling source-table reference);
- quality/condition rules;
- contamination, damage, cause-of-death, elapsed-time and preservation modifiers;
- restrictions for protected status, legality, taboo, food safety, disease, sentience/sapience concerns, cannibalism, consent, faction/campaign rules, or GM adjudication.

Generic biological common sense is not evidence.

## Harvest opportunity snapshot

The caller supplies a versioned snapshot containing creature instance ID, canonical creature definition reference, owner-domain reference and expected version, life/capture state, visible condition facts, elapsed-time facts where relevant, depletion/reservation state, applicable world/reality scope, permission-visible knowledge, and harvest-profile reference. ICF-07 never infers hidden anatomy or secret GM facts from a name.

## Deterministic resolution order

1. Validate profile identity, creature-definition match and evidence status.
2. Validate expected creature-owner version.
3. Validate requested mode is explicitly allowed.
4. Validate life/capture state and authored eligibility predicates.
5. Apply hard restrictions and GM/human stop rules.
6. Validate skill/knowledge/tool/workstation/environment requirements.
7. Resolve the supplied deterministic procedure outcome.
8. Resolve each output slot through its explicit yield rule.
9. Apply only explicit condition/cause/time/preservation modifiers.
10. Resolve quality/condition only from explicit rules.
11. Produce source-owner reservation intents, not output Assets.
12. After durable source-owner reservation receipt, bind D17 output creation to that receipt and its resulting source-owner version.
13. Reconcile the durable D17 receipt and emit source-owner finalization.
14. After ambiguous/lost responses, query owner status before retry; replay durable receipts and fail closed on conflicting same-idempotency receipts.

## Two-owner commit protocol

Harvesting can change both creature-instance state and inventory state. ICF-07 therefore orchestrates:

**plan → source-owner reservation → D17 output commit → source-owner finalization**

Source reservation prevents the same milk/egg/venom/organ/carcass slot from being harvested twice. D17 output creation is one idempotent commit for all outputs produced by the resolution. If D17 fails before a durable output receipt, the source reservation can be released using the post-reservation source-owner version. If D17 succeeds but finalization response is lost, recovery queries both owner domains and finalizes from the durable D17 receipt; it never recreates output.

No output is real until D17 returns a durable receipt. No source depletion is final until the creature owner returns finalization. This follows the MIB-12 rule that durable owner receipts, not guessed future versions, bind later mutations.

## Yield and quality

There is no universal body-size, body-weight, “one heart per creature,” meat-per-weight, or similar formula. Quality likewise has no implicit biological defaults. Procedure outcome, source condition, cause, elapsed time, contamination, preservation and damage can change quantity/quality only when the profile contains an explicit rule. Missing rules produce `unknown`/no modifier rather than an invented value.

## Restrictions

A biological creature is not automatically edible, useful, legal, safe or culturally acceptable. Restrictions are governed data and may block, warn, or require GM/human adjudication.

## Nonstandard creatures

Profiles can describe elementals → essence/crystal/residue, oozes → biomass/acid/slime/core, plant/fungal creatures → botanical/fungal parts, constructs → salvage, undead → bone/ectoplasm/reagents, and alien/reality-specific outputs **only when authored**. These are profile capabilities, not automatic type-wide loot tables. Type/part effect tendencies remain ICF-08.

## Renewable/nonlethal harvest

Milk, eggs, wool, hair, feathers, venom, silk, honey, controlled blood, secretions, shed scales/skin, antlers, spores and similar outputs are supported only when the profile supplies authored evidence plus depletion/recovery rules. The source owner controls cooldown/recovery state; wall-clock time is not progress by default.

## Required proof fixtures

ICF-07 must prove: authored renewable harvest succeeds; stale source versions reject; missing requirements reject; missing anatomy/harvest evidence fails closed; an ICF-06 Phoenix Feather-style ingredient identity does not authorize harvesting it from a creature; explicit elapsed-time rules can degrade/block postmortem harvest; restrictions can block otherwise valid work; D17 failure leaves no durable output and permits reservation release; lost D17 responses query D17 before retry; and lost source-finalization responses after a durable D17 receipt never duplicate output.

## No migration/provider decision

This is a governed rules/orchestration contract. It requires no new durable persistence choice, does not reserve migration `0022`, and selects no production database, AI, search, payment or other provider.

## Completion invariants

- no anatomy/output inferred from creature name/type alone;
- no automatic edibility/usefulness/legality/cultural acceptability;
- every output points to a canonical ingredient/material definition;
- every source-specific anatomy/harvest assertion has provenance;
- source-owner mutations are expected-version gated;
- D17 remains output truth;
- durable source reservation precedes D17 output creation;
- D17 output creation is idempotent/replay-safe;
- owner-status lookup precedes retry after ambiguous response;
- repeated requests cannot duplicate renewable or postmortem outputs;
- quality/contamination/time/cause/preservation effects are explicit-rule-only;
- ICF-08 affinity grammar, ICF-09 mass crosswalk and ICF-10 processing are not implemented here;
- no migration `0022`.