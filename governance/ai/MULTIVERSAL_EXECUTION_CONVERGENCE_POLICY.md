# Multiversal Execution Convergence Policy

**Document ID:** MV-AI-CONVERGENCE-001  
**Version:** 1.2.0
**Status:** ACTIVE — OWNER APPROVED  
**Owner and final authority:** John Brandon Turner  
**Effective:** 2026-08-27  
**Controls:** owner-intervention load, repeated repair/rerun behavior, diagnostic escalation, validation scope, and cross-repository closeout convergence

## 1. Purpose

The existing interaction and completion-integrity controls remain binding. This policy adds the missing requirement that governed development must not merely remain truthful while unfinished; it must actively converge toward a bounded result with minimal owner repetition.

The governing rule is:

> A repeated `Continue` is a measurable execution-cost signal. Repeating the same tranche without materially new evidence, a changed hypothesis, or a genuine blocker is a control failure, not ordinary progress.

This policy does not weaken provenance, permission, privacy, security, deterministic validation, final-head evidence, release gates, or `completed_verified` completion truth.

## 2. Owner-continuation service objective

For an ordinary bounded tranche without a genuine owner-only or unavailable-environment blocker:

- target at least **80%** completion from governed start through merge/closeout in one owner continuation;
- target at least **95%** completion within two owner continuations;
- more than two execution cycles without a genuine blocker requires control-plane incident treatment rather than another generic retry.

A conversation/runtime interruption may explain a failed execution cycle but does not erase it from live measurement.

## 3. Mandatory convergence state

Every governed implementation attempt with implementation authority must carry a `convergence_control` record containing at least:

- `owner_continue_count`;
- `execution_cycles`;
- `repair_cycles`;
- `no_progress_cycles`;
- `diagnostic_mode`;
- `last_failure_signature`;
- `last_failure_class`;
- `diagnostic_hypotheses`;
- `retry_basis`;
- the active service-objective thresholds.

Counts are monotonic within an attempt. A new conversation resumes these counters from repository state; it does not reset them.

Cross-repository convergence has two distinct gates. Repository-scoped AIOC CI validates AIOC state consistency without access to the private sibling application repository. Before an AIOC recovery or closeout merge, an authenticated operator must additionally run `scripts/validate_repository_health.py --app-root <canonical-app-checkout>` against the registered application main. A personal authentication token must not be copied into an Actions secret merely to collapse these gates; a future CI-native cross-repository gate requires a separately approved repository-managed read credential.

## 4. Failure classes

A material failed cycle is classified as exactly one primary class before another repair or rerun:

1. `feature_implementation` — the bounded implementation violates its contract.
2. `validation_contract` — the validator/profile/assertion is wrong, incomplete, stale, or broader than the declared acceptance contract.
3. `validation_infrastructure` — orchestration, artifact, comparator, workflow, or evidence plumbing failed independently of the product contract.
4. `runner_environment` — a required execution environment or listener is unavailable or contaminated.
5. `repository_state` — branch, pointer, lifecycle, merge, authority, or cross-repository state is contradictory/stale.
6. `owner_only` — progress genuinely requires an owner decision/action that cannot be performed by the governed automation/tool surface.

Unclassified repeated failure is not an acceptable retry basis.

## 5. Diagnostic escalation

The first bounded repair may proceed normally after identifying the failure signature.

If a second repair is required for the same work item or materially related failure family:

- `diagnostic_mode` becomes `true` before further mutation;
- the assistant records at least one falsifiable root-cause hypothesis;
- relevant failure evidence is inspected as a set rather than patching only the first visible assertion;
- related repairs are batched into one bounded repair cycle;
- the next final rerun occurs only after the repair batch is complete.

A third patch-and-rerun cycle is forbidden unless the repository records why the prior diagnosis was falsified or what materially new evidence changes the hypothesis.

## 6. One recovery pass and evidence-freshness lease

At the start of an execution cycle, perform one bounded recovery pass: resolve the authority registry and current pointer/checkpoint, establish the exact relevant repository head/branch/PR, and inspect the required current gate. Those facts form an evidence-freshness lease for the cycle.

Do not restart the recovery sequence, reread the same authorities, or re-prove unchanged facts unless a concrete invalidating event occurs. Validating events are limited to:

- an authoritative file, selected checkpoint, branch, base, or live main head changes;
- a merge, rebase, force-push, or conflicting active writer changes repository state;
- a required check reports a materially new result or failure signature;
- a tool reports stale, missing, contradictory, or inaccessible evidence; or
- the work crosses its declared final validation or closeout boundary, where live main is reread once.

A completed tool batch, elapsed time, context compaction, commentary/status request, uncertainty without contradictory evidence, or the existence of additional historical files is not an invalidating event. Local mutation on the already-established active branch requires focused candidate validation, not a full authority-recovery restart.

