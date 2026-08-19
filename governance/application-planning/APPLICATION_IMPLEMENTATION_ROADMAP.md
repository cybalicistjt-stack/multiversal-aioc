# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 5.5.0  
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
| CSW-I07 | **selected_not_started** | `CSW-I07-attempt-001` | inspect live head first |

### CSW-I06 completion evidence

Application PR #218 completed from exact validated head `8bbecee4ee3adcf068b07b73159361263d78cf50`. Repository-health run `32282219761` passed. Product run `32282219562` ended with self-hosted Linux PASS, self-hosted Windows PASS and deterministic comparison PASS before squash merge `c7aac6ffc91a8f7d4117f6a862a14cf5030692b3`.

CSW-I06 added migration `0017_csw_writing_studio_revision_workspace.json` only after live inspection proved a genuine D29 gap. The implementation separates stable WritingDocument identity, independent DocumentBranch lineage, high-frequency recoverable WorkingDraft generations and immutable append-only DocumentRevision/checkpoint evidence. Autosave does not create revision-history noise; stale writes fail without overwriting current authored text; deterministic revision compare and explicit candidate apply remain creator-controlled; reference context is authorization-filtered; exact revision export pins the revision and audience projection but never creates publication/canonical authority.

Validation history is preserved in `CSW-I06-attempt-001`: initial candidate `bbae8e332bb031fa163393bf9a16d88b176998f4` stopped at the same client TypeScript error on both lanes because the UI passed `description` to `EmptyState`, whose contract requires `body`. The repair was UI typing-only and did not weaken any persistence, privacy, history, export, no-AI or authority boundary. The repaired exact head passed every required gate.

## Current work — CSW-I07

**CSW-I07 — Reuse, Remix and Transformation** is the sole selected application implementation slice.

Repository: `cybalicistjt-stack/Multiversal-app`  
Attempt: `CSW-I07-attempt-001`  
State: `selected_not_started`

The governing source rule is:

`Exact authorized source snapshot → explicit derivative operation → new independent identity/version → independent editing → optional later compare/manual adaptation`

Never:

`Source changes → silent derivative mutation`.

Required boundaries:
- clone/adapt/fork/remix/template/transform always creates a new derivative identity/version and never reuses source identity;
- exact source object/version/revision/span evidence and transform provenance are retained;
- multi-source remix preserves each source/version independently;
- origin and destination Personal/Project/Campaign context classification is explicit and does not transfer authority;
- inherited references are classified as retained-compatible, destination-incompatible, inaccessible, detached, remapped or unresolved without leaking protected identity/cardinality;
- Campaign/runtime → reusable extraction reauthorizes before extraction and excludes material the creator cannot reuse; proposal/review-required or denied paths remain possible;
- source and derivative evolve independently; later source change produces only an advisory review state;
- compare/manual-adapt/explicit rebase-candidate flows never auto-merge source updates;
- compatibility findings remain evidence-backed/advisory unless an owning-domain operation genuinely requires compatibility;
- exact CSW-I06 WritingDocument/revision/span and CSW-I05 narrative structure sources may participate through stable refs without copying governed truth;
- deterministic transform recipes and no-AI reuse remain first-class; optional AI output stays candidate-only and must be explicitly applied;
- derivative creation/apply is idempotent and stale-source/concurrent edits fail without source/derivative overwrite;
- APW Workshop/Sandbox can consume derivative candidates without changing their authority class.

First operation: re-fetch App main and migration head **once**, inspect current D29 CreativeFragment source/relationship refs, Project Memory lineage, APW Workshop reuse/save-out receipts, CSW-I05/I06 exact-source seams and Campaign extraction/reference authorization boundaries, determine whether the smallest derivative model genuinely requires migration `0018`, then implement the first deterministic exact-snapshot derivative + source-drift review path.

Canonical App baseline after CSW-I06: `c7aac6ffc91a8f7d4117f6a862a14cf5030692b3`. Migration head: `0017_csw_writing_studio_revision_workspace.json`.

## Default strict implementation sequence

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

Everything through CSW-I06 is completed_verified. CSW-I07 is selected_not_started. Later slices remain inactive.

## Migration and ownership policy

- migrations `0001` through `0017` are immutable predecessors;
- every tranche rechecks current App main/migration head once before mutation;
- no next migration number is reserved in advance;
- no migration is added without a genuine durable schema delta;
- D29 CSW records may hold pre-authoritative creative support, writing history, derivative lineage, source-version observations, reference dispositions and provenance but never duplicate D18/D28/A9/Campaign authoritative payload truth;
- D05 authorization precedes source preview, search, lineage topology/counts, Campaign extraction, compatibility analysis, mapping, export and optional-AI context;
- derivative identity, prose, advisory findings and generated candidates never gain authority through source ancestry, polish, export, repetition or AI fluency;
- D18/D28/A9/Character/Campaign transitions remain explicit owning-domain operations.

## Internal Alpha milestones

1. Persistent Personal/async foundation — APW-I01, APW-I02, APW-I03 — **complete**.
2. Between-session and creator foundation — APW-I04, CSW-I01, CSW-I02, APW-I05 — **complete**.
3. First creator and automated experiences — CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03 — **complete**.
4. Deep creator workspace — CSW-I05, CSW-I06, CSW-I07 — **CSW-I05/I06 complete; CSW-I07 current**.
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

Current selection authorizes only CSW-I07. It does not authorize CSW-I08+, APW-I06+, APM-I04+, migration `0018` without a proven durable delta, silent source/derivative synchronization, Campaign/runtime extraction without explicit authority, permission/ownership/visibility/publication inheritance, automatic source-update merge, AI auto-apply, hidden lineage/reference leakage, T04 before September, tester distribution, release/deployment or paid-provider activation.

“Continue” means execute the next verified unfinished operation.
