from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation145.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='05ff411a8c6490c06671270bb93d5372b6b673d2'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation145.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
now=datetime.now(timezone.utc).isoformat()
readers=[]
for n,a,pages in [(131,'P19.1',[1,9,18]),(132,'P16.5',[1,6,11])]:
    D=K/f'public-{a}-round{n}-partial-research-reader';p=D/'publication-binding.json';b=json.loads(p.read_text())
    assert not b['candidate'] and b['status']['status']=='PARTIAL' and b['whole_mathematical_markdown_root_read']
    for f in b['files']:assert sha(D/f['name'])==f['sha256']
    b['actual_visual_pages']=pages;p.write_text(json.dumps(b,ensure_ascii=False,indent=2)+'\n');readers.append(D)
L=K/'public-P16.5-continuation183-entire-big-surface-reader';b=json.loads((L/'publication-binding.json').read_text())
assert b['whole_final_tex_root_read'] and b['actual_visual_pages']==[1,3,5]
assert sha(b['tex'])==b['tex_sha256'] and sha(b['pdf'])==b['pdf_sha256']
S=K/'current-small-batch134135-20261006-continuation146';S.mkdir(exist_ok=False)
labels={134:'P19.1-original-all-starting-points-calibrated-entropy-independent-review',
        135:'P16.5-original-entire-big-cone-surface-and-filtered-ideal-research'}
observed={};items=[]
for n,label in labels.items():
    C=R/f'campaigns/round-{n}'/label
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    d=json.loads(r.stdout);assert d['status'] in ['running','completed']
    dest=S/f'round{n}-public-native-status.json';save(dest,d)
    observed[n]={'observed_status':d['status'],'observed_utc':d['observedAt'],'public_status':str(dest),'public_status_sha256':sha(dest)}
    freeze=json.loads((C/'freeze.json').read_text())
    for f,key in [('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/f)==freeze[key]
    if n==135:assert sha(C/'input.json')==freeze['input_sha256']
    else:assert sha(C/'argument.md')==freeze['argument_sha256']
    items.append({'round':n,'atom':'P19.1' if n==134 else 'P16.5','directory':str(C),'database':'work.sqlite',
                  'tool_session_id':46101 if n==134 else 72521,'route':'Xean native Codex','model':'gpt-6.1-sol',
                  'reasoning':'xhigh','author_research_only':n==135,'whole_original_review':n==134,
                  'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,
                  'freeze':freeze,**observed[n]})
assert sum(x['observed_status']=='running' for x in items)<=2
C=R/'campaigns/round-135'/labels[135];freeze=json.loads((C/'freeze.json').read_text())
save(C/'launch-record.json',{'recorded_utc':now,'round':135,'role':'codex','tool_session_id':72521,
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','unchanged_original_task':True,
    'maximum_concurrent_campaigns':2,'frozen_input_sha256':freeze['input_sha256'],
    'frozen_task_sha256':freeze['task_sha256'],'frozen_settings_sha256':freeze['settings_sha256']})
shutil.copyfile(S/'round135-public-native-status.json',C/'launch-public-native-status.json')
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
       'maximum_concurrent_campaigns':2,'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
       'focus':'Whole original P19.1 entropy review134 and original P16.5 entire-cone closure research135; entire big-surface structural candidate183 and completed PARTIAL papers131/132.'}
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==7 and d['historical_reviewed_scoped_papers']==51
    d['current_small_batch']=batch;d['updated_utc']=now;d['github_pending_checkpoint']='continuation146 frozen'
    d['completed_partial_research_readers131132']=[{'directory':str(D),'publication_binding_sha256':sha(D/'publication-binding.json'),'original_closed':False} for D in readers]
    d['P16_5_entire_big_surface_candidate183']=b
    if name=='checklist-current.json':
        t=next(t for t in d['targets'] if t['id']=='P16.5');assert not t['fully_solved'] and t['closure']=='open'
        t['research_status']='entire_big_surface_candidate183_unreviewed_original_general_big_closure135_running'
        t['current_native_research']=next(i for i in items if i['round']==135)
        t['current_remaining_gaps']=['Reconstruct the whole surface Zariski division and genuine-cone candidate183 without a new nonample grant.',
          'Repair genuine all-point closure and normalized compactness for arbitrary-dimensional nonnef big rational classes.',
          'Reconstruct entire original-carrier finite-energy operator, intrinsic targets, derivatives, comparison, variational attainment and uniqueness on the full actual domain.']
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';rows=tsv.read_text().splitlines()
for j,line in enumerate(rows):
    f=line.split('\t')
    if f[0]=='P16.5':f[2]='Original remains open.132 PARTIAL entire nef closure and fixed-gauge subcone;183 unreviewed ENTIRE big-surface Zariski cone candidate,5 pages.135 reconstructs and researches higher-dimensional actual closure.129 failure preserved.'
    rows[j]='\t'.join(f)
tsv.write_text('\n'.join(rows)+'\n')
D=G/'continuation146-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,'historical_reviewed_scoped_papers':51,
    'research131_132':'PARTIAL full draft papers now published','surface183_independently_accepted':False,'active_batch':[i['round'] for i in items if i['observed_status']=='running']})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert 'LOCALONLY' not in p.name and p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.stdout','.stderr','.out'}
    if p.suffix=='.pdf':assert p.parent in {*readers,L}
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation146/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in sorted(S.iterdir()):add(p)
for reader in readers:
    for name in ['publication-binding.json','status.json','source-application-ledger.json']:
        add(reader/name)
    for p in sorted(reader.glob('*-argument.md')):add(p)
    for p in sorted(reader.glob('*-paper.tex')):add(p)
    for p in sorted(reader.glob('*-paper.pdf')):add(p)
for p in [Path(b['tex']),Path(b['pdf']),L/'publication-binding.json',previous,R/'record_verified145_20261006.py',
          R/'prepare_original_genuine_closure135_surface_and_filtered_ideals_20261006.py',
          R/'publish_completed_partial_research131132_readers_20261006.py',Path(__file__)]:add(p)
for name in ['freeze.json','mathematical-data-bindings.json','launch-record.json','launch-public-native-status.json']:add(C/name)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation146.json'
save(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],'expected_previous_checkpoint':receipt['commit_sha'],
    'files':files,'file_count':len(files),'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
    'historical_reviewed_scoped_papers':51,'commit_message':'Checkpoint entire big-surface cone candidate and completed partial entropy and genuine-closure papers',
    'scope':'Originals remain7/42 solved and51 scoped accepted papers.183 is an unreviewed5-page entire big-SURFACE structural candidate, not the full P16.5 theorem. Completed131/132 PARTIAL draft papers are published with exact scope and source ledgers. Original entropy review134 and general-big closure research135 keep immutable frozen inputs.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),'native_status':observed,'originals_solved':7,'accepted_scoped_papers':51},indent=2))
