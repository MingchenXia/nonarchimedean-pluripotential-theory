from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import shutil

R = Path('/workspace/research')
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
pending = G / 'upload-manifest-continuation43.json'
assert sha(pending) == '2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'
out = G / 'local-packet-continuation51.json'
saved = G / 'continuation51-local-records'
assert not out.exists() and not saved.exists()
stamp = datetime.now(timezone.utc).isoformat()

active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
active['updated_utc'] = stamp
active['goal_state'] = 'ACTIVE. All 42 original targets remain open. Current two native authors R43/R44 completed; full proofs/canonical notes/TeX read and locally reproduced. Exact reviews locally prepared only, not submitted. New root bridges and current-positivity clarification are unaccepted local work. Four earlier rejected exports remain pending specific approval; none retried.'
active['next_work'] = 'Continue in small original/public-source batches; preserve local proof and requirement reconstruction. Keep existing export questions pending and frozen inputs unchanged.'
active['prepared_local_followup_packet_51'] = str(out)
found = set()
for items in [active.get('research', []), active.get('continuations', []),
              active['current_public_smooth_regularization_batch']['campaigns']]:
    for item in items:
        directory = item.get('directory', '')
        for number, atom, slug in [(43, 'P02.3', 'P02.3-public-source-decreasing-weakly-smooth'),
                                  (44, 'P02.4', 'P02.4-public-source-decreasing-ordinary-smooth')]:
            if directory == str(R / 'campaigns' / f'round-{number}' / slug):
                item['state'] = item['research_state'] = 'Completed, candidate=false; full scoped proof, all four actual canonical notes, TeX and source applications root read. Fresh local two-pass reproduction passed. Original target remains open.'
                item['review_state'] = 'Exact scoped review prepared locally only; never submitted. No independent acceptance.'
                item['root_read_record'] = str(R / 'root-checks' / f'public-smooth-round-{number}-final-reader/complete-root-read.json')
                item['pending_review_directory'] = str(R / 'campaigns' / f'round-{number}' / (slug + '-review'))
                found.add(number)
assert found == {43, 44}
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')

check_path = R / 'checklist-current.json'
check = json.loads(check_path.read_text())
assert len(check['targets']) == 42 and check['fully_solved_original_atoms'] == []
assert all(t['fully_solved'] is False and t['closure'] == 'open' for t in check['targets'])
check['updated_utc'] = stamp
for t in check['targets']:
    if t['id'] in {'P02.3', 'P02.4'}:
        number = 43 if t['id'] == 'P02.3' else 44
        t['research_status'] = 'New native scoped proof draft read and locally reproduced; exact independent review prepared locally only. Original characterization remains open.'
        t.setdefault('local_unaccepted_drafts', []).append({
            'round': number, 'root_read': str(R / 'root-checks' / f'public-smooth-round-{number}-final-reader/complete-root-read.json'),
            'independently_accepted': False, 'original_target_closed': False})
