"""Preserve round58 and bind the completed round51 review to primary bytes."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import unicodedata

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
C = R / 'campaigns/round-58/P16.1-public-source-algebraic-collar-trace-and-unibranch-equation'
result = json.loads((R / 'root-checks/P16.1-round58-actual-result-20261005.json').read_text())
assert result['kind'] == 'notes' and result['candidate'] is False
assert [n['id'] for n in result['notes']] == ['n1', 'n2', 'n3', 'n4']
W = Path(result['workspace'])
assert W == C / 'artifacts/codex-8LHPwu'
D = R / 'root-checks/public-P16.1-round-58-final-reader'
assert not D.exists()
shutil.copytree(W, D)
bindings = []
for p in sorted(W.rglob('*')):
    if p.is_file():
        q = D / p.relative_to(W)
        assert p.read_bytes() == q.read_bytes()
        bindings.append({'relative_path': str(p.relative_to(W)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
write(D / 'canonical-notes.json', result)
prov = json.loads((D / 'source-extracts/source-provenance.json').read_text())
sources = {s['id']: s for s in prov['sources']}
assert len(sources) == 6
for s in sources.values():
    for f in s['files']:
        assert sha(f['cache']) == f['sha256'] == sha(D / f['artifact'])
for e in prov['excerpts']:
    s = sources[e['source']]
    f = next(f for f in s['files'] if f['artifact'].endswith('.txt'))
    a, b = e['inclusive_one_based_LF_range']
    literal = '\n'.join(Path(f['cache']).read_bytes().decode('utf-8').split('\n')[a-1:b])
    assert literal == e['literal_statement_and_relevant_proof_body']
    assert literal == (D / e['artifact']).read_bytes().decode('utf-8')
assert len(prov['excerpts']) == 56
ci = json.loads((C / 'input.json').read_text())
assert json.loads((D / 'input.json').read_text()) == ci
assert (D / 'input.json').read_bytes() == (D / 'input-original.json').read_bytes()
assert json.loads((D / 'task-original.json').read_text()) == ci['task']
assert (D / 'assignment-original.txt').read_text() == ci['assignment']
status = json.loads((D / 'status.json').read_text())
assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert status['status'] == 'partial' and status['id'] == 'P16.1'
write(D / 'root-preservation-and-read-state-continuation69.json', {
    'recorded_utc': now(), 'original_workspace': str(W), 'frozen_reader': str(D),
    'candidate': False, 'original_problem_solved': False,
    'entire_completed_native_result_and_four_notes_root_read': True,
    'whole_argument_root_read': True, 'argument_LF_count': 1106,
    'whole_tex_root_read': False,
    'source_application_checks_and_excerpt_index_root_read': True,
    'all_literal_excerpts_byte_reproduced': True, 'literal_excerpts': 56,
    'all_literal_excerpt_bodies_root_read': False, 'whole_primary_sources_root_read': False,
    'campaign_and_native_input_semantically_equal': True,
    'native_input_original_bytes_equal': True,
    'campaign_input_sha256': sha(C / 'input.json'), 'native_input_sha256': sha(D / 'input.json'),
    'root_independent_tex_compilation': 'NOT_YET_RUN',
    'native_editor_compilation': 'NOT_YET_REQUESTED', 'independent_correctness_review': 'NOT_LAUNCHED',
    'original_author_file_bindings': bindings,
    'evidence_limit': 'Exact preservation and selected root reading; mathematical claims are unreviewed.'
})

P = R / 'root-checks/P13.2-round51-v2-actual-review-result-20261005.json'
review = json.loads(P.read_text())
assert review['verdict'] == 'INCONCLUSIVE'
assert len(review['premises']) == 4 and len(review['passages']) == 11
author = R / 'root-checks/public-P13.2-round-51-final-reader'
sp = json.loads((author / 'source-extracts/source-provenance.json').read_text())
by_url = {s['public_source']: s for s in sp['sources']}
normalize = lambda s: ''.join(unicodedata.normalize('NFKC', s).split())
passage_bindings = []
for p in review['passages']:
    assert p['statement'] == review['premises'][p['premise']]
    s = by_url[p['url']]
    assert sha(s['extract']) == s['extract_sha256']
    assert normalize(p['quote']) in normalize(Path(s['extract']).read_text())
    passage_bindings.append({
        'id': p['id'], 'premise_index': p['premise'], 'exact_statement_binding': True,
        'url': p['url'], 'source_version': s['saved_version'],
        'literal_text_sha256': s['extract_sha256'],
        'quote_NFKC_whitespace_binding': True
    })
write(R / 'root-checks/P13.2-round51-v2-root-review-read-and-bindings-continuation69.json', {
    'recorded_utc': now(), 'actual_result': str(P), 'actual_result_sha256': sha(P),
    'operationId': review['operationId'], 'reportedAt': review['reportedAt'],
    'verdict': review['verdict'], 'whole_report_all_premises_all_passages_root_read': True,
    'mathematical_scope': 'Exact partial n1-n3; original image/existence characterization remains open.',
    'remaining_review_limit': 'Native reviewer could not verify requested n4 local execution, hashes, preserved inputs or compilation observations because it lacked a local file reader.',
    'independently_accepted': False, 'fully_solved_original_atom': False,
    'all_zero_based_statement_bindings': True, 'passage_bindings': passage_bindings
})
print(json.dumps({'P16.1_reader': str(D), 'author_files': len(bindings), 'LF_bindings': 56,
                  'P13.2_verdict': review['verdict'], 'P13.2_passage_bindings': len(passage_bindings)}, indent=2))
