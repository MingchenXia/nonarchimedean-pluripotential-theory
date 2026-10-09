"""Freeze WHOLE four papers and next-task metadata with bounded exact transport."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation311-publication-records';A=G/'api-recovery-continuation311';M=G/'upload-manifest-continuation311.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not A.exists() and not M.exists()
prior=load(G/'push-receipt-continuation310.json')
assert prior['commit_sha']=='4a6c9682257ba9124490e399b631c6b2435a8526' and prior['tree_sha']=='98399a91137fd4de701806dcc0f34e451a80a182' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for n in ['active-work.json','checklist-current.json']:
    y=load(R/n);assert y['current_active_batch']==[300,301] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==310
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
domains=[K/'public-P12.3-continuation435-normal-finite-cover-maxima-and-reduced-compatibility-unreviewed',K/'public-P16.7-continuation436-two-residue-radon-and-family-limit-unreviewed']
paths=[]
for d in domains:
    z=load(d/'ROOT-whole-proof-source-scope-and-binding.json');assert not z['accepted'] and not z['original_closed']
    for e in z['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
    paths+=sorted(p for p in d.iterdir() if p.is_file())
for n in [434,437]:
    b=K/f'P16.7-continuation{n}-ROOT-whole-paper-source-scope-and-binding-20261009.json';z=load(b)
    assert not z['accepted'] and not z['original_closed']
    for e in z['public_files']:
        assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes'];paths.append(Path(e['path']))
    paths.append(b)
for n,suffix in [(300,'P12.3-whole435-normal-nonisolated-and-conductor-classification'),(301,'P16.7-whole434436437-isotropic-dirac-and-actual-recognition')]:
    c=R/f'campaigns/round-{n}'/suffix
    paths+=[c/name for name in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [R/n for n in ['stage_native298_whole_ROOT435_normal_finite_cover_20261009.py','stage_native299_whole_ROOT436_two_residue_20261009.py','retain_ROOT434_whole_quadratic_pencil_dirac_20261009.py','retain_ROOT437_whole_angle_degeneration_20261009.py','prepare_native300301_whole_current_small_batch_20261009.py','launch_frozen_native300301_checked_20261009.py','record_verified_checkpoint310_v2_20261009.py']]
paths += [G/'push-receipt-continuation310.json',Path(__file__)]
assert len(paths)==len(set(paths))
F.mkdir();A.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    q=F/'frozen-files'/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);assert sha(q)==sha(p)
now=datetime.now(timezone.utc).isoformat()
write(F/'current-research-status.json',dict(recorded_utc=now,solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[300,301],new_papers=[434,435,436,437],UNREVIEWED=True,accepted=False,original_closed=False,whole434_quadratic_degree2_Dirac_and_mass2_Radon_sector=True,whole435_NORMALfinitecover_envelopes_and_reducedconductorcriterion=True,whole436_actual299ALLthreeALLfivefields_and_corrected565LF_proof_read=True,whole437_angledegeneration_oldisotropic_dual_bound=[3/8,1/2],oldisotropic_Dirac_existence_OPEN=True,original_P12_3_P16_7_OPEN=True,full_current_recursive_source_book_geometry_descent_audit_INCOMPLETE=True,retention_hashing_NOTreading_or_correctness_credit=True,compiler_UNVERIFIED=True,active300301_math_NOTread_or_published_or_hotfed=True,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F/'desktop-compiler-observations.json',dict(recorded_utc=now,paper434='Actual built-in request35 pending',paper435='Actual built-in request50 pending',paper436='Actual built-in request71 pending',paper437='Actual built-in request78 pending',compiler_verified=False,no_success_observed=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint311: finite-cover envelopes and angular Dirac degeneration\n\nComplete UNREVIEWED working papers434435436437, current actual notes in all fields, formal sources, source-application ledgers, exact original task/residuals and frozen native300301 metadata are preserved. Original problems remain OPEN; counts16/42 solved,26OPEN,97acceptedscopedpapers. No mathematical acceptance or compiler success is asserted.\n\n434 gives actual positive quadratic pencils with entire rawmass2 at one unequal-radius linear-coordinate Gauss point, a degree-two whole-fibre calculation, and an actual mass-two Radon branch. 435 gives full-support characteristic-coefficient fibre maxima and raw C/D finite-cover envelope transfer over NORMAL domains, anycharacteristic; reduced normalization compatibility is exact under its disclosed continuous-source/density hypotheses. There is no universal regular cover or general higher-dimensional normal continuity theorem. 436 retains settled299 ALLthree notes ALLfivefields and the expanded analytic proof; its reader explicitly adds the required norm-one centre condition, while exact native material remains unchanged. Two distinct residue branches carry all nonskeletal mass; weak coalescence is obstructed only in that family. Native solver claims about missing nested services are distinguished from the completed official host Xean call. 437 proves actual angular Gauss convergence and improves the oldisotropic wholeDirac full-dual bound to3/8<=D<=1/2 atdepth1/8. Its uniformlybounded unordered pointwise potentials have different MA/energy limits; convexaverages convergeuniformly with exacterrora/N. Solvedweakapproximation equations have limiting-target objectivegap>=a and supply no maximizingsequence/existence.\n\nEvery current formal proof and current actual-note fields/scopes were physically read in bounded untruncated outputs; each paper keeps exact applied primary and deeper-audit qualifications. Whole historical companions are retained as DATA, not claimed wholly read or correct. Literal primary bodies/pixels/books remain LOCALONLY. The built-in compiler requests35/50/71/78 remain pending/unverified. ProtectedP16.4editor stays open unchanged. Native300301 each use the requested official signed-in Xean native Codex gpt-6.1-sol xhigh, at most two active; no active mathematics inspected or fed back.\n\nLarge public mathematical bodies are byte-exact ordered UTF-8 parts. Reconstruct each whole body by concatenating its ordered parts WITHOUT separators or added newlines, as bound in whole-body-reconstruction.json and the upload manifest. Original frozen whole files remain locally intact. All connector arguments are bounded below200000bytes. NONFORCE publication requires independent native Git root, every remote path/blob and parent/commit/final-ref verification; publication gives no mathematical reading or acceptance credit.\n')
files=[];splits=[]
for p in sorted((F/'frozen-files').rglob('*'))+[F/'current-research-status.json',F/'desktop-compiler-observations.json',F/'README.md']:
    if not p.is_file():continue
    rel=str(p.relative_to(F));remote='research-checkpoints/continuation311/'+rel
    original=dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p))
    if p.stat().st_size<=150000:files.append(original);continue
    data=p.read_bytes();off=0;indices=[];folder=F/'parts'/f'{len(splits):02d}';folder.mkdir(parents=True)
    while off<len(data):
        end=min(off+150000,len(data))
        while end<len(data) and data[end]&192==128:end-=1
        body=data[off:end];body.decode('utf-8');q=folder/f'part-{len(indices)+1:03d}.txt';q.write_bytes(body)
        indices.append(len(files));files.append(dict(local=str(q),path=remote+'.parts/'+q.name,bytes=len(body),sha256=sha(q)));off=end
    assert b''.join(Path(files[i]['local']).read_bytes() for i in indices)==data
    splits.append(dict(original=original,ordered_file_indices=indices,whole_body_retained=True,whole_public_body_byteexact_across_parts=True,reading_credit=False))
reconstruction=F/'whole-body-reconstruction.json';write(reconstruction,dict(recorded_utc=now,split_files=[dict(original=x['original'],ordered_part_paths=[files[i]['path'] for i in x['ordered_file_indices']]) for x in splits],instruction='Concatenate exact UTF-8 bytes in order WITHOUT added separators/newlines.',retention_NOTreading_or_correctness=True))
files.append(dict(local=str(reconstruction),path='research-checkpoints/continuation311/whole-body-reconstruction.json',bytes=reconstruction.stat().st_size,sha256=sha(reconstruction)))
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),whole_body_binding=splits,solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint full nonskeletal Dirac pencils, angular bounds and finite-cover envelopes',scope='WHOLE UNREVIEWED434435436437 andfrozen300301; active300301math excluded, compilerunverified, originalOPEN.',force=False,connector_argument_limit_bytes=200000))
assert M.stat().st_size<=150000
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation311.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation311.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
old_rows=subprocess.run(git+['ls-tree','-r',prior['tree_sha']],capture_output=True,text=True,check=True).stdout.splitlines();existing={s.split()[2] for s in old_rows if s.split()[1]=='blob'}
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf-8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
chunks=[];batch=[]
for h,e in groups.items():
    if h in existing:continue
    x=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text())
    candidate=batch+[x];size=len((json.dumps(dict(tree=candidate),ensure_ascii=True,indent=2)+'\n').encode())
    if batch and size>190000:chunks.append(batch);batch=[]
    batch.append(x)
    assert len((json.dumps(dict(tree=batch),ensure_ascii=True,indent=2)+'\n').encode())<200000
if batch:chunks.append(batch)
sizes=[];tree_shas=[]
for i,ch in enumerate(chunks):
    p=A/f'content-chunk-{i}.json';p.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2)+'\n');sizes.append(p.stat().st_size)
    body=b''.join(b'100644 '+e['path'].encode()+b'\0'+bytes.fromhex(e['path']) for e in sorted(ch,key=lambda e:e['path']))
    tree_shas.append(hashlib.sha1(b'tree '+str(len(body)).encode()+b'\0'+body).hexdigest())
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=sizes,content_tree_shas=tree_shas,unique_blobs=len(groups),reused_parent_blobs=sum(h in existing for h in groups),commit_message=load(M)['commit_message'],force=False))
for n in ['active-work.json','checklist-current.json']:
    p=R/n;y=load(p);y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=311,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],expected_tree=expected,push_complete=False,bounded_transport=True));write(p,y)
print(json.dumps(dict(manifest=str(M),manifest_bytes=M.stat().st_size,manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),unique_blobs=len(groups),reused_parent_blobs=sum(h in existing for h in groups),content_chunks=len(chunks),max_chunk_bytes=max(sizes),split_bodies=len(splits),split_parts=sum(len(x['ordered_file_indices']) for x in splits),expected_tree=expected),indent=2))
