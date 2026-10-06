from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-146/P19.2-entire-closed-toric-profile-actual-model-independent-review'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
review = K / 'P19.2-round146-actual-scoped-independent-review-20261006.json'
r = json.loads(review.read_text())
assert r['kind'] == 'codex-report' and r['verdict'] == 'PASS'
assert len(r['premises']) == 14 and len(r['passages']) == 23
for e in r['passages']:
    assert type(e['premise']) is int and 0 <= e['premise'] < 14
    assert e['statement'] == r['premises'][e['premise']] and e['quote'] and e['url']
assert {e['premise'] for e in r['passages']} == set(range(14))
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
s = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')],
    cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
assert s['status'] == 'completed' and s['calls']['settled'] == 1
now = datetime.now(timezone.utc).isoformat()
scope = 'P1 over C, fixed O(1), zero analytic initial point, every continuous nonnegative nonincreasing convex finite-height roof g on[0,1] with g(1)=0. Actual smooth relatively ample rational model approximation; positive degree on every central/resolution component; uniform entire closed P singularity and raw mass profile, including zero-mass terminal c=1, strong energy and discrepancy entropy recovery, and uniform analytic entropy remainder giving every joint index/time limit.'
a = {'recorded_utc': now, 'atom': 'P19.2', 'classification': 'Independently accepted supporting entire closed one-branch toric-profile existence theorem.',
    'review': str(review), 'review_sha256': sha(review),
    'whole_canonical_report_premises_passages_root_read': True,
    'strict_schema_and_indices_validated': True, 'external_premises': 14, 'evidence_passages': 23,
    'mathematical_theorem_grants': [], 'task_sha256': f['task_sha256'], 'argument_sha256': f['argument_sha256'],
    'scope': scope, 'original_closed': False, 'full_residual_P19_2_claim': False,
    'accepted_papers_before': 54, 'accepted_papers_after': 55, 'originals_solved': 8, 'originals_open': 34,
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
    'harmless_clarifications': ['Positive weights are on the finite positive-slope rays only.',
        'Monomials are relative sections over the affine time chart containing zero.',
        'Curvature means b delta0 plus omega restricted to the outer region.',
        'Identify precise Legendre and NA energy-defect source statements and their log-norm/time transport.']}
ap = K / 'P19.2-round146-toric-acceptance-and-original-scope-record-20261006.json'
assert not ap.exists()
source = K / 'P19.2-endpoint-preserving-actual-toric-model-approximation-candidate-20261006-continuation189.tex'
old = source.read_text()
new = old.replace('Research candidate for a restricted case of Problem P19.2', 'A constructive one-branch model approximation theorem')
new = new.replace('This is an unreviewed theorem candidate in\none toric branch, with zero analytic starting point; it is not a solution\nof the full residual hybrid approximation problem.',
    'The complete theorem has passed independent review in this precise\none-branch signature, with zero analytic starting point. The full\nresidual hybrid approximation problem remains open.')
before = r'''Choose positive rational weights
$a_i$ on \emph{all} of them, with sum exactly $c_j$, arbitrarily close'''
after = r'''Choose positive rational weights
$a_i$ on every positive-slope ray $n_1,\ldots,n_r$, with sum exactly
$c_j$, arbitrarily close'''
assert before in new
new = new.replace(before, after)
new = new.replace('of $g_j$, include both $x=0$ and $x=1$. For a common denominator $M$\nthe sections are',
    'of $g_j$, include both $x=0$ and $x=1$. Over the affine time chart\ncontaining zero, for a common denominator $M$ the relative sections are')
new = new.replace(r'''is $b\delta_0+\omega$ on the outer region, with no interface atom;''',
    r'''is $b\delta_0+\mathbf1_{\rm outer}\omega$, with no interface atom;''')
before = r'''Legendre biconjugacy recovers $u_t$. Thus the ray is maximal in
the standard test-curve correspondence, with datum (5).'''
after = r'''Legendre biconjugacy recovers $u_t$; the maximal-test-curve
correspondence applies \cite{levels}, including the zero-mass endpoint.
The total weight differs by at most $\log2$ from
$\sup_x(x\rho+g(x)\log|\tau|^2)$, whose actual Gauss divisorial
orders give exactly (5). For the logarithmic-norm convention in
\cite{maximal}, use $s=-\log|\tau|$ and $U_s=u_{2s}/2$ with the
same background curvature. The energy calculation below gives
$E(U_s)=sE^{\rm NA}(\varphi)$, so the source's exact energy-defect
criterion proves NA maximality for the usual actual datum. Thus
P-maximal test levels and NA maximal rays are each justified.'''
assert before in new
new = new.replace(before, after)
new = new.replace('The present paper has no independent acceptance and changes no\noriginal-problem completion count.',
    'The complete precisely scoped theorem has passed independent review.\nIt contributes one accepted supporting paper and changes no\noriginal-problem completion count.')
