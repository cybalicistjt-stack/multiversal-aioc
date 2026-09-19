# Multiversal Operations V3 Operating Contract

**Document ID:** MV-OPS3-CONTRACT-001  
**Version:** 3.8.0  
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

Execution guards, lane-state journals, and the ready-candidate publication queue are **validation/executor-coordination mechanisms only**. They may block an unsafe transition, but they may never select work, expand scope, or grant implementation authority.

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

OPS3 permanently preserves three independent persistent implementation lanes: `msas`, `mrcs`, and `mvps`. A lane may be `completed_verified`, `selected_not_started`, or `in_progress`, but completion or inactivity never deletes, folds into, or revokes either of the other persistent lanes. UISR-11 remains preserved as completed program history rather than occupying one of these slots. Operations work may repair lane selectors without collapsing this three-lane topology.


OPS3 may keep more than one persistent implementation lane active at once when the owner has explicitly separated the work streams.

- Each conversation/executor still selects exactly one lane from user intent.
- Implementation authority is lane-local. Starting or continuing one lane does not implicitly pause, revoke, reorder, or rewrite another active lane.
- A lane may change another lane's selector/checkpoint only when the owner explicitly directs cross-lane reprioritization or when an operations-lane repair is required to restore canonical truth.
- Active lanes that target the same repository must use distinct branches.
- Shared-repository publication is serialized only at the READY-candidate integration boundary. Lanes implement and run full tranche validation independently before queue entry.
- A candidate enters FIFO publication order only with an immutable PR head and green exact-head prequeue validation. There is no reservation for future work and no active holder that freezes `main`.
- The publication broker fresh-reads `main` for the FIFO head, runs the drift-sensitive integration gate, merges only the exact ready head, and reconciles the durable result. A failed candidate is removed without blocking later ready candidates.
- Cross-lane reads remain minimal and evidence-driven.

## 4. Meaning of execution commands

Within an established lane, `Continue`, `keep going`, `fix this`, and `implement this` authorize ordinary reversible work through the requested bounded result unless an owner-only decision or genuine external blocker is reached.

Do not stop merely because a substep, commit, RED/GREEN transition, tool batch, PR creation, validation start, validation completion, product merge, or control-plane PR creation completed. Do not manufacture extra work to satisfy a timer. No minimum runtime exists.

For a governed bounded execution, the active checkpoint carries `execution_guard` evidence. The first owner execution command for the attempt increments `continue_turns`, sets `terminal_response_allowed=false`, and keeps it false until either:

- the bounded result is fully completed and reconciled; or
- a genuine owner-only or external blocker is recorded with concrete evidence.

Before a normal terminal response, the executor must fresh-read `operations/CURRENT.json` plus the active checkpoint and apply `scripts/ops3_execution_guard.py` or its exact equivalent. A response that would hand control back while authorized work or closeout remains is nonterminal and must not be emitted as the result of the Continue.

A status request without execution wording is read-only. `get ready` means reconcile enough current state that the next `Continue` can execute without repeating broad discovery.

### Material-progress anti-loop

Every newly governed or repaired in-progress attempt must carry a machine-readable material-progress receipt in `execution_guard`: `material_progress_seq`, `progress_at_last_owner_command`, `no_progress_cycles`, `last_material_progress`, and `active_stall`.

On every additional owner execution command for an already in-progress attempt, compare `material_progress_seq` with `progress_at_last_owner_command` before beginning another ordinary cycle. If they are equal, record `OPS3.NO_MATERIAL_PROGRESS`, set `active_stall=true`, and enter diagnosis/recovery immediately. Do not begin another broad discovery, polling, validation, or retry cycle until changed evidence clears the stall. Repeated polling, re-reading unchanged sources, re-emitting status, waiting on the same deterministic failure, or recreating the same candidate is not material progress.

A status request is read-only and must expose enough current evidence to make a stall visible: work item, active substep, material-progress sequence and last evidence, protected-main holder/phase/liveness when applicable, and the first unresolved blocker/failure. Status reporting never resets a stall or counts as progress.

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

## 7. Changes, validation, lane state, and ready-candidate publication

For implementation work:

1. resolve the selected lane/work item from `CURRENT.json`;
2. read that lane's independent execution-state ref and start/resume the selected attempt there; starting execution does not require an AIOC-main publication;
3. work on the lane's implementation branch and record material progress on the lane-state ref;
4. run focused validation and the lane's full required prequeue acceptance gate on the immutable candidate head;
5. only after the exact head is green, submit one READY candidate containing lane, work item, PR, exact head, prequeue validation receipt, and relevant write/dependency fingerprint;
6. READY candidates are FIFO by submission order; implementation work never reserves a future position;
7. for the FIFO head, fresh-read target `main` and run the smallest drift-sensitive integration gate against that base;
8. if integration is green and the PR head is unchanged, merge with expected-head protection and atomic main-ref semantics;
9. verify the durable `main` result and reconcile the queue candidate from repository evidence; **there is no release step**;
10. if integration fails, mark/remove that head candidate with the causal failure so later READY candidates are not stranded; repair/revalidate the failed lane independently before resubmission;
11. record lane completion on its lane-state ref; project successor/global aggregate state through a separate READY candidate only when protected-main source state actually must change;
12. build, packaging, deployment, release, and post-merge distribution consume the merged artifact/result independently and never own the source-publication queue.

### Independent lane execution state

MSAS, MRCS, and MVPS use separate compare-and-swap coordination refs:

