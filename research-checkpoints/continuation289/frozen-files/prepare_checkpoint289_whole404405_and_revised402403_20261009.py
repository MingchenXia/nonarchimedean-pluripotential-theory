from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R = Path('/workspace/research'); K = R/'root-checks'; G = R/'github-checkpoint'
F = G/'continuation289-publication-records'; M = G/'upload-manifest-continuation289.json'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text())
def write(p, x): p.write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n')
assert not F.exists() and not M.exists()
prior = load(G/'push-receipt-continuation288.json')
assert prior['commit_sha']=='b1a3de693bbfae52f95de50e2bfc5285b6bcf63a' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
paths = []
for number, dirname in [(404,'public-P16.7-continuation404-finite-extension-and-unbounded-probe-currents-unreviewed'),(405,'public-P12.3-continuation405-excellent-germ-contact-and-nonmonomial-envelopes-unreviewed')]:
    directory = K/dirname; binding = directory/'ROOT-whole-proof-source-scope-and-binding.json'; b = load(binding)
    assert b['paper']==number and not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='success'
    for e in b['public_files']:
        p = Path(e['path']); assert p.parent==directory and sha(p)==e['sha256'] and p.stat().st_size==e['bytes']; paths.append(p)
    assert set(paths[-len(b['public_files']):]+[binding])==set(p for p in directory.iterdir() if p.is_file())
    paths.append(binding)
for number in [402,403]:
    binding = K/f'P16.7-continuation{number}-ROOT-whole-paper-source-scope-and-binding-20261009.json'; b = load(binding)
    assert not b['accepted'] and not b['original_closed'] and b['compiler']['kind']=='success'
    e = b.get('whole_paper', b.get('paper')); paper = Path(e['path'])
    assert sha(paper)==e['sha256'] and paper.stat().st_size==e['bytes']
    scope = Path(b['source_scope']['path']); assert sha(scope)==b['source_scope']['sha256']
    paths.extend([binding,paper,scope])
paths.extend(K/name for name in ['ROOT402403-GR-source-designation-only-revision-20261009.json','round280281-ROOT-whole-serialization-and-first-mathematical-scope-audit-20261009.json','ROOT404-native-editor-compiler-success-20261009.json','ROOT405-native-editor-compiler-success-20261009.json'])
paths.extend(R/name for name in ['read_terminal_native280281_whole_actual_notes_20261009.py','audit_and_stage_whole_native280281_papers404405_ROOT_20261009.py','retain_ROOT404405_actual_compiler_success_20261009.py','retain_ROOT402403_exact_GR_citation_revision_20261009.py','prepare_native282_whole402403404_generated_unique_and_compactness_20261009.py','prepare_native283_whole405_contact_and_arbitrary_envelope_residual_20261009.py','launch_frozen_native282283_checked_20261009.py','record_verified_checkpoint288_20261009.py'])
for number, label in [(282,'P16.7-whole402403404-generated-uniqueness-and-compactness'),(283,'P12.3-whole405-contact-and-arbitrary-envelope-residual')]:
    c = R/f'campaigns/round-{number}'/label; freeze = load(c/'freeze.json'); launch = load(c/'launch-record.json')
    assert launch['round']==number and launch['model']=='gpt-6.1-sol' and launch['reasoning']=='xhigh'
    assert launch['public_status']['calls']['admitted']==1 and not launch['initialization_pending']
    assert sha(c/'input.json')==freeze['input_sha256']==launch['frozen_input_sha256']
    paths.extend(c/name for name in ['freeze.json','settings.json','launch-record.json','mathematical-packet-bindings.json'])
paths.extend([G/'push-receipt-continuation288.json',Path(__file__)])
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir()
for p in paths:
    rel = p.relative_to(R); assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    dst = F/'frozen-files'/rel; dst.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(p,dst); assert sha(dst)==sha(p)
now = datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p = R/name; x = load(p)
    assert x['github_pending_checkpoint'] is None and x['latest_verified_github_checkpoint']['continuation']==288 and x['current_active_batch']==[282,283]
    assert len(x['fully_solved_original_atoms'])==16 and x['remaining_open_original_atoms']==26 and x['historical_reviewed_scoped_papers']==97
    x.update(updated_utc=now,github_pending_checkpoint=dict(continuation=289,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify289 whole compiled404405 and revised402403, all UNREVIEWED. Native282283 independently audit frozen full proofs and advance original P16.7/P12.3 residuals. ROOT continues actual energy-sublevel compactness/envelopes. At mostTWO campaigns, no hot feedback/count change, protected editor OPEN UNCHANGED.')
    write(p,x)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=x['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[282,283],terminal_native_campaigns=[280,281],new_papers=[404,405],citation_only_revised_papers=[402,403],UNREVIEWED=True,original_closed=False,accepted=False,source_bodies_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True,native_generated_programs_DATA_not_executed_or_imported=True))
(F/'README.md').write_text('Checkpoint289: whole finite-extension/probe-current and excellent-germ contact papers\n\nWhole native-identical standalone papers404405, full proof companions, actual settled native notes, expanded mathematics, source/application ledgers, residuals and qualified ROOT scope/compiler/binding records are preserved. Paper404 develops finite-extension normalization and bounded mixed-measure control of unbounded moment probes; ROOT explicitly corrects the inherited GR theorem labels: Proposition4.2 sheaf/decreasing closure, Theorem6.1 local maximum, Theorem6.4 affinoid Shilov maximum, and no claimed USC-regularization theorem6.4. Paper405 proves a finite-contact obstacle sector for excellent reduced germs, including singular/non-normal and non-monomial equal/mixed-characteristic examples; arbitrary-obstacle CE remains OPEN. Exact inherited body identities are not another independent audit or new support grant.\n\nRevised whole402403 correct only the designation of the smooth recognition statement to the unnumbered argument in GR Section1.2; the mathematics is unchanged. All four current standalone sources compiled successfully. Entire new unique mathematical bodies and actual FINALs were physically ROOT read; primary recursive foundations remain qualified as published citations. Source hashes and compilation do not certify mathematics. Full primary bodies, literal units, source pixels and book-context packets stay LOCALONLY and are excluded here. Native/generated programs were read as DATA and not executed/imported by ROOT.\n\nNative282283 launched through the existing signed-in native OpenAI Codex path with the user-selected gpt-6.1-sol xhigh, exactly one admitted call each and a maximum of TWO concurrent campaigns. This includes frozen metadata, not their active mathematics or source packets. Read-only destination checks established that Xean is a local controller invoking official Codex, not a separate external Xean service. The user explicitly authorized uploading any materials and selected this native path; automatic review accepted both exact launches after those checks. Authentication, credentials, proxy, CA and model endpoint settings stayed unchanged; the child workspace-write sandbox stayed enabled.\n\nAll new claims remain UNREVIEWED; counts remain16/42 solved,26OPEN,97accepted scoped papers. No original P16.7/P12.3 closure, no hot feedback, and the protected P16.4 editor remains OPEN UNCHANGED. NONFORCE publication requires an independent native Git whole-tree identity and all remote file/ref bindings.\n')
files = [dict(local=str(p),path='research-checkpoints/continuation289/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint whole excellent-germ contact and unbounded probe-current working papers',scope='Whole compiled UNREVIEWED404405, citation-only revised402403 and qualified frozen282283 launch metadata; original residuals remain OPEN; primary bodies LOCALONLY.'))
items = files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation289.json',bytes=M.stat().st_size,sha256=sha(M))]
git = ['git','--git-dir='+str(G/'native-continuation56.git')]
task_env = dict(os.environ); task_env['GIT_INDEX_FILE']=str(G/'native-continuation289.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=task_env,capture_output=True,check=True)
entries = []; groups = {}
for e in items:
    data = Path(e['local']).read_bytes(); data.decode('utf-8'); assert hashlib.sha256(data).hexdigest()==e['sha256']
    h = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h)); groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=task_env,capture_output=True,check=True)
expected = subprocess.run(git+['write-tree'],env=task_env,capture_output=True,text=True,check=True).stdout.strip()
A = G/'api-recovery-continuation289'; A.mkdir(); chunks = []; chunk = []; size = 0
for h,e in groups.items():
    item = dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text()); n = len(json.dumps(item,ensure_ascii=False).encode())
    if chunk and size+n>250000: chunks.append(chunk); chunk=[]; size=0
    chunk.append(item); size+=n
if chunk: chunks.append(chunk)
for i,ch in enumerate(chunks): write(A/f'content-chunk-{i}.json',dict(tree=ch))
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),unique_blobs=len(groups),content_chunks=len(chunks),expected_tree=expected,source_bodies_published=False),indent=2))
