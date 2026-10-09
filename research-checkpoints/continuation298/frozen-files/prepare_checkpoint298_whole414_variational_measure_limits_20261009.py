from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation298-publication-records';M=G/'upload-manifest-continuation298.json'
B=K/'P16.7-continuation414-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation297.json')
assert prior['commit_sha']=='8cbfe025d86dcd48354703546c8f1288ed65feed' and prior['tree_sha']=='639a45409a00013d09a6ad3bbc029e7ec3ac147b' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(B);assert b['paper']==414 and b['compiler']['kind']=='success' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
paths=[Path(e['path']) for e in b['public_files']]+[B]
paths += [R/n for n in ['retain_ROOT414_whole_proof_compilation_and_scope_20261009.py','record_verified_checkpoint297_20261009.py']]
paths += [G/'push-receipt-continuation297.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==297 and x['current_active_batch']==[287,288]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=298,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE298 whole compiled414 universal variational MA measure limits and calibrated dual retraction. Native287/288 continue P16.7/P12.3. Only compact statuses until terminal; then capture and read ALL actual/expanded proofs before reconstruction or follow-up. At mostTWO, counts/editor unchanged.');write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[287,288],new_papers=[414],compiler='success',whole_new_proofs_ROOT_physically_read=True,active_native_math_NOT_read_or_published=True,UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint298: universal variational measure limits and calibrated full-dual retraction\n\nWhole compiled UNREVIEWED ROOT414 combines qualified universal coercivity411 with nonordered endpoint/maximum-energy estimates412. For EVERY arbitrary-support positive raw-mass-two Radon measure mu of finite FULL bounded dual, every normalized maximizing net has a common energy bound and midpoint I at most four times the deficit sum. Real energies converge WITHOUT L1(mu) domination. Actual Green and endpoint absolute moments make diagonal MA integrals Cauchy, with |D_a-D_b|<=H_C(I)+sqrt(12CI), and all four joint-tail endpoint moments converge. Fixed C test transgression bounds MA measure differences by sqrt(12LI); actual span-C density and positive raw mass2 give an actual Radon weak limit nu without a countable test set or subsequence.\n\nThe full dual is exactly E*(nu)=e-D, with quantitative calibration |int a_alpha nu-D_alpha|<=sqrt(48C epsilon_alpha), so the SAME normalized net also maximizes nu. All these limits are independent of the maximizing net. The canonical measure map V(mu)=nu decreases full dual by exact cubic scaling/Taylor remainder and is idempotent. It fixes EVERY already generated actual MA(u). Every FIXED generated finite-energy u has convergent moments against these MA measures using uniform ordered presentation errors. All unique new proofs and the full467-line formal source were ROOT physically read and compiled successfully; entire source and source/application/scope/residual companion retained. Qualified analytic foundations and deeper source-reading limits remain unchanged, not a new independent recursive audit. No new native/model call or agent produced this separate ROOT deduction; no active mathematics inspection or hot feedback. Primary full bodies/pixels/books LOCALONLY.\n\nActual analytic representation of the nonordered full-point tuple and recognition in original G, equality V(mu)=mu for EVERY prescribed measure, suitable envelopes/orthogonality or legitimate two-sided variational replacement, and full prescribed-measure existence/uniqueness remain OPEN. Fixed-point necessity is not sufficiency. Signed integral convergence is not L1(mu) convergence, and fixed generated tests do not justify an unproved moving unbounded limit. Native287/288 continue user-selected local Xean plus signed-in official Codex gpt-6.1-sol xhigh, at mostTWO; active mathematics excluded. Counts16/42 solved,26OPEN,97accepted scoped papers unchanged; no new acceptance. Protected P16.4 editor OPEN UNCHANGED. NONFORCE update verifies remote blob/tree/file/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation298/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint universal variational MA limits and calibrated full-dual retraction',scope='Whole compiled UNREVIEWED ROOT414; original analytic representation and prescribed-measure existence OPEN, primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation298.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation298.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API=G/'api-recovery-continuation298';API.mkdir();chunks=[];chunk=[];size=0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());n=len(json.dumps(item,ensure_ascii=True).encode())
    if chunk and size+n>250000:chunks.append(chunk);chunk=[];size=0
    chunk.append(item);size+=n
if chunk:chunks.append(chunk)
chunk_sizes=[]
for i,ch in enumerate(chunks):
    p=API/f'content-chunk-{i}.json';p.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2)+'\n');chunk_sizes.append(p.stat().st_size)
write(API/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=chunk_sizes,commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),content_chunks=len(chunks),content_chunk_bytes=chunk_sizes,expected_tree=expected,primary_bodies_published=False),indent=2))
