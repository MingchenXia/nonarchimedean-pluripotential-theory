from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

ROOT = Path('/workspace/research')
JOBS = {
    45: ('P16.1', 'P16.1-public-source-singular-finite-energy-equations', 'codex-ZDgZTo', '2a3d274ed61ffa658d8db5a78500c2c5af6c706170113c66b4f05f4598f26d9c'),
    46: ('P16.4', 'P16.4-public-source-arbitrary-field-finite-energy-equations', 'codex-cC7tVd', 'd45347bd77e25fa7e0089d0ebb2ae096b35b78493811b73ffec4ff5a8962d46d'),
}

def binding(path):
    data = Path(path).read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

for number, (atom, slug, worker, input_sha) in JOBS.items():
    campaign = ROOT / 'campaigns' / f'round-{number}' / slug
    assert binding(campaign / 'input.json')['sha256'] == input_sha
    run = json.loads((campaign / 'run.json').read_text())['campaign']
    assert run['status'] == 'completed' and run['error'] is None
    result = run['result']
    assert result['kind'] == 'notes'
    origin = campaign / 'artifacts' / worker
    assert Path(result['workspace']) == origin
    target = ROOT / 'root-checks' / f'public-P16-round-{number}-final-reader'
    assert not target.exists()
    target.mkdir()
    files = []
    for source in sorted(origin.rglob('*')):
        if not source.is_file():
            continue
        assert not source.is_symlink()
        assert source.suffix in {'.md', '.tex', '.pdf', '.txt', '.json', '.py', '.log', '.aux', '.out', '.png', '.sh'}, str(source)
        relative = source.relative_to(origin)
        assert not any(word in str(relative).lower() for word in ('transcript', 'session', 'events'))
        copied = target / relative
        copied.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, copied)
        assert binding(source) == binding(copied)
        files.append({'path': str(relative), 'origin': str(source), **binding(copied)})
    canonical = target / 'actual-canonical-notes.json'
    canonical.write_text(json.dumps(result['notes'], ensure_ascii=False, indent=2) + '\n')
    for index, note in enumerate(result['notes'], 1):
        assert set(note) == {'id', 'summary', 'detailedSummary', 'text', 'support'}
        (target / f'canonical-note-{index}.md').write_text(
            'ID: ' + str(note['id']) + '\n\nSUMMARY:\n' + note['summary'] +
            '\n\nDETAILED SUMMARY:\n' + note['detailedSummary'] +
            '\n\nSUPPORT:\n' + json.dumps(note['support'], ensure_ascii=False) +
            '\n\nTEXT:\n' + note['text'] + '\n')
    for name in ('input.json', 'settings.json', 'input-manifest.json'):
        shutil.copyfile(campaign / name, target / ('campaign-' + name))
    assert json.loads((target / 'input.json').read_text()) == json.loads((campaign / 'input.json').read_text())
    snapshot = {
        'created_utc': datetime.now(timezone.utc).isoformat(), 'round': number, 'atom': atom,
        'campaign': str(campaign), 'campaign_status': run['status'], 'campaign_error': run['error'],
        'worker': worker, 'candidate': result['candidate'], 'run_binding': binding(campaign / 'run.json'),
        'canonical_binding': binding(canonical), 'canonical_note_count': len(result['notes']),
        'files': files, 'author_helpers_executed_by_root': False,
        'independent_mathematical_acceptance': False, 'original_target_closed': False,
        'private_transcripts_or_SQL_copied': False,
    }
    (target / 'snapshot.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'round': number, 'reader': str(target), 'files': len(files),
                      'notes': len(result['notes']), 'canonical': binding(canonical)}))
