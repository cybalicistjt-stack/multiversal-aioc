# PCV-03 Adversarial Candidate Audit — 2026-09-25

**Status:** baseline adversarial pass complete; NOT the final preimplementation gate  
**Audited application candidate:** `8232e52a089360939b17e58229af192a283b3a53`  
**Application PR:** `Multiversal-app#775`  
**Prior exact-head validation:** `36053261478`  
**Prior package artifact:** `10832224601`  
**Scope:** PCV-03 only. PCV-01/02 remain completed_verified. PCV-04+ remain unauthorized.

## Conclusion

The prior automated green run and package build are valid evidence that the candidate builds and that the original focused tests pass. They are **not sufficient evidence that the candidate satisfies PCV-03's authority, recovery, security, transport, or installed-proof contract**.

The candidate must not proceed to physical-device certification unchanged. The physical-proof gate is superseded by a bounded PCV-03 candidate-integrity repair pass. After repair, exact-head automated validation and exact-head Windows/Android packages must be regenerated before the physical proof is run.

This audit does not authorize PCV-04 gameplay/action implementation and does not replace existing A3/A5/Session/SMB owner domains.

## Canonical acceptance used

PCV-03 requires:
- real invitation/join;
- stable subject/device continuity;
- advisory presence;
- ordered Events;
- idempotent commands;
- resume tokens/checkpoints;
- authority epoch;
- hidden-before-publication filtering;
- direct/manual WebRTC zero-service baseline;
- installed Android↔Windows proof;
- phone-capable controls;
- composition of existing A3/A5/Session/SMB authority rather than a parallel owner.

Cross-checks also consumed the current Development Bible security, serialization, data-flow/recovery, local/online-session, testing, and storage rules plus the existing P9-06 two-device acceptance fixtures/contracts.

## Blocking findings

### A. Authority, membership, invitation, and identity

1. **Parallel Campaign membership authority.** `pcv03Session.ts` mints and persists `Pcv03Membership` while also mutating PCV-02 `memberSubjectIds`. This bypasses the canonical A5 Campaign membership/invitation owner instead of adapting it.

2. **Join is not A3 invitation acceptance.** PCV-03 compares `invitationId + raw secret` directly, then creates membership itself. A3's lifecycle semantics—recipient binding, one-time/idempotent acceptance, decline, revoke, inference-safe preview—are not composed.

3. **Accepted invitation remains reusable.** PCV-03 writes `acceptedSubjectId` but never checks it before later acceptance. The same invitation secret can be presented again by another subject/device.

4. **Peer is not bound to the joined subject.** After a data channel opens, `command.actorId` and presence `subjectId/deviceId` remain caller-supplied. Authorization is evaluated using the claimed actor rather than the authenticated/bound connection identity. A connected member can therefore attempt to act as another active member.

5. **Resume authorization is hard-coded current.** `acceptPcv03Resume` calls the reconnect contract with `membershipActive:true` and `permissionCurrent:true` rather than rechecking current membership/authorization.

6. **Resume device is not validated against registered device continuity.** A valid subject/resume token/epoch can supply a different `deviceId`; the handler does not prove that device is an already-authorized continuity device.

7. **No Campaign membership state transition seam is consumed.** A5 models `active | suspended | left | removed`, but PCV-03 cannot observe/enforce those states through its local membership copy. Revocation/suspension cannot reliably terminate live/resume authority.

8. **Supported role vocabulary is not explicitly adapted.** A5 uses `game-master/assistant-gm/content-creator`; the older Campaign authorization policy uses `gm/player/observer`. PCV-03 currently uses only player/observer but has no explicit fail-closed translation seam for future A5 roles.

### B. Session lifecycle and canonical launch authority

9. **PCV-03 creates a parallel Session owner.** It creates `Pcv03HostSession` directly from PCV-02 Campaign/Scene state rather than consuming the canonical A5 launched Session shell / immutable launch snapshot.

10. **Paused/closed Session state is not enforced.** PCV-03 join, resume, command, and presence paths have no A5 `launched | paused | closed` gate.

11. **Old Sessions remain addressable.** Starting a new host changes the `active-host` pointer but does not close the old Session or revoke its invitations/resume credentials. Old records can continue accepting traffic if addressed directly.

12. **Session replacement/closure does not advance authority epoch or revoke credentials.** The authority epoch is initialized to 1 and never participates in a real lifecycle transition.

13. **Selected Campaign context is ignored when hosting.** `ensurePcv03CampaignContext` returns the first Campaign in the foundation rather than the user's selected Campaign context.

14. **Remote joined Campaign continuity is not integrated into ordinary product context.** The player retains a PCV-03 continuity record, but the joined remote Campaign/Session is not represented as a role-safe selected-context/Home projection after restart.

15. **Client continuity key is only `subjectId`.** Multiple Campaign/Session continuities for one subject collide instead of being keyed by authoritative Campaign/Session identity.

### C. Command and Event authority

