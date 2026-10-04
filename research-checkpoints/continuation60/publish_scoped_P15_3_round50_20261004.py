"""Publish the reviewed divisorial partial result; original P15.3 stays open."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess
import unicodedata

R = Path('/workspace/research')
C = R / 'campaigns/round-50/P15.3-public-source-zero-volume-P-sensitive-bodies-review'
A = R / 'root-checks/public-P15.3-round-50-final-reader-v2'
D = R / 'deliverables/scoped-P15.3-round50'
D.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
result = json.loads((C / 'run.json').read_text())['campaign']['result']
assert result['verdict'] == 'PASS'
assert result['operationId'] == '3804277b-4e6d-4dd4-8eea-1a0f72abc1dc'
assert len(result['premises']) == 11 and len(result['passages']) == 18
freeze = json.loads((C / 'freeze.json').read_text())
assert sha(C / 'argument.md') == freeze['argument_sha256']
assert sha(A / 'P15.3-argument.md') == freeze['author_argument_sha256']
assert sha(A / 'canonical-result.json') == freeze['canonical_result_sha256']
files = {
    '2309.07584': 'P15.3-arxiv-2309.07584v3-20261004.txt',
    '2112.04290': 'P15.3-arxiv-2112.04290v2-20261004.txt',
    '1210.5692': 'P15.3-arxiv-1210.5692v1-20261004.txt',
    '1508.03922': 'P15.3-arxiv-1508.03922v5-20261004.txt',
    '0812.3674': 'BEGZ-0812.3674v2-20261004.txt',
}
norm = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s)).strip()
nonmatches = {
    1: ('2309.07584', 1389, 1415, 'The factorial is extracted on a separate line in the fraction.'),
    7: ('1210.5692', 172, 184, 'OCR extracts the subset sign as a different glyph.'),
    9: ('2112.04290', 70, 85, 'Extracted section-space expression has parentheses whitespace and a trailing nonzero superscript.'),
    10: ('2112.04290', 476, 494, 'Displayed fraction, integral and subscripts are extracted across separate lines.'),
}
coverage = {i: [] for i in range(11)}
checks = []
annex = ['# P15.3 round50 actual correctness review and primary checks', '',
         'The entire actual report, eleven premises and eighteen passages were read. '
         'Every zero-based premise binding and passage ID was checked. PASS covers '
         'the retained partial proof and all four canonical notes. Original P15.3 remains open.', '']
for i, p in enumerate(result['passages']):
    assert p['id'] == result['operationId'] + '/' + str(i)
    assert p['statement'] == result['premises'][p['premise']]
    coverage[p['premise']].append(i)
    source = C / 'task.json' if p['url'] == 'urn:xean:task' else R / 'shared-sources' / next(v for k, v in files.items() if k in p['url'])
    matched = norm(p['quote']) in norm(source.read_text())
    assert matched == (i not in nonmatches)
    item = {'passage': i, 'premise': p['premise'], 'source': str(source),
            'source_sha256': sha(source), 'normalized_literal_match': matched}
    if not matched:
        key, start, end, explanation = nonmatches[i]
        literal = '\n'.join(source.read_text().split('\n')[start-1:end])
        item.update({'primary_LF': [start, end], 'root_read': True, 'difference': explanation})
        annex.extend(['## Passage ' + str(i), '', p['quote'], '', explanation, '',
                      'Primary LF ' + str(start) + '--' + str(end) + ':', '', '```text', literal, '```', ''])
    checks.append(item)
assert all(coverage.values())
for key, start, end, application in [
    ('0812.3674', 175, 278, 'Bedford–Taylor plurifine locality, bounded truncations and trivial extension for small unbounded locus. Here the smooth residual wedges have finite mass and extend across the divisor without charging it.'),
    ('1210.5692', 666, 825, 'The complete Lemma4.1 statement and proof were read. Very-general smooth hypersurface restrictions concern projective line-bundle data, not the transcendental product example. Only this source-scope distinction is used.'),
    ('2112.04290', 1824, 1840, 'The open Chebyshev choice is the more-singular Kähler-current potential eta, under positive I-envelope mass; it is not a choice of auxiliary positive form.'),
]:
    source = R / 'shared-sources' / files[key]
    literal = '\n'.join(source.read_text().split('\n')[start-1:end])
    annex.extend(['## Additional primary application: ' + key, '', application, '',
                  'Source LF ' + str(start) + '--' + str(end) + '; SHA256 ' + sha(source), '',
                  '```text', literal, '```', ''])
review = D / 'P15.3-correctness-review.json'
review.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
assert sha(review) == sha(R / 'root-checks/P15.3-round50-actual-correctness-review.json')
for name in ['P15.3-argument.md', 'canonical-result.json', 'complete-root-read.json']:
    shutil.copyfile(A / name, D / name)
shutil.copyfile(A / 'source-extracts/source-provenance.json', D / 'author-source-provenance.json')
(D / 'P15.3-source-review-annex.md').write_text('\n'.join(annex))
tex = (A / 'P15.3-paper.tex').read_text()
replacements = {
    r'\author{Unverified draft for original P15.3}': r'\author{Reviewed partial results for original P15.3}',
    'Thus unchanged original P15.3 remains open in this draft. Execution, compilation, and hashes are not mathematical verification.': 'Unchanged original P15.3 remains open. The complete retained argument and all four canonical notes received an independent source-aware computational correctness review with verdict PASS on 4 October 2026. The report accompanies this paper; it is not a formal proof certificate or a priority claim.',
    'The only mathematical sources read are the four supplied primary caches:': 'The author argument uses the four supplied primary caches:',
    'The sandwich proves convergence along these positive paths to (2.2).': r'The sandwich proves convergence of the residual bodies to $\Delta_Y([\beta])$. After translation by $\nu_Y([D])$, it proves convergence of the partial bodies to (2.1), equivalently (2.2).',
    'No exhaustive numerical experiment or independent mathematical review is claimed.': 'The frozen author artifacts remain unchanged. The exact independent correctness report, its eleven premises and eighteen passages, and the primary application checks are preserved with this reviewed edition. Local TeX builds check presentation only.',
    r'\begin{thebibliography}{4}': r'\begin{thebibliography}{5}',
}
for old, new in replacements.items():
    assert tex.count(old) == 1, old
    tex = tex.replace(old, new)
marker = "Cao Definitions 2 and 3,"
assert tex.count(marker) == 1
tex = tex.replace(marker, "Xia's section 6.4 leaves open independence of the Chebyshev transform from the auxiliary more-singular K\\\"ahler-current potential $\\eta$, under positive I-envelope mass. It is not a question about an auxiliary positive form. This distinction does not supply a theorem at zero volume.\n\n" + marker)
marker = r'\section{Divisorial construction and all claimed independence}'
assert tex.count(marker) == 1
tex = tex.replace(marker, r'The review also checks the bounded-truncation and nonpluripolar locality inputs against BEGZ, arXiv:0812.3674v2, section 1.2. Its extra source passages and Cao Lemma 4.1 are reproduced in the accompanying review annex.' + '\n\n' + marker)
marker = r'\end{thebibliography}'
tex = tex.replace(marker, r'\bibitem{B} S. Boucksom, P. Eyssidieux, V. Guedj, A. Zeriahi, \emph{Monge--Amp\`ere equations in big cohomology classes}, arXiv:0812.3674v2, 2009.' + '\n' + marker)
(D / 'P15.3-paper.tex').write_text(tex)
build = D / 'build'
build.mkdir()
codes = []
for i in [1, 2]:
    proc = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                           '-output-directory=' + str(build), str(D / 'P15.3-paper.tex')], cwd=D, capture_output=True)
    (build / ('pass' + str(i) + '.stdout.txt')).write_bytes(proc.stdout)
    (build / ('pass' + str(i) + '.stderr.txt')).write_bytes(proc.stderr)
    codes.append(proc.returncode)
    if (build / 'P15.3-paper.log').exists():
        shutil.copyfile(build / 'P15.3-paper.log', build / ('pass' + str(i) + '.tex.log'))
    assert proc.returncode == 0, proc.stdout[-2500:]
shutil.copyfile(build / 'P15.3-paper.pdf', D / 'P15.3-paper.pdf')
info = subprocess.run(['pdfinfo', str(D / 'P15.3-paper.pdf')], capture_output=True, text=True, check=True).stdout
(D / 'pdfinfo.txt').write_text(info)
record = {
    'published_utc': datetime.now(timezone.utc).isoformat(), 'atom': 'P15.3', 'round': 50,
    'scope': 'Rational smooth-divisor singularities with smooth semipositive remainder; actual partial-body limit, bounded ordinary P-type retention, specified transcendental product with dimension-two mass, and dense-pole obstruction to direct analytic domination.',
    'independently_reviewed_partial_theorem': True, 'fully_solved_original_atom': False,
    'original_remaining_gaps': ['Arbitrary nonanalytic prescribed P-types', 'General numerical dimension and flag hypotheses', 'General modification and carrier/reference-scale claims'],
    'review': str(review), 'review_sha256': sha(review), 'verdict': 'PASS',
    'operation_id': result['operationId'], 'reported_utc': result['reportedAt'],
    'entire_report_premises_and_passages_root_read': True, 'premises': 11, 'passages': 18,
    'exact_zero_based_binding_coverage': coverage, 'primary_quote_checks': checks,
    'harmless_corrections': ['Translate the residual Hausdorff limit by nu(D)', 'Auxiliary Chebyshev choice is a Kähler-current potential eta'],
    'original_author_tex': str(A / 'P15.3-paper.tex'), 'original_author_tex_sha256': sha(A / 'P15.3-paper.tex'),
    'source': str(D / 'P15.3-paper.tex'), 'source_sha256': sha(D / 'P15.3-paper.tex'),
    'pdf': str(D / 'P15.3-paper.pdf'), 'pdf_sha256': sha(D / 'P15.3-paper.pdf'),
    'pages': int(re.search(r'Pages:\s*(\d+)', info).group(1)),
    'local_two_pass_return_codes': codes, 'native_compile': 'Not yet checked; no native success asserted.',
    'review_limit': 'Independent source-aware computational review by the user-selected native model; not a formal proof certificate or novelty certification.',
}
(D / 'publication-preparation.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: record[k] for k in ['verdict', 'review_sha256', 'source_sha256', 'pdf_sha256', 'pages', 'fully_solved_original_atom']}, indent=2))
