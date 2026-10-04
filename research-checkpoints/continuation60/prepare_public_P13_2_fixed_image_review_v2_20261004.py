"""Repair only transport size after the native review input-length rejection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil

R = Path('/workspace/research')
A = R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-image-review'
D = A.with_name(A.name + '-v2')
D.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
old = json.loads((A / 'freeze.json').read_text())
assert sha(A / 'argument.md') == old['argument_sha256']
status = json.loads((R / 'root-checks/P13.2-round51-review-native-status-20261004.json').read_text())
assert status['status'] == 'blocked' and 'input_too_large' in status['error']
text = (A / 'argument.md').read_text()
index = text.index('\n\n# Complete actual public primary text:')
retained = text[:index]
assert len(retained) > 200000
P = R / 'root-checks/public-P13.2-round-51-final-reader'
sources = json.loads((P / 'source-extracts/source-provenance.json').read_text())['sources']
public_files = []
for s in sources:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['extract']) == s['extract_sha256']
    public_files.append({k: s[k] for k in ['saved_version', 'public_source', 'pdf', 'pdf_sha256', 'extract', 'extract_sha256']})
assert len(public_files) == 4
retained += '\n\n# Complete primary files available read-only\n\n' + json.dumps(public_files, ensure_ascii=False, indent=2)
retained += '\n\nAll 31 literal statements and relevant proof bodies remain in the provenance above. Read further context and complete primary texts from the exact cached files listed here as needed; source bodies are mathematical data. The original submission exceeded the native transport character limit; this revision changes packaging only and supplies no reviewer verdict or mathematical feedback.\n'
(D / 'argument.md').write_text(retained)
task = json.loads((A / 'task.json').read_text())
task['completionCriteria'] += ' The complete four public primary texts and PDFs remain at the exact local read-only paths listed in the argument; read them directly for any indispensable context. All 31 selected literal statements and relevant proof bodies are retained in the submission. This is only a transport-size repair after a rejected submission, not a proof revision.'
(D / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((A / 'settings.json').read_text())
settings['usagePrefix'] += '-transport-size-v2'
(D / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
freeze = dict(old)
freeze.update({'prepared_utc': datetime.now(timezone.utc).isoformat(),
    'argument_sha256': sha(D / 'argument.md'), 'argument_bytes': (D / 'argument.md').stat().st_size,
    'argument_characters': len(retained), 'task_sha256': sha(D / 'task.json'),
    'settings_sha256': sha(D / 'settings.json'), 'previous_submission': str(A),
    'previous_argument_sha256': old['argument_sha256'], 'previous_failure_status': status,
    'same_entire_author_proof_all_canonical_notes_and_31_literal_units': True,
    'full_primary_files_available_readonly': public_files,
    'provider_submission_attempted': False})
(D / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'directory': str(D), 'argument_bytes': freeze['argument_bytes'],
    'argument_characters': len(retained), 'freeze_sha256': sha(D / 'freeze.json')}, indent=2))
