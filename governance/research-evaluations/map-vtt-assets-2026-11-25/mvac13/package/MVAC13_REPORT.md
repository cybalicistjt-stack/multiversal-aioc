# MVAC-13 — Portable saves, recovery and legacy migration

26 November 2026. **implemented_validation_partial**: this standalone cycle is delivered, with browser/device and installed-product acceptance still open.

## Delivered behavior

**Save & restore** adds a linked-save transport and a portable-backup transport around the unchanged `multiversal-cartography-tester-v2` native document. The existing native Save button remains available. All 59 built-in assets stay inside the HTML, and backups reference those stable built-in IDs rather than copying that artwork into every map. No server, source folder, downloaded art pack or other companion is required for the built-in examples.

A save captures visible illustrated dressing into native editable instances so a recovered map's new identity cannot generate different default dressing. The source draft and its history are not changed by saving. Off-map vertices, native feature IDs, placements, transforms and source pins survive. The existing native parser validates loaded documents; the existing native copy constructor creates recovery identities and remaps map-owned/self links according to its established copy behavior. This is a transport/recovery adapter, not a replacement document owner.

**Linked native save** carries the native document and exact optional dependency/version/hash report while omitting external pack bytes. **Portable backup** can carry the exact original bytes for the required optional dependency closure. Optional sources with unresolved rights are omitted by default. Including them requires the user's explicit private-backup selection and at least 12 characters of applicable permission/license evidence. The evidence is labeled **user-supplied, not verified**; resource rights remain unknown. Known prohibited records cannot be included. This is not authenticated ARI permission enforcement or public redistribution clearance. Existing inline legacy PNGs remain part of their native document and retain unresolved-rights notices.

**Review selected file** validates structure, document integrity, source pins, optional pack identities and source hashes before offering Restore. Included pack PNGs and inline legacy PNGs go through the existing quarantine decoder with actual dimensions/pixel budgets. Unsupported external/active media sources are rejected without fetching them. Missing sources are listed explicitly; no thumbnail or placeholder is substituted. Changed native content, malformed UTF-8, duplicate packs, altered version receipts, unsupported formats, unsafe keys and over-budget structures reject before applying.

**Restore as new native copy** retains the current author map. It requires Creator/GM Author, finished edits/drawing, a current review, and unchanged target/storage revisions. Repeating the same file reopens its existing session copy and retains later edits. Recovery is bounded to 16 copies per session/persistent store. Keep a fresh downloaded backup after editing; the stored recovery snapshot is not automatic autosave.

Where optional persistence is available, the restored native document, original pack bytes, representation cache and manifest update commit in the same strict-durability transaction. Needed versions are pinned and persistent recovery-document references are restored into the existing pack reference collector. Failed writes leave the previous complete state; post-commit rendering failure reports a complete stored copy that requires reloading. Stored recovery copies can be reopened from the recovery dialog. Where IndexedDB is unavailable, embedded-only maps can still restore in the current session, explicitly labeled **session-only**. Optional-source restores require the atomic backend; they do not silently claim durable success.

## Existing Map Forge compatibility

The existing `MVForgeImportCore` adapter is reused byte-for-byte. A Map Forge v1 file is reviewed locally, its PNGs decoded through quarantine, and its artwork composed onto a new copy of the current native target. Explicit units-per-cell and origin controls define placement; the selected native floor is retained. Settlement/interior/tactical targets support art placement; regional targets use the adapter's existing assets-only path.

The bounded migration supports PNG-based v1 projects with up to 16 tiles per review (the current shared decoder's per-pack bound), existing adapter geometry/layer limits and at most 350 composed native illustrations. Larger/different legacy projects receive an explicit unsupported/budget result. Tile pixels do not become inferred rooms, walls, doors, vision or gameplay data.

The actual legacy exporter fixture migrates three tiles and six placements, retaining its hidden layer, placement identities and original native geometry. A SHA-256 receipt supplements the legacy accidental-change fingerprint. The source file is unchanged. A portable native backup of this migrated scene restores in a fresh session without the original `.mapforge.json` file.

## Verification

| Suite | Passed |
| --- | ---: |
| Recovery contracts, seven fresh native fixture restores, actual SQLite atomic/quota/process failures | 34 |
| Delivered recovery controls and actual legacy decoding/migration | 20 |
| Prior map-boundary, pointer, undo/save/export and fallback regression | 24 |
| Prior split-store/cache/GC lifecycle and real SQLite failure regression | 18 |
| Embedded manifest resolution and original-image verification | 69 |
| Quarantine/intake regression using actual PNG/SVG workers | 20 |
| **Total** | **185** |

**Zero failures.** Real SQLite tests cover atomic native-document plus source writes, close/reopen, a process exiting inside an uncommitted transaction and after commit, a forced database page-limit failure, stale reviews, capacity refusal, duplicate restores, corrupt stored identities and the 17th-copy limit. Actual native workers validate backup and legacy source bytes. Controlled DOM tests run the delivered HTML controllers and actual native renderer; these do not certify a browser file picker, IndexedDB implementation, touch UI or device.

The native before/after render is pixel-identical with the recovered title normalized solely for comparison; geometry and editable artwork instances also match exactly. The actual copy retains its recovered title suffix. All embedded image data URIs remain byte-identical, and all 48 original manifest image pins/ranges are reverified. Fourteen prior script bodies are unchanged; the native decode/copy seam, author-copy integration, source locator offsets and storage runtime change intentionally, and one recovery script is added. The new HTML is 14,425,345 bytes, growing 36,231 bytes. Original Map Forge adapter SHA-256: `5addef492cebf24399c4b0126375a6a3e973ce35f0e9deb99652f86b0b00d30f`.

## Acceptance still open

Browser IndexedDB v3 upgrade/success/strict durability, origin persistence, eviction, OS power failure, real file picker/download/accessibility and physical devices remain NOT_RUN. SQLite evidence does not substitute for those boundaries. Private-backup evidence is user supplied; authenticated multi-user/tenant rights enforcement remains outside this adapter. Legacy compatibility beyond the stated v1 PNG scope is unverified. Native/GPU lifetime and previous broader workflow/device gates remain open. No installed implementation_complete flag changes.

OPS5 records seven completed bounded scopes, six prototypes with open acceptance and eleven planned steps. **Next: MVAC-14 — editable road joins, rooms, roofs, walls and doors**, including crossing/branching/nonconsecutive roads, bridge preservation and structural attachment behavior. The canvas-edge fix remains intact.
