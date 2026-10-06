from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess
R = Path('/workspace/research')
K = R / 'root-checks'
G = R / 'github-checkpoint'
now = datetime.now(timezone.utc).isoformat()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p, value):
    assert not p.exists(), str(p)
    p.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
T = K / 'P16.5-convex-energy-completion-and-general-mixed-stability-candidate-20261006-continuation206.tex'
D = K / 'public-P16.5-continuation206-general-mixed-stability-reader'
assert sha(T) == '4b3cf4cbbb4f856c4632359dee9f9e44e5d3d00f7dc4593b709b66bda3c33543'
assert sha(D / 'paper.pdf') == sha(T.with_suffix('.pdf')) == 'bd28b8d2b87d4f68a9c6d48f4f54776ad12f72a98c6a7e56c71c85e6fe306933'
assert len(T.read_text().splitlines()) == 229
assert not any(s in T.with_suffix('.log').read_text() for s in ('Warning:', 'Overfull', 'Underfull', 'undefined'))
b = {'recorded_utc': now, 'classification': 'Unreviewed conditional206: uniform real-simplex energy completion derived from individual genuine convergence; all genuine mixed and independent weighted stability.', 'tex': str(T), 'tex_sha256': sha(T), 'pdf': str(D / 'paper.pdf'), 'pdf_sha256': sha(D / 'paper.pdf'), 'pages': 3, 'source_lines': 229, 'whole_final_tex_root_read': True, 'whole_final_tex_root_read_chunks': ['whole final229LF after exact constant-invariance and paragraph corrections'], 'actual_visual_pages': [1, 2, 3], 'final_visual_image_hashes': {str(n): sha(D / f'page-{n}.png') for n in range(1, 4)}, 'final_two_pass_local_build_succeeded': True, 'warnings': 0, 'overfull': 0, 'underfull': 0, 'undefined': 0, 'native_compile_request_cell': '602', 'native_final_compile_success_observed': True, 'native_compile_success_observed': True, 'native_final_success_message': "The current source compiled successfully with the desktop editor's compiler.", 'existing_editor_unchanged': True, 'independent_acceptance': False, 'original_closed': False, 'accepted_paper_count_unchanged': 63, 'scope': 'Whole genuine supporting planes and the absolute midpoint modulus derive uniform real-simplex energy convergence from each independently indexed genuine weak-and-energy input, without assuming barycenter completion. Whole205 diagonal output and weighted limits at fixed rational parameters, with whole202 fixed-degree polynomial identities and fixed unisolvent matrices, give all genuine mixed outputs, energy coefficients and independently changing weak cost-bounded tests.', 'remaining': 'Actual whole nonample foundations and independent acceptance of204205206; physical fixed-original-test reference defect remains unresolved. Prepared165 retains its exact earlier17-page scope and receives no206 feedback.'}
save(D / 'publication-binding.json', b)
front = json.loads((R / 'active-work.json').read_text())
data = []
for key in ('P16_5_completed_partial159', 'P16_5_conditional_filtered_trace_and_genuine_mixed202', 'P16_5_genuine_affine_and_weighted_stability205'):
    p = Path(front[key]['tex'])
    assert sha(p) == front[key]['tex_sha256']
    data.append({'front_key': key, 'file': str(p), 'sha256': sha(p), 'whole_body_previously_root_read': True, 'authority': 'Only the stated finite/conditional mathematical signature. Supporting-paper status does not assert actual nonample antecedents.'})
