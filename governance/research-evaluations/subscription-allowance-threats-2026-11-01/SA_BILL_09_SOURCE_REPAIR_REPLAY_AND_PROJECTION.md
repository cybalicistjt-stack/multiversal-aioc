# SA-BILL-09 — Session Replay and Projection Source Repair Study

**Scope:** Security research on pinned Multiversal-app lower-level TypeScript functions. **Do not treat this as an application patch, live threat mitigation, shipping feature, billing authorization, or security certification.** Continuation of SA-BILL-08 under OPS5 session-scoped research-evaluation authority.

## Pinned actual source

Reuses verbatim Git-blob-pinned app source in `tests/fixtures/sa-bill08/app-src`: authorization `b7b038b63774b7e4e8c1deb72c9ed09d35bc48b6`, event filter `d948d92c06560fb9a560fcf4325ba4a258216e2a`, command handler `8b0ec123e99ccbbfc00fdc0c4e1e38aa42c71656`. The test verifies these blobs before any temporary transformation. Node's import-extension rewrite is applied only to throwaway execution copies. If the app main changes, this historical test does not certify the new version.

**Test-first RED evidence:** The same fifteen desired-security-semantic tests were run against unmodified pinned source on PR #1925 at head `08e6f2a359c6ae45f87d480cb8e0ccc4cbf19e3c`, Operations V5 run **41393073601**. Exact log reported **8 passed, 7 failed**: SA09-02/03/04/05/06/08/10. The failing cases were behavior assertions, not loader or fixture setup errors. This supports actual source-function gaps, not proof of reachable live endpoints.

**GREEN candidate (research only):** `tests/control_plane/sa_bill09_source_patch.mjs` applies strictly anchored, fail-on-drift edits only to temporary copies of pinned original source; `tests/control_plane/test_sa_bill09_source_repair.mjs` runs the **same 15 tests** with `SA_BILL09_MODE=fixed`. The exact-head GREEN workflow result must be checked before claiming a validated patch proposal. The unmodified app source has NOT been changed.

## Defect, minimum research repair, full-product implications

| ID | Source observation (verified RED) | Test-only proposed repair | Real production prerequisite |
|---|---|---|---|
| SA09-REPLAY-ROLE | `handleAuthoritativeSessionCommand` returns an existing receipt for processed command ID before `authorizeCampaignRequest`, including with missing membership | Move current authorization ahead of all replay handling | Prove current authoritative A3 subject/session, A5 membership revision, command ownership; forbid using client-supplied context |
| SA09-REPLAY-BINDING | Replayed `commandId` may return an unrelated `existingReceipt`; actor/payload changes are not checked | Require matching `receipt.commandId`, accepted status, valid revision, persisted `originalAcceptedCommand`, and identical serialized command body; fail closed otherwise | Server-owned immutable command ledger with *canonical cryptographic command digest*, actor/session/permission epoch; exact `JSON.stringify` matching is a conservative research-only approximation that may reject JSON objects with equivalent key orders, and is not a production hash design |
| SA09-PUBLIC-PAYLOAD | Generic command handler makes a `public` Session Event containing raw `commandPayload` | Omit `commandPayload` from public accepted event while retaining command ID/type/actor and event sequence | Inspect every reducer/state-sync consumer of event payload; split private execution data from minimal public acknowledgments; ensure hidden events have correct visibility per event type, preserve legitimate state computation |
| SA09-HIDDEN-COUNT | Generic `filterSessionEventsForViewer` reports hidden event cardinality to otherwise-authorized Players | Remove `hiddenEventCount` from general projection; A9 wrapper continues omitting it | Reconcile generic callers, UI counters, checkpoint/count ordering and no hidden-ID/count side channels across WSS/REST/A9/AI |

**No false replacement claim:** simply moving an authorization call does not prove the authentication session or Campaign membership is real, recent, or server-issued. A pure function cannot cryptographically verify its passed `context`. The reference implementation does not produce payment-provider verification, device-bound entitlement, database uniqueness, signed offline leases or external source-epoch fencing.

**Conservative compatibility warning:** this proposed change removes a field (`hiddenEventCount`) and removes raw command payloads from a formerly publicly visible event. These are intentional security contracts but could break event sourcing, replay, UI or external API consumers. Before any authorized Multiversal-app implementation, inspect callers and serialized fixtures across the app, write migration/compatibility tests, preserve authorized private state transitions, and do not automatically make all command events GM-only (which may break legitimate Player sync).

## Additional test result semantics

- **SA09-01:** verify exact source Git blobs, not only file path names.
- **SA09-02–07:** reauthorization, receipt/original command binding, legitimate idempotent replay after fresh membership.
- **SA09-08–09:** generic accepted public event and A9-safe projection exclude confidential command body.
- **SA09-10–12:** generic and A9 hidden-event projection have zero hidden cardinality, continue role-visible events for authorized GM.
- **SA09-13–15:** no untrusted viewer/cross-session access; ordinary command revision/receipt semantics and wrong-session denial remain intact.

## Highest-priority integration gaps after GREEN

1. **Authorized app source patch** under selected product implementation authority and fresh app-main diff; preserve direct event reducers and lower-level private payload processing. Do not merge merely because research mirrors are green.
2. **Live PCV-03F service**: authenticate A3 subject + registered device and current Session membership before any command status/receipt; bind `commandId` to actor, session, payload digest and owner-authorized revision; do not allow replay across subject/role/device contexts. Test concurrent request vs GM revocation and delayed WSS delivery.
3. **Actual WSS and search/AI/export**: malicious replay must not leak timing, counts, payload, private source provenance, or protected Campaign dependencies. Denial before serializing any secret.
4. **Real billing allowance**: remain subject to validated provider-paid GM, Campaign Player membership, one transactionally-enforced slot, registered root and dependency rights, source-epoch revocation and transfer quarantine.
5. **Native offline**: no authenticated online action from merely cached grant; bounded crypto lease with a documented disconnected revocation residual risk; installed Android/Windows two-device acceptance.

## Governance and proof boundary

This work modifies only AIOC research files, added tests, and its Operations V5 test invocation. **No changes** to `Multiversal-app` product source, `operations/CURRENT.json`, GPR PCV-03F, MTLC-14, AXI-01, prices, live subscriptions, allowance grants, game canon, deployment or app release. Publication requires exact-head Operations V5 success, checked pinned source, fresh main/queue and protected FIFO merge. SA-BILL-01's 60 hostile end-to-end scenarios remain NOT EXECUTED.
