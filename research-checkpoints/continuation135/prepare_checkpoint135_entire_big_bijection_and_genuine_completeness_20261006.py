from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research'); K=R/'root-checks'; G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation134.json'
receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='73b2ce3b5a0181daa47e60c92278c20ac0f87fd8'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation134.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
notes=[K/'P16.5-general-big-model-weighted-limits-and-maximizer-I-Cauchy-draft-20261006-continuation164.md',
       K/'P16.5-general-big-all-target-variational-attainment-candidate-20261006-continuation165.md',
       K/'P16.5-general-big-weak-output-weighted-continuity-draft-20261006-continuation166.md',
       K/'P16.5-general-big-entire-supporting-planes-bijection-and-domination-candidate-20261006-continuation167.md',
       K/'P16.5-general-big-entire-I-weighted-continuity-and-genuine-completeness-candidate-20261006-continuation168.md']
for round,label,db in [(126,'P16.5-original-general-big-relative-operator-and-equation-research','work.sqlite'),
                      (128,'P16.5-general-big-entire-genuine-E1-operator-independent-review','review.sqlite')]:
    c=R/f'campaigns/round-{round}'/label
    freeze=json.loads((c/'freeze.json').read_text())
    for name in ['settings.json','input.json' if round==126 else 'argument.md']:
        key='settings_sha256' if name=='settings.json' else 'input_sha256' if round==126 else 'argument_sha256'
        assert sha(c/name)==freeze[key]
    if round==128:assert not (c/db).exists()
    else:assert (c/db).exists()
S=K/'current-small-batch124-125-20261006-continuation135'
if S.exists():assert not list(S.iterdir())
else:S.mkdir()
public={}
for round,label in [(124,'P16.5-entire-intrinsic-nef-weighted-outer-and-dual-independent-review'),
                    (125,'P16.5-entire-nef-big-variational-equation-independent-review'),
                    (126,'P16.5-original-general-big-relative-operator-and-equation-research')]:
    db=R/f'campaigns/round-{round}'/label/('work.sqlite' if round==126 else 'review.sqlite')
    result=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(db)],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(result.stdout)
    expected='completed' if round==124 else 'running'
    assert status['status']==expected and status['work']['active']==(0 if round==124 else 1)
    assert status['work']['completed']==(1 if round==124 else 0)
    assert status['calls']['byModel'][0]['model']=='gpt-6.1-sol'
    p=S/f'P16.5-round{round}-public-native-status.json';save(p,status)
    public[round]={'path':str(p),'sha256':sha(p),'observed_utc':status['observedAt'],'status':expected,
                   'whole_public_compact_status_root_read_at_freeze':False}
now=datetime.now(timezone.utc).isoformat()
review_path=K/'P16.5-round124-actual-scoped-independent-review-20261006.json'
review=json.loads(review_path.read_text())
assert review['verdict']=='PASS' and review['operationId']=='17bacb62-99e4-4d2d-ae29-f4aaec3874d7'
assert len(review['premises'])==7 and len(review['passages'])==12
review_binding={'canonical_result':str(review_path),'sha256':sha(review_path),'whole_canonical_report_premises_and_passages_root_read':True,
    'verdict':'PASS','scope':'Exact own132--135 entire intrinsic nef operator, mixed weighted nets, outer variation and dual support; no inverse or original closure.',
    'original_closed':False,'public_scoped_reader_still_to_prepare':True,'count_promotion_pending_reader':True}
