"""Publish two exact-scoped reviewed theorems, preserving immutable evidence."""
from pathlib import Path
import datetime, hashlib, json, shutil, zipfile

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
load = lambda p: json.loads(p.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()

def write_new(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

common = ('Supplied surjective holomorphic pi:X->B between connected smooth compact '
    'Kahler manifolds, dim X=n>nu=dim B>=1, beta Kahler, theta=pi*beta, m=n-nu. '
    'Critical and dimension-jumping fibres included, with no connected-fibre assumption '
    'for the main theorem. Globally bounded beta-psh phi and bounded admissible '
    'u_epsilon uniformly converging to pi*phi; u_epsilon need not descend and no '
    'epsilon-relative rate is required. All auxiliary Kahler classes after the '
    'explicit c_omega=pi_*(omega^m)>0 calibration; smoothly converging auxiliary '
    'paths with Kahler limit included. Raw base mass is int_B beta^nu. ')
limits = ('This requires a supplied fibration and pullback Kahler class. No canonical '
    'carrier for general pseudoeffective classes, minimum necessary reference data, '
    'unbounded prescribed singularity type or E1 completion, or arbitrary degenerate '
    'auxiliary path is proved. The original problem remains open.')
items = [
 (27, 'P15.2', 'P15.2-relative-zero-volume-operator', 5, 6,
  common + 'The pushforward of (theta+epsilon omega+ddc u_epsilon)^n divided by '
  'binom(n,nu)c_omega epsilon^m converges against every continuous base test to '
  '(beta+ddc phi)^nu. Supporting bounded energy, cocycle and affine variation laws '
  'and compensating base representative changes are proved. ' + limits,
  'The full first page is legible; the title, stated scope and displayed operator '
  'formula have no clipping. Remaining pages checked by compilation diagnostics only.'),
 (28, 'P15.1', 'P15.1-relative-zero-volume-energy', 6, 9,
  common + 'Unnormalized energy divided by binom(n,nu)c_epsilon epsilon^m '
  'converges to E_beta(phi), and corresponding relative energies converge. '
  'Exact bounded shift, cocycle, monotonicity, concavity, affine variation and '
  'C1 uniform paths in C(B) with continuous velocities are proved. The calibrated '
  'base operator is supporting. Base representative changes have an explicit '
  'reference cocycle. Optional continuous descent requires connected fibres. ' + limits,
  'The full first page is legible, including the title and opening energy definition, '
  'which continues on the next page. A second full-resolution inspection confirmed '
  'the page footer and no clipping; remaining pages checked by compilation diagnostics only.')]

for n, atom, stem, nprem, npass, scope, observation in items:
    out = R / f'deliverables/round-{n}'
    d = R / f'campaigns/round-{n}' / (stem + '-review')
    phase1 = R / f'root-checks/relative-zero-volume-{atom}-phase1'
    phase2 = R / f'root-checks/relative-zero-volume-{atom}-phase2'
    run = load(d / 'run.json'); result = run['campaign']['result']
    f = load(d / 'freeze.json'); b = load(d / 'source-artifact-binding.json')
    att = load(d / 'review-read-attestation.json')
    author = load(phase1 / 'complete-read-before-review.json')
    root_review = load(phase2 / 'complete-review-read-record.json')
    repro = load(phase1 / 'reproduction-result.json')
    assert run['campaign']['status'] == 'completed' and result['verdict'] == 'PASS'
    assert len(result['premises']) == nprem and len(result['passages']) == npass
    assert result == load(d / 'review-result.json') == load(phase2 / 'canonical-review-result.json')
    for p in result['passages']:
        assert 0 <= p['premise'] < nprem and p['statement'] == result['premises'][p['premise']]
    assert att['verdict'] == 'PASS' and att['publish_exact_scope'] and not att['full_original_atom_solved']
    assert att['run_sha256'] == sha(d / 'run.json')
    assert att['canonical_review_result_sha256'] == sha(phase2 / 'canonical-review-result.json')
    assert att['source_artifact_binding_sha256'] == sha(d / 'source-artifact-binding.json')
    for key in ('root_complete_review_read_record', 'root_complete_author_read_record'):
        assert sha(Path(att[key])) == att[key + '_sha256']
    assert author['all_main_LF_entries_directly_read'] and author['all_actual_canonical_notes_full_text_directly_read']
    assert author['canonical_result_record_sha256'] == sha(phase1 / 'canonical-result-record.json')
    for key in ('entire_report_directly_read', 'all_premises_directly_read', 'all_passages_directly_read',
                'all_zero_based_indices_and_exact_statements_verified', 'all_source_tex_LF_entries_directly_read'):
        assert root_review[key]
    assert root_review['review_freeze_sha256'] == sha(d / 'freeze.json') == b['original_freeze_sha256']
    assert sha(d / 'argument.md') == f['argument_sha256'] == b['review_argument_sha256']
    for key, hashkey in [('main_argument', 'main_argument_sha256'), ('source_tex', 'source_tex_sha256'),
                         ('declared_proof_file', 'declared_proof_sha256')]:
        assert sha(Path(b[key])) == b[hashkey] == f[hashkey]
    w = Path(f['source_workspace'])
    assert sha(w / 'status.json') == f['source_status_sha256'] == b['source_status_sha256']
    assert repro['success'] and repro['frozen_worker_proof_and_tex_unchanged']
    assert repro['fresh_generated_tex_byte_identical_to_frozen_author_tex']
    assert repro['copied_reproduction_proof_sha256'] == b['main_argument_sha256']
    assert repro['copied_reproduction_tex_sha256'] == b['source_tex_sha256']
    edits = load(d / 'publication-edits.json'); text = Path(b['source_tex']).read_text()
    for e in edits:
        assert text.count(e['before']) == e['expected_occurrences']
        text = text.replace(e['before'], e['after'])
    tex = out / (stem + '.tex'); pdf = out / (stem + '.pdf')
    prep = load(R / f'deliverables/round-{n}-source-preparation.json')
    assert tex.read_text() == text and sha(tex) == prep['sha256']
    assert sha(d / 'publication-edits.json') == prep['publication_edits_sha256']
    native = load(R / f'deliverables/round-{n}-native-verification-v2.json')
    export = load(out / 'export-evidence.json')
    assert native['native_compilation_confirmed'] and native['tool_result']['kind'] == 'success'
    assert json.loads(native['tool_result_raw']) == native['tool_result']
    assert native['source_sha256'] == export['source_sha256'] == sha(tex)
    assert export['pdf_sha256'] == sha(pdf) and not export['source_changed']
    assert len(export['runs']) == 2 and all(x['exit_code'] == 0 for x in export['runs'])
    assert not any(export['final_notices'].values())
    visual = {'recorded_utc': now, 'inspection_utc_interval': '2026-10-04 06:41--06:42 UTC',
        'pdf_sha256': sha(pdf), 'pages': export['pages'], 'image': str(out / 'first-page.png'),
        'image_sha256': sha(out / 'first-page.png'), 'first_page_visually_inspected': True,
        'observation': observation, 'all_pages_visually_inspected': False}
    write_new(R / f'deliverables/round-{n}-visual-check.json', visual)
    arg = out / (stem + '-argument.md'); assert not arg.exists()
    shutil.copyfile(d / 'argument.md', arg)
    receipt = out / (stem + '-review.json')
    write_new(receipt, {'generated_utc': now, 'original_atom': atom, 'full_original_atom_solved': False,
        'precise_scope': scope, 'route': 'Xean native Codex independent review',
        'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'review_run_sha256': sha(d / 'run.json'),
        'freeze': f, 'source_artifact_binding': b, 'review_read_attestation': att,
        'result': result, 'post_review_edits': edits,
        'published_files': {p.name: sha(p) for p in (tex, pdf, arg)},
        'native_editor_verification': native, 'export_verification': export,
        'visual_verification': visual,
        'review_limit': 'Same-model independent review is not formal verification, original-problem closure or priority certification.'})
    write_new(out / 'results.json', {'generated_utc': now, 'selected_atoms': ['P15.1', 'P15.2'],
        'catalogue_atoms': 42, 'fully_solved_original_atoms': [], 'route': 'Xean native Codex',
        'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'papers_and_supporting_note': [
            {'atom': atom, 'scope': scope, 'full_original_atom_solved': False, 'pages': export['pages'],
             'files': {p.name: sha(p) for p in (tex, pdf, arg, receipt)}}]})
    source_metadata_path = w / ('evidence/source-provenance.json' if n == 27 else 'source-provenance.json')
    write_new(out / 'source-provenance.json', {'generated_utc': now, 'source_workspace': str(w),
        'source_metadata': load(source_metadata_path), 'source_metadata_sha256': sha(source_metadata_path),
        'primary_units': author['primary_units'], 'standard_foundations': author['standard_foundations'],
        'full_essential_primary_bodies_retained_in_frozen_argument': True,
        'primary_bodies_and_new_mathematical_applications_fully_root_read': True,
        'frozen_source_binding': b, 'publication_edits_sha256': sha(d / 'publication-edits.json'),
        'post_review_changes': 'Reviewed-status metadata, bibliography attribution and native math grouping only, replayed exactly. No new mathematical argument.',
        'native_metadata_history': {'initial_record': str(R / f'deliverables/round-{n}-native-verification.json'),
            'corrected_record': str(R / f'deliverables/round-{n}-native-verification-v2.json'),
            'explanation': 'Native compiler returned successful serialized JSON. The first parser failed to decode it; the preserved correction changes metadata only.'},
        'whole_archival_PDFs_and_texts_local_only': True})
    copies = {phase1 / 'canonical-result-record.json': 'canonical-native-result.json',
        phase1 / 'complete-read-before-review.json': 'root-complete-author-read.json',
        phase2 / 'complete-review-read-record.json': 'root-complete-review-read.json',
        phase1 / 'reproduction-result.json': 'root-reproduction-result.json',
        d / 'review-read-attestation.json': 'review-read-attestation.json',
        R / f'deliverables/round-{n}-native-verification-v2.json': 'native-editor-verification.json',
        R / f'deliverables/round-{n}-visual-check.json': 'visual-check.json'}
    for src, name in copies.items():
        assert not (out / name).exists(); shutil.copyfile(src, out / name)
    (out / 'INDEX.txt').write_text('Reviewed relative zero-volume fibration theorem\n\n' + scope +
        '\n\nThe packet contains the paper and source, full frozen proof and essential primary quotations, '
        'complete independent review, canonical native notes, root read and reproduction records, '
        'source provenance and native compilation/PDF export evidence. Same-model review is not '
        'formal verification or priority certification. All 42 original problems remain open.\n')
    names = [tex.name, pdf.name, arg.name, receipt.name, 'results.json', 'source-provenance.json',
        *copies.values(), 'export-evidence.json', 'INDEX.txt']
    entries = {name: sha(out / name) for name in names}
    bundle = R / f'deliverables/reviewed-papers-round-{n}.zip'; assert not bundle.exists()
    with zipfile.ZipFile(bundle, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name in names: z.write(out / name, name)
    with zipfile.ZipFile(bundle) as z:
        assert set(z.namelist()) == set(entries)
        for name, h in entries.items(): assert hashlib.sha256(z.read(name)).hexdigest() == h
    write_new(R / f'deliverables/round-{n}-bundle-manifest.json', {'created_utc': now,
        'bundle': str(bundle), 'sha256': sha(bundle), 'bytes': bundle.stat().st_size,
        'entries': entries, 'full_original_atom_solved': False})
    print(json.dumps({'round': n, 'atom': atom, 'bundle': str(bundle), 'sha256': sha(bundle),
        'pages': export['pages'], 'entries': len(entries), 'full_original_atoms_solved': 0}))
