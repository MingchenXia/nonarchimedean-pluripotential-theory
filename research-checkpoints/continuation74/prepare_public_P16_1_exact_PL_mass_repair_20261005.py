"""Prepare exact local PL extension and partition repair after controlled affine input."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-66/P16.1-public-source-controlled-affine-Rossi-and-unibranch-equation'
C = R / 'campaigns/round-67/P16.1-public-source-exact-PL-local-mass-and-unibranch-equation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
m = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == m['input_sha256']
assert sha(old / 'settings.json') == m['settings_sha256']
assert not (old / 'campaign.sqlite').exists()
previous = json.loads((old / 'input.json').read_text())
contexts = list(m['embedded_context'])
p = R / 'root-checks/P16.1-exact-Gauss-model-PL-descent-and-partitions-20261005-continuation74.md'
item = {'kind': 'New unreviewed root proposal: exact Gauss model-PL descent, compact local extension and PL partitions',
    'path': str(p), 'sha256': sha(p), 'accepted_dependency': False}
contexts.append(item)
marker = '\nActual read-only primary sources:\n'
prefix, suffix = previous['assignment'].split(marker, 1)
additional = '''

Further exact reconstruction for local IBP and mass: independently prove that an actual rational formal model function over a finite Laurent field has an exact algebraic PL Gauss pullback over k, not merely continuous PSH approximations. Add the fixed ample reference to get a rational model B of L. On a suitable dominating projective model with ample A generic L^m, rA+B and rA are ample for large r and suitable multiples are relatively globally generated. Their model metrics are exact pure FS metrics, and B is their difference. Apply exact finite Laurent coefficient/Gauss FS descent to both and cancel the canonical reference terms. Check all generic classes and rational tensor factors. The result is an actual difference of rational global FS potentials and hence BJ algebraic PL, without assuming the initial K-model was equivariant or that a FS difference is positive.

Use actual GM2.7/2.10 only after proving strict-G-local rational membership on a compact rational domain neighborhood of the test support. Extend that formal metric on the trivial bundle to X_K, use proper algebraic/formal equivalence2.6, and descend its Gauss value by the preceding exact construction. Agreement is needed only near the compact support, not on the entire original analytic open. Reconstruct the ample-model domination step from GM4.11 or vertical-ideal blowup domination over the noetherian Laurent DVR. Do not assume an arbitrary relatively ample E in the printed4.12 proof has trivial generic restriction; use a suitable vertical blowup with exceptional bundle trivial on the generic fiber. Every algebraic and source application must be checked.

Construct a global rational algebraic PL partition directly from BJ2.2/2.3 uniform density and vector-lattice operations. For compact shrinkings K_i inside U_i choose continuous bumps a_i, rational PL p_i within1/8, and chi_i=min(1,max(0,2p_i-1/2)). They are one on K_i with compact support inside U_i. Allocate rho_1=chi_1 and rho_i=min(chi_i,1-sum_(j<i)rho_j), proving nonnegativity, subordinate supports and sum rho_i=1. Do not normalize by a variable denominator or assume arbitrary analytic opens are exactly preimages of toric opens.

Use exact local PL extensions, genuine global model locality and integration by parts for the compact PL identity. Then prove bounded decreasing weighted local compatibility using the common genuine global collar, actual BJ multilinear pairing and weighted mixed continuity. Establish overlap and approximation independence rather than defining a proxy local operator. The subordinate global PL partition and cutoffs should let the mass calculation sum to ddc1=0; show every cutoff support and weighted limit, with the correct mixed background forms, signs and raw degrees. Only then use comparison and positive-model-atom domination to recover smooth local/global equality. All original weak-trace, singular Runge, envelope, cardinality, real-class and equation gates still require full reconstruction; do not declare candidate=true from these local repairs alone.
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
assert len(contexts) == 10 and len(m['public_sources']) == 10
C.mkdir(parents=True, exist_ok=False)
write(C / 'input.json', inp)
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r67/P16.1-exact-PL-local-mass-and-unibranch-equation'
settings['codex']['workspace'] = str(C / 'artifacts')
write(C / 'settings.json', settings)
manifest = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 67,
    'atom': 'P16.1', 'directory': str(C), 'input_sha256': sha(C / 'input.json'),
    'settings_sha256': sha(C / 'settings.json'), 'original_task_unchanged_from_round66': True,
    'public_sources': m['public_sources'], 'embedded_context': contexts, 'notes_imported': [],
    'root_proposals_independently_reviewed': False, 'fully_solved_original_atom': False,
    'round64_through_round66_preserved_unlaunched': True,
    'state': 'PREPARED LOCAL ONLY; no worker launched. Wait for a free native two-item batch slot.'}
write(C / 'input-manifest.json', manifest)
print(json.dumps({'directory': str(C), 'input_sha256': manifest['input_sha256'],
    'settings_sha256': manifest['settings_sha256'], 'bytes': (C / 'input.json').stat().st_size,
    'public_sources': 10, 'context_bodies': 10, 'original_task_unchanged': True,
    'launched': False}, indent=2))
