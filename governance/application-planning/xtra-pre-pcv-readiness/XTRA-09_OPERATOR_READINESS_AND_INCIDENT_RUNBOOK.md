# XTRA-09 — Operational, Privacy and Incident Readiness

**Version:** 1.0.0. **Classification:** source-derived operator preparation, not a deployed service or security certification. Companion: `XTRA-09_OPERATIONAL_PRIVACY_INCIDENT_MATRIX_v1.0.0.json` and `tests/control_plane/test_xtra09_operator_readiness.py` (51 synthetic scenarios, seven gate families, 44 defensive denials).

## Source evidence and proof boundary

- `XTRA-02_RENDER_CERTIFICATION_RECOVERY_2026-11-02.md`: read-only inventory recorded a free PostgreSQL 17 Render certification database, available on November 2, expiring **2026-11-08T11:53:54Z**; empty external IP allowlist, no verified export, no restore. XTRA-02 remains **blocked_external**. An availability indicator never proves recoverability.
- `governance/phase9/P9-04_POSTGRES_CENTERED_ARCHITECTURE_CONTRACT.md`: provider-neutral identity, entitlement, persistence, authoritative command, realtime, checkpoint, object storage and telemetry boundaries; encryption, least privilege, migration and restore gates.
- `governance/application-planning/product-convergence/PCV-I01C_LOCAL_HOST_PRODUCTION_SERVICE_AUTHORITY_ENTITLEMENT_CONTRACT_v1.0.0.json`: local-host and managed-service executors must preserve one canonical history and a single current mutation authority epoch.
- `governance/application-planning/internal-alpha/owner-decision/IA_D09_CANDIDATE_DATA_PRIVACY_BOUNDARY.md`: only synthetic/test-only data is authorized for the candidate; no real-user content, credentials, private prose or raw provider payloads in diagnostics.
- `XTRA-06_PCV_ACCEPTANCE_HANDOFF.md` and `XTRA-08_THREAT_PREFLIGHT_AND_OWNER_HANDOFF.md`: future PCV and live allowance/security tests remain explicitly unexecuted.

## Operator preflight

Before operational decisions, identify environment, selected authoritative executor, service build/config revision, actual privacy classification, owner role, provider status, current health observation, backup receipt and restore evidence. Preserve unknown entries as `NOT_OBSERVED`. Check authentication, current Campaign membership, entitlement, durable Session revision/checkpoint and authorized projections separately; generic internet reachability or websocket presence is not proof of Session health.

A safe observation receipt includes UTC timestamp, environment, source head, probe category, scope, redacted outcome, failure category and correlation reference. Exclude personal data, hidden GM notes, tokens, billing payloads, database credentials and raw private logs. Do not represent a fictional probe as a real service measurement.

## Alert/incident matrix

| Severity | Trigger | Triage action | Required independent closeout |
| --- | --- | --- | --- |
| P0 preservation | Expiry approaching without verified independent restore | Raise XTRA-02 with owner; assess disposable vs irreplaceable data; do not claim a backup | Real archive hash + verified isolated restore + smoke receipt, or explicit accepted loss |
| P0 confidentiality | Possible hidden/tenant leak, entitlement bypass or exposed secret | Limit further exposure through separately authorized owner; preserve sanitized evidence | Affected scope, remedial fix, independent denial regression, owner/privacy review |
| P1 integrity | Duplicate authoritative command, stale checkpoint, split authority epoch | Freeze affected mutation only under PCV authority; trace sequence/version | Reconciled state/event/checkpoint evidence and separately approved recovery |
| P1 availability | Authenticated authoritative service unavailable | Compare service, provider, authentication, database and network hypotheses | New actual authenticated bounded service proof |
| P2 telemetry | Stale/missing measurements or exceeded owner-approved budget | Report UNKNOWN rather than GREEN and repair monitoring | New current redacted measurements |

No numeric warning thresholds, restore objectives, downtime budget or service-level guarantees are approved by this tranche. Alert intervals and performance budgets require real calibration and owner approval.

## Backup, restore and rollback

The complete authorized-operator command procedure is in `XTRA-02_RENDER_CERTIFICATION_RECOVERY_2026-11-02.md`. Never publish private archives, content, credentials or connection strings. Preservation first requires an owner decision about the actual database contents. An authorized trusted operator may then independently capture a logical archive, verify its integrity and restore into an isolated empty database. Archive presence or an archive listing alone is not restore proof. Record non-sensitive schema checks, app smoke, archive digest, source time, actual restore elapsed time and independent reviewer. Never restore over the source. Do not modify allowlists, incur costs or activate a provider in XTRA-09.

Owner must approve numerical RPO and RTO; both remain `NOT_MEASURED`. A profile transition requires same canonical history, matching checkpoint and strictly newer authority epoch; previous mutator must be fenced. Never use a cached client copy or source-only synthetic fixture as a recovered canonical production database.

## Privacy and retention

Data classifications: (1) synthetic fixtures (only allowed class here), (2) real identities/memberships/payments, (3) private GM/hidden campaign/protected asset content, (4) secrets and privileged tokens, (5) minimized operational telemetry. Classes 2–4 are not authorized as new XTRA test inputs; classes 3–4 must never be included in generic logs, AI context, diagnostics or public exports. User-owned raw material and campaign-granted derivative content require separate rights/taint treatment.

Real-user collection is not approved. Proposed future policy needs a purpose and data inventory, legal/consent assessment where applicable, access-role matrix, retention start and end triggers, delete/backup lifecycle, support request identity verification and scope checks. No retention duration is invented. A real access/export/deletion request requires requester verification, Campaign/GM secret filtering, permitted source-rights review, and owner/privacy approval; it is never automatically satisfied by a chat request.

## Incident response procedure

1. Detect and classify the observed boundary, timestamp, environment and exact failure; distinguish incident from speculation.
2. Identify affected scope and at least two plausible causal classes before retrying changes.
3. Contain only through authorized service/security owners; preserve redacted proof without spreading hidden content.
4. Investigate first failure, compare provider vs product vs identity vs telemetry causes, and test the smallest capable correction.
5. Recover by audited rollback/forward repair, reauthorization and tested checkpoint; protect Session epochs and entitlements.
6. Let owner/privacy reviewer decide actual user notifications, lawful duties and timing from the observed facts.
7. Close only with independent real-boundary outcome, user impact assessment, durable receipt and owner signoff. A green synthetic oracle cannot close a real incident.

A safe incident receipt records incident ID, UTC, build/config revision, redacted data class and affected scope, failure family, competing explanations, remediation reference, artifact digest, measured outcome, independent reviewer and pending owner decisions. Unknown fields explicitly say `NOT_OBSERVED`.

## Evidence grades and handoff

The 51 matrix vectors encode 7 assumption-complete synthetic positives and 44 denial cases. `SYNTHETIC_REFERENCE_ONLY` is **not** authorization, real restore verification or production health. A live gate requires independently verified provider/auth/DB/runtime artifacts, not caller-provided booleans.

**Open decisions:** Render preservation/export before November 8; owner-approved RPO/RTO, data retention, operator alert thresholds and privacy/legal review; any paid hosting; actual PCV security and installed acceptance. XTRA-02 remains **blocked_external**, PCV-03F and MTLC-14 unchanged, and XTRA-09 cannot certify operational readiness beyond these source and synthetic deliverables.
