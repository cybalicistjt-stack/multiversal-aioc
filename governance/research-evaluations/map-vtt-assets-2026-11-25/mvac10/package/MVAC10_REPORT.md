# MVAC-10 — Asset discovery and editable placement prototype

26 November 2026. Standalone implementation delivered with local validation; real-browser, layout/accessibility, lower-powered-device and installed-product acceptance remain open. MVAC-10 is implemented_validation_partial, not full UX acceptance.

Open **Multiversal_MVAC10_Asset_Library_and_Placement.html → Asset library**. Search 59 embedded objects; filter category, style, suggested scale, favorites or recently placed. Choose an asset, width/rotation and 1–12 objects per click, then **Place decoration on canvas**. Click inside the map. Repeat placement can stay active until Escape. Context/floor/map changes cancel the armed tool.

New native artwork appears in the existing Objects list. Select one to change its label, position, width and rotation, or delete it. Batch placement is one undo operation; individual instances remain independently editable. Existing selection/lock/isolate, compound movement, undo/redo, checkpoints and native Save apply. A saved draft contains references and per-instance properties, not another copy of every image. Draft persistence still requires downloading the native JSON; no new durable project store is claimed.

## Discovery, previews and provenance

The catalog contains the 48 prior embedded assets plus the 11 harbor-family assets. Their image bytes and source renderers remain embedded. Each catalog record has source hash/version, category/style/tags, suggested size, provenance and rights state. Unknown licenses remain unknown; generated study assets are identified separately without inferring copyright or redistribution approval.

A scroll window creates at most 18 asset cards at once. The pane uses 64-pixel-or-smaller PNG thumbnails and does not request full originals for browsing. There are 490,782 thumbnail bytes in the file; total HTML growth is 704,348 bytes, to 14,323,263 bytes. No network fetch or required companion is added. Existing renderers may already cache images needed by the visible scene; this is not a claim about whole-browser memory or all earlier hidden panels.

Search/filter functions are exercised against the real 59-row catalog and a clearly synthetic 10,000-row dense metadata fixture. The dense fixture proves bounded window logic locally; it is not a fabricated product library, browser timing or target-device benchmark. Favorites and 12 recent placements use local browser storage when available, with an in-memory fallback. Browser file-origin/storage persistence is not certified.

The selected asset panel displays exact source identity, provenance and availability. A simulated unavailable registry entry disables placement and reports the missing requirement while leaving the draft unchanged. Existing placed references remain in the document, and their inspector reports missing assets instead of deleting them. Actual downloadable/optional pack lifecycle is later MVAC-11 work, not claimed from this simulation.

## Native placement and editing

The existing `multiversal:art-dressing:v1` layer is reused with map ID, revision and separate item IDs. New items record logical asset ID, source SHA-256/version, rights reference and per-instance position/width/rotation. A multi-placement batch also records a lightweight assembly ID; it is not a linked prefab, gameplay entity or procedural construction system.

On the first placement, any existing visible illustrated suggestions are retained in the native layer. Existing authored features, showcase objects and source fixtures are unchanged. Appending preserves prior records and unknown layer extension metadata. The native 350-item limit, invalid inputs, unavailable asset, ID collision or mismatched layer reject without a partial commit. New groups must fit inside the map, including their rotated extent. Existing general author editing remains flexible and may move an item outside the view.

Placement converts the canvas pointer through the existing zoom/pan transform to native map coordinates. It commits once after validation and then selects the new native items. Width/rotation changes affect only the selected item; compound movement still operates on the selected set. Deletion and restoration use the same author history. Prepared scenes keep their prior copies; later author edits mark them stale rather than modifying an accepted preview.

Decoration does not create walls, blockers, loot, inventory, combat records or gameplay authority. Role controls remain local preview, not authentication. Native item hashes are retained as references; this cycle does not certify a future pack-upgrade resolver or license delivery policy.

## Verification and rendered evidence

345 local checks pass, zero fail:

| Suite | Checks |
| --- | ---: |
| Catalog, thumbnails, search/window, native placement and delivered UI | 79 |
| Native editor / selection-history | 48 / 33 |
| Rights / manifest review | 66 / 71 |
| Intake controls with actual isolated Node decoder workers | 20 |
| Harbor family regression | 28 |

Evidence includes actual decoding of all 59 small previews, pointer placement after zoom, favorite/recent behavior, source/geometry preservation, atomic four-object placement, independent movement/size/rotation, native serialization, deletion/undo, repeat cancellation, context changes, preparation pinning and boundary rejection. The before/after native render uses matching camera and geometry, adding four shrubs and one cart as editable items; all prior dressing is retained.

Only the author shell changes among the fourteen MVAC-09 script bodies. Thirteen inherited bodies remain byte-identical, including the original renderer, rights, manifests, intake, family data/rendering and rendition code. Older shell-wide immutability assertions are scoped to the intentional new native author integration; functional editor/history regressions still exercise the modified shell.

This is a controlled DOM/native canvas test environment, not real-browser or physical-device acceptance. MVAC-03 remains blocked_external; MVAC-04 and MVAC-10 are implemented_validation_partial. All 40 broader workflow/device tasks remain NOT_RUN. No independent creator approval or installed-product completion is inferred.

This execution resumed after a session/environment interruption. Two owner execution commands belong to this one cycle; it is not recorded as single-Continue execution. The final bounded delivery and durable OPS5 log do not erase that re-entry.

## Next independently ready step

MVAC-11 — optional packs and crash-safe activation. Keep all current built-in artwork embedded and the HTML usable by itself; optional user-selected packs must never become an unstated runtime dependency. Preserve the existing native document and ARI ownership, then test stage/verify/activate/rollback and last-good recovery at the actual available storage boundary. MVAC-10 browser acceptance remains open independently.