16. **PCV-03 accepts arbitrary command types/payloads.** Any `SessionCommand.type` and arbitrary payload can enter the generic authoritative handler. PCV-03 should expose only its bounded session-continuity/proof command schema; PCV-04 owns gameplay/action convergence.

17. **Conflicting idempotency reuse is not detected.** Reusing a processed `commandId` returns the prior receipt even if the new command type/payload differs. No payload fingerprint binds idempotency identity to semantics.

18. **Client timestamp becomes authoritative Event time.** The generic handler uses `command.submittedAt` for `occurredAt`; PCV-03 passes the phone-supplied timestamp through instead of stamping host-authoritative receipt time.

19. **Ordered transport does not serialize asynchronous host mutations.** The data channel is ordered, but each received envelope launches an independent async task. Two rapid commands can overlap reads/writes and race the compare-and-swap store.

20. **Cross-owner join mutation is non-atomic.** PCV-03 mutates the PCV-02 Campaign member list before persisting its own Session membership. A later save conflict/failure can leave the two records inconsistent.

### D. Recovery, checkpoints, acknowledgments, and delivery cursors

21. **Join acceptance advances the player's acknowledged Event cursor before delivery.** `join-accepted.lastSequence` is stored as `lastAcknowledgedSequence` before the subsequent Event batch is actually received.

22. **Command ACK advances the Event cursor before Event delivery.** The ACK's host `lastSequence` is written into the client recovery cursor before the Event batch arrives. A disconnect between ACK and batch can cause reconnect to skip an Event permanently.

23. **Client Event merge does not perform gap detection.** Incoming Events are deduplicated/sorted by ID/sequence, but the canonical ordered-delivery reducer is not used to detect gaps or trigger authoritative recovery.

24. **Visible Events and authoritative stream cursor are conflated.** Hidden-before-publication filtering can legitimately omit global sequence numbers. PCV-03 needs an explicit authoritative durable cursor separate from the visible Event list so secrecy does not look like loss and loss does not look like secrecy.

25. **Checkpoint never rolls forward.** The only checkpoint is created at Session start; later commands/events never create or advance a checkpoint lifecycle.

26. **Checkpoint checksum is not integrity evidence.** The value is a predictable label (`pcv03-checkpoint:<campaign>:1:1`) and reconnect compares the checkpoint's value to itself. There is no separately trusted content digest.

27. **No replay fingerprint.** Current architecture requires checkpoints + acknowledgments + sequence cursors + replay fingerprints for reconnect/recovery; PCV-03 has no replay fingerprint binding restored history/state.

28. **Reconnect rendezvous is coupled to a new Campaign invitation.** The client can only establish a fresh WebRTC path by accepting another invitation offer. Membership invitation and transport rendezvous/resume should be separate after membership exists.

### E. Presence

29. **Disconnect does not make host presence disconnected.** Closing the player's peer updates only local UI phase; no trusted host-side connection lifecycle updates presence.

30. **Presence messages are spoofable.** Host persistence trusts caller-supplied subject/device/status/timestamp rather than deriving identity and time from the bound transport connection.

31. **Presence time is client-authored.** `envelope.at` is accepted as the durable last-seen timestamp rather than host receipt time.

### F. Capability negotiation, packs, rules, entitlement

32. **Capability negotiation is an echo, not a client capability proof.** The host embeds pack/rules/epoch in the offer; the Android client copies those same values into the join request; the host compares them to itself.

33. **Joining device does not report locally measured installed pack/rules state.** It does not demonstrate that the required pack, exact rules profile/runtime version, or compatible schema is actually installed.

34. **Entitlement/grant compatibility from the canonical handshake is absent.** The current local/online Session contract calls for membership plus entitlement snapshot/grant digest/count/pack set/rules version/authority epoch/projection scope.

35. **PCV-02 exposes `rulesProfileVersion: "current"` into Session compatibility.** An immutable live Session must bind an exact resolved version/snapshot, not a moving symbolic version.

### G. Secret handling and protocol hardening

36. **Raw invitation secrets are persisted in ordinary Session JSON/SQLite.**

37. **Raw resume tokens are persisted in ordinary host and client document records.** Current security canon requires secrets to use an approved secret store; no secure-store adapter is used here.

38. **Secret generation fails open to `Math.random`.** If Web Crypto is unavailable, invitation/resume/private markers fall back to non-cryptographic randomness rather than failing closed.

39. **Wire envelopes are not actually decoded/validated.** `decodeWireEnvelope` checks only `kind` and casts arbitrary JSON to the union.

40. **No per-envelope protocol/schema version.** Unsupported major versions and unknown top-level fields cannot be rejected as required by serialization/versioning canon.

41. **No message size/depth/list/batch bounds.** A connected peer can send arbitrarily large JSON/payloads. No bounded-work/backpressure/rate contract exists.

42. **Malformed transport input is silently swallowed.** The transport catch block drops invalid input even though the comment claims the coordinator will return a role-safe protocol error.

### H. Installed evidence can false-positive