binding={'recorded_utc':now,
    'own_notes':[{'path':str(p),'sha256':sha(p),'whole_saved_final_own_proof_root_read':True} for p in notes],
    'scope':'Own164 exact finite model weighted limits and numerical estimates yield model I-Cauchy maximizers. Own165 fixed atomic support planes close the energy jump and give actual all-target variational attainment and a unique normalized maximizer. Own166 capped original section tests and closed polar collars identify all full E1 relative integrals at bounded-cost model-output weak limits. Own167 passes global planes to arbitrary genuine bases, makes every actual operator solution a maximizer, proposes the entire big raw-volume equation bijection and domination. Own168 passes entire I/J and four-point estimates, joint relative weighted continuity, weak target integration on cost sublevels and actual rooftop metric completeness. All new mathematics is unreviewed. Full mixed nonnef products and full strict-set mass comparison are not established here; the additional nonbig zero-volume domain and final exact original review remain separate.',
    'independently_accepted':False,'original_closed':False,
    'all_recursive_background_foundations_reproved':False,
    'current_native_observations':public,'current_native_small_batch':[125,126],'prepared_native_launch_order':[128],
    'completed_native124_scoped_pass':review_binding,
    'active_or_prepared_native_inputs_modified':False,'hot_feedback_sent':False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened':False}
B=K/'P16.5-root-continuation164-168-whole-proofs-and-exact-scope-binding-20261006.json';save(B,binding)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==47
    assert [item['round'] for item in data['current_small_batch']['items']]==[124,125]
    data.update({'updated_utc':now,'continuation164_168_entire_big_bijection_and_completeness_candidate':binding,
                 'round124_scoped_pass_pending_public_reader':review_binding,
                 'github_pending_checkpoint':'continuation135 frozen'})
    batch=data['current_small_batch'];batch['recorded_utc']=now
    old124=next(item for item in batch['items'] if item['round']==124)
    old124.update({'observed_status':'completed','public_status':public[124]['path'],'public_status_sha256':public[124]['sha256'],
                   'observed_utc':public[124]['observed_utc'],'scoped_review_verdict':'PASS','canonical_result':str(review_path)})
    data['latest_completed_native124']=old124
    old125=next(item for item in batch['items'] if item['round']==125)
    new126={'round':126,'atom':'P16.5','directory':str(R/'campaigns/round-126/P16.5-original-general-big-relative-operator-and-equation-research'),
            'database':'work.sqlite','tool_session_id':13496,'original_closed':False,'private_active_output_read':False,'hot_feedback_sent':False,
            'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
    batch['items']=[old125,new126]
    for item in batch['items']:
        s=public[item['round']]
        item.update({'public_status':s['path'],'public_status_sha256':s['sha256'],'observed_status':'running','observed_utc':s['observed_utc']})
    batch['active_items']=list(batch['items'])
    batch['focus']='Independent125 full intrinsic nef-big equation; original126 general-big research. Independent124 scoped PASS read in full; public reader pending. Frozen128 remains next.'
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
p=R/'checklist-current.tsv';lines=p.read_text().splitlines()
for i,line in enumerate(lines):
    if line.startswith('P16.5\t'):
        cols=line.split('\t')
        cols[2]='Original123 PARTIAL; independent124 scoped PASS read, public reader pending; independent125 and original126 active. General-big143--168 unreviewed: entire genuine relative energy/operator, intrinsic output and target conditions, actual all-target attainment, all-solution uniqueness, domination, joint relative weighted continuity, weak target integration on cost sublevels and genuine rooftop completeness. Complete operator128 prepared. Full mixed nonnef products, full strict-set mass comparison, additional zero-volume scope and final original review remain open.'
        lines[i]='\t'.join(cols)
p.write_text('\n'.join(lines)+'\n')
D=G/'continuation135-publication-records';D.mkdir(exist_ok=False)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/name,D/name)
save(D/'scope-observation.json',{'recorded_utc':now,'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],
    'remaining_open_originals':35,'historical_reviewed_scoped_papers':47,'new_unreviewed_support':[164,165,166,167,168],
    'current_native_small_batch':[125,126],'prepared_next_native_launch_order':[128],'original_closed':False,
    'completed_native124_scoped_pass':review_binding,
    'extended_primary_transcripts_or_private_native_state_uploaded':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json','artifacts','shared-sources','evidence'} for x in rel.parts)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.pdf','.aux','.log'} and 'LOCALONLY' not in p.name
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation135/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in notes+[B,review_path,previous,R/'record_verified134_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
assert len({f['path'] for f in files})==len(files)
M=G/'upload-manifest-continuation135.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,
    'historical_reviewed_scoped_papers':47,
    'commit_message':'Record candidate entire big equation bijection, weighted continuity and genuine completeness',
    'scope':binding['scope']+' Seven originals solved,35open,47 independently accepted scoped papers.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'current_batch':[125,126],
    'next_launches':[128],'originals_solved':7,'originals_open':35},indent=2))
