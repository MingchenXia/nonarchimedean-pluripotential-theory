from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation292-publication-records';M=G/'upload-manifest-continuation292.json'
D=K/'public-P12.3-continuation408-canonical-obstacle-filtration-and-finite-generation-envelopes-unreviewed'
C=R/'campaigns/round-284/P12.3-whole408-canonical-filtration-and-general-envelope-residual'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation291.json')
assert prior['commit_sha']=='9e02dab574529993f85c368ef73c79ecab8d8517' and prior['tree_sha']=='92486881d6b0c09c0ad0b4cbae2bc909f584da28' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(D/'ROOT-whole-proof-source-scope-and-binding.json')
assert b['paper']==408 and b['compiler']['kind']=='unknown' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
assert sha(Path(b['whole_paper']['path']))==b['whole_paper']['sha256']
paths=[p for p in sorted(D.iterdir()) if p.is_file()]
paths += [R/x for x in ['audit_and_stage_whole_native283_paper408_ROOT_20261009.py','inspect_native283_actual_expanded_differences_ROOT_20261009.py','retain_ROOT408_actual_unknown_compilation_and_scope_20261009.py','capture_terminal_native282283_actual_FINAL_20261009.py','read_terminal_native283_whole_actual_notes_20261009.py','prepare_native284_whole408_canonical_obstacle_and_general_CE_residual_20261009.py','launch_frozen_native284_checked_20261009.py','record_verified_checkpoint291_20261009.py']]
paths += [G/'push-receipt-continuation291.json',Path(__file__)]
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
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==291 and x['current_active_batch']==[284]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=292,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify regular NONFORCE292 whole408 canonical-filtration/rational-attainment proof, compiler UNKNOWN qualified. ROOT reconstructs terminal282 ordered energy-gap and sequence-generated arbitrary-net closure as409. Native284 continues general original P12.3 CE. At mostTWO, unchanged counts/editor.');write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[284],terminal_native_campaigns=[282,283],terminal282_actual_fields_ROOT_read_but_full_formal_proof_not_yet_read=True,terminal282_math_NOT_published_in_this_checkpoint=True,new_papers=[408],compiler='unknown; no source errors reported; source preserved; success NOT claimed',UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint292: canonical obstacle filtration and finite-generation envelopes\n\nWhole UNREVIEWED paper408 constructs primary canonical ideals in EVERY degree for every finite continuous signed obstacle on an excellent reduced germ, keeping ALL semivaluation supports. Their raw geometric envelope is the full degree asymptotic limit. Obstacle-specific finite generation is equivalent to rational unit/primary attainment and finite canonical-max attainment, and gives uniform all-support O(1/m) error. Continuity is equivalent to uniform canonical convergence; finite generation is NOT necessary for continuity, as the irrational DVR example proves. Exact gauges, actual decreasing obstacles, conditional EVERY-fibre conductor descent and explicit nonmonomial any-field/mixed examples are preserved. General arbitrary-obstacle CE and approximation density remain OPEN.\n\nFour actual five-field FINALs and every distinct expanded current proof were ROOT physically read. Full standalone/companion component identity is verified; repeated inherited bodies are retention, not a new whole historical independent proof/source audit. Only the entire qualifiedG331 is an incoming native grant. Fresh whole SH1.1.5 and6.8.1--4 immediate units and actual PDF153--154 pixels were checked; deeper conventional excellent/Nagata foundations are named. All primary bodies/literal units/pixels/book contexts remain LOCALONLY and excluded. Published bodies are our own proofs and qualified scope/binding/compiler metadata.\n\nBuilt-in compilation returned UNKNOWN on three attempts without source errors. Source is preserved unchanged; successful compilation is NOT claimed. Native284 is running through the explicitly requested signed-in official OpenAI Codex path invoked by local Xean. Native282 has settled and its actual fields are read, but the full formal proof is not yet ROOT read/reconstructed and its mathematics is excluded. Original counts16/42 solved,26OPEN,97accepted scoped papers unchanged. No new acceptance. At mostTWO campaigns; protected P16.4 editor OPEN UNCHANGED. NONFORCE publication verifies all remote file/tree/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation292/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint canonical obstacle filtration and finite-generation envelope working paper',scope='Whole UNREVIEWED408; built-in compiler UNKNOWN/source unchanged. All-support scoped proofs, general CE OPEN, primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation292.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation292.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
A=G/'api-recovery-continuation292';A.mkdir();chunks=[];chunk=[];size=0
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
