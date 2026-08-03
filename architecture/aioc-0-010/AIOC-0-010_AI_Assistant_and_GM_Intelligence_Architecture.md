# AIOC-0-010 — AI Assistant and GM Intelligence Architecture

## 1. Purpose

Define the intelligence architecture that lets the AIOC answer project questions, guide development, assist GMs, search evidence, simulate impact, propose governed actions, and coordinate specialized agents without becoming an unbounded authority.

## 2. Scope

The architecture covers:

- conversational project command;
- GM preparation and live-session assistance;
- context retrieval and assembly;
- evidence and provenance;
- natural-language intent parsing;
- recommendations and alternatives;
- action proposals and approval;
- uncertainty and contradiction handling;
- scoped memory and continuity;
- multi-agent planning and review;
- cross-repository execution;
- privacy, hidden information, and safety;
- diagnostics, evaluation, and recovery.

## 3. Assistant operating model

Every request passes through these stages:

1. **Identity and workspace resolution** — determine user, role, campaign/project workspace, repository, and active branch.
2. **Intent classification** — distinguish question, search, draft, analysis, simulation, proposal, command, monitoring request, or emergency action.
3. **Context plan** — identify required sources and access boundaries.
4. **Evidence retrieval** — retrieve authoritative records before relying on conversation memory.
5. **Conflict analysis** — detect contradictory versions, stale state, or missing evidence.
6. **Response or proposal generation** — answer directly or produce a governed action proposal.
7. **Risk and permission evaluation** — classify reversibility, blast radius, privacy, and required approvals.
8. **Human review or execution** — execute only through approved tools and commands.
9. **Evidence recording** — preserve sources, tool results, decisions, and resulting state references.
10. **Memory update** — write only approved, scoped continuity records.

## 4. Intelligence surfaces

### 4.1 Executive assistant

Provides current milestone, blockers, repository health, pending approvals, next executable work, risk summaries, and cross-project impact.

### 4.2 Development assistant

Searches specifications and code, drafts work packages, proposes changes, routes agents, explains failures, and assembles validation evidence.

### 4.3 GM intelligence

Supports campaign preparation, scene and encounter setup, NPC and faction recall, rules lookup, consequence modeling, pacing support, hidden-information-aware summaries, and live action assistance.

### 4.4 Content intelligence

Assists with governed authoring, source extraction, provenance, duplicate detection, canon checks, pack construction, and adaptation.

### 4.5 Operations intelligence

Supports runtime incidents, synchronization problems, deployment questions, recovery recommendations, diagnostics, and audit review.

## 5. Context architecture

Context is assembled from explicit layers:

1. system and governance rules;
2. authenticated user and role;
3. active workspace and repository;
4. canonical current-state records;
5. task-specific authoritative documents;
6. recent verified events and tool results;
7. scoped conversation history;
8. optional user preferences.

Context bundles record source IDs, versions, timestamps, visibility, confidence, and reason for inclusion. Hidden information is filtered before model exposure, not merely hidden in the UI afterward.

## 6. Evidence model

Material factual claims use evidence references. Evidence may be:

- repository files and commits;
- schemas and manifests;
- campaign records and event streams;
- tests and validation reports;
- tool responses;
- approved source documents;
- explicit owner decisions.

Evidence records include authority class, source locator, version or commit, retrieval time, visibility, extracted claim, and confidence. Conversation memory alone is not authoritative evidence.

## 7. Answer classes

The assistant classifies outputs as:

- **Verified answer** — supported by authoritative evidence;
- **Reasoned inference** — derived from cited evidence with inference labeled;
- **Recommendation** — presents rationale, alternatives, and tradeoffs;
- **Draft** — non-authoritative proposed text or artifact;
- **Action proposal** — structured request awaiting approval or execution;
- **Unresolved** — evidence is missing or contradictory;
- **Safety escalation** — requires owner, administrator, GM, or specialist review.

## 8. Natural-language command architecture

Commands are never executed directly from raw model text. The assistant produces a typed command proposal containing:

- interpreted intent;
- target repository/workspace;
- action type;
- parameters;
- expected effects;
- risk class;
- reversibility;
- required approvals;
- validation plan;
- evidence references.

A policy engine validates the proposal before any connector or application command is invoked.

## 9. Permission and approval model

Permission checks evaluate identity, role, workspace, resource, operation, data visibility, and current state. Approval levels are:

