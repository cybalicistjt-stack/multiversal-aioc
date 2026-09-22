# SAA-15 Completion Report

**Status:** `completed_verified`  
**Schema:** `SAA-15.1`  
**Application PR:** #733  
**Causal RED:** run `35711835494`, head `d4311ba8b81e2046dc866b6f203593f958c62159`  
**Validated GREEN:** run `35712776570`, head `11bb3cb975906aa2fd5d185cb30a1a6e02d35a38`  
**Application merge:** `3fc56538791293aea33cea160a3dcc853102d95e`

SAA-15 delivers deterministic panel/page image and multipage-package export metadata with explicit output profiles and exact SAA-11 page/panel ordering. Coordinates and filesystem order are never used to infer reading order.

ARI-11 rights are checked before render/export authorization. Transform and export capability are required for every referenced resource; redistribution capability is additionally required only when the output profile declares redistribution intent. Unknown, denied, revoked, stale, unavailable, incompatible or mismatched rights/resource state fails closed without fabricated permission, rights repair or reference rebasing.

Export does not mutate SAA project history, ARI source resources, derivative provenance, owner-domain truth or rights state. Provider-off local export remains supported.

Two post-implementation validation failures were confined to TypeScript typing of the test fixture itself; production invariants already passed on both. The fixture was repaired without changing SAA-15 production behavior, and the final exact head passed Linux, Windows and deterministic cross-platform comparison.

SAA-16 — Optional Digital-Comic Audio Cue Lane — is selected next but not started.
