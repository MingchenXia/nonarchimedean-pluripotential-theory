"""Reproduce read-only author artifacts in a fresh, local root-check directory."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil
import subprocess

reader = Path('/workspace/research/root-checks/public-envelope-round-37-final-reader')
fresh = reader / 'reproduction'
fresh.mkdir(exist_ok=False)
for p in reader.iterdir():
    if p.is_file() and p.suffix in {'.json', '.md', '.py', '.tex', '.txt'}:
        shutil.copy2(p, fresh / p.name)
shutil.copytree(reader / 'source-extracts', fresh / 'source-extracts')
records = []
for i, helper in enumerate(['prepare_sources.py', 'build_artifacts.py', 'check_artifacts.py'], 1):
    command = ['python3', helper]
    result = subprocess.run(command, cwd=fresh, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    log = reader / f'reproduction-command-{i}.log'
    log.write_text(result.stdout)
    records.append({'command': command, 'exit_code': result.returncode, 'log': str(log)})
    print(helper, result.returncode, result.stdout[-1000:])
    assert result.returncode == 0, helper

identities = []
for name in ['P03.1-argument.md', 'P03.1-paper.tex', 'source-provenance.json']:
    assert (fresh / name).read_bytes() == (reader / name).read_bytes(), name
    identities.append(name)
for p in (reader / 'source-extracts').glob('*.txt'):
    assert p.read_bytes() == (fresh / 'source-extracts' / p.name).read_bytes(), p.name
    identities.append('source-extracts/' + p.name)

execution = json.loads((fresh / 'execution.json').read_text())
diagnostics = []
for command in execution['commands']:
    log = (fresh / command['diagnostics_file']).read_text()
    diagnostics.append({**command, 'diagnostics': [line for line in log.splitlines()
                        if any(term in line for term in ['Warning', 'Overfull', 'Underfull', 'Output written', 'Error'])]})
checks = json.loads((fresh / 'artifact-checks.json').read_text())
assert checks['all_passed'] and all(x['passed'] for x in checks['checks'])
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
record = {
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'fresh_directory': str(fresh), 'commands': records,
    'byte_identical_files': identities,
    'two_local_TeX_passes': diagnostics,
    'reproduced_pdf_sha256': sha(fresh / 'P03.1-paper.pdf'),
    'administrative_checks_passed': len(checks['checks']),
    'make_notes_py_executed_by_root': False,
    'local_author_note_view_retained_as_data': True,
    'local_note_view_not_assumed_identical_to_native_canonical': True,
    'native_editor_verified': False, 'independent_review_launched': False,
    'original_atom_closed': False,
    'limitation': 'Successful builds and administrative checks are execution evidence, not mathematical proof certificates.'
}
(reader / 'reproduction-result.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
