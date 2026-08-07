# IA-D08-005 — Optional and Experimental Isolation Fixture Matrix

**Owner:** John Brandon Turner  
**Status:** DETERMINISTIC DESIGN FIXTURES

| ID | Scenario | Expected result |
|---|---|---|
| ISO-FX-001 | All optional capabilities disabled at startup | Core alpha initializes and core journeys remain available. |
| ISO-FX-002 | AI provider unavailable | Manual core workflow remains complete; AI surface shows bounded unavailable state. |
| ISO-FX-003 | AI quota exhausted mid-request | No canonical mutation occurs; user retains manual fallback and draft context. |
| ISO-FX-004 | AI response arrives after source version changes | Output is stale and must be revalidated before proposal use. |
| ISO-FX-005 | AI provider returns malformed payload | Payload is rejected; no partial core commit. |
| ISO-FX-006 | Advanced map renderer disabled | Semantic zones/list/outline positioning remain operational. |
| ISO-FX-007 | Unknown map processor is present in imported data | Processor is not executed; payload is preserved or explicitly rejected. |
| ISO-FX-008 | Advanced vehicle subsystem unsupported | Core vehicle ownership/control/station state remains valid and usable. |
| ISO-FX-009 | Broad offline hosting unavailable | Online authoritative path remains required; drafts/cache/reconnect recovery still work. |
| ISO-FX-010 | Optional module removed after records were created | Core records remain valid; optional extensions remain opaque/versioned where safe. |
| ISO-FX-011 | Feature flag changes from enabled to disabled | Optional surface disappears without changing canonical meaning or authority. |
| ISO-FX-012 | Feature flag changes while request is pending | Pending optional work cannot bypass fresh authorization/version validation. |
| ISO-FX-013 | Optional provider SDK returns provider-native ID | Provider ID is stored only as integration metadata, never canonical identity. |
| ISO-FX-014 | Optional telemetry pipeline fails | Core transaction and diagnostics continue; failure is typed as optional. |
| ISO-FX-015 | Optional telemetry receives hidden data candidate | Unauthorized/hidden content is filtered before emission. |
| ISO-FX-016 | Graph visualization unavailable | Relationship/investigation list/table/outline and nonvisual navigation remain complete. |
| ISO-FX-017 | Voice or image feature unavailable | Required task remains keyboard/text/touch accessible. |
| ISO-FX-018 | Optional export enrichment fails | Core export still succeeds without enrichment or fails explicitly without partial artifact. |
| ISO-FX-019 | Experimental simulation disagrees with core rules | Simulation remains advisory and cannot override authoritative rule resolution. |
| ISO-FX-020 | Optional processor requests wider permission scope | Request is denied; feature gate cannot widen authority. |
| ISO-FX-021 | Unknown extension round-trips through older client | Data is preserved opaquely where safe and not silently reinterpreted. |
| ISO-FX-022 | Optional dependency becomes incompatible after upgrade | Capability reports incompatible; core workflow remains available. |
| ISO-FX-023 | Optional provider times out during governed proposal preparation | Proposal remains draft/noncanonical; no half-applied result. |
| ISO-FX-024 | Removal-test configuration disables I1–I3 capabilities | Declared Internal Alpha core acceptance journeys still pass. |

## Coverage assertions

The matrix covers disabled, unavailable, quota, timeout, malformed, stale, unsupported, incompatible, revoked/removal, hidden-information, provider-identity, telemetry, accessibility, advanced-rendering, offline, atomicity, extension-preservation, feature-gate, and all-optionals-off cases.

## Pass rule

Every fixture must preserve core availability, canonical authority, permission filtering, deterministic recovery, accessibility, provenance, and explicit failure/fallback behavior without I4 coupling.
