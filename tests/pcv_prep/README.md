# PCV-PREP fixture runner

`node --test tests/pcv_prep/*.test.mjs` — Node 22 standard-library-only deterministic tests. No service, app build or platform keys.

The source census in `governance/application-planning/product-convergence/prep/APP_SOURCE_CENSUS.json` is a fixed Git-tree snapshot of two directories in Multiversal-app. It is complete for those two directories at the recorded commit but it is not a whole-repository inventory, not a runtime route census, and not a PCV-08 completion certificate.

This testbed provides fail-closed authorization and fictional-resource mock behaviors, scenario fixtures, rough phone/desktop capability parity, and negative installed-package evidence claims. It does **not** import actual Multiversal-app A6/A7/A9, MIB13, GPR, MRCS or platform code. It is intended for consumption by future authorized PCV children, after PCV-03F finishes.
