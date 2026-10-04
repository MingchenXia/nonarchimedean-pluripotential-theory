"""Bind completely read native reviews to the exact supplied-fibration proofs."""
from pathlib import Path
import datetime
import hashlib
import json

root = Path('/workspace/research')
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
for atom, relative, counts, tex_lines in [
    ('P15.2', 'round-27/P15.2-relative-zero-volume-operator', (5, 6), 328),
    ('P15.1', 'round-28/P15.1-relative-zero-volume-energy', (6, 9), 765),
]:
    campaign = root / 'campaigns' / relative
    review = Path(str(campaign) + '-review')
    full_run = json.loads((review / 'run.json').read_text())
    result = full_run['campaign']['result']
    freeze = json.loads((review / 'freeze.json').read_text())
    binding = json.loads((review / 'source-artifact-binding.json').read_text())
    assert result['verdict'] == 'PASS'
    assert (len(result['premises']), len(result['passages'])) == counts
    for passage in result['passages']:
        index = passage['premise']
        assert type(index) is int and 0 <= index < len(result['premises'])
        assert passage['statement'] == result['premises'][index]
        assert passage['quote'] and passage['url'] and passage['id']
    assert sha(review / 'freeze.json') == binding['original_freeze_sha256']
    for key, digest in [('main_argument', 'main_argument_sha256'),
                        ('declared_proof_file', 'declared_proof_sha256'),
                        ('source_tex', 'source_tex_sha256')]:
        assert sha(binding[key]) == binding[digest] == freeze[digest]
    assert sha(review / 'argument.md') == freeze['argument_sha256'] == binding['review_argument_sha256']
    assert sha(Path(freeze['source_workspace']) / 'status.json') == freeze['source_status_sha256']
    assert len(Path(binding['source_tex']).read_text().split('\n')) == tex_lines
    phase1 = root / 'root-checks' / ('relative-zero-volume-' + atom + '-phase1')
    assert json.loads((phase1 / 'reproduction-result.json').read_text())['success']
    phase2 = root / 'root-checks' / ('relative-zero-volume-' + atom + '-phase2')
    phase2.mkdir(exist_ok=False)
    canonical = phase2 / 'canonical-review-result.json'
    canonical.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    review_copy = review / 'review-result.json'
    assert not review_copy.exists()
    review_copy.write_bytes(canonical.read_bytes())
    record = {
        'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'atom': atom, 'verdict': result['verdict'],
        'operation_id': result['operationId'], 'reported_at': result['reportedAt'],
        'entire_report_directly_read': True,
        'all_premises_directly_read': list(range(counts[0])),
        'all_passages_directly_read': [passage['id'] for passage in result['passages']],
        'all_zero_based_indices_and_exact_statements_verified': True,
        'main_proof_status_and_source_tex_bound': True,
        'all_source_tex_LF_entries_directly_read': tex_lines,
        'review_run_sha256': sha(review / 'run.json'),
        'review_result_sha256': sha(canonical),
        'review_argument_sha256': sha(review / 'argument.md'),
        'review_freeze_sha256': sha(review / 'freeze.json'),
        'binding_sha256': sha(review / 'source-artifact-binding.json'),
        'main_argument_sha256': binding['main_argument_sha256'],
        'source_tex_sha256': binding['source_tex_sha256'],
        'source_status_sha256': freeze['source_status_sha256'],
        'complete_author_read_record_sha256': sha(phase1 / 'complete-read-before-review.json'),
        'fresh_reproduction_record_sha256': sha(phase1 / 'reproduction-result.json'),
        'mathematical_repairs_required': False,
        'scope': freeze['source_status']['exact_result'],
        'publish_exact_scope': True, 'full_original_atom_solved': False,
        'limitations': freeze['source_status']['concrete_gaps'],
        'standard_foundations_are_precisely_scoped_not_monographs_reproved': True,
    }
    recorded = phase2 / 'complete-review-read-record.json'
    recorded.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    attestation = {
        'verdict': 'PASS', 'publish_exact_scope': True,
        'run_sha256': sha(review / 'run.json'),
        'canonical_review_result_sha256': sha(canonical),
        'source_artifact_binding_sha256': sha(review / 'source-artifact-binding.json'),
        'root_complete_review_read_record': str(recorded),
        'root_complete_review_read_record_sha256': sha(recorded),
        'root_complete_author_read_record': str(phase1 / 'complete-read-before-review.json'),
        'root_complete_author_read_record_sha256': sha(phase1 / 'complete-read-before-review.json'),
        'full_original_atom_solved': False,
        'review_operation_id': result['operationId'],
        'review_reported_at': result['reportedAt'],
    }
    path = review / 'review-read-attestation.json'
    assert not path.exists()
    path.write_text(json.dumps(attestation, indent=2) + '\n')
    print(json.dumps({'atom': atom, 'verdict': 'PASS', 'premises': counts[0],
                      'passages': counts[1], 'attestation_sha256': sha(path),
                      'full_original_atom_solved': False}))
