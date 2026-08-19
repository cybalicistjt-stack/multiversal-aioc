# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 4.0.0  
**Status:** ACTIVE — FINAL DESIGN HANDOFF / IMPLEMENTATION ACTIVATION PENDING  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-19

## Authority and purpose

This is the concise current application roadmap. Historical revisions remain in Git history and receipts; they are not current-work selectors. Current work is selected only by bootstrap → authority registry → current pointer → selected checkpoint → live GitHub evidence.

## Completed verified foundations

Phase 9 through P9-06-023, DT-001–DT-010, Stage A A0–A12, Internal Alpha tester/GATX T01–T08, PPIA-01–16, CAPP-01–12, CCTI-01–11 plus CCTI-12 T01–T03, VCH-01–06, CRS-01–06, and POST-GATX-SUCCESSOR are **COMPLETED_VERIFIED**.

POST-GATX application evidence remains:
- App PR #203 exact head `3b9e33cb22b8d4e3f2558135ba0fc36a8c8ad223`, merge `8685165318b1f3782903bfe137ba8257539af017`;
- cross-platform run `32197192589`: Linux/headed-browser PASS, Windows packaged PowerShell PASS, deterministic byte comparator PASS;
- app repository-health `32197192592`: PASS;
- package `Multiversal-Internal-Alpha-Windows-3b9e33cb22b8-POST-GATX.zip`, SHA-256 `f07bfc00bb2708e48d0d85118fd1861e017b720d4d85ba1d912ede7b6b5bc694`;
- temporary validation exception retired in App PR #204 / current App main `bf61c64c89e7ea997842ea7442797fba619d0e28`.

Tester distribution remains separately owner-gated.

## APW / APM / CSW design series

The owner-approved combined design order is:

`APW-01 → APM-01 → CSW-01 → CSW-02 → APW-02 → APW-03 → APW-04 → APM-02 → CSW-03 → CSW-04 → CSW-05 → APM-03 → CSW-06 → APM-04 → CSW-07 → CSW-08 → APW-05 → CSW-09 → APW-06 → APM-05 → CSW-10 → APW-07 → APM-06 → APW-08`.

**APW-01 through APW-07, APM-01 through APM-06, and CSW-01 through CSW-10 are COMPLETED_VERIFIED.**

Current final design work is **APW-08 — Implementation Handoff and Stage/Internal-Alpha Integration**. APW-08 is building the final combined implementation packet, migration/change inventory, touch-point map, feature/fallback policy, deterministic acceptance program, Internal Alpha milestones and roadmap activation contract.

Application implementation is **not yet active**. The recommended first implementation item is APW-I01, but it may become current only after APW-08 itself passes exact-head validation, merges, and a separate canonical selector transition explicitly activates APW-I01.

## Final implementation handles

### APW

- APW-I01 — contextual account/role projection and Personal-context authority extensions
- APW-I02 — Personal Home and workspace switching
- APW-I03 — asynchronous Action submission, durable GM inbox and delayed resolution
- APW-I04 — bounded Campaign Activity/downtime integration
- APW-I05 — Creator Workshop, reusable library and Sandbox/Lab integration
- APW-I06 — notification, visibility, recovery and hybrid cross-device integration
- APW-I07 — whole-program live→async→GM result→Player return→live acceptance

### CSW

CSW-I01 through CSW-I08 are finalized by CSW-10 and remain additive D29/owning-domain implementation destinations. No new top-level creative truth store is authorized.

### APM

APM-I01 through APM-I06 are finalized by APM-06 and remain bounded automation implementation destinations over ordinary Multiversal authority/Event history. No second state engine or global AutoGM authority is authorized.

## Recommended strict implementation sequence after APW-08 closure

`APW-I01 → CSW-I01 → APM-I01 → APW-I02 → APW-I03 → APW-I04 → CSW-I02 → APM-I02 → APM-I03 → APW-I05 → CSW-I03 → CSW-I04 → CSW-I05 → CSW-I06 → CSW-I07 → APW-I06 → CSW-I08 → APM-I04 → APM-I05 → APM-I06 → APW-I07`

This order maximizes shared infrastructure while preserving the approved automated-play product ladder: Cozy Solo → Single-Encounter AutoGM → Connected Cozy → AutoGM Mini-Campaign.

