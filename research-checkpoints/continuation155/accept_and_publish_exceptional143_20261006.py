from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
C = R / 'campaigns/round-143/P16.5-entire-exceptional-big-equation-independent-review-retry1'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
review = K / 'P16.5-round143-actual-scoped-independent-review-20261006.json'
r = json.loads(review.read_text())
assert r['kind'] == 'codex-report' and r['verdict'] == 'PASS'
assert len(r['premises']) == 9 and len(r['passages']) == 53
for e in r['passages']:
    assert type(e['premise']) is int and 0 <= e['premise'] < 9
    assert e['statement'] == r['premises'][e['premise']] and e['quote'] and e['url']
assert {e['premise'] for e in r['passages']} == set(range(9))
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
status = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(C / 'work.sqlite')],
    cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
assert status['status'] == 'completed' and status['calls']['settled'] == 1
now = datetime.now(timezone.utc).isoformat()
scope = 'Every smooth projective Y over every algebraically closed trivially valued characteristic-zero field, every dimension n>=2, any nonempty smooth center of codimension>=2, X=Bl_ZY, actual ample rational A on Y and c>0 rational, L=pi*A+cE. Entire genuine cone, intrinsic relative E1 and preconstructed moving operator, all continuous derivatives, arbitrary-support intrinsic target criterion, actual attainment, comparison, domination and uniqueness.'
a = {'recorded_utc': now, 'atom': 'P16.5', 'classification': 'Independently accepted supporting entire exceptional-big-family equation; original remains open.',
    'review': str(review), 'review_sha256': sha(review), 'whole_canonical_report_premises_passages_root_read': True,
    'strict_schema_and_indices_validated': True, 'external_premises': 9, 'evidence_passages': 53,
    'actual_task_grant_evidence_passages': 0,
    'metadata_clarification': 'Report mentions an unindexed task passage; canonical passages contain none. Sole grant is supplied directly and exactly in frozen task and argument, not a fabricated external evidence index.',
    'task_sha256': f['task_sha256'], 'argument_sha256': f['argument_sha256'], 'scope': scope,
    'sole_grant': 'Exact complete actual-ample G0 mathematical body, only within its retained actual-ample hypotheses.',
    'harmless_clarifications': ['Weighted decrease uses one common upper constant on a tail, never per-stage generic normalization.',
        'Remove the total pulled-back fixed exceptional factor, including vertical components.',
        'The usc-majorant argument requires its genuine lower anchor, in particular u+tf.'],
    'original_closed': False, 'arbitrary_big_class_claim': False, 'zero_volume_claim': False,
    'accepted_papers_before': 53, 'accepted_papers_after': 54, 'originals_solved': 8, 'originals_open': 34,
    'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh'}
ap = K / 'P16.5-round143-exceptional-acceptance-and-original-scope-record-20261006.json'
if ap.exists():
    saved = json.loads(ap.read_text())
    assert saved['review_sha256'] == a['review_sha256'] and saved['accepted_papers_after'] == 54
    a = saved
else:
    ap.write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
source = K / 'P16.5-exceptional-big-cone-entire-relative-equation-candidate-20261006-continuation185.tex'
old = source.read_text()
new = old.replace('center, this unreviewed candidate constructs the whole genuine',
                  'center, this paper constructs the whole genuine')
new = new.replace('The construction\nhas not undergone independent review and does not solve original\nP16.5 for arbitrary big or zero-volume pseudoeffective classes.',
                  'The complete construction has passed independent review in this\nprecise signature. Original P16.5 for arbitrary big classes remains open;\nzero-volume pseudoeffective classes are not asserted here.')
new = new.replace('Unreviewed entire exceptional-class equation', 'Entire exceptional-class equation')
before = 'All horizontal fixed\nexceptional factors are removed in the relative moving product.'
after = 'The fixed exceptional factor is its total pullback on the common\nmodel, including every vertical component; this entire fixed factor is\nremoved in the relative moving product.'
assert before in new
new = new.replace(before, after)
before = r'''The identical model projection and limiting proof gives every mixed
relative product on this fixed class, with mass $V$. Weighted limits
are genuine: for decreasing finite-energy tests $z_j\to z$ and
mixed ample outputs $\mu_j\to\mu$, the ample theorem gives weak
convergence of $(-z_j)\mu_j$ after generic normalization. Their
positive limit charges no center, since $\mu$ does not and the
test is integrable. Apply the signed continuity statement after
(15), restoring the converging generic constants.'''
after = r'''The identical model projection and limiting proof gives every mixed
relative product on this fixed class, with mass $V$. Each mixed output
has finite dual energy by the ample integrability criterion, so it
also charges no center. Weighted limits are genuine: for decreasing
finite-energy tests $z_j\to z$ and mixed ample outputs
$\mu_j\to\mu$, subtract one common upper constant on a tail.
The tests still decrease and their negative weighted measures are
positive. The ample theorem gives their weak convergence; the limit
charges no center because $\mu$ does not and $z$ is integrable.
Apply the signed continuity statement after (15), and restore constants
by the weighted-measure identity. Generic constants converge, but
normalizing each stage by its own generic value is not used to claim
decrease.'''
assert before in new
new = new.replace(before, after)
new = new.replace('For an upper bounded usc obstacle $h$ define the outer extension',
    'For an upper bounded usc obstacle $h$ with a genuine lower anchor,\ndefine the outer extension')
