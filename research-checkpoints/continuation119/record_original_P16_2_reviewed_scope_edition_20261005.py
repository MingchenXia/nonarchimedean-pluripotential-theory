from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, fitz

R = Path('/workspace/research')
D = R / 'deliverables/original-P16.2'
K = R / 'root-checks'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def immutable(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

scope_path = D / 'publication-reviewed-log-coordinate-scope-clarification.json'
scope = json.loads(scope_path.read_text())
assert sha(D / 'P16.2-core.md') == scope['core_sha256']
assert sha(D / 'P16.2-paper.tex') == scope['tex_sha256']
assert sha(D / 'P16.2-paper.pdf') == 'bc4d2745a56e94c0d902f5ef37a0347429c4a823bd8182b062537d29d2419ff7'
for i in [1, 2]:
    assert '(28 pages)' in (D / f'local-scope-clarification-build-pass{i}.stdout.txt').read_text()
log = (D / 'P16.2-paper.log').read_text()
assert not any(x in log for x in ['Undefined control sequence', 'Missing character', 'Overfull', 'LaTeX Error', 'Warning:'])
assert len(fitz.open(D / 'P16.2-paper.pdf')) == 28
canonical = K / 'P16.2-round115-actual-full-original-review-20261005.json'
assert sha(canonical) == 'ce6d0c3aadf67cce1171315d997acbf8ed58a79235fd47da8b8e3b61a3051189'
assert scope['actual_canonical_scope_paragraph'] in json.loads(canonical.read_text())['report']
old_build = json.loads((D / 'prior-checkpoint118/publication-build-and-root-reading.json').read_text())
old_closure = json.loads((D / 'prior-checkpoint118/P16.2-original-closure.json').read_text())
assert old_closure['source_sha256'] == scope['old_tex_sha256']
now = datetime.now(timezone.utc).isoformat()
build = {
    'recorded_utc': now, 'atom': 'P16.2', 'pages': 28,
    'core_sha256': sha(D / 'P16.2-core.md'),
    'source_sha256': sha(D / 'P16.2-paper.tex'),
    'pdf_sha256': sha(D / 'P16.2-paper.pdf'),
    'local_two_pass_compilation': 'SUCCESS',
    'source_errors_missing_glyphs_overfull_or_warnings': False,
    'native_compile': 'Built-in calls1280/1286/1314 have not returned compiler diagnostics or success; no native success asserted.',
    'native_repair_attempts': 2,
    'whole_initial_assembled_core_and_saved_editorial_patches_root_read': True,
    'whole_generated_tex_separately_root_read': False,
    'visually_root_read_pages': [
        {'page': i, 'image': str(K / 'P16.2-reviewed-log-coordinate-scope-layout-20261005' / f'page-{i}.png'),
         'sha256': sha(K / 'P16.2-reviewed-log-coordinate-scope-layout-20261005' / f'page-{i}.png')}
        for i in [23, 24]],
    'prior_edition_visual_reading': old_build['visually_root_read_pages'],
    'prior_images_claimed_as_current_edition': False,
    'whole_PDF_visually_read': False,
    'scope_clarification_record': str(scope_path), 'scope_clarification_sha256': sha(scope_path),
    'accepted_original_theorem_or_generated_operator_category_changed': False,
    'existing_P16_4_editor_modified_replaced_or_new_tab_opened': False
}
build_path = D / 'publication-reviewed-scope-edition-build-20261005.json'
immutable(build_path, build)
(D / 'publication-build-and-root-reading.json').write_text(json.dumps(build, ensure_ascii=False, indent=2) + '\n')
closure = dict(old_closure)
closure.update({
    'edition_updated_utc': now,
    'source_sha256': build['source_sha256'], 'pdf_sha256': build['pdf_sha256'],
    'argument_sha256': build['core_sha256'], 'native_compilation': build['native_compile'],
    'publication_build': str(build_path), 'publication_build_sha256': sha(build_path),
    'reviewed_scope_clarification': str(scope_path), 'reviewed_scope_clarification_sha256': sha(scope_path),
    'prior_checkpoint118_publication_preserved': True,
    'publication_changes': old_closure['publication_changes'] + ' State explicitly that the auxiliary finite PL selector is a specified function of logarithmic coordinates, exactly as canonical115 already required.',
    'new_unreviewed_mathematical_premise_imported': False
})
immutable(K / 'P16.2-original-reviewed-scope-edition-closure-20261005.json', closure)
(D / 'P16.2-original-closure.json').write_text(json.dumps(closure, ensure_ascii=False, indent=2) + '\n')
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    a = json.loads(p.read_text())
    assert len(a['fully_solved_original_atoms']) == 7
    if name == 'checklist-current.json':
        assert a['historical_reviewed_scoped_papers'] == 44
        target = next(t for t in a['targets'] if t['id'] == 'P16.2')
        assert target['fully_solved']
        target['reviewed_papers'] = [closure]
    a['original_P16_2_full_solution'] = closure
    a['updated_utc'] = now
    a['github_pending_checkpoint'] = 'Checkpoint119: reviewed logarithmic-coordinate scope clarification of P16.2, two own unreviewed source observations, and current small batch P16.5/P16.3; no original count increment.'
    p.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'edition_build': str(build_path), 'pdf_sha256': build['pdf_sha256'],
                  'pages': 28, 'original_counts_unchanged': True, 'native_compiler_success_asserted': False}, indent=2))
