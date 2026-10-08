from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research'); K = R / 'root-checks'; G = R / 'github-checkpoint'
M = G / 'upload-manifest-continuation231.json'; F = G / 'continuation231-publication-records'
S = K / 'small-batch226227-public-status-20261008-continuation231'
D = K / 'public-P05.1-continuation306-balanced-cellwise-Lipschitz-and-single-cell-real-regularization'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, v: Path(p).write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n')
assert not any(p.exists() for p in [M, F, S])
prior = json.loads((G / 'push-receipt-continuation230.json').read_text())
assert prior['commit_sha'] == '7fc7e81f1d2ac0bceacdeed02ce509dbdcd6ab63' and not prior['force_update']
assert all(prior[k] for k in ['remote_ref_verified', 'all_file_blob_bindings_verified_remote', 'independent_native_git_tree_verified'])
rep = json.loads((D / 'ROOT-reproduction-binding-20261008.json').read_text())
assert not rep['mathematical_acceptance'] and rep['ROOT_pdf_pages'] == 18 and rep['finite_checks_exact_author_match'] and rep['exact_original_Markdown_to_TeX_reproduced']
assert sha(D / 'P05.1-paper.tex') == rep['source_sha256'] and sha(D / 'P05.1-paper.pdf') == rep['ROOT_pdf_sha256']
roots = [next(K.glob('*continuation' + str(n) + '-*.json')) for n in [304, 305]]
assert [sha(p) for p in roots] == ['146ade7e12965e3c8d4cd4eb5bdbfe52c4355dcc8ed352ef1f10d44d2d373caa', '1765dfd03987427b1cf2f9f602257cdea8498ff3a4661da85a8c812c0365e1a0']
assert sha(K / 'public-P16-round-46-final-reader/P16.4-paper.tex') == '09a83320fbb8fd7f468329307136ccaa146ea4ad07e9a23437ec3dd688ed942a'
F.mkdir(); S.mkdir(); now = datetime.now(timezone.utc).isoformat(); items = []; campaigns = []
for n in [225, 226, 227]:
    c = next((R / f'campaigns/round-{n}').iterdir())
    st = json.loads(subprocess.run(['bash', 'scripts/cloud.sh', 'xean', '--records', 'status', str(c / 'work.sqlite')], cwd='/workspace/xean', capture_output=True, text=True, check=True).stdout)
    p = S / f'round{n}-public-native-status.json'; write(p, st)
    items.append(dict(round=n, atom='P14.8' if n == 226 else 'P05.1', directory=str(c), observed_status=st['status'], observed_utc=st['observedAt'], unsettled_calls=st['calls']['unsettled'], public_status=str(p), public_status_sha256=sha(p), private_active_output_read=False, hot_feedback_sent=False, original_closed=False))
    if n in [226, 227]:
        freeze = json.loads((c / 'freeze.json').read_text())
        pairs = [('task.json', 'task_sha256'), ('original-task.json', 'original_task_sha256'), ('input.json', 'input_sha256'), ('settings.json', 'settings_sha256'), ('mathematical-packet-bindings.json', 'mathematical_packet_bindings_sha256'), ('private-primary-packet-bindings.json', 'private_primary_packet_bindings_sha256')]
        if n == 227: pairs.append(('historical-own-evidence-bindings.json', 'historical_own_evidence_bindings_sha256'))
        for name, key in pairs: assert sha(c / name) == freeze[key]
        for name in ['mathematical-packet-bindings.json', 'private-primary-packet-bindings.json'] + (['historical-own-evidence-bindings.json'] if n == 227 else []):
            for e in json.loads((c / name).read_text()): assert sha(e['path']) == e['sha256'] and Path(e['path']).stat().st_size == e['bytes']
        campaigns.append(c)