check_path.write_text(json.dumps(check, ensure_ascii=False, indent=2) + '\n')
with (R / 'checklist-current.tsv').open('w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['ID', 'Closure', 'Research', 'Reviewed_papers', 'Title'])
    for t in check['targets']:
        writer.writerow([t['id'], t['closure'], t['research_status'], len(t['reviewed_papers']), t['title']])

files = [Path(__file__), G / 'prepare_local_packet_continuation51.py',
         G / 'continuation51-preparer-schema-correction.json',
         R / 'prepare_public_smooth_draft_reviews_20261004.py',
         R / 'root-checks/snapshot_public_smooth_final_20261004.py',
         R / 'root-checks/reproduce_public_smooth_round43_20261004.py',
         R / 'root-checks/reproduce_public_smooth_round44_20261004.py',
         R / 'root-checks/record_public_smooth_final_read_20261004.py',
         R / 'root-checks/bind_fixed_domain_smooth_bridge_20261004.py',
         R / 'root-checks/P02.4-fixed-domain-net-and-sequence-bridge-20261004.md',
         R / 'root-checks/P02.4-fixed-domain-net-and-sequence-bridge-20261004.binding.json',
         R / 'root-checks/P02.3-round43-current-positivity-clarification-20261004.md',
         R / 'root-checks/P15-joint-reference-working-proof-20261004.md',
         R / 'root-checks/P15-joint-reference-working-proof-20261004.binding.json',
         R / 'shared-sources/P02-smooth-final-additional-primary-root-read-20261004.json']
for number, atom, slug in [(43, 'P02.3', 'P02.3-public-source-decreasing-weakly-smooth'),
                           (44, 'P02.4', 'P02.4-public-source-decreasing-ordinary-smooth')]:
    reader = R / 'root-checks' / f'public-smooth-round-{number}-final-reader'
    files.extend(p for p in reader.iterdir() if p.is_file() and p.suffix in {'.md', '.tex', '.json', '.py', '.txt', '.log'})
    files.extend(p for p in (reader / 'source-extracts').rglob('*') if p.is_file() and p.suffix in {'.txt', '.json', '.png'})
    for sub in ['build', 'pdf-checks']:
        if (reader / sub).exists():
            files.extend(p for p in (reader / sub).rglob('*') if p.is_file() and p.suffix in {'.txt', '.log', '.png'})
    reproduction = reader / 'reproduction'
    files.append(reproduction / f'{atom}-paper.pdf')
    files.extend(p for p in reproduction.rglob('*') if p.is_file() and
                 (p.name.startswith('root-') or p.name.startswith('tex-pass-') or p.name.startswith('build-')) and
                 p.suffix in {'.json', '.txt', '.log', '.png'})
    review = R / 'campaigns' / f'round-{number}' / (slug + '-review')
    files.extend(review / name for name in ['task.json', 'argument.md', 'settings.json', 'freeze.json'])
saved.mkdir()
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    source = R / name
    destination = saved / name
    shutil.copyfile(source, destination)
    assert sha(source) == sha(destination)
    files.append(destination)
assert len(files) == len(set(files))
entries = []
for p in files:
    assert p.is_file() and not p.is_symlink(), str(p)
    entries.append({'local': str(p), 'path': 'research-checkpoints/continuation51/' + str(p.relative_to(R)),
                    'bytes': p.stat().st_size, 'sha256': sha(p)})
packet = {'prepared_utc': stamp, 'state': 'LOCAL ONLY; no GitHub mutation or provider export.',
          'files': entries, 'file_count': len(entries), 'original_atoms': 42, 'fully_solved_original_atoms': [],
          'completed_native_batch': ['P02.3', 'P02.4'], 'active_native_authors_in_this_batch': [],
          'scoped_drafts_independently_accepted': False, 'reviews_prepared_but_never_submitted': [43, 44],
          'root_mathematical_notes_unaccepted': True,
          'previous_local_packet': str(G / 'local-packet-continuation50.json'),
          'last_verified_remote_commit': '604fea852c6a27d4cdc83d97f17393ea67087301',
          'pending_GitHub43_manifest_sha256': sha(pending), 'blocked_exports_not_resubmitted': True,
          'whole_uploaded_PDF_or_extract_included': False, 'book_source_proofs_included': False,
          'private_transcripts_sql_auth_runtime_included': False,
          'native_editor_limitation': 'Both native open requests were unresponsive; no result or handler error returned and dependent compile requests not reached. Sources preserved; fresh local two-pass builds succeeded.',
          'verification_limit': 'Full proofs and canon read, scoped applications reconstructed, R43 current-cone clarification recorded. No independent PASS, original characterization or catalogue closure.'}
out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(out), 'files': len(entries), 'sha256': sha(out), 'uploaded': False,
                  'original_atoms_closed': 0}, indent=2))
