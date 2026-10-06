from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
T=K/'P16.5-finite-atomic-dual-density-before-attainment-candidate-20261006-continuation204.tex'
P=T.with_suffix('.pdf');D=K/'public-P16.5-continuation204-finite-atomic-dual-density-reader'
assert sha(T)=='a0ada79422814336756127b93dd802b48b19be433f98eae9ac9d146e240820f4'
assert sha(P)==sha(D/'paper.pdf')=='abf255781d2dfbb6ec20a46a89b994b48bc3cab92712c1c7bf1fed6c5546743c'
log=T.with_suffix('.log').read_text();assert not any(x in log for x in ('Warning:','Overfull','Underfull','undefined'))
b={'recorded_utc':now,'classification':'Unreviewed conditional204: finite atomic uniform dual density before attainment; target integrals weak continuous on energy sublevels; actual weak attainment and original equation under unresolved foundations.','tex':str(T),'tex_sha256':sha(T),'pdf':str(D/'paper.pdf'),'pdf_sha256':sha(P),'pages':5,'source_lines':326,'whole_final_tex_root_read':True,'whole_final_tex_root_read_chunks':['1-185','186-end'],'actual_visual_pages':list(range(1,6)),'warnings':0,'overfull':0,'underfull':0,'undefined':0,'two_pass_local_build_succeeded':True,'native_compile_request_cell':'542','native_compile_success_observed':True,'native_final_success_message':"The current source compiled successfully with the desktop editor's compiler.",'existing_editor_unchanged':True,'independent_acceptance':False,'original_closed':False,'accepted_paper_count_unchanged':59,'scope':'Finite four-point bound I_output^1/2 J_test^(2^-n) maxJ^(1/2-2^-n). Bounded shared full-system passage and202 midpoint identification give whole genuine bound and I<=4^(n+1) midpoint defect. Model near-max outputs from pre-attainment159 are dual-Cauchy uniformly over any genuine energy sublevel; fixed-test weighted convergence identifies limit with intrinsic target without an inverse. Atomic finite supports then give weak sublevel target-integral continuity, compact genuine weak attainment and both-sign original C0 equation.','remaining':'All actual genuine scalar/full-list energy/output antecedents; independent checking of source-dependent finite/genuine passages; original physical reference-defect assertions and further nonzero zero-volume range.'}
save(D/'publication-binding.json',b)
data=[]
for label,p in [('WHOLE159',K/'public-P16.5-round159-partial-conditional-attainment-reader/paper.tex'),('WHOLE202',K/'P16.5-filtered-quotient-traces-and-genuine-mixed-measures-candidate-20261006-continuation202.tex')]:
    data.append({'label':label,'file':str(p),'sha256':sha(p),'whole_body_root_read':True,'authority':'Unreviewed finite/conditional proof data only.'})
L=K/'P16.5-continuation204-root-source-application-and-read-scope-20261006.json'
save(L,{'recorded_utc':now,'classification':b['classification'],'final_tex_sha256':sha(T),'whole_final_source_root_read':True,'whole_source_read_chunks':b['whole_final_tex_root_read_chunks'],'all5final_visual_pages_root_read':True,'conditional_proof_data':data,'exact_extra_pertinent_units_reread':['159 sourceLF166-252: correct tangent, raw J and midpoint inequalities, complete finite slot-change proof leading to finite four-point estimate.','202 sourceLF594-630: whole mixed energy identity and canonical paired weighted passage.'],'new_proofs':['Finite top-power telescoping and graph Cauchy--Schwarz followed by raw slot-change bound give output-I square-root/test-J exponent2^-n four-point estimate, with no generic term because output raw masses agree.','Fixed bounded finite-list physical differences pass to original I and test moments on fixed U collars.202 convex-combination energy identifies finite midpoint defect; independent canonical weighted passage gives every genuine pair/test bound and I<=4^(n+1)delta.','Pre-attainment model near-max objectives force small pairwise midpoint defects, so their atomic output measures are uniformly dual-Cauchy on every bounded-cost genuine test set.','Fixed-test weighted limit is identified using one fixed model majorant first, bounded continuous U collars, uniform ordered errors at all approximate outputs, then directed continuous Radon integration at intrinsic target. No attained inverse used.','Pass the same uniform Cauchy bound to each fixed test and take the supremum only afterwards, giving genuine energy-sublevel dual density of finite divisorial outputs.','Finite atomic coordinate continuity plus uniform dual density makes every intrinsic-target integral weak continuous on normalized energy sublevels. E weak usc and genuine compactness produce actual variational maximizer; both signs of original continuous variation identify the equation.'],'pre_attainment_dependencies_only':['159 Sections6-8 bounded density/coercivity/output approximation/all-test absolute moment.','202 whole genuine mixed canonical weighted continuity and bounded convex-combination identification.'],'159_attained_inverse_used':False,'target_used_to_define_operator':False,'actual_conditional_foundations_asserted_true':False,'whole_primary_sources_read':False,'all_recursive_primary_foundations_read':False,'new_primary_sources_retrieved':False,'native_final_compile_success_observed':True,'independent_acceptance':False,'original_closed':False,'accepted_paper_count_unchanged':59,'active_private_outputs_read':False,'hot_feedback_sent':False})

