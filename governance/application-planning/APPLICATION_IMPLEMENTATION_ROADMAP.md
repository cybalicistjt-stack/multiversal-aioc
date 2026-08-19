# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.2.0  
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
| APW-I01 | completed_verified | PR #205 / `2814de3c…` / merge `e1f074bb…` | none |
| CSW-I01 | completed_verified | PR #206 / `2836c170…` / merge `bebf833d…` | `0009_csw_creative_fragment_foundation.json` |
| APM-I01 | completed_verified | PR #207 / `cdf80bd3…` / merge `3941a066…` | `0010_apm_automated_run_foundation.json` |
| APW-I02 | completed_verified | PR #208 / `d5463609…` / merge `c5c4e896…` | none |
| APW-I03 | completed_verified | PR #209 / `9b6da923…` / merge `06c0d4ff…` | none |
| APW-I04 | completed_verified | PR #210 / `67029683…` / merge `a907fec7…` | `0011_apw_campaign_activity_foundation.json` |
| CSW-I02 | completed_verified | PR #211 / `8a067465…` / merge `72eb9a6b…` | `0012_csw_creator_library_memory.json` |
| APM-I02 | completed_verified | PR #212 / `9e3719fc…` / merge `8d3684ed…` | none |
| APM-I03 | completed_verified | PR #213 / `f94f6815…` / merge `ffe354ca…` | `0013_apm_autogm_encounter_foundation.json` |
| APW-I05 | completed_verified | PR #214 / `b3eee7cc…` / merge `c043c6b9…` | `0014_apw_creator_workshop_sandbox.json` |
| CSW-I03 | completed_verified | PR #215 / `22963399…` / merge `0c49376a…` | none |
| CSW-I04 | **selected_not_started** | `CSW-I04-attempt-001` | inspect live head first |

### CSW-I03 completion evidence

Application PR #215 completed from exact validated head `22963399944c999eaa44c295fec9feb9b08ddad0`. Repository-health run `32275445166` passed. Product run `32275445385` ended with self-hosted Windows PASS, self-hosted Linux PASS and deterministic comparison PASS before squash merge `0c49376ab74e27b15db6678d34c8c200e3caf210`.

CSW-I03 reused existing CSW-I01/I02 D29 persistence instead of claiming migration `0015`: migration `0009` already supplies CreativeFragment Inbox identity/lifecycle/provenance/relationships/idempotent operation recovery and CSW-I02 already supplies D05 authorization-before-search/count/topology. Inspiration requests/candidates remain intentionally ephemeral until explicit creator disposition. The tranche delivered minimal capture, later triage, five deterministic no-AI inspiration primitives, bounded count/depth, exact source/generator/seed provenance, explicit dismiss/save-new/branch/alternate/source-revision operations, authorization-safe related discovery and the Idea Inbox UI.

Validation history is preserved in `CSW-I03-attempt-001`: initial candidate `fa2580766d85faea9ff513b695aa88d1b969a943` passed invariants/typecheck and 320/321 client tests but exposed one real focused defect—related discovery selected the first usable seed token rather than the strongest token, missing an authorized related item. The deterministic query selection was repaired without weakening privacy, tests or scope. The repaired exact head passed every required gate.

## Current work — CSW-I04

**CSW-I04 — Guided Creation Workflows and templates** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `CSW-I04-attempt-001`  
State: `selected_not_started`

CSW-I04 implements optional creative scaffolding over the same CSW material. Guidance is orchestration, never truth, and freeform authoring remains an equal path.

Required boundaries:
- reusable workflow definitions/versions describe guidance only and contain no hidden authority or arbitrary executable behavior;
- workflow runs may remember progress, visited/skipped steps, branch choices and references, but durable creative answers remain ordinary CSW-I01/02 material rather than a second content store;
- run definition version is pinned; definition/template updates never silently rewrite existing runs;
- creators may skip, revisit, reorder independent steps, pause/resume, branch, abandon, finish with unresolved items, or leave guided mode for equivalent freeform editing;
- prerequisites constrain only genuinely dependent steps; suggested order is not mandatory creative chronology;
- CSW-I02/D05 authorization precedes reference search/count/ranking/autocomplete and protected references are reauthorized on resume;
- CSW-I03 Inspiration remains bounded and candidate-only; workflow state may remember a disposition but cannot convert a candidate into truth;
- workflow completion means creator progress only, never publication, canon, mechanical validity, Campaign approval or owning-domain incorporation;
- progress is informative and noncoercive: skips are not failures, completion is not a quality percentage and finish cannot be hidden behind forced answers;
- accessibility/nonvisual parity must cover progress, branching and reordering; the core path remains deterministic and no-AI.

First operation: re-fetch App main and migration head **once**, inspect existing D29 workflow/run/recovery records plus CSW-I01 answer/version operations, CSW-I02 reference projection and CSW-I03 Inspiration seams, determine whether durable guided-run orchestration genuinely requires migration `0015`, then implement the smallest reusable guided workflow with an explicit freeform escape.

Canonical App baseline after CSW-I03: `0c49376ab74e27b15db6678d34c8c200e3caf210`. Migration head remains `0014_apw_creator_workshop_sandbox.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through CSW-I03 is completed_verified. CSW-I04 is selected_not_started. Later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0014` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- D29 remains creative-support metadata/provenance/reference/workflow oriented, not governed World/Adventure/Campaign truth;
- guided-run state cannot become a parallel creative answer store;
- D05 authorization precedes derived aggregation/presentation/generator/reference context;
- generated candidates and workflow completion never gain authority through ranking, progress, repetition or AI fluency.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **CSW-I04 remains**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07.
5. Integrated shell and connected automation — APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06.
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

Current selection authorizes only CSW-I04. It does not authorize CSW-I05+, APW-I06+, APM-I04+, a parallel creative answer truth store, mandatory wizard-only authoring, workflow-completion authority, automatic candidate application/incorporation/publication, arbitrary executable templates, hidden/private source leakage, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
