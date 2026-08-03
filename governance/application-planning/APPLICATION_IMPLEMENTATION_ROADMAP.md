# Multiversal Application Implementation Roadmap

**Document ID:** MV-APP-ROADMAP-001  
**Version:** 1.0.0  
**Status:** OWNER APPROVED — PLANNED  
**Owner and final authority:** John Brandon Turner  
**Approved:** 2026-08-03

## Purpose

This roadmap governs the work after the repository, content, and application foundations are sufficiently verified. It expands the former single “Phase 10 — Begin application development” milestone into four major implementation phases.

Nothing in this roadmap is considered complete merely because it was described in conversation. Completion requires repository evidence, tests, previews, and owner approval.

## Phase 10 — Core Application Implementation

Connect verified engines, registries, services, and permissions to production user interfaces.

Primary programs:

1. application shell and design system;
2. universal object browser, inspector, picker, relationships, variants, and provenance;
3. identity, dashboards, workspaces, and permissions;
4. character workspace and character creation;
5. campaign and scene builder;
6. live session and action-proposal/GM-approval loop;
7. combat interface;
8. inventory, equipment, crafting, and vehicles;
9. investigation and social workspaces;
10. world builder and content creation tools;
11. contextual AI interfaces;
12. internal-alpha hardening.

Implementation method:

- build vertical slices, not disconnected mock screens;
- each slice includes navigation, real data, actions, permissions, save/load, loading/error states, desktop/mobile behavior, tests, and owner review;
- reuse universal object and relationship components rather than creating domain-specific duplicates;
- significant UI changes require deployed interaction verification.

## Phase 11 — GM and Player Experience

Complete the day-to-day product experience.

GM workspace:

- campaign, session, timeline, and participant management;
- scene, encounter, investigation, relationship, social, and world-building tools;
- maps, environments, creatures, NPCs, hazards, clues, objectives, triggers, rewards, hidden information, and notes;
- approvals, modifications, permissions, and live-session control.

Player workspace:

- character progression;
- abilities and resources;
- inventory, equipment, crafting, vehicles, companions, journals, quests, relationships, party assets, and customization;
- clear live-session views with secondary access to logs and proposals.

Exit condition:

A GM and players can create a campaign, create characters, build scenes, run combat and non-combat sessions, persist state, and resume safely.

## Phase 12 — AI Team and Automation

Integrate specialized AI assistants into real workflows instead of a single generic chat box.

Planned assistants:

- GM Assistant;
- Rules Assistant;
- Narrative Assistant;
- World Assistant;
- Character Assistant;
- Encounter Assistant;
- Developer and Content Assistant.

Requirements:

- contextual canonical-object retrieval;
- provenance-aware answers;
- permission awareness;
- visible proposals;
- reversible actions;
- owner/GM approval gates;
- no silent canonical publication;
- regression tests for context, tool use, and approval behavior.

## Phase 13 — Internal Alpha Completion

Bring the product to feature-complete internal use.

Work includes:

- complete planned workflows;
- connect every major screen to real services;
- populate the application with approved recovered content;
- test combat, social, investigation, exploration, crafting, vehicles, campaigns, and world building;
- multiplayer, reconnect, offline recovery, conflict resolution, and permissions testing;
- accessibility, responsive layout, touch targets, performance, autosave, rollback, onboarding, help, telemetry, and error reporting;
- stable pack creation, validation, installation, upgrade, rollback, and removal workflows;
- internal tester and contributor documentation.

## Parallel Apple track

`WP-011 — Tauri iOS/iPadOS Spike` remains a bounded Mac-dependent track.

Mac-only work should be limited to:

- Xcode and Apple tooling setup;
- iOS/iPadOS build generation;
- signing and provisioning;
- simulator/device validation;
- App Store-compatible packaging and Apple-specific checks.

Most application implementation proceeds safely on web/Windows/Linux while waiting. The Mac should function primarily as an Apple build and certification environment rather than the main development machine.

Estimated focused Mac requirement after repository preparation: approximately one working day in the uncomplicated case, with a two-to-three-day contingency for account, certificate, provisioning, or Apple tooling problems.

## Governance and delivery

Every batch must be bounded and include:

- exact scope and acceptance criteria;
- real application data;
- permissions and authority behavior;
- save/load and recovery behavior where relevant;
- desktop and mobile interaction;
- automated tests;
- deployable preview or reproducible local demonstration;
- owner review before merge or production promotion.

The active workstream remains Content Recovery and Ingestion until its governed handoff authorizes implementation work. This roadmap defines the approved destination and sequencing; it does not falsely mark unverified application work complete.
