"""Freeze WHOLE428 public checkpoint and independently bind native Git objects."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R=Path('/workspace/research')
K=R/'root-checks'
G=R/'github-checkpoint'
F=G/'continuation308-publication-records'
M=G/'upload-manifest-continuation308.json'
B=K/'P12.3-continuation428-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation307.json')
assert prior['commit_sha']=='6a6bdf513eff650f8971b9cf59ef281de7b6c160' and prior['tree_sha']=='370d7eb90cc58621859e84165d1f936ec8b5c84f' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
b=load(B)
assert not b['accepted'] and not b['original_closed']
for e in b['public_files']:
    assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
paths=[Path(e['path']) for e in b['public_files']]+[B,R/'retain_ROOT428_whole_finite_group_quotient_proof_20261009.py',R/'record_verified_checkpoint307_20261009.py',G/'push-receipt-continuation307.json',Path(__file__)]
for round,name in [(296,'P12.3-whole425426-same-centre-and-normal-quotient-envelopes'),(297,'P16.7-whole427-whole-dirac-and-actual-analytic-representation')]:
    C=R/f'campaigns/round-{round}'/name
    paths += [C/n for n in ['task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==307 and y['current_active_batch']==[296,297]
    assert len(y['fully_solved_original_atoms'])==16 and y['remaining_open_original_atoms']==26 and y['historical_reviewed_scoped_papers']==97
F.mkdir()
for p in paths:
    rel=p.relative_to(R)
    assert 'LOCALONLY' not in str(rel) and 'primary-data' not in str(rel)
    q=F/'frozen-files'/rel
    q.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(p,q)
    assert sha(q)==sha(p)
now=datetime.now(timezone.utc).isoformat()
for name in ['active-work.json','checklist-current.json']:
    p=R/name
    y=load(p)
    y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=308,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE308 WHOLE428 quotient/orbit/envelope/norm-filtration proof. Native296297 compactstatus running17:10:44UTC, no active math inspection/hot feedback. Compiler993 pending/unverified; counts/editor unchanged.')
    write(p,y)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=y['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[296,297],new_papers=[428],whole_current394LF20229byte_TeX_ROOT_physically_read=True,source_sha256=b['whole_source']['sha256'],source_had_one_accidental_fraction_formfeed_repaired_before_retention=True,whole_corrected_source_reread_output='75b75b',three_complete_immediate_BFJ_units_freshly_ROOT_reread=True,other_eleven_immediate_units_and_two_pixels_reused_NO_fresh_credit=True,entire_qualified_G331_ALLfivefields_and_426n1_current_scope_original_residual_retained=True,full_recursive_deeper_source_audit_NOT_complete=True,compilation_UNVERIFIED=True,actual_builtin_compile_request='pending cell993',native296297_compact_status='bothrunning17:10:44UTC',active296297_mathematics_NOT_read_or_published=True,UNREVIEWED=True,original_closed=False,accepted=False,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F/'desktop-compiler-observations.json',dict(recorded_utc=now,paper428='Actual built-in compile requested AFTER whole retention; pending cell993. Historical frozen compiler observation accurately precedes this request.',compiler_verified=False,no_success_observed=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint308: finite-group quotients and geometric envelopes\n\nWhole UNREVIEWED ROOT428 proves full semivaluation restriction fibres are finite-group orbits for excellent normal R=S^G finite excellent normal semilocalDOMAIN S. All nonminimal supports and infinite values retained. Coefficient ideals of orbit products with finite R-MODULE generators give exact all-support norm values. Equal finite orbit measures follow from compact ideal-difference lattice density. Finite positive traces and orbit maxima yield exact pullback of raw C/D envelopes, and greatest minorants exist iff the invariant source obstacle has one. No faithfulness or invertibility of grouporder required.\n\nEvery canonical target/source degree has exact contraction I_m=J_m capR, norm inclusion N_G(J_m) subset I_hm and sandwich pullh_mR<=h_mS<=pullh_hmR. Source continuous envelope gives target EVERY-degree uniform error <=beta_floor(n/h)+(h-1)||vI1||/n, with actual primary geometric profiles before limits and no finite generation. Every finite quotient of a smoothAFFINE CLOSED germ over algclosedCHAR0 has universalCE in everydimension. Nonisolated NORMAL singularities ac=b² times affine(d-2)-space are explicit examples. Completion and gauge transport retain exact qualifications. General NORMALdim>=3 and highercharp/mixed regular sourceCE, arbitrary conductorclassification and full originalP12.3 remainOPEN.\n\nEntire corrected394LF20229-byte TeX physically ROOT reread, source hash bound;302041-byte mathematical companion retains ENTIRE qualifiedG331 ALLfivefields and TXT, entire426n1 actual/formal proof, current426 source qualifications and unchanged original dossier/residual. Three COMPLETE immediate BFJ setting/simple-modification/3.15-3.25 units freshly physically reread. Real t=m+C, bounded thinness on FIXEDcomplex and ALLretraction/closed-simplex application checked. Other eleven whole immediate units and two pixels retain earlier reading with no freshcredit. Primary literal bodies/pixels/books LOCALONLY. No supplied/native programs executed/imported, no full deeperrecursiveaudit claim.\n\nProof independent AFTER native296297 launches and BEFORE any active math inspection. Both tasks compactstatus RUNNING17:10:44UTC, signed-in official Xean native Codex gpt-6.1-sol xhigh, maximumTWO. No active math read/published/hot-fed. Actual desktop compiler request pending993, unverified; no newtabs/localTeX/plugin. Protected P16.4 editor OPEN UNCHANGED. Counts16/42originalsolved,26OPEN,97accepted scoped papers. Publication NONFORCE with independent native Git root/blob/path/parent/finalref checks; retention/hashes are not correctness or new reading credit.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation308/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint finite-group quotient envelopes and every-degree norm bounds',scope='WHOLE UNREVIEWED428, active296297 math excluded, compiler unverified, original OPEN.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation308.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]
env=dict(os.environ)
env['GIT_INDEX_FILE']=str(G/'native-continuation308.index')
subprocess.run(git+['read-tree',prior['tree_sha']],env=env,capture_output=True,check=True)
entries,groups=[],{}
for e in items:
    body=Path(e['local']).read_bytes()
    body.decode('utf-8')
    assert hashlib.sha256(body).hexdigest()==e['sha256']
    h=hashlib.sha1(b'blob '+str(len(body)).encode()+b'\0'+body).hexdigest()
    assert subprocess.run(git+['hash-object','-w',e['local']],capture_output=True,text=True,check=True).stdout.strip()==h
    entries.append(dict(path=e['path'],mode='100644',type='blob',sha=h))
    groups.setdefault(h,e)
    subprocess.run(git+['update-index','--add','--cacheinfo','100644',h,e['path']],env=env,capture_output=True,check=True)
expected=subprocess.run(git+['write-tree'],env=env,capture_output=True,text=True,check=True).stdout.strip()
API=G/'api-recovery-continuation308'
API.mkdir()
chunks,chunk,size=[],[],0
for h,e in groups.items():
    item=dict(path=h,mode='100644',type='blob',content=Path(e['local']).read_text())
    n=len(json.dumps(item,ensure_ascii=True).encode())
    if chunk and size+n>250000:
        chunks.append(chunk)
        chunk,size=[],0
    chunk.append(item)
    size+=n
if chunk:
    chunks.append(chunk)
sizes=[]
for i,ch in enumerate(chunks):
    p=API/f'content-chunk-{i}.json'
    p.write_text(json.dumps(dict(tree=ch),ensure_ascii=True,indent=2)+'\n')
    sizes.append(p.stat().st_size)
write(API/'connector-plan.json',dict(repository=prior['repository'],branch=prior['branch'],parent=prior['commit_sha'],base_tree=prior['tree_sha'],expected_tree=expected,manifest_sha256=sha(M),entries=entries,content_chunks=len(chunks),content_chunk_bytes=sizes,commit_message=load(M)['commit_message'],force=False))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),actual_files=len(items),unique_blobs=len(groups),content_chunks=len(chunks),content_chunk_bytes=sizes,expected_tree=expected,primary_bodies_published=False),indent=2))
