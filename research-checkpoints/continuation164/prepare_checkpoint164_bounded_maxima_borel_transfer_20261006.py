from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint';now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
prev=G/'push-receipt-continuation163.json';prior=json.loads(prev.read_text())
assert prior['commit_sha']=='dd759b205e536000c7d9f2992ffb405d532f0ef4'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
readers={159:K/'public-P16.5-round159-partial-conditional-attainment-reader',201:K/'public-P16.5-continuation201-strict-Borel-comparison-reader'};bindings={}
for n,d in readers.items():
    b=json.loads((d/'publication-binding.json').read_text())
    assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256'] and b['whole_final_tex_root_read']
    assert b['warnings']==b['overfull']==b['undefined']==0
    assert not b['independent_acceptance'] and not b['original_closed'] and b['actual_visual_pages']
    bindings[n]=b
S=K/'small-batch158160-public-status-20261006-continuation164';S.mkdir();items=[]
for n in (158,159,160):
    C=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    if n==159:assert st['status']=='completed' and st['calls']['unsettled']==0
    f=json.loads((C/'freeze.json').read_text());body,key=('argument.md','argument_sha256') if n==158 else ('input.json','input_sha256')
    for name,field in [('task.json','task_sha256'),('settings.json','settings_sha256'),(body,key)]:assert sha(C/name)==f[field]
    p=S/f'round{n}-public-native-status.json';save(p,st)
    items.append({'round':n,'atom':'P16.5','directory':str(C),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'launch_record':json.loads((C/'launch-record.json').read_text()),'frozen_metadata':f,'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running'];assert len(active)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Independent entire foundation158 review and full original160 after complete159 conditional attained/separated equation and new201 bounded maximum/Borel transfer.'}
F=G/'continuation164-publication-records';F.mkdir()
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers']==59 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
    j.update(updated_utc=now,current_small_batch=batch,P16_5_completed_partial159=bindings[159],P16_5_conditional_bounded_maxima_Borel_transfer201=bindings[201],github_pending_checkpoint='continuation164 frozen',goal_state='8/42 originals solved;34 open;59 independently accepted supporting papers. Completed15914-page conditional actual attainment/every-solution separation and new2018-page bounded-max/Borel comparison and PSH-pole nullness remain unreviewed. Entire foundations, all unbounded mixed/physical weighted identification and nonpolar negligible sets remain open. At most two native campaigns158/160, no hot feedback.')
    for target in j.get('targets',[]):
        if target['id']=='P16.5':target['current_focus']='Full original160 after completed159 conditional midpoint modulus/attainment/every-solution separation and new201 bounded moving-max identification/strict Borel comparison/PSH-pole covering. Entire genuine S-M foundations and all unbounded mixed/physical weighted independence/nonpolar negligible sets still outstanding; independent whole foundation158 review pending.'
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
lines=(R/'checklist-current.tsv').read_text().splitlines()
for i,line in enumerate(lines):
    row=line.split('\t')
    if row[0]=='P16.5':row[2]='Completed15914-page unreviewed conditional attainment/every-solution separation, repaired finite signed Taylor margin. New2018-page conditional bounded moving-max identification, strict Borel locality/comparison and all genuine PSH-pole nullness. Foundation158 '+next(x['observed_status'] for x in items if x['round']==158)+'; full original160 '+next(x['observed_status'] for x in items if x['round']==160)+'. Full original remains open.'
    lines[i]='\t'.join(row)
(R/'checklist-current.tsv').write_text('\n'.join(lines)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
save(F/'scope-observation.json',{'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_papers':59,'new_unreviewed_papers':[159,201],'new_original_closure':None,'new_independent_acceptance':None,'active_batch':[x['round'] for x in active],'active_private_outputs_read':False,'hot_feedback_sent':False,'native_compiler_success_observed':False,'existing_editor_unchanged':True,'whole_goal_blocked':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.out','.aux')
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation164/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S):
    for p in sorted(folder.iterdir()):add(p)
for n,d in readers.items():
    b=bindings[n]
    for p in (Path(b['tex']),Path(b['pdf']),d/'publication-binding.json'):add(p)
    if n==159:
        for name in ('source-ledger.json','gaps.md','remaining-gaps.json'):add(d/name)
        add(K/'P16.5-round159-actual-canonical-author-result-20261006.json')
        add(K/'P16.5-round159-completed-partial-root-reading-and-scope-record-20261006.json')
    else:add(K/'P16.5-continuation201-root-source-application-and-read-scope-20261006.json')
C=next((R/'campaigns/round-160').iterdir())
for name in ('task.json','settings.json','freeze.json','mathematical-data-bindings.json','input.json','launch-record.json'):add(C/name)
for p in (prev,R/'record_verified163_20261006.py',R/'finalize201_prepare_original160_20261006.py',R/'launch_frozen_original160_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
M=G/'upload-manifest-continuation164.json'
save(M,{'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms'],'remaining_open_atoms':34,'historical_reviewed_scoped_papers':59,'commit_message':'Record bounded moving maxima and conditional strict Borel comparison','scope':'Completed15914-page conditional absolute midpoint modulus/actual no-jump attainment/every-solution separation with entire S-M antecedents explicit, finite Taylor signed bigness margin repaired. New2018-page conditional moving-max exact energy/raw weak identification, fixed-nef collars/test bounds, finite ample-to-nef locality, fixed continuous ramps for strict original Borel locality/comparison, and E1 convex pole covering. Full genuine foundations, all unbounded mixed/physical approximation identification and nonpolar negligible discrepancies remain open. Fresh full original160 beside independent foundation158;8/42 originals and59 accepted papers unchanged, no private active reads/hot feedback or native compiler success claims.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'statuses':[{k:x[k] for k in ('round','observed_status','observed_utc')} for x in items]},indent=2))
