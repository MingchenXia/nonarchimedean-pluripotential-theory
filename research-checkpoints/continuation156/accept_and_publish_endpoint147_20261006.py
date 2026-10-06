from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-147/P19.2-finite-entropy-singular-start-zero-endpoint-independent-review'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
review = K / 'P19.2-round147-actual-scoped-independent-review-20261006.json'
r = json.loads(review.read_text())
assert sha(review) == 'e3efc158e999505f91a1bdb48d735231bcf1bbec5eb9c61651ec21f75adacb95'
assert r['kind'] == 'codex-report' and r['verdict'] == 'PASS'
assert len(r['premises']) == 5 and len(r['passages']) == 10
for e in r['passages']:
    assert type(e['premise']) is int and 0 <= e['premise'] < 5
    assert e['statement'] == r['premises'][e['premise']] and e['quote'] and e['url']
external = [e for e in r['passages'] if e['url'] != 'urn:xean:task']
assert len(external) == 9 and {e['premise'] for e in external} == set(range(5))
assert r['passages'][9]['url'] == 'urn:xean:task'
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
s = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')],
    cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
assert s['status'] == 'completed' and s['calls']['settled'] == 1
now = datetime.now(timezone.utc).isoformat()
scope = 'Every complex projective space P^n with n>=2, FS volume one. Explicit singular full-mass E1 initial potential with finite probability entropy; actual bounded relatively nef/semiample hyperplane model datum on the full supported NA carrier; zero-start absolute nontrivial P-model endpoint of zero raw mass; singular-start actual maximal ray with identically minus-infinite zero level; constant finite d1 distance and entropy slope one, with finite entropy at every finite time.'
a = {'recorded_utc': now, 'atom': 'P19.2',
    'classification': 'Independently accepted supporting finite-initial-entropy absolute-endpoint counterexample.',
    'review': str(review), 'review_sha256': sha(review),
    'whole_canonical_report_premises_passages_root_read': True,
    'strict_structural_schema_and_indices_validated': True,
    'external_premises': 5, 'external_evidence_passages': 9, 'total_passages': 10,
    'task_passage_annotation': 'Canonical passage 9 repeats the task grant but carries index 0 and the unrelated BT statement. Retained unchanged as defective task metadata, excluded from external-premise evidence. Independent primary passages 0-8 cover all five external premises; the complete original P19.1 grant is directly authorized and fully present in the frozen task/argument.',
    'mathematical_theorem_grant': 'Complete established original P19.1 mathematical theorem R in its retained fixed smooth compact-Kahler signature, including its stated finite-energy foundations.',
    'task_sha256': f['task_sha256'], 'argument_sha256': f['argument_sha256'],
    'scope': scope, 'original_closed': False, 'full_residual_P19_2_claim': False,
    'relative_singular_start_endpoint_failure_claim': False,
    'accepted_papers_before': 55, 'accepted_papers_after': 56, 'originals_solved': 8, 'originals_open': 34,
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
    'harmless_correction': 'On the affine blowup chart the extended total current is [E]+g*omega_FS. Its residual current after removal of [E] is g*omega_FS. HCMA is imposed on the punctured family where [E] disappears; the actual datum retains E.'}
ap = K / 'P19.2-round147-endpoint-acceptance-and-original-scope-record-20261006.json'
assert not ap.exists()
source = K / 'P19.2-finite-entropy-singular-start-zero-endpoint-counterexample-candidate-20261006-continuation190.tex'
assert sha(source) == '342ad1ad104753f2bfd8d9cffc141241dd37e4301b2d9a5918dccfd60aca5478'
new = source.read_text().replace('An unreviewed supporting candidate for Problem P19.2', 'A finite-entropy counterexample to absolute endpoint invariance')
before = r'''It is bounded on each finite time annulus. On the blowup over the
affine time chart its total current is $g^*\omega_{\rm FS}$, whose
$(n+1)$st power vanishes.
It therefore solves the actual homogeneous geodesic equation.'''
after = r'''It is bounded on each finite time annulus. On the affine blowup chart
the extended total current is $[E]+g^*\omega_{\rm FS}$; after removal
of the exceptional fixed divisor its residual current is
$g^*\omega_{\rm FS}$. On the punctured family $[E]$ disappears
and the $(n+1)$st power vanishes. Thus the actual homogeneous
geodesic equation holds on its required domain.'''
assert before in new
new = new.replace(before, after)
new = new.replace('this unreviewed supporting candidate changes no completion count.',
    'this independently accepted supporting theorem changes no\noriginal-problem completion count.')
D = R / 'deliverables/scoped-P19.2-finite-entropy-zero-endpoint'
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
b = {'recorded_utc': now, 'classification': 'Final independently accepted supporting finite-initial-entropy endpoint counterexample.',
    'tex': str(tex), 'tex_sha256': sha(tex), 'pdf': str(pdf), 'pdf_sha256': sha(pdf), 'pages': pages,
    'source_candidate': str(source), 'source_candidate_sha256': sha(source), 'builds': rows,
    'overfull': log.count('Overfull'), 'warnings': log.count('Warning'), 'undefined': log.lower().count('undefined'),
    'whole_candidate_tex_root_read': True, 'whole_assembled_final_tex_separately_root_read': False,
    'whole_canonical_review_root_read': True, 'review': str(review), 'review_sha256': sha(review),
    'review_verdict': 'PASS', 'accepted_paper_count': 56, 'scope': scope, 'original_closed': False,
    'editorial_changes': 'Reviewed status and the single harmless total-current clarification expressly verified in the canonical review. Frozen candidate and native input unchanged.',
    'actual_visual_pages': [], 'native_compile_success_observed': False, 'existing_editor_unchanged': True}
assert b['overfull'] == b['warnings'] == b['undefined'] == 0
(D / 'publication-binding.json').write_text(json.dumps(b, indent=2) + '\n')
ap.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
for n in sorted({1, (pages + 1) // 2, pages}):
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-scale-to', '1500', '-png', '-singlefile', str(pdf), str(D / f'page-{n}-LOCALONLY')], capture_output=True, check=True)
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 55 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update({'historical_reviewed_scoped_papers': 56, 'updated_utc': now, 'P19_2_actual_scoped147': a,
        'P19_2_accepted_finite_entropy_endpoint_paper147': b,
        'current_finite_entropy_endpoint_review147': {'round':147,'observed_status':'completed','review_verdict':'PASS','acceptance_record':str(ap),'original_closed':False},
        'goal_state': '8/42 originals solved;34 open;56 independently accepted papers. Continue small batches.'})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
tsv = R / 'checklist-current.tsv'
out = []
for line in tsv.read_text().splitlines():
    z = line.split('\t')
    if z[0] == 'P19.2':
        z[2] = 'Entire closed toric-profile theorem PASS146 and finite-initial-entropy absolute zero-endpoint counterexample PASS147. Full unchanged compact-Kahler residual existence original remains open.'
        z[3] = str(int(z[3]) + 1)
    out.append('\t'.join(z))
tsv.write_text('\n'.join(out) + '\n')
print(json.dumps({'accepted_papers': 56, 'originals_solved': 8, 'pages': pages,
    'final_paper': str(tex), 'canonical_review_sha256': sha(review)}, indent=2))
