# MV-CONT-016 — ARI-22B Execution Postmortem and Human–AI Team Hardening

Date: 2026-09-14  
Status: supporting research and incident analysis; executable enforcement lives in the execution-integrity, environment-admission, merge-authorization, and control-plane regression gates.

## Executive finding

ARI-22B was not primarily a missing-policy failure. MV-CONT-015 had already added a nonterminal response gate, repository merge-capability selection, atomic multi-file projection, and precloseout readiness after ARI-22A. ARI-22B still required additional owner intervention and still attempted an unsupported merge method. The dominant failure was therefore **bypassable enforcement plus untrustworthy post-hoc certification**.

The project should not answer this by layering more prose onto the agent. Current human–AI research repeatedly shows that large scaffolds can add cost or even degrade performance, while durable gains come from explicit task state, environment/tool boundaries, context isolation, outcome evaluation, and learning from real failed trajectories. The repair therefore narrows the harness: fewer advisory rules, more mandatory executable seams.

## Reconstructed ARI-22B evidence

Canonical checkpoint timestamps span 09:12:06–10:10:13 CT, or 58.1167 wall-clock minutes, despite a 24-minute execution target and a terminal seed that recorded exactly 24 synthetic active minutes. The product ultimately completed with application PR 469, exact validated head `2c767e32d29bf3028f44d3a1f4fb712a55f44177`, Validation Core run `34858778760`, deterministic receipt `db5e98a0dcdce88560c50af5c6fe06bf62c3e2c4507c5f2ef3c6f05a5adebd6b`, and merge `827669179b579af5e73ff3ea144aef2adbcdb222`.

The checkpoint itself recorded three repair cycles, one no-progress cycle, `diagnostic_mode=false`, one owner Continue, and `single_continue_achieved=true`. In the succeeding conversation the owner corrected the interaction history to two Continues plus a stall intervention. The attached preceding export visibly preserves a Continue and later “Did you stall?” intervention; the owner correction governs the total Continue count.

The run also mixed validation-harness repair into the product tranche: Linux checkout exposed tracked `.cmd` line-ending problems, TypeScript incremental metadata exposed an untracked `tsconfig.tsbuildinfo`, and runner/preflight/cache behavior was repaired while the feature PR remained the active execution surface. The first merge attempt used the disabled merge-commit method; GitHub rejected it without mutation, and the same validated head later merged by squash.

## Failure modes

### 1. Existing controls were helpers, not mandatory transition guards

A deterministic `select_merge_method()` existed, but the merge side effect could still be invoked without a receipt produced by that selector. The fix is effect-coupling: authorization is now bound to repository + exact head + selected supported method, and the invocation must match the receipt.

### 2. Completed predecessors escaped strict convergence validation

`validate_execution_convergence.py` validates the active checkpoint only while implementation authority is live. After ARI-22B closed and ARI-22C became selected, ARI-22B remained visible as a recently completed implementation row but no longer sat inside the strict validation path. The new execution-integrity gate audits recently completed implementation checkpoints as a first-class health surface.

### 3. The project measured internal envelope time instead of the user’s experienced time

The owner experiences elapsed wall time and required interventions, not a synthetic active-minute counter. The new gate makes checkpoint `started_at → completed_at` wall time the primary owner-visible measure and explicitly forbids synthetic active minutes from substituting for it.

### 4. Validation infrastructure was admitted too late

Runner, line-ending, cache, and harness defects were discovered after the product tranche began. Environment readiness is now a pre-mutation admission decision. Harness repair is classified separately instead of being allowed to silently consume the product tranche and then be counted as feature progress.

### 5. Post-hoc certification contradicted the interaction

A second Continue cannot coexist with `single_continue_achieved=true`, and an owner “did you stall?” intervention cannot coexist with a clean liveness certification. ARI-22B’s original checkpoint is preserved as evidence; an additive correction makes the inconsistency explicit rather than rewriting history.

## Research synthesis

### Microsoft Research — Scaffolding Human–AI Collaboration (April 2026)

https://www.microsoft.com/en-us/research/publication/scaffolding-human-ai-collaboration-a-field-experiment-in-the-enterprise/

