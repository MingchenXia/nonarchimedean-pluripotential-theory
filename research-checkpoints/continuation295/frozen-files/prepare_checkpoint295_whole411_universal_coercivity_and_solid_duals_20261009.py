from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation295-publication-records';M=G/'upload-manifest-continuation295.json'
B=K/'P16.7-continuation411-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation294.json')
assert prior['commit_sha']=='9e2205b4b46953624b4a73018cb9bea6e0c4894a' and prior['tree_sha']=='e93a258f6fc50d6fb96e342f8e24d2103c809b10' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(B);assert b['paper']==411 and b['compiler']['kind']=='success' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
paths=[Path(e['path']) for e in b['public_files']]+[B]
paths += [R/x for x in ['retain_ROOT411_whole_proof_compilation_and_scope_20261009.py','capture_terminal_native285_actual_FINAL_20261009.py',
    'read_terminal_native285_whole_actual_notes_20261009.py','record_verified_checkpoint294_20261009.py']]
paths += [G/'push-receipt-continuation294.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==294 and x['current_active_batch']==[286]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=295,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),
        next_work='Verify NONFORCE295 whole compiled ROOT411 universal variational coercivity/solid full duals. Native286 continues; all terminal285 actual five fields read, distinct formal/expanded proof not yet ROOT read or reconstructed and excluded from checkpoint295. At mostTWO, counts/editor unchanged.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,
    accepted_scoped_papers=97,current_active_batch=[286],terminal_native_campaigns=[285],new_papers=[411],compiler='success',
    terminal285_actual_five_fields_ROOT_physically_read=True,terminal285_distinct_expanded_formal_proof_NOT_yet_ROOT_physically_read=True,
    terminal285_math_NOT_published_in_this_checkpoint=True,UNREVIEWED=True,original_closed=False,accepted=False,
    source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint295: quadratic scaling, solid full duals and universal variational coercivity\n\nWhole compiled UNREVIEWED ROOT411 combines the qualified actual Gauss reference bound with the exact cubic Green energy identity. Small-scale energy is bounded quadratically. Finite FULL bounded dual is equivalent to a normalized bounded-unit-energy integral test. EVERY finite-full-dual positive raw-mass-two Radon measure has square-root energy-sublevel integrability and a coercive variational objective, with an explicit bound for every maximizing tail. Finite full dual is solid under bounded domination. Every actual total-dimension-two point has a finite-full-dual normalized Dirac measure via its actual bounded MA atom and the NEW solidity proof. Countable summable-cost mixtures and dominated measures inherit the specified uniform-tail sector.\n\nAll new unique proofs and the complete current formal source were ROOT physically read. Analytic Green, Gauss/reference-measure and local atom foundations remain precisely qualified against their actual current407/409 applications; this is not another independent whole recursive source audit. Generated extensions normalize actual decreasing presentations; the normalized terms need NOT decrease and their convergence is established in L1. No extra model/native call or hot feedback produced this paper. Entire proof companion and source/application/scope/residual and actual compiler result are retained. Primary literal bodies/units/pixels/books LOCALONLY.\n\nNONORDERED analytic representability/compactness, sufficient intrinsic recognition, actual envelopes/orthogonality and EVERY arbitrary-support prescribed-measure existence remain OPEN. Coercivity supplies neither an actual maximizer nor an equation solution. Full-dual UI is proved only in the explicit summable-mixture/domination sector. Terminal285 actual five-field proofs were read, but its distinct full expanded formal proof remains unread/unreconstructed at this freeze and its mathematics is excluded. Native286 continues original general P12.3 CE. Counts16/42 solved,26OPEN,97accepted scoped papers unchanged; no new acceptance. Protected P16.4 editor OPEN UNCHANGED. NONFORCE update verifies remote blob/tree/file/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation295/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,
    file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,
    commit_message='Checkpoint universal variational coercivity and solid full-dual measures working paper',
    scope='Whole compiled UNREVIEWED ROOT411; original analytic compactness/envelopes/existence OPEN, primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation295.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation295.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API=G/'api-recovery-continuation295';API.mkdir();chunks=[];chunk=[];size=0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());n=len(json.dumps(item,ensure_ascii=True).encode())
    if chunk and size+n>250000:chunks.append(chunk);chunk=[];size=0
    chunk.append(item);size+=n
if chunk:chunks.append(chunk)
chunk_sizes=[]
for i,ch in enumerate(chunks):
    p=API/f'content-chunk-{i}.json';p.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2)+'\n');chunk_sizes.append(p.stat().st_size)
write(API/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],
    expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=chunk_sizes,
    commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),content_chunks=len(chunks),
    content_chunk_bytes=chunk_sizes,expected_tree=expected,primary_bodies_published=False),indent=2))
