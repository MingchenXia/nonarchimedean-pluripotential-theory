from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';D=R/'deliverables/scoped-P19.2-general-joint-entropy-fixed-start';now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):assert not p.exists(),str(p);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
b=json.loads((D/'publication-binding.json').read_text());v=json.loads((D/'independent-review-and-final-correction-binding.json').read_text());review=json.loads(Path(v['review']).read_text())
assert sha(b['tex'])==b['tex_sha256']==v['final_tex_sha256'] and sha(b['pdf'])==b['pdf_sha256']
assert b['pages']==8 and b['warnings']==b['overfull']==b['undefined']==0 and b['whole_final_tex_root_read']
assert review['verdict']=='PASS' and len(review['premises'])==5 and len(review['passages'])==18 and v['whole_report_all5premises_all18passages_root_read']
b.update(recorded_utc=now,classification='Independently accepted precisely scoped supporting theorem; original P19.2 remains open.',independent_acceptance=True,review_verdict='PASS',review=v['review'],review_sha256=v['review_sha256'],review_scope=v['accepted_scope'],harmless_wording_correction=v['harmless_mathematical_wording_correction'],original_closed=False,accepted_paper_count=59,actual_visual_pages=[1,4,6,8],native_compile_request_cells=['390','394'],native_compile_request_cell='394',native_compile_success_observed=False)
(D/'publication-binding.json').write_text(json.dumps(b,indent=2)+'\n')
ledger={'recorded_utc':now,'classification':'Quote-free applications for independently accepted scoped joint-entropy theorem.','final_tex_sha256':b['tex_sha256'],'whole_final_tex_root_read':True,'independent_review_sha256':v['review_sha256'],'whole_canonical_review_root_read':True,'whole_author_source_ledger_root_read':True,'external_coverage_valid':True,'caller_grants':['R entire originalP19.1','T exact zero-start one-branch finite-height toric profile','C exact CPn n>=2 finite-H absolute endpoint','S exact singular-start relative-profile and stated general lemmas'],'source_applications':[{'premise_index':x['premise_index'],'complete_mathematical_statement':x['exact_statement'],'independent_external_passage_ids':x['independent_external_passage_ids']} for x in v['external_coverage']],'reviewer_primary_read_scope':'Complete published BDL Propositions4.4/4.5 and Theorem4.7 with definitions and nonpluripolar-product identification; complete DZ v2 Theorem10.1 statement/proof, DXZ v3 Section2.1 envelope definitions.','root_primary_read_scope':'Entire canonical review report, all5premises/all18passages and complete own author application ledger; no claim of ROOT whole BDL/DZ/DXZ papers or all recursive foundations read.','primary_quotations_republished':False,'excluded_external_evidence':v['task_assumption_passage_excluded_from_external_coverage'],'convention_check':'dd^c=i/(2pi)partialbarpartial; t=-log|tau|^2; u/(2pi) gives BDL conventions; probability entropy coefficient1.','limitations':'No fixed-time entropy continuity, closed relative-P density, arbitrary nonmaximal-ray approximation or infinite-initial-entropy-start theorem.','original_closed':False,'accepted_scope':v['accepted_scope'],'existing_editor_unchanged':True}
save(D/'source-application-ledger.json',ledger)
save(K/'P19.2-round156-general-joint-entropy-acceptance-and-original-scope-record-20261006.json',{'recorded_utc':now,'round':156,'classification':'Exactly scoped supporting-paper acceptance only.','canonical_verdict':'PASS','whole5premises18passages_root_read':True,'external_coverage_valid':True,'accepted_paper_count_before':58,'accepted_paper_count_after':59,'originals_solved':8,'originals_open':34,'new_original_closure':None,'paper_binding':b,'whole_goal_blocked':False})
S=K/'small-batch157158-public-status-20261006-continuation161';S.mkdir();items=[]
for n in (156,157,158):
    C=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if n==156:assert st['status']=='completed' and st['calls']['unsettled']==0
    p=S/f'round{n}-public-native-status.json';save(p,st);items.append({'round':n,'atom':'P19.2' if n==156 else 'P16.5','directory':str(C),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'launch_record':json.loads((C/'launch-record.json').read_text()),'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2 and all(x['round'] in (157,158) for x in active)
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Full original P16.5 author157 and independent review158 of whole genuine foundations151 and bounded obstacle density198.'}
b198=json.loads((K/'public-P16.5-continuation198-bounded-weighted-reader/publication-binding.json').read_text());assert b198['whole_final_tex_separately_root_read'] and b198['actual_visual_pages']==[1,2,3,4]
prev=G/'push-receipt-continuation160.json';prior=json.loads(prev.read_text());assert prior['commit_sha']=='e2c2c9e598391b2421a271eb512489472a507f61' and all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==58 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
    j.update(updated_utc=now,historical_reviewed_scoped_papers=59,P19_2_accepted_general_joint_entropy156=b,P16_5_bounded_obstacle_density198=b198,current_small_batch=batch,github_pending_checkpoint='continuation161 frozen',goal_state='8/42 originals solved;34 open;59 independently accepted supporting papers. Scoped general joint entropy156 accepted; full original P19.2 remains open. Whole P16.5 author157 and independent foundation158 review continue; at most two campaigns.')
    for target in j.get('targets',[]):
        if target['id']=='P19.2':
            target['current_focus']='Whole general fixed-start maximal joint-entropy theorem independently PASS156, final8-page paper checked. Closed relative P profiles, arbitrary nonmaximal rays and other residual branches remain open.'
            target['reviewed_papers'].append({'round':156,'scope':b['review_scope'],'source':b['tex'],'pdf':b['pdf'],'review':b['review'],'full_original_atom_solved':False,'accepted':True})
        if target['id']=='P16.5':target['current_focus']='Full original author157 ongoing; independent foundation158 review tests entire genuine foundation151 and new bounded section-density198, all proposed nonample bridges still unreviewed.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
lines=(R/'checklist-current.tsv').read_text().splitlines()
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P19.2':row[2]='General fixed-start maximal joint entropy supporting theorem independently PASS156;8-page final.59 accepted supporting papers overall. Closed relative P-density/nonmaximal branches open; original open.'
    if row[0]=='P16.5':row[2]='Full original author157 '+next(x['observed_status'] for x in items if x['round']==157)+'; independent whole genuine foundation151 and bounded section-density198 review158 '+next(x['observed_status'] for x in items if x['round']==158)+'. Full original open; all new nonample bridges unreviewed.'
    lines[i]='\t'.join(row)
(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
F=G/'continuation161-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
save(F/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':59,'new_independent_acceptance':156,'new_original_closure':None,'new_unreviewed_paper':198,'active_batch':[x['round'] for x in active],'active_private_outputs_read':False,'hot_feedback_sent':False,'native_compiler_success_observed':False,'existing_editor_unchanged':True,'whole_goal_blocked':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.out','.aux');files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation161/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for name in ('P19.2-paper.tex','P19.2-paper.pdf','publication-binding.json','independent-review-and-final-correction-binding.json','source-application-ledger.json','author-source-applications.json'):add(D/name)
add(K/'P19.2-round156-actual-canonical-independent-review-result-20261006.json');add(K/'P19.2-round156-general-joint-entropy-acceptance-and-original-scope-record-20261006.json')
for p in (Path(b198['tex']),Path(b198['pdf']),K/'public-P16.5-continuation198-bounded-weighted-reader/publication-binding.json',K/'P16.5-continuation198-root-source-application-and-read-scope-20261006.json'):add(p)
C=next((R/'campaigns/round-158').iterdir())
for name in ('task.json','settings.json','freeze.json','mathematical-data-bindings.json','argument.md','launch-record.json'):add(C/name)
for p in (prev,R/'record_verified160_20261006.py',R/'finalize198_prepare_foundation158_and_joint156_20261006.py',R/'launch_frozen_foundation_review158_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation161.json';save(M,{'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':59,'commit_message':'Accept scoped joint entropy theorem and review genuine big-class foundations','scope':'Independent scoped156 PASS of general compact-Kahler fixed actual finite-entropy-start maximal joint entropy and infinite-target divergence, final8-page paper and exact correction/source scopes. New unreviewed conditional1984-page all bounded-obstacle section density and general weak-output absolute C0-L1 approximation. Whole151+198 independent review158 launched beside whole original157; at most two active.8/42 originals unchanged,59 accepted supporting papers; no full original closure, native compiler success, active private reads or hot feedback.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'accepted_papers':59,'originals_solved':8,'statuses':[{k:x[k] for k in ('round','observed_status','observed_utc')} for x in items]},indent=2))
