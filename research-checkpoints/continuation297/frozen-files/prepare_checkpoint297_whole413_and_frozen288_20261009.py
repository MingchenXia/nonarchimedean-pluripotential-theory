from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation297-publication-records';M=G/'upload-manifest-continuation297.json'
D=K/'public-P12.3-continuation413-algebraic-field-and-Frobenius-root-envelope-descent-unreviewed'
B=D/'ROOT-whole-proof-source-scope-and-binding.json'
C=R/'campaigns/round-288/P12.3-whole413-general-excellent-and-characteristic-envelope-residual'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation296.json')
assert prior['commit_sha']=='950fb067dc6af402bf0c34225a728971cf093b2f' and prior['tree_sha']=='754d99e453dc004c2b02142f5e6f88c5c5f318c3' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(B);assert b['paper']==413 and b['compiler']['kind']=='success' and not b['accepted'] and not b['original_closed']
for e in b['public_files']:assert sha(e['path'])==e['sha256']
f=load(C/'freeze.json');launch=load(C/'launch-record.json')
assert f['only_grants']==['G331'] and f['round']==288 and launch['model']=='gpt-6.1-sol' and launch['reasoning']=='xhigh'
paths=[Path(e['path']) for e in b['public_files']]+[B]
paths += [C/n for n in ['freeze.json','settings.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [R/n for n in ['audit_and_stage_native286_whole_paper413_ROOT_20261009.py','retain_ROOT413_actual_compilation_and_scope_20261009.py','prepare_native288_whole413_general_excellent_envelope_residual_20261009.py','launch_frozen_native288_checked_20261009.py','read_terminal_native286_whole_actual_notes_20261009.py','record_verified_checkpoint296_20261009.py']]
paths += [G/'push-receipt-continuation296.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    x=load(R/name)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==296 and x['current_active_batch']==[287,288]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p)
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=297,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE297 whole compiled413 separable-field/Frobenius-root geometric envelope descent and frozen288 qualified metadata. Native287/288 continue original P16.7/P12.3. ROOT independently advances universal P16.7 variational measure limits from settled411412, no active mathematics inspection or hot feedback. At mostTWO, counts/editor unchanged.');write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[287,288],terminal_native_campaigns=[286],new_papers=[413],compiler='success',terminal286_all_five_actual_fields_and_all_distinct_expanded_proofs_ROOT_physically_read=True,active_native_math_NOT_read_or_published=True,UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint297: algebraic field and Frobenius-root geometric envelope descent\n\nWhole compiled UNREVIEWED ROOT413 independently reconstructs the current canonical/smooth/finite quotient arguments and adds complete scoped algebraic descent proofs. For geometrically integral/normal rational-point finite-type local domains, separable coefficient extension gives the inverse-limit boundary and FULL profinite Galois orbits on EVERY fibre. Trace-dual coefficient extraction descends actual invariant ideals without dividing by group order. Canonical ideals commute in EVERY degree, so raw compatible envelopes, continuity and uniform canonical errors descend without a field-degree loss; finite generation equivalence retains its fixed-obstacle scope. The resulting all-continuous-signed-obstacle CE theorem applies to geometric finite smooth quotient rational germs over ANY characteristic-zero field, including actual normal nonisolated examples over Q, using BFJ ONLY after algebraic closure.\n\nFor finite S^q subset R, q=p^e, and the specified Noetherian unbounded-root extensions, actual semivaluation coordinates and primary-ideal Frobenius expressions identify EVERY support, geometric C and actual decreasing D. Raw envelopes commute for ALL obstacles. Finite purely inseparable normal-domain extensions and perfection of geometrically normal rational finite-type germs over imperfect fields are included. Positive-characteristic CE is explicitly CONDITIONAL on source regularity; the quantitative rate has its precise source hypothesis. Mixed characteristic and arbitrary excellent normal singularities beyond the covered source class remain OPEN.\n\nAll five actual notes including all five fields and all five distinct expanded TeX proofs, entire unique ledger/verdict/residual and formal preamble were ROOT physically read. The whole source and3.3MB companion were reconstructed exactly, with inherited repeated retention distinguished from a fresh recursive audit. Complete immediate SH/BFJ units and actual SH formula PDF153154 pixels were freshly ROOT read/viewed; named deeper foundations remain qualified. All four native programs were physically read solely as DATA and never executed/imported. Full primary literal bodies/pixels/books LOCALONLY. Compiler success validates typesetting, not mathematical acceptance.\n\nNative287 and288 continue the user-selected signed-in official OpenAI Codex CLI gpt-6.1-sol xhigh through local Xean, at mostTWO. Only freeze/settings/launch/math-binding metadata of288 are included; active mathematics is neither read nor published. Original criteria and residual unchanged. Counts16/42 solved,26OPEN,97accepted scoped papers unchanged; no new acceptance. Protected P16.4 editor OPEN UNCHANGED. NONFORCE update verifies remote blob/tree/file/ref bindings.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation297/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint field and Frobenius-root descent for geometric obstacle envelopes',scope='Whole compiled UNREVIEWED ROOT413; original general excellent/positive/mixed-characteristic CE OPEN, primary bodies LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation297.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation297.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API=G/'api-recovery-continuation297';API.mkdir();chunks=[];chunk=[];size=0
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
