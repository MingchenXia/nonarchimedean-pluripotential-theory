from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil

R = Path('/workspace/research'); K = R / 'root-checks'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
out = []
for n, atom, worker, expected_status in ((171, 'P16.4', 'codex-89WpBw', 'completed'), (172, 'P14.4', 'codex-YpNB0s', 'blocked')):
    C = next((R / f'campaigns/round-{n}').iterdir()); W = C / 'artifacts' / worker
    inspection = K / (f'round{n}-completed-inspection-LOCALONLY.json' if n == 171 else f'round{n}-settled-inspection-LOCALONLY.json')
    x = json.loads(inspection.read_text()); ca = x['campaign']
    assert ca['status'] == expected_status
    assert ca['error'] == (None if n == 171 else 'Unknown, dead, or forward support: B')
    request = next(t['data']['payload'] for t in x['records'] if t['kind'] == 'xean.call.request')
    message = next(t['data']['message'] for t in x['records'] if t['kind'] == 'xean.call.settled')
    assert message['exitCode'] == 0 and not message['failed'] and not message['isCanceled']
    finals = []
    for line in message['stdout'].splitlines():
        item = json.loads(line)
        if item.get('type') == 'item.completed' and item.get('item', {}).get('type') == 'agent_message':
            try: f = json.loads(item['item']['text'])
            except (ValueError, TypeError): continue
            if isinstance(f, dict) and set(f) == {'notes', 'candidate'}: finals.append(f)
    assert len(finals) == 1; native = finals[0]
    assert native['candidate'] is False and len(native['notes']) == 3
    p = json.loads(request['prompt']); frozen = json.loads((C / 'input.json').read_text())
    assert set(p) == {'task', 'notes', 'assignment', 'workspace'}
    assert {k: v for k, v in p.items() if k != 'workspace'} == frozen
    assert p['workspace'] == str(W) and json.loads((W / 'input.json').read_text()) == frozen
    assert request['model'] == 'gpt-6.1-sol' and request['reasoning'] == 'xhigh'
    assert request['sandbox'] == 'workspace-write' and request['shell'] is True
    freeze = json.loads((C / 'freeze.json').read_text())
    for name, key in [('task.json', 'task_sha256'), ('input.json', 'input_sha256'), ('settings.json', 'settings_sha256')]: assert sha(C / name) == freeze[key]
    for unit in json.loads((C / 'mathematical-data-bindings.json').read_text()): assert sha(unit['source']) == unit['sha256']
    N = K / f'{atom}-round{n}-native-model-final-author-result-20261007.json'
    binding = K / f'{atom}-round{n}-settled-partial-author-input-binding-20261007.json'
    D = K / f'public-{atom}-round{n}-partial-reader'
    assert not any(q.exists() for q in (N, binding, D))
    N.write_text(json.dumps(native, ensure_ascii=False, indent=2) + '\n')
    normalizations = []
    canonical = None
    if n == 171:
        kernel = ca['result']; assert kernel['candidate'] is False and len(kernel['notes']) == 3
        for i, (a, b) in enumerate(zip(native['notes'], kernel['notes'])):
            assert {k: b[k] for k in a if k != 'text'} == {k: v for k, v in a.items() if k != 'text'}
            tail = '\n\nArtifacts: ' + str(W)
            assert b['text'] == a['text'] + tail
            normalizations.append({'note_index': i, 'unchanged_fields': ['id', 'summary', 'detailedSummary', 'support'], 'kernel_added_text_tail': tail, 'mathematical_text_unchanged': True})
        assert [z['support'] for z in native['notes']] == [[], ['n1'], ['n1', 'n2']]
        canonical = K / f'{atom}-round{n}-actual-canonical-author-result-20261007.json'
        assert not canonical.exists(); canonical.write_text(json.dumps(kernel, ensure_ascii=False, indent=2) + '\n')
    else:
        assert ca['result'] is None
        assert [z['support'] for z in native['notes']] == [[], ['n1'], ['B', 'n1']]
    D.mkdir()
    for name in (f'{atom}-paper.tex', f'{atom}-paper.pdf', f'{atom}-argument.md', 'source-application-ledger.json'):
        shutil.copyfile(W / name, D / name)
    shutil.copyfile(N, D / N.name)
    if canonical: shutil.copyfile(canonical, D / canonical.name)
    record = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'round': n, 'atom': atom, 'campaign_status': expected_status, 'campaign_error': ca['error'], 'candidate': False, 'actual_canonical_result': str(canonical) if canonical else None, 'actual_canonical_sha256': sha(canonical) if canonical else None, 'native_final': str(N), 'native_final_sha256': sha(N), 'native_result_published_by_kernel': n == 171, 'native_model_exit_success': True, 'native_result_all_note_fields_root_read': True, 'entire_standalone_tex_root_read': True, 'standalone_tex': str(D / f'{atom}-paper.tex'), 'standalone_tex_sha256': sha(D / f'{atom}-paper.tex'), 'standalone_tex_lines': len((D / f'{atom}-paper.tex').read_text().splitlines()), 'original_frozen_task_sha256': freeze['task_sha256'], 'original_frozen_input_sha256': freeze['input_sha256'], 'original_frozen_settings_sha256': freeze['settings_sha256'], 'native_prompt_sha256': hashlib.sha256(request['prompt'].encode()).hexdigest(), 'native_decoded_input_exactly_equals_frozen_after_workspace_removal': True, 'native_input_semantically_equals_frozen': True, 'native_input_byte_equality_not_claimed': True, 'native_input_sha256': sha(W / 'input.json'), 'kernel_normalizations': normalizations, 'failure_boundary': None if n == 171 else 'Complete native result settled successfully, but kernel publication failed because B is a caller-grant label absent from registered input notes. No canonical result exists. No failed work/result is mutated, replayed or accepted. Independent mathematical review may examine the complete standalone source and native unaccepted notes as research data.', 'only_complete_mathematical_grant': 'B complete originalP16.5 in its exact projective algebraically-closed trivial-characteristic-zero rational-bundle domain', 'independent_acceptance': False, 'original_closed': False, 'root_primary_reading_limit': 'Full author source, every final note field and whole quote-free application ledger were read; not every author-retrieved full source or recursive foundation was freshly read by ROOT.', 'all_pdf_pages_visual_read': False, 'native_compile': 'pending', 'private_active_output_read': False, 'hot_feedback_sent': False, 'protected_editor_unchanged': True}
    binding.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n'); shutil.copyfile(binding, D / binding.name)
    (D / 'README.md').write_text(f'# {atom} round{n}: unverified partial research\n\nThe original atom remains open; candidate=false. The complete standalone source, every final native note and the exact frozen task/input bindings were read. Independent mathematical review has not been completed.\n\n' + ('Round171 has an actual completed canonical author result. Its all-dimensional trivial-valuation descent theorem does not cover the original nontrivial/nondiscrete field axis.\n' if n == 171 else 'Round172 native submission settled successfully but kernel publication failed on the unregistered support label B. The preserved native result is unaccepted and is not relabeled as a canonical result. It gives a restricted geometric polar-measure sector and a claimed entire-modification-tower information-loss example; arbitrary transcendental P14.4 positivity remains open.\n') + '\nAuthor provenance/compilation is not mathematical certification. The existing P16.4 editor remains untouched/open.\n')
    out.append({'round': n, 'binding': str(binding), 'binding_sha256': sha(binding), 'tex_sha256': record['standalone_tex_sha256'], 'canonical_published': n == 171})
print(json.dumps(out, indent=2))
