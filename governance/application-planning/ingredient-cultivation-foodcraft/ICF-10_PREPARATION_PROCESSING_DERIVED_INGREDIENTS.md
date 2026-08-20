# ICF-10 — Preparation, Processing & Derived Ingredients

**Status:** implementation candidate  
**Authority:** ICF-10 only  
**Upstream:** ICF-02 schema/lineage; ICF-03..06 primary libraries; ICF-07 harvest boundary; ICF-08 tendency grammar; ICF-09 creature/signature crosswalk  
**Reserved downstream:** ICF-11 alchemical formula/effect grammar; ICF-12 culinary outcome mechanics; ICF-13 production integration

## Purpose

ICF-10 defines a deterministic, lineage-preserving preparation layer between canonical primary ingredients and later formula/recipe systems. The implemented first-party foundation contains **400 derived preparations** across **37 transformation families** and **27 registered processing rules**.

Every preparation is an ICF-02 `derived-preparation` with canonical input definition refs and an explicit transformation rule. Processing does not create a second inventory ledger, current price, creature harvest authority, or World/Reality truth. D17 remains live Asset state; MIB-13 remains current price/scarcity; MIB-11 remains World/Reality authority.

## Deterministic processing boundary

A processing rule defines the kind and identity-preserving transformation semantics. It does **not** provide a universal yield, wall-clock progress rule, shelf life, safety threshold, exact alchemical effect, or recipe outcome. Those values require explicit operation/source rules in their owning tranche.

Implemented families cover milling/flour/meal, starch extraction, spice grinding, drying/dehydration, oil pressing, dairy separation/churning/culturing, wax refining, pickling, malting, juice/syrup/vinegar processing, curing/smoking/salting, stocks, neutral extracts, steam distillates, recovered-solvent tincture concentrates, hide tanning, gelatin clarification, and elemental-ash refining.

## Lineage

Each derived record retains `lineage.inputDefinitionRefs`, `lineage.transformationRuleRef`, and `retain-all-input-lineage`. A live output is still created only through the owning D17 Asset/inventory path. ICF-10 defines reusable preparation identities; it does not mutate live Assets by itself.

## Legacy Animal Leather reconciliation

ICF-05 preserves `ingredient:animal-leather` because the canonical Animal Pen source explicitly names leather as a direct weekly output. ICF-10 **does not silently rewrite or supersede that source-backed identity**. Instead, exact authored hide inputs such as `ingredient:cattle-hide` can produce distinct lineage-bearing preparations such as `preparation:cattle-hide-leather` through `processing:hide-tanning`. The legacy generic direct-output identity remains an explicit compatibility exception until a source-authority migration is separately approved.

## Gelatin and ash boundary

No generic creature bone/connective-tissue anatomy is invented to manufacture gelatin. The library only creates `preparation:arcane-gelatin-clarified` from the already-canonical `ingredient:arcane-gelatin`. Likewise, arbitrary material-to-ash rules are not inferred; ash processing is represented by refining the already-canonical elemental ash inputs.

## Tincture/distillate boundary

Steam distillates treat process water as a non-retained medium. Tincture-concentrate rules explicitly recover/remove the neutral solvent before the output is committed, so retained product lineage can remain bound to the canonical botanical without inventing an unmodeled solvent ingredient. This does not authorize executable alchemical effects; ICF-11 owns those.

## Completion invariants

- 400 ICF-02-compatible derived-preparation definitions, inside the approved 300–500 target;
- every preparation has canonical input refs and a registered transformation rule;
- no universal processing yield/time/tool/facility formula is invented;
- no edibility is inferred from an input or process;
- no exact alchemical or magical-culinary effect is assigned;
- no culinary recipe outcome is assigned;
- D17 remains live Asset authority; MIB-13 remains current price/scarcity authority; MIB-11 remains World/Reality authority;
- ICF-07/09 remain creature harvest/crosswalk authority;
- legacy `ingredient:animal-leather` is preserved rather than silently rewritten;
- migration `0022` is not required.
