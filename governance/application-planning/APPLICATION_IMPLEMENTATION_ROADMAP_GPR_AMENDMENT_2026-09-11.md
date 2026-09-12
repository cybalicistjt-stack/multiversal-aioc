# Application Implementation Roadmap — GPR Amendment — 2026-09-11

**Status:** OWNER-APPROVED FUTURE PLANNING AMENDMENT  
**Program:** GPR — Gameplay Pattern Runtime & Loop Minis  
**Implementation authority:** none

## Decision

Insert GPR after MRCS and before MERA:

`CNI-01..13 → PCA-01..16 → MCS-01..21 → MCCS-01..21 → MNCS-01..24 → MAS-01..21 → MSAS-01..21 → MRCS-01..21 → GPR-01..16 → MERA-01..24 → MBES-01..24 → SMB-08 → SMB-09`

This amendment supersedes only the MRCS→MERA direct successor wiring in the earlier MERA planning amendment. It does not change current product execution. ARI-16 remains the selected live work item with no implementation branch or implementation authority.

## Why GPR belongs here

MAL is already completed and supplies the original microgame/ambient-loop foundation. The later 175-game research established a much broader reusable gameplay capability: 168 patterns, 461 primitives, 29 mechanics modules, 85 primitive-bound operations exercised in conformance, seven delivery modes, 129 presentation roles, deterministic replay/snapshot behavior and 672 adaptation cases.

GPR must come after MRCS because MRCS owns authoring of reusable rule/content definitions that GPR executes. It also benefits from already-completed MCS/MCCS/MNCS/MAS/MSAS creator surfaces.

GPR must come before MERA and MBES because engineering, repair, construction, settlement and later first-party content should consume one shared gameplay-pattern runtime rather than inventing separate bespoke interaction engines.

## Successor wiring

- MRCS-21 successor becomes **GPR-01**.
- GPR-16 successor is **MERA-01**.
- MERA activation becomes **after GPR-16**.
- MERA-24 remains successor to **MBES-01**.
- MBES-24 remains successor to **SMB-08**.
- SAA remains after SMB-09.

## Non-duplication rule

- MAL-01..10 remain `completed_verified` and frozen.
- GPR may reuse MAL contracts and reference fixtures but may not reopen MAL completion or silently replace its owner boundaries.
- MRCS remains definition/authoring authority; GPR is execution/composition.
- Existing Character, World, Scene, Combat, Inventory, Economy, Project and Action/Event owners remain authoritative.

## Research provenance

The planning baseline is stored at:

`governance/application-planning/gameplay-pattern-runtime/GPR_RESEARCH_BASELINE_v3.6.json`

The source research archive is identified there by exact SHA-256. The archive itself is not copied into AIOC and remains reference/conformance provenance only.

## Authority preservation

This amendment grants no GPR implementation branch or implementation authority. It does not move the current ARI pointer, reopen MAL, publish copyrighted reference assets, activate providers, reserve a migration, distribute to testers or deploy/release software.
