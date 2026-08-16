# IA-D09 Candidate Data / Privacy Boundary

**Candidate:** `56b127f1fc01eebe5c73ba0472a5b6496fe92b5e`  
**Build ID:** `5033f55d3344209c1719d6003d1369b4bc201c74ba9d64f046767263daee5a45`  
**State:** evidence prepared; no owner decision made

## Allowed Internal Alpha data boundary

For the currently validated candidate, tester activity is restricted to **synthetic/test-only** data. This packet does not authorize collection of real-user data, production credentials, paid-provider credentials, release tokens, private production payloads, or any other production secret.

Candidate diagnostics must remain build/correlation/failure bounded and must exclude credentials, secrets, hidden/private prose, raw provider payloads, and real-user content. The A12 diagnostics lane passed on the exact candidate and reused the P9 structured-audit/privacy controls plus the A11 privacy boundary.

## Retention / reporting boundary

Evidence, screenshots, reproduction steps, tutorial receipts, and diagnostic bundles may be retained as governed test evidence only when they remain candidate-bound and synthetic/test-only. This packet does not define or authorize a retention policy for real-user data because real-user data collection is not authorized.

## Owner-gate consequence

- `authorize Internal Alpha tester access`: may be considered only under this synthetic/test-only boundary.
- `authorize real-user data collection`: **not decision-ready** from this packet. A separate data inventory, purpose, retention schedule, and privacy/security control package is still required.
- production credentials and paid-provider commitments remain closed.

## Evidence

- `Multiversal-app/fixtures/stage-a-a12/onboarding/a12-onboarding-source.json` — `data_classification: synthetic-test-only`.
- `Multiversal-app/docs/acceptance/STAGE_A_A12_TESTER_ENTRY.md` — prohibits credentials, secrets, hidden/private prose, raw provider payloads, and real-user content in tester evidence.
- A12 final artifact `9261392785`, `a12-evidence-preserved/diagnostics.json` — PASS.
- `Multiversal-app/receipts/STAGE-A-A12-CLOSURE.json` — real-user data / credentials / paid-provider / release / deployment authority remain false.
