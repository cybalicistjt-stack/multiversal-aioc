# APM-06 — Recovery, Safety, Acceptance and Implementation Handoff

**Work item:** APM-06  
**Program:** APM — Automated Play Modes  
**Status:** DESIGN / GOVERNANCE HANDOFF  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-19

## 1. Decision

APM-06 closes the Automated Play Modes design series by integrating APM-01 through APM-05 with the persistence, recovery, security and hybrid guarantees established by APW-07.

Automated play remains ordinary Multiversal state operated through bounded automation. There is no separate AutoGM save universe, Cozy save universe, AI-owned truth store, or automation-owned canonical ledger. Authoritative state remains owned by the ordinary domains and their accepted Events. Automation-run records preserve execution authority, provenance and recovery evidence only.

The final design must prove that Cozy Solo, Connected Cozy, AutoGM Single Encounter and AutoGM Mini-Campaign can pause, disconnect, recover, change cadence, encounter stale or revoked authority, survive optional-AI failure, and return to ordinary Multiversal play without duplicate accepted effects, silent state forks, protected-information leakage or authority expansion.

Application implementation remains inactive. The implementation IDs in this handoff are planning destinations only until the governing application roadmap explicitly activates them.

## 2. Controlling dependencies

APM-06 consumes APM-01 controller/delegation authority, APM-02 Cozy Solo, APM-03 AutoGM Encounter, APM-04 Mini-Campaign parent/child progression, APM-05 Connected Cozy participant/resource contracts, and APW-07 stable-operation/expected-version/status/EventCursor recovery semantics.

## 3. Unified automated-run recovery contract

Every state-affecting automated operation binds the automation run/controller/profile/delegation identities, Context, one stable operation ID, owning domain, expected versions, exact package/activity versions, deterministic seed/entropy evidence where needed, permission/entitlement/policy/visibility versions, resulting Event/status receipts, pending human choice/approval IDs, and optional-assistance provenance.

Retries reuse the same operation identity. Lack of a response is never treated as failure; reconnect queries status and Event history before any retry.

## 4. Recovery revalidation order

Recovery revalidates authenticated subject, Context membership/control/role, automation delegation/expiry/revocation, permission and visibility, entitlement/pack compatibility, scenario/activity versions, schema/rules/policy versions, authoritative Event cursor and operation status, reservations/leases, and pending human decisions. Material mismatch enters stale/review/revoked/expired/fail-safe behavior rather than silent migration.

## 5. Duplicate and stale rules

Duplicate `operationId` returns the existing result and cannot repeat costs, rewards, progress, resource movement, encounter effects, route progress or other accepted business effects. Stale expected versions reject unless the owning domain explicitly permits a commutative operation. A materially changed eligible action requires human review rather than automatic substitution. Automation never turns recovery into last-write-wins.

## 6. Cozy Solo recovery

Accepted progress applies once; spent resources are not spent again; rewards are not reissued; automatic progress resumes only from the last proven Event sequence; wall-clock time alone creates no progress unless explicitly authorized; expired authority/budgets/reservations stop or narrow the run; meaningful human choices remain pending; foreground-only disconnect pauses rather than continuing invisibly; optional AI is unnecessary for recovery.

## 7. Connected Cozy recovery

Connected Cozy preserves independent participant authority, attributable contribution IDs, reserve/commit/release resource receipts, accepted contribution order, consent barriers and leave/revoke/rejoin history. Host disconnect never authorizes another participant's choices or resources. Rejoin creates a fresh authorized projection; stale cached shared state cannot restore removed permissions or hidden data.

## 8. AutoGM Single-Encounter recovery

Recovery references the exact encounter package/version, participants, initiative/turn position, pending reactions/interrupts/human choices, deterministic seed cursor, accepted Events, end conditions and controller delegation. It resumes from the last proven barrier and cannot reroll resolved rolls, repeat effects/rewards, skip reactions/choices, expose scenario-private state or use AI to decide mechanical ambiguity. Incompatible versions pause for review.

## 9. AutoGM Mini-Campaign recovery

The parent run records current node/route state, exact APM-03 child run IDs and completion receipts, child-to-parent advancement operation IDs, route-eligibility inputs, pending human route choices, hidden projection version and run budgets. Each child completion advances the parent exactly once. Duplicate delivery returns the prior parent result rather than launching a second child or applying consequences twice.

## 10. Mode-transition acceptance

Cozy ↔ ordinary Personal/Campaign changes orchestration, not state ownership, and automation authority does not silently follow into ordinary play. Solo Cozy ↔ Connected Cozy uses explicit invitation/share boundaries; returning to Solo cannot copy other participants' protected payloads. AutoGM Encounter ↔ Mini-Campaign requires explicit parent-child binding and exact-once advancement receipts.

