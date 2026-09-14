# MV-CONT-016 — Execution System v2 Design

Date: 2026-09-14  
Status: owner-approved control-plane repair design; ARI-22C remains selected_not_started and product implementation authority remains false.

## Objective

Replace the failure-prone conversational execution model with a small deterministic execution kernel that can carry one authorized Multiversal work item from start through verification, merge, canonical closeout and successor selection without using the owner as a heartbeat.

Acceptance statement:

> An ordinary authorized tranche can start, execute, diagnose routine failures, validate, merge, reconcile cross-repository state, close, and select its successor without owner continuation being required merely to resume obvious authorized work; completion, timing and interaction facts are derived from external events rather than authored by the executing agent.

## Root causes being corrected

ARI-22B demonstrated that the previous control plane could both execute poorly and later certify the execution as successful. Its canonical checkpoint reported one owner Continue and single-Continue success despite two owner Continues plus a stall nudge. It also recorded three repair cycles while diagnostic mode remained false. The run attempted an unsupported merge method and mixed validation-harness repair into the product tranche. Product evidence remained valid; execution-quality evidence did not.

The post-incident field study also found that the existing 24-minute envelope was shaped as a minimum amount of activity before ordinary closure. That is an inverted latency objective: correct terminal state could be blocked because too little time had elapsed. Execution System v2 makes elapsed time an SLO/diagnostic signal, never proof that work is complete and never a minimum runtime gate.

## Trusted invariant kernel

Only the following rules belong on the mandatory critical path:

1. authority and bounded scope are explicit;
2. one mutation domain has one authoritative writer at a time;
3. material facts come from durable observed events/evidence rather than model narration;
4. externally visible side effects are idempotent, exactly identified and verified or compensated;
5. retry requires materially changed evidence, and repeated failure transitions into diagnosis rather than hot-loop retry;
6. high-risk/out-of-scope/owner-only decisions remain owner gates;
7. exact-head evidence must match the state being merged or closed;
8. final response is permitted only by actual terminal invariants plus independent reconciliation evidence.

Everything else is guidance, optimization, telemetry or a diagnostic heuristic and must not create a hidden terminal gate.

## 1. Immutable execution event ledger

Execution truth is an append-only, hash-chained event stream. Events carry run identity, sequence, timestamp, source, type, payload, previous digest and event digest.

Derived facts include owner Continue count, owner stall nudges, wall-clock latency, single-Continue outcome, retry/no-progress counts and later phase/side-effect metrics. The executing model may project those facts into checkpoints for readability but may not author their values independently.

Historical attempts that predate the ledger retain additive correction/audit records rather than having their original checkpoint rewritten.

## 2. Timing semantics

The current 24-minute value becomes an initial owner-visible latency SLO. It is not a minimum runtime.

- If terminal invariants are satisfied at minute 8, close at minute 8.
- If terminal invariants are satisfied at minute 31, close at minute 31 and record an SLO miss.
- If terminal invariants remain unsatisfied at minute 31, continue the same durable run unless a genuine blocker applies.
- A risk signal may cause optional work to be abandoned, but elapsed time cannot authorize or prohibit completion.

Future scorecards should use observed p50/p90/p95 wall latency by tranche class rather than one universal forced duration.

## 3. Durable execution supervisor

The execution abstraction is `work item -> durable run -> terminal result`, not `chat turn -> tool batch -> response -> owner Continue`.

A Continue starts or resumes the current run. Routine substep completion, validation completion, ordinary repair, merge and closeout do not transfer scheduling responsibility to the owner. Conversation/session changes preserve run identity and next machine action.

This first MV-CONT-016 slice establishes the truth and termination primitives. The supervisor loop is a subsequent slice and must consume those primitives rather than invent a parallel state model.

## 4. Trajectory-level diagnostics

A failed run must make the causal trajectory inspectable:

`exact failure signature -> failure domain -> first critical failure -> downstream consequences -> falsifiable hypotheses -> discriminating test -> changed evidence -> repair -> outcome`.

Repeated identical failure with unchanged evidence is no progress. Diagnosis should target the first causally decisive transition rather than narrating only the terminal failed state.

## 5. Cross-repository saga/outbox

Application merge and AIOC closeout are a distributed transition. They are handled as a resumable saga:

`prepare closeout projection -> validate exact app head -> idempotent merge -> durable merge-observed event -> reconcile AIOC closeout -> select successor -> verify canonical state`.

An interruption resumes from the durable observed event. It does not require the owner to discover which half of the transition completed.

## 6. Deterministic tools and capability discovery

Prefer unit-testable deterministic tools for repository search, diffs, validation, dependency/provenance checks, environment admission and other mechanically decidable work. Repository/tool capabilities are discovered before side effects. Tool discovery is hierarchical/on-demand so capability catalogs do not crowd out task context.

The verified local workstation inventory is a future source for a controlled local capability layer; this design does not silently make local tools a dependency before that interface exists.

## 7. AI-team topology

Do not create a mutation swarm. The default topology is one executor plus deterministic tools plus independent verification/evaluation. Parallel AI workers are appropriate only for isolated research, read-only investigation, test generation or independent review with explicit ownership boundaries.

## 8. Independent acceptance

The executing agent's statement that work is done is not acceptance evidence. The work type determines required independent evidence: focused contract/unit checks, integration evidence, deterministic cross-platform evidence, end-to-end journeys, independent review or combinations thereof.

## Operating metrics

Execution System v2 measures owner interventions, owner-visible start-to-terminal latency, time to first meaningful action/RED, time to first critical-failure localization, GREEN-to-merge latency, merge-to-canonical-closeout latency, control-plane overhead, unchanged-evidence retries, no-progress transitions, event/projection mismatches, stale-pointer incidents, unsupported capability attempts, unintended side effects, platform interruptions and independent-review rework.

`single_continue_achieved` is a derived user-experience metric. It is never an AI-authored certification field.

## Harness complexity rule

An incident is not fixed by adding prose alone. Every proposed control must do at least one of:

- change a deterministic machine decision;
- add a missing observable fact;
- remove or simplify a harmful rule;
- enforce an evidence/authority boundary;
- deliberately accept and document residual risk.

New mandatory controls require a reproduced Multiversal failure plus an executable regression. Controls that add context or procedure without changing an observable decision stay off the critical path.

## Historical acceptance cases

Execution System v2 will be evaluated against representative prior failures including VTI-12 stale cross-repository closeout, ARI-20 control-plane/routing delay, ARI-22A premature boundary/wrong merge method/minimum-runtime defect, and ARI-22B false interaction certification, stall, harness repair and timing overrun.

## Immediate MV-CONT-016 slice

The first implementation slice is intentionally small:

1. make the Execution System v2 contract executable in RED tests;
2. add a hash-chained event ledger and event-derived metrics;
3. make 24 minutes a latency SLO instead of a minimum terminal gate;
4. revise termination/precloseout semantics so actual terminal invariants decide closure;
5. retain ARI-22B as historical nonconformance without rewriting its original checkpoint;
6. prove the repaired AIOC control plane through the canonical repository-health workflow before any ARI-22C product start.
