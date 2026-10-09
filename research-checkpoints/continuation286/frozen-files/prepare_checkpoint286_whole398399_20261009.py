from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation286-publication-records'; M=G/'upload-manifest-continuation286.json'
assert not F.exists() and not M.exists()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
prior=load(G/'push-receipt-continuation285.json')
assert prior['commit_sha']=='80475a6b047ac041dd4173dcf0b75267b0113430'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
paths=[]
for n in [398,399]:
    p=K/f'P16.7-continuation{n}-ROOT-whole-paper-source-scope-and-binding-20261009.json'; b=load(p)
    assert not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='success'
    tex=Path(b['whole_paper']['path']); assert sha(tex)==b['whole_paper']['sha256'] and tex.stat().st_size==b['whole_paper']['bytes']
    paths += [p,tex]
paths += [K/'ROOT398399-fresh-primary-application-and-compilation-scope-20261009.json',K/'ROOT398399-native-editor-compiler-success-20261009.json',R/'write_ROOT399_bounded_continuous_uniqueness_20261009.py',R/'retain_ROOT398399_source_units_and_public_bindings_20261009.py',R/'record_verified_checkpoint285_20261009.py',G/'push-receipt-continuation285.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir()
for p in paths:
    rel=p.relative_to(R); assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    assert p.suffix in ['.tex','.json','.py']
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==285
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=286,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify286 whole local analytic divisor and bounded continuous uniqueness working papers with exact qualified source/compiler bindings. Native278279 independent at mostTWO; pursue actual full unbounded uniqueness/compactness/existence and formal residuals; no countchange.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=x['current_active_batch'],new_papers=[398,399],UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint286: whole local analytic divisor and bounded continuous Monge--Ampere uniqueness working papers\n\nPaper398 gives local principal analytic divisor-current annihilation, rational-domain approximation and the exact conditional classical pluriharmonic criterion. Paper399 includes the entire prior bounded-calculus/divisor proof and adds a coordinate-curve uniqueness argument: injective scalar Radon measure pushforward, the finite-ground-field calibration factor, finite Galois averaging with normalized base-change integration, bounded Gauss-ray Liouville, density of closed rigid points, and coordinate-fibre connection. Both complete saved sources compiled successfully with the built-in editor compiler.\n\nAll mathematical claims remain UNREVIEWED. The bounded uniqueness claim does not close full P16.7: unbounded intrinsic recognition, finite-energy compactness, obstacle envelopes/orthogonality, arbitrary-support equation existence and full-domain uniqueness remain OPEN. Counts stay16/42 solved,26OPEN,97accepted scoped papers. Native278279 continue independently on frozen inputs using Xean native signed-in Codex gpt-6.1-sol xhigh, at mostTWO. New398399 material was not sent as hot feedback to active campaigns.\n\nQualified metadata binds exact full source versions, entire immediate applied proof-reading ranges and actual Van-der-Put pixels03,05,06. Primary source bodies, literal units, pixels and whole books remain LOCALONLY. The deeper Tate/Weierstrass foundations are named rather than falsely claimed wholly reaudited. Literal-LF slicing preserves form-feed pagination. Protected P16.4 editor stays OPEN UNCHANGED. Publication is NONFORCE with native tree and all remote blob/ref verification.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation286/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint whole local analytic divisor tests and bounded continuous uniqueness working papers',scope='Entire UNREVIEWED398399 proofs and qualified source/compiler records; no original closure or accepted-count change; full primary bodies/pixels/books LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation286.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]
task_env=dict(os.environ);task_env['GIT_INDEX_FILE']=str(G/'native-continuation286.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=task_env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=task_env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=task_env,capture_output=True,text=True,check=True).stdout.strip()
A=G/'api-recovery-continuation286';A.mkdir();chunks=[];chunk=[];size=0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());n=len(json.dumps(item,ensure_ascii=False).encode())
    if chunk and size+n>250000:chunks.append(chunk);chunk=[];size=0
    chunk.append(item);size+=n
if chunk:chunks.append(chunk)
for i,ch in enumerate(chunks):write(A/f'content-chunk-{i}.json',dict(tree=ch))
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),content_chunks=len(chunks),expected_tree=expected,source_bodies_published=False),indent=2))
