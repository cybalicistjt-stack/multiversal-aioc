# MVAC-11 — Optional pack activation and recovery prototype

26 November 2026. Standalone adapter/prototype delivered with actual local storage failure tests. Browser IndexedDB durability, eviction/origin behavior and target-device acceptance remain open; MVAC-11 is implemented_validation_partial.

Open **Multiversal_MVAC11_Optional_Pack_Activation.html → Optional packs**. Try Stage test pack v1 or v2, inspect the staged result, then Activate. The test packs contain explicitly synthetic colored markers. User-selected pack JSON is also accepted. Rollback, offline pin, staging cleanup and uninstall act through the same manifest adapter.

All 59 current built-in assets, original maps, renderers and prior controls remain embedded. They need no pack, database, server, companion file or network. Optional imports are user data, not an externalization of existing artwork. The new HTML is 14,373,990 bytes, growing by 50,727 bytes. Browser storage being unavailable leaves the built-in editor usable.

## Manifest, validation and version policy

The deliberately narrow `multiversal:optional-art-pack:v1` JSON format contains packId, exact version, exact dependency pins and 1–16 PNG asset records. Names are bounded ASCII identifiers, not extraction paths. No remote URLs, arbitrary scripts, active SVG, installer code or filesystem extraction is admitted. The original JSON bytes and asset hashes are retained unchanged.

The existing MVAC-07/ARI-10 validator checks actual signatures/chunks/CRC, byte/dimension/pixel/frame budgets and real isolated image decoding. Source asset SHA-256 must match the manifest. Registration receives a worker-produced PNG representation after metadata stripping, rather than displaying raw user source bytes. Sources and representations have separate hashes; rights remain unknown. This is native art registration, not canonical rights/entitlement approval.

Asset IDs include pack and exact version, so v2 cannot replace v1's placed instance silently. A pack/version hash receipt survives logical uninstall and prevents altered reinstallation under that identity. Dependency resolution uses exact installed versions and rejects missing/cyclic requirements. Older versions referenced by current drafts, undo/redo history, checkpoints or prepared scenes remain available. Manual offline pins also protect versions. New active versions are browsable through Asset library's optional category; referenced older versions can still render.

Bounds: 8 MiB per selected pack, 16 assets per pack, 320 pixels per axis per admitted PNG, 1,638,400 decoded pixels per candidate pack, at most 8 installed versions, 64 optional asset records and 16 MiB of installed original pack bytes. The immutable hash-receipt ledger holds at most 256 entries. Previous-state and temporary staging data add storage overhead. The existing native palette also has its own 130-entry session cap; preflight failure leaves storage unchanged. This prototype does not grow an unlimited asset store.

## Transaction and recovery behavior

Staging/verification remain private. Activation performs a revision compare-and-swap, stores the complete current manifest plus its previous complete state and clears staging in one transaction. Native catalog publication follows commit. A runtime hydration failure reports **saved-complete-reload-required** instead of falsely claiming rollback or showing a half-ready pack.

The browser adapter uses IndexedDB and requests strict durability. It also checks the transaction's reported durability; a missing/different result aborts activation rather than silently downgrading. That request is an implementation policy, not proof of a specific browser's power-loss behavior. Transaction/durability semantics were checked against the [W3C Indexed Database API 3.0 draft, 30 October 2026](https://www.w3.org/TR/2026/WD-IndexedDB-3-20261030/). A durability hint and real-device durability certification remain separate.

Local executable validation uses a separate real SQLite adapter with WAL and synchronous FULL. That adapter tests the same pack-manager policy through actual database writes and process exits; it does not stand in for browser IndexedDB certification. In each interruption test, reopening and validating gives the old or new complete pack.

| Failure point / operation | Observed local result |
| --- | --- |
| Before database write | Prior complete version |
| After private staging write | Prior complete version; staging not active |
| During manifest transaction, before commit | Prior complete version |
| After committed manifest | New complete version |
| Actual SQLite page-limit write failure | Prior committed state unchanged |
| Cancel during real media-worker decoding | No activation |
| Stale second writer | Rejected; earlier activation retained |
| Corrupted saved original | No optional rows exposed |
| Missing dependency or native palette budget failure | No activation |
| Runtime catalog hydration failure after commit | Complete state retained, reload explicitly required |

Rollback restores the previous complete manifest while retaining versions needed by live references/pins and their dependencies. Uninstall blocks referenced, pinned or required dependency content. Logical uninstall may leave prior-state bytes for rollback and already decoded images until reload; it is not a secure-erasure claim. Staging cleanup never deletes installed originals or pins. Actual browser eviction, user clearing site data, changing file origin or external storage damage can still remove optional data; keep original pack files and native draft backups. Native save continues to store references, not a portable copy of optional pack bytes. Full storage lifecycle/garbage collection and portable bundles are later MVAC-12/13 work.

## Native integration and evidence

The existing library receives active optional records and cheap previews after verification/commit. Original native document, renderer, history and placement owners are retained. A small author-shell hook collects asset references from all in-memory native drafts, prepared scenes, history and checkpoints. Fourteen of the sixteen MVAC-10 script bodies are byte-identical; only that reference hook and the library's optional-catalog synchronization seam are added.

The matched before/after native render adds synthetic v1/v2 markers through the real SQLite-backed adapter and existing native placement commands. The older placed v1 remains distinct after v2 activation; original source geometry/showcase records remain unchanged. This is a storage/version demonstration, not new finished illustrated artwork or a browser screenshot.

374 local checks pass, zero fail:

| Suite | Checks |
| --- | ---: |
| Pack validation, actual SQLite failure/restart policy and fallback | 29 |
| Discovery/placement regression | 79 |
| Native editor / selection-history | 48 / 33 |
| Rights / manifest review | 66 / 71 |
| Intake controls / harbor family | 20 / 28 |

Actual native worker decoding, actual SQLite process termination/full-page failures and actual native author history are exercised. The browser adapter's storage-success path, file-origin persistence, IndexedDB crash/OS-power behavior, layout/accessibility and physical devices are NOT_RUN. Remote download interruption is not claimed; this prototype accepts bounded local files. All 40 broader workflow/device tasks remain NOT_RUN. MVAC-03/04/10 acceptance gaps remain open. No installed-product or independent creator approval is inferred.

An initial test rerun reused its prior SQLite file and therefore failed assumptions about a fresh revision zero. The test now uses a distinct database directory per execution; no product behavior was weakened to make that fixture pass.

## Next

MVAC-12 — separate durable originals, disposable renditions/caches and safe garbage collection. Preserve references, checkpoints, offline pins and last-good recovery; distinguish clearing caches from deleting projects/packs. Retain all current built-ins inside the HTML, and keep actual browser/device acceptance explicit.
