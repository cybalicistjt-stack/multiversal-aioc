# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 3.0.0  
**Status:** ACTIVE — CLEANED CURRENT ROADMAP  
**Owner and final authority:** John Brandon Turner  
**Last updated:** 2026-08-18

## Authority and purpose

This is the concise current application roadmap. Detailed historical roadmap revisions remain preserved in Git history and completion receipts; they are not current-work selectors.

Current work is selected only by:

1. `governance/ai/MULTIVERSAL_NEW_CONVERSATION_BOOTSTRAP.md`
2. `governance/ai/runtime/ACTIVE_AUTHORITY_REGISTRY.json`
3. `governance/ai/runtime/CURRENT_WORK_POINTER.json`
4. the checkpoint named by that pointer
5. live GitHub branch/PR/CI evidence

Repository evidence is mandatory. A historical workflow, validator, work order, amendment, branch, PR, roadmap revision or checkpoint cannot regain authority merely because it still exists in Git history.

## Current verified position

### Completed foundations

- Phase 9 bounded implementation through P9-06-023: **COMPLETED_VERIFIED**.
- Developer Toolbelt DT-001 through DT-010: **COMPLETED_VERIFIED**.
- Stage A A0 through A12: **COMPLETED_VERIFIED**.
- Internal Alpha tester access, 20-account physical role testing, GATX T01 through T08 including remote/geographic proof: **COMPLETED_VERIFIED**.
- PPIA-01 through PPIA-16: **COMPLETED_VERIFIED**.
- CAPP-01 through CAPP-12: **COMPLETED_VERIFIED**.
- CCTI-01 through CCTI-11 and CCTI-12 T01 through T03: **COMPLETED_VERIFIED**.
- VCH-01 through VCH-06 Validation Core Hardening: **COMPLETED_VERIFIED**. Closure: App PR #200, validated head `70e0480030c39ecd67c3c137eb2e3ba666e92bf8`, merge `aa286a481fc53fdb969cc10be0388974bdbd3c9e`.
- CRS-01 through CRS-06 Canonicalization & Retirement Sweep: **COMPLETED_VERIFIED**. App repository-health PR #202 merged `ec4ad52910fd8728134df4bdbad31476f44602e9`; AIOC health PR #405 merged `9a74d10988ca41201c8155956a09564c7d1289a9`; final audit result `zero_known_conflicting_authority`.

### Active work

**POST-GATX-SUCCESSOR — current selected operation.**

- App PR: #201
- Branch: `internal-alpha/post-gatx-successor-refresh`
- Observed pre-reconciliation head: `3a80eae066650a312707cfae5adb70a2770e8918`
- Clean App main baseline after CRS: `ec4ad52910fd8728134df4bdbad31476f44602e9`
- State: `IN_PROGRESS`; draft/non-merge-authorized until its exact completion gate passes.
- Scope: deterministic successor package builder/verifier and the minimum current validation surface only. Historical PR #185 is superseded and is not an integration path.
- Required next action: reconcile PR #201 to cleaned main without restoring retired workflows/validators; explicitly register any active successor-specific validation surface; run one frozen exact-head self-hosted Linux/headed + Windows/PowerShell + deterministic comparison gate with bound artifacts.
- Merge creates a validated successor candidate only. Tester distribution remains a separate owner decision for the exact package/SHA-256.

### Preserved unfinished work

**CCTI-12-T04 — Local Review Worksets & Proposal Disposition**

- App PR #191.
- Construction complete; **VALIDATION_QUARANTINED / NOT COMPLETE**.
- Known prior failure class: brittle repeated-boundary UI assertion around `Canonical taxonomy: OFF`.
- VCH and CRS now provide the runner, compact evidence, deterministic comparison and clean authority model needed to resume safely.
- T04 may merge only after reconciliation to cleaned main, targeted repair from exported evidence, and exact-final-head Windows + Linux + deterministic comparator success.

