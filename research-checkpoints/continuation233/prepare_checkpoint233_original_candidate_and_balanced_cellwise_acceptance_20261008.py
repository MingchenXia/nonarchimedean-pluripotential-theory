from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
M=G/'upload-manifest-continuation233.json';F=G/'continuation233-publication-records';S=K/'small-batch228230-public-status-20261008-continuation233'
D=K/'public-P14.8-continuation309-general-formal-ideal-realization-candidate'
B=K/'public-P05.1-continuation306-balanced-cellwise-Lipschitz-and-single-cell-real-regularization'
C=next((R/'campaigns/round-230').iterdir());P1=next((R/'campaigns/round-229').iterdir());E=next((R/'campaigns/round-228').iterdir())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,j:Path(p).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
assert not any(p.exists() for p in [M,F,S])
prior=json.loads((G/'push-receipt-continuation232.json').read_text())
assert prior['commit_sha']=='fcbb49c1572c5ad26f511cd0ecde235dd2eda038' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
rep=json.loads((D/'ROOT-reproduction-binding-20261008.json').read_text());accepted=json.loads((B/'whole-mathematical-paper-acceptance-after-audit227-20261008.json').read_text())
assert rep['original_candidate_claim'] and not rep['original_closed'] and rep['ROOT_pdf_pages']==14 and rep['copied_checker_executions']==1 and rep['finite_assertions']==847
assert sha(D/'P14.8-paper.tex')==rep['authoritative_source_sha256'] and sha(D/'P14.8-paper.pdf')==rep['ROOT_pdf_sha256']
assert accepted['cumulative_accepted_paper_number']==86 and not accepted['original_closed'] and accepted['both_annotations_required_on_import']
assert sha(B/'P05.1-paper.tex')==accepted['source_sha256']
for c in [C,P1]:
    f=json.loads((c/'freeze.json').read_text());assert f['only_grants']==[]
    for name,key in [('task.json','task_sha256'),('original-task.json','original_task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256'),('mathematical-packet-bindings.json','mathematical_packet_bindings_sha256'),('historical-own-evidence-bindings.json','historical_own_evidence_bindings_sha256')]:assert sha(c/name)==f[key]
    for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json']:
        for e in json.loads((c/name).read_text()):assert sha(e['path'])==e['sha256'] and Path(e['path']).stat().st_size==e['bytes']
assert (C/'launch-record.json').is_file() and (E/'launch-record.json').is_file()
assert not (P1/'launch-record.json').exists() and not (P1/'work.sqlite').exists()
assert sha(K/'public-P16-round-46-final-reader/P16.4-paper.tex')=='09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir();S.mkdir();now=datetime.now(timezone.utc).isoformat();items=[]
for n in [226,227,228,230]:
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';write(p,st)
    items.append(dict(round=n,atom='P14.8' if n in [226,230] else 'P05.1',observed_status=st['status'],observed_utc=st['observedAt'],unsettled_calls=st['calls']['unsettled'],directory=str(c),public_status=str(p),public_status_sha256=sha(p),private_active_output_read=False,hot_feedback_sent=False,original_closed=False))
