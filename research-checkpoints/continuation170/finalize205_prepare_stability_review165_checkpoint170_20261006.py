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
T = K / 'P16.5-finite-affine-planes-and-genuine-stability-candidate-20261006-continuation205.tex'
D = K / 'public-P16.5-continuation205-genuine-stability-reader'
assert sha(T) == '4ea30e2999e3ff75cf059c1a5754f8b479f212b2d720524e4e771f7847b68172'
assert sha(D / 'paper.pdf') == sha(T.with_suffix('.pdf')) == '937f5a1e5d247ba9dcb087861e4922e468cac2a2927cb4e93cd4738818eedc21'
assert len(T.read_text().splitlines()) == 343
assert not any(s in T.with_suffix('.log').read_text() for s in ('Warning:', 'Overfull', 'Underfull', 'undefined'))
b = {'recorded_utc': now, 'classification': 'Unreviewed conditional205: finite-affine-plane usc envelope energy; genuine energy-convergence output stability; fixed-target absolute L1 on weak cost sublevels; independent changing-test weighted convergence at genuine outputs.', 'tex': str(T), 'tex_sha256': sha(T), 'pdf': str(D / 'paper.pdf'), 'pdf_sha256': sha(D / 'paper.pdf'), 'pages': 5, 'source_lines': 343, 'whole_final_tex_root_read': True, 'whole_final_tex_root_read_chunks': ['whole final343LF after exact normalization/reference corrections'], 'actual_visual_pages': [1, 2, 3, 4, 5], 'final_visual_image_hashes': {str(n): sha(D / f'page-{n}.png') for n in range(1, 6)}, 'final_two_pass_local_build_succeeded': True, 'warnings': 0, 'overfull': 0, 'underfull': 0, 'undefined': 0, 'native_compile_request_cells': ['584', '588', '592'], 'native_compile_request_cell': '592', 'native_final_compile_success_observed': True, 'native_compile_success_observed': True, 'native_final_success_message': "The current source compiled successfully with the desktop editor's compiler.", 'existing_editor_unchanged': True, 'independent_acceptance': False, 'original_closed': False, 'accepted_paper_count_unchanged': 63, 'scope': 'Under exact conditional antecedents: finite-coordinate planes extend section energy to usc obstacles and make every perturbed envelope energy weak usc; signed uniform Taylor gives output weak convergence along all genuine weak nets with converging energy. Finite-atomic dual density gives all fixed-target absolute L1 on bounded-cost weak nets. Whole204 four-point bound gives uniform dual convergence of genuine outputs; max identity and fixed canonical collars give every independent weak cost-bounded changing test weighted convergence on the product index.', 'remaining': 'Actual entire nonample energy/output/full-list foundations; independent checking of new204 and205; no fixed original unbounded test at physical auxiliary outputs or reference-defect claim.'}
save(D / 'publication-binding.json', b)
L = K / 'P16.5-continuation205-root-source-application-and-read-scope-20261006.json'
proof_data = []
front = json.loads((R / 'active-work.json').read_text())
for key in ('P16_5_completed_partial151', 'P16_5_completed_partial159', 'P16_5_conditional_filtered_trace_and_genuine_mixed202', 'P16_5_atomic_dual_density_before_attainment204'):
    p = Path(front[key]['tex'])
    proof_data.append({'front_key': key, 'file': str(p), 'sha256': sha(p), 'whole_body_previously_root_read': True, 'authority': 'Exact finite/conditional mathematical proof data; actual nonample foundations are not inferred from supporting-paper status.'})
