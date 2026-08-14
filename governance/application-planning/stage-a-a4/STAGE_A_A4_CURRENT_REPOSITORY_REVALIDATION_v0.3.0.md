# STAGE-A-A4 Current Repository Revalidation v0.3.0

**Stage:** STAGE-A-A4 — Character Workspace  
**Status:** REVALIDATED — READY FOR BOUNDED ACTIVATION  
**Owner/final authority:** John Brandon Turner  
**Historical preparation branch:** `governance/stage-a-a4-preimplementation` at `75eeda3d00747d75b36903a7acd0e48a30e09c8d`  
**Historical compatibility artifact:** `STAGE_A_A4_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`  
**Historical compatibility SHA-256:** `340791f2eae9f1db50904d455aa18de8246463b08d0394da02b3a38f91ae8439`  
**Nested preimplementation artifact:** `STAGE_A_A4_CHARACTER_WORKSPACE_PREIMPLEMENTATION_v0.1.0.zip`  
**Nested preimplementation SHA-256:** `b3f207e1cae8649afda372d902579bdaade5e3f07470a0ecb149de3978d2c7d9`  
**AIOC revalidation baseline:** `1b2de74245b082f51c92abfefa09d07353ae3e10`  
**Application revalidation baseline:** `9173f132ea773cb697364ad0636b8b951fd36699`

## Result

The recovered A4 Character Workspace preparation remains compatible with the current repositories after applying completed A2, A3, PPIA-03/PPIA-05/PPIA-06 and CAPP-01..12 authority. Historical preparation remains provenance/input and is not wholesale-merged implementation truth.

**Activation verdict:** `PASS — READY_FOR_BOUNDED_A4_ACTIVATION`.

This authorizes bounded A4 implementation only. It does not authorize release, deployment, tester activation, production identity-provider selection, production credentials, paid services, public exposure, or a database-vendor decision.

## Exact source recovery

The exact historical archives were recovered from project sources. The v0.2 compatibility archive hashes to `340791f2eae9f1db50904d455aa18de8246463b08d0394da02b3a38f91ae8439`; its nested v0.1 preimplementation archive hashes to `b3f207e1cae8649afda372d902579bdaade5e3f07470a0ecb149de3978d2c7d9`. Historical checksum validation and both package validators pass. These results establish provenance only; current readiness comes from this revalidation.

## Current predecessor state

Historical blocking gaps **A4-GAP-003 and A4-GAP-004 are resolved**.

A2 is `COMPLETED_VERIFIED`; `ObjectPicker.tsx`, `pickerState.ts`, and `revalidateSelection.ts` now exist and are mandatory reuse seams. A4 mechanical selection must not create a duplicate governed-object browser.

A3 is `COMPLETED_VERIFIED` through application PR #136 / squash merge `7c1392977962a54b91af4519ed258a2a86823665`. Current A3 contracts explicitly support Character context: `A3WorkspaceType` includes `character`, `SelectedContextReceipt` includes `characterIdWhenApplicable`, and `WorkspaceEntryPort` requires fresh entry authorization and explicitly rechecks Character control. A4 must consume these contracts rather than invent a second identity/workspace/context layer.

## Current persistence re-check — A4-01 gate

The historical package required persistence to be rechecked after A2/A3. Current `database/migrations/` still contains only `0001_initial_logical_schema.json`, the provider-neutral 17-table foundation. There are no Character aggregate/draft/control/event/snapshot persistence categories, and no current `packages/contracts/src/a4`, `apps/client-ui/src/a4`, or `schemas/a4` namespace.

Therefore A4-01 remains necessary. Character persistence is additive rather than a rewrite of `0001`; the next logical migration is now `database/migrations/0002_character_workspace.json`. A4-01 may govern logical Character record categories but must not choose a production database vendor or move renderer/presentation metadata into Character mechanical truth.

## Current gaps

The intended A4 work remains real and additive: Character persistence/draft/repository contracts; all 18 validation classes and deterministic calculation; separate Character control; seven-class role-safe projection; autosave/conflict/ambiguous-outcome recovery; advancement/correction exact-once history; migration and historical-entitlement continuity; permission-filtered export; the actual Character workspace; and the bounded Character-to-Scene exit reference. None requires a production provider, new runtime dependency, paid service, or vendor selection.

## Current higher/newer overlays

- **PPIA-03** remains actual Asset/equipment mechanics and ownership authority. A4 may reference/summarize Character Asset state; full inventory/crafting/vehicles remain A8.
- **PPIA-05** remains Species/Form biology and mechanical eligibility authority. A4 stores governed selections/references and resulting Character state; it does not redefine biology.
- **PPIA-06 + CAPP-01..12** control appearance architecture and production preparation. A4 may retain player-authored appearance descriptors and governed appearance choices/references where allowed; renderer/presentation metadata remains outside Character mechanical truth. A4 must not recreate or supersede CAPP.
- **PPIA-13/14/15** constrain onboarding/help, permission-safe recovery/error language, mobile/high-zoom/accessibility and awkward-state regression cases.

## Current repository-path reconciliation

`A4_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv` replaces the historical 37-action snapshot. It contains 52 rows: 36 `CREATE`, 2 `MODIFY_BOUNDED`, 13 `REUSE`, and 1 `PRESERVE`.

Key reconciliations:

- A2 and A3 are now `REUSE`, not `REUSE_FUTURE`.
- the conditional migration resolves to `database/migrations/0002_character_workspace.json` because current main still has only `0001`;
- client tests are colocated under `apps/client-ui/src/a4` to match the current Vitest package boundary instead of disconnected root `tests/a4` suites;
- `apps/client-ui/package.json` remains preserved because the existing stack is sufficient;
- `apps/client-ui/src/App.tsx` remains a bounded integration point;
- `apps/client-ui/src/a3/services/localAlphaIdentityAdapter.ts` is authorized for one bounded synthetic A4 extension so the final local-alpha Character flow exercises A3's existing fresh-entry contract rather than bypassing it.

Current scope SHA-256: `489b38e60ec3401a81dc9702a14a48dab692f9aca67022ba01e72aaa2c80da79`.

## Activation gates

PASS conditions are satisfied: A2 and A3 are `COMPLETED_VERIFIED`; exact A4 historical bytes are recovered/validated; the post-A2/A3 persistence re-check is complete; A2 Picker and A3 Character-context seams exist; current A4 runtime/schema namespaces are absent; PPIA/CAPP overlays are identified; persistence can be extended additively without a vendor decision; the current test/accessibility stack is sufficient; and no provider, paid-service, credential, release, or deployment decision is required.

**Verdict:** `PASS — READY_FOR_BOUNDED_A4_ACTIVATION`.

## Construction/validation efficiency rule

A4 follows the owner-directed **build-first rule**: build meaningful slices before broad validation, use the smallest relevant deterministic checks during construction, batch repairs, do not run the full A1/A2/A3/DT/evidence matrix after every A4 commit, and reserve broad predecessor regression plus real browser evidence for the meaningful A4 package/closure boundary.

## Exact next action

After focused validation and merge of this revalidation package: create the governed A4 application branch from current app main; install the A4 work order and current scope authority; begin A4-01 by building provider-neutral Character persistence records, draft/repository ports, schemas, deterministic persistence fixtures and additive `0002_character_workspace.json`; keep provider/vendor/release/deployment false; and use focused A4-01 checks before continuing construction.
