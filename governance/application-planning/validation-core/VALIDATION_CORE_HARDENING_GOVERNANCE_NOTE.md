# Validation Core Hardening Governance Note

**Program:** VCH — Multiversal Validation Core Hardening  
**Status:** OWNER APPROVED — activation after CCTI-12-T04 exact-evidence closure  
**Owner and final authority:** John Brandon Turner

The application repository now contains the owner-approved VCH program/backlog. This governance note records the decision in AIOC without changing the current work pointer prematurely.

VCH exists to eliminate recurring tranche-specific validation drift by establishing a shared cross-platform validation core, explicit persistent-runner contracts, deterministic evidence, a governed failure taxonomy, and harness self-tests/fault injection.

The approved failure taxonomy is:

`RUNNER_ENV`, `GIT_STATE`, `TOOLCHAIN`, `SRC_GOV`, `BUILD`, `TEST_UNIT`, `TEST_UI`, `RECEIPT_GEN`, `XP_COMPARE`, `ARTIFACT`, `HARNESS_INT`.

Each classification preserves raw evidence and declares cause, feature blame yes/no/undetermined, and remediation. Persistent-runner state is verified rather than assumed clean. Host-level state is not silently reconfigured during application gates. Product/UI failures cannot be automatically retried into an ordinary clean pass. The existing owner-approved self-hosted Windows/Linux final-validation policy remains authoritative.

Sequence:

1. VCH-01 Failure Taxonomy and Diagnostic Contract
2. VCH-02 Runner Contract and Preflight
3. VCH-03 Shared Execution Core and Thin Profiles
4. VCH-04 Deterministic Evidence and Cross-Platform Comparator
5. VCH-05 Harness Self-Tests and Fault Injection
6. VCH-06 Migration and Adoption Gate

Activation order remains: close CCTI-12-T04 on exact evidence first, then activate VCH-01 before broader roadmap reconciliation.
