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
- When active lanes share a repository, they use separate implementation branches and the publication lease serializes `main` mutation. Stale-base reconciliation is a publication concern, not a reason to collapse the lanes.
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

## 8. Publication serialization

Before any executor merges or pushes to `main` in `cybalicistjt-stack/Multiversal-app` or `cybalicistjt-stack/multiversal-aioc`, follow the publication-lease protocol in `operations/OPERATING_CONTRACT.md` using `scripts/ops3_merge_lease.py`.

Acquire the target-repository lease by compare-and-swap, fresh-read target `main` while holding it, require that `main` still equals the base SHA recorded by the successful validation run, merge only the expected validated PR head, verify the durable result, and release the lease with the merge SHA. Never force the coordination ref or merge around another holder.

## 9. Evidence and completion

Use the smallest validation that proves the changed behavior, then the lane's required acceptance gate. Never claim a file, branch, commit, PR, test, merge, deployment, or completion without tool evidence.

`completed_verified` means the requested bounded work is implemented, required validation passed, durable side effects are verified, publication coordination is reconciled when applicable, and the current record has been reconciled. A process exit code, generated patch, open PR, running check, product merge without control-plane closeout, or narrative assertion is not completion by itself.

Multi-file governed-start/closeout projections should use one tree, one commit and one ref advance whenever the executor exposes Git object primitives; sequential one-file commits are fallback-only.

## 10. Context discipline

Prefer the shortest path from current state to the requested result. Do not restart repository archaeology after the lane and work item are known. Expand context only for a concrete contradiction, failure signature, or source dependency.

Historical records remain valuable for provenance and recovery, but they never become live instructions by being rediscovered.
