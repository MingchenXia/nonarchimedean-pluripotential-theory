from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';now=datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
T=K/'P16.5-original-big-equation-with-retained-vertical-moving-factors-candidate-20261006-continuation210.tex';D=K/'public-P16.5-continuation210-corrected-original-reader';C=next((R/'campaigns/round-167').iterdir())
assert sha(T)=='d1473f933a5c08096a97df253c259c1d8a7dae583132e35bd5ab2c3b7da9b5f7' and sha(D/'paper.pdf')=='dbd09e24dda266c2a53f4d1614ec2e8f575f2546f7a58a796c9e1470ac7c7553'
b=json.loads((D/'publication-binding.json').read_text());assert b['pages']==18 and b['native_final_compile']=='SUCCESS' and b['all18final_visual_pages_root_read']
f=json.loads((C/'freeze.json').read_text());assert not(C/'work.sqlite').exists() and not(C/'launch-record.json').exists()
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(C/name)==f[key]
old=json.loads((K/'public-P16.5-round163-full-original-candidate-reader/source-application-register.json').read_text())
old['revision210_root_read_scope']={'classification':'Reused byte-bound primary units and complete root reading; no new retrieval or independent acceptance','complete_units':json.loads((K/'public-P16.5-round163-full-original-candidate-reader/publication-binding.json').read_text())['complete_pertinent_primary_units_root_read_this_application'],'new_application':'Whole corrected actual full-system moving formula retains Tver and resolves only residual vertical base after horizontal division; full finite proof and blowup computation in appendix A. Ordinary background must be checked afresh by independent167.','whole_original_independent_verdict':None,'original_closed':False}
(D/'source-application-register.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
prior=json.loads((G/'push-receipt-continuation175.json').read_text());assert prior['commit_sha']=='11ddd50d0263d2bd0b638dd5fc0f001e7bf7000c' and all(prior[x] for x in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
S=K/'small-batch158166-public-status-20261006-continuation176';S.mkdir();items=[]
for n in (158,166):
 c=next((R/f'campaigns/round-{n}').iterdir());s=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(s,indent=2)+'\n');items.append({'round':n,'atom':'P16.5','directory':str(c),'observed_status':s['status'],'observed_utc':s['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'158foundation and166immutable-author163 original audits remain active. Corrected18-page original210 completed locally with retained Tver and complete appendix. Fresh167 whole-original review frozen, not launched; await free slot and read completed canonical reviews before launch decision.165remains unlaunched.'}
F=G/'continuation176-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==63 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
 j.update(updated_utc=now,current_small_batch=batch,P16_5_corrected_original_retained_vertical210=b,prepared_corrected_full_original_review167=f,github_pending_checkpoint='continuation176 frozen',goal_state='8/42originals independently accepted;34open;63supporting papers. Corrected whole18-page P16.5 proposed proof210 retains Tver in5.2 and exact actual horizontal section division throughout; appendix reconstructs full absolute moving bundle and finite Bl_pP2 obstruction. Whole base plus every exact diff, all18final pages, native and two-pass compile checked; zero final warnings. No new native author or independent verdict; original open. Fresh167full-original review prepared and frozen, not launched while158166active; no hot feedback. Prepared165preserved unlaunched. Stronger physical unbounded fixed-test assertion remains separate and unproved.')
 for target in j.get('targets',[]):
  if target['id']=='P16.5':target['current_focus']=batch['focus']
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
rows=(R/'checklist-current.tsv').read_text().splitlines()
for i,row in enumerate(rows):
 cells=row.split('\t')
 if cells[0]=='P16.5':cells[2]='Corrected18-page full-original proof210 includes actual retained Tver formula and full finite appendix; prepared fresh167whole audit unsent.158166active, original open;8/42,63supports.'
 rows[i]='\t'.join(cells)
(R/'checklist-current.tsv').write_text('\n'.join(rows)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_supporting_papers':63,'whole_corrected_original_proof':210,'pages':18,'prepared_fresh_independent_review':167,'launched':False,'active_batch':[x['round'] for x in active],'no_hot_feedback':True,'original_closed':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.aux','.out');files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation176/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
 for p in sorted(folder.iterdir()):add(p)
for p in (T,D/'paper.pdf',D/'publication-binding.json',D/'revision-binding.json',D/'source-application-register.json',D/'README.md',K/'P16.5-continuation210-exact-author163-mathematical-diff.patch',G/'push-receipt-continuation175.json',R/'record_verified175_20261006.py',R/'prepare_corrected_original210_20261006.py',R/'prepare_corrected_original_review167_20261006.py',R/'launch_frozen_corrected_original_review167_20261006.py',Path(__file__)):add(p)
for name in ('task.json','argument.md','settings.json','freeze.json','mathematical-data-bindings.json','original-task.json'):add(C/name)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation176.json';M.write_text(json.dumps({'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':63,'commit_message':'Preserve corrected full P16.5 proof with vertical moving factors and freeze whole audit','scope':'Unreviewed corrected18-page whole original proof210 and exact full actual horizontal division appendix; Tver retained in complete moving bundle, finite surface obstruction fully proved. Exact final source diff, all18visual pages, native and2pass checks, source reading scope and fresh independent167task/argument/settings frozen but unlaunched. Active158166unchanged; no feedback, original open, counts8/42 and63.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'manifest_sha256':sha(M),'files':len(files),'active_batch':[x['round'] for x in active],'prepared_review167':True,'original_closed':False},indent=2))
