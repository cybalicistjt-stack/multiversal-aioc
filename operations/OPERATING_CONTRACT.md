# Multiversal Operations V3 Operating Contract

**Document ID:** MV-OPS3-CONTRACT-001  
**Version:** 3.3.0  
**Status:** CANONICAL  
**Owner and final authority:** John Brandon Turner

## Purpose

This is the single behavior contract for Multiversal work. It applies equally to ChatGPT conversations, Codex sessions, local agents, CI-assisted execution, and human operators. Lane files define scope and sources; they may not redefine this contract.

## 1. Authority model

Authority is intentionally shallow:

1. John Brandon Turner may set or change priority, scope, and owner-only decisions.
2. `operations/BOOTSTRAP.md` is the only operational door.
3. `operations/CURRENT.json` is the only mutable selector of current operational state.
4. `operations/LANES.json` maps user intent to one lane and its bounded source bundle.
5. A work-item record named by `CURRENT.json` defines the authorized scope for persistent execution.
6. Repository, PR, CI, filesystem, and tool evidence prove implementation facts; they do not independently grant product authority.

No other file is allowed to declare current work or override this chain. Compatibility projections may repeat data only when they explicitly identify `operations/CURRENT.json` as their source.

Execution guards and merge leases are **validation/executor-coordination mechanisms only**. They may block an unsafe transition, but they may never select work, expand scope, or grant implementation authority.

## 2. GPT-first startup

Every new GPT conversation begins by entering through `operations/BOOTSTRAP.md`. Project Sources, restart prompts, repository `AGENTS.md` files, and executor activation documents must all point to that same door and must not restate live current state.

The bootstrap must be small enough to read every time. Historical governance is not startup context.

## 3. Lane selection

Select one lane from the user's actual request. Do not assume that every Multiversal conversation is software implementation.

Lane selection determines:

- which current work record, if any, is relevant;
- which repositories or source collections may be loaded;
- which acceptance evidence applies.

Lane selection does not change behavior rules, owner authority, or completion standards.

When a conversation changes topics materially, reselect the lane once. Do not carry irrelevant lane context forward.

### Parallel persistent lanes

OPS3 may keep more than one persistent implementation lane active at once when the owner has explicitly separated the work streams.

- Each conversation/executor still selects exactly one lane from user intent.
- Implementation authority is lane-local. Starting or continuing one lane does not implicitly pause, revoke, reorder, or rewrite another active lane.
- A lane may change another lane's selector/checkpoint only when the owner explicitly directs cross-lane reprioritization or when an operations-lane repair is required to restore canonical truth.
- Active lanes that target the same repository must use distinct branches.
- Shared-repository publication is serialized by the OPS3 FIFO publication queue. A lane reserves a publication turn first; queued lanes do not prepare/reconcile/revalidate a publication candidate until their reservation reaches the active head.
- When a reservation becomes active, that holder owns the publication window, fresh-reads `main`, prepares/reconciles exactly once from that turn base, validates the candidate while the window is held, merges the exact validated head, then releases so the next reservation can activate.
- A queue wait never changes lane authority. It delays only publication preparation and `main` mutation; implementation work that cannot invalidate the eventual turn-base preparation may continue independently.
- Cross-lane reads remain minimal and evidence-driven.

## 4. Meaning of execution commands

Within an established lane, `Continue`, `keep going`, `fix this`, and `implement this` authorize ordinary reversible work through the requested bounded result unless an owner-only decision or genuine external blocker is reached.

Do not stop merely because a substep, commit, RED/GREEN transition, tool batch, PR creation, validation start, validation completion, product merge, or control-plane PR creation completed. Do not manufacture extra work to satisfy a timer. No minimum runtime exists.

For a governed bounded execution, the active checkpoint carries `execution_guard` evidence. The first owner execution command for the attempt increments `continue_turns`, sets `terminal_response_allowed=false`, and keeps it false until either:

