"""Freeze one completed geometric theorem and its canonical native notes for review."""
from pathlib import Path
import datetime
import hashlib
import json
import sys

R = Path('/workspace/research')
number = int(sys.argv[1])
assert number in {37, 38}
atom, stem = {
    37: ('P03.1', 'P03.1-public-source-geometric-positivity'),
    38: ('P03.3', 'P03.3-public-source-geometric-continuity'),
}[number]
author = R / 'campaigns' / f'round-{number}' / stem
reader = R / 'root-checks' / f'public-envelope-round-{number}-final-reader'
run = json.loads((author / 'run.json').read_text())
assert run['campaign']['status'] == 'completed' and run['campaign']['error'] is None
result = run['campaign']['result']
assert result['kind'] == 'notes' and result['candidate'] is False
w = Path(result['workspace'])
read = json.loads((reader / 'complete-root-read.json').read_text())
assert read['full_argument_read'] and read['all_actual_canonical_notes_read']
assert json.loads((reader / 'canonical-result.json').read_text()) == result
status = json.loads((w / 'status.json').read_text())
assert set(status) == {'id', 'status', 'exact_result', 'proof_file', 'concrete_gaps'}
assert status['id'] == atom and status['status'] == 'partial'
proof = w / status['proof_file']
assert proof.read_bytes() == (reader / proof.name).read_bytes()
seen = set()
for note in result['notes']:
    assert set(note['support']) <= seen
    seen.add(note['id'])

criteria = {
    38: 'Independently reconstruct the complete rational-affinoid and projective-space theorems and split-node counterexample. Check exact LFS/residue definitions and legal value-group radii; actual finite-tree retractions and density for EVERY continuous obstacle, including nested-disc/type-4 points; graph charge signs, root-kernel realization, signed boundary-unit terms and an ACTUAL globally defined LFS minorant; analytic rational-star, annulus and omitted-disc comparisons bounding EVERY member of the union; uniform obstacle contractivity; every analytic extension via its completed algebraic closure and scalar surjectivity, with no general scalar-openness assumption; actual connected compact boundaryless projective fibres, relative smoothness/open and proper/closed maps, fibre-minimum continuity and exact class descent; the relative-boundary composition equality with its local-separation hypothesis; curve tests; and the exact full-family node computation and its projective-product regularization. No arbitrary-field obstacle, general semistable, closed-polydisc-product or sharp-classification claim may be silently added.',
    37: 'Independently reconstruct the curve-family lemma and exact full semipositive-real-PL family descent for arbitrary smooth geometrically connected projective factors and analytic projective bundles, including factors lacking a rational point. Check perfected scalar/reduction/normalization homeomorphisms, the directed finite-max family anchored at a continuous member, literal local boundedness, absolute boundary extension and all scalar/curve quantifiers. Check degree-zero proper torsion comparison for fibre connectedness; completed residue-field fibres; maximum principles only in their relative interior; finite-extension real-PL and semipositivity descent with divisible coefficients; actual smooth openness, proper closedness, sheaf gluing, fibre INFIMUM for usc obstacles and empty families; normal and cusp-product geometry. Reconstruct ALL split-node, seminormal codimension-two pinching and irreducible nonsplit-node-surface counterexamples, including analytic germ seminormality, strict charts, global obstacle continuity, rational LFS membership, binomial coefficient bounds, the exact minorant estimates on every point, and the scalar curve failure. No general higher-dimensional necessity or sharp classification is claimed.',
}[number]
task = {
    'problem': 'Independently verify only the following exact new geometric partial result for ' + atom + ': ' + status['exact_result'] + '\n\nThe entire final proof, every actual native canonical note and published primary-source passages are supplied directly. This is a correctness/completeness review of the stated geometric theorems and counterexamples. It is not a review of the earlier conditional abstract or toric drafts, and it does not claim closure of the original sharp-classification target.',
    'completionCriteria': criteria + ' Check the original definitions, source versions and EVERY indispensable new source application. Published foundations may be cited with their exact hypotheses, but new applications need complete proofs. Do not use supplied book assertions, prior reviews, source hashes, finite diagnostics or compilation as proof certificates. PASS only if the entire exact scope is correct and completely justified; FAIL for a substantive false statement or proof defect; INCONCLUSIVE for an unresolved indispensable premise. Use Xean native Codex gpt-6.1-sol/xhigh. Do not read private transcripts, SQL, authentication, other generated draft workspaces or any blocked P15/P03.3 review inputs. Do not invoke other models, workers or subagents, change runtime/account/sandbox, install software or send external messages. Original catalogue closure is explicitly separate.'
}

