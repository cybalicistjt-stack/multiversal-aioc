#!/usr/bin/env python3
"""Create a 125-row DWC acceptance table with unique governed row IDs and WAV filenames.

This changes only acceptance evidence identity/persistence. It does NOT change DWC text,
IPA, exact phoneme-ID sequences, styles, or the governed waveform thresholds.
"""
from __future__ import annotations
import argparse,csv,re
from pathlib import Path

def safe(s:str)->str:
    x=re.sub(r"[^A-Za-z0-9._-]+","_",s).strip("_")
    return x or "row"

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("legacy_tsv"); ap.add_argument("output_tsv"); a=ap.parse_args()
    src=Path(a.legacy_tsv); dst=Path(a.output_tsv)
    rows=list(csv.DictReader(src.open(encoding="utf-8"),delimiter="\t"))
    if len(rows)!=125: raise SystemExit(f"expected 125 rows, got {len(rows)}")
    required={"utterance_id","tier","dwc_text","english_gloss","ipa","phoneme_id_sequence","base_style","stance_overlay","audio_filename"}
    if not rows or not required.issubset(rows[0]): raise SystemExit(f"legacy table missing {sorted(required-set(rows[0] if rows else []))}")
    out=[]
    for i,r in enumerate(rows,1):
        q={
          "acceptance_row_id":f"DWCACC-{i:04d}",
          "source_utterance_id":r["utterance_id"],
          "tier":r["tier"],"dwc_text":r["dwc_text"],"english_gloss":r["english_gloss"],"ipa":r["ipa"],
          "phoneme_id_sequence":r["phoneme_id_sequence"],"base_style":r["base_style"],"stance_overlay":r["stance_overlay"],
          "legacy_audio_filename":r["audio_filename"],
          "audio_filename":f"DWCACC-{i:04d}__{safe(r['utterance_id'])}.wav",
        }
        out.append(q)
    if len({r['acceptance_row_id'] for r in out})!=125 or len({r['audio_filename'] for r in out})!=125:
        raise SystemExit("identity repair failed uniqueness check")
    dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]),delimiter="\t",lineterminator="\n");w.writeheader();w.writerows(out)
    print(f"PASS acceptance identity repair: rows=125 unique_row_ids=125 unique_audio_filenames=125 output={dst}")

if __name__=="__main__": main()
