# Current Game-Object Family Certification Status

## Weapons

The current normalized weapon family contains **2,056 objects**: 1,024 melee and 1,032 ranged.

All 2,056 now have:
- complete core attack mechanics;
- complete resource/reload profiles where applicable;
- every source property/effect bound to explicit, peer-derived, rule-derived, constructed, or fail-safe qualitative semantics;
- current runtime truth-owner bindings;
- the A6 atomic action write-set contract.

They stop at `MECHANICS_COMPLETE_OWNER_BOUND_RUNTIME_ADAPTER_PENDING`.

The product does not yet expose a certified generic weapon-property/effect resolver, so this status does not claim runtime execution or GAME_READY.

## Protection / EVA

The current normalized protection family contains **691 objects**:
- 195 armor;
- 48 shields;
- 28 powered armor;
- 25 EVA suits;
- 395 EVA modules.

All 691 now have mechanics/content-complete family profiles and runtime truth-owner bindings. The family pass produced **1,361 inline repairs/constructions** and a **273-entry protection-rule registry**, with **0 remaining family content blockers**.

The eight Magitech armor/shield records that lacked conventional armor-envelope fields received owner-authorized current-rule constructions for AC/category/proficiency and wear-state fields. All 25 EVA chassis now have typed armor, hardpoint, sealed-life-support, environmental, power, compatibility, installation and decompression profiles. All 395 EVA modules now have typed slot, compatibility, activation, power/consumable, installation and failure profiles.

Protection/EVA stops at `MECHANICS_COMPLETE_OWNER_BOUND_RUNTIME_ADAPTER_PENDING`.

The product still needs certified generic protection/effect, protection/environment/EVA-suit, and EVA-module effect/compatibility resolvers before runtime-ready or GAME_READY can be claimed.

## Working-set rule

Use `CURRENT_GAME_OBJECT_NORMALIZATION_AUTHORITY.json` to select the current normalized 21,495-object working population, then apply the current family certification overlays. Earlier P1/CCTI/OGR/FIAA family counts and pilot records are historical/provenance inputs only and must not select the active working population.

## Next family

Computers, computer components, software, computer expansion/modules, and AI-system objects.
