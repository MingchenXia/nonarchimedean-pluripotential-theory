from pathlib import Path
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone

ROOT = Path('/workspace/research/root-checks')
JOBS = [
    (39, 'P03.2', ['extract_sources.py', 'build_deliverables.py', 'verify_artifacts.py']),
    (40, 'P03.3', ['prepare_sources.py', 'verify_deliverable.py']),
]

def binding(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

for number, problem, scripts in JOBS:
    source = ROOT / f'public-curves-CLD-round-{number}-final-reader'
    snapshot = json.loads((source / 'snapshot.json').read_text())
    dest = source / 'reproduction'
    dest.mkdir(exist_ok=False)
    for record in snapshot['files']:
        relative = record['path']
        original = source / relative
        assert binding(original) == {k: record[k] for k in ('bytes', 'sha256')}
        target = dest / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, target)
    steps = []
    for index, script in enumerate(scripts, 1):
        command = ['python3', script]
        started = datetime.now(timezone.utc).isoformat()
        result = subprocess.run(command, cwd=dest, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, timeout=90)
        log = source / f'reproduction-command-{index}.log'
        log.write_text(result.stdout)
        steps.append({'command': command, 'cwd': str(dest), 'started_utc': started,
                      'exit_code': result.returncode, 'log': str(log), **binding(log)})
        if result.returncode:
            break
    comparisons = []
    paths = [f'{problem}-argument.md', f'{problem}-paper.tex', 'source-extracts/source-provenance.json']
    paths += [str(p.relative_to(source)) for p in sorted((source / 'source-extracts').rglob('*.txt'))
              if 'stdout' not in p.name]
    for relative in paths:
        original, fresh = source / relative, dest / relative
        comparisons.append({'path': relative, 'identical': original.read_bytes() == fresh.read_bytes(),
                            'original': binding(original), 'fresh': binding(fresh)})
    pdf = dest / f'{problem}-paper.pdf'
    info = subprocess.run(['pdfinfo', str(pdf)], text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT, timeout=15)
    (source / 'reproduction-pdfinfo.txt').write_text(info.stdout)
    render = subprocess.run(['pdftoppm', '-f', '1', '-l', '1', '-scale-to', '1600',
                             '-singlefile', '-png', str(pdf), str(source / 'paper-first-page')],
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30)
    (source / 'reproduction-first-page-render.log').write_text(render.stdout)
    report = {'round': number, 'problem': problem, 'steps': steps,
              'comparisons': comparisons, 'pdf': {'path': str(pdf), **binding(pdf)},
              'pdfinfo_exit_code': info.returncode, 'first_page_render_exit_code': render.returncode,
              'all_script_steps_succeeded': len(steps) == len(scripts) and all(s['exit_code'] == 0 for s in steps),
              'core_tex_provenance_and_literal_units_identical': all(c['identical'] for c in comparisons),
              'local_notes_not_assumed_identical_to_actual_campaign_canonical_notes': True,
              'mathematical_verification': False, 'original_target_closed': False}
    (source / 'reproduction-result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('round', 'all_script_steps_succeeded',
                       'core_tex_provenance_and_literal_units_identical', 'pdf')}, ensure_ascii=False))