# Supersede the prepared-only162 packet, preserving every frozen byte.
Old=R/'campaigns/round-162/P16.5-original-equation-after-energy-complete-unbounded-moving-limits'
assert not (Old/'work.sqlite').exists() and not (Old/'launch-record.json').exists()
oldf=json.loads((Old/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('input.json','input_sha256'),('settings.json','settings_sha256')]:
    assert sha(Old/name)==oldf[key]
C=R/'campaigns/round-163/P16.5-original-equation-after-unbounded-moving-and-atomic-dual-density'
C.mkdir(parents=True);(C/'artifacts').mkdir()
shutil.copyfile(Old/'task.json',C/'task.json')
inp=json.loads((Old/'input.json').read_text())
inp['assignment']+='''

NEW WHOLE204: Reconstruct the finite four-point output-I square-root estimate and its all-genuine passage, including I<=4^(n+1) midpoint defect from202 bounded midpoint identification. Its key claimed new theorem precedes attainment: finite Div model near-max outputs, already weakly approximating the target by159's signed stationary estimate, become uniformly dual-Cauchy on every genuine energy sublevel. Fixed-test weighted convergence identifies that dual limit with the intrinsic target without an inverse. The finite atomic supports imply target-integral continuity in the Div-coordinate topology on every energy sublevel, so genuine compactness and energy weak usc give actual weak attainment. Both signs of original C0 variation give the original equation. Verify the entire noncircular chain; do not use159's later inverse to prove204's atomic density or weak target-integral continuity. This could supply a direct variational proof once the actual entire scalar/energy/output/full-list foundations are independently reconstructed.
'''
bindings=json.loads((Old/'mathematical-data-bindings.json').read_text())
for label,p in [('WHOLE204 ATOMIC DUAL DENSITY BEFORE ATTAINMENT',T),('204 OWN APPLICATION LEDGER',L)]:
    inp['assignment']+='\nBEGIN COMPLETE MATHEMATICAL BODY '+label+'\n'+p.read_text()+'\nEND COMPLETE MATHEMATICAL BODY\n'
    bindings['supplied'].append({'label':label,'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size,'whole_body_supplied':True,'authority':'Unreviewed finite/conditional proof data only; no actual nonample grant.'})
save(C/'input.json',inp)
s=json.loads((Old/'settings.json').read_text())
s['usagePrefix']='catalogue-20261003/r163/P16.5-original-moving-atomic-dual-density';s['codex']['workspace']=str(C/'artifacts')
save(C/'settings.json',s)
bindings['whole_proof_pages']=66
save(C/'mathematical-data-bindings.json',bindings)
save(C/'freeze.json',{'prepared_utc':now,'round':163,'atom':'P16.5','directory':str(C),'prepared_only':True,'not_launched_while_two_reviews_active':True,'task_sha256':sha(C/'task.json'),'input_sha256':sha(C/'input.json'),'input_bytes':(C/'input.json').stat().st_size,'settings_sha256':sha(C/'settings.json'),'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','maximum_concurrent_campaigns':2,'unchanged_original_task':True,'whole_proof_papers':[151,159,160,201,202,203,204],'whole_proof_pages':66,'original_closed':False,'existing_editor_unchanged':True,'superseded_prepared_only_round':162})
save(Old/'superseded-before-launch.json',{'recorded_utc':now,'never_launched':True,'frozen_task_sha256':oldf['task_sha256'],'frozen_input_sha256':oldf['input_sha256'],'frozen_settings_sha256':oldf['settings_sha256'],'all_frozen_bytes_preserved':True,'superseded_by':str(C),'reason':'New whole204 finite atomic dual density BEFORE attained inverse and weak target-integral continuity supply additional mathematical proof data; preserve162 rather than altering a frozen input.'})

prior=json.loads((G/'push-receipt-continuation167.json').read_text())
assert prior['commit_sha']=='edac8a297152e7b45086bd09b9c4b0f206719713'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
S=K/'small-batch158161-public-status-20261006-continuation168';S.mkdir();items=[]
for n in (158,161):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';save(p,st)
    items.append({'round':n,'atom':'P16.5','directory':str(c),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Separate whole foundation158 and whole40-page bridge161 audits. New204 and fresh original163 packet are frozen;163 is prepared only and will launch only when one active slot clears. No hot feedback.'}
F=G/'continuation168-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers']==59 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
    j.update(updated_utc=now,current_small_batch=batch,P16_5_atomic_dual_density_before_attainment204=b,prepared_next_original_campaign=json.loads((C/'freeze.json').read_text()),github_pending_checkpoint='continuation168 frozen',goal_state='8/42 originals solved;34 open;59 accepted supporting papers. New2045-page unreviewed finite four-point and conditional uniform finite-atomic dual density before actual attainment, weak target-integral continuity on genuine energy sublevels and direct actual weak variational equation. All actual nonample foundations remain unproved. Fresh unchanged original163 whole66-page proof packet prepared only, superseding unlaunched162 with all frozen bytes retained.158 and161 reviews unchanged; no hot feedback.')
    for target in j.get('targets',[]):
        if target['id']=='P16.5':
            target['current_focus']='Foundation158 and whole40-page bridge161 reviews pending. New204 conditional uniform finite-atomic dual density before inverse, weak energy-sublevel target-integral continuity and direct genuine weak attainment; new203 unbounded energy-complete weak mixed/paired weighted limits. Fresh original16366-page packet prepared only; actual foundations and physical fixed-test reference defect remain open.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
lines=(R/'checklist-current.tsv').read_text().splitlines()
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P16.5':row[2]='New2045-page unreviewed conditional finite atomic uniform dual density before inverse; weak target-integral continuity and actual weak attainment. New203 unbounded energy-complete mixed weak/paired weighted.158/161 reviews pending; fresh unchanged original163 prepared only. Actual foundations and physical reference defect open.'
    lines[i]='\t'.join(row)
(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
save(F/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':59,'new_unreviewed_continuation':204,'pages':5,'new_original_closure':None,'new_independent_acceptance':None,'active_batch':[x['round'] for x in active],'prepared_only_original':163,'superseded_never_launched_original':162,'active_private_outputs_read':False,'hot_feedback_sent':False,'native_final_compiler_success_observed':True,'existing_editor_unchanged':True,'whole_goal_blocked':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.out','.aux')
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation168/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for p in (T,D/'paper.pdf',D/'publication-binding.json',L,G/'push-receipt-continuation167.json',R/'record_verified167_20261006.py',R/'prepare_original162_after_energy_complete_limits_20261006.py',Old/'superseded-before-launch.json',Path(__file__)):add(p)
for folder in (Old,C):
    for name in ('task.json','settings.json','input.json','freeze.json','mathematical-data-bindings.json'):add(folder/name)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation168.json'
save(M,{'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':59,'commit_message':'Record atomic dual density before attainment and freeze full equation packet','scope':'New2045-page unreviewed finite four-point and conditional whole energy-sublevel finite-atomic dual approximation before inverse, weak target-integral continuity and direct actual weak variational attainment. Fresh unchanged original16366-page proof packet prepared only, superseding never-launched162 with all frozen bytes preserved; will launch only after current at-most-two reviews release a slot. Actual nonample foundations, physical fixed-test reference defect and further nonzero zero-volume range open.8/42 originals and59 supporting papers unchanged; native final compile succeeded; no active private reads/hot feedback.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'prepared_original163':json.loads((C/'freeze.json').read_text()),'public_states':[{k:x[k] for k in ('round','observed_status','observed_utc')} for x in items]},indent=2))
