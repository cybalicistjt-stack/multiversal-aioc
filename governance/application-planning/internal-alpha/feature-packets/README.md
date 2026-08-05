# Internal Alpha Feature Packets

**Program:** MV-IA-001  
**Status:** ACTIVE PACKET INDEX  
**Owner:** John Brandon Turner

Implementation-ready and in-progress feature design packets are stored in this directory.

## Status values

- `packet-in-progress` — packet is being completed and is not yet a valid implementation handoff.
- `implementation-ready` — design packet passes readiness validation; implementation may still be blocked by repository dependencies or owner gates.
- `implemented` — bounded repository implementation exists.
- `validated` — required implementation tests and reviews pass.
- `alpha-ready` — integrated candidate passes feature and release gates.
- `deferred` — explicitly outside the current bounded scope.

## Packet index

| Feature ID | Feature | Classification | Packet status | Implementation status | Packet | Companion artifacts |
|---|---|---|---|---|---|---|
| MV-IA-F002 | Universal Object Experience | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F002_UNIVERSAL_OBJECT_EXPERIENCE.md` | none |
| MV-IA-F020 | Permissions and Hidden Information | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F020_PERMISSIONS_AND_HIDDEN_INFORMATION.md` | `MV-IA-F020_PERMISSION_SURFACE_MATRIX.json` |
| MV-IA-F003 | Identity, Dashboard, and Workspace Selection | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md` | `MV-IA-F003_IDENTITY_WORKSPACE_MATRIX.json` |
| MV-IA-F021 | Autosave, Reconnect, Recovery, and Bounded Offline Use | entry-critical | implementation-ready | not started; dependency-gated | `MV-IA-F021_AUTOSAVE_RECONNECT_RECOVERY_AND_BOUNDED_OFFLINE_USE.md` | `MV-IA-F021_RECOVERY_AND_OFFLINE_MATRIX.json` |

## Packet rule

Every implementation-ready packet must:

- use the standard 24-section template;
- match the machine registry identity and status;
- define a bounded alpha slice and explicit exclusions;
- define role, permission, entitlement, persistence, recovery, responsive, accessibility, telemetry, security, cost, and test behavior;
- include exact blocking acceptance criteria;
- identify owner gates and dependency holds;
- pass `validate_feature_packets.py`;
- provide every registry-listed companion artifact;
- keep machine-readable companion identity, ownership, acceptance criteria, and implementation boundary consistent with the packet.

An implementation-ready design packet does not by itself authorize code, provider activation, spending, production, alpha release, or public release.

## Completed shared-foundation packets

### MV-IA-F002

Establishes the reusable browser, inspector, source, provenance, relationship, comparison, and picker experience.

### MV-IA-F020

Establishes deny-by-default authorization, field-safe projection, safe query and inference behavior, role and delegation boundaries, Player-private and GM-only handling, realtime and export controls, revocation, support access, diagnostics, AI restrictions, and permission recovery states.

The companion matrix records ten visibility classes, twenty-eight protected surfaces, internal and user-safe reason codes, twenty denied cases, and twenty blocking acceptance criteria.

### MV-IA-F003

Establishes stable provider-neutral subject identity, identity mappings, authentication-session lifecycle, invitation lifecycle, role-aware dashboards, recent-work and notification safety, explicit selected-context receipts, deep-link authorization, role and Campaign switching, revocation, account recovery, responsive behavior, and accessible entry flows.

The companion matrix records eight role contexts, nine workspace types, six primary entry flows, twenty protected discovery surfaces, twenty denied cases, selected-context receipt fields, zero-service requirements, and twenty blocking acceptance criteria.

### MV-IA-F021

Establishes exact local-versus-authoritative state vocabulary, local autosave receipts, stable operation and command IDs, idempotent retry, expected-version conflicts, ambiguous command-status lookup, Event-gap recovery, duplicate suppression, pending-GM continuity, selected-context revalidation, service-restart and checkpoint recovery, history-preserving restore, and privacy-safe diagnostics.

The bounded offline slice permits only manifest-listed read-only projections and approved local drafts. It explicitly prohibits offline authoritative mutation, silent last-write-wins, client-generated Events, unverified checkpoint restore, and indefinite offline entitlement.

The companion matrix records sixteen state values, ten operation types, fifteen interruption points, fifteen protected recovery surfaces, twenty-four denied cases, required reconnect and conflict fields, offline capability boundaries, ten required receipt families, and twenty blocking acceptance criteria.

## Next packet

`MV-IA-F025_ONBOARDING_HELP_DIAGNOSTICS_AND_ISSUE_REPORTING.md`
