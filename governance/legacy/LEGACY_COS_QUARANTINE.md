# Legacy COS Quarantine

**Status:** QUARANTINED  
**System:** legacy COS migration-control shell  
**Historical route:** `/v2/`  
**Operational replacement:** `/operational/`  
**Public default:** operational AIOC only

## Decision

The legacy COS interface is retained solely as historical migration tooling. It is not the operational AIOC, is not an approved public default, and must not be included in the GitHub Pages deployment artifact.

## Enforced boundaries

- The repository root must redirect to `./operational/`.
- The Pages artifact must contain the operational command center.
- The Pages artifact must not publish `v2/index.html`.
- Deployment health evidence must report `legacyCos: quarantined`.
- Any change that restores `/v2/` as the root target must fail CI.
- Legacy COS scripts, migration assets, and content builders may not block operational AIOC deployment.

## Legacy content database relationship

The corrupted Phase 1–7 Base64 seed fragments are also quarantined from execution. The active content database pipeline uses the 487 governed canonical objects. The approved 1,347-row 8E-008G foundational inventory may be restored only by importing the intact authoritative audit source and passing a new independent certification.

## Recovery and future use

Historical COS assets may be inspected for migration research, but any feature reused by the operational AIOC must be reimplemented under current governance, testing, evidence, and deployment contracts. The legacy shell itself must not be promoted, relabeled, or silently restored as the product frontend.
