"""Prepare the actual BE5.16/5.17 exact PL descent shortcut without launching."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

R = Path('/workspace/research')
old = R / 'campaigns/round-67/P16.1-public-source-exact-PL-local-mass-and-unibranch-equation'
C = R / 'campaigns/round-68/P16.1-public-source-BE-exact-PL-local-mass-and-unibranch-equation'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
write = lambda p, d: Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
m = json.loads((old / 'input-manifest.json').read_text())
assert sha(old / 'input.json') == m['input_sha256']
assert sha(old / 'settings.json') == m['settings_sha256']
assert not (old / 'campaign.sqlite').exists()
previous = json.loads((old / 'input.json').read_text())
contexts = list(m['embedded_context'])
p = R / 'root-checks/P16.1-BE-actual-model-difference-and-same-class-descent-shortcut-20261005-continuation74.md'
item = {'kind': 'New unreviewed root simplification: actual BE5.16/5.17 same-class pure FS difference',
    'path': str(p), 'sha256': sha(p), 'accepted_dependency': False}
contexts.append(item)
marker = '\nActual read-only primary sources:\n'
prefix, suffix = previous['assignment'].split(marker, 1)
additional = '''

Simplify the immediately preceding exact-PL route using the actual BE1805.01016v3 passages: Theorem5.14, Proposition5.16(vi) and Lemma5.17 with their whole proofs, literal LF1989--2043. A global formal model function is a model metric on O_XK. On a projective algebraic model, choose any ample model bundle A; rA+B and rA are globally generated after suitable multiples and give an exact pure FS difference. Their common generic class M may be defined only over K. Choose a fixed ample H over k and a large integer a with aH_K-M ample. Adding a pure FS metric tau on aH_K-M to both expressions puts both on the same descending class aH_K and tau cancels. Apply Laurent coefficient/Gauss descent only to the final sections on multiples of aH_K. This proves exact BJ algebraic PL for the Gauss value without needing A's generic class to be a power of H or an equivariance assumption.

This actual-source simplification supersedes the extra ample-generic-class/GM4.12 route in the preceding diagnostic proposal. Do not retain that avoidable proof gate. Verify projective algebraic representation, relative global generation, rational factors, FS addition/product sections, final H0 base change and exact coefficient cutoff. The global PL partition and compact GM2.7 extension remain as previously assigned. All common-local mixed continuity, locality, IBP/mass, comparison, model-atom domination, weak trace, singular Runge, singular EP and original equation obligations remain unchanged. Reconstruct the exact full original task and return candidate=false if any indispensable gate is unresolved.
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
assert len(contexts) == 11 and len(m['public_sources']) == 10
C.mkdir(parents=True, exist_ok=False)
write(C / 'input.json', inp)
settings = json.loads((old / 'settings.json').read_text())
settings['usagePrefix'] = 'catalogue-20261003/r68/P16.1-BE-exact-PL-local-mass-and-unibranch-equation'
settings['codex']['workspace'] = str(C / 'artifacts')
write(C / 'settings.json', settings)
manifest = {'prepared_utc': datetime.now(timezone.utc).isoformat(), 'round': 68,
    'atom': 'P16.1', 'directory': str(C), 'input_sha256': sha(C / 'input.json'),
    'settings_sha256': sha(C / 'settings.json'), 'original_task_unchanged_from_round67': True,
    'public_sources': m['public_sources'], 'embedded_context': contexts, 'notes_imported': [],
    'root_proposals_independently_reviewed': False, 'fully_solved_original_atom': False,
    'round64_through_round67_preserved_unlaunched': True,
    'state': 'PREPARED LOCAL ONLY; no worker launched. Wait for a free native two-item batch slot.'}
write(C / 'input-manifest.json', manifest)
print(json.dumps({'directory': str(C), 'input_sha256': manifest['input_sha256'],
    'settings_sha256': manifest['settings_sha256'], 'bytes': (C / 'input.json').stat().st_size,
    'public_sources': 10, 'context_bodies': 11, 'original_task_unchanged': True,
    'launched': False}, indent=2))
