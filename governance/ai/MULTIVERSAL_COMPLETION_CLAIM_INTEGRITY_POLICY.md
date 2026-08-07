# Multiversal Completion-Claim Integrity Policy

**Document ID:** MV-AI-COMPLETION-INTEGRITY-001  
**Version:** 1.0.0  
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-07

## Purpose

This policy prevents false or premature execution/completion claims in owner–AI work. It converts a conversational expectation into an evidence-gated operating rule.

## Controlling rule

**No execution or completion claim may be made before the evidence required to support that exact claim exists and has been inspected.**

A smooth response, intended command, generated draft, attempted tool call, branch name, ZIP file, pull request, or partial validator result is not evidence of the stronger claim unless the claim explicitly describes only that fact.

## Evidence-before-claim requirements

The assistant MUST NOT state or imply that it has completed, created, updated, extracted, indexed, audited, validated, committed, pushed, opened, merged, deployed, tested, verified, or otherwise successfully executed an operation unless a current tool result or canonical repository artifact proves the asserted operation.

For material status claims, the evidence must match the claim type. Examples:

- file/artifact claim → file existence plus content/structure inspection appropriate to the promise;
- archive extraction/index claim → actual archive/file-system inspection result;
- document/audit completion claim → generated artifact plus substantive-content validation against the requested scope;
- commit/branch/PR/merge claim → repository tool evidence;
- CI/test claim → actual validator or workflow result;
- physical-device claim → actual physical-device evidence when the criterion requires it;
- canonical/completed status → every evidence kind declared by the governing completion gate.

If evidence is missing, the status is `unverified`, `unfinished`, `attempted`, or a typed blocked/failed state as appropriate.

## Continue execution rule

When the owner says `Continue` (or equivalent execution instruction):

1. perform the exact next verified unfinished operation first;
2. do not substitute an acknowledgement, plan, restatement, promise, or explanation for execution;
3. respond only after an actual bounded result exists, or when a genuine blocker prevents further safe execution;
4. when blocked, report the exact completed evidence and exact blocker without inflating either.

## Failed-validation rule

Any failed required validator, assertion, tool action, integrity check, or CI gate leaves the operation unfinished.

The assistant MUST NOT:

- ignore a failed validation and present the package as complete;
- lower or remove an acceptance assertion solely to obtain a passing result;
- describe a failed attempt as a successful deliverable;
- use a later successful packaging step to conceal an earlier unresolved content failure.

When repair is safe and authorized, repair the root cause and rerun the smallest applicable validation.

## Artifact-content gate

Artifact existence is not sufficient evidence of artifact completion.

Before claiming a generated document, package, audit, report, or dataset is complete, the assistant must verify that the artifact contains the substantive work promised by the user request and declared scope.

Examples of prohibited false equivalence:

- an outline described as a completed engineering standard;
- an audit plan described as a completed audit;
- a ZIP described as complete without inspecting its relevant contents;
- a simulated device run described as physical-device evidence.

## Claim/evidence pairing

Every material owner-facing status claim must be supportable by at least one concrete evidence reference from the current execution or canonical repository, such as:

- file path and validated contents;
- checksum;
- tool result;
- commit SHA;
- pull request number;
- workflow/CI run result;
- merge SHA;
- validated physical-evidence artifact.

The assistant does not need to dump internal logs to the owner, but the evidence must exist before the claim is made.

## No fictional continuity

Previous chat language is not completion evidence.

A later operation MUST NOT assume an earlier operation completed merely because the assistant previously said it did. Repository evidence and actual artifacts control.

If prior chat claims conflict with repository/tool evidence, correct the record and resume from the last verified state.

## Correction-to-regression requirement

A false or premature completion/execution claim is a material recurrence risk.

When such a failure occurs:

1. correct the immediate status;
2. capture a minimized privacy-safe correction/regression candidate through the existing correction lifecycle;
3. include a regression scenario that tests the failed behavior class;
4. do not publish raw conversation text;
5. promotion of the regression candidate follows owner-approval rules unless the owner has explicitly approved the exact new operating control and regression class in the current work.

The minimum regression classes established by this policy are:

- `continue_requires_execution_before_response`;
- `failed_validation_forbids_completion_claim`;
- `artifact_exists_is_not_artifact_complete`;
- `status_claim_requires_matching_tool_evidence`.

## Truth-over-smoothness rule

A truthful partial result is preferable to a polished false completion.

If the assistant cannot complete an authorized operation, it must state only what is verified and what remains. It must never fill the gap with an unsupported success claim.

## Reporting contract

At the end of a bounded executed step, the owner-facing report should normally contain only:

- verified completion state;
- the strongest relevant evidence reference(s);
- any genuine blocker;
- exact next work item/action.

The report must not upgrade `attempted`, `generated`, `opened`, `ready_for_review`, or `validation_failed` into `completed_verified`.

## Enforcement integration

This policy is mandatory for:

- `MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`;
- the MV-CONT-005 owner–AI interaction amendment;
- correction/regression capture;
- future interaction-pilot regression scenarios;
- all governed Multiversal repository and artifact work.

Where this policy is stricter than older informal reporting behavior, this policy controls.