provenance = json.loads((w / 'source-provenance.json').read_text())
pieces = ['# Exact new geometric scope and remaining original obligations\n\n',
          json.dumps(status, ensure_ascii=False, indent=2),
          '\n\n# Entire final proof\n\n', proof.read_text(),
          '\n\n# All actual native canonical notes\n\n', json.dumps(result['notes'], ensure_ascii=False, indent=2),
          '\n\n# Actual published source provenance and hypothesis checks\n\n',
          (w / 'source-provenance.json').read_text()]
source_records = []
for source in provenance['sources']:
    cache = Path(source['literal_extract'])
    pages = cache.read_text().split('\f')
    if number == 38:
        for page in source['selected_full_pages']:
            p = w / page['literal_file']
            text = p.read_text()
            assert text == pages[page['pdf_page'] - 1]
            pieces += ['\n\n## Published source ' + source['id'] + ', PDF page ' + str(page['pdf_page']) + '\n\n', text]
            source_records.append({'source': source['id'], 'pdf_page': page['pdf_page'],
                                   'literal_file': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    else:
        for unit in source['retained_extracts']:
            start, end = unit['pdf_pages']
            p = w / unit['file']
            text = p.read_text()
            assert text == '\f'.join(pages[start - 1:end])
            pieces += ['\n\n## Published source ' + source['id'] + ', PDF pages ' + str(start) + '-' + str(end) + '\n\n', text]
            source_records.append({'source': source['id'], 'pdf_pages': [start, end],
                                   'literal_file': str(p), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
application_file = w / 'source-extracts/checked-applications.md'
if application_file.exists():
    pieces += ['\n\n# Explicit source application checks\n\n', application_file.read_text()]

review = author.with_name(author.name + '-review')
review.mkdir(exist_ok=False)
(review / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
(review / 'argument.md').write_text(''.join(pieces))
settings = json.loads((R / 'campaigns/round-36/P03.3-original-envelope-continuity-review/settings.json').read_text())
settings['usagePrefix'] = f'catalogue-20261003/r{number}/{atom}-exact-geometric-review'
assert settings['profiles']['default'] == {'provider': 'openai-codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
(review / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
freeze = {'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'exact_scope': status['exact_result'], 'original_atom_solved': False,
          'argument_sha256': sha(review / 'argument.md'), 'argument_bytes': (review / 'argument.md').stat().st_size,
          'task_sha256': sha(review / 'task.json'), 'settings_sha256': sha(review / 'settings.json'),
          'author_proof_sha256': sha(proof), 'author_tex_sha256': sha(w / f'{atom}-paper.tex'),
          'canonical_result_sha256': sha(reader / 'canonical-result.json'),
          'root_complete_read_record_sha256': sha(reader / 'complete-root-read.json'),
          'literal_published_primary_pages': source_records,
          'earlier_generated_draft_or_blocked_review_payload_included': False,
          'private_transcripts_sql_auth_included': False,
          'provider_submission_attempted': False}
(review / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'directory': str(review), 'freeze_sha256': sha(review / 'freeze.json'),
                  'argument_bytes': freeze['argument_bytes'], 'primary_units': len(source_records),
                  'original_atom_solved': False}, indent=2))
