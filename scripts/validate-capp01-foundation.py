#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
B=R/'governance/application-planning/character-appearance-production'
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
s=load(B/'CAPP-01_SOURCE_AUTHORITY_AND_PROFILE_INDEX_v0.1.0.json')
r=load(B/'CAPP-01_APPEARANCE_CHOICE_REGISTRY_v0.1.0.json')
c=load(B/'CAPP-01_CONSTRAINT_MODEL_v0.1.0.json')
expected=['Antyrri','Brambleborn','Caligan','Cesidian','Cosmenella','Crystal Dragon','Feline','Ganymede','Gliesian','Human','Iaoth','Kobold','Logical Stage','Malaphant','ManyToms','Munyubbles','Nekron','Raconite','Ramogliese','Regalian','The Great Race','Thetans','Vortex Cat','Whimsbug','Wogol']
cats={'scale.relative_size','body_shape.silhouette','symmetry.laterality','locomotion.appendages','texture.covering','coloration.marking','head_face.structure','hair_crest_spine','evolutionary_residue','age_bearing_posture','gender_manifestation','adornment','presentation_wardrobe','equipment_state'}
def req(x,m):
 if not x: raise SystemExit('CAPP-01 foundation FAILED: '+m)
req(s['profile_count']==25 and [p['display_name'] for p in s['profiles']]==expected,'25-profile source order')
req(r['profile_count']==25 and r['category_count']==14,'registry counts')
req({x['category_id'] for x in r['categories']}==cats,'category IDs')
req([p['display_name'] for p in r['profiles']]==expected,'registry profile order')
by={p['display_name']:p for p in r['profiles']}
for n in ['Munyubbles','Wogol']:
 req(by[n]['authority_status']=='unknown_morphology' and by[n]['default_dimension_policy']=='unknown_preserved',n+' unknown preservation')
req(by['Thetans']['default_dimension_policy']=='delegated_not_species_owned','Thetan body delegation')
req(set(c['eligibility_domain'])=={'true','false','conditional','unknown'},'eligibility domain')
req({x['id'] for x in c['constraint_classes']}=={'topology','species','form','phase','dependency','exclusion','cardinality','permission'},'constraint classes')
req(c['unknown_and_failure_semantics']['no_silent_substitution'] is True,'silent substitution guard')
req(c['unknown_and_failure_semantics']['identity_validity_independent_of_renderer_support'] is True,'renderer independence')
source=json.dumps(load(R/'governance/application-planning/parallel-preimplementation/PPIA-06_SPECIES_MORPHOLOGY_PROFILES_v0.1.0.json'),ensure_ascii=False)
for n in expected: req(n in source,n+' missing from PPIA-06 authority')
print('CAPP-01 foundation validation: PASS; profiles=25 categories=14 classes=8')
