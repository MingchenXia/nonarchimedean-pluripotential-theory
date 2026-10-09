"""Record verified NONFORCE310v2, exact whole-companion reconstruction, no acceptance."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,os

R=Path('/workspace/research');G=R/'github-checkpoint';D=G/'api-recovery-continuation310-v2'
Q=G/'push-receipt-continuation310.json';M=G/'upload-manifest-continuation310-v2.json'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not Q.exists()
p=load(D/'connector-plan.json');m=load(M);root=load(D/'public-GET-root-verification.json');fin=load(D/'public-GET-final-verification.json')
assert p['manifest_sha256']==sha(M)=='2e928ce4b963b1b0b01013617d5d3e45fa2e60add65ab7f3bbea7aa215f8057b'
assert root['all_frozen_paths_verified'] and root['actual_file_bindings']==112 and root['actual_trees']==14
assert root['expected_tree']==fin['tree_sha']==p['expected_tree']=='98399a91137fd4de701806dcc0f34e451a80a182'
assert fin['ref_verified'] and fin['commit_sha']=='4a6c9682257ba9124490e399b631c6b2435a8526' and fin['parents']==[p['parent']]
assert p['parent']=='9556f41667eb56aea7e4ec0ddf1b8665a320698e'
assert len(m['files'])==m['file_count']==111
for e in m['files']:assert sha(e['local'])==e['sha256'] and Path(e['local']).stat().st_size==e['bytes']
for f in m['whole_companion_binding']:
 body=b''.join(Path(e['local']).read_bytes() for e in f['ordered_parts'])
 assert body==Path(f['original']['local']).read_bytes() and len(body)==f['whole_bytes'] and hashlib.sha256(body).hexdigest()==f['whole_sha256']
returns=load(D/'connector-content-tree-upload-returns.json')['uploads'];assert len(returns)==40
for e in returns:
 ch=load(D/f"content-chunk-{e['i']}.json")['tree'];body=b''
 for x in sorted(ch,key=lambda x:x['path']):
  data=x['content'].encode();h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();assert h==x['path']
  body+=b'100644 '+h.encode()+b'\0'+bytes.fromhex(h)
 assert hashlib.sha1(b'tree '+str(len(body)).encode()+b'\0'+body).hexdigest()==e['sha']
env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation310-v2.index')
native=subprocess.run(['git','--git-dir='+str(G/'native-continuation56.git'),'write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip();assert native==p['expected_tree']
assert len({e['sha'] for e in p['entries']})==p['unique_blobs']==109
assert sha(R/'root-checks/public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
now=datetime.now(timezone.utc).isoformat()
q=dict(continuation=310,transport_version=2,repository=p['repository'],branch=p['branch'],commit_sha=fin['commit_sha'],tree_sha=p['expected_tree'],parent_sha=p['parent'],manifest=str(M),manifest_sha256=sha(M),verified_utc=fin['recorded_utc'],recorded_utc=now,force_update=False,remote_ref_verified=True,remote_commit_parent_and_tree_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True,file_count=112,listed_file_count=111,remote_blobs_verified=109,remote_actual_tree_nodes_verified=14,whole_7084039B_companion_reconstructed_from40_public_parts_byteexact=True,mathematical_acceptance=False,original_closure=False,counts=dict(solved=16,open=26,accepted_scoped_papers=97),source_qualification='UNREVIEWED WHOLE431432433 and frozen299 metadata; native298/299 terminal math excluded. Compiler unverified. ROOT434 independently retained locally and NOT part of310.',verification=dict(root_public_GET=str(D/'public-GET-root-verification.json'),root_public_GET_sha256=sha(D/'public-GET-root-verification.json'),final_public_GET=str(D/'public-GET-final-verification.json'),final_public_GET_sha256=sha(D/'public-GET-final-verification.json'),connector_content_returns=str(D/'connector-content-tree-upload-returns.json'),bounded_transport_MAX189740B=True,earlier_oversized_requests_interrupted_and_not_counted_success=True),primary_literal_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True)
Q.write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n')
for n in ['active-work.json','checklist-current.json']:
 f=R/n;y=load(f);assert y['github_pending_checkpoint']['continuation']==310 and y['latest_verified_github_checkpoint']['continuation']==309 and y['current_active_batch']==[299]
 assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
 y.update(updated_utc=now,github_pending_checkpoint=None,latest_verified_github_checkpoint=dict(continuation=310,commit_sha=q['commit_sha'],tree_sha=q['tree_sha'],parent_sha=q['parent_sha'],receipt=str(Q),receipt_sha256=sha(Q),manifest=str(M),manifest_sha256=sha(M),verified_utc=q['verified_utc'],transport_version=2,force_update=False,remote_ref_verified=True,all_file_blob_bindings_verified_remote=True,independent_native_git_tree_verified=True),next_work='VerifiedNONFORCE310WHOLE431432433 andfrozen299. IndependentWHOLE434quadraticpencilwhole2Dirac andtotalmass2Radonbranch retainedBEFOREANYsettled298/299math. Captureonlysettled298actualFINALthenALLfivefields/distinctformal/wholeledgers/exactimmediateprimary beforequalifiedROOT435. Both298299completedcompactonly, nohotfeedback,maxTWO,counts/editor unchanged,originalsOPEN,compileunverified.')
 f.write_text(json.dumps(y,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(continuation=310,commit=q['commit_sha'],verified=True,transport_version=2,files=112,unique_blobs=109,actual_trees=14,counts_unchanged=True),indent=2))