If an invalidating event occurs, record the event and refresh only the affected facts. A second full recovery pass in the same cycle without a named invalidation is a no-progress control failure.

## 7. No identical reruns

A failed or queued operation may not simply be rerun to create activity.

Before a retry, `retry_basis` must identify at least one material change in:

- source/code/configuration;
- validation contract/profile;
- repository state;
- runner/environment state;
- evidence availability; or
- the diagnostic hypothesis being tested.

If none changed, wait on the genuine blocker or enter control-plane incident status. Repeating the same command against the same state is not progress.

## 8. No-progress escalation

`no_progress_cycles` increments when an execution cycle ends without any of:

- a new substantive bounded artifact/commit;
- a newly inspected failure cause that narrows the hypothesis space;
- a changed blocker with current evidence;
- a passed required gate; or
- completed merge/closeout evidence.

Two no-progress cycles require one of:

- `blocked_control_plane`;
- `blocked_environment`;
- `blocked_owner`;
- or a documented diagnostic repair that changes the retry basis.

The owner must not be asked to supply another bare `Continue` merely to make the assistant inspect the same state again.

## 9. Validation-scope rule

Final validation is dependency-aware and tranche-bounded.

- A substantive application/package PR selects exactly one current governed Validation Core profile unless an explicitly reviewed integration tranche declares more.
- Predecessor regressions required by the current tranche belong inside that current profile.
- Completed historical tranche profiles do not automatically run merely because their files still exist.
- Historical proof remains sealed evidence unless the current change touches a dependency the proof protects or the acceptance contract explicitly calls for revalidation.
- An unrelated historical profile job count greater than zero is a validation-scope defect.

The application workflow `validate-current-family.yml` is the one automatic selector and repository-health path. It invokes `_validation-core-profile.yml` at most once for a substantive current-family tranche. `ACTIVE_FAMILY_CONTRACT.json` seals predecessor proof and changes only at a family boundary or an explicitly reviewed integration exception.

## 10. Cross-repository closeout convergence

Application merge evidence and AIOC state projection form one governed closeout transaction.

- Before projecting completion, re-read the live application `main` SHA and merged PR evidence.
- AIOC must not retain an active pointer to a merged/deleted implementation branch.
- A successful application merge with stale AIOC `in_progress` state is `repository_state` failure and stop-the-line until reconciled.
- Closeout should select the strict successor in the same governed reconciliation when no separate owner gate intervenes.
- A merge API response is not canonical application-main evidence until live `main` is re-read.

Before crossing an application merge boundary, prepare the exact AIOC closeout mutation and preserve enough execution reserve to validate and merge it. When the runtime exposes a usage warning or another bounded execution ceiling and that reserve is not credible, leave the validated application pull request unmerged. A validated open pull request is a recoverable boundary; a merged application with stale canonical governance is not.

If an external usage ceiling interrupts execution despite that reserve, classify it as `environment_unavailable`, preserve every pending authorized closeout step in the blocker handoff, and resume from repository evidence. The interruption may explain the incomplete cycle but cannot convert pending closeout into completion or erase it from the scorecard.

## 11. Live throughput scorecard

Synthetic interaction-pilot results and live operational throughput are separate evidence classes.

The live scorecard records minimized aggregate measurements including owner `Continue` turns per tranche, same-cycle completion rate, completion within two cycles, repair/no-progress cycles, execution interruptions, unrelated historical validation jobs, retries without changed evidence, post-merge stale-pointer incidents, and genuine owner/environment blockers separately from assistant/control failures.

Raw private conversation text, titles, and attachment content are not published in the scorecard.

## 12. CI retirement rule

The former all-profile self-hosted workflow `self-hosted-windows-runner-smoke.yml` is retired from the application live workflow namespace. It may remain in Git history only.

Repository health must reject reintroduction of that workflow, automatic invocation of all completed DPL/MAI/AAI profiles on ordinary current-tranche PRs, a substantive current-tranche PR that changes no governed profile, and more than one changed governed profile without an explicitly reviewed integration-tranche exception.

## 13. Executable termination gate

Before a final response from an execution turn, the runtime must evaluate an ephemeral state through `scripts/execution_termination_preflight.py`. Queued/running validation, open PRs, partial green results, pending merge/closeout and a completed tool-call batch are nonterminal. Repository checks validate the contract and regression cases; longitudinal live scorecard evidence, not synthetic cases alone, determines whether owner-intervention objectives are actually being achieved.

## 14. Completion standard

This convergence remediation is complete only when legacy CI fan-out is absent from live application workflows; the family-scoped selector is live and repository-health enforced; AIOC workflow lifecycle registration matches the live application namespace; convergence state, diagnostic escalation and termination preflight cases are machine-validated; the minimized live throughput scorecard exists; exact-head AIOC repository health passes; the remediation merges; and the active product tranche remains preserved rather than reset by the remediation.
