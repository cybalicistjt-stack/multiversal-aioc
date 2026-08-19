# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.11.0  
**Status:** ACTIVE — FINAL COMBINED WORKSPACE ACCEPTANCE  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and operating rule

Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence. Historical detail remains in Git history and completed checkpoints rather than being recopied into every roadmap revision.

Implementation transitions use one bounded state synchronization after a verified application merge, one AIOC repository-health gate, and one final selector verification. Ordinary implementation operations do not trigger repeated roadmap/pointer rewrites.

## Completed verified foundations

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06 and POST-GATX-SUCCESSOR are **COMPLETED_VERIFIED**.

The APW/APM/CSW design series is **COMPLETED_VERIFIED** through APW-08, APM-06 and CSW-10.

## Combined implementation progress

| Slice | State | Application evidence | Migration |
|---|---|---|---|
| APW-I01 | completed_verified | PR #205 / merge `e1f074bb…` | none |
| CSW-I01 | completed_verified | PR #206 / merge `bebf833d…` | `0009_csw_creative_fragment_foundation.json` |
| APM-I01 | completed_verified | PR #207 / merge `3941a066…` | `0010_apm_automated_run_foundation.json` |
| APW-I02 | completed_verified | PR #208 / merge `c5c4e896…` | none |
| APW-I03 | completed_verified | PR #209 / merge `06c0d4ff…` | none |
| APW-I04 | completed_verified | PR #210 / merge `a907fec7…` | `0011_apw_campaign_activity_foundation.json` |
| CSW-I02 | completed_verified | PR #211 / merge `72eb9a6b…` | `0012_csw_creator_library_memory.json` |
| APM-I02 | completed_verified | PR #212 / merge `8d3684ed…` | none |
| APM-I03 | completed_verified | PR #213 / merge `ffe354ca…` | `0013_apm_autogm_encounter_foundation.json` |
| APW-I05 | completed_verified | PR #214 / merge `c043c6b9…` | `0014_apw_creator_workshop_sandbox.json` |
| CSW-I03 | completed_verified | PR #215 / merge `0c49376a…` | none |
| CSW-I04 | completed_verified | PR #216 / merge `de028a41…` | `0015_csw_guided_creation_workflow.json` |
| CSW-I05 | completed_verified | PR #217 / merge `dc9c0f75…` | `0016_csw_narrative_lab_continuity.json` |
| CSW-I06 | completed_verified | PR #218 / merge `c7aac6ff…` | `0017_csw_writing_studio_revision_workspace.json` |
| CSW-I07 | completed_verified | PR #219 / merge `5d349777…` | `0018_csw_reuse_remix_transformation.json` |
| APW-I06 | completed_verified | PR #220 / merge `10e6bd05…` | `0019_apw_shell_notification_recovery.json` |
| CSW-I08 | completed_verified | PR #222 / merge `43788e22…` | none |
| APM-I04 | completed_verified | PR #223 / merge `4276d50c…` | `0020_apm_connected_cozy_shared_play.json` |
| APM-I05 | completed_verified | PR #224 / merge `eff6a3b5…` | `0021_apm_autogm_mini_campaign_director.json` |
| APM-I06 | completed_verified | PR #225 / merge `3f30cc2b…` | none |
| APW-I07 | **selected_not_started** | `APW-I07-attempt-001` | inspect live head first |

### APM-I06 completion evidence

Application PR #225 completed from exact validated head `b9726b15e5b32fa66610769f011fd7a8379b7e9c`. Repository-health run `32296415327` passed. Product run `32296415533` passed self-hosted Linux, self-hosted Windows and deterministic cross-platform comparison on the first attempt. All 24 focused APM-I06 recovery/safety tests passed before squash merge `3f30cc2ba1ace9a73fdb101b536a9e55bf140a92`.

Live inspection proved no durable APM-I06 schema gap, so no migration `0022` was created. Shared APM-I01 run/delegation/operation/lifecycle/recovery checkpoints plus APM-I03/I04/I05 mode-specific recovery evidence were sufficient. The implementation added a status-first cross-mode recovery coordinator, role-safe projection, non-mutating replay evidence, mode-transition authority isolation, optional-AI rejection and accessible no-AI/zero-paid-service recovery acceptance without creating a second canonical ledger.

## Current work — APW-I07

