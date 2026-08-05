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

## Next packet

`MV-IA-F003_IDENTITY_DASHBOARD_AND_WORKSPACE_SELECTION.md`
