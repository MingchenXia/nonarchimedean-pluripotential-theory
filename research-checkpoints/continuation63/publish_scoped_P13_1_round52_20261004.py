"""Publish the exactly reviewed partial Reeb comparison, preserving frozen inputs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess
import unicodedata

R = Path('/workspace/research')
C = R / 'campaigns/round-52/P13.1-public-source-new-unibranch-envelope-Reeb-calculus-review'
A = R / 'root-checks/public-P13.1-round-52-final-reader'
D = R / 'deliverables/scoped-P13.1-round52'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
result = json.loads((C / 'run.json').read_text())['campaign']['result']
assert result['verdict'] == 'PASS'
assert result['operationId'] == '540a829c-ca07-476f-a96c-eed24d9a0fa3'
assert len(result['premises']) == 9 and len(result['passages']) == 11
freeze = json.loads((C / 'freeze.json').read_text())
assert sha(C / 'argument.md') == freeze['argument_sha256']
assert sha(A / 'P13.1-argument.md') == freeze['author_argument_sha256']
assert sha(A / 'canonical-result.json') == freeze['canonical_result_sha256']
assert not D.exists()
D.mkdir()
norm = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s)).strip()
coverage = {i: [] for i in range(9)}
checks = []
annex = ['# P13.1 round52 exact review and source checks', '',
         'The entire actual correctness report, nine premises and eleven passages were read. '
         'PASS covers the retained partial proof and its four canonical notes, including the '
         'expressly conditional implication under (Env). It does not establish (Env), '
         'cross-Reeb E1 preservation or uniform energy differentiation. Original P13.1 remains open.', '',
         'Publication adds only the review\'s harmless clarifications: rational then real '
         'coefficient approximation, the centered-obstacle scope of transported envelope estimates, '
         'and the supporting-affine-function argument in the source typo.', '']
for i, p in enumerate(result['passages']):
    assert p['id'] == result['operationId'] + '/' + str(i)
    assert p['statement'] == result['premises'][p['premise']]
    coverage[p['premise']].append(i)
    source = next(s for s in freeze['full_primary_files_available_readonly'] if s['public_source'] == p['url'])
    path = Path(source['literal_extract'])
    assert sha(path) == source['extract_sha256']
    matched = norm(p['quote']) in norm(path.read_text())
    assert matched == (i != 7)
    item = {'passage': i, 'premise': p['premise'], 'source': str(path),
            'source_sha256': sha(path), 'normalized_literal_match': matched}
    if not matched:
        literal = '\n'.join(path.read_text().split('\n')[2421:2443])
        assert 'closure of Hdom (ω)' in literal
        item.update({'primary_LF': [2422, 2443], 'root_read': True,
                     'difference': 'The source extraction inserts whitespace before the argument of Hdom.'})
        annex.extend(['## Passage 7', '', p['quote'], '', item['difference'], '',
                      'Primary one-based LF 2422--2443:', '', '```text', literal, '```', ''])
    checks.append(item)
assert all(coverage.values())
review = D / 'P13.1-correctness-review.json'
review.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
assert sha(review) == sha(R / 'root-checks/P13.1-round52-actual-correctness-review.json')
for name in ['P13.1-argument.md', 'canonical-result.json', 'complete-root-read.json',
             'input-original.json', 'input.json', 'task-original.json', 'assignment-original.txt',
             'reproduce.py', 'audit_sources.py', 'check_partial_results.py', 'environment.json']:
    shutil.copyfile(A / name, D / name)
shutil.copytree(A / 'source-extracts', D / 'source-extracts')
(D / 'P13.1-source-review-annex.md').write_text('\n'.join(annex))
tex = (A / 'P13.1-paper.tex').read_text()
replacements = {
    r'\author{Draft implementation for unchanged P13.1}': r'\author{Reviewed partial results for unchanged P13.1}',
    'Computations, hashes, and successful compilation do not verify the mathematical arguments.':
        'The complete retained proof and all four canonical notes received an independent source-aware computational correctness review with verdict PASS on 4 October 2026. The accompanying report is not a formal proof certificate or a priority claim. Its conditional envelope result does not establish the envelope premise.',
    'Same-ray CPSH sums have the harmonic-sum polarization: for rational fields take common homogeneous degrees and multiply FS lists; for irrational fields rationally approximate using the uniform orbit bounds and then use diagonal approximation.':
        'Same-ray CPSH sums have the harmonic-sum polarization. At a rational Reeb field, common-degree products first give this assertion for rational degree and coefficient ratios. Approximate real coefficients uniformly on the compact carrier and use CPSH closedness. For irrational fields, rationally approximate the field, use the uniform orbit bounds and root transport, and then use diagonal approximation.',
    'Only the input and the five explicitly supplied public caches were read.':
        'The author proof uses the input and the five explicitly supplied public caches. The exact independent review, its nine premises and eleven passages, and the root primary quotation checks accompany this reviewed edition.',
}
for old, new in replacements.items():
    assert tex.count(old) == 1, old
    tex = tex.replace(old, new)
marker = 'At a fixed field monotonicity and constants give the usual 1-Lipschitz obstacle bound.'
assert tex.count(marker) == 1
clarification = r'''The transported $3\kappa M$ estimate above uses the centered obstacle.
For arbitrary $h$, set $c=\sup_S h$; its precise form is
\[
 \|C_{\zeta,\xi}(P_\zeta(h-c))+c-P_\xi h\|_\infty
 \leq 3\kappa\osc_S h.
\]
The first, direct envelope comparison holds for arbitrary $h$ because fixed-field
envelopes commute with constants. Raw root transport does not commute with constants.
'''
tex = tex.replace(marker, clarification + '\n' + marker)
marker = 'Lemma 6.6 imports APW26b Proposition 5.7 and Lemma 5.11.'
assert tex.count(marker) == 1
tex = tex.replace(marker, marker + '\n' + r'The strict supporting inequality in that lemma must evaluate the supporting affine function at the comparison point, $l(t^{\prime})$, rather than at the fixed contact point, $l(t)$. This harmless source correction does not establish the imported dependencies.')
(D / 'P13.1-paper.tex').write_text(tex)
build = D / 'build'
build.mkdir()
codes = []
for i in [1, 2]:
    proc = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                           '-output-directory=' + str(build), str(D / 'P13.1-paper.tex')], cwd=D, capture_output=True)
    (build / ('pass' + str(i) + '.stdout.txt')).write_bytes(proc.stdout)
    (build / ('pass' + str(i) + '.stderr.txt')).write_bytes(proc.stderr)
    codes.append(proc.returncode)
    if (build / 'P13.1-paper.log').exists():
        shutil.copyfile(build / 'P13.1-paper.log', build / ('pass' + str(i) + '.tex.log'))
    assert proc.returncode == 0, proc.stdout[-2500:]
shutil.copyfile(build / 'P13.1-paper.pdf', D / 'P13.1-paper.pdf')
info = subprocess.run(['pdfinfo', str(D / 'P13.1-paper.pdf')], capture_output=True, text=True, check=True).stdout
(D / 'pdfinfo.txt').write_text(info)
record = {
    'published_utc': datetime.now(timezone.utc).isoformat(), 'atom': 'P13.1', 'round': 52,
    'scope': 'Genuine all-Reeb PSH root order comparison, fixed-carrier density and quantitative nonnegative cumulative S comparison; rational quotient and all-Reeb bounded-obstacle envelope calculus conditional on explicit Env.',
    'independently_reviewed_partial_theorem': True, 'fully_solved_original_atom': False,
    'original_remaining_gaps': ['Unconditional Env in the retained proof', 'Cross-Reeb genuine E1 preservation', 'Moving mixed-measure tail control', 'Uniform genuine cone energy differentiation'],
    'review': str(review), 'review_sha256': sha(review), 'verdict': 'PASS',
    'operation_id': result['operationId'], 'reported_utc': result['reportedAt'],
    'entire_report_premises_and_passages_root_read': True, 'premises': 9, 'passages': 11,
    'exact_zero_based_binding_coverage': coverage, 'primary_quote_checks': checks,
    'harmless_corrections': ['Rational-to-real coefficient approximation', 'Centered transported obstacle with restored additive constant', 'Source supporting inequality evaluates l at t-prime'],
    'original_author_tex': str(A / 'P13.1-paper.tex'), 'original_author_tex_sha256': sha(A / 'P13.1-paper.tex'),
    'source': str(D / 'P13.1-paper.tex'), 'source_sha256': sha(D / 'P13.1-paper.tex'),
    'pdf': str(D / 'P13.1-paper.pdf'), 'pdf_sha256': sha(D / 'P13.1-paper.pdf'),
    'pages': int(re.search(r'Pages:\s*(\d+)', info).group(1)),
    'local_two_pass_return_codes': codes, 'native_compile': 'Not yet checked; no native success asserted.',
    'review_limit': 'Independent source-aware computational review by the user-selected native model; not a formal proof certificate or novelty certification.',
}
(D / 'publication-preparation.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: record[k] for k in ['verdict', 'review_sha256', 'source_sha256', 'pdf_sha256', 'pages', 'fully_solved_original_atom']}, indent=2))
