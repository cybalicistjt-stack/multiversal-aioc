#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
CONTRACT = BASE / "PPIA-07_COST_COMPLEXITY_STABILITY_PROGRESSION_CONTRACT_v0.1.0.json"
BENCH = BASE / "PPIA-07_COST_STABILITY_PROGRESSION_BENCHMARKS_v0.1.0.json"
NOTE = BASE / "PPIA-07_COST_STABILITY_PROGRESSION_CANDIDATE.md"
GRAMMAR = BASE / "PPIA-07_DETERMINISTIC_GRAMMAR_CANDIDATE_v0.1.0.json"
CORPUS = BASE / "PPIA-07_RUNE_REFERENCE_CORPUS_v0.1.0.json"
AUTH = BASE / "PPIA-07_AUTHORITY_AND_BOUNDARY_MATRIX_v0.1.0.json"
CP = ROOT / "governance/ai/work-state/PPIA-07-attempt-001.json"
PTR = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
FOUNDATION_MERGE = "183d199d69f5cce121d4b971f33fe6c0145a6c45"
GRAMMAR_MERGE = "15202626a0ba96d7675ee4ab4cbec4923158cd63"
P12_COMPLETION_MERGE = "0ed9f9a0c53b2a132d8f38c0d3cae22cc7ae14a0"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-07 COST/STABILITY/PROGRESSION: FAIL — {message}")


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def load(path: Path) -> dict:
    require(path.exists(), f"missing {path.relative_to(ROOT)}")
    return json.loads(path.read_text(encoding="utf-8"))


def strip_outer_group(expr: str) -> str:
    if not (expr.startswith("(") and expr.endswith(")")):
        return expr
    paren = bracket = 0
    for i, ch in enumerate(expr):
        if ch == "[":
            bracket += 1
        elif ch == "]":
            bracket -= 1
        elif bracket == 0:
            if ch == "(":
                paren += 1
            elif ch == ")":
                paren -= 1
                if paren == 0 and i != len(expr) - 1:
                    return expr
    return expr[1:-1]


def top_level_connectors(expr: str) -> list[tuple[int, str]]:
    paren = bracket = 0
    out: list[tuple[int, str]] = []
    for i, ch in enumerate(expr):
        if ch == "[":
            bracket += 1
        elif ch == "]":
            bracket -= 1
        elif bracket == 0:
            if ch == "(":
                paren += 1
            elif ch == ")":
                paren -= 1
            elif paren == 0 and ch in ">&@?":
                out.append((i, ch))
        require(paren >= 0 and bracket >= 0, "unbalanced expression delimiter")
    require(paren == 0 and bracket == 0, "unbalanced expression delimiter")
    return out


def parse_atom(expr: str, atom_map: dict[str, dict], slot_ids: set[str]) -> dict:
    m = re.fullmatch(r"([A-Z]+)\[(.*)\]", expr)
    require(m is not None, f"invalid atom form {expr!r}")
    atom_id, raw = m.group(1), m.group(2)
    require(atom_id in atom_map, f"unknown atom {atom_id}")
    pairs: list[tuple[str, str]] = []
    if raw:
        for item in raw.split(","):
            require("=" in item, f"bad modifier {item!r}")
            key, value = item.split("=", 1)
            require(key and value, f"empty modifier key/value in {expr!r}")
            pairs.append((key, value))
    keys = [k for k, _ in pairs]
    require(len(keys) == len(set(keys)), f"duplicate modifier key in {expr!r}")
    require(set(keys) <= slot_ids, f"unknown modifier key in {expr!r}")
    require(set(atom_map[atom_id]["required_slots"]) <= set(keys), f"missing required slot for {atom_id}")
    return {"type": "atom", "id": atom_id, "slots": dict(pairs)}


def parse_expr(expr: str, atom_map: dict[str, dict], slot_ids: set[str]) -> dict:
    expr = "".join(expr.split())
    require(expr, "empty expression")
    stripped = strip_outer_group(expr)
    if stripped != expr:
        return {"type": "group", "child": parse_expr(stripped, atom_map, slot_ids)}
    connectors = top_level_connectors(expr)
    if not connectors:
        return parse_atom(expr, atom_map, slot_ids)
    kinds = {token for _, token in connectors}
    require(len(kinds) == 1, "mixed connector types require explicit grouping")
    token = next(iter(kinds))
    parts: list[str] = []
    start = 0
    for pos, _ in connectors:
        parts.append(expr[start:pos])
        start = pos + 1
    parts.append(expr[start:])
    require(all(parts), "connector requires complete left and right expression")
    return {"type": "chain", "connector": token, "children": [parse_expr(p, atom_map, slot_ids) for p in parts]}


