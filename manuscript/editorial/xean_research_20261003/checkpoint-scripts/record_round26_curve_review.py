"""Bind the fully read all-K curve review to the unchanged proof and supports."""
from pathlib import Path
import datetime, hashlib, json
r=Path('/workspace/research');d=r/'campaigns/round-26/P06.2-arbitrary-field-curve-recognition-integration-v2-review'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
prior=r/'root-checks/arbitrary-field-curve-integration-phase1/root-complete-read-before-review.json'
record=json.loads(prior.read_text());j=json.loads((d/'run.json').read_text());review=j['campaign']['result']
f=json.loads((d/'freeze.json').read_text());b=json.loads((d/'source-artifact-binding.json').read_text())
assert j['campaign']['status']=='completed' and review['verdict']=='PASS'
assert len(review['premises'])==43 and len(review['passages'])==75
for p in review['passages']:
    assert isinstance(p['premise'],int) and 0<=p['premise']<43
    assert p['statement']==review['premises'][p['premise']]
assert sha(d/'argument.md')==f['argument_sha256']==b['review_argument_sha256']
assert sha(d/'freeze.json')==b['original_freeze_sha256']
for k,h in [('main_argument','main_argument_sha256'),('source_tex','source_tex_sha256'),('declared_proof_file','declared_proof_sha256')]:assert sha(Path(b[k]))==b[h]==f[h]
w=Path(f['source_workspace']);assert sha(w/'status.json')==f['source_status_sha256']==b['source_status_sha256']
assert record['main_argument_sha256']==sha(w/'P06.2-argument.md')
assert record['all_three_actual_canonical_native_notes_fully_read'] and record['all_16_raw_LF_bodies_and_main_embeddings_exact']
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={**record,'checked_utc':now,'previous_complete_read_record':str(prior),
 'previous_complete_read_record_sha256':sha(prior),'independent_review_verdict_read':True,
 'publication_allowed':True,'review_verdict':'PASS','review_premises':43,'review_passages':75,
 'all_review_report_premises_passages_fully_read':True,
 'truncated_passages_36_37_38_reread_in_full':True,'full_original_atom_solved':False}
assert not (d/'root-draft-read-record.json').exists()
(d/'root-draft-read-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
att={'read_utc':now,'verdict':'PASS','premise_count':43,'passage_count':75,
 'full_report_read':True,'all_premises_read':True,'all_passages_read':True,
 'passage_premise_zero_based_exact_statement_checks':True,
 'root_full_main_and_all_canonical_notes_read':True,'publish_exact_scope':True,
 'run_sha256':sha(d/'run.json'),'argument_sha256':sha(d/'argument.md'),'freeze_sha256':sha(d/'freeze.json'),
 'source_artifact_binding_sha256':sha(d/'source-artifact-binding.json'),
 'root_read_record_sha256':sha(d/'root-draft-read-record.json'),'full_original_atom_solved':False,
 'governing_report':review['report'],
 'editorial_corrections_only':'Cross-reference GR older GJR labels5.3(3)/5.11 to v3 Lemma5.4(3)/Corollary5.12; imported n700 A/I is a strict affinoid integral algebra, not an analytic domain; raw transcription defects preserved and precise theorem statements used.',
 'limit':'Same-model independent review is not formal verification or priority certification.'}
assert not (d/'review-read-attestation.json').exists()
(d/'review-read-attestation.json').write_text(json.dumps(att,ensure_ascii=False,indent=2)+'\n')
root=r/'root-checks/arbitrary-field-curve-integration-phase2';root.mkdir(exist_ok=False)
(root/'root-complete-read-record.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
(root/'canonical-review-result.json').write_text(json.dumps({'source_run_sha256':sha(d/'run.json'),'result':review},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'verdict':'PASS','premises':43,'passages':75,'review_read_attestation_sha256':sha(d/'review-read-attestation.json')},indent=2))
