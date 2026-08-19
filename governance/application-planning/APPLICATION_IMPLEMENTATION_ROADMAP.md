# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.9.0  
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
| APM-I03 | **selected_not_started** | `APM-I03-attempt-001` | inspect live head first |

### APM-I02 completion evidence

Application PR #212 passed on its first implementation head `9e3719fc3e08856226c9ece1866626d07cb7af31`: repository-health run `32266678738` PASS and product run `32266679050` PASS with self-hosted Windows, self-hosted Linux and deterministic comparison. It squash merged as `8d3684ed5ae8058518a8684d9f2d68f21f893723`.

APM-I02 delivered a Personal-context Cozy Solo core loop over APM-I01 delegation/run authority: delegated focus discovery, explicit bound confirmation, one-step and bounded-batch routine progress, fresh owning-domain authorization before every state-affecting step, proposal/human/GM/prohibited/budget/authorization stop barriers, operation-status lost-response recovery, zero real-money automation, no mechanical AI authority, manual/no-AI fallback and a guided Orient → Confirm bounds → Progress → Summary/Return-to-ordinary-play surface.

No migration `0013` was needed because APM-I01 already persists the governing profile/grant/run/bounds/recovery references. Migration head remains `0012_csw_creator_library_memory.json`.

## Current work — APM-I03

**APM-I03 — AutoGM Single-Encounter runner** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APM-I03-attempt-001`  
State: `selected_not_started`

Initial scope is one **foreground-only solo encounter** over ordinary Multiversal authority. AutoGM orchestrates a versioned encounter package and eligible NPC/world responses; it does not become GM authority, a second rules engine or a second game-state ledger.

Target loop:

**Select Character + Encounter Package → validate setup/delegation → start → player Action → deterministic owner-domain resolution → eligible bounded NPC/world response → deterministic resolution → reaction/human-choice barrier as needed → repeat → package-valid end/abort/fail-safe → governed reward/summary → stop.**

Required boundaries:
- explicit package ID/version, rules/pack compatibility, controlled actor set, response policy, hidden-state reference, end conditions and deterministic seed/entropy evidence;
- APM-I01 delegation/run authority remains necessary but every state-affecting operation still requires fresh owning-domain authorization;
- A6 remains player Action/proposal/result authority and A7/rules remain encounter/combat/initiative/reaction authority;
- player Character choices remain human-controlled unless a separately explicit narrow delegation exists;
- NPC/world responses may execute only when the owning-domain operation class is `automatic_permitted` or `automatic_with_bounds` and current grant/authorization permits it;
- proposal-required, human-required, prohibited, undefined/out-of-scope, revoked/stale/conflict and unsupported reaction states are barriers;
- D05 filters hidden scenario truth before player-visible action enumeration, labels, counts, errors, summaries, accessibility output and optional AI context;
- initial AutoGM is foreground-only; disconnect creates safe pause/recovery rather than background rounds;
- deterministic replay pins starting authoritative state/version, package/rules/controller/delegation versions, ordered player Actions, seed/entropy stream and owner-domain Event sequence;
- defeat/retreat/abort/fail-safe preserve already-committed Events without pretending completion;
- rewards/resources/advancement route through their owning domains; irreversible advancement remains human-required;
- AI may narrate resolved player-safe state only and is never mechanical, GM or hidden-information authority;
- no-AI deterministic text/templates/manual presentation must complete the encounter.

First operation: re-fetch App main and migration head **once**, inspect current A6 Action, A7 combat/runtime, Adventure/encounter, D05 visibility, APM-I01 delegation/run and D12 recovery seams, determine whether encounter-run state genuinely requires a new additive migration, then implement the smallest complete deterministic single-encounter loop.

Canonical App baseline after APM-I02: `8d3684ed5ae8058518a8684d9f2d68f21f893723`. Migration head remains `0012_csw_creator_library_memory.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through APM-I02 is completed_verified. APM-I03 is selected_not_started. Later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0012` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- owning domains remain authoritative for gameplay state and Events;
- D05 authorization precedes derived aggregation/presentation;
- APM delegation never replaces fresh owning-domain authorization;
- AutoGM package/controller state cannot duplicate Character, Campaign, Adventure, combat/rules or reward truth.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **APW-I05 remains**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **in progress**.
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

Current selection authorizes only APM-I03. It does not authorize APM-I04+, mini-campaign direction, Connected Cozy/multiplayer AutoGM, AI-as-GM authority, background encounter rounds, unbounded autonomous play, automatic irreversible Character choices, hidden scenario leakage, APW-I05+, CSW-I03+, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
