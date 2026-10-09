"""Freeze whole438439440; reuse byte-exact already verified public body parts."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess,os

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
F=G/'continuation312-publication-records';A=G/'api-recovery-continuation312';M=G/'upload-manifest-continuation312.json'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not A.exists() and not M.exists()
prior=load(G/'push-receipt-continuation311.json')
assert prior['commit_sha']=='06ee0bee368eb41cde475c6ad38c06968a86b9d6' and prior['tree_sha']=='1ef6adaf1c7ead43aa75efd85f1c0d988d51139a' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
assert sha(G/'upload-manifest-continuation311.json')==prior['manifest_sha256']
old=load(G/'upload-manifest-continuation311.json');known=[]
for e in old['whole_body_binding']:
    b=Path(e['original']['local']).read_bytes();parts=[old['files'][i] for i in e['ordered_file_indices']]
    assert b==b''.join(Path(p['local']).read_bytes() for p in parts) and hashlib.sha256(b).hexdigest()==e['original']['sha256']
    known.append(dict(body=b,parts=parts))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name);assert y['current_active_batch']==[302,303] and y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==311
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
paths=[]
for domain in ['public-P12.3-continuation439-conductor-centre-obstruction-unreviewed','public-P16.7-continuation440-actual-finite-energy-recognition-unreviewed']:
    d=K/domain;z=load(d/'ROOT-whole-proof-source-scope-and-binding.json');assert not z['accepted'] and not z['original_closed']
    for e in z['public_files']:assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
    paths += sorted(p for p in d.iterdir() if p.is_file())
b=K/'P16.7-continuation438-ROOT-whole-paper-source-scope-and-binding-20261009.json';z=load(b);assert not z['accepted'] and not z['original_closed']
for e in z['public_files']:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes'];paths.append(Path(e['path']))
paths.append(b)
for n,suffix in [(302,'P12.3-whole439-internal-conductor-and-normal-nonisolated'),(303,'P16.7-whole438440-majorant-feasibility-and-isotropic-equation')]:
    c=R/f'campaigns/round-{n}'/suffix
    paths += [c/name for name in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [R/name for name in ['stage_native300301_whole_ROOT439440_20261009.py','capture_terminal_native300301_actual_FINAL_20261009.py','retain_ROOT438_whole_angular_convex_hull_20261009.py','prepare_native302303_whole439440438_20261009.py','launch_frozen_native302303_checked_20261009.py','record_verified_checkpoint311_20261009.py','verify_checkpoint311_public_get_20261009.py']]
paths += [G/'push-receipt-continuation311.json',Path(__file__)]
assert len(paths)==len(set(paths));F.mkdir();A.mkdir()
for p in paths:
    rel=p.relative_to(R);assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    q=F/'frozen-files'/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);assert sha(p)==sha(q)
now=datetime.now(timezone.utc).isoformat()
write(F/'current-research-status.json',dict(recorded_utc=now,solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[302,303],new_papers=[438,439,440],UNREVIEWED=True,accepted=False,original_closed=False,actual300301_final_distinct_from_assembled_separately_retained=True,original_P12_3_P16_7_OPEN=True,full_historical_recursive_source_book_geometry_descent_audit_INCOMPLETE=True,retention_and_reuse_NOT_reading_or_correctness_credit=True,compiler_UNVERIFIED=True,active302303_math_NOTread_or_published_or_hotfed=True,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F/'desktop-compiler-observations.json',dict(recorded_utc=now,pending_actual_request_cells=dict(p434=35,p435=50,p436=71,p437=78,p438=114,p439440=168),compiler_verified=False,no_success_observed=True,no_new_editor_tabs=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint312: whole angular hull, conductor obstruction and actual recognition\n\nComplete UNREVIEWED papers438439440 retain full formal proofs, every actual FINAL note in all five fields, distinct assembled notes, exact original tasks/residuals, source-application ledgers and whole incoming mathematical companions. Actual FINAL and assembled notes differ in some fields and are kept separate. Neither original problem is closed; counts16/42 solved,26OPEN,97acceptedscopedpapers remain unchanged.\n\n438 computes all actual angular mixed products, the entire uniformly closed angular convex hull and its exact cubic energy. Against the old isotropic Dirac, every member has a positive objective gap, so this entire hull contains no maximizing sequence; this does not obstruct the entire original C/G. 439 constructs a universal explicit primary obstacle for every full normalization fibre joining distinct local centres, without source-envelope continuity or a regular-cover hypothesis, relative to ENTIRE qualified G331. An internally injective centrewise restriction gives an exact incidence-plus-source-CE criterion. Arbitrary within-centre conductor identification and normal nonisolated continuity remain open. 440 gives an exact original-G recognition criterion using cozero rational sublevels and energy-controlled analytic majorants under every strict continuous obstacle. It constructs actual decreasing presentations when those predicates hold, but does not establish them for a target potential. Its actual Gauss singleton is not G_delta; the USC indicator has no decreasing continuous presentation, with no psh or prescribed-equation nonexistence claim.\n\nCurrent actual fields, every distinct formal proof, full unique scope/ledger/verdict/originals and inert programs were physically read; directly applied CLD units were read with complete immediate proofs. Exact current applications and incomplete deeper/historical/geometry/descent audits remain disclosed. Literal primary bodies/pixels/books LOCALONLY. All built-in compilation requests remain pending/unverified. ProtectedP16.4 editor OPEN UNCHANGED. Native302303 use signed-in official Xean Codex gpt-6.1-sol xhigh, at most two active; active mathematics is excluded.\n\nLarge public bodies are byte-exact ordered UTF8 parts. Whole-body reconstruction reuses exact already verified checkpoint311 parts wherever the complete old payload occurs in a new companion; fresh gaps are split at UTF8 boundaries. Concatenate the bound ordered part paths WITHOUT separators or added newlines. Reuse gives no mathematical reading or correctness credit. Original frozen whole files remain intact. All connector arguments stay below200000bytes. NONFORCE publication requires independent native Git root, all remote path/blob bindings, parent/commit/final-ref verification.\n')
files=[];by_path={};splits=[];reuse_count=0
def add(e):
    if e['path'] in by_path:
        i=by_path[e['path']];assert all(files[i][k]==e[k] for k in ['bytes','sha256']);return i
    i=len(files);files.append(e);by_path[e['path']]=i;return i
def fragment(data,folder,remote,serial):
    indices=[];off=0
    while off<len(data):
        end=min(off+150000,len(data))
        while end<len(data) and data[end]&192==128:end-=1
        body=data[off:end];body.decode('utf8');q=folder/f'fresh-{serial:04d}.txt';serial+=1;q.write_bytes(body)
        indices.append(add(dict(local=str(q),path=remote+'.parts/'+q.name,bytes=len(body),sha256=sha(q))));off=end
    return indices,serial
for p in sorted((F/'frozen-files').rglob('*'))+[F/'current-research-status.json',F/'desktop-compiler-observations.json',F/'README.md']:
    if not p.is_file():continue
    remote='research-checkpoints/continuation312/'+str(p.relative_to(F));original=dict(local=str(p),path=remote,bytes=p.stat().st_size,sha256=sha(p))
    if p.stat().st_size<=150000:add(original);continue
    data=p.read_bytes();intervals=[]
    for e in sorted(known,key=lambda x:len(x['body']),reverse=True):
        pos=data.find(e['body'])
        if pos<0:continue
        end=pos+len(e['body'])
        if any(pos<stop and start<end for start,stop,_ in intervals):continue
        intervals.append((pos,end,e))
    intervals.sort(key=lambda e:e[0]);indices=[];off=0;serial=1;folder=F/'parts'/f'{len(splits):02d}';folder.mkdir(parents=True)
    for start,end,e in intervals:
        extra,serial=fragment(data[off:start],folder,remote,serial);indices+=extra
        for oldpart in e['parts']:
            q=dict(oldpart,reused_verified_checkpoint=311);assert sha(q['local'])==q['sha256'];indices.append(add(q));reuse_count+=1
        off=end
    extra,serial=fragment(data[off:],folder,remote,serial);indices+=extra
    assert b''.join(Path(files[i]['local']).read_bytes() for i in indices)==data
    splits.append(dict(original=original,ordered_file_indices=indices,whole_body_retained=True,whole_public_body_byteexact_across_parts=True,reused_complete_payloads=len(intervals),reading_credit=False))
reconstruction=F/'whole-body-reconstruction.json';write(reconstruction,dict(recorded_utc=now,split_files=[dict(original=e['original'],ordered_part_paths=[files[i]['path'] for i in e['ordered_file_indices']]) for e in splits],instruction='Concatenate exact UTF8 bytes in order WITHOUT separators/newlines.',reused_old_part_occurrences=reuse_count,retention_NOT_reading_or_correctness=True))
add(dict(local=str(reconstruction),path='research-checkpoints/continuation312/whole-body-reconstruction.json',bytes=reconstruction.stat().st_size,sha256=sha(reconstruction)))
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),whole_body_binding=splits,solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint whole angular hull, conductor obstruction and actual finite-energy recognition',scope='WHOLE UNREVIEWED438439440 andfrozen302303; actual300301vsassembleddifferences preserved; active302303math excluded, compilerunverified, originalsOPEN.',force=False,connector_argument_limit_bytes=200000,reused_verified_checkpoint=311))
assert M.stat().st_size<=150000
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation312.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')];env=dict(os.environ);env['GIT_INDEX_FILE']=str(G/'native-continuation312.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
oldrows=subprocess.run(git+['ls-tree','-r',prior['tree_sha']],capture_output=True,text=True,check=True).stdout.splitlines();existing={e.split()[2] for e in oldrows if e.split()[1]=='blob'}
entries=[];groups={}
for e in items:
    data=Path(e['local']).read_bytes();data.decode('utf8');assert hashlib.sha256(data).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h));groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
chunks=[];batch=[]
for h,e in groups.items():
    if h in existing:continue
    x=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text());candidate=batch+[x]
    if batch and len((json.dumps(dict(tree=candidate),ensure_ascii=True,indent=2)+'\n').encode())>190000:chunks.append(batch);batch=[]
    batch.append(x);assert len((json.dumps(dict(tree=batch),ensure_ascii=True,indent=2)+'\n').encode())<200000
if batch:chunks.append(batch)
sizes=[];trees=[]
for i,ch in enumerate(chunks):
    q=A/f'content-chunk-{i}.json';q.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2)+'\n');sizes.append(q.stat().st_size)
    body=b''.join(b'100644 '+e['path'].encode()+b'\0'+bytes.fromhex(e['path']) for e in sorted(ch,key=lambda x:x['path']));trees.append(hashlib.sha1(b'tree '+str(len(body)).encode()+b'\0'+body).hexdigest())
write(A/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=sizes,content_tree_shas=trees,unique_blobs=len(groups),reused_parent_blobs=sum(h in existing for h in groups),commit_message=load(M)['commit_message'],force=False))
for name in ['active-work.json','checklist-current.json']:
    p=R/name;y=load(p);y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=312,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],expected_tree=expected,push_complete=False,bounded_transport=True,reuses_verified311_whole_parts=True));write(p,y)
print(json.dumps(dict(manifest=str(M),manifest_bytes=M.stat().st_size,manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),unique_blobs=len(groups),reused_parent_blobs=sum(h in existing for h in groups),content_chunks=len(chunks),max_chunk_bytes=max(sizes),split_bodies=len(splits),reused_old_part_occurrences=reuse_count,expected_tree=expected),indent=2))
