# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.6.0  
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
| CSW-I06 | completed_verified | PR #218 / `8bbecee4…` / merge `c7aac6ff…` | `0017_csw_writing_studio_revision_workspace.json` |
| CSW-I07 | completed_verified | PR #219 / `245b90df…` / merge `5d349777…` | `0018_csw_reuse_remix_transformation.json` |
| APW-I06 | **selected_not_started** | `APW-I06-attempt-001` | inspect live head first |

### CSW-I07 completion evidence

Application PR #219 completed from exact validated head `245b90dfc6b9728df5a9d1954bf7c1176c5b0d2e`. Repository-health run `32285069748` passed. Product run `32285069972` ended with self-hosted Windows PASS, self-hosted Linux PASS after the policy-permitted unchanged retry, and deterministic comparison PASS before squash merge `5d34977710ae1229e32de06e7e7b28610b90ae84`.

CSW-I07 added migration `0018_csw_reuse_remix_transformation.json` only after live inspection proved a genuine D29 gap. The implementation stores derivative identity/lineage, exact source snapshots, deterministic transform recipe evidence, inherited-reference dispositions, idempotent derivative/rebase operations and advisory source-drift review without copying source/result payload truth. Clone/adapt/fork/remix/template/transform creates independent identity, Campaign/runtime extraction requires current explicit reuse authority, hidden references are filtered before lineage/count processing, and source changes never silently propagate.

Validation history is preserved in `CSW-I07-attempt-001`: candidate `7a0d96f…` stopped at an over-specific validator formatting check; `39d5bde…` passed invariants but stopped at a focused test-fixture TS2783 typing defect; final head `245b90df…` passed CSW-I07 invariants, typecheck and all 11 focused tests. Its first Linux full-suite attempt had only the pre-existing A2 p95 timing fluctuation; the unchanged permitted retry passed. No A2 threshold/test or CSW-I07 acceptance boundary was weakened.

## Current work — APW-I06

**APW-I06 — Shell, Navigation, Notifications, Visibility and Spoiler UX** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I06-attempt-001`  
State: `selected_not_started`

The shell is an orchestration/projection layer over existing authority. It must answer where the user is, which contextual role/capabilities apply, what authorized work needs attention, what visibility class an item has, and whether it is safe to continue.

Required boundaries:
- Personal, Campaign and Session context anchors remain explicit; context switching re-evaluates protected projections;
- roles such as GM/Player/Assistant GM/Observer remain contextual, never permanent account types;
- authorization and visibility filtering occur before attention counts, badges, search, autocomplete, ranking, recents, notification previews or related-work aggregation;
- primary navigation is capability/context aware but never exposes hidden destinations merely as disabled controls;
- attention groups decision-required, result-ready, waiting, recovery-required, informational and creator-advisory projections without becoming a second queue;
- notification records are projections of owning-domain state/events and read/dismiss state does not become workflow authority;
- deep links/return targets are navigation hints only and reauthorize/re-resolve target/version on open;
- stale, moved, deleted, archived, offline or permission-revoked targets recover safely without protected metadata leakage;
- Personal, Reusable, Campaign-local and Sandbox visibility classes are explicit; unauthorized material is absent rather than visually hidden;
- Sandbox/Lab material is always explicitly noncanonical and cannot be confused with Campaign/reusable truth;
- Spoiler Shield may obscure already-authorized previews but never grants/revokes access, reveals hidden cardinality or substitutes for D05/parental-control security;
- connected/offline-cached/recovering state is explicit and cannot invent offline write authority;
- mobile, keyboard, screen-reader/nonvisual and reduced-motion paths carry equivalent context/role/visibility/notification semantics;
- shell language is warm, calm and noncoercive; no streaks, punitive urgency or pressure to enable AI;
- core context/navigation/attention/search/deep-link/spoiler behavior remains deterministic and useful without AI.

First operation: re-fetch App main and migration head **once**, inspect existing shell/context/navigation, notification/attention, visibility/search and deep-link/recovery seams plus Personal/Campaign/Session projections, determine whether any genuine durable APW-I06 delta requires migration `0019`, then implement the smallest deterministic shell context + authorization-safe attention/deep-link recovery path.

Canonical App baseline after CSW-I07: `5d34977710ae1229e32de06e7e7b28610b90ae84`. Migration head: `0018_csw_reuse_remix_transformation.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through CSW-I07 is completed_verified. APW-I06 is selected_not_started. CSW-I08 and later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0018` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- APW-I06 shell records, if any genuine durable delta exists, may hold projection/navigation/notification preference or recovery metadata only and never replace owning-domain Campaign/Personal/CSW/APM truth;
- D05 authorization precedes shell counts, badges, search, recents, notification previews, deep-link previews and optional-AI context;
- notification/read state, deep-link descriptors, visibility labels and Spoiler Shield never create permissions or owning-domain workflow authority;
- D18/D28/A9/Character/Campaign and creator transitions remain explicit owning-domain operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **complete**.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06 — **APW-I06 current**.
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

Current selection authorizes only APW-I06. It does not authorize CSW-I08+, APM-I04+, APW-I07+, migration `0019` without a proven durable delta, new permission/Campaign truth authority, notification-as-workflow authority, Spoiler Shield as authorization/parental-control security, hidden result/count/cardinality leakage, automatic cross-context protected-cache retention, AI-required shell/navigation, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
