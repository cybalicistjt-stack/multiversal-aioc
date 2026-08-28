# Multiversal Owner–AI Interaction Contract

**Document ID:** MV-CONT-CONTRACT-001  
**Version:** 1.3.0
**Status:** CANONICAL IMPLEMENTATION CANDIDATE  
**Owner and final authority:** John Brandon Turner

## 1. Command meaning

The commands `Continue`, `fix this`, and `implement this` mean:

1. recover repository state;
2. inspect the primary active attempt and exact checkpoint;
3. reconcile it with branch, commit, pull-request, review, CI, and merge evidence;
4. execute the exact next unfinished operation;
5. carry the bounded unit through required validation, merge, canonical closeout, and strict-successor selection when authorized;
6. save and push bounded progress automatically;
7. report only verified results after the executable termination preflight allows finalization.

It does not mean restate the plan, summarize prior work, ask for already-known information, or assume the planned endpoint was reached.

`status report and continue` preserves execution authority after a concise status. `keep going`, `continue until you need me`, and a named finish boundary persist through that boundary. `get ready`, status-only, and analysis-only are explicit non-execution modes.

## 2. Permanent restart command

The owner may start any new conversation with only the exact text stored in:

`governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`

The prompt must remain static. Dynamic state belongs in repository records.

## 3. Authority and capability separation

The executor must separately establish:

- owner authorization;
- contributor authority;
- connector or tool availability;
- repository permission;
- successful operation evidence.

Authorization does not prove tool availability. Tool availability does not prove that an operation succeeded.

## 4. Status vocabulary

Only these checkpoint states are valid:

- `started`
- `in_progress`
- `validation_failed`
- `blocked_non_owner`
- `blocked_owner`
- `ready_for_review`
- `completed_verified`
- `superseded`

Only `completed_verified` means complete.

## 5. Automatic preservation

Before substantial execution, create and push one `started` checkpoint or recover the existing current attempt checkpoint.

During uninterrupted work:

1. run the smallest relevant validation;
2. commit coherent validated slices where recovery risk warrants it;
3. update the durable checkpoint only for start, material recovery-path change/blocker, ready-for-review, or `completed_verified`;
4. push the active branch before a long or failure-prone operation and at review boundaries;
5. continue automatically until the requested boundary or a genuine blocker.

Before a long, failure-prone, bulk, or context-heavy operation, push the current checkpoint first.

The executor must not hold more than one successful uncommitted atomic batch.

## 6. Interrupted work

A later conversation must treat every non-`completed_verified` checkpoint as unfinished.

- Pushed files with unrun tests resume at validation.
- Failed tests resume at reproduction and repair.
- An open PR resumes at review, CI, repair, and merge.
- A conversational claim without evidence is ignored.
- A stale roadmap cannot override newer repository evidence.

## 7. Completion evidence

Completion requires the work-type gate declared in the checkpoint. Depending on the task, evidence may include:

- pushed commit;
- pull request;
- exact-head review;
- required CI pass;
- merge or squash commit;
- generated artifact and checksum;
- required validation report;
- owner approval.

The completion checkpoint must have `active_substep: null`, a nonempty evidence list, and an exact next item or owner-only boundary.

## 8. Parallel work

`CURRENT_WORK_POINTER.json` contains one selected product attempt. It may also contain one exclusive control-plane maintenance lease that blocks feature starts without replacing the selected product attempt.

A new attempt or maintenance lease must not silently replace another attempt. Concurrent authoritative integration paths for one work item are a reconciliation failure.

## 9. Cross-repository closeout safety

Application merge evidence and AIOC state projection are one governed closeout transaction.

Before completion projection, re-read live repository heads and merge evidence. Do not leave an active pointer on a merged/deleted branch. Superseded PRs must be preserved but closed. A partial cross-repository merge is a `repository_state` failure and remains nonterminal while the authorized repair is possible.

## 10. Roadmap efficiency

Routine progress is stored in small runtime records, not in the full roadmap.

The roadmap is patched only when:

- a work item becomes `completed_verified`;
- dependencies or execution order change;
- an owner decision changes scope;
- a milestone changes;
- a material risk, deferral, or release gate changes.

A pending roadmap projection does not erase newer verified work.

## 11. Truthfulness

Never say a file, checkpoint, commit, branch, PR, review, CI run, merge, artifact, deployment, or completion exists without tool evidence.

If canonical persistence fails, say that the progress is not durably saved. Conversation memory is not a substitute.

## 12. Owner-only boundaries

Stop only for a genuine owner-only decision, spending, paid-plan enrollment, production credential, irreversible provider commitment, production deployment, internal-alpha/public release approval, or another explicitly reserved gate. Ordinary reversible ambiguities use the approved recommendation process.

When a tool action is unavailable, report the exact failed capability layer: host/filesystem, shell/network, repository authentication, plugin/MCP surface, sandbox/approval policy, or external model/session quota. State whether the capability was required, which fallback was used, and whether the failure consumed time or changed the completion boundary. Do not use vague “environment” language that can be mistaken for loss of the owner-authorized Windows host or repository access.

## 13. Executable termination gate

Before a final response from an execution turn, build an ephemeral state object conforming to `EXECUTION_TERMINATION_STATE.schema.json` and run:

`python scripts/execution_termination_preflight.py --state <temporary-state.json>`

Continue execution when the decision is `CONTINUE_EXECUTION`. A final response is permitted only for `completed_verified` at the requested boundary, a genuine blocker supported by current recovery evidence that blocks all authorized progress, or an explicit non-execution mode. Queued/running checks, open PRs, partial green evidence, pending merge/closeout, or a completed tool batch remain nonterminal.
