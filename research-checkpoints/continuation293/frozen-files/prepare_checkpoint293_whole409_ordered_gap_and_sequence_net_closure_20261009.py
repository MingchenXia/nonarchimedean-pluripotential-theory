from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation293-publication-records';M=G/'upload-manifest-continuation293.json'
D=K/'public-P16.7-continuation409-ordered-energy-gaps-and-sequence-generated-net-closure-unreviewed'
C=R/'campaigns/round-285/P16.7-whole406407409-nonordered-compactness-and-existence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation292.json')
assert prior['commit_sha']=='348850f690b3a427e9b3788946b6261ba27d514f' and prior['tree_sha']=='4839becc6a0fbf496e8491f6b8181fe8c364651e' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(D/'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper']==409 and b['compiler']['kind']=='success' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
assert sha(Path(b['whole_paper']['path']))==b['whole_paper']['sha256']
paths=[p for p in sorted(D.iterdir()) if p.is_file()]
paths += [R/x for x in ['audit_and_stage_native282_whole_paper409_ROOT_20261009.py','read_terminal_native284_whole_actual_notes_20261009.py','retain_ROOT409_actual_compilation_and_scope_20261009.py','capture_terminal_native282283_actual_FINAL_20261009.py','read_terminal_native282_whole_actual_notes_20261009.py','prepare_native285_whole406407409_actual_compactness_and_existence_20261009.py','launch_frozen_native285_checked_20261009.py','record_verified_checkpoint292_20261009.py']]
paths += [G/'push-receipt-continuation292.json',Path(__file__)]
paths += [C/x for x in ['freeze.json','launch-record.json','settings.json','mathematical-packet-bindings.json']]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==292 and x['current_active_batch']==[285]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=293,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify regular NONFORCE293 whole compiled409 ordered gap and same-Gseq arbitrary decreasing-net closure. Native285 advances original P16.7 nonordered compactness/existence; ROOT reads terminal284 distinct formal P12.3 quotient theorem before reconstruction/follow-up. At mostTWO, unchanged counts/editor.');write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[285],terminal_native_campaigns=[282,284],terminal284_actual_fields_ROOT_read_but_full_expanded_formal_proof_not_yet_read=True,terminal284_math_NOT_published_in_this_checkpoint=True,new_papers=[409],compiler='success',UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint293: ordered energy gaps and original sequence-generated decreasing-net closure\n\nWhole compiled UNREVIEWED paper409 reconstructs the qualified actual generated calculus, all-four moving moments, point atoms, full pointwise uniqueness, finite-extension and fixed-probe current chain. A quantitative ordered energy-gap modulus controls each fixed bounded-test MA integral and every full-dimensional point. Energy selection represents ANY finite-energy decreasing generated net in the SAME original sequence-generated class without asserting a cofinal sequence. ALL Shilov boundaries reconstruct actual values including poles. Directed energy/MA/mixed/moving-moment and arbitrary-support full-dual ordered L1 continuity follow.\n\nThe entire actual and distinct expanded five-field notes, whole current887-line formal source and unique ledger/residual were ROOT physically read. The formal countable-flattening paragraph now explicitly sets L to its energy infimum, exactly as actual n2 already does. Native source and native whole companion are preserved separately unmodified, while corrected entire source/companion differ only there. Fresh whole GR4.2 and6.1--6.5 immediate bodies were read. Historical metadata or native reading ledgers are not new ROOT recursive whole-source receipts. Named deeper CLD/analytic/algebraic foundations stay qualified. Primary bodies/literal units/pixels/books remain LOCALONLY, excluded from publication.\n\nNonordered sublevel compactness/actual representability, sufficient intrinsic recognition, actual envelopes/orthogonality and EVERY arbitrary-support prescribed finite-full-dual measure existence remain OPEN. Native285 uses whole406407409 to advance these residuals. Terminal284 actual fields are read, but its distinct full formal proof is not yet ROOT read/reconstructed and is excluded. Counts16/42 solved,26OPEN,97accepted scoped papers unchanged; no new acceptance. Protected P16.4 editor OPEN UNCHANGED. NONFORCE update verifies all remote file/tree/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation293/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint ordered energy gaps and sequence-generated decreasing-net closure working paper',scope='Whole compiled UNREVIEWED409 with separately preserved native formal DATA and exact infimum clarification; original nonordered compactness/existence OPEN, primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation293.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation293.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
A=G/'api-recovery-continuation293';A.mkdir();chunks=[];chunk=[];size=0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());n=len(json.dumps(item,ensure_ascii=True).encode())
    if chunk and size+n>250000:chunks.append(chunk);chunk=[];size=0
    chunk.append(item);size+=n
if chunk:chunks.append(chunk)
chunk_sizes=[]
for i,ch in enumerate(chunks):
    p=A/f'content-chunk-{i}.json';p.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2)+'\n');chunk_sizes.append(p.stat().st_size)
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=chunk_sizes,commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),content_chunks=len(chunks),content_chunk_bytes=chunk_sizes,expected_tree=expected,primary_bodies_published=False),indent=2))
