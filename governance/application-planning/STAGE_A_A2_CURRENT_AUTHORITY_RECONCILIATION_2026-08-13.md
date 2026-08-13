# STAGE-A-A2 Current Authority Reconciliation

**Date:** 2026-08-13  
**Work item:** STAGE-A-A2 — Universal Object Experience  
**Purpose:** give ChatGPT, Codex, and repository operators one bounded authority map for A2 without rebuilding historical preparation or treating unmerged strategy work as canonical implementation state.

## Current conclusion

**STAGE-A-A2 remains the authorized current application item and is not activated.**

No later Stage A item, historical A2 preparation branch, PPIA/CAPP package, MXS strategy branch, WP-011 Apple work, or DS-008 work supersedes the application repository's current work order.

A2 implementation may start only from a repository-capable private checkout after the mandatory A2 runner, repository state, exact changed-path scope, preflight, and A2-01 task capsule gates are satisfied.

## Authority stack

### Layer 1 — current application implementation reality

**Repository:** `cybalicistjt-stack/Multiversal-app`  
**Canonical main:** `354e24007d2c453d090a2a6cdb31d3e3333c84c1`  
**Current work order:** `.ai/current-work-order.md`  
**Authorized item:** `STAGE-A-A2 — Universal Object Experience`  
**Governed implementation branch:** `stage-a/a2-universal-object-experience`

This layer controls what product code exists and whether A2 is activated. The governed A2 branch currently starts from the same application baseline; historical planning material does not imply hidden A2 product implementation.

A solidity correction on application branch `governance/repository-solidity-001-clean` aligns `.ai/next-task.md` with this work order. Until that correction is merged, `.ai/current-work-order.md` remains the stronger current application authority when older application control prose disagrees.

### Layer 2 — current AIOC recovery/state evidence

`governance/ai/runtime/CURRENT_WORK_POINTER.json` records application implementation as a deferred retained track with:

- `next_work_item_id = STAGE-A-A2`;
- state `authorized_current_application_item_checkout_runner_blocked`;
- reason: A2 is authorized but not activated because its mandatory runner needs a repository-capable checkout.

The AIOC conversational primary may point at a completed or governance-side recovery anchor without superseding the application work order.

### Layer 3 — exact A2 execution-source package

The recovered A2 execution authority includes:

- superseding Sunday master v2.7.1;
- preimplementation package v1.0.0;
- repository compatibility audit v2.7.0;
- exact `A2_CHANGED_PATH_SCOPE_v1.0.0.csv`;
- changed-path CSV SHA-256 `945b3619b25bd24e54267c8259fc17e667063a3056214e080cbe8034836d5aa6`;
- mandatory evidence/checkpoint/recovery runner and A2 preflight/task-capsule tooling.

These execution artifacts control A2 startup details once a repository-capable checkout is available.

### Layer 4 — historical A2 preimplementation reservoir

Historical branch `governance/stage-a-a2-detailed-design` contains 26 additive A2 handoffs covering behavioral/screen refinement, implementation contracts, real-data acceptance, search/filter/ranking, Picker/Scene insertion, version/variant/conflict/provenance, privacy/performance, promotion, runtime corpus, hostile failure, repository compatibility, and Sunday execution preparation.

**Disposition:** RETAIN / RECONCILE. Do not rebuild it and do not merge it wholesale.

Its valid design intent should be consumed through the current v2.7.1 execution package and refreshed against current application code, tooling, and newer domain authorities. Historical PASS results prove the historical baseline only.

### Layer 5 — completed PPIA implementation inputs

Canonical `PPIA_PROGRAM_BACKLOG.json` is `completed_verified_owner_approved_parallel_work`. PPIA does not activate A2 and explicitly retains `a2_activation_authorized = false`.

A2 should consume relevant completed PPIA authority, especially:

- PPIA-02 Creature/NPC presentation and permission-safe object behavior;
- PPIA-03 Item/Asset ownership, state, provenance, variants and reference cases;
- PPIA-04 Vehicle/Mecha/Starship object behavior;
- PPIA-05 Species/Form biology and projection boundaries;
- PPIA-08 Campaign/Scene/Session authoring seams used by Picker/Scene Add Object;
- PPIA-12 World/Setting authoring and extension boundaries;
- PPIA-13/14 onboarding, recovery, permissions, and microcopy;
- PPIA-15 awkward/scale/accessibility/mobile regression cases.

