from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
F=G/'continuation285-publication-records'; M=G/'upload-manifest-continuation285.json'
assert not F.exists() and not M.exists()
sha=lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p: json.loads(Path(p).read_text())
def write(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
prior=load(G/'push-receipt-continuation284.json'); assert prior['commit_sha']=='d2a8d1809109dbe2cfc92e69b30fb625d0c80ec7'
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified']) and not prior['force_update']
paths=[]
for name in ['public-P12.3-continuation396-corrected-formal-BIG-and-isolated-CE-unreviewed','public-P16.7-continuation397-generated-operator-and-all-test-I-estimate-unreviewed']:
    d=K/name; b=load(d/'ROOT-whole-proof-source-scope-and-binding.json')
    assert not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='success'
    for e in b['public_files']: assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
    paths += [p for p in sorted(d.iterdir()) if p.is_file()]
paths += [K/'round276277-ROOT-whole-serialization-and-unique-framing-audit-20261009.json',K/'round276277-ROOT-fresh-primary-application-and-compilation-scope-20261009.json',R/'stage_whole396397_with_ROOT_convention_correction_20261009.py',R/'retain_ROOT396397_actual_primary_units_and_compilation_bindings_20261009.py',R/'audit_terminal_native276277_whole_serializations_ROOT_20261009.py',R/'prepare_native278279_whole396397_and_classical_bridge_20261009.py',R/'launch_frozen_native278279_checked_20261009.py',R/'record_verified_checkpoint284_20261009.py',G/'push-receipt-continuation284.json',Path(__file__)]
campaigns=[R/'campaigns/round-278/P12.3-whole396-corrected-formal-CE-and-original-residual',R/'campaigns/round-279/P16.7-whole397394395-full-uniqueness-and-compactness']
launches=[]
for c in campaigns:
    l=load(c/'launch-record.json'); assert l['public_status']['status']=='running' and l['public_status']['calls']['admitted']==1
    launches.append(l)
    paths += [c/'freeze.json',c/'settings.json',c/'launch-record.json',c/'mathematical-packet-bindings.json']
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir()
for p in paths:
    rel=p.relative_to(R); assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    assert p.suffix not in ['.sqlite','.log','.pdf','.png','.html']
    dst=F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name; x=load(p); assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==284
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=285,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify285 whole corrected396 and expanded397 plus exact actualFINALs/source/compiler qualification and native278279 launches. Continue mathematical originals at mostTWO, no active-math inspection/hot feedback; no countchange.')
    write(p,x)
summary=dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=x['current_active_batch'],new_papers=[396,397],new_papers_UNREVIEWED=True,original_closed=False,accepted=False,protected_editor_OPEN_UNCHANGED=True,all_full_primary_source_bodies_units_pixels_whole_books_LOCALONLY=True,authoritative_full_local_catalogues=[str(R/'active-work.json'),str(R/'checklist-current.json')])
write(F/'current-research-status.json',summary)
(F/'README.md').write_text('Checkpoint285: entire corrected formal BIG/isolated CE and analytic all-test strictness papers\n\nWhole396 explicitly repairs root-source d versus underlying Frobenius-source d^q in immutable native276. The complete corrected paper, original seven actual notes, expanded framing and full proof/ledgers remain separate. Whole397 retains five actual native277 FINAL notes separately from all FIVE DIFFERENT expanded proofs, complete companion and source-qualified all-test I estimate with coefficient42 plus bounded divisor-current consequence. Both standalone ROOT copies compiled successfully using the native editor compiler; compilation is not mathematical certification.\n\nAll claims UNREVIEWED. Original P12.3 and P16.7 remain OPEN; 16/42 solved,26OPEN,97accepted scoped papers unchanged. Independent native278 and279 use user-selected existing signed-in Codex gpt-6.1-sol xhigh, at mostTWO, with complete frozen proofs and original criteria. New ROOT394395 classical/Shilov bridge enters only the new279 freeze. No active campaign mathematics read or hot feedback.\n\nThe immediate CEMS and Stacks applications and entire CLD Poincare-Lelong statement/immediate proof were freshly ROOT read with exact literal-LF/version qualification. Full primary sources, literal source units, actual pixels and whole-book chapters stay LOCALONLY. Public items contain own/native mathematical drafts and qualified metadata, not source bodies. Supplied/native programs are inert. Protected P16.4 editor OPEN UNCHANGED. NONFORCE Git publication requires exact native tree, all remote file blobs and branch verification.\n')
files=[]
for p in sorted(F.rglob('*')):
    if p.is_file(): files.append(dict(local=str(p),path='research-checkpoints/continuation285/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)))
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=x['fully_solved_original_atoms'],remaining_open_atoms=26,historical_reviewed_scoped_papers=97,commit_message='Checkpoint corrected formal CE and analytic all-test strictness papers; launch native278279',scope='Entire UNREVIEWED working papers/actual versus expanded FINALs/qualified source and compiler metadata/frozen launches. Full source bodies and whole books LOCALONLY. No closure/acceptance/editor change. Compact public status avoids duplicating megabyte local catalogues.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation285.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]
base_tree=prior['tree_sha']; entries=[]; groups={}
task_env=dict(__import__('os').environ); task_env['GIT_INDEX_FILE']=str(G/'native-continuation285.index')
subprocess.run(git+['read-tree',base_tree],env=task_env,capture_output=True,check=True)
for e in items:
    data=Path(e['local']).read_bytes(); data.decode('utf-8'); assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entry=dict(path=e['path'],mode='100644',type='blob',sha=h); entries.append(entry); groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=task_env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=task_env,capture_output=True,text=True,check=True).stdout.strip()
A=G/'api-recovery-continuation285'; A.mkdir(); chunks=[]; chunk=[]; size=0
for h,e in groups.items():
    content=Path(e['local']).read_text(); item=dict(path=h,mode='100644',type='blob',content=content); n=len(json.dumps(item,ensure_ascii=False).encode())
    if chunk and size+n>250000: chunks.append(chunk); chunk=[]; size=0
    chunk.append(item); size+=n
if chunk: chunks.append(chunk)
for i,ch in enumerate(chunks): write(A/f'content-chunk-{i}.json',dict(tree=ch))
plan=dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=base_tree,expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),commit_message=load(M)['commit_message'],force=False)
write(A/'connector-plan.json',plan)
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),unique_text_blobs=len(groups),content_chunks=len(chunks),expected_tree=expected,source_bodies_published=False),indent=2))
