#!/usr/bin/env python3
"""Compile parsed candidates plus existing canon into a provenance-backed knowledge graph."""
from __future__ import annotations
import argparse, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

def load_jsonl(p): return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def stable(*p): return hashlib.sha256('\n'.join(p).encode('utf-8','ignore')).hexdigest()[:20]
def norm(s): return re.sub(r"[^a-z0-9]+"," ",str(s or '').lower()).strip()
def aliases(name):
    raw=str(name or '').strip(); values={norm(raw)}
    values.add(norm(re.sub(r'^\d+(?:\.\d+)*[.)]?\s*','',raw)))
    values.add(norm(re.sub(r'\s*\([^)]*\)\s*$','',raw)))
    values.add(norm(re.sub(r'\s*[:—-]\s*.*$','',raw)))
    return {x for x in values if len(x)>=3}
def canonical_rows(path):
    if not path or not path.exists(): return []
    p=json.loads(path.read_text(encoding='utf-8')); return p.get('records',p if isinstance(p,list) else [])
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--parsed',type=Path,required=True);ap.add_argument('--canonical',type=Path);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    parsed=load_jsonl(a.parsed/'family-parser-candidates.jsonl'); canon=canonical_rows(a.canonical)
    nodes=[]; name_index=defaultdict(list)
    def add_node(n):
        nodes.append(n)
        for key in aliases(n['name']): name_index[key].append(n)
    for r in canon:
        nid=str(r.get('id') or r.get('stableId') or 'canonical-'+stable(json.dumps(r,sort_keys=True)))
        add_node({'nodeId':nid,'nodeType':r.get('objectType') or r.get('type') or 'unknown','name':r.get('name') or r.get('title') or nid,'authority':'canonical','status':r.get('status','active'),'provenance':r.get('provenance') or []})
    for c in parsed:
        add_node({'nodeId':c['candidateId'],'nodeType':c['objectType'],'name':c['name'],'authority':'candidate','status':c['status'],'provenance':c['provenance'],'readinessScore':c['readinessScore'],'spec':c['spec']})
    edges=[]; unresolved=[]
    searchable=[(key,rows) for key,rows in name_index.items()]
    for c in parsed:
        for rel in c.get('relationships') or []:
            key=norm(rel.get('targetName')); matches=name_index.get(key,[]); method='exact-alias'; confidence=rel.get('confidence',50)
            if not matches and len(key)>=5:
                ranked=[]
                for candidate_key,candidate_rows in searchable:
                    ratio=SequenceMatcher(None,key,candidate_key).ratio()
                    if ratio>=0.88 or (key in candidate_key and len(key)/max(1,len(candidate_key))>=0.72) or (candidate_key in key and len(candidate_key)/max(1,len(key))>=0.72):
                        ranked.append((ratio,candidate_rows))
                ranked.sort(key=lambda x:-x[0])
                if ranked and (len(ranked)==1 or ranked[0][0]-ranked[1][0]>=0.06):
                    matches=ranked[0][1];method='fuzzy-alias';confidence=min(confidence,round(ranked[0][0]*100))
            eid='edge-'+stable(c['candidateId'],rel.get('type','references'),key)
            unique={m['nodeId']:m for m in matches if m['nodeId']!=c['candidateId']}
            matches=list(unique.values())
            if len(matches)==1:
                edges.append({'edgeId':eid,'sourceId':c['candidateId'],'targetId':matches[0]['nodeId'],'relationshipType':rel.get('type','references'),'confidence':confidence,'resolutionMethod':method,'state':'resolved','provenance':c['provenance']})
            else:
                unresolved.append({'edgeId':eid,'sourceId':c['candidateId'],'sourceName':c['name'],'targetText':rel.get('targetName'),'relationshipType':rel.get('type','references'),'candidateTargetIds':[m['nodeId'] for m in matches[:10]],'state':'ambiguous' if matches else 'unresolved','provenance':c['provenance']})
    evidence_nodes={}
    for c in parsed:
        for p in c.get('provenance') or []:
            ev='evidence-'+stable(str(p.get('sourcePath')),str(p.get('locator')),str(p.get('findingId')))
            if ev not in evidence_nodes:
                evidence_nodes[ev]={'nodeId':ev,'nodeType':'source-evidence','name':f"{p.get('sourcePath')} {p.get('locator')}",'authority':'evidence','status':'active','provenance':[p]}
            edges.append({'edgeId':'edge-'+stable(c['candidateId'],'supportedBy',ev),'sourceId':c['candidateId'],'targetId':ev,'relationshipType':'supportedBy','confidence':100,'resolutionMethod':'provenance','state':'resolved','provenance':[p]})
    nodes.extend(evidence_nodes.values())
    degree=Counter()
    for e in edges:degree[e['sourceId']]+=1;degree[e['targetId']]+=1
    graph={'format':'multiversal-canonical-knowledge-graph','version':'1.1.0','generatedAt':datetime.now(timezone.utc).isoformat(),'nodes':nodes,'edges':edges,'unresolvedEdges':unresolved}
    (a.out/'canonical-knowledge-graph.json').write_text(json.dumps(graph,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    semantic=[e for e in edges if e['relationshipType']!='supportedBy']
    summary={'format':'multiversal-knowledge-graph-index','version':'1.1.0','generatedAt':graph['generatedAt'],'nodeCount':len(nodes),'edgeCount':len(edges),'resolvedRelationshipCount':len(semantic),'exactAliasRelationshipCount':sum(e.get('resolutionMethod')=='exact-alias' for e in semantic),'fuzzyAliasRelationshipCount':sum(e.get('resolutionMethod')=='fuzzy-alias' for e in semantic),'evidenceEdgeCount':sum(e['relationshipType']=='supportedBy' for e in edges),'unresolvedRelationshipCount':len(unresolved),'nodeTypeCounts':dict(Counter(n['nodeType'] for n in nodes)),'authorityCounts':dict(Counter(n['authority'] for n in nodes)),'isolatedNodeCount':sum(degree[n['nodeId']]==0 for n in nodes),'publishedNodeSample':nodes[:200],'publishedEdgeSample':edges[:250],'publishedUnresolvedSample':unresolved[:200],'authorityNote':'Candidate graph nodes and edges remain non-canonical until approved.'}
    (a.out/'knowledge-graph-index.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');print(json.dumps({k:summary[k] for k in ('nodeCount','edgeCount','resolvedRelationshipCount','unresolvedRelationshipCount','isolatedNodeCount')},indent=2))
if __name__=='__main__':main()
