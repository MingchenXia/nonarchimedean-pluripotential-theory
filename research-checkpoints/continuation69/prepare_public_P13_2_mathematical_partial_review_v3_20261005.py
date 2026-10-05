"""New mathematical-only audit; preserve the prior operationally inconclusive audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
A = R / 'campaigns/round-51/P13.2-public-source-fixed-Reeb-image-review-v2'
D = A.with_name('P13.2-public-source-fixed-Reeb-mathematical-review-v3')
assert not D.exists()
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
freeze_old = json.loads((A / 'freeze.json').read_text())
assert sha(A / 'argument.md') == freeze_old['argument_sha256']
task = json.loads((A / 'task.json').read_text())
task['problem'] = task['problem'].replace('and all four actual canonical notes.', 'and the mathematical claims in all four actual canonical notes.')
task['completionCriteria'] = task['completionCriteria'].replace('Check all four canonical notes.', 'Check every mathematical assertion in all four canonical notes, including the precise analysis of remaining mathematical gaps.')
task['completionCriteria'] += (
    ' This is a new mathematical-only audit of the exact retained partial results n1-n3 '
    'and the mathematical gap analysis in n4. Execution reports, local-file preservation, '
    'hash calculations, program runs, and compiler observations in n4 and the reproducibility '
    'appendix are outside this mathematical audit. They are neither mathematical premises '
    'nor claims whose operational verification is requested here. The complete proof, '
    'all four notes, and all 31 literal source units are retained unchanged as context. '
    'Judge all mathematical claims and dependencies independently; a local-file reader '
    'is not required solely to verify operational observations. If an indispensable '
    'mathematical premise remains unresolved, retain INCONCLUSIVE; a false mathematical '
    'assertion or proof defect remains FAIL. No acceptance of the original P13.2 image '
    'or existence characterization is requested or implied.'
)
settings = json.loads((A / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r51/P13.2-fixed-Reeb-mathematical-partial-review-v3'
D.mkdir()
(D / 'argument.md').write_bytes((A / 'argument.md').read_bytes())
(D / 'task.json').write_text(json.dumps(task, ensure_ascii=False, indent=2) + '\n')
(D / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
freeze = {
    'prepared_utc': datetime.now(timezone.utc).isoformat(),
    'previous_audit_directory': str(A),
    'previous_audit_disposition': 'Preserved INCONCLUSIVE; this is a new narrower mathematical-only audit.',
    'argument_sha256': sha(D / 'argument.md'), 'argument_bytes': (D / 'argument.md').stat().st_size,
    'task_sha256': sha(D / 'task.json'), 'settings_sha256': sha(D / 'settings.json'),
    'entire_author_proof_notes_and_source_units_byte_unchanged': True,
    'operational_observations_requested': False,
    'original_problem_acceptance_requested': False,
    'provider_submission_attempted': False
}
(D / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(freeze, ensure_ascii=False, indent=2))
