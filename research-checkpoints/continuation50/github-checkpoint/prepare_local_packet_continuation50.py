from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import csv

R = Path('/workspace/research')
G = R / 'github-checkpoint'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
pending = G / 'upload-manifest-continuation43.json'
assert sha(pending) == '2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'
out = G / 'local-packet-continuation50.json'
saved = G / 'continuation50-local-records'
assert not out.exists() and not saved.exists()
stamp = datetime.now(timezone.utc).isoformat()
active_path = R / 'active-work.json'
active = json.loads(active_path.read_text())
active['updated_utc'] = stamp
active['prepared_local_followup_packet_50'] = str(out)
active_path.write_text(json.dumps(active, ensure_ascii=False, indent=2) + '\n')
check_path = R / 'checklist-current.json'
check = json.loads(check_path.read_text())
assert check['fully_solved_original_atoms'] == [] and len(check['targets']) == 42
assert all(t['fully_solved'] is False and t['closure'] == 'open' for t in check['targets'])
check['updated_utc'] = stamp
check_path.write_text(json.dumps(check, ensure_ascii=False, indent=2) + '\n')
with (R / 'checklist-current.tsv').open('w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(['ID', 'Closure', 'Research', 'Reviewed_papers', 'Title'])
    for t in check['targets']:
        w.writerow([t['id'], t['closure'], t['research_status'], len(t['reviewed_papers']), t['title']])
files = [Path(__file__), R / 'prepare_public_regularization_draft_reviews_20261004.py',
         R / 'prepare_public_smooth_regularization_batch_20261004.py',
         R / 'record_public_smooth_regularization_launch_20261004.py',
         R / 'public-smooth-regularization-batch-manifest-20261004.json',
         R / 'public-smooth-regularization-batch-launch-20261004.json',
         R / 'root-checks/snapshot_public_regularization_preliminary_20261004.py',
         R / 'root-checks/snapshot_public_regularization_final_20261004.py',
         R / 'root-checks/reproduce_public_regularization_final_20261004.py',
         R / 'root-checks/record_public_regularization_final_read_20261004.py',
         R / 'root-checks/P02-legal-above-approximation-and-LFS-working-proof-20261004.md',
         R / 'root-checks/P02-legal-above-approximation-and-LFS-working-proof-20261004.binding.json',
         R / 'shared-sources/P02-regularization-additional-primary-root-read-20261004.json']
scopes = {}
for n, atom, stem in [(41, 'P02.1', 'P02.1-public-source-decreasing-real-PL'),
                      (42, 'P02.2', 'P02.2-public-source-decreasing-LFS')]:
    reader = R / 'root-checks' / f'public-regularization-round-{n}-final-reader'
    files.extend(p for p in reader.iterdir() if p.is_file() and p.suffix in {'.md', '.tex', '.json', '.py', '.txt', '.log'})
    files.extend(p for p in (reader / 'source-extracts').rglob('*') if p.is_file() and p.suffix in {'.md', '.txt', '.json'})
    reproduction = reader / 'reproduction'
    files.append(reproduction / ('build' if n == 41 else '') / f'{atom}-paper.pdf')
    if n == 41:
        files.extend(p for p in (reproduction / 'diagnostics').rglob('*') if p.is_file() and p.suffix in {'.json', '.txt', '.log'})
    else:
        files.extend(reproduction / name for name in ['tex-build-diagnostics.json', 'tex-build-pass-1.log', 'tex-build-pass-2.log', 'artifact-validation.json', 'finite-diagnostics.json'])
    review = R / 'campaigns' / f'round-{n}' / (stem + '-review')
    files.extend(review / name for name in ['task.json', 'argument.md', 'settings.json', 'freeze.json'])
    preliminary = R / 'root-checks' / f'public-regularization-round-{n}-preliminary-reader'
    files.extend(p for p in preliminary.iterdir() if p.is_file())
    scopes[str(n)] = json.loads((reader / 'status.json').read_text())
for n, stem in [(43, 'P02.3-public-source-decreasing-weakly-smooth'), (44, 'P02.4-public-source-decreasing-ordinary-smooth')]:
    campaign = R / 'campaigns' / f'round-{n}' / stem
    files.extend(campaign / name for name in ['input.json', 'settings.json', 'input-manifest.json'])
saved.mkdir()
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    source = R / name
    target = saved / name
    shutil.copyfile(source, target)
    assert sha(source) == sha(target)
    files.append(target)
assert len(files) == len(set(files))
entries = []
for p in files:
    assert p.is_file() and not p.is_symlink(), str(p)
    entries.append({'local': str(p), 'path': 'research-checkpoints/continuation50/' + str(p.relative_to(R)),
                    'sha256': sha(p), 'bytes': p.stat().st_size})
packet = {'prepared_utc': stamp, 'state': 'LOCAL ONLY; no GitHub mutation or generated-material provider submission.',
          'files': entries, 'file_count': len(entries), 'original_atoms': 42, 'fully_solved_original_atoms': [],
          'completed_draft_scope': scopes, 'current_selected_atoms': ['P02.3', 'P02.4'],
          'current_native_launch_record': str(R / 'public-smooth-regularization-batch-launch-20261004.json'),
          'drafts_independently_accepted': False,
          'previous_local_packet': str(G / 'local-packet-continuation49.json'),
          'last_verified_remote_commit': '604fea852c6a27d4cdc83d97f17393ea67087301',
          'pending_GitHub43_manifest_sha256': sha(pending), 'blocked_exports_not_resubmitted': True,
          'whole_uploaded_PDF_or_extract_included': False, 'public_primary_PDF_cache_files_included': False,
          'private_transcripts_sql_auth_runtime_included': False,
          'native_editor_limitation': 'Both open requests were unresponsive; no result or handler error was returned and dependent compile calls were not reached. Sources preserved, no editor close requested. Local two-pass TeX reproduction succeeded.',
          'verification_limit': 'Full scoped proofs and actual canonical notes read. No original classification or independent correctness acceptance claimed. Hashes, finite diagnostics and builds do not certify mathematics.'}
out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(out), 'sha256': sha(out), 'files': len(entries),
                  'external_upload': False, 'original_atoms_closed': 0}, indent=2))
