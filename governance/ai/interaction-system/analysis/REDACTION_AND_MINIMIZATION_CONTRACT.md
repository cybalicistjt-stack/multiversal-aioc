# Interaction Evidence Redaction and Minimization Contract

**Document ID:** MV-CONT-PRIV-001  
**Version:** 1.0.0  
**Status:** ACTIVE FOR MV-CONT-002  
**Owner and final authority:** John Brandon Turner

## Purpose

This contract allows Multiversal to learn from its private conversation history without publishing the private transcript to the public governance repository.

## Allowed public evidence

Public interaction-audit artifacts may contain:

- immutable package and source hashes;
- aggregate conversation and message counts;
- synthetic episode IDs;
- internal conversation IDs and message-index ranges;
- broad project-domain labels;
- paraphrased trigger, behavior, and outcome summaries;
- controlled taxonomy and evaluation identifiers;
- severity and owner-intervention flags;
- validation and release metadata.

## Prohibited public evidence

Public artifacts must not contain:

- raw or lightly edited conversation messages;
- verbatim private passages;
- attachment contents;
- personal contact information;
- credentials, secrets, tokens, private URLs, or private repository content not already public;
- hidden chain-of-thought or private scratchpad material;
- file names or conversation titles when they add no evaluation value;
- unique sensitive details that are unnecessary for reproducing the interaction pattern.

## Minimization rules

1. Preserve the behavioral fact, not the original phrasing.
2. Use the smallest source locator needed for audit: conversation ID plus message-index range.
3. Do not publish a direct quote merely because it is memorable.
4. Replace project-specific details with governed identifiers when the detail is not necessary to the test.
5. Keep raw source bytes only in the owner-held immutable package.
6. A public episode must set `verbatim_content_included` to `false`.
7. Every published pattern must be supported by at least one redacted episode.
8. Every evaluation case must identify the patterns it tests without reproducing the original message.

## Review and correction

If a public record is later found to reveal unnecessary private detail:

1. preserve the original release hash and incident record;
2. remove or further generalize the exposed detail;
3. issue a new version;
4. update validation to prevent recurrence;
5. never rewrite history silently.

## Training boundary

The public redacted corpus is suitable for regression tests, rubric design, prompt evaluation, and synthetic training examples. It is not a replacement for the private source archive and must not be presented as a verbatim transcript.
