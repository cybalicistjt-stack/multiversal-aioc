# MV-CONT-014 — Execution Critical-Path Optimization Research

**Date:** 2026-09-13  
**Status:** SUPPORTING RESEARCH — adopted controls are authoritative only where encoded in CURRENT machine policy/tests/workflows.

## 1. Experiment basis: ARI-21

ARI-21 was the first clean post-ARI-20 routing experiment. It completed in one owner Continue with zero repair and zero no-progress cycles. Approximate observed milestones were:

| Milestone | Elapsed from owner command |
|---|---:|
| governed-start PR open | ~3:09 |
| product RED dispatched | ~6:10 |
| intended RED observed | ~6:47 |
| exact-head GREEN | ~9:40 |
| application merge | ~11:08 |
| canonical AIOC main health | ~14:10 |
| separate terminal proof | ~16:37 |

The product path was no longer dominated by rediscovery or repair. The remaining avoidable latency was orchestration and repeated validation setup.

## 2. Measured validation critical path

ARI-21 Validation Core run 34756512864 showed:

- Windows shared validation was the slow lane.
- Windows dependency install was ~2.3 seconds.
- The focused Vitest regression was ~1.39 seconds.
- Nearly all remaining profile time was the full `tsc -b --pretty false` typecheck.
- Reusable profile jobs used full-history checkout and clean checkout deleted `apps/client-ui/tsconfig.tsbuildinfo`, preventing safe incremental reuse.
- AIOC repository health also used full-history checkout even though the new terminal comparison only requires the candidate and parent.

These are observed repository/run facts, not external research claims.

## 3. External engineering patterns reviewed

### Small batches and fast integration

Google engineering practice recommends small, self-contained changes because they are easier to review and integrate quickly:
- https://google.github.io/eng-practices/review/developer/small-cls.html
- https://google.github.io/eng-practices/review/reviewer/speed.html

DORA likewise connects continuous integration and small batches with faster, more stable delivery:
- https://dora.dev/capabilities/continuous-integration/
- https://dora.dev/capabilities/working-in-small-batches/

**Adopted:** preserve the bounded tranche and exact-head acceptance model; remove orchestration layers around it rather than widening the work unit.

### Impact analysis and affected work

Microsoft Test Impact Analysis and Nx affected execution reduce unnecessary test/build work using dependency information and retain fallbacks when impact is uncertain:
- https://learn.microsoft.com/en-us/azure/devops/pipelines/test/test-impact-analysis
- https://nx.dev/docs/features/ci-features/affected
- https://nx.dev/docs/getting-started/setup-ci

**Deferred:** ARI does not yet have a trustworthy test-granularity dependency graph sufficient to skip required full acceptance checks. No impact-based skipping is authorized by MV-CONT-014.

### Cache and incremental compilation

TypeScript's incremental compiler persists project-graph information in `.tsbuildinfo` specifically to accelerate subsequent builds, including build/noEmit workflows:
- https://www.typescriptlang.org/tsconfig/incremental.html
- https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-4.html
- https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-0.html

GitHub Actions supports dependency/build caching with key and restore-prefix semantics:
- https://docs.github.com/actions/using-workflows/caching-dependencies-to-speed-up-workflows

Uber has reported major monorepo CI gains from changed-target analysis, caching, and submit-queue optimization:
- https://www.uber.com/blog/how-we-halved-go-monorepo-ci-build-time/
- https://www.uber.com/blog/bypassing-large-diffs-in-submitqueue/
- https://www.uber.com/blog/slashing-ci-costs-at-uber/

**Adopted:** preserve per-OS TypeScript incremental metadata while keeping the full typecheck; minimize checkout history to the consumer's actual need.

### Parallelism and critical-path ordering

Buildkite guidance emphasizes parallel jobs, failure-prone/fast checks early, and timing-aware test splitting where appropriate:
- https://buildkite.com/docs/pipelines/configure/workflows/controlling-concurrency
- https://buildkite.com/docs/pipelines/configure/workflows/parallel-builds

**Already aligned:** Linux and Windows acceptance lanes remain parallel and deterministic comparison remains a downstream convergence proof. MV-CONT-014 does not weaken or serialize them.

## 4. Adopted MV-CONT-014 controls

1. **Direct atomic projection** — multi-file start/closeout control-plane transitions use Git object primitives (`create_blob` -> `create_tree` -> `create_commit` -> `update_ref`) from one validated base. Per-tranche temporary workflow creation/deletion is prohibited when those primitives are available.
2. **Embedded terminal proof** — canonical-main repository health performs terminal reconciliation after its authority/regression checks when that main push introduced a new completed implementation item. No separate terminal-proof workflow is needed.
3. **Stable terminal identity before start** — ARI-22A preallocates cycle, trace, operation and side-effect identities while remaining `selected_not_started` with no branch/authority. Start and closeout update the same identities rather than inventing terminal history afterward.
4. **Incremental typecheck reuse** — self-hosted Linux/Windows Validation Core lanes cache compatible `apps/client-ui/tsconfig.tsbuildinfo` state per OS and restore compatible prior state without skipping the full typecheck.
5. **Minimum checkout history** — exact-head profile jobs use shallow history; comparator uses a sparse checkout; AIOC main health keeps only candidate+parent history needed for automatic terminal comparison.
6. **Infrastructure-only validation isolation** — changes only to Validation Core infrastructure validate repository/workflow health without manufacturing a product-family run.

## 5. Explicit non-adoptions

- No probabilistic test selection.
- No skipping Linux or Windows full typecheck.
- No removal of deterministic cross-platform receipt comparison.
- No blind retry or flaky-test masking.
- No pre-start implementation authority for ARI-22A.
- No ARI-22B/22C activation.

## 6. ARI-22A experiment targets

ARI-22A is the next process experiment. Measure against ARI-21:

- zero temporary start/closeout/terminal workflow files;
- governed start materially faster than ~3:09;
- intended RED preferably under 5 minutes, stretch goal under 4;
- compare cold RED Windows typecheck to warm-compatible GREEN typecheck (ARI-22A RED may be the cache-primer);
- terminal decision produced in the same canonical-main health run;
- one owner Continue, zero repair cycles, zero no-progress cycles;
- total terminal time target approximately 12–14 minutes when runner queue latency is comparable.

The timing target is an experiment target, not permission to weaken acceptance or terminate early.
