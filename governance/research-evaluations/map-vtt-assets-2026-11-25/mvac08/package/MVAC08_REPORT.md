# MVAC-08 — Harbor illustrated family

26 November 2026. Bounded standalone artwork preparation and native rendering adapter complete; creator acceptance, browser/device acceptance and installed integration are not certified.

Open **Multiversal_MVAC08_Harbor_Illustrated_Family.html → Harbor family**. Compare the current urban/interior draft at 50%, 100% or 200%, then apply the family or restore its original appearance. Applying is one undoable native draft edit. Download the native author draft to retain that choice. Closing/reloading the HTML otherwise resets the edited drafts, as before.

## Delivered artwork and integration

Eleven coordinated, generated objects: slate cottage roof, cedar warehouse roof, striped market canopy, stone well, loaded handcart, crate/barrel cluster, broadleaf oak, coastal pine, flowering shrub, teal bed and provisioned oak table. The palette combines slate, weathered cedar, sea green, muted ochre and warm stone. This is a small review family, not a claim that the entire previous library has been artistically unified.

The source atlas and generation prompts are preserved. The first atlas's doorway was rejected for elevation/perspective; its 11 other cells were extracted. A requested correction repaired the doorway but introduced a nontransparent background, so that entire corrected sheet was rejected. No rejected doorway/correction bytes are in the HTML. Native structural doors and openings remain in use.

Each selected source rectangle is cropped and scaled into a transparent, padded PNG no larger than 320 pixels per axis. No painted background replacement or RGB/alpha color editing is performed. The original atlas bytes remain unchanged. An actual source decode required the available Pillow decoder before raw RGBA transfer to the native canvas exporter; the exported sprite PNGs themselves pass actual native decoding. Runtime needs only those checked PNG representations, not the source atlas or Pillow.

Metadata records exact source crop, representation hash, dimensions, content rectangle, center anchor/pivot, category, suggested scale, view/orientation, version and source lineage. Generated-for-review provenance is explicit; no third-party clearance, raw redistribution approval or legal copyright certification is inferred. Existing unknown sheet licenses remain unchanged.

The existing sprite registry now contains the original 48 entries plus 11 family entries. The adapter uses the existing native rendering stage and document system. `draft.illustratedFamily` stores family/version bindings to existing source feature/showcase IDs; it contains no image copies or new gameplay records. Source geometry, labels, anchors, counts, seeds, floor IDs and object IDs remain unchanged. Moving a mapped native object through the existing inspector moves its illustration. Undo/redo, checkpoints and preparation use the existing author history and revision model.

Urban rectangular footprints receive fitted roof artwork, with orientation derived from their edges. Nonrectangular or skewed candidates do not receive a fabricated fit. Existing supported showcase props receive corresponding sprites at their source anchors; group counts use a deterministic decorative spread. Roof fitting can stretch artwork to an authored rectangle. The study does not claim a modular architectural construction system or new collision geometry.

Painted contact shadows are retained; the family renderer adds no additional cast shadow. Sprite rotation also rotates painted highlights, so arbitrary-rotation lighting consistency is not certified. This limitation is explicit in the manifest. These are individual object sprites, not seamless tiles; there are no tile-edge/seam claims. Environmental lighting and broader material/style work remain in their later steps.

## Size and self-containment

| Measure | Result |
| --- | --- |
| New sprite PNG bytes | 1,490,044 |
| Total new sprite decoded pixels | 892,803 |
| Approximate RGBA surface payload | 3.4 MiB, excluding codec/browser overhead |
| Delivered HTML | 13,605,936 bytes |
| Growth from MVAC-07 | 2,011,748 bytes |
| Runtime fetches / required companion files | None added |

Only the 11 bounded sprite renditions enter the HTML, once each. The larger source atlas, rejection evidence and render archive are optional development evidence. Existing images are retained in the original renderer. Nine of the ten inherited script bodies are byte-identical; the author shell is extended only with the tested family apply/current hook. Its surrounding source is unchanged.

This cycle keeps a deliberately small embedded family. Optional packs, cache eviction and durable asset activation remain MVAC-11/12 work; it does not externalize any existing required content. MVAC-09 will measure PNG/WebP rendition tradeoffs rather than embedding multiple full-resolution alternatives by default.

## Same-geometry visual review

Twelve actual native renderer outputs cover Harbor City and Tidewatch Interior, each before/after at 0.5×, 1× and 2×. Every pair uses the same source geometry, object IDs, anchors, floor and camera. No alternate scene is substituted for the after image. Source and render snapshots remain unchanged.

A separate black/white contact sheet exposes each sprite's edges. Automated checks verify transparent outside padding on all four edges; the model also visually inspected the contact sheet and city/interior renders separately from those checks. This inspection prompted rejection of the doorway/corrected sheet and reduction of prop sizing to avoid crowding source anchors. It is implementer review, not independent human creator approval. The owner receives the comparisons for review; no final artistic acceptance is assumed.

## Verification

266 fresh checks passed, zero failed:

| Suite | Checks | Boundary |
| --- | --- | --- |
| Family verification | 28 | Real PNG decode, hashes, dimensions/alpha padding, binding rejection, actual native before/after renders at fixed zoom, deterministic output, source preservation and delivered apply/undo/preparation behavior |
| MVAC-03 regressions | 48 | Controlled DOM and real native canvas/editor |
| MVAC-04 regressions | 33 | Selection, history and checkpoints |
| Rights review | 66 | Existing delivered review logic |
| Manifest review | 71 | Existing embedded-asset review logic |
| Intake review | 20 | Delivered intake controls and real Node worker decoders through a Worker shim |

Two old immutability assertions initially failed because they expected the entire author shell hash to remain unchanged. The deliberate new hook is now covered by behavior tests; the regression checks still require byte-identical original renderer/review/intake scripts and exact preservation of the shell before and after that hook. Baselines were not silently rewritten. No application failure was hidden by that test adjustment.

The MVAC-07 core is unchanged; its earlier 78-check report remains historical evidence and is not added to this cycle's fresh count. Browser layout, file-picker/drop behavior, browser worker APIs, physical devices, high-resolution print quality, receiving VTTs and installed builds remain NOT_RUN. MVAC-03 remains blocked_external; MVAC-04 remains implemented_validation_partial. The 40 broader full workflow/device tasks remain NOT_RUN.

## Next

MVAC-09 — measured renditions and color/alpha pipeline: preserve exact source, compare practical PNG/WebP variants, measure bytes and decode on named targets, test opaque/translucent edges and color/orientation handling, and retain a source fallback. This family's preparation does not close those future measurements or require accepting the current artwork as final.
