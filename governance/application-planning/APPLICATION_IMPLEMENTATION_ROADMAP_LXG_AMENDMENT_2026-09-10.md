# Application Implementation Roadmap — LXG Parallel Infrastructure Amendment — 2026-09-10

**Status:** OWNER-APPROVED PLANNING/EXECUTION AMENDMENT  
**Work order:** LXG-01 — Local Execution Gateway for ChatGPT and Local Agents

## Decision

Add **LXG-01** as a bounded **parallel developer-infrastructure** work order. It does not enter the product critical-path numbering and does not change the current work selector.

ARI-04 remains the current application implementation item. The forward product order remains unchanged.

## Why LXG runs now

MLR-01 completed and validated 45 workstation resources, but ordinary ChatGPT conversations cannot call those local programs merely because they exist on the laptop. Without a stable bridge, the project would continue depending on Codex/desktop-local sessions for operations that do not require frontier coding intelligence.

LXG turns the installed workstation into a provider-neutral local execution surface through MCP. This lets ChatGPT, Codex, Goose and later Multiversal developer tooling consume the same governed local capabilities without each learning bespoke shell commands.

## Placement

LXG executes in parallel with the current ARI family because:

- ARI immediately benefits from safe local archive/media/metadata/search tools;
- MIB-16 diagnostics can consume its evidence model;
- MIB-18 can include it in portability/readiness handoff;
- PCA can build higher-level production recipes on top rather than inventing another execution bridge;
- SMB-12 can use the same local-provider connectivity principles for real local AI;
- SAA/P3D later gain controlled local production adapters.

It must not mutate ARI-04's branch or broaden ARI-04's acceptance scope.

## Product roadmap effect

**No product-order change.**

Current sequence remains:

`ARI-04..21 → ARI-22A/B/C → MIB-16 → MIB-17 → MIB-18 → SMB-01..07 → CNI-01..13 → PCA-01..16 → SMB-08 → SMB-09 → SAA-01..20 → SMB-10 → SMB-11 → SMB-12..16 → BRP-01..11 → SMB-17 → SMB-18`

LXG is a reusable execution capability beneath that sequence.

## Required initial scope

LXG-01 Phase 1 provides a read-only/search/compute gateway:

- standard MCP `search` and `fetch`;
- gateway/tool/service status;
- bounded file and media inspection;
- bounded local Ollama query;
- loopback-only server;
- deny-by-default named filesystem roots;
- no arbitrary shell;
- no unrestricted filesystem access;
- no product mutation.

This baseline is deliberately useful on ChatGPT surfaces that support only read/fetch custom MCP access.

Phase-2 action tools are separately gated by app/workspace capability and explicit tool permissions.

## Implementation principle

LXG does **not** duplicate the 45 installed programs. It wraps approved capability through stable typed tools and fixed adapters.

Product code should request semantic operations such as `inspect_media`, `transcribe_audio` or `run_test_profile`, not command strings such as `ffprobe ...` or `whisper ...`.

## ChatGPT connection

The local MCP endpoint remains loopback-only. Current OpenAI product documentation states ordinary ChatGPT cannot connect directly to a localhost MCP endpoint; use Secure MCP Tunnel or another supported private-machine bridge. The ChatGPT-side custom app remains private/internal and should expose only the minimum enabled tools.

## Completion

LXG-01 may close independently of ARI when:

1. governed source and tests are merged;
2. local installation passes self-tests;
3. secure ChatGPT connection is established where the user's plan/workspace supports it;
4. ordinary Chat proves status + search/fetch access;
5. security boundaries pass;
6. actual connection/action capability is recorded.

A plan/workspace limitation on ChatGPT custom MCP may block only the ChatGPT connection portion, not invalidate the local gateway for Codex/Goose/MCP clients.
