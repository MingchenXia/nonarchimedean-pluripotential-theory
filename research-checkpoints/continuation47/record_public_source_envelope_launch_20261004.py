"""Record a fresh published-source-only pair without altering blocked exports."""
from pathlib import Path
import datetime
import hashlib
import json

R = Path('/workspace/research')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
path = R / 'public-source-envelope-continuation-manifest-20261004.json'
manifest = json.loads(path.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sessions = {'P03.1': 25422, 'P03.3': 88877}
records = []
for rec in manifest['campaigns']:
    directory = Path(rec['directory'])
    assert sha(rec['selected_input']) == rec['input_sha256']
    assert sha(directory / 'settings.json') == rec['settings_sha256']
    records.append({**rec, 'tool_session_id': sessions[rec['atom']],
                    'state': 'Native Xean author running; original task and published-source pointers only; no result or acceptance yet.'})
launch = R / 'public-source-envelope-continuation-launch-20261004.json'
assert not launch.exists()
launch.write_text(json.dumps({'recorded_utc': now, 'prepared_manifest': str(path),
                             'prepared_manifest_sha256': sha(path), 'campaigns': records,
                             'route': 'Xean native Codex', 'model': 'gpt-6.1-sol', 'reasoning': 'xhigh',
                             'blocked_review_payloads_resubmitted': False,
                             'GitHub_mutation_attempted': False}, indent=2) + '\n')
a = json.loads((R / 'active-work.json').read_text())
a['updated_utc'] = now
a['batch_manifest'] = str(path)
a['selected_atoms'] = ['P03.1', 'P03.3']
a['current_public_source_envelope_batch'] = {'launch_record': str(launch), 'launch_record_sha256': sha(launch),
                                           'campaigns': records, 'public_source_cache_manifest': manifest['public_source_cache_manifest']}
a['goal_state'] = 'ACTIVE. All42originalsopen. Current authors ONLY P03.1/P03.3 R37/R38 running with original tasks and five published primary-source cache pointers, no generated prior proof payload. R35 conditional toric reconstruction and R36 abstract criterion do not close originals. R36 exact abstract review, R32 P15.2 original-scope audit, and GitHub43 export separately await explicit pending approvals; no workaround. Local R36 full proof/canonical/TEX read and fresh reproduction successful; native unresponsive, source preserved.'
a['next_work'] = 'Finish the R37/R38 public-source geometric investigations and fully inspect/reconstruct any actual analytic proofs. Keep originals open until every literal obligation is proved. Execute each frozen blocked review/checkpoint only after its specific approval; preserve all source and rejection evidence.'
for rec in records:
    a['research'].append({'atom': rec['atom'], 'directory': rec['directory'],
                          'tool_session_id': rec['tool_session_id'], 'selected_input': rec['selected_input'],
                          'input_sha256': rec['input_sha256'], 'settings_sha256': rec['settings_sha256'],
                          'research_state': rec['state'], 'review_state': 'Not prepared or launched.'})
a['prepared_local_followup_packet_46'] = {'manifest': str(R / 'github-checkpoint/local-packet-continuation46.json'),
                                         'sha256': sha(R / 'github-checkpoint/local-packet-continuation46.json'),
                                         'state': '26-file local-only checkpoint; no external upload.'}
(R / 'active-work.json').write_text(json.dumps(a, ensure_ascii=False, indent=2) + '\n')
c = json.loads((R / 'checklist-current.json').read_text())
c['updated_utc'] = now
c['current_batch_launch_record'] = str(launch)
assert len(c['targets']) == 42 and c['fully_solved_original_atoms'] == []
for t in c['targets']:
    assert t['closure'] == 'open' and t['fully_solved'] is False
    if t['id'] in a['selected_atoms']:
        t['research_status'] = 'active'
        t['current_focus'] += ' Fresh R37/R38 geometric investigations running with direct published-source caches; original task unchanged and no preceding generated proof supplied.'
(R / 'checklist-current.json').write_text(json.dumps(c, ensure_ascii=False, indent=2) + '\n')
rows = ['ID\tClosure\tResearch\tReviewed_papers\tTitle']
rows.extend('\t'.join((t['id'], t['closure'], t['research_status'], str(len(t['reviewed_papers'])), t['title'])) for t in c['targets'])
(R / 'checklist-current.tsv').write_text('\n'.join(rows) + '\n')
print(json.dumps({'launch_record': str(launch), 'sha256': sha(launch), 'active_atoms': a['selected_atoms'],
                  'fully_solved_original_atoms': [], 'blocked_actions_unchanged': True}, indent=2))
