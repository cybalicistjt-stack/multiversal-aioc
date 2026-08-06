# IA-D04-004 — Authoritative Result and History Presentation

**Program:** MV-IA-001  
**Version:** 0.1.0  
**Status:** implementation-ready design  
**Owner and final authority:** John Brandon Turner  
**Companion matrix:** `IA-D04-004_AUTHORITATIVE_RESULT_HISTORY_MATRIX.json`

## 1. Purpose

Define how accepted, modified, denied, pending, stale, revoked, and recovery-required proposal outcomes are presented as role-safe results and durable history.

## 2. Scope

Covers result banners, detail panels, modification differences, denial explanations, cost and Effect summaries, source evidence, history timelines, exports, reconnect states, and accessibility. It excludes broader combat logs, campaign analytics, and release operations.

## 3. Authority and precedence

MV-IA-F006 controls Action results. IA-D04-002 controls reusable decisions and receipts. IA-D04-003 controls interruption and convergence. MV-IA-F020 controls hidden information. Lower-precedence presentation rules cannot widen authority or visibility.

## 4. Controlling authority statement

> Only accepted durable decisions, consumer commits, ordered Events, and current server projections may be presented as authoritative results.

Notifications, realtime messages, local caches, animations, calculated previews, and AI summaries are advisory.

## 5. Result identity

Every presentation binds stable history entry, Event, proposal, decision, consumer profile, aggregate, actor, source, and correlation identities. Display labels never replace stable IDs.

## 6. Authoritative status resolver

Before showing completion, the client resolves proposal, decision, and consumer-commit status. An ambiguous response produces `commit-status-unknown` and status lookup, not a success banner.

## 7. Player result summary

The primary Player result shows the authorized final outcome, accepted costs, visible Effects, Conditions, Resource changes, target changes, and a user-safe decision explanation. Action history and My Proposals remain secondary.

## 8. GM result detail

The GM projection may include original proposal evidence, current authoritative state, semantic modification diff, final values, reasons, warnings, hidden Effects, exact source versions, and commit receipts within current authority.

## 9. Assistant-GM and observer projections

Assistant-GM history is narrowed by active delegation. Observer history contains only observer-visible outcomes. Queue existence, proposal evidence, hidden targets, private notes, and secret modifiers are filtered before serialization.

## 10. Approve result

An approved result presents the reviewed proposal values that were actually committed. Preview values or requested costs are not shown as accepted unless the commit receipt confirms them.

## 11. Modify-and-approve result

The original proposal remains immutable. Presentation identifies changed paths, original values, final values, reasons, decider attribution, and final committed outcome. Player projections use authorized user-safe detail.

## 12. Deny result

A denial is durable and attributable but commits no proposed costs or Effects. The explanation uses a user-safe reason and does not reveal protected existence or GM-only evidence.

## 13. Cost, Effect, Condition, Resource, and target summaries

Summaries are derived from the accepted consumer commit and current projection. Each change includes stable source identity, amount or state transition, visibility class, and sequence reference.

## 14. Source and rule evidence

History preserves the exact Action or proposal definition, source pack, source version, rules profile, schema version, and relevant provenance used for the decision. Later content updates do not rewrite historical evidence.

## 15. Ordered history timeline

Timeline rows are keyed by durable Event identity and sequence. Duplicate delivery is suppressed. Gaps are explicit and recover through ordered Events or a current snapshot plus sequence anchor.

## 16. Pending, projection-pending, stale, and recovery states

The UI distinguishes decision pending, commit pending, status unknown, projection pending, stale, conflict, Event gap, revoked, forbidden, and recovery required. None is represented as completed.

## 17. Cache and reconnect behavior

Cached history is labeled nonauthoritative. Reconnect revalidates subject, role, delegation, Campaign, Session, permission, entitlement, and projection versions before replacing cached content.

## 18. Revocation and deletion of protected projections

Revocation removes protected result details, timeline entries, exports, subscriptions, diagnostics, and optional-AI context from every device. Audit evidence remains server-side under its own authorization.

## 19. Exports and diagnostics

Exports use the same role-safe projection as the interactive history. Diagnostics default to stable IDs, statuses, versions, sequences, and error codes while excluding protected prose, hidden targets, notes, and unrestricted source text.

## 20. Accessibility and responsive parity

Desktop, tablet, and mobile preserve outcome, authority status, attribution, costs, Effects, source evidence, modification differences, denial meaning, and recovery options. Screen-reader order states original value, final value, reason, and decider.

## 21. Deterministic fixtures

Twenty fixtures cover approve, modify, deny, GM detail, observer filtering, hidden targets, ambiguous commits, delayed projections, Event gaps, duplicates, stale caches, revocation, delegation, mobile, screen readers, exports, source versions, NPC history, and offline caches.

## 22. Implementation slices

Eight slices cover schemas; authoritative resolution; role-safe summaries; modification and denial; ordered history; evidence and exports; accessibility; and deterministic zero-service adapters.

## 23. Blocking acceptance criteria

- **ARH-AC-001:** Completion is shown only after authoritative decision and consumer-commit resolution.
- **ARH-AC-002:** Ambiguous commit responses trigger status lookup.
- **ARH-AC-003:** Player results contain only authorized final outcome data.
- **ARH-AC-004:** GM results retain attributable adjudication evidence within authority.
- **ARH-AC-005:** Assistant-GM detail is limited by delegation.
- **ARH-AC-006:** Observer history excludes proposal and queue evidence.
- **ARH-AC-007:** Approved results reflect committed rather than preview values.
- **ARH-AC-008:** Modified results preserve original and final values plus reasons.
- **ARH-AC-009:** Denied results commit no proposed costs or Effects.
- **ARH-AC-010:** Costs and Effects derive from accepted consumer commit evidence.
- **ARH-AC-011:** Exact source versions are preserved historically.
- **ARH-AC-012:** Duplicate Events do not duplicate timeline entries.
- **ARH-AC-013:** Event gaps remain explicit until recovery.
- **ARH-AC-014:** Pending, stale, revoked, and recovery states are not shown as complete.
- **ARH-AC-015:** Cached history is clearly nonauthoritative.
- **ARH-AC-016:** Revocation clears protected result and history projections.
- **ARH-AC-017:** Exports apply the same role-safe filtering.
- **ARH-AC-018:** Responsive and assistive presentations preserve semantic meaning.
- **ARH-AC-019:** Zero-paid-service and zero-AI core presentation remains possible.
- **ARH-AC-020:** The exact next handoff is IA-D04-005.

## 24. Handoff

IA-D04-005 must consolidate IA-D04-001 through IA-D04-004 into the first-playable-loop implementation handoff, dependency order, acceptance gate, and bounded implementation queue.
