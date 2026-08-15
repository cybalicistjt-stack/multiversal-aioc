from __future__ import annotations
import csv, hashlib
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'governance/application-planning/stage-a-a9'
SCOPE=BASE/'A9_CURRENT_CHANGED_PATH_SCOPE_v0.3.0.csv'
AUTH=BASE/'A9_CURRENT_AUTHORITY_DISPOSITION_v0.3.0.csv'
HANDOFF=BASE/'STAGE_A_A9_CURRENT_REPOSITORY_REVALIDATION_v0.3.0.md'
EXPECTED_SCOPE_SHA='8436f021735757b0513d71969bd7c4dea06b316d11eb1765535ccb474dba075f'
EXPECTED_AUTH_SHA='17d96b52dcd65b44c087e2f91c54589361ff3e220d131065bd8a7d4b2e06cb3f'
EXPECTED_PRE_SHA='95d11bc619bbe48d7ede9565c0c5f8abbb9ccdd9e4386959bbc01cbf6a0e2e11'
EXPECTED_COMP_SHA='2a9a3b41aba8cf4ecf252fc1676b0420c229ac9fab28057c827d15c0251f37a8'
EXPECTED_HIST_PLAN_SHA='782c88d2404893546bdab98a1c1429ccb7fa864eca234359b7e2619a65c4af62'
EXPECTED_APP_A8='e9aaa858b345e6a29e27369c01468551752a2483'
EXPECTED_APP_MAIN='957335a9f5724c8934f9c4a6f011db6f55ecab55'
EXPECTED_AIOC='4f1a51b39651922d039031c941400e924991dc39'
EXPECTED_SCOPE_ROWS=102
EXPECTED_AUTH_ROWS=75
EXPECTED_OPS=Counter({'CREATE': 67, 'MODIFY_BOUNDED': 1, 'REUSE': 28, 'REUSE_CONTEXT': 4, 'WRAP': 2})
errors=[]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if not SCOPE.is_file(): errors.append('missing A9 current scope')
else:
 if sha(SCOPE)!=EXPECTED_SCOPE_SHA: errors.append('scope sha mismatch: '+sha(SCOPE))
 rows=list(csv.DictReader(SCOPE.open(encoding='utf-8',newline='')))
 if len(rows)!=EXPECTED_SCOPE_ROWS: errors.append(f'scope rows {len(rows)} != {EXPECTED_SCOPE_ROWS}')
 paths=[r['Path'] for r in rows]
 if len(paths)!=len(set(paths)): errors.append('duplicate current scope paths')
 if Counter(r['Operation'] for r in rows)!=EXPECTED_OPS: errors.append('unexpected scope operation counts')
 ps=set(paths)
 required={
  'database/migrations/0007_a9_investigation_social_runtime.json',
  'packages/contracts/src/social-relations/relationship-edge-port.ts',
  'packages/contracts/src/social-relations/faction-standing-influence-port.ts',
  'packages/contracts/src/social-relations/social-outcome-coordinator.ts',
  'packages/contracts/src/social-relations/a9-source-state-preservation-port.ts',
  'packages/contracts/src/investigation/investigation-port.ts',
  'packages/contracts/src/investigation/observation-claim-port.ts',
  'packages/contracts/src/investigation/evidence-reference-port.ts',
  'packages/contracts/src/investigation/investigation-operation-status-port.ts',
  'packages/contracts/src/investigation/investigation-source-state-preservation-port.ts',
  'packages/contracts/src/visibility-projection/a9-projection-port.ts',
  'packages/contracts/src/visibility-projection/semantic-node-edge-projection-port.ts',
  'schemas/domains/social-relations/a9-*.schema.json',
  'schemas/domains/investigation/a9-*.schema.json',
  'packages/contracts/src/a6/action-proposal-port.ts',
  'packages/contracts/src/a7/combat-atomic-result-coordinator.ts',
  'packages/contracts/src/shared-assets/a8-cross-domain-result-coordinator.ts',
  'packages/contracts/src/session/authoritative-session-command-handler.ts',
  'packages/contracts/src/session/hidden-information-response-filter.ts',
  'apps/client-ui/src/App.tsx','tools/verify_stage_a_a9.py',
  '.github/workflows/validate-stage-a-a9-investigation-social.yml',
  'docs/evidence/stage-a-a9/**','receipts/STAGE-A-A9-CLOSURE.json'
 }
 if required-ps: errors.append('scope missing required paths: '+str(sorted(required-ps)))
 if any('<next>' in p for p in ps): errors.append('stale <next> migration remains')
 if 'packages/contracts/src/social-relations/a9-pack-lifecycle-port.ts' in ps or 'packages/contracts/src/investigation/investigation-pack-lifecycle-port.ts' in ps: errors.append('unresolved F024 historical lifecycle paths remain')
 if any(r['Operation'] in {'DELETE','REWRITE','REPLACE'} for r in rows): errors.append('destructive operation present')
 wraps={r['Path'] for r in rows if r['Operation']=='WRAP'}
 expected_wraps={'packages/contracts/src/session/authoritative-session-command-handler.ts','packages/contracts/src/session/hidden-information-response-filter.ts'}
 if wraps!=expected_wraps: errors.append('wrapper set unexpected: '+str(sorted(wraps)))
 closure=[r for r in rows if r['Path']=='receipts/STAGE-A-A9-CLOSURE.json']
 if len(closure)!=1 or 'completion-only' not in closure[0]['Purpose'].lower(): errors.append('closure receipt must remain completion-only')
