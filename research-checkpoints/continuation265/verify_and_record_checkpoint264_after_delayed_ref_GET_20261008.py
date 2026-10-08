from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,time

R=Path('/workspace/research');G=R/'github-checkpoint';M=G/'upload-manifest-continuation264.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert sha(M)=='20b51552c9e71a7cf8370f692c228167e4c67b61101cc6add9e5e5bfd47f253f'
m=load(M);repo=m['repository'];branch=m['branch'];assert repo=='MingchenXia/nonarchimedean-pluripotential-theory' and branch=='codex/xean-research-20261003'
A=G/'api-recovery-continuation264';commit=load(A/'commit-response.json');tree=load(A/'independent-tree-binding.json')
assert commit['sha']=='888e40107fcf09df083b8b3ba58e12a25b1761e2'
assert commit['tree']['sha']==tree['expected_tree']=='6f7049e6ed2747340f604af6e5eb8c30135a7887'
assert commit['parents'][0]['sha']==m['expected_previous_checkpoint']=='d29dda3225f257f7a728dcc56e6cf945313d4da7'
assert load(A/'ref-request.json')==dict(sha=commit['sha'],force=False)
def get(endpoint):
 r=subprocess.run(['gh','api',endpoint+('&' if '?' in endpoint else '?')+'checkpoint_verification='+str(time.time_ns()),'--header','Cache-Control: no-cache'],capture_output=True,text=True,check=True);return json.loads(r.stdout)
base='repos/'+repo+'/git/'
ref=get(base+'ref/heads/'+branch);assert ref['object']['sha']==commit['sha']
remote=get(base+'commits/'+commit['sha']);assert remote['tree']['sha']==tree['expected_tree'] and remote['parents'][0]['sha']==m['expected_previous_checkpoint']
entries=get(base+'trees/'+tree['expected_tree']+'?recursive=1');assert not entries.get('truncated');blobs={e['path']:e['sha'] for e in entries['tree'] if e['type']=='blob'}
files=m['files']+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation264.json',sha256=sha(M))]
for e in files:
 data=Path(e['local']).read_bytes();assert hashlib.sha256(data).hexdigest()==e['sha256']
 assert blobs[e['path']]==hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
assert len(files)==m['file_count']+1==tree['files']==138
assert get(base+'ref/heads/'+branch)['object']['sha']==commit['sha']
now=datetime.now(timezone.utc).isoformat()
receipt=dict(verified_utc=now,repository=repo,branch=branch,parent_sha=m['expected_previous_checkpoint'],commit_sha=commit['sha'],tree_sha=tree['expected_tree'],files=len(files),manifest_sha256=sha(M),independent_native_git_tree_verified=True,all_file_blob_bindings_verified_remote=True,remote_ref_verified=True,force_update=False,fully_solved_original_atoms=m['fully_solved_original_atoms'],remaining_open_atoms=26,route='Authorized paced GitHub bulk UTF8 tree API; original nonforce PATCH succeeded, immediate fresh GET disagreed, two later fresh GETs and fresh commit/tree/all138blob bindings independently confirm commit; recovery performs ONLY GETs',commit_url='https://github.com/'+repo+'/commit/'+commit['sha'])
P=G/'push-receipt-continuation264.json';assert not P.exists();write(P,receipt)
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=load(p);assert x['github_pending_checkpoint']['continuation']==264 and len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=264,commit=commit['sha'],tree=tree['expected_tree'],receipt=str(P),receipt_sha256=sha(P),receipt_reported_utc=now,ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False),next_work='Continue TWO native263/P21.3 and264/P16.7 campaigns, completed261 whole370 draft ROOT staged; no new original/count increase. Next verified checkpoint publishes entire370 and receipt264. Read ONLY settled complete outputs; protected editor OPEN UNCHANGED; no hot feedback.16solved26OPEN97papers.');write(p,x)
print(json.dumps(receipt,indent=2))
