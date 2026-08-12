from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "governance" / "application-planning" / "parallel-preimplementation"
WORK = ROOT / "governance" / "ai" / "work-state" / "PPIA-13-attempt-001.json"
BACKLOG = P / "PPIA_PROGRAM_BACKLOG.json"

MANIFEST = P / "PPIA-13_GM_ACADEMY_SOURCE_MANIFEST_v0.1.0.json"
CURRICULUM = P / "PPIA-13_GM_ACADEMY_CURRICULUM_AND_MULTIVERSAL_MAP_v0.1.0.json"
CASES = P / "PPIA-13_GM_ACADEMY_REFERENCE_CASES_v0.1.0.json"
INVENTORY = P / "PPIA-13_GM_ACADEMY_SOURCE_AND_CURRICULUM_INVENTORY.md"

EXPECTED_HASHES = {
    "Academy index.PDF": "9b8a55023c404442613d5933d760b16c8064a9fce14f51475465b62ef47d4976",
    "GM Academy 1.PDF": "2063cc0c1dbb69c11e32d4b1d109621ae872eebca8b87c2b8bc24c2a994cbbeb",
    "INTERMEDIATE GAME MASTERING.PDF": "cf49e0e713ad4fe63ebccc42cc47d6dc7bf3230f94625141da38d1bd6075ef98",
    "ADVANCED GAME MASTERING.PDF": "07faac0edc9206d26d561e18d5876e146ed53a3c51694aa5c1cfdf0a2f641711",
    "Worldbuilding.PDF": "9b9b8cfdfc9fb9358e151bd4753396ff75f7a5f6fd00927557d262787665174d",
    "World Creation tables.PDF": "ccd901fde30b37547e988d2db6fa9286c631330cbbba0fb14d284e334535cab8",
}
P13_FINAL_HEAD = "81e5c75effa1d4f8a8215493ef84b57108e20fae"
P13_FINAL_MERGE = "cbfb6b931b11326afd5b826ad2a500e9b6d2d9c9"

def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    manifest=load(MANIFEST); curriculum=load(CURRICULUM); cases=load(CASES); checkpoint=load(WORK); backlog=load(BACKLOG); inventory=INVENTORY.read_text(encoding="utf-8")
    assert manifest["work_item_id"] == curriculum["work_item_id"] == cases["work_item_id"] == "PPIA-13"
    assert len(manifest["sources"]) == 6
    assert {s["filename"]: s["sha256"] for s in manifest["sources"]} == EXPECTED_HASHES
    assert manifest["curriculum_status"]["multiversal_gming_and_system_mastery"] == "outline_only_in_academy_index"
    assert "do not override canonical Multiversal rules" in manifest["source_authority_rule"]
    assert "noncanonical prompts" in manifest["world_creation_tables_rule"]
    tracks=curriculum["tracks"]
    assert len(tracks)==5 and [len(t["topics"]) for t in tracks]==[9,8,8,10,18]
    assert curriculum["locked_counts"]=={"tracks":5,"total_modules":53,"developed_source_modules":35,"outline_only_multiversal_modules":18,"initial_curated_source_backed_modules":24}
    assert sum(len(t["initial_curated_topics"]) for t in tracks[:4])==24
    assert tracks[4]["source_status"]=="outline_only" and tracks[4]["initial_curated_topics"]==[]
    required={"Multiversal System Mastery","Advanced Multiversal Combat Design","Handling Inter-Reality Travel & Causal Complexity","Mastering Faction Play in Multiversal","Running Multiversal Warfare and Strategic Play","Creating a Living Multiversal Setting"}
    assert required.issubset(set(tracks[4]["topics"]))
    assert curriculum["delivery_model"]["course_progress"]=="optional and never a permission/capability gate"
    assert curriculum["world_creation_tables_policy"]["canonical_promotion"] is False
    grounding=json.dumps(curriculum["canonical_grounding"])
    for term in ("PPIA-07","PPIA-08","PPIA-09","PPIA-11","MV-IA-F025","MV-IA-F006"): assert term in grounding
    assert cases["case_count"]==len(cases["cases"])==20
    names={c["name"] for c in cases["cases"]}
    for name in ("source-precedence","outline-gap","worldbuilding-draft","nonhuman-culture","combat-design","ai-automation","accessibility","f024-gap","progress-not-gate","multiversal-grounding"): assert name in names
    for term in ("53 top-level modules","24 source-backed modules","outline-only","World Creation tables.PDF","PPIA-14","F024 Pack source gap","No application runtime","Teaching Library / Inspector-Action-Reference Contracts"): assert term.lower() in inventory.lower(), f"inventory missing {term!r}"
    assert checkpoint["work_item_id"]=="PPIA-13" and checkpoint["owner_decision_required"] is False and checkpoint["unresolved_failures"]==[]
    if backlog["current_work_item_id"]=="PPIA-13":
        assert checkpoint["status"] in {"started","ready_for_review"}
        mode="current"
    else:
        assert checkpoint["status"]=="completed_verified" and checkpoint["active_substep"] is None
        assert checkpoint["latest_pushed_commit"]==P13_FINAL_HEAD and checkpoint["merge_commit"]==P13_FINAL_MERGE and checkpoint["pull_request"]==279
        mode="historical"
    assert "No application runtime activation" in " ".join(checkpoint.get("notes", []))
    print("PPIA-13 GM ACADEMY CURRICULUM EXTRACTION: PASS")
    print("sources=6 tracks=5 modules=53 developed=35 outline_only_multiversal=18 curated=24 cases=20")
    print("continuity_mode="+mode)
    return 0

if __name__ == "__main__": raise SystemExit(main())