L = K / 'P16.5-continuation206-root-source-application-and-read-scope-20261006.json'
save(L, {'recorded_utc': now, 'classification': b['classification'], 'final_tex_sha256': sha(T), 'whole_final_source_root_read': True, 'final_source_lines': 229, 'all3final_visual_pages_root_read': True, 'conditional_proof_data': data, 'new_derivations': ['Each genuine weak-and-energy input has vanishing midpoint defect by weak usc and concavity.', 'At either output of a convex combination, whole159 absolute moment is uniformly bounded by C D^(1-alpha) times each individual midpoint defect^alpha. Two actual whole supporting planes give the two signed energy bounds.', 'The weighted sum of those defects has supremum at most their finite maximum; hence every real-simplex barycenter energy converges uniformly without an added completion hypothesis.', 'At fixed rational unisolvent points, whole205 applies to actual genuine barycenters. Fixed inverse interpolation with raw multinomial coefficients gives every genuine positive mixed weak coefficient. Degree n+1 interpolation gives energy coefficients.', 'At the same finite points, the independent changing-test diagonal weighted theorem and a fixed measure identity give all mixed weighted limits on product-directed indices. No moving parameter or support indicator is passed through weak convergence.', 'Diagonal constant invariance implies each mixed-slot constant invariance by fixed interpolation. Original generic energy and test constants are restored with raw V.'], 'all_required_conditional_signatures_explicit': True, 'barycenter_energy_completion_assumed': False, 'interpolation_claims_positivity_without_input': False, 'actual_nonample_foundations_asserted_true': False, 'physical_auxiliary_output_substituted_for_genuine': False, 'new_primary_retrieval': False, 'whole_primary_sources_read': False, 'all_recursive_foundations_read': False, 'elementary_background': 'Finite real polynomial uniqueness on an open cone and selection of a fixed rational invertible evaluation matrix; no source-dependent new NA theorem.', 'native_final_compile_success_observed': True, 'independent_acceptance': False, 'original_closed': False, 'accepted_paper_count_unchanged': 63, 'active_private_outputs_read': False, 'hot_feedback_sent': False})
prior = json.loads((G / 'push-receipt-continuation170.json').read_text())
assert prior['commit_sha'] == '4e9caa569adf91337807ebd47c53cdcbc2313b68'
assert all(prior[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
S = K / 'small-batch158163-public-status-20261006-continuation171'
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
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': 'Actual foundation158 audit and unchanged full original163 author. Prepared165 unchanged, with whole20320420517-page scope; new206 remains separate unreviewed proof data. Original candidate review takes priority.'}
F = G / 'continuation171-publication-records'
F.mkdir()
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, current_small_batch=batch, P16_5_convex_energy_completion_and_general_mixed_stability206=b, github_pending_checkpoint='continuation171 frozen', goal_state='8/42 originals solved;34 open;63 accepted supporting papers. New2063-page unreviewed uniform real-simplex genuine barycenter energy completion derived from individual inputs, all mixed output and independently weighted test convergence using205 and202. Actual foundations and physical reference defect remain open. Actual158 and full unchanged163 continue; maximum two campaigns. Prepared165 remains unchanged at17 pages and new206 is separate.')
    for target in j.get('targets', []):
        if target['id'] == 'P16.5':
            target['current_focus'] = batch['focus'] + ' New206 completes genuine barycenter/mixed stability conditionally; full original open.'
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
lines = (R / 'checklist-current.tsv').read_text().splitlines()
for i, line in enumerate(lines):
    row = line.split('\t')
    if row[0] == 'P16.5':
        row[2] = 'New2063-page unreviewed derived uniform real-simplex barycenter energies and all genuine mixed/independent weighted stability. Actual158 and full original163 active; prepared165 unchanged.8/42 originals,63 accepted supports; original open.'
    lines[i] = '\t'.join(row)
(R / 'checklist-current.tsv').write_text('\n'.join(lines) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    shutil.copyfile(R / name, F / name)
save(F / 'scope-observation.json', {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_papers': 63, 'new_unreviewed_continuation': 206, 'pages': 3, 'new_original_closure': None, 'active_batch': [x['round'] for x in active], 'prepared_review165_unchanged': True, 'active_private_outputs_read': False, 'hot_feedback_sent': False, 'native_final_compile_success_observed': True, 'existing_editor_unchanged': True})
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.aux', '.out')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation171/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()):
        add(p)
for p in (T, D / 'paper.pdf', D / 'publication-binding.json', L, G / 'push-receipt-continuation170.json', R / 'record_verified170_20261006.py', R / 'launch_frozen_support_review165_20261006.py', Path(__file__)):
    add(p)
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
M = G / 'upload-manifest-continuation171.json'
save(M, {'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': front['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 63, 'commit_message': 'Record derived convex energy completion and general genuine mixed stability', 'scope': 'New2063-page unreviewed whole genuine uniform real-simplex energy completion from each input, without barycenter assumptions; whole205 fixed diagonal and weighted convergence and202 fixed raw interpolation yield every genuine mixed/independently weighted limit and energy coefficient. All229 final source lines and3visual pages ROOT read; native602 compiled. Prepared16517-page audit remains frozen unchanged, with ready guarded launcher. Actual158 and full unchanged163 continue; counts8/42 and63 unchanged. No actual foundation, physical reference-defect, active private read or hot-feedback claim.'})
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(files), 'statuses': [{'round': x['round'], 'status': x['observed_status']} for x in items]}, indent=2))