## 11. Automation-out-of-scope safety

Controllers reject/stop rather than improvise when asked to widen delegation, perform human-required choices, bypass consent/approval/ownership/publication gates, call ungranted domains, invent missing authoritative facts/rules/resources/routes/rewards, exceed budgets, use stale authority, mutate during unsupported offline state, infer hidden data, convert AI text into mechanics, or silently switch versions to succeed.

## 12. Optional-AI failure and illegality

Optional AI is replaceable presentation/proposal. Unavailable, timed-out, malformed, unauthorized, illegal or over-budget output is discarded/quarantined from authoritative processing, logged through privacy-safe provenance, and replaced by deterministic/manual presentation where possible. AI failure never widens authority and cannot undo an already committed domain operation merely because narration failed.

## 13. Hidden-information contract

D05/APW-06/APW-07 filtering precedes optional-AI context, Player summaries, notifications/counts, replay exports, diagnostics, support evidence, search and related projections. Scenario-private controller data is separately bounded by the exact scenario authority package and is never copied wholesale into AI or Player projections. Replay evidence may prove hidden evaluation without disclosing hidden payloads.

## 14. Deterministic replay and provenance

For the same authoritative starting state, exact package/rules/schema/profile versions, deterministic seed/entropy inputs, human decisions and accepted command sequence, mechanical outcomes reproduce. Presentation text need not be identical. Replay validates provenance and never reapplies Events.

Minimum chain: `subject/context → mode/profile → automationRunId → delegationGrantId → package/activity version → operationId + expected versions → deterministic inputs → owning-domain decision → authoritative Event IDs/sequences → parent/child receipt where applicable → role-safe projection → optional presentation provenance`.

## 15. Final APM implementation handles

1. **APM-I01 — Automated-run authority and lifecycle foundation** — controller/run identity, delegation, operation classes, lifecycle, provenance and shared feature flags.
2. **APM-I02 — Cozy Solo core loop** — bounded activities/progress/projects/resources/relationships/research/journaling/light exploration and mandatory-choice barriers.
3. **APM-I03 — AutoGM Single-Encounter runner** — package validation, deterministic turns/reactions, bounded NPC/world operations, player-required Actions and encounter replay.
4. **APM-I04 — Connected Cozy shared play** — invitation-only spaces, participant authority, attributable contributions, resource reservation, async/live coordination, consent and leave/rejoin.
5. **APM-I05 — AutoGM Mini-Campaign director** — bounded graph progression over APM-I03 child runs, exact-once completion, route choice, hidden projections and finite endings.
6. **APM-I06 — Automated-play recovery, safety and end-to-end acceptance** — APW-07 recovery across all modes, optional-AI/out-of-scope safety, deterministic replay, transitions and final acceptance.

Preferred activation order: `APM-I01 → APM-I02 → APM-I03 → APM-I04 → APM-I05 → APM-I06`.

## 16. Feature flags and rollout

Availability flags may independently gate automated-run foundation, Cozy Solo, AutoGM encounter, Connected Cozy, Mini-Campaign, optional AI presentation, bounded-background Cozy and recovery diagnostics. Flags never grant permissions or bypass domain authority. No core acceptance requires a paid AI/service.

## 17. Accessibility/mobile/no-AI

Start/pause/resume/stop/recovery is keyboard-complete; screen readers receive mode/context/authority/pending/status labels; route/encounter/progress/history have nonvisual equivalents; touch/mobile supports all required decisions and recovery; reduced motion is supported; warnings are not color-only; deterministic structured presentation exists without AI; zero-paid-service validation is mandatory.

## 18. Explicit non-goals

No public stranger matchmaking, multiplayer AutoGM authority, unrestricted/open-ended autonomous campaigns, AI mechanical/canonical/permission/consent authority, broad offline authoritative automated play, peer/multi-master canonical synchronization, autonomous publication/canonical promotion, paid-AI dependency, release/deployment, or CCTI-12-T04 before September 2026.

## 19. Completion gate

APM-06 is design-complete when every APM mode has APW-07-grounded recovery; duplicate/stale/ambiguous operations cannot duplicate accepted effects; mode transitions preserve one ordinary history; optional-AI failure cannot widen authority; hidden-information boundaries cover controller/AI/player/replay projections; deterministic replay can explain/reproduce mechanical outcomes without reapplying Events; APM-I01..I06 have clear boundaries and acceptance destinations; accessibility/mobile/no-AI/zero-paid-service paths are mandatory; and future multiplayer/public/open-ended autonomy remains deferred.

APW-08 is the final design-series tranche and must integrate APW, CSW and APM handoffs into the Stage/Internal-Alpha implementation package and roadmap placement.