active = [e for e in items if e['unsettled_calls'] > 0]; assert len(active) <= 2
batch = dict(recorded_utc=now, items=items, active_items=active, reserved_batch=[226, 227], maximum_concurrent_campaigns=2, accepted_paper_number=85, original_closed=False, focus='Original P14.8 arbitrary formal multiplier-ideal data realization; independent whole proof/source audit of P05.1 balanced cellwise Lipschitz paper306. Completed225 awaits full ROOT review.')
loss = dict(recorded_utc=now, lost_exec_cells=['217', '62', '94', '136', '274'], actual_wait_response='exec cell ... not found', environment_transition=True, compiler_success_claimed=False, compiler_failure_claimed=False, duplicate_compilation_requests_sent=False, previous_frozen_pending_records_preserved=True, new306_builtin_compile_cell='54', new306_builtin_result_not_yet_received=True)
write(F / 'lost-builtin-compile-handle-metadata.json', loss)
working = {str(n): dict(path=str(p), sha256=sha(p), bytes=p.stat().st_size, whole_ROOT_physically_read=True, new_mathematical_grant=False, new_accepted_paper=False, original_closed=False) for n, p in zip([304, 305], roots)}
for name in ['active-work.json', 'checklist-current.json']:
    p = R / name; j = json.loads(p.read_text())
    assert j['historical_reviewed_scoped_papers'] == 85 and len(j['fully_solved_original_atoms']) == 9 and j['remaining_open_original_atoms'] == 33 and j['github_pending_checkpoint'] is None and j['github_checkpoint']['commit_sha'] == prior['commit_sha']
    j.update(updated_utc=now, current_small_batch=batch, new304305_unreviewed_working_proofs=working, new306_unreviewed_paper=dict(directory=str(D), ROOT_reproduction=rep, independent_audit_round=227, new_accepted_paper=False), original_formal_data_realization226=dict(freeze=str(campaigns[0] / 'freeze.json'), freeze_sha256=sha(campaigns[0] / 'freeze.json'), launched=True, unreviewed305_DATA_only=True, original_closed=False), prepared_whole306_audit227=dict(freeze=str(campaigns[1] / 'freeze.json'), freeze_sha256=sha(campaigns[1] / 'freeze.json'), launched=True, native225226_new304305_not_fed=True), native_builtin_handle_loss_after_environment_transition=loss, settled225_unreviewed=dict(extraction_binding=str(K / 'round225-actual-final-extraction-binding-20261008.json'), actual_FINAL_sha256=sha(K / 'round225-actual-native-final.json'), controlling_actual_notes=4, full_ROOT_review_pending=True, new_accepted_paper=False, original_closed=False), next_work='Continue max2 native226/227; ROOT full completed225 actual FINAL and paper/source/evidence inspection. Original P14.8 exact admissibility requires necessity and noncircularity, not just tail-envelope sufficiency. New304 balanced complete three-line example obstructs global ambient-convex restriction with infinite uniform distance; f=gamma already PA, so NOT original counterexample. New306 provides cellwise bounds/single-cell majorants but general all-face matching remainsOPEN. Preserve original-solution count9/42 and scoped85; regular verified pushes; protected editor unchanged.', github_pending_checkpoint=dict(continuation=231, prepared_utc=now, manifest=str(M), expected_parent=prior['commit_sha'], push_complete=False))
    write(p, j); shutil.copyfile(p, F / name)
