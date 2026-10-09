from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation287-publication-records';M=G/'upload-manifest-continuation287.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation286.json')
assert prior['commit_sha']=='f6179edfdefcf078c5df4e52c51aebb89c241b98' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
paths=[]
for label in ['public-P16.7-continuation400-countable-monotone-closure-and-actual-operator-continuity-unreviewed','public-P12.3-continuation401-toric-weight-envelopes-and-primary-correction-obstruction-unreviewed']:
    d=K/label;b=load(d/'ROOT-whole-proof-source-scope-and-binding.json')
    assert not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='success'
    for e in b['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
    paths += [p for p in sorted(d.iterdir()) if p.is_file()]
paths += [K/'ROOT400-native-editor-compiler-success-20261009.json',K/'ROOT401-native-editor-compiler-success-20261009.json']
for n,label in [(280,'P16.7-whole400398399-unbounded-uniqueness-and-compactness'),(281,'P12.3-whole401-toric-and-general-envelope-residual')]:
    c=R/f'campaigns/round-{n}'/label;f=load(c/'freeze.json');l=load(c/'launch-record.json')
    assert l['public_status']['calls']['admitted']==1 and not l['initialization_pending']
    for name in ['settings.json','mathematical-packet-bindings.json']:assert sha(c/name)==f[name.replace('.json','').replace('-','_')+'_sha256']
    paths += [c/name for name in ['freeze.json','launch-record.json','settings.json','mathematical-packet-bindings.json']]
helpers=['retain_ROOT400_actual_compile_success_20261009.py','retain_ROOT401_actual_compile_success_20261009.py','capture_terminal_native278_actual_FINAL_20261009.py','capture_terminal_native279_actual_FINAL_20261009.py','read_terminal_native278_whole_actual_notes_20261009.py','read_terminal_native279_whole_actual_notes_20261009.py','audit_terminal_native278_whole_serializations_ROOT_20261009.py','audit_terminal_native279_whole_serializations_ROOT_20261009.py','stage_whole_native278_toric_envelopes_paper401_ROOT_20261009.py','stage_whole_native279_countable_closure_paper400_ROOT_20261009.py','prepare_native280_whole400398399_and_unbounded_residual_20261009.py','prepare_native281_whole401_toric_and_general_envelope_residual_20261009.py','launch_frozen_native280_checked_20261009.py','launch_frozen_native281_checked_20261009.py','record_verified_checkpoint286_20261009.py']
paths += [R/name for name in helpers]+[G/'push-receipt-continuation286.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst=F/'frozen-files'/rel;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dst);assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name;x=load(p);assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==286 and x['current_active_batch']==[280,281]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=287,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify287 whole countable closure400 and whole toric-envelope401 plus terminal audits and frozen native280281. Continue actual original residual proofs at mostTWO; no countchange, protected editor OPEN UNCHANGED.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[280,281],new_papers=[400,401],UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint287: whole countable monotone closure and toric-weight envelope working papers\n\nPaper400 proves countable energy-bounded monotone closure by an actual constrained continuous decreasing diagonal, with energy/operator/moment continuity and summable convex-series closure. It does not prove arbitrary-family compactness or full unbounded uniqueness. Entire actual native279 five-field notes equal expanded notes; only terminal artifact-path tails are distinct. Paper401 retains the whole corrected formal BIG/isolated envelope audit and adds genuine positive envelopes for every continuous monomial-weight obstacle on complete normal toric germs over ANY field among ALL geometric competitors, and a normal nonisolated obstruction to one universal primary subadditivity correction. That obstruction is not a CE counterexample. Entire native278 actual notes differ from expansion only by two TeX spacing-command backslashes in n2; both exact versions retained.\n\nBoth complete standalone sources compiled successfully with the built-in editor compiler. Entire notes/unique mathematical framing/ledgers were ROOT physically read; exact full qualified appendices are inherited identities, not extra fresh historical-source readings. Native source-reading reports are qualified evidence, not a second fresh recursive ROOT audit. All native/supplied programs are DATA and were never imported or executed by ROOT. Full primary bodies/literal units/pixels/book contexts remain LOCALONLY. Source-body hashes do not certify correctness.\n\nALL new mathematics remains UNREVIEWED. Counts16/42 solved,26OPEN,97accepted scoped papers. Original P12.3 andP16.7 remain OPEN. Fresh immutable native280281 use the existing signed-in Xean Codex gpt-6.1-sol xhigh path, at mostTWO campaigns, with whole current mathematical bodies and unchanged original criteria. No hot feedback, active mathematics inspection, authentication/proxy/CA change, or protected P16.4 editor modification. NONFORCE publication requires independent native Git tree and every remote blob/ref verification.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation287/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint whole monotone closure and toric envelope working papers with frozen research continuations',scope='Whole UNREVIEWED400401 plus exact actual/expanded/terminal audits and native280281 freezes; no original closure/countchange; primary bodies/pixels/books LOCALONLY.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation287.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]
task_env=dict(os.environ);task_env['GIT_INDEX_FILE']=str(G/'native-continuation287.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=task_env,capture_output=True,check=True)
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=task_env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=task_env,capture_output=True,text=True,check=True).stdout.strip()
A=G/'api-recovery-continuation287';A.mkdir();chunks=[];chunk=[];size=0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());n=len(json.dumps(item,ensure_ascii=False).encode())
    if chunk and size+n>250000:chunks.append(chunk);chunk=[];size=0
    chunk.append(item);size+=n
if chunk:chunks.append(chunk)
for i,ch in enumerate(chunks):write(A/f'content-chunk-{i}.json',dict(tree=ch))
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),content_chunks=len(chunks),expected_tree=expected,source_bodies_published=False),indent=2))

