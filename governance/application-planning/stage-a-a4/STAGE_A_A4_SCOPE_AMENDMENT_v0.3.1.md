# STAGE-A-A4 Scope Amendment v0.3.1

**Status:** PASS — BOUNDED TEST-MAINTENANCE AMENDMENT AUTHORIZED  
**Parent authority:** AIOC PR #312 / merge `442677a504be4463c47d02810d332cc10cf1de6c`  
**Prior scope:** `A4_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv`, 52 rows, SHA-256 `489b38e60ec3401a81dc9702a14a48dab692f9aca67022ba01e72aaa2c80da79`  
**Current scope:** `A4_CURRENT_CHANGED_PATH_SCOPE_v0.3.1.csv`, 53 rows, SHA-256 `9145d0dea1f312174e6e23958d08e03433d0bfc0337068c0680d555c05498072`

## Reason

At the first meaningful A4 package validation boundary, focused A4, A3 and DT-008 passed. A1 and A2 each failed the same legacy shell regression because `apps/client-ui/src/App.test.tsx` used an unscoped `getByRole("button", { name: "Open" })` assertion written when the deterministic dashboard contained exactly one Campaign card. A4 correctly adds a separately authorized Character card through the existing A3 dashboard/fresh-entry contract, so two legitimate `Open` controls now exist.

This is a predecessor-test expectation mismatch, not an A4 product or A3 authorization defect. The product behavior is frozen. The amendment authorizes only `apps/client-ui/src/App.test.tsx` as `MODIFY_BOUNDED` so the predecessor shell regression can target the intended Campaign card explicitly and add explicit Character-entry coverage.

## Boundary

- no production/runtime behavior change is authorized by this amendment;
- A3 dashboard/entry semantics remain unchanged;
- Campaign and Character entry remain separate fresh authorization decisions;
- the updated test must preserve the existing Campaign assertion and add the A4 Character path rather than weaken either one;
- no new dependency, provider, vendor, paid service, release or deployment authority is added.

**Verdict:** `PASS — BOUNDED TEST-MAINTENANCE AMENDMENT AUTHORIZED`.
