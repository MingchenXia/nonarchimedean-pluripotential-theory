"""Update live status for the original-input-only P03 pair; keep frozen records."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
manifest_path = R / 'original-envelope-batch-v2-manifest-20261004.json'
manifest = json.loads(manifest_path.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sessions = {'P03.1': 19654, 'P03.3': 73461}
records = []
for rec in manifest['campaigns']:
    p = Path(rec['directory'])
    assert sha(rec['selected_input']) == rec['input_sha256']
    assert sha(p / 'settings.json') == rec['settings_sha256']
    records.append({**rec, 'tool_session_id': sessions[rec['atom']],
                    'run_json': str(p / 'run-v2.json'), 'run_stderr': str(p / 'run-v2.stderr'),
                    'state': 'Native Xean author launched; result not yet received; no acceptance or original closure.'})
launch = R / 'original-envelope-batch-launch-20261004.json'
assert not launch.exists()
launch.write_text(json.dumps({'recorded_utc': now, 'prepared_manifest': str(manifest_path),
                             'prepared_manifest_sha256': sha(manifest_path), 'campaigns': records,
                             'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
                             'previous_P03_1_schema_failure_preserved': True,
                             'blocked_P15_audit_resubmitted': False, 'GitHub_mutation_attempted': False}, indent=2) + '\n')
a = json.loads((R / 'active-work.json').read_text())
a['updated_utc'] = now
a['selected_atoms'] = ['P03.1', 'P03.3']
a['batch_manifest'] = str(manifest_path)
a['current_original_envelope_batch'] = {'launch_record': str(launch), 'launch_record_sha256': sha(launch),
                                        'campaigns': records, 'original_input_only': True}
a['goal_state'] = 'ACTIVE. All42originalsopen. Current batch only P03.1/P03.3: fresh original-user-PDF-only Xean native gpt-6.1-sol/xhigh author investigations launched. R31/R32 scoped papers are locally published; native editor/compiler returned No handler registered. P15.2 original-scope audit and GitHub43 export still await their specific pending approvals; no workaround or export retry.'
a['next_work'] = 'Finish the fresh original-input-only P03 pair, read full canonical proofs and sources, prepare exact independent reviews and separate papers for proved results. Preserve blocked P15.2 audit and GitHub43 until their explicit approvals. No original closure without a complete exact-scope proof and audit.'
for rec in records:
    a['research'].append({'atom': rec['atom'], 'directory': rec['directory'],
                          'tool_session_id': rec['tool_session_id'], 'selected_input': rec['selected_input'],
                          'input_sha256': rec['input_sha256'], 'settings_sha256': rec['settings_sha256'],
                          'research_state': rec['state'], 'review_state': 'Not prepared or launched.'})
(R / 'active-work.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
c = json.loads((R / 'checklist-current.json').read_text())
assert c['catalogue_atoms'] == len(c['targets']) == 42
assert c['fully_solved_original_atoms'] == []
c['updated_utc'] = now
c['active_atoms'] = a['selected_atoms']
c['current_batch_launch_record'] = str(launch)
for t in c['targets']:
    assert t['closure'] == 'open' and t['fully_solved'] is False
    if t['id'] in a['selected_atoms']:
        t['research_status'] = 'active'
        t['current_focus'] = 'Fresh original-PDF-only full-family investigation via Xean native gpt-6.1-sol/xhigh. No generated prior proof supplied; no result or original closure yet.'
    elif t['id'] in ['P15.1', 'P15.2']:
        t['research_status'] = 'partial'
        t['current_focus'] += ' Native requests subsequently returned No handler registered for open_in_codex and compile_latex_document; source and successful local builds preserved in separate addenda.'
(R / 'checklist-current.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
rows = ['ID\tClosure\tResearch\tReviewed_papers\tTitle']
rows.extend('\t'.join((t['id'], t['closure'], t['research_status'], str(len(t['reviewed_papers'])), t['title'])) for t in c['targets'])
(R / 'checklist-current.tsv').write_text('\n'.join(rows) + '\n')
print(json.dumps({'active_atoms': a['selected_atoms'], 'fully_solved_original_atoms': [],
                  'launch_record': str(launch), 'launch_record_sha256': sha(launch),
                  'pending_specific_approvals_unchanged': True}, indent=2))
