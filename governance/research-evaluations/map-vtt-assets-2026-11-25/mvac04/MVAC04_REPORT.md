# MVAC-04 — Selection, author history and checkpoints

25 November 2026. Standalone prototype implementation delivered. 33 new focused checks and 48 prior-flow regression checks passed. Real-browser validation remains open. The owner explicitly directed moving to the next implementation step despite the existing MVAC-03 browser-test limitation; that limitation is not a missing application dependency.

## One HTML file remains the deliverable

`Multiversal_MVAC04_Selection_History_Checkpoints.html` includes its scripts, native renderer, illustrated artwork, first-frame image and seven example maps. It needs no companion directory, server, asset download or optional evidence archive. Existing consolidated UHT28 and MVAC-03 artifacts remain unchanged. This deliverable continues the scoped Map & Scene Studio prototype; it does not remove or replace the other tools in the older consolidated tester.

The optional ZIP contains source, test evidence and native render comparisons for inspection/reproduction. A downloaded native draft is user-created map data, not a required runtime dependency. Nothing in this cycle converts embedded artwork into external files.

## Implemented interaction

| Action | Result |
| --- | --- |
| Select / Shift-select | Select one native feature or add/remove objects. Each keeps its original stable ID, source pointer and layer. The overlap chooser can select an exact candidate. |
| Move selection | Enter native-unit offsets and move every selected object in one validated operation. A compound move creates one history command and one new native revision. |
| Lock selection | Protect selected objects from author edits. A mixed locked/unlocked selection rejects the entire move. Locks are per-map, in-memory editor preferences. |
| Isolate selection | Filter object search/list and hit testing to selected objects; dim surrounding artwork. Baked background art can remain within the selected area. Show all restores editing access without changing native geometry. |
| Undo / Redo | Reverse or reapply one author command; a multi-object move reverses in one action. New edits clear the redo branch. Each map has its own history, capped at 50 entries. |
| Rename map | One author command with undo/redo. Cancelling the modal changes no native content. |
| Named checkpoint | Store a named snapshot of the current author draft, up to 12 per map. Restoring it is one new, undoable author command. |
| Save | Download the current author draft in the unchanged `multiversal-cartography-tester-v2` format. |

Single-object fields are disabled for multiple selections so a label or absolute coordinate is not accidentally applied to an ambiguous group. Compound movement validates the whole result before retaining it; a rejection restores the previous draft. No command mutates the original embedded fixture.

## History and scene boundaries

Undo stores before/after native document snapshots for author commands only. Restore applies the snapshot content with a new monotonically increasing native revision and modified timestamp. It does not move the revision counter backwards or accidentally make an old prepared scene appear current again.

Prepared scene snapshots remain separate. Author undo/redo/checkpoint restore neither rewrites that snapshot nor changes a gameplay object. Author history controls are disabled in Prepare and Play. Player preview cannot use them. Requests to undo from the Play canvas leave both author and prepared data unchanged.

This prototype has no connected authoritative gameplay event journal. These checks prove separation of its local author and prepared records; they do not certify a real encounter server, accepted gameplay event, account or network session. Those owners remain under their existing programs and later MVAC integration steps.

Checkpoints, undo history, locks and isolation are in-memory session state. The interface says so. Closing/reloading the page loses that state; Save downloads native map content. Durable checkpoint storage and portable restoration are later recovery work, not a new external runtime requirement.

## Keyboard and cancellation rules

- V selects, H chooses Hand, F fits, and Space-drag pans when the map canvas has focus.
- Ctrl/Cmd+Z undoes an author command from the canvas. Ctrl/Cmd+Shift+Z or Ctrl+Y redoes.
- Text inputs, search fields, selects, content-editable regions and open dialogs do not route keyboard events into author history or tool changes. The browser retains native text undo handling.
- Unapplied inspector fields block tool/context/history changes until Apply or Cancel.
- Escape closes an overlap chooser first; otherwise it clears selection/isolation and returns to Select. Open dialogs retain native browser Escape handling.

Actual browser text undo, modal dismissal/focus restoration, desktop/narrow layout, touch and pointer usability still require browser observations. The single-file artifact can be opened independently; this limitation applies to the agent's test coverage, not its contents.

## Verification

33 MVAC-04 checks passed against the actual delivered HTML scripts in a controlled DOM with the native `@napi-rs/canvas` renderer. They cover compound movement and undo, redo branching, lock enforcement, isolate/view restoration, checkpoint restore/undo, monotonically increasing revisions, per-map history, memory bounds, prepared snapshot protection, Play/player history rejection, focused keyboard guards and self-contained resource packaging.

All 48 MVAC-03 regression checks passed on the new artifact: native rendering of seven fixtures, native save format, original fixture hashes, selection/source identification, single-object edit/cancel, scene revision preparation and invalidation, local player preview, dependency examples, zoom/pan/fit and overlap candidate selection.

`VERIFICATION.json` and `MVAC03_REGRESSION.json` preserve individual results. A list-selection modifier bug was found during integration (a chooser-local variable leaked into the list handler), corrected, and both suites then passed. Earlier syntax/packaging errors were corrected before final validation. No remote CI run or real-browser result is claimed.

The native group-move render pair shows two highlighted Harbor City objects before and after one compound move using the existing renderer. It demonstrates native editability, not an artistic-quality upgrade or browser screenshot. Underlying source fixtures remain unchanged.

## Status and next step

MVAC-04 is `implemented_validation_partial`: its standalone prototype is delivered, while browser/full-workflow acceptance remains open. MVAC-03 retains its recorded browser gap. The owner-approved advance does not silently waive or mark those tests passed. All 40 broader MVAC-01 full workflow/device tasks remain NOT_RUN; J03/J10/J11 have only the local evidence described here.

The next independently ready step is MVAC-05, asset provenance and action-specific rights capabilities. Its dependency is the completed MVAC-02 contract design. Browser validation of MVAC-03/04 can be resumed when a capable authorized browser is available. CURRENT, persistent lane states, native document ownership, installed application and gameplay authorities remain unchanged.
