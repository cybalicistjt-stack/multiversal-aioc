# IA-D09 Tester Recovery / Support Procedure

**Candidate:** `56b127f1fc01eebe5c73ba0472a5b6496fe92b5e`  
**State:** prepared for owner decision; does not authorize tester access

## Entry and recovery rules

1. Confirm the exact candidate SHA/build ID before beginning a tester session.
2. Use only the owner-authorized account/Campaign role and synthetic/reference data assigned to that tester.
3. If authentication, authorization, connectivity, or current-authority context is lost, stop the governed mutation and re-establish current online authority rather than attempting an offline canonical write.
4. Reconnect/retry must use the existing idempotent recovery path; do not manually duplicate Actions, decisions, transfers, charges, Effects, or Events.
5. If a draft/autosave conflict is shown, preserve the tester input and current authoritative version separately; never resolve it with silent last-write-wins.
6. For a destructive action, require the current version/authority confirmation and preserve the attributable receipt.
7. For a defect, record candidate SHA/build ID, bounded reproduction steps, device/browser profile, relevant safe correlation/build identifiers, expected/observed behavior, and permitted screenshots. Do not include credentials, secrets, hidden/private prose, raw provider payloads, or real-user content.
8. If the defect implicates permission leakage, duplicate canonical mutation, history reconstruction, destructive integrity, or another blocking A12 gate, stop using that candidate for the affected journey and return it to engineering review. Owner approval never converts a blocking defect into a known limitation.

## Reference evidence

- A12 final artifact `9261392785`: recovery, destructive/draft, diagnostics, security, onboarding, and exact-head clean-checkout lanes PASS.
- `Multiversal-app/docs/acceptance/STAGE_A_A12_PHYSICAL_DEVICE_QUICKSTART.md`.
- `Multiversal-app/docs/acceptance/STAGE_A_A12_TESTER_ENTRY.md`.
- P9-06-023 home physical-test / runner procedures retained in `Multiversal-app/docs/acceptance/`.

## Support boundary

This is an Internal Alpha engineering/test support procedure, not a public support commitment. It authorizes no public enrollment, public deployment, production credential use, paid provider, or real-user data collection.
