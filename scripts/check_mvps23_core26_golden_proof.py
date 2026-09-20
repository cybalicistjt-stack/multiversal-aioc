#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"governance/application-planning/player-species"

def j(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

std=j(BASE/"CORE_26_GAME_READY_STANDARD_v1.0.0.json")
m22=j(BASE/"MVPS-22_CORE26_CERTIFICATION_MATRIX_v1.0.0.json")
g=j(BASE/"MVPS-23_CORE26_GAME_READY_GOLDEN_PROOF_v1.0.0.json")

assert g["standard_ref"]==std["standard_id"]=="CORE26.GAME_READY.v1"
assert g["exact_core26_authority_order"]==std["applies_to"]
assert [x["species"] for x in m22["species"]]==std["applies_to"]
assert [x["species"] for x in g["species"]]==std["applies_to"]
assert g["species_count"]==26 and g["dimension_count"]==19
assert g["game_ready_certified_count"]==26
assert g["unresolved_mandatory_gap_count"]==0
assert g["waived_mandatory_dimension_count"]==0
assert g["application_branch_audit"]["species_name_application_branch_count"]==0

dims=[d["id"] for d in std["dimensions"]]
mby={x["species"]:x for x in m22["species"]}

for row in g["species"]:
    species=row["species"]
    src=mby[species]
    slug=row["slug"]
    dp=ROOT/f"content-source/core26-species/{slug}/definition-v1.2.0.json"
    rp=ROOT/f"content-source/core26-species/{slug}/register-v1.2.0.json"
    assert dp.is_file(), dp
    assert rp.is_file(), rp
    d=j(dp)["records"][0]
    r=j(rp)["records"][0]
    assert d["contentVersion"]=="1.2.0"
    assert d["gameObject"]["id"]==row["stable_id"]==src["stable_id"]
    assert r["contentVersion"]=="1.2.0"
    assert row["definition_version"]=="1.2.0"
    assert row["register_version"]=="1.2.0"
    assert row["result"]=="game_ready_certified"
    assert row["source_traceable"] is True
    assert row["unresolved_mandatory_gaps"]==[]
    assert list(row["dimension_replay"])==dims
    for dim in dims:
        replay=row["dimension_replay"][dim]
        certified=src["dimensions"][dim]
        assert replay["result"]=="pass"
        assert replay["certification_state"]==certified["state"]
        assert replay["evidence_refs"]==certified["evidence_refs"]
        assert replay["evidence_refs"]
        assert certified["state"] in {"certified","explicit_not_applicable"}

print("MVPS-23 Core-26 terminal golden replay: OK")
