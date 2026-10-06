from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, subprocess

R = Path('/workspace/research')
K = R / 'root-checks'
C = next((R / 'campaigns/round-168').iterdir())
P = K / 'P19.2-round168-actual-canonical-author-result-20261006.json'
N = K / 'P19.2-round168-native-model-final-author-result-20261006.json'
B = K / 'P19.2-round168-completed-partial-original-and-input-binding-20261006.json'
D = K / 'public-P19.2-round168-partial-relative-levels-reader'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert not B.exists() and not D.exists()
j = json.loads((K / 'round168-completed-inspection-LOCALONLY.json').read_text())
kernel = j['campaign']['result']
native = json.loads(N.read_text())
assert j['campaign']['status'] == 'completed' and j['campaign']['error'] is None
assert json.loads(P.read_text()) == kernel
assert not native['candidate'] and not kernel['candidate']
assert len(native['notes']) == len(kernel['notes']) == 3
W = Path(kernel['workspace'])
normalization = []
for i, (a, b) in enumerate(zip(native['notes'], kernel['notes'])):
    assert {k: v for k, v in b.items() if k != 'text'} == {k: v for k, v in a.items() if k != 'text'}
    assert b['text'] == a['text'] + '\n\nArtifacts: ' + str(W)
    assert a['id'] == 'n' + str(i + 1)
    assert set(a['support']).issubset({x['id'] for x in native['notes'][:i]})
    normalization.append({'note_id': a['id'], 'unchanged_model_fields': ['id', 'summary', 'detailedSummary', 'text mathematical body', 'support'], 'only_added_text': '\n\nArtifacts: ' + str(W)})
payload = next(x['data']['payload'] for x in j['records'] if x['kind'] == 'xean.call.request')
message = next(x['data']['message'] for x in j['records'] if x['kind'] == 'xean.call.settled')
assert message['exitCode'] == 0 and not message['failed'] and not message['isCanceled']
prompt = json.loads(payload['prompt'])
assert set(prompt) == {'task', 'notes', 'assignment', 'workspace'}
assert prompt.pop('workspace') == str(W)
assert prompt == json.loads((C / 'input.json').read_text())
assert json.loads((W / 'input-frozen.json').read_text()) == prompt
assert payload['model'] == 'gpt-6.1-sol' and payload['reasoning'] == 'xhigh'
assert payload['sandbox'] == 'workspace-write' and payload['shell'] is True
f = json.loads((C / 'freeze.json').read_text())
for name, key in [('input.json', 'input_sha256'), ('task.json', 'task_sha256'), ('settings.json', 'settings_sha256')]:
    assert sha(C / name) == f[key]
assert f['input_sha256'] == '16862f135d05608a734623a38d5e2d7b953e34747d6f356d2e1d6b724fde1fae'
T = W / 'P19.2-paper.tex'
pdf = W / 'build/P19.2-paper.pdf'
assert sha(T) == '806d12236a7d6bfb8a15a143ae4ca6d60c08b1bb6d0419c399a39c18ca6f1f77'
assert sha(pdf) == 'e8dd90b3d1ed68b9f3fb4ed05b775faff7bba37bb8f527aebd3e8beb9563c1b9'
assert len(T.read_text().splitlines()) == 816
assert int(subprocess.check_output(['pdfinfo', str(pdf)], text=True).split('Pages:')[1].split()[0]) == 10
log = (W / 'build/P19.2-paper.log').read_text()
assert not any(s in log for s in ('Warning:', 'Overfull', 'undefined'))
assert log.count('Underfull') == 1
D.mkdir()
for source, name in [(T, 'P19.2-paper.tex'), (pdf, 'paper.pdf'), (W / 'P19.2-argument.md', 'P19.2-argument.md'), (W / 'source-application-ledger.json', 'source-application-ledger.json')]:
    shutil.copyfile(source, D / name)
