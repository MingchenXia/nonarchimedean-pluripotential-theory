from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K, G = R / 'root-checks', R / 'github-checkpoint'
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, value):
    if p.exists():
        assert json.loads(p.read_text()) == value, str(p)
        return
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
T = K / 'P16.5-complete-moving-foundations-and-relative-contraction-candidate-20261006-continuation208.tex'
D = K / 'public-P16.5-continuation208-moving-contraction-reader'
if (D / 'publication-binding.json').exists():
    now = json.loads((D / 'publication-binding.json').read_text())['recorded_utc']
assert sha(T) == '850d724b2f4435e0a45d93c3a1cafc9265749fc502a2982db4c6105b8bd55867'
assert sha(D / 'paper.pdf') == sha(T.with_suffix('.pdf')) == '8c5f6413d79a19da8fe1d8cb4b7c9fdfdb1eb3838b8e3e5d66561dee0b70f308'
assert len(T.read_text().splitlines()) == 484
assert not any(x in T.with_suffix('.log').read_text() for x in ('Warning:', 'Overfull', 'Underfull', 'undefined'))
b = {'recorded_utc': now, 'classification': 'Unreviewed actual-domain reconstruction208: whole finite-list moving foundations and relative contraction, with complete companion207 proof rather than S-M axiom grants.', 'tex': str(T), 'tex_sha256': sha(T), 'pdf': str(D / 'paper.pdf'), 'pdf_sha256': sha(D / 'paper.pdf'), 'pages': 7, 'source_lines': 484, 'whole_final_tex_root_read': True, 'whole_final_tex_root_read_chunks': ['whole final484LF after exact normalization and bibliography corrections'], 'actual_visual_pages': list(range(1, 8)), 'final_visual_image_hashes': {str(n): sha(D / f'page-{n}.png') for n in range(1, 8)}, 'final_two_pass_local_build_succeeded': True, 'warnings': 0, 'overfull': 0, 'underfull': 0, 'undefined': 0, 'native_final_compile_success_observed': True, 'native_final_success_message': "The current source compiled successfully with the desktop editor's compiler.", 'existing_editor_unchanged': True, 'independent_acceptance': False, 'original_closed': False, 'accepted_paper_count_unchanged': 63, 'scope': 'All lower full-system moving positive products and fixed signed tests; same actual generated A_m for every finite obstacle list, entire horizontal pullback removed before vertical principalization, energy and weak top limits; actual bounded section density on U; fixed-model degree-first missing-rank trace; generic-error-retaining finite energy polynomial gives whole quadratic relative contraction; genuine finite-energy Kodaira pole; intrinsic all-test integrability iff finite dual energy and coercivity.', 'remaining': 'Joint independent review of207208 and complete original proof-chain identification. Fixed-original-unbounded-test physical reference defect remains separate. Frozen165 and active158163 receive no new proof data.'}
save(D / 'publication-binding.json', b)
front = json.loads((R / 'active-work.json').read_text())
deps = []
for key, scope in [('P16_5_completed_partial159', 'Only unconditional finite graph/nef energy calculus and full finite-model section lattice; no conditional S-M granted.'), ('P16_5_scalar_negligible_big_pole160', 'Only independently accepted actual scalar result from G0/G1.'), ('P16_5_actual_outer_energy_and_full_volume_derivative207', 'Whole unreviewed companion proof of actual outer energy and derivative. Must be jointly checked, not granted as a separate actual nonample axiom.')]:
    q = Path(front[key]['tex'])
    assert sha(q) == front[key]['tex_sha256']
    deps.append({'front_key': key, 'file': str(q), 'sha256': sha(q), 'whole_body_root_read': True, 'exact_scope': scope})
units = []
source_base = R / 'campaigns/round-159/P16.5-original-equation-after-arbitrary-target-output-approximation/artifacts/codex-0lpuxa/sources/units'
for name, expected, coords in [('BFJ-v2-positive-products', '6c15466488dfc98ca2b08915a967e744399ae3309639ca9c3d543d686f895c8a', [310, 441]), ('BFJ-v2-volume-differentiation', '8651090225d1a0201460f316a49cd69fc8a7734a1a9d4dc29ded54b60aaf1c47', [445, 545])]:
    q = source_base / (name + '.txt')
    assert sha(q) == expected
    units.append({'file': str(q), 'sha256': expected, 'original_renderer_inclusive_zero_based': coords, 'whole_retained_unit_root_read_this_application': True, 'url': 'https://arxiv.org/html/math/0608260v2', 'new_application': 'Actual algebraic directed cofinality of complete moving systems in every lower power, smooth projective algclosed char0, with signed fixed tests decomposed before pairing. BFJ top positive product equals actual volume; no big-product multilinearity claimed.'})
