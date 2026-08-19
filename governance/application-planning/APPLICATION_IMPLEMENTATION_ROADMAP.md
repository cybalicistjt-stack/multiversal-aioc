# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.0.0  
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
| APW-I05 | **selected_not_started** | `APW-I05-attempt-001` | inspect live head first |

### APM-I03 completion evidence

Application PR #213 completed from exact validated head `f94f68154ba5aae64ad5ee81f20a7fc5d26140c1`. Repository-health run `32269349724` passed. Product run `32269350388` ended with self-hosted Windows PASS, self-hosted Linux PASS after an unchanged retry, and deterministic comparison PASS before squash merge `ffe354caccea7c2457de09c4a313fbb30834028f`.

APM-I03 delivered one deterministic foreground-only AutoGM encounter over ordinary authority: committed A6 Player Action handoff, A7 combat/timing/reaction authority, exact external encounter-package reference/version, controlled NPC/world response policy, APM-I01 classification plus fresh authorization, persisted reaction/human/proposal/stale/budget barriers, deterministic seed/Event/window recovery cursors, player-safe hidden-information projection, package-listed owner-domain completion and a complete no-AI path. Migration `0013_apm_autogm_encounter_foundation.json` stores D04/D12 binding/recovery references only; it does not copy combat, Character, reward or encounter-package payload truth.

Validation provenance is preserved in `APM-I03-attempt-001`: all 13 focused APM-I03 tests, invariant validation and TypeScript passed on the initial exact head, while Linux alone hit the existing A2 p95 fluctuation (`346.6231200000002ms` vs `250ms`). The failed jobs were rerun unchanged and passed; no source, test, threshold or validation scope was weakened.

## Current work — APW-I05

**APW-I05 — Creator Workshop reusable library and Sandbox/Lab integration** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `APW-I05-attempt-001`  
State: `selected_not_started`

APW-I05 turns the Personal creator foundation into a useful reusable Workshop and isolated experimentation surface without creating a new truth super-domain.

Required boundaries:
- stable D29 CreativeFragment/Creator Project/Library records remain the creative-support identity/provenance foundation;
- Workshop may organize reusable creative fragments, projects, templates, entity references and other authorized source references without transferring ownership or authority;
- reference, copy/fork/derive and sandbox-instance semantics must remain explicit and provenance-bearing;
- Sandbox/Lab experiments are isolated from live Campaign and global canonical state;
- World, Adventure, Character, Campaign, entity-catalog and other governed payload truth stays with its owning domains;
- Campaign-private/revoked sources are filtered through D05 before library search, counts, labels, previews and sandbox construction;
- experimentation cannot silently incorporate, publish or promote results;
- any governed incorporation/promotion uses an explicit owning-domain receipt path and current authorization;
- disable/re-enable and reload preserve compatible creative/sandbox provenance records;
- direct owner-domain/creator screens remain usable if Workshop orchestration is disabled;
- the core Internal Alpha path remains deterministic and usable without AI or paid providers.

First operation: re-fetch App main and migration head **once**, inspect current D29 CreativeFragment/Creator Library persistence, entity-catalog and World/Adventure authoring/reference seams plus Personal creator surfaces, determine whether Workshop organization or sandbox-instance provenance genuinely requires the next additive migration, then implement the smallest useful reusable Workshop + isolated Sandbox/Lab path.

Canonical App baseline after APM-I03: `ffe354caccea7c2457de09c4a313fbb30834028f`. Migration head: `0013_apm_autogm_encounter_foundation.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through APM-I03 is completed_verified. APW-I05 is selected_not_started. Later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0013` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- no monolithic APW/CSW/APM state store is authorized;
- D29 remains creative-support metadata/provenance/reference oriented, not governed World/Adventure/Campaign truth;
- D05 authorization precedes derived aggregation/presentation;
- reuse/sandbox orchestration cannot imply source ownership transfer or Campaign/global canonical mutation.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **APW-I05 remains**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **APM portion complete; CSW-I03/I04 remain**.
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

Current selection authorizes only APW-I05. It does not authorize CSW-I03+, APW-I06+, APM-I04+, a new creative/sandbox truth super-domain, silent Campaign/global canonical mutation, automatic incorporation/publication, hidden/private source leakage, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
