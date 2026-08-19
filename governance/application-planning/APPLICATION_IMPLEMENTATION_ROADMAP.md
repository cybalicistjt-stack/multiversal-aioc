# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.7.0  
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
| APW-I06 | completed_verified | PR #220 / `caed3960…` / merge `10e6bd05…` | `0019_apw_shell_notification_recovery.json` |
| CSW-I08 | **selected_not_started** | `CSW-I08-attempt-001` | inspect live head first |

### APW-I06 completion evidence

Application PR #220 completed from exact validated head `caed396040edf9fd3b64224f962a5536c855303e`. Repository-health run `32287504862` passed. Product run `32287505491` ended with self-hosted Windows PASS, self-hosted Linux PASS and deterministic comparison PASS before merge `10e6bd051aa51dfb8f93014b46473074d19bb6c5`.

APW-I06 added migration `0019_apw_shell_notification_recovery.json` only after live inspection proved a genuine `notifications-work` persistence gap. The implementation stores recipient-safe notification projection lifecycle, safe target/context/version recovery descriptors and presentation preferences while Campaign, Action, Session, creator and other workflow truth stays in its owner domains. Authorization/current-context filtering occurs before attention counts or search matching; deep links reauthorize/re-resolve; Spoiler Shield applies only after authorization; offline safe caches remain read-only; context changes clear/reproject shell state; Sandbox content is explicitly noncanonical; core operation needs no AI or external notification provider.

Validation history remains in `APW-I06-attempt-001`: initial candidates exposed only bounded local fixture/asynchronous UI-test synchronization defects. Final head passed all 19 focused APW-I06 tests. Its first Linux full-suite execution failed only the pre-existing A2 p95 timing budget at `469.7934699999996 ms` versus `250 ms` while 393 other tests passed; the exact unchanged permitted Linux retry passed, followed by deterministic comparison. No source, test, threshold, privacy or authority boundary was weakened for the retry.

## Current work — CSW-I08

**CSW-I08 — Creator Command Center, Workshop/shell integration and end-to-end acceptance** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `CSW-I08-attempt-001`  
State: `selected_not_started`

The governing flow is:

`authorized owning-domain projections → context-safe ranking/grouping → creator-facing resume/attention surfaces → exact deep link or bounded command → owning-domain action`

Required boundaries:
- the Command Center is a projection/navigation layer, not a new creator truth, task authority, notification authority, social-engagement feed or hidden AI workspace;
- authorization precedes cards, counts, ranking, search, related-work analysis, Campaign-usage projections and optional-assistance source collection;
- Continue Writing, Ideas to Develop, Open Threads, Needs Attention, Recent, Unused Material, Drafts, Story Bible, Campaigns Using My Work and Workshop/Sandbox project existing owning-domain state rather than duplicating it;
- Personal/Project/Campaign/Sandbox context is explicit; Sandbox remains visibly Experiment/noncanonical;
- exact resume/return targets reauthorize and re-resolve before rendering or actioning protected content and reuse APW-I06 safe deep-link/recovery semantics where possible;
- stale/moved/deleted/archived/lost-access/offline targets fail or recover safely without protected metadata leakage;
- Unused Material and Campaign-usage wording describes only the authorized visible subset and never implies absence of hidden/protected usage;
- transparent ranking may use creator pins, resume state, unresolved creator action, meaningful recency, user priority, creator-configured reminder metadata, recovery/conflict need and saved-view relevance;
- ranking must not use streaks, hidden engagement scores, FOMO, arbitrary inactivity urgency or creator productivity scoring;
- dismissed/snoozed advisory items do not repeatedly nag unless evidence materially changes;
- creator search/command palette is a router only; every command returns to an owning domain for current authorization, validation and confirmation;
- Needs Attention represents creator-actionable or advisory workflow state, never objective creative quality;
- optional assistance exposes exact Scope, Sources, Task, Capabilities, candidate/draft/advisory output status and privacy boundary before invocation; user can narrow sources where the flow permits;
- AI is optional/candidate-only and may not publish, incorporate, accept revisions, resolve OpenThreads, widen permissions, execute arbitrary commands or schedule reminders;
- no-AI organization, resume, search, guided development, writing, continuity, reuse/remix and Workshop flows remain useful;
- mobile, keyboard, screen-reader/nonvisual and reduced-motion paths preserve equivalent context, resume, reason/status and command meaning;
- product voice remains warm, calm, encouraging and non-obsequious.

First operation: re-fetch App main and migration head **once**, inspect current CSW-I02 Library/Project Memory, CSW-I03 Idea Inbox, CSW-I05 OpenThread/continuity, CSW-I06 Writing resume/revision, CSW-I07 derivative lineage, APW-I05 Workshop/Sandbox and APW-I06 attention/search/safe-destination/recovery seams plus existing pin/saved-view state. Determine whether any genuine durable CSW-I08 delta requires migration `0020`; prefer a reconstructable projection and reuse existing persistence when it is sufficient.

Canonical App baseline after APW-I06: `10e6bd051aa51dfb8f93014b46473074d19bb6c5`. Migration head: `0019_apw_shell_notification_recovery.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through APW-I06 is completed_verified. CSW-I08 is selected_not_started. APM-I04 and later slices remain inactive.

A later slice may move earlier only when its declared dependencies remain satisfied **and the owner approves the reorder**. No such reorder is active.

## Migration and ownership policy

- migrations `0001` through `0019` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- CSW-I08 should prefer reconstructable projections from existing D29/APW records and APW-I06 safe destination/notification lifecycle rather than duplicating creator truth;
- if durable creator pin/snooze/saved-view/return-target state is missing, storage must remain bounded to its correct existing owner and cannot become a generic Command Center truth store;
- D05 authorization precedes Command Center cards/counts/ranking/search/related/usage and optional-assistance context;
- APW-I06 remains global shell/attention/deep-link orchestration authority; CSW-I08 does not create a parallel shell or notification engine;
- D18/D28/A9/Character/Campaign and creator incorporation transitions remain explicit owning-domain operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **complete**.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06 — **APW-I06 complete; CSW-I08 current**.
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

Current selection authorizes only CSW-I08. It does not authorize APM-I04+, APW-I07, migration `0020` without a proven durable delta, a new creator truth/task/notification authority, hidden Campaign usage/count/cardinality leakage, engagement/productivity scoring, command-palette authority bypass, AI auto-apply/publish/incorporate/schedule, unauthorized assistance context, external provider activation, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
