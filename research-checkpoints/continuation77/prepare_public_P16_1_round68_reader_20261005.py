"""Freeze the completed public result and reproduce literal source bindings."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
C = R/'campaigns/round-68/P16.1-public-source-BE-exact-PL-local-mass-and-unibranch-equation'
P = R/'root-checks/P16.1-round68-actual-result-20261005.json'
result = json.loads(P.read_text())
assert result == json.loads((C/'run.json').read_text())['campaign']['result']
assert result['kind'] == 'notes' and result['candidate'] is False
assert [n['id'] for n in result['notes']] == ['n1', 'n2', 'n3', 'n4']
W = Path(result['workspace'])
assert W == C/'artifacts/codex-9wTVxt'
D = R/'root-checks/public-P16.1-round-68-final-reader'
assert not D.exists()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
shutil.copytree(W, D)
checks = []
for p in sorted(W.rglob('*')):
    if p.is_file():
        q = D/p.relative_to(W)
        assert p.read_bytes() == q.read_bytes()
        checks.append({'relative_path': str(p.relative_to(W)), 'bytes': p.stat().st_size,
                       'sha256': sha(p)})
(D/'canonical-native-result.json').write_bytes(P.read_bytes())
prov = json.loads((D/'source-extracts/source-provenance.json').read_text())
file_count = excerpt_count = 0
for source in prov['sources']:
    for kind, f in source['files'].items():
        assert sha(D/f['local_copy']) == sha(f['authorized_path']) == f['sha256']
        file_count += 1
    text_path = D/source['files']['literal_extract']['local_copy']
    lines = text_path.read_bytes().decode('utf-8').split('\n')
    assert len(lines) == source['LF_split_count']
    scope = {'checked_applications': source['checked_applications'],
             'concrete_limits': source['concrete_limits']}
    for e in source['literal_statements_and_proof_bodies']:
        literal = '\n'.join(lines[e['start_LF']-1:e['end_LF']])
        assert literal == e['literal'] == (D/e['artifact']).read_bytes().decode('utf-8')
        assert sha(D/e['artifact']) == e['literal_sha256']
        assert e['application_scope'] == scope
        excerpt_count += 1
assert file_count == 23 and excerpt_count == prov['excerpt_count'] == 84
native = json.loads((D/'input.json').read_text())
campaign = json.loads((C/'input.json').read_text())
assert native == campaign
assert (D/'input.json').read_bytes() == (D/'input-original.json').read_bytes()
assert json.loads((D/'task-original.json').read_text()) == campaign['task']
assert (D/'assignment-original.txt').read_bytes().decode('utf-8') == campaign['assignment']
status = json.loads((D/'status.json').read_text())
assert set(status) == {'id','status','exact_result','proof_file','concrete_gaps'}
assert status['status'] == 'partial'
argument = D/'P16.1-argument.md'
assert len(argument.read_bytes().decode('utf-8').split('\n')) == 1151
record = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'original_workspace': str(W), 'frozen_reader': str(D),
    'candidate': False, 'original_problem_solved': False,
    'all_four_actual_canonical_notes_root_read': True,
    'whole_argument_root_read': True, 'argument_LF_count': 1151,
    'whole_tex_root_read': False,
    'all_source_application_scopes_and_excerpt_index_root_read': True,
    'all_literal_excerpt_bodies_root_read': False,
    'whole_primary_source_bodies_root_read': False,
    'all_literal_excerpt_bindings_reproduced': True,
    'literal_excerpts': excerpt_count, 'primary_files_hash_bound': file_count,
    'campaign_and_native_input_semantically_equal': True,
    'native_input_and_preserved_original_byte_equal': True,
    'task_and_assignment_preserved': True,
    'native_editor_compilation': 'NOT_YET_REQUESTED',
    'author_two_pass_compilation': 'Reported successful; build records preserved. Root did not rerun.',
    'independent_correctness_review': 'NOT_LAUNCHED',
    'actual_result_sha256': sha(P), 'argument_sha256': sha(argument),
    'tex_sha256': sha(D/'P16.1-paper.tex'), 'pdf_sha256': sha(D/'P16.1-paper.pdf'),
    'binding_checks': checks,
    'evidence_limit': 'Literal preservation and root reading do not certify the new mathematics.'
}
(D/'root-preservation-and-read-state-continuation77.json').write_text(
    json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({k: record[k] for k in ['frozen_reader','candidate','argument_sha256',
       'tex_sha256','pdf_sha256','literal_excerpts','primary_files_hash_bound']}, indent=2))
print('preserved_author_files', len(checks))
