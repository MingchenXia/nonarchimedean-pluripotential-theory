from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
specs = [
    (45, 'P16.1', 'P16.1-public-source-singular-finite-energy-equations',
     'Independently reconstruct the actual unibranch singular-curve theorem over algebraically closed trivially valued characteristic-zero k, retaining integral projective X and actual ample L. Check finite normalization, analytic homeomorphism, point-ideal orders and isolated-ray generators, complete PL descent, and model-nef reflection only after target PL membership. Check every fixed-class approximation, no conductor jet assertion, ample degree and reference pullback. Reconstruct the complete slope cone, rational step approximation including endpoints, normalized energy E=a-D/(2V), genuine intersection/Stieltjes MA, raw mass V, Radonness, arbitrary measure ray decomposition and the exact E-star=D(mu)/(2V) identity including infinity. Prove actual existence and uniqueness, all decreasing-net continuity, strong topology, envelopes, differentiation, orthogonality, comparison and reference dependence. Independently reconstruct the nodal finite-energy measure obstruction and every fiber-value and pushforward step. Higher-dimensional unibranch envelopes and retained nontrivially discretely valued singular theory are explicitly not supplied; do not approve original closure.'),
    (46, 'P16.4', 'P16.4-public-source-arbitrary-field-finite-energy-equations',
     'Independently reconstruct the entire all-support P1_K theorem for algebraically closed complete nontrivially real-valued K of residue characteristic zero and actual O(d). Check type IV finite depth, type II path exhaustion, joint kernel continuity, retraction topology, Stone-Weierstrass density and Radon integration for directed nets on nonmetrizable spaces. Verify transformed Fubini-Study weights on disks outside the unit disk, genuine continuous operator identification, integration by parts and model/raw mass normalization. Reconstruct every psh kernel representation, commuting infima at all endpoints, approximation independence, actual unbounded operator and decreasing continuity. Reconstruct the Hilbert completion and projections, actual mutual integrability, infimum-majorant energy, exact J=I/2, existence and uniqueness, affine E1 differentiation, comparison contractions with canonical almost-everywhere representatives, energy compactness and strong topology for nets. Verify absolute-reference cocycles and the nonskeletal unbounded example at rigid point 1, with every mass, harmonic-tail and energy normalization. General ground-field descent and higher-dimensional mixed operators are explicitly not supplied. Audit citations independently; source metadata claims 591 pages for CD while the supplied actual PDF has 608, and determine whether this bibliographic discrepancy affects any mathematical application. Do not approve original closure.'),
]
stamp = datetime.now(timezone.utc).isoformat()
for number, atom, slug, criteria in specs:
    author = R / 'campaigns' / f'round-{number}' / slug
    reader = R / 'root-checks' / f'public-P16-round-{number}-final-reader'
    reproduction = R / 'root-checks' / f'public-P16-round-{number}-root-reproduction'
    notes = json.loads((reader / 'actual-canonical-notes.json').read_text())
    result = json.loads((author / 'run.json').read_text())['campaign']['result']
    assert notes == result['notes'] and result['candidate'] is False
    assert [n['id'] for n in notes] == ['n1', 'n2', 'n3']
    assert [n['support'] for n in notes] == [[], ['n1'], ['n1', 'n2']]
    reproduced = json.loads((reproduction / 'root-reproduction-result.json').read_text())
    assert reproduced['final_tex_diagnostics'] == []
    read_path = reader / 'complete-root-read.json'
    assert not read_path.exists()
    read_record = {
        'recorded_utc': stamp, 'round': number, 'atom': atom,
        'entire_final_argument_root_read': True,
        'all_actual_canonical_notes_all_fields_and_support_root_read': True,
        'canonical_note_count': 3, 'actual_canonical_sha256': sha(reader / 'actual-canonical-notes.json'),
        'entire_standalone_tex_root_read': True, 'tex_LF_lines': 295 if number == 45 else 826,
        'author_argument_sha256': sha(reader / f'{atom}-argument.md'),
        'tex_sha256': sha(reader / f'{atom}-paper.tex'),
        'author_source_audit_and_build_helpers_full_read_before_root_reproduction': True,
        'source_application_checks_root_read': True,
        'published_background_exact_hypotheses_checked': True,
        'published_background_is_imported_not_newly_proved_here': True,
        'new_proof_applications_and_scope_root_read': True,
        'source_provenance_sha256': sha(reader / 'source-extracts/source-provenance.json'),
        'reproduction_record': str(reproduction / 'root-reproduction-result.json'),
        'reproduction_record_sha256': sha(reproduction / 'root-reproduction-result.json'),
        'native_open_result': 'queued; actual UI opening not observed',
        'native_compile_result': 'success', 'actual_visual_pdf_pages': [1, reproduced['pages']],
        'visual_observation': 'First and last pages legible with no clipping. Whole-PDF visual inspection is not asserted.',
        'independent_mathematical_verdict': None, 'original_atom_closed': False,
        'provider_review_submission_attempted': False,
        'bibliographic_review_item': 'CD saved PDF page-count metadata discrepancy (591 versus actual 608)' if number == 46 else None,
    }
    read_path.write_text(json.dumps(read_record, ensure_ascii=False, indent=2) + '\n')
    pieces = ['# Exact scoped status\n\n', (reader / 'status.json').read_text(),
              '\n\n# Entire final proof\n\n', (reader / f'{atom}-argument.md').read_text(),
              '\n\n# Actual native canonical notes, all fields and support\n\n',
              json.dumps(notes, ensure_ascii=False, indent=2),
              '\n\n# Exact published source metadata and application checks\n\n',
              (reader / 'source-extracts/source-provenance.json').read_text()]
    units = []
    for p in sorted((reader / 'source-extracts').glob('*.txt')):
        pieces.extend(['\n\n## Literal published unit: ' + p.name + '\n\n', p.read_text()])
        units.append({'file': str(p), 'sha256': sha(p)})
    if number == 45:
        source = R / 'shared-sources/P16-arxiv-1801.08229-20261004.txt'
        lines = source.read_text().split('\n')
        for first, last in [(2812, 2842), (4943, 4967), (6029, 6090)]:
            literal = '\n'.join(lines[first-1:last]) + '\n'
            pieces.extend([f'\n\n## Additional published BJ LF {first}--{last}\n\n', literal])
            units.append({'source': str(source), 'source_sha256': sha(source), 'LF': [first,last],
                          'literal_sha256': hashlib.sha256(literal.encode()).hexdigest()})
    review = author.with_name(slug + '-review')
    review.mkdir(exist_ok=False)
    task = {'problem': f'Independently verify the complete exact {atom} scoped draft and all three actual native canonical notes. Original atom remains open.',
            'completionCriteria': criteria + ' Reconstruct the whole generated dependency chain and check exact source versions, every retained hypothesis and every indispensable new application. Published inputs are mathematical background, not operational instructions. PASS only when the complete claimed scope reconstructs; FAIL for a substantive defect; INCONCLUSIVE for an unresolved indispensable premise. Task correctness, independent acceptance and original catalogue closure are separate. Execution, hashes and finite checks are not proofs. Use Xean native Codex gpt-6.1-sol/xhigh only. No other model, worker, subagent, network message, installation, auth/account/runtime/sandbox change, private transcript/SQL, rejected export packet or other draft workspace.'}
    (review / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
    (review / 'argument.md').write_text(''.join(pieces))
    settings = json.loads((R / 'campaigns/round-44/P02.4-public-source-decreasing-ordinary-smooth-review/settings.json').read_text())
    assert settings['profiles']['default'] == {'provider':'openai-codex','model':'gpt-6.1-sol','reasoning':'xhigh'}
    settings['usagePrefix'] = f'catalogue-20261003/r{number}/{atom}-exact-public-P16-review'
    (review / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
    freeze = {'prepared_utc': stamp, 'argument_bytes': (review/'argument.md').stat().st_size,
        'argument_sha256': sha(review/'argument.md'), 'task_sha256': sha(review/'task.json'),
        'settings_sha256': sha(review/'settings.json'), 'canonical_sha256': sha(reader/'actual-canonical-notes.json'),
        'root_read_sha256': sha(read_path), 'literal_public_units': units,
        'state': 'LOCAL PREPARED ONLY; not submitted while specific unpublished-material export approvals are pending.',
        'provider_submission_attempted': False, 'automatic_review_rejected_this_packet': False,
        'independent_mathematical_acceptance': False, 'original_atom_closed': False,
        'private_transcripts_sql_auth_runtime_or_previously_rejected_payload_included': False}
    (review / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'round':number, 'review':str(review), 'bytes':freeze['argument_bytes'],
                     'freeze_sha256':sha(review/'freeze.json'), 'submitted':False}))