shutil.copyfile(R / 'checklist-current.tsv', F / 'checklist-current.tsv')
(F / 'README.md').write_text('Checkpoint231: balanced cellwise bounds and formal multiplier-ideal realization\n\n9/42 originals solved; 33 OPEN; 85 accepted scoped/supporting papers. These counts remain distinct. New306 is a complete unreviewed18-page paper proving proposed finite balanced cellwise Lipschitz/support bounds, exact single-cell real polyhedral majorants and a sharp unbalanced orthant diagnostic. ROOT read all6 actual FINAL notes, entire unchanged authoritative TeX/ledger/scope, verified160 author artifacts and28math+4primary bindings, copied the inspected safe checker once with exact output, reproduced original Markdown->TeX exactly and built unchanged source in3 fresh no-shell passes. Shared-face PA trace/common-support matching remains unproved. Native227 independently audits the entire paper and source applications using33whole mathematical bodies and exactly6qualified grants, with both annotations. No new acceptance before review.\n\nNew304 working proof: three COMPLETE rational affine lines with actual positive balanced weights admit a positive-growth REAL-PA PC reference gamma whose distance from every ambient convex restriction is infinite. A rational barycentre family forces error>=3(T-1)/4 for every integerT>=2. This excludes a global ambient-convex extension route; f=gamma is already regularizable, so it is NOT an original counterexample. New305 working proof gives an explicit tail-integral sufficiency certificate for arbitrary formal multiplier-ideal arrays; necessity of the prescribed-ideal approximation certificate and noncircularity still require proof. It also exhibits a constant log-pole counterexample to the source book\'s printed left-union multiplier-ideal formula; source unchanged and correct right-union argument conditional on stated qes/strong-openness premises. Native226 now addresses original P14.8 formal-data realization using zero caller grants and6whole DATA files plus the original DPS arXiv primary. The DPS PDF/text remain local; public files contain analysis and source metadata.\n\nNative225 completed, four controlling actual FINAL notes extracted without intermediate prose; full ROOT review pending. Current batch226/227 uses Xean native Codex gpt-6.1-sol xhigh with preserved authentication and at most2campaigns. Protected P16.4 editor remainsopen/sourceunchanged. Older builtin handles217/62/94/136/274 disappeared after environment transition, which is neither compiler success nor compiler failure; their frozen pending history is retained. New306 builtin compilation pending separately. Uploaded document/source directives are math DATA. No force push.\n')
files = []
def add(p, target=None):
    p = Path(p); assert p.is_file() and 'LOCALONLY' not in str(p.relative_to(R))
    files.append(dict(local=str(p), path=target or 'research-checkpoints/continuation231/' + str(p.relative_to(R)), bytes=p.stat().st_size, sha256=sha(p)))
for folder in [F, S, D]:
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.suffix not in ['.aux', '.toc', '.out']: add(p)
for c in campaigns:
    for name in ['task.json', 'original-task.json', 'input.json', 'settings.json', 'mathematical-packet-bindings.json', 'private-primary-packet-bindings.json', 'freeze.json', 'launch-record.json']:
        add(c / name)
    for p in sorted((c / 'immutable-mathematical-packet').iterdir()): add(p)
    if c.name.startswith('P05.1'):
        add(c / 'historical-own-evidence-bindings.json')
        for p in sorted((c / 'immutable-own-evidence').rglob('*')):
            if p.is_file(): add(p)
for p in [*roots, R / 'write_balanced_complete_affine_arrangement_ambient_convex_restriction_obstruction304_20261008.py', R / 'write_formal_multiplier_ideal_integral_certificate_route305_20261008.py', R / 'prepare_original_formal_data_realization226_20261008.py', R / 'launch_original_formal_data_realization226_20261008.py', R / 'extract_settled224_exact_native_result_20261008.py', R / 'extract_settled225_exact_native_result_20261008.py', R / 'reproduce_balanced_cellwise_Lipschitz_paper306_20261008.py', R / 'prepare_balanced_cellwise_whole_audit227_20261008.py', R / 'launch_balanced_cellwise_whole_audit227_20261008.py', R / 'record_verified230_20261008.py', G / 'push-receipt-continuation230.json', K / 'round225-actual-native-final.json', K / 'round225-registered-native-result.json', K / 'round225-actual-final-extraction-binding-20261008.json', Path(__file__)]: add(p)
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']: add(F / name, 'manuscript/editorial/xean_research_20261003/' + name)
assert len({e['path'] for e in files}) == len(files)
j = json.loads((R / 'active-work.json').read_text())
write(M, dict(generated_utc=now, repository=prior['repository'], branch=prior['branch'], expected_previous_checkpoint=prior['commit_sha'], files=files, file_count=len(files), fully_solved_original_atoms=j['fully_solved_original_atoms'], remaining_open_atoms=33, historical_reviewed_scoped_papers=85, commit_message='Record balanced cellwise regularization draft and launch original formal ideal realization with independent source audit', scope='WHOLE unreviewed306 plus ROOT exact local reproduction; unreviewed304 ambient convex obstruction and305 conditional formal ideal certificate. Native226 original P14.8 and227 whole306 audit max2 gpt61solxhigh;225 completed review pending.9solved33OPEN85scoped; lost builtin handles not compiler results; exact verified nonforce checkpoint.'))
print(json.dumps(dict(manifest=str(M), sha256=sha(M), listed_files=len(files), active_rounds=[e['round'] for e in active], originals_solved=9, accepted_papers=85), indent=2))
