from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
T=K/'P16.5-energy-complete-unbounded-moving-limits-candidate-20261006-continuation203.tex'
P=T.with_suffix('.pdf');D=K/'public-P16.5-continuation203-energy-complete-moving-reader'
assert sha(T)=='96222fa199a5e00e355b11343498733244df5c7182d192a60807000bbfc99f62'
assert sha(P)==sha(D/'paper.pdf')=='b370b1b76ee2770aa10dd6b603a17900780b6a1e54532cacc51605177a0d0cec'
log=T.with_suffix('.log').read_text()
assert not any(x in log for x in ('Warning:','Overfull','Underfull','undefined'))
b={'recorded_utc':now,'classification':'Unreviewed conditional203: energy-complete unbounded full-system diagonal/mixed weak limits and paired relative weighted moments; original open.','tex':str(T),'tex_sha256':sha(T),'pdf':str(D/'paper.pdf'),'pdf_sha256':sha(P),'pages':7,'source_lines':509,'whole_final_tex_root_read':True,'whole_final_tex_root_read_chunks':['1-250 (reread after final plus corrections)','251-end (unchanged final source)'],'actual_visual_pages':list(range(1,8)),'final_changed_visual_pages_reread':[2,3],'other_final_visuals_pixel_identical_to_prior_read':[1,4,5,6,7],'final_visual_image_hashes':{str(i):sha(D/f'visual-final-LOCALONLY-{i}.png') for i in range(1,8)},'warnings':0,'overfull':0,'underfull':0,'undefined':0,'final_two_pass_local_build_succeeded':True,'native_compile_request_cells':['526','530'],'native_compile_request_cell':'530','native_compile_success_observed':True,'native_final_success_message':"The current source compiled successfully with the desktop editor's compiler.",'existing_editor_unchanged':True,'independent_acceptance':False,'original_closed':False,'accepted_paper_count_unchanged':59,'scope':'Finite TV truncation and absolute-energy truncation modulus; directed admissible joint filter imposes only energy/generic errors, no output convergence. Uniform bounded cap comparison gives all unbounded energy-complete diagonal weak limits; finite absolute planes derive barycenter energy limits without new barycenter assumptions; fixed polarization gives all mixed weak and energy coefficients. Finite mixed domination and ordered absolute tails give paired moving relative weighted moments with independently changing test index.','remaining':'Actual genuine scalar/output/full-list antecedents; every fixed original unbounded test against physical auxiliary outputs needs separate singular-reference-defect and genuine-test-error control; further nonzero zero-volume range.'}
save(D/'publication-binding.json',b)
data=[]
for label,p in [
 ('WHOLE159',K/'public-P16.5-round159-partial-conditional-attainment-reader/paper.tex'),
 ('WHOLE201',K/'P16.5-strict-Borel-locality-from-bounded-moving-maxima-candidate-20261006-continuation201.tex'),
 ('WHOLE202',K/'P16.5-filtered-quotient-traces-and-genuine-mixed-measures-candidate-20261006-continuation202.tex')]:
    data.append({'label':label,'file':str(p),'sha256':sha(p),'whole_body_root_read':True,'authority':'Unreviewed conditional or finite proof data, not caller theorem grant.'})
