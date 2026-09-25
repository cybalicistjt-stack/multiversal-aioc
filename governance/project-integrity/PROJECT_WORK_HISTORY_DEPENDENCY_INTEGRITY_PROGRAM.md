# Project Work-History & Dependency Integrity Mapping

**Status:** in progress — PIM-03 validation  
**Lane:** gpr  
**Product runtime authority:** none

Owner direction on 2026-09-25 requires the project to stop before PCV implementation and durably preserve every group of work, every known gap, and the dependencies between features, families, and the wider app.

This program does not reopen completed feature families and does not make historical records live. It creates a preservation/index layer over existing sources.

## PIM-01 — Immutable Work-Group Registry

Candidate artifacts:
- `PROJECT_WORK_HISTORY_REGISTRY.json`
- `PROJECT_WORK_IDENTITY_IMMUTABILITY_POLICY.md`

Coverage: all archaeology chronology nodes, 83 planning groups, 73 work-state families, 662 unique work items across 667 attempt files, 10 PDCP reductions, explicit non-work-state families, external lineages, and the retained Project Source surface.

## PIM-02 — Feature / Family / Wider-App Dependency Map

Candidate artifacts:
- `PROJECT_FEATURE_FAMILY_APP_DEPENDENCY_MAP.json`
- `PROJECT_DEPENDENCY_MAP_GUIDE.md`
- `PROJECT_INTEGRITY_GAP_REGISTER.json`

The map separates structural lineage from actual dependency/consumer evidence. It includes PCV-01 capability convergence assignments and current-canon downstream consumers without inventing unsupported edges.

## PIM-03 — Integrity Validation & Mutation Guard

Candidate validator:
- `scripts/validate_project_integrity_map.py`

It enforces exact inventory coverage, identity uniqueness, parent lineage, graph reachability, child gap ownership, Project Source integrity anchors, and the no-silent-mutation policy. The archaeology validator is updated so canon reconstruction can stay verified while candidate-specific wiring is reopened by later evidence.

PCV-PRE remains blocked until PIM-03 is completed_verified.
