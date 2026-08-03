# Browser, MCP, REST, and Codex Integration

## Purpose

Step 9 exposes validated Development Brain artifacts through the existing AIOC browser and bridge architecture without creating a second source of truth.

## Governed surfaces

- **Browser** — read-only inspection of artifacts, findings, evidence, freshness, and authority warnings.
- **MCP** — typed reads and governed proposal creation through the existing `/mcp` bridge.
- **REST** — versioned read endpoints and proposal submission under `/api/development-brain/v1`.
- **Codex** — governed skill workflow for reading context, selecting verified tasks, preparing bounded changes, running validation, and submitting reviewable proposals.

## Authority boundaries

- Validated artifacts and canonical governance records may be read.
- Browser access is read-only in Step 9.
- MCP, REST, and Codex writes are proposal-only.
- No surface may directly mutate, promote, certify, or recertify canonical content.
- No surface may infer, grant, or substitute owner or governance approval.
- Verified recommendations remain advisory until accepted through normal repository governance.

## Freshness and provenance

Every surfaced artifact carries a source path, authority class, and freshness token tied to a repository ref. Consumers must compare the token with the source ref before relying on executable eligibility. Stale or mismatched artifacts must be rejected and regenerated.

## Audit requirements

Every integration request must preserve the surface ID, request ID, artifact ID, source ref, operation, timestamp, and outcome. Proposal writes must retain the complete evidence chain and normal review/CI gates.

## Existing architecture alignment

This contract extends the existing `bridge/` architecture: canonical repository data, remote MCP proposal tools, and the operational browser. Browser-local working state remains a known limitation until shared server-side state is implemented; Step 9 does not pretend that local storage is remotely synchronized.

## Validation

The generator produces a deterministic integration manifest for all eight Development Brain artifact families and four integration surfaces. The validator enforces surface completeness, read/write boundaries, stale-artifact rejection, audit fields, authority safeguards, and summary consistency. CI publishes the `aioc-development-brain-integration` artifact.
