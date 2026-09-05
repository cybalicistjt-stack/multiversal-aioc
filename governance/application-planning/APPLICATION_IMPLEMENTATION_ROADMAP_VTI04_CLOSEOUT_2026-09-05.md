# VTI-04 Closeout — Rules Action & Roll Bridge

**Date:** 2026-09-05  
**Work item:** VTI-04  
**Status:** `completed_verified`  
**Application PR:** #418  
**Application merge:** `295424982135337de80cccfac072764ab35183cc`  
**Strict successor:** VTI-05 — Character Sheet, Item & Compendium Projection — `selected_not_started`

## Completed contract

VTI-04 now provides the bounded provider-neutral rules-action and roll bridge promised by the VTI program. External VTTs can form requests for roll, attack, check, power, resource, condition, initiative, reaction and GM-adjudication actions; Multiversal remains the validation, rules-resolution and authoritative-RNG authority; authoritative results/receipts can be projected back for external presentation; duplicate/idempotent requests reuse VTI-03/MIB-03 receipt-replay, status-before-retry and fail-closed behavior instead of resolving twice; and presentation fidelity remains explicit and hidden-information safe.

The tranche did **not** authorize or perform provider-specific schemas, vendor selection/ranking, external rules authority, external RNG authority, autonomous GM adjudication, credential or external-account mutation, adapter implementation, live external synchronization mutation, canonical game-state mutation, durable VTI persistence, new migration, provider activation, tester distribution, release/deployment or VTI-05+ implementation.

## Acceptance RED

Genuine matching RED was sealed from exact application head `c9a3cc09aa9ce6ce2ca55c35df7ba7032ffb7126` in run `33993535896`.

- repository-health selector job: `101379876588` — PASS;
- self-hosted Linux job: `101379894331` — expected FAIL at `vti04-invariants`;
- self-hosted Windows job: `101379894324` — expected FAIL at `vti04-invariants`;
- deterministic comparison job: `101379945379` — PASS;
- deterministic RED receipt: `ee79438a64ccaccabe8acd2953df5f911d1e0ee8b92352952b3026ede1d0e028`;
- expected failure: bounded production contract intentionally absent;
- unrelated historical profile fanout: `0`.

That RED unlocked only `packages/contracts/src/virtual-tabletop-interoperability/rules-action-roll-bridge-contract.ts`.

## Final GREEN

The first production implementation head, `8806fce4a0143281942dd2d68a23301c70501999`, passed run `33994055604` without an application-feature repair.

- repository-health selector job: `101381251547` — PASS;
- self-hosted Linux job: `101381267156` — PASS;
- self-hosted Windows job: `101381267141` — PASS;
- deterministic cross-platform comparison job: `101381348850` — PASS;
- deterministic receipt: `766e06c3f2de74e4cbee599fa56c3d88e4a49fe98481b7f65f70d30a5970050c`;
- unrelated historical profile fanout: `0`.

Application PR #418 was then squash-merged as exact canonical application main `295424982135337de80cccfac072764ab35183cc`.

## Convergence accounting

VTI-04 required two validation-contract repairs during the RED-unlock AIOC transaction and zero application-feature repairs. The second repair correctly entered diagnostic mode. There were no unchanged-evidence reruns, no no-progress cycles and no historical-family fanout.

The original owner `Continue` should have carried through this AIOC closeout and successor selection after the application merge. Execution returned early with that authorized terminal work still pending, so this second owner `Continue` is recorded as a control-plane incident under the execution-termination contract rather than as a normal second-cycle requirement. The corrective rule remains: an ordinary continuation does not terminate at an open PR, CI milestone, application merge or closeout-pending state; it carries through canonical closeout and strict-successor selection unless a genuine blocker exists.

## VTI-05 selection boundary

VTI-05 is selected from exact application main `295424982135337de80cccfac072764ab35183cc` as `VTI-05-attempt-001` and remains `selected_not_started`.

No VTI-05 application branch, acceptance package, production mutation or provider integration is authorized by this closeout. A future owner `Continue` must first governed-start VTI-05 in AIOC; only after that governed-start validates and merges may its registered application branch be created.

VTI-06+, SGC-01+, provider activation, tester distribution, release and deployment remain unauthorized.
