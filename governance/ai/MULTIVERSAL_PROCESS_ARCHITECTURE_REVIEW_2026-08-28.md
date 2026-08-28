# Multiversal Phase 1-to-Present Process Architecture Review

**Document ID:** MV-PROCESS-REVIEW-2026-08-28
**Status:** GOVERNED REVIEW — MV-CONT-008
**Owner and final authority:** John Brandon Turner
**Scope:** planning, implementation, validation, repository topology and owner/AI operating behavior from the early foundation through the AAI-09 boundary

## Executive decision

Multiversal's product architecture is on the right track. The strongest decisions—local-first ownership, stable identities, explicit provenance and permissions, deterministic contracts, narrow domain owners, and definitions separated from variants, placements and live instances—have continued to compound well across a very large feature surface.

The delivery architecture did not scale as well as the product architecture. Repository state became spread across too many lifecycle projections, historical validators remained executable, each new tranche accumulated validation ancestry, and workers learned to treat recovery and governance ceremony as recurring work rather than a one-time boundary. The result was truthful but slow execution, high owner-intervention cost and, in the failed triage attempt, a recursive verification loop that diagnosed the problem without crossing into repair.

The correction is not less rigor. It is state-driven rigor: mutable facts live in canonical data, validators check relationships rather than copy those facts into code, historical proof stays sealed, recovery evidence remains fresh until a concrete invalidation, and one bounded tranche flows continuously through merge and closeout.

## Evidence reviewed

This review used:

- current and historical records in `multiversal-aioc` and `Multiversal-app`;
- live GitHub branches, pull requests, Actions history and exact main heads;
- the third named repository, `NCG`;
- the owner-supplied prior triage conversation and comparison work history;
- connected Drive and Airtable business records.

Authority remained repository-first. Drive and Airtable consistently identify GitHub/AIOC as the engineering source of truth and serve as durable business projections and indexes. The `NCG` repository currently contains only its initial README and is not an active engineering authority. Private conversation history supplied behavioral evidence but did not select or authorize product work.

## Evolution and assessment

### Foundation and early phases

The early work established a large canonical domain model and recovery discipline before accelerating feature delivery. That was the right strategic choice for a multiversal product: identity, provenance, source/profile scope, owner domains, offline behavior and deterministic boundaries were made explicit before later systems composed over them.

The durable success of this foundation is visible in later programs. New mechanics repeatedly reuse existing World, Character, Asset, Event, Project, permission and provenance owners instead of creating parallel ledgers. Recovered sources are classified and routed without automatic canon promotion. The 487-record Phase 1–8 source bundle remains a restorable collection rather than being silently rewritten.

The weakness was process density. Recovery, certification and proof mechanisms grew with the corpus. They were valuable when resolving damaged or ambiguous sources, but their shapes were later reused for ordinary feature delivery where a smaller current-state contract would have been sufficient.

### Program and tranche implementation

The recurring product pattern is strong:

1. resolve a narrow owner/domain contract;
2. implement stable types and behavior in the owning package/application surface;
3. add focused invariants and integration regressions;
4. validate the exact candidate on Linux and Windows when cross-platform behavior matters;
5. compare deterministic receipts;
6. merge, record exact evidence and select—but do not implicitly start—the strict successor.

PPIA, CCP, DPL, MAI and AAI demonstrate that this pattern can deliver complex, compositional systems quickly. AAI-01 through AAI-09, for example, progress coherently from provider/legal evidence through canonical schemas, adapters, playback, semantic resolution, bindings, authoring and multiplayer/privacy boundaries.

The implementation is generally better than the process surrounding it. Focused tests, fail-closed provider/permission behavior, stable IDs, deterministic ordering and explicit non-authority boundaries are the correct patterns. The codebase should continue to prefer composition over parallel state and should keep fixtures/proposals distinct from canonical or live evidence.

The main implementation risk is not a single bad subsystem; it is that rapid tranche production can turn reports and literal-evidence verifiers into substitutes for behavior. DPL-01 required three verifier-evidence repairs before its passing run, and AAI-06 required four repair cycles. These are signals to test contracts and behavior directly, batch diagnostic fixes, and avoid assertions whose only purpose is matching prose.

### Validation and control-plane growth

The AIOC repository contains 3,767 commits and 778 pull requests in the reviewed history, while the application contains 372 commits and 300 pull requests. Counts are not a productivity score, but the distribution is diagnostic: 276 AIOC commit subjects include governed starts, 593 include closes and 663 include selections. On peak days AIOC recorded more than 400 commits. Control records were frequently changing faster than product code.

Normal recent tranches commonly used one application PR plus two AIOC lifecycle PRs (start and close/select). That is the maximum acceptable control tax under the current canonical lease model, not a target to exceed. Earlier packages accumulated more: PPIA-16 preserved 70 hosted workflow results and five PRs for one tranche. Repeated predecessor profiles then turned this historical proof into current CI fan-out.

MV-CONT-007 correctly retired the all-profile workflow, reduced the application to one automatic family selector, sealed predecessor proof, flattened the AIOC entrypoint, retired five legacy behavioral suites and added an executable final-response gate. Its recovery was necessary and successful.

The first flat validator nevertheless repeated the deeper design error: it embedded the literal selected attempt, maintenance item, application SHAs, AIOC merge SHAs and Actions run IDs in executable Python. Every legitimate state transition therefore required editing the validator. The application selector also omitted root manifests, lockfiles, toolchains, general tests and many tools; the AIOC workflow neither triggered on nor executed its current control-plane unit tests.

