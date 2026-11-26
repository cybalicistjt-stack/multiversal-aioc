# MVAC-12 — Storage separation and map continuity

26 November 2026. Status: **implemented_validation_partial**. Standalone HTML delivery complete; browser persistent-storage, physical-device and installed-app acceptance remain open. This cycle does not certify the full application.

## Map continuity

The user identified roads stopping short and landscapes constrained to the canvas. Two separate causes were confirmed: presentation padding, and source endpoints/placement constraints. The regional/settlement Author preview now follows each map's aspect ratio without its former inset. Shared native rendering and player export crop artwork to the map rectangle, retaining all model-space geometry.

**Draw road** and **Draw landscape** accept vertices in the surrounding workspace, including negative coordinates. Zoom out to expose that workspace. Click vertices, then Finish drawing or Enter; Escape cancels. Paths are ordinary native features, validated and saved through the existing multiversal-cartography-tester-v2 document and undo/redo system. Regional landscapes use native land polygons; settlement landscapes use native district polygons. The tool is bounded to 128 vertices and finite coordinates within ±100000. The inspector and selection handles retain off-map geometry. The canvas boundary is a presentation crop, not a clipping edit to source data.

**Extend selected road** adds outward endpoints beyond the native rectangle along the first/last segment directions; it is one reversible author command. It does not extend every cul-de-sac automatically. Decorative asset groups may also straddle the map boundary. Harbor City's six example streets have nine outward-facing endpoints deliberately extended; their internal waterfront ends remain intentional. Its built-in example revision advances from 1 to 2. Regional source geometry is unchanged.

The before/after PNG uses the actual native canvas renderer with matching output sizes; it is not generated artwork or a browser screenshot. The regional comparison shows the removal of presentation padding, with the same underlying geography. Author preview uses map-shaped dimensions so complete geography is retained.

## Durable originals and disposable caches

Optional-pack persistence now separates manifest/index records, exact original pack bytes addressed by hash, disposable validated PNG representations, staging, and garbage-collection tombstones. The current and previous rollback manifests protect their installed original records; the pack manager already preserves native draft/history/checkpoint/prepared references, offline pins and dependencies when allowing uninstall/rollback. Collection conservatively retains every installed record in either manifest, including inactive versions. Originals are never automatically evicted for space.

**Storage & caches** shows encoded source/cache byte counts and the browser's origin quota estimate when available. SQLite evidence reports allocated database pages separately. These values do not claim physical disk, embedded HTML, decoded native renderer or GPU memory measurements.

**Clear disposable previews** clears the optional representation store and releases this prototype's rendition canvases, cancelling stale asynchronous source loads. It does not uninstall packs, delete maps, erase originals, remove pins or change rollback records. Native renderer image caches and GPU allocations remain outside this prototype's release/measurement scope. Optional previews regenerate through the existing quarantine validator/decoder from the preserved original. Corrupt cached representations fail verification; clearing them permits source-based repair. A missing/corrupt original fails closed, rather than substituting a thumbnail.

**Verify originals & rebuild previews** validates current and previous states and atomically repopulates disposable representations, without incrementing the logical revision or replacing the previous rollback root. Disk representation retention is bounded to 8 MiB per commit; omitted entries can regenerate. The older v1 inline-root layout remains readable; its first normal write migrates through an atomic split-store commit. Browser database upgrade adds the v2 stores without deleting the old root.

**Clean unreferenced originals** first marks retired source hashes. Only a later collection at least 60 seconds after marking may remove them. Every write transaction rereads the current/rollback roots. Re-referenced sources are rescued. Missing or malformed manifests stop collection. Staging has its own explicit discard and is not confused with installed originals. Browser write transactions require confirmed strict durability; unsupported/denied storage leaves built-ins usable. Browser clearing/eviction can still remove optional local storage; keep original pack files and native document backups.

Deduplication is physical only: immutable source/representation pins and unresolved rights stay on their existing logical records. This is local-origin storage, not a multi-user authenticated service; cross-tenant authorization/isolation remains unverified and is not claimed from hash equality. No new canonical media/document/ARI owner is introduced.

## Verification

| Local suite | Passed | Evidence |
| --- | ---: | --- |
| Map boundary, pointer projection, save, undo, export and storage fallback | 24 | EDGE_VERIFICATION.json |
| Actual SQLite lifecycle, worker regeneration, quota and process interruption | 18 | STORAGE_VERIFICATION.json |
| Quarantine/intake regression with real native workers | 20 | UI_VERIFICATION.json |
| Illustrated family regression and native rendering | 28 | FAMILY_REGRESSION.json |
| Rights-review regression | 64 | MVAC05_REVIEW_REGRESSION.json |
| Embedded manifest resolution/verification regression | 69 | MVAC06_REVIEW_REGRESSION.json |
| **Total** | **223** | **0 failures** |

Real SQLite WAL/FULL transactions cover restart/process exits before write, inside an uncommitted split-store transaction, and after commit; a real database page limit forces a failed multi-store write and proves that the last manifest, originals and cache remain intact. These are actual local adapter boundaries, not proof of browser IndexedDB or OS power-loss behavior. Controlled DOM tests execute the delivered scripts with the actual native canvas renderer and workers; they do not certify a browser layout, accessibility tree, touch device or file-origin behavior.

The artifact audit verifies all embedded image data URIs remain identical; 48 source manifest byte ranges were relocated after the renderer changed and their original SHA-256/length pins rechecked. All 59 original assets remain inside the HTML. Twelve of eighteen inline script bodies remain exact. Six intentionally change: the settlement example data, renderer crop, author tools/projection, image locator offsets, rendition lifetime handling, and optional storage runtime. The HTML grows by 15,124 bytes to 14,389,114 bytes. No external script, stylesheet, artwork download, server or required companion is added.

## Open acceptance and next step

Browser IndexedDB success/migration/strict-durability/quota/eviction, OS crash/power behavior, target-device layout/pointer capture/accessibility, native renderer/GPU cache disposal and authenticated cross-tenant isolation remain NOT_RUN. MVAC-03/04/10/11 gaps and all 40 broader workflow/device checks remain open. No installed implementation_complete flags change.

OPS5 scope is the owner-authorized standalone research/adapter prototype. Seven bounded scopes remain completed, five prototypes now have open acceptance, and twelve steps remain planned. **Next: MVAC-13 — portable save, backup/restore and legacy migration**, preserving the current native document and embedded built-ins. The legacy .mapforge.json adapter remains a compatibility path, not a replacement document system.
