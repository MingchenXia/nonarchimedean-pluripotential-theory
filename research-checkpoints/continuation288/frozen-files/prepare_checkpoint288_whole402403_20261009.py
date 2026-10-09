from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation288-publication-records';M=G/'upload-manifest-continuation288.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation287.json')
assert prior['commit_sha']=='7aa3b5de5b0881dc83f633e5819235c3b2840c8f' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
bindings=[K/'P16.7-continuation402-ROOT-whole-paper-source-scope-and-binding-20261009.json',K/'P16.7-continuation403-ROOT-whole-paper-source-scope-and-binding-20261009.json']
paths=[]
for p in bindings:
    b=load(p);assert not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='success'
    e=b.get('whole_paper',b.get('paper'));q=Path(e['path']);assert sha(q)==e['sha256'] and q.stat().st_size==e['bytes']
    s=Path(b['source_scope']['path']);assert sha(s)==b['source_scope']['sha256']
    paths += [p,q,s]
paths += [R/name for name in ['retain_ROOT402_literal_source_units_and_whole_binding_20261009.py','append_whole_ROOT402_to_ROOT403_20261009.py','retain_ROOT403_whole_unique_proof_and_source_scope_20261009.py','capture_terminal_native280281_actual_FINAL_20261009.py','record_verified_checkpoint287_20261009.py']]
paths += [G/'push-receipt-continuation287.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==287 and x['current_active_batch']==[]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=288,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify288 whole402403 compiled UNREVIEWED point-atom and full generated uniqueness working proofs. Physically read all actual/expanded terminal280281 bodies before reconstruction and fresh frozen campaigns. No acceptance/count change; protected editor OPEN UNCHANGED.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[],terminal_native_campaigns=[280,281],terminal_mathematical_bodies_not_yet_ROOT_physically_read=True,terminal_outputs_not_published_in_this_checkpoint=True,new_papers=[402,403],UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint288: whole atomic-point and generated uniqueness working papers\n\nPaper402 constructs actual positive bounded MA atoms at every full graded-dimension-two point and proves finite-energy point bounds, hence all-Shilov coordinate bounds. Paper403 gives a complete WORKING proof of pointwise uniqueness in the actual decreasing-generated class using all four moving moments, the all-bounded-test gradient estimate, finite Gauss-disc curve endpoint control, normalized finite curve extensions, TWO actual coordinate fibres, finite point limits and all-Shilov reconstruction. The full402 mathematical body is reproduced as a standalone appendix; exact identity is not another independent source audit. No unbounded divisor restriction, analytic varying Shilov-section shortcut, or surface MA base-change formula is used.\n\nBoth whole standalone sources compiled successfully with the built-in editor compiler. Entire current unique mathematics and the applied immediate primary units were physically ROOT read. The published deeper analytic, intersection and calibration foundations are named, not freshly recursively reproved. Full primary bodies/literal units/pixels/book contexts remain LOCALONLY. Source hashes do not certify correctness. Native/generated programs remain DATA and were never imported or executed by ROOT. The user-protected P16.4 editor stays OPEN UNCHANGED.\n\nALL new mathematical claims remain UNREVIEWED. Counts16/42 solved,26OPEN,97accepted scoped papers. Original P16.7 still requires intrinsic E1 recognition, actual energy-sublevel representability/compactness and arbitrary-measure existence; P12.3 also remains OPEN. Native280281 have settled, their actual FINALs were retained but whole mathematical audit is pending and those outputs are excluded here. No hot feedback was sent. NONFORCE checkpoint requires independent native Git whole tree and all remote file/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation288/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint whole atomic point tests and generated uniqueness working proofs',scope='Whole compiled UNREVIEWED402403 plus qualified source/application/binding/compiler metadata; no original closure/count change; primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation288.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]
task_env=dict(os.environ);task_env['GIT_INDEX_FILE']=str(G/'native-continuation288.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=task_env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=task_env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=task_env,capture_output=True,text=True,check=True).stdout.strip()
A=G/'api-recovery-continuation288';A.mkdir();chunks=[];chunk=[];size=0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());n=len(json.dumps(item,ensure_ascii=False).encode())
    if chunk and size+n>250000:chunks.append(chunk);chunk=[];size=0
    chunk.append(item);size+=n
if chunk:chunks.append(chunk)
for i,ch in enumerate(chunks):write(A/f'content-chunk-{i}.json',dict(tree=ch))
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),content_chunks=len(chunks),expected_tree=expected,source_bodies_published=False),indent=2))
