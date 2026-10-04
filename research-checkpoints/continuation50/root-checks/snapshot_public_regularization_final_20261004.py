from pathlib import Path
import hashlib
import json
import shutil
from datetime import datetime, timezone

ROOT = Path('/workspace/research')
JOBS = [
    (41, 'P02.1', 'P02.1-public-source-decreasing-real-PL', 'codex-RyjJ79'),
    (42, 'P02.2', 'P02.2-public-source-decreasing-LFS', 'codex-gsYJxq'),
]

def bind(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

for number, problem, slug, worker in JOBS:
    campaign = ROOT / 'campaigns' / f'round-{number}' / slug
    run = json.loads((campaign / 'run.json').read_text())['campaign']
    assert run['status'] == 'completed' and run['error'] is None
    result = run['result']
    assert result['kind'] == 'notes' and result['candidate'] is False
    artifact = campaign / 'artifacts' / worker
    assert Path(result['workspace']) == artifact
    dest = ROOT / 'root-checks' / f'public-regularization-round-{number}-final-reader'
    dest.mkdir(exist_ok=False)
    records = []
    for source in sorted(artifact.rglob('*')):
        if not source.is_file():
            continue
        relative = source.relative_to(artifact)
        assert not source.is_symlink()
        assert source.suffix in {'.md', '.tex', '.pdf', '.txt', '.json', '.py', '.log', '.aux', '.out', '.png'}
        target = dest / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        assert bind(source) == bind(target)
        records.append({'path': str(relative), 'origin': str(source), **bind(target)})
    canonical = dest / 'actual-canonical-notes.json'
    canonical.write_text(json.dumps(result['notes'], ensure_ascii=False, indent=2) + '\n')
    for index, note in enumerate(result['notes']):
        assert set(note) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
        (dest / f'canonical-note-{index+1}.md').write_text(
            'ID: ' + str(note['id']) + '\n\nSUMMARY:\n' + note['summary'] +
            '\n\nDETAILED SUMMARY:\n' + note['detailedSummary'] +
            '\n\nSUPPORT:\n' + json.dumps(note['support'], ensure_ascii=False) +
            '\n\nTEXT:\n' + note['text'] + '\n')
    for name in ('input.json', 'settings.json', 'input-manifest.json'):
        shutil.copyfile(campaign / name, dest / ('campaign-' + name))
    worker_input = json.loads((dest / 'input.json').read_text())
    assert worker_input == json.loads((campaign / 'input.json').read_text())
    snapshot = {
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'round': number, 'problem': problem, 'worker': worker,
        'campaign': str(campaign), 'campaign_status': run['status'],
        'campaign_error': run['error'], 'candidate': result['candidate'],
        'run_binding': bind(campaign / 'run.json'),
        'canonical_binding': bind(canonical), 'canonical_note_count': len(result['notes']),
        'worker_input_semantically_identical_to_frozen_campaign_input': True,
        'files': records, 'mathematical_acceptance': False,
        'original_target_closed': False, 'generated_scripts_executed_by_root': False,
    }
    (dest / 'snapshot.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'round': number, 'destination': str(dest), 'artifact_files': len(records),
                      'notes': len(result['notes']), 'canonical': bind(canonical)}, ensure_ascii=False))
