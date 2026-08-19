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

Application PR #220 completed from exact validated head `caed396040edf9fd3b64224f962a5536c855303e`. Repository-health run `32287504862` passed. Product run `32287505491` ended with self-hosted Windows PASS, self-hosted Linux PASS after the policy-permitted unchanged retry, and deterministic comparison PASS before squash merge `10e6bd051aa51dfb8f93014b46473074d19bb6c5`.

APW-I06 added migration `0019_apw_shell_notification_recovery.json` after live inspection proved a genuine notifications-work persistence gap. The implementation mounts a real integrated shell around the App while preserving `ProtectedContextBoundary`; exposes Personal/Campaign/Session context and contextual role; filters authorization before attention/search/count aggregation; keeps read/dismiss/quieting non-authoritative; labels Sandbox as noncanonical; reauthorizes and re-resolves deep links; makes offline cached results read-only; and treats Spoiler Shield as presentation-only rather than permission or parental-control security.

Validation history is preserved in `APW-I06-attempt-001`: candidate `887147c1…` passed invariants/typecheck but had two focused integrated-shell UI assertion failures. Final head `caed3960…` passed all 19 APW-I06 focused tests and the complete Windows profile. Its first Linux full-suite attempt had only the pre-existing A2 p95 timing fluctuation (`469.79347ms > 250ms`); the unchanged permitted retry passed. No A2 threshold/test or APW-I06 authority/privacy acceptance boundary was weakened.

## Current work — CSW-I08

**CSW-I08 — Creator Command Center, Workshop/shell integration and end-to-end acceptance** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `CSW-I08-attempt-001`  
State: `selected_not_started`

The Creator Command Center is a projection/navigation layer over existing CSW/APW/owning-domain state. It is not a new source of truth, social-engagement feed, task authority engine, notification queue or hidden AI workspace.

Required boundaries:
- Continue Writing, Ideas to Develop, Open Threads, Needs Attention, Recent, Unused, Drafts, Story Bible, Campaign usage and Workshop/Sandbox surfaces are projections from existing owners;
- authorization/visibility filtering happens before counts, ranking, search, related-work, similarity, Campaign usage or optional-assistance context;
- every item shows explicit Personal/Project/Campaign/Sandbox context, and Sandbox remains **Experiment / noncanonical**;
- creator return targets carry owner/context/object/version/branch/revision/node/focus/fallback navigation metadata only and reauthorize before protected rendering/action;
- stale/moved/archived/deleted/lost-access/offline targets recover through the owning feature without protected leakage;
- Needs Attention reflects explicit creator-actionable or advisory workflow state, not objective story quality or productivity scoring;
- dismissed/snoozed advisory items do not nag again without changed evidence;
- “Unused” and Campaign-usage projections describe only the authorized visible subset and never imply hidden-global completeness;
- the creator search/command palette routes to owning-domain commands and cannot bypass authorization, validation or confirmation;
- optional assistance exposes scope/sources/task/capabilities/output status and remains candidate-only; AI is never required for core resume/development;
- ranking favors recoverability and creator intent, never streak loss, FOMO, inactivity pressure or competitive productivity scores;
- Workshop assets can appear as reusable work, while Sandbox sessions remain visibly separate from Campaign progress/reusable truth until explicit save-out;
- mobile/keyboard/screen-reader/nonvisual/reduced-motion paths preserve the same semantics;
- the final CSW haunted-lighthouse proof must exercise `Capture → Develop → Connect → Structure → Write → Check → Use → Reuse` while keeping governed incorporation explicit.

First operation: re-fetch App main and migration head **once**, inspect CSW-I01–I07 resume/projection seams plus APW-I05/I06 shell/Workshop/deep-link integration, decide whether a genuine durable delta requires migration `0020`, then implement the smallest authorization-safe Creator Command Center + exact return-target path before the final CSW end-to-end proof.

Canonical App baseline after APW-I06: `10e6bd051aa51dfb8f93014b46473074d19bb6c5`. Migration head: `0019_apw_shell_notification_recovery.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through APW-I06 is completed_verified. CSW-I08 is selected_not_started. APM-I04 and later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0019` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- Command Center cards/return targets should remain projections/navigation metadata where existing owner state is sufficient; migration `0020` is allowed only if live evidence proves a durable gap;
- D05 authorization precedes Command Center counts, ranking, search, related-work, Campaign usage and optional-assistance context;
- APW-I06 notification/read state remains shell presentation metadata and is not duplicated as a CSW queue;
- D18/D28/A9/Character/Campaign and creator incorporation/publication transitions remain explicit owning-domain operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **complete**.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06 — **CSW-I08 current**.
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

Current selection authorizes only CSW-I08. It does not authorize APM-I04+, APW-I07+, migration `0020` without a proven durable delta, a second creator truth/workflow/notification/command authority, automatic idea promotion/continuity resolution/writing acceptance/derivative update/incorporation/publication, objective creative-quality/productivity scoring, streak/FOMO/inactivity pressure, hidden Campaign usage/count leakage, AI-required Command Center or auto-apply, arbitrary command execution outside owning-domain authority, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
