# APW-07 — Persistence, Recovery, Security and Hybrid Acceptance Architecture

**Work item:** APW-07  
**Attempt:** APW-07-attempt-001  
**Status:** design-complete candidate; exact-head repository validation required  
**Owner/final authority:** John Brandon Turner  
**Scope:** design/governance only; no application implementation or migration is activated by this document.

## 1. Decision

APW uses one authoritative persistence/history model across Personal, Campaign and Session contexts and across live, asynchronous and hybrid cadence. It does not create a second asynchronous database, an offline authority engine, or a parallel synchronization protocol.

The controlling recovery chain is:

`local draft → stable operation/command identity → authorization/version validation → owning-domain transaction/Event → durable operation status → role-safe projection/notification → reconnect/status/Event-gap recovery`

A client may cache authorized projections and local drafts. A client may never manufacture authoritative acceptance, Event ordering, Campaign history, GM decisions, resource spending, or canonical content while disconnected.

The APW-07 completion target is therefore not “everything works offline.” It is:

- accepted effects happen at most once for one user intent;
- stale state cannot silently overwrite newer state;
- ambiguous network failures are resolved by status lookup rather than blind retry;
- permission/entitlement changes are re-evaluated before protected restoration or mutation;
- notifications, counts, history, diagnostics and assistant context cannot leak protected existence/cardinality;
- live and asynchronous cadence share one coherent Campaign identity and authoritative history;
- local/offline creator work remains recoverable without being confused with authoritative state.

## 2. Existing recovery foundation reused

APW-07 extends, rather than replaces, the existing Internal Alpha recovery contract represented by MV-IA-F021 and related proposal/approval contracts.

The implementation handoff must reuse the established concepts:

- `LocalDraftEnvelope` — device/local recoverable editing state, never authoritative;
- `ClientOperationId` / stable command identity — retries for one intent reuse one ID;
- expected authoritative versions / optimistic concurrency;
- authoritative save/decision receipts;
- durable command/operation status lookup;
- `EventCursor` / last acknowledged authoritative sequence;
- Event-gap recovery or verified projection/checkpoint recovery;
- selected-context revalidation;
- permission, entitlement, pack/schema and lifecycle revalidation;
- `ConflictRecord` and safe comparison projections;
- bounded read-only offline snapshots;
- deterministic interruption/failure-injection fixtures;
- privacy-safe recovery diagnostics.

APW-07 does not authorize broad offline authoritative mutation, peer-to-peer authoritative synchronization, last-write-wins governed state, or silent multi-writer merge.

## 3. Persistence/data-contract delta map

APW-07 defines semantics required across APW. Exact implementation schemas remain an APW-08/application concern.

### 3.1 Personal drafts and creator work

Personal drafts may persist locally and/or through already-governed server-side Personal/authoring persistence when connected.

Required properties:

- stable subject and Personal/project context;
- stable draft/creative object identity;
- base authoritative/server version when applicable;
- device-local revision identity;
- schema version and source/version provenance;
- explicit sync/reconciliation state;
- no label suggesting a local draft is submitted/accepted/published;
- conflicts preserve both recoverable sides until disposition.

### 3.2 Asynchronous Action/proposal operations

APW-02 proposal identity remains the durable delayed-interaction record. APW-07 requires:

- one stable proposal/operation identity per submit intent;
- immutable submitted evidence/version;
- expected Campaign/actor/target versions where required;
- durable `pending`, `clarification`, `resolved`, `denied`, `withdrawn`, `stale`, `forbidden` or equivalent status;
- a single attributable authoritative result;
- a decision receipt referencing the original proposal identity;
- status lookup after disconnect/ambiguous response;
- reauthorization before decision and before any resulting authoritative mutation.

### 3.3 Campaign Activity/downtime

APW-03 activity operations require stable activity identity and versioned progress. Long wall-clock delay does not itself advance Campaign state.

