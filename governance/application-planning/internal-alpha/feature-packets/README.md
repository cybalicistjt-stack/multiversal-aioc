# Internal Alpha Feature Packets

**Program:** MV-IA-001  
**Status:** ACTIVE PACKET INDEX  
**Owner:** John Brandon Turner

Implementation-ready and in-progress feature design packets are stored in this directory.

## Status values

- `packet-in-progress`
- `implementation-ready`
- `implemented`
- `validated`
- `alpha-ready`
- `deferred`

## Packet index

| Feature ID | Feature | Classification | Packet status | Implementation status | Packet | Companion artifacts |
|---|---|---|---|---|---|---|
| MV-IA-F002 | Universal Object Experience | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md` | none |
| MV-IA-F020 | Permissions and Hidden Information | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md` | `MV-IA-F020_PERMISSION_SURFACE_MATRIX.json` |
| MV-IA-F003 | Identity, Dashboard, and Workspace Selection | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md` | `MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json` |
| MV-IA-F021 | Autosave, Reconnect, Recovery, and Bounded Offline Use | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F021_AUTOSAVE_RECONNECT_RECOVERY_AND_BOUNDED_OFFLINE_USE.md` | `MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json` |
| MV-IA-F025 | Onboarding, Help, Diagnostics, and Issue Reporting | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md` | `MV-IA-F025_ONBOARDING_SUPPORT_MATRIX.json` |

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

## Completed shared-foundation packets

### MV-IA-F002

Reusable browser, inspector, source, provenance, relationship, comparison, and picker experience.

### MV-IA-F020

Deny-by-default authorization, field-safe projection, safe query and inference, role and delegation boundaries, private and GM-only handling, realtime and export controls, revocation, support access, diagnostics, AI restrictions, and permission recovery states.

### MV-IA-F003

Stable provider-neutral identity, invitations, role-aware dashboards, recent-work and notification safety, selected-context receipts, deep-link authorization, switching, revocation, recovery, responsive behavior, and accessible entry.

### MV-IA-F021

Local and authoritative state boundaries, autosave, idempotency, status lookup, Event-gap recovery, pending-GM continuity, conflict preservation, checkpoint restore, bounded offline use, revocation, and provider-exit compatibility.

### MV-IA-F025

Role-specific onboarding, release identity, contextual help, known limitations, structured issue reporting, diagnostic allowlisting and redaction, attachment preview and consent, receipts, follow-up, export-only operation, accessibility, recovery, zero-service operation, and support-access separation.

## Next item

`IA-D02-006_SHARED_FOUNDATIONS_INTEGRATION_REVIEW.md`
