# Multiversal Owner–AI Continuity System

**Document ID:** MV-CONT-001  
**Version:** 1.0.0  
**Status:** CANONICAL IMPLEMENTATION CANDIDATE  
**Owner and final authority:** John Brandon Turner

## Purpose

This directory converts conversation continuity into repository-enforced state. It provides the static restart command, active-work pointer, work checkpoints, generated implementation status, roadmap indexing, validation, and acceptance tests required to prevent interrupted or partially completed work from being mistaken for finished work.

## Canonical runtime files

- `../MULTIVERSAL_STATIC_RESTART_PROMPT.txt` — permanent owner-facing restart command.
- `../runtime/CURRENT_WORK_POINTER.json` — small primary/parallel active-attempt index.
- `../runtime/CURRENT_IMPLEMENTATION_STATUS.json` — generated status projection.
- `../runtime/ROADMAP_INDEX.json` — bounded lookup from work items to roadmap or governing records.
- `../work-state/<attempt-id>.json` — exact checkpoint for an active or retained attempt.

## Contracts

- `OWNER_AI_INTERACTION_CONTRACT.md`
- `WORK_CHECKPOINT.schema.json`
- `CURRENT_WORK_POINTER.schema.json`
- `CONTINUITY_ACCEPTANCE_TESTS.md`

## Automation

`tools/continuity_state.py` provides dependency-free commands to:

- validate all continuity records;
- start a new attempt without overwriting an existing active attempt;
- update an attempt using expected-revision protection;
- select a primary attempt;
- regenerate the compact implementation-status projection.

The tool changes local repository files. The active executor must commit and push each bounded atomic batch. A successful local write without a pushed commit is not durable project progress.

## Roadmap performance rule

The full roadmap is not the autosave surface. Routine progress updates touch only the checkpoint, pointer, and generated status. The roadmap changes only at a verified completion boundary, dependency or scope change, owner decision, milestone transition, material risk, or release gate.

## Foundation preservation

The owner-approved v0.1.0 package documentation, manifest, schemas, examples, and checksums are preserved under `foundation/v0.1.0/`. The raw normalized corpus remains only in the owner-held immutable package identified by `FOUNDATION_PACKAGE_REFERENCE.json`.

## Privacy boundary

The raw normalized conversation corpus is retained in the owner-held immutable foundation package and is intentionally not published to this public repository. `FOUNDATION_PACKAGE_REFERENCE.json` preserves its exact hash, byte count, and source counts. Any future training or evaluation publication must be minimized and redacted first.
