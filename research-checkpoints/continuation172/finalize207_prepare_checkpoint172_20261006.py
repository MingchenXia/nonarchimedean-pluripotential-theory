from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K, G = R / 'root-checks', R / 'github-checkpoint'
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

T = K / 'P16.5-actual-outer-energy-and-full-volume-derivative-candidate-20261006-continuation207.tex'
D = K / 'public-P16.5-continuation207-actual-outer-energy-reader'
assert sha(T) == '13b2ddfd3fb9fe3365b9a3177f00dd2d616f0c89b39e289e3d820339a0ad3722'
assert sha(D / 'paper.pdf') == sha(T.with_suffix('.pdf')) == '3b3fbc5ecd1dff06b26104d342c5c180946f474d4d3373a2e9305f33b12e71d9'
assert len(T.read_text().splitlines()) == 466
assert not any(x in T.with_suffix('.log').read_text() for x in ('Warning:', 'Overfull', 'Underfull', 'undefined'))
binding = {
    'recorded_utc': now,
    'classification': 'Unreviewed actual-domain construction207 from independently accepted scalar160 and unconditional finite159; no whole-energy or whole-operator axiom granted.',
    'tex': str(T), 'tex_sha256': sha(T), 'pdf': str(D / 'paper.pdf'), 'pdf_sha256': sha(D / 'paper.pdf'),
    'pages': 6, 'source_lines': 466, 'whole_final_tex_root_read': True,
    'whole_final_tex_root_read_chunks': ['whole466 final LF after bibliography and spacing corrections'],
    'actual_visual_pages': list(range(1, 7)),
    'final_visual_image_hashes': {str(n): sha(D / f'page-{n}.png') for n in range(1, 7)},
    'final_two_pass_local_build_succeeded': True, 'warnings': 0, 'overfull': 0, 'underfull': 0, 'undefined': 0,
    'native_final_compile_success_observed': True,
    'native_final_success_message': "The current source compiled successfully with the desktop editor's compiler.",
    'existing_editor_unchanged': True, 'independent_acceptance': False, 'original_closed': False,
    'accepted_paper_count_unchanged': 63,
    'scope': 'Actual full-section continuous trace and outer energy on the literal whole genuine big rational cone; finite divisorial planes, weak usc, decreasing continuity and actual finite-energy compactness; target-independent raw-V original derivative from both signed finite Taylor limits; two-sided touching model-envelope compatibility; all weak-and-energy output convergence; algebraic and reference-pole nullness.',
    'remaining': 'Independent review of the new whole construction. Quadratic contraction, full finite-list moving signatures and unbounded physical weighted reference defect are separate obligations. Original P16.5 remains open.',
}
save(D / 'publication-binding.json', binding)
proof_inputs = []
for n, scope in [(159, 'Only unconditional finite Section4: full lattice/intercept, finite derivative/refinement, positive deficient tail and corrected signed uniform Taylor; no conditional S-M package.'), (160, 'Only actual scalar Sections2-4: literal one-net closure, genuine envelopes, divisorial order and normalized compactness from G0/G1.')]:
    folder = K / ('public-P16.5-round159-partial-conditional-attainment-reader' if n == 159 else 'public-P16.5-round160-partial-negligible-transfer-reader')
    b = json.loads((folder / 'publication-binding.json').read_text())
    assert b['independent_acceptance'] and b['review_verdict'] == 'PASS'
    assert sha(folder / 'paper.tex') == b['tex_sha256']
    proof_inputs.append({'round': n, 'whole_source': str(folder / 'paper.tex'), 'source_sha256': b['tex_sha256'], 'whole_body_previously_root_read': True, 'review': b['review'], 'review_sha256': b['review_sha256'], 'exact_new_application_scope': scope})
