#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "governance/application-planning/parallel-preimplementation"
GRAMMAR = BASE / "PPIA-07_DETERMINISTIC_GRAMMAR_CANDIDATE_v0.1.0.json"
CORPUS = BASE / "PPIA-07_RUNE_REFERENCE_CORPUS_v0.1.0.json"
NOTE = BASE / "PPIA-07_GRAMMAR_AND_REFERENCE_CANDIDATE.md"
FOUNDATION = BASE / "PPIA-07_SOURCE_AND_DESIGN_INVENTORY.md"
TAXONOMY = BASE / "PPIA-07_RUNE_COMPOSITION_TAXONOMY_v0.1.0.json"
CP = ROOT / "governance/ai/work-state/PPIA-07-attempt-001.json"
PTR = ROOT / "governance/ai/runtime/CURRENT_WORK_POINTER.json"
STATUS = ROOT / "governance/ai/runtime/CURRENT_IMPLEMENTATION_STATUS.json"
FOUNDATION_MERGE = "183d199d69f5cce121d4b971f33fe6c0145a6c45"


def fail(message: str) -> None:
    raise SystemExit(f"PPIA-07 GRAMMAR/REFERENCE: FAIL — {message}")


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
        if ch == "[": bracket += 1
        elif ch == "]": bracket -= 1
        elif bracket == 0:
            if ch == "(": paren += 1
            elif ch == ")":
                paren -= 1
                if paren == 0 and i != len(expr) - 1:
                    return expr
    return expr[1:-1]


def top_level_connectors(expr: str) -> list[tuple[int, str]]:
    paren = bracket = 0
    out: list[tuple[int, str]] = []
    for i, ch in enumerate(expr):
        if ch == "[": bracket += 1
        elif ch == "]": bracket -= 1
        elif bracket == 0:
            if ch == "(": paren += 1
            elif ch == ")": paren -= 1
            elif paren == 0 and ch in ">&@?": out.append((i, ch))
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
    positions = [i for i, _ in connectors]
    parts: list[str] = []
    start = 0
    for pos in positions:
        parts.append(expr[start:pos])
        start = pos + 1
    parts.append(expr[start:])
    require(all(parts), "connector requires complete left and right expression")
    return {"type": "chain", "connector": token, "children": [parse_expr(p, atom_map, slot_ids) for p in parts]}


def canonical(ast: dict) -> str:
    if ast["type"] == "atom":
        slots = ast["slots"]
        inside = ",".join(f"{k}={slots[k]}" for k in sorted(slots))
        return f"{ast['id']}[{inside}]"
    if ast["type"] == "group":
        return f"({canonical(ast['child'])})"
    token = ast["connector"]
    return token.join(canonical(child) for child in ast["children"])