- the bounded result is fully completed and reconciled; or
- a genuine owner-only or external blocker is recorded with concrete evidence.

Before a normal terminal response, the executor must fresh-read `operations/CURRENT.json` plus the active checkpoint and apply `scripts/ops3_execution_guard.py` or its exact equivalent. A response that would hand control back while authorized work or closeout remains is nonterminal and must not be emitted as the result of the Continue.

A status request without execution wording is read-only. `get ready` means reconcile enough current state that the next `Continue` can execute without repeating broad discovery.

## 5. Critical-path discipline

Once lane, work item, repository, branch, and acceptance gate are known:

- load only the declared dependency closure;
- prefer direct evidence over narrative reconstruction;
- do not re-read unchanged sources without an invalidating event;
- do not search unrelated history to fill time;
- diagnose the first material failure before retrying;
- require changed evidence before repeating a failed operation;
- batch related repairs before rerunning expensive terminal gates.

Research is progress only when it resolves a concrete unknown needed for the result.

## 6. Executor independence

Executors are replaceable capabilities.

- ChatGPT may execute through connected repository/file/app tools.
- Codex may execute bounded implementation tasks.
- Local workers may run deterministic commands.
- GitHub Actions may validate or publish according to repository permissions.
- Humans may perform owner-only or unavailable-tool actions.

An executor outage, quota, sandbox defect, PATH defect, or local-host problem is an executor capability issue. Preserve the work item and use another lawful executor when possible.

Never make Codex availability, a specific laptop, or a specific chat session part of product authority.

## 7. Changes, validation, publication, and merge serialization

For implementation work:

1. verify the authorized repository/base/branch or create the authorized branch;
2. make the smallest coherent change;
3. run focused validation;
4. run the lane's required acceptance gate;
5. reserve a FIFO publication turn for the target repository before publication preparation;
6. if the reservation is not first, wait without rebasing, reconciling, or repeatedly validating a publication candidate;
7. when the reservation reaches the head, activate the turn and fresh-read target `main`; that SHA becomes the immutable `turn_base` for this publication window;
8. only after activation, prepare/reconcile the branch exactly once from `turn_base` and run the required focused/acceptance validation while the publication window is held;
9. bind the exact validated PR head and validated base to the active turn; `validated_base` must equal `turn_base`;
10. merge only that exact validated PR head using an expected-head check;
11. verify the durable `main` result/tree;
12. release the active turn with the verified merge SHA, preserving FIFO order for queued reservations;
13. reconcile the work record after durable side effects.

### FIFO publication reservation queue

`main` publication in `cybalicistjt-stack/Multiversal-app` and `cybalicistjt-stack/multiversal-aioc` is serialized by a compare-and-swap FIFO reservation queue stored on dedicated non-authoritative AIOC coordination branches named:

`ops3-merge-lease/<lowercase-target-repository-slug>`

The queue state is modeled by `scripts/ops3_merge_lease.py`.

- A publisher first appends one reservation containing only `reservation_id` and `holder`. A queued reservation must not contain a prepared/validated candidate head or base.
- Reservations are FIFO. Only the first queued reservation may activate when no turn is currently held.
- Activation records the fresh target-main SHA as `turn_base` and removes that reservation from the queue. From activation until release, no other publisher may mutate that target `main`.
- The active holder performs its one publication preparation/reconciliation **after activation**, from `turn_base`, then validates while the turn remains held. This is the normal path; repeated stale-base rebases caused by racing lanes are a protocol failure, not expected work.
- After validation, the holder binds `validated_head` and `validated_base`; `validated_base` must equal `turn_base`.
- Merge authorization requires the same active holder, exact PR head, and fresh target `main` still equal to both `turn_base` and `validated_base`. A mismatch is `OPS3.STALE_MAIN` and fails closed.
- Release requires the same holder and a verified durable merge SHA. Release clears the active turn but preserves the remaining FIFO queue so the next reservation can activate on the newly published `main`.
- A queued reservation may be cancelled before activation without reordering the remaining queue. An active turn may be yielded without merge only with an explicit failure/blocker reason.
- Every queue-state mutation must build from the observed coordination-branch head and advance that ref **without force**. Competing writes from the same head must fail and re-read rather than overwrite.
- Queue branches are executor coordination only and cannot select work, reorder product priority, or grant implementation authority.