L = K / 'P16.5-continuation208-root-source-application-and-read-scope-20261006.json'
save(L, {'recorded_utc': now, 'classification': b['classification'], 'whole_final_source_root_read': True, 'final_source_lines': 484, 'final_tex_sha256': sha(T), 'all7final_visual_pages_root_read': True, 'whole_mathematical_dependencies': deps, 'primary_units_for_this_application': units, 'new_derivations': ['Actual ample Qi perturbed from each dominated nef competitor inject via actual effective sections into full |qN|. This dominates all positive-product competitors and yields every lower directed moving product, not only top volume.', 'Every time-weight basis term is retained; the entire actual pulled generic fixed divisor is removed before principalizing vertical residual ideals, with one generic A_m for every fixed finite list.', 'All lower signed-test moving limits identify each raw central measure coefficient and pushed output; full section intercept identifies auxiliary energy. Actual density gives generic error zero.', 'Actual bounded section density from one genuine FS net, fixed positive ample gap, real feasible weights and integer power losses gives local-uniform U reference and obstacle convergence.', 'The fixed-m injected full section filtration retains quotient rank times min(f), then degree ell tends to infinity before m and before the infimum of continuous majorants.', 'Exact finite nef energy polynomial retains raw generic linear term and gives whole intrinsic quadratic contraction after the prescribed limits.', 'Floors16^j and contractions8^-j with weights2^-j give an actual finite-energy pole on the entire Kodaira divisor, without assuming all-test output integrability.', 'A countable gliding-hump actual finite-energy endpoint proves uniform unit-sublevel target integrability; contraction gives sublinear growth, finite intrinsic dual energy and quantitative coercivity.'], 'whole_S_M_axioms_granted': False, 'actual_nonample_conclusions_claimed_as_candidate': True, 'joint_independent_review_of207208_required': True, 'independent_acceptance': False, 'original_closed': False, 'unbounded_physical_reference_defect_resolved': False, 'new_primary_retrieval': False, 'whole_primary_sources_read': False, 'all_recursive_foundations_read': False, 'native_final_compile_success_observed': True, 'existing_editor_unchanged': True, 'active_private_outputs_read': False, 'hot_feedback_sent': False})
prior = json.loads((G / 'push-receipt-continuation172.json').read_text())
assert prior['commit_sha'] == 'a61bb373885ed4a270f528a5eae0d51799931df8'
assert all(prior[x] for x in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
S = K / 'small-batch158163-public-status-20261006-continuation173'
S.mkdir()
items = []
for n in (158, 163):
    c = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'
    save(p, st)
    items.append({'round': n, 'atom': 'P16.5', 'directory': str(c), 'observed_status': st['status'], 'observed_utc': st['observedAt'], 'public_status': str(p), 'public_status_sha256': sha(p), 'private_active_output_read': False, 'hot_feedback_sent': False, 'original_closed': False})
active = [x for x in items if x['observed_status'] == 'running']
assert len(active) <= 2
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': 'Actual foundation158 audit and unchanged original163 author continue. New20720813-page actual-domain foundation reconstruction is separate unreviewed proof data; original-scope candidate assembly is next. Prepared165 unchanged and any complete original candidate audit has priority.'}
F = G / 'continuation173-publication-records'
F.mkdir()
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, current_small_batch=batch, P16_5_actual_complete_moving_and_relative_contraction208=b, github_pending_checkpoint='continuation173 frozen', goal_state='8/42 originals solved;34 open;63 accepted supporting papers. New2087-page actual finite-list moving foundations, all lower full positive products, retained rank trace, whole relative contraction, actual Kodaira E1 pole and intrinsic all-test dual-energy/coercivity reconstructed using complete unreviewed207 and accepted finite159/scalar160. New20720813-page proof requires joint independent review; complete original candidate assembly next. Active158 and unchanged163 continue; prepared165 unchanged; maximum two campaigns and no active feedback.')
    for target in j.get('targets', []):
        if target['id'] == 'P16.5': target['current_focus'] = batch['focus']
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
lines = (R / 'checklist-current.tsv').read_text().splitlines()
for i, line in enumerate(lines):
    row = line.split('\t')
    if row[0] == 'P16.5': row[2] = 'New20720813-page actual foundation reconstruction unreviewed; full original candidate assembly next. Active158163; prepared165 unchanged.8/42 originals,63 supports; original open.'
    lines[i] = '\t'.join(row)
(R / 'checklist-current.tsv').write_text('\n'.join(lines) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'): shutil.copyfile(R / name, F / name)
save(F / 'scope-observation.json', {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_papers': 63, 'new_unreviewed_continuation': 208, 'pages': 7, 'joint207208_pages': 13, 'new_original_closure': None, 'active_batch': [x['round'] for x in active], 'prepared165_unchanged': True, 'active_private_outputs_read': False, 'hot_feedback_sent': False})
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.aux', '.out')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation173/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()): add(p)
for p in (T, D / 'paper.pdf', D / 'publication-binding.json', L, G / 'push-receipt-continuation172.json', R / 'record_verified172_20261006.py', Path(__file__)): add(p)
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'): add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
M = G / 'upload-manifest-continuation173.json'
save(M, {'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': front['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 63, 'commit_message': 'Record actual complete moving foundations and relative contraction', 'scope': 'New2087-page actual-domain reconstruction together with unreviewed companion207. All lower complete moving products and fixed signed tests, whole shared generic A_m and horizontal-factor extraction, auxiliary energy/weak raw limits, original U section density, retained degree-first missing-rank trace, whole relative quadratic contraction, genuine E1 Kodaira pole and intrinsic target equivalence/coercivity. All484 final LF and7final visual pages ROOT read; native final compiled. Joint new proofs remain unreviewed; counts8/42 and63 unchanged. Active158 and unchanged163 and frozen165 unchanged; no active-private read or feedback.'})
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(files), 'statuses': [{'round': x['round'], 'status': x['observed_status']} for x in items]}, indent=2))
