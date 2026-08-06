# Internal Alpha Feature Packets

**Program:** MV-IA-001  
**Status:** ACTIVE PACKET AND INTEGRATION INDEX  
**Owner:** John Brandon Turner

Implementation-ready and in-progress feature design packets, companion matrices, review receipts, and integration records are stored in this directory.

## Status values

- `packet-in-progress`
- `implementation-ready`
- `implemented`
- `validated`
- `alpha-ready`
- `deferred`

## Feature packet index

| Feature ID | Feature | Classification | Packet status | Implementation status | Packet | Companion artifacts |
|---|---|---|---|---|---|---|
| MV-IA-F002 | Universal Object Experience | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md` | none |
| MV-IA-F020 | Permissions and Hidden Information | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md` | `MV-IA-F020_PERMISSION_SURFACE_MATRIX.json` |
| MV-IA-F003 | Identity, Dashboard, and Workspace Selection | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md` | `MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json` |
| MV-IA-F021 | Autosave, Reconnect, Recovery, and Bounded Offline Use | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F021_AUTOSAVE_RECONNECT_RECOVERY_AND_BOUNDED_OFFLINE_USE.md` | `MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json` |
| MV-IA-F025 | Onboarding, Help, Diagnostics, and Issue Reporting | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md` | `MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json` |
| MV-IA-F004 | Character Creation and Advancement | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md` | `MV-IA-F004_CHARACTER_CREATION_MATRIX.json` |
| MV-IA-F005 | Campaign, Scene, and Session Builder | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md` | `MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json`; `MV-IA-F005_IMPLEMENTATION_TRACEABILITY.json`; `MV-IA-F005_REVIEW_RECEIPT.md`; `MV-IA-F005_READINESS_RECORD.md`; `MV-IA-F005_COMPLETION_RECORD.json` |
| MV-IA-F012 | Encounter Builder and Balance Lab | alpha-required | implementation-ready | not started; dependency-gated | `MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md` | `MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json`; `MV-IA-F012_IMPLEMENTATION_TRACEABILITY.json`; `MV-IA-F012_REVIEW_RECEIPT.md`; `MV-IA-F012_READINESS_RECORD.md`; `MV-IA-F012_COMPLETION_RECORD.json` |

## Integration review index

| Review ID | Scope | Status | Review | Contract matrix | Receipt | Completion record |
|---|---|---|---|---|---|---|
| IA-D02-006 | F002, F020, F003, F021, and F025 shared foundations | complete | `IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md` | `IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json` | `IA-D02-006_REVIEW_RECEIPT.md` | `IA-D02-006_COMPLETION_RECORD.json` |

## Packet rule

Every implementation-ready packet must use the standard 24-section template, match registry identity and status, define a bounded alpha slice and explicit exclusions, cover permissions, persistence, recovery, responsive and accessible behavior, telemetry, security, cost, tests, exact blocking acceptance criteria, owner gates, dependency holds, companion artifacts, and machine validation.

An implementation-ready packet does not authorize code, provider activation, spending, real tester data collection, production, alpha release, or public release.

## Shared-foundation integration rule

All packets beginning with IA-D03 consume `IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json`, declare SFI-C001 through SFI-C024 as applicable, preserve stable IDs, authorization, projection safety, local/authoritative/Event/projection separation, idempotency, ambiguous-failure lookup, recovery, revocation, diagnostics, accessibility, provider neutrality, and zero-service fallback.

## Completed Character preparation result

MV-IA-F004 establishes governed Character identity, selection, calculation, control, lifecycle, history, recovery, accessibility, twenty acceptance criteria, and deterministic fixtures.

## Completed Campaign preparation result

MV-IA-F005 establishes Campaign rules and packs, membership, Scene drafts and placements, safe previews, launch snapshots, Session state, recovery, exports, accessibility, twenty acceptance criteria, and deterministic fixtures.

## Completed Encounter preparation result

MV-IA-F012 establishes governed Encounter composition, stable-ID provenance, dependency and compatibility validation, twelve pressure dimensions, uncertainty and source-grounded warnings, deterministic bounded simulation, comparisons, permission-safe projections, Scene attachment, recovery, exports, accessibility, zero-service operation, twenty blocking acceptance criteria, forty-eight denied cases, and ten deterministic fixtures. It prohibits guaranteed-balance, fairness, safety, victory, survival, optimality, and actual-play prediction claims.

## Next item

IA-D03-004 — internal-alpha content and deterministic fixture specification.
