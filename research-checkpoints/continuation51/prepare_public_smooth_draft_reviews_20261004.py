from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
for number, atom, slug in [(43, 'P02.3', 'P02.3-public-source-decreasing-weakly-smooth'),
                           (44, 'P02.4', 'P02.4-public-source-decreasing-ordinary-smooth')]:
    author = R / 'campaigns' / f'round-{number}' / slug
    reader = R / 'root-checks' / f'public-smooth-round-{number}-final-reader'
    read = json.loads((reader / 'complete-root-read.json').read_text())
    assert read['entire_final_argument_root_read'] and read['all_actual_canonical_notes_all_fields_and_support_root_read']
    result = json.loads((author / 'run.json').read_text())['campaign']['result']
    notes = json.loads((reader / 'actual-canonical-notes.json').read_text())
    assert result['notes'] == notes and result['candidate'] is False
    criteria = (
        'Reconstruct arbitrary-target countable extraction over countably dense fields and its affinoid topology proof. Check the exact GJR weakly smooth net premise, finite Galois smoothing and descent, harmonic integer coordinates, classical positivity, positive curvature forms and strong currents, scalar pullbacks, and current conventions. Reconstruct reduced boundaryless curve normalization over perfect fields, finite branch separation at possibly non-rational rigid points, one fixed compact preimage, local constancy, and compact domination. Check the entire inductive synchronization separately for finite and minus-infinity node values, identically minus-infinity branches, quantitative gaps, actual constant neighborhoods downstairs, finite classical descent and every scalar extension. Verify the saturated proper connected-fiber theorem, sections, completed residue-field fibers, absolute boundary and purity, singular fibers and concrete examples. Reconstruct the ANY-field Gauss spike, residue-class neighborhood lemma, sequence obstruction, irreducible residue-polynomial lifts, Bezout argument, smooth concave cutoff, every point and every scalar limit. Distinguish net versus sequence failures. Inspect the core current proof: ambient tropical dimension can exceed analytic dimension. The supplied root clarification is an unaccepted diagnostic, not a premise; independently decide whether the exact claimed scope reconstructs or requires a fresh addendum.'
        if number == 43 else
        'Reconstruct arbitrary extended-real classical curve targets, second-countable affinoid topology and countable extraction without continuity or cofinality assumptions. Verify every exact Wanner field, proper curve and harmonic-smoothness condition, application of finite-lisse Lemma 5.2 to one fixed strict affinoid Y, and the interstage gap yielding one ordinary smooth sequence. Check ordinary charts and positive-form representatives, general analytic pullbacks and scalar extensions without assuming an ambient Hessian is globally positive. Reconstruct finite geometrically unibranch normalization, one rigid preimage, closed bijection and common domain, termwise constant neighborhoods, actual smooth descent, forms and classical positivity. Verify saturated projective products over completed residue fields, proper-fiber maximum principle and rational-section descent. Independently reconstruct the Gauss spike as classical psh, whole-residue-disc neighborhood property, uncountable-residue obstruction to ANY continuous sequence, smooth convex polynomial cutoff for countable residue, zeros, every point, monotonicity, scalar extensions and correct distinction between pullback spike and new Gauss singleton. Check the exact Picard quotient and torsion argument; harmonic nonsmoothness is not an approximation obstruction.'
    )
    task = {'problem': f'Independently verify the exact completed {atom} scoped draft and all four actual native canonical notes. Locally prepared only; no original characterization is marked solved.',
            'completionCriteria': criteria + ' Verify precise source hypotheses, versions and all indispensable new applications. Saturated-domain results do not imply a theorem for every nonsaturated sheaf germ. PASS only if the complete claimed scope reconstructs; FAIL for a substantive defect; INCONCLUSIVE for an unresolved indispensable premise. Correctness acceptance and original-task closure are separate. Source hashes, builds and finite diagnostics are not proof. Use Xean native Codex gpt-6.1-sol/xhigh only. No other worker/model/subagent, network messages, installations, auth/account/runtime changes, private transcripts/SQL, earlier blocked payloads or other draft workspaces.'}
    prov = json.loads((reader / 'source-extracts/source-provenance.json').read_text())
    pieces = ['# Exact scoped status\n\n', (reader / 'status.json').read_text(),
              '\n\n# Entire final proof\n\n', (reader / f'{atom}-argument.md').read_text(),
              '\n\n# All actual native canonical fields and support\n\n', json.dumps(notes, ensure_ascii=False, indent=2),
              '\n\n# Published source versions and application checks\n\n', json.dumps(prov, ensure_ascii=False, indent=2)]
    units = []
    for source in prov['sources']:
        if number == 43:
            original_pages = Path(source['literal_extract']).read_bytes().split(b'\x0c')
            path = reader / source['selected_literal_file']
            expected = b'\x0c'.join(original_pages[p-1] for p in source['selected_pdf_pages_1_based'])
            assert expected == path.read_bytes() and sha(path) == source['selected_literal_sha256']
            pieces += ['\n\n## ' + source['public_source'] + ' selected literal PDF-cache pages\n\n', path.read_bytes().decode()]
            units.append({'source': source['public_source'], 'pages': source['selected_pdf_pages_1_based'], 'file': str(path), 'sha256': sha(path)})
        else:
            raw = Path(source['literal_extract']).read_bytes().split(b'\n')
            for unit in source['selected_literal_extracts']:
                path = reader / unit['file']
                expected = b'\n'.join(raw[unit['first_line']-1:unit['last_line']]) + b'\n'
                assert expected == path.read_bytes() and sha(path) == unit['sha256']
                pieces += ['\n\n## ' + source['public_source'] + ' ' + str(unit['first_line']) + '--' + str(unit['last_line']) + '\n\n', path.read_bytes().decode()]
                units.append({'source': source['public_source'], 'LF': [unit['first_line'], unit['last_line']], 'file': str(path), 'sha256': sha(path)})
    clarification = None
    if number == 43:
        clarification = R / 'root-checks/P02.3-round43-current-positivity-clarification-20261004.md'
        pieces += ['\n\n# Unaccepted root diagnostic; independently assess, not a proof premise\n\n', clarification.read_text()]
    review = author.with_name(slug + '-review')
    assert not review.exists()
    review.mkdir()
    (review / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
    (review / 'argument.md').write_text(''.join(pieces))
    settings = json.loads((R / 'campaigns/round-42/P02.2-public-source-decreasing-LFS-review/settings.json').read_text())
    assert settings['profiles']['default'] == {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
    settings['usagePrefix'] = f'catalogue-20261003/r{number}/{atom}-exact-public-smooth-review'
    (review / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
    freeze = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'argument_bytes': (review / 'argument.md').stat().st_size,
              'argument_sha256': sha(review / 'argument.md'), 'task_sha256': sha(review / 'task.json'),
              'settings_sha256': sha(review / 'settings.json'), 'author_argument_sha256': sha(reader / f'{atom}-argument.md'),
              'actual_canonical_sha256': sha(reader / 'actual-canonical-notes.json'),
              'root_read_sha256': sha(reader / 'complete-root-read.json'), 'literal_published_units': units,
              'root_clarification_sha256': sha(clarification) if clarification else None,
              'provider_submission_attempted': False, 'automatic_review_rejected_this_packet': False,
              'blocked_payload_or_private_transcripts_sql_auth_included': False,
              'state': 'LOCAL PREPARED ONLY. Never submitted while specific generated-material export approvals are pending.',
              'independent_acceptance': False, 'original_atom_closed': False}
    (review / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'round': number, 'review': str(review), 'bytes': freeze['argument_bytes'],
                      'freeze_sha256': sha(review / 'freeze.json'), 'submitted': False}))
