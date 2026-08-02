# AIOC UI/UX Consultancy and Game-Development Workflow Refinement Phase

Status: Planned and approved
Placement: After semantic recovery quality stabilizes; before final AIOC hardening, release validation, and long-term production use
Owner and final authority: John Brandon Turner

## Purpose

Treat the AIOC as professional specialist software for one primary owner who is managing a large tabletop-RPG canon, AI development team, forensic recovery process, and future application production without relying on professional programming expertise.

This phase is not cosmetic. It will refine information architecture, task flow, review speed, error prevention, recovery, accessibility, and the relationship between AI assistance and owner authority.

## Owner-centered constraints

The design must:

- minimize repeated prompts, manual file handling, and context transfer;
- support long-running work completed across many sessions;
- clearly separate machine completion, human review, owner approval, and canonical completion;
- never make a successful workflow run look like completed content work;
- preserve provenance and show why a recommendation exists;
- favor large, coherent work tranches over many tiny interruptions;
- make the next useful action obvious without hiding advanced controls;
- reduce memory burden by preserving decisions, progress, filters, and work position;
- prevent destructive or canonical actions from being triggered accidentally;
- work well for a non-programmer while retaining expert-level depth when needed.

## Timeline placement

1. Complete the current semantic-cleaning cycle and establish a trustworthy candidate-quality baseline.
2. Freeze major AIOC navigation and workflow additions.
3. Run this UI/UX Consultancy Phase.
4. Implement and validate the approved redesign.
5. Resume large-scale semantic review and canonical recovery through the refined interface.
6. Perform final AIOC hardening, accessibility validation, release validation, and operational handoff.

The consultancy phase belongs before large-scale human review because reviewing thousands of candidates through a weak interface would create avoidable rework, inconsistent decisions, and owner fatigue.

## Consultant process

### UXC-001 — Discovery and workflow inventory

- Inventory every AIOC module, button, dashboard, queue, and status.
- Identify actual owner jobs rather than organizing around internal implementation systems.
- Map frequent, expensive, risky, and confusing workflows.
- Record current pain points, repeated actions, dead ends, ambiguous states, and duplicated modules.
- Produce an authoritative workflow map and module disposition list: keep, merge, relocate, redesign, or remove.

Deliverables:

- owner workflow inventory;
- module audit;
- task-frequency and risk matrix;
- terminology glossary;
- current-state journey maps.

### UXC-002 — Information architecture redesign

Organize the AIOC around owner goals:

- Understand project status
- Continue current work
- Review recovered content
- Resolve blockers and relationships
- Approve or reject candidates
- Inspect canon and provenance
- Manage releases and development
- Diagnose system problems

Replace the growing collection of equally weighted right-side buttons with a small number of stable workspaces and contextual secondary navigation.

Deliverables:

- proposed navigation tree;
- workspace model;
- module consolidation map;
- naming and status-language standard;
- breadcrumb and backtracking rules.

### UXC-003 — Interaction and state model

Define consistent behavior for:

- task statuses;
- progress states;
- filters and saved views;
- bulk actions;
- undo and rollback;
- draft versus approved decisions;
- machine suggestions versus owner decisions;
- loading, empty, error, stale-data, and partially complete states;
- return-to-work and resume behavior.

Every long process must distinguish at least:

- Not started
- Running
- Machine complete
- Needs review
- In review
- Blocked
- Owner approved
- Canonically complete

### UXC-004 — AI-assisted work design

AI must function as an expert assistant, not an invisible authority.

Each AI recommendation should show:

- recommendation;
- confidence;
- evidence and provenance;
- affected objects and relationships;
- likely consequences;
- unresolved uncertainty;
- reversible action options.

AI should help with batching, summarization, comparison, duplicate detection, field completion, relationship suggestions, and quality checks. It must not silently approve, merge, or rewrite canon.

### UXC-005 — Game-development specialist review

Evaluate the AIOC as a tabletop-RPG production environment, including:

- rules and exception management;
- object families and nested mechanics;
- ability trees and prerequisites;
- species, creatures, items, vehicles, worlds, factions, environments, and adventures;
- cross-pack dependencies;
- provenance and source comparison;
- balance and validation information;
- incomplete-object workflows;
- release and pack readiness.

The interface should support both object-centered and source-centered review, plus graph-centered relationship work.

### UXC-006 — Low-fidelity prototypes

Produce at least three competing structures for:

- home / return-to-work dashboard;
- content recovery workspace;
- candidate review screen;
- canonical object inspector;
- project control and release readiness;
- diagnostics and failed-workflow recovery.

Compare prototypes using realistic Multiversal tasks rather than generic placeholder data.

### UXC-007 — Owner-guided usability testing

Run task-based walkthroughs built around the owner's real habits:

- return after several days and find the correct next task;
- determine whether a workflow, review batch, or canonical phase is actually complete;
- review and disposition a candidate without losing source context;
- recover from an error without opening GitHub unless necessary;
- process a large batch while preserving position and decisions;
- understand what remains and why.

Capture time, confusion, wrong turns, unnecessary clicks, unresolved questions, and confidence after each task.

### UXC-008 — Visual system and accessibility

Refine the existing Multiversal visual identity without sacrificing readability.

Requirements:

- accessible contrast and focus indicators;
- keyboard-operable core workflows;
- readable type hierarchy;
- color never used as the only status signal;
- reduced-motion support;
- scalable text and responsive layouts;
- dense-data modes that remain scannable;
- consistent table, card, badge, panel, modal, and notification behavior.

### UXC-009 — High-fidelity implementation

Implement the approved workspace model and shared components. Migrate modules in controlled groups, preserving existing functions and data.

Required shared components include:

- return-to-work panel;
- task and batch list;
- source-evidence viewer;
- candidate comparison panel;
- relationship resolver;
- status timeline;
- persistent filter bar;
- bulk-action review tray;
- decision ledger;
- diagnostics and recovery panel.

### UXC-010 — Validation and acceptance

Acceptance requires:

- no orphaned legacy module;
- no ambiguous completion state;
- all core workflows recoverable after refresh or return;
- owner can identify the next useful action from the home workspace;
- destructive actions have confirmation and rollback paths;
- accessibility checks pass;
- representative large datasets remain usable;
- owner approves the final workflow and visual system.

## Design principles adopted for AIOC

1. Organize around user tasks, not implementation phases.
2. Use progressive disclosure: show the next decision first, details and expert controls on demand.
3. Preserve place and progress across sessions.
4. Prefer clear status language over decorative dashboards.
5. Put provenance beside decisions, not on a distant page.
6. Use bulk review carefully, with preview, exceptions, and undo.
7. Treat empty, loading, stale, failed, and complete as different states.
8. Keep navigation stable; context changes inside workspaces.
9. Make the safest likely action easiest, while keeping owner authority explicit.
10. Measure success by completed owner tasks and reduced confusion, not number of features or panels.

## Success measures

- Time required to resume work after returning to the AIOC
- Time required to determine true project status
- Number of clicks and context switches per candidate decision
- Percentage of decisions made with visible provenance
- Number of accidental or reversed decisions
- Batch completion rate and abandonment rate
- Frequency of opening GitHub to diagnose ordinary problems
- Owner confidence after completing representative tasks

## Immediate next action

Finish the current semantic-cleaning run and capture its quality metrics. Then begin UXC-001 before the next major human-review tranche. Semantic-engine fixes may continue when necessary, but major AIOC interface expansion should pause until the consultancy information architecture is approved.
