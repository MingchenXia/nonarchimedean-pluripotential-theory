from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation294-publication-records'; M=G/'upload-manifest-continuation294.json'
D=K/'public-P12.3-continuation410-finite-smooth-quotient-continuous-envelopes-unreviewed'
C=R/'campaigns/round-286/P12.3-whole410-general-excellent-envelope-residual'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation293.json')
assert prior['commit_sha']=='ea296f0c4988436141045660ae4ac0d23c6047d1' and prior['tree_sha']=='81bf23aec4971d63ebba4f2df90722bbc66c934b' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(D/'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper']==410 and b['compiler']['kind']=='success' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
assert sha(b['whole_paper']['path'])==b['whole_paper']['sha256']
paths=[p for p in sorted(D.iterdir()) if p.is_file()]
paths += [R/x for x in ['audit_and_stage_native284_whole_paper410_ROOT_20261009.py',
    'retain_ROOT410_actual_compilation_and_scope_20261009.py','capture_terminal_native284_actual_FINAL_20261009.py',
    'read_terminal_native284_whole_actual_notes_20261009.py','prepare_native286_whole410_general_excellent_envelope_residual_20261009.py',
    'launch_frozen_native286_checked_20261009.py','record_verified_checkpoint293_20261009.py']]
paths += [G/'push-receipt-continuation293.json',Path(__file__)]
paths += [C/x for x in ['freeze.json','launch-record.json','settings.json','mathematical-packet-bindings.json']]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==293 and x['current_active_batch']==[285,286]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=294,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),
        next_work='Verify regular NONFORCE294 whole compiled410 finite smooth quotient continuous envelopes. Native285 advances original P16.7 nonordered compactness/existence, native286 original P12.3 general excellent/mixed/imperfect CE. At mostTWO, no active proof inspection/hot feedback, counts/editor unchanged.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,
    accepted_scoped_papers=97,current_active_batch=[285,286],terminal_native_campaigns=[284],new_papers=[410],compiler='success',
    all_actual_five_fields_and_all_distinct_expanded_current_proofs_ROOT_physically_read=True,
    inherited_historical_recursive_audit_complete=False,UNREVIEWED=True,original_closed=False,accepted=False,
    source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint294: continuous geometric envelopes on finite smooth quotient germs\n\nWhole compiled UNREVIEWED paper410 reconstructs the general canonical all-support filtration and finite-generation/rational-attainment criterion. The exact published smooth BFJ model-envelope estimate gives uniform canonical primary approximation without finite generation. Signed-model obstacle density and raw Lipschitz stability then yield every continuous signed obstacle at the smooth affine CLOSED/algebraically closed/characteristic-zero hypotheses. Qualified G331 full-support coefficient trace identifies EVERY finite invariant quotient restriction fibre with a group orbit. The invariant source envelope descends positively, proving arbitrary continuous-obstacle regularity on finite smooth quotients, including actual normal nonisolated A1-product germs. Signed real Cartier model obstacles have a full-degree O(1/m) bound, with no finite-generation hypothesis. An explicit cancellation-sensitive nonlinear signed obstacle is included.\n\nALL four actual five-field FINALs and ALL four distinct expanded TeX proofs, unique preamble/ledger/verdict/residual and complete applied BFJ immediate units were physically ROOT read. Entire251721-byte standalone and2654027-byte companion are reconstructed against complete components; retained historical repetition does not establish a fresh entire historical audit. Only ENTIRE qualified G331 is incoming correctness background; compiler, native/ROOT verdicts and historical papers are DATA. Native programs were read only as DATA and NEVER executed/imported. Deeper Hironaka, multiplier-ideal and Izumi/thinness foundations remain named at their exact smooth hypotheses. Primary literal bodies/units/pixels/books stay LOCALONLY, excluded from publication.\n\nOriginal arbitrary excellent normal/nonisolated, imperfect residue and mixed-characteristic envelope residual remains OPEN. Native286 advances those original gates using frozen whole410; native285 continues P16.7 nonordered compactness/envelopes/existence. Counts16/42 solved,26OPEN,97accepted scoped papers unchanged. No new original closure or acceptance. Protected P16.4 editor OPEN UNCHANGED. NONFORCE update verifies remote blob/tree/file/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation294/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,
    file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,
    commit_message='Checkpoint continuous envelopes on finite smooth quotient germs working paper',
    scope='Whole compiled UNREVIEWED410 with full actual and distinct expanded proofs; original general excellent/mixed/imperfect CE OPEN, primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation294.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation294.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API=G/'api-recovery-continuation294';API.mkdir();chunks=[];chunk=[];size=0
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