new = new.replace('Exact scope of this unreviewed equation candidate', 'Exact scope of the equation theorem')
before = '''The new model projection, pole exclusions, outer derivative and
target transport have not yet undergone independent review.
This paper therefore adds no solved original atom or accepted paper.'''
after = '''The complete structural and equation proof has passed independent
review, relative to that exact actual-ample premise. It contributes
one accepted supporting paper; it closes no additional original atom.'''
assert before in new
new = new.replace(before, after)
new = new.replace('This candidate is mathematical data for a future\nindependent review, and changes no already running native input.',
    'The frozen candidate and canonical independent review are retained\nseparately. None of the new editorial clarifications changes an active\nresearch input.')
D = R / 'deliverables/scoped-P16.5-exceptional-big-family'
D.mkdir(parents=True, exist_ok=False)
tex = D / 'P16.5-paper.tex'
tex.write_text(new)
rows = []
for i in range(2):
    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=' + str(D), str(tex)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    (D / f'build{i+1}-LOCALONLY.stdout').write_text(p.stdout)
    rows.append({'argv': cmd, 'returncode': p.returncode})
    assert p.returncode == 0, p.stdout[-4000:]
log = (D / 'P16.5-paper.log').read_text()
pdf = D / 'P16.5-paper.pdf'
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
b = {'recorded_utc': now, 'classification': 'Final independently accepted supporting exceptional-big-family paper.',
    'tex': str(tex), 'tex_sha256': sha(tex), 'pdf': str(pdf), 'pdf_sha256': sha(pdf), 'pages': pages,
    'source_candidate': str(source), 'source_candidate_sha256': sha(source), 'builds': rows,
    'overfull': log.count('Overfull'), 'warnings': log.count('Warning'), 'undefined': log.lower().count('undefined'),
    'whole_candidate_tex_root_read': True, 'whole_assembled_final_tex_separately_root_read': False,
    'whole_canonical_review_root_read': True, 'review': str(review), 'review_sha256': sha(review),
    'review_verdict': 'PASS', 'accepted_paper_count': 54, 'scope': scope, 'original_closed': False,
    'editorial_changes': 'Reviewed status plus three exact harmless clarifications expressly verified by the independent review; source candidate and frozen input unchanged.',
    'actual_visual_pages': [], 'native_compile_success_observed': False, 'existing_editor_unchanged': True}
assert b['overfull'] == b['warnings'] == b['undefined'] == 0
(D / 'publication-binding.json').write_text(json.dumps(b, indent=2) + '\n')
for n in [1, (pages + 1) // 2, pages]:
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-scale-to', '1500', '-png', '-singlefile', str(pdf), str(D / f'page-{n}-LOCALONLY')], capture_output=True, check=True)
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 53 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update({'historical_reviewed_scoped_papers': 54, 'updated_utc': now,
        'P16_5_actual_scoped143': a,
        'goal_state': '8/42 originals solved;34 open;54 independently accepted papers. Continue small batches.'})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
tsv = R / 'checklist-current.tsv'
out = []
for line in tsv.read_text().splitlines():
    s = line.split('\t')
    if s[0] == 'P16.5':
        s[2] = 'All-big SURFACE entire equation PASS142; entire exceptional nonnef-big family all dimensions PASS143. Original arbitrary-big full research145 running.'
        s[3] = str(int(s[3]) + 1)
    out.append('\t'.join(s))
tsv.write_text('\n'.join(out) + '\n')
print(json.dumps({'accepted_papers': 54, 'originals_solved': 8, 'final_paper': str(tex), 'pages': pages,
    'canonical_review_sha256': sha(review)}, indent=2))