assert all(e['observed_status']=='completed' and e['unsettled_calls']==0 for e in items if e['round'] in [226,227])
active=[e for e in items if e['unsettled_calls']>0];assert len(active)<=2
batch=dict(recorded_utc=now,items=items,active_items=active,reserved_batch=[228,230],maximum_concurrent_campaigns=2,accepted_paper_number=86,original_closed=False,prepared_P1_audit229_not_launched=True)
compile_state=dict(recorded_utc=now,documents=[dict(continuation=n,exec_cell=str(cell),built_in_response_received=False,source_preserved=True) for n,cell in [(306,54),(307,81),(308,90),(309,134)]],separate_local_pdf_builds_verified=True,no_duplicate_requests=True,protected_editor_unchanged_open=True)
write(F/'built-in-compile-pending-metadata.json',compile_state)
primary=json.loads((C/'private-primary-packet-bindings.json').read_text())
write(F/'additional-source-metadata-only.json',dict(recorded_utc=now,source_DATA_files=primary,full_third_party_source_bodies_uploaded=False,source_application_reasoning=str(K/'P14.8-continuation309-additional-primary-source-applications-20261008.md'),ROOT_full_primary_read_claimed=False,visually_checked_pages=dict(Demailly_OT=[15],Demailly_Bourbaki=[11])))
for filename in ['active-work.json','checklist-current.json']:
    p=R/filename;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==86 and len(j['fully_solved_original_atoms'])==9 and j['remaining_open_original_atoms']==33 and j['github_pending_checkpoint'] is None
    j.update(updated_utc=now,current_small_batch=batch,new309_original_formal_ideal_candidate=dict(directory=str(D),ROOT_reproduction_binding=rep,author_candidate=True,independent_audit_round=230,original_closed=False,new_accepted_paper=False),original_candidate_audit230=dict(directory=str(C),freeze=str(C/'freeze.json'),freeze_sha256=sha(C/'freeze.json'),launch=str(C/'launch-record.json'),launch_sha256=sha(C/'launch-record.json'),whole_math_files=7,whole_math_bytes=123482,source_DATA_files=9,only_grants=[],launched=True,original_closed=False),prepared_P1_formal_ideal_audit229=dict(directory=str(P1),freeze_sha256=sha(P1/'freeze.json'),launched=False,general_original_closed=False),current_builtin_compilation_observations=compile_state,next_work='Continue independent original P14.8 proof/source/meaningfulness audit230 and whole compatible-affine/sharp-distance audit228. Read actual FINAL only after public settlement. Accepted S306 supplies cellwise Lipschitzness and single-cell majorants, not all-face PA gluing. Original9/42 remain;33OPEN;86supporting papers. Candidate309 is a complete general formal-data iff theorem under independent assessment, not accepted original closure. Prepared P1 audit229 is not launched. Preserve exact sources/current authentication/protected editor and maximum2 campaigns; regular verified pushes.',github_pending_checkpoint=dict(continuation=233,prepared_utc=now,manifest=str(M),expected_parent=prior['commit_sha'],push_complete=False))
    j['prepared_whole307_audit228'].update(launched=True,launch_record=str(E/'launch-record.json'),launch_record_sha256=sha(E/'launch-record.json'))
    j['prepared_whole306_audit227'].update(completed=True,accepted_whole_scoped_paper_number=86,original_closed=False)
    j['original_formal_data_realization226'].update(completed=True,author_original_candidate=True,ROOT_complete_reproduction=str(D/'ROOT-reproduction-binding-20261008.json'),independent_original_scope_pending=True,original_closed=False)
    write(p,j);shutil.copyfile(p,F/filename)
