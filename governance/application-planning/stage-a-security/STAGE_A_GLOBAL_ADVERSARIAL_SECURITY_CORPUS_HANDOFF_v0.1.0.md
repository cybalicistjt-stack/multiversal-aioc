# STAGE-A Global Adversarial/Security Corpus — Handoff v0.1.0

Status: **DEFENSIVE QA CORPUS COMPLETE — IMPLEMENTATION REGRESSION EXECUTION DEFERRED TO OWNING STAGES/A12**

Owner and final authority: **John Brandon Turner**

Prepared against:
- Multiversal-app main: `dced7f92163050690c807c1fda937146bb8dce85`
- multiversal-aioc main at branch creation: `1397212b85f5b1c7960b20787c88ff52114294e1`

## Completion-integrity recovery

The owner-approved work-ahead sequence placed a global adversarial/security corpus after A5 and before A6. Repository search found no durable corpus file, branch, or commit. This handoff records the recovered missing deliverable rather than silently assuming it was complete.

## Artifact

`STAGE_A_GLOBAL_ADVERSARIAL_SECURITY_CORPUS_v0.1.0.zip`

SHA-256: `9d65ac51f6ffd9f9221b1c05ae52f46edbc31ec521e453e06e1f67f5f4498295`

Validator:

`STAGE-A GLOBAL ADVERSARIAL/SECURITY CORPUS v0.1.0: PASS`

Validated counts:
- threat families: 30
- defensive scenarios: 90
- variants per family: 3
- evidence classes: 15
- P9/Stage coverage rows: 12
- exploit tooling: 0
- real credentials required: 0
- destructive/public testing authorized: 0

## Threat coverage

The corpus covers:
- cross-Campaign isolation;
- horizontal and vertical privilege escalation;
- Owner/Admin versus private Campaign separation;
- Assistant-GM delegation scope/time abuse;
- revocation races;
- entitlement transitions;
- direct hidden-information leakage;
- search/facet/count/topology inference;
- relationship/provenance leakage;
- Picker receipt forgery/replay;
- Character-control hijack;
- Scene placement/source confusion;
- preview-as-role abuse;
- invitation reuse/recipient swap/expiry;
- launch snapshot tamper/staleness;
- duplicate/ambiguous launch;
- command replay/idempotency/revision conflict;
- realtime duplicate/order/gap/cross-session behavior;
- reconnect/checkpoint tamper;
- offline authoritative mutation;
- export/backup/restore leakage;
- audit/telemetry secrets, PII, private prose and raw-payload leakage;
- media enumeration/authorization;
- optional-AI context leakage and prompt-instruction authority escalation;
- accessibility/authority parity;
- bounded DoS/performance behavior;
- migration/history/provider-exit integrity;
- diagnostic/support privilege constraints;
- optional-provider/capability isolation.

Every family is exercised through three defensive variants:
1. direct unauthorized operation/read;
2. stale/replay/race/revocation condition;
3. derivative/secondary surface such as search, counts, preview, export, diagnostics, notification, graph/layout, media, cache, AI context, or accessibility path.

## Required implementation evidence

The corpus defines blocking evidence classes for authorization decisions, role-safe projection diffs, idempotency/status recovery, expected-version conflicts, revocation convergence, ordered Event recovery, cross-Campaign negatives, derivative inference negatives, audit safety, backup/export/restore, offline nonauthority, accessibility parity, bounded work, optional-provider isolation, and migration integrity.

## Defensive-only boundary

This package is a defensive QA corpus only.

It contains no exploit scripts, credential attacks, persistence mechanisms, malware, destructive automation, network flooding, public-target testing, credential guessing, or bypass recipes. It does not authorize production testing, real-user testing, paid-provider testing, or use of real credentials.

## Authority and sequence

This recovery does not:
- alter Multiversal-app code;
- activate A6 through A12;
- change the current application work pointer;
- authorize destructive testing, real credentials, release, deployment, public testing, provider spend, or production exposure.

A2 remains the authorized current Stage A implementation work item. A3 through A11 remain preparation-only.

## A12 consumption rule

Stage A12 hardening must consume this corpus as a cross-stage blocking regression source. Every threat family must map to executable regression lanes or explicit nonapplicability evidence before an internal-alpha release claim. Critical/high unresolved blocking findings must remain zero for such a claim.

## Exact next preparation step

Prepare **Stage A12 — Internal-alpha Hardening**, consolidating completed release-design, security/privacy, accessibility, performance, offline/reconnect, recovery, onboarding/help, telemetry/error-reporting, optional-isolation, interface-consistency, and this recovered global adversarial/security corpus into the A12 preimplementation package while leaving A12 unactivated and A2 current.