Resource-consuming activity must use owning-domain reserve/commit/release or equivalent saga semantics. Expiry/cancellation rules are explicit per activity; they are not inferred from inactivity alone.

### 3.4 Creator Workshop / Sandbox

APW-05 reusable assets and save-out/import/instantiate/propose operations use stable operation IDs and exact source versions. Sandbox state remains noncanonical. A failed or ambiguous save-out cannot create two reusable assets from one intended operation.

### 3.5 Shell, notification and attention projections

APW-06 shell/attention data is projection state, not source authority. Durable notification/attention records, where implementation needs them, reference authoritative operations/outcomes and contain only role-safe metadata.

A notification delivery acknowledgement does not acknowledge, accept or undo the underlying business operation.

## 4. Stable operation identity and idempotency

### 4.1 Core rule

**One user intent → one stable operation ID.**

Retries caused by timeout, reconnect, refresh, duplicated UI event or second-device status uncertainty reuse the same operation identity when they represent the same intent.

A materially new user intent requires a new ID.

### 4.2 Server behavior

For an operation ID already known to the authoritative service, a retry must return the existing status/result or a safe status reference. It must not apply the business effect again.

Duplicate transport requests may occur. Duplicate accepted business effects may not.

### 4.3 Operation families

The rule applies at least to:

- async Action/proposal submit;
- clarify/resubmit version creation;
- GM approve/deny/modify-and-approve decision;
- withdrawal/cancellation where allowed;
- Campaign Activity/downtime submit/progress/complete/cancel operations;
- resource reservation and commit/release operations;
- reusable-asset save-out/import/instantiate/propose operations;
- notification acknowledgement/preferences changes when persisted;
- authoritative shell/context changes only where those changes themselves are server mutations.

Local UI navigation and read-only projection fetches do not need business-effect idempotency, though requests may still carry correlation IDs.

## 5. Expected versions, stale state and conflicts

Every mutation that depends on mutable authoritative state carries the expected version, revision token or equivalent domain-owned precondition.

If the current version differs:

- no silent overwrite occurs;
- operation status becomes stale/conflict/review-required as appropriate;
- the user receives a safe current projection or conflict summary;
- the original draft/proposal intent remains recoverable;
- automatic merge is limited to explicitly commutative/schema-approved fields;
- game judgment, ownership, resource or hidden-information conflicts never use generic last-write-wins.

A stale proposal may remain durable historical evidence even when it can no longer be accepted as originally submitted.

## 6. Authoritative ordering and one Campaign history

### 6.1 Cadence is not history authority

Live, asynchronous and hybrid are cadences over the same Campaign. Switching cadence does not fork Campaign identity, duplicate a Campaign ledger or create a second Event stream.

### 6.2 Ordering rule

Authoritative ordering comes from the owning service/domain transaction/Event sequence, not:

- client clock;
- notification delivery time;
- wall-clock draft creation time;
- device arrival order;
- UI list position.

### 6.3 Interleaved live/async operations

When an async operation is pending and live play changes relevant state:

1. the live operation commits normally if authorized;
2. the pending async record remains durable;
3. decision/commit later re-checks current versions/authority;
4. incompatible async work becomes stale/review-required rather than overwriting live state;
5. if compatible, the owning domain may accept it once and append one authoritative result;
6. all clients recover from the same resulting Event/history order.

### 6.4 Event gap recovery

A reconnecting client presents its last acknowledged authoritative cursor. The service provides authorized Events after that cursor or a verified replacement projection/checkpoint when a direct gap cannot be safely replayed.

Events are applied once. Cursor advancement happens only after successful role-safe application/acknowledgement.

## 7. Ambiguous failure recovery

An ambiguous failure occurs when the client cannot determine whether an authoritative request reached or committed on the server.

Required client state is `status unknown` / `checking result`, not an invented success or failure.

Recovery flow:

