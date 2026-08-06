# IA-D04-005 — First-Playable-Loop Implementation Handoff

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** implementation-ready handoff; implementation dependency-gated  
**Owner and final authority:** John Brandon Turner  
**Source design tranche:** IA-D04-001 through IA-D04-004  
**Companion queue:** `IA-D04-005_IMPLEMENTATION_QUEUE.json`

## 1. Purpose

Consolidate the completed first-playable-loop design into one bounded implementation order that future application work can execute without rediscovering authority, recovery, presentation, or acceptance requirements.

## 2. What this handoff does

This package defines the exact implementation packages and dependency order, P9-06 prerequisites, shared contracts that must not be privately reimplemented, minimum Player and GM experience, deterministic acceptance scenarios, blocking gates, prohibited shortcuts, and the boundary between implementation readiness and implementation authorization.

## 3. What this handoff does not do

It does not implement application code, resume or replace `P9-06-008-attempt-002`, authorize paid services, use production credentials, collect real-user data, deploy, release an internal alpha, publish publicly, or promote canonical content.

## 4. Source authority

Precedence remains: owner decisions and governance; permissions and hidden-information contracts; Campaign, Character, Scene, Session, and Action authority; IA-D04-002 proposal/approval; IA-D04-003 interruption and convergence; IA-D04-004 result/history; then this implementation order. This handoff may sequence work but cannot widen authority.

## 5. First playable loop

`Campaign → controlled Character/actor → active Scene/Session → Action draft and evidence → proposal submit → GM approve/deny/modify → atomic Action result → ordered Event → role-safe result/history → reconnect-safe convergence`

The same governed path applies to GM-controlled NPC and enemy Actions.

## 6. Implementation-entry conditions

A package may begin only when its listed P9 dependencies are completed and verified. The complete online two-device loop requires provider-neutral persistence and migration foundations, provider-independent identity mapping, Campaign and row authorization, authoritative session commands, ordered Event delivery, hidden-information filtering, deterministic reconnect/restoration, and deterministic fixtures/reset capability.

Current unfinished parallel work `P9-06-008-attempt-002` remains preserved and is not silently completed or superseded.

## 7. Dependency-ordered implementation packages

| Package | Scope | Depends on | P9 prerequisites |
|---|---|---|---|
| FPL-I01 | Contract schemas, stable IDs, and typed ports | none | P9-06-008, P9-06-009 |
| FPL-I02 | Identity, role, delegation, and actor-control authorization | FPL-I01 | P9-06-012, P9-06-013 |
| FPL-I03 | Action draft, source inspection, targeting, and deterministic preview | FPL-I01, FPL-I02 | P9-06-009, P9-06-013 |
| FPL-I04 | Proposal submission, idempotency, and decision queue | FPL-I02, FPL-I03 | P9-06-016 |
| FPL-I05 | Approve, deny, and modify-and-approve adjudication | FPL-I04 | P9-06-016, P9-06-018 |
| FPL-I06 | Atomic Action result commit and ordered Event | FPL-I05 | P9-06-016, P9-06-017 |
| FPL-I07 | Role-safe projections, notifications, and realtime convergence | FPL-I06 | P9-06-017, P9-06-018 |
| FPL-I08 | Authoritative result and history presentation | FPL-I06, FPL-I07 | P9-06-017, P9-06-018 |
| FPL-I09 | Two-device reconnect, status recovery, and revocation | FPL-I04, FPL-I06, FPL-I07 | P9-06-019 |
| FPL-I10 | Audit, diagnostics, and privacy-safe support evidence | FPL-I05, FPL-I06, FPL-I09 | P9-06-020 |
| FPL-I11 | Responsive and accessible Player/GM interaction surfaces | FPL-I03, FPL-I04, FPL-I05, FPL-I08, FPL-I09 | existing verified foundations |
| FPL-I12 | Deterministic first-playable-loop acceptance harness | FPL-I01 through FPL-I11 | P9-06-023 |

## 8. Package rules

Finish packages in dependency order, not by UI convenience. Keep contracts provider-neutral and testable without paid services. Do not create private proposal, decision, Event, projection, or recovery models inside feature components. A UI is not complete until its authoritative state, failure states, recovery path, role filtering, and accessible semantics are complete. A service is not complete until idempotency, expected versions, denial behavior, audit evidence, and deterministic tests exist.

