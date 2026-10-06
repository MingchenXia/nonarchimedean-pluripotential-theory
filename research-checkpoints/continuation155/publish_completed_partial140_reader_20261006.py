from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
W = R / 'campaigns/round-140/P19.2-original-endpoint-preserving-model-approximation-research/artifacts/codex-fv0BtB'
D = K / 'public-P19.2-round140-partial-endpoint-reader'
D.mkdir(parents=True, exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
canonical = K / 'P19.2-round140-completed-author-result-PUBLIC-20261006.json'
r = json.loads(canonical.read_text())
assert r['candidate'] is False and len(r['notes']) == 4
for n in ['P19.2-argument.md', 'P19.2-paper.tex', 'P19.2-paper.pdf', 'source-application-ledger.json']:
    shutil.copyfile(W / n, D / n)
info = subprocess.run(['pdfinfo', str(D / 'P19.2-paper.pdf')], capture_output=True, text=True, check=True).stdout
pages = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
log = (W / 'P19.2-paper.log').read_text()
b = {'recorded_utc': datetime.now(timezone.utc).isoformat(),
    'classification': 'Completed native author PARTIAL mathematical paper; no independent acceptance and no original closure.',
    'author': 'Xean native Codex gpt-6.1-sol xhigh', 'candidate': False, 'original_closed': False,
    'canonical_author_result': str(canonical), 'canonical_sha256': sha(canonical),
    'whole_all_four_canonical_notes_root_read': True,
    'whole_953_line_standalone_argument_root_read': True,
    'whole_source_application_ledger_root_read': True,
    'whole_standalone_tex_separately_root_read': False,
    'pages': pages, 'source_worker_two_pass_build': True,
    'root_reran_unchanged_build': False, 'overfull': log.count('Overfull'),
    'warnings': log.count('Warning'), 'undefined': log.lower().count('undefined'),
    'independent_review': False, 'accepted_count_change': 0, 'existing_editor_unchanged': True,
    'actual_visual_pages': [], 'native_compile_success_observed': False,
    'scope': 'Finite-entropy singular-start joint rescaled entropy; actual normalized model endpoint implication defect; real infinite-chain constructive exact positive-mass endpoint and discrepancy moment; bounded-start ceilings and an infinite-initial-entropy unbounded-start zero endpoint diagnostic. Full P19.2 remains open.',
    'file_bindings': [{'name': n, 'bytes': (D / n).stat().st_size, 'sha256': sha(D / n),
                       'byte_identical_to_completed_native_author': True}
                      for n in ['P19.2-argument.md', 'P19.2-paper.tex', 'P19.2-paper.pdf', 'source-application-ledger.json']]}
assert b['overfull'] == b['warnings'] == b['undefined'] == 0
(D / 'publication-binding.json').write_text(json.dumps(b, indent=2) + '\n')
for n in [1, (pages + 1) // 2, pages]:
    subprocess.run(['pdftoppm', '-f', str(n), '-l', str(n), '-scale-to', '1500', '-png', '-singlefile', str(D / 'P19.2-paper.pdf'), str(D / f'page-{n}-LOCALONLY')], capture_output=True, check=True)
print(json.dumps({'reader': str(D), 'pages': pages, 'classification': 'PARTIAL; unreviewed',
                  'whole_argument_and_source_ledger_root_read': True}, indent=2))
