# PPIA-14 Foundation — Source and Message-State Inventory

**Work item:** PPIA-14 — Error, Recovery & Permission Microcopy  
**Artifact version:** 0.1.0  
**Status:** FOUNDATION CANDIDATE — NOT PPIA-14 COMPLETION  
**Owner:** John Brandon Turner

## Purpose

This bounded Foundation inventories the authoritative state and disclosure inputs that later PPIA-14 wording must consume. It defines semantic message states, hidden-information boundaries, actor/context delivery rules, safe affordance classes, accessibility/nonvisual/localization requirements, source gaps, and deterministic reference cases. It intentionally does **not** claim the complete final prose/string library.

## Authority and source order

Current canonical repository governance and owner decisions control. Completed PPIA-13 and PPIA-08 contracts are inherited without modification. MV-IA-F020 controls permission and hidden-information projection; MV-IA-F021 controls draft/save/command/accepted durable Event/projection, reconnect, stale/conflict, status-unknown and bounded-offline semantics; MV-IA-F025 controls help, diagnostics, issue reporting and support context.

PPIA-13 remains the authority for concept teaching. PPIA-14 may word a governed state but cannot create gameplay truth, permission, recovery authority, Pack lifecycle truth, canonical content, Campaign/Character state, approval truth, runtime state or entitlement.

## Message-state model

The Foundation defines 18 stable semantic message states across permission, validation, conflict, recovery, transport, approval, support and governance. State selection is downstream of authorization and minimum-safe disclosure reduction.

A local draft/edit state, save intent, authoritative command, accepted durable Event and derived projection/cache remain distinct. `status-unknown` is not failure. An accepted durable Event with a lagging projection is not an unsuccessful command. Offline/local behavior never becomes authoritative merely because copy says it saved.

## Hidden-information nonleak boundary

Permission and entitlement filtering occur before copy selection, counts, search/facets, diagnostics, support context, exports, notifications, localization variables and optional AI context.

When existence is protected, the user-visible result must not let the subject distinguish a missing resource from one that exists but is hidden, revoked or outside scope. That includes wording, names/IDs/types, counts, reason detail, actions, retry choices, timing/state transitions, diagnostics, support references and pluralization behavior.

## Safe affordances

The Foundation defines dismiss/return, correct-visible-input, retry-read, reconnect, operation-status lookup, upstream-proven idempotent retry, projection refresh, stale/conflict review, visible approval observation, help, redacted issue reporting and redacted diagnostic preview.

Blind retry after an ambiguous mutation, existence-proving actions, local permission escalation, unsupported forced overwrite, raw diagnostic reveal, automatic support screenshot capture and invented F024 actions are prohibited.

## Actors and delivery

The nine canonical F025 actors are preserved exactly: invited-tester, player, game-master, assistant-gm, content-creator, observer, owner-admin, service-actor and optional redacted read-only ai.

The same disclosure ceiling applies across inline, transient, dialog, unavailable/empty, nonvisual live-status and help/support channels. Cached wording/actions are re-evaluated after role change, revocation or reconnect.

## Accessibility, mobile, nonvisual and localization

Keyboard, touch, screen-reader, mobile single-focus, high-zoom/reflow, reduced-motion and noncolor equivalents are required. Meaning cannot rely solely on color, icon or motion, and required recovery information cannot exist only in a disappearing transient message.

Localization is semantic-key based. Interpolation values are allowlisted only after authorization. Hidden names, IDs, counts, policy internals, secrets, raw diagnostics and unauthorized reasons cannot enter localized copy or pluralization.

## Explicit source gaps

`P13-GAP-001` remains inherited as `P14-GAP-001`: a completed canonical MV-IA-F024 Pack Lifecycle packet is unavailable. No F024 lifecycle behavior, action, reason, recovery rule or wording is invented here.

`P14-GAP-002` records that the complete final PPIA-14 wording library is not supplied by upstream sources. This Foundation therefore remains a semantic/safety contract, not the final copy library.

## Deterministic Foundation corpus

32 synthetic, noncanonical reference cases cover hidden/missing equivalence, visible denial, validation, stale/conflict, bounded offline/reconnect, ambiguous mutation status, idempotent retry, accepted-Event projection lag, approval, entitlement, diagnostics/support, service actors, optional AI, accessibility/mobile/localization and the F024 gap.

## Nonactivation boundary

This Foundation does not activate application runtime, STAGE-A-A2, release, deployment, tester access, paid services, production credentials, or canonical promotion. PPIA-14 is not complete until the later complete state-by-state microcopy library and its declared completion evidence exist.
