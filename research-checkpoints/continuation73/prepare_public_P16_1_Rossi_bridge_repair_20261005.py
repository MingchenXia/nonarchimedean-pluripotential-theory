"""Prepare a successor with the explicit ample collar and Rossi compact-perturbation route."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-64/P16.1-public-source-curve-detection-and-singular-globalization'
C = R / 'campaigns/round-65/P16.1-public-source-ample-collars-Rossi-and-unibranch-equation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
m = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == m['input_sha256']
assert sha(old / 'settings.json') == m['settings_sha256']
assert not (old / 'campaign.sqlite').exists()
previous = json.loads((old / 'input.json').read_text())
contexts = list(m['embedded_context'])
p = R / 'root-checks/P16.1-ample-localized-collars-and-Rossi-FS-bridge-20261005-continuation73.md'
item = {'kind': 'New unreviewed root proposal: ample principal collars and Rossi compact-perturbation FS bridge',
    'path': str(p), 'sha256': sha(p), 'accepted_dependency': False}
contexts.append(item)
marker = '\nActual read-only primary sources:\n'
prefix, suffix = previous['assignment'].split(marker, 1)
additional = '''

Additional concrete reconstruction after preparing round64: independently prove the new ample principal-open collar and compact-perturbation FS bridge. The whole proposal is diagnostic, unreviewed data, not an accepted theorem. For an arbitrary analytic neighborhood on the original projective X, start with an ample standard open D(s), write finitely many regular localization functions as tau_i/s^d_i, and use the product s times all tau_i to obtain exactly the localized open D(a). Prove the section-localization identity on reduced nonnormal X and clear all constraint numerators with one ample power of a. Add a complete very ample generating system and a rational negative floor, keeping all 1/m, constraint bounds and class scalars consistent. This should supply actual nested compact collars, not merely an unspecified affine compactification.

For Rossi Theorem5.6, first establish a precise compact-perturbation theorem: a continuous corrected contact Q-PL function v on an affine Y which equals a rational affine FS function b outside a compact set induces a globally continuous metric on the ample projective closure determined by b. The boundary is untouched by that compact set. Reconstruct strict model representation and curve-detected nefness on this actual metric, then BE7.8 and exact Laurent Gauss descent yield uniform global FS approximation. Prove conversion to the actual affine FS class on all of Y, retaining regular coefficients, complete affine generators and a constant branch, with rational weights and uniform error. A basepoint-free system alone need not induce a closed embedding; add the necessary complete high-degree sections at suitably low weights. Uniform global metric error remains uniform on the noncompact affine chart because the same reference is subtracted. If needed, construct a decreasing sequence by errors epsilon_j and shifts 2epsilon_j with 3epsilon_(j+1)<=epsilon_j rather than assuming an unavailable sequence.

Apply this theorem to v=Cu outside the relatively compact analytic V and max(Cu,log|f|-t) inside V. Prove the strict boundary inequality yields a whole winning-branch collar, handle zero coordinates, choose positive rational/integer C, and verify finite corrected contact Q-PL charts. The actual polynomial-hull polytope and vanishing separating FS exhaustion are elementary finite polynomial constructions that still need proof. A uniform affine FS approximant with error below one third of the separating gap gives the Rossi contradiction directly, without assuming arbitrary affine psh regularization. Do not extend this conclusion automatically to controlled principal-open removable extension or weak-input finite trace extension. Reconstruct every later Hartogs/Runge and singular-envelope gate in the original assignment before candidate=true.
'''
assignment = prefix + additional + marker + suffix
assignment += '\n## ' + item['kind'] + '\n\n' + p.read_text() + '\n'
for b in contexts:
    assert sha(b['path']) == b['sha256']
    assert Path(b['path']).read_text() in assignment
for s in m['public_sources']:
    assert sha(s['pdf']) == s['pdf_sha256']
    assert sha(s['literal_extract']) == s['extract_sha256']
inp = {'task': previous['task'], 'notes': [], 'assignment': assignment}
assert inp['task'] == previous['task']
assert len(contexts) == 8 and len(m['public_sources']) == 10
C.mkdir(parents=True, exist_ok=False)
write(C / 'input.json', inp)
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r65/P16.1-ample-collars-Rossi-and-unibranch-equation'
settings['codex']['workspace'] = str(C / 'artifacts')
write(C / 'settings.json', settings)
manifest = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 65,
    'atom': 'P16.1', 'directory': str(C), 'input_sha256': sha(C / 'input.json'),
    'settings_sha256': sha(C / 'settings.json'), 'original_task_unchanged_from_round64': True,
    'public_sources': m['public_sources'], 'embedded_context': contexts, 'notes_imported': [],
    'root_proposals_independently_reviewed': False, 'fully_solved_original_atom': False,
    'round64_preserved_unlaunched': True,
    'state': 'PREPARED LOCAL ONLY; no worker launched. Wait for a free native two-item batch slot.'}
write(C / 'input-manifest.json', manifest)
print(json.dumps({'directory': str(C), 'input_sha256': manifest['input_sha256'],
    'settings_sha256': manifest['settings_sha256'], 'bytes': (C / 'input.json').stat().st_size,
    'public_sources': 10, 'context_bodies': 8, 'original_task_unchanged': True,
    'launched': False}, indent=2))
