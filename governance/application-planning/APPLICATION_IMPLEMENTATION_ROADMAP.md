# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.10.0  
**Status:** ACTIVE — COMBINED WORKSPACE IMPLEMENTATION  
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
| APM-I04 | completed_verified | PR #223 / `d465adc4…` / merge `4276d50c…` | `0020_apm_connected_cozy_shared_play.json` |
| APM-I05 | completed_verified | PR #224 / `5a7e685e…` / merge `eff6a3b5…` | `0021_apm_autogm_mini_campaign_director.json` |
| APM-I06 | **selected_not_started** | `APM-I06-attempt-001` | inspect live head first |

### APM-I05 completion evidence

Application PR #224 completed from exact validated head `5a7e685eccc94b746c5116f3973c0992f20c65f1`. Repository-health run `32294799511` passed. Product run `32294800000` ended with self-hosted Windows PASS, self-hosted Linux PASS and deterministic comparison PASS after the policy-permitted unchanged retry of the only remaining pre-existing A2 p95 timing fluctuation. All 19 focused APM-I05 tests passed on the final head before squash merge `eff6a3b5c5ee0f7a5068bdc9badf6eb36ef932b1`.

Migration `0021_apm_autogm_mini_campaign_director.json` was added only after live inspection proved a genuine parent-orchestration gap. It stores finite exact-version Mini-Campaign package binding, parent run position/budgets, route receipts, APM-I03 child correlations, exact-once parent advancement and recovery cursors only. D28 Adventure/run truth, APM-I03 child encounter truth, APM-I01 controller/delegation/operation authority and ordinary Character/resource/inventory/relationship/investigation/World/Campaign state remain in their owning systems.

Validation history is preserved in `APM-I05-attempt-001`: initial PR head `6c618efd…` failed the contract-invariant lane because the validator required the literal words “Runtime AI” inside a deterministic service that exposed no AI execution seam. The validator was strengthened to structural forbidden-AI authority checks rather than weakening the product. Final head `5a7e685e…` then passed repository health and Windows; Linux's first full-suite attempt had only the existing A2 p95 fluctuation (`338.7460209999999ms` > unchanged `250ms`) while all APM-I05 focused tests passed. The Linux lane was retried unchanged and passed, followed by deterministic comparison PASS. No A2 threshold/test or APM-I05 authority/privacy/recovery boundary was weakened.

## Current work — APM-I06

**APM-I06 — Automated-play recovery, safety and end-to-end acceptance** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APM-I06-attempt-001`  
State: `selected_not_started`

APM-I06 integrates recovery and safety across the already-completed APM-I01 through APM-I05 modes. It does not create a new play mode, new canonical state engine, global GM authority or broad offline synchronization system.

Required boundaries:
- recovery binds exact authenticated subject, Context, mode/profile, automation run, delegation, package/activity versions, stable operation ID, expected owner versions, deterministic inputs, Event/status receipts, pending human barriers and provenance;
- reconnect/status recovery checks authenticated subject, Context membership/control/role, delegation expiry/revocation, permission/visibility, entitlement/pack compatibility, exact package/activity/schema/rules/policy versions, Event cursor, operation status, reservations/leases and pending human decisions before restoring automation;
- lack of a response is never proof of failure; ambiguous operations query status/Event history before any retry and reuse the same stable operation identity;
- duplicate operations return prior results without duplicating costs, rewards, progress, resource movement, encounter effects, route progress or other accepted effects;
- stale expected versions, revoked authority or materially changed eligibility enter review/revoked/expired/fail-safe behavior instead of last-write-wins or silent substitution;
- Cozy Solo resumes only from proven accepted progress/Event sequence and preserves mandatory human choices;
- Connected Cozy recovery preserves independent participant authority, contribution/resource receipts and leave/revoke/rejoin history; stale cache cannot restore removed permissions or hidden data;
- AutoGM Single-Encounter recovery resumes exact package/turn/reaction/seed/Event barriers without rerolls, duplicate effects, skipped reactions or hidden-state exposure;
- AutoGM Mini-Campaign recovery preserves exact current node/route state, child run IDs/terminal receipts, one parent advancement per child terminal result, route eligibility inputs, pending human route choices, hidden projection version and hard run budgets;
- mode transitions preserve one ordinary authoritative history and never silently carry automation delegation into a different mode/context;
- optional AI remains replaceable presentation/proposal only; unavailable, malformed, unauthorized, illegal or over-budget output cannot widen authority, alter committed mechanics, undo owner-domain commits or become canonical state;
- D05/visibility filtering precedes player, AI, notification, count, log, replay, diagnostics and support projections, including recovery paths;
- deterministic replay is non-mutating and reproduces mechanical outcomes from exact authoritative starting state, versions, deterministic inputs and human decisions without reapplying Events;
- keyboard, screen-reader, touch/mobile, reduced-motion, warning and manual-fallback parity covers start/pause/resume/stop/recovery across modes;
- zero-paid-service and no-AI recovery/acceptance remain mandatory.

First operation: re-fetch App main and migration head **once**, inspect APM-I01..I05 recovery/serialization/status seams, APW-07 recovery helpers, visibility/notification/replay projections and mode-transition boundaries, decide whether a genuine durable APM-I06 delta requires migration `0022`, then implement the smallest cross-mode recovery/safety/end-to-end acceptance slice.

Canonical App baseline after APM-I05: `eff6a3b5c5ee0f7a5068bdc9badf6eb36ef932b1`. Migration head: `0021_apm_autogm_mini_campaign_director.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through APM-I05 is completed_verified. APM-I06 is selected_not_started. APW-I07 remains inactive.

## Migration and ownership policy

- migrations `0001` through `0021` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- APM-I06 may use migration `0022` only if live inspection proves existing APM-I01..I05 and APW-07 records cannot represent required shared recovery/safety evidence;
- any APM-I06 persistence stores recovery orchestration/evidence references only and cannot become a parallel automated-play ledger or duplicate Character, resource, inventory, relationship, investigation, World, Campaign, Adventure, encounter or Connected Cozy truth;
- stable operation identity, expected-version checks and owner status/Event evidence remain the basis of retries and recovery;
- pending human choices/reactions/consent/approval remain human-required after reconnect;
- D05 authorization/reveal filtering precedes all player/AI/count/notification/log/replay/support projections;
- deterministic replay never reapplies accepted Events;
- AI never owns mechanical, canonical, permission, consent, reveal, route or completion authority;
- participating owning-domain mutations remain explicit owner operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **complete**.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06 — **APM-I06 current**.
6. Whole-system hybrid proof — APW-I07.

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

Current selection authorizes only APM-I06. It does not authorize APW-I07+, migration `0022` without a proven durable delta, new automated-play mode semantics beyond recovery/safety/acceptance integration, public matchmaking, multiplayer AutoGM authority, unbounded autonomous campaigns, AI mechanical/canonical/permission/consent authority, broad offline authoritative automated play, a second canonical ledger, autonomous publication/canonical promotion, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
