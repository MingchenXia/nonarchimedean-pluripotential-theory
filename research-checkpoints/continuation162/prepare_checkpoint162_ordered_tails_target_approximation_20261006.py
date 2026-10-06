from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';now=datetime.now(timezone.utc).isoformat();sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):assert not p.exists(),str(p);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
prev=G/'push-receipt-continuation161.json';prior=json.loads(prev.read_text());assert prior['commit_sha']=='9e3a5396216d4b06b61258d023ec355b884fc2c0' and all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
readers={157:K/'public-P16.5-round157-partial-ordered-gap-tails-reader',199:K/'public-P16.5-continuation199-target-output-approximation-reader'};bindings={}
for n,d in readers.items():
    p=d/'publication-binding.json';b=json.loads(p.read_text());assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256'] and not b['independent_acceptance'] and not b['original_closed'] and b['whole_final_tex_root_read'];assert b['warnings']==b['overfull']==b['undefined']==0
    if n==157:b.update(actual_visual_pages=[1,4,8,12],native_compile_request_cell='419',native_compile_success_observed=False);p.write_text(json.dumps(b,indent=2)+'\n')
    bindings[n]=b
save(K/'P16.5-round157-completed-partial-root-reading-and-scope-record-20261006.json',bindings[157])
S=K/'small-batch158159-public-status-20261006-continuation162';S.mkdir();items=[]
for n in (157,158,159):
    C=next((R/f'campaigns/round-{n}').iterdir());st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if n==157:assert st['status']=='completed' and st['calls']['unsettled']==0
    f=json.loads((C/'freeze.json').read_text());body,key=('argument.md','argument_sha256') if n==158 else ('input.json','input_sha256')
    for name,field in [('task.json','task_sha256'),('settings.json','settings_sha256'),(body,key)]:assert sha(C/name)==f[field]
    p=S/f'round{n}-public-native-status.json';save(p,st);items.append({'round':n,'atom':'P16.5','directory':str(C),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'launch_record':json.loads((C/'launch-record.json').read_text()),'frozen_metadata':f,'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2 and all(x['round'] in (158,159) for x in active)
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Independent whole genuine foundation158 review and full original159 after new arbitrary-target-output approximation bridge.'}
F=G/'continuation162-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text());assert j['historical_reviewed_scoped_papers']==59 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
    j.update(updated_utc=now,current_small_batch=batch,P16_5_completed_partial157=bindings[157],P16_5_arbitrary_target_output_approximation199=bindings[199],github_pending_checkpoint='continuation162 frozen',goal_state='8/42 originals solved;34 open;59 accepted supporting papers. Completed15712-page partial and1995-page target-output approximation are unreviewed conditional progress, no new closure. Independent whole foundation158 and full original159 remain the current two-campaign batch.')
    for target in j.get('targets',[]):
        if target['id']=='P16.5':target['current_focus']='Full original159 active after new conditional199 approximate stationarity yields arbitrary target as weak bounded-cost output limit before attainment.157 reconstructed bounded density/target algebraic nullness and ordered-gap output tails conditional on F. Independent whole foundation158 review active. All full mixed/locality/attainment/every-uniqueness obligations retained.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
lines=(R/'checklist-current.tsv').read_text().splitlines()
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P16.5':row[2]='Completed15712-page partial, output-family tails/whole planes conditional on unaudited F. New1995-page conditional approximate-stationarity target-output limit before attainment. Independent whole foundation158 '+next(x['observed_status'] for x in items if x['round']==158)+'; full original159 '+next(x['observed_status'] for x in items if x['round']==159)+'. Full original open.'
    lines[i]='\t'.join(row)
(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
save(F/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':59,'new_independent_acceptance':None,'new_original_closure':None,'new_unreviewed_papers':[157,199],'active_batch':[x['round'] for x in active],'active_private_outputs_read':False,'hot_feedback_sent':False,'native_compiler_success_observed':False,'existing_editor_unchanged':True,'whole_goal_blocked':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.out','.aux');files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation162/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for n,d in readers.items():
    b=bindings[n]
    for p in (Path(b['tex']),Path(b['pdf']),d/'publication-binding.json'):add(p)
    if n==157:
        for name in ('source-ledger.json','remaining-gaps.json','status.json'):add(d/name)
        add(K/'P16.5-round157-actual-canonical-author-result-20261006.json');add(K/'P16.5-round157-completed-partial-root-reading-and-scope-record-20261006.json')
    else:add(K/'P16.5-continuation199-root-source-application-and-read-scope-20261006.json')
C=next((R/'campaigns/round-159').iterdir())
for name in ('task.json','settings.json','freeze.json','mathematical-data-bindings.json','input.json','launch-record.json'):add(C/name)
for p in (prev,R/'record_verified161_20261006.py',R/'publish_partial157_finalize199_prepare_original159_20261006.py',R/'launch_frozen_original159_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation162.json';save(M,{'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':59,'commit_message':'Record conditional ordered-gap tails and arbitrary-target output approximation','scope':'Completed15712-page candidatefalse scalar reconstruction/target algebraic nullness and finite ordered gaps; output-family tails/whole planes conditional on F. New unreviewed1995-page model-near-maximizer output convergence to every intrinsic target before attainment, directed Radon proof, uniform genuine Taylor transfer and optional fixed-E1 integrals. Fresh full original159 with both papers launched beside independent foundation158.8/42 originals and59 accepted papers unchanged; no new acceptance or full closure, native compiler success or private active-output reading.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'statuses':[{k:x[k] for k in ('round','observed_status','observed_utc')} for x in items]},indent=2))
