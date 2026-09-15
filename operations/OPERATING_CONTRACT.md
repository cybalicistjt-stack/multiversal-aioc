# Multiversal Operations V3 Operating Contract

**Document ID:** MV-OPS3-CONTRACT-001  
**Version:** 3.0.0  
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

Do not stop merely because a substep, commit, RED/GREEN transition, tool batch, or PR creation completed. Do not manufacture extra work to satisfy a timer. No minimum runtime exists.

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

## 7. Changes, validation, and publication

For implementation work:

1. verify the authorized repository/base/branch or create the authorized branch;
2. make the smallest coherent change;
3. run focused validation;
4. run the lane's required acceptance gate;
5. verify exact-head evidence before merge or publication;
6. reconcile the work record after durable side effects.

Keep execution credentials separate from publication credentials when the execution system requires that boundary. Do not weaken security controls simply to make a worker green.

## 8. Failure discipline

Classify failures before repair. Useful classes include product defect, validation defect, repository state, executor/tooling, source availability, external service, and owner-only decision.

A deterministic failure is not retried unchanged. Record the exact failure signature or evidence, form a falsifiable cause, apply the smallest causal repair, and rerun the smallest proof first.

If a failure is isolated to one executor, do not rewrite project governance around that executor.

## 9. Completion and truthfulness

Only verified evidence can support completion claims.

A bounded work item may be called `completed_verified` only when:

- requested scope is complete;
- required validation is green for the exact candidate;
- required durable side effects are observed;
- no authorized closeout action remains;
- current operational state is reconciled.

An open PR, queued/running check, patch, local success, model exit code, or conversational assertion is nonterminal unless the work item explicitly defines it as the requested endpoint.

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

Changes to this contract, the canonical door, current-state schema, or lane semantics are operations-lane work. Product lanes stay preserved while a stop-the-line operations freeze is active.

The operations system should become simpler over time. A new control file is justified only when it owns data that cannot live clearly in the existing contract, current state, lane registry, work item, evidence, or adapter.