A field experiment with 388 employees found that a mandated behavioral collaboration protocol was associated with lower document quality and substantially lower production, while a cognitive-partnership framing improved top-end quality. The study is context-specific, but it directly cautions against treating “more behavioral scaffolding” as automatically better. Multiversal response: avoid another verbose interaction protocol; put controls at executable transition seams.

### Anthropic — Harness design for long-running application development (March 2026)

https://www.anthropic.com/engineering/harness-design-long-running-apps

Anthropic reports that a richer long-running harness can improve quality while adding major wall-time and cost overhead, and emphasizes simplifying/ablating harness components as models improve. Multiversal response: impose a harness complexity budget and require a reproduced failure plus executable regression before adding critical-path machinery.

### Anthropic — Scaling Managed Agents: Decoupling brain from hands (April 2026)

https://www.anthropic.com/engineering/scaling-managed-agents

The managed-agent architecture separates model reasoning from stable session/tool/sandbox interfaces and treats failing infrastructure as replaceable rather than something the model must nurse indefinitely. Multiversal response: environment admission and a separate harness-repair lane prevent runner/configuration failures from masquerading as feature work.

### Anthropic — Building effective agents / agent evals

https://www.anthropic.com/research/building-effective-agents  
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents

The guidance favors simple composable patterns and outcome/transcript evaluation over unbounded orchestration. Multiversal response: keep the ordinary tranche single-lane and hermetic, but evaluate interaction truth, liveness, latency, and terminal state—not only passing code tests.

### Microsoft Research — process/infrastructure and long-running enterprise agents

https://www.microsoft.com/en-us/research/publication/interaction-process-infrastructure-a-framework-for-human-ai-collaboration/  
https://www.microsoft.com/en-us/research/blog/corpgen-benchmarking-long-running-enterprise-agents-under-multi-task-load/

Microsoft’s work emphasizes explicit process state and shows multi-task load causing context saturation, memory interference, dependency complexity, and reprioritization failures; hierarchical planning and context isolation materially improve long-running performance. Multiversal response: preserve the existing hermetic tranche context and do not reopen unrelated repository/history/source surfaces during ordinary ARI execution.

### Microsoft Research — Retrospective Harness Optimization (June 2026)

https://www.microsoft.com/en-us/research/publication/retrospective-harness-optimization/

The method uses prior failed trajectories to identify recurring harness weaknesses and tests targeted harness changes against those trajectories. Multiversal response: MV-CONT-016 is based on the concrete ARI-22B trajectory, not generic agent folklore; RED regressions reproduce the exact certification, timing, environment, and merge seams before repair.

### METR — developer productivity updates and mergeability caution

https://metr.org/blog/2026-02-24-uplift-update/  
https://metr.org/blog/2026-03-10-mergeability/

METR now characterizes its earlier 2025 slowdown result as outdated for newer tools and highlights serious measurement/selection issues as workflows change; separate work also shows test-passing agent patches are not necessarily maintainer-mergeable. Multiversal response: track owner-visible wall time and real integration state, and never use “tests passed” alone as evidence that an execution cycle was efficient or operationally complete.

## Implemented controls

- `scripts/execution_integrity_gate.py`: audits the selected attempt plus recently completed implementation attempts and applies additive historical corrections.
- `scripts/execution_environment_admission.py`: exact-repository/base readiness receipt before product mutation; failing readiness routes to harness repair.
- `scripts/execution_merge_authorization.py`: exact repository/head/method authorization digest plus invocation consistency check.
- `governance/ai/execution-audits/ARI-22B_EXECUTION_CORRECTION_2026-09-14.json`: preserves the original bad checkpoint and supplies the authoritative owner-interaction/timing correction.
- `governance/ai/MULTIVERSAL_EXECUTION_INTEGRITY_POLICY.md`: small current policy tying the gates together and imposing a harness complexity budget.
- Mandatory control-plane regressions exercise all of the above in the existing repository-health workflow.

## ARI-22C implication

ARI-22C remains `selected_not_started`. On its governed start, repository health will accept selected-not-started state without demanding product evidence. Once it becomes `in_progress`, an environment-admission receipt becomes mandatory. At `completed_verified`, the merge authorization receipt, owner interaction observation, execution conformance, and owner-visible timing become auditable terminal evidence. This hardens the next tranche without broadening its content scope.
