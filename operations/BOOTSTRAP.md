# Multiversal Operations Bootstrap

**System:** Operations V3 (OPS3)  
**Status:** CANONICAL SINGLE DOOR  
**Owner and final authority:** John Brandon Turner

This is the only operational bootstrap for Multiversal. Every ChatGPT conversation, Codex session, human operator, CI helper, or future agent begins here. No other file may independently select current work, grant authority, redefine `Continue`, or declare the next action.

## 1. Load the one global contract

Read `operations/OPERATING_CONTRACT.md`.

Do not merge instructions from older bootstraps, handoffs, `.ai` files, application-repository status prose, conversation exports, recovery archives, or executor-specific runbooks. Those surfaces are compatibility, evidence, implementation context, or history only.

## 2. Load current operational state

Read `operations/CURRENT.json`.

`CURRENT.json` is the only mutable selector of live operational state. It identifies freezes, the active operations work item, and each lane's current state. If another source disagrees with it, `CURRENT.json` wins unless John explicitly changes the direction in the current conversation.

If `CURRENT.json` names a domain authority relevant to the requested scope, load that **CURRENT-referenced domain authority** before historical domain records, generated catalogs, or sealed completion evidence. It controls current canon for that domain only; it cannot select work, grant implementation authority, or expand the lane's scope.

## 3. Select the lane from user intent

Read `operations/LANES.json` and choose exactly one lane that matches the user's request.

- Explicit requests name or imply their lane and override the default lane.
- A bare `Continue` resumes the lane already established by the conversation. If this is a new conversation, use `CURRENT.json` and the user's opening request to resolve the lane.
- Lane selection changes scope and source bundle only. It never changes the global operating contract.
- The persistent implementation lanes are `msas`, `mrcs`, and `mvps`. They may hold implementation authority at the same time. A conversation still selects exactly one lane; selecting it does **not** pause, revoke, or rewrite another lane merely because both change product code. Completed UISR history is not a persistent implementation lane.
- Active lanes work independently on separate implementation branches and separate lane-state refs. Shared-repository publication is serialized only after a lane has an immutable, prevalidated READY candidate; no lane reserves future access to `main`.
- Do not load or mutate another lane merely because it exists; cross-lane reads are limited to explicit dependencies, publication conflicts, or owner-directed coordination.

## 4. Load only the lane's active work record

For a persistent lane, read the selected work-item/checkpoint path named by `CURRENT.json`, then read that lane's `execution_state_ref` for live execution progress. `CURRENT.json` selects work; the lane-state ref records execution only and may not select a different item. For an on-demand lane, use only the sources named by `LANES.json` plus the user's request.

Then reconcile the work record with live repository/PR/CI/tool evidence needed for the requested action. Repository evidence determines implementation facts; the work record determines authorization and scope.

## 5. Execute with executor independence

ChatGPT, Codex, local workers, GitHub Actions, and humans are executors or validators, never authority sources. An executor failure does not change project truth and does not force a new work item. Use another capable executor when the contract allows it.

Codex is optional. The local Windows worker is optional. No product work may become authorized merely because an executor is available, and no authorized work becomes unauthorized merely because one executor is unavailable.

## 6. Current stop-the-line rule

While `operations/CURRENT.json` has `product_start_freeze.active=true`, do not start new product implementation. Preserve the selected product item exactly as recorded and work only in the authorized operations lane until the freeze is cleared by verified operations closeout.

## 7. Continue/response gate

A governed `Continue` is one bounded execution, not permission to stop after an intermediate milestone. Once an attempt is in progress, its checkpoint must carry `execution_guard` evidence and keep `terminal_response_allowed=false` while ordinary authorized work or closeout remains.

Before returning a normal terminal response for an execution command:

1. fresh-read `operations/CURRENT.json` and the active checkpoint;
2. apply `scripts/ops3_execution_guard.py` or the exact equivalent logic;
3. continue working if the result is nonterminal;
4. stop only on verified completion or a recorded owner-only/external blocker.

Multiple owner Continues or owner stall nudges are execution-quality incidents and must be recorded truthfully; they may not be certified as clean single-Continue execution.

