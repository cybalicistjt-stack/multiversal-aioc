# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.9.0  
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
| APM-I05 | **selected_not_started** | `APM-I05-attempt-001` | inspect live head first |

### APM-I04 completion evidence

Application PR #223 completed from exact validated head `d465adc4184592aff52639a1b9f9a50fd51ce09a`. Repository-health run `32292150819` passed. Product run `32292154603` ended with self-hosted Linux PASS, self-hosted Windows PASS and deterministic comparison PASS after policy-permitted unchanged retries of the only remaining pre-existing A2 p95 timing fluctuations. All 19 focused APM-I04 tests passed on the final head before squash merge `4276d50cf8a090c807a6ffa24238cef2cad34ee1`.

Migration `0020_apm_connected_cozy_shared_play.json` was added only after live inspection proved a genuine orchestration gap. It stores Connected Cozy shared-space, participant membership/invitation, attributable contribution and operation/recovery metadata only. Character, resource, inventory, relationship and Campaign truth remain in their owning domains. Participant authority never pools through host/space identity; invitation acceptance revalidates current binding/version/authority; visibility filtering precedes participant counts; resource claims use owner reservation receipts; ambiguous owner commit keeps reservations/evidence and enters recovery instead of assuming failure or blindly retrying; leave/revoke removes future authority while preserving committed history; rejoin requires fresh authorization; and core operation requires no AI.

Validation history is preserved in `APM-I04-attempt-001`: candidate `f4b16674…` exposed one accessible UI-state defect where projection refresh overwrote successful contribution feedback. Final head `d465adc4…` repaired the ordering without weakening behavior. Its first exact-head Linux/Windows full-suite attempts then had only the existing A2 p95 fluctuations (`262.589018ms` and `268.5609ms` > unchanged `250ms`); unchanged retries passed. No A2 threshold/test or APM-I04 privacy/authority/recovery boundary was weakened.

## Current work — APM-I05

**APM-I05 — AutoGM Mini-Campaign Director** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APM-I05-attempt-001`  
State: `selected_not_started`

APM-I05 extends the verified APM-I03 single-encounter runner across a finite, exact-version, governed Adventure scenario graph. It is a bounded director, not an unlimited autonomous Campaign generator and not a second game engine.

Required boundaries:
- `MiniCampaignPackage` is derived only from a governed Adventure definition or explicitly incorporated governed source; unincorporated CSW planning material is not executable;
- package ID/version, graph nodes/edges, entry/endpoints, route predicates, hidden/reveal state, allowed APM-I03 child encounter packages, deterministic policy/seeds, rewards/results and hard run budgets are finite and inspectable;
- parent run lifecycle records current graph node, visited/terminal/route receipts, current eligible route-set version, child-run correlations, package-local reveal/objective state, owner-state evidence refs, budget counters and recovery/end state without copying ordinary game truth;
- route eligibility is computed only from committed current owner state and exact package/policy versions;
- when two or more meaningfully distinct player-facing eligible routes exist, selection is human-required unless the package explicitly declares a non-choice automatic transition;
- hidden routes/nodes/future revelations and their cardinality are absent from player projections, summaries, accessibility text, logs, notifications and optional-AI context until revealed;
- encounter nodes launch APM-I03 child runs with a durable parent→child correlation before child effects can advance parent progression;
- retry/recovery resolves an existing child before starting another, and one child terminal receipt advances the parent at most once;
- child abort/fail-safe follows package-declared failure/retreat/recovery semantics rather than being coerced into success;
- between scenes the director re-reads authoritative Character/resource/inventory/investigation/relationship/World/Campaign state and stores references/evidence rather than parallel state;
- CSW continuity/open-thread material remains advisory and cannot rewrite runtime routes or package state;
- hard maximum node transitions, child encounters, automatic steps/Events and explicit endpoints/fail-safe rules prevent endless generation;
- ambiguous operations recover status before retry and deterministic route/mechanical replay uses exact versions, human choices and governed seed streams;
- optional AI receives only the player-safe resolved projection and may narrate/summarize/phrase, never own route legality, mechanics, reveals or completion;
- core route/run/recovery behavior remains useful without AI.

First operation: re-fetch App main and migration head **once**, inspect APM-I01 parent automation-run/delegation/operation recovery, APM-I03 encounter package/run/terminal receipt, D28 Adventure graph/incorporation, committed owner-state references, hidden-state projection and recovery/idempotency seams, decide whether a genuine durable APM-I05 delta requires migration `0021`, then implement the smallest finite MiniCampaignPackage + parent route-choice/child-run correlation path.

Canonical App baseline after APM-I04: `4276d50cf8a090c807a6ffa24238cef2cad34ee1`. Migration head: `0020_apm_connected_cozy_shared_play.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through APM-I04 is completed_verified. APM-I05 is selected_not_started. APM-I06 and APW-I07 remain inactive.

## Migration and ownership policy

- migrations `0001` through `0020` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- APM-I05 may use migration `0021` only if live inspection proves existing APM-I01/APM-I03/D28 records cannot represent required parent package/run/route/child-correlation/recovery metadata;
- any APM-I05 persistence stores package/director orchestration, bounded hidden package-local state, route receipts, child correlations, budgets and recovery evidence only; Character, resource, inventory, relationship, investigation, World and Campaign truth remains in owner domains;
- meaningful player-facing route choices remain human-required;
- APM-I03 child terminal receipts advance the parent exactly once;
- D05 authorization/reveal filtering precedes player route counts, summaries, logs, notifications, search and optional-AI context;
- AI never owns route legality, mechanics, reveal state, completion or package mutation;
- D18/D28/A9/Character/Campaign and creator incorporation/publication transitions remain explicit owning-domain operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **complete**.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06 — **APM-I05 current**.
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

Current selection authorizes only APM-I05. It does not authorize APM-I06+, APW-I07+, migration `0021` without a proven durable delta, unlimited autonomous Campaign generation, runtime AI-authored authoritative nodes/edges, direct execution of unincorporated CSW planning material, AI route/mechanical/reveal/completion authority, hidden route/cardinality leakage, parallel ordinary-domain state engines, broad offline authoritative Mini-Campaign mutation, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