1. preserve operation ID and payload/result digest metadata;
2. reconnect/reauthenticate;
3. revalidate selected context;
4. query authoritative operation status using the same ID;
5. if status is committed, fetch permitted receipt/Event/projection;
6. if rejected/stale/forbidden, show the role-safe result;
7. if pending, continue waiting without resubmitting a new intent;
8. if truly unknown and the server declares retry-safe, retry with the same ID;
9. if recovery cannot determine a safe path, enter `recovery-required` and provide issue/diagnostic receipt.

Blind generation of a new operation ID after timeout is prohibited.

## 8. Durable notification semantics

Notifications and attention surfaces exist to help users discover durable state. They are not the state itself.

### 8.1 Durable categories

APW-06 categories remain controlling:

- decision-required;
- result-ready;
- waiting/pending;
- stale/recovery-required;
- informational;
- creator-advisory.

### 8.2 Required durability

If a proposal/result/activity state must survive a user disconnect, the **underlying operation/outcome** is durable. Notification delivery may be retried or reconstructed from that durable state.

Where a durable notification record exists, it must contain:

- stable notification/attention ID;
- subject/recipient scope;
- safe context reference;
- category;
- source operation/result reference;
- created/current status;
- preference/delivery state;
- no unauthorized payload or hidden cardinality.

### 8.3 Delivery failure

Failure to deliver a notification:

- never rolls back the accepted game/authoring operation;
- never causes the operation to execute again;
- leaves the result discoverable through authorized inbox/history/status surfaces;
- may create a delivery diagnostic/attention state without exposing protected content.

## 9. Permission/delegation changes during delayed work

Authorization is evaluated at least at submission where relevant and again immediately before authoritative decision/mutation.

### Revoked after draft, before submit

- local draft may remain recoverable according to privacy policy;
- submission is denied if current authority no longer permits it;
- protected current state is not restored merely because the draft once referenced it.

### Revoked after submit, before GM decision

- original submitted evidence may remain durable for audit/history if policy permits;
- the decision engine re-checks current subject/actor/control/target authority;
- an operation that is no longer legal becomes forbidden/stale/cancelled/review-required as owning domain dictates;
- no prior permission snapshot grants perpetual mutation authority.

### GM/delegation revoked while item awaits review

- the former reviewer loses queue/detail access on next authorization check;
- cached labels/counts/details are not reused;
- another currently authorized reviewer may act only through normal authority.

### Permission change after commit

- committed history is not erased;
- future projections filter the history to the user's current visibility;
- notification/search/history cardinality cannot reveal newly hidden entries.

## 10. Entitlement change behavior

Entitlement is re-evaluated at context restore, protected content access and operations whose legality depends on entitled content.

An entitlement loss does not rewrite accepted Campaign history. It may restrict:

- future content browsing/use;
- opening a reusable definition outside an already-governed Campaign binding;
- creating new work requiring unavailable content;
- export or reference details beyond current entitlement.

Role-safe historical outcomes remain available only to the extent the current authority/entitlement contracts permit them.

Local/offline snapshots never extend entitlement indefinitely. Expiry/reconnect triggers entitlement revalidation.

## 11. Hidden-information nonleakage

D05/APW-06 visibility filtering happens **before**:

- notification generation and notification counts;
- GM/Player queue counts;
- search/autocomplete;
- recent/history lists;
- related-work or Campaign-usage projections;
- diagnostic/export payload construction;
- conflict comparison projections;
- offline snapshot issuance;
- assistant/AI context;
- telemetry fields that could reveal protected labels or cardinality.

### Cardinality rule

If the existence or number of hidden records is protected, the system cannot expose a raw total and merely hide their labels. Counts are computed from the authorized projection.

### Revocation rule

After visibility/permission revocation, cache and reconnect behavior must not resurrect prior hidden labels, previews, attachments, counts or search tokens.

## 12. Cross-device behavior

### 12.1 Authority source

No device is authoritative. The server-side owning domains and Event/history records are authoritative.

### 12.2 Device-local drafts

