# Multiversal Owner–AI Interaction Contract

**Document ID:** MV-CONT-CONTRACT-001  
**Version:** 1.1.0  
**Status:** ACTIVE  
**Owner and final authority:** John Brandon Turner

## 1. Command meaning

The command `Continue` means:

1. recover repository state;
2. inspect the primary active attempt and exact checkpoint;
3. reconcile it with branch, commit, pull-request, review, CI, and merge evidence;
4. execute the exact next unfinished operation;
5. save and push bounded progress automatically;
6. report only verified results.

It does not mean restate the plan, summarize prior work, ask for already-known information, or assume the planned endpoint was reached.

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

Before substantial execution, create and push a `started` checkpoint.

After every bounded successful mutation batch:

1. run the smallest relevant validation;
2. update the checkpoint with expected-revision protection;
3. commit the work and checkpoint together where practical;
4. push the active branch;
5. continue automatically.

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

`CURRENT_WORK_POINTER.json` may contain multiple active attempts, but exactly one is primary.

A new attempt must not silently replace another attempt. The pointer records track, priority, owner selection, repository, branch, checkpoint path, status, and update time. A tie or conflicting primary selection is a reconciliation failure.

## 9. Duplicate-agent safety

Every checkpoint has a monotonically increasing `revision` and an `expected_remote_head`.

An update must provide the expected revision. If the stored revision differs, the update fails instead of overwriting newer work. Executors must inspect the remote branch before retrying.

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

## 13. Mandatory typed interaction controls

The typed receipts defined by `governance/ai/interaction-system/enforcement/CONTROL_RECEIPT.schema.json` are mandatory whenever their trigger applies. They supplement task evidence; they do not replace commits, pull requests, CI, merges, checksums, or owner approvals.

- Use a `deliverable` receipt before claiming that an artifact was delivered or is downloadable. It must verify bytes or repository existence, an owner-accessible locator, and a checksum or immutable identity.
- Use a `capability` receipt before claiming a repository or connector operation succeeded. It must separate authorization, actor identity, contributor authority, connector availability, repository permission, attempted action, and successful evidence.
- Use a `source_coverage` receipt before completing work whose correctness depends on a declared source set. Missing or deferred required sources block completion unless the controlling contract explicitly permits the disposition.
- Use a `ui_verification` receipt before presenting current interface instructions as verified. Current observation or a current official source is required.
- Use a `notification` receipt before sending a recurring owner alert. A materially unchanged evidence fingerprint must be suppressed.
- Use a `request_alignment` receipt when the owner asks for comparison, estimation, verification, status, or decision support alongside related execution. The immediate question must be answered before the related execution report.
- Use an `owner_report` receipt for bounded-step closure. It must identify completed work, evidence, remaining work, owner decision state, and exact next action.

Validate an individual receipt with:

```bash
python tools/interaction_enforcement.py validate-receipt <receipt.json>
```

A failed required receipt blocks the associated verified claim, notification, review transition, or completion state. Receipt evidence should be retained in the work checkpoint, pull request, governed operational ledger, or another canonical record appropriate to the work type.
