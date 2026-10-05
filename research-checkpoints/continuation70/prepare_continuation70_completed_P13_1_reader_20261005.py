"""Freeze completed round60 actual notes and argument, with reproduced source bindings."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
C = R / 'campaigns/round-60/P13.1-public-source-relative-volume-and-uniform-Reeb-energy'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
actual = json.loads((C / 'run.json').read_text())['campaign']['result']
assert actual['kind'] == 'notes' and actual['candidate'] is False
assert [n['id'] for n in actual['notes']] == ['n1', 'n2', 'n3', 'n4']
W = Path(actual['workspace'])
assert W == C / 'artifacts/codex-ohEvFG'
P = R / 'root-checks/P13.1-round60-actual-result-20261005.json'
D = R / 'root-checks/public-P13.1-round-60-final-reader'
assert not P.exists() and not D.exists()
write(P, actual)
shutil.copytree(W, D)
bindings = []
for p in sorted(W.rglob('*')):
    if p.is_file():
        assert p.read_bytes() == (D / p.relative_to(W)).read_bytes()
        bindings.append({'relative_path': str(p.relative_to(W)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
write(D / 'canonical-notes.json', actual)
prov = json.loads((D / 'source-extracts/source-provenance.json').read_text())
assert len(prov['sources']) == 10
excerpt_count = 0
file_count = 0
for s in prov['sources']:
    for f in s['files']:
        assert sha(f['path']) == f['sha256'] == f['expected_sha256']
        file_count += 1
    text_file = next(f for f in s['files'] if f['kind'] == 'literal_extract')
    lines = Path(text_file['path']).read_bytes().decode('utf-8').split('\n')
    assert len(lines) == s['LF_split_length']
    for e in s['excerpts']:
        a, b = e['inclusive_one_based_LF_range']
        assert '\n'.join(lines[a-1:b]) == e['literal_text']
        excerpt_count += 1
assert excerpt_count == 64
ci = json.loads((C / 'input.json').read_text())
assert json.loads((D / 'input.json').read_text()) == ci
assert (D / 'input.json').read_bytes() == (D / 'input-original.json').read_bytes()
assert json.loads((D / 'task-original.json').read_text()) == ci['task']
assert (D / 'assignment-original.txt').read_text() == ci['assignment']
status = json.loads((D / 'status.json').read_text())
assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert status['status'] == 'partial' and status['id'] == 'P13.1'
write(D / 'root-preservation-and-read-state-continuation70.json', {
    'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'original_workspace': str(W), 'frozen_reader': str(D),
    'actual_result': str(P), 'actual_result_sha256': sha(P),
    'candidate': False, 'original_problem_solved': False,
    'entire_completed_native_result_and_four_notes_root_read': True,
    'whole_argument_root_read': True, 'argument_LF_count': 348,
    'whole_tex_root_read': False,
    'source_application_checks_and_excerpt_index_root_read': True,
    'all_literal_excerpts_byte_reproduced': True, 'literal_excerpts': excerpt_count,
    'source_file_hash_bindings_reproduced': file_count,
    'all_literal_excerpt_bodies_root_read': False, 'whole_primary_sources_root_read': False,
    'campaign_and_native_input_semantically_equal': True,
    'native_input_original_bytes_equal': True,
    'campaign_input_sha256': sha(C / 'input.json'), 'native_input_sha256': sha(D / 'input.json'),
    'root_independent_tex_compilation': 'NOT_YET_RUN',
    'native_editor_compilation': 'NOT_YET_REQUESTED', 'independent_correctness_review': 'NOT_LAUNCHED',
    'original_author_file_bindings': bindings,
    'evidence_limit': 'Exact preservation and selected root reading; mathematical claims are unreviewed.'
})
print(json.dumps({'reader': str(D), 'author_files': len(bindings),
                  'source_hashes': file_count, 'LF_bindings': excerpt_count,
                  'candidate': False, 'original_closed': False}, indent=2))