Two devices may hold different local drafts. They retain distinct local revision/device metadata and share stable server/base references where applicable.

A device-local draft does not silently overwrite another device's draft or current authoritative object.

### 12.3 Same intent on two devices

If both devices submit the same logical operation through the same recovered operation ID, idempotency returns one result.

If they represent separate user intents, they receive different IDs and normal version/conflict rules decide legality/order.

### 12.4 Context cache isolation

Switching device or context requires fresh authorization of:

- Personal/Campaign/Session selection;
- contextual role/delegation;
- Character control;
- entitlement;
- visibility classification;
- operation/queue access;
- offline snapshot validity.

No device may infer current access from an old UI cache alone.

## 13. Long-delay behavior

Delay itself does not create authority or state progress.

After long delay, before mutation/decision the system rechecks:

- subject/session validity;
- Campaign membership/control/delegation;
- expected versions;
- object lifecycle;
- entitlement/pack/schema requirements;
- resource reservation status/expiry;
- explicit activity/proposal expiry policy;
- target visibility.

Expired or stale work remains inspectable only through safe authorized history/draft views and can be copied/resubmitted as a **new intent** when allowed.

A new intent receives a new operation ID; the old historical record is not mutated into the new submission.

## 14. Offline boundary

APW-07 preserves the Internal Alpha bounded-offline rule:

- authorized read-only snapshots may exist with explicit expiry;
- approved local draft families may be edited offline;
- authoritative mutation controls remain disabled offline;
- offline snapshots contain only already-authorized projections;
- reconnect revalidates permissions, entitlement, pack/schema/lifecycle and versions;
- local drafts reconcile, branch or become conflicts;
- an offline snapshot never overwrites current authoritative state.

Broad offline authoritative play remains separately deferred.

## 15. Live → async → live continuity proof

The canonical hybrid proof is:

1. two users are in one Campaign with contextual GM/Player authority;
2. live play reaches authoritative Event sequence `N`;
3. the Campaign moves to asynchronous cadence without changing Campaign identity;
4. Player submits one delayed Action/proposal with stable operation/proposal ID and expected version;
5. Player disconnects;
6. unrelated compatible Campaign work may occur and append authoritative Events;
7. GM later opens the authorized durable inbox and revalidates current state;
8. GM resolves the proposal exactly once;
9. owning domain appends one authoritative result/Event or returns stale/review-required without partial mutation;
10. result-ready state is discoverable even if notification delivery fails;
11. Player returns on the same or another device and performs status/Event-gap recovery;
12. current permission/entitlement/visibility is applied before result/history projection;
13. Campaign resumes live cadence from the same authoritative Event/history sequence;
14. no duplicate Campaign, forked history or second rules engine exists.

## 16. Recovery status model

APW-07 standardizes the UX meaning, not necessarily one global database enum, for:

- `local-draft`;
- `queued/submitting`;
- `submitted/received`;
- `validating`;
- `pending-review`;
- `accepted/committed`;
- `modified-and-accepted`;
- `rejected/denied`;
- `withdrawn/cancelled-before-acceptance`;
- `stale/conflict`;
- `forbidden/revoked`;
- `entitlement-restricted`;
- `status-unknown`;
- `recovery-required`;
- `reconciled`.

Owning domains may use more specific states, but the shell must not collapse meaningful distinctions such as `local draft`, `submitted`, `accepted` and `displayed result`.

## 17. Security and privacy requirements

APW-07 requires:

- server-side authorization on every protected mutation and projection;
- no trust in client role flags or cached context;
- no sensitive data restoration solely from client snapshots;
- integrity/version checks on offline/cache manifests;
- safe purge/lock behavior after revocation as implementation policy dictates;
- privacy-safe diagnostics using stable IDs, status classes and digests instead of raw protected payloads;
- no secrets/tokens in exports, notification payloads or issue receipts;
- no optional AI access to hidden cache, conflict payload or unfiltered Campaign history;
- no security claims based on Spoiler Shield.

