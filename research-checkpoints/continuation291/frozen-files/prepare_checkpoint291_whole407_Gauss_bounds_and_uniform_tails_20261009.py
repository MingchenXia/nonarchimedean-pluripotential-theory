from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation291-publication-records'; M=G/'upload-manifest-continuation291.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation290.json')
assert prior['commit_sha']=='e06a7bd245d51eb160c84938a16bdae4ee7d4c69' and prior['tree_sha']=='93bc2e2ee49c355ffb0a22a8a67066dd4d7e0681' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
B=K/'P16.7-continuation407-ROOT-whole-paper-source-scope-and-binding-20261009.json'; b=load(B)
assert b['paper']==407 and not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='success'
P=Path(b['whole_paper']['path']); S=Path(b['source_scope']['path']); A=Path(b['compiler']['result_record'])
assert sha(P)==b['whole_paper']['sha256'] and P.stat().st_size==b['whole_paper']['bytes']
assert sha(S)==b['source_scope']['sha256'] and sha(A)==b['compiler']['result_record_sha256']
assert load(A)['kind']=='success' and load(A)['actual_result_observed']
paths=[P,S,B,A,R/'append_and_bind_ROOT407_Gauss_bounds_and_uniform_tails_20261009.py',R/'retain_ROOT407_actual_compilation_and_scope_20261009.py',R/'record_verified_checkpoint290_20261009.py',G/'push-receipt-continuation290.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir()
for p in paths:
    rel=p.relative_to(R); assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==290 and x['current_active_batch']==[282]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=291,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify291 whole compiled407 Gauss reference bounds, fixed-test gradient domination and uniform negative-part tails including decreasing nets. Native282283 independently continue whole P16.7/P12.3 residual audit. ROOT advances arbitrary-limit representability/actual compactness. At mostTWO, no hot feedback/count change; protected editor OPEN UNCHANGED.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[282],terminal_native_campaigns=[283],terminal283_actual_FINAL_retained_not_yet_ROOT_physically_read=True,terminal283_math_NOT_published_in_this_checkpoint=True,new_papers=[407],compiler='success',UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint291: universal Gauss bounds and fixed-bounded-test uniform tails\n\nWhole compiled working paper407 proves coordinate one-half Lipschitz Gauss values and normalized reference bounds [-1/2,0] through TWO actual coordinate-annulus comparisons. The full actual reference curvature measure is supported on the Gauss skeleton, with raw calibrated density two; Laurent cancellation proves vanishing off that skeleton. Fixed bounded-test gradient measures are dominated by finite actual bounded mixed-MA measures using all-stage square composition and global psh caps. The Green/mixed-moment estimate gives uniform T^(-1/2) negative-part truncation tails against each fixed bounded test MA measure. Smooth truncation uses only bounded continuous gradient multipliers. Actual decreasing-net and pole passage uses the Radon continuous-net integral theorem.\n\nThis is uniform integrability for each fixed bounded-test measure. Arbitrary finite-full-dual measure tails without additional domination, arbitrary-coordinate-limit representability, upper-envelope regularity, actual energy-sublevel compactness and arbitrary-support equation existence remain OPEN. No countable dense set, countable cofinal net or full-support Radon measure on the actual nonmetrizable space is presumed.\n\nThe entire new unique math body was physically ROOT read. The exact whole402 mathematical body is retained as its bounded gradient/product/energy foundation; identity is not another independent audit or correctness grant. Whole immediate CLD5.10.1/2 tropical integration and14.5.2/3 calibration readings are qualified, alongside exact GR classical recognition/extension/annulus maximum applications. Deeper recursive foundations remain named citations. Full primary bodies/literal units/pixels/book contexts stay LOCALONLY and are not uploaded. Our own paper/helpers and qualified compiler/source/binding metadata are published. Compilation and hashes do not certify mathematics.\n\nAll new claims UNREVIEWED; counts16/42 solved,26OPEN,97accepted scoped papers unchanged. Native282 independently continues its frozen research. Native283 has settled and its actual FINAL is retained, but its mathematics is not yet ROOT physically read and is excluded from this checkpoint. At mostTWO campaigns, without hot feedback or active mathematical inspection. The protected P16.4 editor remains OPEN UNCHANGED. NONFORCE publication requires whole native Git tree identity and all remote file/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation291/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint Gauss skeleton bounds and bounded-test uniform tail working paper',scope='Whole compiled UNREVIEWED407 with qualified own source/application/compiler/binding records. Actual arbitrary-limit compactness remains OPEN; primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation291.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]; task_env=dict(os.environ); task_env['GIT_INDEX_FILE']=str(G/'native-continuation291.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=task_env,capture_output=True,check=True)
entries=[]; groups={}
for e in items:
    data=Path(e['local']).read_bytes(); data.decode('utf-8'); assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h)); groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=task_env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=task_env,capture_output=True,text=True,check=True).stdout.strip()
A=G/'api-recovery-continuation291'; A.mkdir(); chunks=[]; chunk=[]; size=0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text()); n=len(json.dumps(item,ensure_ascii=False).encode())
    if chunk and size+n>250000: chunks.append(chunk); chunk=[]; size=0
    chunk.append(item); size+=n
if chunk: chunks.append(chunk)
for i,ch in enumerate(chunks): write(A/f'content-chunk-{i}.json',dict(tree=ch))
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),content_chunks=len(chunks),expected_tree=expected,source_bodies_published=False),indent=2))
