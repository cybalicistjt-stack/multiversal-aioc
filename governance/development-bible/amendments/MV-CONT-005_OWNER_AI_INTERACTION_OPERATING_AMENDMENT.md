# Multiversal Project Bible Operating Amendment
## Owner–AI Interaction, Continuity, and Evidence Controls

**Amendment ID:** MV-CONT-005-PB-AMENDMENT  
**Applies to:** `MULTIVERSAL_PROJECT_BIBLE_v2.0.md`  
**Status:** NORMATIVE PENDING NEXT CONSOLIDATED BIBLE RELEASE  
**Owner and final authority:** John Brandon Turner

## Purpose

This amendment incorporates the completed owner–AI interaction program into the Project Bible operating model without requiring the large canonical Bible file to serve as a high-frequency autosave surface.

## Normative requirements

1. **Permanent entry point.** A new conversation starts from the unchanged static prompt in `governance/ai/MULTIVERSAL_STATIC_RESTART_PROMPT.txt`.
2. **Repository-first recovery.** Changing state is recovered from the canonical bootstrap, current-work pointer, attempt checkpoint, compact implementation status, operational interaction scorecard, and relevant repository evidence.
3. **Completion truth.** Only `completed_verified` is complete. Started, in-progress, failed, blocked, and ready-for-review attempts remain unfinished.
4. **Automatic preservation.** Every governed operation creates a durable started checkpoint before substantive mutation and pushes bounded atomic progress without requiring the owner to request a handoff.
5. **Interruption safety.** A conversation ending, blocking messages, or lacking a final response cannot advance or complete work. The next conversation resumes the exact recorded substep.
6. **Evidence gating.** Completion, deliverables, capabilities, source coverage, UI guidance, notifications, request alignment, and owner reports use the applicable typed evidence controls.
7. **Correction lifecycle.** A material explicit owner correction must repair or block the immediate work and enter the governed correction-to-regression lifecycle as a minimized record when recurrence risk is material.
8. **Privacy.** Raw private conversation text, titles, and attachment content are not published. Public audit, training, evaluation, and correction records are minimized and paraphrased.
9. **Owner authority.** Proposed regression candidates may be created automatically, but only John Brandon Turner may approve or reject them for canonical promotion unless he has explicitly approved the exact operating control and regression class in the current governed change.
10. **Parallel-track safety.** A side mission changes primary selection only. It does not mark application or design tracks complete, superseded, or abandoned.
11. **Roadmap efficiency.** Routine progress updates use the checkpoint, pointer, compact status, scorecard, branch, and pull request. The full roadmap changes only at a verified milestone, dependency, scope, risk, release-gate, or owner-decision boundary.
12. **Operational measurement.** Deterministic pilot results are recorded separately from live longitudinal measurements. Unmeasured intervention reduction must remain explicitly unmeasured rather than inferred.
13. **Evidence-before-claim.** No material execution or completion claim may be made before matching tool/repository evidence exists and has been inspected. Permission, intent, an attempted command, or previous assistant prose is not success evidence.
14. **Continue execution.** When the owner says `Continue` or gives an equivalent execution instruction, execution happens before the response. An acknowledgement, plan, promise, summary, or explanation is not a substitute for the requested work.
15. **Failed-validation integrity.** A failed required validator, assertion, tool operation, integrity check, or CI gate leaves the work unfinished. Later packaging or file creation cannot conceal an unresolved failure.
16. **Artifact-content gate.** Artifact existence is not artifact completion. Before a document, package, audit, report, or dataset is called complete, its substantive content must be inspected against the promised scope.
17. **Claim/evidence pairing.** Every material owner-facing status claim must be supportable by a concrete current-execution or canonical-repository evidence reference appropriate to the claim type.
18. **No fictional continuity.** A later step may not infer completion from an earlier chat claim. Repository evidence and actual artifacts decide the starting state.
19. **Truth over smoothness.** A truthful partial result or explicit blocker is preferable to an unsupported polished completion claim.

## Completion-claim integrity policy

The detailed controlling requirements for items 13 through 19 are defined in:

`governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md`

False or premature execution/completion claims are material recurrence risks and enter the correction-to-regression lifecycle automatically.

The minimum approved regression classes are:

- `continue_requires_execution_before_response`;
- `failed_validation_forbids_completion_claim`;
- `artifact_exists_is_not_artifact_complete`;
- `status_claim_requires_matching_tool_evidence`.

## Current validated baseline

The prior MV-CONT-005 deterministic operational pilot passed 17 of 17 scenarios. It rejected the simulated false-completion attempt, privacy violation, unapproved promotion, and seven invalid typed receipts; suppressed duplicate correction capture; preserved two parallel tracks; and performed zero full application-roadmap rewrites.

That 17/17 result is a historical baseline for the controls that existed in that pilot. The completion-claim integrity controls approved on 2026-08-07 require their own targeted validation and future interaction-pilot incorporation; they must not be described as covered by the older 17-scenario run merely because this amendment now references them.

## Canonical implementation references

- `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
- `governance/ai/MULTIVERSAL_COMPLETION_CLAIM_INTEGRITY_POLICY.md`
- `governance/ai/runtime/CURRENT_WORK_POINTER.json`
- `governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json`
- `governance/ai/runtime/INTERACTION_OPERATIONAL_SCORECARD.json`
- `governance/ai/interaction-system/`
- `tools/continuity_state.py`
- `tools/interaction_audit.py`
- `tools/interaction_enforcement.py`
- `tools/correction_regression.py`
- `tools/interaction_pilot.py`

## Consolidation rule

The next consolidated Project Bible release must incorporate these requirements into the main Bible text and then mark this amendment superseded by that exact release. Until then, this amendment is authoritative for owner–AI interaction operations.
