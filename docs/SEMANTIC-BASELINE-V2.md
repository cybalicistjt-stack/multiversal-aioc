# Semantic Recovery Baseline v2

Status: implementation baseline
Owner: John Brandon Turner
Purpose: establish a trustworthy, measurable semantic-recovery threshold before UI/UX consultancy and large-scale human review.

## Why the prior approach was insufficient

Earlier passes proved corpus traversal and candidate generation, but they relied too heavily on string heuristics and aggregate counts. They repeatedly allowed section headings, clause fragments, table cells, procedures, and family mismatches into review queues. Successful workflow execution was therefore not evidence of semantic quality.

Baseline v2 changes the success definition from “outputs were generated” to “outputs passed measured quality gates.”

## Research-informed architecture

The pipeline treats document recovery as separate linked tasks:

1. evidence detection and ordering;
2. document hierarchy construction;
3. candidate identity detection;
4. family classification;
5. field extraction;
6. entity and relationship resolution;
7. error analysis and evaluation;
8. precision-first publication.

No stage may hide failures from a later stage.

## Required outputs

- `semantic-baseline-v2-index.json`
- `semantic-baseline-v2-ready.jsonl`
- `semantic-baseline-v2-needs-review.jsonl`
- `semantic-baseline-v2-rejected.jsonl`
- `semantic-baseline-v2-error-report.json`
- `semantic-baseline-v2-regression-report.json`

## Candidate identity contract

A publishable candidate must have all of the following:

- complete document/page/finding provenance;
- a normalized, object-like identity rather than a clause or section instruction;
- substantive supporting text;
- family evidence from at least two independent channels among title, body, document path, structural context, and extracted fields;
- a clear winning family score rather than a near tie;
- no known regression signature;
- a stable evidence hash;
- an explicit confidence tier.

## Confidence tiers

### Ready for substantive review

Precision-first tier. Minimum confidence 85. Strong identity, family agreement, substantive evidence, and no hard rejection reason.

### Needs semantic review

Confidence 70–84. Potentially useful but ambiguous identity, family, segmentation, or relationship evidence.

### Rejected evidence

Below 70 or any hard failure: clause heading, table fragment, numeric noise, generic section title, missing provenance, insufficient text, family conflict, duplicate fragment, or known regression.

## Evaluation gates

The workflow must fail closed unless:

- regression fixture accuracy is at least 95%;
- no known bad example is accepted into the ready tier;
- every ready candidate has complete provenance;
- every ready candidate has a family margin of at least 3;
- at least five object families are represented when the corpus contains them;
- graph field parsing is verified against `sourceId`, `targetId`, and `relationshipType`;
- ready-tier duplicates are below 2%;
- all counts reconcile exactly.

A manually reviewed stratified gold set remains the final acceptance gate. Automatic fixtures prevent regression, but they do not replace owner/expert validation.

## Error taxonomy

- `clause-heading`
- `section-heading`
- `table-fragment`
- `numeric-noise`
- `generic-title`
- `missing-provenance`
- `non-substantive`
- `family-conflict`
- `family-ambiguous`
- `duplicate-fragment`
- `relationship-noise`
- `known-regression`

Every rejected or downgraded candidate must record one or more reasons.

## Baseline completion criteria

The engineering baseline is complete when the automated gates pass and a stratified owner-review packet is generated. The semantic baseline is fully accepted only after the owner or designated expert reviews that packet and the measured precision meets the agreed threshold.

## Timeline

1. Implement and run Baseline v2.
2. Review the stratified acceptance packet.
3. Correct any remaining systematic error classes.
4. Lock the semantic baseline.
5. Begin the AIOC UI/UX Consultancy Phase.
6. Resume large-scale canonical recovery through the redesigned interface.
