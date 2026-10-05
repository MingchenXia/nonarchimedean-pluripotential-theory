from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,shutil

R=Path('/workspace/research')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
review_campaign=R/'campaigns/round-108/P16.5-original-full-big-reference-independent-review'
author_campaign=R/'campaigns/round-109/P16.2-original-proper-nonprojective-input-repair-research'
rv=json.loads((review_campaign/'run.json').read_text())['campaign']
au=json.loads((author_campaign/'run.json').read_text())['campaign']
assert rv['status']=='completed' and au['status']=='completed'
review=rv['result']; result=au['result']
assert review['verdict']=='FAIL' and review['kind']=='codex-report'
assert len(review['premises'])==12 and len(review['passages'])==20
assert {p['premise'] for p in review['passages']}==set(range(12))
assert result['kind']=='notes' and not result['candidate'] and len(result['notes'])==4
W=Path(result['workspace'])
P=R/'root-checks/public-P16.2-round109-final-reader'
assert not P.exists() and W.is_dir()
for p in W.rglob('*'):
    assert not p.is_symlink(),str(p)
    assert not any(x in {'.codex','.aws','.git','auth.json','.env'} for x in p.relative_to(W).parts)
shutil.copytree(W,P)
for source,target in [(review,R/'root-checks/P16.5-round108-actual-full-original-fail-review-20261005.json'),
                      (result,P/'canonical-native-result.json')]:
    assert not target.exists()
    target.write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n')
files=[]
for p in sorted(P.rglob('*')):
    if p.is_file():
        files.append({'path':str(p.relative_to(P)),'bytes':p.stat().st_size,'sha256':sha(p)})
obs={'recorded_utc':datetime.now(timezone.utc).isoformat(),'author_campaign':str(author_campaign),
     'native_result_returned':True,'candidate':False,'canonical_notes_entire_root_read':True,
     'whole_paper_root_read':False,'all_premise_ledger_statements_root_read':False,
     'whole_primary_works_root_read':False,'original_closed':False,'artifacts':files}
(P/'root-terminal-reader-observation.json').write_text(json.dumps(obs,ensure_ascii=False,indent=2)+'\n')
binding=R/'root-checks/P16.5-round108-actual-fail-root-reading-binding-20261005.json'
assert not binding.exists()
binding.write_text(json.dumps({'recorded_utc':datetime.now(timezone.utc).isoformat(),
 'review':str(R/'root-checks/P16.5-round108-actual-full-original-fail-review-20261005.json'),
 'verdict':'FAIL','operation_id':review['operationId'],'reported_at':review['reportedAt'],
 'entire_report_root_read':True,'all12_exact_premises_root_read':True,
 'all20_actual_passage_records_root_read':True,'premise_indices_covered':list(range(12)),
 'all_passage_urls_are_HTTPS':all(p['url'].startswith('https://') for p in review['passages']),
 'whole_primary_works_root_read':False,'original_closed':False,
 'counterexample_is_to_general_flattening_not_to_equation_theorem':True},indent=2)+'\n')
print(json.dumps({'review_verdict':review['verdict'],'reader':str(P),'author_candidate':result['candidate'],
                  'artifacts':len(files),'paper_bytes':(P/'paper.md').stat().st_size},indent=2))
