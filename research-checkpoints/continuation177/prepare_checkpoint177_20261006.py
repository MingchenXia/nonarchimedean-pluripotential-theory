from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
now=datetime.now(timezone.utc).isoformat(); sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
M=G/'upload-manifest-continuation177.json'; assert not M.exists()
failure=json.loads((K/'P16.5-round166-whole-original-failure-and-correction-binding-20261006.json').read_text())
connection=json.loads((K/'P16.5-round158-settled-native-connection-failure-binding-20261006.json').read_text())
assert failure['verdict']=='FAIL' and failure['whole_report_all9premises_all15passages_root_read'] and connection['mathematical_verdict'] is None
C=next((R/'campaigns/round-167').iterdir()); launch=json.loads((C/'launch-record.json').read_text()); freeze=json.loads((C/'freeze.json').read_text())
assert launch['frozen_math_input_sha256']==freeze['argument_sha256']=='b5d0cfff955ef0caa6bed2a5a8f7e97dd665eb05f433fa61cdc68ef02d51ced9'
prior=json.loads((G/'push-receipt-continuation176.json').read_text()); assert prior['commit_sha']=='492c7a02fc4b5713463225fdc855d7ace6f1a3d2'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
S=K/'small-batch167-public-status-20261006-continuation177'; S.mkdir(); items=[]
for n in (158,166,167):
 c=next((R/f'campaigns/round-{n}').iterdir())
 status=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
 p=S/f'round{n}-public-native-status.json';p.write_text(json.dumps(status,indent=2)+'\n')
 items.append({'round':n,'atom':'P16.5','directory':str(c),'observed_status':status['status'],'observed_utc':status['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'unsettled_calls':status['calls']['unsettled'],'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['unsettled_calls']>0]; assert len(active)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Fresh167 whole corrected18-page original P16.5 audit active;166 full old original FAIL with exact vertical fixed-factor counterexample, independently matching prior ROOT209.158 settled connection failure has no verdict.165 preserved unlaunched. Only G0/G1 grants; original remains open.'}
F=G/'continuation177-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
 p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==63 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
 j.update(updated_utc=now,current_small_batch=batch,P16_5_actual_full_original_review166=failure,P16_5_settled_native_connection_failure158=connection,P16_5_launched_corrected_full_original_review167=launch,github_pending_checkpoint='continuation177 frozen',goal_state='8/42 original problems independently accepted;34 open;63 accepted supporting papers.166 whole old original FAIL: complete moving bundle must retain Tver. ROOT209 finite repair predates completed166 read. Corrected full18-page210 frozen and fresh167 full-original audit launched with exact task and only G0/G1 grants.158 settled native stream disconnection without final verdict. No new acceptance or closure; no hot feedback; prepared165 preserved.')
 if 'P16_5_full_original_candidate163' in j:
  j['P16_5_full_original_candidate163'].update(review_verdict='FAIL',mathematical_certification=False,root_acceptance_withheld=True,completed_original_review_binding=str(K/'P16.5-round166-whole-original-failure-and-correction-binding-20261006.json'))
 p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
rows=(R/'checklist-current.tsv').read_text().splitlines()
for i,row in enumerate(rows):
 cells=row.split('\t')
 if cells[0]=='P16.5':cells[2]='Fresh167 whole corrected18-page original audit active.166 old original FAIL: missing vertical fixed factor, repaired210.158 settled connection failure/no verdict. Original open;8/42,63 supports.'
 rows[i]='\t'.join(cells)
(R/'checklist-current.tsv').write_text('\n'.join(rows)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_supporting_papers':63,'old_full_original_review166':'FAIL','foundation_review158':None,'fresh_full_original_review167_launched':True,'active_batch':[x['round'] for x in active],'original_closed':False,'no_hot_feedback':True,'existing_editor_unchanged':True},indent=2)+'\n')
files=[]
def add(p,remote=None):
 p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.aux','.out')
 files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation177/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
 for p in sorted(folder.iterdir()):add(p)
for p in (K/'P16.5-round166-actual-canonical-independent-review-20261006.json',K/'P16.5-round166-native-model-final-review-20261006.json',K/'P16.5-round166-whole-original-failure-and-correction-binding-20261006.json',K/'P16.5-round158-settled-native-connection-failure-binding-20261006.json',C/'launch-record.json',R/'bind_completed_review166_20261006.py',R/'bind_settled_failure158_20261006.py',R/'launch_frozen_corrected_original_review167_20261006.py',G/'push-receipt-continuation176.json',R/'record_verified176_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M.write_text(json.dumps({'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':63,'commit_message':'Record old P16.5 audit counterexample and launch complete corrected proof review','scope':'Whole completed166 canonical FAIL, all9premises and15 normalized passages, exact native input binding, full finite geometric counterexample and correction scope.158 connection failure has no mathematical verdict; fresh167 whole18-page corrected original review launched using G0/G1 only and unchanged frozen full input. No new original closure or supporting acceptance. Preserve user editor and prepared165.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'manifest_sha256':sha(M),'files':len(files),'active_batch':[x['round'] for x in active],'original_closed':False},indent=2))
