from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, fitz

R = Path('/workspace/research'); K = R / 'root-checks'
C = R / 'campaigns/round-116/P16.3-original-full-residue-characteristic-reconstruction'
W = C / 'artifacts/codex-xAHbiy'
P = K / 'public-P16.3-round116-final-reader'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
canonical = K / 'P16.3-round116-actual-native-author-result-20261005.json'
v = json.loads(canonical.read_text())
assert v['candidate'] is False and len(v['notes']) == 5
assert sha(canonical) == '11cc64118dbac74b7b84ac6c1db0a30e936583dfa1773fcf53f92675ee91449b'
assert Path(v['workspace']) == W
outer = json.loads((C / 'input.json').read_text())
worker = json.loads((W / 'input.json').read_text())
assert outer == worker
assert (W / 'input.json').read_bytes() == (W / 'input-original.json').read_bytes()
assert (W / 'assignment-original.txt').read_text() == worker['assignment']
assert json.loads((W / 'task-original.json').read_text()) == worker['task']
status = json.loads((W / 'status.json').read_text())
assert status['status'] == 'partial' and set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
build = json.loads((W / 'build/build-results.json').read_text())
assert [p['returncode'] for p in build['passes']] == [0, 0]
assert sha(W / 'P16.3-paper.tex') == build['tex_sha256']
assert sha(W / 'build/P16.3-paper.pdf') == build['pdf_sha256']
assert len(fitz.open(W / 'build/P16.3-paper.pdf')) == 16
assert len((W / 'P16.3-argument.md').read_text().split('\n')) - 1 == 551
assert not P.exists(); P.mkdir()
for name in ['P16.3-argument.md', 'P16.3-paper.tex', 'status.json', 'source-application-ledger.json',
             'artifact-checks.json', 'descent-check-results.json', 'descent_check.py', 'build_paper.py']:
    shutil.copyfile(W / name, P / name)
shutil.copyfile(W / 'build/P16.3-paper.pdf', P / 'P16.3-paper.pdf')
shutil.copyfile(W / 'build/build-results.json', P / 'author-local-two-pass-build.json')
shutil.copyfile(canonical, P / 'canonical-native-author-result.json')
record = {
    'recorded_utc': datetime.now(timezone.utc).isoformat(), 'atom': 'P16.3', 'round': 116,
    'state': 'Completed native author, partial, candidate=false; not independent acceptance.',
    'canonical_sha256': sha(canonical), 'canonical_candidate': False,
    'whole_551LF_argument_all5_actual_canonical_notes_status_and_source_application_ledger_root_read': True,
    'whole_generated_tex_separately_root_read': False,
    'worker_frozen_input_byte_identity': True, 'outer_to_worker_decoded_input_semantic_identity': True,
    'outer_input': str(C / 'input.json'), 'outer_input_sha256': sha(C / 'input.json'),
    'worker_input_sha256': sha(W / 'input.json'),
    'outer_and_worker_serialized_bytes_identical': (C / 'input.json').read_bytes() == (W / 'input.json').read_bytes(),
    'serialization_note': 'Xean serializes the native worker input independently; both decoded objects and the worker input/original pair are exact. Distinct serialized hashes are not conflated.',
    'standalone_pages': 16, 'local_two_pass_build': [0, 0], 'build_source_and_pdf_hashes_match': True,
    'source_sha256': sha(P / 'P16.3-paper.tex'), 'pdf_sha256': sha(P / 'P16.3-paper.pdf'),
    'argument_sha256': sha(P / 'P16.3-argument.md'),
    'source_application_ledger_sha256': sha(P / 'source-application-ledger.json'),
    'entire76_author_primary_page_extracts_or_complete_provenance_root_read': False,
    'author_primary_reading_claims_treated_as_source_audit_not_independent_root_reading': True,
    'conditional_two_FGK_resolution_inputs_preserved': True,
    'original_P16_3_closed': False, 'original_count_incremented': False, 'scoped_count_incremented': False,
    'private_native_transcripts_or_extended_inspection_uploaded': False,
    'whole_third_party_primary_papers_page_extracts_images_uploaded': False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened': False,
    'native_compilation': 'Not yet requested for this reader; no native success asserted.',
    'visual_reading': 'Not yet performed; no whole PDF visual reading claimed.'
}
(P / 'root-terminal-reader-observation.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
layout = K / 'P16.3-round116-reader-layout-20261005'; assert not layout.exists(); layout.mkdir()
pdf = fitz.open(P / 'P16.3-paper.pdf')
for page in [1, 8, 16]:
    pdf[page - 1].get_pixmap(matrix=fitz.Matrix(1.3, 1.3)).save(layout / f'page-{page}.png')
print(json.dumps({'public_reader': str(P), 'pages': 16, 'original_closed': False,
                  'outer_worker_semantic_identity': True, 'canonical_candidate': False}, indent=2))
