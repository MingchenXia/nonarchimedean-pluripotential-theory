"""Freeze WHOLE429430 and native298 metadata; bind native Git independently."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess, os

R=Path('/workspace/research')
K=R/'root-checks'
G=R/'github-checkpoint'
F=G/'continuation309-publication-records'
M=G/'upload-manifest-continuation309.json'
D=K/'public-P12.3-continuation430-formal-group-quotients-and-wild-separable-conductors-unreviewed'
C=R/'campaigns/round-298/P12.3-whole429430-normal-finite-cover-envelope-transfer'
B429=K/'P12.3-continuation429-ROOT-whole-paper-source-scope-and-binding-20261009.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
write=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not F.exists() and not M.exists()
prior=load(G/'push-receipt-continuation308.json')
assert prior['commit_sha']=='91609cb14e933072e9a6199014a5a443284d3717' and prior['tree_sha']=='d5511897a06f3354108cbef00a72ef31980a8cc4' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
paths=sorted(p for p in D.iterdir() if p.is_file())
for p in [D/'ROOT-whole-proof-source-scope-and-binding.json',B429]:
    b=load(p)
    assert not b['accepted'] and not b['original_closed']
    for e in b['public_files']:
        assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
    if b['paper']==429:
        paths += [Path(e['path']) for e in b['public_files']]+[p]
paths += [R/n for n in ['audit_and_stage_native296_whole_paper430_ROOT_20261009.py','retain_ROOT429_whole_normalization_compatibility_proof_20261009.py','capture_terminal_native296_actual_FINAL_20261009.py','prepare_native298_whole429430_normal_finite_cover_envelopes_20261009.py','launch_frozen_native298_checked_20261009.py','record_verified_checkpoint308_20261009.py']]
paths += [C/n for n in ['original-task.json','task.json','settings.json','freeze.json','launch-record.json','mathematical-packet-bindings.json']]
paths += [G/'push-receipt-continuation308.json',Path(__file__)]
assert len(paths)==len(set(paths))
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
for name in ['active-work.json','checklist-current.json']:
    y=load(R/name)
    assert y['github_pending_checkpoint'] is None and y['latest_verified_github_checkpoint']['continuation']==308 and y['current_active_batch']==[298]
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
    y.update(updated_utc=now,github_pending_checkpoint=dict(continuation=309,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False),next_work='Verify NONFORCE309 WHOLE429430 andqualifiedfrozen298 normalfinitecoverMAX route. Native297 terminalcompactonly, mathematicsnotyetread; native298 isolatedactive, no hotfeedback. Compiler99310141028unverified; counts/editor unchanged.')
    write(p,y)
write(F/'current-research-status.json',dict(recorded_utc=now,fully_solved_original_atoms=y['fully_solved_original_atoms'],solved=16,open=26,accepted_scoped_papers=97,current_active_batch=[298],new_papers=[429,430],independent429_full314LF16407byte_source_physically_ROOT_read=True,actual296_ALLfivefields_ALLfiveactualnotes_and_all5distinct787LFformalproofs_ROOT_physically_read=True,current296_actual_vs_assembled_structurally_IDENTICAL_retained_separately=True,complete_unique_current_header_ledgers_verdict_task_completion_residual_physically_ROOT_read=True,all_FOUR_native_programs_physically_ROOT_read_as_inertDATA_ONLY=True,native_source_and_native9522630byte_companion_ROOT_passively_literally_reconstructed=True,ROOTreader_ONLY_two_math_separator_typo_corrections_exact_native_retained=True,all44_incoming_math_bodies_retained_WHOLE_in8450743byte_ROOTcompanion=True,all16_immediate_primary_carriers_excluded_from_public=True,allSIX_complete_immediateBFJunits_ROOT_freshly_physically_reread=True,entire_inherited426_source_and_companion_NOTcurrent_end_to_end_physically_read=True,entire_current_and_deeper_recursive_source_audit_INCOMPLETE=True,storage_deduplication_NOTreading_or_correctness_credit=True,compiler_UNVERIFIED=True,native297_terminal_compact_only_math_NOTread=True,active298_mathematics_NOTread_or_published=True,new_normal_finite_cover_MAX_route_UNPROVED_at298launch=True,UNREVIEWED=True,accepted=False,original_closed=False,primary_bodies_pixels_books_LOCALONLY=True,protected_editor_OPEN_UNCHANGED=True))
write(F/'desktop-compiler-observations.json',dict(recorded_utc=now,paper429='Actual native desktop request pending1014 afterwhole retention',paper430='Actual native desktop request pending1028; briefwait stillpending',paper428='Actual native desktop request pending993',compiler_verified=False,no_success_observed=True,sources_preserved=True,no_local_TeX_or_plugin_install=True,no_new_editor_tabs=True,protected_editor_OPEN_UNCHANGED=True))
(F/'README.md').write_text('Checkpoint309: normalization compatibility, formal quotient envelopes and wild conductors\n\nWhole UNREVIEWED ROOT429 proves exact normal-source/raw-target envelope equality at EVERYfinite-conductor point for finite normalization of excellentlocalDOMAIN, with ACTUALtarget primary ideals C J_m^n+a^(mnM) and allinfinite-support truncation tests. If source envelope continuous AND finite-conductor locus dense, greatest targetC/D exists IFF source envelope constant onEVERYfullfibre. A discrepancyDelta gives nonUSCjump>=Delta, EVERYDminorant/EVERYcanonical error>=Delta and perturbationstability. Complete translatedGauss formal-series proof establishes fullsupport density for smoothCLOSED centres overalgclosedfield ANYcharacteristic. Thus arbitrary conductorgeometry withsmoothAFFINEclosednormalcentres algclosedCHAR0 has an exact obstaclecompatibility criterion; intrinsic universal ringclassification remainsOPEN.\n\nWhole UNREVIEWED ROOT430 retains actual296. Full fibre-orbit theorem applies to excellentREDUCEDlocal finiteinvariantinclusions ANYcharacteristic. EVERYcontinuoussigned obstacle on normal smoothAFFINEfixedpointquotients and invariant rings of ANYcontinuousfinite action on formalregular k[[x]] overalgclosedCHAR0 has continuousgreatestC/D. Elementaryformal orbit-coefficientA0 and recursiveArtinianmonomialbasis provefinite/Noetherian/complete/excellent/normal withoutactionalgebraization. Exactenvelopepullback, canonicalcontraction and EVERYdegreeuniformconvergence; signedprimarymodels have allsupport error d(K+M1)/m. A conditional samecentreconductorobstruction is completely verified for EVERYformal separable parameter cover u=P(t),ordP>=2,Pprime!=0,ANYfield,dimension>=3. RingR=A+yS has one regularnormalizationcentre and exactconductoryS; finitefreebasis/characteristicpolynomialunitidentity/completefiniteDVRconjugatearc/all-elementGaussnet/ALLdownstairsprimarymonomialcomparison proved. NEWwildcharp P=t^p+t^(p+1) givescontactp/(p-1),rawp(o)=h_m(o)=-4 EVERYm and EVERYcanonicalgap>=3-p/(p-1)>=1, perturbationstable, evenimperfectfields. These failures are NONnormal.\n\nALLFIVEfields of ALLFIVE actual296notes, all FIVE distinct787LF43201-byte formalproofs, completeunique header/ledgers/verdict/unchangedtask/completion/residual and FOUR inertprograms physically ROOTread. Currentactual/assembledfields structurallyIDENTICAL independentlychecked and retainedseparately. Exactnative59685-byte standalone and9522630-byte companion passivelyliterallyreconstructed, neverexecuting/importingnativeprograms. ROOTreader59687-byte897LF onlycorrectsTWO ,qquad mathseparator spellings; exactnative/formal versions preserved. ROOT8450743-byte companion retains every44 incomingmathbodyWHOLE byexactcontainment, excludesall16 immediateprimarycarriers. All SIX complete immediateBFJ units freshly physicallyROOTread atsmoothaffineCLOSEDalgclosedCHAR0 domain, realt=m+C, FIXEDcomplexthinness, substantiveclosed-simplex3.11/ALLretractions/all-supporttests andcomplete3.9/3.10proofs. Entire inherited906751-byte426source and7085210-bytecompanion are NOTcurrent end-to-endphysicallyread; entire-current/deeperrecursive/book/pixel audit INCOMPLETE, disclosed. Retention/hashes/deduplication are not reading or correctnesscredit. GeneralNORMAL>=3, highercharp/mixedsourceCE, arbitraryintrinsicconductorclassification and fulloriginalP12.3 remainOPEN.\n\nNative298 frozenWHOLE429430 plus prior360isolatedchar0proofDATA seeks a NEW UNPROVEDnormal finite-cover fibreMAX/characteristic-coefficient envelope descent route beyondfinitegroups. No arbitrarysingular regularfinitecover presumed. Signed-in official Xean native Codex gpt-6.1-sol xhigh, maxTWO; native297completedcompactonly, mathunread,298active mathNOTread/published/hotfed. Actualdesktop compiler requests99310141028pendingUNVERIFIED; no newtabs/localTeX/plugin. Literalprimarybodies/pixels/books LOCALONLY, protectedP16.4editorOPEN UNCHANGED. Counts16/42originalssolved,26OPEN,97acceptedscopedpapers. NONFORCEpublication independently verifies exactfrozenfiles, everypath/blob/nativeGitroot/parent/tree/finalref.\n')
files=[dict(local=str(p),path='research-checkpoints/continuation309/'+str(p.relative_to(F)),bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(F.rglob('*')) if p.is_file()]
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),solved=16,remaining_open=26,accepted_scoped_papers=97,commit_message='Checkpoint normalization compatibility and wild separable conductor proofs',scope='WHOLE UNREVIEWED429430 and qualifiedfrozen298; terminal297 math unread, active298 math excluded, compilerunverified, originalOPEN.'))
items=files+[dict(local=str(M),path='manuscript/editorial/xean_research_20261003/UPLOAD_MANIFEST-continuation309.json',bytes=M.stat().st_size,sha256=sha(M))]
git=['git','--git-dir='+str(G/'native-continuation56.git')]
env=dict(os.environ)
env['GIT_INDEX_FILE']=str(G/'native-continuation309.index')
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
API=G/'api-recovery-continuation309'
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
