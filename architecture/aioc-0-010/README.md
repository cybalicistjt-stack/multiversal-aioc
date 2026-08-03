# AIOC-0-010 — AI Assistant and GM Intelligence Architecture

**Status:** Implementation-ready architecture package  
**Version:** 0.1.0  
**Owner:** John Brandon Turner  
**Validation target:** PASS

This package defines the governed conversational intelligence layer for the AIOC command center and the Multiversal GM experience. It covers context assembly, evidence-backed answers, bounded recommendations, natural-language commands, action proposals, permissions, memory, explainability, uncertainty, escalation, multi-agent collaboration, and cross-repository execution.

## Package contents

- `AIOC-0-010_AI_Assistant_and_GM_Intelligence_Architecture.md`
- `capability-catalog.json`
- `workflow-catalog.json`
- `validation-rules.json`
- `schemas/assistant-request.schema.json`
- `schemas/assistant-proposal.schema.json`
- `schemas/intelligence-evidence.schema.json`
- `tests/acceptance-test-matrix.json`
- `VALIDATION_RESULT.md`
- `MANIFEST.json`
- `work-orders/AIOC-0-011_WORK_ORDER.md`

## Governing invariants

1. AI may advise, draft, classify, search, simulate, and propose.
2. AI may not silently mutate authoritative project or campaign state.
3. Every material answer identifies evidence, uncertainty, and scope.
4. Every executable action passes permission, risk, and approval checks.
5. GM intelligence preserves hidden information and player boundaries.
6. Conversation memory is scoped, reviewable, and never more authoritative than repository or campaign records.
7. Cross-repository actions identify the target repository before execution.
8. Human authority remains final.