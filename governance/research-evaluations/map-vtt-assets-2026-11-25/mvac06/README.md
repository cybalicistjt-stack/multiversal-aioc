MVAC-06 standalone manifest adapter evidence. The HTML is self-contained; this archive is optional.

From the extracted root, run Node 24 `node work/mvac06/verify.mjs` for actual byte/manifest checks. Controlled UI/editor tests require @napi-rs/canvas and run via check-manifest-review.cjs, check-review.cjs, regression04.cjs and regression03.cjs. No network/browser is required for those local tests.

The optional build scripts require the preceding MVAC-05 HTML as a build input. That is not a runtime dependency of the delivered MVAC-06 artifact. All test inputs and the current self-contained HTML are in this archive.
