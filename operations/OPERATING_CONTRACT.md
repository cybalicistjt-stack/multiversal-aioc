# Multiversal Operations V3 Operating Contract

**Document ID:** MV-OPS3-CONTRACT-001  
**Version:** 3.11.0  
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

### CURRENT-referenced domain authority

`operations/CURRENT.json` may name a domain-specific canon authority for a bounded product domain. When the requested work touches that domain, load the **CURRENT-referenced domain authority** after `CURRENT.json` and before historical domain sources, generated catalogs, sealed completion evidence, or compatibility projections. The referenced authority defines current canon for that domain; **historical domain material cannot override** it. A domain authority cannot select work, change lane priority, expand scope, or grant implementation authority.

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

OPS3 preserves exactly three independent persistent implementation slots. The current persistent lanes are `gpr`, `mrcs`, and `oarc`. A lane may be `completed_verified`, `selected_not_started`, or `in_progress`; one lane's completion or inactivity never pauses, folds into, or revokes another active lane. After a lane is terminal `completed_verified`, the owner may explicitly replace that persistent slot through operations governance while preserving the completed program as immutable history. MSAS-21, MVPS-23 and UISR-11 are preserved as completed program history and no longer occupy persistent slots. Operations work may repair lane selectors without collapsing this three-slot topology.


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
- batch related repairs before rerunning expensive terminal gates;
- treat one workflow run as one validation gate; do not journal or narrate each platform/job transition;
- inspect job logs or artifacts only for a terminal failure or a concrete unresolved failure signature;
- batch known reads/writes instead of turning each mechanical observation into its own tool/commit/status milestone.

Research is progress only when it resolves a concrete unknown needed for the result.


### Single-active-lane mode and quiet execution

When exactly one persistent implementation lane is nonterminal, OPS3 enters **single-active-lane mode**. Derive this mode once from the fresh `CURRENT.json` used to select the lane. Until an invalidating event occurs, ordinary execution must not rescan terminal sibling lane refs, enumerate "concurrent writers," read an empty publication queue, or perform routine branch update/rebase work. Terminal siblings are history; read them only for a concrete dependency or after an observed repository change proves they are relevant.

The durable lane ref is the **lane-state terminal gate**. `in_progress`, `prequeue_green`, or `published` forbids a normal terminal response to an owner execution command. Repeated owner execution commands remain useful diagnostic input for detecting stalls, but counting the interaction is not a lane milestone. Do not create a lane-state write solely for owner re-entry, stall nudges, status checks, queue checks, rebase checks, or mergeability polls. Aggregate any interaction-quality telemetry into an already-required terminal/closeout record.

Use **quiet execution** for governed tranches. While CI is healthy, inspect workflow-level status only at sparse, transition-driven points. Do not narrate or persist per-job progress, lane scans, queue emptiness, fresh-main observations, rebase checks, or mergeability polling as work. Job/step/log detail is failure-driven. Browser/session interruption resumes from durable lane state plus the smallest repository/PR/CI evidence needed.

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
2. read that lane's independent execution-state ref and start/resume the selected attempt;
3. work on the lane implementation branch without using lane state as an activity log;
4. run focused validation and the lane's full required prequeue acceptance gate on one immutable candidate head;
5. after that exact-head gate is green, write the single `prequeue_green` lane milestone.

Then choose publication coordination **once** from the number of nonterminal persistent lanes observed in the same fresh `CURRENT.json` read:

- **Exactly one nonterminal persistent lane — single-lane direct publication.** Do not consult or mutate the READY queue. Fresh-read target `main` once immediately before integration, run the smallest drift-sensitive integration gate against that base, and merge only the exact validated PR head with expected-head protection. Verify the durable `main` result, then write `published`. If `main` drifts after the receipt, rerun only that integration gate against the new base. Do not rebase or update the branch merely to make it current. If a real conflict requires a candidate-head change, invalidate prequeue GREEN and validate the repaired exact head.
- **Two or more nonterminal persistent lanes — multi-lane READY queue.** Submit one immutable READY candidate containing lane, work item, PR, exact head, prequeue receipt, and relevant write/dependency fingerprint. Only the FIFO head may integrate. Fresh-read `main`, run the drift-sensitive integration gate, merge with expected-head protection, verify the durable result, reconcile the candidate, then write `published`. A causally failed head is removed so followers are not stranded.

After application publication, prepare the atomic global selector/successor closeout candidate. Use the same publication mode that applies at that time: direct exact-head publication in single-active-lane mode, READY FIFO only when multiple persistent lanes are nonterminal. After durable closeout, perform one deterministic successor reseed. There are no lane-journal writes inside closeout before the reseed.

