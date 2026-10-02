# MTLC Planning Write Incident

**Date:** 2026-10-02  
**Scope:** Planning/governance artifact recording only  
**Status:** CORRECTED_BY_PR_PATH

While recording the owner-approved MTLC community-demand convergence update, the executor mistakenly issued two repository-content writes without the intended planning branch:

1. `MTLC_COMMUNITY_FRICTION_REGISTRY.json` was created directly on the default branch with placeholder content.
2. The first version of this incident note was also mistakenly created directly on the default branch while attempting to document the first error.

Both were executor/tool-use errors. Neither changed `operations/CURRENT.json`, selected product work, granted implementation authority, or modified application code.

Corrective action: the complete community friction registry, amended MTLC charter, amended machine-readable backlog, and this corrected incident record were prepared on `planning/mtlc-community-demand-convergence` for pull-request integration. The incident is retained so the protected-main control-surface mistake is not hidden.

Prevention: repository content mutations for planning/governance changes must explicitly create/select the intended branch before the first content write; omission of the branch argument must be treated as unsafe when the repository default branch is protected.