L = K / 'P16.5-continuation207-root-source-application-and-read-scope-20261006.json'
save(L, {
    'recorded_utc': now, 'classification': binding['classification'], 'whole_final_source_root_read': True,
    'final_source_lines': 466, 'final_tex_sha256': sha(T), 'all6final_visual_pages_root_read': True,
    'independently_checked_mathematical_inputs': proof_inputs,
    'new_derivations': ['Finite filtration has finitely many attained weights by independence of vectors of distinct weights; full trace extends the exact model intercept.', 'Section feasible inequalities prove the outer-envelope energy identity without infinity subtraction.', 'Compact strict margins prove all decreasing-net energy continuity, including minus infinity.', 'Finite support permits swapping two infima; actual genuine and usc energy equals global finite-coordinate supporting planes.', 'Canonical nonpositive model majorants and corrected two-sided finite Taylor give the whole target-independent derivative, raw mass V, and every absolute C0 direction.', 'An inequality touching at zero and both derivatives identify M(P f_D) with finite mu_D before any ordered-output continuity.', 'Weak usc perturbed energy and uniform Taylor yield all weak-and-energy output convergence.', 'The positive deficient tail and an effective-horizontal derivative bound give nullness of every proper algebraic subset, with fixed continuous caps before the model limit.'],
    'whole_energy_axiom_granted': False, 'whole_operator_axiom_granted': False,
    'actual_nonample_conclusions_claimed_as_candidate': True, 'independent_acceptance': False, 'original_closed': False,
    'quadratic_contraction_or_all_test_integrability_claimed_here': False,
    'unbounded_physical_weighted_reference_defect_resolved': False,
    'new_primary_retrieval': False, 'whole_primary_sources_read': False, 'all_recursive_foundations_read': False,
    'ordinary_algebraic_inputs': 'Precisely those in accepted finite159 and independently verified round161: smooth char0 volume asymptotics, volume C1/positive-product order and normal section descent. No new algebraic domain extension.',
    'native_final_compile_success_observed': True, 'existing_editor_unchanged': True,
    'active_private_outputs_read': False, 'hot_feedback_sent': False,
})
prior = json.loads((G / 'push-receipt-continuation171.json').read_text())
assert prior['commit_sha'] == 'e9d743fdbe9d7e73b453965a954cf50f7b284e88'
assert all(prior[x] for x in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
S = K / 'small-batch158163-public-status-20261006-continuation172'
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
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': 'Actual foundation158 review and unchanged original163 author continue. New207 actual outer-energy/derivative construction is separate unreviewed proof data; frozen165 remains unchanged. Complete original candidate review has priority.'}
F = G / 'continuation172-publication-records'
F.mkdir()
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, current_small_batch=batch, P16_5_actual_outer_energy_and_full_volume_derivative207=binding, github_pending_checkpoint='continuation172 frozen', goal_state='8/42 originals solved;34 open;63 accepted supporting papers. New2076-page actual-domain outer section energy and target-independent raw-V derivative constructed from accepted scalar160 and unconditional finite159, with two-sided touching compatibility and all weak-energy output continuity. New construction remains unreviewed; original open. Actual158 and unchanged original163 continue; at most two campaigns. Prepared165 unchanged; no active private reads or feedback.')
    for target in j.get('targets', []):
        if target['id'] == 'P16.5': target['current_focus'] = batch['focus']
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
lines = (R / 'checklist-current.tsv').read_text().splitlines()
for i, line in enumerate(lines):
    row = line.split('\t')
    if row[0] == 'P16.5': row[2] = 'New2076-page unreviewed actual full outer-energy/derivative construction from accepted scalar160 and finite159. Actual158 and original163 active; prepared165 unchanged.8/42 originals,63 accepted supports; original open.'
    lines[i] = '\t'.join(row)
(R / 'checklist-current.tsv').write_text('\n'.join(lines) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'): shutil.copyfile(R / name, F / name)
save(F / 'scope-observation.json', {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_papers': 63, 'new_unreviewed_continuation': 207, 'pages': 6, 'new_original_closure': None, 'active_batch': [x['round'] for x in active], 'prepared165_unchanged': True, 'active_private_outputs_read': False, 'hot_feedback_sent': False})
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.aux', '.out')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation172/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()): add(p)
for p in (T, D / 'paper.pdf', D / 'publication-binding.json', L, G / 'push-receipt-continuation171.json', R / 'record_verified171_20261006.py', Path(__file__)): add(p)
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'): add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
M = G / 'upload-manifest-continuation172.json'
save(M, {'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': json.loads((R / 'active-work.json').read_text())['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 63, 'commit_message': 'Record actual outer section energy and full-volume derivative construction', 'scope': 'New2076-page unreviewed actual whole-domain outer-energy/derivative construction from independently accepted scalar160 and unconditional finite159. Finite planes, signed variation, two-sided touching compatibility, general weak-energy continuity and algebraic nullness. All466 final source lines and6final visual pages ROOT read; native final compiler succeeded. No S2/M1 axiom grant, all physical weighted conclusion, original closure, active-private read or hot feedback. Frozen165 unchanged; actual158 and unchanged full original163 continue.'})
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(files), 'statuses': [{'round': x['round'], 'status': x['observed_status']} for x in items]}, indent=2))
