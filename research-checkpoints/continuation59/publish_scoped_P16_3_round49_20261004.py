"""Publish the exact reviewed surface result without closing original P16.3."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import subprocess
import unicodedata

R = Path('/workspace/research')
C = R / 'campaigns/round-49/P16.3-public-source-positive-residue-geometric-inputs-review'
A = R / 'root-checks/public-P16-round-49-final-reader'
D = R / 'deliverables/scoped-P16.3-round49'
D.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
result = json.loads((C / 'run.json').read_text())['campaign']['result']
assert result['verdict'] == 'PASS'
assert result['operationId'] == '07a89a5c-49da-4ea5-87de-541d575f426a'
assert len(result['premises']) == 10 and len(result['passages']) == 25
freeze = json.loads((C / 'freeze.json').read_text())
assert sha(C / 'argument.md') == freeze['argument_sha256']
assert sha(A / 'P16.3-argument.md') == freeze['author_argument_sha256']
assert sha(A / 'canonical-result.json') == freeze['canonical_result_sha256']
assert sha(A / 'P16.3-paper.tex') == '08d29e4fb4af93aff797c3e825b66e28db1e6212372f1a6af3e5af361463a316'
coverage = {i: [] for i in range(10)}
files = {
    '1712.00980v3': 'P16-completion-envelopes-arxiv-1712.00980-20261004.txt',
    '1201.0187v2': 'P16-arxiv-1201.0187-20261004.txt',
    '1201.0188v1': 'P16-arxiv-1201.0188-20261004.txt',
    '2307.01697v1': 'P16-arxiv-2307.01697-20261004.txt',
    '0366': 'P16.3-Stacks-0366-20261004.txt',
    '0AY8': 'P16.3-Stacks-0AY8-20261004.txt',
}
norm = lambda s: re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s)).strip()
# These nine OCR/layout differences were read against these exact primary LF ranges.
nonmatches = {
    5: ('1712.00980v3', 1110, 1117, 'Line-break hyphenation in projective.'),
    7: ('1712.00980v3', 1147, 1154, 'Line-break hyphenation in functions.'),
    12: ('1201.0187v2', 1122, 1125, 'Spaces inside the displayed curvature expression.'),
    16: ('1201.0188v1', 1252, 1260, 'Accented Ampere and extracted truncation superscript.'),
    17: ('1201.0188v1', 1317, 1327, 'Extracted superscript has whitespace.'),
    18: ('1201.0188v1', 1413, 1418, 'Accent encoding and C0 superscript layout.'),
    19: ('1201.0188v1', 1424, 1429, 'E1 superscript and expression whitespace.'),
    21: ('2307.01697v1', 1127, 1131, 'Subscript/superscript layout and expression whitespace.'),
    22: ('2307.01697v1', 1199, 1201, 'M1 subscript/superscript layout.'),
}
checks = []
annex = ['# P16.3 round49 actual review and primary quotation checks', '',
         'The entire actual report, ten premises and twenty-five passages were read. '
         'Every zero-based premise binding and passage ID was checked. The verdict covers '
         'the retained partial theorem only; original P16.3 remains open.', '']
for i, p in enumerate(result['passages']):
    assert p['id'] == result['operationId'] + '/' + str(i)
    assert p['statement'] == result['premises'][p['premise']]
    coverage[p['premise']].append(i)
    if p['url'] == 'urn:xean:task':
        source = C / 'task.json'
    else:
        source = R / 'shared-sources' / next(v for k, v in files.items() if k in p['url'])
    matched = norm(p['quote']) in norm(source.read_text())
    assert matched == (i not in nonmatches)
    item = {'passage': i, 'premise': p['premise'], 'source': str(source),
            'source_sha256': sha(source), 'normalized_literal_match': matched}
    if not matched:
        key, start, end, explanation = nonmatches[i]
        literal = '\n'.join(source.read_text().split('\n')[start-1:end])
        item.update({'primary_LF': [start, end], 'root_read': True, 'difference': explanation})
        annex.extend(['## Passage ' + str(i), '', p['quote'], '', explanation,
                      '', 'Primary LF ' + str(start) + '--' + str(end) + ':',
                      '', '```text', literal, '```', ''])
    checks.append(item)
assert all(coverage.values())
review = D / 'P16.3-correctness-review.json'
review.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
shutil.copyfile(review, R / 'root-checks/P16.3-round49-actual-correctness-review.json')
for name in ['P16.3-argument.md', 'canonical-result.json', 'complete-root-read.json']:
    shutil.copyfile(A / name, D / name)
shutil.copyfile(A / 'source-extracts/source-provenance.json', D / 'author-source-provenance.json')
for tag in ['0366', '0AY8']:
    source = R / ('shared-sources/P16.3-Stacks-' + tag + '-20261004.txt')
    annex.extend(['## Stacks tag ' + tag, '',
                  'The complete relevant statement and proof were read in the cached primary source. '
                  'Applied to a regular integral proper flat SNC model over a DVR, all its generic '
                  'points dominate the base, the base is integral and normal, and geometric '
                  'integrality of the proper generic fiber gives H0=K. Therefore the special '
                  'fiber is geometrically connected. The reducedness and dominance hypotheses '
                  'are properties of the whole model; the special fiber need not be reduced.',
                  '', 'Source: ' + str(source), ''])
(D / 'P16.3-source-review-annex.md').write_text('\n'.join(annex))
tex = (A / 'P16.3-paper.tex').read_text()
old = 'All mathematical assertions below are draft deductions from the eleven supplied public primary-source caches. No priority claim is made for the combination proved here. Successful hash checks and TeX builds do not verify these deductions.'
new = ('The retained partial theorem and its supporting canonical notes received a source-aware '
       'independent computational correctness review with verdict PASS on 4 October 2026. '
       'The complete report is preserved with this paper. This is not a formal proof certificate '
       'or a solution of the entire original P16.3. No priority claim is made. '
       'The original eleven-source deductions are preserved; the accompanying review annex '
       'also checks the Stacks Project connectedness inputs.')
assert tex.count(old) == 1
tex = tex.replace(old, new)
old = 'the initial mixed norms sum to S.'
assert tex.count(old) == 1
tex = tex.replace(old, 'the initial mixed norms sum to VS in the raw norm convention. '
                  'The fixed factor V is absorbed in the estimate constant.')
marker = '\\section{Exact finite-dual-energy measure condition}'
clarification = r'''\paragraph{Source sign and polynomial degree.}
For $u,w\leq0$, the proof of [B], Lemma 6.10, gives
\[
e((u+w)/2)\leq\frac{1}{2^{n+1}(n+1)}\int w\,m(u),
\qquad
\int(-w)\,m(u)\leq2^{n+1}(n+1)[-e((u+w)/2)]<\infty.
\]
Its displayed statement has a sign slip; its proof supplies the expression with
$w$ used here. The energy polynomial in [B], Proposition 6.12, has degree at
most $n+1$, rather than the printed $n$. A fixed finite degree is all that the
coefficient-convergence argument requires. These clarifications and the raw
factor $V$ in the uniqueness argument preserve the reviewed conclusions.

'''
assert tex.count(marker) == 1
tex = tex.replace(marker, clarification + marker)
(D / 'P16.3-paper.tex').write_text(tex)
build = D / 'build'
build.mkdir()
codes = []
for i in [1, 2]:
    command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
               '-output-directory=' + str(build), str(D / 'P16.3-paper.tex')]
    proc = subprocess.run(command, cwd=D, capture_output=True)
    (build / ('pass' + str(i) + '.stdout.txt')).write_bytes(proc.stdout)
    (build / ('pass' + str(i) + '.stderr.txt')).write_bytes(proc.stderr)
    codes.append(proc.returncode)
    if (build / 'P16.3-paper.log').exists():
        shutil.copyfile(build / 'P16.3-paper.log', build / ('pass' + str(i) + '.tex.log'))
    assert proc.returncode == 0, proc.stdout[-2500:]
shutil.copyfile(build / 'P16.3-paper.pdf', D / 'P16.3-paper.pdf')
info = subprocess.run(['pdfinfo', str(D / 'P16.3-paper.pdf')], capture_output=True, text=True, check=True).stdout
(D / 'pdfinfo.txt').write_text(info)
pages = int(re.search(r'Pages:\s*(\d+)', info).group(1))
record = {'published_utc': now, 'atom': 'P16.3', 'round': 49,
          'scope': 'Equal-characteristic p geometric-origin smooth projective surfaces over completion at a closed point of a normal curve over a perfect field; every ample L, genuine mixed E1 operator, arbitrary-support finite-dual-energy existence and uniqueness. Higher-dimensional extension conditional on both resolution premises in dimension d+n.',
          'independently_reviewed_partial_theorem': True, 'fully_solved_original_atom': False,
          'original_remaining_gaps': ['Mixed characteristic', 'Dimensions without both proved resolution inputs', 'Removal of geometric-origin hypotheses'],
          'review': str(review), 'review_sha256': sha(review), 'verdict': 'PASS',
          'operation_id': result['operationId'], 'reported_utc': result['reportedAt'],
          'entire_report_premises_and_passages_root_read': True,
          'premises': 10, 'passages': 25, 'exact_zero_based_binding_coverage': coverage,
          'primary_quote_checks': checks,
          'harmless_corrections': ['BFJ-v1 Lemma6.10 displayed sign', 'BFJ-v1 Proposition6.12 polynomial degree at most n+1', 'Raw initial mixed norms sum VS'],
          'original_author_tex': str(A / 'P16.3-paper.tex'), 'original_author_tex_sha256': sha(A / 'P16.3-paper.tex'),
          'source': str(D / 'P16.3-paper.tex'), 'source_sha256': sha(D / 'P16.3-paper.tex'),
          'pdf': str(D / 'P16.3-paper.pdf'), 'pdf_sha256': sha(D / 'P16.3-paper.pdf'), 'pages': pages,
          'local_two_pass_return_codes': codes, 'native_compile': 'Not yet checked; no native success asserted.',
          'review_limit': 'Source-aware independent computational reconstruction by the user-selected native model, not a formal proof certificate or literature priority certification.'}
(D / 'publication-preparation.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: record[k] for k in ['verdict', 'review_sha256', 'source_sha256', 'pdf_sha256', 'pages', 'fully_solved_original_atom']}, indent=2))