def compute_metrics(ast: dict, execution_context: str, atom_map: dict[str, dict]) -> dict:
    atoms: list[dict] = []
    connectors: list[str] = []
    max_group_depth = 0

    def walk(node: dict, group_depth: int = 0) -> None:
        nonlocal max_group_depth
        if node["type"] == "atom":
            atoms.append(node)
        elif node["type"] == "group":
            max_group_depth = max(max_group_depth, group_depth + 1)
            walk(node["child"], group_depth + 1)
        else:
            connectors.extend([node["connector"]] * (len(node["children"]) - 1))
            for child in node["children"]:
                walk(child, group_depth)

    walk(ast)
    connector_weights = {">": 1, "&": 2, "@": 2, "?": 2}
    optional_modifiers = sum(len(set(atom["slots"]) - set(atom_map[atom["id"]]["required_slots"])) for atom in atoms)
    sci = len(atoms) + sum(connector_weights[c] for c in connectors) + max(0, max_group_depth - 1) * 2 + math.ceil(optional_modifiers / 2)
    sci_band = "simple" if sci <= 3 else "standard" if sci <= 6 else "advanced" if sci <= 10 else "expert"

    payloads = {atom["slots"]["payload"] for atom in atoms if "payload" in atom["slots"]}
    link_count = sum(atom["id"] == "LINK" for atom in atoms)
    csl = (
        connectors.count("&")
        + connectors.count("@")
        + connectors.count("?")
        + max(0, link_count - 1)
        + max(0, len(payloads) - 1)
        + max(0, max_group_depth - 2)
        + (1 if execution_context == "prepared-macro" else 0)
    )
    csl_band = "baseline" if csl == 0 else "watch" if csl <= 2 else "strained" if csl <= 4 else "high-attention"

    band = {"simple": 0, "standard": 1, "advanced": 2, "expert": 3}[sci_band]
    if "@" in connectors or "?" in connectors:
        band = max(band, 2)
    if execution_context == "prepared-macro":
        band = max(band, 2)
    if link_count >= 2:
        band = max(band, 3)

    return {
        "SCI": sci,
        "SCI_band": sci_band,
        "CSL": csl,
        "CSL_band": csl_band,
        "recommended_band": band,
    }