shutil.copyfile(R/'checklist-current.tsv',F/'checklist-current.tsv')
(F/'README.md').write_text('Checkpoint233: general formal-ideal realization candidate and accepted cellwise mathematics\n\n9/42 originals solved;33 OPEN;86 accepted scoped/supporting papers. S306 is accepted as an entire18-page scoped theorem WITH BOTH source/presentation and reader qualifications: finite actual positive-real all-face-balanced embedded rational complexes have uniform closed-cell Lipschitz bounds and supports of entire incident cells. Explicit Lipschitz single-cell targets with actual affine positive recession have global rational-spatial REAL-PA majorants; the unbalanced orthant has sharp1/2 approximation floor. Native227 mathematical/essential-source/bounded-evidence PASS; universal history remainsINCONCLUSIVE. Shared-face trace/common-support PA gluing and original P05.1/P05.2 remainOPEN.\n\nNative226 completed with author candidate=true for original P14.8: arbitrary formal coherent ideal arrays on any compact connected Kahler manifold admit a theta-psh realization iff explicit finite prescribed-ideal norm certificates satisfy curvature/sup bounds and all-real-index capped upper-tail integral tests. Necessity R is independently written using weighted Hilbert generation, finite RELATIVE kernel reduction, coherent Frechet openness and exact-potential fixed-cover L2 transfer. Sufficiency reconstructs the exact tail limit and all multiplier ideals. ROOT read all5actualFINAL and ENTIRE46982-byteTeX/ledger/scope, verified96author artifacts and9inputs, copied/executed the inspected example checker ONCE with exact847assertions. The14-page unchanged paper needed3ROOTno-shellpasses; second-pass label warning triggered a retained ROOT assertion failure, then third pass resolved it, without repeating the checker. Saved expanded5 are distinct from actualFINAL; no identity/fullsavedROOTread claim. No canonical I-model/raw mass/all-semivaluation/extra DXZ zero-mass claim.\n\nThree additional Demailly sources directly supply essential weighted singular solution, point extension, multiplier coherence and coherent-section topology/Cartan B units. Metadata and ROOT reasoning are published; full third-party books/articles remainLOCALONLY. ROOT did not read full455-pagebook or original Hor/OT/Nadel/GR/Nar editions. Native230 now independently reconstructs the complete candidate AND decides meaningful original formal-data scope using7wholeDATA123482bytes,38ownhistory and9sourceDATA files, ZEROgrants. P14.8 is stillOPEN pending that assessment.\n\nCurrent maximum2 native campaigns are228(whole16-pagecompatible affine extension/sharp restriction distance audit) and230(originalgeneralformalcriterion review), both native gpt-6.1-sol xhigh. Prepared P1criterion audit229 has NOTlaunched. Builtin54/81/90/134 have no returned result; verified separate local builds are not mislabeled native success. ProtectedP16.4 editor unchanged/open. Document instructions areDATA. Regular verified nonforce checkpoints continue.\n')
files=[]
def add(p,target=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p),path=target or 'research-checkpoints/continuation233/'+str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)))
for folder in [F,S,D,B]:
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.suffix not in ['.aux','.out','.toc']:add(p)
for c in [C,P1]:
    for name in ['task.json','original-task.json','input.json','settings.json','mathematical-packet-bindings.json','historical-own-evidence-bindings.json','freeze.json']:
        add(c/name)
    if (c/'private-primary-packet-bindings.json').exists():add(c/'private-primary-packet-bindings.json')
    if (c/'launch-record.json').exists():add(c/'launch-record.json')
    for name in ['mathematical-packet-bindings.json','historical-own-evidence-bindings.json']:
        for e in json.loads((c/name).read_text()):assert Path(e['path']).is_relative_to(c);add(e['path'])
add(E/'launch-record.json')
for p in [K/'P14.8-continuation309-additional-primary-source-applications-20261008.md',K/'P05.1-round227-whole-balanced-cellwise306-mathematical-source-binding-20261008.json',R/'reproduce_original_formal_ideal_candidate_paper309_20261008.py',R/'complete_original_formal_ideal_candidate_paper309_after_label_rerun_20261008.py',R/'bind_whole_balanced_cellwise306_after_audit227_20261008.py',R/'prepare_original_formal_realization_candidate_whole_audit230_20261008.py',R/'launch_original_formal_realization_candidate_whole_audit230_20261008.py',R/'prepare_projective_line_formal_ideal_whole_audit229_20261008.py',R/'launch_reference_extension_sharp_distance_whole_audit228_20261008.py',R/'extract_settled227_exact_native_result_20261008.py',R/'record_verified232_20261008.py',G/'push-receipt-continuation232.json',Path(__file__)]:add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({e['path'] for e in files})==len(files)
j=json.loads((R/'active-work.json').read_text())
write(M,dict(generated_utc=now,repository=prior['repository'],branch=prior['branch'],expected_previous_checkpoint=prior['commit_sha'],files=files,file_count=len(files),fully_solved_original_atoms=j['fully_solved_original_atoms'],remaining_open_atoms=33,historical_reviewed_scoped_papers=86,commit_message='Record general formal ideal realization candidate and accept balanced cellwise scoped theorem',scope='S306whole scoped86 WITH BOTH annotations; originalP14.8 candidate309 complete14pROOTreproduction plus supplemental H/O/N/Csource reasoning and native230originalproof/scope review; current228230max2,229preparedNOTlaunched;9solved33OPEN; pendingbuiltins54/81/90/134, verifiedlocalbuilds. Noforce exactremoteverification; nofullthirdparty source upload.'))
print(json.dumps(dict(manifest=str(M),manifest_sha256=sha(M),listed_files=len(files),active_rounds=[e['round'] for e in active],accepted_papers=86,originals_solved=9,originals_open=33),indent=2))