**WP-011 — Tauri iOS/iPadOS Spike**

- Preserved Mac-dependent special-environment work.
- May temporarily preempt normal order when the borrowed Mac is available.

**DS-008 — Design Standards exact-byte ingestion**

- Remains blocked on an exact-byte-capable transfer/validation surface.
- Do not reconstruct checksum-bound source bytes from excerpts, screenshots, OCR or memory.

## Owner-approved future planning tracks

- **APW — Asynchronous Play & Persistent Workspace:** planned, not implementation-active.
- **CSW — Creator Storycraft Workspace:** planned, not implementation-active.
- **APM — Automated Play Modes:** planned, not implementation-active. Covers governed AutoGM and CozyMode without creating a separate game engine. Full approved tranche/order detail is in `APPLICATION_IMPLEMENTATION_ROADMAP_APM_SUPPLEMENT.md`.

The approved combined design order is:

`APW-01 → APM-01 → CSW-01 → CSW-02 → APW-02 → APW-03 → APW-04 → APM-02 → CSW-03 → CSW-04 → CSW-05 → APM-03 → CSW-06 → APM-04 → CSW-07 → CSW-08 → APW-05 → CSW-09 → APW-06 → APM-05 → CSW-10 → APW-07 → APM-06 → APW-08`.

## Current productive execution sequence

Unless newer owner direction or repository evidence changes dependencies:

1. **Finish POST-GATX-SUCCESSOR** from App PR #201 on cleaned current main and the deny-by-default validation lifecycle.
2. **Return to CCTI-12-T04** through the hardened Validation Core, reconcile it to cleaned main, repair only evidence-proven failures, and satisfy its original exact-final-head Windows/Linux/comparator gate.
3. **Begin the approved APW/CSW/APM interleaved design sequence** beginning APW-01 → APM-01 → CSW-01.
4. **Give WP-011 temporary priority whenever the borrowed Mac becomes available.**
5. **Close DS-008 before UI-heavy APW-06 / CSW-09 if practical.**

## Validation and repository-health rules

- `MULTIVERSAL_SELF_HOSTED_FINAL_VALIDATION_POLICY.md` controls normal application/package completion: owner-controlled self-hosted Windows + Linux with deterministic comparison where outputs should agree.
- `MULTIVERSAL_AUTHORITY_AND_RETIREMENT_POLICY.md` controls lifecycle authority: unregistered or superseded material is inert.
- AIOC's single bounded GitHub-hosted repository-health workflow is a governance-only exception because no AIOC self-hosted runner is attached. It cannot satisfy an application/package completion gate.
- App `main` permits only registered live workflows. Historical workflows removed by CRS remain available in Git history but have no automatic authority.
- Historical validators are deny-by-default. Active work may use only registered current validators or explicitly bounded/current-compatible validation surfaces.
- A validation-interface failure may quarantine the affected feature after bounded diagnosis; it never converts unfinished work into complete and should not freeze independent work indefinitely.

## Product-wide approved concerns

- **TODO-UX-VOICE:** Multiversal is a knowledgeable, creative companion: warm enough to invite experimentation, confident enough to give clear guidance, and restrained enough to respect the user.
- **TODO-FSF / Family Safety Framework:** parental controls govern Multiversal-controlled capabilities/exposure, not the conduct or fictional content introduced by other humans. Guardian authority remains separate from GM/Campaign authority and does not imply automatic access to private creative work.

## Mandatory execution behavior

- “Continue” means execute the next verified unfinished operation.
- Read the current pointer/checkpoint and reconcile live GitHub before changing work.
- Preserve unfinished parallel tracks without allowing them to compete for current authority.
- Do not call work complete without its declared evidence.
- Do not revive retired workflows, validators, work orders or amendments from historical branches without explicit registration/current authority.
- Preserve provenance, stable IDs, hidden-information boundaries, permissions, reversibility and owner gates.
- Public release/deployment remains separately owner-gated.