start = new.index('\\bibitem{levels}')
end = new.index('\\end{thebibliography}', start)
refs = r'''\bibitem{levels} J. Ross and D. Witt Nystr\"om,
\emph{Analytic test configurations and geodesic rays},
\href{https://arxiv.org/pdf/1101.1612}{Definition 5.1 and Theorem 6.8}:
maximal test curves with small unbounded locus.
\bibitem{maximal} R. Berman, S. Boucksom and M. Jonsson,
\emph{A variational approach to the Yau--Tian--Donaldson conjecture},
\href{https://arxiv.org/pdf/1509.04561}{Definition 4.2 and Corollary 6.7}:
usual total-potential datum and NA maximality by energy.
\bibitem{BJ} S. Boucksom and M. Jonsson,
\href{https://arxiv.org/pdf/1801.08229}{Singular semipositive metrics
in non-Archimedean geometry}, Section 2.2, Corollary 4.16,
Proposition 7.7, Definition 12.1 and Theorem A;
\href{https://arxiv.org/pdf/2107.11221}{Section 5.2 and Theorem 5.5}
for the NA $d_1$ topology.
\bibitem{BHJ} S. Boucksom, T. Hisamoto and M. Jonsson,
\href{https://www.math.nagoya-u.ac.jp/~hisamoto/papers/BHJ2_16.pdf}
{Uniform K-stability, Duistermaat--Heckman measures and singularities
of pairs}, Sections 2.3 and 2.6--2.7: model intersections and discrepancy.
\bibitem{toric} R. Berman and B. Berndtsson,
\href{https://arxiv.org/pdf/1207.6128}{Sections 2.1--2.2}:
convex and toric Monge--Amp\`ere with its dimension factorial.
\bibitem{BT} E. Bedford and B. A. Taylor,
\href{https://www.math.stonybrook.edu/~ebedford/PapersForM655/BTNewCapacity.pdf}
{A new capacity for plurisubharmonic functions}, Theorems 2.1 and 6.9.
\bibitem{nonpolar} S. Boucksom, P. Eyssidieux, V. Guedj and A. Zeriahi,
\href{https://arxiv.org/pdf/0812.3674}{Section 1.2}:
nonpluripolar products; T. Darvas, E. Di Nezza and C. H. Lu,
\href{https://arxiv.org/pdf/1909.00839}{Lemma 3.4}:
ordered singularity metric through zero mass.
\bibitem{energy} R. Berman, S. Boucksom, V. Guedj and A. Zeriahi,
\href{https://arxiv.org/pdf/0907.4490}{Section 2.1}:
bounded energy cocycle and first variation.
'''
new = new[:start] + refs + new[end:]
new = new.replace('\\begin{thebibliography}{9}', '\\begin{thebibliography}{99}')
D = R / 'deliverables/scoped-P19.2-closed-toric-profile'
D.mkdir(parents=True, exist_ok=False)
tex = D / 'P19.2-paper.tex'
tex.write_text(new)
rows = []
for i in range(2):
    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=' + str(D), str(tex)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    (D / f'build{i+1}-LOCALONLY.stdout').write_text(p.stdout)
    rows.append({'argv': cmd, 'returncode': p.returncode})
    assert p.returncode == 0, p.stdout[-4000:]
log = (D / 'P19.2-paper.log').read_text()
pdf = D / 'P19.2-paper.pdf'
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
b = {'recorded_utc': now, 'classification': 'Final independently accepted supporting entire closed toric-profile theorem.',
    'tex': str(tex), 'tex_sha256': sha(tex), 'pdf': str(pdf), 'pdf_sha256': sha(pdf), 'pages': pages,
    'source_candidate': str(source), 'source_candidate_sha256': sha(source), 'builds': rows,
    'overfull': log.count('Overfull'), 'warnings': log.count('Warning'), 'undefined': log.lower().count('undefined'),
    'whole_candidate_tex_root_read': True, 'whole_assembled_final_tex_separately_root_read': False,
    'whole_canonical_review_root_read': True, 'review': str(review), 'review_sha256': sha(review),
    'review_verdict': 'PASS', 'accepted_paper_count': 55, 'scope': scope, 'original_closed': False,
    'editorial_changes': 'Reviewed status, four harmless clarifications expressly verified in the canonical review, and its precise primary bibliography. Frozen source and native inputs unchanged.',
    'actual_visual_pages': [], 'native_compile_success_observed': False, 'existing_editor_unchanged': True}
assert b['overfull'] == b['warnings'] == b['undefined'] == 0
(D / 'publication-binding.json').write_text(json.dumps(b, indent=2) + '\n')
ap.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
for n in [1, (pages + 1) // 2, pages]:
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-scale-to', '1500', '-png', '-singlefile', str(pdf), str(D / f'page-{n}-LOCALONLY')], capture_output=True, check=True)
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 54 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update({'historical_reviewed_scoped_papers': 55, 'updated_utc': now, 'P19_2_actual_scoped146': a,
        'goal_state': '8/42 originals solved;34 open;55 independently accepted papers. Continue small batches.'})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
tsv = R / 'checklist-current.tsv'
out = []
for line in tsv.read_text().splitlines():
    s = line.split('\t')
    if s[0] == 'P19.2':
        s[2] = 'Entire closed one-branch finite-height toric P profile, including zero-mass endpoint, independently PASS146. Full compact-Kahler residual original open; finite-initial-H zero-endpoint diagnostic review147 launched.'
        s[3] = str(int(s[3]) + 1)
    out.append('\t'.join(s))
tsv.write_text('\n'.join(out) + '\n')
print(json.dumps({'accepted_papers': 55, 'originals_solved': 8, 'pages': pages,
    'final_paper': str(tex), 'canonical_review_sha256': sha(review)}, indent=2))