43. **All major observations are emitted as literal `true` after weak structural checks.** The exporter does not record a causal proof receipt for each observation.

44. **Reconnect proof is only `connectionOrdinal >= 2`.** A second ordinary join can increment the ordinal and satisfy the evidence without a resume request succeeding.

45. **Idempotency proof does not prove a duplicate was attempted.** It checks uniqueness/count consistency of processed command IDs/receipts. One ordinary command can satisfy it.

46. **Ordered-delivery proof inspects host Event summary, not what Android actually received.**

47. **Installed Android runtime is host-trusted client metadata.** The Android join request self-reports `clientKind/clientRuntime/platform`; the evidence exporter later treats that as installed-runtime proof.

48. **Physical-device proof depends on one operator affirmation plus self-reported metadata.** There is no device-side receipt/artifact reference binding the Android installation and observed run to the package artifact.

49. **Verifier checks package `sourceHead` and platform set but not installed-binary identity.** It does not bind a device-side package hash/signature/version receipt to the exact artifact SHA-256 values.

50. **Evidence does not prove ACK-before-batch loss/recovery, stale authorization, invitation reuse, actor spoofing, or event-gap recovery.** The current focused tests are happy-path only.

### I. Upgrade/migration and scope hygiene

51. **No migration/retirement path exists for `PCV-03.session.1`.** A repaired package using the same app data location can encounter old Session records containing raw invitation/resume credentials and stale parallel authority.

52. **Old unsafe records must not be silently upgraded into trusted new authority.** The safe repair should preserve only permitted non-secret audit/history references, retire/revoke old credentials/Sessions, and require fresh governed membership/session establishment under the new schema.

53. **PR #775 contains unrelated UI/skin work.** Showcase-skin plumbing, profile-drawer changes, Search/Notifications removal, and other presentation changes are mixed into the networking candidate. Valid work may be preserved on its owning completed/future surface, but it should not hitchhike as PCV-03 authority/transport repair.

## What is already sound and should be preserved

- direct/manual WebRTC is a real transport, not a placeholder;
- zero-service ICE configuration remains available;
- STUN assistance is optional direct-discovery support rather than rules authority;
- installed Windows and Android packages were generated from the exact candidate head and the package manifest/source-head chain was checked;
- hidden GM Event payload is actually filtered before the player Event batch is built;
- generic P9 authority, ordered-delivery, hidden-filter, reconnect, and SMB-02 contracts exist and should be reused rather than rewritten;
- stable local subject and device identities are already available as building blocks;
- phone layout/touch sizing exists for the current PCV-03 controls.

## Required repair shape

Repair PCV-03 in-place; do not create another multiplayer system.

1. Adapt PCV-03 to canonical A3 invitation + A5 membership/Session lifecycle boundaries.
2. Bind each transport connection to the accepted canonical subject/device and derive actor/presence identity from that binding.
3. Freshly revalidate membership/permission/session status on join, command, projection, and resume.
4. Separate membership invitation from post-membership transport rendezvous/resume.
5. Bind live Session to an immutable exact launch/capability snapshot.
6. Narrow PCV-03 command schema to PCV-03-owned behavior; retain extension seam for PCV-04.
7. Add payload fingerprint conflict checks and host-authoritative timestamps.
8. Serialize per-Session host mutations.
9. Separate authoritative durable cursor from visible Events; acknowledge only delivered/processed projection state.
10. Advance content-hashed checkpoints and replay fingerprints deterministically.
11. Use approved secure storage for bearer/resume secret material; persist only safe references/digests in ordinary documents.
12. Version and strictly validate/bound wire envelopes; return safe protocol errors and apply bounded-work/backpressure.
13. Derive capability claims from locally measured client state and exact resolved pack/rules/entitlement data.
14. Add explicit Session close/supersession/revocation and old-schema retirement/migration.
15. Replace evidence booleans with causal receipts/observations from both installed devices and bind device/package identity to exact artifact hashes where feasible.
16. Add negative/regression cases for every blocker above, including A3/A5/P9/SMB predecessor regressions.
17. Regenerate exact-head validation and packages only after repair; then perform the physical Windows↔Android proof.

## Gate result

- **Old candidate `8232e52…`: REPAIR REQUIRED; not eligible for PCV-03 physical certification.**
- **Old package artifact `10832224601`: preserved as historical pre-audit evidence only; do not use for completion proof.**
- **PCV-03 remains in_progress.**
- **PCV-04 remains unauthorized.**

## Superseding preimplementation gate

Owner direction on 2026-09-25 requires a deeper project/interconnectivity pass before any PCV-03 implementation. This 53-finding audit is preserved as baseline evidence but is **not sufficient to authorize implementation**. The live gate is `PCV_PREIMPLEMENTATION_INTEGRITY_PROGRAM.md` / `PCV_PREIMPLEMENTATION_GAP_REGISTER.json` with PCV-I01..PCV-I06 strict order. New findings must be added there rather than relying on this document as a closed list.
