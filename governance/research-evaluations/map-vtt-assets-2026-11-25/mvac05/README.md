MVAC-05 shared design and synthetic reference evidence, 25 November 2026.

The delivered HTML is self-contained. This archive is optional.

From the extracted root, Node 24 can run `node --disable-warning=ExperimentalWarning work/mvac05/verify.mjs` without external libraries. The controlled review/native editor suites (`check-review.cjs`, `regression04.cjs`, `regression03.cjs`) additionally use @napi-rs/canvas. Tests read the delivered HTML and recreate temporary stripped-TypeScript modules. No browser/network or license clearance is claimed.

Build.mjs requires the preceding MVAC-04 HTML as a build input; that is not a runtime dependency of the delivered MVAC-05 HTML. Pinned source identities are in SOURCE_PINS.json.
