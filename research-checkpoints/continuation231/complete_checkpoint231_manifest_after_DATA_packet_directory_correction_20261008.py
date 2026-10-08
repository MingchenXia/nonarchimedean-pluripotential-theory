from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

R = Path('/workspace/research'); K = R / 'root-checks'; G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation231.json'; F = G / 'continuation231-publication-records'
S = K / 'small-batch226227-public-status-20261008-continuation231'
D = K / 'public-P05.1-continuation306-balanced-cellwise-Lipschitz-and-single-cell-real-regularization'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, v: Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
assert not M.exists() and F.is_dir() and S.is_dir()
prior = json.loads((G / 'push-receipt-continuation230.json').read_text())
j = json.loads((R / 'active-work.json').read_text())
assert j['github_pending_checkpoint']['continuation'] == 231 and j['github_pending_checkpoint']['expected_parent'] == prior['commit_sha']
assert j['historical_reviewed_scoped_papers'] == 85 and len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33
for name in ['active-work.json', 'checklist-current.json']: assert (R / name).read_bytes() == (F / name).read_bytes()
write(F / 'manifest-preparation-directory-error-and-repair.json', dict(recorded_utc=datetime.now(timezone.utc).isoformat(), failed_preparation_script=str(R / 'prepare_checkpoint231_balanced_paper_and_formal_realization_20261008.py'), failed_script_sha256=sha(R / 'prepare_checkpoint231_balanced_paper_and_formal_realization_20261008.py'), actual_error='FileNotFoundError: round226 immutable-mathematical-packet absent; original campaign uses its own immutable DATA packet directory', preserved_prepared_snapshot=True, campaign_inputs_and_sources_unchanged=True, repair='Use exact verified paths from frozen mathematical-packet manifests; do not infer directory names or rerun earlier mutations', no_GitHub_write_had_occurred=True))
files = []
def add(p, target=None):
    p = Path(p); assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p), path=target or 'research-checkpoints/continuation231/' + str(p.relative_to(R)), bytes=p.stat().st_size, sha256=sha(p)))
for folder in [F, S, D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.suffix not in ['.aux', '.toc', '.out']: add(p)
for n in [226, 227]:
    c = next((R / f'campaigns/round-{n}').iterdir()); freeze = json.loads((c / 'freeze.json').read_text())
    for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'private-primary-packet-bindings.json', 'freeze.json', 'launch-record.json']: add(c / name)
    for e in json.loads((c / 'mathematical-packet-bindings.json').read_text()):
        assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
        assert Path(e['path']).is_relative_to(c); add(e['path'])
    if n == 227:
        add(c / 'historical-own-evidence-bindings.json')
        for e in json.loads((c / 'historical-own-evidence-bindings.json').read_text()):
            assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
            assert Path(e['path']).is_relative_to(c); add(e['path'])
roots = [next(K.glob('*continuation' + str(n) + '-*.json')) for n in [304, 305]]
for p in [*roots, R / 'write_balanced_complete_affine_arrangement_ambient_convex_restriction_obstruction304_20261008.py', R / 'write_formal_multiplier_ideal_integral_certificate_route305_20261008.py', R / 'prepare_original_formal_data_realization226_20261008.py', R / 'launch_original_formal_data_realization226_20261008.py', R / 'extract_settled224_exact_native_result_20261008.py', R / 'extract_settled225_exact_native_result_20261008.py', R / 'reproduce_balanced_cellwise_Lipschitz_paper306_20261008.py', R / 'prepare_balanced_cellwise_whole_audit227_20261008.py', R / 'launch_balanced_cellwise_whole_audit227_20261008.py', R / 'record_verified230_20261008.py', G / 'push-receipt-continuation230.json', K / 'round225-actual-native-final.json', K / 'round225-registered-native-result.json', K / 'round225-actual-final-extraction-binding-20261008.json', R / 'prepare_checkpoint231_balanced_paper_and_formal_realization_20261008.py', Path(__file__)]: add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']: add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({e['path'] for e in files}) == len(files)
write(M, dict(generated_utc=datetime.now(timezone.utc).isoformat(), repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), fully_solved_original_atoms=j['fully_solved_original_atoms'], remaining_open_atoms=33, historical_reviewed_scoped_papers=85, commit_message='Record balanced cellwise regularization draft and launch original formal ideal realization with independent source audit', scope='WHOLE unreviewed306 plus ROOT exact local reproduction; unreviewed304 ambient convex obstruction and305 conditional formal ideal certificate. Native226 original P14.8 and227 whole306 audit max2 gpt61solxhigh;225 completed review pending.9solved33OPEN85scoped; lost builtin handles not compiler results; preparation filename failure retained/repaired using exact manifests; exact verified nonforce checkpoint.'))
print(json.dumps(dict(manifest=str(M), sha256=sha(M), listed_files=len(files), originals_solved=9, accepted_papers=85), indent=2))
