# DWC Speech Synthesis Project — Stable Recovery Entry Point

**Project:** DWC language-to-speech / native speech synthesis  
**Owner and final authority:** John Brandon Turner  
**Repository role:** durable DWC project continuity and planning reference  
**Status:** ACTIVE RESEARCH / IMPLEMENTATION

## Purpose

This directory is the stable external recovery point for the DWC speech-synthesis project. It exists so a future conversation does not have to reconstruct the project from chat history, temporary sandboxes, or narrative summaries.

This directory governs DWC project continuity only. It does **not** replace or override the Multiversal software-roadmap runtime authority in `governance/ai/runtime/CURRENT_WORK_POINTER.json`, and it must not be used to select unrelated application work.

## Recovery order

When resuming DWC work, read:

1. `DWC_PROJECT_ANCHOR.md` — durable goals, architecture, established achievements, constraints, operating rules, and non-regression boundaries.
2. `DWC_CURRENT_STATE.json` — latest mutable execution frontier and exact next operation.
3. Any evidence file named by the current state, including training-evidence records, acceptance gates, external Drive artifacts, and live execution-surface evidence.
4. Only then use historical conversation exports/recovery notes when detailed provenance is actually needed.

## Authority rule

Latest verified DWC evidence wins.

- Current durable state and exact artifacts outrank older conversation summaries.
- A newer external recovery artifact may advance the frontier beyond an older GitHub state; when discovered and verified, update GitHub immediately rather than continuing from the stale pointer.
- Missing files in a new sandbox are a runtime rehydration problem, not evidence that completed DWC work has been undone.
- Repeating a settled proof for reproducibility does not reopen it or move the logical frontier backward unless contradictory evidence is produced.

## Update discipline

- Keep this `README.md` stable. **Do not encode the current training stage, checkpoint, or next mutable operation here.**
- Update `DWC_PROJECT_ANCHOR.md` only when a material project goal, settled architecture, verified milestone, or recovery invariant changes.
- Update `DWC_CURRENT_STATE.json` whenever the verified execution frontier materially advances, a blocker changes, or a mutable fact becomes stale.
- Add bounded evidence records for major training/acceptance milestones when exact metrics, hashes, or configurations need durable preservation.
- Never mark work complete because a conversation ended, an artifact was generated, or an operation was merely started.

## Core non-regression rule

> Project state is determined by verified artifacts, files, code, tool results, and explicit owner corrections. Narrative prose is commentary about that state, not the state itself.

Always read `DWC_CURRENT_STATE.json` for the current frontier.