save(L, {'recorded_utc': now, 'classification': b['classification'], 'final_tex_sha256': sha(T), 'whole_final_source_root_read': True, 'final_source_lines': 343, 'all5final_visual_pages_root_read': True, 'conditional_proof_data': proof_data, 'new_derivations': ['Interchange two infima at finite Div-support planes; cofinal continuous usc majorants use compactness with strict margins. No arbitrary measurable-net MCT.', 'Genuine envelopes of continuous majorants of u+th decrease to its actual envelope; energy continuity identifies its finite-affine-plane formula and weak usc.', 'For every weak-and-energy-convergent genuine net, uniform signed Taylor at bounded costs and weak usc of each fixed perturbation identify all output clusters. Constants are restored by raw V.', 'Uniform finite atomic dual approximation BEFORE inverse makes all fixed-target costs weak continuous. Actual max(u_i,u) and a triple relative-cost identity give absolute L1 on any weak cost-bounded net, with each-index full-measure sets separately.', 'Weak-and-energy convergence kills midpoint defects. The genuine four-point bound becomes uniform output dual convergence on a common cost sublevel.', 'That uniform dual bound transfers absolute changing-test L1 to varying genuine outputs with error4epsilon. Fixed canonical majorants give uniform ordered tails with error2epsilon; one fixed continuous collar precedes each output limit. Independent product indices and all generic constants are retained.'], 'genuine_versus_physical_scope': 'Every output in new stability/weighted theorems is M(actual genuine u); no auxiliary physical pushforward is substituted. The unresolved R-q_Tm reference defect is unchanged.', 'attained_inverse_used_to_prove_atomic_density': False, 'extra_antecedents_hidden': False, 'actual_nonample_foundations_asserted_true': False, 'new_primary_retrieval': False, 'whole_primary_sources_read': False, 'all_recursive_foundations_read': False, 'elementary_background': 'Continuous usc majorants and compactness on compact Hausdorff carriers; weak compactness and uniqueness of fixed-mass positive Radon measures, and uniform model density in complete G0.', 'native_final_compile_success_observed': True, 'independent_acceptance': False, 'original_closed': False, 'accepted_paper_count_unchanged': 63, 'active_private_outputs_read': False, 'hot_feedback_sent': False})