ledger={'recorded_utc':now,'classification':b['classification'],'final_tex_sha256':sha(T),'whole_final_source_root_read':True,'whole_final_source_read_chunks':b['whole_final_tex_root_read_chunks'],'whole_final_visual_pages':list(range(1,8)),'conditional_proof_data':data,'new_proofs':['Finite energy identity bounds deep-region mass by (n+1)B/C; finite strict locality and equal raw mass bound truncation TV by twice that mass.','Finite plane at lower cap plus pointwise cap difference and finite absolute estimate bound truncated ordered energy gaps by generic error plus original ordered energy gap to exponent2^-n. No quadratic bound for unbounded slots.','Actual directed degree/obstacle/tolerance filter gives jointly cofinal energy/generic-complete nets using finite-list full-section convergence; no output convergence assumed.','Fixed cap global twists give uniform C0 measure difference; compare each moving lower cap with a fixed canonical upper cap, then upper index endpoint; remove cap by TV and genuine decreasing weak continuity.','Finite ordered planes and absolute estimates at barycenter outputs derive all rational barycenter energy completeness from individual completeness; fixed finite unisolvent inversion identifies all mixed weak limits and energy coefficients.','Finite mixed domination and ordered absolute test errors compare an independently moving test to a fixed model upper test; bounded fixed test passes weak limits on a fixed compact U collar, then genuine ordered errors pass to actual test.'],'generic_errors_retained':True,'raw_volumes_retained':True,'conditional_actual_foundations_asserted_true':False,'fixed_original_unbounded_test_on_physical_outputs_claimed':False,'whole_primary_sources_read':False,'all_recursive_primary_foundations_read':False,'new_primary_sources_retrieved':False,'ordinary_background_not_recursively_reproved':['Finite nef graph/Hodge and bounded model locality, applied from whole159/201 proof units.','Finite fixed-twist algebraic positive-product comparison, applied only in the bounded range from201.','Compact Hausdorff Radon collars and finite polynomial interpolation.'],'native_final_compilation_success_observed':True,'independent_acceptance':False,'original_closed':False,'accepted_paper_count_unchanged':59,'active_private_outputs_read':False,'hot_feedback_sent':False}
save(K/'P16.5-continuation203-root-source-application-and-read-scope-20261006.json',ledger)
prior=json.loads((G/'push-receipt-continuation166.json').read_text())
assert prior['commit_sha']=='29e939088159937de76a0605f8b2b4a662146b0d'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
S=K/'small-batch158161-public-status-20261006-continuation167';S.mkdir();items=[]
for n in (158,161):
    C=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json';save(p,st)
    items.append({'round':n,'atom':'P16.5','directory':str(C),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Foundation158 and whole40-page scalar/conditional bridge161 independent reviews. New203 frozen energy-complete moving progress is not hot feedback.'}
F=G/'continuation167-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers']==59 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
    j.update(updated_utc=now,current_small_batch=batch,P16_5_energy_complete_unbounded_moving203=b,github_pending_checkpoint='continuation167 frozen',goal_state='8/42 originals solved;34 open;59 accepted supporting papers. New2037-page unreviewed conditional finite truncation/energy-complete joint filter identifies all unbounded full-system diagonal/mixed weak limits and paired relative weighted moments. It does not prove fixed original unbounded-test integration against every physical auxiliary output; singular-reference defect retained. Actual foundations and further zero-volume range remain unproved. Separate158 and161 whole reviews unchanged; no hot feedback.')
    for target in j.get('targets',[]):
        if target['id']=='P16.5':
            target['current_focus']='Foundation158 and whole40-page bridge161 reviews pending. New203 conditional energy-complete unbounded full-system weak diagonal/mixed identification, individual-to-barycenter energy completeness and independently changing paired relative weighted tests via finite cap TV/absolute gap. Actual foundations and fixed original-test physical reference defect still unresolved.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
lines=(R/'checklist-current.tsv').read_text().splitlines()
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P16.5':
        row[2]='New2037-page unreviewed conditional all unbounded energy-complete full-system diagonal/mixed weak limits and paired moving relative weighted moments. Actual foundations and fixed original-test physical reference defect open.158/161 separate whole reviews pending.'
    lines[i]='\t'.join(row)
(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
save(F/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':59,'new_unreviewed_continuation':203,'pages':7,'new_original_closure':None,'new_independent_acceptance':None,'active_batch':[x['round'] for x in active],'active_private_outputs_read':False,'hot_feedback_sent':False,'native_final_compiler_success_observed':True,'existing_editor_unchanged':True,'whole_goal_blocked':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.out','.aux')
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation167/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for p in (T,D/'paper.pdf',D/'publication-binding.json',K/'P16.5-continuation203-root-source-application-and-read-scope-20261006.json',G/'push-receipt-continuation166.json',R/'record_verified166_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation167.json'
save(M,{'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':59,'commit_message':'Record energy-complete unbounded moving and paired weighted limits','scope':'New2037-page unreviewed conditional finite cap TV and absolute truncation-gap estimates, explicit energy/generic-only joint filter, all unbounded full-system diagonal/mixed weak limits and paired relative weighted moments independent of degree selection. Every fixed original unbounded test at physical auxiliary outputs still needs singular-reference/genuine-test error control; actual energy/output/moving antecedents and further nonzero zero-volume range remain unresolved.8/42 originals and59 supporting papers unchanged; native final compile success observed; no active private reads/hot feedback.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'public_states':[{k:x[k] for k in ('round','observed_status','observed_utc')} for x in items]},indent=2))
