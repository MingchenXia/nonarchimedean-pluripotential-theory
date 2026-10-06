from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
T=K/'P16.5-horizontal-fixed-factor-and-retained-vertical-correction-candidate-20261006-continuation209.tex'
D=K/'public-P16.5-continuation209-vertical-correction-reader'
now=datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(T)=='4e727fcbc6b19c9a5b424ab9a8d8ddc53d0da01c72d6dd0a91933756f6f932da'
assert sha(D/'paper.pdf')=='019f662157f38525f13ed6f648cbd9269647eddcb69283ca0e8958940993d6a2'
assert len(T.read_text().splitlines())==239
assert not any(x in (D/(T.stem+'.log')).read_text() for x in ('Warning:','Overfull','Underfull','undefined'))
binding={'recorded_utc':now,'classification':'Unreviewed explicit finite counterexample and actual moving-factor correction209; no original closure','tex':str(T),'tex_sha256':sha(T),'pdf':str(D/'paper.pdf'),'pdf_sha256':sha(D/'paper.pdf'),'pages':4,'source_lines':239,'whole_final_source_root_read':True,'all4final_visual_pages_root_read':True,'actual_visual_pages':[1,2,3,4],'two_pass_local_compile':'SUCCESS','native_final_compile':'SUCCESS','native_final_message':"The current source compiled successfully with the desktop editor's compiler.",'warnings':0,'overfull':0,'underfull':0,'original_editor_unchanged':True,'independent_acceptance':False,'original_closed':False,'scope':'Actual full absolute moving bundle retains T_m^ver after removing only horizontal fixed components. Explicit X=Bl_p P2,L=H+E, time blowup E×0,D=-B has all original weights0 and quotient0; omitting vertical B instead gives auxiliary energy-1/3 and unit atom ord_E rather than generic. Correct full bundle A+D+Tver+cF-Gvert/m retains whole-system interpretation.','affected_frozen_drafts':[{'round':163,'formula':'(5.2)','source_sha256':'53428fabcc63e9c04ef5f6f05c79dde4b415d833c3b78c27c95224794c58da61'},{'continuation':208,'formula':'(7)','source_sha256':'850d724b2f4435e0a45d93c3a1cafc9265749fc502a2982db4c6105b8bd55867'}],'known_compatible_formula':'round163(9.2) retains vertical term correctly','frozen_author_papers_preserved':True,'mathematical_certification':False,'active_private_outputs_read':False,'hot_feedback_sent':False,'whole_primary_sources_read':False,'recursive_background_proofs_read':False,'remaining':'Reconstruct complete corrected original proof with this formula throughout, then obtain fresh whole independent review; current166 reviews unchanged historical163.'}
(D/'publication-binding.json').write_text(json.dumps(binding,ensure_ascii=False,indent=2)+'\n')
ledger=K/'P16.5-continuation209-root-finite-geometric-correction-and-read-scope-20261006.json'
ledger.write_text(json.dumps({'recorded_utc':now,'classification':binding['classification'],'whole_source_read':True,'actual_source_hash':sha(T),'proof_data':'Only actual finite section spaces, complete filtered flags, effective horizontal division, principalized residual ideals, and finite nef intersections; no whole nonample S-M or equation grant.','ordinary_background':['Normal proper birational section descent','Characteristic-zero common smooth equivariant principalization','Generation implies nefness','Smooth codimension2 blowup exceptional projective-bundle and self-intersection formulas'],'explicit_reconstruction':['All H0(m(H+E)) have exactly the generic E factor by repeated negative-degree restriction','Model blowup ideal(O(-E),t) gives f_D=-min(v(E),1)','Every complete original feasible weight is0; quotient is identically0','Only E^hor is the absolute base divisor; Tver=B is consumed by D=-B','Missing B changes component masses0,1 and cubic volume3c-1, yielding energy-1/3'],'external_background_recursively_reproved':False,'new_primary_retrieval':False,'independent_review':None,'original_closed':False,'stronger_unbounded_physical_weighted_defect_resolved':False,'active_private_output_read':False,'hot_feedback_sent':False},indent=2)+'\n')
prior=json.loads((G/'push-receipt-continuation174.json').read_text());assert prior['commit_sha']=='c276910b860adabfec83dda9674812db3d308b49'
assert all(prior[x] for x in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
S=K/'small-batch158166-public-status-20261006-continuation175';S.mkdir();items=[]
for n in (158,166):
 c=next((R/f'campaigns/round-{n}').iterdir());s=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(s,indent=2)+'\n');items.append({'round':n,'atom':'P16.5','directory':str(c),'observed_status':s['status'],'observed_utc':s['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'158actual-foundation and166unchanged-full-original audits continue. Independent root209finite blowup example exposes missing vertical term in163(5.2)/208(7); exact horizontal-only moving formula repair drafted. No new result fed to either active reviewer.'}
F=G/'continuation175-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==63 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
 j.update(updated_utc=now,current_small_batch=batch,P16_5_actual_horizontal_fixed_factor_and_vertical_correction209=binding,github_pending_checkpoint='continuation175 frozen',goal_state='8/42 originals independently accepted;34open;63supporting papers. Author163full candidate remains unaccepted. Root2094-page explicit finite blowup computation finds missing Tver in163(5.2) and208(7): correct quotient0 vs omitted-term energy-1/3/divisorial mass. Horizontal-only factor removal and retained vertical moving formula reconstructed; complete corrected original proof and fresh independent audit still needed. Frozen originals and active158166 preserved, no feedback; maximum2campaigns. Stronger physical unbounded fixed-test convergence remains unproved.')
 j['P16_5_full_original_candidate163']['root_acceptance_withheld']=True;j['P16_5_full_original_candidate163']['new_root_finite_correction209']=str(T)
 j['P16_5_actual_complete_moving_and_relative_contraction208']['new_root_finite_correction209']=str(T)
 for target in j.get('targets',[]):
  if target['id']=='P16.5':target['current_focus']=batch['focus']
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
rows=(R/'checklist-current.tsv').read_text().splitlines()
for i,row in enumerate(rows):
 cells=row.split('\t')
 if cells[0]=='P16.5':cells[2]='Root209finite counterexample identifies missing Tver in163/208; actual full moving formula repaired, full corrected proof next. Frozen158166active; original open;8/42,63supports.'
 rows[i]='\t'.join(cells)
(R/'checklist-current.tsv').write_text('\n'.join(rows)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_supporting_papers':63,'new_unreviewed_finite_correction':209,'pages':4,'affected_frozen_drafts':[163,208],'active_batch':[x['round'] for x in active],'no_hot_feedback':True,'original_closed':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.aux','.out');files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation175/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
 for p in sorted(folder.iterdir()):add(p)
for p in (T,D/'paper.pdf',D/'publication-binding.json',ledger,G/'push-receipt-continuation174.json',R/'record_verified174_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation175.json';M.write_text(json.dumps({'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':63,'commit_message':'Record finite vertical-factor obstruction and exact full-system repair','scope':binding['scope']+' Explicit unreviewed root correction; no original acceptance or active reviewer feedback.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'manifest_sha256':sha(M),'files':len(files),'active_batch':[x['round'] for x in active]},indent=2))
