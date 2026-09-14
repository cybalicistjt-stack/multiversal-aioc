# MV-CONT-015 — ARI-22A Execution Review and Human-AI Team Hardening

Date: 2026-09-14
Status: supporting research and incident analysis; executable controls live in the current execution profile, scripts, and control-plane regressions.

## Purpose

Reconstruct ARI-22A from repository evidence, distinguish product-engineering time from execution-harness delay, compare the observed failures with current human-AI and long-running-agent practice, and convert the findings into deterministic controls before ARI-22B begins.

## Evidence-backed ARI-22A timeline

ARI-22A governed start was recorded at 2026-09-13T08:04:20-05:00. The focused RED validation run was created at approximately 08:16 CT. The bounded application implementation reached candidate head `20fb7c6b29cbf54215d7968736fdf25b4849c7e3` at approximately 08:19 CT. Exact-head Linux/Windows deterministic Validation Core run `34759534305` completed successfully at approximately 08:21 CT.

The product implementation therefore reached exact-head GREEN in roughly 17 active minutes from governed start. The material delay occurred after GREEN, across integration/closeout and human-AI execution boundaries rather than inside the product change.

Application evidence:
- PR 468
- validated head `20fb7c6b29cbf54215d7968736fdf25b4849c7e3`
- validation run `34759534305`
- deterministic receipt `a6f8b70fd47f52d4cc1bebd0a24ddd4a8d8b04c3d2e95982489d311ddde36706`
- merge `95f8ee8cdae919dfd8181bc1140a0463d96fac49`

Terminal evidence:
- AIOC canonical main `1b163ee577d2257de509448913540c7c7bbe327f`
- main health run `34850025599`
- terminal decision `ALLOW_FINAL_RESPONSE`
- reason `MVTERM-COMPLETED-VERIFIED`

## Observed execution failures

### 1. GREEN was treated as a conversational boundary instead of a machine nonterminal state

The implementation and exact-head validation were complete, but the owner had to return with another instruction to finish ARI-22A. The existing policy already said that GREEN, an open PR, or pending closeout is not terminal. The failure therefore was not lack of prose; it was lack of an explicit state-machine response gate carried by the reconciler.

Repair: every reconciled nonclosed state now emits `response_gate=CONTINUE_EXECUTION`; a closed lifecycle state emits `TERMINATION_PREFLIGHT_REQUIRED`, which still does not authorize a final response by itself.

### 2. Repository merge capability was assumed instead of discovered

The first application merge attempted the repository-disabled merge-commit method. Multiversal-app permits squash merge and disables merge commits and rebase merge. GitHub rejected the unsupported method without mutation; a second attempt using squash succeeded.

Repair: the transaction preflight now derives merge method from a fresh repository capability snapshot before the side effect. Unsupported requested methods stop before mutation.

### 3. Multi-file closeout mutation used a sequential contents path before being collapsed atomically

ARI-22A closeout ultimately became one Git-tree commit, but intermediate staging used sequential file writes and hit a stale blob-SHA mismatch. This added tool work and exposed exactly the transient inconsistency/stale-write risk that atomic projection is intended to avoid.

Repair: the atomic projection planner now rejects `contents_api` transport for multi-file projections. Multi-file execution projections require Git data primitives: create blobs, create one tree, create one commit, update one ref.

### 4. Closeout publication was attempted before the execution envelope could pass terminal proof

The first terminal seed truthfully reported 22 active minutes against a 24-minute target. Canonical-main terminal proof correctly rejected it with `MVTERM-ENVELOPE-TARGET-PENDING`. Continued same-cycle work brought the envelope to 24 minutes and the repaired proof passed.

Repair: a deterministic precloseout readiness gate now runs before closeout publication. If target time remains pending and safe-work exhaustion is not proven, it returns `CONTINUE_SAME_CYCLE` instead of publishing state that canonical-main proof must reject later.

### 5. Same-item terminal repair originally skipped re-proof

