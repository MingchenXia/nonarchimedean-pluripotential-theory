from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K, G = R/'root-checks', R/'github-checkpoint'
P = K/'public-P16.5-round163-full-original-candidate-reader'
C = next((R/'campaigns/round-166').iterdir())
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
prior = json.loads((G/'push-receipt-continuation173.json').read_text())
assert prior['commit_sha'] == '728a240fe3d219cead75408c760d3168b698b2e3'
assert all(prior[k] for k in ('remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'))
assert sha(P/'paper.tex') == '53428fabcc63e9c04ef5f6f05c79dde4b415d833c3b78c27c95224794c58da61'
assert sha(P/'paper.pdf') == 'fe4465005f56405069df9f1dca5cdc06fc67c50531f9bcbe9073becc2dec23ca'
b = json.loads((P/'publication-binding.json').read_text())
assert b['paper']['native_root_compilation']=='SUCCESS' and b['paper']['all_pages_root_visually_read']
b['updated_utc']=now
(P/'publication-binding.json').write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n')
f = json.loads((C/'freeze.json').read_text())
launch = json.loads((C/'launch-record.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
    assert sha(C/name)==f[key]
S = K/'small-batch158166-public-status-20261006-continuation174'
S.mkdir()
items=[]
for n in (158,163,166):
    c=next((R/f'campaigns/round-{n}').iterdir())
    st=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout)
    p=S/f'round{n}-public-native-status.json'
    p.write_text(json.dumps(st,indent=2)+'\n')
    items.append({'round':n,'atom':'P16.5','directory':str(c),'observed_status':st['status'],'observed_utc':st['observedAt'],'public_status':str(p),'public_status_sha256':sha(p),'private_active_output_read':False,'hot_feedback_sent':False,'original_closed':False})
active=[x for x in items if x['observed_status']=='running']
assert len(active)<=2 and sum(json.loads(Path(x['public_status']).read_text())['calls']['unsettled'] for x in items)<=2
batch={'recorded_utc':now,'items':items,'active_items':active,'maximum_concurrent_campaigns':2,'focus':'Whole actual-foundation audit158 and full original-candidate audit166. Author163 completed with candidate=true; complete16-page paper and all five notes frozen for fresh original-scope review. Prepared supporting165 remains unlaunched because full-original review has priority.'}
review=dict(f,prepared_only=False,launch_record=str(C/'launch-record.json'),launch_record_sha256=sha(C/'launch-record.json'),pid=launch['pid'],independent_verdict=None,original_closed=False)
F=G/'continuation174-publication-records'
F.mkdir()
for name in ('active-work.json','checklist-current.json'):
    p=R/name;j=json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers']==63 and len(j['fully_solved_original_atoms'])==8 and j['remaining_open_original_atoms']==34
    j.update(updated_utc=now,current_small_batch=batch,P16_5_full_original_candidate163=b,current_full_original_review166=review,github_pending_checkpoint='continuation174 frozen',goal_state='8/42 originals independently accepted;34 open;63 accepted supporting papers. P16.5 author163 returned full-original candidate=true with exact16-page standalone paper; source/notes/read ledgers and native byte bindings checked, all16 visual pages read and native compiler succeeded. Fresh full-original independent review166 launched on unchanged complete original scope, all actual foundations require reconstruction from G0/G1.158 remains separate actual-foundation audit. Maximum two active campaigns. No original closure before whole independent verdict. Prepared165 preserved unlaunched. Stronger fixed-original-unbounded weighted physical-output assertion expressly unproved and its necessity for original completion explicitly assigned to166.')
    if 'current_original_campaign163' in j:
        j['current_original_campaign163'].update(observed_status='completed',candidate=True,original_closed=False,full_original_review_round=166)
    for t in j.get('targets',[]):
        if t['id']=='P16.5':t['current_focus']=batch['focus']
    p.write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
rows=(R/'checklist-current.tsv').read_text().splitlines()
for i,row in enumerate(rows):
    cells=row.split('\t')
    if cells[0]=='P16.5':cells[2]='Whole16-page original candidate163 completed; fresh full-original audit166 active with158. Stronger physical unbounded-test assertion unproved;166 audits whether it is essential. Original open;8/42 solved,63 supports.'
    rows[i]='\t'.join(cells)
(R/'checklist-current.tsv').write_text('\n'.join(rows)+'\n')
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):shutil.copyfile(R/name,F/name)
(F/'scope-observation.json').write_text(json.dumps({'recorded_utc':now,'originals_solved':8,'originals_open':34,'accepted_supporting_papers':63,'author_round':163,'canonical_candidate':True,'whole_pages':16,'independent_review_round':166,'independent_verdict':None,'active_batch':[x['round'] for x in active],'prepared165_unlaunched':True,'existing_editor_unchanged':True,'private_active_output_read':False,'hot_feedback_sent':False},indent=2)+'\n')
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite','.png','.log','.aux','.out')
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation174/'+str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in (F,S,P):
    for p in sorted(folder.iterdir()):
        if p.suffix in ('.json','.tex','.pdf','.md','.py','.tsv'):add(p)
for name in ('task.json','argument.md','settings.json','freeze.json','mathematical-data-bindings.json','original-task.json','canonical-author-result.json','launch-record.json'):add(C/name)
for p in (K/'P16.5-round163-actual-canonical-author-result-20261006.json',G/'push-receipt-continuation173.json',R/'record_verified173_20261006.py',R/'prepare_full_original_review166_20261006.py',R/'launch_frozen_original_review166_20261006.py',Path(__file__)):add(p)
for name in ('active-work.json','checklist-current.json','checklist-current.tsv'):add(F/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest={'generated_utc':now,'repository':prior['repository'],'branch':prior['branch'],'expected_previous_checkpoint':prior['commit_sha'],'files':files,'file_count':len(files),'fully_solved_original_atoms':b.get('fully_solved_original_atoms',json.loads((R/'active-work.json').read_text())['fully_solved_original_atoms']),'remaining_open_atoms':34,'historical_reviewed_scoped_papers':63,'commit_message':'Publish complete P16.5 original candidate and start independent full-scope audit','scope':'Exact author16316-page standalone original candidate, all5canonical notes, whole-source/all-page/native compilation bindings, exact frozen decoded native input and16whole supplied slices verified. Fresh Xean native gpt-6.1-sol xhigh full-original review166 with onlyG0G1grants; full actual foundations reconstructed and explicit stronger physical-weighted gap assessed for original necessity.158separate audit continues;165unlaunched. No original closure; counts8/42 and63 unchanged.'}
M=G/'upload-manifest-continuation174.json'
M.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest':str(M),'manifest_sha256':sha(M),'files':len(files),'active_batch':[x['round'] for x in active],'originals_solved':8},indent=2))