## Current application baseline for handoff

- App main: `bf61c64c89e7ea997842ea7442797fba619d0e28`.
- Migration head: `database/migrations/0008_a10_world_content_authoring.json`.
- Existing migrations are immutable predecessors.
- `0009` is the current next slot only while that exact baseline remains unchanged; every implementation branch must re-check migration head before claiming a number.
- No monolithic APW/CSW/APM persistence store is authorized. Use additive records in established owning domains.

## Internal Alpha implementation milestones

1. **Persistent Personal/async foundation:** APW-I01, APW-I02, APW-I03.
2. **Between-session and creator foundation:** APW-I04, CSW-I01, CSW-I02, APW-I05.
3. **First creator and automated experiences:** CSW-I03, CSW-I04, APM-I01, APM-I02, APM-I03.
4. **Deep creator workspace:** CSW-I05, CSW-I06, CSW-I07.
5. **Integrated shell and connected automation:** APW-I06, CSW-I08, APM-I04, APM-I05, APM-I06.
6. **Whole-system hybrid proof:** APW-I07.

Each milestone remains feature-flagged, additive, no-AI capable where specified, and compatible with ordinary existing play.

## Deferred work — CCTI-12-T04

**CCTI-12-T04 — Local Review Worksets & Proposal Disposition remains unfinished and owner-deferred until September 2026.**

Owner decision: `governance/ai/runtime/OWNER_DECISION_2026-08-18_DEFER_CCTI12_T04_TO_SEPTEMBER.md`.

Preserve App PR #191 and branch `internal-alpha/ccti12-t04-local-review-worksets` plus partial reconstruction `internal-alpha/ccti12-t04-clean` as provenance only. Neither gains merge authority by existence. Do not advance T04 during August absent explicit owner override. On/after 2026-09-01, first establish the owner-approved GitHub-hosted T04 validation path or explicit bounded policy exception before re-evaluating preserved work against then-current App main.

## Other preserved unfinished work

- **WP-011:** Mac-dependent special-environment work; may temporarily preempt normal implementation order when the borrowed Mac is available.
- **DS-008:** blocked on exact-byte-capable non-owner transfer/validation; never reconstruct checksum-bound bytes from excerpts, OCR or memory.

## Next productive route after APW-08

If APW-08 passes exact-head AIOC repository health and merges while the current owner deferral/environment states remain unchanged:

1. close APW/APM/CSW planning `completed_verified`;
2. explicitly select **APW-I01-attempt-001** in `cybalicistjt-stack/Multiversal-app` as `selected_not_started`;
3. grant implementation authority for APW-I01 only;
4. revalidate App main and migration head before the first application change;
5. keep T04 deferred, WP-011 dormant unless hardware appears, and DS-008 blocked;
6. keep tester distribution, release and deployment separately owner-gated.

## Permanent repository-health and completion rules

- Unregistered/superseded workflows, validators, selectors, branches and PRs are inert by existence.
- Governance/AIOC exact-head repository health does not substitute for product/platform validation.
- Normal application/package final acceptance uses owner-controlled self-hosted Windows + Linux plus deterministic comparison where outputs should agree, unless a bounded owner-approved exception explicitly applies.
- One stable operation identity represents one authoritative intent across retries; accepted effects are at-most-once.
- Authorization/visibility filtering precedes counts, search, topology, notifications, diagnostics, exports and optional-AI context.
- Artifact existence, partial tests, or a previous-conversation claim never establishes completion.
- Only evidence-backed `completed_verified` is complete.
- Successor work does not reopen completed Stage A evidence unless fresh independent evidence demonstrates a predecessor regression.

## Product-wide approved concerns

- **TODO-UX-VOICE:** knowledgeable, creative companion; warm, welcoming, clear, confident, restrained and respectful of user intelligence/autonomy; encouraging without obsequiousness.
- **TODO-FSF:** parental controls govern Multiversal-controlled capability/exposure; guardian authority remains separate from GM/Campaign authority and does not imply access to private creative work.

## Mandatory execution behavior

“Continue” means execute the next verified unfinished operation. Preserve provenance, hidden-information boundaries, permissions, reversibility and owner gates. Public release/deployment and tester distribution remain separately owner-gated.
