"""Freeze a local checkpoint without any external upload or provider call."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil

R = Path('/workspace/research')
G = R / 'github-checkpoint'
out = G / 'local-packet-continuation46.json'
snapshot = G / 'continuation46-local-records'
assert not out.exists() and not snapshot.exists()
snapshot.mkdir()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
files = [R / name for name in [
    'prepare_original_envelope_batch_20261004.py',
    'prepare_original_envelope_batch_v2_20261004.py',
    'record_original_envelope_batch_launch_20261004.py',
    'original-envelope-batch-manifest-20261004.json',
    'original-envelope-batch-v2-manifest-20261004.json',
    'original-envelope-batch-launch-20261004.json',
    'dossiers/family-02.txt',
    'shared-sources/P03-public-primary-root-read-20261004.json',
    'P15-literal-obligation-local-comparison-20261004.md',
    'P15-literal-obligation-local-comparison-binding-20261004.json',
]]
for number, stem in [(35, 'P03.1-original-envelope-positivity'), (36, 'P03.3-original-envelope-continuity')]:
    directory = R / 'campaigns' / f'round-{number}' / stem
    files.extend(directory / name for name in ['input.json', 'input-v2.json', 'input-manifest.json', 'input-v2-correction.json', 'settings.json'])
    if number == 35:
        files.extend(directory / name for name in ['run.stderr', 'launch-v1-schema-failure.json'])
for name in ['active-work.json', 'checklist-current.json', 'checklist-current.tsv']:
    src = R / name
    dest = snapshot / name
    shutil.copy2(src, dest)
    assert sha(src) == sha(dest)
    files.append(dest)
files.append(Path(__file__))
assert len(files) == len(set(files))
entries = []
for p in files:
    assert p.is_file()
    entries.append({'local': str(p), 'path': 'research-checkpoints/continuation46/' + str(p.relative_to(R)),
                    'sha256': sha(p), 'bytes': p.stat().st_size})
pending = G / 'upload-manifest-continuation43.json'
assert sha(pending) == '2ba3d0bb286624a9d7b1cb5298f748b640324717ebeaf42dab8c75405adc2c78'
manifest = {'prepared_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'state': 'LOCAL_ONLY; no GitHub mutation or new provider submission',
            'files': entries, 'file_count': len(entries), 'original_atoms': 42,
            'fully_solved_original_atoms': [], 'active_atoms': ['P03.1', 'P03.3'],
            'previous_local_packet': str(G / 'local-packet-continuation45.json'),
            'pending_GitHub43_manifest_unchanged': sha(pending),
            'last_verified_remote_commit': '604fea852c6a27d4cdc83d97f17393ea67087301',
            'pending_P15_2_audit_approval_unchanged': True,
            'whole_uploaded_PDF_or_extract_included': False,
            'private_raw_conversations_sql_auth_runtime_included': False,
            'source_section_origin': 'Exact user-uploaded relevant dossier, with separate explicit OCR control-marker correction.'}
out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'manifest': str(out), 'sha256': sha(out), 'files': len(entries), 'external_upload': False}, indent=2))
