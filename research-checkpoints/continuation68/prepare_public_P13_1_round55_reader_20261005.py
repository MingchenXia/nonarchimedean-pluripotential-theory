"""Preserve completed round55; verify bindings without changing its files."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
C = R / 'campaigns/round-55/P13.1-public-source-expanded-signed-energy-uniform-Reeb-differentiation'
result = json.loads((R / 'root-checks/P13.1-round55-actual-result-20261005.json').read_text())
assert result['kind'] == 'notes' and result['candidate'] is False
assert [n['id'] for n in result['notes']] == ['n1', 'n2', 'n3', 'n4']
W = Path(result['workspace'])
assert W == C / 'artifacts/codex-TWhkS8'
D = R / 'root-checks/public-P13.1-round-55-final-reader'
assert not D.exists()
shutil.copytree(W, D)
(D / 'canonical-notes.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
bindings = []
for p in sorted(W.rglob('*')):
    if p.is_file():
        q = D / p.relative_to(W)
        assert p.read_bytes() == q.read_bytes()
        bindings.append({'relative_path': str(p.relative_to(W)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
provenance = json.loads((D / 'source-extracts/source-provenance.json').read_text())
literal_count = 0
for s in provenance['sources']:
    for key, expected in [('pdf', 'pdf_sha256'), ('literal_extract', 'extract_sha256')]:
        assert sha(s[key]) == s[expected]
    if 'html' in s:
        assert sha(s['html']) == s['html_sha256']
    source = Path(s['literal_extract']).read_bytes().decode('utf-8').split('\n')
    for e in s['excerpts']:
        actual = '\n'.join(source[e['first_line'] - 1:e['last_line']])
        q = D / e['file']
        assert actual == e['literal'] == q.read_bytes().decode('utf-8')
        assert sha(q) == e['sha256']
        literal_count += 1
assert len(provenance['sources']) == 8 and literal_count == 55
campaign_input = json.loads((C / 'input.json').read_text())
native_input = json.loads((D / 'input.json').read_text())
assert native_input == campaign_input
assert (D / 'input.json').read_bytes() == (D / 'input-original.json').read_bytes()
assert json.loads((D / 'task-original.json').read_text()) == campaign_input['task']
assert (D / 'assignment-original.txt').read_text() == campaign_input['assignment']
status = json.loads((D / 'status.json').read_text())
assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert status['id'] == 'P13.1' and status['status'] == 'partial'
record = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'original_workspace': str(W), 'frozen_reader': str(D),
    'candidate': False, 'original_problem_solved': False,
    'entire_completed_native_result_and_all_four_notes_root_read': True,
    'whole_argument_root_read': True, 'argument_LF_count': 905,
    'whole_tex_root_read': True, 'tex_LF_count': 951,
    'source_application_checks_and_excerpt_index_root_read': True,
    'all_literal_excerpts_byte_reproduced': True, 'literal_excerpts': 55,
    'all_literal_excerpt_bodies_root_read': False,
    'whole_primary_source_bodies_root_read': False,
    'campaign_and_native_input_semantically_equal': True,
    'native_input_original_bytes_equal': True,
    'campaign_input_sha256': sha(C / 'input.json'),
    'native_input_sha256': sha(D / 'input.json'),
    'root_independent_tex_compilation': 'NOT_YET_RUN',
    'native_editor_compilation': 'NOT_YET_REQUESTED',
    'independent_correctness_review': 'NOT_LAUNCHED',
    'binding_checks': bindings,
    'evidence_limit': 'Preservation and LF bindings only; new mathematical claims unreviewed.'
}
(D / 'root-preservation-and-read-state-continuation68.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'reader': str(D), 'files': len(bindings), 'literal_bindings': literal_count,
                  'argument_sha256': sha(D / 'P13.1-argument.md'),
                  'pdf_sha256': sha(D / 'P13.1-paper.pdf'),
                  'canonical_result_sha256': sha(D / 'canonical-notes.json'), 'candidate': False}, indent=2))