if not AUTH.is_file(): errors.append('missing A9 authority disposition')
else:
 if sha(AUTH)!=EXPECTED_AUTH_SHA: errors.append('authority sha mismatch: '+sha(AUTH))
 a=list(csv.DictReader(AUTH.open(encoding='utf-8',newline='')))
 if len(a)!=EXPECTED_AUTH_ROWS: errors.append(f'authority rows {len(a)} != {EXPECTED_AUTH_ROWS}')
 hist=[r for r in a if r['Source']=='HISTORICAL_70_PATH_PLAN']
 if len(hist)!=70: errors.append(f'historical authority rows {len(hist)} != 70')
 overlays=[r for r in a if r['Authority_ID'].startswith('A9O-')]
 if len(overlays)!=5: errors.append(f'overlay rows {len(overlays)} != 5')
 if {r['Authority_ID'] for r in overlays}!={f'A9O-{i:03d}' for i in range(1,6)}: errors.append('overlay IDs unexpected')
 lifecycle=[r for r in hist if 'pack-lifecycle-port.ts' in r['Source_Item']]
 if len(lifecycle)!=3: errors.append(f'historical lifecycle authority rows {len(lifecycle)} != 3')
 if any(r['Classification']!='CONFLICT_REQUIRES_REDESIGN' for r in lifecycle): errors.append('historical F024 lifecycle path not redesigned')
if not HANDOFF.is_file(): errors.append('missing A9 revalidation handoff')
else:
 t=HANDOFF.read_text(encoding='utf-8')
 required=(
  'PASS — READY_FOR_BOUNDED_A9_ACTIVATION',EXPECTED_SCOPE_SHA,EXPECTED_AUTH_SHA,EXPECTED_PRE_SHA,EXPECTED_COMP_SHA,EXPECTED_HIST_PLAN_SHA,
  EXPECTED_APP_A8,EXPECTED_APP_MAIN,EXPECTED_AIOC,'0007_a9_investigation_social_runtime.json',
  'F024 / Pack Lifecycle reconciliation','P14-GAP-001','P15-GAP-001','hiddenEventCount','raw `commandPayload`',
  'A6 remains sole Action','A7 remains combat','A8 remains Asset/currency/ownership','A9 owns only Campaign runtime faction',
  'releaseAuthorized=false','deploymentAuthorized=false','providerVendorPaidServiceAuthorized=false'
 )
 for x in required:
  if x not in t: errors.append('handoff missing phrase: '+x)
if errors: raise SystemExit('STAGE-A-A9 CURRENT REVALIDATION: FAIL\n- '+'\n- '.join(errors))
print('STAGE-A-A9 CURRENT REVALIDATION: PASS')
print('historical_path_actions=70 overlays=5 authority_rows='+str(EXPECTED_AUTH_ROWS))
print('current_scope_rows='+str(EXPECTED_SCOPE_ROWS)+' operations='+str(dict(EXPECTED_OPS)))
print('scope_sha='+EXPECTED_SCOPE_SHA+' authority_sha='+EXPECTED_AUTH_SHA)
print('app_a8_predecessor='+EXPECTED_APP_A8+' app_current_main='+EXPECTED_APP_MAIN)
print('next_migration=0007_a9_investigation_social_runtime.json')
print('activation=READY_FOR_BOUNDED_A9_ACTIVATION release=false deployment=false provider_vendor_paid=false')
