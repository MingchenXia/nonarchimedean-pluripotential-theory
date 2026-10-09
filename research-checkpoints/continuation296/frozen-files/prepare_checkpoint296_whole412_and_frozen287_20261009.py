from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation296-publication-records';M=G/'upload-manifest-continuation296.json'
D=K/'public-P16.7-continuation412-nonordered-midpoint-absolute-moments-and-maximum-energy-gains-unreviewed'
B=D/'ROOT-whole-proof-source-scope-and-binding.json'
C=R/'campaigns/round-287/P16.7-whole411412-universal-variational-limits-and-actual-representability'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation295.json')
assert prior['commit_sha']=='974cae4738cff711f09e9e3b32e5748fa8d16094' and prior['tree_sha']=='3b2b0735acd2c311964aa6c0bfcbe7c95b83022c' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(B);assert b['paper']==412 and b['compiler']['kind']=='success' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
f=load(C/'freeze.json');launch=load(C/'launch-record.json')
assert f['only_grants']==[] and f['round']==287 and launch['model']=='gpt-6.1-sol' and launch['reasoning']=='xhigh'
paths=[Path(e['path']) for e in b['public_files']]+[B]
paths += [C/n for n in ['freeze.json','settings.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [R/n for n in ['audit_and_stage_native285_whole_paper412_ROOT_20261009.py','retain_ROOT412_actual_compilation_and_scope_20261009.py','prepare_native287_whole411412_universal_variational_limits_20261009.py','launch_frozen_native287_checked_20261009.py','record_verified_checkpoint295_20261009.py']]
paths += [G/'push-receipt-continuation295.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==295 and x['current_active_batch']==[287]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=296,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),
        next_work='Verify NONFORCE296 whole compiled412 nonordered midpoint/absolute moments/maximum-energy gains and frozen287 qualified metadata. Native287 continues P16.7. ROOT reads ALL terminal286 actual five fields and distinct expanded P12.3 proofs before reconstruction/follow-up. At mostTWO, counts/editor unchanged.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[287],terminal_native_campaigns=[285,286],new_papers=[412],compiler='success',terminal285_actual_and_distinct_expanded_proofs_ROOT_physically_read=True,terminal286_mathematics_NOT_yet_ROOT_read_at_this_freeze=True,terminal286_mathematics_excluded=True,UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint296: nonordered midpoint deficits, absolute moments and maximum-energy gains\n\nWhole compiled UNREVIEWED ROOT412 retains the complete native285 formal paper, actual five-field notes, original companion and precise ROOT clarification of the nonempty grid-test list including w0=0 and A1=0. Exact cubic energy gives midpoint deficit I/8. Calibrated finite Gauss grids control reference absolute moments; smooth absolute-value approximations and signed Radon Green identities control BOTH moving MA absolute moments. Consequently the energy gains of max(a,b), every fixed bounded-MA test moment, and every full-dimension-two point difference vanish with I on a bounded energy sublevel. Every finite-full-dual maximizing family restricted to a fixed energy sublevel is I-Cauchy. Native coercivity and L1(mu) convergence are proved for the finite bounded-MA domination sector; the later separate ROOT411 supplies universal coercivity but was not input to native285.\n\nAll unique actual proofs and the complete expanded formal source were physically read by ROOT. Immediate applied CLD18.6.1,18.6.2 and calibration14.5.2-3 proof bodies were fully read and retained LOCALONLY; deeper named foundations and inherited exact source identities remain qualified, not another independent recursive whole audit. Native programs were read solely as DATA and never executed or imported. Whole source, companion, reading ledger, scope/residual and actual successful compiler result are retained. New native287 has an immutable whole411412 input using the existing signed-in official OpenAI Codex CLI gpt-6.1-sol xhigh through local Xean; only freeze/settings/launch/math-binding metadata are included, no active mathematics or private primary bodies.\n\nActual nonordered analytic representation/compactness, adequate intrinsic recognition, envelopes/orthogonality and every arbitrary-support prescribed-measure existence remain OPEN. Terminal286 mathematics was not yet ROOT read at this freeze and is excluded. Counts16/42 solved,26OPEN,97accepted scoped papers unchanged; no new acceptance. Protected P16.4 editor OPEN UNCHANGED. NONFORCE update verifies remote blob/tree/file/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation296/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint nonordered energy and moving-moment estimates with frozen variational follow-up',scope='Whole compiled UNREVIEWED ROOT412; original analytic representation/envelopes/existence OPEN, primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation296.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation296.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API=G/'api-recovery-continuation296';API.mkdir();chunks=[];chunk=[];size=0
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
