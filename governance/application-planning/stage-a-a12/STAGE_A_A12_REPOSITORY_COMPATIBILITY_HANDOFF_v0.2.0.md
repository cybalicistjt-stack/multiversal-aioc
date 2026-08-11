# STAGE-A-A12 Repository Compatibility + Implementation Contracts Handoff v0.2.0

**Status:** PREIMPLEMENTATION DESIGN — NOT ACTIVATED  
**Application baseline:** `dced7f92163050690c807c1fda937146bb8dce85`  
**Current Stage A implementation pointer:** A2 remains current  

## Artifact

`STAGE_A_A12_REPOSITORY_COMPATIBILITY_AND_IMPLEMENTATION_CONTRACTS_v0.2.0.zip`

SHA-256:

`f7e80038c26b94b5641ae9afc222c3f987776313fc636d45e94442f4cf149859`

Validator:

`STAGE-A-A12 REPOSITORY COMPATIBILITY + CONTRACTS v0.2.0: PASS`

Validated counts:

- repository/predecessor anchors: 30;
- blocking gaps/risks: 26;
- ownership/evidence decisions: 12;
- planned acceptance contracts: 26;
- exact future path actions: 66 across all 12 A12 slices;
- reuse/composition decisions: 20;
- validation/CI lanes: 37;
- implementation invariants: 40;
- repository-compatibility blocking gates: 15.

## Compatibility verdict

`COMPATIBLE_WITH_CROSS_STAGE_EVIDENCE_AGGREGATION_OVER_EXISTING_P9_A1_FOUNDATIONS`

A12 does not need a new gameplay/content domain or production service. It is a candidate validation/evidence layer over existing P9/A1 foundations and future A2-A11 implementation validators.

## Repository-specific findings

1. A1 already provides the React/Vite/TypeScript client, Vitest/Testing Library interaction tests, an axe accessibility baseline, responsive contract tests, and focused typecheck/test/build CI.
2. The current A1 axe test explicitly disables `color-contrast`; therefore it cannot by itself satisfy IA-D09 high-contrast/non-color candidate evidence.
3. The current responsive contract tests prove CSS structure, not supported-device/browser behavior. A12 requires measured/physical device evidence for selected supported profiles.
4. P9-06-011 supplies deterministic backup/restore/export integrity, corruption rejection, no-partial-restore, zero-residue reset, and reproducible reseed evidence.
5. P9-06-019 supplies checksum-bound reconnect/restoration, cross-session rejection, sequence-gap and revision-discontinuity protection.
6. P9-06-020 supplies provider-neutral bounded audit/telemetry, but A12 candidate diagnostics require an even stricter positive safe-field allowlist so domain-private prose, hidden content, raw payloads and AI prompt/response text cannot become diagnostics metadata.
7. P9-06-022 supplies checksum-complete provider-exit export/import and corruption/missing-category rejection.
8. P9-06-023 supplies a reusable local physical-device operator/evidence pattern that A12 can adapt for bounded browser/device evidence without introducing a production service.
9. No candidate-wide A12 hardening runner, performance measurement harness, large-corpus hardening harness, tester-entry package, candidate evidence manifest, or cross-stage security execution layer exists yet.

## Planned repository root

Cross-stage candidate evidence contracts are placed under:

`packages/contracts/src/acceptance/`

This layer owns only validation/evidence records. It does not own Character, Campaign, Session, Action, combat, Asset, social, investigation, World, Adventure, content, AI, or other domain truth.

The planned contracts cover exact build identity, validation-lane status, reverse traceability, candidate state, stop conditions, known limitations, owner-decision evidence, performance, large-corpus workload evidence, accessibility, responsive/device evidence, permission/security results, destructive confirmation, draft recovery, reconnect journeys, history reconstruction, optional isolation, diagnostics, tester entry, onboarding, interface consistency, candidate package checksums, manual evidence, and A12 hardening scope.

## Global security requirement

The restored `STAGE_A_GLOBAL_ADVERSARIAL_SECURITY_CORPUS_v0.1.0` is a mandatory A12 input.

All 30 threat families must map to executable candidate regression evidence for applicable implemented surfaces or explicit justified nonapplicability. Zero unresolved applicable CRITICAL/HIGH findings are permitted before a `candidate_validated` claim.

## Candidate state boundary

A12 automation may produce evidence supporting only:

- `candidate_built`;
- `candidate_validated`.

It must never set or infer:

- `release_approved`.

Tester access, real-user data collection, production credentials, paid-provider commitments, Internal Alpha release, public deployment, and canonical promotion remain separate owner-only decisions.

## Current nonauthorization

This handoff does **not** authorize or claim:

- an A12 application implementation branch;
- implementation completion of A2-A11;
- a built or validated candidate;
- Internal Alpha tester access;
- real-user data collection;
- production credentials;
- paid-provider commitments;
- release or deployment;
- canonical promotion.

A2 remains the current authorized Stage A implementation. `.ai/task-queue.md` is not changed.

## Exact next work

The Stage A3-A12 work-ahead preparation series is now complete through repository-compatibility planning. The next work must follow the current canonical implementation pointer rather than starting A12: resume/activate the governed Stage A A2 implementation from its existing ready work order and frozen A2 master execution package, unless newer repository evidence or an explicit owner decision supersedes that pointer.
