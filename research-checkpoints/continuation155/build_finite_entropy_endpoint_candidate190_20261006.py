from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
source = K / 'P19.2-finite-entropy-singular-start-zero-endpoint-counterexample-candidate-20261006-continuation190.tex'
D = K / 'public-P19.2-continuation190-finite-entropy-endpoint-reader'
D.mkdir(parents=True, exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
raw = source.read_bytes()
assert bytes([13]) not in raw and bytes([9]) not in raw
rows = []
for i in range(2):
    cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-output-directory=' + str(D), str(source)]
    p = subprocess.run(cmd, capture_output=True, text=True)
    (D / f'build{i+1}-LOCALONLY.stdout').write_text(p.stdout)
    rows.append({'argv': cmd, 'returncode': p.returncode})
    assert p.returncode == 0, p.stdout[-4000:]
pdf = D / (source.stem + '.pdf')
log = (D / (source.stem + '.log')).read_text()
info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
grant = R / 'deliverables/original-P19.1/P19.1-paper.tex'
b = {'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'classification': 'New unreviewed finite-initial-entropy zero-endpoint diagnostic candidate.',
    'tex': str(source), 'tex_sha256': sha(source), 'pdf': str(pdf), 'pdf_sha256': sha(pdf),
    'pages': pages, 'builds': rows, 'overfull': log.count('Overfull'),
    'warnings': log.count('Warning'), 'undefined': log.lower().count('undefined'),
    'whole_tex_root_authored': True, 'whole_final_tex_separately_root_read': False,
    'sole_substantial_theorem_grant': str(grant), 'grant_tex_sha256': sha(grant),
    'grant_application': 'Exact fixed smooth compact-Kahler maximal-ray existence/order, energy defect, and finite-slice entropy classification; not an endpoint grant.',
    'proof_scope': 'Every complex P^n with n>=2; explicit isolated full-mass E1 finite-H start; actual hyperplane boundary-nef model; absolute terminal P ceiling erased at constant finite ray d1 distance and entropy slope1.',
    'primary_background_application': 'Finite-energy Mabuchi convexity and finite contracted energies in BDL4.7, also explicitly retained in whole granted R. No new source quotation or broad source grant.',
    'actual_visual_pages': [], 'native_compile_success_observed': False,
    'independent_review': False, 'original_closed': False, 'accepted_count_change': 0,
    'full_P19_2_nonexistence_claim': False, 'relative_singular_background_claim': False,
    'active145_and146_inputs_unchanged': True, 'new_math_sent_to_active_workers': False,
    'existing_editor_unchanged': True}
(D / 'publication-binding.json').write_text(json.dumps(b, indent=2) + '\n')
for n in [1, (pages + 1) // 2, pages]:
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-scale-to', '1500', '-png', '-singlefile', str(pdf), str(D / f'page-{n}-LOCALONLY')], capture_output=True, check=True)
print(json.dumps({'pages': pages, 'tex_sha256': sha(source), 'pdf_sha256': sha(pdf),
    'overfull': b['overfull'], 'warnings': b['warnings'], 'undefined': b['undefined']}, indent=2))
