# Bootstrap Current-State Amendment — VCH-06 Completion, APM Addition, Post-GATX Activation

**Status:** ACTIVE CURRENT-STATE AMENDMENT  
**Owner and final authority:** John Brandon Turner  
**Date:** 2026-08-18

This amendment supersedes older compact recovery projections where they conflict with the evidence below. The canonical bootstrap and full roadmap remain controlling for general procedure and scope.

## Completed in this milestone

### VCH — Validation Core Hardening

VCH-01 through VCH-06 are `COMPLETED_VERIFIED`.

VCH-06 completed in two repository stages because the substantive adoption PR was merged while the repository-bound closure receipt was being sealed:

- substantive application PR #199 merged as `b815906c2bd68aab7421c86684d613b733533e34` after DT-004, DT-005, and VCH-06 had each passed self-hosted Windows, self-hosted Linux, and deterministic comparison on substantive candidate head `9ab9a3ee2a3a804810d1f3964fdccf0e019b6a39`;
- corrective receipt-bearing closure application PR #200 then restored the unintended historical A2 Exact Scope workflow drift detected by the new closure audit and proved the complete declared gate on exact final head `70e0480030c39ecd67c3c137eb2e3ba666e92bf8`;
- corrective PR #200 merged as `aa286a481fc53fdb969cc10be0388974bdbd3c9e` with no further final-head movement.

Exact receipt-bearing final evidence:

- DT-004 final run `32166962863`: self-hosted Windows PASS, self-hosted Linux PASS, deterministic comparison PASS;
- DT-005 final run `32166962815`: self-hosted Windows PASS, self-hosted Linux PASS, deterministic comparison PASS;
- VCH-06 final run `32166962770`: self-hosted Windows PASS, self-hosted Linux PASS, deterministic comparison PASS;
- VCH-06 deterministic payload SHA-256 `c1412de2e335af1df984af3ba61c9f55e94f493497d59f1ea48038faf16b50e6`;
- VCH-06 comparison artifact `9335810990`, Linux artifact `9335776143`, Windows artifact `9335776144`;
- historical A2 Exact Scope workflow restored to VCH-05-baseline blob `706833234e664ed0e759b46bc302897338ec2ce9`;
- historical DT-002 workflow preserved at VCH-05-baseline blob `58a02ff03446b868e4e16a0feeaa4d16a361e7ce`;
- repository-bound closure receipt: `Multiversal-app/receipts/VCH-06-CLOSURE.json`.

The first corrective closure run was valuable evidence rather than a product failure: it was classified at the harness-integrity layer and exposed the historical A2 workflow drift before VCH was finally closed. The repaired receipt-bearing head then passed the complete gate.

The final comparison path used the owner-controlled self-hosted Windows/Linux architecture rather than GitHub-hosted compute. Queue delay observed during VCH-06 was runner serialization, not billing failure or feature failure.

VCH establishes the governed normal validation foundation: cause-based diagnostics, persistent-runner preflight, thin shared profiles, raw/compact evidence, deterministic receipts, cross-platform comparison, fault injection, and bounded representative adoption.

CCTI-12-T04 remains separately `validation_quarantined` and unfinished. VCH completion does not convert T04 into complete work.

## New owner-approved planning track

APM — Automated Play Modes is now an owner-approved planned/not-implementation-active track through AIOC PR #400, merge `217672c8dee5d5cd53ea1b5f4020ff0f76dd90ab`.

APM covers:

- AutoGM as bounded governed automated orchestration, not unrestricted AI GM authority;
- CozyMode as setting-independent low-pressure solo persistent/downtime play;
- later invited Connected Cozy;
- six planning tranches APM-01 through APM-06;
- approved APW/CSW/APM interleave in `APPLICATION_IMPLEMENTATION_ROADMAP_APM_SUPPLEMENT.md`;
- preferred implementation ladder: Cozy Solo → Single-Encounter AutoGM → Connected Cozy → AutoGM Mini-Campaign → broader/multiplayer AutoGM later.

APM does not move the present implementation pointer.

## Current selected operation

The selected primary operation is now **POST-GATX-SUCCESSOR-attempt-001**.

Repository: `cybalicistjt-stack/Multiversal-app`  
Branch: `internal-alpha/post-gatx-successor-distribution`  
PR: #185  
Observed preserved head: `5028a5d2bbdc73adeae6fa31ce719cd66e512969`

PR #185 is unfinished and diverged from newer main. Its old text still treats GitHub-hosted validation as a mandatory final hold; that is superseded by `MV-AI-VALIDATION-003` and must be reconciled. Do not automatically mark the old package complete merely because policy changed.

Exact next action:

1. reconcile PR #185 with current main, including the completed VCH baseline and receipt-bearing closure;
2. preserve its post-GATX package and remote-exclusion boundaries;
3. remove obsolete generic hosted-runner completion dependence in favor of the controlling self-hosted Windows/Linux deterministic gate;
4. adopt the hardened evidence/comparison path where appropriate;
5. run exact-final-candidate Windows, Linux/headed and deterministic comparison validation;
6. merge only if that gate passes;
7. treat the merge as a validated successor candidate, not automatic tester-distribution approval.

## Preserved parallel work

- CCTI-12-T04: `validation_quarantined`, PR #191, unfinished.
- DS-008-working-series-attempt-002: `blocked_non_owner`.
- WP-011 Apple: preserved and takes temporary priority when borrowed Mac hardware is available.
- APW / CSW / APM: owner-approved planning tracks, not implementation-active.
