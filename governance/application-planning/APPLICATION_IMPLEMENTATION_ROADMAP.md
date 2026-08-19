# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.8.0  
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
| CSW-I08 | completed_verified | PR #222 / `6537ebf7…` / merge `43788e22…` | none |
| APM-I04 | **selected_not_started** | `APM-I04-attempt-001` | inspect live head first |

### CSW-I08 completion evidence

Application PR #222 completed from exact validated head `6537ebf724f96badc79639b0acf60ab1820e9d6b`. Repository-health run `32289550905` passed. Product run `32289551216` ended with self-hosted Windows PASS, self-hosted Linux PASS after the policy-permitted unchanged retry, and deterministic comparison PASS before squash merge `43788e22d58a4976bd87abd90aec69b2c1c0e8bc`.

CSW-I08 added **no migration `0020`**. Live inspection proved that CSW-I01–I07 already own the required creator identities/versions and APW-I06 already owns authorization-safe shell/deep-link recovery. The implementation therefore kept Creator Command Center state projection-only: Continue Writing, Ideas to Develop, Open Threads, Needs Attention, Recent, Unused, Drafts, Story Bible, authorized Campaign usage, Workshop and Sandbox are owner-derived projections; exact return targets reauthorize/re-resolve current state; commands route to owning domains without executing authority; Sandbox remains **Experiment / noncanonical**; visible usage remains visible-subset-only; optional assistance is candidate-only; and core use remains no-AI.

Validation history is preserved in `CSW-I08-attempt-001`: candidate `2facc116…` stopped at shared TypeScript typing/assertion defects before behavioral validation. Final head `6537ebf7…` repaired only those defects and passed all 15 focused CSW-I08 tests. Its first Linux full-suite attempt had only the pre-existing A2 p95 timing fluctuation (`379.370941ms > 250ms`); the unchanged permitted retry passed, followed by deterministic comparison PASS. No A2 threshold/test or CSW-I08 authority/privacy boundary was weakened.

The final haunted-lighthouse acceptance proved the no-AI creator loop `Capture → Develop → Connect → Structure → Write → Check → Use → Reuse` without automatic incorporation/publication or hidden-cardinality leakage.

## Current work — APM-I04

**APM-I04 — Connected Cozy shared play** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APM-I04-attempt-001`  
State: `selected_not_started`

Connected Cozy is invitation-only shared orchestration over ordinary Multiversal state. It does not create pooled participant authority, a second rules engine, public matchmaking, or an AI-operated social simulation.

Required boundaries:
- a shared Cozy space has explicit stable identity/lifecycle and references ordinary owner-domain state rather than copying Character/resource/Campaign truth;
- Solo Cozy → Connected Cozy creates/binds a new shared orchestration identity and never silently converts a Personal workspace into shared authority;
- every participant has independent identity, authorization, visibility, capability and automation-delegation bounds;
- the host can administer the space but cannot spend, consent, choose, speak canonically or widen delegation for another participant;
- invitations disclose only safe join information and are revalidated against current space/version/entitlement/context before acceptance;
- participant counts, badges, notifications, search, waiting state, deep links and optional-AI context are authorization-filtered before aggregation;
- contributions are attributable to the acting participant and revalidate current authority/resources/expected versions;
- shared resource contribution uses explicit reserve/commit/release/refund semantics and cannot double-spend Personal or Campaign resources;
- live and asynchronous coordination share one governed history and do not create separate state forks;
- human-required choices and relationship/social consent remain human-required;
- leave/revoke removes future authority without erasing already-committed attributable history;
- rejoin creates a fresh authorized projection; stale cached shared state cannot restore removed permissions or hidden data;
- hidden information is filtered per participant before presentation or optional-AI context;
- core Connected Cozy operation and recovery require no AI provider;
- public stranger matchmaking, multiplayer AutoGM authority and broad offline authoritative shared play remain out of scope.

First operation: re-fetch App main and migration head **once**, inspect APM-I01 run/delegation authority, APM-I02 Cozy Solo, APW-I03 asynchronous action/recovery, APW-I04 Campaign activity and existing invitation/membership/resource/idempotency seams, decide whether a genuine durable APM-I04 delta requires migration `0020`, then implement the smallest invitation-only Connected Cozy space + independent participant contribution path.

Canonical App baseline after CSW-I08: `43788e22d58a4976bd87abd90aec69b2c1c0e8bc`. Migration head: `0019_apw_shell_notification_recovery.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through CSW-I08 is completed_verified. APM-I04 is selected_not_started. APM-I05 and later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0019` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- APM-I04 may use migration `0020` only if live inspection proves existing automation/activity/membership/resource records cannot represent required Connected Cozy orchestration metadata;
- any Connected Cozy persistence must store orchestration/membership/contribution/recovery metadata only and never copy Character, resource, inventory, relationship or Campaign truth;
- stable operation IDs and expected versions must prevent duplicate accepted effects and double-spend;
- D05/APW-I06 authorization precedes shared counts, notifications, search, waiting state, deep links and optional-AI context;
- participant authority never pools, and host/automation/AI cannot substitute for another human's consent or required choice;
- D18/D28/A9/Character/Campaign and creator incorporation/publication transitions remain explicit owning-domain operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **complete**.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06 — **APM-I04 current**.
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

Current selection authorizes only APM-I04. It does not authorize APM-I05+, APW-I07+, migration `0020` without a proven durable delta, public stranger matchmaking, multiplayer AutoGM authority, pooled participant authority, host/AI action or consent on behalf of another human, AI mechanical/canonical/permission/consent authority, hidden participant/Campaign/resource leakage, broad offline authoritative shared play, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
