#!/usr/bin/env python3
import json, pathlib, sys
ROOT=pathlib.Path(__file__).parent
tax=json.loads((ROOT/"ICF-08_PART_EFFECT_TAXONOMY.json").read_text())
fx=json.loads((ROOT/"ICF-08_REFERENCE_FIXTURES.json").read_text())

def resolve(inp):
    if not inp["creatureEvidence"] or not inp["partEvidence"]:
        return {"ok":False,"reason":"missing-authored-creature-or-part-evidence","tendencies":[]}
    pb=tax["partBaselines"].get(inp["partBaseline"])
    if not pb:
        return {"ok":False,"reason":"unknown-part-baseline","tendencies":[]}
    terms=set(pb["tendencies"])
    layers=[f"part:{inp['partBaseline']}"]
    for p in inp.get("bodyProfiles",[]):
        prof=tax["bodyPlanTypeProfiles"].get(p)
        if not prof: return {"ok":False,"reason":"unknown-body-profile","tendencies":[]}
        terms.update(prof["tendencies"]); layers.append("body:"+p)
    for p in inp.get("traitProfiles",[]):
        prof=tax["creatureAffinityTraitProfiles"].get(p)
        if not prof: return {"ok":False,"reason":"unknown-trait-profile","tendencies":[]}
        terms.update(prof["tendencies"]); layers.append("trait:"+p)
    ov=inp.get("speciesOverride")
    if ov:
        if not ov.get("evidenceRefs"):
            return {"ok":False,"reason":"override-without-evidence","tendencies":[]}
        for t in ov.get("suppress",[]): terms.discard(t)
        for t in ov.get("add",[]):
            if t.startswith("effect:"): return {"ok":False,"reason":"exact-effect-token-forbidden","tendencies":[]}
            terms.add(t)
        layers.append("species-variant-override")
    if any(t.startswith("effect:") for t in terms):
        return {"ok":False,"reason":"exact-effect-token-forbidden","tendencies":[]}
    qmap={"ruined":("low","trace"),"poor":("low","low"),"standard":("medium","moderate"),"fine":("high","moderate"),"exceptional":("high","high")}
    smap={"contaminated":"unstable","degraded":"degraded","stable":"stable","fresh":"stable","preserved":"preserved"}
    conf,pot=qmap[inp["quality"]]; stability=smap[inp["condition"]]
    resolved=[{"tendencyRef":t,"sourceLayers":layers,"confidenceBand":conf,"potencyBand":pot,"stabilityBand":stability} for t in sorted(terms)]
    return {"ok":True,"reason":None,"tendencies":resolved,"exactEffectStatus":"unresolved-downstream-rule-content"}

errors=[]
for sc in fx["scenarios"]:
    out=resolve(sc["input"])
    if sc["expect"]=="pass":
        if not out["ok"]: errors.append(f"{sc['id']}: expected pass got {out['reason']}"); continue
        got={x["tendencyRef"] for x in out["tendencies"]}
        for t in sc.get("mustContain",[]):
            if t not in got: errors.append(f"{sc['id']}: missing {t}")
        for t in sc.get("mustNotContain",[]):
            if t=="effect:any":
                if any(x.startswith("effect:") for x in got): errors.append(f"{sc['id']}: exact effect leaked")
            elif t in got: errors.append(f"{sc['id']}: forbidden {t}")
        if out.get("exactEffectStatus")!="unresolved-downstream-rule-content": errors.append(f"{sc['id']}: exact effect status wrong")
    elif out["ok"]:
        errors.append(f"{sc['id']}: expected fail-closed")
if len(tax["partBaselines"]) < 19: errors.append("part baseline coverage too small")
if len(tax["bodyPlanTypeProfiles"]) < 20: errors.append("body/type coverage too small")
if len(tax["creatureAffinityTraitProfiles"]) < 15: errors.append("trait coverage too small")
for section in ("partBaselines","bodyPlanTypeProfiles","creatureAffinityTraitProfiles"):
    for key,obj in tax[section].items():
        for t in obj["tendencies"]:
            if not t.startswith("tendency:"): errors.append(f"{section}/{key}: non-tendency token {t}")
            if t.startswith("effect:"): errors.append(f"{section}/{key}: exact effect token")
if errors:
    print("ICF-08 VALIDATION FAIL")
    for e in errors: print(" -",e)
    sys.exit(1)
print(f"ICF-08 VALIDATION PASS: {len(tax['partBaselines'])} part baselines; {len(tax['bodyPlanTypeProfiles'])} body/type profiles; {len(tax['creatureAffinityTraitProfiles'])} trait profiles; {len(fx['scenarios'])} fixtures")
