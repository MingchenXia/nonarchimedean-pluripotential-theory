"""Freeze direct curve/Gauss trace identification with exact read scopes; no new acceptance."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import shutil
import subprocess

R=Path('/workspace/research');G=R/'github-checkpoint'
D=G/'continuation86-publication-records'
S=R/'root-checks/continuation86-direct-curve-trace-source-reads'
F=R/'root-checks/P16.1-direct-curve-Gauss-whole-base-trace-20261005-continuation86.md'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
write=lambda p,d:Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not D.exists() and not S.exists()
assert sha(F)=='36c388547d6da9187f5d15dc8257909cf0139ef14443c1c9434176c888c43626'
assert len(F.read_bytes().decode().split('\n'))==102 and b'\r' not in F.read_bytes()
receipt=json.loads((G/'push-receipt-continuation85.json').read_text())
assert receipt['commit_sha']=='132d3db477c1d335e43d238f9e78e5230714a301'
assert receipt['remote_ref_verified'] and receipt['all_file_blob_bindings_verified_remote']
assert sha(G/'upload-manifest-continuation85.json')==receipt['manifest_sha256']
now=datetime.now(timezone.utc).isoformat()
S.mkdir();units=[]
for name,version,digest,ranges in [
    ('Thuillier-tel-00010990v1.txt','tel-00010990v1','e82226b3dde6a8088c35e1481bfd43f64bb69ee309b5cfda92c8c927a7885570',
        [(3730,3741,'Harmonic maximum principle and local strict domains.'),
         (3783,3945,'Direct strict-disc comparison definition, decreasing closure, finite boundary values and harmonic-test characterization, with their pertinent proofs.')]),
    ('new-primary-2609.27610v1-20261004.txt','2609.27610v1','c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d',
        [(2200,2372,'Whole printed trace chain audited, not accepted support; its general completed-residue-field affine regularization application is replaced conditionally by direct contact curve restriction.')])]:
    source=R/'shared-sources'/name;assert sha(source)==digest
    lines=source.read_bytes().decode().split('\n')
    for first,last,limit in ranges:
        p=S/f'{source.stem}-LF{first}-{last}.txt'
        p.write_text('\n'.join(lines[first-1:last]))
        units.append({'source':str(source),'source_sha256':digest,'version':version,
            'inclusive_one_based_LF':[first,last],'literal_file':str(p),'literal_sha256':sha(p),
            'whole_literal_body_root_read':True,'application_and_limit':limit})
web=[
    {'tag':'0BXQ','url':'https://stacks.math.columbia.edu/tag/0BXQ',
     'pertinent_read':'Lemma33.27.1 full statement/proof, live rendered lines20-34; normalization finite for locally algebraic schemes.'},
    {'tag':'0BXX','url':'https://stacks.math.columbia.edu/tag/0BXX',
     'pertinent_read':'Lemma53.2.3 full statement/proof, live rendered lines26-28; finite nonconstant normalized curve maps are flat by torsion-free DVR modules.'},
    {'tag':'0B8Y','url':'https://stacks.math.columbia.edu/tag/0B8Y',
     'pertinent_read':'Full statement/proof, live rendered lines23-38; normal curve closed local rings are DVRs and smooth over a perfect field.'},
    {'tag':'0BX4','url':'https://stacks.math.columbia.edu/tag/0BX4',
     'pertinent_read':'Proper valuative criterion29.43.1 and relative rational-map extension29.43.5 full pertinent statement/proof, live rendered lines21-32 and92-107. Properness is relative, not absolute.'},
    {'tag':'0BBZ','url':'https://stacks.math.columbia.edu/tag/0BBZ',
     'pertinent_read':'Full statement/proof, live rendered lines23-28; minimal components of n-1 equations have height at most n-1.'},
    {'tag':'00KQ','url':'https://stacks.math.columbia.edu/tag/00KQ',
     'pertinent_read':'Height-bound cited dimension-parameter proof full pertinent body, live rendered lines23-39.'},
    {'tag':'02JT','url':'https://stacks.math.columbia.edu/tag/02JT',
     'pertinent_read':'Dimension formula29.53.1 and pertinent proof-reference, live rendered lines20-37. Recursively cited algebra10.113.1 full proof was not newly read.'}
]
write(S/'source-read-record.json',{'recorded_utc':now,'proposal':str(F),'proposal_sha256':sha(F),
    'whole_saved_proposal_root_read':True,'proposal_read_ranges':[[1,51],[52,102]],'units':units,
    'live_primary_web_application_reads':web,'live_web_rendered_line_numbers_are_not_cached_source_LF':True,
    'whole_web_pages_pinned_or_hashed':False,'whole_primary_files_root_read':False,
    'all_recursive_primary_dependencies_read':False,'accepted_dependency':False,'original_closed':False,
    'unreviewed_antecedents':'Round77 actual smooth upper-growth/removal with its geometric witness premises; canonical norm polynomial law and complete-field weights; exact contact-curve class.',
    'new_argument':'Original witness lifts over each normalized line; direct harmonic supports/decreasing closure; strict-disc radial limit; exact unit-root Gauss fibers; every positive weight and finite or minus-infinity value.',
    'remaining':'Independent review, controlled split-piece/Runge/Hartogs/singular induction, fiber descent, arbitrary-field EP, normalization and actual singular equation.'})
D.mkdir();items=[]
prep=json.loads((R/'partial-mathematical-review80-81-preparation-20261005.json').read_text())
for it,session in zip(prep['items'],[82517,75571]):
    C=Path(it['directory'])
    for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]: assert sha(C/name)==it[key]
    proc=subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(C/'review.sqlite')],
        cwd='/workspace/xean',capture_output=True,text=True,check=True)
    path=D/f"{it['atom']}-round{it['round']}-native-status.json";path.write_text(proc.stdout);state=json.loads(proc.stdout)
    items.append({**it,'role':'review','tool_session_id':session,'observed_status':state['status'],
        'status':str(path),'status_sha256':sha(path),'hot_feedback_sent':False,'original_closed':False})
batch={'recorded_utc':now,'items':items,'active_items':[i for i in items if i['observed_status']=='running'],
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh','hot_feedback_sent':False,
    'new_draft_supplied_to_active_reviews':False,'original_closed':False}
write(D/'current-small-batch-observation.json',batch)
a=json.loads((R/'active-work.json').read_text());c=json.loads((R/'checklist-current.json').read_text())
solved=['P13.1','P15.1','P15.2','P16.6']
assert sorted(t['id'] for t in c['targets'] if t['fully_solved'])==solved
assert sum(len(t['reviewed_papers']) for t in c['targets'])==41
a['updated_utc']=c['updated_utc']=now;a['current_small_batch']=c['current_small_batch']=batch
c['active_atoms']=[i['atom'] for i in batch['active_items']]
a['continuation86_unreviewed_root_proposal']={'path':str(F),'sha256':sha(F),
    'source_read_record':str(S/'source-read-record.json'),'accepted_dependency':False,'original_closed':False}
a['github_checkpoint']=c['latest_verified_github_checkpoint']=receipt
a['github_pending_checkpoint']=c['github_pending_checkpoint']='Checkpoint86: unreviewed original-witness direct curve/Gauss whole-base trace implication; independent partial reviews80/81 remain frozen.'
write(R/'active-work.json',a);write(R/'checklist-current.json',c)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']: shutil.copyfile(R/name,D/name)
files=[]
def add(path,remote=None):
    p=Path(path);assert p.is_file() and not p.is_symlink()
    assert p.suffix not in {'.sqlite','.jsonl'}
    assert not any(x in {'.git','.codex','.aws','.env','auth.json','run.json'} for x in p.relative_to(R).parts)
    files.append({'local':str(p),'path':remote or 'research-checkpoints/continuation86/'+str(p.relative_to(R)),
        'bytes':p.stat().st_size,'sha256':sha(p)})
for folder in [S,D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file(): add(p)
for p in [F,G/'prepare_checkpoint_continuation86.py',G/'push-receipt-continuation85.json']: add(p)
for name in ['active-work.json','checklist-current.json','checklist-current.tsv']:
    add(D/name,'manuscript/editorial/xean_research_20261003/'+name)
manifest=G/'upload-manifest-continuation86.json';assert not manifest.exists()
write(manifest,{'generated_utc':now,'repository':receipt['repository'],'branch':receipt['branch'],
    'expected_previous_checkpoint':receipt['commit_sha'],'files':files,'file_count':len(files),
    'fully_solved_original_atoms':solved,'remaining_open_atoms':38,'historical_reviewed_scoped_papers':41,
    'commit_message':'Retain original-witness curve and Gauss trace-value reconstruction',
    'scope':'Unreviewed conditional whole-base trace identification from actual round77 smooth upper-growth/removal and positive norm-law antecedents; direct restriction on the same witness avoids an arbitrary completed-residue-field affine regularization assumption. Three actual-read literal units and seven live primary applications with honest recursive-read limits. Two frozen independent reviews80/81 observed; no hot feedback, new acceptance, original closure, private SQL/transcripts/auth or book edits.'})
print(json.dumps({'manifest':str(manifest),'sha256':sha(manifest),'files':len(files),
    'statuses':[(i['atom'],i['observed_status']) for i in items]},indent=2))
