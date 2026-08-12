#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
INV = BASE / "PPIA-09_SOURCE_AND_DESIGN_INVENTORY.md"
SRC = BASE / "PPIA-09_SOURCE_MANIFEST_v0.1.0.json"
TAX = BASE / "PPIA-09_INVESTIGATION_MYSTERY_TAXONOMY_v0.1.0.json"
AUTH = BASE / "PPIA-09_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
CAND = BASE / "PPIA-09_FOUNDATION_CANDIDATE.md"
BACKLOG = BASE / "PPIA_PROGRAM_BACKLOG.json"
P8 = ROOT / "governance/ai/work-state/PPIA-08-attempt-001.json"
P9 = ROOT / "governance/ai/work-state/PPIA-09-attempt-001.json"
PTR = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
F011 = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_AND_CLUE_BOARD.md"
F011_MATRIX = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_INVESTIGATION_CLUE_MATRIX.json"
F011_SOURCE = ROOT / "governance/application-planning/internal-alpha/feature-packets/MV-IA-F011_SOURCE_COVERAGE_AND_PROVENANCE.json"

TRANSITION_MERGE = "a3545f2b77bd2bddade747ffc2ef58863eedff21"
P8_COMPLETION_MERGE = "09f9df2607398010097e834e8ad7b129cd10645f"
PACKAGE_SHA = "c5732c5b4c3cdf5eca1d19eef7354289d1f92a87397b56aa7623b3f0a24177ec"
FOUNDATION_FINAL_HEAD = "e4999c40e1fe92852c142789b3d70596dfad52a8"
FOUNDATION_PR = 253
FOUNDATION_MERGE = "511b7b3edc0b88ff8ea5683fd093d2853b50ccf1"
P9_COMPLETION_HEAD = "7393eac19d88eb5b2c58e44b51c1c3a2f3e2b968"
P9_COMPLETION_PR = 256
P9_COMPLETION_MERGE = "3996ca97a2e31fa89ce5c9d4101c96affb83ea71"
ACTIVE = {"started", "in_progress"}
COMPLETE = {"complete", "completed", "completed_verified"}


