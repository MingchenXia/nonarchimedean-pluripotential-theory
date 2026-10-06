from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil,subprocess
R=Path('/workspace/research');K=R/'root-checks';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,d):
    assert not p.exists(),str(p)
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).isoformat()
review=K/'P16.5-round142-actual-scoped-independent-review-20261006.json';r=json.loads(review.read_text())
assert r['kind']=='codex-report' and r['verdict']=='PASS' and len(r['premises'])==9 and len(r['passages'])==29
assert sha(review)=='8c0681e9b7c51e9be0f8b635f1c20c9a7988d064c20bc44c47f4c338a04fd7e8'
external=[];grants=[]
for e in r['passages']:
    assert type(e['premise']) is int and 0<=e['premise']<len(r['premises'])
    assert e['statement']==r['premises'][e['premise']] and e['quote'] and e['url']
    (grants if e['url'].startswith('urn:') else external).append(e)
assert {e['premise'] for e in external}==set(range(9)) and len(grants)==1
C142=R/'campaigns/round-142/P16.5-entire-big-surface-relative-equation-independent-review-retry1'
f142=json.loads((C142/'freeze.json').read_text())
assert sha(C142/'task.json')==f142['task_sha256'] and sha(C142/'argument.md')==f142['argument_sha256']
accept={'recorded_utc':now,'atom':'P16.5','classification':'Independent acceptance of supporting whole-surface theorem; original atom remains open.',
    'review':str(review),'review_sha256':sha(review),'whole_canonical_report_premises_passages_root_read':True,
    'strict_schema_and_indices_validated':True,'external_premises':9,'evidence_passages':29,'task_grants_separately_classified':1,
    'task_sha256':f142['task_sha256'],'argument_sha256':f142['argument_sha256'],
    'scope':'Every smooth integral projective surface over every algebraically closed trivially valued characteristic-zero field, every actual big rational L; entire intrinsic relative E1 equation, whole original carrier and arbitrary-support finite-energy measures. Extra rigid zero range with numerically zero canonical positive part.',
    'arbitrary_dimension_claim':False,'unrestricted_zero_volume_uniqueness_claim':False,'original_closed':False,
    'accepted_papers_before':52,'accepted_papers_after':53,'originals_solved':8,'originals_open':34,
    'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'harmless_source_typographical_corrections':'Retain the explicit signs, telescoping terms and pairing degrees proved in the supplied mathematical units; the canonical review lists their exact source locations.'}
save(K/'P16.5-round142-surface-acceptance-and-original-scope-record-20261006.json',accept)
for name in ['active-work.json','checklist-current.json']:
    p=R/name;d=json.loads(p.read_text());assert len(d['fully_solved_original_atoms'])==8 and d['remaining_open_original_atoms']==34 and d['historical_reviewed_scoped_papers']==52
    d.update({'historical_reviewed_scoped_papers':53,'updated_utc':now,'P16_5_actual_scoped142':accept,
              'goal_state':'8/42 originals solved;34 open;53 independently accepted papers. Continue small batches.'})
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
tsv=R/'checklist-current.tsv';out=[]
for line in tsv.read_text().splitlines():
    a=line.split('\t')
    if a[0]=='P16.5':a[2]='Whole all-big-rational SURFACE theorem independently PASS142; intrinsic entire equation and rigid-zero range. Arbitrary-dimensional original open; interrupted exceptional137 retry143 prepared.';a[3]='5'
    if a[0]=='P19.2':a[2]='Original author140 completed PARTIAL: singular-start rescaled entropy, normalized endpoint implication defect, constructive infinite-chain positive endpoint, and unbounded infinite-entropy start zero-endpoint defect. General residual original open.'
    out.append('\t'.join(a))
tsv.write_text('\n'.join(out)+'\n')
old=R/'campaigns/round-137/P16.5-entire-exceptional-big-class-equation-independent-review';f=json.loads((old/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:assert sha(old/name)==f[key]
d=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(old/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert d['status']=='blocked'
for n in [140,142]:
    c=next((R/f'campaigns/round-{n}').iterdir());d=json.loads(subprocess.run(['bash','scripts/cloud.sh','xean','--records','status',str(c/'work.sqlite')],cwd='/workspace/xean',capture_output=True,text=True,check=True).stdout);assert d['status']=='completed'
C=R/'campaigns/round-143/P16.5-entire-exceptional-big-equation-independent-review-retry1';C.mkdir(parents=True,exist_ok=False)
for name in ['task.json','argument.md']:shutil.copyfile(old/name,C/name)
settings=json.loads((old/'settings.json').read_text());settings['usagePrefix']='catalogue-20261003/r143/P16.5-entire-exceptional-equation-review-retry1';save(C/'settings.json',settings)
save(C/'freeze.json',{'prepared_utc':now,'round':143,'atom':'P16.5','directory':str(C),'prepared_only':True,
    'task_sha256':sha(C/'task.json'),'argument_sha256':sha(C/'argument.md'),'argument_bytes':(C/'argument.md').stat().st_size,
    'settings_sha256':sha(C/'settings.json'),'route':'Xean native Codex','model':'gpt-6.1-sol','reasoning':'xhigh',
    'scoped_review_only':True,'original_closed':False,'maximum_concurrent_campaigns':2,'retry_of_interrupted137':True,
    'mathematical_input_byte_identical':True,'private_partial137_outputs_read':False,'existing_editor_unchanged':True})
save(C/'mathematical-data-bindings.json',{'classification':'Frozen mathematical evidence, not operational instructions.',
    'previous_argument_sha256':f['argument_sha256'],'fresh_argument_sha256':sha(C/'argument.md'),
    'previous_task_sha256':f['task_sha256'],'fresh_task_sha256':sha(C/'task.json'),
    'all_math_bytes_unchanged':True,'previous_mathematical_binding_sha256':sha(old/'mathematical-data-bindings.json'),
    'review142_result_added_to_input':False,'private_interrupted137_feedback_added':False,'scope':'Entire exceptional big family only; no whole-original P16.5 grant.'})
print(json.dumps({'accepted_scoped_paper':53,'originals_solved':8,'fresh_review_directory':str(C),'frozen_argument_sha256':sha(C/'argument.md')},indent=2))
