# Internal Alpha Feature Packets

**Program:** MV-IA-001  
**Status:** ACTIVE PACKET AND INTEGRATION INDEX  
**Owner:** John Brandon Turner

Implementation-ready and in-progress feature design packets, companion matrices, review receipts, and integration records are stored in this directory.

## Feature packet index

| Feature ID | Feature | Classification | Packet status | Implementation status | Packet | Companion artifacts |
|---|---|---|---|---|---|---|
| MV-IA-F002 | Universal Object Experience | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md` | none |
| MV-IA-F020 | Permissions and Hidden Information | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md` | `MV-IA-F020_PERMISSION_SURFACE_MATRIX.json` |
| MV-IA-F003 | Identity, Dashboard, and Workspace Selection | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md` | `MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json` |
| MV-IA-F021 | Autosave, Reconnect, Recovery, and Bounded Offline Use | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F021_AUTOSAVE_RECONNECT_RECOVERY_AND_BOUNDED_OFFLINE_USE.md` | `MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json` |
| MV-IA-F025 | Onboarding, Help, Diagnostics, and Issue Reporting | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md` | `MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json` |
| MV-IA-F004 | Character Creation and Advancement | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F004_CHARACTER_CREATION_AND_ADVANCEMENT.md` | `MV-IA-F004_CHARACTER_CREATION_MATRIX.json` |
| MV-IA-F005 | Campaign, Scene, and Session Builder | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F005_CAMPAIGN_SCENE_AND_SESSION_BUILDER.md` | `MV-IA-F005_CAMPAIGN_SCENE_SESSION_MATRIX.json`; traceability; receipt; readiness; completion |
| MV-IA-F012 | Encounter Builder and Balance Lab | alpha-required | implementation-ready | not started; dependency-gated | `MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md` | `MV-IA-F012_ENCOUNTER_BALANCE_MATRIX.json`; traceability; receipt; readiness; completion |

## Integration review index

| Review ID | Scope | Status | Review | Contract matrix | Findings | Receipt | Completion record |
|---|---|---|---|---|---|---|---|
| IA-D02-006 | F002, F020, F003, F021, and F025 shared foundations | complete | `IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md` | `IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json` | resolved in review | `IA-D02-006_REVIEW_RECEIPT.md` | `IA-D02-006_COMPLETION_RECORD.json` |
| IA-D03-005 | Character/Campaign preparation: F004, F005, F012, and IA-D03-004 | complete | `IA-D03-005_CHARACTER_CAMPAIGN_INTEGRATION_REVIEW.md` | `IA-D03-005_CHARACTER_CAMPAIGN_CONTRACT_MATRIX.json` | `IA-D03-005_INTEGRATION_FINDINGS_REGISTER.json` | `IA-D03-005_REVIEW_RECEIPT.md` | `IA-D03-005_COMPLETION_RECORD.json` |

## Shared-foundation integration rule

All packets beginning with IA-D03 consume `IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json`, preserve stable IDs, authorization, projection safety, local/authoritative/Event/projection separation, idempotency, ambiguous-failure lookup, recovery, revocation, diagnostics, accessibility, provider neutrality, and zero-service fallback.

## Character/Campaign preparation result

IA-D03-005 proves that Character creation and advancement, Campaign/Scene/Session preparation, Encounter composition and advisory analysis, and the bounded deterministic fixture corpus form one coherent permission-safe, versioned, recoverable preparation path.

The integration defines 28 controlling contracts, eight journeys, twelve resolved findings, ten implementation slices, twenty-four blocking acceptance criteria, and zero blocking findings. It preserves 36 source-backed and 119 synthetic noncanonical fixture identities.

No integration artifact authorizes application implementation, canonical promotion, paid services, production credentials, real-user data collection, internal-alpha release, production deployment, or public release.

## Next item

**IA-D04-001 — MV-IA-F006 First Playable Action and GM Approval Loop.**
