# Semantic Recovery Retrieval Architecture

Status: Implementation approved

## Decision

Adopt all four techniques as a staged system:

1. section-aware hierarchical chunking;
2. metadata-rich indexing;
3. hybrid sparse/semantic retrieval;
4. bounded reranking.

They are not substitutes for one another. Chunking determines the evidence units, metadata preserves context, hybrid retrieval produces a high-recall candidate set, and reranking produces a high-precision shortlist.

## Why the previous approach failed

The original structure engine split findings using isolated heading regexes and length thresholds. It did not maintain a section stack, distinguish container headings from object identities, attach labels such as Actions or Traits to their parent object, or preserve neighboring context. This caused headings, table rows, and child sections to become independent candidate objects.

## Architecture

### Stage A — Hierarchical document model

Each source document becomes a tree:

- document;
- chapter or major section;
- subsection;
- object section;
- child section or field group;
- atomic evidence block.

Every node has a stable ID, parent ID, ancestor path, section role, source page range, reading order, and provenance.

### Stage B — Section-aware chunks

Chunks are built inside section boundaries. A chunk may include:

- the current section title;
- a bounded ancestor-title path;
- the local body;
- small previous/next sibling context when needed;
- child labels attached to the parent object.

Generic container labels such as Actions, Traits, Effects, Objectives, Statistics, and Equipment are never independent object identities.

### Stage C — Metadata-rich retrieval index

Every searchable unit includes:

- chunk ID and structural node ID;
- document and archive family;
- source-relative path;
- page start/end and locator;
- heading path and parent object title;
- structural role;
- block type;
- candidate object-family signals;
- mechanic signals;
- provenance hash;
- exact searchable text;
- normalized lexical terms;
- optional embedding text;
- neighboring and parent IDs.

### Stage D — Hybrid retrieval

The first-stage candidate pool combines:

- exact/normalized name matches;
- BM25-style lexical scoring;
- metadata filters and boosts;
- semantic-vector scoring when an embedding provider is configured;
- structural proximity and parent-child boosts.

Rank fusion is used rather than directly comparing incompatible sparse and dense scores.

### Stage E — Reranking

Only the bounded top candidate pool is reranked. The reranker considers:

- query-to-text relevance;
- title and parent-title agreement;
- expected family agreement;
- structural role;
- provenance completeness;
- section coherence;
- candidate completeness;
- penalties for generic headings, table fragments, and duplicated evidence.

A cross-encoder can replace the deterministic reranker later without changing the index contract.

## Evaluation

The system must be tested at each layer:

- boundary precision/recall for section and object boundaries;
- parent-attachment accuracy;
- container-heading false-positive rate;
- retrieval Recall@k;
- MRR and nDCG;
- reranker precision at the review cutoff;
- family-level coverage;
- duplicate rate;
- owner acceptance precision.

Publication gates remain precision-first. Retrieval may increase recall, but cannot promote candidates whose structural identity is invalid.

## Rollout

1. Replace flat block splitting with hierarchical section construction.
2. Generate the metadata-rich retrieval index.
3. Add deterministic lexical hybrid search and rank fusion.
4. Add reranking and a retrieval evaluation harness.
5. Integrate the new structural and retrieval signals into Baseline v2.
6. Add external embeddings or a cross-encoder only after the deterministic baseline is measured and stable.
