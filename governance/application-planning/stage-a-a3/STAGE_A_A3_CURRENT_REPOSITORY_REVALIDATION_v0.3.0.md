# STAGE-A-A3 Current Repository Revalidation v0.3.0

**Stage:** STAGE-A-A3 — Identity, Dashboard, and Workspace Selection  
**Status:** REVALIDATED — READY FOR BOUNDED ACTIVATION  
**Owner/final authority:** John Brandon Turner  
**Historical preparation branch:** `governance/stage-a-a3-preimplementation` at `ebba2ddff260a77d32656606a37e6d635cbeaea1`  
**Historical compatibility artifact:** `STAGE_A_A3_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`  
**Historical artifact SHA-256:** `b0396d3945a0c200a2b7d3821bb851c06c57fbc83a29373fc0a5758df32bf1b7`  
**AIOC revalidation baseline:** `4395a38770f1d0049da6fe908b331ce869548513`  
**Application revalidation baseline:** `92f3f2e029ca041d2e0fdb739c614d58c7e913e8`

## Result

The recovered A3 preparation is still compatible with the current repositories after applying the completed A2 and PPIA overlays. The historical package is retained as provenance/input, not wholesale-merged implementation truth.

The A3 activation gate is **PASS — READY_FOR_BOUNDED_A3_ACTIVATION**.

This result does not authorize release, deployment, public registration, production identity-provider selection, production credentials, paid services, database-vendor changes, or tester activation.

## Evidence used

1. The exact historical v0.2.0 compatibility archive was recovered from project sources and its `SHA256SUMS.txt` passed for every file.
2. Its own validator returned `STAGE-A-A3 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS` with 22 anchors, 10 gaps, 10 contracts, 37 historical path actions, 12 reuse decisions, and 12 gates.
3. A2 is now `COMPLETED_VERIFIED`: PR #134 squash-merged at `cdd0713864edc6b6fc3ad78c66b3d2edb5491b2d`, with closure receipt and real browser evidence.
4. Current application `main` is `92f3f2e029ca041d2e0fdb739c614d58c7e913e8`. Compared with the A2 merge, only five governance/evidence files changed; no product source changed after A2 merge.
5. The seven P9 foundations A3 depends on were rerun against the merged product code and all passed: P9-06-012 through P9-06-018.
6. Current Campaign authority remains deliberately narrow: `CampaignRole = owner | gm | player | observer`; global application Owner/Admin, creator, invited tester, Assistant GM delegation, and support access remain separate A3 concerns.
7. The current client still stores Workspace selection as local UI state. A3 therefore still has real additive work to do rather than replacing an already-authoritative implementation.

## Anchor revalidation

The historical package described 22 repository anchors.

- 12 exact-blob anchors remain byte-identical to the historical compatibility baseline.
- 8 presence-based anchors remain present and valid.
- 2 anchors changed intentionally and must be reinterpreted:
  - `apps/client-ui/src/App.tsx` now contains completed A2 Library, A2 authorization projection, A2 styles, and A2 hash-route integration.
  - `.ai/task-queue.md` now records A2 `COMPLETED_VERIFIED` and A3 `CURRENT NEXT — REVALIDATE / NOT ACTIVATED`.

No reuse foundation disappeared.

## Current A3 gaps

All ten historical gaps remain legitimate A3 work. None requires a production provider or a new runtime dependency.

1. **A3-GAP-001 — runtime identity adapter:** still absent; add a deterministic local alpha/test adapter behind provider-neutral identity contracts.
2. **A3-GAP-002 — invitations:** no invitation runtime/schema/service is present.
3. **A3-GAP-003 — application/workspace roles:** Campaign roles remain intentionally separate; A3 adds workspace/delegation/support semantics without broadening `CampaignRole`.
4. **A3-GAP-004 — workspace selection authority:** current selector remains client-local state. A3 must add discovery and entry decisions plus a nonauthoritative selected-context receipt while preserving A2 Library behavior.
5. **A3-GAP-005 — dashboard projection:** no authorization-first dashboard projection service exists.
6. **A3-GAP-006 — notification summaries:** notifications-work remains a boundary/placeholder; A3 may implement only inference-safe dashboard summaries.
7. **A3-GAP-007 — recent work:** no revocation-aware recent-work service exists.
8. **A3-GAP-008 — selected-context receipt:** still absent.
9. **A3-GAP-009 — Owner/Admin separation:** existing Campaign owner can read private GM material, so global operational Owner/Admin must never be mapped to Campaign owner automatically.
10. **A3-GAP-010 — entry/deep-link guard:** the shell now has A2 hash/history integration but still lacks authenticated workspace-entry authorization.

