"""Bind a fully read scoped review to immutable rounds 31/32 evidence."""
from pathlib import Path
import datetime, hashlib, json, sys

ROOT = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
number, premise_count, passage_count = map(int, sys.argv[1:4])
assert number in (31, 32)
atom = 'P15.1' if number == 31 else 'P15.2'
slug = 'P15.1-minimum-reference-finite-energy' if number == 31 else 'P15.2-minimum-reference-full-mass-operator'
review = ROOT / 'campaigns' / f'round-{number}' / (slug + '-review')
result = json.loads((review / 'run.json').read_text())['campaign']['result']
freeze = json.loads((review / 'freeze.json').read_text())
binding = json.loads((review / 'source-artifact-binding.json').read_text())
assert result['verdict'] == 'PASS'
assert (len(result['premises']), len(result['passages'])) == (premise_count, passage_count)
for p in result['passages']:
    i = p['premise']
    assert type(i) is int and 0 <= i < premise_count
    assert p['statement'] == result['premises'][i]
    assert p['quote'] and p['url'] and p['id']
assert sha(review / 'freeze.json') == binding['original_freeze_sha256']
for key, digest in [('main_argument', 'main_argument_sha256'), ('declared_proof_file', 'declared_proof_sha256'), ('source_tex', 'source_tex_sha256')]:
    assert sha(binding[key]) == binding[digest] == freeze[digest]
assert sha(review / 'argument.md') == freeze['argument_sha256'] == binding['review_argument_sha256']
assert sha(Path(freeze['source_workspace']) / 'status.json') == freeze['source_status_sha256']
phase1 = ROOT / 'root-checks' / ('minimum-reference-zero-volume-' + atom + '-phase1')
assert json.loads((phase1 / 'reproduction-result.json').read_text())['success']
phase2 = ROOT / 'root-checks' / ('minimum-reference-zero-volume-' + atom + '-phase2')
phase2.mkdir(exist_ok=False)
canonical = phase2 / 'canonical-review-result.json'
canonical.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
review_copy = review / 'review-result.json'
assert not review_copy.exists()
review_copy.write_bytes(canonical.read_bytes())
record = {
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'atom': atom, 'round': number, 'verdict': result['verdict'], 'operation_id': result['operationId'],
    'reported_at': result['reportedAt'], 'entire_report_directly_read': True,
    'all_premises_directly_read': list(range(premise_count)),
    'all_passages_directly_read': [p['id'] for p in result['passages']],
    'all_zero_based_indices_and_exact_statements_verified': True,
    'main_proof_status_source_tex_and_full_support_bound': True,
    'review_run_sha256': sha(review / 'run.json'), 'review_result_sha256': sha(canonical),
    'review_argument_sha256': sha(review / 'argument.md'), 'review_freeze_sha256': sha(review / 'freeze.json'),
    'binding_sha256': sha(review / 'source-artifact-binding.json'),
    'main_argument_sha256': binding['main_argument_sha256'], 'source_tex_sha256': binding['source_tex_sha256'],
    'source_status_sha256': freeze['source_status_sha256'],
    'complete_author_read_record_sha256': sha(phase1 / 'complete-read-before-review.json'),
    'fresh_reproduction_record_sha256': sha(phase1 / 'reproduction-result.json'),
    'substantive_mathematical_repairs_required': False,
    'scope': freeze['source_status']['exact_result'], 'publish_exact_scope': True,
    'full_original_atom_solved': False,
    'author_residuals_are_not_automatically_original_obligations': True,
    'original_scope_audit_pending': True, 'author_limitations': freeze['source_status']['concrete_gaps'],
    'primary_source_body_bindings': 'All24complete literal primary bodies authenticated and rebound in phase1; all new indispensable applications directly read. Standard foundations are used with exact hypotheses.',
    'DGMS_quote_authentication': 'StonyBrook public PDF authenticated; full selected standing hypotheses, Lemma5.11 proof and Remark5.14 directly root read and bound. Historical IAS403 retained separately.',
    'source_quote_defects_retained': 'Complete literal units preserve OCR and printed defects. Checked normalization and intrinsic half-factor identity govern their use.',
    'same_model_review_is_not_formal_verification': True,
}
recorded = phase2 / 'complete-review-read-record.json'
recorded.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
att = {
    'verdict': 'PASS', 'publish_exact_scope': True, 'run_sha256': sha(review / 'run.json'),
    'canonical_review_result_sha256': sha(canonical),
    'source_artifact_binding_sha256': sha(review / 'source-artifact-binding.json'),
    'root_complete_review_read_record': str(recorded), 'root_complete_review_read_record_sha256': sha(recorded),
    'root_complete_author_read_record': str(phase1 / 'complete-read-before-review.json'),
    'root_complete_author_read_record_sha256': sha(phase1 / 'complete-read-before-review.json'),
    'full_original_atom_solved': False, 'review_operation_id': result['operationId'],
    'review_reported_at': result['reportedAt'],
}
p = review / 'review-read-attestation.json'
assert not p.exists()
p.write_text(json.dumps(att, indent=2) + '\n')
print(json.dumps({'atom': atom, 'verdict': 'PASS', 'premises': premise_count, 'passages': passage_count,
                  'attestation_sha256': sha(p), 'full_original_atom_solved': False}))
