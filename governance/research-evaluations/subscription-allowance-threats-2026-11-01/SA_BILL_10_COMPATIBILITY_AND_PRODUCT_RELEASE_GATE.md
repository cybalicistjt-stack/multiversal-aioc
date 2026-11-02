# SA-BILL-10 — Legacy Contract Compatibility and Safe External Boundary

**Classification:** research, additive compatibility proof, and product implementation handoff. **Not a deployed security patch or authorization to modify an active product implementation lane.** Source review follows SA-BILL-09, previously published as AIOC PR #1925. No real Multiversal-app source changes, payment operation, subscriber or allowance activation.

## Critical finding: the direct SA-BILL-09 patch is NOT backwards compatible

The previous SA-BILL-09 research proposal changed the *generic* session handler and *generic* event projection directly. Source review of actual application `main` revealed inherited acceptance contracts:

- `fixtures/session/p9-06-016-authoritative-command-handler.json` contains `duplicate-replayed` with `membership` and `existingReceipt`, **not** `originalAcceptedCommand`. The unmodified generic handler accepts/replays that fixture; the proposed direct SA09 patch rejects it as `duplicate-without-receipt`. Production migration must establish real persisted command/actor/digest binding and adjust the relevant acceptance contract with explicit authority rather than silently invalidate it.
- `fixtures/session/p9-06-018-hidden-information-response-filter.json` expects hidden counts from the **generic** viewer filter. The unmodified generic projection returns `hiddenEventCount`. The direct SA09 patch removes it. Hiding that information from *external* viewers is essential, but changing the internal diagnostic projection without a compatibility assessment is unsafe.
- `tools/verify_p9_06_016.py` and `tools/verify_p9_06_018.py` mostly check source markers and a separate Python reconstruction of fixture expectations. Their successful exit is **not a runtime TypeScript test**. The SA-BILL-10 tests execute the original Python verifier scripts on test scaffolding against both original and proposed-patch source. **Both may return green while their actual TypeScript behaviors differ**. This is a verification coverage defect in the current test strategy. Test scaffolding supplies minimal workflow marker files only, so this is NOT the app's whole CI environment.

Source blobs are pinned in `tests/fixtures/sa-bill08/app-src/` and newly pinned historic app verification sources/fixtures in `tests/fixtures/sa-bill10/app-src/`. Tests verify exact Git blobs before running. Historical app `main` is the source for these pins; future app heads must be compared separately.

## Safer staged implementation strategy

**Keep the existing internal contract until consumer migration is explicit.** `tests/control_plane/sa_bill10_safe_boundary.mjs` demonstrates an additive reference *outer* boundary. The lower-level app functions are called exactly as published; external projections exclusively use the existing `projectAcceptedSessionCommandForA9` and `filterSessionEventsForA9` sanitizers.

The proposed external command adapter requires all of the following before calling the lower-level handler:

1. A *server-derived and current* actor, canonical subject/session/campaign match, active member, GM and entitlement revision checks; the test representation uses synthetic `owner` facts, which are NOT authenticated merely by properties or booleans.
2. For processed command retries, a trusted persisted original command and accepted receipt; command, actor, session, type, submitted time and canonical payload digest must bind to the exact authenticated request. The reference model normalizes JSON object keys but **production needs a specified canonical serialization and cryptographic digest**.
3. On denied/unknown identities, do not call the lower-level replay handler or leak command existence. Use a scope-safe denial response. A valid replay remains idempotent, because verified original requests still reach the generic handler with its old accepted receipt contract.
4. Internal accepted command payloads may remain necessary for actual state reducers. Do not simply strip them from durable canonical events until event consumers, recovery/checkpoint state, downstream Combat and PCV-03F reducers are verified. Strip them **before any external serialization**; a safe A9 wrapper exists but real endpoint call-site use is currently unverified.
5. The generic internal hidden-event count is retained for compatibility, while external event projections omit counts and hidden payloads. Use least-privilege API projections; direct access to internal state/handler is prohibited.

The sample external adapter is NOT the actual PCV-03F service and does NOT authenticate producer origin, verify a subscription, implement real database row-level security, enforce registered source-rights closure, issue allowances or manage WSS. It is one candidate policy **only**, not a parallel product authorization authority. The shipped design must use the canonical A3/A5/PCV owner ports and their current role/entitlement revisions rather than accepting the client-supplied `trustedCurrent` or `activeMembership` used in research tests.

## Executable proof

`tests/control_plane/test_sa_bill10_compatibility.mjs` contains 13 cases:
- exact Git pin verification of historical real app sources, fixtures and verifier scripts;
- original existing `duplicate-replayed` fixture passes original handler but not SA09 directly patched handler;
- generic hidden count exists in original and is absent from SA09 patched generic source;
- the existing two Python validators run in a fixture layout on **both** differing variants, exposing static-verifier blind spots rather than claiming product runtime acceptance;
- additive external adapter preserves internal replay and hidden count while preventing external payload/count exposure;
- membership, entitlement epoch, other actor/changed payload/receipt mismatches are denied before lower-level replay;
- normal fresh command still returns correct revision while external payload is excluded.

**Source/test readout is valid only after exact-head Ops V5 run turns green.** CI on this AIOC research branch does not run the full `Multiversal-app` integration test suite or a deployed app.

## Product integration dependency gate — owner action not assumed

Before a production PR merges, the owning product lane must choose how to integrate an external-only adapter into the actual PCV-03F HTTPS command/status/bootstrap and WSS routes, or authorize a breaking change to the old P9 fixtures and all consumers. Run current app TypeScript checks, P9-016/P9-018 verifiers *and* runtime TypeScript replay privacy assertions, PCV-03F service-first reconnect/diagnostic suites, direct API authorization with current A3 subject, GM role and Player membership revocation, serialized bytes inspection, idempotency under auth downgrade, and installed Windows/Android tests where applicable. Verify any stored command digest and source release closure are server owned. No study gate substitutes for owner-authorized paid product policy or release.

**Unselected decisions remain frozen:** billing SKU/price, new grants in trial/grace, GM succession, replacement allowance, offline cryptographic lease, refunds, and data portability rights. Preserve `operations/CURRENT.json` with GPR PCV-03F, MTLC-14 and AXI-01; research evidence cannot retarget active implementation authority.

**Conclusion:** the tested additive boundary is the safer nonbreaking *research* route; the direct SA-BILL-09 generic-source edits are inappropriate for an unreviewed production cherry-pick. Existing static P9 validators alone cannot certify it.