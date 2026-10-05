"""Prepare controlled affine truncation repair, preserving the unlaunched Rossi input."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-65/P16.1-public-source-ample-collars-Rossi-and-unibranch-equation'
C = R / 'campaigns/round-66/P16.1-public-source-controlled-affine-Rossi-and-unibranch-equation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
m = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == m['input_sha256']
assert sha(old / 'settings.json') == m['settings_sha256']
assert not (old / 'campaign.sqlite').exists()
previous = json.loads((old / 'input.json').read_text())
contexts = list(m['embedded_context'])
p = R / 'root-checks/P16.1-controlled-affine-FS-from-moving-compact-truncations-20261005-continuation73.md'
item = {'kind': 'New unreviewed root proposal: controlled affine FS via nested compact truncations',
    'path': str(p), 'sha256': sha(p), 'accepted_dependency': False}
contexts.append(item)
marker = '\nActual read-only primary sources:\n'
prefix, suffix = previous['assignment'].split(marker, 1)
additional = '''

Further concrete reconstruction: the newly embedded moving-compact truncation proposal targets the controlled original-exhaustion approximants needed for principal-open pole damping. Independently prove it. Start only with an actually already regularizable u_j decreasing to u on the affine Y and u<=g, with g an actual rational FS exhaustion. On Q_r={g<=R_r}, compact decreasing closed-set emptiness yields u_(j_r)<g+1 for large j_r. With C_r negative tending to minus infinity and R_r>2-C_r increasing, glue phi_r=max(u_(j_r)-2g,C_r) on Q_r and C_r outside. Verify the whole winning boundary collar, actual contact Q-PL/model representation, curve nefness, global genuine membership and every scalar. Prove phi_r is decreasing also on the expanding annuli using u_(j_r)-2g<1-g<C_(r-1); a mere diagonal does not imply monotonicity. Uniform rational global FS approximations to each continuous phi_r, plus shifts B_r=2 sum_(i>=r) epsilon_i, give an explicitly decreasing sequence with controlled affine bounds w_r<=2g+sup H_1 after actual generator/floor conversion. No singular EP, metrizability or unbounded-net sequence theorem is an antecedent.

For Y_f and positive rational c, use g_epsilon=max(g,-(c/3)log|f|) as the actual FS exhaustion of Y_f. Controlled approximants satisfy w_i+c log|f|<=max(2g+c log|f|,(c/3)log|f|)+B. Floors D_i tending to minus infinity yield continuous locally corrected contact Q-PL functions on Y, constant on a genuine neighborhood of Z(f). Bound all of them by one affine FS exhaustion h. For each continuous function b<=h, construct genuine global PSH b-2h by moving compact truncations without assuming already regularizability. The global potentials psi_i then decrease; eta_i=max(psi_i,-i) is continuous genuine CPSH because psi_i<=-h forces a whole constant boundary collar. Use uniform FS approximations and summable shifts again to obtain the required affine FS sequence for the final pole-damped function. Verify actual maximum stability and uniform density in the genuine cone, not a proxy operator.

This proposes a noncircular repair of Wu3.25(2)/3.30 rather than citing them as their own proof. Then reconstruct smooth removable extension3.31 using a smooth ample compactification and known smooth EP: the parameter family c_i log|f| is not globally monotone when log|f| changes sign, so use the exact upper-envelope/usc closure theorem with all hypotheses. Keep weak-input trace extension, Runge/singular-stratum induction and singular EP separate until proved. Reconstruct the full original task, not only these new conditional lemmas.
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
assert len(contexts) == 9 and len(m['public_sources']) == 10
C.mkdir(parents=True, exist_ok=False)
write(C / 'input.json', inp)
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r66/P16.1-controlled-affine-Rossi-and-unibranch-equation'
settings['codex']['workspace'] = str(C / 'artifacts')
write(C / 'settings.json', settings)
manifest = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 66,
    'atom': 'P16.1', 'directory': str(C), 'input_sha256': sha(C / 'input.json'),
    'settings_sha256': sha(C / 'settings.json'), 'original_task_unchanged_from_round65': True,
    'public_sources': m['public_sources'], 'embedded_context': contexts, 'notes_imported': [],
    'root_proposals_independently_reviewed': False, 'fully_solved_original_atom': False,
    'round64_and_round65_preserved_unlaunched': True,
    'state': 'PREPARED LOCAL ONLY; no worker launched. Wait for a free native two-item batch slot.'}
write(C / 'input-manifest.json', manifest)
print(json.dumps({'directory': str(C), 'input_sha256': manifest['input_sha256'],
    'settings_sha256': manifest['settings_sha256'], 'bytes': (C / 'input.json').stat().st_size,
    'public_sources': 10, 'context_bodies': 9, 'original_task_unchanged': True,
    'launched': False}, indent=2))