Where historical A2 assumptions conflict with a later completed PPIA contract in that PPIA contract's domain, the later completed PPIA authority controls.

### Layer 6 — completed CAPP implementation inputs

All CAPP-01 through CAPP-12 work items are `completed_verified`, `completed_work_items = 12`, and both `active_work_item_id` and `next_planned_work_item_id` are null. Repository Solidity Tranche 2 corrects the stale top-level CAPP backlog status to `completed_verified`.

CAPP is implementation input primarily for later Character/appearance surfaces. For A2 it may affect generic object inspection, provenance, permissions, accessibility description, variant/version/migration presentation, and asset-support diagnostics when appearance artifacts are inspected. CAPP does not alter Item/Asset truth, Species/Form biology truth, or A2 activation authority.

### Layer 7 — MXS owner-approved strategic input, pending canonical merge

Branch `governance/mxs-strategic-product-superset` is owner-approved and currently at `9d6dab320033147da191abda0cd3689ce257619c`, but it has no PR/merge and therefore is **not canonical merged repository authority yet**.

MXS may be used as an explicit owner-approved strategic constraint while its branch is preserved, but implementation completion claims must not pretend it is merged. For A2 its relevant direction is:

- competitors establish the user-value floor rather than copied architecture;
- apply Parity / Integration / Multiversal value gates;
- preserve profile-neutral universal-object infrastructure for multiple Play Experience Profiles;
- support progressive complexity rather than separate beginner/expert truth;
- preserve capability discovery, bounded scale, portability, human-experience and anti-dark-pattern constraints;
- do not put full native VTT work on the A2 critical path.

If MXS and current canonical implementation authority disagree materially, stop and reconcile rather than silently promoting the unmerged strategy branch.

## A2 non-authorities / retained parallel tracks

The following do not select or activate A2:

- `WP-011` Apple/iOS spike — separate Mac-dependent bounded track;
- `DS-008-working-series-attempt-002` — separate exact-byte Design Standards track, blocked_non_owner;
- IA-D09 — completed Internal Alpha design anchor, not A2 implementation;
- historical Stage A A3-A12 preparation — retained future-stage input only;
- historical open PRs/branches merely because they exist.

## A2 implementation invariants

A2 must preserve:

1. stable object identity and exact source/provenance visibility appropriate to role;
2. authorization filtering before search counts, facets, relationship traversal, previews, deep links, exports, or other projections can leak hidden existence;
3. read-only distinction among definitions, variants, versions, conflicts, recovered/source-only records, and runtime instances;
4. one reusable Picker/search/Inspector foundation rather than per-domain duplicate selectors;
5. Generic fallback for supported unknown/new domains without fabricating semantics;
6. desktop/mobile/touch/keyboard/high-zoom/reflow/accessibility behavior;
7. deterministic recovery/history/deep-link behavior;
8. bounded search/graph work over large libraries;
9. no mutation of canonical truth merely for presentation convenience;
10. no release/deployment/tester/paid-service authority inferred from A2 work.

## Exact activation sequence

On the repository-capable private checkout:

1. fetch/reverify the application repository and classify any local uncommitted changes before mutation;
2. verify local `main` and the governed A2 branch against their intended remote refs and do not discard unexplained local work;
3. enter/reverify `stage-a/a2-universal-object-experience`;
4. initialize/verify the mandatory evidence/checkpoint/recovery runner under the v2.7.1 master;
5. require `verify-state` PASS and zero unexplained substantive dirty paths;
6. continue the v2.7.1 master execution order from the applicable activation step;
7. verify the exact changed-path scope CSV and its recorded hash;
8. run `python -m tools.mv_dev preflight a2 --json`;
9. run `python -m tools.mv_dev task A2-01 --json`;
10. require exact A2-01 scope authority READY;
11. only then begin product implementation.

## Completion meaning of this reconciliation

This file does not activate A2, merge historical preparation, complete repository solidity, merge MXS, authorize release/deployment, or certify the local Codex checkout. It removes authority ambiguity so the later repository-capable A2 activation has one deterministic decision chain.
