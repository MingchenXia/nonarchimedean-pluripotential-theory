"""Record verified NONFORCE311 only after all public path/ref checks pass."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,os

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'api-recovery-continuation311'
Q=G/'push-receipt-continuation311.json';M=G/'upload-manifest-continuation311.json'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not Q.exists()
p=load(D/'connector-plan.json');m=load(M);root=load(D/'public-GET-root-verification.json');fin=load(D/'public-GET-final-verification.json');created=load(D/'public-GET-created-verification.json')
assert p['manifest_sha256']==sha(M)=='30a0f6c2f1ec5d5342c13af26e1822bbba5be8b5745322dbe69fccadc7ed09f1'
assert root['all_frozen_paths_verified'] and root['actual_file_bindings']==233
assert root['expected_tree']==fin['tree_sha']==created['tree_sha']==p['expected_tree']=='1ef6adaf1c7ead43aa75efd85f1c0d988d51139a'
assert fin['ref_verified'] and fin['commit_sha']==created['commit_sha'] and fin['parents']==created['parents']==[p['parent']]
assert p['parent']=='4a6c9682257ba9124490e399b631c6b2435a8526' and not p['force']
assert len(m['files'])==m['file_count']==232 and len(m['whole_body_binding'])==5
for e in m['files']:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
for f in m['whole_body_binding']:
    body=b''.join(Path(m['files'][i]['local']).read_bytes() for i in f['ordered_file_indices']);e=f['original']
    assert body==Path(e['local']).read_bytes() and len(body)==e['bytes'] and hashlib.sha256(body).hexdigest()==e['sha256']
returns=load(D/'connector-content-tree-upload-returns.json')['uploads']
assert len(returns)==p['content_chunks']==135 and {x['i'] for x in returns}==set(range(135))
for e in returns:
    ch=load(D/f"content-chunk-{e['i']}.json")['tree'];body=b''
    for x in sorted(ch,key=lambda x:x['path']):
        data=x['content'].encode();h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();assert h==x['path']
        body+=b'100644 '+h.encode()+b'\0'+bytes.fromhex(h)
    assert hashlib.sha1(b'tree '+str(len(body)).encode()+b'\0'+body).hexdigest()==e['sha']==p['content_tree_shas'][e['i']]
env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation311.index')
native=subprocess.run(['git','--git-dir='+str(G/'native-continuation56.git'),'write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip();assert native==p['expected_tree']
assert len({e['sha'] for e in p['entries']})==p['unique_blobs']==230 and max(p['content_chunk_bytes'])==186744
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
q=dict(continuation=311,repository=p['repository'],branch=p['branch'],commit_sha=fin['commit_sha'],tree_sha=p['expected_tree'],parent_sha=p['parent'],manifest=str(M),manifest_sha256=sha(M),verified_utc=fin['recorded_utc'],recorded_utc=now,force_update=False,remote_ref_verified=True,remote_commit_parent_and_tree_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,file_count=233,listed_file_count=232,remote_blobs_verified=230,remote_actual_tree_nodes_verified=root['actual_trees'],all_five_split_bodies_reconstructed_byteexact=True,split_parts=129,content_objects_uploaded_in135_bounded_calls=True,maximum_content_chunk_bytes=186744,mathematical_acceptance=False,original_closure=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),source_qualification='WHOLE UNREVIEWED434435436437 andfrozen300301; active300301math excluded, compilationunverified, fulloriginals/deeperauditOPEN. Independent438 locallyretainedBEFOREANY300301math and NOTpartof311.',verification=dict(root_public_GET=str(D/'public-GET-root-verification.json'),root_public_GET_sha256=sha(D/'public-GET-root-verification.json'),created_public_GET=str(D/'public-GET-created-verification.json'),created_public_GET_sha256=sha(D/'public-GET-created-verification.json'),final_public_GET=str(D/'public-GET-final-verification.json'),final_public_GET_sha256=sha(D/'public-GET-final-verification.json'),connector_content_returns=str(D/'connector-content-tree-upload-returns.json'),bounded_transport_ALLbelow200000B=True),primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
Q.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
for n in ['active-work.json','checklist-current.json']:
    f=R/n;y=load(f);assert y['github_pending_checkpoint']['continuation']==311 and y['latest_verified_github_checkpoint']['continuation']==310 and y['current_active_batch']==[300,301]
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
    y.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=311,commit_sha=q['commit_sha'],tree_sha=q['tree_sha'],parent_sha=q['parent_sha'],receipt=str(Q),receipt_sha256=sha(Q),manifest=str(M),manifest_sha256=sha(M),verified_utc=q['verified_utc'],force_update=False,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True),next_work='VerifiedNONFORCE311 WHOLE434435436437 andfrozen300301. IndependentWHOLE438 angularmixedproducts/closedconvexhull/exactcubicenergy/gap>=a/3 retainedBEFOREANY300301math; publishnext312withnextsmallbatch whenready. Native300301 compactstatusONLY untilsettled; nohotfeedback,maxTWO. Continueindependentresearch; fulloriginals/deeperauditOPEN,counts/editorunchanged,compilerunverified.')
    f.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=311,commit=q['commit_sha'],verified=True,files=233,unique_blobs=230,actual_trees=root['actual_trees'],counts_unchanged=True),indent=2))
