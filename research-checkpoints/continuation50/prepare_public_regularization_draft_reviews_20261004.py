from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
for n, atom, stem in [(41, 'P02.1', 'P02.1-public-source-decreasing-real-PL'),
                      (42, 'P02.2', 'P02.2-public-source-decreasing-LFS')]:
    author = R / 'campaigns' / f'round-{n}' / stem
    reader = R / 'root-checks' / f'public-regularization-round-{n}-final-reader'
    read = json.loads((reader / 'complete-root-read.json').read_text())
    assert read['entire_preliminary_argument_root_read'] and read['entire_final_argument_diff_root_read']
    assert read['all_actual_canonical_notes_all_fields_and_support_root_read']
    result = json.loads((author / 'run.json').read_text())['campaign']['result']
    notes = json.loads((reader / 'actual-canonical-notes.json').read_text())
    assert result['notes'] == notes and result['candidate'] is False
    proof = reader / f'{atom}-argument.md'
    assert proof.read_bytes() == (Path(result['workspace']) / proof.name).read_bytes()
    criteria = (
        'Reconstruct the entire one-sided strict approximation lemma over every stated complete nontrivially valued field: compact Thuillier-lisse semistable representation, finite separable and Galois base changes, skeleton retractions and edge weights, convex chord majorization and vertex positivity, actual value-group cuts in dense or discrete groups, separable roots including mixed characteristic, strict star/interval Cartier-model realization with real coefficients, all omitted directions, continuous Galois quotient descent, finite-flat divisible-coefficient strict descent, and the exact scalar relative-boundary identity. Check arbitrary extended-real targets, component finiteness, the entire interpolation net and countable extraction, explicit interstage shifts on one fixed domain, and optional compact uniform convergence. Verify compact projective-fibre constancy for all analytic fibre points, analytic sections, actual psh descent, termwise transition-chart agreement and every analytic scalar extension. Check the F_sigma and retraction necessity statements and distinguish counterexamples to shortcuts from actual failure examples. A saturated/global-function theorem must not be silently changed into a theorem for every nonsaturated germ.'
        if n == 41 else
        'Reconstruct the type-2-only harmonic interpolation net on one fixed strict affinoid domain, finite refinements over the actual ground field, global strict real-PL star realization, weighted Dirichlet uniqueness, harmonic/subharmonic comparison, and convergence at type 2, type 3, rigid poles and type 4. Check that one fixed initial skeleton contains all positive-genus residue points, that one bounded nonnegative Dirichlet perturbation has positive residue degree at precisely the required vertices, and that every perturbed function is actually LFS everywhere on the same ordinary open set. Reconstruct the rational-simplex positive-degree real Picard semiampleness proof, germ reductions at interior and other point types, arbitrary targets, countable extraction and monotonicity. Verify every stated proper algebraic factor, actual fibres, geometric/analytic connectedness via the exact degree-zero torsion comparison, sections, saturated descent, overlaps and all analytic scalar extensions. Independently reconstruct the boundary spike as an arbitrary-class classical psh target, the ordinary-neighborhood finite-residue-branch property, no continuous sequence for uncountable residue, every explicit countable-residue LFS formula, value-group legality, decreasing convergence and the general net. Distinguish the sharp condition for this one target from a sharp original classification. No claim for arbitrary nonsaturated germs or nonclosed-field construction is made.'
    )
    task = {'problem': 'Independently verify this exact completed ' + atom + ' draft and every actual native canonical note, using the supplied literal published sources. This packet is prepared locally only. The original characterization remains open.',
            'completionCriteria': criteria + ' Check exact source hypotheses, versions and every indispensable new application. PASS only if the entire claimed scope is correct; FAIL for a substantive defect; INCONCLUSIVE for an unresolved indispensable premise. Proof acceptance and original-task closure are separate. Builds, source hashes and finite diagnostics do not certify mathematics. Use Xean native Codex gpt-6.1-sol/xhigh. No other model, worker or subagent, external messages, installations, runtime/account/auth changes, private transcripts/SQL, other draft workspaces or blocked export payloads.'}
    prov = json.loads((reader / 'source-extracts/source-provenance.json').read_text())
    pieces = ['# Exact final status\n\n', (reader / 'status.json').read_text(),
              '\n\n# Entire final proof\n\n', proof.read_text(),
              '\n\n# Every actual native canonical note\n\n', json.dumps(notes, ensure_ascii=False, indent=2),
              '\n\n# Published source versions and application checks\n\n', json.dumps(prov, ensure_ascii=False, indent=2)]
    units = []
    for source in prov['sources']:
        if n == 41:
            raw = Path(source['source_literal_extract']).read_bytes().split(b'\x0c')
            for unit in source['literal_page_files']:
                path = reader / 'source-extracts' / unit['literal_file']
                data = path.read_bytes()
                assert data == raw[unit['original_pdf_page'] - 1]
                assert sha(path) == unit['literal_sha256']
                pieces += ['\n\n## ' + source['id'] + ' cache page ' + str(unit['original_pdf_page']) + '\n\n', data.decode()]
                units.append({'source': source['id'], 'page': unit['original_pdf_page'], 'file': str(path), 'sha256': sha(path)})
        else:
            raw = Path(source['literal_extract']).read_bytes()
            for unit in source['literal_excerpts']:
                assert raw[unit['byte_start']:unit['byte_end']].decode() == unit['literal_text']
                units.append({'source': source['id'], 'label': unit['label'], 'byte_start': unit['byte_start'], 'byte_end': unit['byte_end'], 'embedded_in_provenance': True})
            for page in source['actual_pdf_pages']:
                path = reader / 'source-extracts' / f"{source['id']}-pdf-page-{page:03}.txt"
                pieces += ['\n\n## ' + source['id'] + ' actual PDF page ' + str(page) + '\n\n', path.read_text()]
                units.append({'source': source['id'], 'page': page, 'file': str(path), 'sha256': sha(path)})
    review = author.with_name(stem + '-review')
    review.mkdir(exist_ok=False)
    (review / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
    (review / 'argument.md').write_text(''.join(pieces))
    settings = json.loads((R / 'campaigns/round-36/P03.3-original-envelope-continuity-review/settings.json').read_text())
    assert settings['profiles']['default'] == {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
    settings['usagePrefix'] = f'catalogue-20261003/r{n}/{atom}-exact-public-regularization-review'
    (review / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
    freeze = {'prepared_utc': datetime.now(timezone.utc).isoformat(),
              'argument_sha256': sha(review / 'argument.md'), 'argument_bytes': (review / 'argument.md').stat().st_size,
              'task_sha256': sha(review / 'task.json'), 'settings_sha256': sha(review / 'settings.json'),
              'author_argument_sha256': sha(proof), 'actual_canonical_notes_sha256': sha(reader / 'actual-canonical-notes.json'),
              'root_read_record_sha256': sha(reader / 'complete-root-read.json'), 'literal_published_units': units,
              'earlier_blocked_review_payload_included': False, 'private_transcripts_sql_auth_included': False,
              'provider_submission_attempted': False, 'automatic_review_rejected_this_new_packet': False,
              'state': 'Prepared locally only; not submitted while specific generated-material export approvals remain pending.',
              'original_atom_solved': False}
    (review / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'round': n, 'directory': str(review), 'argument_bytes': freeze['argument_bytes'],
                      'freeze_sha256': sha(review / 'freeze.json'), 'provider_submission_attempted': False}))