- no approval for read-only low-risk queries;
- user confirmation for reversible personal changes;
- GM approval for governed campaign actions;
- maintainer approval for repository writes;
- owner approval for architectural, release, destructive, or cross-project changes;
- multi-party approval where policy requires separation of duties.

The AI may never approve its own high-risk proposal.

## 10. Recommendation engine

Recommendations include:

- objective;
- evidence;
- constraints;
- ranked options;
- expected benefit;
- cost and risk;
- downstream impact;
- uncertainty;
- recommended validation;
- decision owner.

The system avoids false precision and distinguishes measured data from estimates.

## 11. GM intelligence requirements

GM intelligence must:

- preserve GM-only and player-private information;
- separate canon, campaign truth, rumor, and speculation;
- provide rapid rules references with source links;
- explain action participants, targets, rolls, modifiers, and proposed outcomes;
- allow the GM to approve, deny, or alter governed results;
- create evidence-bearing alterations rather than rewriting history invisibly;
- support combat, social, investigation, travel, downtime, and custom modes;
- track unresolved threads, relationships, clues, consequences, and pacing;
- provide accessibility-friendly summaries and alternatives;
- function in degraded or offline modes using verified local context.

## 12. Memory architecture

Memory is divided into:

- ephemeral turn context;
- session working memory;
- task handoff memory;
- user preference memory;
- project continuity records;
- campaign memory;
- protected audit history.

Only explicit, governed records become durable memory. Durable entries identify owner, scope, source, retention, visibility, and supersession rules. Repository and campaign state supersede remembered summaries.

## 13. Multi-agent collaboration

The lead assistant may delegate bounded subtasks to specialist agents for architecture, implementation, review, testing, security, documentation, lore, balance, or data analysis. Delegation packets contain scope, evidence, constraints, output contract, and validation requirements.

Specialist outputs are proposals until independently reviewed or validated. Agents may not recursively expand scope without authorization.

## 14. Contradiction and uncertainty handling

When evidence conflicts, the assistant:

1. identifies the conflicting claims;
2. compares authority, date, version, and scope;
3. refuses silent synthesis where meanings differ;
4. proposes resolution paths;
5. records the final human decision.

Confidence is expressed qualitatively with supporting reasons, not as invented numerical certainty.

## 15. Explainability

For consequential recommendations and actions, the system exposes:

- what it understood;
- what evidence it used;
- what assumptions it made;
- what alternatives it considered;
- why the recommendation was selected;
- what could invalidate it;
- what will happen if approved.

Private chain-of-thought is not required; concise decision rationale and evidence are sufficient.

## 16. Cross-repository execution

Every repository action explicitly identifies the repository and branch. The current canonical mapping is:

- actual application: `cybalicistjt-stack/Multiversal-app`;
- command center: `cybalicistjt-stack/multiversal-aioc`.

The former TallBunyon repository is not an active target. Significant writes use a branch and draft pull request unless established policy permits otherwise.

## 17. Privacy and security

The assistant enforces least privilege, secret redaction, hidden-information filtering, attachment quarantine, prompt-injection resistance, data-retention rules, and auditability. Retrieved content is treated as data, not trusted instruction, unless it comes from a governed instruction source.

## 18. Failure and recovery

If tools, context, or permissions fail, the assistant stops unsafe writes, records the attempted action, verifies partial effects, and returns to the last known state. It never simulates completion. Recovery mode rechecks connectors, repository identity, current state, and pending proposals.

## 19. Evaluation

Evaluation domains include factual grounding, evidence completeness, permission enforcement, hidden-information protection, command interpretation, recommendation quality, uncertainty handling, tool-use correctness, recovery behavior, latency, and user correction rate.

## 20. Implementation slices

1. assistant request and response contracts;
2. context and evidence service;
3. intent and command proposal parser;
4. policy and approval engine;
5. scoped memory service;
6. GM intelligence adapters;
7. recommendation and impact service;
8. multi-agent routing;
9. diagnostics and evaluation harness;
10. UI integration and operational hardening.

## 21. Acceptance criteria

AIOC-0-010 is complete when:

- answers distinguish evidence, inference, recommendation, and uncertainty;
- action requests become typed governed proposals;
- repository and workspace targets are explicit;
- hidden information is filtered before AI context assembly;
- durable memory is scoped and reviewable;
- GM alterations remain evidence-bearing;
- multi-agent outputs are bounded and reviewable;
- tool failures cannot be represented as success;
- cross-repository execution follows permissions and branch policy;
- tests cover normal, adversarial, degraded, and recovery scenarios.