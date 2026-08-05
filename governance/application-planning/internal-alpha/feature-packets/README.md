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

## Integration review index

| Review ID | Scope | Status | Review | Contract matrix | Receipt | Completion record |
|---|---|---|---|---|---|---|
| IA-D02-006 | F002, F020, F003, F021, and F025 shared foundations | complete | `IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md` | `IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json` | `IA-D02-006_REVIEW_RECEIPT.md` | `IA-D02-006_COMPLETION_RECORD.json` |

## Packet rule

Every implementation-ready packet must:

- use the standard 24-section template;
- match registry identity and status;
- define a bounded alpha slice and explicit exclusions;
- define role, permission, entitlement, persistence, recovery, responsive, accessibility, telemetry, security, cost, and test behavior;
- include exact blocking acceptance criteria;
- identify owner gates and dependency holds;
- pass `validate_feature_packets.py`;
- provide every registry-listed companion artifact;
- keep companion identity, ownership, acceptance criteria, and implementation boundary consistent.

An implementation-ready design packet does not authorize code, provider activation, spending, real tester data collection, production, alpha release, or public release.

## Shared-foundation integration rule

All packets beginning with IA-D03 must consume `IA-D02-006_SHARED_FOUNDATIONS_CONTRACT_MATRIX.json`.

They must:

- declare consumed `SFI-C###` contract IDs;
- use canonical role IDs and contract fields;
- treat selected-context receipts as nonauthoritative;
- authorize before counts, facets, suggestions, relationships, and serialization;
- use stable IDs rather than display names or provider IDs;
- distinguish local draft, authoritative save, submitted command, accepted Event, and current projection;
- define idempotency and ambiguous-failure status lookup;
- define revocation, reconnect, conflict, and bounded offline behavior;
- define role-safe diagnostics and separate support access;
- define equivalent responsive and accessible behavior;
- preserve provider-neutral adapters and zero-service fallback;
- record implementation dependencies and owner gates.

A later packet may extend a shared contract only with recorded consumer impact, compatibility impact, migration impact, retest list, fallback, and documentation update.

## Completed shared-foundation result

The IA-D02 packets and integration review establish:

- stable provider-neutral subject identity;
- deny-by-default authorization and field-safe projection;
- permission-safe workspace discovery and selected context;
- stable-ID object browse, inspection, comparison, and selection;
- explicit authority states and durable receipts;
- idempotency, reconnect, Event-gap recovery, conflict preservation, and revocation;
- bounded offline reading and local drafts with no offline authoritative mutation;
- exact release identity, contextual help, diagnostic exclusion, redaction, consent, quarantine, and issue receipts;
- issue-reporting and support-access separation;
- desktop, tablet, mobile, keyboard, touch, screen-reader, zoom, reduced-motion, and noncolor equivalence;
- provider-neutral and zero-paid-service, zero-AI core operation.

## Completed Character preparation result

MV-IA-F004 establishes:

- Campaign- and rules-profile-bound Character identity and build state;
- stable-ID governed selection and source-linked calculation;
- explicit controller authority and role-safe projections;
- validation, activation, advancement, correction, migration, retirement, archival, and export contracts;
- idempotency, conflict preservation, reconnect, and bounded offline behavior;
- historical entitlement and append-only history requirements;
- accessible and responsive Character creation and advancement;
- twenty acceptance criteria and deterministic fixtures.

## Completed Campaign preparation result

MV-IA-F005 establishes:

- Campaign rules, packs, policy, membership, invitation, role, and Character-control boundaries;
- Scene drafts, stable-ID placements, local overrides, notes, maps, visibility, objectives, and launch configuration;
- server-generated Player and observer previews without protected existence or count leakage;
- immutable launch snapshots and separate authoritative Session state;
- idempotent saves and commands, conflict preservation, Event-gap recovery, revocation, and bounded offline behavior;
- realtime as advisory and durable Events plus current server projections as authority;
- role-safe exports and diagnostics, accessible and responsive preparation, and zero-paid-service operation;
- twenty acceptance criteria and deterministic fixtures.

## Next item

`MV-IA-F012_ENCOUNTER_BUILDER_AND_BALANCE_LAB.md` under IA-D03-003.