**APW-I07 — End-to-end hybrid acceptance: live → async → GM resolution → Player return → live continuation** is the sole selected application implementation slice and the final item in the strict combined implementation sequence.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I07-attempt-001`  
State: `selected_not_started`

APW-I07 is a whole-program acceptance/integration slice. It proves that completed APW, CSW and APM work shares one authoritative account/context/Campaign/Session/Action/Event history. It does not create a new state engine or feature family.

Required boundaries:
- one deterministic journey begins in live Session state, submits one stable asynchronous Player Action, survives disconnect, resolves later through existing GM/Action authority, returns one accepted result to the reauthorized Player and resumes live play after the exact resulting Event cursor;
- duplicate submit/status/reconnect paths return prior evidence and never duplicate the accepted Action/Event outcome;
- stale Action versions, stale context membership, revoked permission or stale notification/deep-link cache cannot silently overwrite or restore protected authority;
- authorization and D05 visibility filtering happen before return notifications, badges/counts, deep-link previews, result cards, search, replay or support evidence;
- delayed GM resolution stays in the existing Action/adjudication owner; APW coordinates cadence/status only;
- creator Personal/Workshop material remains independent from Campaign authority and incorporation remains explicit/receipt-bound;
- automated-play pause/recovery remains compatible with the same ordinary history and cannot fork Campaign/Event state;
- desktop/mobile/keyboard/screen-reader/nonvisual paths expose equivalent cadence, pending/result/recovery and continuation state;
- optional AI can be fully disabled and blocking acceptance uses zero paid services;
- cross-platform deterministic receipts agree on authoritative identities, versions and Event cursors while presentation text may differ.

First operation: re-fetch App main and migration head once, inspect completed APW-I03 async Action/GM inbox/result-return seams, APW-I06 notification/deep-link recovery, CSW-I08 creator compatibility and APM-I06 recovery compatibility, decide whether any genuine durable APW-I07 delta requires migration `0022`, then implement the smallest deterministic whole-program hybrid acceptance journey.

Canonical App baseline after APM-I06: `3f30cc2ba1ace9a73fdb101b536a9e55bf140a92`. Migration head remains `0021_apm_autogm_mini_campaign_director.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through APM-I06 is completed_verified. APW-I07 is selected_not_started.

## Migration and ownership policy

- migrations `0001` through `0021` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- APW-I07 uses migration `0022` only if live inspection proves a genuine durable schema delta; an end-to-end acceptance fixture alone is not a schema reason;
- APW-I07 cannot absorb Campaign, Session, Action, Event, Character, creator, automated-play or visibility truth into a new hybrid ledger;
- one stable operation ID and owner-domain accepted Event evidence remain the basis of async retries and return recovery;
- deep links/notifications are navigation/recovery hints, never permission tokens;
- broad offline authoritative mutation remains out of scope;
- optional AI has no mechanical, canonical, permission, consent or adjudication authority.

## Internal Alpha milestones

1. Persistent Personal/async foundation — **complete**.
2. Between-session and creator foundation — **complete**.
3. First creator and automated experiences — **complete**.
4. Deep creator workspace — **complete**.
5. Integrated shell and connected automation — **complete** through APM-I06.
6. Whole-system hybrid proof — **APW-I07 current**.

Tester distribution remains separately owner-gated.

## Preserved/deferred work

- **CCTI-12-T04:** owner-deferred until September 2026; preserve App PR #191 and its branches. On/after 2026-09-01 establish the owner-approved validation route before reevaluation.
- **WP-011:** dormant until the required special Mac environment is available.
- **DS-008:** blocked non-owner exact-byte transfer/validation; never reconstruct checksum-bound bytes from excerpts/OCR/memory.

## Permanent validation rules

Only evidence-backed `completed_verified` is complete. A failed required gate leaves work unfinished. Normal App/package acceptance is self-hosted Windows + self-hosted Linux + deterministic comparison where outputs should agree, plus exact-head repository health. AIOC repository health validates governance state; it does not substitute for product validation.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, encouraging, clear, confident and restrained; never obsequious.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains distinct from GM/Campaign authority and does not imply access to private creative work.

## Nonauthorization

Current selection authorizes only APW-I07. It does not authorize migration `0022` without a proven durable delta, new product feature families, public matchmaking, multiplayer AutoGM expansion, broad offline authoritative mutation, AI mechanical/canonical/permission/consent authority, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
