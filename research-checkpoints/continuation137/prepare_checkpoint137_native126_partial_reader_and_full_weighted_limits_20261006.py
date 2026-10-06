from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
import fitz

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation136.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='91d181d137797962ede0f9cf962dd409ae924089'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation136.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
P=K/'public-P16.5-round126-main-reader'
pub=json.loads((P/'publication-preparation.json').read_text())
assert pub['status']=='PARTIAL' and not pub['candidate'] and not pub['independently_accepted']
assert len(fitz.open(P/'P16.5-paper.pdf'))==10
assert pub['overfull_diagnostics']==0 and pub['undefined_diagnostics']==0
for name,key in [('P16.5-argument.md','argument_sha256'),('P16.5-paper.tex','source_sha256'),('P16.5-paper.pdf','pdf_sha256')]:
    assert sha(P/name)==pub[key]
pub['actual_visual_pages']=[1,6,10]
pub['native_compiler_request_cell']=1934
pub['native_compiler_status']='PENDING'
(P/'publication-preparation.json').write_text(json.dumps(pub,ensure_ascii=False,indent=2)+'\n')
own=list(K.glob('*continuation172.md'));assert len(own)==1;own=own[0]
C128=R/'campaigns/round-128/P16.5-general-big-entire-genuine-E1-operator-independent-review'
C129=R/'campaigns/round-129/P16.5-original-entire-general-big-equation-independent-review'
freeze128=json.loads((C128/'freeze.json').read_text());freeze129=json.loads((C129/'freeze.json').read_text())
for c,freeze in [(C128,freeze128),(C129,freeze129)]:
    for name,key in [('argument.md','argument_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(c/name)==freeze[key]
assert not (C129/'review.sqlite').exists()
S=K/'current-small-batch125-128-after-native126-20261006-continuation137';S.mkdir(exist_ok=False)
items=[];observations={}
for n,label,db,pty in [(125,'P16.5-entire-nef-big-variational-equation-independent-review','review.sqlite',47713),
                       (126,'P16.5-original-general-big-relative-operator-and-equation-research','work.sqlite',13496),
                       (128,'P16.5-general-big-entire-genuine-E1-operator-independent-review','review.sqlite',40722)]:
    c=R/f'campaigns/round-{n}'/label
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(r.stdout);assert status['status'] in ['running','completed']
    assert status['calls']['byModel'][0]['model']=='gpt-6.1-sol'
    if n==126:assert status['status']=='completed' and status['work']['completed']==1
    p=S/f'P16.5-round{n}-public-native-status.json';save(p,status)
    observations[n]={'public_status':str(p),'public_status_sha256':sha(p),'observed_utc':status['observedAt'],'observed_status':status['status']}
    if n!=126:items.append({'round':n,'atom':'P16.5','directory':str(c),'database':db,'tool_session_id':pty,
                            'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
                            'scoped_review_only':True,'original_closed':False,'private_active_output_read':False,
                            'hot_feedback_sent':False,**observations[n]})
now=datetime.now(timezone.utc).isoformat()
launch={'recorded_utc':now,'round':128,'frozen_input':freeze128,'tool_session_id':40722,
        'launched':True,'prepared_only':False,**observations[128],'active_inputs_modified':False,
        'scope':'Entire genuine general-big E1 operator and both outer signs only; no inverse theorem granted.',
        'private_active_output_read':False,'hot_feedback_sent':False}
save(S/'round128-launch-and-input-binding.json',launch)
binding={'recorded_utc':now,'proof':str(own),'sha256':sha(own),'whole_saved_final_own_proof_root_read':True,
         'scope':'Own172 extends original continuous L1 approximations to all full outputs with bounded cost, proving relative signed weighted weak continuity for fixed and strongly moving full tests and independent product nets.',
         'independently_accepted':False,'original_closed':False,'active_or_frozen_native_inputs_modified':False,
         'included_in_frozen129':False,'current_native_batch':[i['round'] for i in items if i['observed_status']=='running'],
         'next_native_launch':129,'existing_editor_unchanged':True}
B=K/'P16.5-root-continuation172-entire-weighted-continuity-and-native126-result-binding-20261006.json';save(B,binding)
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Independent125 entire nef-big equation and independent128 general-big genuine operator; original126 completed PARTIAL. Exact original129 full equation review frozen and next.'}
save(S/'current-batch-and-next-launch.json',batch)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==48
    data.update({'updated_utc':now,'current_small_batch':batch,'P16_5_actual_original_research126':pub,
                 'continuation172_entire_relative_weighted_candidate':binding,'launched_general_big_operator_review128':launch,
                 'prepared_original_general_big_equation_review129':freeze129,'next_native_launch_order':[129],
                 'goal_state':'7/42 originals solved;35 open;48 independently accepted scoped papers. Continue small batches.',
                 'github_pending_checkpoint':'continuation137 frozen'})
    if name=='active-work.json':data['next_work']='Launch exact original129 when125 or128 frees a slot. Read completed independent reports in full; reconstruct unresolved proofs. Preserve PARTIAL126 main paper. Push checkpoints regularly.'
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        cols=line.split('\t');assert cols[1]=='open';cols[3]='3'
        cols[2]='Original126 PARTIAL; 10-page main reader, general nonnef signed-domain obstruction and narrower point-blowup equation. Scoped124 PASS paper published. Independent125/128 active; original129 full general-big equation packet frozen and next. Own143--172 full general-big candidate unreviewed; numerical-zero range separate. Original open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation137-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':35,'historical_reviewed_scoped_papers':48,'native126_result':'PARTIAL, candidate=false',
    'current_native_small_batch':[i['round'] for i in batch['active_items']],'next_launch':129,
    'new_independent_mathematical_acceptance':False,'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr'} and 'LOCALONLY' not in p.name
    if p.suffix=='.pdf':assert p==P/'P16.5-paper.pdf'
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation137/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for name in ['P16.5-argument.md','P16.5-core.md','P16.5-paper.tex','P16.5-paper.pdf','status.json',
             'source-application-ledger.json','canonical-native-result.json','publication-preparation.json','README.md']:add(P/name)
for p in [own,B,previous,R/'record_verified136_20261006.py',R/'prepare_native126_main_public_reader_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation137.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':48,
    'commit_message':'Preserve original P16.5 partial point-blowup paper and full relative weighted candidate; record native125 and128 batch',
    'scope':binding['scope']+' Original126 remains PARTIAL. No new original or scoped mathematical acceptance.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'current_batch':[i['round'] for i in batch['active_items']],
                  'next_launch':129,'originals_solved':7,'originals_open':35,'reviewed_scoped_papers':48},indent=2))
