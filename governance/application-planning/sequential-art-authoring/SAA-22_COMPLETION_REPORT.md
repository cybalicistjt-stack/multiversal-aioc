# SAA-22 Completion Report

**Status:** `completed_verified`  
**Schema:** `SAA-22.1`  
**Application PR:** #740  
**Causal RED:** run `35731095592`, head `432859ebf3be0a1dc64a4fba5593d35739947220`  
**Validated GREEN:** run `35731842827`, head `854067e2f529f5c3924ccd115e5ed5a876f34b8f`  
**Application merge:** `c32e877e22daffca2ef2a6baa23e416b4810b31e`

SAA-22 extends the sealed SAA-09/10 text and balloon presentation contracts while preserving editable semantic text as canonical authoring state.

The delivered contract adds speech/thought/shout/whisper/custom presentation, explicit balloon shape/border/fill/tail styling, deterministic font fallback plus kerning/spacing/alignment, authorized batch story-text editing and deterministic search/replace. All mutation targets are checked against the sealed SAA-21 authorization boundary before application.

Speech-to-text remains optional authoring input. Provider-off local input is valid; external speech input requires explicit provider provenance. Accepted transcripts populate editable authoring text only and do not silently mutate Dialogue or narrative owner truth.

Three bounded repair heads followed causal RED: readonly working-state typing, the remaining Map inference boundary, and one mechanical newline serialization typo. Every retry changed causal evidence and remained inside SAA-22. The final exact head passed repository health, Linux, hosted Windows and deterministic cross-platform comparison.

SAA-23 — Pro Raster/Vector Drawing, Masks & Layer Interop — is selected next but not started.