def req(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("PPIA-09 FOUNDATION: FAIL — " + message)


def load(path: Path) -> dict:
    req(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (INV, SRC, TAX, AUTH, CAND, F011, F011_MATRIX, F011_SOURCE):
        req(path.exists(), f"missing {path.relative_to(ROOT)}")

    inv = INV.read_text(encoding="utf-8")
    src = load(SRC)
    tax = load(TAX)
    auth = load(AUTH)
    cand = CAND.read_text(encoding="utf-8")
    backlog = load(BACKLOG)
    p8 = load(P8)
    p9 = load(P9)
    ptr = load(PTR)
    status = load(STATUS)
    f011 = F011.read_text(encoding="utf-8")
    f011_matrix = load(F011_MATRIX)
    f011_source = load(F011_SOURCE)

    tranches = {x["work_item_id"]: x for x in backlog["tranches"]}
    req(p8["status"] == "completed_verified" and p8["merge_commit"] == P8_COMPLETION_MERGE, "PPIA-08 dependency must remain completed_verified")
    req(tranches["PPIA-08"]["status"] == "completed_verified", "PPIA-08 backlog dependency changed")
    req("PPIA-08" in tranches["PPIA-09"]["dependencies"], "PPIA-09 dependency on PPIA-08 missing")

    src_identity_ok = src["work_item_id"] == "PPIA-09" and src["transition_merge"] == TRANSITION_MERGE
    req(src_identity_ok, "source manifest identity/transition mismatch")
    req(src["retained_package"]["sha256"] == PACKAGE_SHA, "retained package SHA changed")
    pdfs = src["direct_pdf_sources"]
    req(len(pdfs) == 3 and src["direct_pdf_totals"] == {"files":3,"pages":53}, "direct PDF source boundary must remain 3 files / 53 pages")
    req(all(x.get("visual_review_complete") is True for x in pdfs), "all direct PDFs must be visually reviewed")
    expected_pdf = {
        "ac76b433d2b0d007667eaf4701070aae738dd20262b9d9c30d13a09a3a888760":40,
        "f3df38da25d46e03724d0161663bb81c805411f62df7886337e95c26594a20a6":11,
        "929b3fcf928fd6ec423128ca0688061eaaff812605b5986380553adda3795ffc":2,
    }
    req({x["sha256"]:x["pages"] for x in pdfs} == expected_pdf, "direct PDF hash/page evidence changed")
    req(len(src["direct_design_sources"]) == 4, "expected four direct design-source entries")
    structured = src["structured_support_sources"]
    req(len(structured) == 4, "expected four structured support sources")
    req(src["structured_support_totals"] == {"files":4,"rows":4936,"bounded_keyword_hit_rows":1570}, "structured support totals changed")
    req(next(x for x in structured if x["path"].endswith("Abilities_Core.csv"))["explicit_investigation_knowledge_tree_rows"] == 109, "explicit Investigation/Knowledge ability-tree row count changed")
    req(len(src["canonical_repository_support"]) == 12, "expected twelve canonical repository support boundaries")
    req(len(src["source_backed_findings"]) == 14, "expected fourteen source-backed findings")
    req(len(src["explicit_source_gaps"]) == 10, "expected ten explicit source gaps")
    req(all(v is False for v in src["non_assumptions"].values()), "source non-assumptions must remain false")

    req(f011_matrix["featureId"] == "MV-IA-F011", "wrong F011 matrix feature")
    req(len(f011_matrix["records"]) == 10, "F011 must retain ten core record families")
    req(len(f011_matrix["connectionTypes"]) == 15, "F011 must retain fifteen typed connection predicates")
    req(len(f011_matrix["fixtures"]) == 24, "F011 must retain twenty-four deterministic fixtures")
    req(f011_source["coverageClaims"]["deterministicFixtures"] == 24 and f011_source["coverageClaims"]["blockingAcceptanceCriteria"] == 28, "F011 source coverage evidence changed")
    req(any("does not claim exhaustive extraction" in x for x in f011_source["limitations"]), "F011 bounded-source limitation missing")
    low_f011 = f011.lower()
    for phrase in ("player deductions are not auto-promoted to fact", "spatial placement is presentation state", "private clue", "false lead", "idempotency", "nonvisual"):
        req(phrase in low_f011, f"F011 invariant missing {phrase!r}")

    layers = tax["identity_state_layers"]
    req(len(layers) == 16 and len({x["id"] for x in layers}) == 16, "expected sixteen unique PPIA-09 semantic layers")
    required_layers = {
        "objective-truth-and-gm-solution","campaign-clue-discovery-and-analysis-state","observation-claim-and-statement",
        "witness-source-reliability-and-authenticity","hypothesis-theory-and-deduction","timeline-temporal-order-and-alibi",
        "contradiction-false-lead-and-uncertainty","discovery-condition-reveal-and-knowledge-audience",
        "solvability-redundancy-progression-and-stall-recovery","permission-provenance-version-recovery-accessibility"
    }
    req(required_layers <= {x["id"] for x in layers}, "critical investigation semantic layer missing")
    req(len(tax["presentation_profiles"]) == 12 and len(set(tax["presentation_profiles"])) == 12, "expected twelve presentation profiles")
    req(len(tax["truth_belief_invariants"]) == 6, "truth/belief invariants changed")
    req(len(tax["authoring_invariants"]) == 7, "authoring invariants changed")
    req(all(v is False for v in tax["foundation_non_assumptions"].values()), "foundation non-assumptions must remain false")

    req(len(auth["authority_levels"]) == 4, "expected four authority levels")
    handoffs = auth["domain_handoffs"]
    req(len(handoffs) == 12, "expected twelve domain handoffs")
    req([x["id"] for x in handoffs] == [f"P9-HO-{i:03d}" for i in range(1,13)], "handoff IDs must be contiguous P9-HO-001..012")
    guard = " ".join(auth["blocking_guardrails"]).lower()
    for phrase in ("player-visible", "objective truth", "contradiction", "false leads", "owning-domain", "timeline", "permissions", "operation-id", "non-authoritative presentation", "ai-generated", "runtime"):
        req(phrase in guard, f"authority guardrail missing {phrase!r}")
    req(len(auth["proposal_stage_design_domains"]) == 6, "proposal-stage design-domain set changed")

    for phrase in ("3 PDFs / 53 pages", "4 CSVs / 4,936 rows", "109 records", "The Vanishing of Dr. Wen", "surface / hidden / revealed", "at least two places", "explicit source/design gaps", "truth ≠ belief"):
        req(phrase.lower() in inv.lower(), f"source inventory missing {phrase!r}")
    for phrase in ("FOUNDATION CANDIDATE — NOT PPIA-09 COMPLETE", "3 directly relevant PDFs / 53 pages", "16 semantic layers", "12 presentation profiles", "12 domain handoffs", "24 F011 deterministic fixtures", "The Vanishing of Dr. Wen", "deterministic solvability", "graph layout", "No application runtime"):
        req(phrase.lower() in cand.lower(), f"foundation candidate missing {phrase!r}")

    # Historical milestone validation is dual-mode. Durable foundation proof is the immutable validated head + PR + merge retained in checkpoint history.
    req(p9["work_item_id"] == "PPIA-09" and p9["attempt_id"] == "PPIA-09-attempt-001", "PPIA-09 checkpoint identity mismatch")
    req(p9["branch"] == "governance/ppia-09-investigation-mystery-authoring", "PPIA-09 branch mismatch")
    req(p9["base_commit"] == P8_COMPLETION_MERGE, "PPIA-09 original base anchor changed")
    req(not p9["unresolved_failures"] and p9["owner_decision_required"] is False, "PPIA-09 checkpoint unresolved state")
    req(p9["status"] in ACTIVE | {"completed_verified"}, f"unexpected PPIA-09 checkpoint status {p9['status']!r}")
    foundation_history = json.dumps({
        "last_verified_action": p9.get("last_verified_action"),
        "completed_substeps": p9.get("completed_substeps", []),
        "validation": p9.get("validation", []),
        "evidence": p9.get("evidence", []),
    }, ensure_ascii=False)
    for value in (FOUNDATION_FINAL_HEAD, f"PR #{FOUNDATION_PR}", FOUNDATION_MERGE):
        req(value in foundation_history, f"immutable PPIA-09 foundation evidence missing {value}")

    current_id = backlog["current_work_item_id"]
    if current_id == "PPIA-09":
        req(tranches["PPIA-09"]["status"] in ACTIVE and p9["status"] in ACTIVE, "active PPIA-09 must remain started/in_progress")
        req(ptr["primary_attempt_id"] == "PPIA-09-attempt-001", "active pointer must select PPIA-09")
        selected = [x for x in ptr["active_attempts"] if x.get("owner_selected")]
        req(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-09", "exactly one owner-selected PPIA-09 attempt required")
        req(status["primary"]["work_item_id"] == "PPIA-09" and status["primary"]["status"] in ACTIVE, "active compact status must select PPIA-09")
        continuity_mode = "active_ppia09"
    else:
        order = backlog["execution_order"]
        req(order.index(current_id) > order.index("PPIA-09"), "historical foundation validation may only run after PPIA-09")
        req(tranches["PPIA-09"]["status"] in COMPLETE, "historical PPIA-09 backlog must be complete")
        req(p9["status"] == "completed_verified" and p9.get("completed_at") and p9.get("active_substep") is None, "historical PPIA-09 checkpoint must be completed_verified")
        req(p9.get("latest_pushed_commit") == P9_COMPLETION_HEAD, "PPIA-09 completion head changed")
        req(p9.get("pull_request") == P9_COMPLETION_PR and p9.get("merge_commit") == P9_COMPLETION_MERGE, "PPIA-09 completion PR/merge changed")
        continuity_mode = "historical_after_ppia09"

    print("PPIA-09 FOUNDATION: PASS")
    print("direct_pdfs=3 direct_pdf_pages=53 direct_design_sources=4")
    print("structured_support_files=4 structured_rows=4936 keyword_hits=1570 explicit_investigation_knowledge_tree_rows=109")
    print("f011_records=10 f011_connection_types=15 f011_fixtures=24")
    print("semantic_layers=16 presentation_profiles=12 domain_handoffs=12")
    print("source_backed_findings=14 explicit_source_gaps=10 proposal_design_domains=6")
    print(f"historical_foundation_merge={FOUNDATION_MERGE}")
    print("truth_belief_separation=true permission_before_derivatives=true graph_layout_authority=false")
    print(f"continuity_mode={continuity_mode} runtime_activation=false")


if __name__ == "__main__":
    main()
