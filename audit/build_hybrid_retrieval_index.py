#!/usr/bin/env python3
"""Build a metadata-rich retrieval index with sparse retrieval, rank fusion, and reranking.

Dense embeddings are optional. The on-disk contract supports external vectors without
making them a prerequisite for deterministic CI evaluation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

TOKEN = re.compile(r"[a-z0-9][a-z0-9'’\-]+", re.I)
STOP = {"the", "a", "an", "and", "or", "of", "to", "in", "for", "with", "on", "at", "by", "is", "are", "be", "as", "that", "this"}
GENERIC = re.compile(r"^(?:actions?|traits?|effects?|statistics?|objectives?|notes?|description|equipment|abilities|attacks?|table|examples?)$", re.I)


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def terms(text: object) -> list[str]:
    return [token.lower().replace("’", "'") for token in TOKEN.findall(str(text or "")) if token.lower() not in STOP]


def stable(*parts: object) -> str:
    return hashlib.sha256("\n".join(str(x or "") for x in parts).encode("utf-8", "ignore")).hexdigest()[:20]


def archive_family(path: str) -> str:
    path = path.lower().replace("\\", "/")
    for family in ("part-1", "part-2", "part-3", "creatures"):
        if f"/{family}/" in f"/{path}/":
            return family
    return "unknown"


def build_index(chunks: list[dict]) -> tuple[list[dict], dict]:
    document_frequency: Counter[str] = Counter()
    indexed: list[dict] = []
    for chunk in chunks:
        title_text = " ".join(filter(None, [chunk.get("title"), chunk.get("localTitle"), chunk.get("parentObjectTitle")]))
        body_text = chunk.get("searchableText") or chunk.get("text") or ""
        title_terms = terms(title_text)
        body_terms = terms(body_text)
        all_terms = title_terms + body_terms
        unique = set(all_terms)
        document_frequency.update(unique)
        metadata = {
            "chunkId": chunk["chunkId"],
            "nodeId": chunk["nodeId"],
            "parentId": chunk.get("parentId"),
            "archiveFamily": archive_family(chunk.get("sourceRelativePath") or chunk.get("sourcePath") or ""),
            "sourceRelativePath": chunk.get("sourceRelativePath"),
            "pageStart": chunk.get("pageStart"),
            "pageEnd": chunk.get("pageEnd"),
            "locator": chunk.get("locator"),
            "findingId": chunk.get("findingId"),
            "title": chunk.get("title"),
            "localTitle": chunk.get("localTitle"),
            "parentObjectTitle": chunk.get("parentObjectTitle"),
            "headingPath": chunk.get("headingPath") or [],
            "sectionRole": chunk.get("sectionRole"),
            "blockType": chunk.get("blockType"),
            "identityEligible": bool(chunk.get("identityEligible")),
            "provenanceComplete": bool(chunk.get("provenanceComplete")),
            "familyScores": chunk.get("familyScores") or {},
            "mechanicSignals": chunk.get("mechanicSignals") or [],
            "contentHash": chunk.get("contentHash"),
            "text": chunk.get("text") or "",
            "searchableText": body_text,
            "embeddingText": "\n".join(part for part in [" > ".join(chunk.get("headingPath") or []), body_text] if part),
            "titleTerms": title_terms,
            "bodyTerms": body_terms,
            "termFrequency": dict(Counter(all_terms)),
            "length": len(all_terms),
        }
        metadata["indexHash"] = stable(metadata["contentHash"], metadata["embeddingText"])
        indexed.append(metadata)
    corpus = {
        "documentCount": len(indexed),
        "averageLength": sum(row["length"] for row in indexed) / max(1, len(indexed)),
        "documentFrequency": dict(document_frequency),
    }
    return indexed, corpus


def bm25(query_terms: list[str], row: dict, corpus: dict, k1: float = 1.2, b: float = 0.75) -> float:
    score = 0.0
    n = corpus["documentCount"]
    avg = corpus["averageLength"] or 1.0
    for term in query_terms:
        tf = row["termFrequency"].get(term, 0)
        if not tf:
            continue
        df = corpus["documentFrequency"].get(term, 0)
        idf = math.log(1 + (n - df + 0.5) / (df + 0.5))
        denom = tf + k1 * (1 - b + b * row["length"] / avg)
        score += idf * (tf * (k1 + 1)) / denom
    return score


def exact_score(query: str, row: dict) -> float:
    q = " ".join(terms(query))
    title = " ".join(terms(row.get("title")))
    parent = " ".join(terms(row.get("parentObjectTitle")))
    if q and q == title:
        return 10.0
    if q and q == parent:
        return 8.0
    if q and (q in title or title in q):
        return 5.0
    return 0.0


def structural_score(row: dict, expected_family: str | None = None) -> float:
    score = 0.0
    if row.get("identityEligible"):
        score += 2.0
    if row.get("provenanceComplete"):
        score += 1.0
    if row.get("sectionRole") == "object-section":
        score += 2.0
    if row.get("sectionRole") == "container":
        score -= 5.0
    if GENERIC.match(str(row.get("localTitle") or "")):
        score -= 4.0
    if expected_family:
        score += min(3.0, float((row.get("familyScores") or {}).get(expected_family, 0)) / 3.0)
    return score


def reciprocal_rank_fusion(rankings: list[list[str]], k: int = 60) -> dict[str, float]:
    fused: defaultdict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, chunk_id in enumerate(ranking, start=1):
            fused[chunk_id] += 1.0 / (k + rank)
    return dict(fused)


def retrieve(query: str, rows: list[dict], corpus: dict, expected_family: str | None = None, top_k: int = 20) -> list[dict]:
    qterms = terms(query)
    lexical = sorted(rows, key=lambda row: bm25(qterms, row, corpus), reverse=True)[: max(top_k * 4, 40)]
    exact = sorted(rows, key=lambda row: exact_score(query, row), reverse=True)[: max(top_k * 4, 40)]
    structural = sorted(rows, key=lambda row: structural_score(row, expected_family), reverse=True)[: max(top_k * 4, 40)]
    fused = reciprocal_rank_fusion([[row["chunkId"] for row in ranking] for ranking in (lexical, exact, structural)])
    by_id = {row["chunkId"]: row for row in rows}
    pool = sorted(fused, key=fused.get, reverse=True)[: max(top_k * 3, 30)]
    reranked = []
    for chunk_id in pool:
        row = by_id[chunk_id]
        lexical_score = bm25(qterms, row, corpus)
        title_score = exact_score(query, row)
        structure = structural_score(row, expected_family)
        family = float((row.get("familyScores") or {}).get(expected_family, 0)) if expected_family else 0.0
        coherence = min(3.0, len(row.get("headingPath") or []) * 0.5)
        duplicate_penalty = -3.0 if GENERIC.match(str(row.get("title") or "")) else 0.0
        final = fused[chunk_id] * 100 + lexical_score + title_score + structure + min(3.0, family / 2.0) + coherence + duplicate_penalty
        reranked.append({
            "chunkId": chunk_id,
            "score": round(final, 6),
            "fusedScore": round(fused[chunk_id], 8),
            "lexicalScore": round(lexical_score, 6),
            "titleScore": round(title_score, 6),
            "structuralScore": round(structure, 6),
            "row": row,
        })
    reranked.sort(key=lambda result: (-result["score"], result["chunkId"]))
    return reranked[:top_k]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--structure", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--queries", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    chunks = load_jsonl(args.structure / "section-aware-chunks.jsonl")
    rows, corpus = build_index(chunks)
    with (args.out / "retrieval-index.jsonl").open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    (args.out / "retrieval-corpus-stats.json").write_text(json.dumps(corpus, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    evaluations = []
    if args.queries and args.queries.exists():
        query_payload = json.loads(args.queries.read_text(encoding="utf-8"))
        for query in query_payload.get("queries", []):
            results = retrieve(query["query"], rows, corpus, query.get("expectedFamily"), query.get("topK", 20))
            expected = set(query.get("expectedChunkIds") or [])
            ranks = [i + 1 for i, result in enumerate(results) if result["chunkId"] in expected]
            evaluations.append({
                "queryId": query.get("queryId"),
                "query": query["query"],
                "expectedFamily": query.get("expectedFamily"),
                "resultCount": len(results),
                "hit": bool(ranks) if expected else None,
                "firstRelevantRank": min(ranks) if ranks else None,
                "results": results,
            })
        (args.out / "retrieval-evaluation-results.json").write_text(json.dumps({"queries": evaluations}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    summary = {
        "format": "multiversal-hybrid-retrieval-index",
        "version": "1.0.0",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "chunkCount": len(rows),
        "identityEligibleCount": sum(row["identityEligible"] for row in rows),
        "provenanceCompleteCount": sum(row["provenanceComplete"] for row in rows),
        "archiveFamilyCounts": dict(Counter(row["archiveFamily"] for row in rows)),
        "sectionRoleCounts": dict(Counter(row["sectionRole"] for row in rows)),
        "embeddingContractReady": True,
        "denseEmbeddingsPresent": False,
        "hybridMethod": "BM25 + exact-title + metadata/structure via reciprocal-rank fusion",
        "rerankingMethod": "deterministic structure-aware reranking; cross-encoder replaceable",
        "evaluationQueryCount": len(evaluations),
        "publishedSample": rows[:100],
        "authorityNote": "Retrieval index entries are evidence records, not canonical objects.",
    }
    (args.out / "hybrid-retrieval-index.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("chunkCount", "identityEligibleCount", "archiveFamilyCounts", "sectionRoleCounts")}, indent=2))


if __name__ == "__main__":
    main()