MV-CONT-008 corrects those defects by deriving identity and evidence from canonical pointer/registry/proof data, keeping exact values in data rather than code, machine-enforcing the application dependency map, and executing focused current regressions inside the one AIOC health job.

## What the prior triage got right—and where it failed

The prior triage correctly identified validator inheritance, zombie CI, large job fan-out, repeated owner `Continue` turns, synthetic behavioral tests and governance accretion. Its aggregate conversation sample contained eight substantive conversations, 64 visible turns and 16 owner continuations; only 62.5% completed in the same cycle. Median visible assistant time was about 17 minutes 53 seconds. That is useful baseline evidence and is retained only in aggregate.

It then reproduced the failure it described. The worker repeatedly declared an internal "execution boundary" after reconciliation and verification passes even though no external blocker existed and no owner input was needed. Verification had become unbounded work. The assistant treated a completed diagnostic batch as a terminal event, requiring the owner to send another continuation to cross from diagnosis into mutation.

The corrected golden path is:

`recover once → establish authority/head evidence lease → implement continuously → diagnose actual failures only → validate once → batch repairs → rerun with changed evidence → merge → reread live main once → close out/select`

## Chat-worker failure modes to prevent

- **Reconnaissance restart:** rereading all authorities after every tool batch, context change or status request. Recovery is one pass unless a named invalidating event changes relevant facts.
- **Narrative completion:** reporting what should be fixed without making the authorized mutation. In execution mode, a plan or diagnosis is not a boundary.
- **Synthetic overclaim:** treating regression fixtures or a termination self-test as proof that live throughput improved. They prove the control shape; the live scorecard proves behavior.
- **Historical reactivation:** executing old validators or profiles because files still exist. Presence is provenance, not authority.
- **Planning-authority confusion:** treating a roadmap entry, prepared work order or selected successor as implementation authority.
- **Queue-as-blocker:** stopping because CI is queued, a PR is open or merge/closeout remains. Those are nonterminal asynchronous steps.
- **First-error patching:** repairing one visible assertion and rerunning before inspecting related failures. Related fixes must be diagnosed and batched.
- **Projection drift:** treating Drive, Airtable, app compatibility selectors or chat summaries as engineering truth over AIOC/GitHub.
- **Zombie misclassification:** closing old work by age alone. Application PR #61 is registered special-environment dormant work and #191 is owner-deferred; both are non-authoritative but intentionally preserved, not live pipeline work.

## Operating model from this point

### Product work

- Keep one selected product attempt and at most one exclusive maintenance lease.
- Use one application PR for one ordinary tranche.
- Keep the AIOC control tax at no more than the required start and close/select transactions; do not create separate acknowledgment, evidence-only or selection-churn PRs when state can be updated coherently at a real boundary.
- Plan family-wide invariants once, then resolve only tranche-specific scope at each start.
- Run focused construction checks during implementation and one exact-head final profile. Re-run only after a material code/contract/environment/evidence change.

### Validation

- One automatic application workflow, one selected current-family profile at most, and zero unrelated historical jobs.
- One AIOC workflow and one validator entrypoint; focused regression tests run inside that job and are not another validator.
- No work-item IDs, mutable SHAs, PR numbers or run IDs in validator source. Exact evidence belongs in pointer/checkpoint/registry/sealed-proof data.
- A shared dependency, lockfile, toolchain, test or validation-core change must invalidate the relevant current profile or health surface explicitly.
- Historical proofs remain immutable by Git object/digest and do not execute unless an owner-approved dependency exception reactivates them.

### Recovery and execution

- A bounded recovery pass creates an evidence-freshness lease for the execution cycle.
- Only an authority/head/branch change, merge/rebase/conflicting writer, materially new check result, explicit stale/contradictory tool response, or final closeout boundary invalidates relevant evidence.
- Refresh affected facts only. A second full recovery pass without a named invalidation counts as no progress.
- The executable termination preflight remains the final-response gate; it complements rather than replaces continuous execution judgment.

## Measures and review cadence

The existing live objectives remain:

- at least 80% of ordinary tranches complete in one owner continuation;
- at least 95% complete within two;
- zero unrelated historical validation jobs;
- zero identical reruns without changed evidence;
- zero post-merge stale-pointer incidents.

Add these interpretation rules to the monthly control review:

- recovery passes per execution cycle should be one unless named invalidation evidence exists;
- validator-source changes should correspond to policy/topology changes, not ordinary state transitions;
- ordinary product/control PR ratio should not exceed one product PR plus the two lifecycle transactions required by the current lease model;
- control-plane files and checks should be deleted or retired when replaced, not layered indefinitely;
- failed checks should be reported as product, validation-contract, validation-infrastructure, environment, repository-state or owner-only before another repair cycle.

Do not optimize for commit count, PR count, job count or visible agent activity. Optimize for bounded verified product outcomes, low owner intervention, small current execution surfaces and truthful recovery.

## Current direction

AAI-10 remains correctly selected but unstarted. Its product goal—multi-provider golden audio proof—is the right closure for the AAI sequence, but it should begin only after this maintenance lease is cleared and its provider/source matrix, live-versus-fixture authority, persistence decision and single bounded profile are resolved. Nothing in this review authorizes paid provider activation, credentials, content acquisition, migration 0022, tester distribution, release or deployment.
