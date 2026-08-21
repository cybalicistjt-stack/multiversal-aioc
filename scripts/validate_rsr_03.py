#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "governance/source-material/recovered-legacy/now-this-2026-08-21"
RSR01 = SRC / "RSR-01_DISPOSITION_REGISTRY.json"
REG = SRC / "RSR-03_ICF_RECONCILIATION_REGISTRY.json"
QUEUE = SRC / "RSR-03_CONTENT_CANDIDATE_AND_CONFLICT_QUEUE.json"
ROUTES = SRC / "RSR-03_DOWNSTREAM_ROUTING.json"
REPORT = SRC / "RSR-03_COMPLETION_REPORT.md"
ICF_BACKLOG = ROOT / "governance/application-planning/ingredient-cultivation-foodcraft/ICF_PROGRAM_BACKLOG.json"

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    errors: list[str] = []
    for path in [RSR01, REG, QUEUE, ROUTES, REPORT, ICF_BACKLOG]:
        if not path.is_file():
            errors.append(f"missing RSR-03 dependency: {path.relative_to(ROOT)}")
    if errors:
        print("RSR-03 integrity: BLOCK")
        print("\n".join(f"- {e}" for e in errors))
        return 1

    r1 = load(RSR01)
    reg = load(REG)
    queue = load(QUEUE)
    routes = load(ROUTES)
    icf = load(ICF_BACKLOG)

    if reg.get("archive_sha256") != r1.get("archive_sha256"):
        errors.append("archive checksum drift between RSR-01 and RSR-03")
    if reg.get("source_count") != 24 or len(reg.get("sources", [])) != 24:
        errors.append("RSR-03 must cover all 24 retained MHT sources")

    r1_by_id = {x["source_id"]: x for x in r1.get("sources", [])}
    reg_by_id = {x["source_id"]: x for x in reg.get("sources", [])}
    if set(reg_by_id) != set(r1_by_id):
        errors.append("RSR-03 source IDs do not exactly cover RSR-01 source IDs")
    else:
        for sid, row in reg_by_id.items():
            src = r1_by_id[sid]
            if row.get("filename") != src.get("filename"):
                errors.append(f"filename drift for {sid}")
            if row.get("mht_sha256") != src.get("mht_sha256"):
                errors.append(f"source checksum drift for {sid}")
            if row.get("automatic_canon_promotion") is not False:
                errors.append(f"automatic canon promotion enabled for {sid}")
            if row.get("canonical_icf_mutation") is not False:
                errors.append(f"canonical ICF mutation recorded for {sid}")

    explicit = {sid for sid, src in r1_by_id.items() if "RSR-03" in src.get("routes", [])}
    marked = {sid for sid, row in reg_by_id.items() if row.get("rsr01_explicit_rsr03_route")}
    if explicit != marked:
        errors.append("original RSR-01→RSR-03 route set was not preserved exactly")
    if explicit != {"rsr01:sharra", "rsr01:kola-ha-bioengineering"}:
        errors.append("unexpected original RSR-03 route set")

    summary = reg.get("summary", {})
    supplemental = [x for x in reg.get("sources", []) if str(x.get("icf_relevance_class", "")).startswith("supplemental")]
    none_rows = [x for x in reg.get("sources", []) if x.get("icf_relevance_class") == "none"]
    if summary.get("supplemental_icf_signal_count") != len(supplemental):
        errors.append("supplemental ICF signal count mismatch")
    if summary.get("no_icf_signal_count") != len(none_rows):
        errors.append("no-ICF signal count mismatch")
    if summary.get("canonical_icf_mutation_count") != 0:
        errors.append("RSR-03 must record zero canonical ICF mutations")

    candidates = queue.get("candidates", [])
    if len(candidates) != 9:
        errors.append("expected 9 source-bound RSR-03 proposal candidates")
    for c in candidates:
        if not str(c.get("candidate_id", "")).startswith("rsr03:"):
            errors.append("candidate missing rsr03 bookkeeping prefix")
        if c.get("canonical") is not False:
            errors.append(f"candidate promoted to canonical: {c.get('candidate_id')}")
        if c.get("source_id") not in r1_by_id:
            errors.append(f"candidate source missing from RSR-01: {c.get('candidate_id')}")

    boundaries = queue.get("uncertainties_and_boundaries", [])
    if len(boundaries) != 11:
        errors.append("expected 11 explicit RSR-03 uncertainty/boundary records")
    boundary_ids = {x.get("issue_id") for x in boundaries}
    for required in [
        "rsr03:boundary:sharra-filename-content-mismatch",
        "rsr03:boundary:kola-ha-forms-not-ingredients",
        "rsr03:boundary:eldritch-yields-and-dcs",
        "rsr03:boundary:magen-mana-not-ingredient",
        "rsr03:boundary:isekai-crafting-progression",
    ]:
        if required not in boundary_ids:
            errors.append(f"required boundary missing: {required}")

    route_by_dest = {x["destination"]: x for x in routes.get("routes", [])}
    if set(route_by_dest.get("SGC", {}).get("source_ids", [])) != set(r1_by_id):
        errors.append("SGC final coverage route must include all 24 source IDs")
    if routes.get("implementation_authority_granted") is not False:
        errors.append("downstream routing must not grant successor implementation authority")

    if icf.get("status") != "completed_verified" or icf.get("completed_through") != "ICF-15":
        errors.append("completed ICF-01..15 authority is not preserved")

    report = REPORT.read_text(encoding="utf-8")
    for phrase in [
        "24 / 24 retained sources",
        "9 source-bound `rsr03:*` proposal candidates",
        "11 explicit uncertainty/ownership-boundary records",
        "0 canonical ingredient, recipe, harvest, creature, formula, facility, Asset, market or production-state mutations",
    ]:
        if phrase not in report:
            errors.append(f"completion report missing invariant: {phrase}")

    if errors:
        print("RSR-03 integrity: BLOCK")
        for e in errors:
            print(f"- {e}")
        return 1

    print("RSR-03 integrity: PASS")
    print("- all 24 retained MHT sources have an ICF relevance decision")
    print("- original 2 RSR-03 routes are preserved and 15 supplemental ICF signals are recorded")
    print("- 9 proposal candidates and 11 ownership/conflict boundaries remain noncanonical")
    print("- completed ICF-01..15 remains authoritative; no canonical ICF/live-state mutation occurred")
    print("- all 24 sources remain routed to SGC final coverage")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
