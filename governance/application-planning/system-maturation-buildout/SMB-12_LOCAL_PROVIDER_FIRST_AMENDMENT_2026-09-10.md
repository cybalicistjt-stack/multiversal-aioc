# SMB-12 — Local-Provider-First AI Integration Amendment — 2026-09-10

**Status:** OWNER-APPROVED PLANNING AMENDMENT  
**Owning tranche:** SMB-12 — Real Optional AI Integrations  
**Order change:** none  
**Provider lock-in:** prohibited

## Decision

SMB-12's first real-provider proof shall use a **local provider through the existing MIB-15 provider-neutral adapter contract** before any paid hosted provider becomes necessary for acceptance.

The currently validated workstation includes Ollama/local-inference capability. Ollama is the preferred first reference provider because it is already available locally, but it does **not** become canonical AI infrastructure and may be replaced by another conforming local provider.

## Required acceptance sequence

1. **Provider-off baseline:** all blocking product workflows pass with AI disabled.
2. **Deterministic/fake provider:** existing MIB-15 contract tests continue to prove proposal/candidate envelopes, errors, timeout and fallback behavior.
3. **Real local provider:** a local provider such as Ollama is connected through the MIB-15 adapter without bypassing context/visibility/proposal rules.
4. **Local-provider failure/fallback:** stopping or degrading the local provider does not break blocking product workflows or grant fallback authority to AI.
5. **Cost/privacy/provenance evidence:** local execution records provider/model/version, context provenance, output disposition and resource usage where practical.
6. **Optional hosted provider(s):** only after the local real-provider proof, and only under separate then-current authority for credentials, spend, privacy and network use.

## Local-provider scope

Appropriate first local-provider tasks include bounded writing assistance, worldbuilding alternatives, retrieval/search assistance, summarization, structured drafting, permitted GM presentation and other advisory workflows whose outputs are inspectable and noncanonical by default.

Do not use local-provider status as justification for mechanical/canonical/permission/consent/adjudication authority, hidden-information leakage, unrestricted NPC/GM mutation or bypass of Action/Event approval paths.

## Quality rule

Local-first does not mean local-only. If a task-level benchmark shows the local provider cannot satisfy an optional experience at acceptable quality or cost, SMB-12 may expose a replaceable hosted provider as an enhancement. Paid/cloud execution remains optional for blocking workflows.

## PCA relationship

PCA-09 and PCA-11 may later supply richer routing, caching, style/reference manifests and character-intelligence orchestration. SMB-12 consumes those capabilities where complete rather than creating a second provider/router authority.

## Current-work boundary

This amendment does not start SMB-12, activate Ollama as a product service, authorize paid providers, alter `CURRENT_WORK_POINTER.json`, or change the current ARI-04 implementation authority.