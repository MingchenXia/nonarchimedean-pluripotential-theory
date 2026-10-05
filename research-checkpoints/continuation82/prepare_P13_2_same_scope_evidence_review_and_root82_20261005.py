"""Preserve the inconclusive actual audit and prepare an unchanged-scope review."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
O = R/'campaigns/round-74/P13.2-public-source-fixed-ray-polynomial-and-uniform-target-mathematical-review'
Q = R/'campaigns/round-76/P13.2-public-source-same-partial-theorem-and-valid-evidence-mathematical-review'
N = R/'root-checks/P13.2-round74-actual-partial-mathematical-review-20261005.json'
D = R/'root-checks/public-P13.2-round-74-actual-partial-mathematical-review-reader'
P = R/'root-checks/P16.1-canonical-nonflat-norm-weights-and-direct-radial-trace-20261005-continuation82.md'
S = R/'root-checks/continuation82-canonical-norm-and-radial-trace-source-reads'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p,d: Path(p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not Q.exists() and not D.exists() and not S.exists()
assert sha(N) == 'bfa964b16717216c2fdcf9e877fdb27cab67d64787e26fbc95a3e2d438f317fc'
j = json.loads(N.read_text())
assert j == json.loads((O/'run.json').read_text())['campaign']['result']
assert j['verdict'] == 'INCONCLUSIVE' and len(j['premises']) == 200 and len(j['passages']) == 209
assert j['report'].startswith('Codex PASS lacked valid task or source evidence for every premise.')
assert j['operationId'] == 'cea089ba-4701-4b7b-b260-e4d72893db4a'
coverage = set()
for p in j['passages']:
    index = p['premise']
    assert isinstance(index,int) and 0 <= index < len(j['premises'])
    assert p['statement'] == j['premises'][index] and p['quote'].strip()
    assert p['id'].startswith(j['operationId']+'/')
    coverage.add(index)
assert coverage == set(range(200)) and len({p['id'] for p in j['passages']}) == 209
old = json.loads((O/'freeze.json').read_text())
for name,key in [('task.json','task_sha256'),('argument.md','argument_sha256'),('settings.json','settings_sha256')]:
    assert sha(O/name) == old[key]
now = datetime.now(timezone.utc).isoformat()
D.mkdir()
for name in ['task.json','argument.md','settings.json','freeze.json']: shutil.copyfile(O/name,D/name)
shutil.copyfile(N,D/'canonical-native-review.json')
write(D/'root-read-and-binding-observation-continuation82.json',{
    'recorded_utc':now,'actual_verdict':'INCONCLUSIVE','actual_result_sha256':sha(N),
    'operation_id':j['operationId'],'entire_actual_report_root_read':True,
    'all_200_actual_premises_root_read':True,'all_209_retained_passage_quotes_root_read':True,
    'all_passage_statements_match_indexed_premises':True,'all_retained_indices_valid':True,
    'all_200_premises_have_retained_passage':True,'passage_ids_unique_and_operation_bound':True,
    'whole_primary_bodies_root_read':False,'source_quote_authentication_or_sufficiency_certified':False,
    'native_validator_still_inconclusive':True,'new_partial_accepted':False,'original_closed':False,
    'reported_binding_issue':'The mathematical report describes a task-grant passage with premise index -1. Native binding rejects negative indices; all returned retained passages cover the200 external entries, but the native report remains INCONCLUSIVE.',
    'limits':'Root checked the complete actual public result, not private native records. Many retained quotations are too short to establish standalone hypotheses. No alteration of the result, task, original proof or frozen source revision is made.'})

task = json.loads((O/'task.json').read_text())
notice = '''Evidence-format clarification for an independent review of the EXACT SAME partial task and argument. No mathematical scope, hypothesis, conclusion, grant or proof is changed. The preserved round74 actual result is INCONCLUSIVE: its mathematical narrative reports PASS, while native evidence validation rejected the result. It is diagnostic data and is not a granted theorem or accepted review.

Follow the native evidence contract. Every returned passage must index an existing entry of premises by a nonnegative zero-based integer; do not return a task-grant passage with index -1. If a granted background statement is listed as a premise, return url="urn:xean:task" and an EXACT quote from the unchanged task.problem or task.completionCriteria, indexed to that premise. The accepted P13.1 full mathematical body and its granted scope are unchanged. A generated assertion or requested conclusion is not a grant. Do not use a passageId from prose as if it were evidence supplied in the native structured evidence field.

List the actual nonroutine external claims with their complete hypotheses. For fresh primary evidence use exact quotations from matching statements and pertinent proof bodies, sufficient to establish the standalone claim and application; a theorem title, bare symbol or short fragment alone does not establish its scope. Reconstruct the entire unchanged mathematical proof independently and retain every antecedent of its conditional auxiliary results. Do not inherit the former mathematical narrative, reduce the review to a formatting check, omit a substantive defect or narrow the claims to obtain PASS. If a mathematical premise or valid evidence remains unresolved, return the honest INCONCLUSIVE or FAIL as appropriate. No runtime, source revision, account, sandbox or external application is changed.

The unchanged original task, complete round73 mathematical argument, actual n1-n4 and exact source provenance follow verbatim. The previous actual review is appended only for diagnosis.
'''
Q.mkdir(parents=True)
shutil.copyfile(O/'task.json',Q/'task.json')
(Q/'argument.md').write_text(notice+'\n\n'+(O/'argument.md').read_text()+'\n\n# Previous actual INCONCLUSIVE result; diagnostic only\n\n'+N.read_text())
settings = json.loads((O/'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r76/P13.2-same-partial-theorem-valid-evidence-mathematical-review'
write(Q/'settings.json',settings)
write(Q/'freeze.json',{'prepared_utc':now,'task_sha256':sha(Q/'task.json'),
    'argument_sha256':sha(Q/'argument.md'),'argument_bytes':(Q/'argument.md').stat().st_size,
    'settings_sha256':sha(Q/'settings.json'),'previous_actual_result_sha256':sha(N),
    'previous_actual_verdict':'INCONCLUSIVE','original_task_bytes_unchanged_from_round74':True,
    'previous_complete_argument_embedded_verbatim':True,'mathematical_scope_unchanged':True,
    'new_granted_mathematics_added':False,'original_solved':False,'submission_attempted':False,
    'review_scope':'Independent full mathematical reconstruction of the exact original partial task; evidence indices and source scope must satisfy the existing native contract.'})
assert (Q/'task.json').read_bytes() == (O/'task.json').read_bytes()

assert sha(P) == '099e025e5d9f64a45083bd9c0857179fcc004b1b6646e0755bc3949e413eedf4'
W = R/'shared-sources/new-primary-2609.27610v1-20261004.txt'
assert sha(W) == 'c8ffe91a631da67f6d3872a1a06ab8d15755aed2f926cdf326725ca3662cef7d'
S.mkdir(); first,last = 2200,2372
literal = S/'Wu-LF2200-2372.txt'
literal.write_bytes('\n'.join(W.read_bytes().decode().split('\n')[first-1:last]).encode())
write(S/'source-read-record.json',{'recorded_utc':now,'proposal':str(P),'proposal_sha256':sha(P),
    'whole_saved_proposal_root_read':True,'proposal_LF_count':107,'read_ranges':[[1,74],[75,107]],
    'units':[{'source':str(W),'source_sha256':sha(W),'version':'2609.27610v1',
        'inclusive_one_based_LF':[first,last],'literal_file':str(literal),'literal_sha256':sha(literal),
        'whole_literal_body_root_read':True,
        'application_and_limit':'Printed nonflat transverse-curve trace is diagnostic. New algebra proves canonical weights and a Gauss formula; weak trace extension retains smooth membership/removal and local-expression compatibility.'}],
    'LF_convention':'UTF-8 bytes decode and split("\\n"), inclusive one-based ranges',
    'whole_primary_bodies_root_read':False,'accepted_dependency':False,'original_closed':False,
    'new_mathematics_independently_reviewed':False,'hot_feedback_to_active_author_sent':False,
    'unconditional_draft_scope':'Normal-target finite integral norm polynomial law, positive integer weights at all actual fibers, exact whole-base finite-max Gauss trace, flat-weight and slicing compatibility.',
    'conditional_antecedents':['Actual local logarithmic-expression field/curve compatibility','Smooth upper-growth membership and principal-open removal','Actual uniform/decreasing genuine target class closure'],
    'limits':'A new unreviewed mathematical proposal. It establishes no arbitrary weak-input approximation theorem, singular EP or original finite-energy equation.'})
print(json.dumps({'review':str(Q),'argument_sha256':sha(Q/'argument.md'),'argument_bytes':(Q/'argument.md').stat().st_size,
    'task_sha256':sha(Q/'task.json'),'settings_sha256':sha(Q/'settings.json'),
    'previous_verdict':'INCONCLUSIVE','old_mathematical_task_unchanged':True,
    'new_root_proposal_sha256':sha(P),'source_read_record_sha256':sha(S/'source-read-record.json')},indent=2))
