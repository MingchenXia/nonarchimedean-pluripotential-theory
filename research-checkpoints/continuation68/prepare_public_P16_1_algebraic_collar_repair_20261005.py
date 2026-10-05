"""Freeze a new, unlaunched repair; preserve the earlier round57 packet."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-57/P16.1-public-source-direct-FS-trace-and-unibranch-equation'
C = R / 'campaigns/round-58/P16.1-public-source-algebraic-collar-trace-and-unibranch-equation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
previous = json.loads((old / 'input.json').read_text())
manifest57 = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == manifest57['input_sha256']
assert sha(old / 'settings.json') == manifest57['settings_sha256']
note = R / 'root-checks/P16.1-algebraic-model-PL-for-affine-FS-gluing-20261005-continuation68.md'
body = note.read_text()
marker = '\nActual read-only primary sources:\n'
prefix, suffix = previous['assignment'].split(marker, 1)
additional = '''

Additional unreviewed root proposal: the attached explicit lattice formula targets the singular model-PL representation obligation specifically for collar gluing of globally algebraic affine FS inputs. It is diagnostic data, not an accepted theorem. Verify the BJ Section2.1 rational vector-lattice statement, membership of clipped section norms as differences of actual basepoint-free FS metrics, the capped exhaustion G, every signed coefficient, the uniform clipping thresholds, and the min-cap F on the entire boundary divisor. Check the exact local c-theta-psh interpretation and independently reconstruct the field extension, formal-model/residual-degree and model-nef criterion applications on singular and nonnormal projective spaces. Do not infer that arbitrary analytic PL is algebraic model PL.

For already globally affine-FS-regularizable u with upper growth, a single compact collar for an entire tail of decreasing FS approximants should supply the legitimate noncircular Theorem3.25 antecedent and controlled global FS regularization. Verify the limiting floors, nontriviality and genuine original PSH class. For the arbitrary smooth local starting class, the separate GM/BJ smooth route remains required. For the actual Hartogs/Runge induction, identify its precise finite polynomial coefficient expressions and prove that they meet this narrower formula's hypotheses; do not claim the missing general Runge theorem follows merely from a representation lemma. Every dependency leading to singular envelope continuity and the original equation must still be reconstructed.
'''
assignment = prefix + additional + marker + suffix
assignment += '\n## Unreviewed explicit algebraic model-PL collar formula\n\n' + body + '\n'
inp = {'task': previous['task'], 'notes': [], 'assignment': assignment}
sources = manifest57['public_sources']
assert len(sources) == 6
for s in sources:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
for context in manifest57['embedded_context']:
    assert sha(context['path']) == context['sha256']
    assert Path(context['path']).read_text() in assignment
assert body in assignment
assert inp['task'] == previous['task'] and inp['notes'] == []
C.mkdir(parents=True, exist_ok=False)
(C / 'input.json').write_text(json.dumps(inp, ensure_ascii=False, indent=2) + '\n')
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r58/P16.1-algebraic-collar-trace-and-unibranch-equation'
settings['codex']['workspace'] = str(C / 'artifacts')
(C / 'settings.json').write_text(json.dumps(settings, indent=2) + '\n')
contexts = manifest57['embedded_context'] + [{'kind': 'Unreviewed explicit algebraic model-PL collar formula', 'path': str(note), 'sha256': sha(note), 'accepted_dependency': False}]
manifest = {
    'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 58,
    'atom': 'P16.1', 'directory': str(C),
    'input_sha256': sha(C / 'input.json'), 'settings_sha256': sha(C / 'settings.json'),
    'original_task_unchanged_from_round57': inp['task'] == previous['task'],
    'public_sources': sources, 'embedded_context': contexts,
    'notes_imported': [], 'root_proposals_independently_reviewed': False,
    'fully_solved_original_atom': False, 'supersedes_unlaunched_round57': True,
    'state': 'PREPARED LOCAL ONLY; not launched. Round55 author has completed; round51 P13.2 review remains active.'
}
(C / 'input-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: manifest[k] for k in ['directory', 'input_sha256', 'settings_sha256', 'original_task_unchanged_from_round57', 'state']}, indent=2))
print('input_bytes', (C / 'input.json').stat().st_size)