- `ops3-lane-state/msas`
- `ops3-lane-state/mrcs`
- `ops3-lane-state/mvps`

The state model is implemented by `scripts/ops3_lane_state.py`.

- `CURRENT.json` remains the global selector of which work item is authorized for each persistent lane.
- A lane-state ref may record only execution state for the work item/attempt selected by `CURRENT.json`; it cannot select a successor, reprioritize another lane, or expand scope.
- Starting a selected attempt, recording progress, and marking the lane attempt terminal are lane-local CAS writes and do not mutate protected `main`.
- One lane-state ref never contains another lane's progress. A stalled or lost executor therefore cannot block execution-state updates by another lane.
- Material durable side effects should be followed by a lane-state progress receipt before another substantial external-tool batch so replacement executors can resume without archaeology.

### Ready-candidate publication queue

Protected repositories use repository-local coordination refs named:

`ops3-publication-queue/<lowercase-target-repository-slug>`

The queue model is implemented by `scripts/ops3_merge_lease.py` (legacy filename retained for compatibility during the OPS3-10 cutover).

- Queue state contains READY immutable candidates and publication history only. Normal state has no `holder`, `turn_base`, activation phase, heartbeat, lease expiry, or release/recovery-release state.
- Prequeue validation must be green and bound to the submitted exact head. Pending, failed, mutable, or merely anticipated work cannot enter the queue.
- Only the FIFO head may receive merge authorization.
- Integration authorization binds the exact candidate head to a fresh observed `main` base and a green integration receipt. Base drift invalidates that receipt and requires a new integration check; it does not force the lane to redo unrelated implementation work.
- Direct writes to protected `main` remain prohibited. Protected-main mutation occurs only through the exact READY pull-request merge authorized by the integration gate.
- After durable merge, any executor may reconcile the queue from the observed candidate head and merge SHA. Because there is no holder/release step, a disappearing conversation after merge cannot strand publication.
- A causally failed FIFO head is marked failed and removed. Later READY candidates remain queued and may proceed.
- A native GitHub merge queue may later replace the transport if it preserves exact-head readiness, FIFO integration order, fresh-base integration validation, and durable-result reconciliation.

### Executor/session liveness

A conversation, Codex session, local process, CI poller, or connector call is replaceable execution capacity and must never become a lock.

- Do not silently sleep or wait in chat for another lane, queue position, CI completion, or a tool to recover. Use direct status reads only when needed for the current transition; unchanged polling is not progress.
- If a call produces no usable result, the session terminates unexpectedly, quota is exhausted, or the user has to restart the conversation, classify it as an executor/tooling interruption.
- On recovery, fresh-read `CURRENT.json`, the selected lane-state ref, and only the repository/PR evidence named by the last durable receipt. Resume from that point instead of replaying the tranche.
- A session interruption never creates publication ownership. Other lanes and READY candidates remain able to progress.
- Repeated owner `Continue` commands or stall nudges remain execution-quality incidents and are recorded truthfully even when durable product progress survives.

### Protected-main interlock

The protected repositories remain `cybalicistjt-stack/Multiversal-app` and `cybalicistjt-stack/multiversal-aioc`.

- Every protected-main mutation must be a pull-request merge of a READY exact head authorized by the fresh-base integration gate.
- Contents/ref writes directly to protected `main` are prohibited.
- Serialization covers only the atomic integration/merge decision; it does not freeze `main` while a lane implements or performs full validation.
- If target `main` changes after an integration receipt was produced, that receipt is stale and the broker reruns the drift-sensitive integration gate on the new base.
- Generated-content or CI work must prepare outputs on a candidate branch. It may not push directly to protected `main`.

### Atomic control-plane projection

When a global selector/successor projection really must change protected AIOC `main`, prepare its multi-file update as one tree/commit whenever possible, validate it before READY submission, and publish it through the same ready-candidate protocol. Do not use global selector publication as the live progress journal for a lane.

Keep execution credentials separate from publication credentials when the execution system requires that boundary. Do not weaken security controls simply to make a worker green.

## 8. Failure discipline

Classify failures before repair. Useful classes include product defect, validation defect, repository state, executor/tooling, source availability, external service, publication lease conflict, stale-main validation, and owner-only decision.

A deterministic failure is not retried unchanged. Record the exact failure signature or evidence, form a falsifiable cause, apply the smallest causal repair, and rerun the smallest proof first.

A lost publication-queue CAS is not a product failure. Re-read the READY queue and retry the coordination update from the observed generation. Never force the coordination ref or skip a READY candidate. There is no active holder to recover or wait for.

If a failure is isolated to one executor, do not rewrite project governance around that executor.

## 9. Completion and truthfulness

Only verified evidence can support completion claims.

A bounded work item may be called `completed_verified` only when:

- requested scope is complete;
- required validation is green for the exact candidate and recorded base;
- required durable side effects are observed;
- READY-candidate prequeue validation, fresh-base integration authorization, exact-head merge evidence, and durable queue reconciliation exist when protected `main` was mutated;
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

Changes to this contract, the canonical door, current-state schema, lane semantics, response guard, or ready-candidate publication or lane-state protocol are operations-lane work. Product lanes stay preserved while a stop-the-line operations freeze is active.

The operations system should become simpler over time. A new control file is justified only when it owns data that cannot live clearly in the existing contract, current state, lane registry, work item, evidence, or adapter. New execution controls require a reproduced failure plus an executable regression before they enter the critical path.