record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'classification': 'Completed original author research returns candidate=false; unreviewed conditional/supporting results only.', 'round': 168, 'canonical_author_result': str(P), 'canonical_sha256': sha(P), 'native_model_final': str(N), 'native_model_final_sha256': sha(N), 'candidate': False, 'whole_all3canonical_notes_root_read': True, 'all3normalizations_root_read': True, 'normalization': normalization, 'original_frozen_task_sha256': f['task_sha256'], 'original_frozen_input_sha256': f['input_sha256'], 'original_frozen_settings_sha256': f['settings_sha256'], 'exact_decoded_native_task_notes_assignment_equal_complete_frozen_input': True, 'native_added_workspace_is_only_extra_prompt_field': str(W), 'native_prompt_sha256': hashlib.sha256(payload['prompt'].encode()).hexdigest(), 'native_input_frozen_bytes': (W / 'input-frozen.json').stat().st_size, 'native_input_frozen_sha256': sha(W / 'input-frozen.json'), 'native_input_frozen_is_json_reserialization_with_identical_complete_mathematical_content': True, 'model': payload['model'], 'reasoning': payload['reasoning'], 'child_sandbox': payload['sandbox'], 'native_exit_code': message['exitCode'], 'canceled': False, 'whole_standalone_source_root_read': True, 'source_lines': 816, 'source_sha256': sha(T), 'pdf_pages': 10, 'pdf_sha256': sha(pdf), 'all10final_visual_pages_root_read': True, 'actual_visual_pages': list(range(1, 11)), 'native_final_compile': 'SUCCESS', 'native_final_message': "The current source compiled successfully with the desktop editor's compiler.", 'worker_final_two_pass_compile': 'SUCCESS; final log has no LaTeX warnings/overfull/undefined; one harmless underfull bibliography paragraph at source808-814, final visual pages checked.', 'source_application_ledger_whole_root_read': True, 'root_new_primary_read_from_author_ledger': False, 'only_mathematical_grants': ['R', 'T', 'C', 'S', 'E'], 'exact_partial_results': ['Sufficient identical-start ordered affine comparison, with bounded error removed by finite-horizon comparison, recovers scalar closed levels and genuine relative ceilings pointwise/L1.', 'Under that comparison, finite initial entropy and infinite target entropy slope imply every joint entropy/time divergence, including nonmaximal targets.', 'Two actual hyperplane model rays have different genuine P levels but identical entire scalar mixed-mass profiles and same-time energy/entropy; this is information loss, not universal nonexistence.'], 'remaining_full_original_gaps': ['General positive model/flag existence retaining arbitrary prescribed starts and ray/data.', 'Nonmaximal ray and energy-defect recovery or qualifying full-signature universal obstruction.', 'General closed finer relative P density with specified topology.', 'All raw mixed-mass continuity at genuine/zero/placeholder boundaries.', 'Required entropy outside finite-initial-entropy grants and any needed fixed-time recovery.', 'General residual log-discrepancy positivity and joint regularization.'], 'research_result_not_supplied_to_review169': True, 'new_ROOT211_predates_completed168_result_read': True, 'independent_review169': 'Active on unchanged complete original211, with callerR only; no168 material or feedback supplied.', 'independent_acceptance': False, 'original_closed': False, 'originals_solved': 8, 'originals_open': 34, 'accepted_supporting_papers': 63, 'private_active_outputs_read': False, 'hot_feedback_sent': False, 'existing_editor_unchanged': True}
B.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
(D / 'publication-binding.json').write_bytes(B.read_bytes())
(D / 'README.md').write_text('# Completed P19.2 author168 partial results\n\nThe10-page standalone manuscript and actual native canonical result explicitly leave original P19.2 unresolved (candidate=false). It gives a conditional same-start affine comparison criterion and conditional joint infinite entropy recovery, and two actual hyperplane profiles illustrating scalar information loss. It does not give general model/flag existence, raw mixed-mass continuity or a qualifying full-original counterexample.\n\nROOT read the entire816-line source, all3 canonical notes and their normalization, source application ledger, and all10 PDF pages. Native compilation succeeded. These are reading/compilation/provenance checks, not independent mathematical acceptance. The input/task/assignment were checked against the exact unchanged whole168 frozen mathematical input. All counts remain8/42 originals and63 accepted supporting papers. This result was not sent to the active independent169 audit of earlier independent ROOT211.\n')
print(json.dumps({'binding': str(B), 'binding_sha256': sha(B), 'candidate': False, 'pages': 10, 'source_root_read': True, 'original_closed': False}, indent=2))