# Preserve the never-launched164 packet; the new whole205 needs a fresh audit.
Old = next((R / 'campaigns/round-164').iterdir())
assert not (Old / 'work.sqlite').exists() and not (Old / 'launch-record.json').exists()
oldf = json.loads((Old / 'freeze.json').read_text())
for name, key in [('task.json', 'task_sha256'), ('argument.md', 'argument_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(Old / name) == oldf[key]
C = R / 'campaigns/round-165/P16.5-whole-moving-atomic-and-genuine-stability-independent-review'
C.mkdir(parents=True)
task = json.loads((Old / 'task.json').read_text())
task['problem'] = task['problem'].replace('complete WHOLE203 (7 pages) and complete WHOLE204 (5 pages)', 'complete WHOLE203 (7 pages), complete WHOLE204 (5 pages) and complete WHOLE205 (5 pages)')
task['problem'] += """

Reconstruct EVERY new WHOLE205 proof under its explicit antecedents. Check that finite Div affine planes for continuous section energy extend to every usc obstacle by independent continuous majorants and an interchange of infima; finite support, not arbitrary measurable-net MCT, passes their coordinates. Check genuine decreasing closure and envelope order identifying P(u+th), energy continuity and weak usc of EVERY fixed perturbed envelope energy. Check the all-genuine weak-and-energy-convergence output theorem, uniform signed Taylor at one cost bound, generic normalization, both signs, fixed c then t then c limits and all original Radon clusters. Check fixed-target absolute L1 under only weak convergence and bounded cost, via actual max(u_i,u), finite atomic uniform dual density and a three-cost identity; each index has its own full-measure set and no uncountable intersection is used. Check every simultaneous weighted claim: midpoint defects tend to zero by weak usc and concavity; the whole204 four-point estimate gives uniform output dual convergence on one cost sublevel; changing tests at varying genuine outputs have error4epsilon, canonical ordered tails have error2epsilon; fixed bounded relative model tests use original C0 collars before output limits, with independent product indices and all generic constants restored. No actual nonample antecedent or physical reference-defect convergence is silently concluded.
"""
task['completionCriteria'] = task['completionCriteria'].replace('BOTH WHOLE203 and WHOLE204', 'ALL THREE WHOLE203, WHOLE204 and WHOLE205').replace('whole12-page support audit', 'whole17-page support audit')
save(C / 'task.json', task)
argument = (Old / 'argument.md').read_text()
bindings = json.loads((Old / 'mathematical-data-bindings.json').read_text())
for label, p in [('WHOLE205', T), ('205 OWN APPLICATION LEDGER', L)]:
    argument += '\nBEGIN COMPLETE MATHEMATICAL BODY ' + label + '\n' + p.read_text() + '\nEND COMPLETE MATHEMATICAL BODY\n'
    bindings['supplied'].append({'label': label, 'file': str(p), 'sha256': sha(p), 'bytes': p.stat().st_size, 'whole_body_supplied': True, 'authority': 'Whole new explicitly conditional proof and provenance only.'})
(C / 'argument.md').write_text(argument)
bindings['new_whole_proof_pages'] = 17
save(C / 'mathematical-data-bindings.json', bindings)
settings = json.loads((Old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r165/P16.5-whole-moving-atomic-genuine-stability'
save(C / 'settings.json', settings)
save(C / 'freeze.json', {'prepared_utc': now, 'round': 165, 'atom': 'P16.5', 'directory': str(C), 'prepared_only': True, 'task_sha256': sha(C / 'task.json'), 'argument_sha256': sha(C / 'argument.md'), 'argument_bytes': (C / 'argument.md').stat().st_size, 'settings_sha256': sha(C / 'settings.json'), 'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh', 'maximum_concurrent_campaigns': 2, 'new_whole_papers': [203, 204, 205], 'new_whole_pages': 17, 'original_closed': False, 'existing_editor_unchanged': True, 'superseded_prepared_only_round': 164})
save(Old / 'superseded-before-launch.json', {'recorded_utc': now, 'never_launched': True, 'frozen_task_sha256': oldf['task_sha256'], 'frozen_argument_sha256': oldf['argument_sha256'], 'frozen_settings_sha256': oldf['settings_sha256'], 'all_frozen_bytes_preserved': True, 'superseded_by': str(C), 'reason': 'New whole205 genuine finite-affine-plane and independent changing-test stability proofs require a fresh whole17-page audit. Preserve frozen164 rather than editing it.'})

prior = json.loads((G / 'push-receipt-continuation169.json').read_text())
assert prior['commit_sha'] == '2ec4386cbeec687e2a75a26b457ba9e7fd574aa0'
assert all(prior[k] for k in ('remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'))
S = K / 'small-batch158163-public-status-20261006-continuation170'
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
batch = {'recorded_utc': now, 'items': items, 'active_items': active, 'maximum_concurrent_campaigns': 2, 'focus': 'Actual foundation158 audit and unchanged full original163 author. Fresh whole17-page supporting review165 prepared only; complete original candidate review has priority when available.'}
F = G / 'continuation170-publication-records'
F.mkdir()
for name in ('active-work.json', 'checklist-current.json'):
    p = R / name
    j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 63 and len(j['fully_solved_original_atoms']) == 8 and j['remaining_open_original_atoms'] == 34
    j.update(updated_utc=now, current_small_batch=batch, P16_5_genuine_affine_and_weighted_stability205=b, prepared_support_review165=json.loads((C / 'freeze.json').read_text()), github_pending_checkpoint='continuation170 frozen', goal_state='8/42 originals solved;34 open;63 accepted supporting papers. New2055-page unreviewed conditional finite-plane usc perturbed energy, genuine weak-and-energy output stability, absolute fixed-target L1 on all weak energy sublevels and independent changing-test weighted convergence at genuine outputs. No physical reference-defect claim. Actual foundation158 and unchanged original163 active; at most two. Fresh whole17-page support review165 prepared only;164 never launched and frozen bytes preserved.')
    for target in j.get('targets', []):
        if target['id'] == 'P16.5':
            target['current_focus'] = batch['focus'] + ' New205 all-genuine stability and weighted independence conditional on whole204 and actual foundations; original open.'
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
lines = (R / 'checklist-current.tsv').read_text().splitlines()
for i, line in enumerate(lines):
    row = line.split('\t')
    if row[0] == 'P16.5':
        row[2] = 'New2055-page unreviewed genuine weak/energy output, fixed-target absolute L1 and independent weighted stability. Actual foundation158 and full original163 active; fresh whole17-page review165 prepared only.63 accepted supports,8/42 originals; full original open.'
    lines[i] = '\t'.join(row)
(R / 'checklist-current.tsv').write_text('\n'.join(lines) + '\n')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    shutil.copyfile(R / name, F / name)
save(F / 'scope-observation.json', {'recorded_utc': now, 'originals_solved': 8, 'originals_open': 34, 'accepted_papers': 63, 'new_unreviewed_continuation': 205, 'pages': 5, 'new_original_closure': None, 'active_batch': [x['round'] for x in active], 'prepared_only_review': 165, 'superseded_never_launched_review': 164, 'active_private_outputs_read': False, 'hot_feedback_sent': False, 'native_final_compile_success_observed': True, 'existing_editor_unchanged': True})
files = []
def add(p, remote=None):
    p = Path(p)
    assert p.is_file() and 'LOCALONLY' not in p.name and p.suffix not in ('.sqlite', '.png', '.log', '.aux', '.out')
    files.append({'local': str(p), 'path': remote or 'research-checkpoints/continuation170/' + str(p.relative_to(R)), 'bytes': p.stat().st_size, 'sha256': sha(p)})
for folder in (F, S):
    for p in sorted(folder.iterdir()):
        add(p)
for p in (T, D / 'paper.pdf', D / 'publication-binding.json', L, G / 'push-receipt-continuation169.json', R / 'record_verified169_20261006.py', R / 'prepare_unbounded_atomic_independent_review164_20261006.py', Old / 'superseded-before-launch.json', Path(__file__)):
    add(p)
for folder in (Old, C):
    for name in ('task.json', 'settings.json', 'argument.md', 'freeze.json', 'mathematical-data-bindings.json'):
        add(folder / name)
add(Old / 'caller-mathematical-application-clarifications.json')
for name in ('active-work.json', 'checklist-current.json', 'checklist-current.tsv'):
    add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
M = G / 'upload-manifest-continuation170.json'
save(M, {'generated_utc': now, 'repository': prior['repository'], 'branch': prior['branch'], 'expected_previous_checkpoint': prior['commit_sha'], 'files': files, 'file_count': len(files), 'fully_solved_original_atoms': front['fully_solved_original_atoms'], 'remaining_open_atoms': 34, 'historical_reviewed_scoped_papers': 63, 'commit_message': 'Record genuine affine and weighted stability with full support audit packet', 'scope': 'New2055-page unreviewed conditional finite-plane usc envelope energies and all genuine weak-and-energy output stability; absolute target L1 on arbitrary weak cost-bounded nets; four-point dual output convergence and every independent changing-test weighted genuine-output limit. All343 final source lines and5visual pages ROOT read; native final592 compiled. Fresh whole17-page review165 prepared only, preserving never-launched164. Actual foundations and physical fixed-original-test reference defect remain open; actual158 and full unchanged163 continue, at most two. Counts8/42 and63 unchanged; no active private reads/hot feedback.'})
print(json.dumps({'manifest': str(M), 'manifest_sha256': sha(M), 'files': len(files), 'prepared_review165': json.loads((C / 'freeze.json').read_text()), 'statuses': [{'round': x['round'], 'status': x['observed_status']} for x in items]}, indent=2))