Build, packaging, deployment, release, and post-merge distribution consume merged artifacts independently and never own source publication.

### Independent lane execution state

GPR, MRCS, and OARC use separate compare-and-swap coordination refs:

- `ops3-lane-state/gpr`
- `ops3-lane-state/mrcs`
- `ops3-lane-state/oarc`

The state model is implemented by `scripts/ops3_lane_state.py`.

- `CURRENT.json` remains the global selector of which work item is authorized for each persistent lane.
- A lane-state ref may record only execution state for the work item/attempt selected by `CURRENT.json`; it cannot reprioritize another lane or expand scope. A successor appears in lane state only through the deterministic reseed after the matching canonical closeout selects it.
- Lane state is a coarse recovery state machine, not an event stream. Ordinary execution has three writes only: `started`, `prequeue_green`, and `published`; `reseed_successor` is the single post-closeout reset.
- Repository/PR/CI/publication-queue evidence owns intermediate mechanics. Do not duplicate PR creation, workflow/job states, per-platform success, artifact inspection, queue submission, fresh-main reads, merge preparation/verification, queue reconciliation, or closeout validation into lane state.
- The generic `record_progress` and `complete_execution` lane APIs do not exist. Executors must use the explicit milestone transitions in `scripts/ops3_lane_state.py`.
- One lane-state ref never contains another lane's progress. A stalled or lost executor therefore cannot block execution-state updates by another lane.
- Exceptional candidate invalidation may return `prequeue_green` to `in_progress` when changed repository evidence proves the exact candidate is no longer publishable; it is not a license for status journaling.

### Overinstrumentation guard

OPS3 protects throughput by treating instrumentation as overhead, not work.

- Use **milestone receipts, not activity receipts**.
- Do not write lane state for status reads, polling, PR creation, individual CI/platform results, artifact/log inspection, READY submission, integration binding, merge preparation, merge verification, queue reconciliation, or closeout-candidate progress.
- Repository/PR/CI/publication-queue evidence is the source of truth for those mechanics.
- Do not emit a user-facing progress message for every mechanical transition. Group updates around real execution phases or changed failure signatures.
- Do not create extra commits, control files, receipts, or projections merely to prove that an executor looked at something.
- A normal attempt's lane-state progress sequence reaches at most three before successor reseed. Additional ordinary progress receipts are a design smell and require an actual exceptional state transition, not “more visibility.”
- Successor reseed is generated by the shared lane-state helper. Never inspect or copy another lane merely to learn reset shape.
- The closeout fast path is validation → READY CAS → fresh-main check → exact merge → durable reconcile → successor reseed, with no intermediate lane-state receipts.

### Ready-candidate publication queue

This queue is **dormant in single-active-lane mode**. It is used only when two or more persistent implementation lanes are nonterminal and can produce competing READY candidates for protected repositories.

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
- On recovery, fresh-read `CURRENT.json`, the selected lane-state milestone, and the smallest repository/PR/CI/queue evidence needed to determine what happened since that milestone. Resume from durable repository truth instead of replaying the tranche or requiring every intermediate action to have been journaled.
- A session interruption never creates publication ownership. Other lanes and READY candidates remain able to progress.
- Repeated owner `Continue` commands or stall nudges remain execution-quality incidents and are recorded truthfully even when durable product progress survives.

### Protected-main interlock

The protected repositories remain `cybalicistjt-stack/Multiversal-app` and `cybalicistjt-stack/multiversal-aioc`.

- Every protected-main mutation is a pull-request merge of one immutable expected head. Direct contents/ref writes to protected `main` are prohibited.
- In single-active-lane mode, no publication queue is consulted or mutated. A fresh observed `main` plus a green drift-sensitive integration receipt for the exact PR head authorizes the merge.
- With two or more nonterminal persistent lanes, only the FIFO READY head may merge after the same fresh-base integration requirement.
- OPS3 never requires a routine rebase. Base drift invalidates only the integration receipt; rerun the narrow integration gate. Change the candidate head only for a real conflict or repair, then revalidate that exact head.
- Generated-content or CI work prepares outputs on the candidate branch and may not push directly to protected `main`.

### Atomic control-plane projection

When a global selector/successor projection really must change protected AIOC `main`, prepare its multi-file update as one tree/commit whenever possible and validate it before publication. In single-active-lane mode publish it through the direct exact-head fresh-base path; use READY FIFO only when multiple persistent lanes are nonterminal. Do not use global selector publication as the live progress journal for a lane.

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
