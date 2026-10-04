from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import sys

ROOT = Path('/workspace/research')
JOBS = {
    43: ('P02.3', 'P02.3-public-source-decreasing-weakly-smooth', 'codex-4O8X0J', '4ea05c9921207ab94ab0849124094f1401b3faabc679a8ae577d4367566c8ad3'),
    44: ('P02.4', 'P02.4-public-source-decreasing-ordinary-smooth', 'codex-QKCSac', 'df589bb736b1185ace59eb962d91776c41937800ea397a22cd0c4b08d4761417'),
}

def binding(path):
    data = Path(path).read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

for number in [int(x) for x in sys.argv[1:]]:
    atom, slug, worker, input_sha = JOBS[number]
    campaign = ROOT / 'campaigns' / f'round-{number}' / slug
    assert binding(campaign / 'input.json')['sha256'] == input_sha
    run = json.loads((campaign / 'run.json').read_text())['campaign']
    assert run['status'] == 'completed' and run['error'] is None
    result = run['result']
    assert result['kind'] == 'notes'
    origin = campaign / 'artifacts' / worker
    assert Path(result['workspace']) == origin
    target = ROOT / 'root-checks' / f'public-smooth-round-{number}-final-reader'
    assert not target.exists()
    target.mkdir()
    files = []
    for source in sorted(origin.rglob('*')):
        if not source.is_file():
            continue
        assert not source.is_symlink()
        assert source.suffix in {'.md', '.tex', '.pdf', '.txt', '.json', '.py', '.log', '.aux', '.out', '.png', '.sh'}, str(source)
        relative = source.relative_to(origin)
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
