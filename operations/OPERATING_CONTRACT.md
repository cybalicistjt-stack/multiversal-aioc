# Multiversal Operations V3 Operating Contract

**Document ID:** MV-OPS3-CONTRACT-001  
**Version:** 3.1.0  
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
5. verify exact-head evidence before publication;
6. acquire the OPS3 publication lease for the target repository;
7. while holding the lease, fresh-read target `main` and compare it with the **base SHA recorded by the successful validation run**;
8. if `main` changed, fail closed, release/reacquire as necessary, reconcile the branch, and revalidate against the new base before merge;
9. merge only the exact validated PR head using an expected-head check;
10. verify the durable `main` result/tree;
11. release the lease with the verified merge SHA;
12. reconcile the work record after durable side effects.

### Serialized publication lease

`main` publication in `cybalicistjt-stack/Multiversal-app` and `cybalicistjt-stack/multiversal-aioc` is serialized by a compare-and-swap lease stored on dedicated non-authoritative AIOC coordination branches named:

`ops3-merge-lease/<lowercase-target-repository-slug>`

The lease state is modeled by `scripts/ops3_merge_lease.py`.

- Lease acquisition must build the next lease commit from the observed lease-branch head and advance the lease ref **without force**.
- Competing acquisitions from the same observed head create sibling commits; after the first fast-forward succeeds, the other ref update must fail and re-read rather than overwrite.
- The held lease binds holder/attempt, validated PR head, and validated target-main base.
- A fresh target-main SHA that differs from `validated_base` is `OPS3.STALE_MAIN` and forbids merge.
- Lease release requires the same holder and a verified durable merge SHA.
- Lease branches are executor coordination only and cannot select work or grant authority.

This is the default concurrency defense even if GitHub native merge queue/branch protection is unavailable. If native GitHub merge queue is later enabled, it may replace the transport mechanism only if these stale-base, exact-head, and durable-verification properties are preserved.

### Atomic control-plane projection

Multi-file governed-start and closeout updates must be projected as one repository tree, one commit, and one ref advance whenever the executor exposes Git object primitives. Sequential one-file commits are fallback-only. This prevents partial control-plane states and reduces serial round trips.

Keep execution credentials separate from publication credentials when the execution system requires that boundary. Do not weaken security controls simply to make a worker green.

## 8. Failure discipline

Classify failures before repair. Useful classes include product defect, validation defect, repository state, executor/tooling, source availability, external service, publication lease conflict, stale-main validation, and owner-only decision.

A deterministic failure is not retried unchanged. Record the exact failure signature or evidence, form a falsifiable cause, apply the smallest causal repair, and rerun the smallest proof first.

A lost publication lease is not a product failure. Re-read the lease and target `main`; do not force-update the coordination ref and do not merge around the holder.

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
