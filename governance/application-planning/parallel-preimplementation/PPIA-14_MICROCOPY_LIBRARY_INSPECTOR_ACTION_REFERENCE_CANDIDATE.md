# PPIA-14 Microcopy Library / Inspector-Action-Reference Candidate

This bounded milestone turns the verified PPIA-14 Foundation semantic states into the first complete permission-safe state-by-state microcopy library without changing any upstream gameplay, permission, recovery, entitlement, approval, support, Pack, Character, Campaign, canonical-content or runtime authority.

## Library lock

The candidate defines **18 stable message objects**, exactly one for each Foundation message state. Each object has stable semantic, title, body and nonvisual localization keys; baseline English visual and nonvisual copy; severity semantics; disclosure class; allowlisted interpolation; action classes; pluralization policy and support-reference policy.

The library preserves the Foundation distinction between internal truth and user-visible copy. `P14-MS-002 safe-unavailable` and `P14-MS-003 hidden-information-suppressed` are externally equivalent whenever existence is protected. Hidden state cannot be inferred through wording, counts, action presence, timing, localization variables, diagnostics, support context or nonvisual output.

`status-unknown` explicitly means that success and failure are both unproven. It offers authorized status lookup rather than blind mutation retry. An accepted durable Event remains distinct from a lagging projection. Offline/local state remains nonauthoritative. Idempotent retry wording and action are available only when upstream `operation_id`, status and safe-retry semantics prove the retry eligible.

## Inspector and action contracts

The Inspector exposes **12 permission-safe projection groups** covering message identity, safe copy, disclosure, severity, interpolation, actions, nonvisual copy, localization, support, variant selection, authority provenance and recovery trace. Permission and entitlement filtering occur before message discovery, action discovery, interpolation, diagnostics and support projection.

The action matrix defines **20 action presentations**. Only two can present upstream mutating operations: a proven-safe idempotent retry and F025-governed redacted issue reporting. Both remain presentations of upstream authority and do not create mutation authority. Permission escalation, hidden-existence-proving actions, blind ambiguous retry, forced overwrite, raw diagnostic disclosure, automatic support screenshots, invented F024 behavior and AI decision authority remain forbidden.

## Wording and localization

The candidate includes baseline English copy but the stable contract is semantic and localization-ready. `visible_field_label` and `safe_reason` are the only allowlisted interpolation keys in this milestone. They bind only after authorization and disclosure reduction. Hidden names, IDs, counts, relationships, policy internals, secrets, raw diagnostics and unauthorized denial reasons never enter localized strings.

Visual and screen-reader/nonvisual wording may differ only when safe meaning and disclosure ceiling remain equivalent. Required recovery information cannot be toast-only, icon-only or color-only. Keyboard, touch, mobile single-focus, high-zoom/reflow and reduced-motion presentations retain the same required meaning and available recovery action.

## Deterministic coverage

The milestone adds **40 new synthetic noncanonical cases**, combined with the 32 Foundation cases for **72 effective deterministic cases**. Coverage includes all 18 semantic states plus hidden-vs-missing equivalence, hidden counts, visible and hidden validation fields, stale/conflict review, bounded offline behavior, reconnect, status unknown, safe idempotent retry, accepted durable Event/projection lag, approval reason suppression, minimum-safe support/diagnostics, entitlement fallback, F024 governance fallback, mobile, keyboard and nonvisual parity.

## Boundaries

PPIA-13 remains completed_verified and retains concept-teaching ownership. PPIA-14 owns final state-by-state error/recovery/permission wording and behavior guidance.

`P14-GAP-001` remains open because authoritative MV-IA-F024 Pack Lifecycle behavior is unavailable; ordinary users fall back to safe-unavailable and governance actors may inspect the gap without inventing Pack behavior. `P14-GAP-002`, the Foundation’s intentionally unfinished wording-library gap, is resolved by this candidate only; that resolution does not complete PPIA-14 overall or create upstream behavior. This package does not activate application runtime, STAGE-A-A2, release, deployment, tester access, paid services or production credentials.

This is an intermediate PPIA-14 milestone, not PPIA-14 completion. The exact next bounded milestone is **PPIA-14 Integrated Error Recovery Permission Workflows / Traceability**, which must bind these message objects and action presentations into governed end-to-end recovery, permission, approval, support and diagnostic flows before the tranche can proceed to completion evidence.
