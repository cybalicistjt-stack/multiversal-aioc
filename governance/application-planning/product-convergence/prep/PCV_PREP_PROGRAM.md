# PCV-PREP 01–07: owner-approved nonproduction engineering scaffold

**Authority:** owner approved 2026-11-02. The only authorized mutation is this AIOC source-only/isolated test program. The GPR implementation selector remains PCV-03F and PCV-04..10 retain `blocked_by_predecessor`. No work transfers A3/A5 Session authority to this program.

## Expected deliverables and explicit limitations

| Package | Delivered scaffold | Not proved |
|---|---|---|
| PREP-01 | Evidence-qualified owner/source crosswalk with selected current app blobs, unreconciled risks and gates | Exhaustive source census or live integration |
| PREP-02 | Standalone deterministic action/GM-approved encounter simulator and negative tests | Direct production A6/A7 integration and installed two-human Session |
| PREP-03 | Noncanonical six-stage golden adventure fixture and transition replay | Official SMB-09 canon or real campaign play |
| PREP-04 | Fictional-only game/wager/economy fixture, Free Play isolated wallet, restrictions, idempotency | Canonical MIB13 settlement, legal/commercial gaming |
| PREP-05 | Restricted authoring dependency graph and small sampled feature classification | Full PCV-08 no-stranded-feature audit or real cross-account sharing |
| PREP-06 | UI capability parity and accessibility metadata tests | Rendered Playwright/native phone/desktop visual parity or full Desktop View |
| PREP-07 | Deterministic evidence/sequence checksum and package preflight model | Installed binary, exact Android/Windows package provenance or fresh human-run beta |

## Prior authorized dependencies

- Product roadmap: `governance/application-planning/product-convergence/PCV_PROGRAM_BACKLOG.json` PCV-04..10, strict order. Do not mutate.
- Game/wager program: `PCV_GAMES_WAGERING_INTEGRATION_v1.2.0.md` is owner-approved; intrinsic games and external-event wagers use GPR and canonical MIB13 domain when implemented. **No real-world-value stakes** and MRC overlay off must leave base game working.
- PCV-I05 mobile/product contract: phone capability parity (players, GMs, creators), accessible controls, protected projections and installed evidence later.
- Source crosswalk records app main SHA and selected file SHAs where read; unverified directory entries are tagged separately rather than invented.

## Verification

`node --test tests/pcv_prep/*.test.mjs` from AIOC repository root. The isolated workflow under `.github/workflows/validate-pcv-prep.yml` executes focused Node checks and validates source metadata. Passing models do not elevate to PCV-04..10 implementation acceptance.

## Future integration acceptance handoff

After PCV-03F reaches `completed_verified`, the actual PCV-04 owner must fetch app HEAD afresh and wire canonical A5 session, A6 actions, A7 combat and GPR encounter outputs through existing source owners. PCV-05 takes A9/adventure flows; PCV-06 MIB13 and GPR games; PCV-07 MRCS; PCV-08 full source census; PCV-09 actual UI; PCV-10 installed proof. Each retains its explicit predecessor gate.

**Evidence rule:** No self-reported screenshot, synthetic event log, mocked provider/account, game fixture or source-only test can prove installed Windows/Android two-human behavior.

## Isolated preparation publication status

PR1963 exact HEAD `5ac25d245847d85cc7723fe1ebaa02e00639f473` validated OPS5 run 41528487308 and Node test run 41528487335 (23/23), merged `03edef371050c9c1c1fa99f899f1286230850a92`, queue generation432. The [evidence closeout](PCV_PREP_EVIDENCE_CLOSEOUT.md) makes the unclassified path audit and real integration gates explicit. **This does not complete PCV04–10.**
