from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,time

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'api-recovery-continuation259'
M=G/'upload-manifest-continuation259.json';receipt=G/'push-receipt-continuation259.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not receipt.exists() and sha(M)=='54cd962452193c0ed67ceb5ec935617f3b7ea7b39c1fc6c9a9505fcf3e873669'
m=json.loads(M.read_text());z=json.loads((D/'commit-response.json').read_text());t=json.loads((D/'independent-tree-binding.json').read_text())
assert m['repository']=='MingchenXia/nonarchimedean-pluripotential-theory' and m['branch']=='codex/xean-research-20261003'
assert z['sha']=='525c3eb34ee595983d5d67693f3d8de5ed7299c7' and z['tree']['sha']==t['expected_tree']=='2e9a21be29bdbfee737fb860efd6e18590cb3dfc'
assert [x['sha'] for x in z['parents']]==[m['expected_previous_checkpoint']]==['568aed3f9ac956a05ce665857881cc44766606e6']
assert json.loads((D/'ref-request.json').read_text())==dict(sha=z['sha'],force=False)
base='repos/'+m['repository']+'/git/'
def get(endpoint,label):
 stamp=str(time.time_ns());sep='&' if '?' in endpoint else '?'
 r=subprocess.run(['gh','api',endpoint+sep+'checkpoint_verification='+stamp,'--method','GET','--header','Cache-Control: no-cache'],capture_output=True,text=True,check=True)
 value=json.loads(r.stdout);(D/(label+'-response.json')).write_text(json.dumps(value,indent=2)+'\n');return value
ref1=get(base+'ref/heads/'+m['branch'],'fresh-ref1');assert ref1['object']['sha']==z['sha']
commit=get(base+'commits/'+z['sha'],'fresh-commit');assert commit['tree']['sha']==t['expected_tree'] and [x['sha'] for x in commit['parents']]==[t['parent']]
tree=get(base+'trees/'+t['expected_tree']+'?recursive=1','fresh-tree');assert not tree.get('truncated')
actual={e['path']:e['sha'] for e in tree['tree'] if e['type']=='blob'}
entries=m['files']+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation259.json',sha256=sha(M))]
assert len(entries)==22
for e in entries:
 p=Path(e['local']);data=p.read_bytes();assert hashlib.sha256(data).hexdigest()==e['sha256']
 expected=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();assert actual[e['path']]==expected
ref2=get(base+'ref/heads/'+m['branch'],'fresh-ref2');assert ref2['object']['sha']==z['sha']
now=datetime.now(timezone.utc).isoformat();out=dict(verified_utc=now,repository=m['repository'],branch=m['branch'],parent_sha=t['parent'],commit_sha=z['sha'],tree_sha=t['expected_tree'],files=len(entries),manifest_sha256=sha(M),independent_native_git_tree_verified=True,all_file_blob_bindings_verified_remote=True,remote_ref_verified=True,force_update=False,fully_solved_original_atoms=m['fully_solved_original_atoms'],remaining_open_atoms=m['remaining_open_atoms'],route='Existing authorized nonforcePATCH succeeded; original finalGET assertion failed. READONLY fresh cache-qualified GETs verify two refreads, commitparents/tree and everyblob against independentlybuilt tree. No secondmutation/authenticationchange.',commit_url='https://github.com/'+m['repository']+'/commit/'+z['sha'])
receipt.write_text(json.dumps(out,indent=2)+'\n')
for name in ['active-work.json','checklist-current.json']:
 p=R/name;x=json.loads(p.read_text());assert x['github_pending_checkpoint']['continuation']==259
 assert len(x['fully_solved_original_atoms'])==15 and x['remaining_open_original_atoms']==27 and x['historical_reviewed_scoped_papers']==96
 x.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=259,commit=z['sha'],tree=t['expected_tree'],receipt=str(receipt),receipt_sha256=sha(receipt),receipt_reported_utc=now,ROOT_observed_completed_utc=now,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,force_update=False));p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,indent=2))
