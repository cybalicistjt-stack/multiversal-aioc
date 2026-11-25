# MVAC-03 — Author / Prepare / Play prototype

25 November 2026. Prototype built; real-browser acceptance blocked in this executor. MVAC-03 remains open pending browser validation. MVAC-01 and MVAC-02 remain complete within their fixture/planning and shared-design scopes. No installed app, CURRENT selector or persistent lane changed.

Open `Multiversal_MVAC03_Author_Prepare_Play.html` directly to review the standalone prototype. It starts with Harbor City artwork already present, without a setup dialog. Seven existing native fixtures remain available. The source fixtures and UHT28 are unchanged; edits affect in-memory copies until the user downloads a native draft.

## Implemented behavior

- One canvas-first workspace with explicit Author, Prepare and Play controls. Tools stay above the canvas; object search and inspector sit beside it. The canvas toolbar and inspector positions remain stable across contexts.
- Native map renderer and native document serialization reused from UHT28. Rendering functions and map geometries were not replaced. A renderer-only DOM facade suppresses legacy panel installers so the new shell owns its UI.
- Native features and showcase elements are selectable by stable ID. Pointer hits on overlapping art produce a chooser. Search can find the exact archive door; the inspector shows its kind, stable identity, layer and native source path. Door actions are visibly disconnected and cannot mutate gameplay.
- Author can apply or cancel label/position edits. A tree's cluster count, seed and other instances survive its edit. Native validation must accept edits. Unapplied changes block context/tool switches. Map rename uses a modal and only commits on Apply.
- Prepare reviews the selected floor and dependency state and pins a separate scene revision. Missing-pack and incompatible-version examples block preparation. Preparing stays in Prepare; entering Play is explicit. Later author edits or a floor change invalidate readiness while retaining the previous prepared snapshot.
- Play is read-only. Map/floor switching and author actions are disabled there. Player preview uses the existing static-export audience filter and reduces the visible controls to navigation/help and audience return. All role labels explicitly say preview; no connection or authentication is claimed.
- Zoom is anchored at the pointer, Hand/Space-drag pans, and Fit resets the view. Navigation does not modify native geometry. V/H/F shortcuts are scoped away from text fields and dialogs. The shell leaves text undo and native dialog Escape handling to the browser; actual browser behavior remains unverified.
- Save downloads the native `multiversal-cartography-tester-v2` author draft. The browser does not persist edits automatically. No second native document or gameplay system is introduced.

The responsive layout defines side drawers below 780 CSS pixels; this CSS is implemented but its actual browser layout/touch/accessibility behavior has not been observed here. No full undo/checkpoint system is claimed; that remains MVAC-04.

## Evidence and acceptance boundary

48 focused checks passed: actual delivered HTML script handlers and the existing native renderer were executed together in a controlled DOM with `@napi-rs/canvas`. The seven map types rendered without runtime errors. Exact native serialization, original-byte hashes, object identity, edits/cancel, revision invalidation, read-only Play, dependency failures, overlap selection and focus guards were exercised. `VERIFICATION.json` contains each result. These are development/integration checks; they do not certify a browser, physical device, account, network or installed app.

| Acceptance task | Local evidence | Remaining real-boundary work |
| --- | --- | --- |
| J01: open settlement as author, GM and player | Harbor City opens in Author; explicit Prepare/Play; player local view has reduced controls; map art renders. | Actual browser artwork-first observation and authenticated clients remain unverified. |
| J03: select overlapping door and find its action | Exact door selected by search/pointer chooser; inspector identifies source/layer; disconnected open/close action explained. | Actual browser pointer/keyboard usability and connected owner action remain unverified. |
| J10: dialog typing, text undo, Escape and tools | Delivered key handlers ignore modal/text input; no underlying draft/tool change; dirty tool/context guard tested. | Native text undo, focus restoration and Escape dismissal must be observed in a real browser. |

All 40 broader MVAC-01 full workflow/device tasks remain NOT_RUN. The three tasks above have partial local evidence, not full acceptance.

Browser testing was attempted through the available routes. The local Chromium launcher points to a missing executable (`/usr/lib/chromium/chromium`). The connected-browser tool reported that the originating browser context was unavailable. The cloud browser rejected local `file:` navigation under its URL policy. No workaround to that denial was attempted. These are executor/tool access limitations, not evidence that the prototype fails in a user's browser.

During local testing, a prototype defect was found and fixed: scene switching selected the first listed floor rather than the native document's saved floor. The shell now prefers a valid saved floor. Two test-harness defects (heading-tag parsing and initial animation-frame ordering) and a slow contextified VM setup were also corrected; those were test infrastructure issues, not product defects. The final run uses the delivered HTML's scripts and a non-contextified VM for native raster work.

## Before and after render

`Multiversal_MVAC03_Native_Edit_Before_After.png` shows the archive entrance before and after applying a native point/label edit in the shell handlers. Both use the same existing renderer at 800×520, the same floor and the same surrounding map. The door retains its stable ID and moves from native X=6 to X=6.8; this is an editability demonstration, not an architecture/material quality upgrade or browser screenshot. Linking a moved door to a wall opening remains MVAC-14.

## Size and source preservation

The standalone HTML is approximately 11.4 MB, including reused illustrated assets and a first-frame poster. This cycle adds no external art family or remote download. It is a portable prototype, not the final optional-pack storage design; pack manifests, measured renditions and optional activation remain MVAC-06/09/11. The current 58.7 MB consolidated UHT28 tester is not modified or replaced by this scoped deliverable.

`RENDERER_PROVENANCE.json` records the pinned core hash and reused rendering modules. `FIXTURE_PINS.json` records the seven immutable native source hashes. The evidence archive includes the HTML, shell source, native fixture copies, tests and render pair. To reproduce controlled checks with Node 24 and `@napi-rs/canvas`, extract the archive and run `node work/mvac03/verify.cjs` from its root. The tests require no browser or network.

## Next step

Finish MVAC-03 in a capable browser: open the delivered HTML at desktop and narrow widths; observe J01/J03/J10, including actual typing/undo/Escape, overlap selection, zoom/pan and read-only player controls. Record console and visual results, fix any browser-specific defects, and then close the standalone prototype step. MVAC-04 follows: unified selection/tools/shortcuts, compound undo and named checkpoints. No automatic product integration is selected.