## 9. Minimum Player experience

The primary Player surface provides current Scene and actor context; Action selection and quick source-linked rule inspection; targets; costs, requirements, roll/seed, modifiers, computed result, proposed Effects, and warnings; explicit confirmation and submit; safe pending, stale, status-unknown, revoked, and recovery states; and authoritative result with accepted visible costs and Effects. Action history and My Proposals remain secondary.

## 10. Minimum GM experience

The GM notification and review provides proposer/controller and actor; Action and exact source/rule versions; targets; costs and requirements; roll/seed, modifiers, computed result, proposed Effects, and warnings; approve, deny, and explicit field-addressed modify-and-approve; semantic modification diff, reasons, attribution, and final revalidation; and current role-safe result/history. GM-controlled NPC/enemy Actions use this same structure.

## 11. Authoritative transaction

Only this ordered sequence may create an accepted Action result:

1. authenticate and resolve selected context;
2. authorize proposer, actor control, targets, and decision-maker;
3. validate consumer profile, evidence, source versions, requirements, costs, calculation, and Effects;
4. record immutable proposal using idempotent operation identity and expected aggregate version;
5. record one attributable final decision;
6. revalidate final values and current authority;
7. atomically commit accepted costs and Effects with one `ActionResultCommitted` Event;
8. publish role-safe projections;
9. present completion only after authoritative status resolution.

Failure at any step must not partially apply accepted Effects.

## 12. Recovery and two-device behavior

Lost responses trigger status lookup before retry. Review claims are advisory and expire safely. Duplicate delivery is suppressed by stable IDs and sequence. Event gaps remain explicit. Reconnect revalidates subject, role, delegation, Campaign, Character control, Scene, Session, permission, entitlement, pack lock, schema, and projection versions. No device may grant authority to another device. Silent last-write-wins is prohibited.

## 13. Result and history

Approved results show values actually committed. Modified results preserve original values, final values, changed paths, reasons, and attribution. Denied results show a durable user-safe explanation and no accepted costs or Effects. History uses durable Event identity and ordered sequence. Exact historical source, pack, rules-profile, schema, and provenance versions remain bound. Exports apply the same role-safe filtering as the current interactive projection.

## 14. Fixture inputs

Implementation consumes the 155 provenance-labeled alpha fixture identities from IA-D03-004, fourteen F006 loop fixtures, sixteen shared proposal/approval fixtures, twenty-four two-device interruption fixtures, twenty result/history fixtures, and twenty-four normalized acceptance scenarios in this handoff. Source fixture sets remain distinct evidence; this handoff does not claim they are deduplicated or the complete game.

## 15. Deterministic acceptance scenarios

Twenty-four scenarios cover approve, modify, deny, NPC/enemy parity, duplicate and lost responses, reconnect, review-claim expiry, Event duplication/gaps, stale versions, revocation, delegation expiry, observer and hidden-target projections, source-version preservation, offline drafts, mobile, screen readers, protected export, and deterministic two-device replay.

## 16. Blocking acceptance criteria

Twenty-eight blocking criteria require P9 dependency completion, shared-component reuse, stable IDs, idempotency, expected versions, atomic Event-backed commits, immutable proposals, attributable decisions, no Effects on denial, server-side hidden-information filtering, status lookup before retry, exactly-once decision/commit, ordered reconnect convergence, safe revocation, exact historical source versions, duplicate suppression, explicit Event gaps, bounded offline behavior, secondary logs/proposals, accessible parity, privacy-safe diagnostics, zero-paid-service/zero-AI core operation, deterministic replay, zero duplicate Effects, zero hidden-information leaks, and unchanged owner release gates.

## 17. Implementation evidence per package

Every package must provide changed-path inventory, contract/schema versions, deterministic and negative tests, authorization and hidden-information tests, idempotency/stale-version tests where mutation occurs, reconnect/revocation tests where state crosses devices, responsive/assistive evidence where UI changes, and exact commit, PR, final-head CI, and squash-merge evidence.

## 18. Release boundary

Completion of all packages proves implementation readiness for the bounded first-playable loop. It does not authorize internal-alpha release. Release remains behind P9-06 AG-08 and an explicit owner decision.

## 19. Next design route

IA-D04 closes after this handoff. The next original internal-alpha design item is **IA-D05-001 — MV-IA-F009 Relationship Tracker**.