## 18. Export and diagnostics

### User/support recovery receipt

A safe recovery receipt may include:

- recovery/operation ID;
- context type and opaque/stable authorized identifier;
- client/app/schema version;
- last acknowledged Event sequence;
- status category;
- expected/current version identifiers where safe;
- timestamps;
- correlation IDs;
- integrity/result digests;
- retry/status-lookup history;
- privacy-safe error class.

It must exclude unauthorized game content, secrets, private notes and credentials.

### Provider-exit/export

Export must preserve attributable history/provenance under existing provider-exit contracts while applying current authorization. Export failure cannot mutate source state.

## 19. Accessibility and recovery UX

All recovery/conflict/status/history behavior must have equivalent:

- keyboard;
- touch;
- screen-reader;
- reduced-motion;
- mobile/narrow-screen;
- nonvisual status descriptions.

Users must be able to tell:

- whether content is a local draft or authoritative;
- whether a submission is pending, accepted, rejected, stale or unknown;
- what context they are in;
- whether permissions/entitlement changed;
- whether data is offline/cached and its expiry;
- what safe action is available next.

Conflict resolution cannot require drag-only interaction or color-only comparison.

## 20. Performance and zero-paid-service acceptance

APW-07 does not invent new fixed latency targets. Implementation acceptance must use existing application performance budgets and prove that recovery does not introduce unbounded work.

Required evidence includes:

- bounded status lookup by stable operation identity;
- bounded Event-gap or checkpoint/projection recovery;
- paginated/filtered history and queues;
- authorization filtering before expensive aggregation;
- bounded offline snapshots;
- deterministic test execution without paid services;
- local/self-hosted-compatible diagnostics and fixtures;
- no paid notification, synchronization or AI dependency required for core acceptance.

## 21. Failure philosophy

When certainty is unavailable, preserve evidence and surface uncertainty.

Prefer:

- `status unknown` over guessed failure;
- `stale` over silent overwrite;
- `conflict` over last-write-wins;
- `forbidden` over cached access;
- `pending` over duplicate submit;
- `recovery required` over destructive reset.

Accepted authoritative history is not destructively rolled back merely to make a client projection easier to reconcile.

## 22. Deterministic fixture families

The companion acceptance matrix includes at least:

- duplicate submit before/after commit;
- ambiguous network failure before response;
- Event committed but notification/realtime missed;
- live mutation while async proposal waits;
- stale GM decision attempt;
- role/control/delegation revocation before decision;
- entitlement loss before return;
- hidden-count/search/history leakage attempts;
- second-device same intent;
- second-device distinct conflicting intent;
- long-delay reservation expiry;
- offline draft rebase/conflict;
- offline snapshot expiry/revocation;
- service restart/Event-gap recovery;
- notification delivery failure with durable result;
- live→async→live one-history proof;
- cross-context cache isolation;
- export/diagnostic privacy;
- no-AI/zero-paid-service operation;
- keyboard/screen-reader/mobile recovery parity.

## 23. APW-08 handoff

APW-07 hands APW-08:

- persistence/data-delta requirements;
- stable operation/idempotency rules;
- expected-version/conflict rules;
- Event/history ordering requirements;
- durable notification reconstruction rules;
- permission/entitlement revocation behavior;
- offline/cross-device/long-delay boundaries;
- security/nonleakage invariants;
- hybrid live→async→live proof;
- deterministic fixture inventory;
- implementation touchpoint requirements without activating them.

## 24. Completion boundary

APW-07 may be `completed_verified` when this bounded design package, matrices and review receipt pass exact-head AIOC repository health and merge.

That status means the **architecture and acceptance design is ready**. It does not mean application persistence, recovery, migration, notification delivery or hybrid implementation is complete.

APM-06 is selected only after APW-07 completion evidence is recorded. APW-08 remains after APM-06 in the owner-approved interleave.