def main() -> None:
    grammar = load(GRAMMAR)
    corpus = load(CORPUS)
    taxonomy = load(TAXONOMY)
    cp = load(CP)
    ptr = load(PTR)
    status = load(STATUS)
    note = NOTE.read_text(encoding="utf-8")
    foundation = FOUNDATION.read_text(encoding="utf-8")

    require(grammar["work_item_id"] == "PPIA-07", "grammar work item mismatch")
    atoms = grammar["atom_vocabulary"]
    connectors = grammar["connection_types"]
    require([a["id"] for a in atoms] == ["SOURCE","MOVE","SHAPE","BIND","CHANGE","SENSE","WARD","LINK"], "atom vocabulary mismatch")
    require(len(atoms) == 8 and len({a["id"] for a in atoms}) == 8, "expected eight unique atoms")
    require([(c["id"], c["token"]) for c in connectors] == [("THEN",">"),("WITH","&"),("WHEN","@"),("IF","?")], "connection set mismatch")
    require(len(grammar["validity_rules"]) == 12, "expected twelve validity rules")
    require(grammar["design_goals"]["no_implicit_operator_precedence"] is True, "no-implicit-precedence goal missing")
    require(grammar["complexity_guidance"]["effect"] == "warning_and_explainability_prompt_only", "complexity guidance must not be a hard balance cap")
    for key in ("final_atom_vocabulary_locked","final_cost_formula_defined","final_balance_defined","all_spells_convertible","all_payloads_universal","visual_graph_required","source_specific_progression_prices_promoted"):
        require(grammar["non_assumptions"][key] is False, f"non-assumption must remain false: {key}")

    slot_ids = {s["id"] for s in grammar["general_modifier_slots"]}
    require({"payload","target","geometry","direction","condition","trigger","channel","anchor","to"} <= slot_ids, "modifier slots incomplete")
    atom_map = {a["id"]: a for a in atoms}

    cases = corpus["cases"]
    require(len(cases) == 20, "expected 20 bounded reference cases")
    require([c["case_id"] for c in cases] == [f"PPIA07-RC-{i:03d}" for i in range(1,21)], "reference IDs must be contiguous")
    require(all(c.get("acceptance") for c in cases), "every reference case needs acceptance criteria")

    seen_atoms: set[str] = set()
    seen_connectors: set[str] = set()
    token_to_id = {c["token"]: c["id"] for c in connectors}
    for case in cases:
        expected = case["expected"]
        should_parse = not expected.startswith("invalid")
        try:
            ast = parse_expr(case["expression"], atom_map, slot_ids)
            parsed = True
            canon = canonical(ast)
            ast2 = parse_expr(canon, atom_map, slot_ids)
            require(canonical(ast2) == canon, f"round-trip instability in {case['case_id']}")
            text = json.dumps(ast)
            for atom_id in atom_map:
                if f'"id": "{atom_id}"' in text: seen_atoms.add(atom_id)
            for token, connector_id in token_to_id.items():
                if f'"connector": "{token}"' in text: seen_connectors.add(connector_id)
        except SystemExit:
            parsed = False
        require(parsed == should_parse, f"parse expectation mismatch for {case['case_id']}: expected {expected}")

    require(seen_atoms == set(corpus["coverage_requirements"]["all_atoms"]), "reference corpus does not exercise every atom")
    require(seen_connectors == set(corpus["coverage_requirements"]["all_connections"]), "reference corpus does not exercise every connector")
    policy = corpus["policy"]
    require(all(value is False for value in policy.values()), "all corpus guardrail policy booleans must remain false")

    require(len(taxonomy["identity_state_layers"]) == 15, "foundation taxonomy lost 15 layers")
    for phrase in ("9 PDFs / 170 pages", "Four retained CSVs", "2,225 rows", "3 explicit rune records", "16 records sourced from Scripts and Macros"):
        require(phrase in foundation, f"foundation inventory missing {phrase!r}")
    for phrase in ("functional atom vocabulary", "no implicit precedence", "20 bounded cases", "cost/balance"):
        require(phrase.lower() in note.lower(), f"candidate note missing {phrase!r}")

    require(cp["work_item_id"] == "PPIA-07" and cp["attempt_id"] == "PPIA-07-attempt-001", "checkpoint identity mismatch")
    require(cp["base_commit"] == "a7803f8438a837b741f78c875d7ec2e915d37a19", "PPIA-07 base transition merge mismatch")
    require(any(FOUNDATION_MERGE in e.get("value", "") for e in cp.get("evidence", [])), "checkpoint must preserve verified foundation merge")
    require(not cp["unresolved_failures"] and cp["owner_decision_required"] is False, "checkpoint unresolved state")
    if cp["status"] in {"started","in_progress"}:
        selected = [x for x in ptr["active_attempts"] if x.get("owner_selected")]
        require(len(selected) == 1 and selected[0]["work_item_id"] == "PPIA-07", "active PPIA-07 must be owner-selected")
        require(ptr["primary_attempt_id"] == "PPIA-07-attempt-001", "primary attempt mismatch")
        require(status["primary"]["work_item_id"] == "PPIA-07" and status["primary"]["status"] == cp["status"], "compact status mismatch")
    else:
        require(cp["status"] == "completed_verified", "unexpected historical PPIA-07 status")

    print("PPIA-07 GRAMMAR/REFERENCE: PASS")
    print("atoms=8")
    print("connections=4")
    print("validity_rules=12")
    print("reference_cases=20")
    print("implicit_precedence=false")
    print("cost_formula_final=false")
    print("balance_final=false")


if __name__ == "__main__":
    main()
