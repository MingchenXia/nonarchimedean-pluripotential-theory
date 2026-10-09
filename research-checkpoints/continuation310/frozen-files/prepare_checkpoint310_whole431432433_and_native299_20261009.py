"""Freeze whole431432433 and native299 metadata; independent native Git binding."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R=Path('/workspace/research')
K=R/'root-checks'
G=R/'github-checkpoint'
F=G/'continuation310-publication-records'
M=G/'upload-manifest-continuation310.json'
D=K/'public-P16.7-continuation432-nested-nonskeletal-radon-equations-and-fan-obstruction-unreviewed'
C=R/'campaigns/round-299/P16.7-whole432-two-point-mass-and-whole-dirac'
B431=K/'P12.3-continuation431-ROOT-whole-paper-source-scope-and-binding-20261009.json'
B433=K/'P16.7-continuation433-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation309.json')
assert prior['commit_sha']=='9556f41667eb56aea7e4ec0ddf1b8665a320698e' and prior['tree_sha']=='fcdba33ef15df4736ced1664baccd73a184f7b09' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
paths=sorted(p for p in D.iterdir() if p.is_file())
for p in [D/'ROOT-whole-proof-source-scope-and-binding.json',B431,B433]:
    b=load(p)
    assert not b['accepted'] and not b['original_closed']
    for e in b['public_files']:
        assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
    if b['paper'] in [431,433]:
        paths += [Path(e['path']) for e in b['public_files']]+[p]
paths += [R/n for n in ['stage_native297_whole_ROOT432_nested_radon_branch_20261009.py','capture_terminal_native297_actual_FINAL_20261009.py','retain_ROOT431_normal_finite_cover_whole_proof_20261009.py','retain_ROOT433_whole_two_residue_nonskeletal_mass_20261009.py','prepare_native299_whole432_two_point_and_whole_dirac_20261009.py','launch_frozen_native299_checked_20261009.py','record_verified_checkpoint309_20261009.py']]
paths += [C/n for n in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [K/'native299-approval-review-resolution-20261009.json',G/'push-receipt-continuation309.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==309 and y['current_active_batch']==[299]
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
    y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=310,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE310 WHOLE431432433 and frozen299. Independent433 full nonskeletal rawmass2/twoRadonbranches retainedbefore ANY settled298 oractive299 math; then captureonlysettled298 actualFINAL. Native299isolatedactive; maxTWO,nohotfeedback, compilerunverified, originalOPEN,counts/editor unchanged.')
    write(p,y)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=y['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[299],new_papers=[431,432,433],independent431_341LF17055B_whole_ROOT_read=True,actual297_ALLfour_ALLfivefields_and552LF29837Bformal_ROOT_physically_read=True,current297_actual_vs_assembled_STRUCTURALLY_IDENTICAL_separately_retained=True,whole_unique_current_header_ledger_verdict_originaltask_residual_ROOT_read=True,ALLfive_native_programs_ROOT_read_ONLY_DATA=True,all15_complete_immediate_CLD_GR_primary_units_fresh_ROOT_read=True,native_source_and7036826Bcompanion_passive_literal_reconstruction_exact=True,whole40incoming_math_retained_inside7084039B_ROOT432companion=True,all15_complete_immediate_primary_literal_bodies_excluded_from_public=True,independent433_364LF17788B_whole_ROOT_read=True,independent433_proof_after299launch_BEFOREsettled298_oractive299_math=True,full_current427_inherited_source_and_companion_NOTfresh_end_to_end_ROOT_read=True,entire_current_recursive_source_book_geometry_descent_audit_INCOMPLETE=True,retention_hashing_NOTreading_or_correctness_credit=True,compiler_UNVERIFIED=True,native298_completed_compact_ONLY_math_NOTread=True,active299_math_NOTread_or_published_or_hotfed=True,new_two_residue_polynomial_route_UNPROVED_at299launch=True,UNREVIEWED=True,accepted=False,original_closed=False,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F/'desktop-compiler-observations.json',dict(recorded_utc=now,paper431='Actual built-in request13 pending afterwhole retention; briefwait pending',paper432='Actual built-in request31 pending afterwhole retention',paper433='Actual built-in request47 pending afterwhole retention',compiler_verified=False,no_success_observed=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint310: normal finite-cover maxima and full nonskeletal mass\n\nWhole UNREVIEWED independent ROOT431 proves characteristic-coefficient full-fibre maxima preserve actual positive C and decreasing-net D for finite DOMAIN extensions over excellent NORMALlocalDOMAIN, anycharacteristic/allsemilocalcentres/allnonminimal supports/inseparablelengths. R-MODULE coefficientintegrality, unique lowest root product and ACTUALprimarytruncations D_l=C_l+a^(Nl) establish the finite maximum of actualAMPLE primary profiles. TraceLp proves ordinary continuity separately. Exact raw C/D envelopepullback, sourcefullfibreconstancy, greatestminorant iff pulledsourcegreatest, known sourceCE descent, Jensen/tower identities andeverydegree canonicalnormbounds are proved withoutgroup/flatness. SmoothAFFINE CLOSEDalgclosedCHAR0 actualfiniteregular sources give a targetsector; arbitrarynormalgerms are NOTassumed tohavefinite regularcover. GeneralNORMALdim>=3 andhighercharp/mixedregularsourceCE/fulloriginalP12.3 remainOPEN. ENTIREqualifiedG331 allfields andcurrent430canonical/smooth proof/sourcequalifications/originalscope retained; sixBFJcompletecurrent430units reusedwithnoadditionalprimarycredit.\n\nWhole UNREVIEWED ROOT432 retains actual297 and new nestednonskeletalRadonbranch solutions. For ANYdepthlaw zeta ofmassM<=1, FULLDfinite IFF S=int tail^(3/2) finite; actualcontinuousCcutoffsdecrease toactualGsolution, MA=(2-M)delta_g+pushzeta, E=-1/3-S/3,D=1/6+2S/3. Explicit c^-2dc[1,infinity) hasS3,E-4/3,D13/6, unboundedonlyrigidP. AllactualGuniqueness/nonorderedrepresentation inTHISsector retainqualifiedboundedfoundationantecedents. EVERYspecified outsidequadrantfixedREALfinitefan retainsactualGaussmass>=1 viafullycalibratedraw2!subgradientarea; this isONLYrouteobstruction. FamilyrestrictedwholeDiracobjective3/8 isNOTfullDupperbound/nonexistence. ALLfouractualALLfivefields, distinct552LF29837Bformal, wholeuniquecurrentheader/JSONandTXTledgers/verdict/unchangedoriginaltask/residual andFIVEinertprograms physicallyROOTread. Native167735B3376LFsource and7036826Bcompanion passivelyliterallyreconstructed, neverexecuted/imported nativeprograms. ROOT7084039Bcompanion retainsevery40incomingbodywhole; all15completeimmediateCLD/GRunits freshlyROOTread atpreciseactualordinaryopen/boundaryless/fixedfibres/positiveradii/degree1 scopes andexcludedliteralbodies. Inherited427whole137655Bstandalone/6551521Bcompanion NOTcurrentend-to-endROOTread; entire-current/deeperrecursivebook/geometryaudit incomplete.\n\nWhole UNREVIEWED independentROOT433 proves a NEWactualpositiveSIXpolynomialmaximum for TWOcentres withnorm-one coordinates anddistinctresiduesinBOTHcoordinates. Two bilinearpolynomials plusfourdepth-selective capslots equal the sum ofdisjointcorrections onEVERYactualpoint. Actualunitlogmax/ordinarycollar provespositivitybeforeproducts. Fixedcoordinatefibres give MA=delta_x1+delta_x2, ENTIRErawmass2 nonskeletal withNOgatom. Actualcross-currentvanishing andFOURpositivecorners permit independent EACHmassmi<=1, notsum<=1. PRODUCTconvexfinite-depth combinations andatomicuniformclosure give TWORadonbranches EACHmass<=1, FULLDfinite IFF S=sum int tail_i^(3/2) finite, actualCcutoffs/Goperator,E=-1/3-S/3,D=1/6+2S/3. Bothmasses1 haveZEROgatom. Depth1/8at(1,1),(2,3): E-5/12,D1/3. Bothc^-2dc[1,infinity): S6,E-7/3,D25/6,actualunboundedtwo-centresolution withnomassrigidcentres. Exactsource/currentfoundations andwholeactualfields/whole3376LF432source retained; all15primaryunits reusedwithoutnewreadingcredit. Fullhistorical432companion remainsseparatelywholebound. Coalescedwhole2delta_xONEpoint, generaleligiblearbitrarysupport/recognition/envelopes/genuinegeometry andfulloriginalP16.7 OPEN. Independent433 authoredandretained AFTER299launch BEFOREany299active or298terminalmathematics; nohotfeedback.\n\nNative299 frozenWHOLE432 continues two-residue fullmass, coalescedwholeDirac andgeneralrecognition; the polynomialproposal was UNPROVEDatlaunch, no433formalproofhotfed. Signed-in official Xean nativeCodex gpt-6.1-sol xhigh/maxTWO. Initialautomatedapprovalrejectedsourceexport; sameactionapprovedafterexplicit prioruser authorization "授权你上传任何材料" andmetadataevidence, no bypass/auth/proxy/CAchange. Native298completedcompactonly/mathunread,299active/mathnotread/published/hotfed. Actualnativecompiler requests13/31/47pendingUNVERIFIED; no newtabs/localTeX/plugin. ProtectedP16.4editorOPENUNCHANGED. Counts16/42solved26OPEN97acceptedscopedpapers. Literalprimarybodies/pixels/books LOCALONLY. NONFORCEpublication independentlyverifies exactfrozenfiles/blob/path/nativeGitroot/parent/tree/finalref; no publication is mathematicalacceptance.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation310/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint finite-cover envelopes and full nonskeletal Radon equations',scope='WHOLE UNREVIEWED431432433 plusfrozen299; terminal298 andactive299 math excluded, compilerunverified, originalOPEN.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation310.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]
env=dict(os.environ)
env['GIT_INDEX_FILE']=str(G/'native-continuation310.index')
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
API=G/'api-recovery-continuation310'
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