def main() -> None:
    contract = load(CONTRACT)
    bench = load(BENCH)
    grammar = load(GRAMMAR)
    corpus = load(CORPUS)
    auth = load(AUTH)
    cp = load(CP)
    ptr = load(PTR)
    status = load(STATUS)
    note = NOTE.read_text(encoding="utf-8")

    require(contract["work_item_id"] == "PPIA-07", "contract work item mismatch")
    require(contract["status"] == "design_candidate_not_final_balance", "contract status mismatch")
    require(contract["verified_inputs"]["foundation_merge"] == FOUNDATION_MERGE, "foundation merge mismatch")
    require(contract["verified_inputs"]["grammar_reference_merge"] == GRAMMAR_MERGE, "grammar merge mismatch")
    require(contract["structural_complexity"]["formula"].startswith("SCI ="), "SCI formula missing")
    require(contract["composition_stability"]["formula"].startswith("CSL ="), "CSL formula missing")
    require([b["id"] for b in contract["structural_complexity"]["bands"]] == ["simple","standard","advanced","expert"], "SCI bands mismatch")
    require([b["id"] for b in contract["composition_stability"]["bands"]] == ["baseline","watch","strained","high-attention"], "CSL bands mismatch")
    require(len(contract["resource_adapter_contract"]["adapter_keys"]) == 12, "expected twelve typed resource adapters")
    require(set(contract["resource_adapter_contract"]["execution_profiles"]) == {"cast","ritual","inscribed","item-bound","prepared-macro"}, "execution profile set mismatch")
    require(len(contract["counterplay_hooks"]) == 6, "expected six counterplay hooks")
    require(len(contract["progression_contract"]["bands"]) == 4, "expected four progression bands")
    require(contract["progression_contract"]["source_specific_xp_prices_promoted"] is False, "source XP prices must not be promoted")
    require(contract["progression_contract"]["scripts_macros_progression_conflict_silently_resolved"] is False, "progression conflict must remain explicit")
    require(contract["composition_stability"]["automatic_failure_chance"] is False, "CSL must not become failure probability")
    require(contract["composition_stability"]["automatic_damage_or_backlash"] is False, "CSL must not invent backlash")
    require(all(value is False for key, value in contract["axis_separation"].items() if key != "final_balance_owner"), "axis separation booleans must remain false")
    require(contract["axis_separation"]["final_balance_owner"] == "PPIA-11", "PPIA-11 final balance boundary missing")
    require(all(value is False for value in contract["non_assumptions"].values()), "final-form non-assumptions must remain false")

    require(grammar["status"] == "design_candidate_not_final_balance", "verified grammar status changed unexpectedly")
    atom_map = {a["id"]: a for a in grammar["atom_vocabulary"]}
    slot_ids = {s["id"] for s in grammar["general_modifier_slots"]}
    require(len(atom_map) == 8 and len(grammar["connection_types"]) == 4, "verified grammar cardinality changed")
    require(len(corpus["cases"]) == 20, "verified grammar corpus must remain twenty cases")
    require(len(auth["authority_levels"]) == 4, "authority level contract changed")

    cases = bench["cases"]
    require(len(cases) == 16, "expected sixteen cost/stability/progression benchmarks")
    require([c["case_id"] for c in cases] == [f"PPIA07-CSP-{i:03d}" for i in range(1,17)], "benchmark IDs must be contiguous")
    metric_cases = [c for c in cases if "expected" in c]
    require(len(metric_cases) == 9, "expected nine deterministic metric cases")
    for case in metric_cases:
        ast = parse_expr(case["expression"], atom_map, slot_ids)
        actual = compute_metrics(ast, case["execution_context"], atom_map)
        require(actual == case["expected"], f"metric mismatch for {case['case_id']}: {actual} != {case['expected']}")

    guardrails = {c["case_id"]: c for c in cases if "expected_behavior" in c}
    require(len(guardrails) == 7, "expected seven adapter/guardrail cases")
    require(guardrails["PPIA07-CSP-010"]["expected_behavior"] == "authoritative_execution_blocked_without_default", "unresolved adapter guardrail mismatch")
    require(guardrails["PPIA07-CSP-011"]["expected_behavior"] == "preserve_external_value_without_repricing", "external value preservation mismatch")
    require("counter" in guardrails["PPIA07-CSP-012"]["expected_behavior"], "counterplay guardrail missing")
    require("XP" in guardrails["PPIA07-CSP-013"]["expected_behavior"], "progression conflict guardrail missing")
    require("filter" in guardrails["PPIA07-CSP-014"]["expected_behavior"], "permission guardrail missing")
    require("operation" in guardrails["PPIA07-CSP-015"]["expected_behavior"], "recovery guardrail missing")
    try:
        parse_expr(guardrails["PPIA07-CSP-016"]["expression"], atom_map, slot_ids)
        fail("invalid mixed-connector benchmark parsed unexpectedly")
    except SystemExit as exc:
        if not str(exc).startswith("PPIA-07 COST/STABILITY/PROGRESSION: FAIL — mixed connector types"):
            raise

    require(all(value is False for value in bench["policy"].values()), "benchmark guardrail policy booleans must remain false")
    require(bench["coverage"]["SCI_bands"] == ["simple","standard","advanced","expert"], "benchmark SCI coverage mismatch")
    require(bench["coverage"]["progression_bands_exercised"] == [0,1,2,3], "progression coverage mismatch")

    for phrase in ("Four separate axes", "Structural Complexity Index", "typed resource", "Composition Stability Load", "Band 3", "16 cases", "PPIA-11"):
        require(phrase.lower() in note.lower(), f"candidate note missing {phrase!r}")

    require(cp["work_item_id"] == "PPIA-07" and cp["attempt_id"] == "PPIA-07-attempt-001", "checkpoint identity mismatch")
    require(any(FOUNDATION_MERGE in e.get("value", "") for e in cp.get("evidence", [])), "checkpoint lost foundation merge evidence")
    require(any(GRAMMAR_MERGE in e.get("value", "") for e in cp.get("evidence", [])), "checkpoint lost grammar/reference merge evidence")
    require(any(P12_COMPLETION_MERGE in e.get("value", "") for e in cp.get("evidence", [])), "checkpoint lost PPIA-12 completion evidence")
    require(not cp["unresolved_failures"] and cp["owner_decision_required"] is False, "checkpoint unresolved state")
    if cp["status"] in {"started", "in_progress"}:
        selected = [x for x in ptr["active_attempts"] if x.get("owner_selected")]
        require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-07", "active PPIA-07 must be owner-selected")
        require(ptr["primary_attempt_id"] == "PPIA-07-attempt-001", "primary attempt mismatch")
        require(status["primary"]["work_item_id"] == "PPIA-07" and status["primary"]["status"] == cp["status"], "compact status mismatch")
    else:
        require(cp["status"] == "completed_verified", "unexpected historical PPIA-07 status")

    print("PPIA-07 COST/STABILITY/PROGRESSION: PASS")
    print("SCI_bands=4")
    print("CSL_bands=4")
    print("resource_adapters=12")
    print("progression_bands=4")
    print("counterplay_hooks=6")
    print("benchmarks=16")
    print("final_balance_owner=PPIA-11")
    print("universal_cost_formula=false")
    print("automatic_failure_probability=false")


if __name__ == "__main__":
    main()