A repeated owner execution command on the same in-progress attempt is not a fresh cycle by default. Compare the checkpoint's material-progress sequence with the sequence observed at the prior execution command. If nothing material changed, record `OPS3.NO_MATERIAL_PROGRESS` and enter stall diagnosis/recovery before doing more ordinary work. Polling, unchanged reads, or restating status do not count as progress. Status requests must report the current coarse milestone, any READY publication candidate, and the first unresolved blocker so the owner can distinguish active work from a stall.


### Executor/session interruption rule + anti-overinstrumentation guard

A chat/session/tool runtime is never a project dependency. Do not silently wait, sleep, or run open-ended polling loops for CI, tools, another lane, or a publication position.

OPS3 uses **milestone receipts, not activity receipts**. Repository/PR/CI/publication-queue evidence is already durable truth and must not be copied into the lane journal after every observation.

For an ordinary persistent-lane attempt, the lane-state ref has only these execution milestones before successor reseed:

1. `start_execution` — selected attempt becomes `in_progress` and records the implementation branch;
2. `mark_prequeue_green` — one exact immutable application head has passed the complete required prequeue gate;
3. `mark_published` — that exact application head is durably merged and its READY candidate is reconciled;
4. `reseed_successor` — after the control-plane closeout is durably merged/reconciled, reset the lane once to the selected successor.

Do not write lane state for PR creation, workflow dispatch, CI queued/running status, individual Linux/Windows/cross-platform success, artifact or log inspection, READY queue submission, fresh-`main` reads, merge preparation, merge verification, publication-queue reconciliation, closeout PR creation, or closeout prequeue GREEN. Those are mechanical transitions already evidenced by their owning systems.

The **closeout fast path** is one bounded phase: prepare/validate the atomic closeout candidate → submit READY → fresh-main integration check → exact merge → durable queue reconcile → one deterministic successor reseed. There are no lane-journal writes inside that phase before the final successor reseed.

Treat a workflow run as one validation gate. While it is healthy/in-progress, inspect only workflow-level status as needed; inspect per-job logs/artifacts only after a terminal failure or when a concrete failure signature requires them. Do not narrate every mechanical tool transition as a separate milestone.

If a tool call returns no usable result, a session aborts, or execution resumes after an interruption, fresh-read the lane milestone plus the repository/PR/CI/queue evidence needed to determine what happened since that milestone; never replay completed work merely because it was not mirrored into lane state. An executor interruption is an executor/tooling incident, not permission to restart the tranche, reserve `main`, or block another lane.

## 8. Ready-then-queue publication

Before any executor mutates protected `main` in `cybalicistjt-stack/Multiversal-app` or `cybalicistjt-stack/multiversal-aioc`, follow the ready-candidate protocol in `operations/OPERATING_CONTRACT.md` using `scripts/ops3_merge_lease.py`.

Implementation, RED/GREEN construction, full tranche validation, checkpoint progress, and release work happen **before** or outside the shared publication queue. A candidate enters FIFO order only after it has an immutable PR head and green prequeue validation for that exact head. The queue has no active holder, no `turn_base`, no publication lease, and no release operation.

For the FIFO head, fresh-read target `main`, run only the drift-sensitive integration gate against that fresh base, merge the exact ready head with expected-head protection, verify the durable repository result, and reconcile the candidate from that observed merge. A failed head candidate is marked failed/removed without stranding later candidates. Build/release/deployment status never owns or blocks the source-publication queue.

Persistent lane execution state lives on independent refs `ops3-lane-state/msas`, `ops3-lane-state/mrcs`, and `ops3-lane-state/mvps`; one lane's progress write cannot block another lane.

## 9. Evidence and completion

Use the smallest validation that proves the changed behavior, then the lane's required acceptance gate. Never claim a file, branch, commit, PR, test, merge, deployment, or completion without tool evidence.

`completed_verified` means the requested bounded work is implemented, required validation passed, durable side effects are verified, publication coordination is reconciled when applicable, and the current record has been reconciled. A process exit code, generated patch, open PR, running check, product merge without control-plane closeout, or narrative assertion is not completion by itself.

Multi-file governed-start/closeout projections should use one tree, one commit and one ref advance whenever the executor exposes Git object primitives; sequential one-file commits are fallback-only.

## 10. Context discipline

Prefer the shortest path from current state to the requested result. Do not restart repository archaeology after the lane and work item are known. Expand context only for a concrete contradiction, failure signature, or source dependency.

Historical records remain valuable for provenance and recovery, but they never become live instructions by being rediscovered.
