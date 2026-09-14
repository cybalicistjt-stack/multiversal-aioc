# MV-CONT-016 Implementation Plan — Execution System v2

Status: in progress  
Scope: AIOC control plane only. ARI-22C remains `selected_not_started`; no application product branch or implementation authority is created by this plan.

## Goal

Install the minimum trustworthy execution substrate needed before roadmap work resumes: event-derived execution truth and state-driven termination with latency treated as telemetry rather than a minimum runtime gate.

## Task 1 — Lock the RED contract

Files:
- `tests/control_plane/test_execution_system_v2.py`
- `.github/workflows/validate-repository-health.yml`

Acceptance:
- new regression suite is on the canonical repository-health path;
- it initially fails because the event ledger does not exist and the old timing contract blocks early terminal state;
- failure is caused by the intended missing behavior, not syntax/test harness damage.

## Task 2 — Add immutable event ledger

Create:
- `scripts/execution_event_ledger.py`

Required behavior:
- canonical hash-chained execution events;
- stable run/sequence identities;
- offset-aware monotonic timestamps;
- previous-digest linkage and tamper detection;
- derived owner Continue count, stall-nudge count, single-Continue result, wall latency and latency-SLO status;
- the executor cannot independently override those derived metrics.

Focused verification:
- run `tests/control_plane/test_execution_system_v2.py` and prove ledger tests green while timing tests remain RED if not yet implemented.

## Task 3 — Replace minimum-runtime closeout logic

Modify:
- `scripts/execution_transaction_preflight.py`
- `scripts/execution_termination_preflight.py`

Required behavior:
- actual terminal invariants decide whether closeout/response is permitted;
- 24 minutes is SLO telemetry only;
- terminal state before 24 minutes is allowed;
- terminal state after 24 minutes is allowed and records an SLO miss;
- nonterminal state after 24 minutes continues the same run;
- open PR, active validation, pending merge closeout, unreconciled side effects/evidence and real nonterminal state remain hard blockers.

## Task 4 — Update machine-readable authority and documentation

Modify:
- `governance/ai/runtime/EXECUTION_PROFILE.json`
- `governance/ai/interaction-system/EXECUTION_TERMINATION_CONTRACT.json`
- `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
- `governance/ai/MULTIVERSAL_CHECKPOINT_AND_VALIDATION_EFFICIENCY_POLICY.md`
- related envelope/ARI-22A/control-plane regressions.

Required behavior:
- profile exposes `latency_slo_minutes: 24` and `minimum_runtime_gate: false`;
- profile names `scripts/execution_event_ledger.py` as the event-ledger primitive;
- no current policy says ordinary correct terminal state must accumulate 24 active minutes;
- compatibility timing fields may remain temporarily where historical projections require them, but cannot act as a completion gate.

## Task 5 — Bind future execution-integrity projections to event truth

Modify:
- `scripts/execution_integrity_gate.py`
- execution integrity policy/regressions as needed.

Required behavior:
- future ledger-backed attempts derive interaction/timing facts from their ledger;
- checkpoint projection disagreement with derived truth is a repository-health failure;
- ARI-22B remains an additive historical correction because it predates the ledger;
- successor selection cannot make a recently completed integrity defect disappear.

## Task 6 — Full validation and integration

Run through PR #1163:
- canonical repository-health validator;
- canonical control-plane regressions;
- Execution System v2 regressions.

Before merge:
- fetch fresh AIOC repository capabilities;
- bind merge to the exact validated PR head and a permitted method.

After merge:
- verify canonical main repository health once;
- record MV-CONT-016 completion evidence without starting ARI-22C.

## Subsequent approved slices after this substrate

These are part of the approved repair program but should build on the first slice rather than be entangled with it:

1. durable execution supervisor / heartbeat-free continuation;
2. first-critical-failure trajectory diagnostics and no-progress circuit breaker;
3. cross-repository saga/outbox for application merge → AIOC closeout;
4. controlled workstation/local capability gateway;
5. independent evaluator path and acceptance-profile generation;
6. historical incident replay/evaluation suite and owner-burden/latency scorecard.

Each subsequent slice must preserve the harness-complexity rule: reproduced failure, executable acceptance test, smallest deterministic mechanism, independent evidence, and removal of superseded controls rather than indefinite layering.
