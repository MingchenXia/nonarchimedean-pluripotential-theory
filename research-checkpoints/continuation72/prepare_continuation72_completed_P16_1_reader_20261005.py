"""Freeze round61 exactly and independently reproduce all literal/source bindings."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
C = R / 'campaigns/round-61/P16.1-public-source-calibrated-local-BT-and-unibranch-equation'
P = R / 'root-checks/P16.1-round61-actual-result-20261005.json'
D = R / 'root-checks/public-P16.1-round-61-final-reader'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
actual = json.loads((C / 'run.json').read_text())['campaign']['result']
assert actual == json.loads(P.read_text())
assert actual['kind'] == 'notes' and actual['candidate'] is False
assert [n['id'] for n in actual['notes']] == ['n1', 'n2', 'n3', 'n4']
W = Path(actual['workspace'])
assert W == C / 'artifacts/codex-w7E2hK' and not D.exists()
shutil.copytree(W, D)
bindings = []
for p in sorted(W.rglob('*')):
    if p.is_file():
        assert p.read_bytes() == (D / p.relative_to(W)).read_bytes()
        bindings.append({'relative_path': str(p.relative_to(W)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
write(D / 'actual-canonical-notes.json', actual)
prov = json.loads((D / 'source-extracts/source-provenance.json').read_text())
assert len(prov['sources']) == 6
excerpt_count = 0
file_count = 0
index = []
for s in prov['sources']:
    for f in s['local_files'].values():
        assert sha(D / f['path']) == f['sha256']
        file_count += 1
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
    lines = Path(s['literal_extract']).read_bytes().decode().split('\n')
    assert len(lines) == s['lf_line_count']
    for e in s['excerpts']:
        first, last = e['start_lf_1based'], e['end_lf_1based_inclusive']
        literal = '\n'.join(lines[first-1:last])
        assert literal == e['literal']
        assert (D / e['artifact']).read_bytes().decode() == literal
        assert sha(D / e['artifact']) == e['sha256']
        excerpt_count += 1
        index.append({'version': s['saved_version'], 'title': e['title'], 'inclusive_LF': [first, last],
            'application_and_limit': e['application_and_limit'], 'literal_sha256': e['sha256']})
assert excerpt_count == 61 and file_count == 12
ci = json.loads((C / 'input.json').read_text())
assert json.loads((D / 'input.json').read_text()) == ci
assert (D / 'input.json').read_bytes() == (D / 'input-original.json').read_bytes()
assert json.loads((D / 'task-original.json').read_text()) == ci['task']
assert (D / 'assignment-original.txt').read_text() == ci['assignment']
status = json.loads((D / 'status.json').read_text())
assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert status['status'] == 'partial' and status['id'] == 'P16.1'
assert len((D / 'P16.1-argument.md').read_bytes().decode().split('\n')) == 1393
write(D / 'root-preservation-and-read-state-continuation72.json', {
    'recorded_utc': datetime.now(timezone.utc).isoformat(), 'original_workspace': str(W),
    'frozen_reader': str(D), 'actual_result': str(P), 'actual_result_sha256': sha(P),
    'candidate': False, 'original_problem_solved': False,
    'entire_completed_native_result_and_four_notes_root_read': True,
    'whole_argument_root_read': True, 'argument_LF_count': 1393, 'whole_tex_root_read': False,
    'source_application_checks_and_excerpt_index_root_read': False,
    'all_literal_excerpts_byte_reproduced': True, 'literal_excerpts': excerpt_count,
    'source_file_hash_bindings_reproduced': file_count,
    'all_literal_excerpt_bodies_root_read': False, 'whole_primary_sources_root_read': False,
    'campaign_and_native_input_semantically_equal': True, 'native_input_original_bytes_equal': True,
    'campaign_input_sha256': sha(C / 'input.json'), 'native_input_sha256': sha(D / 'input.json'),
    'argument_sha256': sha(D / 'P16.1-argument.md'), 'tex_sha256': sha(D / 'P16.1-paper.tex'),
    'pdf_sha256': sha(D / 'P16.1-paper.pdf'),
    'root_independent_tex_compilation': 'NOT_YET_RUN', 'native_editor_compilation': 'NOT_YET_REQUESTED',
    'independent_correctness_review': 'NOT_LAUNCHED', 'original_author_file_bindings': bindings,
    'evidence_limit': 'Exact preservation and selected root reading; mathematical claims are unreviewed.'})
write(D / 'source-binding-and-application-index-continuation72.json', index)
print(json.dumps({'reader': str(D), 'author_files': len(bindings), 'LF_bindings': excerpt_count,
    'source_file_hashes': file_count, 'candidate': False, 'original_closed': False}, indent=2))
