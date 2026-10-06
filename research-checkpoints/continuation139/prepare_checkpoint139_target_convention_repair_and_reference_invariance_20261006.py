from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R=Path('/workspace/research');K=R/'root-checks';G=R/'github-checkpoint'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
previous=G/'push-receipt-continuation138.json';receipt=json.loads(previous.read_text())
assert receipt['commit_sha']=='05ac40aebb18f23d7aa135bb1efcab0a8926dd8d'
assert receipt['manifest_sha256']==sha(G/'upload-manifest-continuation138.json')
assert all(receipt[k] for k in ['remote_ref_verified','all_file_blob_bindings_verified_remote','independent_native_git_tree_verified'])
repair=K/'P16.5-general-big-intrinsic-target-metric-and-solution-stability-candidate-20261006-continuation174-repair1.md'
old=K/'P16.5-general-big-intrinsic-target-metric-and-solution-stability-candidate-20261006-continuation174.md'
new=K/'P16.5-general-big-bounded-reference-invariance-and-explicit-target-pole-convention-candidate-20261006-continuation175.md'
assert sha(old)=='03c335072a5f0e1a31603fe79449b1f50e5aac2c8af087eace4c487bc8516a01'
assert 'nu(Z)=0 and finite D' in repair.read_text()
C=R/'campaigns/round-129/P16.5-original-entire-general-big-equation-independent-review'
freeze=json.loads((C/'freeze.json').read_text())
for n,key in [('argument.md','argument_sha256'),('task.json','task_sha256'),('settings.json','settings_sha256')]:assert sha(C/n)==freeze[key]
assert 'nu({V_theta=-infinity})=0' in (C/'argument.md').read_text()
S=K/'current-small-batch125-129-20261006-continuation139';S.mkdir(exist_ok=False)
observed={}
for n,label in [(125,'P16.5-entire-nef-big-variational-equation-independent-review'),
                 (129,'P16.5-original-entire-general-big-equation-independent-review')]:
    c=R/f'campaigns/round-{n}'/label
    r=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'review.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True)
    status=json.loads(r.stdout);assert status['status'] in ['running','completed']
    p=S/f'P16.5-round{n}-public-native-status.json';save(p,status)
    observed[n]={'observed_status':status['status'],'observed_utc':status['observedAt'],'public_status':str(p),'public_status_sha256':sha(p)}
now=datetime.now(timezone.utc).isoformat()
binding={'recorded_utc':now,'corrected_proof':str(repair),'corrected_proof_sha256':sha(repair),
         'old_proof_preserved':str(old),'old_proof_sha256':sha(old),'old_version_requires_correction':True,
         'new_reference_proof':str(new),'new_reference_proof_sha256':sha(new),
         'whole_saved_final_repaired_and_new_math_root_read':True,
         'correction':'The target space explicitly requires zero mass on the minimal-reference pole set before its relative differences are integrated. Own158 assumes this convention and only then derives other polar nullness. The initial174 wording omitted it;174-repair1 restores the exact target space.',
         'new_scope':'Own175 proves bounded-relative reference changes preserve the entire genuine energy space, floor operator limits and derivatives; gives the exact finite shift of relative dual energy and preserves target maximizers, conditional on the full equation chain for inverse claims.',
         'new_mathematics_independently_accepted':False,'original_closed':False,
         'frozen129_already_retains_necessary_pole_convention':True,'frozen129_input_modified':False,
         'hot_feedback_sent':False,'existing_editor_unchanged':True}
B=K/'P16.5-root-continuation174-repair1-175-target-convention-and-reference-binding-20261006.json';save(B,binding)
for n in ['active-work.json','checklist-current.json']:
    p=R/n;data=json.loads(p.read_text())
    assert len(data['fully_solved_original_atoms'])==7 and data['historical_reviewed_scoped_papers']==49
    data.update({'updated_utc':now,'continuation174_corrected_target_convention_and175_reference_candidate':binding,
                 'github_pending_checkpoint':'continuation139 frozen'})
    for item in data['current_small_batch']['items']:item.update(observed[item['round']])
    data['current_small_batch']['active_items']=[i for i in data['current_small_batch']['items'] if i['observed_status']=='running']
    data['current_small_batch']['recorded_utc']=now
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
D=G/'continuation139-publication-records';D.mkdir(exist_ok=False)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:shutil.copyfile(R/n,D/n)
save(D/'scope-observation.json',{'recorded_utc':now,'originals_solved':7,'originals_open':35,'historical_reviewed_scoped_papers':49,
    'target_definition_correction_published':True,'new_reference_deduction_reviewed':False,'original_closed':False})
files=[]
def add(p,remote=None):
    p=Path(p);assert p.is_file() and not p.is_symlink();rel=p.relative_to(R)
    assert p.suffix not in {'.sqlite','.jsonl','.png','.aux','.log','.pdf'} and 'LOCALONLY' not in p.name
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation139/'+str(rel),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in sorted(D.iterdir()):add(p)
for p in [repair,new,B,previous,R/'record_verified138_20261006.py',Path(__file__)]:add(p)
for p in sorted(S.iterdir()):add(p)
for n in ['active-work.json','checklist-current.json','checklist-current.tsv']:add(D/n,'manuscript/editorial/xean_research_20261003/'+n)
M=G/'upload-manifest-continuation139.json'
save(M,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':receipt['fully_solved_original_atoms'],'remaining_open_atoms':35,'historical_reviewed_scoped_papers':49,
    'commit_message':'Correct candidate target-pole convention and prove bounded-reference invariance',
    'scope':binding['correction']+' '+binding['new_scope']+' Both new proofs unreviewed;originals7solved35open.'})
print(json.dumps({'manifest':str(M),'sha256':sha(M),'files':len(files),'native_status':observed,'originals_solved':7,'reviewed_scoped_papers':49},indent=2))
