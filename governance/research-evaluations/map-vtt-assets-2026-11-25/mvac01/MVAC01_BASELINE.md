# MVAC-01 — Representative fixture and measurable gap baseline

25 November 2026. Bounded result: seven existing illustrative UHT28 maps frozen as native editable files, with native renderer and static export expectations. This is an acceptance fixture package and review HTML, not a new UHT product build or installed-game release.

## Completed in this cycle

- Seven source-identified native fixtures: regional, settlement, interior, tactical, cave, ship and non-Euclidean topology.
- Native document validation and save/load round trips preserving draft, identity and revision.
- Four artwork zoom snapshots per scene (800×520, DPR1); per-scene static player export and one repeated-render check: 36 PNG snapshots in total.
- GM and player static projection snapshots on every one of 14 levels: 28 JSON records. Player variants omit unreviewed decorative dressing. This test acknowledgement is not a claim of owner artwork approval.
- Existing GM-only feature expectations plus a same-floor synthetic canary retained in GM and omitted from local player export.
- Six dependency-failure inputs with expected statuses: missing pack, wrong version, corrupt bytes, unknown rights, unsupported format and interrupted install. These are NOT_RUN acceptance fixtures, not an implemented resolver.
- Forty linked acceptance tasks: retained T01–T12, J01–J16 and asset A-T01–A-T12; explicit target-device matrix and blank observation records.

102 focused component checks passed. No original source image or UHT28 application was changed. The source hash is ab66ac31aeacec06b3a78db9e4689532774c0a7d21b6ecd957f1367ce43eb9d2. Renderer, source, catalog, native-file and pixel hashes are recorded in MANIFEST.json.

## Frozen scenes

| ID | Scene | Type | Levels | Feature records | GM-only features |
| --- | --- | --- | --- | --- | --- |
| F01 | Stormfold Frontier | Regional geography | 1 | 25 | 0 |
| F02 | Harbor City | Settlement / districts | 1 | 59 | 0 |
| F03 | Tidewatch Archive | Multi-floor architecture | 3 | 117 | 2 |
| F04 | The Ruined Keep | Tactical encounter | 1 | 0 | 0 |
| F05 | Brinegate · Split Caverns | Cave / tunnel | 3 | 12 | 2 |
| F06 | Kestrel · Courier docking layout | Ship / docking decks | 2 | 19 | 0 |
| F07 | Carnival · Impossible Arcade (illustrative topology) | Non-Euclidean topology | 3 | 5 | 1 |

The tactical map stores its tactical layout outside draft.features; a feature count of zero is not an empty map. All source IDs, revisions and specialty records are retained. This freezes test content without promoting it to world canon.

## How to use the package

Open the companion review HTML to inspect the native artwork and download a native fixture. Import native/*.native-map.json through the current Map Maker file importer. These files use the existing multiversal-cartography-tester-v2 envelope. The header's historical sourceCommit is preserved from the existing exporter and is not a new app publication claim.

Run the same fixture/settings against a future candidate and compare source diffs, render pixels and workflow observations. A pixel difference identifies a changed result; it does not by itself say whether the change is desirable. Deliberate art improvements need an explicit reviewed baseline update. Byte-level PNG hashes are tied to this exact environment; use pixels/settings plus visual review across different platforms.

The review's GM artwork is a native component render with fog off and gameplay/specialty overlays omitted. The player image uses the existing static export projection, with unreviewed decorative dressing excluded. These are different views of an unchanged baseline, not a before/after improvement comparison. Deck/topology drawings do not prove travel, live sight or portal reachability.

This package includes synthetic GM test information and is a private acceptance reference, not a safe player distribution bundle. Expected secrets are intentionally listed so future privacy tests can detect disclosure. Production network privacy requires actual authenticated-client payload inspection; local export filtering cannot close J04 or A-T08.

## Measurable acceptance and open gates

ACCEPTANCE_MATRIX.csv maps every task to concrete fixture IDs, an oracle and the boundary that must be exercised. DEVICE_MATRIX.csv distinguishes the one controlled component run from desktop browser, Android, owner MacBook Air and receiving-VTT tests. OBSERVATIONS_TEMPLATE.json keeps outcomes NOT_RUN until actual evidence is recorded.

Record exact build/fixture hashes, browser/client version, CPU/GPU/RAM, viewport/DPR, cold/warm load, first useful artwork, task completion, wrong actions, help/recovery effort, visible latency distributions and retained resources where measurable. Do not replace these with the one draw-duration sample in each PNG receipt. No actual device budget or competitor-derived performance promise is adopted here.

Known open gaps: browser first-view/focus/selection; general road-network joins; production pack resolution and atomic install; full specialty overlays; native-to-live owner operations; real auth/privacy/reconnect; clean-device backup/restore; actual receiving imports; creator/user visual acceptance. These gaps have frozen inputs now; they are not counted as implementation failures from an unexecuted test.

## Verification and incident classification

The first local fixture-builder attempt compared an artwork benchmark with a static export by using the wrong repeat-render branch. That was a fixture-harness defect, not an app regression. The branch was corrected; the changed builder then completed all 102 checks, including identical repeated artwork pixels. The original failure and repair are recorded in the cycle receipt rather than erased or attributed to the product.

The fixture verifier checks every referenced byte hash, PNG dimensions, decoded pixel hash, normalized projection identity, private-feature exclusions, task coverage, case statuses and baseline identity. It supports package integrity; it is not installed-device, browser, network or security acceptance.

## Scope and next step

MVAC-01 is complete for its stated fixture/planning scope. Product implementation_complete remains false. MVAC-02 is the next recommendation: define shared spatial/media integration contracts using these fixtures. No product lane or CURRENT selection changes automatically.