The first auto-proof implementation skipped a follow-up main commit when the latest completed work-item ID was unchanged. ARI-22A exposed that a repaired checkpoint for the same work item must be re-proved when checkpoint content changes. This was repaired during ARI-22A and is retained as prior hardening.

## Human-AI team synthesis

The external literature is consistent with the repository evidence: reliable human-AI execution depends less on adding narrative reminders and more on explicit shared task state, role boundaries, capability discovery, deterministic exit conditions, recovery, and timely escalation.

### Anthropic: long-running agent teams and harnesses

Sources:
- Building a C compiler with a team of parallel Claudes: https://www.anthropic.com/engineering/building-c-compiler
- Harness design for long-running application development: https://www.anthropic.com/engineering/harness-design-long-running-apps
- How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- Scaling Managed Agents: https://www.anthropic.com/engineering/managed-agents

Applicable findings:
- Long-running agents need a harness that keeps selecting the next task rather than stopping after a subtask.
- State and handoff artifacts must live outside one model context.
- Tool boundaries and objectives need to be explicit to avoid duplicate or incorrect work.
- Independent evaluator/verification roles improve reliability over self-evaluation alone.
- Time blindness and infrastructure noise should be handled by the harness, not left to model intuition.
- Checkpoints and resumable execution are preferable to restarting long workflows after minor failures.

### Microsoft HAX: human-AI interaction and team alignment

Sources:
- Guidelines for Human-AI Interaction: https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/
- HAX Workbook: https://www.microsoft.com/en-us/haxtoolkit/workbook/

Applicable findings:
- Make system capabilities and limitations clear before action.
- Time system action and interruption to the user's current context.
- Make correction and recovery efficient when the AI is wrong.
- Make consequences and responsibility changes visible.
- Align multiple roles around a shared implementation plan rather than leaving interaction behavior implicit.

### NASA Human-Autonomy Teaming

Source:
- Human-Autonomy Teaming: https://www.nasa.gov/human-systems-integration-division/integration-and-evaluation/human-autonomy-teaming/

Applicable findings:
- Human-autonomy delegation depends on feedback, transparency, calibrated trust, and shared understanding of tasks and responsibilities.
- Transfer or intervention should be timely and explicit rather than occurring because the automation silently stopped.

### OpenAI: agent workflow and intervention design

Source:
- A practical guide to building agents: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/

Applicable findings:
- Agent execution should run in a loop until an explicit exit condition is reached.
- Tools and guardrails should be clearly defined.
- Human intervention is especially appropriate after retry/failure thresholds or for high-risk actions, rather than as a default continuation mechanism.
- Real-world failures should feed new guardrails and evaluations.

## Adopted human-AI team contract

For governed Multiversal execution:
- The owner sets priority and resolves explicit owner decisions.
- The agent executes the authorized bounded unit to its terminal machine boundary.
- A progress update is never terminal authority.
- Repository/tool capabilities are discovered before irreversible or externally visible side effects.
- The agent interrupts only for a genuine blocker, an explicit owner decision requirement, or an out-of-scope high-risk action.
- Retry-threshold exhaustion escalates rather than silently looping.
- The canonical checkpoint, state reconciler, response gate, execution envelope, and terminal preflight form the shared task model.
- Context/session changes preserve execution identity and next action instead of transferring responsibility back to the owner.

## Executable controls introduced by MV-CONT-015

1. `select_merge_method(...)` in `scripts/execution_transaction_preflight.py`.
2. `assess_precloseout_readiness(...)` and `precloseout` CLI mode in the same preflight.
3. Envelope-aware closeout preparation when envelope fields are supplied.
4. `response_gate` in `scripts/execution_state_reconciler.py`.
5. Multi-file `contents_api` rejection in `scripts/execution_atomic_projection.py`.
6. Machine-readable `human_ai_team_contract` in `governance/ai/runtime/EXECUTION_PROFILE.json`.
7. RED-first regression coverage in `tests/control_plane/test_ari22a_execution_review_gate.py`, loaded by the canonical control-plane suite.

The research note is explanatory only. The scripts, machine-readable profile, canonical regression tests, and repository-health workflow are the enforcement authority.
