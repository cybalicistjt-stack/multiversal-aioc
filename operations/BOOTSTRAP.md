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

## 3. Select the lane from user intent

Read `operations/LANES.json` and choose exactly one lane that matches the user's request.

- Explicit requests name or imply their lane and override the default lane.
- A bare `Continue` resumes the lane already established by the conversation. If this is a new conversation, use `CURRENT.json` and the user's opening request to resolve the lane.
- Lane selection changes scope and source bundle only. It never changes the global operating contract.
- Multiple persistent lanes may hold implementation authority at the same time. A conversation still selects exactly one lane; selecting it does **not** pause, revoke, or rewrite another lane merely because both change product code.
- When active lanes share a repository, they use separate implementation branches and the FIFO publication queue serializes `main` mutation. Each lane reserves a turn; only the active head prepares/reconciles/validates its publication candidate against the fresh turn base.
- Do not load or mutate another lane merely because it exists; cross-lane reads are limited to explicit dependencies, publication conflicts, or owner-directed coordination.

## 4. Load only the lane's active work record

For a persistent lane, read the work-item/checkpoint path named by `CURRENT.json`. For an on-demand lane, use only the sources named by `LANES.json` plus the user's request.

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

A repeated owner execution command on the same in-progress attempt is not a fresh cycle by default. Compare the checkpoint's material-progress sequence with the sequence observed at the prior execution command. If nothing material changed, record `OPS3.NO_MATERIAL_PROGRESS` and enter stall diagnosis/recovery before doing more ordinary work. Polling, unchanged reads, or restating status do not count as progress. Status requests must report the current progress receipt and any held publication turn so the owner can distinguish active work from a stall.

## 8. Publication serialization

Before any executor mutates `main` in `cybalicistjt-stack/Multiversal-app` or `cybalicistjt-stack/multiversal-aioc`, follow the FIFO publication-reservation protocol in `operations/OPERATING_CONTRACT.md` using `scripts/ops3_merge_lease.py`. This includes product merges, OPS3/control-plane closeout, `CURRENT.json` or checkpoint projection, compatibility projection, operations repair, and any contents/ref write. Protected `main` is never a direct-write surface.

Reserve one queue turn first. If another reservation is ahead, wait without rebasing/reconciling/revalidating a publication candidate. When the reservation becomes first, activate it against the fresh target `main`; only then prepare/reconcile once from that `turn_base`, validate while holding the publication window, bind the exact validated head/base, merge, verify the durable result, and release so the next reservation can activate. From activation until that exact merge or an explicit yield, target `main` is frozen at `turn_base` for every other lane and executor. If it advances anyway, treat that as an OPS3 protocol breach and diagnose the bypassing writer; do not normalize the breach by making the holder rebase/yield/re-reserve. Never force the coordination ref, skip the queue, or merge around the active holder. If the originating conversation stalls after a durable verified merge but before release, a replacement executor must record a durable recovery pointer and recovery-release that completed turn; a finished holder may not strand the FIFO queue.

An activated FIFO turn also has bounded liveness. Future schema-2.1 turns carry material progress timestamps/evidence and a 900-second idle limit. A stale turn cannot merge or be cosmetically revived; a replacement executor must recovery-release it after a completed merge or recover the unmerged turn only after proving target `main` is still `turn_base`. Generated-content or CI jobs must never push directly to protected `main`; generated outputs belong in the queue-bound candidate branch.

## 9. Evidence and completion

Use the smallest validation that proves the changed behavior, then the lane's required acceptance gate. Never claim a file, branch, commit, PR, test, merge, deployment, or completion without tool evidence.

`completed_verified` means the requested bounded work is implemented, required validation passed, durable side effects are verified, publication coordination is reconciled when applicable, and the current record has been reconciled. A process exit code, generated patch, open PR, running check, product merge without control-plane closeout, or narrative assertion is not completion by itself.

Multi-file governed-start/closeout projections should use one tree, one commit and one ref advance whenever the executor exposes Git object primitives; sequential one-file commits are fallback-only.

## 10. Context discipline

Prefer the shortest path from current state to the requested result. Do not restart repository archaeology after the lane and work item are known. Expand context only for a concrete contradiction, failure signature, or source dependency.

Historical records remain valuable for provenance and recovery, but they never become live instructions by being rediscovered.
