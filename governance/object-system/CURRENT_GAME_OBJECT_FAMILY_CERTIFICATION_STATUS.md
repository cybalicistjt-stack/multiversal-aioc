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

## Next family

Protection: armor, shields, powered armor and EVA suits, followed by EVA modules.