## New completed-A2 reuse seams

A3 must compose with, not duplicate or break:

- `apps/client-ui/src/a2/data/authorizationProjection.ts` — authorization-before-projection pattern;
- `apps/client-ui/src/a2/navigation/a2LocationState.ts` — hash/deep-link/history compatibility pattern;
- `apps/client-ui/src/a2/a2.css` — responsive/reduced-motion/focus conventions;
- `apps/client-ui/src/a2/a2.a11y.test.tsx` — accessibility regression pattern;
- `apps/client-ui/src/a2/library/LibraryPage.tsx` — completed Library route and authorization semantics;
- `.github/workflows/validate-stage-a-a2-universal-object-experience.yml` — A2 regression lane where A3 integration touches shared shell behavior.

## Superseded historical assumptions

The following v0.2.0 assumptions are no longer current:

- A2 is incomplete and blocks A3 activation.
- `dced7f92163050690c807c1fda937146bb8dce85` is the current application baseline.
- the shell is A1-only and has no A2 route/history/authorization integration.
- the old task queue still names A2 as current next.
- A3 needs to modify `apps/client-ui/package.json` to obtain an accessibility lane. The current stack already includes axe/Testing Library; focused A3 CI can run the A3 test explicitly without changing dependencies or the lockfile.
- the old handoff instruction to proceed to A4 preparation is an execution instruction. It is historical only; A3 is now the sequential current-next revalidation target.

## Current overlays

The following later completed authority must be applied during A3 implementation:

- PPIA-13 onboarding/help content;
- PPIA-14 permission-safe error/recovery microcopy;
- PPIA-15 awkward/scale/accessibility/mobile regression cases;
- PPIA-16 Developer Console/control-surface authority remains separate from ordinary Player/GM/Creator workspace authority;
- completed A2 keyboard/focus, responsive/reflow, reduced-motion, high-zoom, authorization-before-projection, history/deep-link, and recovery patterns.

## Current changed-path authority

`A3_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv` replaces the historical 37-action snapshot for activation planning.

It contains 49 classified rows:

- 31 `CREATE`;
- 1 `MODIFY_BOUNDED` (`apps/client-ui/src/App.tsx`);
- 15 `REUSE`;
- 2 `PRESERVE`.

The scope deliberately preserves `apps/client-ui/package.json`, A2 Library behavior, and existing A1/A2 validation lanes. No dependency or lockfile change is planned.

## Activation gate

PASS requires all of the following, all of which are currently satisfied:

- A2 `COMPLETED_VERIFIED`;
- exact historical A3 source bytes recovered and checksum-verified;
- historical A3 validator PASS;
- current product source stable after A2 merge;
- provider-neutral identity/authorization/entitlement/session foundations present;
- P9-06-012 through P9-06-018 regression validators PASS;
- no existing `packages/contracts/src/a3` implementation collision;
- no new runtime dependency required;
- no production identity-provider decision required;
- no database-vendor change required;
- no paid service, production credential, release, or deployment authority required.

**Verdict:** `PASS — READY_FOR_BOUNDED_A3_ACTIVATION`.

## Exact next action

After focused validation and merge of this revalidation package:

1. create the bounded application branch/work order for STAGE-A-A3 from current `Multiversal-app` `main`;
2. install `A3_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv` as the current activation scope authority;
3. preserve provider neutrality and release/deployment false;
4. begin A3-01 with the StableSubjectSessionPort/local alpha adapter/IdentityEntry seam and rerun the P9 identity regression before broader A3 work.