This is the default concurrency defense even if GitHub native merge queue/branch protection is unavailable. If a native GitHub merge queue is later enabled, it may replace the transport only if FIFO reservation, turn-base ownership, exact-head validation, and durable-verification properties are preserved.

### Atomic control-plane projection

Multi-file governed-start and closeout updates must be projected as one repository tree, one commit, and one ref advance whenever the executor exposes Git object primitives. Sequential one-file commits are fallback-only. This prevents partial control-plane states and reduces serial round trips.

Keep execution credentials separate from publication credentials when the execution system requires that boundary. Do not weaken security controls simply to make a worker green.

## 8. Failure discipline

Classify failures before repair. Useful classes include product defect, validation defect, repository state, executor/tooling, source availability, external service, publication lease conflict, stale-main validation, and owner-only decision.

A deterministic failure is not retried unchanged. Record the exact failure signature or evidence, form a falsifiable cause, apply the smallest causal repair, and rerun the smallest proof first.

A lost publication-queue CAS is not a product failure. Re-read the queue; do not force-update the coordination ref, skip ahead of queued reservations, prepare a competing publication candidate, or merge around the active holder.

If a failure is isolated to one executor, do not rewrite project governance around that executor.

## 9. Completion and truthfulness

Only verified evidence can support completion claims.

A bounded work item may be called `completed_verified` only when:

- requested scope is complete;
- required validation is green for the exact candidate and recorded base;
- required durable side effects are observed;
- publication lease acquisition/release evidence exists when `main` was mutated;
- no authorized closeout action remains;
- current operational state is reconciled.

An open PR, queued/running check, patch, local success, model exit code, product merge without control-plane closeout, or conversational assertion is nonterminal unless the work item explicitly defines it as the requested endpoint.

Product completion and execution-process conformance are separate. If `continue_turns > 1`, the checkpoint may still preserve valid completed product work, but execution conformance must record `OPS3.MULTI_CONTINUE_UNRECORDED` (or an equivalent explicit multi-Continue violation) rather than falsely reporting a clean one-Continue execution. Any owner stall nudge must likewise be recorded as a process violation. `scripts/ops3_execution_guard.py` enforces these evidence rules.

## 10. Owner-only boundaries

Stop for John when the remaining action requires a genuine owner decision, new spending or recurring obligation, production credential, irreversible provider commitment, release/publication approval reserved to the owner, destructive data loss, or a material product/canon/architecture decision not already authorized.

For ordinary reversible engineering choices, choose the simplest option consistent with approved architecture, validate it, record the assumption when material, and continue.

## 11. Preservation

Never delete project history merely because it is retired from authority. Preserve historical governance, conversations, work packages, proofs, and source archives for provenance and recovery.

Retirement means "cannot steer live work," not "erase the record."

## 12. Projections and compatibility

Legacy files may remain when tooling still expects their paths, but they must be one of:

- redirect to the canonical door;
- generated/checkable projection from `operations/CURRENT.json`;
- validation-only data;
- executor adapter;
- historical/evidence material.

A compatibility surface must state its disposition and may not invent current work, next action, or authority.

## 13. Operations-system changes

Changes to this contract, the canonical door, current-state schema, lane semantics, response guard, or publication lease protocol are operations-lane work. Product lanes stay preserved while a stop-the-line operations freeze is active.

The operations system should become simpler over time. A new control file is justified only when it owns data that cannot live clearly in the existing contract, current state, lane registry, work item, evidence, or adapter. New execution controls require a reproduced failure plus an executable regression before they enter the critical path.
